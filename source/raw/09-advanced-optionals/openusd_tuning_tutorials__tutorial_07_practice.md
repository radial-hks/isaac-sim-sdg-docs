---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/openusd_tuning_tutorials/tutorial_07_practice.html
title: "Tutorial 07: Practice"
section: "USD Tuning"
module: "09-advanced-optionals"
checksum: "9aafab87b0b71d21"
fetched: "2026-06-21T14:14:41"
---

* [Robot Setup](../robot_setup/index.html)
* [OpenUSD and Tuning Best Practices Tutorial Series](index.html)
* Tutorial 7: Using the Dexterous Hand in Practice

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Tutorial 7: Using the Dexterous Hand in Practice

With asset structure verified, collision pairs filtered, and joint parameters tuned, the Inspire Hand in Isaac Sim is stable and ready for downstream use.

## Learning Objectives

In this tutorial, you will:

* **Review** what you accomplished across the OpenUSD and Tuning Best Practices series.
* **Learn** next steps for using the tuned Inspire Hand (attach to an arm, watch demos, fine tune, extend to other hands).
* **Find** additional documentation and resources for PhysX and articulation.

## Prerequisites

* Complete [Tutorial 6: Joint Gains Tuning](tutorial_06_joint_gains_tuning.html#isaac-sim-tutorial-tuning-openusd-module-5). You should have a tuned, stable Inspire Hand USD.

## What You Accomplished

* **Tutorial 2** — You inspected the multi-physics asset structure.
* **Tutorial 3** — You enabled joint and mass/inertia visualization, and verified collision meshes.
* **Tutorial 4** — You identified problematic self-collisions and added filtered pairs so the hand simulates without artifacts.
* **Tutorial 5** — You set mimic joints, max joint torque, and max velocity from specs.
* **Tutorial 6** — You tuned drive stiffness and damping with the Gain Tuner and analyzed results with the built-in charts.

You now have a tuned, stable robotic hand USD that can be attached to an arm and used with a grasping controller in Isaac Sim or Isaac Lab.

## Next Steps

* **Attach to an arm** — Use the hand as an end effector on a manipulator (e.g. Kuka) in Isaac Sim or Isaac Lab and run grasping or manipulation tasks.
* **Watch applied demos** — Look for Isaac Lab Kuka + Inspire Hand demos (e.g. from GTC) to see the same hand used in full workflows.
* **Fine Tune in Simple Scene Setups** — Bring the hand into simple scenes involving contact. Tune mimic joint compliance as needed for realistic and stable behavior in contact scenarios.
* **Extend tuning** — Apply the same process (collision filters, max force/velocity, stiffness/damping) to other digits or to custom dexterous hands.

## Additional Resources

* [NVIDIA Isaac Sim Documentation](https://docs.omniverse.nvidia.com/isaacsim/latest/)
* [Physics and Rigid Body Dynamics](https://docs.omniverse.nvidia.com/isaacsim/latest/core/physics_tutorials/tutorial_rigid_body_dynamics.html) — For deeper coverage of PhysX and articulation.

## Summary

This tutorial reviewed what you accomplished in the series, outlined next steps for using the tuned Inspire Hand (attach to an arm, demos, fine tuning, extending to other hands), and pointed to additional resources for further learning.

On this page

* [Learning Objectives](#learning-objectives)
* [Prerequisites](#prerequisites)
* [What You Accomplished](#what-you-accomplished)
* [Next Steps](#next-steps)
* [Additional Resources](#additional-resources)
* [Summary](#summary)