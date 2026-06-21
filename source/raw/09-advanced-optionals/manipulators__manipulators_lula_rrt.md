---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/manipulators/manipulators_lula_rrt.html
title: "Lula RRT Tutorial"
section: "Manipulators"
module: "09-advanced-optionals"
checksum: "b3095ee01ba78924"
fetched: "2026-06-21T14:14:39"
---

* [Robot Simulation](../robot_simulation/index.html)
* [Motion Generation (Deprecated)](motion_generation_overview.html)
* Lula RRT

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Lula RRT

Deprecated

For new development, consider using the newer [Robot Motion (Experimental)](../robot_motion_experimental/index.html) API, which provides improved interfaces and additional features over Lula.

This tutorial shows how the [Lula RRT](concepts/lula_rrt.html#isaac-sim-motion-generation-rrt) class in the [Motion Generation](concepts/index.html#isaac-sim-motion-generation) extension can be used to
produce a collision free path from a starting configuration space (c-space) position to a c-space or task-space target.

## Getting Started

**Prerequisites**

* Complete the [Adding a Manipulator Robot](../core_api_tutorials/tutorial_core_adding_manipulator.html#isaac-sim-app-tutorial-core-adding-manipulator) tutorial prior to beginning this tutorial.
* You can reference the Lula Robot Description Editor to understand how to generate your own robot\_description.yaml file to be able to use RRT on unsupported robots.
* Review the [Loaded Scenario Extension Template](../utilities/extension_templates_tutorial.html#isaac-sim-app-tutorial-extension-templates-loaded-scenario) to understand how this tutorial is structured and run.

To follow along with the tutorial, run your Isaac Sim 6.0 instance. Then open **Window > Extensions**, search for **Motion Generation Examples** (`isaacsim.robot_motion.motion_generation.examples`), and enable it. If you cannot find it, remove `@feature` from the Extensions search bar and search again.
Within the isaacsim.robot\_motion.motion\_generation.examples extension, there is a fully functional example of RRT being used to plan to a task-space target.
The sections of this tutorial build up the file `scenario.py` from basic functionality to the completed code.

Note

**Motion Generation Examples** (`isaacsim.robot_motion.motion_generation.examples`) are deprecated **since Isaac Sim 6.0.0**. In the Isaac Sim source repository they live under `source/deprecated/isaacsim.robot_motion.motion_generation.examples`; the extension id is unchanged.

**Replacement:** Use the `isaacsim.robot_motion.cumotion.examples` extension and the [cuMotion Integration](../cumotion/index.html) tutorials.

## Generating a Path Using an RRT Instance

### Required Configuration Files

[Lula RRT](concepts/lula_rrt.html#isaac-sim-motion-generation-rrt) requires three configuration files to identify a specific robot in
[Lula RRT Configuration](concepts/lula_rrt.html#isaac-sim-motion-generation-rrt-configuration). Paths to these configuration files are used to initialize the `RRT`
class along with an end effector name matching a frame in the robot URDF.

One of the required files contains parameters for the RRT algorithm specifically, and is not shared with any other Lula algorithms.
This tutorial loads the following RRT config file for the Franka robot:

```python
 1seed: 123456
 2step_size: 0.05
 3max_iterations: 50000
 4max_sampling: 10000
 5distance_metric_weights: [3.0, 2.0, 2.0, 1.5, 1.5, 1.0, 1.0]
 6task_space_frame_name: "panda_rightfingertip"
 7task_space_limits: [[0.0, 0.7], [-0.6, 0.6], [0.0, 0.8]]
 8cuda_tree_params:
 9    max_num_nodes: 10000
10    max_buffer_size: 30
11    num_nodes_cpu_gpu_crossover: 3000
12c_space_planning_params:
13    exploration_fraction: 0.5
14task_space_planning_params:
15    translation_target_zone_tolerance: 0.05
16    orientation_target_zone_tolerance: 0.09
17    translation_target_final_tolerance: 1e-4
18    orientation_target_final_tolerance: 0.005
19    translation_gradient_weight: 1.0
20    orientation_gradient_weight: 0.125
21    nn_translation_distance_weight: 1.0
22    nn_orientation_distance_weight: 0.125
23    task_space_exploitation_fraction: 0.4
24    task_space_exploration_fraction: 0.1
25    max_extension_substeps_away_from_target: 6
26    max_extension_substeps_near_target: 50
27    extension_substep_target_region_scale_factor: 2.0
28    unexploited_nodes_culling_scalar: 1.0
29    gradient_substep_size: 0.025
```

You can reference the `docstring` to the function `RRT.set_param()` in our [API Documentation](../py/source/deprecated/isaacsim.robot_motion.motion_generation/docs/index.html) for a description of each parameter.

### RRT Example

The file `/RRT_Example_python/scenario.py` loads the Franka robot and uses `RRT` to move it around obstacles to a target.
Every 60 frames, the planner replans to move to the current target position (if possible). In this example, the planner does
not attempt to plan to the same target multiple times if a failure is encountered. The returned plan will be `None` and no actions will be taken.

Initialize RRT:

```python
 1        # Lula config files for supported robots are stored in the motion_generation extension under
 2        # "/path_planner_configs" and "/motion_policy_configs"
 3        mg_extension_path = get_extension_path_from_name("isaacsim.robot_motion.motion_generation")
 4        rmp_config_dir = os.path.join(mg_extension_path, "motion_policy_configs")
 5        rrt_config_dir = os.path.join(mg_extension_path, "path_planner_configs")
 6
 7        # Initialize an RRT object
 8        self._rrt = RRT(
 9            robot_description_path=rmp_config_dir + "/franka/rmpflow/robot_descriptor.yaml",
10            urdf_path=rmp_config_dir + "/franka/lula_franka_gen.urdf",
11            rrt_config_path=rrt_config_dir + "/franka/rrt/franka_planner_config.yaml",
12            end_effector_frame_name="right_gripper",
13        )
```

For supported robots, this can be simplified:

```python
1        # RRT for supported robots can also be loaded with a simpler equivalent:
2        # rrt_config = interface_config_loader.load_supported_path_planner_config("Franka", "RRT")
3        # self._rrt = RRT(**rrt_confg)
```

To make `RRT` aware of the obstacle it needs to watch the obstacles:

```python
1        self._rrt.add_obstacle(self._obstacle)
```

Any time `RRT.update_world()` is called, it will query the current position
of watched obstacles.

`RRT` outputs sparse plans that, when linearly interpolated, form a collision-free path to the goal position.
As an instance of the `PathPlanner` interface, `RRT` can be passed to a [Path Planner Visualizer](concepts/path_planner.html#isaac-sim-path-planner-visualizer) to convert its output
to a form that is directly usable by the robot `Articulation`:

```python
1        # Use the PathPlannerVisualizer wrapper to generate a trajectory of ArticulationActions
2        self._path_planner_visualizer = PathPlannerVisualizer(self._articulation, self._rrt)
```

Complete code:

```python
  1import os
  2
  3import numpy as np
  4from isaacsim.core.api.objects.cuboid import VisualCuboid
  5from isaacsim.core.prims import SingleArticulation as Articulation
  6from isaacsim.core.prims import SingleXFormPrim as XFormPrim
  7from isaacsim.core.utils.distance_metrics import rotational_distance_angle
  8from isaacsim.core.utils.extensions import get_extension_path_from_name
  9from isaacsim.core.utils.numpy.rotations import euler_angles_to_quats, quats_to_rot_matrices
 10from isaacsim.core.utils.stage import add_reference_to_stage
 11from isaacsim.robot_motion.motion_generation import PathPlannerVisualizer, interface_config_loader
 12from isaacsim.robot_motion.motion_generation.lula import RRT
 13from isaacsim.storage.native import get_assets_root_path
 14
 15
 16class FrankaRrtExample:
 17    def __init__(self):
 18        self._rrt = None
 19        self._path_planner_visualizer = None
 20        self._plan = []
 21
 22        self._articulation = None
 23        self._target = None
 24        self._target_position = None
 25
 26        self._frame_counter = 0
 27
 28    def load_example_assets(self):
 29        # Add the Franka and target to the stage
 30        # The position in which things are loaded is also the position in which they
 31
 32        robot_prim_path = "/panda"
 33        path_to_robot_usd = get_assets_root_path() + "/Isaac/Robots/FrankaRobotics/FrankaPanda/franka.usd"
 34
 35        add_reference_to_stage(path_to_robot_usd, robot_prim_path)
 36        self._articulation = Articulation(robot_prim_path)
 37
 38        add_reference_to_stage(get_assets_root_path() + "/Isaac/Props/UIElements/frame_prim.usd", "/World/target")
 39        self._target = XFormPrim("/World/target", scale=[0.04, 0.04, 0.04])
 40        self._target.set_default_state(np.array([0.45, 0.5, 0.7]), euler_angles_to_quats([3 * np.pi / 4, 0, np.pi]))
 41
 42        self._obstacle = VisualCuboid(
 43            "/World/Wall", position=np.array([0.3, 0.6, 0.6]), size=1.0, scale=np.array([0.1, 0.4, 0.4])
 44        )
 45
 46        # Return assets that were added to the stage so that they can be registered with the core.World
 47        return self._articulation, self._target
 48
 49    def setup(self):
 50        # -- Begin initializing RRT -- #
 51        # Lula config files for supported robots are stored in the motion_generation extension under
 52        # "/path_planner_configs" and "/motion_policy_configs"
 53        mg_extension_path = get_extension_path_from_name("isaacsim.robot_motion.motion_generation")
 54        rmp_config_dir = os.path.join(mg_extension_path, "motion_policy_configs")
 55        rrt_config_dir = os.path.join(mg_extension_path, "path_planner_configs")
 56
 57        # Initialize an RRT object
 58        self._rrt = RRT(
 59            robot_description_path=rmp_config_dir + "/franka/rmpflow/robot_descriptor.yaml",
 60            urdf_path=rmp_config_dir + "/franka/lula_franka_gen.urdf",
 61            rrt_config_path=rrt_config_dir + "/franka/rrt/franka_planner_config.yaml",
 62            end_effector_frame_name="right_gripper",
 63        )
 64        # -- End of initializing RRT -- #
 65
 66        # -- Begin simplified initialization of RRT -- #
 67        # RRT for supported robots can also be loaded with a simpler equivalent:
 68        # rrt_config = interface_config_loader.load_supported_path_planner_config("Franka", "RRT")
 69        # self._rrt = RRT(**rrt_confg)
 70        # -- End of simplified initialization of RRT -- #
 71
 72        # -- Begin adding obstacle -- #
 73        self._rrt.add_obstacle(self._obstacle)
 74        # -- End of adding obstacle -- #
 75
 76        # Set the maximum number of iterations of RRT to prevent it from blocking Isaac Sim for
 77        # too long.
 78        self._rrt.set_max_iterations(5000)
 79
 80        # -- Begin setting PathPlannerVisualizer -- #
 81        # Use the PathPlannerVisualizer wrapper to generate a trajectory of ArticulationActions
 82        self._path_planner_visualizer = PathPlannerVisualizer(self._articulation, self._rrt)
 83        # -- End of setting PathPlannerVisualizer -- #
 84
 85        self.reset()
 86
 87    def update(self, step: float):
 88        current_target_translation, current_target_orientation = self._target.get_world_pose()
 89        current_target_rotation = quats_to_rot_matrices(current_target_orientation)
 90
 91        translation_distance = np.linalg.norm(self._target_translation - current_target_translation)
 92        rotation_distance = rotational_distance_angle(current_target_rotation, self._target_rotation)
 93        target_moved = translation_distance > 0.01 or rotation_distance > 0.01
 94
 95        if self._frame_counter % 60 == 0 and target_moved:
 96            # -- Begin computing plan -- #
 97            # Replan every 60 frames if the target has moved
 98            self._rrt.set_end_effector_target(current_target_translation, current_target_orientation)
 99            self._rrt.update_world()
100            self._plan = self._path_planner_visualizer.compute_plan_as_articulation_actions(max_cspace_dist=0.01)
101            # -- End of computing plan -- #
102
103            self._target_translation = current_target_translation
104            self._target_rotation = current_target_rotation
105
106        if self._plan:
107            action = self._plan.pop(0)
108            self._articulation.apply_action(action)
109
110        self._frame_counter += 1
111
112    def reset(self):
113        self._target_translation = np.zeros(3)
114        self._target_rotation = np.eye(3)
115        self._frame_counter = 0
116        self._plan = []
```

In this example, `RRT` replans every second if the target has been moved. The replanning is performed as follows:

```python
1            # Replan every 60 frames if the target has moved
2            self._rrt.set_end_effector_target(current_target_translation, current_target_orientation)
3            self._rrt.update_world()
4            self._plan = self._path_planner_visualizer.compute_plan_as_articulation_actions(max_cspace_dist=0.01)
```

* First, `RRT` is informed of the new target position.
* Then it is told to query the position of watched obstacles.
* Finally, the `path_planner_visualizer` wrapping `RRT` is used to generate a plan in the form of a list of `ArticulationAction`.

The `max_cspace_dist` argument passed to the `path_planner_visualizer` interpolates the sparse output with a maximum l2 norm of `.01`
between any two commanded robot positions. On every frame, one of the actions in the plan is removed from the plan and sent to the
robot.

## Current Limitations

### Following a Plan with Exactness

The `PathPlannerVisualizer` class is called a “Visualizer” because it is only meant to give a visualization of an output plan, but it is not likely to be useful
beyond this. By densely linearly interpolating an `RRT` plan, the resulting trajectory is far from time-optimal or smooth. To follow a plan in a
more theoretically sound way, the output of `RRT` can be combined with the `LulaTrajectoryGenerator`. This is demonstrated in the NVIDIA Isaac Sim Path Planning Example
in the **Robotics Examples** tab. You can activate **Robotics Examples** tab from **Windows** > **Examples** > **Robotics Examples**.

## Summary

This tutorial reviews using the `RRT` class to generate a collision-free path through an environment from a starting position to a task-space target.

### Further Learning

To understand the motivation behind the structure and usage of `RRT` in NVIDIA Isaac Sim, reference the [Motion Generation](concepts/index.html#isaac-sim-motion-generation)
page.

On this page

* [Getting Started](#getting-started)
* [Generating a Path Using an RRT Instance](#generating-a-path-using-an-rrt-instance)
  + [Required Configuration Files](#required-configuration-files)
  + [RRT Example](#rrt-example)
* [Current Limitations](#current-limitations)
  + [Following a Plan with Exactness](#following-a-plan-with-exactness)
* [Summary](#summary)
  + [Further Learning](#further-learning)