# Isaac Sim SDG Docs

> Isaac Sim 6.0 合成数据生成 (SDG) 离线知识库
> 16 模块 · 225 覆盖页 · 58% 覆盖率 · 自动化采集 + 迭代更新

## 状态

| 指标 | 值 |
|------|-----|
| 采集页面 | 235 raw → 229 unique URL → 225 covered |
| 覆盖率 | 225 / 385 (Isaac Sim 主文档站) = **58%** |
| 模块数 | 16 个 (manifests/) |
| 输出体积 | ~5.0 MB (output/) |
| Isaac Sim 版本 | 6.0 |
| 最后更新 | 2026-06-21 |

## 目录结构

```
isaac-sim-sdg-docs/
├── collect.py                       # 采集脚本 (并发 + defuddle + 组装)
├── pyproject.toml                   # uv 项目配置
├── README.md                        # 本文件
├── PROJECT_WORKFLOW.md              # 项目工作流手册 (采集/迭代/Agent 集成/故障恢复)
│
├── manifests/                       # URL 清单 (编辑这里来增删页面)
│   ├── 01-concepts.json             # 概念与架构 (20 页)
│   ├── 02-fundamentals-dev.json     # 开发基础 (21 页)
│   ├── 03-extension-dev.json        # Extension 开发 (10 页)
│   ├── 04-headless-deploy.json      # Headless & 部署 (8 页)
│   ├── 05-python-api-quickref.json  # Python API 速查 (23 页)
│   ├── 06-sim2real-ue5.json         # Sim2Real & UE5 (15 页)
│   ├── 07-robot-setup.json          # 机器人配置 (32 页)
│   ├── 08-omnigraph-robot-sim.json  # OmniGraph + 机器人仿真 (13 页)
│   ├── 09-advanced-optionals.json   # 进阶可选 (44 页)
│   ├── 11-replicator-core.json      # Replicator 核心 (10 页)
│   ├── 12-sdg-workflows.json        # SDG 工作流 (9 页)
│   ├── 13-replicator-agent.json     # Replicator Agent (14 页)
│   ├── 14-domain-randomization.json # Domain Randomization (15 页)
│   ├── 15-sensors-annotators.json   # 传感器与标注器 (9 页)
│   ├── 16-simready-assets.json      # SimReady 资产 (11 页)
│   └── 17-sdg-pipeline.json         # SDG Pipeline (8 页)
│
├── source/raw/                      # 单页原始提取 (YAML frontmatter, git tracked)
├── source/cache/                    # 采集缓存 (.gitignore)
├── output/                          # 组装后的模块文档 (最终产物)
│   ├── 00_统一学习路径.md           # 学习导航 (手动维护)
│   ├── 01_Concepts_and_Architecture.md    # 214K
│   ├── 02_Development_Fundamentals.md     # 180K
│   ├── 03_Extension_Development.md        # 77K
│   ├── 04_Headless_and_Deploy.md          # 81K
│   ├── 05_Python_API_Quickref.md          # 1.8M
│   ├── 06_Sim2Real_and_UE5.md             # 137K
│   ├── 07_Robot_Setup.md                  # 411K
│   ├── 08_OmniGraph_and_Robot_Sim.md      # 156K
│   ├── 09_Manipulators_Sensors_USDTuning.md # 433K
│   ├── 11_Replicator_Core.md              # 364K
│   ├── 12_SDG_Workflows.md                # 449K
│   ├── 13_Replicator_Agent.md             # 185K
│   ├── 14_Domain_Randomization.md         # 108K
│   ├── 15_Sensors_and_Annotators.md       # 107K
│   ├── 16_SimReady_Assets.md              # 111K
│   ├── 17_SDG_Pipeline.md                 # 204K
│   └── 20_OmniGraph.md                    # 8.8K (手动整理)
│
└── scripts/                         # 辅助脚本
    ├── check_coverage.py            # 覆盖率检查
    ├── compare_coverage.py          # 覆盖率详细对比
    ├── check_mojibake.py            # 乱码质量检查
    └── repair_mojibake.py           # 既有 Markdown 乱码修复
```

| 文档 | 说明 |
|------|------|
| README.md | 本文件 |
| PROJECT_WORKFLOW.md | 项目工作流手册 (采集/迭代/Agent 集成/故障恢复) |
| COVERAGE_ANALYSIS.md | 覆盖率决策分析 (为什么采/没采某个模块) |
```

## 用法

```bash
cd ~/Desktop/isaac-sim-sdg-docs
uv sync

# 全量采集 + 组装 (首次或大版本升级)
uv run python collect.py

# 增量更新 (只抓内容变化的页面)
uv run python collect.py --incremental

# 只更新指定模块
uv run python collect.py --incremental --module 11-replicator-core

# 试运行 (不写文件)
uv run python collect.py --dry-run

# 只组装 (跳过采集，调格式用)
uv run python collect.py --assemble-only

# 检查覆盖率
python3 scripts/check_coverage.py

# 检查提取乱码
python3 scripts/check_mojibake.py
```

## 学习入口

阅读顺序：`output/00_统一学习路径.md`

三阶段路径：
1. **Phase 1 (1-2 w)**: 01 Concepts → 02 Dev Fundamentals → 建立心智模型
2. **Phase 2 (2-4 w)**: 08 OmniGraph → 03 Extension → 11 Replicator → 14 DR → 开发层
3. **Phase 3 (4-8 w)**: 07 Robot Setup → 15 Sensors → 12 SDG → 17 Pipeline → 工程化

## 文档来源

- Isaac Sim 6.0: https://docs.isaacsim.omniverse.nvidia.com/latest/
- Python API: https://docs.isaacsim.omniverse.nvidia.com/latest/py/
- Omniverse: https://docs.omniverse.nvidia.com/

## 详细文档

- **项目工作流**: [PROJECT_WORKFLOW.md](./PROJECT_WORKFLOW.md) — 采集策略、Agent 集成、迭代流程、故障恢复

## 排除清单 (明确不采集的模块)

| 模块 | 页数 | 排除原因 |
|------|------|---------|
| ros2_tutorials | 37 | 不需要 ROS 集成 |
| common | 13 | 法律/许可 |
| migration_guides | 13 | 版本迁移 |
| cortex_tutorials | 6 | 行为树 (非 SDG) |
| cumotion | 7 | GPU 运动规划 |
| newton_actuators | 5 | Newton 执行器 |
| pink | 4 | IK 控制器 |
| 其他 index/search/genindex | ~10 | 导航页 |
