---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/manipulators/concepts/index.html
title: "Manipulators Concepts"
section: "Manipulators"
module: "09-advanced-optionals"
checksum: "5eee63fba26c5209"
fetched: "2026-06-21T14:14:38"
---

* [Robot Simulation](../../robot_simulation/index.html)
* [Motion Generation (Deprecated)](../motion_generation_overview.html)
* Motion Generation

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Motion Generation

Deprecated

For new development, consider using the newer [Robot Motion (Experimental)](../../robot_motion_experimental/index.html) API, which provides improved interfaces and additional features.

The [Motion Generation](#isaac-sim-motion-generation) provides an API that you can use to control objects within Isaac Sim.
The API is made up of abstract interfaces for adding motion control algorithms to Isaac Sim.
The interfaces in the [Motion Generation](#isaac-sim-motion-generation) provide two basic utilities:

> * Simplify the integration of new robotics algorithms into NVIDIA Isaac Sim.
> * Provide a standard structure with which to compare similar robotics algorithms.

For example, if you have a robot that has not previously been described to Isaac Sim, you can use these APIs to define that robot and how it moves.

> * Simplify the integration of new robotics algorithms into NVIDIA Isaac Sim.
> * Provide a standard structure with which to compare similar robotics algorithms.

For example, if you have a robot that has not previously been described to Isaac Sim, you can use these APIs to define that robot and how it moves.

Three interfaces are provided in the Motion Generation Extension:

* [Motion Policy Algorithm](motion_policy.html)
* [Path Planner](path_planner.html#isaac-sim-path-planner)
* [Kinematics Solvers](kinematics_solver.html)

In Isaac Sim, the robot is specified using a USD file that gets added to the stage. However, we expect that robotics algorithms will have their
own way of specifying the robot’s kinematic structure and custom parameters. To avoid interfering with any particular robot description format, the interfaces
in the Motion Generation Extension include functions that facilitate the translation between the USD robot and a specific algorithm. Specifically,
an algorithm can specify which joints in the robot it cares about, and the order in which it expects those joints to be listed. The helper classes provided in this extension,
[Articulation Motion Policy](motion_policy.html#isaac-sim-articulation-motion-policy), [Path Planner Visualizer](path_planner.html#isaac-sim-path-planner-visualizer), and [Articulation Kinematics Solver](kinematics_solver.html#isaac-sim-articulation-kinematics-solver), use the interface
functions to appropriately map robot joint states between the USD robot articulation and an interface implementation.

In Isaac Sim, we use the word [Articulation](https://docs.omniverse.nvidia.com/kit/docs/omni_physics/latest/dev_guide/rigid_bodies_articulations/articulations.html "(in Omni Physics)") to refer to the simulated robot represented through USD.
The word “Articulation” is used as a prefix in the
Motion Generation Extension to indicate utility classes that handle interfacing an algorithm with the simulated robot.

In addition, the **Motion Generation extension** includes a handful of special-purpose
controllers that do not leverage MotionPolicy or PathPlanner.

* [Motion Generation Extension API Documentation](motion_gen_api.html)
* [Kinematics Solvers](kinematics_solver.html)
* [Trajectory Generation](trajectory_interface.html)
* [Path Planner Algorithm](path_planner.html)
* [Lula RRT](lula_rrt.html)
* [Motion Policy Algorithm](motion_policy.html)
* [RMPflow](rmpflow.html)
* [RMPflow Tuning Guide](rmpflow_tuning_guide.html)

## References

On this page

* [References](#references)