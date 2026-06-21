---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/action_and_event_data_generation/index.html
title: "Action & Event Data Gen Index"
section: "概览"
module: "03-replicator-agent"
checksum: "1aa16f70bf80d6e8"
fetched: "2026-06-21T11:55:26"
---

* [Synthetic Data Generation](../synthetic_data_generation/index.html)
* Action and Event Data Generation

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Action and Event Data Generation

**Action and Event Data Generation** is a reference application for Isaac Sim that provides a suite of extensions for realistic indoor simulation and large-scale synthetic data generation. It is designed to address the challenges of collecting high-quality, diverse, and richly labeled datasets for training Vision AI models.

Real-world data collection often faces limitations in scalability, cost, and the ability to capture rare or dangerous scenarios (such as accidents or near-misses). This application enables the programmatic generation of synthetic data that is accurate and diverse, effectively bridging the gap between simulation and real-world deployment.

## Key Features

* **Ground Truth Generation**: Provides accurate ground truth across multiple modalities by leveraging [Replicator](../replicator_tutorials/index.html#isaac-replicator-tutorials-page) for precise data capture and rich annotation.
* **Rare Event Generation**: Enables the programmatic creation of rare and long-tail events to improve model robustness.
* **Scalable Workflow**: Supports both an interactive interface for rapid prototyping and a headless batch generation mode for producing massive, reproducible datasets.
* **Configurable Control**: Utilizes YAML configuration files to define scenes, agents, and events, ensuring the data generation process is versionable and reproducible.

## Architecture and Workflow

Built on the Omniverse platform, this toolset integrates technologies such as [Omniverse Animation](https://docs.omniverse.nvidia.com/extensions/latest/ext_anim.html) for character behaviors, [Omniverse Flow](https://docs.omniverse.nvidia.com/extensions/latest/ext_fluid-dynamics/using.html) for dynamic events, and [Replicator](../replicator_tutorials/index.html#isaac-replicator-tutorials-page) for data capture.

The architecture employs a layered approach to scene construction and data capture. **Object Simulation** defines the static environment, which serves as the foundation for dynamic elements introduced by **Event Generation** and **Actor Simulation**. The pipeline culminates in the data acquisition phase, where **Sensor Placement** optimizes sensor coverage and **VLM Scene Captioning** synthesizes semantic descriptions.

## Launching the Application

To launch the app, use:

* **Linux**: `./isaac-sim.action_and_event_data_generation.sh`
* **Windows**: `.\isaac-sim.action_and_event_data_generation.bat`

The application launches with the Action and Event Data Generation extensions pre-enabled and a custom workspace layout.

Tip

**New to Action and Event Data Generation?** Start with the [Actor Simulation and Synthetic Data Generation](tutorial_replicator_agent.html#actor-sim-getting-started) tutorial for an end-to-end walkthrough with a default config.

## Action and Event Data Generation Stack

## Extensions

The core functionality is provided by a set of application-level extensions and supporting tools:

| Extension | API Name | Description |
| --- | --- | --- |
| Actor Simulation and SDG | `isaacsim.replicator.agent.core` | The **Isaac Sim Replicator Agent (IRA)** extension simulates intelligent actors in 3D environments. It handles complex human and robot behaviors, from large-scale routines like warehouse operations (for example, workers patrolling, forklifts roaming) to specific reactions to dynamic events. It captures diverse data and action metadata. |
| Object Simulation and SDG | `isaacsim.replicator.object.core` | The **Isaac Sim Replicator Object (IRO)** extension allows you to programmatically create and place objects at scale. It can procedurally generate unique shapes, automatically stack racks, and pack boxes before applying physics to settle the scene realistically. |
| Physical Space Event Generation | `isaacsim.replicator.incident.core` | The **Isaac Sim Replicator Incident (IRI)** extension generates realistic, configurable physical events. It orchestrates simulations using Omniverse Flow and PhysX to create scenarios ranging from spills and toppling boxes to complex fires with smoke, all with rich annotation and event metadata. |
| VLM Scene Captioning | `isaacsim.replicator.caption.core` | The **Isaac Sim Replicator Caption (IRC)** extension bridges the gap between vision and language. It analyzes the scene to build a scene graph (objects and spatial relationships) and uses an LLM to generate rich, human-readable descriptions (global and brief captions) and visualized scene graphs. |
| RTX Sensor Placement | `isaacsim.sensors.rtx.placement` | The **RTX Sensor Placement (ISP)** extension automates camera positioning. It algorithmically places sensors to maximize visual coverage, focus on points of interest, control occlusion, or create Birdâs-Eye-View groups, while extracting intrinsic and extrinsic calibration data. |
| RTX Sensor Calibration | `isaacsim.sensors.rtx.calibration` | The **RTX Sensor Calibration (ISC)** extension generates camera calibration data for deployed cameras in the scene. |
| Behavior Tree Generation | `omni.ai.behavior_tree_gen.core` and `omni.ai.behavior_tree_gen.bridge` | The **Behavior Tree Generation** workflow converts natural-language scenarios into behavior tree outputs. `omni.ai.behavior_tree_gen.core` provides the reusable pipeline and scripted API, while `omni.ai.behavior_tree_gen.bridge` provides the Kit UI, example loaders, and interactive workflow orchestration. |
| Animated Robot Controller | `isaacsim.anim.robot.core` | The **Animated Robot Controller (IAR)** extension enables realistic robot animation by playing back captured simulation motion data. It bridges physics-based simulation and animation, allowing for precise robot movements without the overhead of real-time physics. |
| Action and Event Data Generation Utilities | `omni.metropolis.utils` | The **Action and Event Data Generation Utilities (OMU)** extension provides shared utilities across the Action and Event Data Generation extension stack. |
| Chat IRO | `omni.ai.langchain.agent.chat_iro` | **Chat IRO** is an AI assistant that enables natural language scene authoring for the **Object Simulation (IRO)** extension. It allows users to describe scenes in plain English to automatically generate YAML configurations, providing immediate viewport previews and iterative editing capabilities. |

## Extension Tutorials

* [Actor Simulation and Synthetic Data Generation](tutorial_replicator_agent.html)
* [Behavior Tree Generation](tutorial_behavior_tree_gen.html)
* [Object Simulation and Synthetic Data Generation](tutorial_replicator_object.html)
* [VLM Scene Captioning](tutorial_replicator_caption.html)
* [Physical Space Event Generation](tutorial_replicator_incident.html)
* [RTX Sensors Placement and Calibration](tutorial_sensors_rtx_placement.html)

## Integration Tutorials

End-to-end examples that wire multiple extensions together.

* [Reacting to Events with Actor Triggers](example_event_reactive_actors.html)

## Other Tools and Utilities

* [Omni Metropolis Pipeline](tutorial_omni_metropolis_pipeline.html)
* [Telemetry and Performance Tracking](tutorial_telemetry.html)

On this page

* [Key Features](#key-features)
* [Architecture and Workflow](#architecture-and-workflow)
* [Launching the Application](#launching-the-application)
* [Action and Event Data Generation Stack](#action-and-event-data-generation-stack)
* [Extensions](#extensions)
* [Extension Tutorials](#extension-tutorials)
* [Integration Tutorials](#integration-tutorials)
* [Other Tools and Utilities](#other-tools-and-utilities)