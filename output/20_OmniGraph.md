# OmniGraph — 可视化编程框架

> Isaac Sim 的核心计算和逻辑编排引擎
> 来源：https://docs.isaacsim.omniverse.nvidia.com/latest/omnigraph/

---

## 什么是 OmniGraph

OmniGraph 是 Omniverse 的可视化编程框架：
- **图框架**：连接多个系统的函数
- **计算框架**：高效后端 + 高度自定义节点
- 在 Isaac Sim 中是 **Replicator、ROS 2 Bridge、传感器访问、控制器、I/O 设备、UI** 的主引擎

访问：Window > Graph Editors > Action Graph

---

## 核心概念

### 图的类型
- **Action Graph**：事件驱动，需要显式触发（execIn），适合控制器和状态机
- **Push Graph**：每帧自动执行

### 节点结构
每个节点由两个文件定义：
1. **.ogn 文件**（JSON）— 定义结构：inputs/outputs/parameters
2. **.py 或 .cpp 文件** — 实现功能

### .ogn 文件示例
```json
{
  "NodeName": {
    "version": 1,
    "categories": "examples",
    "description": ["Minimum Example"],
    "language": "python",
    "metadata": { "uiName": "minimum example" },
    "inputs": {
      "execIn": {
        "description": "the trigger input that starts the node",
        "type": "execution"
      },
      "value_input": {
        "type": "double",
        "description": "a number",
        "default": 0.0
      }
    },
    "outputs": {
      "output_bool": {
        "type": "bool",
        "description": "let output be a boolean"
      }
    }
  }
}
```

**`execIn` 特殊输入**：
- Action Graph 中用来触发节点（物理 tick、stage 事件）
- Push Graph 中不需要（自动运行）

### Python 节点实现
```python
class OgnNodeName:   # 类名必须匹配 .ogn 中的 NodeName
    @staticmethod
    def compute(db):
        # db.inputs.xxx / db.outputs.xxx 访问输入输出
        db.outputs.out = bool(db.inputs.value_input > 0.0)
        return True   # 成功返回 True
```

文件命名必须以 `Ogn` 前缀开头：`Ogn<NodeName>.py`

---

## OmniGraph 教程（Jetbot 控制）

### 场景搭建
1. 新建 stage → Create > Physics > Ground Plane
2. Content Browser → Isaac Sim/Robots/NVIDIA/Jetbot/jetbot.usd 拖入
3. 定位到 /World/jetbot，在 ground plane 上方
4. 点击 Play 验证 Jetbot 落地 → Stop

### 构建控制图

#### 节点 1: On Playback Tick（事件）
- 搜索 `playback`
- 每仿真帧发一个 exec 事件

#### 节点 2: Differential Controller（计算）
- 搜索 `controller`
- 接收线速度 + 角速度 → 输出左右轮速度

#### 节点 3: Articulation Controller（执行）
- 连接到 Jetbot 根 prim `/World/jetbot`
- 指定关节名：`left_wheel_joint`, `right_wheel_joint`

#### 常量 Token 节点
- 两个 Constant Token 节点，分别设置关节名
- Make Array 节点组装为 token[] 数组
- 连接到 Articulation Controller 的 Joint Names 输入

#### 连接
```
On Playback Tick (Tick) → Differential Controller (Exec In)
                        → Articulation Controller (Exec In)
Differential Controller (Velocity Command) → Articulation Controller (Velocity Command)
Constant Token[] → Make Array → Articulation Controller (Joint Names)
```

#### 参数设置（Differential Controller）
- wheelDistance = 0.1125
- wheelRadius = 0.03
- maxAngularSpeed = 0.2

Play 后在属性面板拖动 linear/angular velocity 即可控制 Jetbot。

---

## Commonly Used Shortcuts（快捷键）

位置：Tools > Robotics > OmniGraph Controllers

### Articulation Controller（关节位置/速度控制器）
- Robot Prim：机器人父 prim
- Graph Path：生成图的路径（默认 `/Graph/{type}_controller`）
- Add to Existing Graph：追加到现有图

**使用**：
- 播放仿真
- 在 graph 的 JointCommandArray 节点修改值

### Differential Controller（差速驱动）
- Robot Prim, Wheel Radius, Distance between wheels
- Left/Right Joint Names（可选，多关节时需要）
- Use Keyboard Control（可选，WASD）

**WASD 控制**：
- ScaleLinear / ScaleAngular 节点调节速度比例
- 调节后让 DifferentialController 输出在旋转/前进时量级接近

### Gripper Controller
- Parent Robot, Gripper Root
- Gripper Speed（m/s 或 rad/s）
- Gripper Joint Names（逗号分隔）
- Open/Close Position Limit（不填则用 USD 默认）
- O/C/N 键盘控制（开/合/停）

---

## OmniGraph Python Scripting

### 创建图（og.Controller.edit）
```python
import omni.graph.core as og
keys = og.Controller.Keys

graph_handle, list_of_nodes, _, _ = og.Controller.edit(
    {"graph_path": "/action_graph", "evaluator_name": "execution"},
    {
        keys.CREATE_NODES: [
            ("tick", "omni.graph.action.OnTick"),
            ("print", "omni.graph.ui_nodes.PrintText"),
        ],
        keys.SET_VALUES: [
            ("print.inputs:text", "Hello World"),
            ("print.inputs:logLevel", "Warning"),
        ],
        keys.CONNECT: [
            ("tick.outputs:tick", "print.inputs:execIn"),
        ],
    },
)
```

### 读取/修改属性
```python
# 读
existing_text = og.Controller.attribute("/action_graph/print.inputs:text").get()

# 写
og.Controller.attribute("/action_graph/print.inputs:text").set("New Text")
```

### 动态添加节点和连接
```python
og.Controller.create_node("/action_graph/new_node", "omni.graph.nodes.ConstantString")
og.Controller.attribute("/action_graph/new_node.inputs:value").set("test")
og.Controller.connect("/action_graph/new_node.inputs:value", "/action_graph/print.inputs:text")
```

### On Demand 执行（手动触发）
```python
demand_graph, _, _, _ = og.Controller.edit(
    {
        "graph_path": "/ondemand_graph",
        "evaluator_name": "execution",
        "pipeline_stage": og.GraphPipelineStage.GRAPH_PIPELINE_STAGE_ONDEMAND,
    },
    { # ... 节点和连接 ... }
)

# 手动触发
demand_graph.evaluate()

# 切换现有图的执行模式
demand_graph.change_pipeline_stage(og.GraphPipelineStage.GRAPH_PIPELINE_STAGE_ONDEMAND)
```

---

## Custom Python Nodes

### 创建流程
1. 写 `.ogn` 文件（定义 inputs/outputs）
2. 写 `.py` 文件（`class OgnNodeName.compute(db)` 方法）
3. 放入扩展的 `ogn/python/nodes/` 目录
4. 在 Action Graph 中搜索使用

### 命名规则
- 文件名：`Ogn<NodeName>.py`
- 类名：`Ogn<NodeName>`
- .ogn 文件名：`Ogn<NodeName>.ogn`

### 内部状态
`compute()` 内部无状态。如需跨 tick 存储，使用 `internal state`。

### 查找现有节点参考
- 鼠标悬停节点 → tooltip 显示扩展名
- 导航到：`exts/isaacsim.<ext_name>/isaacsim/<ext_name>/ogn/python/nodes/`
- 注意：`OgnXxxDatabase.py` 是生成文件，不是节点实现

---

## Custom C++ Nodes

- .ogn 文件格式与 Python 相同
- 需要 Kit C++ Extension Template 构建
- 参考：[kit-extension-template-cpp](https://github.com/NVIDIA-Omniverse/kit-extension-template-cpp/tree/main/source/extensions/omni.example.cpp.omnigraph_node)

---

## Custom IPC Nodes（进程间通信）

用于构建 OmniGraph 节点进行跨进程通信（如与 ROS 2、外部仿真、硬件）。

### 脚手架生成
```bash
./repo.sh template new
# 选择 "Isaac Sim OmniGraph Node Extension"
# 提供 extension_name, title, description, category
```

### 目录结构
```
source/extensions/<extension_name>/
├── config/extension.toml
├── nodes/
│   ├── OgnExampleCpp.ogn
│   └── OgnExampleCpp.cpp
├── plugins/<extension_name>/PluginInterface.cpp
├── bindings/<extension_name>/Bindings.cpp
├── python/nodes/
│   ├── OgnExamplePython.ogn
│   └── OgnExamplePython.py
├── python/impl/extension.py
└── premake5.lua
```

### 构建
```bash
./build.sh   # 或 .\\build.bat
```

### Python IPC 依赖
`config/extension.toml`：
```toml
[python.pipapi]
requirements = ["pyzmq>=25", "grpcio"]
use_online_index = true   # 必须设置！
```

### 关键模式
- **BaseResetNode**：transport 生命周期
- **compute 中的非阻塞 I/O**：避免卡死仿真
- **internal_state() 工厂 + db.per_instance_state**：多实例支持

### 验证脚手架
1. 启动 repo-build 的 Isaac Sim（不是单独安装的版本）
2. Window > Extensions 启用你的扩展
3. Window > Graph Editors > Action Graph → 节点库搜索
4. 节点不出现 → 检查 build 成功 + 扩展启用 + 重启 Isaac Sim

---

## 关键链接

- [OmniGraph (Omniverse)](https://docs.omniverse.nvidia.com/extensions/latest/ext_omnigraph.html)
- [Core Concepts](https://docs.omniverse.nvidia.com/extensions/latest/ext_omnigraph/getting-started/core_concepts.html)
- [Node Library](https://docs.omniverse.nvidia.com/extensions/latest/ext_omnigraph/node-library/node-library.html)
- [C++ Extension Template](https://docs.omniverse.nvidia.com/kit/docs/kit-extension-template-cpp/latest/index.html)
- [Gentle Intro Tutorial](https://docs.omniverse.nvidia.com/extensions/latest/ext_omnigraph/tutorials/gentle_intro.html)
- [Python API](https://docs.omniverse.nvidia.com/kit/docs/omni.graph/latest/omni.graph.core.html)
