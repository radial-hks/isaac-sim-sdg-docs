---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/manipulators/concepts/trajectory_interface.html
title: "Trajectory Interface"
section: "Manipulators"
module: "09-advanced-optionals"
checksum: "a30321198dfae604"
fetched: "2026-06-21T13:05:41"
---

* [Robot Simulation](../../robot_simulation/index.html)
* [Motion Generation (Deprecated)](../motion_generation_overview.html)
* [Motion Generation](index.html)
* Trajectory Generation

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Trajectory Generation

Deprecated

For new development, consider using the newer [Robot Motion (Experimental)](../../robot_motion_experimental/index.html) API, which provides improved interfaces and additional features.

In the Motion Generation extension, a workflow is provided for defining c-space and task-space trajectories. An interface is provided for a [Trajectory Interface](#isaac-sim-trajectory) class:

* Trajectory Interface
* Articulation Trajectory
* Lula Trajectory Generator

## Trajectory Interface

An interface is provided in the Motion Generation extension for defining a robot trajectory.
An instance of the Trajectory interface must return robot c-space position as a continuous function of time within a specified time horizon. A Trajectory has four basic accessors:

* **start\_time**: The earliest time at which this Trajectory will return a robot c-space position.
* **end\_time**: The latest time at which this Trajectory will return a robot c-space position.
* **active\_joints**: The names of the joints that this Trajectory is intended to control corresponding to the order the joint targets are returned.
* **joint\_targets(time)**: Joint position/velocity targets as a function of time between start\_time and end\_time.

An instance of the Trajectory class can be used to directly control a robot by using it to initialize an [Articulation Trajectory](#isaac-sim-articulation-trajectory).

## Articulation Trajectory

The ArticulationTrajectory class is initialized using a robot Articulation and an instance of the Trajectory class.
This class handles the mapping from a defined Trajectory to controlling a simulated robot Articulation. The ArticulationTrajectory class has two main functions:

* **get\_action\_at\_time(time)**: Return an ArticulationAction at a time that is within the time horizon of the provided Trajectory object.
* **get\_action\_sequence(timestep)**: Return a list of ArticulationAction that interpolates between the provided Trajectory start\_time and end\_time by the specified timestep. This is a convenience method for when the timestep of the physics simulator is known to be fixed.

As a Trajectory only defines the robot behavior within the provided time horizon, it is necessary to bring the robot Articulation to the initial state of the Trajectory before attempting to follow a sequence of generated ArticultionAction.

## Lula Trajectory Generator

We provide a **Lula** implementation of a trajectory generator that can generate a Trajectory given c-space or task-space waypoints. Two classes are provided:

* LulaCSpaceTrajectoryGenerator
* LulaTaskSpaceTrajectoryGenerator

Both classes share the same required configuration information.

To configure Lula Trajectory Generators for a specific robot you must have the following files:

> * A URDF (universal robot description file), used for specifying robot kinematics as well as joint and link names. Position limits for each joint are also required. Other properties in the URDF are ignored and can be omitted; these include masses, moments of inertia, visual and collision meshes.
> * A supplemental robot description file in YAML format. In addition to enumerating the list of actuated joints that define the configuration space (c-space) for the robot, this file also includes sections for specifying the default c-space configuration, acceleration limits, or jerk limits. This file can also be used to specify fixed positions for unactuated joints.

### Lula C-Space Trajectory Generator

The `LulaCSpaceTrajectoryGenerator` class takes in a series of c-space waypoints that correspond to the c-space coordinates listed in the required robot description YAML file.
The generator will use spline-based interpolation to connect the waypoints with an initial and final velocity of 0.
The trajectory is time-optimal â that is, either the velocity, acceleration, or jerk limits are saturated at any given time to produce a trajectory with as short a duration as possible.
The generator will return an instance of the Trajectory interface.

### Lula Task-Space Trajectory Generator

The `LulaTaskSpaceTrajectoryGenerator` class takes in a sequence of task-space targets and an end effector frame name (which must be a valid frame in the provided URDF file), and it returns an instance of the Trajectory interface if possible.

Task-space trajectories can be defined as a series of position and orientation targets. In this case, the generated trajectory will linearly interpolate in task-space between the provided targets.

Task-space trajectories can also be defined using the `lula.TaskSpacePathSpec` class, which provides a set of useful primitives to connect task-space waypoints such as creating an arc, pure rotation, pure translation.

Internally, a task-space trajectory is converted to a c-space trajectory using the
[Lula Kinematics Solver](kinematics_solver.html#isaac-sim-lula-kinematics-solver), and is then passed through the `LulaCSpaceTrajectoryGenerator`. For this reason, the `LulaTaskSpaceTrajectoryGenerator` class shares the same set of parameters as the `LulaCSpaceTrajectoryGenerator` class, with added parameters that affect how the task-space trajectory is converted to c-space.

On this page

* [Trajectory Interface](#trajectory-interface)
* [Articulation Trajectory](#articulation-trajectory)
* [Lula Trajectory Generator](#lula-trajectory-generator)
  + [Lula C-Space Trajectory Generator](#lula-c-space-trajectory-generator)
  + [Lula Task-Space Trajectory Generator](#lula-task-space-trajectory-generator)