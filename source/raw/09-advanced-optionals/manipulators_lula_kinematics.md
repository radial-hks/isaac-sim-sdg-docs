---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/manipulators/manipulators_lula_kinematics.html
title: "Lula Kinematics"
section: "Manipulators"
module: "09-advanced-optionals"
checksum: "0142e94096c0aa04"
fetched: "2026-06-21T13:05:42"
---

* [Robot Simulation](../robot_simulation/index.html)
* [Motion Generation (Deprecated)](motion_generation_overview.html)
* Lula Kinematics Solver

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Lula Kinematics Solver

Deprecated

For new development, consider using the newer [Robot Motion (Experimental)](../robot_motion_experimental/index.html) API, which provides improved interfaces and additional features over Lula.

This tutorial shows how the [Lula Kinematics Solver](concepts/kinematics_solver.html#isaac-sim-lula-kinematics-solver) class is used to compute forward and inverse kinematics on a robot in NVIDIA Isaac Sim.

## Getting Started

**Prerequisites**

* Complete the [Adding a Manipulator Robot](../core_api_tutorials/tutorial_core_adding_manipulator.html#isaac-sim-app-tutorial-core-adding-manipulator) tutorial prior to beginning this tutorial.
* You can reference the [Lula Robot Description and XRDF Editor](manipulators_robot_description_editor.html#isaac-sim-app-tutorial-motion-generation-robot-description-editor) to understand how to generate your own robot\_description.yaml file to be able to use `LulaKinematicsSolver` on unsupported robots.
* Review the [Loaded Scenario Extension Template](../utilities/extension_templates_tutorial.html#isaac-sim-app-tutorial-extension-templates-loaded-scenario) to understand how this tutorial is structured and run.

To follow along with the tutorial, run your Isaac Sim 6.0 instance. Then open **Window > Extensions**, search for **Motion Generation Examples** (`isaacsim.robot_motion.motion_generation.examples`), and enable it. If you cannot find it, remove `@feature` from the Extensions search bar and search again.
Within the isaacsim.robot\_motion.motion\_generation.examples extension, there is a fully functional example using a `LulaKinematicsSolver` to track a task-space target.
The sections of this tutorial build up the file `scenario.py` from basic functionality to the completed code.

Note

**Motion Generation Examples** (`isaacsim.robot_motion.motion_generation.examples`) are deprecated **since Isaac Sim 6.0.0**. In the Isaac Sim source repository they live under `source/deprecated/isaacsim.robot_motion.motion_generation.examples`; the extension id is unchanged.

**Replacement:** Use the `isaacsim.robot_motion.cumotion.examples` extension and the [cuMotion Integration](../cumotion/index.html) tutorials.

## Using the LulaKinematicsSolver to Compute Forward and Inverse Kinematics

The [Lula Kinematics Solver](concepts/kinematics_solver.html#isaac-sim-lula-kinematics-solver) is able to calculate forward and inverse kinematics for a robot that is defined
by two configuration files (see [Lula Kinematics Solver Configuration](concepts/kinematics_solver.html#isaac-sim-lula-kinematics-solver-configuration)). The `LulaKinematicsSolver` can be paired with
an [Articulation Kinematics Solver](concepts/kinematics_solver.html#isaac-sim-articulation-kinematics-solver) to compute kinematics in a way that can be directly applied to the robot `Articulation`.

The file `/Lula_Kinematics_python/scenario.py` uses the `LulaKinematicsSolver` to generate inverse kinematic solutions to move the robot to a target.

```python
import os

import carb
import numpy as np
from isaacsim.core.prims import SingleArticulation as Articulation
from isaacsim.core.prims import SingleXFormPrim as XFormPrim
from isaacsim.core.utils.extensions import get_extension_path_from_name
from isaacsim.core.utils.numpy.rotations import euler_angles_to_quats
from isaacsim.core.utils.stage import add_reference_to_stage
from isaacsim.robot_motion.motion_generation import (
    ArticulationKinematicsSolver,
    LulaKinematicsSolver,
    interface_config_loader,
)
from isaacsim.storage.native import get_assets_root_path

class FrankaKinematicsExample:
    def __init__(self):
        self._kinematics_solver = None
        self._articulation_kinematics_solver = None

        self._articulation = None
        self._target = None

    def load_example_assets(self):
        # Add the Franka and target to the stage

        robot_prim_path = "/panda"
        path_to_robot_usd = get_assets_root_path() + "/Isaac/Robots/FrankaRobotics/FrankaPanda/franka.usd"

        add_reference_to_stage(path_to_robot_usd, robot_prim_path)
        self._articulation = Articulation(robot_prim_path)

        add_reference_to_stage(get_assets_root_path() + "/Isaac/Props/UIElements/frame_prim.usd", "/World/target")
        self._target = XFormPrim("/World/target", scale=[0.04, 0.04, 0.04])
        self._target.set_default_state(np.array([0.3, 0, 0.5]), euler_angles_to_quats([0, np.pi, 0]))

        # Return assets that were added to the stage so that they can be registered with the core.World
        return self._articulation, self._target

    def setup(self):
        # Load a URDF and Lula Robot Description File for this robot:
        mg_extension_path = get_extension_path_from_name("isaacsim.robot_motion.motion_generation")
        kinematics_config_dir = os.path.join(mg_extension_path, "motion_policy_configs")

        self._kinematics_solver = LulaKinematicsSolver(
            robot_description_path=kinematics_config_dir + "/franka/rmpflow/robot_descriptor.yaml",
            urdf_path=kinematics_config_dir + "/franka/lula_franka_gen.urdf",
        )

        # Kinematics for supported robots can be loaded with a simpler equivalent
        # print("Supported Robots with a Lula Kinematics Config:", interface_config_loader.get_supported_robots_with_lula_kinematics())
        # kinematics_config = interface_config_loader.load_supported_lula_kinematics_solver_config("Franka")
        # self._kinematics_solver = LulaKinematicsSolver(**kinematics_config)

        print("Valid frame names at which to compute kinematics:", self._kinematics_solver.get_all_frame_names())

        end_effector_name = "right_gripper"
        self._articulation_kinematics_solver = ArticulationKinematicsSolver(
            self._articulation, self._kinematics_solver, end_effector_name
        )

    def update(self, step: float):
        target_position, target_orientation = self._target.get_world_pose()

        # Track any movements of the robot base
        robot_base_translation, robot_base_orientation = self._articulation.get_world_pose()
        self._kinematics_solver.set_robot_base_pose(robot_base_translation, robot_base_orientation)

        action, success = self._articulation_kinematics_solver.compute_inverse_kinematics(
            target_position, target_orientation
        )

        if success:
            self._articulation.apply_action(action)
        else:
            carb.log_warn("IK did not converge to a solution.  No action is being taken")

        # Unused Forward Kinematics:
        # ee_position,ee_rot_mat = articulation_kinematics_solver.compute_end_effector_pose()

    def reset(self):
        # Kinematics is stateless
        pass
```

The `LulaKinematicsSolver` is instantiated on lines 41-47 using file paths to the appropriate configuration files. The
`LulaKinematicsSolver` uses the same robot description files as the Lula-based [RMPflow](concepts/rmpflow.html#isaac-sim-motion-generation-rmpflow) [Motion Policy Algorithm](concepts/motion_policy.html#isaac-sim-motion-policy).
The `LulaKinematicsSolver` can solve forward and inverse kinematics at any frame that exists in the robot URDF file.
On line 54, the complete list of recognized frames in the Franka robot is printed:

```python
Valid frame names at which to compute kinematics:
['base_link', 'panda_link0', 'panda_link1', 'panda_link2', 'panda_link3', 'panda_link4', 'panda_forearm_end_pt', 'panda_forearm_mid_pt',
 'panda_forearm_mid_pt_shifted', 'panda_link5', 'panda_forearm_distal', 'panda_link6', 'panda_link7', 'panda_link8', 'panda_hand',
 'camera_bottom_screw_frame', 'camera_link', 'camera_depth_frame', 'camera_color_frame', 'camera_color_optical_frame', 'camera_depth_optical_frame',
 'camera_left_ir_frame', 'camera_left_ir_optical_frame', 'camera_right_ir_frame', 'camera_right_ir_optical_frame', 'panda_face_back_left',
 'panda_face_back_right', 'panda_face_left', 'panda_face_right', 'panda_leftfinger', 'panda_leftfingertip', 'panda_rightfinger', 'panda_rightfingertip', 'right_gripper', 'panda_wrist_end_pt']
```

Supported robots can be loaded directly by name as on lines 50-52. This is equivalent to lines 41-47.

On line 57, an [Articulation Kinematics Solver](concepts/kinematics_solver.html#isaac-sim-articulation-kinematics-solver) is instantiated with the Franka robot `Articulation`, the `LulaKinematicsSolver` instance,
and the end effector name. The `ArticulationKinematicsSolver` class allows you to
compute the end effector position and orientation for the robot `Articulation` in a single line (line 75).

The `ArticulationKinematicsSolver` also allows you to compute inverse kinematics.
The current position of the robot `Articulation` is used as a warm start in the IK calculation,
and the result is returned as an `ArticulationAction` that can be consumed by the robot `Articulation`
to move the specified end effector frame to a target position (lines 67 and 70).

The `LulaKinematicsSolver` returns a flag marking the success or failure of the inverse kinematics computation. On line
67, the script applies the inverse kinematics solution to the robot `Articulation` only if the kinematics converged
successfully to a solution, otherwise no new action is sent to the robot,
and a warning is thrown. The `LulaKinematicsSolver` exposes
settings that allow you to specify how quickly it terminates its search. These settings are outside the
scope of this tutorial.

The `LulaKinematicsSolver` assumes that the robot base is positioned at the origin unless another location is specified. On lines 64-65,
the `LulaKinematicsSolver` is given the current position of the robot base on every frame. This allows the forward
and inverse kinematics to operate using world coordinates. For example, the position of the target is queried in world
coordinates and passed to the `LulaKinematicsSolver`, which internally performs the necessary transformation to compute
accurate inverse kinematics.

The `LulaKinematicsSolver` can be used on its own to compute forward kinematics at any position and to compute
inverse kinematics with any warm start. A robot `Articulation` does not need to be present on the USD stage. See [Kinematics Solvers](concepts/kinematics_solver.html#isaac-sim-kinematics-solver) for more details.

Additionally, sending an inverse kinematic solution directly to the robot is not likely to be useful beyond demonstrations.
In a realistic scenario, you need to determine not only the end position of the robot, but also the path to get there. An IK solver on its own can make
for only a rudimentary trajectory through space that is not likely to be optimal.

## Summary

This tutorial reviews how to load the `LulaKinematicsSolver` class and use it alongside the `ArticulationKinematicsSolver`
helper class to compute forward and inverse kinematics at any frame specified in the robot URDF file.

### Further Learning

To understand the motivation behind the structure and usage of `LulaKinematicsSolver` in NVIDIA Isaac Sim, reference the [Motion Generation](concepts/index.html#isaac-sim-motion-generation)
page.

On this page

* [Getting Started](#getting-started)
* [Using the LulaKinematicsSolver to Compute Forward and Inverse Kinematics](#using-the-lulakinematicssolver-to-compute-forward-and-inverse-kinematics)
* [Summary](#summary)
  + [Further Learning](#further-learning)