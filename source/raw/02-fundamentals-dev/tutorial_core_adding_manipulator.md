---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/core_api_tutorials/tutorial_core_adding_manipulator.html
title: "Adding Manipulator"
section: "Core API"
module: "02-fundamentals-dev"
checksum: "66cdcb62714fa473"
fetched: "2026-06-21T12:48:08"
---

* [Python Scripting and Tutorials](../python_scripting/index.html)
* [Core API Tutorial Series](index.html)
* Adding a Manipulator Robot

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Adding a Manipulator Robot

## Learning Objectives

This tutorial introduces a manipulator robot to the simulation, a Franka Panda.
It describes how to add the robot to the scene and execute a pick-and-place operation.
After this tutorial, you will have more experience using manipulator robots and
controlling them with inverse kinematics in NVIDIA Isaac Sim.

*15-20 Minute Tutorial*

## Getting Started

**Prerequisites**

* Review [Hello Robot](tutorial_core_hello_robot.html#isaac-sim-app-tutorial-core-hello-robot) prior to beginning this tutorial.

This tutorial uses **standalone Python scripts**. Run them with a Python environment where Isaac Sim is installed:

## Creating the Scene with a Franka Robot

Add a Franka robot and a cube for the robot to pick up using the `Franka` class.
This class inherits from `Articulation` and provides high-level control methods including
inverse kinematics and gripper control.

When you set `create_robot=True` in the constructor, `Franka` automatically
spawns the Franka robot USD asset at the specified path.

```python
 1"""Create a scene with ground, Franka robot, and blue cube."""
 2
 3import argparse
 4
 5parser = argparse.ArgumentParser()
 6parser.add_argument("--test", action="store_true")
 7args, _ = parser.parse_known_args()
 8
 9from isaacsim import SimulationApp
10
11simulation_app = SimulationApp({"headless": False})
12
13import isaacsim.core.experimental.utils.app as app_utils
14
15app_utils.enable_extension("isaacsim.robot.experimental.manipulators.examples")
16
17from isaacsim.core.experimental.objects import Cube, DomeLight, GroundPlane
18from isaacsim.core.experimental.prims import GeomPrim, RigidPrim
19from isaacsim.core.simulation_manager import SimulationManager
20from isaacsim.robot.experimental.manipulators.examples.franka import Franka
21
22DEVICE = "cpu"
23
24GroundPlane("/World/ground_plane")
25dome_light = DomeLight("/World/DomeLight")
26dome_light.set_intensities(1000)
27
28# Create the Franka robot
29robot = Franka(robot_path="/World/robot", create_robot=True)
30
31# Create a blue cube for the robot to pick up
32cube_shape = Cube(
33    paths="/World/Cube",
34    positions=[0.5, 0.0, 0.0258],
35    sizes=1.0,
36    scales=[0.0515, 0.0515, 0.0515],
37    colors="blue",
38)
39GeomPrim(paths=cube_shape.paths, apply_collision_apis=True)
40RigidPrim(paths=cube_shape.paths)
41
42SimulationManager.setup_simulation(dt=1.0 / 60.0, device=DEVICE)
43physics_scene = SimulationManager.get_physics_scenes()[0]
44physics_scene.set_enabled_gpu_dynamics(False)
45app_utils.play()
46app_utils.update_app(steps=20)
47
48step_count = 0
49max_test_steps = 60
50while simulation_app.is_running():
51    simulation_app.update()
52    step_count += 1
53    if args.test and step_count >= max_test_steps:
54        break
55
56app_utils.stop()
57simulation_app.close()
```

Run the script. A window opens with the Franka robot and cube in the scene; the simulation runs until you close the window.

The `Franka` class provides these key methods for robot control:

* `set_end_effector_pose(position, orientation)` - Move end-effector using inverse kinematics
* `open_gripper()` / `close_gripper()` - Control the gripper
* `get_current_state()` - Get DOF positions and end-effector pose
* `get_downward_orientation()` - Get quaternion for downward-facing orientation
* `reset_to_default_pose()` - Reset robot to home position

## Using FrankaPickPlace for Complete Pick-and-Place

For a complete pick-and-place operation, use the `FrankaPickPlace` class. This class has a
`setup_scene()` method that spawns everything needed for pick-and-place: the Franka robot,
ground plane, and a cube to manipulate.

```python
 1"""Pick-and-place using FrankaPickPlace."""
 2
 3import argparse
 4
 5parser = argparse.ArgumentParser()
 6parser.add_argument("--test", action="store_true")
 7args, _ = parser.parse_known_args()
 8
 9from isaacsim import SimulationApp
10
11simulation_app = SimulationApp({"headless": False})
12
13import isaacsim.core.experimental.utils.app as app_utils
14
15app_utils.enable_extension("isaacsim.robot.experimental.manipulators.examples")
16
17from isaacsim.core.experimental.objects import DomeLight, GroundPlane
18from isaacsim.core.simulation_manager import SimulationManager
19from isaacsim.robot.experimental.manipulators.examples.franka import FrankaPickPlace
20
21DEVICE = "cpu"
22
23GroundPlane("/World/ground_plane")
24dome_light = DomeLight("/World/DomeLight")
25dome_light.set_intensities(1000)
26
27# FrankaPickPlace spawns robot and cube, and provides the pick-place state machine
28controller = FrankaPickPlace()
29controller.setup_scene()
30
31SimulationManager.setup_simulation(dt=1.0 / 60.0, device=DEVICE)
32physics_scene = SimulationManager.get_physics_scenes()[0]
33physics_scene.set_enabled_gpu_dynamics(False)
34app_utils.play()
35# Run a few steps so the articulation's physics tensor entity is valid before `controller.reset()`
36app_utils.update_app(steps=20)
37controller.reset()
38
39# Main loop: run one pick-place step each physics frame until done
40step_count = 0
41max_test_steps = sum(controller.events_dt) + 60
42while simulation_app.is_running():
43    simulation_app.update()
44    step_count += 1
45    if app_utils.is_playing():
46        if not controller.is_done():
47            controller.forward()
48        else:
49            print("Pick-and-place completed")
50            app_utils.pause()
51            if args.test:
52                break
53    if args.test and step_count >= max_test_steps:
54        raise RuntimeError("Pick-and-place did not complete within the test step budget")
55
56app_utils.stop()
57simulation_app.close()
```

Run the script. The robot automatically executes all phases of picking up and placing the cube.

## Understanding the Pick-and-Place State Machine

The `FrankaPickPlace` class uses a state machine with the following phases:

Pick-and-Place Phases

| Phase | Description | Default Steps |
| --- | --- | --- |
| 0 | Move to x,y position above cube | 60 |
| 1 | Approach down to cube | 40 |
| 2 | Close gripper to grasp | 20 |
| 3 | Lift cube upward | 40 |
| 4 | Move cube to target location | 80 |
| 5 | Open gripper to release | 20 |
| 6 | Move up and away | 20 |

You can customize the phase durations by passing `events_dt` to the constructor, and change the cube starting position using `setup_scene`:

```python
1# Custom phase durations (steps for each phase)
2controller = FrankaPickPlace(events_dt=[80, 60, 30, 60, 100, 30, 30])
3# Customize cube position, size, and target position
4controller.setup_scene(
5    cube_initial_position=[0.4, 0.2, 0.0258], cube_size=[0.05, 0.05, 0.05], target_position=[-0.4, 0.2, 0.12]
6)
```

Complete code:

```python
 1"""Pick-and-place using FrankaPickPlace."""
 2
 3import argparse
 4
 5parser = argparse.ArgumentParser()
 6parser.add_argument("--test", action="store_true")
 7args, _ = parser.parse_known_args()
 8
 9from isaacsim import SimulationApp
10
11simulation_app = SimulationApp({"headless": False})
12
13import isaacsim.core.experimental.utils.app as app_utils
14
15app_utils.enable_extension("isaacsim.robot.experimental.manipulators.examples")
16
17from isaacsim.core.experimental.objects import DomeLight, GroundPlane
18from isaacsim.core.simulation_manager import SimulationManager
19from isaacsim.robot.experimental.manipulators.examples.franka import FrankaPickPlace
20
21DEVICE = "cpu"
22
23GroundPlane("/World/ground_plane")
24dome_light = DomeLight("/World/DomeLight")
25dome_light.set_intensities(1000)
26
27# -- Begin custom setup -- #
28# Custom phase durations (steps for each phase)
29controller = FrankaPickPlace(events_dt=[80, 60, 30, 60, 100, 30, 30])
30# Customize cube position, size, and target position
31controller.setup_scene(
32    cube_initial_position=[0.4, 0.2, 0.0258], cube_size=[0.05, 0.05, 0.05], target_position=[-0.4, 0.2, 0.12]
33)
34# -- End of custom setup -- #
35
36SimulationManager.setup_simulation(dt=1.0 / 60.0, device=DEVICE)
37physics_scene = SimulationManager.get_physics_scenes()[0]
38physics_scene.set_enabled_gpu_dynamics(False)
39app_utils.play()
40# Run a few steps so the articulation's physics tensor entity is valid before `controller.reset()`
41app_utils.update_app(steps=20)
42controller.reset()
43
44# Main loop: run one pick-place step each physics frame until done
45step_count = 0
46max_test_steps = sum(controller.events_dt) + 60
47while simulation_app.is_running():
48    simulation_app.update()
49    step_count += 1
50    if app_utils.is_playing():
51        if not controller.is_done():
52            controller.forward()
53        else:
54            print("Pick-and-place completed")
55            app_utils.pause()
56            if args.test:
57                break
58    if args.test and step_count >= max_test_steps:
59        raise RuntimeError("Pick-and-place did not complete within the test step budget")
60
61app_utils.stop()
62simulation_app.close()
```

## See Also

For a complete standalone pick-and-place example with `--device`, `--ik-method`, and `--test` options, see
`standalone_examples/api/isaacsim.robot.experimental.manipulators/franka/pick_place.py`.

## Summary

This tutorial covered the following topics:

1. Adding a Franka manipulator robot using `Franka` with `create_robot=True`
2. Using the `FrankaPickPlace.setup_scene()` method to spawn a complete pick-and-place scene
3. Executing pick-and-place operations with the `forward()` method
4. Understanding and customizing the pick-and-place state machine phases

### Next Steps

Continue to the next tutorial in our Essential Tutorials series, [Adding Multiple Robots](tutorial_core_adding_multiple_robots.html#isaac-sim-app-tutorial-core-adding-multiple-robots),
to learn how to add multiple robots to the simulation.

On this page

* [Learning Objectives](#learning-objectives)
* [Getting Started](#getting-started)
* [Creating the Scene with a Franka Robot](#creating-the-scene-with-a-franka-robot)
* [Using FrankaPickPlace for Complete Pick-and-Place](#using-frankapickplace-for-complete-pick-and-place)
* [Understanding the Pick-and-Place State Machine](#understanding-the-pick-and-place-state-machine)
* [See Also](#see-also)
* [Summary](#summary)
  + [Next Steps](#next-steps)