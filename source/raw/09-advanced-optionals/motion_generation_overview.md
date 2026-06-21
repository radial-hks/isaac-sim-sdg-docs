---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/manipulators/motion_generation_overview.html
title: "Motion Generation Overview"
section: "Manipulators"
module: "09-advanced-optionals"
checksum: "56304377480151f5"
fetched: "2026-06-21T13:05:42"
---

* [Robot Simulation](../robot_simulation/index.html)
* Motion Generation (Deprecated)

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Motion Generation (Deprecated)

Deprecated

For new development, consider using the newer [Robot Motion (Experimental)](../robot_motion_experimental/index.html) API, which provides improved interfaces and additional features.

Lula is a high-performance motion generation library for robotic manipulation. RMPflow provides
real-time, reactive local policies to guide a robot manipulator to a task space target while
avoiding dynamic obstacles. A suite of Rapidly-exploring Random Tree (RRT) algorithms,
including RRT-Connect and JT-RRT, deliver global planning solutions in static environments.
Additionally, the trajectory generation tools in Lula provide time-optimal trajectories for
paths described as a series of c-space and task-space moves. Finally, Lula provides interfaces
to the performant forward and inverse kinematic solvers underpinning the higher-level motion
generation tools.

NVIDIA Isaac Sim also interfaces with [cuRobo](https://curobo.org), a high-performance, GPU-accelerated robotics motion
generation library that adds additional features to NVIDIA Isaac Sim such as batched collision-free inverse kinematics,
collision-free motion planning, and reactive control in the presence of obstacles represented as meshes or Nvblox maps.
For more information, see the [cuRobo tutorial](manipulators_curobo.html#isaac-sim-app-tutorial-curobo).

* [Motion Generation](concepts/index.html)
* [Lula Robot Description and XRDF Editor](manipulators_robot_description_editor.html)
* [Lula RMPflow](manipulators_rmpflow.html)
* [Lula RRT](manipulators_lula_rrt.html)
* [Lula Kinematics Solver](manipulators_lula_kinematics.html)
* [Lula Trajectory Generator](manipulators_lula_trajectory_generator.html)
* [Configuring RMPflow for a New Manipulator](manipulators_configure_rmpflow_denso.html)
* [cuRobo and cuMotion](manipulators_curobo.html)

## Examples

**Interactive Examples**

To locate the interactive examples, go to **Windows** > **Examples** > **Robotics Examples** and open the **Robotics Examples** tab if itâs not already. Select one of the following examples from the browser, read the **Information** tab on the right hand side of the browser window for instructions on how to run it.

* Follow Target Example: **Manipulation > Follow Target**
* RoboFactory Example: **Multi-Robot > RoboFactory**
* RoboParty Example: **Multi-Robot > RoboParty**

Note

Pressing **STOP**, then **PLAY** in this workflow might not reset the world properly. Use
the **RESET** button instead.

**Standalone Examples**

To run a standalone example, navigate to your `<isaac_sim_root_dir>`, then use `./python.sh` for Linux or `python.bat` for Windows to run the example scripts listed here.

* Follow Target with RMPflow (Franka): `standalone_examples/api/isaacsim.robot.experimental.manipulators/franka/follow_target_with_rmpflow.py`
* Follow Target with RMPflow (UR10): `standalone_examples/api/isaacsim.robot.experimental.manipulators/universal_robots/follow_target_with_rmpflow.py`
* Follow Target with IK (UR10): `standalone_examples/api/isaacsim.robot.experimental.manipulators/universal_robots/follow_target_with_ik.py`

On this page

* [Examples](#examples)