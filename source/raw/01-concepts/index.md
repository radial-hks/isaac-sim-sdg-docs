---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/index.html
title: "What Is Isaac Sim?"
section: "入门"
module: "01-concepts"
checksum: "11d5e374bff37356"
fetched: "2026-06-21T14:14:17"
---

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# What Is Isaac Sim?

Import robots and scenes from URDF, MJCF, Onshape CAD, or USD. Simulate with PhysX or Newton, add RTX and physics-based sensors, generate synthetic data, prepare robots for Isaac Lab, and validate robot stacks with ROS 2.

[Quick Install](installation/quick-install.html)
[Browse Tutorials](#tutorials)

* [Open source on GitHub](https://github.com/isaac-sim)

## Getting Started

Pick the setup that matches how you work. Most users should start
with **Quick Install**. Choose Python or containers when you need
pip, conda, CI, or remote workflows.

Quick Install

Fastest path to a working local setup

[Quick Install](installation/quick-install.html#isaac-sim-quick-install)

Workstation Setup

Install the full app and local dependencies

[Workstation Installation](installation/install_workstation.html#isaac-sim-app-install-workstation)

Container Setup

Run Isaac Sim in Docker for repeatable setups

[Container Installation](installation/install_container.html#isaac-sim-app-install-container)

Python Environment

Use pip or conda for Python-first workflows

[Python Environment Installation](installation/install_python.html#isaac-sim-app-install-python)

Tip

**Running into issues?** See [Setup Tips](installation/install_faq.html) for common fixes or the [Troubleshooting](overview/troubleshooting.html#isaac-sim-troubleshooting) page.

---

## Tutorials

Start with the topics users look for most: first simulation, robot
import, sensors, ROS 2, synthetic data, and robot learning.

BeginnerLearn the app, scenes, and core robot workflows

Basic Usage Tutorial

First steps: navigate the UI, load a scene, and run your first simulation.

[Isaac Sim Basic Usage Tutorial](introduction/quickstart_isaacsim.html#isaac-sim-app-intro-quickstart)

Python Scripting Intro

Write your first standalone script to control robots and environments.

[Python Scripting and Tutorials](python_scripting/index.html#isaac-sim-app-python-scripting-overview)

Import Your First URDF

Bring a URDF robot into Isaac Sim, configure it, and simulate it on a stage.

[Tutorial: Import URDF](importer_exporter/import_urdf.html#isaac-sim-app-tutorial-advanced-import-urdf)

IntermediateConnect ROS 2, control simulations, and build data generation workflows

ROS 2 TurtleBot Series

Follow the TurtleBot flow from import and driving to sensors, timing, and transforms.

[URDF Import: Turtlebot](ros2_tutorials/tutorial_ros2_turtlebot.html#isaac-sim-app-tutorial-ros2-turtlebot)

Synthetic Data with Replicator

Generate labeled training data from Isaac Sim scenes with Replicator.

[SDG Workflows](replicator_tutorials/tutorial_replicator_sdg_workflows.html#isaac-sim-app-tutorial-replicator-sdg-workflows)

ROS 2 Simulation Control

Use ROS 2 services and actions to load worlds, spawn entities, and step simulations.

[ROS2 Simulation Control](ros2_tutorials/tutorial_ros2_simulation_control.html#isaac-sim-app-tutorial-ros2-simulation-control)

AdvancedTrain policies, randomize scenes, and deploy results

Prep a Robot for Isaac Lab

Rig your robot and stage a scene in Isaac Sim so Isaac Lab can train policies on it.

[Isaac Lab](isaac_lab_tutorials/index.html#isaac-lab-tutorials-page)

AMR Navigation Synthetic Data

Drive an AMR through randomized warehouse scenes and capture stereo camera data when it nears objects of interest.

[Randomization in Simulation – AMR Navigation](replicator_tutorials/tutorial_replicator_amr_navigation.html#isaac-sim-app-tutorial-replicator-amr-navigation)

ROS 2 Policy Evaluation

Run a reinforcement learning policy through ROS 2 while Isaac Sim publishes observations and receives actions.

[Running a Reinforcement Learning Policy through ROS 2 and Isaac Sim](ros2_tutorials/tutorial_ros2_rl_controller.html#isaac-sim-app-tutorial-ros2-rl-controller)

---

## Isaac Sim Workflow Overview

Isaac Sim

[RTX](https://docs.omniverse.nvidia.com/materials-and-rendering/latest/rtx-renderer.html)
[Newton](https://developer.nvidia.com/newton-physics)
[PhysX](https://nvidia-omniverse.github.io/PhysX/)
[OmniGraph](https://docs.omniverse.nvidia.com/extensions/latest/ext_omnigraph.html)
[Replicator](https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator.html)
[OpenUSD](https://openusd.org/)

Simulation Development Loop

Bring assets in, configure the robot and scene, simulate behavior, then connect external stacks.

Overview

Synthetic Data Generation

Software-in-the-loop Testing

Each stage stays reusable: asset prep, robot and scene configuration, simulation, and stack connection all operate on the shared Isaac Sim scene.

For SDG, label the scene, vary conditions, simulate behavior, and render sensor outputs for downstream datasets.

For SIL, configure robot physics, sensors, and communication graphs, then validate the external robot stack before hardware.

01
**Import**

Scenes, robots, sensors, assets

Scene assets

Target objects

Sensor assets

Robot assets

Robot descriptions

CAD / USD / NuRec

02
**Configure**

Shared setup, then workflow-specific wiring

Materials

Sensors

Scenarios

Semantics

Randomization

Tune robot physics

Communication graph

03
**Simulate**

Run the world and capture evidence

Physics stepping

Sensor output

Randomization

Annotation capture

Rendered frames

Control loop

Stack behavior

04
**Connect / Deploy**

Send results to training or robot stacks

Dataset writers

Training pipelines

Model evaluation

Failure-case tests

Robot stack

Pre-hardware tests

Shared Isaac Sim Scene

USD scene, physics state, sensors, semantics, and graphs in one runtime.

**01
Import**
Bring robot, scene, sensor, CAD, DCC, and reconstructed assets into a shared USD workspace.

**02
Configure**
Set materials, sensors, scenarios, semantics, robot physics, and communication graphs.

**03
Simulate**
Run physics, sensor output, Replicator capture, and stack behavior on the assembled scene.

**04
Connect / Deploy**
Export datasets to training pipelines or connect external robot stacks for pre-hardware validation.

---

## Robotics Ecosystem

Understanding the components of the NVIDIA robotics ecosystem and
where Isaac Sim fits among them.

Software-in-the-Loop Testing

Each row shows the workflow step and the NVIDIA component that supports it.

1. 01

   **Build the scene & rig the robot**

   **Isaac Sim**

   Robotics simulator

   [Open docs](https://docs.isaacsim.omniverse.nvidia.com/)

   Assemble USD scenes, run physics and sensors, connect external robot stacks.
2. 02

   **Train an RL or IL policy**

   Optional

   **Isaac Lab**

   RL / IL framework

   [Open docs](https://isaac-sim.github.io/IsaacLab/)

   Train RL and imitation-learning policies with parallel environments.
3. 03

   **Evaluate policy at scale**

   Optional

   **Lab - Arena**

   Policy benchmark

   [Open docs](https://developer.nvidia.com/isaac/lab-arena)

   Benchmark and compare trained policies across many scenes and seeds.
4. 04

   **Run the integrated SIL test**

   **Isaac Sim**

   SIL test stack

   [Open docs](https://docs.isaacsim.omniverse.nvidia.com/)

   Run software-in-the-loop tests with your ROS 2 or Isaac ROS robot stack.

Synthetic Data Generation

Each row shows the workflow step and the NVIDIA component that supports it.

1. 01

   **Bring in real-world environments**

   Optional

   **NuRec**

   Reconstructed scenes

   [Open docs](https://developer.nvidia.com/omniverse/nurec)

   Gaussian-splat reconstructions of real environments, loaded as USD assets.
2. 02

   **Assemble & configure the scene**

   **Isaac Sim**

   Robotics simulator

   [Open docs](https://docs.isaacsim.omniverse.nvidia.com/)

   Assemble USD scenes, configure robots and sensors, run physics and rendering.
3. 03

   **Define variation, simulate, & write annotations**

   **Replicator**

   SDG framework in Isaac Sim

   [Open docs](https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator.html)

   Script randomization, capture sensor outputs, and write labeled datasets.
4. 04

   **Photoreal augmentation**

   Optional

   **Cosmos Transfer**

   Photoreal augmentation

   [Open docs](https://docs.nvidia.com/cosmos/latest/transfer2.5/index.html)

   Convert rendered RGB plus a text prompt into varied photoreal images, offline.

---

## Open Source & Community

Isaac Sim is open source and built to fit into existing robotics
stacks. Use the shipped tools, read the code, or extend the
simulator with Python and Kit.

Open-source platform

Read the code, extend the simulator, and fit it into your stack.

Start with the built-in tools, then automate with Python, build custom Kit apps, or integrate Isaac Sim into your own ROS 2 and ML workflows.

[Browse GitHub](https://github.com/isaac-sim)
[Install via pip](https://pypi.org/project/isaacsim/)

**Apache 2.0**

Open-source licensing for the simulator stack.

**USD-native**

One scene representation from asset import to deployment.

**PhysX + Newton**

Switch between supported physics backends in one simulator.

**RTX + Physics Sensors**

Use rendering and physics-based sensor models in one place.

[Forum

Ask questions and get help from the NVIDIA developer community.](https://forums.developer.nvidia.com/c/omniverse/simulation/69)[Discord

Chat with other Isaac Sim users and developers in real time.](https://discord.gg/4ZsTFksGh8)[Release Notes

Track the latest features, fixes, and version changes across Isaac Sim releases.](overview/release_notes.html)[Help & FAQ

Start with common installation fixes, troubleshooting, and support guidance.](overview/help.html)

On this page

* [Getting Started](#getting-started)
* [Tutorials](#tutorials)
* [Isaac Sim Workflow Overview](#isaac-sim-workflow-overview)
* [Robotics Ecosystem](#robotics-ecosystem)
* [Open Source & Community](#open-source-community)