---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/manipulators/manipulators_curobo.html
title: "cuRobo"
section: "Manipulators"
module: "09-advanced-optionals"
checksum: "2ec91504e7910625"
fetched: "2026-06-21T13:05:41"
---

* [Robot Simulation](../robot_simulation/index.html)
* [Motion Generation (Deprecated)](motion_generation_overview.html)
* cuRobo and cuMotion

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# cuRobo and cuMotion

Note

The cuRobo and cuMotion tutorials here are no longer maintained. The [cuMotion integration](../cumotion/index.html#isaac-sim-cumotion)
contains much of the same functionality.

Note

This cuRobo tutorial is not supported on aarch64 platforms.

## Learning Objectives

[cuRobo](https://curobo.org) (also on [GitHub](https://github.com/NVlabs/curobo)) is a high-performance,
GPU-accelerated robotics motion generation library for robot manipulators, developed by NVIDIA Research.
It is a standalone Python library that interfaces directly with NVIDIA Isaac Sim, simplifying both testing in simulation
and deploying on physical robots.

[NVIDIA cuMotion](https://nvidia-isaac-ros.github.io/concepts/manipulation/index.html#nvidia-cumotion),
available as a Developer Preview in Isaac 3.0, is a production motion generation package for
manipulators. The current version leverages cuRobo as its backend, providing collision-free motion planning using a
plugin for [MoveIt 2](https://moveit.picknik.ai) and a set of supporting ROS 2 packages. For an example of using
cuMotion with NVIDIA Isaac Sim using the ROS 2 bridge, see the relevant
[section](https://nvidia-isaac-ros.github.io/concepts/manipulation/cumotion_moveit/tutorial_isaac_sim.html)
of the Isaac ROS documentation. This example is somewhat limited in Isaac 3.0 but will be expanded in a future
release.

In the remainder of this tutorial, we focus on direct integration of cuRobo into NVIDIA Isaac Sim, covering cuRobo
installation and use, with examples for collision-free inverse kinematics, motion planning, and reactive
control (MPPI).

## Getting Started

**Prerequisites**

* Complete the [Adding a Manipulator Robot](../core_api_tutorials/tutorial_core_adding_manipulator.html#isaac-sim-app-tutorial-core-adding-manipulator) tutorial prior to beginning this tutorial.

## Installation

Follow the [cuRobo installation instructions](https://curobo.org/get_started/1_install_instructions.html) for
installing cuRobo and required libraries. cuRobo supports NVIDIA Isaac Sim 2022.2.1 and later. Follow the
[workstation installation instructions](../installation/install_workstation.html#isaac-sim-app-install-workstation) to install NVIDIA Isaac Sim.

## Examples

### Using Isaac Sim with cuRobo

In the cuRobo documentation, refer to the
[âUsing Isaac Simâ section](https://curobo.org/get_started/2b_isaacsim_examples.html) for an overview of how cuRobo
is interfaced to Isaac Sim, along with a series of standalone examples demonstrating collision checking, motion
generation, inverse kinematics, model-predictive control, and multi-arm reaching.

### Using Isaac Sim with cuRobo and nvblox

In the cuRobo documentation, refer to the
[âUsing with Depth Cameraâ section](https://curobo.org/get_started/2d_nvblox_demo.html) for examples of
obstacle-aware motion generation in NVIDIA Isaac Sim, both with pre-generated signed distance fields (SDFs)
from [nvblox](https://github.com/nvidia-isaac/nvblox) and with online mapping leveraging nvblox with a
physical RealSense depth camera.

On this page

* [Learning Objectives](#learning-objectives)
* [Getting Started](#getting-started)
* [Installation](#installation)
* [Examples](#examples)
  + [Using Isaac Sim with cuRobo](#using-isaac-sim-with-curobo)
  + [Using Isaac Sim with cuRobo and nvblox](#using-isaac-sim-with-curobo-and-nvblox)