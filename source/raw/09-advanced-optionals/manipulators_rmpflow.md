---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/manipulators/manipulators_rmpflow.html
title: "RMPflow Tutorial"
section: "Manipulators"
module: "09-advanced-optionals"
checksum: "b8ef8d1329674795"
fetched: "2026-06-21T13:05:42"
---

* [Robot Simulation](../robot_simulation/index.html)
* [Motion Generation (Deprecated)](motion_generation_overview.html)
* Lula RMPflow

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Lula RMPflow

Deprecated

For new development, consider using the newer [Robot Motion (Experimental)](../robot_motion_experimental/index.html) API, which provides improved interfaces and additional features over Lula.

This tutorial shows how the [RMPflow](concepts/rmpflow.html#isaac-sim-motion-generation-rmpflow) class in the [Motion Generation](concepts/index.html#isaac-sim-motion-generation) can be used to
generate smooth motions to reach task-space targets while avoiding dynamic obstacles. This tutorial demonstrates how:

* `RmpFlow` can be directly instantiated and used to generate motions using a custom robot description file
* `RmpFlow` can be loaded and used on supported robots
* built-in debugging features can improve easy of use and integration

## Getting Started

**Prerequisites**

* Complete the [Adding a Manipulator Robot](../core_api_tutorials/tutorial_core_adding_manipulator.html#isaac-sim-app-tutorial-core-adding-manipulator) tutorial prior to beginning this tutorial.
* Review the [Loaded Scenario Extension Template](../utilities/extension_templates_tutorial.html#isaac-sim-app-tutorial-extension-templates-loaded-scenario) to understand how this tutorial is structured and run.

To follow along with the tutorial, run your Isaac Sim 6.0 instance. Then open **Window > Extensions**, search for **Motion Generation Examples** (`isaacsim.robot_motion.motion_generation.examples`), and enable it. If you cannot find it, remove `@feature` from the Extensions search bar and search again.
Within the isaacsim.robot\_motion.motion\_generation.examples extension, there is a fully functional example of RMPflow including following a target, world awareness,
and a debugging option. The sections of this tutorial build up the file `scenario.py` from basic functionality to the completed code.

Note

**Motion Generation Examples** (`isaacsim.robot_motion.motion_generation.examples`) are deprecated **since Isaac Sim 6.0.0**. In the Isaac Sim source repository they live under `source/deprecated/isaacsim.robot_motion.motion_generation.examples`; the extension id is unchanged.

**Replacement:** Use the `isaacsim.robot_motion.cumotion.examples` extension and the [cuMotion Integration](../cumotion/index.html) tutorials.

## Generating Motions with an RMPflow Instance

[RMPflow](concepts/rmpflow.html#isaac-sim-motion-generation-rmpflow) is used heavily throughout NVIDIA Isaac Sim for controlling robot manipulators. As documented
in [RMPflow Configuration](concepts/rmpflow.html#isaac-sim-motion-generation-rmpflow-configuration), there are three configuration files needed to directly instantiate the `RmpFlow` class directly.
After these configuration files are loaded and an end effector target has been specified, actions can be computed to move the robot to the desired target.

```python
import os

import numpy as np
from isaacsim.core.api.objects.cuboid import FixedCuboid
from isaacsim.core.prims import SingleArticulation as Articulation
from isaacsim.core.prims import SingleXFormPrim as XFormPrim
from isaacsim.core.utils.extensions import get_extension_path_from_name
from isaacsim.core.utils.numpy.rotations import euler_angles_to_quats
from isaacsim.core.utils.stage import add_reference_to_stage
from isaacsim.robot_motion.motion_generation import ArticulationMotionPolicy, RmpFlow
from isaacsim.storage.native import get_assets_root_path

class FrankaRmpFlowExample:
    def __init__(self):
        self._rmpflow = None
        self._articulation_rmpflow = None

        self._articulation = None
        self._target = None

    def load_example_assets(self):
        # Add the Franka and target to the stage
        # The position in which things are loaded is also the position in which they

        robot_prim_path = "/panda"
        path_to_robot_usd = get_assets_root_path() + "/Isaac/Robots/FrankaRobotics/FrankaPanda/franka.usd"

        add_reference_to_stage(path_to_robot_usd, robot_prim_path)
        self._articulation = Articulation(robot_prim_path)

        add_reference_to_stage(get_assets_root_path() + "/Isaac/Props/UIElements/frame_prim.usd", "/World/target")
        self._target = XFormPrim("/World/target", scale=[0.04, 0.04, 0.04])

        # Return assets that were added to the stage so that they can be registered with the core.World
        return self._articulation, self._target

    def setup(self):
        # RMPflow config files for supported robots are stored in the motion_generation extension under "/motion_policy_configs"
        mg_extension_path = get_extension_path_from_name("isaacsim.robot_motion.motion_generation")
        rmp_config_dir = os.path.join(mg_extension_path, "motion_policy_configs")

        # Initialize an RmpFlow object
        self._rmpflow = RmpFlow(
            robot_description_path=rmp_config_dir + "/franka/rmpflow/robot_descriptor.yaml",
            urdf_path=rmp_config_dir + "/franka/lula_franka_gen.urdf",
            rmpflow_config_path=rmp_config_dir + "/franka/rmpflow/franka_rmpflow_common.yaml",
            end_effector_frame_name="right_gripper",
            maximum_substep_size=0.00334,
        )

        # Use the ArticulationMotionPolicy wrapper object to connect rmpflow to the Franka robot articulation.
        self._articulation_rmpflow = ArticulationMotionPolicy(self._articulation, self._rmpflow)

        self._target.set_world_pose(np.array([0.5, 0, 0.7]), euler_angles_to_quats([0, np.pi, 0]))

    def update(self, step: float):
        # Step is the time elapsed on this frame
        target_position, target_orientation = self._target.get_world_pose()

        self._rmpflow.set_end_effector_target(target_position, target_orientation)

        action = self._articulation_rmpflow.get_next_articulation_action(step)
        self._articulation.apply_action(action)

    def reset(self):
        # Rmpflow is stateless unless it is explicitly told not to be

        self._target.set_world_pose(np.array([0.5, 0, 0.7]), euler_angles_to_quats([0, np.pi, 0]))
```

`RMPflow` is an implementation of the [Motion Policy Algorithm](concepts/motion_policy.html#isaac-sim-motion-policy) interface.
Any MotionPolicy can be passed to an [Articulation Motion Policy](concepts/motion_policy.html#isaac-sim-articulation-motion-policy)
to start moving a robot on the USD stage. On line 43, an instance of `RmpFlow` is instantiated
with the required configuration information. The `ArticulationMotionPolicy` created on line 52 acts as a
translational layer between `RmpFlow` and the simulated Franka robot `Articulation`. You can interact with
`RmpFlow` directly to communicate the world state, set an end effector target, or modify internal settings.
On each frame, an end effector target is passed directly to the `RmpFlow` object (line 60).
The `ArticulationMotionPolicy` is used on line 64 to compute an action that can be directly consumed by the
Franka `Articulation`.

Note

The RMPflow algorithm takes in consideration the robot structure provided by the configuration URDF file. If working on a robot with assembled components (for example, a UR10 with a gripper attached), the URDF file should be updated to reflect the correct robot structure and contain the offset of the gripper at the end effector frame, or additional control joints. The final assembly URDF can be exported with the [USD to URDF Exporter](../importer_exporter/ext_omni_exporter_urdf.html#isaac-sim-app-extension-urdf-exporter). When modifying the source URDF file, it is recommended to review and update the [Robot Description file](manipulators_robot_description_editor.html#isaac-sim-app-tutorial-motion-generation-robot-description-editor) to ensure that the correct supplemental file is being used.

### World State

As a [Motion Policy Algorithm](concepts/motion_policy.html#isaac-sim-motion-policy), `RmpFlow` is capable of dynamic collision avoidance
while navigating the end effector to a target. The world state can be
changing over time while `RmpFlow` is navigating to its target. Objects created with the `isaacsim.core.api.objects` package
(see [Inputs: World State](concepts/motion_policy.html#isaac-sim-motion-policy-world-state)) can be registered with `RmpFlow` and the policy will automatically avoid collisions with these obstacles.
`RmpFlow` is triggered to query the current state of all tracked objects whenever `RmpFlow.update_world()` is called.

`RmpFlow` can also be informed about a change in the robot base pose on a given frame by calling `RmpFlow.set_robot_base_pose()`.
As object positions are queried in world coordinates, it is critical to use this function, if the base of the robot is moved
within the USD stage.

```python
import os

import numpy as np
from isaacsim.core.api.objects.cuboid import FixedCuboid
from isaacsim.core.prims import SingleArticulation as Articulation
from isaacsim.core.prims import SingleXFormPrim as XFormPrim
from isaacsim.core.utils.extensions import get_extension_path_from_name
from isaacsim.core.utils.numpy.rotations import euler_angles_to_quats
from isaacsim.core.utils.stage import add_reference_to_stage
from isaacsim.robot_motion.motion_generation import ArticulationMotionPolicy, RmpFlow
from isaacsim.robot_motion.motion_generation.interface_config_loader import (
    get_supported_robot_policy_pairs,
    load_supported_motion_policy_config,
)
from isaacsim.storage.native import get_assets_root_path

class FrankaRmpFlowExample:
    def __init__(self):
        self._rmpflow = None
        self._articulation_rmpflow = None

        self._articulation = None
        self._target = None

    def load_example_assets(self):
        # Add the Franka and target to the stage
        # The position in which things are loaded is also the position in which they

        robot_prim_path = "/panda"
        path_to_robot_usd = get_assets_root_path() + "/Isaac/Robots/FrankaRobotics/FrankaPanda/franka.usd"

        add_reference_to_stage(path_to_robot_usd, robot_prim_path)
        self._articulation = Articulation(robot_prim_path)

        add_reference_to_stage(get_assets_root_path() + "/Isaac/Props/UIElements/frame_prim.usd", "/World/target")
        self._target = XFormPrim("/World/target", scale=[0.04, 0.04, 0.04])

        self._obstacle = FixedCuboid(
            "/World/obstacle", size=0.05, position=np.array([0.4, 0.0, 0.65]), color=np.array([0.0, 0.0, 1.0])
        )

        # Return assets that were added to the stage so that they can be registered with the core.World
        return self._articulation, self._target, self._obstacle

    def setup(self):
        # RMPflow config files for supported robots are stored in the motion_generation extension under "/motion_policy_configs"
        mg_extension_path = get_extension_path_from_name("isaacsim.robot_motion.motion_generation")
        rmp_config_dir = os.path.join(mg_extension_path, "motion_policy_configs")

        # Initialize an RmpFlow object
        self._rmpflow = RmpFlow(
            robot_description_path=rmp_config_dir + "/franka/rmpflow/robot_descriptor.yaml",
            urdf_path=rmp_config_dir + "/franka/lula_franka_gen.urdf",
            rmpflow_config_path=rmp_config_dir + "/franka/rmpflow/franka_rmpflow_common.yaml",
            end_effector_frame_name="right_gripper",
            maximum_substep_size=0.00334,
        )
        self._rmpflow.add_obstacle(self._obstacle)

        # Use the ArticulationMotionPolicy wrapper object to connect rmpflow to the Franka robot articulation.
        self._articulation_rmpflow = ArticulationMotionPolicy(self._articulation, self._rmpflow)

        self._target.set_world_pose(np.array([0.5, 0, 0.7]), euler_angles_to_quats([0, np.pi, 0]))

    def update(self, step: float):
        # Step is the time elapsed on this frame
        target_position, target_orientation = self._target.get_world_pose()

        self._rmpflow.set_end_effector_target(target_position, target_orientation)

        # Track any movements of the cube obstacle
        self._rmpflow.update_world()

        # Track any movements of the robot base
        robot_base_translation, robot_base_orientation = self._articulation.get_world_pose()
        self._rmpflow.set_robot_base_pose(robot_base_translation, robot_base_orientation)

        action = self._articulation_rmpflow.get_next_articulation_action(step)
        self._articulation.apply_action(action)

    def reset(self):
        # Rmpflow is stateless unless it is explicitly told not to be

        self._target.set_world_pose(np.array([0.5, 0, 0.7]), euler_angles_to_quats([0, np.pi, 0]))
```

On lines 22, an obstacle is added to the stage, and on line 40, it is registered as an obstacle with `RmpFlow`.
On each frame, `RmpFlow.update_world()` is called (line 56). This triggers `RmpFlow` to query the current position of the cube to account for any movement.

On lines 59-60, the current position of the robot base is queried and passed to `RmpFlow`.
This step is separated from other world state because
it is often unnecessary (when the robot base never moves from the origin), or this step might require extra consideration
(for example, `RmpFlow` is controlling an arm that is mounted on a moving base).

## Loading RMPflow for Supported Robots

In the previous sections, observe that `RmpFlow` requires five arguments to be initialized. Three of these arguments are file paths to required configuration files.
The `end_effector_frame_name` argument specifies what frame on the robot (from the frames found in the referenced URDF file) should be considered the end effector.
The `maximum_substep_size` argument specifies a maximum step-size when internally performing the Euler Integration.

For manipulators in the NVIDIA Isaac Sim library, appropriate config information for loading RmpFlow can be found in the `isaacsim.robot_motion.motion_generation` extension.
This information is indexed by robot name and can be accessed simply.
The following change shows how loading configs for supported robots can be simplified.

```python
import os

import numpy as np
from isaacsim.core.api.objects.cuboid import FixedCuboid
from isaacsim.core.prims import SingleArticulation as Articulation
from isaacsim.core.prims import SingleXFormPrim as XFormPrim
from isaacsim.core.utils.extensions import get_extension_path_from_name
from isaacsim.core.utils.numpy.rotations import euler_angles_to_quats
from isaacsim.core.utils.stage import add_reference_to_stage
from isaacsim.robot_motion.motion_generation import ArticulationMotionPolicy, RmpFlow
from isaacsim.robot_motion.motion_generation.interface_config_loader import (
    get_supported_robot_policy_pairs,
    load_supported_motion_policy_config,
)
from isaacsim.storage.native import get_assets_root_path

class FrankaRmpFlowExample:
    def __init__(self):
        self._rmpflow = None
        self._articulation_rmpflow = None

        self._articulation = None
        self._target = None

    def load_example_assets(self):
        # Add the Franka and target to the stage
        # The position in which things are loaded is also the position in which they

        robot_prim_path = "/panda"
        path_to_robot_usd = get_assets_root_path() + "/Isaac/Robots/FrankaRobotics/FrankaPanda/franka.usd"

        add_reference_to_stage(path_to_robot_usd, robot_prim_path)
        self._articulation = Articulation(robot_prim_path)

        add_reference_to_stage(get_assets_root_path() + "/Isaac/Props/UIElements/frame_prim.usd", "/World/target")
        self._target = XFormPrim("/World/target", scale=[0.04, 0.04, 0.04])

        self._obstacle = FixedCuboid(
            "/World/obstacle", size=0.05, position=np.array([0.4, 0.0, 0.65]), color=np.array([0.0, 0.0, 1.0])
        )

        # Return assets that were added to the stage so that they can be registered with the core.World
        return self._articulation, self._target, self._obstacle

    def setup(self):
        # Loading RMPflow can be done quickly for supported robots
        print("Supported Robots with a Provided RMPflow Config:", list(get_supported_robot_policy_pairs().keys()))
        rmp_config = load_supported_motion_policy_config("Franka", "RMPflow")

        # Initialize an RmpFlow object
        self._rmpflow = RmpFlow(**rmp_config)
        self._rmpflow.add_obstacle(self._obstacle)

        # Use the ArticulationMotionPolicy wrapper object to connect rmpflow to the Franka robot articulation.
        self._articulation_rmpflow = ArticulationMotionPolicy(self._articulation, self._rmpflow)

        self._target.set_world_pose(np.array([0.5, 0, 0.7]), euler_angles_to_quats([0, np.pi, 0]))

    def update(self, step: float):
        # Step is the time elapsed on this frame
        target_position, target_orientation = self._target.get_world_pose()

        self._rmpflow.set_end_effector_target(target_position, target_orientation)

        # Track any movements of the cube obstacle
        self._rmpflow.update_world()

        # Track any movements of the robot base
        robot_base_translation, robot_base_orientation = self._articulation.get_world_pose()
        self._rmpflow.set_robot_base_pose(robot_base_translation, robot_base_orientation)

        action = self._articulation_rmpflow.get_next_articulation_action(step)
        self._articulation.apply_action(action)

    def reset(self):
        # Rmpflow is stateless unless it is explicitly told not to be

        self._target.set_world_pose(np.array([0.5, 0, 0.7]), euler_angles_to_quats([0, np.pi, 0]))
```

A supported set of robots can have their RMPflow configs loaded by name.
Line 34 prints the names of every supported robot with a provided RMPflow config (at the time of writing this tutorial):

> [âFrankaâ, âUR3â, âUR3eâ, âUR5â, âUR5eâ, âUR10â, âUR10eâ, âUR16eâ, âRizon4â, âCobotta\_Pro\_900â, âCobotta\_Pro\_1300â, âRS007Lâ, âRS007Nâ, âRS013Nâ, âRS025Nâ, âRS080Nâ, âTechman\_TM12â, âKuka\_KR210â, âFanuc\_CRX10IALâ]

On lines 35,38, the RmpFlow class initializer is simplified to unpacking a dictionary of loaded keyword arguments.
The `load_supported_motion_policy_config()` function is the simplest way to load supported robots.

## Debugging Features

The `RmpFlow` class has contains debugging features that are not generally available in the [Motion Policy Algorithm](concepts/motion_policy.html#isaac-sim-motion-policy) interface.
These debugging features allow decoupling of the simulator from the RmpFlow algorithm to help diagnose any undesirable behaviors
that are encountered ([RMPflow Debugging Features](concepts/rmpflow.html#isaac-sim-motion-generation-rmpflow-debugging-features)).

`RmpFlow` uses collision spheres internally to avoid collisions with external objects. These spheres can be visualized with
the `RmpFlow.visualize_collision_spheres()` function. This helps to determine whether `RmpFlow` has a reasonable representation
of the simulated robot.

The visualization can be used alongside a flag `RmpFlow.set_ignore_state_updates(True)` to ignore state updates from the robot
`Articulation` and instead assume that robot joint targets returned by `RmpFlow` are always perfectly achieved. This causes `RmpFlow`
to compute a robot path over time that is independent of the simulated robot `Articulation`. At each timestep, `RmpFlow` returns joint
targets that are passed to the robot `Articulation`.

```python
import os

import numpy as np
from isaacsim.core.api.objects.cuboid import FixedCuboid
from isaacsim.core.prims import SingleArticulation as Articulation
from isaacsim.core.prims import SingleXFormPrim as XFormPrim
from isaacsim.core.utils.extensions import get_extension_path_from_name
from isaacsim.core.utils.numpy.rotations import euler_angles_to_quats
from isaacsim.core.utils.stage import add_reference_to_stage
from isaacsim.robot_motion.motion_generation import ArticulationMotionPolicy, RmpFlow
from isaacsim.robot_motion.motion_generation.interface_config_loader import (
    get_supported_robot_policy_pairs,
    load_supported_motion_policy_config,
)
from isaacsim.storage.native import get_assets_root_path

class FrankaRmpFlowExample:
    def __init__(self):
        self._rmpflow = None
        self._articulation_rmpflow = None

        self._articulation = None
        self._target = None

        self._dbg_mode = True

    def load_example_assets(self):
        # Add the Franka and target to the stage
        # The position in which things are loaded is also the position in which they

        robot_prim_path = "/panda"
        path_to_robot_usd = get_assets_root_path() + "/Isaac/Robots/FrankaRobotics/FrankaPanda/franka.usd"

        add_reference_to_stage(path_to_robot_usd, robot_prim_path)
        self._articulation = Articulation(robot_prim_path)

        add_reference_to_stage(get_assets_root_path() + "/Isaac/Props/UIElements/frame_prim.usd", "/World/target")
        self._target = XFormPrim("/World/target", scale=[0.04, 0.04, 0.04])

        self._obstacle = FixedCuboid(
            "/World/obstacle", size=0.05, position=np.array([0.4, 0.0, 0.65]), color=np.array([0.0, 0.0, 1.0])
        )

        # Return assets that were added to the stage so that they can be registered with the core.World
        return self._articulation, self._target, self._obstacle

    def setup(self):
        # Loading RMPflow can be done quickly for supported robots
        print("Supported Robots with a Provided RMPflow Config:", list(get_supported_robot_policy_pairs().keys()))
        rmp_config = load_supported_motion_policy_config("Franka", "RMPflow")

        # Initialize an RmpFlow object
        self._rmpflow = RmpFlow(**rmp_config)
        self._rmpflow.add_obstacle(self._obstacle)

        if self._dbg_mode:
            self._rmpflow.set_ignore_state_updates(True)
            self._rmpflow.visualize_collision_spheres()

            # Set the robot gains to be deliberately poor
            bad_proportional_gains = self._articulation.get_articulation_controller().get_gains()[0] / 50
            self._articulation.get_articulation_controller().set_gains(kps=bad_proportional_gains)

        # Use the ArticulationMotionPolicy wrapper object to connect rmpflow to the Franka robot articulation.
        self._articulation_rmpflow = ArticulationMotionPolicy(self._articulation, self._rmpflow)

        self._target.set_world_pose(np.array([0.5, 0, 0.7]), euler_angles_to_quats([0, np.pi, 0]))

    def update(self, step: float):
        # Step is the time elapsed on this frame
        target_position, target_orientation = self._target.get_world_pose()

        self._rmpflow.set_end_effector_target(target_position, target_orientation)

        # Track any movements of the cube obstacle
        self._rmpflow.update_world()

        # Track any movements of the robot base
        robot_base_translation, robot_base_orientation = self._articulation.get_world_pose()
        self._rmpflow.set_robot_base_pose(robot_base_translation, robot_base_orientation)

        action = self._articulation_rmpflow.get_next_articulation_action(step)
        self._articulation.apply_action(action)

    def reset(self):
        # Rmpflow is stateless unless it is explicitly told not to be
        if self._dbg_mode:
            # RMPflow was set to roll out robot state internally, assuming that all returned joint targets were hit exactly.
            self._rmpflow.reset()
            self._rmpflow.visualize_collision_spheres()

        self._target.set_world_pose(np.array([0.5, 0, 0.7]), euler_angles_to_quats([0, np.pi, 0]))
```

The collision sphere visualization can be very helpful to distinguish between behaviors that are coming from the simulator, and behaviors that are coming from `RmpFlow`.
In the image below, the Franka robot is given weak proportional gains (lines 43-44). Using the debugging visualization, it is easy to
determine that RmpFlow is producing reasonable motions, but the simulated robot is simply not able to follow the motions. When RMPflow moves the robot quickly,
the Franka robot `Articulation` lags significantly behind the commanded position.

## Summary

This tutorial reviews using the `RmpFlow` class to generate reactive motions in response to a dynamic environment. The `RmpFlow`
class can be used to generate motions directly alongside an [Articulation Motion Policy](concepts/motion_policy.html#isaac-sim-articulation-motion-policy).

This tutorial reviewed four of the main features of `RmpFlow`:

> 1. Navigating the robot through an environment to a target position and orientation.
> 2. Adapting to a dynamic world on every frame.
> 3. Adapting to a change in the robotâs position on the USD stage.
> 4. Using visualization to decouple the simulated robot `Articulation` from the RMPflow algorithm for quick and easy debugging.

### Further Learning

To learn how to configure RMPflow for a new robot, review the
[basic formalism](concepts/rmpflow.html#isaac-sim-motion-generation-rmpflow), and then read the
[RMPflow tuning guide](concepts/rmpflow_tuning_guide.html#isaac-sim-motion-generation-rmpflow-tuning-guide) for practical advice.

To understand the motivation behind the structure and usage of `RmpFlow` in NVIDIA Isaac Sim, reference
the [Motion Generation](concepts/index.html#isaac-sim-motion-generation) page.

On this page

* [Getting Started](#getting-started)
* [Generating Motions with an RMPflow Instance](#generating-motions-with-an-rmpflow-instance)
  + [World State](#world-state)
* [Loading RMPflow for Supported Robots](#loading-rmpflow-for-supported-robots)
* [Debugging Features](#debugging-features)
* [Summary](#summary)
  + [Further Learning](#further-learning)