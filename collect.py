#!/usr/bin/env python3
"""
Isaac Sim SDG 文档采集与组装 Pipeline

用法:
  uv run python collect.py                     # 全量采集 + 组装
  uv run python collect.py --incremental       # 增量更新（只抓 checksum 变化的）
  uv run python collect.py --module 01-replicator-core  # 只处理指定模块
  uv run python collect.py --assemble-only     # 跳过采集，只组装已有 raw
  uv run python collect.py --dry-run           # 试运行

前置条件:
  uv sync
  网络代理: export https_proxy=http://127.0.0.1:10808 http_proxy=http://127.0.0.1:10808
"""

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urljoin

# ── 配置 ──────────────────────────────────────────────────────────────────────

BASE_DIR = Path(__file__).parent
MANIFESTS_DIR = BASE_DIR / "manifests"
RAW_DIR = BASE_DIR / "source" / "raw"
CACHE_DIR = BASE_DIR / "source" / "cache"
OUTPUT_DIR = BASE_DIR / "output"
LOGS_DIR = BASE_DIR / "logs"

CACHE_FILE = CACHE_DIR / ".collect_cache.json"
PROXY = os.environ.get("https_proxy", os.environ.get("HTTP_PROXY", ""))
MAX_WORKERS = 8  # 并发数
FETCH_TIMEOUT = 30  # 秒

# Isaac Sim 文档特征选择器（Sphinx RTD 主题）
CONTENT_SELECTORS = [
    "article[role='main']",
    "div.wyrm-content",
    "div.rst-content",
    "main",
    "article",
]

# 需要移除的元素选择器（侧栏导航、页脚等）
REMOVE_SELECTORS = [
    "nav.wy-nav-side",
    "div.wy-nav-side",
    "footer",
    "section#footer",
    "div[role='navigation']",
    "div.sphinxsidebar",
    "a.headerlink",
    "div.admonition.note:has(p:contains('This page was generated'))",
]


# ── 工具函数 ──────────────────────────────────────────────────────────────────

def url_to_filepath(url: str) -> str:
    """将 URL 转为安全的文件路径 slug"""
    # 去掉域名和 scheme
    path = url.split("/")[-1] if "/" in url else url
    path = path.replace(".html", "").replace(".htm", "")
    # 清理不安全字符
    path = re.sub(r"[^a-zA-Z0-9_\-.]", "_", path)
    return path


def compute_checksum(text: str) -> str:
    """计算文本内容的 SHA256"""
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]


def load_cache() -> dict:
    """加载采集缓存"""
    if CACHE_FILE.exists():
        return json.loads(CACHE_FILE.read_text())
    return {"pages": {}, "last_run": None}


def save_cache(cache: dict):
    """保存采集缓存"""
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    cache["last_run"] = datetime.now(timezone.utc).isoformat()
    CACHE_FILE.write_text(json.dumps(cache, indent=2, ensure_ascii=False))


def load_manifests(module_filter: str | None = None) -> list[dict]:
    """加载所有模块 manifest"""
    manifests = []
    for f in sorted(MANIFESTS_DIR.glob("*.json")):
        m = json.loads(f.read_text())
        if module_filter and f.stem != module_filter:
            continue
        # 补全 URL
        base = m.get("base_url", "https://docs.isaacsim.omniverse.nvidia.com/latest")
        for page in m.get("pages", []):
            if page["url"].startswith("/"):
                page["full_url"] = base.rstrip("/") + page["url"]
            else:
                page["full_url"] = page["url"]
        manifests.append(m)
    return manifests


def get_session():
    """创建 requests session，配置代理"""
    from requests import Session
    from requests.adapters import HTTPAdapter
    from urllib3.util.retry import Retry

    s = Session()
    s.headers.update({
        "User-Agent": "IsaacSimDocCollector/1.0 (research bot)",
        "Accept": "text/html,application/xhtml+xml",
    })

    # 重试策略
    retry = Retry(total=3, backoff_factor=1.0, status_forcelist=[429, 500, 502, 503, 504])
    adapter = HTTPAdapter(max_retries=retry, pool_connections=MAX_WORKERS, pool_maxsize=MAX_WORKERS)
    s.mount("https://", adapter)
    s.mount("http://", adapter)

    # 代理
    if PROXY:
        s.proxies = {"http": PROXY, "https": PROXY}

    return s


# ── 页面提取 ──────────────────────────────────────────────────────────────────

def extract_markdown_defuddle(html: str) -> str:
    """使用 defuddle CLI 提取正文 Markdown"""
    try:
        result = subprocess.run(
            ["defuddle", "parse", "--format", "markdown"],
            input=html, capture_output=True, text=True, timeout=60,
        )
        if result.returncode == 0 and result.stdout.strip():
            return result.stdout.strip()
    except (subprocess.TimeoutExpired, FileNotFoundError):
        pass
    return ""


def extract_markdown_bs4(html: str) -> str:
    """BeautifulSoup 回退方案"""
    try:
        from bs4 import BeautifulSoup
        from markdownify import markdownify as md

        soup = BeautifulSoup(html, "html.parser")

        # 移除不需要的元素
        for sel in REMOVE_SELECTORS:
            for el in soup.select(sel):
                el.decompose()

        # 找主内容区
        content = None
        for sel in CONTENT_SELECTORS:
            content = soup.select_one(sel)
            if content:
                break

        if not content:
            content = soup.find("body")
        if not content:
            return ""

        # 转 markdown
        text = md(str(content), heading_style="ATX", code_language="python",
                  strip=["img", "script", "style"])

        # 清理
        text = re.sub(r"\n{3,}", "\n\n", text)
        text = re.sub(r"\[.*?\]\(.*?\)\n\n\[.*?\]\(.*?\)", "", text)  # 连续空链接
        return text.strip()
    except Exception as e:
        print(f"  ⚠ bs4 提取失败: {e}")
        return ""


def fetch_and_extract(url: str, module_name: str, session=None) -> dict:
    """抓取单个页面并提取 Markdown"""
    from requests import Session as _S
    s = session or get_session()

    try:
        resp = s.get(url, timeout=FETCH_TIMEOUT)
        resp.raise_for_status()
        html = resp.text
    except Exception as e:
        return {"url": url, "error": f"HTTP {e}", "content": "", "checksum": ""}

    # 先用 defuddle，失败回退 bs4
    md_content = extract_markdown_defuddle(html)
    if not md_content or len(md_content) < 100:
        md_content = extract_markdown_bs4(html)

    checksum = compute_checksum(md_content) if md_content else ""
    return {"url": url, "error": None, "content": md_content, "checksum": checksum}


# ── 采集阶段 ──────────────────────────────────────────────────────────────────

def collect_module(manifest: dict, cache: dict, incremental: bool = False,
                   dry_run: bool = False) -> dict:
    """采集一个模块的所有页面"""
    module_name = manifest["module"]
    pages = manifest.get("pages", [])
    module_dir = RAW_DIR / module_name
    module_dir.mkdir(parents=True, exist_ok=True)

    print(f"\n{'='*60}")
    print(f"模块: {manifest['title']} ({len(pages)} 页)")
    print(f"{'='*60}")

    results = {"total": len(pages), "fetched": 0, "skipped": 0, "errors": 0}

    # 确定需要抓取的页面
    to_fetch = []
    for page in pages:
        url = page["full_url"]
        slug = url_to_filepath(url)
        raw_path = module_dir / f"{slug}.md"
        cache_key = url

        if incremental and cache_key in cache["pages"]:
            old_checksum = cache["pages"][cache_key].get("checksum", "")
            if old_checksum and raw_path.exists():
                results["skipped"] += 1
                print(f"  ⏭️  跳过 (缓存命中): {page['title']}")
                continue

        if dry_run:
            print(f"  🔍 [dry-run] 将抓取: {page['title']}")
            continue

        to_fetch.append((page, slug, raw_path, cache_key))

    if dry_run:
        return results

    # 并发抓取
    session = get_session()

    def _fetch_worker(item):
        page, slug, raw_path, cache_key = item
        return page, raw_path, cache_key, fetch_and_extract(page["full_url"], module_name, session)

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = {executor.submit(_fetch_worker, item): item for item in to_fetch}
        for future in as_completed(futures):
            page, raw_path, cache_key, result = future.result()

            if result["error"]:
                print(f"  ❌ 失败: {page['title']} — {result['error']}")
                results["errors"] += 1
                continue

            content = result["content"]
            if not content:
                print(f"  ⚠  空内容: {page['title']}")
                results["errors"] += 1
                continue

            # 写 raw 文件（带 frontmatter）
            frontmatter = (
                f"---\n"
                f"url: {page['full_url']}\n"
                f"title: \"{page['title']}\"\n"
                f"section: \"{page.get('section', '')}\"\n"
                f"module: \"{module_name}\"\n"
                f"checksum: \"{result['checksum']}\"\n"
                f"fetched: \"{datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%S')}\"\n"
                f"---\n\n"
            )

            raw_path.write_text(frontmatter + content, encoding="utf-8")

            # 更新缓存
            cache["pages"][cache_key] = {
                "checksum": result["checksum"],
                "title": page["title"],
                "module": module_name,
                "raw_path": str(raw_path.relative_to(BASE_DIR)),
            }

            results["fetched"] += 1
            print(f"  ✅ {page['title']} ({len(content)} chars)")

    print(f"\n  结果: {results['fetched']} 新抓 / {results['skipped']} 跳过 / {results['errors']} 错误")
    return results


# ── 组装阶段 ──────────────────────────────────────────────────────────────────

def parse_frontmatter(path: Path) -> tuple[dict, str]:
    """解析带 frontmatter 的 md 文件"""
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return {}, text

    end = text.find("---", 3)
    if end == -1:
        return {}, text

    meta_str = text[3:end].strip()
    body = text[end + 3:].strip()

    meta = {}
    for line in meta_str.split("\n"):
        if ":" in line:
            key, val = line.split(":", 1)
            meta[key.strip()] = val.strip().strip('"')

    return meta, body


def assemble_module(manifest: dict) -> Path:
    """从 raw 文件组装一个模块文档"""
    module_name = manifest["module"]
    module_dir = RAW_DIR / module_name
    output_path = BASE_DIR / manifest["output"]

    pages = manifest.get("pages", [])
    sections = {}  # section -> [(title, content)]

    for page in pages:
        slug = url_to_filepath(page["full_url"])
        raw_path = module_dir / f"{slug}.md"

        if not raw_path.exists():
            print(f"  ⚠  缺少 raw: {raw_path.name}")
            continue

        meta, body = parse_frontmatter(raw_path)
        section = meta.get("section", page.get("section", "其他"))
        title = meta.get("title", page["title"])

        sections.setdefault(section, []).append((title, body, page["full_url"]))

    # 组装输出
    assembled_time = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    header = (
        f"# {manifest['title']}\n\n"
        f"> {manifest.get('description', '')}\n"
        f"> Isaac Sim 版本: {manifest.get('isaac_version', '6.0')}\n"
        f"> 最后组装: {assembled_time}\n"
        f"> 来源页数: {len(pages)}\n\n"
        f"---\n\n"
    )

    # 来源链接表
    header += "## 来源链接\n\n"
    for page in pages:
        header += f"- [{page['title']}]({page['full_url']})\n"
    header += "\n---\n\n"

    # 按 section 分组输出
    content_parts = [header]
    for section_name, items in sections.items():
        content_parts.append(f"\n## {section_name}\n\n")
        for title, body, url in items:
            content_parts.append(f"### {title}\n\n")
            content_parts.append(f"> 来源: {url}\n\n")
            content_parts.append(body)
            content_parts.append(f"\n\n---\n\n")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("".join(content_parts), encoding="utf-8")

    page_count = sum(len(v) for v in sections.values())
    print(f"  📦 组装完成: {output_path.name} ({page_count}/{len(pages)} 页, {output_path.stat().st_size:,} bytes)")
    return output_path


# ── 索引生成 ──────────────────────────────────────────────────────────────────

def generate_index(manifests: list[dict]):
    """生成 00_SDG_概览与索引.md"""
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    total_pages = sum(len(m.get("pages", [])) for m in manifests)

    content = f"""# Isaac Sim SDG 专题文档 — 索引

> SimReady + Replicator + Domain Randomization 完整参考
> Isaac Sim 版本: 6.0
> 最后更新: {now}
> 总页数: {total_pages}

---

## 四大能力覆盖

| 能力 | 对应模块 | 页数 |
|------|---------|------|
| Replicator 引擎 | 01 + 04 | {sum(len(m.get('pages',[])) for m in manifests if m['module'] in ['01-replicator-core','04-domain-randomization'])} |
| SDG 工作流 | 02 + 07 | {sum(len(m.get('pages',[])) for m in manifests if m['module'] in ['02-sdg-workflows','07-sdg-pipeline'])} |
| Replicator Agent | 03 | {sum(len(m.get('pages',[])) for m in manifests if m['module'] == '03-replicator-agent')} |
| 传感器 + 资产 | 05 + 06 | {sum(len(m.get('pages',[])) for m in manifests if m['module'] in ['05-sensors-annotators','06-simready-assets'])} |

---

## 模块总览

"""
    for m in manifests:
        page_count = len(m.get("pages", []))
        output_file = Path(m["output"]).name
        content += f"### {output_file}\n"
        content += f"**{m['title']}** — {m.get('description', '')} ({page_count} 页)\n\n"
        for p in m.get("pages", []):
            content += f"- [{p['title']}]({p['full_url']})\n"
        content += "\n"

    content += f"""
---

## 文件清单

```
Isaac_Sim_SDG_Component/
├── collect.py              ← 采集 + 组装脚本
├── pyproject.toml
├── manifests/              ← URL 清单（编辑这里来增减页面）
"""
    for m in manifests:
        content += f"│   ├── {Path(MANIFESTS_DIR / (m['module'] + '.json')).name}\n"
    content += f"""├── source/raw/             ← 单页原始提取（git tracked）
├── output/                 ← 组装后模块文档（git tracked）
"""
    for m in manifests:
        content += f"│   ├── {Path(m['output']).name}\n"
    content += """└── source/cache/           ← 采集缓存（.gitignore）
```

---

## 与 Development_Component 的关系

本 SDG 专题与 `~/Desktop/Isaac_Sim_Development_Component/` 互补：
- Development_Component 覆盖：开发工具、Python 脚本、OmniGraph、Core API 教程
- SDG_Component 覆盖：Replicator、Domain Randomization、SDG Pipeline、SimReady 资产

开发基础（API 导入、SimulationApp、DOF 控制、OmniGraph Python Scripting）请参考 Development_Component 的 02/03/05。
"""

    idx_path = OUTPUT_DIR / "00_SDG_概览与索引.md"
    idx_path.write_text(content, encoding="utf-8")
    print(f"\n  📋 索引生成: {idx_path.name}")


# ── 主流程 ────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Isaac Sim SDG 文档采集 Pipeline")
    parser.add_argument("--incremental", action="store_true", help="增量更新（只抓 checksum 变化的）")
    parser.add_argument("--module", type=str, help="只处理指定模块")
    parser.add_argument("--dry-run", action="store_true", help="试运行，不执行采集")
    parser.add_argument("--assemble-only", action="store_true", help="跳过采集，只组装")
    args = parser.parse_args()

    manifests = load_manifests(args.module)
    if not manifests:
        print("❌ 未找到匹配的 manifest 文件")
        sys.exit(1)

    total_pages = sum(len(m.get("pages", [])) for m in manifests)
    print(f"Isaac Sim SDG 文档 Pipeline")
    print(f"模块数: {len(manifests)}, 总页数: {total_pages}")
    print(f"模式: {'增量' if args.incremental else '全量'} | {'dry-run' if args.dry_run else '生产'}")
    if PROXY:
        print(f"代理: {PROXY}")
    print()

    # 加载缓存
    cache = load_cache()

    # 采集阶段
    if not args.assemble_only:
        total_results = {"fetched": 0, "skipped": 0, "errors": 0}
        start_time = time.time()

        for manifest in manifests:
            results = collect_module(manifest, cache, args.incremental, args.dry_run)
            for k in total_results:
                total_results[k] += results.get(k, 0)

        elapsed = time.time() - start_time
        save_cache(cache)

        print(f"\n{'='*60}")
        print(f"采集完成 ({elapsed:.1f}s)")
        print(f"  新增: {total_results['fetched']}")
        print(f"  跳过: {total_results['skipped']}")
        print(f"  错误: {total_results['errors']}")
        print(f"{'='*60}")

        if args.dry_run:
            print("\n[dry-run 模式，未写入文件]")
            return

    # 组装阶段
    print(f"\n组装模块文档...")
    for manifest in manifests:
        assemble_module(manifest)

    # 生成索引
    generate_index(load_manifests())

    print(f"\n✅ Pipeline 完成!")
    print(f"   输出目录: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
