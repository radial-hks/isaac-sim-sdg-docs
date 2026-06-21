---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/openusd_tuning_tutorials/index.html
title: "OpenUSD Tuning Index"
section: "USD Tuning"
module: "09-advanced-optionals"
checksum: "c32da09406ce169f"
fetched: "2026-06-21T13:05:45"
---

* [Robot Setup](../robot_setup/index.html)
* OpenUSD and Tuning Best Practices Tutorial Series

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# OpenUSD and Tuning Best Practices Tutorial Series

This tutorial series gives you the intuition and science of physics tuning for robotic assets in NVIDIA Isaac Sim so that your simulated robots behave realistically. Rigging and tuning complex assetsâsuch as a dexterous handâis foundational to successful robot learning and simulation. If the asset is not properly configured (collision meshes, mass properties, joint parameters), the simulation will be unstable, inaccurate, and unusable for training and validation.

Over this series, you work hands-on with the Inspire Hand asset in Isaac Sim to inspect the robot USD and asset structure, apply OpenUSD best practices for performance and stability, and tune joint parameters and control gains for stable, critically damped motion.

This series takes approximately 60â90 minutes to complete as a hands-on lab.

## Learning Objectives

By the end of this series, you will be able to:

* **Explain** the end-to-end process for inspecting and preparing robot USD assets for simulation.
* **Apply** best practices to optimize the robot USD for performance and stability.
* **Tune** joint parameters and control gains to achieve stable, critically damped, and realistic robot motion in simulation.

We start by inspecting the robot USD, then configuring collision filters to manage self-collision, and finally tuning joint parameters: drive limits (max force, max velocity) and stiffness and damping with the Gain Tuner. By the end, you will have a stable, functioning robotic hand ready to attach to an arm for a grasping controller.

## Tutorials in This Series

* [Tutorial 1: Setup](tutorial_01_setup.html)
* [Tutorial 2: Asset Structure](tutorial_02_asset_structure.html)
* [Tutorial 3: Inspect Asset](tutorial_03_inspect_asset.html)
* [Tutorial 4: Collider Pairs](tutorial_04_collider_pairs.html)
* [Tutorial 5: Joint Drive Tuning](tutorial_05_joint_drive_tuning.html)
* [Tutorial 6: Joint Gains Tuning](tutorial_06_joint_gains_tuning.html)
* [Tutorial 7: Using the Dexterous Hand in Practice](tutorial_07_practice.html)

To get started, see [Tutorial 1: Setup](tutorial_01_setup.html#isaac-sim-tutorial-tuning-openusd-setup).

On this page

* [Learning Objectives](#learning-objectives)
* [Tutorials in This Series](#tutorials-in-this-series)