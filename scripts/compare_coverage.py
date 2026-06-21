#!/usr/bin/env python3
"""对比参考 URL 列表 vs 已采集 URL（按模块分类）
使用项目本地的 source/reference_urls.txt。
"""
import re
from pathlib import Path
from collections import defaultdict

BASE_DIR = Path(__file__).resolve().parent.parent
REF_URLS_FILE = BASE_DIR / "source" / "reference_urls.txt"
RAW_DIR = BASE_DIR / "source" / "raw"

if not REF_URLS_FILE.exists():
    print(f"❌ 未找到 {REF_URLS_FILE}")
    exit(1)

urls_in_docs = set(REF_URLS_FILE.read_text().splitlines())
urls_in_docs.discard("")

collected_urls = {}
for mdir in sorted(RAW_DIR.iterdir()):
    if not mdir.is_dir():
        continue
    for f in sorted(mdir.iterdir()):
        if f.suffix != ".md":
            continue
        text = f.read_text(encoding="utf-8")
        m = re.search(r"^---\s*\n(.*?)\n---", text, re.DOTALL)
        if m:
            url_match = re.search(r"url:\s*(.+)", m.group(1))
            if url_match:
                collected_urls[url_match.group(1).strip()] = f"{mdir.name}/{f.name}"

def norm(u):
    return u.rstrip("/").split("?")[0].split("#")[0]

norm_docs = {norm(u): u for u in urls_in_docs}
norm_coll = {norm(u): u for u in collected_urls}

covered = set(norm_docs) & set(norm_coll)
missing = set(norm_docs) - set(norm_coll)

pct = int(100 * len(covered) / len(norm_docs)) if norm_docs else 0
print(f"Reference URLs: {len(norm_docs)}")
print(f"Collected:      {len(norm_coll)}")
print(f"Covered:        {len(covered)} ({pct}%)")
print(f"Missing:        {len(missing)}")

def get_cat(u):
    m2 = re.search(r"/latest/([^/]+)", u)
    return m2.group(1) if m2 else "root"

missing_by_cat = defaultdict(list)
for k in sorted(norm_docs):
    if k not in norm_coll:
        cat = get_cat(norm_docs[k])
        page = norm_docs[k].split("/")[-1].replace(".html", "").replace("_", " ")
        missing_by_cat[cat].append(page)

print("\n" + "=" * 60)
print(f"未采集页面按模块分类 ({len(missing)} 页)")
print("=" * 60)
for cat in sorted(missing_by_cat):
    pages = missing_by_cat[cat]
    print(f"\n  [{cat}] {len(pages)} pages")
    for p in pages:
        print(f"    - {p}")

covered_by_cat = defaultdict(list)
for k in sorted(norm_docs):
    if k in norm_coll:
        cat = get_cat(norm_docs[k])
        page = norm_docs[k].split("/")[-1].replace(".html", "").replace("_", " ")
        covered_by_cat[cat].append(page)

print("\n" + "=" * 60)
print(f"已采集页面 ({len(covered)} 页)")
print("=" * 60)
for cat in sorted(covered_by_cat):
    pages = covered_by_cat[cat]
    print(f"\n  [{cat}] {len(pages)} pages")
    for p in pages:
        print(f"    + {p}")
