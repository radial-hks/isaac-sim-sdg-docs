# Isaac Sim SDG 专题文档 Pipeline

> Isaac Sim 6.0 — SimReady + Replicator + SDG 专题文档的自动化采集与组装系统

## 目标

为 **合成数据生成 (SDG)** 能力构建完整、可迭代更新的离线文档集。
覆盖 Replicator 引擎、Domain Randomization、SimReady 资产、传感器标注、SDG 工作流。

## 目录结构

```
Isaac_Sim_SDG_Component/
├── collect.py              # 主采集脚本（并发抓取 + defuddle 提取 + 组装）
├── pyproject.toml          # uv 项目配置
├── .gitignore
├── README.md
├── manifests/              # 每个模块的 URL 清单（JSON）
│   ├── 01-replicator-core.json
│   ├── 02-sdg-workflows.json
│   ├── 03-replicator-agent.json
│   ├── 04-domain-randomization.json
│   ├── 05-sensors-annotators.json
│   ├── 06-simready-assets.json
│   └── 07-sdg-pipeline.json
├── source/
│   ├── raw/                # 单页提取结果（带 frontmatter 的 md 文件）
│   │   ├── replicator_tutorials/
│   │   ├── synthetic_data_generation/
│   │   └── ...
│   └── cache/              # 采集元数据缓存（.gitignore）
│       └── .collect_cache.json
├── output/                 # 组装后的模块文档（最终产物）
│   ├── 00_SDG_概览与索引.md
│   ├── 01_Replicator_Core.md
│   ├── 02_SDG_Workflows.md
│   ├── 03_Replicator_Agent.md
│   ├── 04_Domain_Randomization.md
│   ├── 05_Sensors_and_Annotators.md
│   ├── 06_SimReady_Assets.md
│   └── 07_SDG_实战Pipeline.md
└── logs/                   # 采集日志
```

## 用法

```bash
cd ~/Desktop/Isaac_Sim_SDG_Component
uv sync

# 全量采集 + 组装
uv run python collect.py

# 增量更新（只抓取 checksum 变化的页面）
uv run python collect.py --incremental

# 只采集指定模块
uv run python collect.py --module 01-replicator-core

# 试运行（不写文件）
uv run python collect.py --dry-run

# 只组装（跳过采集，用已有 raw 文件）
uv run python collect.py --assemble-only
```

## 迭代更新流程

1. 修改 `manifests/*.json` 增删 URL
2. 运行 `uv run python collect.py --incremental`
3. `git diff` 检查变更
4. `git add + commit` 记录版本

## 文档来源

- 主文档站: https://docs.isaacsim.omniverse.nvidia.com/latest/
- Python API: https://docs.isaacsim.omniverse.nvidia.com/latest/py/
- Omniverse 层: https://docs.omniverse.nvidia.com/
- GitHub: https://github.com/NVIDIA-Omniverse/kit-usd-agents

## 与 Development_Component 的关系

本 Pipeline 聚焦 SDG 专题，与 `Isaac_Sim_Development_Component/`（通用开发基础）互补：
- Development_Component 覆盖：开发工具、Python 脚本、OmniGraph、Core API 教程
- SDG_Component 覆盖：Replicator、Domain Randomization、SDG Pipeline、SimReady 资产
