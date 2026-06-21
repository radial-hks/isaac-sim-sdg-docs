# Isaac Sim SDG Docs Project Workflow

本文档定义了整个文档工程的完整生命周期，包括采集、组装、消费、迭代的全流程。

## 1. 项目概述

**目标**: 为 Isaac Sim 6.0 SDG (Synthetic Data Generation) 开发提供离线、可迭代、Agent-friendly 的文档集合。

**覆盖范围**:
- Isaac Sim 核心概念与架构 (139 pages)
- Python 脚本开发与 OmniGraph (32 pages)
- Extension 开发与部署 (8 pages)
- Replicator + Domain Randomization (29 pages)
- 传感器与标注器 (24 pages)
- 机器人配置与仿真 (45 pages)
- 进阶：机械臂运动 + 传感器 + USD 调优 (44 pages)

**当前覆盖率**: 58% (225/385 pages, 未采集的 160 页主要是 ROS2/Legal/Migration 等明确排除模块)

## 2. 数据流

```
manifests/*.json (URL 清单)
    ↓ collect.py (并发抓取 + defuddle 提取)
source/raw/{module}/{page}.md (单页 Markdown + YAML frontmatter)
    ↓ collect.py (按 manifest 顺序组装)
output/{NN}_Title.md (模块级聚合文档)
    ↓ 人类/Agent 消费
Isaac Sim SDG 开发与学习
```

### 2.1 manifest → raw

每个 manifest 定义一个逻辑模块：
```json
{
  "module": "11-replicator-core",
  "title": "Replicator Core",
  "description": "...",
  "output": "output/11_Replicator_Core.md",
  "isaac_version": "6.0",
  "pages": [
    {"url": "/replicator_tutorials/index.html", "title": "Index", "section": "概述"},
    ...
  ]
}
```

采集后，每个 page 生成一个 raw 文件：
```markdown
---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/replicator_tutorials/index.html
title: Index
module: 11-replicator-core
section: 概述
fetch_date: 2026-06-22T10:30:00+08:00
checksum: a3f7c9e2b1d4e6f8
status: success
---

# Replicator Tutorials
...
```

**frontmatter 字段说明**:
- `url`: 源 URL (用于覆盖检测和去重)
- `title`: 页面标题
- `module`: 所属 manifest
- `section`: 在输出文档中的章节位置
- `fetch_date`: ISO 8601 时间戳
- `checksum`: MD5(content) 用于增量更新判断
- `status`: success/failed/partial

### 2.2 raw → output

`collect.py --assemble` 阶段按 manifest 顺序读取 raw 文件，按 `section` 字段分组，写入对应的 output 文件：

```markdown
# Replicator Core

> Isaac Sim 6.0 · 17 pages · Last updated: 2026-06-22

## 目录
- [概述](#概述)
  - Index
- [基础教程](#基础教程)
  - Replicator Overview
  - Getting Started
  - ...

---

## 概述

### Index (0 pages)
_This page is an index page with minimal content._
_Source: https://docs.isaacsim.omniverse.nvidia.com/latest/replicator_tutorials/index.html_

---

## 基础教程

### Replicator Overview
> Source: https://docs.isaacsim.omniverse.nvidia.com/latest/replicator_tutorials/tutorial_replicator_overview.html
> Fetched: 2026-06-22T10:30:00+08:00

[Extracted content here...]

---
```

## 3. 迭代策略

### 3.1 全量采集 (首次或大版本变更)

```bash
# 删除缓存，重新抓取所有页面
rm -rf source/cache
uv run python collect.py
```

**触发条件**:
- 项目首次初始化
- Isaac Sim 大版本升级 (5.0 → 6.0)
- defuddle 提取模板重大更新
- 怀疑缓存数据损坏

**耗时**: ~3-5 分钟 (229 pages)

### 3.2 增量更新 (定期刷新)

```bash
# 只抓取 checksum 变化或新增的页面
uv run python collect.py --incremental
```

**工作原理**:
1. 读取 `source/cache/checksums.json` (URL → checksum 映射)
2. 对每个 manifest 中的 page，先 HEAD 请求获取 Last-Modified
3. 如果 Last-Modified 未变 → 跳过
4. 如果 Last-Modified 变化或无此 header → GET 全文，计算 checksum
5. checksum 与缓存比对，变化则重新提取

**触发条件**:
- 每周定期更新 (建议 cron job)
- Isaac Sim 文档站有小版本更新
- 用户报告某页面内容过时

**耗时**: ~30 秒 (无变化) 到 3 分钟 (大量变化)

### 3.3 模块级更新 (针对性补充)

```bash
# 只更新指定模块
uv run python collect.py --module 11-replicator-core --incremental

# 只更新指定模块，全量抓取
uv run python collect.py --module 11-replicator-core
```

**触发条件**:
- 新增功能需要补充特定主题
- 某模块发现有缺漏页面
- 调试特定模块的提取质量问题

### 3.4 选择性重抓取 (质量修复)

```bash
# 删除特定页面的缓存，强制重新抓取
rm source/raw/11-replicator-core/tutorial_replicator_overview.md
rm source/cache/checksums.json  # 或编辑 JSON 删除对应 key
uv run python collect.py --module 11-replicator-core --incremental
```

**触发条件**:
- defuddle 提取质量差，需要重新尝试
- 页面内容被截断
- 手动编辑 raw 后想恢复原版

### 3.5 只组装不采集 (快速迭代输出格式)

```bash
# 不访问网络，只重新组装 output
uv run python collect.py --assemble-only
```

**触发条件**:
- 调整了组装模板 (section 分组逻辑)
- 修改了 manifest 的 section 分配
- 调试输出格式

**耗时**: < 1 秒

## 4. Manifest 维护

### 4.1 新增模块

```bash
# 1. 创建 manifest
cat > manifests/20-new-topic.json <<'EOF'
{
  "module": "20-new-topic",
  "title": "New Topic Name",
  "description": "Brief description",
  "output": "output/20_New_Topic.md",
  "isaac_version": "6.0",
  "pages": [
    {"url": "/path/page1.html", "title": "Page 1", "section": "Section A"},
    {"url": "/path/page2.html", "title": "Page 2", "section": "Section A"},
    {"url": "/path/page3.html", "title": "Page 3", "section": "Section B"}
  ]
}
EOF

# 2. 采集
uv run python collect.py --module 20-new-topic

# 3. 更新 00_学习路径 和 README
```

**命名约定**:
- 模块编号: `NN-topic-name` (NN 为 2 位数字 + 连字符主题名)
- 00-09: 基础与通用
- 10-19: 核心开发
- 20-29: 进阶专题
- 30-39: 实验性/探索性

### 4.2 增加页面

编辑对应 manifest 的 `pages` 数组：
```json
{"url": "/new/page.html", "title": "New Page Title", "section": "Target Section"}
```

**注意**:
- `url` 必须是相对路径 (以 `/` 开头)
- `title` 用于输出文档的 H2 标题
- `section` 用于输出文档的 H1 分组

### 4.3 重组 Sections

修改 manifest 中页面的 `section` 字段，然后重新组装：
```bash
uv run python collect.py --assemble-only
```

无需重新采集网络内容。

### 4.4 废弃页面

从 manifest 的 `pages` 数组中移除，可选择性删除 raw 文件：
```bash
# 删除 manifest 中的条目
vim manifests/11-replicator-core.json

# 删除 raw 文件 (可选，但建议保留以备恢复)
git rm source/raw/11-replicator-core/old-page.md

# 重新组装
uv run python collect.py --assemble-only

# 提交
git add -A
git commit -m "chore: remove obsolete page from module 11"
```

## 5. Agent 集成模式

### 5.1 Hermes Skill 模式 (推荐)

将 Isaac Sim docs 包装为 Hermes skill，按需加载到 Agent 上下文：

```bash
# 创建 skill
mkdir -p ~/.hermes/skills/isaac-sim-sdg
cd ~/.hermes/skills/isaac-sim-sdg

# SKILL.md 定义何时加载
cat > SKILL.md <<'EOF'
---
name: isaac-sim-sdg
description: Isaac Sim 6.0 合成数据生成开发知识库
version: 1.0.0
triggers:
  - isaac sim
  - replicator
  - domain randomization
  - synthetic data generation
  - SDG
  - omnigraph
  - simready assets
---

# Isaac Sim SDG Docs

当用户查询 Isaac Sim、Replicator、Omniverse USD、Domain Randomization、SDG 相关的开发问题时加载此 skill。

## 文档位置

- 概念与架构: ~/Desktop/isaac-sim-sdg-docs/output/01_*.md
- 开发基础: ~/Desktop/isaac-sim-sdg-docs/output/02_*.md
- Extension 开发: ~/Desktop/isaac-sim-sdg-docs/output/03_*.md
- Headless & 部署: ~/Desktop/isaac-sim-sdg-docs/output/04_*.md
- Python API 速查: ~/Desktop/isaac-sim-sdg-docs/output/05_*.md
- Sim2Real & UE5 对照: ~/Desktop/isaac-sim-sdg-docs/output/06_*.md
- 机器人配置: ~/Desktop/isaac-sim-sdg-docs/output/07_*.md
- OmniGraph & 机器人仿真: ~/Desktop/isaac-sim-sdg-docs/output/08_*.md
- 进阶专题 (机械臂/传感器/USD): ~/Desktop/isaac-sim-sdg-docs/output/09_*.md
- Replicator 核心: ~/Desktop/isaac-sim-sdg-docs/output/11_*.md
- SDG 工作流: ~/Desktop/isaac-sim-sdg-docs/output/12_*.md
- Replicator Agent: ~/Desktop/isaac-sim-sdg-docs/output/13_*.md
- Domain Randomization: ~/Desktop/isaac-sim-sdg-docs/output/14_*.md
- 传感器与标注器: ~/Desktop/isaac-sim-sdg-docs/output/15_*.md
- SimReady 资产: ~/Desktop/isaac-sim-sdg-docs/output/16_*.md
- SDG Pipeline: ~/Desktop/isaac-sim-sdg-docs/output/17_*.md

## 使用指南

1. 优先查找与用户问题最匹配的模块文档
2. 如果涉及多个模块，按依赖顺序读取 (概念 → 开发 → 具体主题)
3. 00_学习路径 提供了从基础到高阶的阅读顺序
4. 对于 API 签名查询，直接读 05_Python_API_Quickref
```

### 5.2 MCP Server 模式 (语义搜索)

使用 MCP (Model Context Protocol) 将文档暴露为可搜索的知识库：

```python
# ~/.hermes/mcp_servers/isaac_sim_docs.py
from mcp.server import Server
from mcp.types import Tool, TextContent
import os, re
from pathlib import Path

DOCS_DIR = Path.home() / "Desktop" / "isaac-sim-sdg-docs" / "output"

server = Server("isaac-sim-docs")

@server.list_tools()
async def list_tools():
    return [
        Tool(
            name="search_docs",
            description="Search Isaac Sim SDG documentation by keyword",
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "Search query"}
                },
                "required": ["query"]
            }
        ),
        Tool(
            name="read_module",
            description="Read a specific module document",
            inputSchema={
                "type": "object",
                "properties": {
                    "module_id": {"type": "string", "description": "e.g., '11' for 11_Replicator_Core"}
                },
                "required": ["module_id"]
            }
        )
    ]

@server.call_tool()
async def call_tool(name: str, arguments: dict):
    if name == "search_docs":
        query = arguments["query"].lower()
        results = []
        for doc_file in DOCS_DIR.glob("*.md"):
            content = doc_file.read_text(encoding="utf-8")
            if query in content.lower():
                # Extract module title from first H1
                match = re.search(r"^# (.+)", content, re.MULTILINE)
                title = match.group(1) if match else doc_file.stem
                results.append(f"- {title} ({doc_file.name})")
        return [TextContent(type="text", text="\n".join(results[:10]))]
    
    elif name == "read_module":
        module_id = arguments["module_id"]
        matches = list(DOCS_DIR.glob(f"{module_id}_*.md"))
        if not matches:
            return [TextContent(type="text", text=f"Module {module_id} not found")]
        content = matches[0].read_text(encoding="utf-8")
        # Truncate to first 8000 chars to avoid context overflow
        return [TextContent(type="text", text=content[:8000] + "\n\n[...truncated...]")]

if __name__ == "__main__":
    import asyncio
    asyncio.run(server.run())
```

**配置 ~/.hermes/mcp_servers.yaml**:
```yaml
servers:
  - name: isaac-sim-docs
    command: python3
    args: ["~/.hermes/mcp_servers/isaac_sim_docs.py"]
```

### 5.3 LangGraph RAG 模式 (向量检索)

对于大规模语义搜索，可以将文档向量化后存入 ChromaDB/FAISS：

```python
# 离线索引脚本
from pathlib import Path
import chromadb
from sentence_transformers import SentenceTransformer

DOCS_DIR = Path.home() / "Desktop" / "isaac-sim-sdg-docs" / "output"
client = chromadb.PersistentClient(path="~/.hermes/chroma/isaac_sim_docs")
collection = client.get_or_create_collection("isaac_sim_sdg")
model = SentenceTransformer("all-MiniLM-L6-v2")

# 按 section 分块
for doc_file in DOCS_DIR.glob("*.md"):
    content = doc_file.read_text(encoding="utf-8")
    module_name = doc_file.stem
    
    # 简单的按 H2 分块
    sections = re.split(r"^## ", content, flags=re.MULTILINE)
    for i, section in enumerate(sections):
        if len(section.strip()) < 100:
            continue
        chunk_id = f"{module_name}_section_{i}"
        embedding = model.encode(section).tolist()
        collection.add(
            ids=[chunk_id],
            embeddings=[embedding],
            documents=[section],
            metadatas=[{"module": module_name, "section_index": i}]
        )

print(f"Indexed {collection.count()} chunks")
```

**LangGraph 工具封装**:
```python
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

vectorstore = Chroma(
    persist_directory="~/.hermes/chroma/isaac_sim_docs",
    embedding_function=HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2"),
    collection_name="isaac_sim_sdg"
)

def search_sim(query: str, k: int = 5) -> str:
    docs = vectorstore.similarity_search(query, k=k)
    return "\n\n---\n\n".join([doc.page_content for doc in docs])
```

### 5.4 直接文件访问模式 (最简单)

Agent 可以直接读取 output 文件：

```python
# Agent 工具调用
tool_call("read_file", {"path": "~/Desktop/isaac-sim-sdg-docs/output/11_Replicator_Core.md"})

# 或读取特定 section
tool_call("grep_file", {
    "path": "~/Desktop/isaac-sim-sdg-docs/output/14_Domain_Randomization.md",
    "pattern": "def randomize_pose"
})
```

**优势**: 零配置，所有 Agent 框架都支持
**劣势**: 需要 Agent 自己判断读哪个文件，缺乏语义搜索

## 6. 人类消费

### 6.1 学习路径

`output/00_统一学习路径.md` 提供了从基础到高阶的阅读顺序：

1. **Phase 1: 概念与基础** (Week 1-2)
   - 01_Concepts_and_Architecture
   - 02_Development_Fundamentals

2. **Phase 2: 核心开发** (Week 3-4)
   - 03_Extension_Development
   - 08_OmniGraph_and_Robot_Sim
   - 05_Python_API_Quickref (作为参考手册)

3. **Phase 3: 机器人配置** (Week 5-6)
   - 07_Robot_Setup
   - 06_Sim2Real_and_UE5 (如果有 UE 背景)

4. **Phase 4: SDG 专项** (Week 7-8)
   - 11_Replicator_Core
   - 14_Domain_Randomization
   - 15_Sensors_and_Annotators

5. **Phase 5: 生产流水线** (Week 9-10)
   - 04_Headless_and_Deploy
   - 12_SDG_Workflows
   - 13_Replicator_Agent
   - 17_SDG_Pipeline

6. **Phase 6: 进阶专题** (按需)
   - 09_Manipulators_Sensors_USDTuning
   - 16_SimReady_Assets

### 6.2 交叉引用

output 文件中包含源 URL，可以跳转回在线文档：
```markdown
> Source: https://docs.isaacsim.omniverse.nvidia.com/latest/replicator_tutorials/tutorial_replicator_overview.html
```

如果离线文档不够详细或版本过旧，可以访问在线版本获取最新内容。

### 6.3 搜索与导航

```bash
# 在所有模块中搜索关键词
grep -r "ReplicatorAgent" output/*.md

# 查看某模块的目录结构
grep "^## " output/11_Replicator_Core.md

# 统计模块页面数
grep -c "^### " output/11_Replicator_Core.md
```

## 7. 版本管理

### 7.1 Commit 策略

```bash
# 采集新内容
git add -A
git commit -m "collect: add 15 pages on robotics control"

# 只调整组装格式
git add -A
git commit -m "assemble: reorganize sections in module 11"

# 修复提取质量
git add -A
git commit -m "fix: improve defuddle extraction for code blocks"

# 更新 manifest
git add -A
git commit -m "manifest: add sensor calibration pages to module 15"
```

**Commit message 前缀约定**:
- `collect:` 新增或更新采集内容
- `assemble:` 调整组装逻辑
- `manifest:` 修改 manifest 配置
- `fix:` 修复提取质量或脚本 bug
- `docs:` 更新文档 (README/WORKFLOW/LEARNING_PATH)
- `chore:` 清理工作 (删除旧文件、格式化等)

### 7.2 Tag 策略

按周快照打 tag：
```bash
# 每周日自动打 tag
git tag -a v2026-W26 -m "Weekly snapshot: 225 pages, 58% coverage"
git push --tags
```

**Tag 命名**: `v{YEAR}-W{WEEK_NUM}`

### 7.3 Coverage 追踪

`scripts/check_coverage.py` 输出当前覆盖率，可以记录到 CHANGELOG：

```markdown
## [2026-W26] - 2026-06-22

### Added
- 89 pages across 3 modules (07, 08, 09)
- Coverage: 36% → 58%

### Changed
- Reorganized module 00 into 01-06
- Updated learning path

### Fixed
- Fixed 1 broken URL (manipulators/index.html → concepts/index.html)
```

## 8. 质量控制

### 8.1 Checksum 验证

每个 raw 文件的 frontmatter 包含 `checksum` 字段（MD5 of content），用于：
- 增量更新判断 (checksum 变化才重新提取)
- 检测页面是否有实质内容变化
- 防止重复抓取未变化的页面

### 8.2 空内容检测

`collect.py` 会自动跳过内容过短的页面 (< 100 bytes)，常见原因：
- 页面是纯索引页 (只有链接列表)
- 页面是空壳 (只有标题和"Coming soon")
- defuddle 提取失败

**处理**: 在 manifest 中标记为 `"skip": true` 或 `"note": "Index page"`

### 8.3 404 处理

如果页面返回 404：
1. 检查 URL 是否拼写错误
2. 检查 Isaac Sim 文档站是否有重定向 (旧版本 URL)
3. 如果页面确实已删除，从 manifest 中移除

**示例修复**:
```bash
# 查找 404 页面
grep "status: failed" source/raw/**/*.md

# 修复 URL
vim manifests/09-advanced-optionals.json

# 重新抓取
uv run python collect.py --module 09-advanced-optionals
```

### 8.4 内容新鲜度

每周运行一次覆盖率检查：
```bash
python3 scripts/check_coverage.py
```

如果发现覆盖率下降 (Isaac Sim 文档站新增页面)，考虑是否需要补充到 manifest。

## 9. 故障恢复

### 9.1 网络错误

**症状**: `collect.py` 报 connection timeout 或 connection refused

**解决**:
```bash
# 1. 检查代理
echo $http_proxy $https_proxy

# 2. 测试连通性
curl -x $http_proxy -I https://docs.isaacsim.omniverse.nvidia.com/

# 3. 增加重试次数
vim collect.py  # 修改 MAX_RETRIES = 5

# 4. 继续采集 (已抓取的会跳过)
uv run python collect.py --incremental
```

### 9.2 部分采集失败

**症状**: 采集到一半中断，部分 raw 文件不完整

**解决**:
```bash
# 1. 检查缓存状态
cat source/cache/checksums.json | python3 -m json.tool | grep -c '"'

# 2. 删除可疑页面的缓存
rm source/raw/11-replicator-core/tutorial_*.md
rm source/cache/checksums.json  # 或编辑删除对应 key

# 3. 重新采集
uv run python collect.py --module 11-replicator-core --incremental
```

### 9.3 缓存损坏

**症状**: `Checksum verification failed` 或内容明显不对

**解决**:
```bash
# 清除所有缓存
rm -rf source/cache
rm -rf source/raw

# 全量重抓
uv run python collect.py
```

### 9.4 Manifest Schema 错误

**症状**: `JSONDecodeError` 或 `KeyError: 'pages'`

**解决**:
```bash
# 1. 验证 JSON 格式
python3 -m json.tool manifests/11-replicator-core.json

# 2. 检查必需字段
python3 - <<'PYEOF'
import json
from pathlib import Path
for f in Path("manifests").glob("*.json"):
    m = json.loads(f.read_text())
    assert "module" in m, f"{f} missing 'module'"
    assert "output" in m, f"{f} missing 'output'"
    assert "pages" in m, f"{f} missing 'pages'"
    for p in m["pages"]:
        assert "url" in p, f"{f} page missing 'url'"
        assert "title" in p, f"{f} page missing 'title'"
    print(f"{f}: OK ({len(m['pages'])} pages)")
PYEOF
```

## 10. 工具清单

| 脚本 | 用途 | 运行频率 |
|------|------|----------|
| `collect.py` | 采集 + 组装 | 每次更新 |
| `scripts/check_coverage.py` | 检查覆盖率 | 每周 |
| `scripts/compare_coverage.py` | 对比已采集 vs 目标 URL | 按需 |
| `scripts/check_mojibake.py` | 检查 raw/output 中的提取乱码 | 每次采集后 |
| `scripts/repair_mojibake.py` | 修复既有 Markdown 中的已知乱码模式 | 按需 |
| `scripts/coverage_analysis.md` | 覆盖率分析报告 | 按需 |

## 11. 常见问题

**Q: 为什么不直接用在线文档？**
A: 离线文档可以：(1) 无网络环境下工作，(2) 快速全文搜索，(3) 版本锁定避免内容漂移，(4) Agent 消费更稳定。

**Q: 为什么覆盖率只有 58%？**
A: 未采集的 42% 主要是明确排除的模块 (ROS2 37页, Legal 13页, Migration 13页, Cortex 6页, Cumotion 7页, Pink 4页等)。这些内容与 SDG 开发关系不大。

**Q: 如何处理 Isaac Sim 版本升级？**
A: 
1. 备份当前 source/raw 和 output
2. 修改 manifest 的 `isaac_version` 字段
3. 清除缓存 `rm -rf source/cache`
4. 全量重抓 `uv run python collect.py`
5. 对比变化 `git diff output/`
6. 更新 05_Python_API_Quickref (如果 API 签名变化)

**Q: 如何贡献新模块？**
A: 
1. 创建 manifest `manifests/NN-topic.json`
2. 运行 `uv run python collect.py --module NN-topic`
3. 在 00_学习路径 中添加入口
4. 更新 README 的模块列表
5. 提交 PR

**Q: defuddle 提取质量差怎么办？**
A: 
1. 尝试 `collect.py --extractor bs4` (备选提取器)
2. 手动编辑 raw 文件，修复后再 `--assemble-only`
3. 如果是系统性问题，检查 defuddle 版本或配置

---

**Last updated**: 2026-06-22
**Maintainer**: R (Hermes Agent)
