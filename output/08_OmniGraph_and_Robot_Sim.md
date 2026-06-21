# OmniGraph 深度教程 + Robot Simulation

> OmniGraph 自定义节点（C++/Python/IPC）+ Robot Simulation 核心（Articulation Controller, Gripper）
> Isaac Sim 版本: 6.0
> 最后组装: 2026-06-21 13:58 UTC
> 来源页数: 13

---

## 来源链接

- [OmniGraph Index](https://docs.isaacsim.omniverse.nvidia.com/latest/omnigraph/index.html)
- [OmniGraph Tutorial](https://docs.isaacsim.omniverse.nvidia.com/latest/omnigraph/omnigraph_tutorial.html)
- [OmniGraph Scripting](https://docs.isaacsim.omniverse.nvidia.com/latest/omnigraph/omnigraph_scripting.html)
- [Custom Python Nodes](https://docs.isaacsim.omniverse.nvidia.com/latest/omnigraph/omnigraph_custom_python_nodes.html)
- [Custom C++ Nodes](https://docs.isaacsim.omniverse.nvidia.com/latest/omnigraph/omnigraph_custom_cpp_nodes.html)
- [Custom IPC Nodes](https://docs.isaacsim.omniverse.nvidia.com/latest/omnigraph/omnigraph_custom_ipc_nodes.html)
- [OmniGraph Shortcuts](https://docs.isaacsim.omniverse.nvidia.com/latest/omnigraph/omnigraph_shortcuts.html)
- [Robot Simulation Index](https://docs.isaacsim.omniverse.nvidia.com/latest/robot_simulation/index.html)
- [Articulation Controller](https://docs.isaacsim.omniverse.nvidia.com/latest/robot_simulation/articulation_controller.html)
- [Mobile Robot Controllers](https://docs.isaacsim.omniverse.nvidia.com/latest/robot_simulation/mobile_robot_controllers.html)
- [Surface Gripper](https://docs.isaacsim.omniverse.nvidia.com/latest/robot_simulation/ext_isaacsim_robot_surface_gripper.html)
- [Grasp Editor](https://docs.isaacsim.omniverse.nvidia.com/latest/robot_simulation/grasp_editor.html)
- [Policy Example](https://docs.isaacsim.omniverse.nvidia.com/latest/robot_simulation/ext_isaacsim_robot_policy_example.html)

---


## Robot Simulation

### Robot Simulation Index

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/omnigraph/index.html

* Robot Simulation

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Robot Simulation

Note

We are introducing a new [Motion Generation (Experimental)](../motion_generation/index.html) API which aims to package all Isaac Sim control algorithms
(wheeled robots, manipulators, humanoids) under a single framework. This new API provides a flexible controller composition
system and simplifies building collision world models from your USD stage. This extension is documented under
the [Robot Motion (Experimental)](../robot_motion_experimental/index.html) section.

The Robot Simulation section provides information on tools that you will need to move a robot. The lowest level of control is joint control. For the next level up, we separated the controllers by the robot types, for they represent the three types of controllers we provide in Isaac Sim:

* **Wheeled Robots**: use controllers that are based on universal formulas and require very few robot-specific parameters as inputs.
* **Manipulators**: use controllers that are based on complex optimization, therefore the same robot performing the same task could use many variety of controllers, each with a different optimization method. They often require the robot models in the optimization process.
* **Policy Controlled Robots**: uses controllers that are trained using reinforcement learning. They also has a much looser definition “controllers”, for they can have task and path planners embedded as well.

## Joint Level Control

* [Articulation Controller](articulation_controller.html)

## Wheeled Robots

* [Mobile Robot Controllers](mobile_robot_controllers.html)

## Manipulators

* [Motion Generation (Deprecated)](../manipulators/motion_generation_overview.html)
* [Surface Gripper Extension](ext_isaacsim_robot_surface_gripper.html)
* [Grasp Editor](grasp_editor.html)

## Policy Controlled Robots

* [Reinforcement Learning Policies Examples in Isaac Sim](ext_isaacsim_robot_policy_example.html)

### Tips and Deep Dives

* [Robot Simulation Tips](robot_simulation_tips.html)
* [Useful Links](robot_simulation_core_concepts.html)

On this page

* [Joint Level Control](#joint-level-control)
* [Wheeled Robots](#wheeled-robots)
* [Manipulators](#manipulators)
* [Policy Controlled Robots](#policy-controlled-robots)
  + [Tips and Deep Dives](#tips-and-deep-dives)

---

### Robot Simulation Index

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/robot_simulation/index.html

* Robot Simulation

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Robot Simulation

Note

We are introducing a new [Motion Generation (Experimental)](../motion_generation/index.html) API which aims to package all Isaac Sim control algorithms
(wheeled robots, manipulators, humanoids) under a single framework. This new API provides a flexible controller composition
system and simplifies building collision world models from your USD stage. This extension is documented under
the [Robot Motion (Experimental)](../robot_motion_experimental/index.html) section.

The Robot Simulation section provides information on tools that you will need to move a robot. The lowest level of control is joint control. For the next level up, we separated the controllers by the robot types, for they represent the three types of controllers we provide in Isaac Sim:

* **Wheeled Robots**: use controllers that are based on universal formulas and require very few robot-specific parameters as inputs.
* **Manipulators**: use controllers that are based on complex optimization, therefore the same robot performing the same task could use many variety of controllers, each with a different optimization method. They often require the robot models in the optimization process.
* **Policy Controlled Robots**: uses controllers that are trained using reinforcement learning. They also has a much looser definition “controllers”, for they can have task and path planners embedded as well.

## Joint Level Control

* [Articulation Controller](articulation_controller.html)

## Wheeled Robots

* [Mobile Robot Controllers](mobile_robot_controllers.html)

## Manipulators

* [Motion Generation (Deprecated)](../manipulators/motion_generation_overview.html)
* [Surface Gripper Extension](ext_isaacsim_robot_surface_gripper.html)
* [Grasp Editor](grasp_editor.html)

## Policy Controlled Robots

* [Reinforcement Learning Policies Examples in Isaac Sim](ext_isaacsim_robot_policy_example.html)

### Tips and Deep Dives

* [Robot Simulation Tips](robot_simulation_tips.html)
* [Useful Links](robot_simulation_core_concepts.html)

On this page

* [Joint Level Control](#joint-level-control)
* [Wheeled Robots](#wheeled-robots)
* [Manipulators](#manipulators)
* [Policy Controlled Robots](#policy-controlled-robots)
  + [Tips and Deep Dives](#tips-and-deep-dives)

---

### Articulation Controller

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/robot_simulation/articulation_controller.html

* [Robot Simulation](index.html)
* Articulation Controller

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Articulation Controller

Deprecated

This page documents the legacy `ArticulationController` / `SingleArticulation` / `ArticulationAction` Python API, which has been deprecated. For new development, use the `Articulation` class from `isaacsim.core.experimental.prims`. See [Robot Simulation Snippets](../python_scripting/robots_simulation.html#isaac-robot-simulation-how-to) for end-to-end examples covering DOF position, velocity, and effort control, and the [Articulation](../py/source/extensions/isaacsim.core.experimental.prims/docs/index.html#isaacsim.core.experimental.prims.Articulation) API reference for the full method list.

**The OmniGraph node at the end of this page is still fully supported**, and wraps the updated [Articulation](../py/source/extensions/isaacsim.core.experimental.prims/docs/index.html#isaacsim.core.experimental.prims.Articulation) class.

## Overview

Articulation controller is the low level controller that controls joint position, joint velocity, and joint effort in Isaac Sim. The articulation controller can be interfaced using Python and OmniGraph.

Note

Angular units are expressed in radians while angles in USD are expressed in degrees and will be adjusted accordingly by the articulation controller.

## Python Interface

### Create the articulation controller

There are several ways to create the articulation controller. The articulation controller is usually created implicitly by applying articulation on a robot prim through the `SingleArticulation` class.
However, the articulation controller can be created directly by importing the controller class before the simulation starts, but this approach will require you to create or pass in the `Articulation` during initialization.

Single Articulation

> The snippet below will load and apply articulation on a franka robot.
>
> ```python
> import isaacsim.core.utils.stage as stage_utils
> from isaacsim.core.prims import SingleArticulation
>
> usd_path = "/Path/To/Robots/FrankaRobotics/FrankaPanda/franka.usd"
> prim_path = "/World/envs/env_0/panda"
>
> # load the Franka Panda robot USD file
> stage_utils.add_reference_to_stage(usd_path, prim_path)
> # wrap the prim as an articulation
> prim = SingleArticulation(prim_path=prim_path, name="franka_panda")
> ```

Articulation Controller

> ```python
> import isaacsim.core.utils.stage as stage_utils
> from isaacsim.core.api.controllers.articulation_controller import ArticulationController
>
> usd_path = "/Path/To/Robots/FrankaRobotics/FrankaPanda/franka.usd"
> prim_path = "/World/envs/env_0/panda"
>
> # load the Franka Panda robot USD file
> stage_utils.add_reference_to_stage(usd_path, prim_path)
> # Create the articulation controller
> articulation_controller = ArticulationController()
> ```

### Initialize the controller

After the simulation is started, the robot articulation must be initialized before any commands can be passed to the robot.

Single Articulation

> The more common approach is by initializing the single articulation object that you have created earlier, this will initialize the articulation controller and articulation view stored in the SingleArticulation object
>
> ```python
> prim.initialize()
> ```

Articulation Controller

> After the simulation starts, the articulation controller must be initialzied with an articulation view. Articulation view is the backend for selecting the joints and applying joint actions.
>
> For example, the code snippet below creates an articulation view with the Franka robot and initializes the articulation controller.
>
> ```python
> from isaacsim.core.prims import Articulation
>
> # Create the articulation view
> articulation_view = Articulation(prim_paths_expr="/World/envs/env_0/panda", name="franka_panda_view")
> # Initialize the articulation controller
> articulation_controller.initialize(articulation_view)
> ```

### Articulation Action

Joint controls commands are packaged in `ArticulationAction` objects first, before sending them to the articulation controller. The articulation controller allows you to specify the command joint postion, velocity and effort, as well as joint indicies of the joints actuated.

If the joint indice is empty, the articulation action will assume the command will apply to all joints of the robot, and if any of the command is 0, articulation action will assume it is unactuated.

For example, the snippet below creates the command that closes the franka robot fingers: panda\_finger\_joint1 (7) and panda\_finger\_joint2 (8) to 0.0

```python
import numpy as np
from isaacsim.core.utils.types import ArticulationAction

action = ArticulationAction(joint_positions=np.array([0.0, 0.0]), joint_indices=np.array([7, 8]))
```

This snippet creates the command that moves all the robot joints to the indicated position

```python
import numpy as np
from isaacsim.core.utils.types import ArticulationAction

action = ArticulationAction(joint_positions=np.array([0.0, -1.0, 0.0, -2.2, 0.0, 2.4, 0.8, 0.04, 0.04]))
```

Important

Make sure the joint commands matches the order and the number of joint indices passed in to the articulation action. If joint indice is not passed in, make sure the command matches the number of joints in the robot.

Note

A joint can only be controlled by one control method. For example a joint cannot be controlled by both desired position and desired torque

### Apply Action

The `apply_action` function in both `SingleArticulation` and `ArticulationController` classes will apply the `ArticulationAction` you created earlier to the robot.

Single Articulation

> ```python
> prim.apply_action(action)
> ```

Articulation Controller

> ```python
> articulation_controller.apply_action(action)
> ```

### Script Editor Example

You can try out basic articulation controller examples by running the following code snippets in the Script Editor. For more advanced usage, it is recommended to follow the [Core API Tutorial Series](../core_api_tutorials/index.html#isaac-sim-core-api-tutorials-page).

Single Articulation

> ```python
> import asyncio
>
> import numpy as np
> from isaacsim.core.api.world import World
> from isaacsim.core.prims import SingleArticulation
> from isaacsim.core.utils.stage import add_reference_to_stage
> from isaacsim.core.utils.types import ArticulationAction
> from isaacsim.storage.native import get_assets_root_path
>
>
> async def robot_control_example():
>     if World.instance():
>         World.instance().clear_instance()
>     world = World()
>     await world.initialize_simulation_context_async()
>     world.scene.add_default_ground_plane()
>
>     # Load the robot USD file
>     usd_path = get_assets_root_path() + "/Isaac/Robots/FrankaRobotics/FrankaPanda/franka.usd"
>     prim_path = "/World/envs/env_0/panda"
>     add_reference_to_stage(usd_path, prim_path)
>
>     # Create SingleArticulation wrapper (automatically creates articulation controller)
>     robot = SingleArticulation(prim_path=prim_path, name="franka_panda")
>     await world.reset_async()
>
>     # Initialize the robot (initializes articulation controller internally)
>     robot.initialize()
>
>     # Run simulation
>     await world.play_async()
>
>     # Get current joint positions
>     current_positions = robot.get_joint_positions()
>     print(f"Current joint positions: {current_positions}")
>
>     # Create target positions
>     target_positions = np.array([0.0, -1.5, 0.0, -2.8, 0.0, 2.8, 1.2, 0.04, 0.04])
>
>     # Create and apply articulation action
>     action = ArticulationAction(joint_positions=target_positions)
>     robot.apply_action(action)
>
>     await asyncio.sleep(5.0)  # Run for 5 seconds to reach target positions
>
>     # Get current joint positions
>     current_positions = robot.get_joint_positions()
>     print(f"Current joint positions: {current_positions}")
>
>     world.pause()
>
>
> # Run the example
> asyncio.ensure_future(robot_control_example())
> ```

Articulation Controller

> ```python
> import asyncio
>
> import numpy as np
> from isaacsim.core.api.controllers.articulation_controller import ArticulationController
> from isaacsim.core.api.world import World
> from isaacsim.core.prims import Articulation
> from isaacsim.core.utils.stage import add_reference_to_stage
> from isaacsim.core.utils.types import ArticulationAction
> from isaacsim.storage.native import get_assets_root_path
>
>
> async def robot_control_example():
>     if World.instance():
>         World.instance().clear_instance()
>     world = World()
>     await world.initialize_simulation_context_async()
>     world.scene.add_default_ground_plane()
>
>     # Load the robot USD file
>     usd_path = get_assets_root_path() + "/Isaac/Robots/FrankaRobotics/FrankaPanda/franka.usd"
>     prim_path = "/World/envs/env_0/panda"
>     add_reference_to_stage(usd_path, prim_path)
>
>     # Create Articulation view for the robot
>     robot_view = Articulation(prim_paths_expr=prim_path, name="franka_panda_view")
>
>     # Create and initialize the articulation controller with the articulation view
>     articulation_controller = ArticulationController()
>     articulation_controller.initialize(robot_view)
>
>     # Run simulation
>     await world.play_async()
>
>     # Get current joint positions
>     current_positions = robot_view.get_joint_positions()
>     print(f"Current joint positions: {current_positions}")
>
>     # Create target positions
>     target_positions = np.array([0.0, -1.5, 0.0, -2.8, 0.0, 2.8, 1.2, 0.04, 0.04])
>
>     # Create and apply articulation action
>     action = ArticulationAction(joint_positions=target_positions)
>     articulation_controller.apply_action(action)
>
>     await asyncio.sleep(5.0)  # Run for 5 seconds to reach target positions
>
>     # Get current joint positions
>     current_positions = robot_view.get_joint_positions()
>     print(f"Current joint positions: {current_positions}")
>
>     world.pause()
>
>
> # Run the example
> asyncio.ensure_future(robot_control_example())
> ```

## OmniGraph Interface

The articulation controller can also be accessed through OmniGraph nodes, providing a visual, node-based approach to robot control.

### Input Parameters

The articulation controller OmniGraph node accepts the following input parameters:

Articulation Controller OmniGraph Inputs

| Input Parameter | Description |
| --- | --- |
| **execIn** | Input execution trigger - connects to other nodes to control when the articulation controller runs |
| **targetPrim** | The prim containing the robot articulation root. Leave empty if using robotPath |
| **robotPath** | String path to the robot articulation root. Leave empty if using targetPrim |
| **jointIndices** | Array of joint indices to control. Leave empty to control all joints or use jointNames |
| **jointNames** | Array of joint names to control. Leave empty to control all joints or use jointIndices |
| **positionCommand** | Desired joint positions. Leave empty if not using position control |
| **velocityCommand** | Desired joint velocities. Leave empty if not using velocity control |
| **effortCommand** | Desired joint efforts/torques. Leave empty if not using effort control |

### Usage Guidelines

Important

**Parameter Validation**: Ensure joint commands match the order and number of joint indices or joint names. If neither joint indices nor joint names are specified, the command must match the total number of joints in the robot.

Note

**Control Method Limitation**: A joint can only be controlled by one method at a time. For example, a joint cannot be controlled by both position and effort commands simultaneously.

### Example Usage

For a complete example of the articulation controller OmniGraph node in action, see the `mock_robot_rigged` asset in the Content Browser at **Isaac Sim > Samples > Rigging > MockRobot > mock\_robot\_rigged.usd**.

On this page

* [Overview](#overview)
* [Python Interface](#python-interface)
  + [Create the articulation controller](#create-the-articulation-controller)
  + [Initialize the controller](#initialize-the-controller)
  + [Articulation Action](#articulation-action)
  + [Apply Action](#apply-action)
  + [Script Editor Example](#script-editor-example)
* [OmniGraph Interface](#omnigraph-interface)
  + [Input Parameters](#input-parameters)
  + [Usage Guidelines](#usage-guidelines)
  + [Example Usage](#example-usage)

---

### Mobile Robot Controllers

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/robot_simulation/mobile_robot_controllers.html

* [Robot Simulation](index.html)
* Mobile Robot Controllers

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Mobile Robot Controllers

Note

For new controller development, consider using the newer experimental motion generation API in [Motion Generation (Experimental)](../motion_generation/index.html), which provides improved interfaces and additional features.

## Differential controller

The differential controller uses the speed differential between the left and right wheels to control the robot’s linear and angular velocity. The differential robot enables the robot to turn in place and is used in the NVIDIA Nova Carter robot.

### The Math

\[ \begin{align}\begin{aligned}\omega\_R &= \frac{1}{2r}(2V + \omega l\_{tw})\\\omega\_L &= \frac{1}{2r}(2V - \omega l\_{tw})\end{aligned}\end{align} \]

where \(\omega\) is the desired angular velocity, \(V\) is the desired linear velocity, \(r\) is the radius of the wheels, and \(l\_{tw}\) is the distance between them.
\(\omega\_R\) is the desired right wheel angular velocity and \(\omega\_L\) is the desired left wheel angular velocity.

### OmniGraph Node

Differential Controller OmniGraph Inputs

| Input Commands | description |
| --- | --- |
| execIn | Input execution |
| wheelRadius | Radius of the wheels in meters |
| wheelDistance | Distance between the wheels in meters |
| dt | Delta time in seconds |
| maxAcceleration | Max linear acceleration for moving forward and reverse in m/s^2, 0.0 means not set |
| maxDeceleration | Max linear breaking of the robot in m/s^2, 0.0 means not set |
| maxAngularAcceleration | Max angular acceleration of the robot in rad/s^2, 0.0 means not set |
| maxLinearSpeed | Max linear speed allowed for the robot in m/s, 0.0 means not set |
| maxAngularSpeed | Max angular speed allowed for the robot in rad/s, 0.0 means not set |
| maxWheelSpeed | Max wheel speed in rad/s |
| Desired Linear Velocity | Desired linear velocity in m/s |
| Desired Angular Velocity | Desired angular velocity in rad/s |

Differential Controller OmniGraph Outputs

| Output Commands | description |
| --- | --- |
| VelocityCommand | Velocity command for the left and right wheel in m/s and rad/s |

Note

`VelocityCommand` is ordered as `[left_wheel_velocity, right_wheel_velocity]`. When wiring this output to an Articulation Controller, list the wheel joint names or indices in the same left-wheel, right-wheel order.

### Python

The code snippet below setups the differential controller for a NVIDIA Jetbot with a wheel radius of 3 cm and a base of 11.25cm, with a linear speed of 0.3m/s and angular speed of 1.0rad/s.

```python
# Reference: source/standalone_examples/api/isaacsim.robot.wheeled_robots.examples/jetbot_differential_move.py
# Timeline: use app_utils (play/stop/is_playing) instead of omni.timeline. Use app_utils.update_app(steps=N) instead of for-loop simulation_app.update(); same for other mobile_robot_controllers examples.

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test", action="store_true")
args, _ = parser.parse_known_args()

from isaacsim import SimulationApp

simulation_app = SimulationApp({"headless": False})

import isaacsim.core.experimental.utils.app as app_utils
import isaacsim.core.experimental.utils.stage as stage_utils
from isaacsim.core.experimental.objects import DomeLight
from isaacsim.core.simulation_manager import SimulationManager
from isaacsim.robot.experimental.wheeled_robots.controllers import DifferentialController
from isaacsim.robot.experimental.wheeled_robots.robots import WheeledRobot
from isaacsim.storage.native import get_assets_root_path

DEVICE = "cpu"

assets_root_path = get_assets_root_path()
if assets_root_path is None:
    raise RuntimeError("Could not find Isaac Sim assets folder")
jetbot_asset_path = assets_root_path + "/Isaac/Robots/NVIDIA/Jetbot/jetbot.usd"

stage_utils.set_stage_up_axis("Z")
stage_utils.set_stage_units(meters_per_unit=1.0)
stage_utils.add_reference_to_stage(
    usd_path=assets_root_path + "/Isaac/Environments/Grid/default_environment.usd",
    path="/World/ground",
)
dome_light = DomeLight("/World/DomeLight")
dome_light.set_intensities(500)

my_jetbot = WheeledRobot(
    paths="/World/Jetbot",
    wheel_dof_names=["left_wheel_joint", "right_wheel_joint"],
    usd_path=jetbot_asset_path,
    positions=[0.0, 0.0, 0.05],
)
my_controller = DifferentialController(wheel_radius=0.03, wheel_base=0.1125)

# Setup simulation and disable GPU dynamics for this example.
SimulationManager.setup_simulation(dt=1.0 / 60.0, device=DEVICE)
physics_scene = SimulationManager.get_physics_scenes()[0]
physics_scene.set_enabled_gpu_dynamics(False)
app_utils.play()
app_utils.update_app(steps=10)

# Simulation loop: apply [linear_speed, angular_speed]; e.g. 0.3 m/s, 1.0 rad/s.
linear_speed = 0.3
angular_speed = 1.0
step_count = 0
max_test_steps = 60
while simulation_app.is_running():
    simulation_app.update()
    step_count += 1
    if app_utils.is_playing():
        velocities = my_controller.forward([linear_speed, angular_speed])
        my_jetbot.apply_wheel_actions(velocities)
    if args.test and step_count >= max_test_steps:
        break

app_utils.stop()
simulation_app.close()
```

## Holonomic Controller

The holonomic controller computes the joint drive commands required on omni-directional robots to produce the commanded forward, lateral, and yaw speeds of the robot. An example of a holonomic robot is the NVIDIA Kaya robot.
The problem is framed as a quadratic program to minimize the residual “net force” acting on the center of mass.

Note

The wheel joints of the robot prim must have additional attributes to definine the roller angles and radii of the mecanum wheels.

```python
joint_prim = stage.GetPrimAtPath("/World/robot/wheel_joint")
joint_prim.CreateAttribute("isaacmecanumwheel:radius", Sdf.ValueTypeNames.Float).Set(0.12)
joint_prim.CreateAttribute("isaacmecanumwheel:angle", Sdf.ValueTypeNames.Float).Set(10.3)
```

The `HolonomicRobotUsdSetup` class automates this process.

### The Math

The cost funciton is defined as the control input to the robot joints. By minimizing the control inputs, excess acceleration and be reduced.

\[J = min(X^T \cdot X)\]

The equality constrains are set by the linear and angular target velocity Inputs:

\[ \begin{align}\begin{aligned}v\_{input} &= V^T \cdot X\\w\_{input} &= (V \times D\_{wheel dist to COM}) \cdot X\end{aligned}\end{align} \]

### OmniGraph Node

Holonomic Controller OmniGraph Inputs

| Input Commands | description |
| --- | --- |
| execIn | Input execution |
| wheelRadius | Array of wheel radius in meters |
| wheelPositions | Position of the wheel with respect to chassis’ center of mass in meters |
| wheelOrientations | Orientation of the wheel with respect to chassis’ center of mass frame |
| mecanumAngles | Angles of the mecanum wheels with respect to wheel’s rotation axis in radians |
| wheelAxis | The rotation axis of the wheels |
| upAxis | The up axis (default to z axis) |
| Velocity Commands for the vehicle | Velocity in x and y (m/s) and rotation (rad/s) |
| maxLinearSpeed | Maximum speed allowed for the vehicle in m/s |
| maxAngularSpeed | Maximum angular rotation speed allowed for the vehicles in rad/s |
| maxWheelSpeed | Maximum rotation speed allowed for the wheel joints in rad/s |
| linearGain | Gain for the linear velocity input |
| angularGain | Gain for the angular input |

Holonomic Controller OmniGraph Outputs

| Output Commands | description |
| --- | --- |
| jointVelocityCommand | Velocity command for the wheel joints in rad/s |

### Python

The code snippet below computes the joint velocity output for a three wheeled NVIDIA Kaya holonomic robot with command velocity of [1.0, 1.0, 0.1]

```python
# Reference: source/standalone_examples/api/isaacsim.robot.wheeled_robots.examples/kaya_holonomic_move.py

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test", action="store_true")
args, _ = parser.parse_known_args()

from isaacsim import SimulationApp

simulation_app = SimulationApp({"headless": False})

import isaacsim.core.experimental.utils.app as app_utils
import isaacsim.core.experimental.utils.stage as stage_utils
from isaacsim.core.experimental.objects import DomeLight
from isaacsim.core.simulation_manager import SimulationManager
from isaacsim.robot.experimental.wheeled_robots.controllers import HolonomicController
from isaacsim.robot.experimental.wheeled_robots.robots import (
    HolonomicRobotUsdSetup,
    WheeledRobot,
)
from isaacsim.storage.native import get_assets_root_path

DEVICE = "cpu"

assets_root_path = get_assets_root_path()
if assets_root_path is None:
    raise RuntimeError("Could not find Isaac Sim assets folder")
kaya_asset_path = assets_root_path + "/Isaac/Robots/NVIDIA/Kaya/kaya.usd"

stage_utils.set_stage_up_axis("Z")
stage_utils.set_stage_units(meters_per_unit=1.0)
stage_utils.add_reference_to_stage(
    usd_path=assets_root_path + "/Isaac/Environments/Grid/default_environment.usd",
    path="/World/ground",
)
# Add dome light to illuminate the whole environment (not just one spot)
dome_light = DomeLight("/World/DomeLight")
dome_light.set_intensities(500)

my_kaya = WheeledRobot(
    paths="/World/Kaya",
    wheel_dof_names=["axle_0_joint", "axle_1_joint", "axle_2_joint"],
    usd_path=kaya_asset_path,
    positions=[0.0, 0.0, 0.02],
    orientations=[1.0, 0.0, 0.0, 0.0],
)

# HolonomicRobotUsdSetup reads wheel geometry from USD for the controller.
kaya_setup = HolonomicRobotUsdSetup(
    robot_prim_path=my_kaya.paths[0],
    com_prim_path="/World/Kaya/base_link/control_offset",
)
(
    wheel_radius,
    wheel_positions,
    wheel_orientations,
    mecanum_angles,
    wheel_axis,
    up_axis,
) = kaya_setup.get_holonomic_controller_params()
my_controller = HolonomicController(
    wheel_radius=wheel_radius,
    wheel_positions=wheel_positions,
    wheel_orientations=wheel_orientations,
    mecanum_angles=mecanum_angles,
    wheel_axis=wheel_axis,
    up_axis=up_axis,
)

# Setup simulation and disable GPU dynamics for this example.
SimulationManager.setup_simulation(dt=1.0 / 60.0, device=DEVICE)
physics_scene = SimulationManager.get_physics_scenes()[0]
physics_scene.set_enabled_gpu_dynamics(False)
app_utils.play()
app_utils.update_app(steps=10)

# Simulation loop: apply [forward, lateral, yaw]; e.g. 1.0, 1.0, 0.1.
command = [1.0, 1.0, 0.1]
step_count = 0
max_test_steps = 60
while simulation_app.is_running():
    simulation_app.update()
    step_count += 1
    if app_utils.is_playing():
        velocities = my_controller.forward(command)
        my_kaya.apply_wheel_actions(velocities)
    if args.test and step_count >= max_test_steps:
        break

app_utils.stop()
simulation_app.close()
```

## Ackermann Controller

The Ackermann controller is commonly used for robots with steerable wheels, an example of steerable robot is the NVIDIA leatherback robot.
The Ackermann controller in Isaac Sim assumes the desired steering angle and linear velocity are provided, and based on the robot geometry

### The Math

Compute the steering angle offset between the left and right steering wheels:

\[ \begin{align}\begin{aligned}R\_{icr} &= \frac{l\_{wb}}{tan(\theta\_{steer})}\\\theta\_L &= \arctan[\frac{l\_{wb}}{R\_{icr} - 0.5 \* l\_{tw}}]\\\theta\_R &= \arctan[\frac{l\_{wb}}{R\_{icr} + 0.5 \* l\_{tw}}]\end{aligned}\end{align} \]

where \(R\_{icr}\) is the radius to the instantaneous center of rotation, \(\theta\_{steer}\) is the desired steering angle, \(l\_{wb}\) is the distance between rear and front axles (wheel base), \(l\_{tw}\) is the track width

Compute the individual wheel velocities (Forward steering case):

First step is to find the distance between the wheels and the instantaneous center of rotation.

\[ \begin{align}\begin{aligned}D\_{front} &= \sqrt{ (R\_{icr} \pm 0.5 l\_{tw})^2 + (l\_{wb})^2 }\\D\_{rear} &= R\_{icr} \pm 0.5 l\_{tw}\end{aligned}\end{align} \]

Note

for \(\pm\), use \(-\) for the wheel closer to the \(R\_{icr}\) and \(+\) for the wheel further to the \(R\_{icr}\)

Then desired wheel velocity can be computed

\[ \begin{align}\begin{aligned}\omega\_{front} &= \frac{V\_{desired}}{R\_{icr}} \cdot \frac{D\_{front}}{r\_{front}}\\\omega\_{rear} &= \frac{V\_{desired}}{R\_{icr}} \cdot \frac{D\_{rear}}{r\_{rear}}\end{aligned}\end{align} \]

Where \(V\_{desired}\) is the desired linear velocity, \(r\_{front}\) is the desired front wheel radius, and \(r\_{rear}\) is the desired rear wheel radius.

### OmniGraph Node

Ackermann Controller OmniGraph Inputs

| Input Commands | description |
| --- | --- |
| execIn | Input execution |
| acceleration | Desired forward acceleration for the robot in m/s^2 |
| speed | Desired forward speed in m/s |
| steeringAngle | Desired steering angle in radians, by default it is positive for turning left for a front wheel drive |
| currentLinearVelocity | Current linear velocity of the robot in m/s |
| wheelBase | Distance between the front and rear axles of the robot in meters |
| trackWidth | Distance between the left and right rear wheels of the robot in meters |
| turningWheelRadius | Radius of the front wheels of the robot in meters |
| maxWheelVelocity | Maximum angular velocity of the robot wheel in rad/s |
| invertSteeringAngle | Flips the sign of the steering angle, Set to true for rear wheel steering |
| useAcceleration | Use acceleration as an input, Set to false to use speed as input instead |
| maxWheelRotation | Maximum angle of rotation for the front wheels in radians |
| dt | Delta time for the simulation step |

Ackermann Controller OmniGraph Outputs

| Output Commands | description |
| --- | --- |
| execOut | Output execution |
| leftWheelAngle | Angle for the left turning wheel in radians |
| rightWheelAngle | Angle for the right turning wheel in radians |
| wheelRotationVelocity | Angular velocity for the turning wheels in rad/s |

### Python

The python snippet below creates an Ackermann controller for a NVIDIA Leatherback robot with a wheel base of 1.65m, track width of 1.25m, and wheel radius of 0.25m, sending it a desired forward velocity of 1.1 m/s and steering angle of 0.1 rad.

```python
# Ackermann steering example using the experimental API (no core World).
# Uses Articulation from core.experimental.prims and AckermannController from
# isaacsim.robot.experimental.wheeled_robots.

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test", action="store_true")
args, _ = parser.parse_known_args()

from isaacsim import SimulationApp

simulation_app = SimulationApp({"headless": False})

import isaacsim.core.experimental.utils.app as app_utils
import isaacsim.core.experimental.utils.stage as stage_utils
from isaacsim.core.experimental.objects import DomeLight
from isaacsim.core.experimental.prims import Articulation
from isaacsim.core.simulation_manager import SimulationManager
from isaacsim.robot.experimental.wheeled_robots.controllers import AckermannController
from isaacsim.storage.native import get_assets_root_path

DEVICE = "cpu"

assets_root_path = get_assets_root_path()
if assets_root_path is None:
    raise RuntimeError("Could not find Isaac Sim assets folder")
leatherback_asset_path = assets_root_path + "/Isaac/Robots/NVIDIA/Leatherback/leatherback.usd"
leatherback_prim_path = "/World/Leatherback"

stage_utils.set_stage_up_axis("Z")
stage_utils.set_stage_units(meters_per_unit=1.0)
stage_utils.add_reference_to_stage(
    usd_path=assets_root_path + "/Isaac/Environments/Grid/default_environment.usd",
    path="/World/ground",
)
dome_light = DomeLight("/World/DomeLight")
dome_light.set_intensities(500)
stage_utils.add_reference_to_stage(usd_path=leatherback_asset_path, path=leatherback_prim_path)

my_leatherback = Articulation(leatherback_prim_path)

# Steering joints (position control) and wheel joints (velocity control)
steering_joint_names = [
    "Knuckle__Upright__Front_Left",
    "Knuckle__Upright__Front_Right",
]
wheel_joint_names = [
    "Wheel__Knuckle__Front_Left",
    "Wheel__Knuckle__Front_Right",
    "Wheel__Upright__Rear_Left",
    "Wheel__Upright__Rear_Right",
]

steering_dof_indices = my_leatherback.get_dof_indices(steering_joint_names)
wheel_dof_indices = my_leatherback.get_dof_indices(wheel_joint_names)

wheel_base = 1.65
track_width = 1.25
wheel_radius = 0.25
desired_forward_vel = 1.1  # m/s
desired_steering_angle = 0.1  # rad
acceleration = 0.0
steering_velocity = 0.0
dt = 0.0

controller = AckermannController(
    wheel_base=wheel_base,
    track_width=track_width,
    front_wheel_radius=wheel_radius,
    back_wheel_radius=wheel_radius,
)
# Command: [steering_angle, steering_angle_velocity, speed, acceleration, dt]
joint_positions, joint_velocities = controller.forward(
    [desired_steering_angle, steering_velocity, desired_forward_vel, acceleration, dt]
)

# Setup simulation and disable GPU dynamics for this example.
SimulationManager.setup_simulation(dt=1.0 / 60.0, device=DEVICE)
physics_scene = SimulationManager.get_physics_scenes()[0]
physics_scene.set_enabled_gpu_dynamics(False)
app_utils.play()
app_utils.update_app(steps=10)

# Simulation loop: apply steering positions and wheel velocities.
step_count = 0
max_test_steps = 60
while simulation_app.is_running():
    simulation_app.update()
    step_count += 1
    if app_utils.is_playing() and joint_positions is not None and joint_velocities is not None:
        my_leatherback.set_dof_position_targets(
            joint_positions,
            dof_indices=steering_dof_indices,
        )
        my_leatherback.set_dof_velocity_targets(
            joint_velocities,
            dof_indices=wheel_dof_indices,
        )
    if args.test and step_count >= max_test_steps:
        break

app_utils.stop()
simulation_app.close()
```

On this page

* [Differential controller](#differential-controller)
  + [The Math](#the-math)
  + [OmniGraph Node](#omnigraph-node)
  + [Python](#python)
* [Holonomic Controller](#holonomic-controller)
  + [The Math](#id1)
  + [OmniGraph Node](#id2)
  + [Python](#id3)
* [Ackermann Controller](#ackermann-controller)
  + [The Math](#id4)
  + [OmniGraph Node](#id5)
  + [Python](#id6)

---

### Surface Gripper

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/robot_simulation/ext_isaacsim_robot_surface_gripper.html

* [Robot Simulation](index.html)
* Surface Gripper Extension

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Surface Gripper Extension

## About

The [Surface Gripper Extension](#isaac-surface-grippers) is used to create a suction cup-style gripper for an end-effector. It works by parsing the Surface Gripper properties on the USD Surface Gripper Schema, and managing a set of D6 joints between the parent and child rigid bodies at points of contact.

The physical properties of the gripper are defined within the D6 joint, such as joint limits across the different degrees of freedom, and the stiffness and damping of the joint. The Surface Gripper object then handles the activation of the constraints, and defines which objects are grasped based on the grip threshold.

This extension is enabled by default. If it is ever disabled, it can be re-enabled from the [Extension Manager](https://docs.omniverse.nvidia.com/extensions/latest/ext_core/ext_extension-manager.html "(in Omniverse Extensions)") by searching for `isaacsim.robot.surface_gripper` and `isaacsim.robot.surface_gripper.ui`.

To create a surface gripper through the GUI, go to the menu `Create` > `Robots` > `Surface Gripper`. This will create a surface gripper prim in the stage.

## API Documentation

See the [API Documentation](../py/source/extensions/isaacsim.robot.surface_gripper/docs/index.html) for usage information.

## Setting up a Surface Gripper

The Surface Gripper has the following properties:

| Property | Description |
| --- | --- |
| Attachment Points | The list of joints that will be used to attach the gripper to the object |
| Status | (Read-Only) The current state of the gripper |
| Gripped Objects | (Read-Only) The list of objects that are currently grasped by the gripper |
| Max Grip Distance | Distance from the gripper point within which closing contact is accepted |
| Retry Interval | How long the gripper will keep attempting to close on an object |
| Shear Force Limit | The maximum lateral force that the gripper can apply to an object before it will break the constraint |
| Coaxial Force Limit | The maximum axial force that the gripper can apply to an object before it will break the constraint |

### Attachment Joints

The joints that are used to attach the gripper to the object are defined by the `Attachment Points` property within the Surface Gripper Schema. This is a list of paths to the D6 joints that will be used to attach the gripper to the object. These joints must be defined in the USD file at the gripper points of contact, and must be of type `D6`. Any physical properties for the joint are defined in the D6 Joint Schema, but there are a few properties that are required to be set for the joint:

* Joint must be enabled.
* For all joints, Body 0 must be the same.
* Joint must have “Exclude from Articulation” set to True. If this is not set, the surface gripper manager will set it to True at runtime.

### Attachment Point API

The joints that are defined by the `Attachment Points` property are automatically assigned the `Attachment API`. This API is responsible for providing additional attributes to the joint, which are necessary for the Surface Gripper Manager to handle the gripper. In the Attachment Point API, the following attributes are available:

* `Clearance Offset`: This registers the distance from the joint to the parent object’s surface. Since the surface gripper works by sending a raycast from the joint world position, this offset will be added to the raycast origin to avoid false positive hits with the parent object. If this offset is not defined, the raycast will start at the joint’s world position, and the gripper will automatically calculate and save the offset the first time it clears the parent object collider.
* `Forward Axis`: This registers which joint axis will be used to attempt to close the gripper. The default value is `X`.

These additional attributes can be found within the Raw USD Properties section of the Property tab.

#### Adding Attachment Joint API

To add an attachment joint API, select the joint in the stage. In the right panel under the **Properties** tab, click the **+ Add** button and navigate to **Isaac** > **Robot Schema** > **Attachment Point API**.

**+ Add** > **Isaac** > **Robot Schema** > **Attachment Point API** in the Property tab.

Note

The Attachment Point API is automatically applied to the joint when the Surface Gripper is created. It does not need to be added manually.

## Omniverse OmniGraph Node

The Surface Gripper extension provides an implementation through Omniverse OmniGraph. To use it, add a surface gripper node to the desired graph, and select the surface gripper prim it will control.

The following inputs are available:

* **Close**: Closes the gripper. If the gripper is already closed, this will do nothing.
* **Open**: Opens the gripper. If the gripper is already open, this will do nothing.
* **Toggle**: Toggles the gripper between open and closed states.
* **Enabled**: Enables or disables the gripper.
* **Surface Gripper**: The surface gripper prim to control.

Surface Gripper node in the graph editor.

## Creating a Surface Gripper fully in code

This section describes how to implement a surface gripper completely from code. These are snippets from the Surface Gripper Example code, and are not complete.

### Defining the Surface Gripper Properties

```python
import usd.schema.isaac.robot_schema as robot_schema
from isaacsim.robot.surface_gripper import _surface_gripper as surface_gripper

gripper_prim_path = "/World/SurfaceGripper"
gripper_interface = surface_gripper.acquire_surface_gripper_interface()

# Create the Surface Gripper Prim
# Once it is created it can be saved and this doesn't need to be redone
robot_schema.CreateSurfaceGripper(stage, gripper_prim_path)
gripper_prim = stage.GetPrimAtPath(gripper_prim_path)
attachment_points_rel = gripper_prim.GetRelationship(robot_schema.Relations.ATTACHMENT_POINTS.name)

# Select the joints to the gripper
# The joints should be D6 joints defined in the usd file.
# All joint attributes can be defined as desired, except for:
# Joint Should be enabled
# Joint Type should be D6
# All Joint Parents should be the same Rigid body
# Exclude from Articulation must be checked
# No Break force/Torque should be set
# Joint drives can be used to derive the desired joint bounce/stretch behavior
# Enable/Disable the joint DoFs and limits as desired.

gripper_joints = [p.GetPath() for p in stage.GetPrimAtPath("/World/Surface_Gripper_Joints").GetChildren()]
attachment_points_rel.SetTargets(gripper_joints)

# Define the distance the joint can grasp, and at what distance from the origin of the joints it will settle
gripper_prim.GetAttribute(robot_schema.Attributes.MAX_GRIP_DISTANCE.name).Set(0.011)
# Define the Override Break limits
gripper_prim.GetAttribute(robot_schema.Attributes.COAXIAL_FORCE_LIMIT.name).Set(0.005)
gripper_prim.GetAttribute(robot_schema.Attributes.SHEAR_FORCE_LIMIT.name).Set(5)

# How long the gripper will try to close if it is open
gripper_prim.GetAttribute(robot_schema.Attributes.RETRY_INTERVAL.name).Set(1.0)
```

### Get Gripper State

The Surface Gripper is updated on every simulation step, and the state can be retrieved at any time through the interface:

```python
status = gripper_interface.get_gripper_status(gripper_prim_path)
print(status)  # Open, Closed, or Closing
```

### Controlling the Gripper

The Gripper State is controlled through the `open` and `close` methods of the interface. Alternatively, there’s also the `set_gripper_action` method, which receives a numeric value between -1 and 1, where `< -0.3` will open the gripper, `> 0.3` will close it, and anything in between will be ignored.

```python
gripper_interface.close_gripper(gripper_prim_path)

gripper_interface.open_gripper(gripper_prim_path)

gripper_interface.set_gripper_action(gripper_prim_path, 0.5)  # Closes the gripper
gripper_interface.set_gripper_action(gripper_prim_path, -0.5)  # Opens the gripper
```

### Keeping USD Scene in Sync

In order to optimize the Surface Gripper Update performance, the USD Scene update is disabled by default. When the USD writeback is disabled, the Properties panel for the Surface Gripper prim will not be updated automatically. The surface gripper status can still be retrieved through the `get_gripper_status` method of the surface gripper interface, and objects currently grasped by the gripper can be retrieved through the `get_gripped_objects` method of the surface gripper interface.

The USD writeback can be enabled by setting the `set_write_to_usd` property to `True` on the Surface Gripper interface. This is a global setting for all surface gripper instances.

## Tutorials & Examples

Activate the `Robotics Examples` content browser from **Windows** > **Examples** > **Robotics Examples**. Navigate to **Manipulation**, select the Surface Gripper Example, and click the load button in the information window on the right side of the Robotics Examples content browser. You may need to adjust the GUI to see the load button.

### Surface Gripper Example (gantry)

This example shows a surface gripper mounted to a gantry, and contains cubes that can be grasped by the gripper. This surface gripper is added by code, and also connected through the surface gripper Omniverse OmniGraph node.

To run the example:

1. Press the **Load** button. The scene should begin playing.
2. You can move the gantry with the gamepad axes, or by manually editing the gantry joint target positions.
3. Move the gantry near some cube or set of cubes, and click on the “Open/Close” button - the button label reflects the current gripper state. The gripper can also be closed by the down face button on the gamepad (e.g. X on PlayStation controllers, or A on Xbox controllers).
4. The gripper will attempt to close on the cubes, and if successful, the cubes will be grasped by the gripper.
5. Lift the gantry. The cubes remain grasped by the gripper unless forces are excessive, in which case the gripper constraint may break.

## Walkthrough

This walkthrough demonstrates how to attach a simple suction-style end effector to a UR10 robot arm, and how to use the Surface Gripper extension to control the gripper. The pick-and-stack sequence is driven by differential inverse kinematics.

### Learning Objectives

In this example, you:

* Attach a suction-style end effector built from simple primitives to a UR10.
* Configure a D6 joint with IsaacAttachmentPointAPI, limits, and drives for the Surface Gripper.
* Add a Surface Gripper prim whose **Attachment Points** reference that joint.
* Run a pick-and-stack sequence using the Surface Gripper.

### Getting Started

**Prerequisite**

* Comfortable with the stage tree and **Property** tab in Isaac Sim, or completion of [Tutorial 2: Assemble a Simple Robot](../robot_setup_tutorials/tutorial_intro_assemble_robot.html#isaac-sim-app-tutorial-intro-assemble-robot).

### Create the Surface Gripper Geometry

1. Go to **File** > **New** to start an empty stage.
2. In the Content Browser, open **Isaac Sim** > **Robots** > **Universal Robots** > **ur10**, then drag `ur10.usd` into the viewport. Zero out the translation and rotation of the UR10 so it is centered in the stage.
3. In the Stage tree, expand `/World/ur10` and find the Xform `ee_link`. You will attach the gripper visuals and the Surface Gripper to this link so they move with the wrist.

**Add cylinder geometry under** `ee_link`

Use three **Cylinder** prims (**Create** > **Shape** > **Cylinder**). For each cylinder, parent it under `ee_link`, rename them and set **Translate**, **Orient** (degrees), and **Scale** in the **Property** tab according to the table below.

| Prim name | Translate | Orient (degrees) | Scale (X, Y, Z) |
| --- | --- | --- | --- |
| `base` | `(0.05, 0, 0)` | `(0, 90, 0)` | `(0.075, 0.075, 0.1)` |
| `tube` | `(0.125, 0, 0)` | `(0, 90, 0)` | `(0.025, 0.025, 0.05)` |
| `suction_cup` | `(0.15, 0, 0)` | `(0, 90, 0)` | `(0.075, 0.075, 0.015)` |

You can add material properties to the cylinders to make them look more realistic.

UR10 with `base`, `tube`, and `suction_cup` parented under `ee_link`.

### Create the D6 Joint and AttachmentPointAPI

Under `ee_link` create a new Xform named `surface_gripper`. Then add a **D6** joint prim to it named `suction_joint` by clicking **Create** > **Physics** > **Joints > D6**. Configure the joint properties as shown below. Note that **Exclude from Articulation** should be checked.

D6 joint `suction_joint` located at the tip of the gripper.

Joint properties for `suction_joint`.

**Configure the D6 joint**

The D6 joint exposes six degrees of freedom that can be configured independently. To simulate suction-cup compliance, you can set linear limits along the suction direction so the cup can sag or compress under load, and rotational limits so the grasped object can bend or twist at the contact point. Higher stiffness produces a stiffer grasp and adding damping prevents oscillation. Together these let you model elastic deformation without true soft-body physics.

In this example, we add small limits of about -5 to 5 degrees for each rotation axis and 0.01 meters for the Z axis limit to allow for some compliance along the gripper’s normal axis. Additionally, add a `Z Axis Translation Drive` by clicking **+ Add > Physics > Z Axis Translation Drive**. Set the `Stiffness` to `1000` and the `Damping` to `100`. These values can be tuned for your specific application.

**AttachmentPointAPI on** `suction_joint`

Note

The **AttachmentPointAPI** is automatically applied to the joint when a Surface Gripper prim is created (see next section). Below is the explicit method. See [Adding Attachment Joint API](#adding-attachment-joint-api) for additional details.

1. Select `suction_joint`. In the **Property** tab, click **+ Add** > **Isaac** > **Robot Schema** > **Attachment Point API** to apply it.
2. Confirm the new attributes in the **Property** tab under **Attachment Point**.
3. Set **Forward Axis** in the **Attachment Point** section to `Z` to align the suction direction with the gripper.

### Add the Surface Gripper Prim

The Surface Gripper prim is used to control the suction action of the gripper. You can create it in the UI or via Python. An OmniGraph node can be used to control the gripper from a graph.

GUI

1. Right-click `ee_link` in the **Stage Tree**, choose **Create** > **Isaac** > **Robots** > **Surface Gripper**.
2. If the new prim is not under `ee_link`, drag it so it is parented under `ee_link`.
3. Select the Surface Gripper prim. Set **Max Grip Distance** to `0.01`.
4. Set **Attachment Points** to the stage path of the D6 joint you created earlier (`suction_joint`).

You can leave **Retry Interval**, **Shear Force Limit**, and **Coaxial Force Limit** at their defaults until something needs tuning. If the grasp releases too easily or never holds, adjust those fields (see the property table under [Setting up a Surface Gripper](#isaac-surface-grippers-tutorials)).

Stage hierarchy under `ee_link`: gripper cylinders, `surface_gripper` / `suction_joint`, and the Surface Gripper prim.

Code

After the previous sections are complete, run the following from the **Script Editor**. It mirrors the GUI tab: it will create the prim under `ee_link`, set **Attachment Points** to `suction_joint`, and set **Max Grip Distance** to `0.01`.

```python
# Create and configure a Surface Gripper prim under ee_link (same outcome as the GUI tab).
# Run with the Isaac Sim stage loaded; paths must match your robot and suction_joint from the walkthrough.

import omni.usd
import usd.schema.isaac.robot_schema as robot_schema
from isaacsim.robot.surface_gripper import create_surface_gripper
from pxr import Sdf

stage = omni.usd.get_context().get_stage()

# Parent Xform for the tool (same as in the walkthrough when the robot lives under /World/ur10).
ee_link_path = "/World/ur10/ee_link"
# D6 joint configured earlier under surface_gripper (see walkthrough).
suction_joint_path = f"{ee_link_path}/surface_gripper/suction_joint"

# Create a SurfaceGripper prim under ee_link using the convenience function.
gripper_prim = create_surface_gripper(stage, ee_link_path)

# **Attachment Points** → suction_joint
attachment_points_rel = gripper_prim.GetRelationship(robot_schema.Relations.ATTACHMENT_POINTS.name)
attachment_points_rel.SetTargets([Sdf.Path(suction_joint_path)])

# **Max Grip Distance** = 0.01 (defaults for retry / force limits match the GUI until you tune them)
gripper_prim.GetAttribute(robot_schema.Attributes.MAX_GRIP_DISTANCE.name).Set(0.01)
```

`create_surface_gripper` is the same function the UI uses when you pick **Create** > **Isaac** > **Robots** > **Surface Gripper**; it picks a free prim name such as `SurfaceGripper` or `SurfaceGripper_01`. For lower-level control, call `robot_schema.CreateSurfaceGripper` directly — see [Creating a Surface Gripper fully in code](#isaac-surface-grippers-code-snippets).

OmniGraph

Ensure you’ve either completed the **GUI** or **Code** tab first. A Surface Gripper can’t be created in an OmniGraph, but it can be controlled by logic within a graph. As shown below, the **Surface Gripper** node can be used to toggle the gripper between open and closed states and entirely enable/disable the gripper.

1. Open **Window** > **Graph Editors** > **Action Graph** and choose **New Action Graph**.
2. In the graph search field, find **Surface Gripper** and add it to the graph.
3. Select the **Surface Gripper** node. In the property panel, set the **SurfaceGripper** target to the prim path you created earlier; for example `/World/ur10/ee_link/SurfaceGripper`.
4. To drive **Toggle** from the keyboard, add a **On Keyboard Input** node. As seen in the **Property** tab, **A** is the default key that can now be used to toggle the gripper when physics simulation is playing. Try this when running the stacking example below.

**Surface Gripper** node. See also [Omniverse OmniGraph Node](#isaac-surface-grippers-omnigraph).

### Save the customized robot

The stacking demo references your USD at `/World/robot`, so the robot must be the USD’s **Default Prim**
and must live at the root of the file — not nested under a `/World` scope.

1. In the Stage tree, drag `/World/ur10` to the root so it becomes `/ur10`.
2. Right-click `/ur10` and choose **Set as Default Prim**.
3. Delete the now-empty `/World` and `/Environment` Xforms.
4. Save the stage as a USD file.

### Run the Demo

**Run with the packaged UR10**

Isaac Sim is packaged with a UR10 USD file that includes a Surface Gripper prim and the necessary joints to control the gripper. Here we demonstrate a working pick-and-stack sequence with the packaged UR10. The example picks up two cubes and stacks them using the Surface Gripper.

From the **Isaac Sim** install folder (where `python.sh` lives), run:

```python
./python.sh standalone_examples/api/isaacsim.robot.experimental.manipulators/universal_robots/stacking.py
```

This uses the stock UR10 USD so you can confirm the script and pick-and-stack sequence before you substitute your file.

Pick-and-stack with the **original** packaged UR10.

**Run with your saved USD**

Pass the USD file you saved earlier to the `--usd-path` argument:

```python
./python.sh standalone_examples/api/isaacsim.robot.experimental.manipulators/universal_robots/stacking.py --usd-path /path/to/your/ur10_custom.usd
```

Use the real path to your USD. The sample expects the Surface Gripper and joint layout from this walkthrough; if your prim paths or articulation root differ from the defaults, update the script to match.

The same demo using the **custom** cylinder gripper and Surface Gripper setup.

On this page

* [About](#about)
* [API Documentation](#api-documentation)
* [Setting up a Surface Gripper](#setting-up-a-surface-gripper)
  + [Attachment Joints](#attachment-joints)
  + [Attachment Point API](#attachment-point-api)
    - [Adding Attachment Joint API](#adding-attachment-joint-api)
* [Omniverse OmniGraph Node](#omnigraph-node)
* [Creating a Surface Gripper fully in code](#creating-a-surface-gripper-fully-in-code)
  + [Defining the Surface Gripper Properties](#defining-the-surface-gripper-properties)
  + [Get Gripper State](#get-gripper-state)
  + [Controlling the Gripper](#controlling-the-gripper)
  + [Keeping USD Scene in Sync](#keeping-usd-scene-in-sync)
* [Tutorials & Examples](#tutorials-examples)
  + [Surface Gripper Example (gantry)](#surface-gripper-example-gantry)
* [Walkthrough](#walkthrough)
  + [Learning Objectives](#learning-objectives)
  + [Getting Started](#getting-started)
  + [Create the Surface Gripper Geometry](#create-the-surface-gripper-geometry)
  + [Create the D6 Joint and AttachmentPointAPI](#create-the-d6-joint-and-attachmentpointapi)
  + [Add the Surface Gripper Prim](#add-the-surface-gripper-prim)
  + [Save the customized robot](#save-the-customized-robot)
  + [Run the Demo](#run-the-demo)

---

### Grasp Editor

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/robot_simulation/grasp_editor.html

* [Robot Simulation](index.html)
* Grasp Editor

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Grasp Editor

## Learning Objectives

This tutorial explains how to use the Grasp Editor extension in NVIDIA Isaac Sim to hand-author and
simulate grasps for a specific gripper/object pair. These grasps are stored in an isaac\_grasp
YAML file that can be imported and used with a motion generation algorithm to move the gripper into
place and grasp the desired object.

## Getting Started

To get started using the Grasp Editor extension, you need to prepare your assets in NVIDIA Isaac Sim.

* You must have an Articulation capable of grasping. This can be a floating gripper, or it can be a gripper attached to an arm.
* You must have a USD version of the object you want to grasp.

For both the gripper and the object, you must be ready to identify the USD frame that should be used to
represent location. This is often the frame in the center of the object mesh and at the base of the gripper.

You can download the stage used in this tutorial
[`here`](../_downloads/4d1aeb9e29208ad4bf35f0a38d105e49/Grasp_Editor_Tutorial_Stage.zip)
and follow along.

After downloading, extract the archive. In your running NVIDIA Isaac Sim instance,
click **File > Open** and select the `grasp_editor_tutorial.usd` file.

## What is an Isaac Grasp File?

The output of the Grasp Editor extension is a YAML in the isaac\_grasp file format. A single isaac\_grasp
file stores a list of grasps for a specific gripper/object pair. The file follows a simple format:

```python
 1format: isaac_grasp
 2format_version: 1.0
 3
 4object_frame: /World/mug
 5gripper_frame: /World/panda_hand
 6
 7grasps:
 8  grasp_0:
 9      confidence: 1.0
10      position: [-0.04346, 0.06759, 0.19895]
11      orientation: {w: 0.00332, xyz: [0.98453, 0.16837, 0.04837]}
12      cspace_position:
13        panda_finger_joint1: 0.00943
14      pregrasp_cspace_position:
15        panda_finger_joint1: 0.04
```

isaac\_grasp files do not need to originate with the Grasp Editor extension. The Grasp Editor
extension is useful for both authoring isaac\_grasp files and importing grasps that were authored
elsewhere for visualization and validation.

A grasp is defined by the relative position of the gripper and object. In order for this relative
position to have meaning, a representative frame must be chosen for the gripper and object positions.
The Grasp Editor handles these frames in two distinct ways:

* On export, the USD paths of the representative frames are written to the isaac\_grasp file
  under the object\_frame and gripper\_frame fields.
* On import, the object\_frame and gripper\_frame fields are ignored, because isaac\_grasp
  files may be authored externally (possibly without going through USD at all).
* As a result, identifying the correct USD frames is the user’s responsibility when using the
  Grasp Editor for importing.

Each grasp in an isaac\_grasp file has a unique name (e.g. grasp\_0). The fields for a named
grasp are:

* confidence: A parameter describing the quality of a grasp.
* position: The translation of the gripper frame relative to the object frame.
* orientation: The orientation of the gripper frame relative to the object frame.
* cspace\_position: A dictionary of joint positions for every joint that is used to control the gripper.
  These joint positions are the state of the gripper as it is actively grasping the object.
* pregrasp\_cspace\_position: A dictionary of joint positions for every joint that is used to control the gripper.
  These joint positions represent the open position of the gripper.

All together, a grasp may be applied in practice by moving the gripper to the correct relative position and orientation
while in the pregrasp\_cspace\_position, then closing the gripper until the joints are in cspace\_position.
If the object’s position and orientation in the world frame of reference is given by \(T\_o, R\_o\), with
the position and orientation fields specifying relative transformation \(^oT\_g, ^o\!\!R\_g\)
(i.e. the translation and rotation of the gripper according to the object frame of reference),
the desired position of the gripper in the world frame \(T\_g , R\_g\) is given by:

\[\begin{split}T\_g = R\_o \cdot {^oT\_g + T\_o} \\
R\_g = R\_o \cdot {^o\!R\_g}\end{split}\]

## Using the Grasp Editor

### Selection Frame

The Grasp Editor is a UI-based extension that can be used to author and import isaac\_grasp files.
In NVIDIA Isaac Sim, the Grasp Editor can be found in the toolbar under **Tools** > **Robotics** > **Grasp Editor**.
The first step is to add an Articulation and an object to the stage. The Articulation may be an
isolated gripper, or it may be a gripper attached to a robot arm. The object can be any
non-Articulation that has an associated mesh.

To fill in the Selection Frame:

1. Select the Articulation and object of interest. The prim path for the object can be copied by
   right clicking on the desired prim and selecting “Copy Prim Path”.
2. Choose an export path for the isaac\_grasp file. This should end in ‘.yaml’.

A few rules apply to the export file:

* The Grasp Editor may be used to author a sequence of grasps to the selected export file, but
  it does not support modifying an existing file.
* If an export path is supplied that already exists, the existing file will be overwritten with a
  new isaac\_grasp file.

This tutorial will author grasps between the Panda hand gripper (isolated from the Franka Emika Panda
robot) and a mug. When “Ready” is clicked, the Grasp Editor will:

* Validate each field in the panel.
* Perform all necessary conversions of the selected object prim (the mug) to make it graspable.
  Specifically, it applies the Rigid Body and Collision APIs from Usd Physics so that the object has
  a collision geometry and can be moved by external forces.

Note

The Grasp Editor does not revert these changes to the object asset, and so it is best not to save the USD stage unless these changes are specifically desired.

Warning

There is a known issue that the mug may “disappear”, this is a visual bug. You can press “STOP”, then “PLAY” again to make it reappear.

### Select Frames of Reference

In this panel, you may select the frames of reference that should be used to describe the position
in space of the gripper and object. It is critical to understand this panel and to make the proper
selections before moving on.

Most motion generation algorithms do not natively consume USD files. It is common for motion generation
algorithms to reference a URDF file. If the Grasp Editor
uses a frame that is not defined in a corresponding URDF file, an authored grasp becomes meaningless from the
perspective of any such motion generation algorithms.

Similarly, the selected frame of reference for the object
must correspond to the existing pipeline in which the object is being manipulated. For example, if a
camera is being used to identify object pose, there is an implicit frame of reference for the object
associated with that vision system. In this case, the selected frame for the object must correspond to this
implicit frame of reference. If there is not already a frame in the USD that represents the correct frame of
reference, a new one should be authored on the stage under the selected object path (e.g. nested under “/World/mug”).

In this tutorial, the base frames for the gripper and object are used. If the entire Franka Panda robot
were being used, the correct frame of reference for the gripper would still be the panda\_hand frame.
Once “Finalize” is clicked, these frames of reference become global to the output isaac\_grasp file and
cannot be changed.

**The Grasp Editor will write the USD paths for the frames of reference to the output isaac\_grasp file,
but this information will not be interpretable by a motion generation algorithm that does not consume USD.**

### Joint Settings

In this menu, you must select which joints in the Articulation are active degrees of freedom (DOFs) in
the gripper. The Panda hand is a two finger gripper, but one of the joints is a mimic joint. Observe
in the figure below that changing the value of panda\_finger\_joint1 causes panda\_finger\_joint\_2 to
move at the same time. This means that the Panda hand gripper is effectively controlled by a single DOF.

Each active DOF in the gripper should be checked as “Part of Gripper”. This will open a new menu of
joint settings that define how the grasp will be simulated and what gets written to the output isaac\_grasp file.

* Position When Open: The position of DOF that is considered to be open. Each grasp will be simulated
  by moving from the open position towards the closed position.
* Position When Closed: The position of the DOF that is considered to be fully closed.
* Grasp Speed: The speed at which the DOF will move from the open position towards the closed position when simulating.
* Max Effort Magnitude: The maximum force/torque (N or N\*m) that this DOF will be able to apply on the object when simulating.

At least one DOF must be marked as part of the Gripper in order to author a grasp. Only active gripper DOFs will
be written to the output isaac\_grasp file.

### Utils

The Utils menu has two useful utility functions that assist in using the Grasp Editor.

The Mask Collision button will mask collisions between the gripper and object. This may be helpful
when moving the object into place in order to test a grasp. Masked collisions are unmasked when a grasp
is simulated. When importing a grasp, collisions are masked automatically.

If the simulated grasp does not appear to have complete contact between the object and gripper,
you can use the “Show Physics Colliders” button to visualize the collision geometry associated
with your assets. It is outside of the scope of this extension to fix incorrect collider geometry,
but the Grasp Editor does allow you to author grasps without simulating them. In this situation
you can mask collisions and move things into place visually.

### Author a Grasp

A grasp may be authored with the aid of simulation, since moving assets by hand into what appears to
be the right position is imprecise. The figure below demonstrates the simulated authoring workflow:

1. Move the object into roughly the right position to be grasped.
2. Click the “Simulate” button to close the gripper according to its joint settings. In the figure,
   this causes the lip of the mug to be pushed into the exact center of the gripper fingers and leaves
   the gripper fingers in the exact position of contact with the object.
3. Once the simulation is complete, the export panel will populate, and the grasp may be written
   to file.

Letting the simulation settle the contact in this way gives a high degree of confidence to the grasp
that is written to the output file.

There may be reasons that the grasp simulation does not support your use-case such as:

* The physics colliders for your assets are not accurate.
* The mechanics for opening and closing the gripper are more complicated than is represented in the Grasp Editor.

In either case, the best way to make use of the Grasp Editor is to move things into place through
external means and export the grasp without simulating by clicking the “Skip Sim” button. For example,
some real robot grippers have heavily coupled degrees of freedom with somewhat complicated mechanics.
For such a gripper, you would want to replicate the exact movement programmatically and send joint
commands to the USD asset accordingly. In this case, you could turn on collisions and use an external
script or OmniGraph node to drive your gripper into a grasping position, then use the export function of the
Grasp Editor to export the current state of grasp on the USD stage to your isaac\_grasp file.

#### Adding External Forces and Torques

An extra feature of the Grasp Editor is that you can apply external forces and torques as part of the
grasp simulation. This may help to discern which grasps have the best force closure over the object.
The amount of force and torque applied may be selected in the “Add External Rigid Body Forces” panel.
A single scalar value may be chosen for force and for torque. A non-zero value \(v\) for force will cause
a force of \(\pm v\) N along each axis, centered at the base frame of the rigid body.
Likewise for torque, a value \(v\) will cause a torque of \(\pm v\) N\*m to be applied about each axis, centered
at the base frame of the rigid body.

The figure below demonstrates closing the grasp and then applying forces of 3 N. This test fails
when the mug flies away under a force of \([3, 0, 0]\). A smaller force value of 0.5 N is then
chosen, and the mug moves under the force, but the grasp is maintained.

### Exporting Grasps

The export frame becomes available once a grasp has been fully simulated, or the option to simulate has been declined.
On clicking “Export”, the current state of the stage is used to fill in the relevant fields of the
isaac\_grasp file.

* The confidence field takes on the value of the “Confidence” field in the Export panel.
* The position and orientation fields for the grasp are determined by finding the relative position
  of the gripper in the object’s frame of reference. This uses the frames defined in
  [Select Frames of Reference](#isaac-sim-app-tutorial-grasp-editor-reference-frames).
* The cspace\_position field is determined based on the current positions of the DOFs that have been marked as
  part of the gripper.
* The pregrasp\_cspace\_position field is taken from the “Position When Open” field of Joint Settings for each
  DOF that has been marked as part of the gripper.

At this stage, multiple grasps may be authored in a row and sequentially exported to the same isaac\_grasp file.

### Importing Grasps

Apart from authoring grasps, the Grasp Editor may be used to validate grasps that were authored
elsewhere. This can be done in the Import panel by selecting an isaac\_grasp file and clicking Import.
This tutorial uses the same file that is used for export, but this does not need to be the case.

In the figure below, multiple grasps have been authored and written to file using the Grasp Editor.
These grasps are imported, and can now be quickly visualized and simulated in sequence.

## Using Authored Grasps in Isaac Sim

The Grasp Editor is primarily a UI-based extension, but it offers some utility for importing and
using authored grasps within NVIDIA Isaac Sim through a Python API.

This section presents the following stage with the goal of determining where the robot should go
to execute one of the authored grasps.

The following function snippet imports a grasp file demonstrated in [Importing Grasps](#isaac-sim-app-tutorial-grasp-editor-import) and
determines where the panda\_hand frame should be in order to duplicate grasp\_1. To try this function, copy it into the
[Script Editor](../development_tools/omniverse_script_editor.html#script-editor), and pass the import\_file\_path=”path/to/your/isaac\_grasp.yaml” argument to the function.

```python
import isaacsim.core.experimental.utils.xform as xform_utils
from isaacsim.robot_setup.grasp_editor import GraspSpec, import_grasps_from_file

def compute_gripper_pose_for_grasp(
    import_file_path: str,
    mug_reference_frame: str = "/World/mug",
    grasp_name: str = "grasp_1",
) -> tuple:
    """Compute and print the gripper pose target needed to execute a named grasp.

    Args:
        import_file_path: Path to an ``isaac_grasp`` YAML file to import.
        mug_reference_frame: USD prim path of the rigid body whose pose anchors the grasp.
        grasp_name: Name of the grasp inside the file to compute targets for.

    Returns:
        Tuple of ``(gripper_trans_target, gripper_orientation_target)``.
    """
    grasp_spec: GraspSpec = import_grasps_from_file(import_file_path)
    grasp_names = grasp_spec.get_grasp_names()

    mug_trans, mug_quat = xform_utils.get_world_pose(mug_reference_frame, device="cpu")
    mug_trans, mug_quat = mug_trans.numpy(), mug_quat.numpy()

    gripper_trans_target, gripper_orientation_target = grasp_spec.compute_gripper_pose_from_rigid_body_pose(
        grasp_name, mug_trans, mug_quat
    )

    print("Grasp Names:", grasp_names)
    print("Gripper Translation Target:", gripper_trans_target)
    print("Gripper Orientation Target:", gripper_orientation_target)

    return gripper_trans_target, gripper_orientation_target
```

```python
Grasp Names: ['grasp_0', 'grasp_1', 'grasp_2']
Gripper Translation Target: [ 0.41496072 -0.03612298  0.27738899]
Gripper Orientation Target: [-0.1690746   0.63886658  0.12752551  0.73959483]
```

The result of the code snippet shows the name of each grasp in the isaac\_grasp file, and
the translation and orientation targets that should be set for the
panda\_hand frame in the full Franka robot. Note that the code snippet uses the frame of reference
for the mug that was selected in the Grasp Editor. It is outside of the scope of this tutorial to
use a motion generation algorithm to achieve this grasp.

Check out the GraspSpec class in our [API Documentation](../py/source/extensions/isaacsim.robot_setup.grasp_editor/docs/index.html) to see the complete set of functionality.

On this page

* [Learning Objectives](#learning-objectives)
* [Getting Started](#getting-started)
* [What is an Isaac Grasp File?](#what-is-an-isaac-grasp-file)
* [Using the Grasp Editor](#using-the-grasp-editor)
  + [Selection Frame](#selection-frame)
  + [Select Frames of Reference](#select-frames-of-reference)
  + [Joint Settings](#joint-settings)
  + [Utils](#utils)
  + [Author a Grasp](#author-a-grasp)
    - [Adding External Forces and Torques](#adding-external-forces-and-torques)
  + [Exporting Grasps](#exporting-grasps)
  + [Importing Grasps](#importing-grasps)
* [Using Authored Grasps in Isaac Sim](#using-authored-grasps-in-isaac-sim)

---

### Policy Example

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/robot_simulation/ext_isaacsim_robot_policy_example.html

* [Robot Simulation](index.html)
* Reinforcement Learning Policies Examples in Isaac Sim

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Reinforcement Learning Policies Examples in Isaac Sim

## About

The isaac\_sim\_policy\_example Extension is a framework and has a set of helper functions to deploy Isaac Lab Reinforcement Learning Policies in Isaac Sim.
For details for training and building the policy in Isaac Sim, visit [deploying policy in Isaac Sim](../isaac_lab_tutorials/tutorial_policy_deployment.html#isaac-sim-app-tutorial-policy-deployment).

This Extension is enabled by default. If it is ever disabled, it can be re-enabled from the [Extension Manager](https://docs.omniverse.nvidia.com/extensions/latest/ext_core/ext_extension-manager.html "(in Omniverse Extensions)") by searching for `isaacsim.robot.policy.example`.
To run examples below activate **Windows** > **Examples** > **Robotics Examples** which will open the `Robotics Examples` tab.

### Unitree H1 Humanoid Example

1. The Unitree H1 humanoid example can be accessed by creating a empty stage.
2. Open the example menu using **Robotics Examples** > **POLICY** > **Humanoid**.
3. (Optional) Use the **Physics Engine** menu in the viewport to switch between PhysX and Newton before loading. The example automatically selects the matching policy for the active engine.
4. Press **LOAD** to open the scene.

This example uses an H1 Flat Terrain Policy trained in Isaac Lab to control the humanoid’s locomotion. Both PhysX and Newton policies are provided so you can compare locomotion behavior across physics engines.

Controls:

* Forward: UP ARROW / NUM 8
* Turn Left: LEFT ARROW / NUM 4
* Turn Right: RIGHT ARROW / NUM 6

### Boston Dynamics Spot Quadruped Example

1. The Boston Dynamics Spot quadruped example can be accessed by creating a empty stage.
2. Open the example menu using **Robotics Examples** > **POLICY** > **Quadruped**.
3. (Optional) Use the **Physics Engine** menu in the viewport to switch between PhysX and Newton before loading. The example automatically selects the matching policy for the active engine.
4. Press **LOAD** to open the scene.

This example uses a Spot Flat Terrain Policy trained in Isaac Lab to control the quadruped’s locomotion. Both PhysX and Newton policies are provided so you can compare locomotion behavior across physics engines.

Controls:

* Forward: UP ARROW / NUM 8
* Backward: BACK ARROW / NUM 2
* Move Left: LEFT ARROW / NUM 4
* Move Right: RIGHT ARROW / NUM 6
* Turn Left: N / NUM 7
* Turn Right: M / NUM 9

### Unitree Go2 Quadruped Example

1. The Unitree Go2 quadruped example can be accessed by creating a empty stage.
2. Open the example menu using **Robotics Examples** > **POLICY** > **Go2**.
3. (Optional) Use the **Physics Engine** menu in the viewport to switch between PhysX and Newton before loading. The example automatically selects the matching policy for the active engine.
4. Press **LOAD** to open the scene.

This example uses a Go2 Flat Terrain Policy trained in Isaac Lab to control the quadruped’s locomotion. Both PhysX and Newton policies are provided so you can compare locomotion behavior across physics engines.

Controls:

* Forward: UP ARROW / NUM 8
* Backward: BACK ARROW / NUM 2
* Move Left: LEFT ARROW / NUM 4
* Move Right: RIGHT ARROW / NUM 6
* Turn Left: N / NUM 7
* Turn Right: M / NUM 9

### Franka Panda Open Drawer Example

1. The Franka Panda Open Drawer example can be accessed by creating a empty stage.
2. Open the example menu using **Robotics Examples** > **POLICY** > **Franka**.
3. Press **LOAD** to open the scene.

This example uses the Franka Open Drawer Policy trained in Isaac Lab to control the robot’s arm.
The robot will open the drawer, hold it open until the would reset.

## Policies Files

The policies used in the examples are trained in Isaac Lab and are available here:

|  |  |  |
| --- | --- | --- |
| Name | Policy | Parameters |
| H1 Flat Terrain Policy (PhysX) | [H1 Flat Terrain Policy (PhysX)](https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Isaac/6.0/Isaac/Samples/Policies/h1/physx_policy.pt) | [H1 Flat Terrain Policy (PhysX) Environment Parameters](https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Isaac/6.0/Isaac/Samples/Policies/h1/physx_env.yaml) |
| H1 Flat Terrain Policy (Newton) | [H1 Flat Terrain Policy (Newton)](https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Isaac/6.0/Isaac/Samples/Policies/h1/newton_policy.pt) | [H1 Flat Terrain Policy (Newton) Environment Parameters](https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Isaac/6.0/Isaac/Samples/Policies/h1/newton_env.yaml) |
| Spot Flat Terrain Policy (PhysX) | [Spot Flat Terrain Policy (PhysX)](https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Isaac/6.0/Isaac/Samples/Policies/Spot_Policies/spot_policy.pt) | [Spot Flat Terrain Policy (PhysX) Environment Parameters](https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Isaac/6.0/Isaac/Samples/Policies/Spot_Policies/spot_env.yaml)  [Spot Flat Terrain Policy Network Parameters](https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Isaac/6.0/Isaac/Samples/Policies/Spot_Policies/agent.yaml) |
| Spot Flat Terrain Policy (Newton) | [Spot Flat Terrain Policy (Newton)](https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Isaac/6.0/Isaac/Samples/Policies/Spot_Policies/newton_policy.pt) | [Spot Flat Terrain Policy (Newton) Environment Parameters](https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Isaac/6.0/Isaac/Samples/Policies/Spot_Policies/newton_env.yaml) |
| ANYmal C Flat Terrain Policy | [ANYmal C Flat Terrain Policy](https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Isaac/6.0/Isaac/Samples/Policies/Anymal_Policies/anymal_policy.pt)  [ANYmal C Actuator Network](https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Isaac/6.0/Isaac/IsaacLab/ActuatorNets/ANYbotics/anydrive_3_lstm_jit.pt) | [ANYmal C Flat Terrain Policy Environment Parameters](https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Isaac/6.0/Isaac/Samples/Policies/Anymal_Policies/anymal_env.yaml)  [ANYmal C Flat Terrain Policy Network Parameters](https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Isaac/6.0/Isaac/Samples/Policies/Anymal_Policies/agent.yaml) |
| Franka Panda Open Drawer Policy | [Franka Panda Open Drawer Policy](https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Isaac/6.0/Isaac/Samples/Policies/Franka_Policies/Open_Drawer_Policy/policy.pt) | [Franka Panda Open Drawer Policy Environment Parameters](https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Isaac/6.0/Isaac/Samples/Policies/Franka_Policies/Open_Drawer_Policy/env.yaml) |
| Go2 Flat Terrain Policy (PhysX) | [Go2 Flat Terrain Policy (PhysX)](https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Isaac/6.0/Isaac/Samples/Policies/go2/physx_policy.pt) | [Go2 Flat Terrain Policy (PhysX) Environment Parameters](https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Isaac/6.0/Isaac/Samples/Policies/go2/physx_env.yaml) |
| Go2 Flat Terrain Policy (Newton) | [Go2 Flat Terrain Policy (Newton)](https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Isaac/6.0/Isaac/Samples/Policies/go2/newton_policy.pt) | [Go2 Flat Terrain Policy (Newton) Environment Parameters](https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Isaac/6.0/Isaac/Samples/Policies/go2/newton_env.yaml) |

Note

The policies can also be downloaded directly from the Content Browser by right clicking the policy and selecting `Download`.

Warning

The example policies uses separate robots for physx and newton, depending on the physics engine selected initially. Switching the physics engine will require the robot to be respawned.

## API Documentation

See the [API documentation](../py/source/extensions/isaacsim.robot.policy.examples/docs/index.html) for complete usage information.

## Standalone Examples

**h1\_standalone.py**

* This standalone example demonstrates a Unitree H1 controlled by a flat terrain policy, following a set of predetermined command sequences. It may be run via the following command:

  > ```python
  > ./python.sh standalone_examples/api/isaacsim.robot.policy.examples/h1_standalone.py --num-robots <number of robot> --env-url </path/to/environment>
  > ```
  >
  > For example, this will spawn 5 robots on the flat grid scene below:
  >
  > ```python
  > ./python.sh standalone_examples/api/isaacsim.robot.policy.examples/h1_standalone.py --num-robots 5 --env-url /Isaac/Environments/Grid/default_environment.usd
  > ```

**spot\_standalone.py**

* This standalone example demonstrates a Boston Dynamics Spot controlled by a flat terrain policy, following a set of predetermined command sequences. It may be run via the following command:

  > ```python
  > ./python.sh standalone_examples/api/isaacsim.robot.policy.examples/spot_standalone.py
  > ```

**anymal\_standalone.py**

* This standalone example demonstrates an ANYmal C robot that is controlled by a neural network policy. The rough terrain policy was trained in Isaac Lab and takes as input the state of the robot, the commanded base velocity, and the surrounding terrain and outputs joint position targets. The example may be run via the following command:

  > ```python
  > ./python.sh standalone_examples/api/isaacsim.robot.policy.examples/anymal_standalone.py
  > ```

Controls:

* Forward: UP ARROW / NUM 8
* Backward: BACK ARROW / NUM 2
* Move Left: LEFT ARROW / NUM 4
* Move Right: RIGHT ARROW / NUM 6
* Turn Left: N / NUM 7
* Turn Right: M / NUM 9

On this page

* [About](#about)
  + [Unitree H1 Humanoid Example](#unitree-h1-humanoid-example)
  + [Boston Dynamics Spot Quadruped Example](#boston-dynamics-spot-quadruped-example)
  + [Unitree Go2 Quadruped Example](#unitree-go2-quadruped-example)
  + [Franka Panda Open Drawer Example](#franka-panda-open-drawer-example)
* [Policies Files](#policies-files)
* [API Documentation](#api-documentation)
* [Standalone Examples](#standalone-examples)

---


## OmniGraph

### OmniGraph Tutorial

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/omnigraph/omnigraph_tutorial.html

* [OmniGraph](index.html)
* Isaac Sim OmniGraph Tutorial

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Isaac Sim OmniGraph Tutorial

This tutorial introduces you to the world of visual programming via OmniGraph.
We highly recommend that you also read [OmniGraph](https://docs.omniverse.nvidia.com/extensions/latest/ext_omnigraph.html "(in Omniverse Extensions)"), because it is a key component in Omniverse Kit.

## Learning Objectives

This tutorial aims to

* walk you through building an action graph to control a robot in Isaac Sim, specifically, the Jetbot.
* show you how to use the OmniGraph shortcuts to generate a differential controller graph for the Jetbot.

## Build the Graph

Let’s build an action graph to control a robot in Isaac Sim the Jetbot.

### Setting Up the Stage

1. On a new stage, start by right clicking and selecting **create > Physics > Ground Plane**.
2. In the Content Browser, navigate to `Isaac Sim/Robots/NVIDIA/Jetbot/jetbot.usd`.
3. Click and drag `jetbot.usd` onto the stage.
4. Position the JetBot just above the ground plane.
5. When completed, verify that the JetBot is under `/World/jetbot` in the context tree and that the stage looks similar to:

Jetbot on the stage

Note

Click play! Validate that the JetBot falls and lands on the stage. Click stop before continuing.

Depending on your default render settings, the camera of the JetBot may have a placeholder mesh (it looks like a gray television camera).
To hide these meshes, click on the  icon in the viewport and select **Show By Type –> Cameras**.

### Building the Graph

1. Select **Window > Graph Editors > Action Graph** from the dropdown menu at the top of the editor.
   The Graph Editor appears in the same pane as the Content browser.
2. Click **New Action Graph** to open an empty graph.
3. Type `controller` in the search bar of the graph editor.
4. Drag an `Articulation Controller` and a `Differential Controller` onto the graph.

The `Articulation Controller` applies driver commands (in the form of force, position, or velocity) to the specified joints
of any prim with an articulation root.

To tell the controller which robot it’s going to control:

1. Select the `Articulation Controller` node in the graph and open up the property pane.
2. You can either:

   * Click **usePath** and Type in the path to the robot */World/jetbot* in **robotPath**

     **OR**
   * Click **Add Targets** near the top of the pane for `input:targetPrim` and select **JetBot** in the pop up window.

The `Differential Controller` computes drive commands for a two wheeled robot given some target linear and angular velocity. Like the
`Articulation Controller`, it also needs to be configured.

1. Select the `Differential Controller` node in the graph.
2. In the properties pane, set the `wheelDistance` to 0.1125, the `wheelRadius` to 0.03, and `maxAngularSpeed` to 0.2.

The `Articulation Controller` also needs to know which joints to articulate. It expects this information in the form of a list of tokens or index values. Each joint in a robot has a name and the JetBot has exactly two. Verify this by examining the JetBot in the stage context tree. Within `/World/jetbot/chassis`
are two revolute physics joints named `left_wheel_joint` and `right_wheel_joint`.

Stage Tree

1. Type `token` into the search bar of the graph editor.
2. Add two `Constant Token` nodes to the graph.
3. Select one and set it’s value to `left_wheel_joint` in the properties pane.
4. Repeat this for the other constant token node, but set the value to `right_wheel_joint`.
5. Type `make array` into the search bar of the graph editor.
6. Add a `Make Array` node to the graph.
7. Select the `Make Array` node and click on the `+` icon in the `inputs` section of the property pane menu to add a second input.
8. Set the `arraySize` to 2 and set the input type to `token[]` from the dropdown menu in the same pane.
9. Connect the constant token nodes to `input0` and `input1` of the `Make Array` node, and then the output of that node to the `Joint Names` input of the `Articulation Controller` node.

The last node is the event node.

1. Search for `playback` in the search bar of the graph editor.
2. Add an `On Playback Tick` node to the graph. This node emits an execution event for every frame, but only while the simulation is playing.
3. Connect the `Tick` output of the `On Playback Tick` node to the `Exec In` input of both controller nodes.
4. Connect the `Velocity Command` output of the differential controller to the `Velocity Command` input of the articulation controller.
5. Validate that the graph looks similar to:

Simple differential control for the JetBot

1. Press the play button.
2. Select the `Differential Controller` node in the graph.
3. Click and drag on either the angular or linear velocity values in the properties pane to change it’s value (or just click and type in the desired value).

Note

Explore the available OmniGraph nodes and try to setup a graph to control the JetBot with the keyboard. The graph
below is an example graph for controlling the JetBot with a keyboard.

Keyboard control Action graph for the JetBot

## OmniGraph Shortcuts

Putting the graph from scratch can be tedious, especially when you have to iterate. We made some shortcuts for frequently used graphs, so that within a couple clicks, you can generate a complex graph with multiple nodes and connections. They can be found under `Tools -> Robotics -> OmniGraph Controllers`, and the instructions for them are in [Commonly Used OmniGraph Shortcuts](omnigraph_shortcuts.html#isaac-sim-app-tutorial-advanced-omnigraph-shortcuts).

To use the Differential Controller graph from the menu shortcut:

1. Delete (or Disable if that is an option) any previous OmniGraphs that controls the Jetbot.
2. Go to the Menu bar and click on **Tools -> Robotics -> OmniGraph Controllers -> Differential Controller**.
3. You are prompted for the necessary parameters.
4. Add “/World/jetbot” to `Articulation Root`, set the **distance between wheels** to 0.1125, and the **wheel radius** to 0.03.
5. Given JetBot only has two controllable joints, you can leave the rest of the fields empty.
6. Turn **Use Keyboard Control (WASD)** on.
7. Click **OK** to generate the graph. You can open the generated graph under `/Graph/differential_controller`.
8. Press **Play** to start simulation.
9. Verify that you can move the JetBot using the WASD keys on the keyboard.

## Summary

This tutorial covered:

* Basic concepts of OmniGraph
* Setting up a stage with a robot
* Using OmniGraph to construct interfaces to a robot
* Using the OmniGraph shortcuts to generate differential controller graph

### Further Learning

* More in-depth concepts in [OmniGraph](https://docs.omniverse.nvidia.com/extensions/latest/ext_omnigraph.html "(in Omniverse Extensions)")
* More details about all the OmniGraph shortcuts [Commonly Used OmniGraph Shortcuts](omnigraph_shortcuts.html#isaac-sim-app-tutorial-advanced-omnigraph-shortcuts)
* Examples for composing OmniGraph via Python scripting: [OmniGraph via Python Scripting Tutorial](omnigraph_scripting.html#isaac-sim-app-tutorial-advanced-omnigraph-scripting)
* Examples for writing custom Python nodes: [Custom Python Nodes](omnigraph_custom_python_nodes.html#isaac-sim-app-omnigraph-custom-python-nodes)

On this page

* [Learning Objectives](#learning-objectives)
* [Build the Graph](#build-the-graph)
  + [Setting Up the Stage](#setting-up-the-stage)
  + [Building the Graph](#building-the-graph)
* [OmniGraph Shortcuts](#omnigraph-shortcuts)
* [Summary](#summary)
  + [Further Learning](#further-learning)

---

### OmniGraph Scripting

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/omnigraph/omnigraph_scripting.html

* [OmniGraph](index.html)
* OmniGraph via Python Scripting Tutorial

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# OmniGraph via Python Scripting Tutorial

While OmniGraph is intended to be a visual scripting tool, it does have Python scripting interfaces. This tutorial will give some examples of how to script an action graph using Python.

## Learning Objectives

This tutorial will

* walk you through examples of scripting an OmniGraph using purely Python APIs
* introduce the basic concepts and frequently used parameters in OmniGraphs and showcase them using scripted examples

## Getting Started

**Prerequisites**

* Review the GUI Tutorial series, especially [Isaac Sim OmniGraph Tutorial](omnigraph_tutorial.html#isaac-sim-app-tutorial-gui-omnigraph) and [Omniverse Script Editor](../development_tools/omniverse_script_editor.html#isaac-sim-app-omniverse-script-editor) prior to beginning this tutorial.
* Review the Core API Tutorial series, especially [Hello World](../core_api_tutorials/tutorial_core_hello_world.html#isaac-sim-app-tutorial-core-hello-world) to become familiar with the extension workflow via Python, as well as the Python Standalone workflow.

## Code Snippets

### Creating a Graph

First let’s build a simple action graph that prints “Hello World” to the console on every simulation frame.

1. Open ‘Window > Script Editor’ and paste the following code:

   > ```python
   > import omni.graph.core as og
   >
   > keys = og.Controller.Keys
   > graph_handle, list_of_nodes, _, _ = og.Controller.edit(
   >     {"graph_path": "/action_graph", "evaluator_name": "execution"},
   >     {
   >         keys.CREATE_NODES: [("tick", "omni.graph.action.OnTick"), ("print", "omni.graph.ui_nodes.PrintText")],
   >         keys.SET_VALUES: [
   >             ("print.inputs:text", "Hello World"),
   >             (
   >                 "print.inputs:logLevel",
   >                 "Warning",
   >             ),  # setting the log level to warning so we can see the printout in terminal
   >         ],
   >         keys.CONNECT: [("tick.outputs:tick", "print.inputs:execIn")],
   >     },
   > )
   > ```
2. Press ‘Run’ to execute the script. You should see a new prim `/action_graph` created on the Stage tree.
3. Expand the prim on stage, the nodes “tick” and “print” should be listed under the graph. These nodes can be accessed just like any other prim on the stage.
4. Press “play” to start the simulation. You should see “Hello World” printed to the console on every frame.
5. Open graph editor by going to Window > Graph Editors > Action Graph.
6. With the newly created graph highlighted on the Stage tree on the right, open the graph by clicking on the icon for ‘Edit Action Graph’ in the graph editor window. You should see two nodes connected with each other by a line.

### Editing a Graph

Once a graph has been created, there are specific APIs to manipulate the graph’s terms.

**Getting and Setting Attribute Values**

Open another tab in the Script Editor, paste the snippet below, and run.

```python
import omni.graph.core as og

# get existing value from an attribute
existing_text = og.Controller.attribute("/action_graph/print.inputs:text").get()
print("Existing Text: ", existing_text)

# set new value
og.Controller.attribute("/action_graph/print.inputs:text").set("New Texts to print")
```

This will change the value in the “Print Text” node from “Hello World” to “New Texts to print”. But this affect won’t take place until the first tick through the graph. So when you press ‘Run’ in the script editor, the graph has yet to be ticked, so it should fetch the current value from the node, and print out a single string of “Existing Text: Hello World” in the Script Editor’s console (as well as the terminal if you are using that, or the main Omniverse’s console if you include “Info” to be printed).

Now press ‘Play’ and start the simulation. It should now print, at the rate of one string per tick, the updated text “New Texts to print”, in the terminal or the main Omniverse console (though not the Script Editor’s console).

**Adding Nodes and Connections**

Open a third tab in the Script Editor to add nodes and make more connections to an existing graph.

```python
import omni.graph.core as og

og.Controller.create_node("/action_graph/new_node_name", "omni.graph.nodes.ConstantString")
og.Controller.attribute("/action_graph/new_node_name.inputs:value").set("This is a new node")
og.Controller.connect("/action_graph/new_node_name.inputs:value", "/action_graph/print.inputs:text")
```

A new node named “new\_node\_name” will be created and connected to the “Print Text” node. If you have the graph editor (Window > Graph Editors > Action Graph) open, you can see that there are now three nodes connected to each other instead of two.

### Graph Execution

By default, the graph is evaluated on every frame. You can change this behavior by setting the graph to evaluate only when you call it.

You can also trigger each graph explicitly by making execute only when you call it. To do this, there is a special parameter called “pipeline\_stage” where you can set the graph to execute “On Demand”. Most of the times we want to set this variable during the creation of the graph:

1. Delete the previous graph by selecting it on the stage tree and pressing ‘Delete’ key.
2. Open a new tab in the Script Editor and paste the following code

   > ```python
   > import omni.graph.core as og
   >
   > keys = og.Controller.Keys
   > demand_graph_handle, _, _, _ = og.Controller.edit(
   >     {
   >         "graph_path": "/ondemand_graph",
   >         "evaluator_name": "execution",
   >         "pipeline_stage": og.GraphPipelineStage.GRAPH_PIPELINE_STAGE_ONDEMAND,
   >     },
   >     {
   >         keys.CREATE_NODES: [("tick", "omni.graph.action.OnTick"), ("print", "omni.graph.ui_nodes.PrintText")],
   >         keys.SET_VALUES: [("print.inputs:text", "On Demand Graph"), ("print.inputs:logLevel", "Warning")],
   >         keys.CONNECT: [("tick.outputs:tick", "print.inputs:execIn")],
   >     },
   > )
   > ```
3. Press ‘Run’ in the Script Editor. A new graph `/ondemand_graph` will be created.
4. Start simulation by press “play”, nothing should be printed from this graph because we did not explicitly call to evaluate it.
5. To manually trigger a graph, open another tab, and paste in `demand_graph_handle.evaluate()`
6. Make sure simulation is still running. Click ‘Run’ in the Script Editor. You should see “On Demand Graph” printed to the console once.

Alternatively, you can also set it for an existing graph by `demand_graph_handle.change_pipeline_stage(og.GraphPipelineStage.GRAPH_PIPELINE_STAGE_ONDEMAND)`

A more in-depth example of attaching graphs to physics callbacks and/or rendering callbacks can be found in standalone\_examples/api/isaacsim.core.experimental.api/omnigraph\_triggers.py

## Summary

In this tutorial, we introduced scripting OmniGraph via Python.

### Further Reading

For more Python Scripting API in [OmniGraph APIs](https://docs.omniverse.nvidia.com/kit/docs/omni.graph/latest/omni.graph.core.html)

On this page

* [Learning Objectives](#learning-objectives)
* [Getting Started](#getting-started)
* [Code Snippets](#code-snippets)
  + [Creating a Graph](#creating-a-graph)
  + [Editing a Graph](#editing-a-graph)
  + [Graph Execution](#graph-execution)
* [Summary](#summary)
  + [Further Reading](#further-reading)

---

### Custom Python Nodes

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/omnigraph/omnigraph_custom_python_nodes.html

* [OmniGraph](index.html)
* Custom Python Nodes

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Custom Python Nodes

There already exist a large number of default nodes that comes with Isaac Sim. You can find the definitions and descriptions for them in either the [OmniGraph Node Library](https://docs.omniverse.nvidia.com/extensions/latest/ext_omnigraph/node-library/node-library.html "(in Omniverse Extensions)") or [API Documentation](../reference_python_api.html#isaac-sim-python-manual). If those prove to be insufficient, you can write your own and integrate them into Isaac Sim.

A node is defined by two files, an .ogn file, which is a JSON file that defines the structure of the node, including its inputs, outputs, and parameters. Either a Python file or a C++ file can be used to define its function. Here we will focus on Python nodes.

## Node Files

All OmniGraph Node files starts with “Ogn” as a prefix. This is expected by the parser.

### Node Definition (.ogn)

The .ogn file is a JSON file that defines the structure of the node, including its inputs, outputs, and parameters. Here is an example of a simple node definition:

```python
 1{
 2 "NodeName": {
 3     "version": 1,
 4     "categories": "examples",
 5     "description": ["Minimum Example"],
 6     "language": "python",
 7     "metadata": {
 8         "uiName": "minimum example"
 9     },
10     "inputs": {
11                        "execIn": {
12             "description": "the trigger input that starts the node",
13             "type": "execution",
14         },
15                        "value_input": {
16             "type": "double",
17             "description": "a number",
18             "default": 0.0,
19          },
20     },
21     "outputs": {
22         "output_bool": {
23             "type": "bool",
24             "description": "let output be a boolean",
25          }
26      }
27   }
28}
```

A note about the input “execIn”. This is a special input that is used to trigger the node. This trigger is only relevant in an Action Graph, where you must explicitly trigger the node to run, such as on a physics tick, or a stage event, like opening and closing a stage. In a Push Graph, the node will run automatically at every frame and the ‘execIn’ input is not necessary.

### Function Definition

Here’s a minimum example of a Python node that takes an input number and outputs a boolean value based on whether the input is greater than 0:

```python
class OgnNodeName:
    @staticmethod
    def compute(db):
        db.outputs.out = bool(db.inputs.value_input > 0.0)
        return True
```

Notes:

* the class name must match the name of the node in the .ogn file, and the file name must match the class name.
* the “compute” function is what the ‘execIn’ input triggers. It takes a single argument, the database, which contains the inputs and outputs of the node. The function should return True if the node ran successfully, and False if it failed.
* this node has no internal state, which means all data that passes through it is gone the next tick. If you need to store data between ticks, you can use the “internal state” to store it.

## Using the Custom Node

You can simply insert your custom node’s `.py` and `.ogn` files into any of extensions that already have a directory that contains the `.py` and `.ogn` files for existing nodes and thereby avoid creating your own extension that way.

You can also create your own extension and insert the files there. (link to the new template generator)

## Isaac Sim Nodes as Examples

You are welcome to dig into the code behind some of our existing OmniGraph nodes to find examples of how to structure a node, or even modify them to suite your own need. To find the backend `.py` and `.ogn` files for a particular node. Hover your mouse over the node in the editor window, a tooltip window will appear and the name of the extension will be written in the parentheses. You can then navigate to the extensions’s folder that contains the backend scripts for the nodes by going to `exts/isaacsim.<ext_name>/isaacsim/<ext_name>/ogn/python/nodes/`.

Not all of the nodes are written in Python, some have C++ backends, so if you won’t necessarily see a corresponding `.py` and `.ogn` files for all the nodes on the list. Note that if you found a folder with a list of `Ogn<node_name>Database.py`, this is NOT the directory that contains the Python description of the node.

On this page

* [Node Files](#node-files)
  + [Node Definition (.ogn)](#node-definition-ogn)
  + [Function Definition](#function-definition)
* [Using the Custom Node](#using-the-custom-node)
* [Isaac Sim Nodes as Examples](#isaac-sim-nodes-as-examples)

---

### Custom C++ Nodes

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/omnigraph/omnigraph_custom_cpp_nodes.html

* [OmniGraph](index.html)
* Custom C++ Nodes

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Custom C++ Nodes

For C++ nodes, the [Node Definition (.ogn)](omnigraph_custom_python_nodes.html#isaac-sim-omnigraph-ogn-file) is the same as the one used for Custom Python Nodes.

Examples of how to include OmniGraph nodes can be found in the extension template’s [GitHub repo](https://github.com/NVIDIA-Omniverse/kit-extension-template-cpp/tree/main/source/extensions/omni.example.cpp.omnigraph_node).

To use the custom C++ nodes, you will need also build your custom C++ extension. Follow [Kit C++ Extension Template](https://docs.omniverse.nvidia.com/kit/docs/kit-extension-template-cpp/latest/index.html) for the detailed instructions.

---

### Custom IPC Nodes

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/omnigraph/omnigraph_custom_ipc_nodes.html

* [OmniGraph](index.html)
* Building Custom IPC OmniGraph Nodes

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Building Custom IPC OmniGraph Nodes

This guide explains how to build OmniGraph nodes for inter-process communication (IPC) in Isaac Sim. It covers the node schema, transport lifecycle with `BaseResetNode`, non-blocking I/O inside `compute`, and how to add your transport library as a dependency. The OmniGraph patterns apply regardless of the IPC stack that you use. The working example is `isaacsim.examples.ipc`, a clock-send and step-receive node pair over BSD sockets in C++ and Python. The tutorial starts by scaffolding a new extension with the CLI template so you have a working build skeleton before writing any IPC code.

Note

This workflow requires a **source checkout** of the [Isaac Sim](https://github.com/isaac-sim/IsaacSim) repository. It is not supported with the pip packages or the binary release. Clone the GitHub repository before you begin.

Note

All commands in this tutorial are run from the **Isaac Sim repository root** (the directory that contains `build.sh`/`build.bat` and `repo.sh`/`repo.bat`).

## Before You Start

**Prerequisites**:

* **Custom C++ extensions** — [Kit C++ Extension Template](https://docs.omniverse.nvidia.com/kit/docs/kit-extension-template-cpp/latest/index.html).
* **OmniGraph** — [OmniGraph Core Concepts](https://docs.omniverse.nvidia.com/extensions/latest/ext_omnigraph/getting-started/core_concepts.html "(in Omniverse Extensions)") and [Basic OmniGraph Tutorial](https://docs.omniverse.nvidia.com/extensions/latest/ext_omnigraph/tutorials/gentle_intro.html "(in Omniverse Extensions)").
* **Custom nodes** — [Custom Python Nodes](omnigraph_custom_python_nodes.html#isaac-sim-app-omnigraph-custom-python-nodes) and [Custom C++ Nodes](omnigraph_custom_cpp_nodes.html#isaac-sim-app-tutorial-advanced-omnigraph-custom-cpp-nodes).

Optional: [Isaac Sim OmniGraph Tutorial](omnigraph_tutorial.html#isaac-sim-app-tutorial-gui-omnigraph), if you are new to the Action Graph editor.

See also

[ROS 2 Python Custom OmniGraph Node](../ros2_tutorials/tutorial_ros2_custom_omnigraph_node_python.html#isaac-sim-app-ros2-custom-omnigraph-node-python) for a complete Python node
example. ROS 2 context, but the `internal_state()` factory,
`BaseResetNode`, `db.per_instance_state`, and
`og.ExecutionAttributeState.ENABLED` patterns are identical for any IPC
node.

## Scaffold Your Extension

Before writing IPC code, create the extension skeleton with the CLI template:

Linux

```python
./repo.sh template new
```

Windows

```python
.\repo.bat template new
```

When prompted, select **Isaac Sim OmniGraph Node Extension**. You will be asked for:

* `extension_name` Dotted identifier, for example `isaacsim.my.ipc.nodes`.
* `title` Human-readable name shown in the Extensions window.
* `description` Short summary.
* `category` Used to group your nodes in the Action Graph node library (for example `Simulation`).

The template creates the full extension skeleton under `source/extensions/<extension_name>/`:

```python
source/extensions/<extension_name>/
├── config/extension.toml          ← metadata, dependencies, test entries
├── nodes/
│   ├── OgnExampleCpp.ogn          ← rename/replace with your IPC node schema
│   └── OgnExampleCpp.cpp          ← rename/replace with your IPC node implementation
├── plugins/<extension_name>/
│   └── PluginInterface.cpp        ← Carbonite plugin + OGN registration (keep as-is)
├── bindings/<extension_name>/
│   └── Bindings.cpp               ← pybind11 bindings; acquires the Carbonite interface (keep as-is)
├── include/<extension_name>/
│   └── IExampleNodes.h            ← Carbonite interface (keep as-is)
├── python/nodes/
│   ├── OgnExamplePython.ogn       ← rename/replace with your Python node schema
│   └── OgnExamplePython.py        ← rename/replace with your Python Node Implementation
├── python/impl/extension.py       ← calls acquire_example_ipc_interface() on startup to load the plugin
├── python/tests/                  ← test modules go here
└── premake5.lua                   ← build configuration
```

The build step is required before the extension loads in Isaac Sim — it compiles the C++ plugin and generates the OmniGraph database files that register your nodes. Run it now:

Linux

```python
./build.sh
```

Windows

```python
.\build.bat
```

The generated nodes — **Example C++ Node** (`OgnExampleCpp`) and **Example Python Node** (`OgnExamplePython`) — are placeholder stubs that double an input value. The display names in the Action Graph library come from the `uiName` field in each `.ogn` file, not the file name. Rename or replace them with your actual IPC node(s) as you work through the sections below.

Try it: verify your scaffold

After the build completes above, confirm the scaffold registers its placeholder nodes:

1. Launch the repo-built Isaac Sim — not a separately installed Isaac Sim:

   Linux

   ```python
   ./_build/linux-x86_64/release/isaac-sim.sh
   ```

   Windows

   ```python
   .\_build\windows-x86_64\release\isaac-sim.bat
   ```
2. Open **Window → Extensions**, search for your extension name (for example `isaacsim.my.ipc.nodes`), and enable it.
3. Open **Window → Graph Editors → Action Graph** and search for `Example C++ Node` and `Example Python Node` in the node library. These names match the `uiName` fields in the scaffold’s `.ogn` files.

If both nodes appear, the scaffold is wired correctly. Proceed to [Design and Implement Your Nodes](#design-and-implement-your-nodes) to replace the placeholders.

If the nodes do not appear, check the following:

* The build (`./build.sh` on Linux, `.\build.bat` on Windows) completed without errors. Nodes are not registered until the C++ plugin is compiled and the OmniGraph database files are generated by the build.
* You launched the repo-built Isaac Sim (`./_build/linux-x86_64/release/isaac-sim.sh` or `.\_build\windows-x86_64\release\isaac-sim.bat`). A separately installed Isaac Sim does not search the repository `exts/` directory and will not find your extension.
* The extension is enabled (green toggle) in **Window → Extensions**. If it was enabled before the build ran, disable and re-enable it.
* After any `.ogn` schema or code change, the build must be re-run and Isaac Sim restarted before updated nodes appear.

## Add Your Transport Library

Before writing node code, wire in the library that provides your IPC and serialization. The generated `config/extension.toml` and `premake5.lua` are already in place. The sections below show where to add entries.

### Python

Isaac Sim ships a pip archive (`omni.isaac.core_archive` and related extensions) that pre-bundles many common packages, including NumPy and SciPy. If your library is already in that archive you can import it directly with no extra configuration.

If the package is not yet bundled, declare it in `config/extension.toml`, for example:

```python
[python.pipapi]
requirements = ["pyzmq>=25", "grpcio"]  # replace with your actual packages
use_online_index = true
```

Isaac Sim resolves these at extension startup. `use_online_index = true` must be set. If it is omitted or set to `false`, `omni.kit.pipapi` logs a warning and skips the `requirements` list entirely.

### C++

Prebuilt native libraries go through packman. These steps follow the same pattern described in the [Kit Extension C++ template documentation](https://docs.omniverse.nvidia.com/kit/docs/kit-extension-template-cpp/latest/index.html):

1. **Declare the dependency.** Add your library to `deps/ext-deps.packman.xml`. It is the designated file for extension-specific dependencies (separate from the Kit SDK deps). The unpacked tree typically lands under `_build/target-deps/<libname>/`:

   ```python
   <project toolsVersion="5.0">
     <dependency name="mylib" linkPath="../_build/target-deps/mylib">
       <package name="mylib" version="1.2.3" />
     </dependency>
   </project>
   ```
2. **Update ``premake5.lua``.** Point to the include and library directories and add the link:

   ```python
   includedirs { "%{target_deps}/mylib/include" }
   libdirs     { "%{target_deps}/mylib/lib/%{platform}" }
   links       { "mylib" }
   ```
3. **Shared libraries at runtime.** If the library ships as a `.so` / `.dll`, either bundle it beside the extension plugin or list it under `[native.library]` in `extension.toml` so Kit’s loader finds it.

The sample extension uses only standard BSD socket APIs and has no additional native library entries beyond the plugin itself.

## Design and Implement Your Nodes

### Design Principle

Keep IPC nodes thin. They should only handle **serialization and transport**. Simulation data reads (joint positions, sensor data, simulation time) belong in upstream built-in nodes wired into the graph before your IPC node. Downstream processing or command writes belong in other nodes after it. This keeps `compute` fast and makes the graph layout self-documenting.

### What Every IPC Node Requires

Every custom IPC node requires the same six things, regardless of transport:

* **Node schema** (`.ogn` file) — declare inputs (URI, config), outputs (data, `execOut`), and state. Refer to the sample `.ogn` files under `nodes/` in `isaacsim.examples.ipc` as a reference.
* `BaseResetNode` subclass — holds per-instance state (sockets, buffers, handles). Implement `reset()` (C++) or `custom_reset()` (Python) to tear down the transport when the timeline stops or inputs change.
* `compute(db)` with a lifecycle split:

  > + Detect input changes (URI, config) → call reset and teardown
  > + Try to open the transport if not ready → return early on failure (retry next evaluation)
  > + Do non-blocking I/O (send or try-receive)
  > + Write `db.outputs` and fire `execOut`
* **Non-blocking I/O** — never block indefinitely in `compute`. Use try-receive, timeouts, or offload slow paths to a worker thread (refer to [Performance Considerations](#performance-considerations)).
* **Fire** `execOut` at the end of `compute` to signal downstream nodes that the transport operation is complete and/or new data is ready. You control when to fire it. For example, fire on every evaluation, only on successful send, or only when a full message has been received.
* **Your transport library** — add it as a dependency (refer to [Add Your Transport Library](#add-your-transport-library) above) and replace the TCP helpers with your stack’s API.

### OGN Schema Quick Reference

Each `.ogn` file is a single JSON object keyed by the node’s registered type
name. The minimum schema for a Python IPC node looks like this:

```python
{
    "MyNodeName": {
        "version": 1,
        "language": "Python",
        "description": "One-line description shown in the node library.",
        "metadata": { "uiName": "My Node Display Name" },
        "categoryDefinitions": "config/CategoryDefinition.json",
        "categories": "myCategory",
        "inputs": {
            "execIn":  { "type": "execution", "description": "Trigger." },
            "uri":     { "type": "string",    "description": "...", "default": "tcp://127.0.0.1:5550" },
            "myValue": { "type": "double",    "description": "...", "default": 0.0 }
        },
        "outputs": {
            "execOut":  { "type": "execution", "description": "Output execution port." },
            "myTokens": { "type": "token[]",   "description": "Array of token outputs." }
        }
    }
}
```

Common scalar types: `"string"`, `"double"`, `"float"`, `"int"`,
`"uint"`, `"bool"`, `"execution"`. Array variants append `[]`:
`"double[]"`, `"float[]"`, `"token[]"`, etc. The `"default"` key is
required for non-execution scalar inputs; use `[]` for array inputs.

`categoryDefinitions` is a path relative to the `nodes/` directory that
points to a JSON file mapping category keys to human-readable display strings:

```python
{
    "categoryDefinitions": {
        "myCategory": "My node group label in the Action Graph library"
    }
}
```

### C++ Node Implementation

`BaseResetNode` is declared in `isaacsim.core.includes`. This extension is a compile-time only dependency, do **not** add it to `[dependencies]` in `extension.toml`. Instead, add the header path in `premake5.lua`:

```python
includedirs { "%{root}/source/extensions/isaacsim.core.includes/include" }
```

Then include the header in your `.cpp` file:

```python
#include <isaacsim/core/includes/BaseResetNode.h>
```

Derive your per-instance node class from `isaacsim::core::includes::BaseResetNode`. That base subscribes to the timeline stop event and calls your `reset()` so transport handles are not left open after simulation stops.

Replace the generated `OgnExampleCpp` stub with a class like this (refer to `OgnSimpleSendSimulationClockCpp.cpp` in `isaacsim.examples.ipc` for TCP implementation):

```python
#include <isaacsim/core/includes/BaseResetNode.h>

#include <OgnMyIpcNodeCppDatabase.h>
#include <memory>
#include <string>

using isaacsim::core::includes::BaseResetNode;

class OgnMyIpcNodeCpp : public BaseResetNode
{
public:
    static bool compute(OgnMyIpcNodeCppDatabase& db)
    {
        auto& state = db.perInstanceState<OgnMyIpcNodeCpp>();

        // Detect input changes (e.g. URI) and reset transport.
        const std::string uriIn(db.inputs.uri());
        if (state.m_handle && state.m_handle->getUri() != uriIn)
        {
            state.reset();
        }

        const bool success = state.ensureOpenAndTransfer(db);
        // Fire execOut unconditionally (send nodes). For receive nodes, fire only when
        // a complete message arrives (i.e. only when success == true).
        db.outputs.execOut() = omni::graph::core::kExecutionAttributeStateEnabled;
        return success;
    }

    static void releaseInstance(NodeObj const& nodeObj, GraphInstanceID instanceId)
    {
        auto& state = OgnMyIpcNodeCppDatabase::sPerInstanceState<OgnMyIpcNodeCpp>(nodeObj, instanceId);
        state.reset();
    }

    void reset() override
    {
        if (m_handle)
        {
            m_handle->close();
            m_handle.reset();
        }
    }

private:
    bool isOpen() const
    {
        return m_handle && m_handle->isOpen();
    }

    void tryOpen(OgnMyIpcNodeCppDatabase& db)
    {
        // Open transport from db.inputs (e.g. URI, config).
        // m_handle = std::make_unique<MyTransportHandle>(std::string(db.inputs.uri()));
    }

    bool transfer(OgnMyIpcNodeCppDatabase& db)
    {
        // Non-blocking send or try-receive; write db.outputs on success.
        // See Performance Considerations for time-budget guidance.
        return false; // replace with actual transfer
    }

    bool ensureOpenAndTransfer(OgnMyIpcNodeCppDatabase& db)
    {
        if (!isOpen())
        {
            tryOpen(db);
            if (!isOpen())
                return false;
        }
        return transfer(db);
    }

    std::unique_ptr<MyTransportHandle> m_handle; // replace with your transport type
};

REGISTER_OGN_NODE()
```

Note

The generated `python/impl/extension.py` calls `acquire_example_ipc_interface()` in
`on_startup()`. This is what triggers the Carbonite plugin to load and run
`INITIALIZE_OGN_NODES()`, registering your C++ nodes. If your nodes do not appear in the
Action Graph library, verify that `extension.py` is calling the acquire function and that
`PluginInterface.cpp` does **not** contain a `CARB_PLUGIN_IMPL_DEPS` line, because that macro
can prevent the plugin from loading.

### Python Node Implementation

`BaseResetNode` is provided by the `isaacsim.core.nodes` extension. Add it as a dependency in `config/extension.toml` and import it in your node file:

```python
[dependencies]
"isaacsim.core.nodes" = {}
```

```python
import omni.graph.core as og
from isaacsim.core.nodes import BaseResetNode
```

Put per-instance data in a small class that subclasses `BaseResetNode`. Pass `initialize=False` to `super().__init__`, if you lazy-open sockets in `compute`, as the samples do. Without it, `BaseResetNode.__init__` calls `custom_reset()` immediately during construction, before your instance attributes (such as, `self.sock = None`) are set, raising `AttributeError`. Implement `custom_reset()` to close sockets and clear buffers. `custom_reset()` runs on timeline stop and mirrors the C++ `reset()`.

Replace the generated `OgnExamplePython` stub with a class like this (refer to `OgnSimpleSendSimulationClockPy.py` in `isaacsim.examples.ipc` for a full TCP implementation):

```python
import omni.graph.core as og
from isaacsim.core.nodes import BaseResetNode

class OgnMyIpcNodePyState(BaseResetNode):
    """Per-instance state for the template IPC node."""

    def __init__(self) -> None:
        # Declare all attributes BEFORE calling super().__init__,
        # because BaseResetNode.__init__ calls custom_reset() immediately.
        self.handle = None  # replace with your transport handle
        self.uri = ""
        super().__init__(initialize=False)

    def custom_reset(self) -> None:
        """Reset transport state when timeline or inputs change."""
        # Called on timeline stop and when inputs change.
        if self.handle is not None:
            self.handle.close()
            self.handle = None
        self.uri = ""

class OgnMyIpcNodePy:
    """Template OmniGraph node for custom IPC transports."""

    @staticmethod
    def internal_state() -> OgnMyIpcNodePyState:
        """Create per-instance state for the node."""
        return OgnMyIpcNodePyState()

    @staticmethod
    def compute(db: object) -> bool:
        """Evaluate one non-blocking IPC transfer step."""
        state = db.per_instance_state

        uri = db.inputs.uri
        if state.handle is not None and state.uri != uri:
            state.custom_reset()

        if state.handle is None:
            # Open transport from inputs (e.g. URI, config).
            # state.handle = open_my_transport(uri)
            # state.uri = uri
            # Fire execOut even on failure so downstream nodes keep running.
            db.outputs.execOut = og.ExecutionAttributeState.ENABLED
            return False

        # Non-blocking send or try-receive; write db.outputs on success.
        # See Performance Considerations for time-budget guidance.
        success = False  # replace with actual transfer

        # For send nodes: fire execOut every tick.
        # For receive nodes: fire execOut only when a full message arrives.
        if success:
            db.outputs.execOut = og.ExecutionAttributeState.ENABLED
        return success
```

Try it: implement and build your node

Adapt your scaffolded extension to a minimal IPC sender:

1. **Update the OGN schema.** In `nodes/OgnExampleCpp.ogn` (or `OgnExamplePython.ogn`), rename the node and add a `uri` string input (default `"127.0.0.1:9000"`) and `execIn`/`execOut` execution ports.
2. **Replace the implementation.** Copy the template above into `OgnExampleCpp.cpp` (or `OgnExamplePython.py`), rename classes to match, and fill in a no-op `transfer()` that always returns `true`.
3. **Rebuild:** `./build.sh` (Linux) or `.\build.bat` (Windows).
4. **Restart Isaac Sim** by closing and relaunching `./_build/linux-x86_64/release/isaac-sim.sh` (Linux) or `.\_build\windows-x86_64\release\isaac-sim.bat` (Windows).
5. **Verify:** enable your extension in Isaac Sim and confirm the renamed node appears in the Action Graph library under its new `uiName`.

For a complete TCP implementation of the same pattern, study `OgnSimpleSendSimulationClockCpp.cpp` (or the Python equivalent) in `source/extensions/isaacsim.examples.ipc/`.

For Python-only extensions (no C++ plugin), omit `project_ext_plugin`, `project_ext_bindings`, and all `includedirs` / `links` entries from `premake5.lua`. Keep `add_ogn_dependencies` (processes `.ogn` files and generates `*Database.py` modules) and the `repo_build.prebuild_link` block:

```python
local ext = get_current_extension_info()
local ogn = get_ogn_project_information(ext, "myorg/my/ipc/nodes")
project_ext(ext)

add_ogn_dependencies(ogn, { "python/nodes" })

repo_build.prebuild_copy {
    { "python/__init__.py",  ogn.python_target_path },
    { "python/extension.py", ogn.python_target_path },
}

repo_build.prebuild_link {
    { "python/nodes",  ogn.python_target_path .. "/nodes" },
    { "python/tests",  ogn.python_target_path .. "/tests" },
}
```

### Sample Extension Reference

Source: `source/extensions/isaacsim.examples.ipc/`.

| Registered type name | Implementation | Role |
| --- | --- | --- |
| `SimpleSendSimulationClockCpp` / `SimpleSendSimulationClockPy` | C++ / Python | Forwards the simulation clock to an external process on each evaluation. Connects as a TCP client to `uri` (`host:port`). Input: `simulationTime` (`double`, seconds; connect from `IsaacReadSimulationTime`). Encodes the value as nanoseconds in an 8-byte signed int64 (little-endian) and sends it. Fires `execOut` on every evaluation. |
| `SimpleReceiveExternalStepCpp` / `SimpleReceiveExternalStepPy` | C++ / Python | Receives a step counter from an external process and exposes it to downstream nodes. Binds as a TCP server on `uri` and accepts one client. Outputs a `step` (uint32). Fires `execOut` only when a complete 4-byte message arrives. Partial reads are buffered across evaluations. |

In graphs, the full path is typically `isaacsim.examples.ipc.<TypeName>` (refer to the extension’s `config/extension.toml`).

C++ and Python follow the same sequence in `compute`. They only differ by name and state wiring. For example, `reset()` compared to `custom_reset()`, and C++ `state` from the OGN database compared to Python `internal_state()`.

```python
compute(db)
     │
     ├─► uri (or relevant inputs) changed? ──yes──► teardown transport
     │                    C++: state.reset()    Python: custom_reset()
     ▼
try open: connect or listen / accept
     │         (retry next eval if not ready)
     ▼
transport ready? ──no──► return false
     │    (recv: often "no full message yet")
     yes
     ▼
framed try-send / try-recv  (see Performance Considerations for time budget)
     │
     ▼
write db.outputs and set execOut
     │
     ▼
return true/false  (per node type / sample rules)
```

## Use Your Nodes in Isaac Sim

### Enable Your Extension and Find Your Nodes

Note

If you have not yet replaced the scaffold placeholders, you can follow the steps below using `isaacsim.examples.ipc` as a stand-in — it ships with Isaac Sim and has fully working nodes ready to enable and find. Repeat the steps with your own extension name once you have implemented and built your nodes.

The build (`./build.sh` on Linux, `.\build.bat` on Windows) compiles your extension and places the output under `_build/<platform>/release/exts/<extension_name>/` (`linux-x86_64` or `windows-x86_64` depending on host). Isaac Sim launched from the same repo automatically searches that directory, so no additional path configuration is needed.

Note

Always launch Isaac Sim from the repo build. A separately installed Isaac Sim does not search the repository `exts/` directory and will not find your extension. After each build run, restart Isaac Sim — a loaded C++ plugin cannot be hot-swapped.

Launch (or restart) Isaac Sim from the repo build:

Linux

```python
./_build/linux-x86_64/release/isaac-sim.sh
```

Windows

```python
.\_build\windows-x86_64\release\isaac-sim.bat
```

Then enable your extension:

1. Open **Window > Extensions**.
2. Search for your extension name (for example `isaacsim.my.ipc.nodes`) and enable it.

Your nodes then appear in the Action Graph node library under the category you chose during scaffolding. Search by the `uiName` value defined in your `.ogn` file (for the scaffold defaults: `Example C++ Node` and `Example Python Node`).

### Building an Example Graph

The steps below build the sample graph for `tcp_tutorial_playback_bridge.py` using the reference nodes from `isaacsim.examples.ipc`. Use it to verify the end-to-end IPC pattern before wiring in your own nodes.

1. Enable the sample extension. **Open Window > Extensions**, search for `isaacsim.examples.ipc`, and enable IPC OmniGraph Node Examples.
2. Open the Action Graph editor. **Window > Graph Editors > Action Graph**.
3. Place the tutorial nodes. Under Isaac Examples in the node library, add Receive External Step and Send Simulation Clock. Use the search box to add On Playback Tick and Isaac Read Simulation Time from `isaacsim.core.nodes`. Either C++ or Python node pair works with the bridge script.
4. Wire the graph.

   Execution chain:

   * On Playback Tick `execOut` → Receive External Step `execIn`
   * Receive External Step `execOut` → Send Simulation Clock `execIn`

   Data:

   * Isaac Read Simulation Time `simulationTime` → Send Simulation Clock `simulationTime`

   The default `uri` values are `127.0.0.1:9001` on the receive node and `127.0.0.1:9000` on the send node.
5. **Start playback.** Click the **Play** button in the toolbar (or press **Space**) to begin the simulation.

General Action Graph UI is covered in [Isaac Sim OmniGraph Tutorial](omnigraph_tutorial.html#isaac-sim-app-tutorial-gui-omnigraph) and in the OmniGraph documentation linked in [Before You Start](#before-you-start).

After the graph is wired and playback is running, Receive External Step listens on its URI, the bridge script connects and sends the first step token, and Send Simulation Clock reports the current simulation time back to the script after each tick. The script drives the timing loop and Isaac Sim advances one tick per received step.

Try it: run the bridge with your own node

Once the reference graph works end-to-end with `isaacsim.examples.ipc` nodes, substitute your custom node:

1. In the graph, delete the `SimpleSendSimulationClock` node.
2. Add your renamed node from the exercise above.
3. Wire it the same way: Receive External Step `execOut` → your node `execIn`, and Isaac Read Simulation Time `simulationTime` → your node `simulationTime`.
4. Run the bridge script. Because `transfer()` is still a stub that returns `true` without sending data, the script will connect but receive no clock output — that is expected. This confirms that your extension loads, enables, and participates in the graph.
5. To complete the implementation, add the actual send logic to `transfer()`. Use `OgnSimpleSendSimulationClockCpp.cpp` (or the Python equivalent) in `source/extensions/isaacsim.examples.ipc/` as a reference.

### External Python Playback Bridge

The `tcp_tutorial_playback_bridge.py` script demonstrates a complete roundtrip. It listens for the eight-byte clock that the Send node emits, connects to the Receive node’s listen port, primes one step, then for each frame reads the clock and sends back the next step so the next `OnPlaybackTick` can fire.

The script only uses the Python standard library (`socket`, `struct`, `argparse`) and has no Isaac Sim or third-party dependencies. Run it from the repo root with any system `python3`:

```python
python3 source/extensions/isaacsim.examples.ipc/python/scripts/tcp_tutorial_playback_bridge.py
```

Pass `--help` to see `--clock-host`, `--clock-port`, `--step-host`, `--step-port`, and `--max-frames` options.

Warning

The script binds a TCP listener on `127.0.0.1`. For real deployments, bind only to loopback unless you intentionally expose a port. Open interfaces can increase attack surface. Treat any IPC bridge like a network service, where authentication, TLS or equivalent, and firewall rules are your responsibility.

## Performance Considerations

**Stay within your frame budget.**

> OmniGraph evaluates `compute` on paths that must stay responsive relative to simulation, UI, and other graphs. The usual failure mode is unpredictably long work and is not “synchronous” I/O by itself. Waiting on a slow peer, large copies, contended locks, or RPC that can stall for many milliseconds may cause performance issues.

**Small, fast paths are often fine.**

> A tiny, fixed-size, fire-and-forget operation in `compute` (the tutorial’s eight byte clock send once the socket is connected) can stay on the graph thread if it consistently completes within your per-node budget at the target frame rate. The same applies to other stacks when you have measured the path and it does not wait on back-pressure from the remote side.

**When to use workers, queues, or async APIs.**

> * If a call can block for an unknown duration (request/response, readiness waits, large payloads, or anything that can exceed your per-node budget), run that IPC on a worker thread. Use callbacks that enqueue results, and keep `compute` to non-blocking dequeue and writing `db.outputs`.
> * For inbound data, try-receive (as in the tutorial’s step node) avoids waiting indefinitely when the external process does not send on your schedule.
> * **Async or callback-based I/O:** Drive network or IPC on a worker thread, push decoded messages into a thread-safe queue, and let `compute` only dequeue (non-blocking) and write `db.outputs`.
> * **Deferred completion:** Post work from `compute` without waiting for the reply. A background thread enqueues results for a later evaluation.

**Structured messages vs fixed bytes.**

> The fixed-size framing in the tutorial is for clarity. A production bridge typically uses your library’s message format (IDL-generated types, JSON, or another schema). You still decide when to send, how to parse inbound data, and how to keep each `compute` within budget.

**Large messages (camera frames, point clouds).**

> Single-shot calls that move multi-megabyte payloads can stress memory and scheduling. Use streaming APIs, explicit back-pressure (drop or skip frames on a slow consumer), or shared-memory and zero-copy paths outside OmniGraph, with the node passing only handles or small metadata.

## Built-In Nodes for Data in and Out

Besides `isaacsim.examples.ipc`, several extensions register OmniGraph nodes that read simulation state or drive simulation inside Isaac Sim, without acting as a general-purpose bridge to another process. The table highlights types that often sit next to custom IPC nodes in a bridge graph.

Before designing your custom node’s inputs and outputs, check the `.ogn` of the built-in nodes you plan to connect to—their output attribute names and types determine what your node needs to consume or produce.

Common built-in OmniGraph nodes for bridge-style graphs

| Goal | Node (registered type) | Extension | Key inputs / outputs (abbrev.) |
| --- | --- | --- | --- |
| Read joint positions / velocities (and efforts) for publishing | `IsaacArticulationState` | `isaacsim.core.nodes` | In: `robotPath` or `targetPrim`, optional `jointNames` / `jointIndices`. Out: `jointPositions`, `jointVelocities` (`double[]`), `jointNames` (`token[]`), plus measured effort arrays. |
| Alternative joint state (physics sensor path) | `isaacsim.sensors.physics.IsaacReadJointState` | `isaacsim.sensors.physics.nodes` | In: `prim` (articulation root). Out: `jointPositions`, `jointVelocities`, `jointEfforts`, `jointNames`, `execOut`, etc. |
| Apply joint position / velocity / effort commands | `IsaacArticulationController` | `isaacsim.core.nodes` | In: same robot targeting as above; `positionCommand`, `velocityCommand`, `effortCommand` (`double[]`). Angular units are radians at the controller API. |
| Simulation tick / gating | `OnPhysicsStep`, `IsaacSimulationGate`, `IsaacReadSimulationTime`, … | `isaacsim.core.nodes` | Use to pace state reads and command writes consistently (exact attributes vary by node). |
| Camera / viewport render product path (setup only) | `IsaacGetViewportRenderProduct`, `IsaacCreateRenderProduct`, `IsaacAttachHydraTexture`, `IsaacSetCameraOnRenderProduct` | `isaacsim.core.nodes` | Mostly paths and targets (`renderProductPath`, `renderProductPrim`). Pixels require a separate readback step. Refer to [Camera and Render Products](#camera-and-render-products). |

Other read extensions you can chain before a custom sender:

* `isaacsim.sensors.physics.nodes` — IMU, contact, effort, etc., backed by `isaacsim.sensors.experimental.physics`.
* `isaacsim.sensors.physx` — for example Isaac Read Lidar Beams, Isaac Read Lidar Point Cloud, Isaac Read Light Beam Sensor.
* `isaacsim.sensors.rtx.nodes` — for example Isaac Extract RTX Sensor Point Cloud.

For IPC with external applications (topics, services, or other runtimes), use dedicated bridge extensions rather than treating the nodes in the table above as a transport layer. Examples include `isaacsim.ros2.nodes` (ROS 2) or `isaacsim.ucx.nodes` (UCX). Those extensions play the same role as the TCP tutorial nodes, not the sensor-read nodes in the table.

**Reference implementations in this repository.**

> The `source/extensions/` directory contains full IPC bridge implementations
> you can study when you outgrow the TCP tutorial. Two stacks are available:
>
> > * **ROS 2**: `isaacsim.ros2.nodes`, `isaacsim.ros2.bridge`, and related
> >   packages.
> > * **UCX**: `isaacsim.ucx.nodes`, `isaacsim.ucx.core`,
> >   `isaacsim.ucx.bridge`.
>
> Each stack shows how a complete bridge is laid out: `extension.toml`
> dependencies, native plugins, C++ and Python OmniGraph nodes, and transport
> backends.

Use the OmniGraph node library in the Kit docs to search by name: [OmniGraph](https://docs.omniverse.nvidia.com/extensions/latest/ext_omnigraph.html "(in Omniverse Extensions)").

## Camera and Render Products

Getting raw RGB pixels into a custom IPC node requires more than a plain `uchar[]` OGN input. Imagery typically flows through a Replicator pipeline or a render product chain before reaching any IPC encoder, not a single wire in the graph editor. The key steps are:

> 1. Set up a render product (`IsaacCreateRenderProduct` or `IsaacGetViewportRenderProduct`) and attach a camera.
> 2. Feed the render product into a readback mechanism either a:
>
>    * Replicator annotator (host-friendly NumPy arrays)
>    * Hydra texture chain (GPU handles through `IsaacAttachHydraTexture`)
> 3. Pass the resulting CPU-addressable bytes or arrays into your IPC encoder node.

The `isaacsim.ros2.bridge` extension’s camera helper node is a concrete reference for how this pipeline is assembled. The ROS 2 camera publisher wires a render product to host readback and then to IPC. Browsing that source is the fastest way to understand the pattern before building your own.

Refer to [Performance Considerations](#performance-considerations) before passing large buffers through `compute`. Camera frames are a common source of frame-budget overruns.

## Testing Your OmniGraph Node Implementation

Python integration tests for OmniGraph nodes can build Action Graphs at runtime
using `og.Controller.edit`, wire nodes together programmatically, drive the
timeline, and assert on output attribute values. Useful areas to cover:

* **Correct outputs**: Given known inputs, the node produces the expected
  `db.outputs` values.
* **execOut timing**: The node fires `execOut` only under the intended
  conditions. For send nodes, this means every evaluation. For receive nodes,
  this means only on data receipt.
* **Reset behavior**: Changing a URI input or stopping the timeline closes the
  transport, and a subsequent evaluation reopens it cleanly.
* **Edge cases**: Partial messages, peer disconnect, and malformed data from the
  external process.

For C++ helpers (parsing, encoding, and endianness), unit tests can run outside
Isaac Sim through a native test library such as doctest, wired in
`premake5.lua` and referenced from `extension.toml`.

Point `[[test]]` entries in your `extension.toml` at your test modules. The
generated test driver is typically
`_build/<platform>/<config>/tests/tests-<your.extension.id>.sh`. For a
scaffolded extension, tests go in `python/tests/` (already created by the
template).

For examples of the patterns above (async tests, `OnImpulseEvent`, free-port
helpers, and timeline control), refer to
`source/extensions/isaacsim.examples.ipc/python/tests/`.

On this page

* [Before You Start](#before-you-start)
* [Scaffold Your Extension](#scaffold-your-extension)
* [Add Your Transport Library](#add-your-transport-library)
  + [Python](#python)
  + [C++](#c)
* [Design and Implement Your Nodes](#design-and-implement-your-nodes)
  + [Design Principle](#design-principle)
  + [What Every IPC Node Requires](#what-every-ipc-node-requires)
  + [OGN Schema Quick Reference](#ogn-schema-quick-reference)
  + [C++ Node Implementation](#c-node-implementation)
  + [Python Node Implementation](#python-node-implementation)
  + [Sample Extension Reference](#sample-extension-reference)
* [Use Your Nodes in Isaac Sim](#use-your-nodes-in-isaac-sim-short)
  + [Enable Your Extension and Find Your Nodes](#enable-your-extension-and-find-your-nodes)
  + [Building an Example Graph](#building-an-example-graph)
  + [External Python Playback Bridge](#external-python-playback-bridge)
* [Performance Considerations](#performance-considerations)
* [Built-In Nodes for Data in and Out](#built-in-nodes-for-data-in-and-out)
* [Camera and Render Products](#camera-and-render-products)
* [Testing Your OmniGraph Node Implementation](#testing-your-omnigraph-node-implementation)

---

### OmniGraph Shortcuts

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/omnigraph/omnigraph_shortcuts.html

* [OmniGraph](index.html)
* Commonly Used OmniGraph Shortcuts

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Commonly Used OmniGraph Shortcuts

Isaac Sim has shortcuts for populating some of the most commonly used OmniGraphs. They can be found under **Tools > Robotics > OmniGraph Controllers**. After selecting the graph you want to create, you are prompted to provide a minimal set of parameters to populate the graph.

The shortcuts are:

[Controller Graphs](#omnigraph-shortcuts-controller-graphs)

* Joint Position Controller
* Joint Velocity Controller
* Differential Controller
* Open Loop Gripper Controller

For information on how to use ROS Graphs, go to each of the relevant [ROS 2 Tutorials (Linux and Windows)](../ros2_tutorials/index.html#isaac-ros2-tutorials-page).

Note

* *No* validation is done to detect a graph with the same tasks or that controls the same robot. You must ensure that your graphs are unique in the scene.
* These are just shortcuts to create the graph. You can always modify the graph after it’s created to suit your needs.

To use Python scripting to create these graphs:

> 1. Click on the icon next to **Python Script for Graph Generation** on the bottom of the popup window.
>    It takes you to the Python script used to generate the graphs for the given shortcut.
> 2. `make_graph()` is where the creation occurs. The relevant commands may or may not all be in one continuous block depending on how the shortcut is setup.

## Controller Graphs

The controller shortcuts for moving the robots are:

* Articulation (Joint Position and Velocity) Controllers
* Differential Drive Controller
* Gripper Controllers

### Articulation Controllers

Both Position and Velocity Controllers issue commands directly to each joint in the articulation.

* **Robot Prim**: The parent prim of the robot.
* **Graph Path**: The path to the graph generated. It is default to be under an independent tree called “/Graph/{type}\_controller”. If a graph already exist in the path given, it’ll find the next available path by appending a number to the end of that path.
* **Add to Existing Graph** (optional): Default to False. If checked, it’ll add the nodes to an existing graph and use an existing tick node if there exist one, but will add new controller nodes regardless of existing ones.

#### Use the Articulation Controller

To use the controller to move the robot:

1. Highlight the **JointCommandArray** node under the newly created graph.
2. Press *play* to start the simulation.
3. Move the robot by changing the values in the **JointCommandArray** node in the Property Tab.

If you had initial targets for position or velocity saved as part of the USD, it immediately moves towards those targets when you press **play**.

### Differential Controller

The Differential Controller takes in linear and angular velocities and converts them to individual wheel velocities.

* **Robot Prim**: The Robot Prim.
* **Graph Path**: The path to the graph generated. By default, it is under an independent tree called “/Graph/{type}\_controller”. If a graph already exist in the path given, it finds the next available path by appending a number to the end of that path.
* **Wheel Radius**: The radius of the wheel in meters.
* **Distance between wheels**: The distance between the two wheels in meters.
* **Left/Right Joint Names** (optional): Names of the joints that control the left and right wheels.
* **Left/Right Joint Index** (optional): The index of the joints that control the left and right wheels in the articulation chain.
* **Use Keyboard Control** (optional): Default to none. If checked, it also populates the graph that receives WASD as keyboard inputs to move the robot forward, backward, spin left, and spin right.
* **Add to Existing Graph** (optional): Defaults to False. If checked, it adds the nodes to an existing graph and uses an existing tick node if there is one, but will add new controller nodes regardless of existing ones.

#### Use the Differential Controller

* In some robots, there are only two controllable joints, so you do not have to specify joint names or indices. For robots with multiple actuated joints in an articulation chain, you must specify either the names or the indices of the joints that control the left and right wheels. List the left wheel before the right wheel so the order matches the Differential Controller output.
* If you did not include the WASD keyboard control in the graph, you can always test the controller by manually changing the “Desired Angular Velocity” and “Desired Linear Velocity” in the **DifferentialController** node under the newly created graph.

* If you are using the WASD Keyboard control, there are two scaling values used to scale the binary input from the keyboard to a linear velocity and an angular velocity that make sense for the vehicle’s size. The values are inside the nodes “ScaleLinear” and “ScaleAngular” respectively. You can print the output of the “DifferentialController” node to see relative affects of the scaling values. You want to tune them so that the rotating commands results in similar magnitude changes in the wheels’ velocities as the forward and backward commands.

* If you are using Isaac Sim Assets, the default values of the wheel radius and distance between wheels can be found on the bottom of the page for Wheeled Robots in [Robot Assets](../assets/usd_assets_robots.html#isaac-assets-robots)

### Gripper Controller

The Gripper Controller works for any end-effector that has only one-degree of actuation per finger. This includes all parallel jaw grippers, as well as any multi-finger, multi-DOF-per-finger hands where each finger has only one degree of actuation.

* **Parent Robot**: The robot that contains the gripper. This could be the gripper itself, or if the gripper is part of an arm, this could be the prim for the entire manipulator.
* **Gripper Root**: The prim that contains all the gripper joints.
* **Graph Path**: The path to the graph generated. It is default to be under an independent tree called “/Graph/{type}\_controller”. If a graph already exists in the path given, it finds the next available path by appending a number to the end of that path.
* **Gripper Speed**: The speed at which the gripper closes or opens in meters (or radian) per second.
* **Gripper Joint Names**: The names of the joints that control the gripper fingers. List them all out separated by commas.
* **Open/Close Position Limit** (optional): The joint position that’s considered fully open. Unit: meter (prismatic) or radian (revolute). If left blank, it defaults to the joint limits inside the asset’s USD file.
* **Use Keyboard Control** (optional): Default to none. If checked, it populates the graph that receives “O”,”C”, and “N” as keyboard inputs to open, close, and stop the gripper.
* **Add to Existing Graph** (optional): Defaults to False. If checked, it adds the nodes to an existing graph and uses an existing tick node if one exists, but will add new controller nodes regardless of existing ones.

#### Use the Gripper Controller

If no joint limits are given, the gripper defaults to the joint limits inside the asset’s USD file. If the Open Position Limit and Close Position Limit are flipped, the gripper controller automatically corrects for it. The controller makes the assumption that the joint limits for opened position is greater than closed position. So if it is the opposite for your gripper, you would have to either adjust your definition of open and close or modify the Python script accordingly.

* Only uniform speed and same joint limits are supported using the shortcut. If you want variable speed or different joint limits for each of the fingers, you can modify the graph by adding arrays for the speed and joint limit inputs.
* If the articulation chain you are working with contains both an arm and a gripper and you wish to control the arm using the Articulcation Position Controller and the Gripper Controller for the gripper separately:

  1. Remove the joints that control the gripper from the arm controller graph.
  2. Validate that there is no conflict between the two graphs.

On this page

* [Controller Graphs](#controller-graphs)
  + [Articulation Controllers](#articulation-controllers)
    - [Use the Articulation Controller](#use-the-articulation-controller)
  + [Differential Controller](#differential-controller)
    - [Use the Differential Controller](#use-the-differential-controller)
  + [Gripper Controller](#gripper-controller)
    - [Use the Gripper Controller](#use-the-gripper-controller)

---

