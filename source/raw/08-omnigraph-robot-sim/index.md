---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/robot_simulation/index.html
title: "Robot Simulation Index"
section: "Robot Simulation"
module: "08-omnigraph-robot-sim"
checksum: "538df2794ea071d1"
fetched: "2026-06-21T13:05:38"
---

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
* **Policy Controlled Robots**: uses controllers that are trained using reinforcement learning. They also has a much looser definition âcontrollersâ, for they can have task and path planners embedded as well.

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