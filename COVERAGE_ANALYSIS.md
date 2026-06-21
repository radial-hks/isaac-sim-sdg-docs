# Isaac Sim 文档覆盖率分析

> 维护此文档的目的: 记录覆盖率的 **决策推理**，不只是数字。
> 数字用 `scripts/check_coverage.py` 实时获取。
> 此文档回答: "为什么采了/没采某个模块"，为后续扩展提供依据。

最后更新: 2026-06-22
当前覆盖率: 225 / 385 页 (58%)

```bash
# 获取实时覆盖率
python3 scripts/check_coverage.py
```

---

## 一、已采集模块（225 页）

| 模块 | 页数 | 采集原因 |
|------|------|----------|
| action_and_event_data_generation | 35 | SDG 行为数据生成核心 |
| replicator_tutorials | 17 | Replicator 全流程 |
| core_api_tutorials | 7 | Python API 基础 |
| development_tools | 6 | VSCode/Python Server/MCP |
| python_scripting | 6 | Standalone 脚本 |
| utilities | 8 | Extension 模板、调试 |
| assets | 7 | SimReady 资产库 |
| installation | 7 | 容器/云端部署 (Headless 刚需) |
| omniverse_usd | 5 | USD 基础 |
| reference_material | 5 | 性能优化、规范 |
| digital_twin | 6 | 数字孪生场景 |
| introduction | 5 | 快速入门 + 架构 |
| isaac_lab_tutorials | 5 | Isaac Lab (Sim2Real) |
| sensors | 9 | 相机、RTX 标注器、PhysX 传感器 |
| physics | 4 | 物理引擎基础 |
| gui | 3 | GUI 参考 |
| robot_setup | 18 | 机器人 rig/pose/wizard 工具链 |
| robot_setup_tutorials | 14 | 机器人配置实战 |
| robot_simulation | 6 | Articulation Controller / Gripper |
| omnigraph | 7 | OmniGraph 自定义节点深度 |
| openusd_tuning_tutorials | 8 | USD collider/joint drive 调优 |
| manipulators | 17 | 机械臂运动规划 (RMPflow/cuRobo) |
| synthetic_data_generation | 4 | SDG 工作流 |
| app_template | 1 | 应用模板 |

## 二、明确不采集的模块（160 页）+ 排除理由

**维护说明**: 此表是排除决策的"记忆"。如果未来某个模块的目标改变（例如决定引入 ROS 2），应从此表移出并采集。

### 🔴 强排除（与 SDG 目标完全无关）

| 模块 | 页数 | 排除理由 | 触发重新评估的条件 |
|------|------|----------|-------------------|
| ros2_tutorials | 37 | SDG 不需要 ROS | 当需要 Sim↔ROS 联调时 |
| nvidia_isaac_ros | 1 | 同上 | 同上 |
| common (Legal) | 13 | 法律文档，无开发价值 | 涉及许可证合规审计时 |
| migration_guides | 13 | 版本迁移，一次性阅读 | Isaac Sim 升级到新版本时 |
| overview | 6 | 论坛/FAQ/帮助 | 无 |
| cortex_tutorials | 6 | 机器人行为树，非 SDG | 需要复杂行为建模时 |
| cumotion | 7 | GPU 运动规划，非 SDG | 需要大规模轨迹优化时 |
| pink (IK 控制器) | 4 | IK 算法细节 | 需要自研 IK 时 |
| newton_actuators | 5 | Newton 物理执行器深度 | 无 |
| robot_motion_experimental | 1 | 实验性运动模块 | 无 |
| search.html/genindex.html | 2 | 导航页，无内容 | 无 |
| reference_python_api.html | 1 | 索引页 | 无 |

**强排除小计: 95 页** (永久不需采集，除非目标扩展)

### 🟡 弱排除（已部分覆盖，剩余页面低价值）

| 模块 | 剩余未采页数 | 已采集 | 剩余页面类型 |
|------|-------------|--------|-------------|
| installation | 8 | 7 | 次要云厂商 (Azure/GCP/Volcano/Baidu/Brev/Launchable)、FAQ、requirements |
| python_scripting | 1 | 6 | index.html (导航页) |
| development_tools | 1 | 6 | index.html (导航页) |
| digital_twin | 2 | 6 | index、troubleshooting (低价值补充) |
| robot_setup | 1 | 18 | 部分页面已去重 |
| introduction | 4 | 5 | examples/menu_examples/standalone_examples_list/tutorial_list (导航页) |
| reference_material | 1 | 5 | community_highlights (非开发) |
| assets | 4 | 7 | 次要资产页 (nova_carter/camera_depth_sensors/nonvisual_sensors/nurec) |
| gui | 4 | 3 | 补充 GUI 页 (index/menu_create/preferences/selection-modes) |
| physics | 4 | 4 | 补充物理页 (joint_inspector/new_physics_engine/newton_physics/physics_resources) |

**弱排除小计: 30 页** (低价值补充页，按需可采)

### 🟢 可补充（按需扩展时考虑）

| 模块 | 页数 | 内容 | 什么场景下采 |
|------|------|------|-------------|
| motion_generation (非 manipulators 下) | 4 | Mobile robot control / trajectory planning | 需要复杂移动机器人运动时 |
| installation 剩余 8 页 | 8 | Azure/GCP 云部署 | 需要部署到特定云厂商时 |
| introduction 剩余 4 页 | 4 | 示例列表 | 需要查找更多 example 时 |

**可补充小计: 16 页** (按需触发)

## 三、覆盖率演进

| 时间点 | 覆盖率 | 页数 | 触发事件 |
|--------|--------|------|----------|
| 2026-06-21 初次采集 | 36% | 139 | SDG + Development_Component |
| 2026-06-22 模块重构 | 36% | 139 | 合并两个集合到单一 repo |
| 2026-06-22 补充采集 | 58% | 225 | 新增 07/08/09 (robot_setup/omnigraph/advanced) |

## 四、后续扩展决策指南

当考虑是否采集新页面时，参照此决策树：

```
需要该页面吗？
├── 是 → 是否已在现有 manifest 里?
│   ├── 是 → 直接采集 (collect.py --incremental)
│   └── 否 → 创建新 manifest 模块
├── 不确定 → 看本表"强排除/弱排除"分类
│   ├── 在强排除列表 → 不采（除非目标扩展）
│   ├── 在弱排除列表 → 评估剩余页面价值再定
│   └── 不在任何列表 → 新模块，按流程评估
└── 否 → 不采
```

**目标扩展清单**（目前不计划，但如果启动以下工作则需采集）：

1. **ROS 2 集成** — 需要完整采集 `ros2_tutorials` (37 页) + `nvidia_isaac_ros` (1 页)
2. **Isaac Sim 版本升级** — 需要重新评估 `migration_guides` (13 页)
3. **复杂行为建模** — 需要 `cortex_tutorials` (6 页)
4. **自研运动规划** — 需要 `cumotion` (7 页) + `pink` (4 页)
5. **多云厂商部署** — 需要 `installation` 剩余 8 页

## 五、维护规范

1. **覆盖率数字不在此文档维护** — 用 `python3 scripts/check_coverage.py` 实时查询
2. **本表只更新决策** — 新采集一个模块，从"未采集"移到"已采集"并删除排除理由
3. **目标变化时更新第四节** — 扩展清单是活的，随业务需求变化
4. **commit message 标记** — 修改本表用 `docs: coverage analysis: <变更说明>`
