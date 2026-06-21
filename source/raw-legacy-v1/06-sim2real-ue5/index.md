---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/isaac_lab_tutorials/index.html
title: "Isaac Lab Index"
section: "Isaac Lab (RL)"
module: "06-sim2real-ue5"
checksum: "9d85a511dac7ee66"
fetched: "2026-06-21T13:40:03"
---

* Isaac Lab

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Isaac Lab

## Overview

Isaac Lab is the official robot learning framework for Isaac Sim, providing APIs and examples for reinforcement learning,
imitation learning, and more. The framework provides the ability to design tasks in different workflows, including
a modular design to easily and efficiently create robot learning environments, while leveraging the latest simulation capabilities.

Some of its core features include:

* Modular configuration-driven system to easily create and modify environments
* Flexible user-designed workflow for optimized performance
* Suite of robot learning environments for training and evaluation
* Support for different reinforcement learning and imitation learning libraries
* Connection to peripheral devices, such as game-pads and keyboards, for collecting demonstrations
* Ability to augment simulation with custom actuator models for sim-to-real transfer

## Isaac Lab Resources

For more information and documentation for Isaac Lab, see the following external references:

* [Isaac Lab Repository](https://github.com/isaac-sim/IsaacLab)
* [Isaac Lab Documentation](https://isaac-sim.github.io/IsaacLab)

## Suggested Isaac Sim Tutorials

The following set of tutorials details usage of reinforcement learning related components in Isaac Sim.

**Robot Setup**

* [Importing URDF](../importer_exporter/import_urdf.html#isaac-sim-app-tutorial-advanced-import-urdf)
* [Importing MJCF](../importer_exporter/import_mjcf.html#isaac-sim-app-tutorial-advanced-import-mjcf)
* [Simulation Fundamentals](../physics/simulation_fundamentals.html#simulation-fundamentals)

**Deploying Policies**

* [Rigging a Legged Robot for Policy Inference](../robot_setup_tutorials/tutorial_rig_legged_robot.html#isaac-sim-app-tutorial-rig-legged-robot)
* [Policy Deployment](tutorial_policy_deployment.html#isaac-sim-app-tutorial-policy-deployment)
* [Policy Deployment in ROS 2](../ros2_tutorials/tutorial_ros2_rl_controller.html#isaac-sim-app-tutorial-ros2-rl-controller)

**Data Generation**

* [Getting Started with Cloner](tutorial_cloner.html#isaac-sim-app-tutorial-cloner)
* [Instanceable Assets](tutorial_instanceable_assets.html#isaac-sim-app-tutorial-instanceable-assets)

**Python Scripting**

* [Python Scripting](../core_api_tutorials/index.html#isaac-sim-core-api-tutorials-page)

## Troubleshooting

* [Isaac Lab Troubleshooting](troubleshooting.html)

Common Isaac Lab issues and their solutions are documented in the [Isaac Lab Troubleshooting](troubleshooting.html#isaac-sim-isaac-lab-troubleshooting) page. For general simulation troubleshooting, see [Troubleshooting](../overview/troubleshooting.html#isaac-sim-troubleshooting).

## Deprecated Frameworks

Isaac Lab will be replacing previously released frameworks for robot learning and reinforcement learning,
including [IsaacGymEnvs](https://github.com/isaac-sim/IsaacGymEnvs) for the
[Isaac Gym Preview Release](https://developer.nvidia.com/isaac-gym), [OmniIsaacGymEnvs](https://github.com/isaac-sim/OmniIsaacGymEnvs) for
Isaac Sim, and [Orbit](https://isaac-orbit.github.io) for Isaac Sim.

These frameworks are now deprecated in favor of continuing development in Isaac Lab.
We encourage users of these frameworks to migrate your work over to Isaac Lab.
Migration guides are available to support the migration process:

* Migrating from IsaacGymEnvs and Isaac Gym Preview Release: [link](https://isaac-sim.github.io/IsaacLab/main/source/migration/migrating_from_isaacgymenvs.html)
* Migrating from OmniIsaacGymEnvs: [link](https://isaac-sim.github.io/IsaacLab/main/source/migration/migrating_from_omniisaacgymenvs.html)
* Migrating from Orbit: [link](https://isaac-sim.github.io/IsaacLab/main/source/migration/migrating_from_orbit.html)

On this page

* [Overview](#overview)
* [Isaac Lab Resources](#isaac-lab-resources)
* [Suggested Isaac Sim Tutorials](#suggested-isaac-sim-tutorials)
* [Troubleshooting](#troubleshooting)
* [Deprecated Frameworks](#deprecated-frameworks)