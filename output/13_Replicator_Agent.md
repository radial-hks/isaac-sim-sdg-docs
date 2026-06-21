# Replicator Agent

> Replicator Agent 配置 + Behavior Tree Gen + 自定义 Writer
> Isaac Sim 版本: 6.0
> 最后组装: 2026-06-21 12:48 UTC
> 来源页数: 14

---

## 来源链接

- [Action & Event Data Gen Index](https://docs.isaacsim.omniverse.nvidia.com/latest/action_and_event_data_generation/index.html)
- [Replicator Agent Tutorial](https://docs.isaacsim.omniverse.nvidia.com/latest/action_and_event_data_generation/tutorial_replicator_agent.html)
- [Replicator Caption](https://docs.isaacsim.omniverse.nvidia.com/latest/action_and_event_data_generation/tutorial_replicator_caption.html)
- [Replicator Incident](https://docs.isaacsim.omniverse.nvidia.com/latest/action_and_event_data_generation/tutorial_replicator_incident.html)
- [Agent Configuration](https://docs.isaacsim.omniverse.nvidia.com/latest/action_and_event_data_generation/ext_replicator-agent/ext_isaacsim_replicator_agent_configuration.html)
- [Configuration Editor](https://docs.isaacsim.omniverse.nvidia.com/latest/action_and_event_data_generation/ext_replicator-agent/ext_isaacsim_replicator_agent_configuration_editor.html)
- [Custom Writer Example](https://docs.isaacsim.omniverse.nvidia.com/latest/action_and_event_data_generation/ext_replicator-agent/ext_isaacsim_replicator_agent_custom_writer_example.html)
- [Sample Configs](https://docs.isaacsim.omniverse.nvidia.com/latest/action_and_event_data_generation/ext_replicator-agent/ext_isaacsim_replicator_agent_sample_configs.html)
- [Anim Robot](https://docs.isaacsim.omniverse.nvidia.com/latest/action_and_event_data_generation/ext_replicator-agent/ext_isaacsim_anim_robot.html)
- [BT Context Files & Schemas](https://docs.isaacsim.omniverse.nvidia.com/latest/action_and_event_data_generation/ext_behavior_tree_gen/context_files_and_schemas.html)
- [BT Example Walkthrough](https://docs.isaacsim.omniverse.nvidia.com/latest/action_and_event_data_generation/ext_behavior_tree_gen/example_walkthrough.html)
- [BT Required Inputs](https://docs.isaacsim.omniverse.nvidia.com/latest/action_and_event_data_generation/ext_behavior_tree_gen/required_inputs.html)
- [BT Three API Functions](https://docs.isaacsim.omniverse.nvidia.com/latest/action_and_event_data_generation/ext_behavior_tree_gen/three_api_functions.html)
- [BT Gen Tutorial](https://docs.isaacsim.omniverse.nvidia.com/latest/action_and_event_data_generation/tutorial_behavior_tree_gen.html)

---


## 概览

### Action & Event Data Gen Index

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/action_and_event_data_generation/index.html

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

---


## Agent

### Replicator Agent Tutorial

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/action_and_event_data_generation/tutorial_replicator_agent.html

* [Synthetic Data Generation](../synthetic_data_generation/index.html)
* [Action and Event Data Generation](index.html)
* Actor Simulation and Synthetic Data Generation

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Actor Simulation and Synthetic Data Generation

Detecting and tracking animated actors or agents like human characters and robots in diverse environments offers significant value across industries like retail, manufacturing, and logistics. It helps optimize layouts, improve safety, and enhance efficiency. However, collecting real-world data to train detection models is often costly and unscalable.

Synthetic data generation offers a flexible, scalable solution. The `Omni.Metropolis.Pipeline` (OMP), `Isaacsim.Replicator.Agent` (IRA), `Isaacsim.Anim.Robot.Core` (IAR) extensions together provide a way to set up human characters and robots in 3D environments and generate synthetic data.
This framework also provides control over actor behaviors, environments, and sensors, through a configuration file. It aims to provide a GPU-accelerated solution for training computer vision models and testing software-in-the-loop systems.

This framework simplifies simulation customization with features like:

* **Codeless Interaction**: Configurations are expressed in a YAML file. No code is needed to get synthetic data.
* **Simplified Setup**: Included in Isaac Sim, it offers both GUI and scripting interfaces for interactive and headless workflows.
* **High-Fidelity Data**: Leverages Omniverseâs SimReady assets, physics, and rendering to produce realistic imagery and accurate annotations essential for AI training.
* **Seamless Integration**: As part of Kit extensions, it works natively with `omni.anim.behavior`, `omni.anim.navigation`, and `omni.replicator.core`.

Before enabling this extension, read [What Is Isaac Sim?](../index.html#isaac-sim-app-overview) to learn about Isaac Sim and follow [Installation](../installation/index.html) to install Isaac Sim.

## Enable Extensions

1. Follow the [Omniverse Extension Manager guide](https://docs.omniverse.nvidia.com/extensions/latest/ext_core/ext_extension-manager.html) to enable the `Omni.Metropolis.Pipeline`, `Isaacsim.Anim.Robot.Core`, and `Isaacsim.Replicator.Agent.Core & UI`.

   > * The extensions fetch sample assets from Isaac Sim Assets during start. Refer to [Isaac Sim Assets](../assets/usd_assets_overview.html), if you encounter issues for loading assets.
   > * If loading the UI appears to be hanging, try starting Isaac Sim with the flag `--/persistent/isaac/asset_root/timeout=1.0`.
2. The UI panel is accessible by **Tools > Action and Event Data Generation > Actor SDG** and it opens on the right side of the screen.

Note

* To have the extension auto-loaded on startup, check the **autoload** checkbox in the extension manager.
* Because of extension dependencies, a restart of the Isaac Sim app might be required.

Tip

If you encounter unexpected errors, try launching Isaac Sim with the `--reset-user` flag to clear previous user settings.

```python
./isaac-sim.sh --reset-user
```

## Getting Started in the UI

For first-time users, start with the UI. Refer to the [Running from script](#actor-sim-running-from-script) section for running with a Python script in Isaac Sim headless mode.

1. Follow the [Enable Extensions](#actor-sim-enable-extensions) section and open the UI panel.
2. The minimal config is loaded by default. You can also load a separate config file using the folder browser icon.

   > * All the sample config files are in `[Isaac Sim App Path]/extscache/isaacsim.replicator.agent.core-[current-version]/data/sample_configs/`. For a description of each file, refer to [Sample Configs](ext_replicator-agent/ext_isaacsim_replicator_agent_sample_configs.html#ira-sample-configs).
   > * The minimal config file does not have actors or cameras. For a more comprehensive example, use `full_pipeline.yaml` in the above folder. This example can take up more loading time.

3. [Optional] Modify the configuration file to your needs.

   > * Use the **New** icon to create a new config file.
   > * Use the **Reload** icon to reset changes in UI and load the original config file again.
   > * Use the **Save** or **Save As** icon to save the changes in UI to config file.
   > * Use the **Verbose save** checkbox to control how much detail is written when saving your configuration file. When off, the written file is kept compact, only writing the values that are modified. When on, all non-empty fields are included, which is useful if you want a complete reference of every available option or need to share a fully explicit config with others.
4. Click the **Set Up Simulation** button from the top of the UI. It starts loading simulation assets (scene, cameras, actors) according to the configuration.

   > * The scene requires a NavMesh to spawn assets and control them correctly. The scenes in the example config have NavMesh set up in advance. If you are using an external scene, refer to [Navigation Mesh](https://docs.omniverse.nvidia.com/extensions/latest/ext_navigation-mesh.html "(in Omniverse Extensions)") for NavMesh set up.
   > * You can also go to **Window > Navigation > NavMesh** and turn off **Auto-Bake** in the NavMesh settings. Turning it off can increase the performance.
   >
   > Note
   >
   > Clicking **Set Up Simulation** always fully reloads the scene from the current configuration. This includes reopening the base environment USD and re-creating all actors (characters and robots), sensors, and prop layers from scratch. This action discards any manual edits made to the stage after a previous setup. If you want to iterate on the configuration, make your changes in the UI or config file first, then click **Set Up Simulation** to apply them.
5. Click the **Start Data Generation** button from the top of the UI. The simulation and data generation run for the duration (in seconds) specified in the **Simulation Duration** field in the **Actor SDG Setup** panel.
6. When data generation finishes, the output data is available in the **Output Directory** specified in the **Replicator** panel.

   > * By default, it is `%USERPROFILE%\IRA_output` on Windows and `~/IRA_output` on Linux.
   > * For the folder layout, expected filenames, and a checklist to confirm a successful run, refer to [Expected Output](#actor-sim-expected-output).

## Running from Script

For large-scale data generation, launching from a script is more efficient. IRA provides an automatic script (`actor_sdg.py`) to run offline data generation.

To run from script, open a terminal from where Isaac Sim is installed and run the following commands:

* For Linux:
  :   `./python.sh tools/actor_sdg/actor_sdg.py -c [config file path]`
* For Windows:
  :   `.\python.bat tools\actor_sdg\actor_sdg.py -c [config file path]`

Note

* `[config file path]` is the path to the IRA configuration file.
* You must use the `python.sh` or `python.bat` bundled with Isaac Sim to run the script.
* An example config file is also provided in the `/tools/actor_sdg` folder. For a sample Linux run, execute: `./python.sh tools/actor_sdg/actor_sdg.py -c tools/actor_sdg/sample_config.yaml`

## Expected Output

After data generation finishes, IRA writes the simulation output to the directory specified by `output_dir` in the `replicator` block of the configuration. If `output_dir` is not set, the default location is:

* **Linux:** `~/IRA_output`
* **Windows:** `%USERPROFILE%\IRA_output`

The exact layout depends on the writer that is active (refer to [Writer Configuration](ext_replicator-agent/ext_isaacsim_replicator_agent_configuration.html#ira-configuration-file) for the full parameter list). With the default **IRABasicWriter** and the bundled `full_pipeline.yaml` sample config, you should expect a structure similar to the following:

```python
<output_dir>/
âââ <render_product_or_camera_subfolder>/
â   âââ rgb/                          # one file per captured frame
â   â   âââ rgb_0030.png
â   â   âââ rgb_0031.png
â   â   âââ ...
â   âââ camera_params/                # camera intrinsics and pose per frame
â   â   âââ camera_params_0030.json
â   â   âââ ...
â   âââ object_detection.json         # consolidated bounding boxes, skeleton data,
â   â                                 # and per-actor action data.
â   âââ ...                           # one folder per additional annotator that
â                                     # was enabled (semantic_segmentation,
â                                     # instance_segmentation, distance_to_camera,
â                                     # normals, motion_vectors, ...)
âââ ...
```

## API Usage

This extension also exposes a Python API that you can use to set up simulations and generate data from your own script.
Ensure that `isaacsim.replicator.agent.core` is enabled, and use the API as in the following example.

Note

The snippet below uses the minimal config bundled with the extension (`data/sample_configs/minimal.yaml`).

```python
import os

from isaacsim import SimulationApp

# Start the application
simulation_app = SimulationApp({"headless": True})

# Get the utility to enable extensions
from isaacsim.core.utils.extensions import enable_extension

# Enable the IRA extension
enable_extension("isaacsim.replicator.agent.core")
simulation_app.update()

def _get_config_path() -> str:
    """Return path to the minimal IRA config bundled with the extension."""
    import omni.kit.app

    core_ext_path = (
        omni.kit.app.get_app().get_extension_manager().get_extension_path_by_module("isaacsim.replicator.agent.core")
    )
    default_config_file_path = os.path.join(core_ext_path, "data", "sample_configs", "minimal.yaml")
    if not os.path.isfile(default_config_file_path):
        raise FileNotFoundError(f"IRA config not found: {default_config_file_path}")
    return default_config_file_path

async def run_ira_data_generation(setup_simulation: bool = False, run_data_generation: bool = False):
    from isaacsim.replicator.agent.core import api as IRA

    # IRA: load config. Specify the config file path.
    config_path = _get_config_path()
    result = IRA.load_config_file(config_path)
    if not result:
        raise RuntimeError(f"Failed to load IRA config: {config_path}")

    # IRA: get config, you can modify the config here
    config = IRA.get_config_file()
    IRA.set_config(config)

    # IRA: setup simulation (only when setup_simulation is True)
    if setup_simulation:
        await IRA.setup_simulation()

        # Allow a few frames for scene to settle
        import omni.kit.app

        app = omni.kit.app.get_app()
        for _ in range(10):
            await app.next_update_async()

        # IRA: generate data (only when run_data_generation is True)
        if run_data_generation:
            await IRA.start_data_generation_async(will_wait_until_complete=True)

from omni.kit.async_engine import run_coroutine

task = run_coroutine(run_ira_data_generation(setup_simulation=False, run_data_generation=False))
while not task.done():
    simulation_app.update()
```

## Configuration File

The configuration file is the central place to define your simulation. It controls everything from the environment and characters to the sensors and data output. The file uses the YAML format.

The configuration file is organized into these top-level sections:

* `environment`: Defines the simulation environment and assets.
* `character`: Configures human characters.
* `robot`: Configures robots.
* `sensor`: Configures RTX sensors.
* `replicator`: Configures data generation and output.

For detailed configuration instructions, parameter lists, and examples, refer to the following document:

* [Configuration File Guide](ext_replicator-agent/ext_isaacsim_replicator_agent_configuration.html)

### Sample Configs

The extension bundles a small set of ready-to-run YAML configs under
`[ext-path]/data/sample_configs/` so you can review each major feature in
isolation before composing your own. The samples cover both character-behavior
APIs side by side:

* the stable routine-trigger system at the top level
* the experimental behavior-tree system under `behavior_tree/`

If you are starting out, open `minimal.yaml` (the UI loads it on launch) to
review the smallest valid config, then switch to `full_pipeline.yaml`
for an end-to-end demo with sensor placement and writers.

* [Sample Configs](ext_replicator-agent/ext_isaacsim_replicator_agent_sample_configs.html)

## Migrating from IRA 0.x.x

If you are upgrading from IRA 0.x.x (shipped with Isaac Sim 5.1 and earlier),
be aware that IRA 1.x.x (Isaac Sim 6.0+) is a complete architectural redesign.
All core capabilities, such as the following, are carried forward:

* environment loading
* character and robot spawning
* sensor placement
* synthetic data generation

However, the configuration schema, behavior system, and Python API have all changed.
Existing 0.x config files and scripts will not work without modification.

Key reasons for the redesign:

* **Simpler workflow** â The multi-step process of generating, saving, and
  loading external command files is gone. Behaviors are now defined inline in
  the YAML config, reducing setup to two clicks in the UI.
* **Greater flexibility** â Named groups let you define multiple character,
  robot, and sensor populations with independent settings in a single config.
  Multiple data writers can run concurrently with per-writer timing and sensor
  selection.
* **Stronger validation** â Pydantic v2 models validate configs on load and
  surface clear error messages, catching mistakes before the simulation starts.
* **USD-native architecture** â Actor configurations are persisted as USD
  schemas and prims, making them inspectable and editable directly in the
  stage.

For the full migration guide covering every breaking change with before/after
examples and a step-by-step checklist, refer to [Replicator Agent (IRA)](../migration_guides/isaac_sim_6_0/ext_isaacsim_replicator_agent_migration_guide.html#ira-migration-guide-0x-to-1x).

For editing the configuration files through UI or code, refer to the [Configuration Editor API](ext_replicator-agent/ext_isaacsim_replicator_agent_configuration_editor.html#ira-configuration-editor-api):

* [Configuration Editor API](ext_replicator-agent/ext_isaacsim_replicator_agent_configuration_editor.html)

For a practical walkthrough of using the CustomWriter to stream RTSP video from IRA cameras, review the following example:

* [Example: RTSP Streaming with CustomWriter](ext_replicator-agent/ext_isaacsim_replicator_agent_custom_writer_example.html)

## Actor Behaviors

Actor behaviors are achieved by OMP, IRA, and IAR together.

Actors perform a âroutine-triggerâ behavior loop at play. This pattern is configurable by the behaviors and triggers assigned to the actor.

### The Routine Trigger Loop

When no actor triggers are activated, actors perform a routine loop by repeatedly picking behaviors from routines to perform, weighted by their probability, using the `actor global seed`.

When any trigger activates, the actor pauses its routine and performs the behaviors under each active trigger. The system pauses and queues running triggers if a higher-priority trigger fires (lower-priority triggers are skipped).
A trigger is marked complete when all its behaviors finish. The first trigger in the queue then resumes.
After all active triggers complete, the actor returns to its routine.

### Configure Behaviors

After the actors are loaded into the scene from the config file, the configurations are embedded in the USD API schemas and USD Prims. Each actor is represented by a MetroAgentAPI schema and its derived type.
For a human character, it is the `IRACharacterAPI` attached on the SkelRoot prim. For an animated robot, it is the `AnimRobotAPI` attached on the root prim of the robot payload.
Each behavior and trigger becomes an individual USD Prim that the actor USD API can have reference to, each actor trigger prim can also have reference to a list of behaviors.

The actor USD API schema defines basic information of the actor:

* name
* group
* seed
* a routine reference slot and a trigger reference slot

At play, the name, group, and seed will be combined and hashed into a single seed as `actor global seed`. This seed will be used for all the ârandomnessâ of the actor, including random routine picking for the actor itself and the picking within each behavior such as picking a speed from speed range.
This also means the same `actor global seed` displays the same result if other settings and the environment do not change.

Each type of actor behavior is represented by a USD Prim type. It defines the configuration of the behavior:

* weight
* repeat
* behavior

For human characters, the behavior prim types follow the `CharacterXXXBehavior` naming pattern. For animated robots, they are `RobotXXXBehavior`.

Each actor trigger is also a USD Prim. It defines the trigger priority and has a reference to a behavior list to be executed sequentially when this trigger activates.
Human characters and anim robots share the same trigger types that are defined in OMP with the `MetroXXXTrigger` naming pattern.

In addition, the actors leverage `omni.behavior.behavior` (Human characters) and `isaacsim.anim.robot.core` (Animated robots) as their animation implementation.
For more information about them, refer to the following documents:

* [Animated Robot Controller](ext_replicator-agent/ext_isaacsim_anim_robot.html)

### Behavior Tree (Experimental)

Warning

Behavior tree character support is **experimental** and might change in future releases.

In addition to the routine-trigger behavior system described above, IRA 1.3.0 introduces support for driving character behavior through **behavior trees**. Behavior trees are authored with the `omni.behavior.tree.core` and `omni.anim.behavior.tree` extensions.

**Behavior Tree Overview**

A behavior tree is a hierarchical model for decision-making. It is composed of different node types that work together:

* **Action nodes** are the leaf-level nodes where characters perform concrete actions (for example, `MoveTo`, `Wait`).
* **Composite nodes** control logic and execution flow. For example, a `Sequence` node runs its children in order, while a `Selector` node tries children until one succeeds.
* **Modifiers and Decorators** wrap other nodes to alter their behavior, such as `Repeat` (loop a subtree) or `RandomNavMeshPoint` (supply a random destination).

By combining these node types, you can compose arbitrarily complex behaviors. Behaviors from simple wander loops to multi-step conditional sequences, that are all within a single tree definition, without writing code. Compared to the IRA routine system, which picks behaviors randomly by weight, a behavior tree gives full deterministic control over ordering, branching, and looping.

**Relationship to Routines and Triggers**

Note

**Triggers are not currently supported** for behavior-tree character groups. Any reactive or conditional logic must be authored as nodes inside the behavior tree itself.

Behavior tree mode is an alternative to the routine-trigger system. Each character group in the configuration uses **one or the other**: a group either defines `routines` and `triggers` (IRA-style) or references a `behavior_tree`. However, a single configuration file can contain multiple groups, so IRA-style and behavior-tree groups can coexist side by side.

**Workflow**

1. Author a behavior tree using `omni.behavior.tree.ui` and save it as a JSON file. The tree references node libraries `omni.behavior.tree.core` and `omni.anim.behavior.tree` for its action, composite, and modifier nodes. Refer to the [Behavior Treeâs User Guide](https://docs.omniverse.nvidia.com/kit/docs/behavior-tree/latest/user-guide.html) for how to author a behavior tree.
2. In the IRA configuration YAML, create a character group with a `behavior_tree` field pointing to the JSON file. Optionally provide an `overrides` field to assign node parameters for different character groups without modifying the tree file.

   Warning

   The `overrides` field is not currently configurable through the UI. It can only be edited directly in the YAML configuration file or API.
3. Run the simulation as usual. The behavior-tree characters share the same spawning, NavMesh, and data-generation pipeline as IRA characters.

Some sample config files with behavior tree character groups are provided in the `[Isaac Sim Assets Path]/Samples/BehaviorTree` folder as well as bundled in the `data/sample_configs/behavior_tree/` folder in the `isaacsim.replicator.agent.core` extension (refer to [Sample Configs](ext_replicator-agent/ext_isaacsim_replicator_agent_sample_configs.html#ira-sample-configs)). For configuration details, parameter reference, and YAML examples, refer to [Behavior Tree Character Group (Experimental)](ext_replicator-agent/ext_isaacsim_replicator_agent_configuration.html#ira-bt-character-group) in the Configuration File Guide.

Warning

Behavior tree characters set up by IRA still have the `IRACharacterAPI` schema applied, but this is only used for data-generation identification (name, group, semantic labels, and related fields). The characterâs behavior is entirely controlled by the behavior tree through `omni.behavior.tree.core` (OBT). IRA-level settings such as `seed` have no effect on behavior-tree characters.

## Terminology

Isaacsim.Replicator.Agent.Core

The core extension that manages the simulation state. It contains the essential API and modules for setting up the simulation and capturing the synthetic data. Its modules can be called independently.

Isaacsim.Replicator.Agent.UI

The UI extension for IRA. When this extension loads, the core extension is loaded automatically. This extension contains the UI components for easy interaction with the extension.

Configuration File

A `.yaml` file that contains configuration data that defines the key components of a simulation, including the randomization seed, duration of the simulation, number of the actors, and output format. To use the extension, you must load a configuration file or use the UI to generate a YAML file first.

Actor

Actors are controlled by the respective controllers (`omni.behavior.tree` and `isaacsim.anim.robot`) and perform actions in the simulation. The extension supports human characters and robots (Nova Carter, iw.hub) as actors. The terms âactorâ and âagentâ are used interchangeably in this documentation.

Seed

Randomization seed. Given the same seed, the extension can generate the same randomized result for camera and agent location and agent behaviors. With the same seed and the same sequence of operations, the same data is guaranteed to be generated.

Replicator (Omni.Replicator.Core)

The data capturing extension that this extension is based on. More information about the Replicator extension can be found in [Replicator Official Documentation](../replicator_tutorials/index.html).

Behavior Tree

A hierarchical data model for organizing decision-making and actions. A behavior tree is defined as a JSON file and referenced from the IRA configuration. It provides an alternative to the routine-trigger system for controlling character behavior. Refer to the [Behavior Tree documentation](https://docs.omniverse.nvidia.com/kit/docs/behavior-tree/latest/index.html) for more information.

On this page

* [Enable Extensions](#enable-extensions)
* [Getting Started in the UI](#getting-started-in-the-ui)
* [Running from Script](#running-from-script)
* [Expected Output](#expected-output)
* [API Usage](#api-usage)
* [Configuration File](#configuration-file)
  + [Sample Configs](#sample-configs)
* [Migrating from IRA 0.x.x](#migrating-from-ira-0-x-x)
* [Actor Behaviors](#actor-behaviors)
  + [The Routine Trigger Loop](#the-routine-trigger-loop)
  + [Configure Behaviors](#configure-behaviors)
  + [Behavior Tree (Experimental)](#behavior-tree-experimental)
* [Terminology](#terminology)

---

### Replicator Caption

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/action_and_event_data_generation/tutorial_replicator_caption.html

* [Synthetic Data Generation](../synthetic_data_generation/index.html)
* [Action and Event Data Generation](index.html)
* VLM Scene Captioning

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# VLM Scene Captioning

Vision-language models (VLMs) rely on paired
image-caption datasets to learn the complex
relationships between visual content and textual
descriptions. Captions provide the semantic
grounding necessary for models to understand
objects, actions, and contexts within images.
High-quality captions are essential for training
VLMs capable of nuanced scene understanding and reasoning.

Leveraging 3D ground truth from NVIDIA
Omniverse transforms the captioning process by
enabling detailed, accurate, and scalable annotations.
These captions include overall scene descriptions,
object relationships, and spatial reasoning, such as
relative positions and interactions between elements in a camera view.
With 3D metadata, captions can describe not just what
is visible but how elements are arranged and interact,
offering richer contextual understanding.

This approach ensures more consistent and diverse
datasets, allowing VLMs to excel in complex tasks like
spatial reasoning and scene analysis, ultimately
bridging the gap between visual and linguistic comprehension.

`Isaacsim.Replicator.Caption.Core` (IRC) has the following features:

* Generate image-caption pairs for loaded scenes in Omniverse.
* Plug in to other `Isaacsim.Replicator` modules, including
  `Isaacsim.replicator.object (IRO)` and `Isaacsim.replicator.agent (IRA)` to
  generate captions for each frame at their runtime.
* Export scene graphs alongside caption outputs for customized postprocessing
  and caption preparation.

## Python API

IRC provides a Python API (`CaptionAPI`) for programmatic model configuration and caption generation:

Note

The snippet below reads the model API key from the `NVIDIA_API_KEY` environment variable. Generate your own key from the [NVIDIA NIM API key page](https://docs.nvidia.com/nim/large-language-models/latest/getting-started.html#generate-an-api-key) and export it (for example, `export NVIDIA_API_KEY=<API_KEY>`) before running the script.

Setting up the IRC model

```python
import os
from isaacsim.replicator.caption.core.api import CaptionAPI

def setup_irc_model():
    CaptionAPI.set_model_params(
        url="https://integrate.api.nvidia.com/v1",
        name="meta/llama-3.1-8b-instruct",
        key=os.environ["NVIDIA_API_KEY"],
    )
    print("IRC model params set successfully.")

setup_irc_model()
```

After setting up the model, you can generate captions programmatically:

Generating captions via the API

```python
import asyncio
from isaacsim.replicator.caption.core.api import CaptionAPI

def on_done(future):
    captions = future.result()
    print(f"Generated captions: {captions}")

task = asyncio.ensure_future(CaptionAPI.get_captions())
task.add_done_callback(on_done)
```

You can also load an IRC configuration file before generating captions:

Loading an IRC configuration file

```python
from isaacsim.replicator.caption.core.api import CaptionAPI

CaptionAPI.load_config_file("/path/to/irc_config.yaml")
```

### Workflow

`Isaacsim.Replicator.Caption.Core` uses the following workflow to generate captions:

## Scene Graph

A scene graph is an intermediate output for caption generation. It is
a structured representation of a visual scene,
where nodes represent objects and edges denote spatial relationships
between them. It captures how elements are arranged in space,
such as relative positions and orientations. For example, in
an image of a person sitting on a bench under a tree, the graph
would include nodes for âperson,â âbench,â and âtree,â with edges
like âsitting onâ and âunder.â This spatial focus makes scene graphs
valuable for tasks requiring detailed spatial reasoning and scene analysis.

You can export scene graphs alongside caption outputs to
enable flexible and customizable management of scene graph data
for your specific requirements.

### Enable Isaacsim.Replicator.Caption.Core Extension

1. Follow the [Omniverse Extension Manager guide](https://docs.omniverse.nvidia.com/extensions/latest/ext_core/ext_extension-manager.html) to enable the `isaacsim.replicator.caption.core` extension.

   > * The extension fetches sample assets from Isaac Sim Assets during start. Refer to [Isaac Sim Assets](../assets/usd_assets_overview.html) if you encounter issues for loading assets.
   > * If loading the UI appears to be hanging, try starting Isaac Sim with the flag `--/persistent/isaac/asset_root/timeout=1.0`.
2. The IRC UI panel is accessible by **Tools > Action and Event Data Generation > VLM Scene Captioning** and it opens on the right side of the screen.

IRC can be invoked using the following methods:

* [Using the UI panel](#using-ui-panel)
* [Using the IRA extension](#using-ira-extension)
* [Using the IRO extension](#using-iro-extension)

## Using the UI Panel

To launch scene caption generation with the UI panel:

1. After enabling, the extension will appear in the UI panel:
2. To load the stage USD file, open up the `Caption Settings` panel, and then click on the file selector icon.
3. Select the USD file you want to caption. There is a default USD file for demonstration.

   Note

   We include an example USD. You can find it in `[Isaac Sim Assets Path]/Samples/Replicator/Captioning/test_caption.usda`.

   `[Isaac Sim Assets Path]` is the path to [Isaac Sim Assets](../assets/usd_assets_overview.html#isaac-assets-overview)

   Refer to [Isaac Sim Assets Check](../installation/install_faq.html#isaac-sim-setup-assets-check) for how to verify the assets access and how to retrieve the asset path.
4. Click on the **Load Scene** button to load the scene.

   The stage will be loaded in the stage view. If prompted to enable script execution, click **Yes**.
5. Enter the LLM model credentials in the [API key](https://docs.nvidia.com/nim/large-language-models/latest/getting-started.html#generate-an-api-key) field of the **Model Settings** panel; click **Accept** to continue.
6. Under the **Caption Settings** panel, enter the desired caption level â **Brief Caption** for short and **Full Caption** for a more elaborate description. Enter the camera prim path in the **Input Camera Prim Path** field.
   Input the **Output Path** to specify where to save the generated captions, the associated scene graphs, and metadata. Ensure the output path is a valid directory. Click **Generate Scene Graph**.

   Note

   The default service URL and model name are provided as a convenience. The services are hosted by NVIDIA and provided free of charge on a trial basis.
   If the service associated with the default model is not reachable, a different model can be selected from the models available on
   the [NVIDIA NIM API reference page](https://docs.api.nvidia.com/nim/reference/llm-apis). Enter the model identifier in the **Model Name** field of the **Model Settings** panel.

   Itâs also possible to obtain NVIDIA NIMs and host them locally.
   Visit [NVIDIAâs NIM page](https://build.nvidia.com) for more details.
7. The scene graph, the caption, and the corresponding images are generated and saved in the output directory.

Note

Focusing on specific regions of interest (ROIs) in a complex scene can be achieved by positioning a camera appropriately.

The following steps demonstrate how to generate captions for a region of interest (ROI).

8. To generate captions for a region of interest (ROI), select the desired camera from the camera drop-down as shown below:
9. Position the camera at the desired location so that the ROI dominates the view plane, as shown below:
10. Click on the **Generate Scene Graph** button to generate the captions for the ROI, after selecting the desired caption and output parameters described in earlier steps.

## Using the IRA Extension

To launch scene caption generation with IRA, load the a YAML configuration file.
Or use the default configuration file that comes with the extension and
follow the steps below to prepare some environment variables.

The anatomy of an IRC configuration file, used to run the extension
under IRO and IRA, is explained.

1. Prepare the [NVIDIA NIM API key](https://docs.nvidia.com/nim/large-language-models/latest/getting-started.html#generate-an-api-key)
   for the extension to use.

   The extension requires NVIDIA NIM AI to generate captions.
   The credentials must be stored in the environment variables.

   **Linux/Mac:**

   Add to `~/.bashrc` or `~/.bash_profile`:

   ```python
   export NVIDIA_API_KEY=<API_KEY>
   ```

   **Windows:**

   Command Prompt:

   ```python
   set NVIDIA_API_KEY=<API_KEY>
   ```

   Note

   * The NVIDIA NIM API key has a limited lifetime. The number of free credits is limited and is accessible through the account associated with the API key. After the credits are exhausted, you can apply for more credits through the developer portal. Refer to [the developer forum](https://forums.developer.nvidia.com/t/nim-pricing/290144) for more details.
   * If you only need to generate scene graphs without captions, the AI credentials are not required.

### Example `Isaacsim.Replicator.Caption.Core` Configuration File

For example, a configuration file is similar to the following:

```python
isaacsim.replicator.caption.core:
   version: 0.6.6
   camera_prim_path: /World/Cameras/Camera
   scene_path: USD_FILE
   caption_configs:
      save_full_scene_graph: true
      save_pruned_scene_graph: true
      attach_label_to_usd: false
      use_ai_label: false
      visualize_caption: true
      max_object_capacity: 100
      export_edges: true
      global_caption: true
      qa_caption: false
      brief_caption: true
      pruning_ratio: 1.0
      verbose: true
      random_seed: 0
      caption_only: false
      export_world: true
   output_path: OUTPUT_PATH
```

## Global Properties

version

The version of IRC extension. If version does not match, the extension will not work.

camera\_prim\_path

The path to the camera prim in the scene. If not provided, the extension uses the default camera path defined in
the `default_config.yaml` file. However, if there is no camera in the scene, the extension will not work.
You must guarantee that the camera is available in the scene.

scene\_path

The path to the scene USD file. The extension can load the scene from this path. However, if the `scene_path` is
not provided, the extension uses whatever scene is loaded in the app. If no scene is loaded, the extension will not work.

output\_path

The path to the output directory where the generated captions will be saved. If not provided, the extension will use the default output path.

## Caption Configurations

save\_full\_scene\_graph

If True, it will save the full scene graph in the output directory.

The file will be saved as `<output_path>/<Camera Prim Name>/Captions/full_scene_graph.json`.

save\_pruned\_scene\_graph

If True, it will save the pruned scene graph in the output directory. The full scene graph includes
the edges between any two objects at the same level in the Support Tree.

The file will be saved as `<output_path>/<Camera Prim Name>/Captions/pruned_scene_graph.json`.

Note

**Support Tree:** A tree that represents the spatial relationships between objects in the scene.
The root of the tree is the floor (0th level). The direct children of the root are the objects on the floor, which is considered the 1st level.
The objects on the 2nd level are the objects supported by the objects on the 1st level, and so on.

pruning\_ratio

The ratio of the scene graph to be pruned. The scene graph will be pruned to a **Minimum Spanning Tree** (MST).
The pruning ratio determines the percentage of the MST edges to be kept. For example, if `pruning_ratio` is set to `0.5`,
the scene graph is pruned to 50% of the MST edges.

By default, `pruning_ratio` is set to `1.0`, which means the scene graph will not be further pruned after the MST is generated.

random\_seed

An integer for the random process. When `pruning_ratio` is less than `1.0`, the edges will be
randomly removed from the MST. The random seed is used to control the randomness of this process.

attach\_label\_to\_usd

If True, it will attach the automatically generated semantic labels to all prims with an USD address in the scene,
if the prim does not have a semantic label pre-attached.
The automatic semantic label is based on the prim path basename. For example, if the prim path is `/World/Objects/Chair`,
the semantic label will be `Chair`.

With semantic label attached, Omniverse [annotators](https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator/annotators_details.html#annotators-information)
are able to capture the prim for the annotation defined. This is critical for captioning tasks, because prims not
captured by annotators cannot be included in the scene graph and therefore will not be captioned.

use\_ai\_label

If True, it will use the AI-generated labels for the prims with semantic labels in the scene. The AI-generated labels
are preprocessed and stored in the database, and they will be pulled from the database at runtime. This function can
be combined with `attach_label_to_usd: true` to handle the case when target prims does not have semantic labels pre-stored
in the scene file.

visualize\_caption

If True, it will visualize the scene graph on the output images. The visualization will be saved as
<output\_path>/<Camera Prim Name>/Captions/vis\_camera\_scene\_graph.jpg.

max\_object\_capacity

The maximum number of objects that the scene graph can contain. The objects are selected by their 2D bounding
box sizes in the camera view in a reverse order.

export\_edges

If True, the edges of the scene graph will be exported to scene graph files. The edges represent the spatial
relationships between objects.

export\_world

If True, the extension will export 3D World locations of the prims in the scene graph, and save them in the scene
graph files. The 3D World locations are the 3D coordinates of the prims in the world space. If not mentioned, all
other locations are in the camera space.

global\_caption

If True, the extension will generate a global caption for the scene. The global caption describes the overall
scene content and context. This will be saved in the output file
`<output_path>/<Camera Prim Name>/Captions/scene_graph_caption.json`.

qa\_caption

If True, the extension will generate QA captions for the scene. The QA captions are questions and answers
that test the modelâs understanding of the scene.

This will be saved in the output file
`<output_path>/<Camera Prim Name>/Captions/scene_graph_caption.json`.

brief\_caption

If True, the extension will generate brief captions for the scene. The brief captions are the short version of
the global caption. This will be saved in the output file
`<output_path>/<Camera Prim Name>/Captions/scene_graph_caption.json`.

verbose

If True, the extension will print the detailed information of the scene graph generation process, such as the `support tree`,
and the number of nodes and edges in the scene graph.

caption\_only

If True, only the prims whose corresponding USD files have their object caption preprocessed and stored in the database
will be included in the scene graph and following caption generation process.

### Use IRC in `Isaacsim.Replicator.Agent`

[Isaacsim.replicator.agent](tutorial_replicator_agent.html#isaac-sim-app-tutorial-replicator-character) (IRA) is a module that generates
synthetic data on human characters and robots across a variety of 3D environments. With the IRC extension enabled
in IRA, you can generate captions for each frame at the same time.

To enable IRC in IRA:

1. In the IRA configuration file, use IRCâs `SceneGraphWriter` to write the captions to the output directory.

   Example:

   ```python
   isaacsim.replicator.agent:
      version: 1.6.0
      simulation_duration: 5
      environment:
         base_stage_asset_path: "Isaac/Samples/Replicator/Captioning/test_caption.usda"
      sensor:
         groups:
            ceiling_cameras:
               num: 2
               aim_at_targets:
                  distance_range: [5, 10]
                  height_range: [7, 10]
                  focal_length_range: [10, 15]
                  look_down_angle_range: [30, 45]
      character:
         groups:
            warehouse_workers:
               asset_path: "Isaac/People/Characters/"
               num: 5
               routines:
               - wander:
                    weight: 1
                    repeat: 1
                    walk:
                       speed_range: [0.8, 1.5]
                       distance_range: [5.0, 10.0]
                    idle:
                       - animation: idle
                         weight: 1
                         time_range: [2.0, 5.0]
      replicator:
         writers:
            SceneGraphWriter:
               semantic_filter_predicate: "class:*"
               rgb: true
               camera_params: true
               object_info_bounding_box_2d_tight: true
               object_info_bounding_box_2d_loose: true
               object_info_bounding_box_3d: true
               pruning_ratio: 1.0
               global_caption: true
               qa_caption: false
               brief_caption: true
               visualize_caption: true
               max_object_capacity: 100
               export_edges: true
               save_full_scene_graph: true
               save_pruned_scene_graph: true
               export_world: false
               attach_label_to_usd: false
               use_ai_label: false
               verbose: false
               random_seed: 0
               caption_only: false
               scene_graph_interval: 10
               caption_interval: 10
   ```

   The caption output will be stored in the output directory as:

   * pruned scene graph: `<output_dir>/<Camera Prim Name>/caption_pruned_json/scene_graph_pruned_<frame id>.json`
   * full scene graph: `<output_dir>/<Camera Prim Name>/caption_full_json/scene_graph_full_<frame id>.json`
   * captions: `<output_dir>/<Camera Prim Name>/caption/scene_graph_caption_<frame id>.json`

   Below are the other parameters in the `SceneGraphWriter`:

   output\_dir

   The path to the output directory where the generated captions as well as IRA outputs will be saved.
   If not provided, the extension will use the default output path.

   caption\_interval

   The interval of the caption generation process. The caption will be generated every `caption_interval` frames.
   By default, `caption_interval` is set to `1000`.

   scene\_graph\_interval

   The interval of the scene graph generation process. The scene graph will be generated every `scene_graph_interval` frames.
   By default, `scene_graph_interval` is set to `1`.

   skip\_frames

   The number of frames to skip before starting the caption generation process.
   By default, `skip_frames` is set to `0`.

   writer\_interval

   The interval of the writer process. The writer will write the IRA outputs to the output directory every `writer_interval` frames.
   By default, `writer_interval` is set to `1`.

   export\_point\_cloud

   If True, the extension will export the point cloud of the frame. The point cloud will be saved in the output directory because `<output_dir>/<Camera Prim Name>/pointcloud/pointcloud_<frame id>.npy`. By default, `export_point_cloud` is set to False.

   export\_depth

   If True, the extension will export the depth map of the frame. The depth map will be saved in the output directory as
   `<output_dir>/<Camera Prim Name>/depth/depth_<frame id>.npy`. By default, `export_depth` is set to False.
2. Follow the steps in the [Isaacsim.replicator.agent](tutorial_replicator_agent.html#isaac-sim-app-tutorial-replicator-character) tutorial to start the data generation process.

### Use IRC in `Isaacsim.Replicator.Object`

[Isaacsim.replicator.object](tutorial_replicator_object.html#isaac-sim-app-tutorial-replicator-object) (IRO) is a module that composes scenes that are
uniquely domain randomized. With the IRC extension enabled in IRC, you can generate captions for each frame at the same time.

To enable IRC in IRO:

1. In the IRO configuration file, use IRCâs `CombinedIROSceneGraphWriter` to write the IRO output together with captions
   to the output directory.

   Example:

   ```python
   isaacsim.replicator.object:
      version: 0.x.y
      camera_parameters: ...
      caption_configs:
         save_full_scene_graph: true
         save_pruned_scene_graph: true
         attach_label_to_usd: false
         use_ai_label: false
         visualize_caption: true
         max_object_capacity: 100
         export_edges: true
         caption_only: false
         global_caption: true
         qa_caption: true
         brief_caption: true
         pruning_ratio: 1.0
         verbose: true
         random_seed: 0
         caption_writer: CombinedIROSceneGraphWriter
      output_switches:
         caption: True
         ...
   ```

   In the `caption_configs` field, the configurations are the same as in the IRC configuration file, with
   one additional field `caption_writer`.

   caption\_writer

   The writer to write the captions to the output directory. The available writers are:

   * `CombinedIROSceneGraphWriter`: This writer combines the IRO outputs with the captions.
   * `IROSceneGraphWriter`: This writer only writes the captions to the output directory while suppressing other
     :   IRO outputs, such as `labels` (The 2D detection labels). However, it can generate `images`, `distance_to_image_plane` and `pointcloud`.

   The caption output will be stored in the output directory as:

   * pruned scene graph: `<output_dir>/caption/caption_pruned_json/<seed>_<camera_name>.json`
   * full scene graph: `<output_dir>/caption/caption_full_json/<seed>_<camera_name>.json`
   * visualized scene graph: `<output_dir>/caption_rgb/<seed>_<camera_name>.jpg`
   * captions: `<output_dir>/<Camera Prim Name>/caption_dict/<seed>_<camera_name>.json`
2. Follow the steps in the [Isaacsim.replicator.object](tutorial_replicator_object.html#isaac-sim-app-tutorial-replicator-object) tutorial to start the data generation process.

On this page

* [Python API](#python-api)
  + [Workflow](#workflow)
* [Scene Graph](#scene-graph)
  + [Enable Isaacsim.Replicator.Caption.Core Extension](#enable-isaacsim-replicator-caption-core-extension)
* [Using the UI Panel](#using-the-ui-panel)
* [Using the IRA Extension](#using-the-ira-extension)
  + [Example `Isaacsim.Replicator.Caption.Core` Configuration File](#example-isaacsim-replicator-caption-core-configuration-file)
* [Global Properties](#global-properties)
* [Caption Configurations](#caption-configurations)
  + [Use IRC in `Isaacsim.Replicator.Agent`](#use-irc-in-isaacsim-replicator-agent)
  + [Use IRC in `Isaacsim.Replicator.Object`](#use-irc-in-isaacsim-replicator-object)

---

### Replicator Incident

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/action_and_event_data_generation/tutorial_replicator_incident.html

* [Synthetic Data Generation](../synthetic_data_generation/index.html)
* [Action and Event Data Generation](index.html)
* Physical Space Event Generation

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Physical Space Event Generation

## Overview

`Isaacsim.Replicator.Incident` (IRI) is an extension that allows you to generate events
in urban simulation scenes.

Currently, IRI supports the following spontaneous event types,

* Box toppling events
* Fire and smoke events
* Liquid spills

To use IRI in a scene, follow this workflow:

1. Tag items in the scene with an appropriate event type using the property dropdown menu **+ Add > Incident
Tagging**.
Items can be tagged, for instance, as âloose itemsâ that can be knocked
over in a topple event, âspillable itemsâ
that can leak or spill liquid in a spill event, or âflammable itemsâ that can catch fire in a fire event.

2. Save the scene to a usd file to commit that tagging information if you plan on closing and re-opening the scene.
A sample scene with tags already applied is provided in the Content Browser

`[Isaac Sim Assets Path]/Isaac/Samples/Replicator/Incidents/full_warehouse_with_incident_tags.usd`.

Note

* `[Isaac Sim Assets Path]` is the path to your Isaac Sim assets; refer to [Isaac Sim Assets](../assets/usd_assets_overview.html#isaac-assets-overview).
* Refer to [Isaac Sim Assets Check](../installation/install_faq.html#isaac-sim-setup-assets-check) for how to verify the assets access and how to retrieve the asset path.

3. (IRI standalone) Set up an event configuration file which defines what events will occur in the scene by using the **Event Config File** window
located in the menu **Tools > Action and Event Data Generation > Event Config File**.
This configuration can also be saved and loaded later, though it is not saved into the sceneâs usd file and must be saved and loaded separately through
the **Event Config File** panel.
After configuring the events or loading an event config file, press **Set Up Events** to load the demons that will trigger the events at the specified times.

4. Run the simulation with the play button to preview the scene. To generate SDG data you can also use the **Record Events** button in the **Event Config File** window.
Event items are given semantic labels as the simulation runs to support replicatorâs SDG collection. A separate incident report is also written
as JSON (by default `incidents_report.json` in the output directory) to record event details. Refer to [Incident Report JSON](#iri-incident-report-json).

Note

No adjustment is made to the viewport camera during an event, so you must manually find the event in the scene and move the viewport camera there to view it.

Warning

If fire effects do not render correctly during a fire event, disable multi-tick
rendering by setting `/rtx/hydra/supportMultiTickRate` to `false`. The fastest
way is to override it on the command line at launch:

Linux

```python
./isaac-sim.sh --/rtx/hydra/supportMultiTickRate=false
```

Windows

```python
.\isaac-sim.bat --/rtx/hydra/supportMultiTickRate=false
```

For other ways to apply this setting (Script Editor snippet, `.kit` or `.toml`
edits), refer to [Modify Carb Settings](../development_tools/carb_settings.html#isaac-sim-carb-settings). Refer to
[Multi-Tick Rendering](../sensors/isaacsim_sensors_multitick_rendering.html#isaac-sim-sensors-multitick-rendering) for what multi-tick rendering does and
the trade-offs of disabling it.

## IRI Standalone UI Example

This example shows how to use the standalone IRI UI to set up boxes falling off a shelf at a specific time.
It starts with the warehouse scene from the isaac assets folder:

`[Isaac Sim Assets Path]/Environments/Simple_Warehouse/full_warehouse.usd`.

1. Open the warehouse scene and ensuring that the navmesh has been baked. This example
uses the navmesh to determine the direction to topple the items.

1. Select boxes on a shelf and use the **IncidentTagging > LooseItem > Navmesh** button to tag them as loose items. When toppled, these boxes will fall off the shelf towards the nearest navmesh point, which will automatically make them fall towards the walkable area of the scene.
2. Optionally, you can save the scene to save your progress.
3. Open the **Event Config File** window located in the menu **Tools > Action and Event Data Generation > Event Config File**.
4. Remove the default **Spill** and **Fire** events, and examine the remaining default topple event settings.

   > The topple item is set to `$random_loose_item$`, which will randomly select a loose item in the scene to topple. The trigger is a time based trigger, and the time is set to `3` seconds.
5. Press **Set Up Events** to load the topple demon that will topple the item at the specified time.
6. Play the scene and collect event data with the **Record Events** button in the **Event Config File** window. Press **Stop Record** to stop the recording.

An incident report is written to the specified output directory (default file name `incidents_report.json`). Refer to [Incident Report JSON](#iri-incident-report-json) for the JSON layout.

## Scene Tagging

To begin using IRI in a scene, tag the desired possible event items using the custom UI and then save the scene to a usd file using the
standard save dialogue **File > Save**.
Right-click a prim in the stage window or viewport and select **+ Add > Incident
Tagging** and select either `loose items`, `spillable items`, or `flammable items`.
This menu is also accessible in the Property tab under the `+ Add`
button.

Currently tagged items in the scene may be visualized by enabling the Incident Scene Tags visualizer under
the eye icon on top of the viewport. Click **Show By Type > Incident Scene
Tags** and toggle the category of tagged items you wish to view.

### Loose Items

To topple items in a scene, forces are applied in a particular direction that depends
on the type of tag the loose item was given.

#### Random Direction

Items tagged as ârandom directionâ will have a force applied in a random direction.

#### NavMesh Direction

Items tagged as ânavmesh directionâ are expected to be outside of the walkable area of
the agents in the scene. A force will be applied in the direction of the nearest navmesh edge,
useful for items on a warehouse shelf, or on a table.

#### Closest Waypoint Direction

The UI allows you to add âWaypointsâ to the scene. Waypoints are modeled as boxes that can be
placed anywhere in the scene and resized to outline walking paths or aisles.
Items tagged as âclosest waypoint directionâ will have a force applied in the direction of the nearest point on the nearest waypoint.

#### Create Waypoint Prim

To add a waypoint to the scene, use the property dropdown menu and select **Create > Incident/Topple > Topple Destination**.
This button will add a waypoint to the scene for use with closest waypoint loose items.
The prim may be resized and duplicated to create
more complex structures like walking paths.

### Flammable Items

Flammable items are any items that can catch fire. When a flammable item is tagged as such,
it can be a target for a pyro event. The itemâs prim must have a visible mesh under itâs hierarchy to act as the fuel source.

### Spillable Items

Spillable items are any items that can leak or spill liquid. When a spillable item is tagged as such,
it can be a target for a spill event. Itemâs currently leak by instantiating a flat liquid surface onto
prims in the scene marked as âspillable areaâ and which reside underneath the spillable item.

#### Spillable Area Floor

Spillable areas are prims that liquid may spill onto. When a spill event occurs, the liquid will be
instantiated on a prim below the spilling item with this tag. If no such prim exists, the liquid will be
instantiated on the ground at height 0.0.

**Untagging**:
Tagged items may be untagged in the Properties panel and removing any properties in the **Raw Usd Properties** section that begin with âisaacsim\_replicator\_incident\_attr:â.

## Event Configuration in IRI UI

IRI has a standalone UI for configuring events. This UI is accessed by navigating to **Tools > Action and Event Data Generation > Event Config File**.
Here, you can add and configure events in the scene and record them.

After adding an event, you must select and configure a trigger that will initiate the event.
The currently supported triggers are

* `time`: Begin the event at the designated time
* `carb_event`: Begin the event whenever the provided carb event happens. Carb events are the main way to integrate IRI events with other extensions.
* `physical_event`: Use the beginning of another IRI event to trigger this event.

The commands are generated as a YAML file, which can be saved and loaded later, or edited directly to change the events configuration. As this file
is not a part of the usd scene, saving and loading must be done separately using the save and load features in the **Event Config File** panel.

## Event Configuration in IRI Script

IRI saves the event configuration to the script file, which can be edited directly to change the event configuration.

```python
isaacsim.replicator.incident:
version: 0.1.0
global:
    report_dir:
    seed: 654321
event:
    event_list:
    - ToppleEvent:
        name: my topple event
        topple_item:
            item: $random_loose_item$
            topple_nearby_radius: 1.5
        trigger:
            type: time
            time: 3
    - FireEvent:
        name: my fire event
        flammable_item:
            item: $random_flammable_item$
        trigger:
            type: time
            time: 6
    - SpillEvent:
        name: my spill event
        leakable_item:
            item: $random_leakable_item$
            target_size: 1.5
            leak_duration: 5.0
        trigger:
            type: time
            time: 9
```

In this example, three events are defined: a topple event, a fire event, and a spill event.
Each event has a name, and a simple time based trigger that will trigger the event at the specified time.

The next few sections will go over the various event types and the parameters available for each.

### Topple Event

A topple event has the following required fields:

> * name: the name of the event
> * topple\_item: the item to topple. Can be a specific tagged item prim path, or a random tagged item given by $random\_loose\_item$
>   :   + topple\_nearby\_radius: Other loose items within this radius will also be toppled.
> * trigger: the trigger for the event. Can be a time based trigger. Refer to [Trigger Fields](#iri-trigger-section) for the trigger section.

```python
- ToppleEvent:
    name: my topple event
    topple_item:
        item: $random_loose_item$
        topple_nearby_radius: 1.5
    trigger:
        type: time
        time: 1.0
```

Toppled items in the scene will be given the semantic label âincident\_toppled\_itemâ.

### Fire Event

A fire event has the following required fields:

> * name: the name of the event
> * flammable\_item: the item to catch fire. Can be a specific tagged item prim path, or a random tagged item given by `$random_flammable_item$`
> * trigger: the trigger for the event. Can be a time based trigger. Refer to [Trigger Fields](#iri-trigger-section) for the trigger section.

```python
- FireEvent:
    name: my fire event
    flammable_item:
        item: $random_flammable_item$
    trigger:
        type: time
        time: 2.0
```

Flammable items in the scene will be given the semantic label âincident\_flaming\_itemâ. The flame itself will require a custom replicator writer to be written.

The YAML `trigger` above sets the fire start time in seconds on the trigger; the incident report JSON records that trigger under `trigger_data` and adds fire-specific `simulation_data` (`start_time` in frames and `fire_prim`). Refer to [Incident Report JSON](#iri-incident-report-json).

### Spill Event

A spill event has the following required fields:

> * name: the name of the event
> * leakable\_item: the item to spill. Can be a specific tagged item prim path, or a random tagged item given by `$random_leakable_item$`
>   :   + target\_size: the size of the spill area.
>       + leak\_duration: the duration of the spill.
> * trigger: the trigger for the event. Can be a time based trigger. Refer to [Trigger Fields](#iri-trigger-section) for the trigger section.

```python
- SpillEvent:
    name: my spill event
    leakable_item:
        item: $random_leakable_item$
        target_size: 3.0
        leak_duration: 5.0
    trigger:
        type: time
        time: 1.5
```

Leaking items in the scene will be given the semantic label âincident\_leaking\_itemâ. The liquid itself is given a separate semantic label,
âincident\_liquid\_spillâ.

## Triggers

Each event type has a trigger field, which is used to specify when the event should occur.
Here are the parameters for the various trigger types currently supported

**time**

```python
trigger:
    type: time
    # time: the time in seconds
    time: 1.5
```

**carb\_event**

```python
trigger:
    type: carb_event
    # event_name: the name associated to the desired carb event
    event_name: my_extension_custom_event
```

**physical\_event**

```python
trigger:
    type: physical_event
    # incident_name: Each physical event in IRI has a unique name.
    # This triggers at the beginning of the provided IRI event
    incident_name: MyFireEvent
```

## SDG Collection

SDG collection is handled by the replicatorâs SDG writers based on the semantic labels of the event items. The structured incident
metadata file written when you record events is **JSON** (`incidents_report.json` by default; refer to [Incident Report JSON](#iri-incident-report-json)).
It is **not** a YAML event log. The event configuration you save and load in Event Config File remains YAML and is separate from the incident report.

### Incident Report JSON

Recording uses `IncidentReport.start_recording` in `isaacsim.replicator.incident.core`. By default the report file name is
`incidents_report.json` (override with the `file_name` argument).

The file is a JSON object whose **top-level keys are event names** (strings). Each event entry may include any of the following
sections (all optional unless noted for a given event type):

* `event_data`: Event-specific fields from configuration or setup.
* `trigger_data`: Present when the event is launched by a trigger whose callback forwards the trigger to the incident handler (typical for time triggers on all event types). Contains a nested `trigger` object with fields such as `type`, `priority`, and `time`. Time-based triggers use `time` in **seconds** (refer to [Triggers](#iri-trigger-section)).
* `simulation_data`: Simulation timeline metadata in simulation frame indices (integers), not seconds. Do not equate these numbers with trigger time unless you convert it using your timeline FPS or ticks-per-frame.

**Per event type (current implementation):**

* **Topple:** `event_data`, `trigger_data`, and `simulation_data` with `start_time` and `end_time` (frames). `end_time` is when the topple observer considers the event finished (for example, loose items sleeping), not only the trigger instant.
* **Spill:** `event_data`, `trigger_data`, and `simulation_data` with `start_time` and `end_time` (frames). The interval spans from the trigger frame through `trigger_time + leak_duration` in simulation time (see spill `leak_duration` in the YAML/UI).
* **Fire:** `event_data`, `trigger_data` (when the event is triggered through the standard trigger callback), and `simulation_data` with only `start_time` (frame at ignition) and `fire_prim` (USD path of the FlowEmitterBox emitter prim). Fire entries do not include `end_time` in `simulation_data`. Note: `event_data` may include a field such as `flame_emitter` that refers to the flammable item prim path. The `fire_prim` field is separate and points to the emitter prim used for the pyro effect.

Parsers should treat `simulation_data` keys as **event-type-specific** (for example `end_time` is absent for fire) and tolerate missing sections if older builds or code paths omit them.

## API usage

This extension also exposes a Python API which you can use to set up the various incidents from your own script.
Ensure that `isaacsim.replicator.incident.core` is enabled, and use the API as in the following example.

```python
import carb
import isaacsim.core.utils.prims as prims_utils
import omni.kit.commands
import omni.usd
from isaacsim.replicator.incident.core import get_instance
from isaacsim.replicator.incident.core.extension import IncidentExt
from isaacsim.replicator.incident.core.settings import IncidentSettings
from isaacsim.storage.native import get_assets_root_path
from omni.metropolis.pipeline.triggers import TriggersManager
from pxr import Gf, UsdLux

SEED = 12345
SKY_TEXTURE = "/NVIDIA/Assets/Skies/Clear/evening_road_01_4k.hdr"

stage = omni.usd.get_context().get_stage()
assets_root = get_assets_root_path()

# Skybox backdrop via dome light HDRI (skipped if assets are unreachable)
if assets_root is not None:
    dome = UsdLux.DomeLight.Define(stage, "/World/SkyDome")
    dome.GetIntensityAttr().Set(1000.0)
    dome.GetTextureFileAttr().Set(assets_root + SKY_TEXTURE)
    dome.GetTextureFormatAttr().Set(UsdLux.Tokens.latlong)
else:
    carb.log_warn("Could not find Isaac Sim assets folder; skipping sky backdrop")

# Get the incident manager and create pyro event manager
incident_manager = get_instance().get_incident_manager()

# Create a TimeTrigger and add callback
time_trigger = TriggersManager.get_instance().create_trigger_by_dict({"trigger": {"type": "time", "time": 1.0}})
time_trigger.add_callback(lambda trigger: carb.log_info("Trigger fired!"))

# Create 3 cubes with incident tags
# Cube 1: Flammable item (for fire events)
prims_utils.create_prim(
    prim_path="/World/FlammableCube",
    prim_type="Cube",
    position=[-1.0, 0.0, 0.5],
    attributes={"size": 0.5},
)

omni.kit.commands.execute("ApplyFlammableItemTagCommand", prims="/World/FlammableCube", flammable_item_type="Box")
# Create randomly selected fire event
pyro_event_manager = incident_manager.create_pyro_event_manager(
    data_path=IncidentExt.data_path, seed=SEED, report=incident_manager.get_incident_report()
)

pyro_event_manager.generate_pyro_event(
    name="fire event",
    selected_flammable_item_prim_path=IncidentSettings.RANDOM_FLAMMABLE_ITEM,
    pyro_nearby_radius=0.0,
    trigger=time_trigger,
)

# Cube 2: Loose item (for topple events)
prims_utils.create_prim(
    prim_path="/World/LooseCube",
    prim_type="Cube",
    position=[0.0, 0.0, 0.5],
    attributes={"size": 0.5},
)

omni.kit.commands.execute("ApplyLooseItemTagCommand", prims="/World/LooseCube", loose_item_type="RandomDir")
# Create randomly selected topple event
topple_event_manager = incident_manager.create_topple_event_manager(
    seed=SEED, report=incident_manager.get_incident_report()
)
topple_event_manager.generate_topple_event(
    name="topple event",
    selected_loose_item=IncidentSettings.RANDOM_LOOSE_ITEM,
    topple_nearby_radius=0.01,
    trigger=time_trigger,
)

# Cube 3: Leakable item (for spill events)
prims_utils.create_prim(
    prim_path="/World/LeakableCube",
    prim_type="Cube",
    position=[1.0, 0.0, 0.5],
    attributes={"size": 0.5},
)
omni.kit.commands.execute("ApplyLeakableItemTagCommand", prims="/World/LeakableCube", leakable_item_type="Item")

# Create a plane for the floor and tag it as a spillable area
omni.kit.commands.execute(
    "AddGroundPlaneCommand",
    stage=stage,
    planePath="/World/Floor",
    axis="Z",  # Normal along Z-axis for x-y plane (ground)
    size=25.0,
    position=Gf.Vec3f(0.0, 0.0, 0.0),
    color=Gf.Vec3f(0.5, 0.5, 0.5),
)
omni.kit.commands.execute("ApplySpillableAreaTagCommand", prims="/World/Floor", spillable_area_type="Floor")
# Create randomly selected spill event
spill_event_manager = incident_manager.create_spill_event_manager(
    seed=SEED, report=incident_manager.get_incident_report()
)
spill_event_manager.generate_spill_event(
    name="spill event",
    selected_spillable_item=IncidentSettings.RANDOM_LEAKABLE_ITEM,
    target_size=1.0,
    leak_duration=1.0,
    trigger=time_trigger,
)
```

You can now press the play button to observe the simulated incidents in a windowed mode or
use Isaacâs `SimulationApp` API to step through the scene frames if running the scene using
Python in a headless mode.

On this page

* [Overview](#overview)
* [IRI Standalone UI Example](#iri-standalone-ui-example)
* [Scene Tagging](#scene-tagging)
  + [Loose Items](#loose-items)
    - [Random Direction](#random-direction)
    - [NavMesh Direction](#navmesh-direction)
    - [Closest Waypoint Direction](#closest-waypoint-direction)
    - [Create Waypoint Prim](#create-waypoint-prim)
  + [Flammable Items](#flammable-items)
  + [Spillable Items](#spillable-items)
    - [Spillable Area Floor](#spillable-area-floor)
* [Event Configuration in IRI UI](#event-configuration-in-iri-ui)
* [Event Configuration in IRI Script](#event-configuration-in-iri-script)
  + [Topple Event](#topple-event)
  + [Fire Event](#fire-event)
  + [Spill Event](#spill-event)
* [Triggers](#triggers)
* [SDG Collection](#sdg-collection)
  + [Incident Report JSON](#incident-report-json)
* [API usage](#api-usage)

---


## Agent配置

### Agent Configuration

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/action_and_event_data_generation/ext_replicator-agent/ext_isaacsim_replicator_agent_configuration.html

* [Synthetic Data Generation](../../synthetic_data_generation/index.html)
* [Action and Event Data Generation](../index.html)
* [Actor Simulation and Synthetic Data Generation](../tutorial_replicator_agent.html)
* Configuration File Guide

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Configuration File Guide

This guide describes how to configure the Isaac Sim Replicator Agent (IRA) for simulation and synthetic data generation. The configuration controls the environment, sensor generation and placement, character/robot agents, behaviors, and data generation.

## Concepts and Workflow

Before diving into detailed configuration, review the general workflow and key concepts of an IRA simulation.

### Workflow Overview

1. **Environment Setup**: Define the static 3D environment where the simulation takes place.
2. **Agent & Sensor Definition**: Configure characters, robots, and cameras (sensors) to populate the environment.
3. **Behavior Configuration**: Assign routines (weighted random actions like walking, idling) and triggers (reactive behaviors like when a collision occurs) to actors. Alternatively, drive a group with a **behavior tree** instead of routines and triggers (experimental; available for both character and robot groups).
4. **Data Generation**: Configure the Replicator writers to generate ground-truth data (RGB, segmentation).

#### Key Concepts

* **Environment**: The static 3D world (USD stage) loaded for the simulation. It also defines the NavMesh for navigation.
* **Agents (Actors)**: Dynamic entities in the scene, which can be **Characters** (humans) or **Robots**.
* **Behaviors**: Atomic actions an actor can perform, such as `wander`, `patrol`, or `idle`.
* **Routines**: A collection of behaviors assigned to an actor group. Actors randomly select behaviors from this pool based on assigned weights.
* **Triggers**: Conditional logic that interrupts normal routines. When a condition is met (for example, a specific time or event), the trigger executes its defined list of behaviors in sequence. Once the trigger sequence is complete, the agent resumes its standard routine until another trigger activates.
* **Behavior Tree (experimental)**: An alternative to the routine-trigger system. A character or robot group may specify a `behavior_tree` JSON asset instead of `routines` / `triggers`; all of the groupâs logic is then authored inside the tree. See [Behavior Tree Character Group (Experimental)](#ira-bt-character-group) and [Behavior Tree Robot Group (Experimental)](#ira-bt-robot-group).
* **Sensors**: Cameras placed in the scene to observe the simulation.
* **Replicator**: The system responsible for rendering frames and writing annotated data (ground truth) to disk or cloud storage.

## Top-level Structure

Configs are YAML files with a single root key `isaacsim.replicator.agent`:

```python
isaacsim.replicator.agent:
  version: 1.6.0
  environment: { ... }            # required
  seed: 123456789                 # optional; 32-bit (0..4294967295); autogenerated if omitted
  simulation_duration: 60.0       # optional; defaults to 60.0
  character: { ... }              # optional
  robot: { ... }                  # optional
  sensor: { ... }                 # optional
  replicator: { ... }             # optional
```

### Root Parameters

* **version** (required): Semantic version of the configuration schema (for example, â1.0.0â).
* **environment** (required): Defines the simulation world.
* **seed** (optional): A 32-bit unsigned integer (0..4,294,967,295).
  - Used to initialize random number generators for deterministic simulations (for example, character spawn locations, routine variations).
  - If omitted, a seed is generated based on the current system time.
* **simulation\_duration** (optional): The total run time of the simulation in seconds (must be >= 0).
  - The simulation runs with the timelineâs per-tick `dt` set to `1/30 s` and the applicationâs loop rate-limited to 30 Hz, giving an effective 30 FPS playback rate.
  - Defaults to `60.0` seconds.
* **character** (optional): Configures human agents (appearance, behaviors like wander/patrol, and triggers).
* **robot** (optional): Configures robot agents (config path, behaviors/commands, data collection).
* **sensor** (optional): Configures static cameras using placement strategies (for example, aim at targets, coverage).
* **replicator** (optional): Configures data writers (for example, output directory, annotators like RGB/segmentation).

### Quick Start (Minimal)

```python
isaacsim.replicator.agent:
  version: 1.6.0
  environment:
    base_stage_asset_path: "Isaac/Environments/Simple_Warehouse/full_warehouse.usd"
```

## Sections

### Environment

Defines the static 3D environment and additional assets to load.

* `base_stage_asset_path` (required): Path or URL to the main USD stage.
  - Supports `http(s)://` (including S3 presigned URLs), Windows/UNC paths, and local filesystem paths.
  - Also supports paths relative to the [Isaac Sim Assets](../../assets/usd_assets_overview.html#isaac-assets-overview) root.
* `prop_asset_paths` (optional): A list of additional USD assets to load as **sublayers** into the stage. This is useful for adding props or lighting to a base environment without modifying it. Supports paths relative to the [Isaac Sim Assets](../../assets/usd_assets_overview.html#isaac-assets-overview) root.

**Example:**

```python
environment:
  base_stage_asset_path: "Isaac/Environments/Simple_Warehouse/full_warehouse.usd"
  prop_asset_paths:
    - "Isaac/Props/Conveyors/ConveyorBelt_A08.usd"
```

### Character

Defines groups of human characters, their appearance, and their behavior.

* `root_prim_path` (optional): Root path for spawning characters (default: `/World/Characters`).
* `motion_library_path` (optional): Path to a custom motion library file. Supports paths relative to the [Isaac Sim Assets](../../assets/usd_assets_overview.html#isaac-assets-overview) root. Default: `Isaac/People/MotionLibrary/HumanMotionLibrary.usd`.
* `groups`: Dictionary of character groups.

There are two types of Character Groups:

* BaseCharacterGroup that define Behaviors on Routine-Trigger manners.
* BehaviorTreeGroup (experimental) that receives a behavior tree json file.

### Base Character Group

#### Group Parameters

* `num` (required): Number of characters to spawn (>= 0).
* `asset_path` (optional): USD path to character assets. Supports paths relative to the [Isaac Sim Assets](../../assets/usd_assets_overview.html#isaac-assets-overview) root. Default: `Isaac/People/Characters/`.
* `spawn_areas` (optional): List of **NavMesh area names** where characters can spawn. If empty, spawns anywhere on the NavMesh.
* `semantic_labels` (optional): List of `[type, data]` pairs for semantic segmentation. Default: `[["class", "character"]]`.
* `routines` (optional): List of behaviors the characters will execute. Default: `[{ wander: {} }]`.
* `triggers` (optional): List of event-based triggers that interrupt routines.
* `colliders` (optional): List of colliders to be spawned under the characters.

#### Behaviors

Behaviors are defined in the `routines` list. Common fields:

* `weight` (default 1): Probability weight for selecting this behavior.
* `repeat` (default 1): How many times to repeat this behavior before choosing a new one.

**Supported Behaviors:**

1. **wander**: Randomly walk and idle.

   * `walk`:
     - `speed_range`: [min, max] m/s (default [1.0, 1.0]).
     - `distance_range`: [min, max] distance to travel per walk leg (default [5.0, 15.0]).
     - `navigation_areas`: List of allowed NavMesh area tags. Each entry must be a unique, non-empty string.
   * `idle`: Array of idle options.
     - `animation`: Name of the animation (must exist in motion lib).
     - `time_range`: [min, max] duration in seconds (default [2.0, 5.0]).
     - `weight`: Selection probability.
2. **patrol**: Follow a specific path.

   * `speed_range`: [min, max] m/s (default [1.0, 1.0]).
   * Exactly one of (required):
     - `path_points`: List of 3D points `[[x,y,z], [x,y,z], ...]`.
     - `target_prims`: List of prim paths to visit.

     Note

     Both `path_points` and `target_prims` must be on the [NavMesh](https://docs.omniverse.nvidia.com/extensions/latest/ext_navigation-mesh.html "(in Omniverse Extensions)") and reachable by the actors.
3. **stop**: Stop and idle in place for a random duration.

   * `time_range`: [min, max] duration in seconds (default [5.0, 5.0]).

#### Colliders

Characters can define a list of [colliders](https://docs.omniverse.nvidia.com/kit/docs/omni_physics/latest/dev_guide/rigid_bodies_articulations/collision.html#colliders) to spawn and attach under their root. These colliders are to be used together with collision\_trigger (details in Trigger section below) to create scenarios where characters perform behaviors when they are entering or exiting other colliders.

When the following two types of colliders supported are spawned, the collider prim will be applied with PhysicsRigidBodyAPI, PhysicsCollisionAPI and PhysxTriggerAPI:

* **box**: The collider from UsdGeom.Cube.

  + `dimension`: The dimension of the cube in x, y, z order (for example, [1.0, 1.0, 1.0]). Value type is Array.
* **cylinder**: The collider from UsdGeom.Cylinder.

  > + `radius`: The cylinder radius. Value type is Float.

|  |  |
| --- | --- |
| Box collider with size 2x2x2 | Cylinder collider with radius 1.5 |

Each colldier also defines a name. This name will be translated into a custom USD String attribute `metro:collider:name` on the collider, to be used in `self_collider` or `other_colliders` from `collision_trigger` for collision filtering.

The spawned colliders will generate overlap events with other colliders that have `PhysicsCollisionAPI`. `collision_trigger` will further filter them by checking if they have the custom USD String attribute `metro:collider:name`.

However, Collision triggering between two characters will not be detected because Physx does not support triggering between two `PhysxTriggerAPI`.

The recommended workflow is to pre-define colliders in stage, adding `metro:collider:name` to them, then set up `colliders` and `collision_trigger` in the config file.

```python
character:
  groups:
    Worker:
      asset_path: "Isaac/People/Characters/"
      num: 10
      colliders:
       # Spawn a cylinder collider for each worker
        - cylinder:
            name: worker_collider_0
            radius: 1.2
      triggers:
        # Worker will pause a few sceonds when it walks into colldiers with name "loading_zone" or "unloading_zone" in stage
        - collision_trigger:
            self_collider: worker_collider_0
            other_colliders: loading_zone;unloading_zone
            behavior:
              - stop:
                  time_range: [2.0, 4.0]
```

#### Triggers

Triggers define events that interrupt normal routines to execute a list of reaction behavior.

Each actor can specify a list of triggers to listen to.

* `priority` (default 1): Higher priority triggers override lower ones. Must be >= 1.
* `behavior`: List of behaviors to execute **in sequence** when triggered.

Note

Every trigger variant is strict: unknown keys inside a trigger block fail validation.

Tip

**Authoring a specific sequence of actions**

Routines select behaviors randomly based on weights, so they are not suited for deterministic sequences. If you need actors to perform actions in a specific order (for example, walk to point A, idle for five seconds, then walk to point B), use a **trigger** instead. A triggerâs `behavior` list is always executed in order, making it the right tool for scripted sequences. Use a `time_trigger` with `time: 0` to start the sequence immediately when the simulation begins.

**Trigger Types:**

* `event_trigger`: Fires on a named carb event.

  + `event`: The carb event name. Value type is String; must be non-empty.
* `time_trigger`: Fires after a specific time after play.

  + `time`: The time in seconds. Value type is Float; must be >= 0.
* `collision_trigger`: Fires after a specific collider under this actor begins or ends overlapping with other colliders.

  + `self_collider`: The name of the collider on this actor to use (spawned by the `colliders` field in the group setting). Value type is String; must be non-empty.
  + `other_colliders`: (Optional) Semicolon-separated name list of other colliders to react to. Value type is String; defaults to `""` (react to any collider on the overlap partner).
  + `trigger_enter`: (Optional) Trigger when entering the overlap. Value type is Boolean. Default is True.
  + `trigger_exit`: (Optional) Trigger when exiting the overlap. Value type is Boolean. Default is False.

  Tip

  **Dispatching Events from Python**

  ```python
  # Send out a custom event named 'my_test_event'
  import carb
  carb.eventdispatcher.get_eventdispatcher().dispatch_event(event_name="my_test_event")

  # Actors spawned by trigger setting will react to `my_test_event`.
  # triggers:
  #   - event_trigger:
  #     event: my_test_event
  #     priority: 10
  #     behavior: [...]
  ```

**Example:**

```python
character:
  root_prim_path: "/World/Characters"
  groups:
    warehouse_workers:
      asset_path: "Isaac/People/Characters/"
      num: 10
      spawn_areas: ["warehouse_floor"]
      routines:
        - wander:
            walk:
              speed_range: [0.8, 1.5]
              distance_range: [5.0, 10.0]
            idle:
              - animation: look_around
                time_range: [2.0, 5.0]
      triggers:
        - time_trigger:
            time: 30.0
            priority: 10
            behavior:
              - patrol: # Move to break room
                  speed_range: [1.0, 1.2]
                  target_prims: ["/World/BreakRoom"]
        - event_trigger:
            event: test_event
            priority: 10
            behavior:
              - patrol:
                  speed_range: [5.0, 5.5]
                  path_points:
                    - [0, 0, 0]
                    - [0, -5, 0]
        # Pause a few sceonds when it walks into colldiers with name "loading_zone" or "unloading_zone"
        - collision_trigger:
            self_collider: worker_sensing_collider
            other_colliders: loading_zone;unloading_zone
            behavior:
              - stop:
                  time_range: [2.0, 4.0]
      colliders:
        - cylinder:
            name: worker_sensing_collider  # A collider to represent the sensing range of the worker
            radius: 10.0
```

#### Behavior Tree Character Group (Experimental)

Warning

Behavior tree character support is **experimental** and may change in future releases.

When a character group contains a `behavior_tree` key instead of `routines` and `triggers`, IRA treats it as a **behavior-tree character group**. In this mode, all behavior logic is defined inside the referenced behavior tree rather than through the IRA routine-trigger system.

A single configuration can mix both group types. For example, one group using IRA routines and another using a behavior tree.

Note

`routines` and `triggers` fields are **not available** for behavior-tree groups. Any reactive or conditional logic must be authored as nodes inside the behavior tree itself.

**Behavior-Tree-Specific Parameters:**

* `behavior_tree` (required): Path or URL to a JSON behavior tree asset. Supports Isaac asset-root-relative paths (for example, `Isaac/...`), absolute filesystem paths, and paths relative to the config file directory. The tree must reference node libraries such as `omni.behavior.tree.core` and `omni.anim.behavior.tree`.
* `overrides` (optional): A YAML multi-line string containing JSON that overrides node port values at runtime without modifying the original tree file. The JSON follows the `omni.behavior.tree` override schema with `schemaVersion` and `instanceOverrides` keys. Refer to the [Behavior Treeâs User Guide](https://docs.omniverse.nvidia.com/kit/docs/behavior-tree/latest/user-guide.html#instance-overrides) for more details on instance overrides.

**Shared Parameters (same as IRA character groups):**

* `num` (required): Number of characters to spawn (>= 0).
* `asset_path` (optional): USD path to character assets. Default: `Isaac/People/Characters/`.
* `spawn_areas` (optional): List of NavMesh area names where characters can spawn.
* `semantic_labels` (optional): List of `[type, data]` pairs. Default: `[["class", "character"]]`.
* `motion_library_path` (optional): Path to a custom motion library file.
* `colliders` (optional): List of collider objects for the character group.

**Minimal Example:**

```python
character:
  groups:
    bt_workers:
      num: 3
      asset_path: "Isaac/People/Characters/"
      behavior_tree: ../sample_behavior_tree/character_wander.json
```

**Example with Overrides:**

The `overrides` field is a JSON string (written as a YAML multi-line block scalar with `|`) that lets you adjust node parameters per-group without editing the tree file. The JSON structure has two keys:

* `schemaVersion` (required): Must be `"2.0.0"`.
* `instanceOverrides` (required): A dictionary mapping **node paths** (for example, `/Root/MoveTo:RandomNavMeshPoint`) to **port overrides**, which is a dictionary of port name to its type and overriden value.

For example, to change the wander radius of a `RandomNavMeshPoint` modifier node:

```python
character:
  groups:
    bt_workers:
      num: 3
      asset_path: "Isaac/People/Characters/"
      behavior_tree: ../sample_behavior_tree/character_wander.json
      overrides: |
        {
          "schemaVersion": "2.0.0",
          "instanceOverrides": {
            "/Root/MoveTo:RandomNavMeshPoint": {
              "radius": {
                "type": "carb::Float2",
                "value": [2.0, 10.0]
              }
            }
          }
        }
```

**Mixed Configuration Example (IRA + Behavior Tree):**

```python
character:
  root_prim_path: "/World/Characters"
  groups:
    ira_wanderers:
      num: 5
      routines:
        - wander:
            walk:
              speed_range: [0.8, 1.5]
    bt_patrol_group:
      num: 3
      behavior_tree: ../sample_behavior_tree/character_wander.json
```

### Robot

Defines robot agents.

* `root_prim_path` (optional): Root path for robots (default: `/World/Robots`).
* `groups`: Dictionary of robot groups.

#### Robot Group Parameters

* `num` (required): Number of robots (>= 1).
* `config_file_path` (required): Path to the robot agent YAML configuration file for this robot type. Supports absolute paths or paths relative to the built-in sample config folder (`data/sample_configs/` within the `isaacsim.anim.robot.core` extension).
* `spawn_areas` (optional): NavMesh areas for spawning.
* `agent_radius` (optional): Radius in meters used for NavMesh queries. Must be > 0 when set. If omitted, defaults to `0.5` at runtime.
* `write_data` (optional): If `true`, enables data collection from the robotâs onboard cameras.
* `camera_prim_paths` (optional): List of specific camera prims on the robot to use. If empty and `write_data` is true, *all* cameras on the robot are used. Requires `write_data` to be `true`.
* `semantic_labels` (optional): Default `[["class", "robot"]]`.
* `semantic_label_path` (optional): Relative path under the robot prim to apply semantics.
* `routines` (optional): List of robot behaviors. Default: `[{ wander: {} }]`.
* `triggers` (optional): List of triggers that interrupt routines. Robots support `event_trigger`, `time_trigger`, and `collision_trigger`.
* `colliders` (optional): List of colliders to spawn and attach under each robot (same schema as character `colliders`; refer to the [Colliders](#ira-colliders) section). Used together with `collision_trigger` to drive behaviors when the robot enters or exits other colliders.

#### Robot Behaviors

* **wander**:
  - `move`: { `distance_range`: [min, max] (default [10.0, 15.0]), `navigation_areas`: list of allowed NavMesh area tags, each entry must be a unique, non-empty string (default []) }
  - `idle`: { `time_range`: [min, max] (default [2.0, 5.0]) }
* **patrol** (exactly one of `path_points` or `target_prims` is required):
  - `path_points`: List of 3D points `[[x,y,z], [x,y,z], ...]`.
  - `target_prims`: List of prim paths to visit.

  Note

  Both `path_points` and `target_prims` must be on the [NavMesh](https://docs.omniverse.nvidia.com/extensions/latest/ext_navigation-mesh.html "(in Omniverse Extensions)") and reachable by the robots.
* **halt**:
  - `time_range`: [min, max] seconds to remain halted (default [5.0, 5.0]).

#### Behavior Tree Robot Group (Experimental)

Warning

Behavior tree robot support is **experimental** and may change in future releases.

When a robot group contains a `behavior_tree` key instead of `routines` and `triggers`, IRA treats it as a **behavior-tree robot group**. In this mode, all behavior logic is defined inside the referenced behavior tree rather than through the IRA routine-trigger system, and the robot is driven by [Animated Robot Behavior Tree Nodes](ext_isaacsim_anim_robot_bt_nodes.html) (`RobotMoveTo`, `RobotTurn`, `RobotIdle`, `RobotPlayAnimation`, and the `RobotIsInState` modifier).

A single configuration can mix both group types. For example, one routine-driven group and another behavior-tree-driven group.

Note

`routines`, `triggers`, and `colliders` are **not available** for behavior-tree robot groups. Any reactive or conditional logic must be authored as nodes inside the behavior tree itself.

**Behavior-Tree-Specific Parameters:**

* `behavior_tree` (required): Path or URL to a JSON behavior tree asset. Supports Isaac asset-root-relative paths (for example, `Isaac/...`), absolute filesystem paths, and paths relative to the config file directory.
* `overrides` (optional): A YAML multi-line string containing JSON that overrides node port values at runtime without modifying the original tree file. Follows the `omni.behavior.tree` override schema (`schemaVersion` + `instanceOverrides`); see [Behavior Tree Character Group (Experimental)](#ira-bt-character-group) for an example.

**Shared Parameters (same as IRA robot groups):**

* `num` (required): Number of robots to spawn (>= 1).
* `config_file_path` (optional): Path to the per-robot agent YAML (default: `nova_carter.yaml`).
* `spawn_areas` (optional): List of NavMesh area names where robots can spawn.
* `agent_radius` (optional): NavMesh query radius in meters (must be > 0 when set).
* `semantic_labels` (optional): Default `[["class", "robot"]]`.
* `semantic_label_path` (optional): Relative path under the robot prim to apply semantics.

**Minimal Example:**

```python
robot:
  groups:
    bt_carters:
      num: 2
      config_file_path: nova_carter.yaml
      behavior_tree: ../sample_behavior_tree/robot_wander.json
```

### Sensor

Defines static cameras in the scene. Cameras are organized into named **groups**.

* `root_prim_path` (optional): Absolute prim path where all camera groups will be created (default: `/World/Cameras`).
* `groups`: A dictionary where keys are group names and values define the camera configuration.

#### Group Configuration

Each group must specify `num` (number of cameras) and **one** placement strategy (`aim_at_targets` OR `maximum_coverage`).
- For `aim_at_targets`, `num` must be >= 0.
- For `maximum_coverage`, `num` can be >= -1. If `-1`, the number of cameras is automatically calculated based on the grid resolution and coverage ratio.

**1. Placement Strategy: aim\_at\_targets**

Places cameras to look at specific targets.

* `targets` (optional): List of target prim paths (for example, `/World/Characters`) or identifiers.
* `raycast_density` (optional): Density of rays used to find valid camera positions. Higher values are more precise but slower.
* `yaw_range` (optional): [min, max] degrees (0..360) for the cameraâs rotation around the target.
* `occlusion_threshold` (optional): Threshold for filtering occluded views (-1 to disable).

**2. Placement Strategy: maximum\_coverage**

Places cameras to maximize visual coverage of the environment.

* `target_coverage_ratio` (optional): Desired coverage ratio (0.0 to 1.0). Default `0.9`.
* `grid_resolution` (optional): Size of the grid cells (in meters) used for coverage calculation. Default `1.0`.

**Shared Parameters**

These apply to all placement strategies:

* `height_range`: [min, max] height in meters (Z-axis).
* `look_down_angle_range`: [min, max] pitch angle in degrees (0 = horizontal, 90 = straight down).
* `focal_length_range`: [min, max] focal length in millimeters.
* `distance_range`: [min, max] distance from the camera to its target or interest point in meters.

**Example:**

```python
sensor:
  root_prim_path: "/World/Cameras"
  groups:
    ceiling_cameras:
      num: 20
      aim_at_targets:
        targets: ["/World/Characters"]
        distance_range: [5, 10]
        height_range: [7, 10]
        focal_length_range: [10, 15]
        look_down_angle_range: [30, 45]
    coverage_cameras:
      num: 5
      maximum_coverage:
        target_coverage_ratio: 0.8
        height_range: [2, 5]
```

### Replicator

Controls the generation of synthetic data (images, annotations) using Omniverse Replicator.

* `writers` (required): Dictionary of writer configurations.
* `hide_debug_visualization` (optional, default `true`): Hides debug visualizations (NavMesh, skeletons, lights) during data capture.

#### Writer Configuration

Supported writers: `IRABasicWriter`, `CosmosIRAWriter`, `SceneGraphWriter`, `CustomWriter`.

Note

In previous releases, the stock Replicator `BasicWriter` appeared as its own entry in the **Add Writer** dropdown and could be used directly as a writer key (for example, `BasicWriter:`). Starting with version 1.6.1 of `isaacsim.replicator.agent.core`, `BasicWriter` has been removed from the UI dropdown and is no longer accepted as a top-level writer key in the configuration. If you need the stock `BasicWriter`, use a `CustomWriter` entry with `writer_name: "BasicWriter"` instead. Refer to the [CustomWriter](#ira-configuration-file) section below for details.

**Common Settings per Writer:**

* **Timing**:
  - `start_frame` / `end_frame`: Frame-based control (inclusive/exclusive). Defaults to `start_frame: 30` if not specified.
  - `start_time` / `end_time`: Time-based control (seconds).
* **Sensors**:
  - `sensor_prim_list`: Optional list of cameras to use. If omitted, uses all cameras defined in `sensor.root_prim_path`.

**Output Settings:**

* `output_dir`: Local directory for output. Defaults to `~/IRA_output` if not set.
* `s3_bucket`, `s3_region`, `s3_endpoint`: For direct S3 upload.

**Common Annotators (Parameters):**

* `rgb`: RGB Image.
* `bounding_box_2d_tight` / `loose`: 2D Bounding boxes.
* `bounding_box_3d`: 3D Bounding boxes.
* `semantic_segmentation`: Pixel-wise semantic class IDs.
* `instance_segmentation`: Pixel-wise instance IDs.
* `distance_to_camera`: Depth map.
* `normals`: Surface normals.
* `motion_vectors`: Pixel motion.
* `colorize_*`: For example, `colorize_semantic_segmentation` (save as visible color map compaired to raw ID).

#### Specialized Writers

1. **IRABasicWriter**:

   The foundational writer for Agent simulations, derived from Replicatorâs `BasicWriter`. It organizes output into separate folders per annotator and consolidates object and agent metadata into `object_detection.json`.

   * **Key Features**:

     + **Folder Structure**: Outputs each annotatorâs data into separate folders for better readability.
     + **Object Detection**: Consolidates bounding box and skeleton data into a single file named `object_detection.json`.
     + **Default Semantic Filter**: `class:character|robot;id:*` (captures characters and robots).
     + **Action data output**: When object detection is enabled (object\_info or agent\_info annotators are on), the action data for each IRA actor will be included as well.
   * **Overwritten Annotators**:
     The following standard annotators are replaced by specialized `object_info_*` versions and written to `object_detection.json`:

     + `bounding_box_2d_tight`
     + `bounding_box_2d_loose`
     + `bounding_box_3d`
     + `skeleton_data` (replaced by `agent_info_skeleton_data`)
   * **Defaults**:

     + `rgb`: Enabled.
     + `camera_params`: Enabled.
     + S3-related parameters: Disabled.
   * **Special Parameters**:

     + `video_rendering_annotator_list`: Generates `.mp4` videos for specified annotators (for example, `["rgb", "semantic_segmentation"]`).
     + `agent_info_skeleton_data`: Exports 2D/3D skeleton joints for characters.
   * **Action data**:

     Action data is for describing the current behavior of each actor. It is in `object_detection.json` under the `metro_agent_data` section. Data includes:

     + `prim path`: The prim path of the actor schema is applied.
     + `agent_type`: The actor schema type.
     + `agent_name`: The name of the actor.
     + `agent_group`: The group name of the actor.
     + `world_position`: Actor position (vec3) in world space.
     + `world_rotation`: Actor rotation (quaternion) in world space.
     + `world_moving_direction`: Actor moving direction (vec3) in world space. `null` means actor is not moving.
     + `world_facing_direction`: Actor facing direction (vec3) in world space.
     + `speed`: The actor moving speed.
     + `current_task_name`: Actorâs current action name (not behavior name).
     + `asset_url`: The asset URL of the actor.

   **IRABasicWriter example:**

   ```python
   replicator:
     writers:
       IRABasicWriter:
         output_dir: "<your_output_directory>"
         start_frame: 0
         end_frame: 300
         rgb: true
         camera_params: true
         bounding_box_2d_tight: true
         semantic_segmentation: true
         agent_info_skeleton_data: true
         video_rendering_annotator_list: ["rgb", "semantic_segmentation"]
   ```
2. **CosmosIRAWriter**:

   * Adds âCosmosâ Specific post-processing.
   * `shaded_seg`: Shaded segmentation visualization.
   * `canny_edge`: Canny edge detection filter (with `canny_threshold_low/high`).
3. **SceneGraphWriter**:

   Writes per-frame scene captions alongside the standard output. This writer is provided by the `Isaacsim.Replicator.Caption` extension; for configuration and a complete example, refer to [Use Isaacsim.Replicator.Caption in Isaacsim.Replicator.Agent](../tutorial_replicator_caption.html#using-ira-extension).
4. **CustomWriter**:

   A flexible wrapper that delegates to **any** writer registered in `omni.replicator.core.WriterRegistry`. Use `CustomWriter` when you want to use a third-party writer, a writer from another extension, or your own `omni.replicator.core.Writer` subclass without modifying the IRA codebase.

   * **Required parameters**:

     + `writer_name` (string, required): The registry name of the target writer (for example, `"BasicWriter"`, `"KittiWriter"`, or a user-defined name). Any writer registered in `WriterRegistry` can be referenced here, including the stock Replicator `BasicWriter`.
   * **Optional parameters**:

     + `writer_scope` (string, optional): A flexible field for discovering and registering writers that are not yet in the `WriterRegistry`. It accepts three input modes, auto-detected by the system:

       - **Package or module path** (for example, `"omni.replicator.core"`): scans all submodules for concrete `Writer` subclasses and batch-registers them.
       - **Full class path** (for example, `"my_extension.writers.MyWriter"`): imports and registers a single specific writer class.
       - **Filesystem path** to a `.py` file (for example, `"<path/to/your_writers.py>"`): loads the file and registers all `Writer` subclasses defined in it.

       Use `writer_name` to select the specific writer from the discovered set.
   * **Additional parameters**: All other key-value pairs in the YAML block are passed directly to the target writerâs `initialize(**kwargs)` call. Only parameters you explicitly list override the writerâs built-in defaults; unlisted parameters keep the writerâs own default values.

   How parameter discovery works

   When a `CustomWriter` entry is loaded, the system introspects the target writerâs `__init__` signature to discover all accepted parameters along with their types and default values. A typed Pydantic model is dynamically generated from this signature, which enables:

   * **Type validation**: Supplied parameter values are checked against the writerâs expected types before the simulation starts.
   * **UI integration**: In the Configuration Editor UI, each discoverable parameter appears as an addable field with the correct widget type. Click **Add Parameter** to override a default, or remove a parameter to revert to the writerâs own default.

   Parameters whose types cannot be represented in JSON (for example, custom backend objects) are excluded from the dynamic model and the UI but can still be passed in YAML.

   Note

   Some writers accept `width` and `height` parameters that configure the writerâs output dimensions but do **not** modify the underlying RenderProduct resolution. To change the actual rendered resolution, first adjust the **RenderProduct Resolution** in the CustomWriter UI panel, then set the writerâs `width` and `height` parameters to match.

   Auto-registration using writer scope

   If the writer class is not yet in the `WriterRegistry` when the config is loaded, provide `writer_scope` to have IRA discover and register it automatically. The system auto-detects which mode to use based on the value:

   * **File path** (contains `/`, `\`, or ends with `.py`): loads the `.py` file from disk and registers all `Writer` subclasses found in it.
   * **Single class path** (last segment starts with an uppercase letter, for example `"my_extension.writers.MyWriter"`): imports and registers that one class.
   * **Package scan** (for example `"omni.replicator.core"`): recursively walks the package and registers all concrete `Writer` subclasses.

   Already-registered writers are skipped silently. After resolution, select the target writer using the `writer_name` field.

   If `writer_scope` is omitted, the writer must already be registered (for example, by enabling the extension that provides it).

   Using CustomWriter in the UI

   When adding a `CustomWriter` through the Configuration Editor:

   1. Click **Add Writer** and select **CustomWriter** from the type list.
   2. A dedicated dialog appears with two fields:

      * **Writer Name**: A dropdown listing all writers currently in the `WriterRegistry`. Select the target writer.
      * **Writer Scope**: An optional text field that accepts a package path, a dotted class path, or a filesystem path to a `.py` file. Click **Register** to discover, validate, and register writers from the scope, which also refreshes the **Writer Name** dropdown.
   3. Click **OK** to confirm. The editor displays the writerâs name as a read-only label and lists all currently set parameters with their values.
   4. Use the **Add Parameter** dropdown at the bottom to override additional defaults from the writerâs `__init__` signature.

   Important

   Always click **OK** to confirm after selecting or registering a writer. The CustomWriter is not added until you confirm the dialog.

   Note

   The **Writer Scope** field in the UI replaces the former **Class Path** field. It accepts all three input modes (package path, class path, and file path) and the system auto-detects which mode to use.

   Note

   Parameter names displayed in the UI are derived automatically from the writerâs `__init__` signature (for example, `sensorSetName` in `RTSPStreamWriter`). Because users can import custom or third-party writers, no specific naming format is enforced. The UI capitalizes the first letter of each name for readability (for example, `sensorSetName` appears as **SensorSetName**), but the original name is used when passing values to the writer.

   Multiple CustomWriter instances

   You can configure multiple `CustomWriter` entries in the same config. Append a numeric suffix to create unique keys:

   ```python
   replicator:
     writers:
       CustomWriter:
         writer_name: "<your_writer_name>"
         <writer_param>: <your_value>
       CustomWriter_1:
         writer_name: "<your_other_writer_name>"
         <writer_param>: <your_value>
   ```

   The suffix (`_1`, `_2`, and so on) is stripped when resolving the writer type; the `writer_name` field determines which registry writer is used.

   For a step-by-step walkthrough that uses `CustomWriter` to set up live RTSP streaming, refer to [Example: RTSP streaming with CustomWriter](ext_isaacsim_replicator_agent_custom_writer_example.html#ira-custom-writer-example).

   **CustomWriter examples:**

   ```python
   # Use a registered writer, overriding only specific defaults
   replicator:
     writers:
       CustomWriter:
         writer_name: "<your_writer_name>"
         <writer_param>: <your_value>
   ```

   ```python
   # Auto-register a writer class by its dotted import path
   replicator:
     writers:
       CustomWriter:
         writer_name: "<your_writer_name>"
         writer_scope: "<your_package.module.ClassName>"
         <writer_param>: <your_value>
   ```

   ```python
   # Discover all writers from a package
   replicator:
     writers:
       CustomWriter:
         writer_name: "<your_writer_name>"
         writer_scope: "<your_package>"
         <writer_param>: <your_value>
   ```

   ```python
   # Load writers from a standalone .py file
   replicator:
     writers:
       CustomWriter:
         writer_name: "<your_writer_name>"
         writer_scope: "<path/to/your_writers.py>"
         <writer_param>: <your_value>
   ```

On this page

* [Concepts and Workflow](#concepts-and-workflow)
  + [Workflow Overview](#workflow-overview)
    - [Key Concepts](#key-concepts)
* [Top-level Structure](#top-level-structure)
  + [Root Parameters](#root-parameters)
  + [Quick Start (Minimal)](#quick-start-minimal)
* [Sections](#sections)
  + [Environment](#environment)
  + [Character](#character)
  + [Base Character Group](#base-character-group)
    - [Group Parameters](#group-parameters)
    - [Behaviors](#behaviors)
    - [Colliders](#colliders)
    - [Triggers](#triggers)
    - [Behavior Tree Character Group (Experimental)](#behavior-tree-character-group-experimental)
  + [Robot](#robot)
    - [Robot Group Parameters](#robot-group-parameters)
    - [Robot Behaviors](#robot-behaviors)
    - [Behavior Tree Robot Group (Experimental)](#behavior-tree-robot-group-experimental)
  + [Sensor](#sensor)
    - [Group Configuration](#group-configuration)
  + [Replicator](#replicator)
    - [Writer Configuration](#writer-configuration)
    - [Specialized Writers](#specialized-writers)

---

### Configuration Editor

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/action_and_event_data_generation/ext_replicator-agent/ext_isaacsim_replicator_agent_configuration_editor.html

* [Synthetic Data Generation](../../synthetic_data_generation/index.html)
* [Action and Event Data Generation](../index.html)
* [Actor Simulation and Synthetic Data Generation](../tutorial_replicator_agent.html)
* Configuration Editor API

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Configuration Editor API

The **Configuration Editor API** is provided by the `isaacsim.replicator.agent.ui` extension. It lets you load, modify, and save IRA (Isaac Sim Replicator Agent) configurations, as well as set up simulations and start data generation from the UI or Python scripts. The in-memory config uses the same schema as the YAML configuration described in the [Configuration File Guide](ext_isaacsim_replicator_agent_configuration.html#ira-configuration-file).

Use this API when you want to:

* Load or switch configuration files at runtime.
* Update specific fields (such as environment path, character counts, or writer settings) without editing YAML by hand.
* Add or remove items in lists (such as `prop_asset_paths`) or in dictionaries (such as character/robot groups).
* Perform simulation setup and data generation from code and react to completion using core carb events.

## Overview

The UI extension keeps an in-memory copy of the IRA config. The API operates on that copy and can optionally persist it to a file. Successful config changes and loads dispatch a UI refresh so that any open Configuration Editor panels stay in sync.

Functions are grouped as follows in `isaacsim.replicator.agent.ui`:

* **Config file and path:** `get_config_file_path`, `load_config_file`, `save_config_file`
* **Read/write config:** `get_config`, `set_config`, `update_config`, `add_config_item`, `delete_config_item`
* **Simulation:** `setup_simulation`, `start_data_generation`

For `get_config`, `update_config`, `add_config_item`, and `delete_config_item`, use dot-separated paths and numeric indices for lists (see [Path Syntax](#ira-config-path-syntax)).

## Config File and Path

* **get\_config\_file\_path()** â Returns the path of the config file currently associated with the in-memory config, or `None` if none is set.
* **load\_config\_file(file\_path, set\_config=True)** â Loads a YAML config from disk. Returns `True` on success. If `set_config` is `True`, the loaded config becomes the current in-memory config. You can subscribe to `isaacsim.replicator.agent.core.events.IRAEvents.CONFIG_FILE_LOADED_EVENT` to be notified when loading has finished.
* **save\_config\_file(file\_path, exclude\_unset=False, exclude\_defaults=False)** â Writes the current in-memory config to a YAML file. Returns `True` on success. Use `exclude_unset` or `exclude_defaults` to trim output.

**Example:**

```python
import os
import tempfile

from isaacsim.replicator.agent.ui import get_config_file_path, load_config_file, save_config_file

config_path = get_config_file_path()
if config_path:
    from pathlib import Path

    target_config_path = Path(config_path).parent / "full_pipeline.yaml"
else:
    target_config_path = None

if target_config_path and load_config_file(target_config_path, set_config=True):
    print("Config loaded; current file:", get_config_file_path())

# ... do some config modifications using update_config and add_config_item

fd, temp_save_path = tempfile.mkstemp(suffix=".yaml")
os.close(fd)
save_config_file(temp_save_path)
```

## Read and Update Config

* **get\_config(path=None)** â Returns the value at a dot-separated path, or the full config object if `path` is `None`. Returns `None` if the path is invalid or config is not loaded.
* **set\_config(config, file\_path=None)** â Replaces the in-memory config with the given object (for example, from `get_config()` or the core loader). Optionally set `file_path` as the current file for the UI.
* **update\_config(path, new\_value)** â Sets one field at the given path. Validates after the change; on failure the update is rolled back and returns `False`.
* **add\_config\_item(path, value, key=None)** â Appends to a list at `path`, or adds a key-value pair to a dict (`key` required for dicts).
* **delete\_config\_item(path, key)** â Removes a list element by index (or last item if `key` is `None`) or a dict entry by key.

**Example:**

```python
from isaacsim.replicator.agent.ui import add_config_item, delete_config_item, get_config, update_config

# Example queries
full_config = get_config()
stage_path = get_config("environment.base_stage_asset_path")

# Example updates
update_config("environment.base_stage_asset_path", "Isaac/Environments/Simple_Warehouse/full_warehouse.usd")
update_config("simulation_duration", 120.0)
add_config_item("environment.prop_asset_paths", "Isaac/Props/Conveyors/ConveyorBelt_A08.usd")
delete_config_item("environment.prop_asset_paths", key=0)
```

## Simulation Control

* **setup\_simulation()** â Validates the current config and passes it to the IRA core to set up the simulation (environment, agents, sensors). Returns `True` if setup was started. Subscribe to `isaacsim.replicator.agent.core.events.IRAEvents.SET_UP_SIMULATION_DONE_EVENT` when setup has finished.
* **start\_data\_generation()** â Starts the data generation pipeline with the current config. Returns `True` if started. Subscribe to `isaacsim.replicator.agent.core.events.IRAEvents.DATA_GENERATION_DONE_EVENT` when generation has completed.

**Example workflow:** load config, optionally update fields, run setup, then start data generation. Use the carb event dispatcher to observe `SET_UP_SIMULATION_DONE_EVENT` and call `start_data_generation()` when setup is ready.

Setup and data generation with event observers

```python
import tempfile
from pathlib import Path

import carb
from isaacsim.replicator.agent.core.events import IRAEvents
from isaacsim.replicator.agent.ui import (
    get_config_file_path,
    load_config_file,
    setup_simulation,
    start_data_generation,
    update_config,
)

# Skipping actual simulation setup and data generation by default for brevity
RUN_SETUP = False

def on_setup_done(event):
    """Callback for when simulation setup is done."""
    carb.log_info("Simulation setup done")
    start_data_generation()
    handle_setup.reset()

def on_data_done(event):
    """Callback for when data generation is done."""
    carb.log_info("Data generation done")
    handle_data.reset()

# Set up callbacks for setup simulation and data generation
dispatcher = carb.eventdispatcher.get_eventdispatcher()
handle_setup = dispatcher.observe_event(
    event_name=IRAEvents.SET_UP_SIMULATION_DONE_EVENT,
    on_event=on_setup_done,
    observer_name="setup_done_observer",
)
handle_data = dispatcher.observe_event(
    event_name=IRAEvents.DATA_GENERATION_DONE_EVENT,
    on_event=on_data_done,
    observer_name="data_done_observer",
)

config_path = get_config_file_path()
if config_path:
    target_config_path = Path(config_path).parent / "full_pipeline.yaml"
else:
    print("No config file path found")
    target_config_path = None

if target_config_path and load_config_file(target_config_path):
    temp_path = Path(tempfile.mkdtemp(prefix="IRA_Output_"))
    update_config("simulation_duration", 2.0)
    update_config("replicator.writers.IRABasicWriter.output_dir", str(temp_path))

    if RUN_SETUP:
        setup_simulation()
        print(f"Generating data to: {temp_path}")
        # When setup is done, SET_UP_SIMULATION_DONE_EVENT will fire
        # calling our local on_setup_done(), which in turn calls start_data_generation()

# If setup_simulation() was not run, the event callbacks never fire; unsubscribe here.
# When RUN_SETUP is True, on_setup_done/on_data_done reset the handles when events fire.
if not RUN_SETUP:
    handle_setup.reset()
    handle_data.reset()
```

## Path Syntax

Config paths use dot-separated segments that correspond to the YAML structure in the [Configuration File Guide](ext_isaacsim_replicator_agent_configuration.html#ira-configuration-file):

* **Top-level keys:** `version`, `environment`, `seed`, `simulation_duration`, `character`, `robot`, `sensor`, `replicator`.
* **Nested keys:** for example, `environment.base_stage_asset_path`, `environment.prop_asset_paths`, `character.groups`, `replicator.writers`.
* **List index:** Use a numeric segment for the element index (for example, `environment.prop_asset_paths.0` for the first prop).
* **Dictionary key:** Use the group or writer name as the segment (for example, `character.groups.warehouse_workers`, `replicator.writers.IRABasicWriter`).

Paths are case-sensitive and must match the schema. When a path targets a list, the last segment can be an integer index; when it targets a dict, the last segment is the key name.

On this page

* [Overview](#overview)
* [Config File and Path](#config-file-and-path)
* [Read and Update Config](#read-and-update-config)
* [Simulation Control](#simulation-control)
* [Path Syntax](#path-syntax)

---

### Custom Writer Example

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/action_and_event_data_generation/ext_replicator-agent/ext_isaacsim_replicator_agent_custom_writer_example.html

* [Synthetic Data Generation](../../synthetic_data_generation/index.html)
* [Action and Event Data Generation](../index.html)
* [Actor Simulation and Synthetic Data Generation](../tutorial_replicator_agent.html)
* Example: RTSP Streaming with CustomWriter

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Example: RTSP Streaming with CustomWriter

This walkthrough demonstrates how to use the [CustomWriter](ext_isaacsim_replicator_agent_configuration.html#ira-configuration-file) to stream live RTSP video from IRA cameras. The `RTSPStreamWriter` provided by the `isaacsim.streaming.rtsp` extension serves as the target writer. This page covers only the minimal working example; for full details on encoding modes, frame metadata, server lifecycle, and troubleshooting, refer to [Live Camera Streaming over RTSP](../../digital_twin/rtsp_camera_streaming.html#isaac-sim-rtsp-camera-streaming).

`RTSPStreamWriter` streams LdrColor frames over RTSP and supports two encoding modes:

* hardware-accelerated H.264 (default)
* raw CUDA

Because it is designed with a **one-to-one mapping** between writer instances and cameras, each camera requires its own `CustomWriter` entry with a unique port.

## Prerequisites

* Isaac Sim is installed and can launch successfully.
* The `isaacsim.replicator.agent.core` and `isaacsim.replicator.agent.ui` extensions are enabled ([Enable extensions](../tutorial_replicator_agent.html#actor-sim-enable-extensions)).
* An RTSP client is available for playback (for example, [VLC](https://www.videolan.org/), `ffplay`, or a GStreamer pipeline).

## Step 1: Enable the RTSP Streaming Extension

`RTSPStreamWriter` is provided by the `isaacsim.streaming.rtsp` extension. If the extension is not already active, enable it before proceeding:

1. Open **Window > Extensions** to launch the Extension Manager.
2. Search for `isaacsim.streaming.rtsp`.
3. If the extension is not enabled, click the toggle to enable it. Check the **autoload** checkbox if you want it to load automatically on future launches.

After enabled, `RTSPStreamWriter` registers itself in `omni.replicator.core.WriterRegistry` and becomes available to the CustomWriter selection dialog.

## Step 2: Add a CustomWriter and Select the Writer

1. Open the Actor SDG panel (**Tools > Action and Event Data Generation > Actor SDG**).
2. Scroll to the **Replicator** section and click **Add Writer**.
3. Select **CustomWriter** from the writer type list and click **Next**.
4. In the **Configure CustomWriter** dialog, open the **Writer Name** dropdown and look for `RTSPStreamWriter`.

   * If `RTSPStreamWriter` appears in the list, select it, click **OK** to confirm, and proceed to step 4.
   * If it does not appear, follow step 3 below to register it manually.

Important

Always click **OK** to confirm after selecting or registering a writer. The CustomWriter is not added until you confirm the dialog.

## Step 3: Manual Registration

If `RTSPStreamWriter` is not listed in the **Writer Name** dropdown, the extension may not have been enabled or its self-registration may not have run yet. You can register the writer class manually using the **Writer Scope** field, which accepts three input modes:

* A dotted class path to a single writer class.
* A package or module path to scan for all `Writer` subclasses.
* A filesystem path to a `.py` file containing writer classes.

The system auto-detects the mode. To register `RTSPStreamWriter`:

1. In the **Writer Scope** field, enter the class path:

   ```python
   isaacsim.streaming.rtsp.impl.rtsp_writer.RTSPStreamWriter
   ```

   Alternatively, enter the package path `isaacsim.streaming.rtsp` to discover all writers in the extension.
2. Click **Register**. The system imports the class (or scans the package), validates that each discovered class is a subclass of `omni.replicator.core.Writer`, and registers it in the `WriterRegistry`.
3. The **Writer Name** dropdown refreshes and `RTSPStreamWriter` appears. Select it.
4. Click **OK** to confirm.

## Step 4: Configure the Sensor Prim List

`RTSPStreamWriter` is designed with a **one-to-one** mapping: each writer instance streams from exactly one camera. You must specify the target camera by adding it to the **Sensor Prim List** within the CustomWriter panel:

1. In the CustomWriter parameters panel, click **Add Parameter** and select `sensor_prim_list`.
2. Add the prim path of the camera you want to stream (for example, `/World/Cameras/Camera_01`).

Note

If `sensor_prim_list` is left empty, the writer attempts to attach to all cameras under the sensor root, which is not supported by `RTSPStreamWriter`. Always specify exactly one camera per CustomWriter instance.

## Step 5: Set the Port and Mount Path

Each RTSP stream requires a unique network port. When streaming from multiple cameras, assign a different `port` value to each CustomWriter instance to avoid conflicts.

1. Click **Add Parameter** and select `port`. Set a port number (default is `8554`). Valid range is 1â65535.
2. Click **Add Parameter** and select `mountPath`. Enter a descriptive mount path that starts with `/` (for example, `/camera_01`). This makes it easier to identify each stream when monitoring.

The resulting RTSP URL for this stream is:

```python
rtsp://localhost:<port><mountPath>
```

For example, with `port: 8554` and `mountPath: /camera_01`, the stream URL is `rtsp://localhost:8554/camera_01`.

## Step 6: Optional Encoding Settings

`RTSPStreamWriter` supports two encoding modes controlled by the `encoding` parameter:

* `"h264"` (default): Pre-encoded H.264 with per-frame SEI metadata injection. This is the recommended mode for most use cases.
* `"raw"`: Uncompressed CUDA RGBA buffer path. The RTSP backend handles encoding internally.

When using `"h264"` encoding, you can also configure `width` and `height` (default 1920x1080) to set the RTSP server resolution.

Note

The `width` and `height` parameters on `RTSPStreamWriter` do **not** change the RenderProduct resolution â they only configure the RTSP stream to match the existing input dimensions. To change the actual rendered resolution, first adjust the **RenderProduct Resolution** in the CustomWriter UI panel, then set the writerâs `width` and `height` to match. Mismatched values result in stretched or cropped frames.

### Parameter Naming in the UI

The CustomWriter UI generates its parameter fields automatically from the
`__init__` signature of the selected writer class (for example,
`sensorSetName` in `RTSPStreamWriter`). Because you can import custom or
third-party writers, no specific parameter naming format is enforced. The UI
capitalizes the first letter of each parameter name purely for visual
consistency (for example, `sensorSetName` appears as **SensorSetName** in the
panel), but the underlying value is passed to the writer using its original
name.

## Multi-camera YAML Example

The following config streams from two cameras on separate ports. Each `CustomWriter` instance must use a **unique** `port` to avoid conflicts:

```python
replicator:
  writers:
    CustomWriter:
      writer_name: "RTSPStreamWriter"
      writer_scope: "isaacsim.streaming.rtsp"
      sensor_prim_list:
        - "<your_camera_prim_path>"
      port: <your_unique_port>
      mountPath: "<your_mount_path>"
      encoding: "h264"
    CustomWriter_1:
      writer_name: "RTSPStreamWriter"
      writer_scope: "isaacsim.streaming.rtsp"
      sensor_prim_list:
        - "<your_camera_prim_path>"
      port: <your_unique_port>  # Must differ from the port above
      mountPath: "<your_mount_path>"
      encoding: "h264"
```

Tip

If the `isaacsim.streaming.rtsp` extension is enabled and `RTSPStreamWriter` is already registered, `writer_scope` can be omitted. It is included here for robustness so the config works even when the extension has not been loaded yet. You can also use a full class path (for example, `"isaacsim.streaming.rtsp.impl.rtsp_writer.RTSPStreamWriter"`) instead of a package path if you prefer to register only one specific writer.

## Verify the Stream

After clicking **Start Data Generation**, open an RTSP client and connect to the stream URL. For example, with `ffplay`:

```python
ffplay rtsp://localhost:8554/camera_01
```

You should receive live rendered frames from the corresponding camera. Repeat for each port and mount-path pair to verify all streams.

See also

[Live Camera Streaming over RTSP](../../digital_twin/rtsp_camera_streaming.html#isaac-sim-rtsp-camera-streaming) for a full reference for the RTSP
streaming pipeline, including encoding modes, frame metadata, server
lifecycle, and troubleshooting.

On this page

* [Prerequisites](#prerequisites)
* [Step 1: Enable the RTSP Streaming Extension](#step-1-enable-the-rtsp-streaming-extension)
* [Step 2: Add a CustomWriter and Select the Writer](#step-2-add-a-customwriter-and-select-the-writer)
* [Step 3: Manual Registration](#step-3-manual-registration)
* [Step 4: Configure the Sensor Prim List](#step-4-configure-the-sensor-prim-list)
* [Step 5: Set the Port and Mount Path](#step-5-set-the-port-and-mount-path)
* [Step 6: Optional Encoding Settings](#step-6-optional-encoding-settings)
  + [Parameter Naming in the UI](#parameter-naming-in-the-ui)
* [Multi-camera YAML Example](#multi-camera-yaml-example)
* [Verify the Stream](#verify-the-stream)

---

### Sample Configs

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/action_and_event_data_generation/ext_replicator-agent/ext_isaacsim_replicator_agent_sample_configs.html

* [Synthetic Data Generation](../../synthetic_data_generation/index.html)
* [Action and Event Data Generation](../index.html)
* [Actor Simulation and Synthetic Data Generation](../tutorial_replicator_agent.html)
* Sample Configs

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Sample Configs

The `isaacsim.replicator.agent.core` extension ships with a small set of YAML
configurations under `[ext-path]/data/sample_configs/`. They demonstrate the
recommended ways to configure the Isaac replicator agent (IRA), from the smallest valid config to a full
data-generation pipeline.

## Layout

The directory is organized as follows:

```python
sample_configs/
  minimal.yaml         # smallest valid config (env only)
  full_pipeline.yaml   # end-to-end demo: routines + sensors + writers
  behavior_tree/       # behavior-tree samples (experimental)
    wander.yaml
    patrol_and_wander.yaml
    instance_overrides.yaml
```

Behavior-tree samples live under `behavior_tree/` because behavior-tree character
support is currently experimental (refer to [Behavior Tree Character
Group (Experimental)](ext_isaacsim_replicator_agent_configuration.html#ira-bt-character-group)). The two top-level samples
use the stable routine-trigger character API and are the recommended
starting point.

## Standard Samples

Top-level samples. They use the stable routine-trigger character API
(refer to [Configuration File](ext_isaacsim_replicator_agent_configuration.html#ira-configuration-file)).

| File | Expected behavior | Demonstrates |
| --- | --- | --- |
| `minimal.yaml` | Opens the warehouse stage. No actors, sensors, or data generation â a sanity check that IRA is enabled and the asset server is reachable. | Smallest valid IRA config. Loaded by the IRA UI on launch. |
| `full_pipeline.yaml` | 10 workers wander the warehouse for 60 seconds while six randomly placed ceiling cameras capture per-frame RGB, depth, segmentation, bounding boxes, and cosmos video annotations to the output folder. | End-to-end pipeline: routine-based character behavior, RTX sensor placement (`aim_at_targets`), and `IRABasicWriter`. |

## Behavior-Tree Samples (Experimental)

Samples under `sample_configs/behavior_tree/` that drive characters with
behavior trees instead of routines. The trees themselves live in the sibling
`sample_behavior_tree/` folder of the extension.

| File | Expected behavior | Demonstrates | Behavior Tree asset |
| --- | --- | --- | --- |
| `behavior_tree/wander.yaml` | Two warehouse workers wander randomly through the warehouse. | Single behavior-tree character group. | `sample_behavior_tree/wander.json` |
| `behavior_tree/patrol_and_wander.yaml` | Two agents follow a fixed patrol route while three others wander around them. | Two BT character groups (patrol + wander) coexisting in one config. | `sample_behavior_tree/patrol.json` + `wander.json` |
| `behavior_tree/instance_overrides.yaml` | Two warehouse workers each pick up a different cardboard box and carry it to a destination marker (`Destination_A`, `Destination_B`). | Per-group `overrides` on a shared Behavior Tree. Each group binds `SetBlackboard.slot`, `PickupObject.target`, and `PlaceObject.xform` to its own values using `instanceOverrides`. | `sample_behavior_tree/box_mover_multiple.json` |

On this page

* [Layout](#layout)
* [Standard Samples](#standard-samples)
* [Behavior-Tree Samples (Experimental)](#behavior-tree-samples-experimental)

---

### Anim Robot

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/action_and_event_data_generation/ext_replicator-agent/ext_isaacsim_anim_robot.html

* [Synthetic Data Generation](../../synthetic_data_generation/index.html)
* [Action and Event Data Generation](../index.html)
* [Actor Simulation and Synthetic Data Generation](../tutorial_replicator_agent.html)
* Animated Robot Controller

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Animated Robot Controller

The `isaacsim.anim.robot.core` extension enables realistic robot animation through the playback of captured simulation motion data. It bridges physics-based simulation and animation, allowing users to recreate precise robot movements without the computational overhead of real-time physics calculations. The extension converts physics-enabled robot models into animated representations while preserving their kinematic accuracy and visual fidelity.

`isaacsim.anim.robot.core` integrates with the `omni.metropolis.pipeline` agent framework. Each robot is an `AnimRobot` â a Metro Agent with a finite state machine that drives animation playback. Robots are configured through YAML files that define their kinematics, states, transitions, and animation data.

## Supported Robots

The extension ships with sample configurations for the following robots:

* **Nova Carter** â differential drive mobile robot
* **iw.hub** â differential drive warehouse robot with lift capability
* **Forklift** â differential drive forklift

Custom robots can be added by creating a new YAML configuration file (see [Customization](#customization)).

## Architecture

The extension is composed of several key modules:

* **AnimRobot** â the agent class that integrates with `omni.metropolis.pipeline`. It parses USD schema attributes, loads configuration, sets up the state machine, and manages the robotâs lifecycle.
* **StateMachine** â a finite state machine that manages animation states and transitions. Each state can have associated animation data that is played back on the robotâs joints.
* **Actions** â high-level commands (`MoveTo`, `Idle`, `Turn`, `Sequence`) that drive the robot by updating the state machine and applying motion each frame.
* **Drive** â drive-base implementations (`OmniDirectionalDrive`, `DifferentialDrive`) that translate navigation paths into per-frame position and orientation updates.
* **PathPlanner** â path planning backends exposing `get_path_points(start, end, agent_radius=0.5)` and returning a `list[Gf.Vec3d]` of waypoints (or `None` when no path exists). The `NavMeshPathPlanner` snaps `start` and `end` to the nearest valid navmesh location, queries the shortest path, and drops near-collinear waypoints before returning; the base `PathPlanner` returns the two-point straight line from `start` to `end` without any obstacle checks.
* **Behaviors** â runtime behaviors (`Wander`, `Patrol`, `Halt`) and triggers (`Event`, `Time`, `Collision`) that compose actions into autonomous agent routines.

## Customization

Robot behavior and animation can be customized by modifying or creating a YAML agent configuration file. Sample configurations ship on the Isaac Sim asset server at `/Isaac/Samples/AnimRobot/sample_configs/{robot type}.yaml`; `get_IAR_sample_config_path()` (refer to [Public API](#public-api)) resolves this path at runtime and falls back to the local copy bundled with the extension at `{isaacsim.anim.robot.core extension path}/data/sample_configs/` when the asset server is unreachable.

## Robot Attributes

The following attributes can be configured for each robot (based on the `BaseAgentConfig` schema):

* **agent\_name** (str): Display name of the agent (default: `"BaseAgent"`). Spaces are automatically replaced with underscores.
* **linear\_velocity** (float): Forward movement speed in meters per second (default: `1.0`, must be >= 0).
* **angular\_velocity** (float): Turning speed in degrees per second (default: `45.0`, must be >= 0).
* **forward\_vec** (list[float]): Initial forward direction vector, exactly 3 elements (default: `[1.0, 0.0, 0.0]`).
* **joints** (list[str]): List of joint prim relative paths that can be animated.
* **drive\_base** (str): Robotâs drive system type. Supported values: `differential`, `omni_directional` (default: `omni_directional`).
* **path\_planner** (str): Path planner type. Supported values: `navmesh`, `base` (default: `navmesh`).
* **states** (list[str]): List of FSM state names (default: `["idle", "turn_left", "turn_right", "forward"]`). Drive implementations push the FSM into these specific state names; any custom `states` list must still include `idle`, `forward`, `turn_left`, and `turn_right`, or the drive base will log a ânot in any valid stateâ error during motion.
* **transitions** (dict[str, list[str]]): State transition graph defining valid transitions between states. Source and destination states are validated against the `states` list. Defaults to `{idle: [turn_left, turn_right, idle, forward], turn_left: [idle, forward], turn_right: [idle, forward], forward: [turn_left, turn_right, idle]}`.
* **animation\_paths** (dict[str, str]): Mapping of state names to folder paths containing animation USDs. Paths may use the `${ext_path}` variable to reference the extensionâs install directory.
* **asset\_path** (str | null): Relative or absolute path/URL to the agent USD. If relative, it tries local file first, then the Isaac Sim asset root. If omitted, the primâs existing references are used.
* **radius** (float | null): Internal runtime override for the navmesh query radius. The YAML loader does not currently populate this field (it is declared `init=False` on `RuntimeAgentConfig` and is not derived from the agentâs bounding box), so setting it in the per-robot YAML has no effect today. To control the planning radius for an IRA-spawned robot, set `agent_radius` on the IRA robot group instead.

**Example Configuration (iw\_hub.yaml):**

```python
agent_name: iw_hub
linear_velocity: 0.5
angular_velocity: 30.0
forward_vec: [1.0, 0.0, 0.0]
joints:
  - /chassis/lift
  - /chassis/left_wheel
  - /chassis/right_wheel
  - /chassis/left_swivel/left_caster
  - /chassis/right_swivel/right_caster
  - /chassis/left_swivel
  - /chassis/right_swivel
drive_base: differential
path_planner: navmesh
animation_paths:
  turn_left: ${ext_path}/data/sample_animations/iw_hub/turn_left
  turn_right: ${ext_path}/data/sample_animations/iw_hub/turn_right
  forward: ${ext_path}/data/sample_animations/iw_hub/forward
  lift_up: ${ext_path}/data/sample_animations/iw_hub/lift_up
  lift_down: ${ext_path}/data/sample_animations/iw_hub/lift_down
states: [idle, turn_left, turn_right, forward, lift_up, lift_down]
transitions:
  idle: [turn_left, turn_right, idle, forward, lift_up, lift_down]
  turn_left: [forward, idle]
  turn_right: [forward, idle]
  forward: [turn_left, turn_right, idle]
  lift_up: [idle]
  lift_down: [idle]
asset_path: Isaac/Samples/AnimRobot/iw_hub.usd
radius: 0.8
```

## Actions

The extension provides the following action types for controlling robots programmatically:

* **MoveTo** â moves the agent to a target position using the configured path planner and drive base. The target may be an `[x, y, z]` coordinate or a USD prim reference (`Sdf.Path`, prim-path string, or `Usd.Prim`); prim targets are re-resolved every 0.25 seconds and the path is replanned when the prim drifts past 0.25 minutes, so the agent tracks a moving target. The agent plans a path, then follows it by transitioning through turn and forward states.
* **Idle** â keeps the agent in the idle state for a specified duration (in seconds).
* **Turn** â rotates the agent in place to face a given 3D direction vector (yaw-only; the Z component is ignored).
* **PlayAnimation** â plays a named FSM state on the agent. When `duration` is `0.0` (the default), the state plays once to its last time sample and the action completes; when `duration > 0`, the state is held for that many seconds.
* **Sequence** â executes a non-empty list of actions in order, one after another.

Actions can be created using functional APIs:

```python
from isaacsim.anim.robot.core import (
    idle,
    move_to,
    play_animation,
    resolve_anim_robot,
    sequence,
    turn,
)

# Resolve the live runtime agent from its USD prim.
agent = resolve_anim_robot(prim)
cfg, sm = agent.runtime_config, agent.state_machine

# Move to a world-space position
action = move_to(cfg, sm, [10.0, 5.0, 0.0])

# Or move to (and track) a USD prim target
action = move_to(cfg, sm, "/World/pickup_target")

# Idle for 3 seconds
action = idle(cfg, sm, 3.0)

# Turn to face a direction (yaw-only)
action = turn(cfg, sm, [0.0, 1.0, 0.0])

# Play a named FSM state (duration=0 plays once to the clip's end)
action = play_animation(cfg, sm, "lift_up")

# Compose a sequence and inject it into the running agent
action = sequence(
    [
        move_to(cfg, sm, [10.0, 5.0, 0.0]),
        idle(cfg, sm, 2.0),
        turn(cfg, sm, [0.0, -1.0, 0.0]),
    ],
    execute_now=True,
)
```

Each action can also be injected into a running agent through the `execute()` method (or using `sequence(..., execute_now=True)`). Injection writes the action into the agentâs routines, so it only applies when the agent is in **RoutineTrigger** control mode; behavior-tree-controlled agents receive actions by ticking BT nodes instead.

## Behaviors

Behaviors define higher-level autonomous routines that compose actions. They are configured through the USD schema and run within the `omni.metropolis.pipeline` trigger system.

* **Wander** â the robot moves to random navmesh-reachable points within a configurable distance range, then idles for a random duration. Configurable attributes include navigation areas, idle time range, and movement distance range.
* **Patrol** â the robot visits a sequence of waypoints (specified as either `[x, y, z]` coordinates or USD prim targets) in order. Unreachable waypoints are skipped with a warning.
* **Halt** â the robot idles for a random duration within a configurable time range.

These behaviors can be triggered by:

* **Event triggers** â activated by external events
* **Time triggers** â activated on a time schedule
* **Collision triggers** â activated when another prim enters a configured collision volume on the agent

## Drive Types

The extension supports different drive-base implementations that control how the robot physically moves and turns:

* **OmniDirectionalDrive** â the agent can move in any direction without needing to turn first. It navigates along a path with constant linear velocity and can independently rotate to face a target direction.
* **DifferentialDrive** â the agent must turn in place to face the target direction before driving forward. It follows a turn-then-drive pattern: first rotating toward the next waypoint, then moving forward in a straight line.

The drive type is selected based on the `drive_base` field in the YAML configuration.

## Customizing Animations

To create custom animations:

1. Simulate the robot in Isaac Sim.
2. Use `omni.kit.stagerecorder.core` to capture motion data.
3. Update the `animation_paths` field in the YAML configuration with new animation folder paths.

Animation files should be organized in state-specific folders. Each jointâs animation data is stored as a separate USD file named after the joint. For example, `iw.hub`âs turn-left animation is located at:
`{isaacsim.anim.robot.core extension path}/data/sample_animations/iw_hub/turn_left/`

## Public API

User code (behavior trees, custom runtime states, standalone scripts) should import only from `isaacsim.anim.robot.core`; other submodules are internal and may change without notice.

**Action factories** â return an opaque action handle with `update(dt)`, `is_done()`, and `cancel()` methods:

* `idle(runtime_config, state_machine, duration)`
* `move_to(runtime_config, state_machine, target)` â `target` may be a Float3-like coordinate or a USD prim reference (`Sdf.Path`, prim-path string, or `Usd.Prim`).
* `turn(runtime_config, state_machine, direction)` â yaw-only.
* `play_animation(runtime_config, state_machine, state_name, duration=0.0)` â `duration=0.0` plays the state once to its last time sample; `duration > 0` holds it for that many seconds.
* `sequence(actions, execute_now=False)` â `actions` must be non-empty; pass `execute_now=True` to inject the sequence into the running agent without a separate `execute()` call.

**Agent lookup**

* `resolve_anim_robot(prim)` â given a `Usd.Prim`, return the live `AnimRobot` registered for that prim (exposing `.runtime_config` and `.state_machine`), or `None` when the prim is invalid, no agent has been registered yet (typical before the timeline starts), or the runtime has been torn down.

**Utility**

* `get_IAR_sample_config_path()` â resolved path to the bundled sample-config folder. Returns the Isaac Sim asset server path (`/Isaac/Samples/AnimRobot/sample_configs/`) when reachable, or the local extension copy as a fallback.

## Behavior Tree Nodes

* [Animated Robot Behavior Tree Nodes](ext_isaacsim_anim_robot_bt_nodes.html)

On this page

* [Supported Robots](#supported-robots)
* [Architecture](#architecture)
* [Customization](#customization)
* [Robot Attributes](#robot-attributes)
* [Actions](#actions)
* [Behaviors](#behaviors)
* [Drive Types](#drive-types)
* [Customizing Animations](#customizing-animations)
* [Public API](#public-api)
* [Behavior Tree Nodes](#behavior-tree-nodes)

---


## BehaviorTree

### BT Context Files & Schemas

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/action_and_event_data_generation/ext_behavior_tree_gen/context_files_and_schemas.html

* [Synthetic Data Generation](../../synthetic_data_generation/index.html)
* [Action and Event Data Generation](../index.html)
* [Behavior Tree Generation](../tutorial_behavior_tree_gen.html)
* Context Files and Metadata Schemas

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Context Files and Metadata Schemas

This guide explains the context-file format used by the example data bundled with
`omni.ai.behavior_tree_gen.bridge` under `data/example/context_info` and the base models defined
in `omni.ai.behavior_tree_gen.core.pydantic.models`.

* **Context** is the runtime knowledge base of actors and objects in a scene. Each context entry is
  a JSON object that follows one of two base models:

  + `ActorInfo`
  + `InteractableObjectInfo`
* **Metadata schema** is a standard JSON Schema document that defines the structure of the
  `metadata` dictionary inside each context entry.

## Base Context Entry Format

Context entries are built on two base models that are defined in the `omni.ai.behavior_tree_gen.core.pydantic.models.context_models` module:

* `ActorInfo`
* `InteractableObjectInfo`

Both models use the same top-level structure:

```python
{
  "id": "UniqueName",
  "semantic_description": "Natural-language description of this entity.",
  "metadata": {
  },
  "supported_interactions": [],
  "entity_type": "object"
}
```

Top-level fields:

* `id`: Stable identifier used by the pipeline to refer to the entity.
* `semantic_description`: Human-readable description used during retrieval and grounding.
* `metadata`: Domain-specific fields defined by the actor or object schema.
* `supported_interactions`: Optional list of passive interaction labels supported by the entity.
* `entity_type`: Must be `actor` or `object`.

Note

`supported_interactions` is defined on the base context models, not in the metadata schema.
When present, the model normalizes the values to lowercase unique tokens.

## Actor Example

The bundled `simple` example uses actor entries shaped like this:

```python
{
  "id": "Anna",
  "semantic_description": "A female human actor with short hair and a purple vest, with jeans and white sneakers.",
  "metadata": {
    "actor_type": "human",
    "role": "test_actor",
    "location": {
      "x": 0.0,
      "y": 0.0,
      "z": 0.0
    },
    "prim_path": "/World/Actors/Anna",
    "move_to": "/World/Characters/Anna/female_adult_business_02/ManRoot/female_adult_business_02",
    "semantic_label": "human"
  },
  "entity_type": "actor"
}
```

This follows `ActorInfo` at the top level and stores domain-specific details such as
`actor_type`, `role`, `location`, and `prim_path` under `metadata`.

## Object Example

The bundled `simple` example uses object entries shaped like this:

```python
{
  "id": "Table",
  "semantic_description": "An office table used for placing objects.",
  "metadata": {
    "interactable_type": "table",
    "prim_path": "/World/TestEnv/SM_TableB",
    "semantic_label": "office table",
    "move_to_targets": {
      "default": "/World/TestEnv/SM_TableB/MoveToTarget"
    },
    "placement_targets": {
      "left_end": "/World/TestEnv/SM_TableB/PlaceObject_LeftEnd",
      "right_end": "/World/TestEnv/SM_TableB/PlaceObject_RightEnd",
      "middle": "/World/TestEnv/SM_TableB/PlaceObject_Middle"
    }
  },
  "supported_interactions": [
    "move to",
    "place on"
  ],
  "entity_type": "object"
}
```

This follows `InteractableObjectInfo` at the top level and stores object-specific metadata such as
`interactable_type`, `prim_path`, `move_to_targets`, and `placement_targets` inside
`metadata`.

## How Metadata Schemas Work

The schema files under `data/example/context_info/schemas` define the structure of `metadata`.
For the bundled examples:

* `actor_metadata_schema.json` defines fields such as `prim_path`, `semantic_label`,
  `actor_type`, `role`, and nested `location` data.
* `object_metadata_schema.json` defines fields such as `interactable_type`, `prim_path`,
  `semantic_label`, `move_to_targets`, `placement_targets`, and `usage_guide`.

In the core implementation, `ContextCacheManager.setup_actor_model_from_schema()` and
`ContextCacheManager.setup_object_model_from_schema()` use
`omni.ai.behavior_tree_gen.core.pydantic.models.schema_builder.build_metadata_model_from_json_schema()` to build a
typed metadata model and then attach it to `ActorInfo` or `InteractableObjectInfo`.

This means:

* Base fields such as `id`, `semantic_description`, `supported_interactions`, and
  `entity_type` stay at the top level.
* Schema-defined fields belong under `metadata`.
* Schema types, descriptions, enums, and numeric constraints are preserved in the typed metadata
  model.
* Extra metadata fields are still allowed because the schema builder uses `allow_extra=True`.

## Bundled Required Metadata Fields

The shipped example schemas mark these metadata fields as required:

* Actors: `metadata.prim_path` and `metadata.actor_type`.
* Objects: `metadata.prim_path` and `metadata.interactable_type`.

If you extend those schemas with new required fields, matching context entries should provide those
fields under `metadata`.

## Planner-visible Schema Paths

The pipeline expands schema-defined metadata fields into planner-visible term paths.

Examples:

* `actors.metadata.role`.
* `actors.metadata.location.x`.
* `objects.metadata.prim_path`.
* `objects.metadata.move_to_targets.default`.
* `objects.metadata.placement_targets.left_end`.

These paths are used for grounding, retrieval, and parameter generation, so field names and
descriptions in the schema directly affect how well the workflow can use your custom data.

## Add a Custom Metadata Field

To add a new item using your own schema:

1. Start from the existing actor or object schema and add the new metadata field there.
2. Add the same field under `metadata` in each matching context item.
3. Reload the workspace so the pipeline rebuilds the typed metadata models from the updated files.

Example schema extension for objects:

```python
{
  "type": "object",
  "properties": {
    "interactable_type": {
      "type": "string",
      "description": "Category of the object."
    },
    "prim_path": {
      "type": "string",
      "description": "USD path for the object."
    },
    "zone": {
      "type": "string",
      "description": "Warehouse zone label for this item.",
      "example": "A1"
    }
  },
  "required": [
    "interactable_type",
    "prim_path"
  ]
}
```

Matching context entry:

```python
{
  "id": "CardBox_C",
  "semantic_description": "A cardboard box stored in zone A1.",
  "metadata": {
    "interactable_type": "box",
    "prim_path": "/World/TestEnv/SM_CardBoxA_04",
    "semantic_label": "cardboard box",
    "zone": "A1"
  },
  "supported_interactions": [
    "pickup",
    "place"
  ],
  "entity_type": "object"
}
```

Tip

Keep stable identity and planner-facing descriptions at the top level, and put schema-defined
domain attributes under `metadata`.

## Using the Files in Behavior Tree Generation

After updating the files:

* In the UI, select the context files and matching schema files in **Context Cache Files** inside
  **Behavior Tree Gen**.
* In Python, pass the context files through `context_data_paths` and the schema files through
  `actor_schema_path` or `object_schema_path` when calling `setup_workspace(...)`.
* Reload the workspace so the updated typed models and schema paths are available to the pipeline.

The bundled example files are good references when authoring your own context data.

On this page

* [Base Context Entry Format](#base-context-entry-format)
* [Actor Example](#actor-example)
* [Object Example](#object-example)
* [How Metadata Schemas Work](#how-metadata-schemas-work)
* [Bundled Required Metadata Fields](#bundled-required-metadata-fields)
* [Planner-visible Schema Paths](#planner-visible-schema-paths)
* [Add a Custom Metadata Field](#add-a-custom-metadata-field)
* [Using the Files in Behavior Tree Generation](#using-the-files-in-behavior-tree-generation)

---

### BT Example Walkthrough

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/action_and_event_data_generation/ext_behavior_tree_gen/example_walkthrough.html

* [Synthetic Data Generation](../../synthetic_data_generation/index.html)
* [Action and Event Data Generation](../index.html)
* [Behavior Tree Generation](../tutorial_behavior_tree_gen.html)
* Example Walkthrough

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Example Walkthrough

This walkthrough uses the bundled **Basic Scene** scene and the **Behavior Tree Gen**
workflow shipped in `omni.ai.behavior_tree_gen.bridge`.

## Goal

Generate a behavior tree for the following scenario:

```python
Anna picks up the CardBox_A and places it on the Table.
```

## Steps

1. Open the examples window from **Window > Examples > Behavior Tree Gen Examples**.
2. In the examples window, select **Basic Scene** and click the button to load the example
   scene.

   * This loads the bundled demo stage.
   * It also pre-fills the workflow panels from the `Basic Scene` scene configuration.
   * The **Behavior Tree Gen** window is shown automatically, so you do not need to open it
     separately.
3. In **Behavior Tree Gen**, verify the loaded inputs.

   * The **Context Cache Files** panel should contain the example actor and object context files,
     node catalogs, and metadata schemas.
   * The **Network Config** panel should contain the example model JSON paths.
   * The **Output Settings** panel should point to a writable output directory.
4. Enter a valid NVIDIA API key, if one is not already available from settings or the environment.
5. Paste or type the scenario text:

   ```python
   Anna picks up the CardBox_A and places it on the Table.
   ```
6. Click **Run Pipeline**.

## What Happens Internally

When you click **Run Pipeline**, the **Behavior Tree Gen** UI performs the same three public API steps that scripted
callers use:

1. It creates or reloads the planner workspace from the selected context, catalog, schema, and
   blackboard files.
2. It prepares the runtime by configuring the LLM, embedding setup, RAG retrievers, and Action IR.
3. It generates the behavior tree from the natural-language scenario.

## Expected Result

If the run succeeds:

* the status line reports that generation completed successfully
* behavior tree output files are written under the selected output folder
* planner cache data is stored under a workspace cache directory
* RAG and vectorstore data is stored under the derived cache directory

## Known limitations of Example Actions

Note

The custom actions bundled with the examples (such as `MoveTo`) are provided to demonstrate that
the system supports action node imports and is fully extensible. At this stage, some actions may
exhibit imperfect behavior. For example, `MoveTo` can produce paths that overlap with the target
object. These examples serve as a transitional reference, a more comprehensive and refined set of
actions is planned.

## Useful Behavior to Know

* If you run the same scenario again without changing the tracked input files, the extension can
  reuse the loaded workspace and prepared runtime.
* If you change a tracked file such as a context file, node catalog, schema, or model config, the
  extension reloads the workspace and prepares the runtime again.
* You can repeat the same flow with **Warehouse Scene** to test a multi-actor scenario.

On this page

* [Goal](#goal)
* [Steps](#steps)
* [What Happens Internally](#what-happens-internally)
* [Expected Result](#expected-result)
* [Known limitations of Example Actions](#known-limitations-of-example-actions)
* [Useful Behavior to Know](#useful-behavior-to-know)

---

### BT Required Inputs

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/action_and_event_data_generation/ext_behavior_tree_gen/required_inputs.html

* [Synthetic Data Generation](../../synthetic_data_generation/index.html)
* [Action and Event Data Generation](../index.html)
* [Behavior Tree Generation](../tutorial_behavior_tree_gen.html)
* Required inputs

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Required inputs

The behavior tree generation workflow in `omni.ai.behavior_tree_gen` can be used in two ways:

* **Manually**, by filling in the UI.
* **From bundled examples**, where most file inputs are pre-populated automatically.

## Base inputs for every run

These inputs form the first layer of a run:

* **Scenario text**: Natural-language task or goal, such as
  `Anna picks up the CardBox_A and places it on the Table.`.
* **Output folder**: Writable folder where generated behavior trees and reusable cache data are
  stored.
* **NVIDIA API key**: Required during runtime preparation for NVIDIA-hosted chat and embedding
  models. The key can come from the UI, carb settings, or `NVIDIA_API_KEY`.
* **Context files**: One or more JSON files containing the actor and object instances for the scene,
  including their metadata values.
* **Node catalog files**: One or more JSON files describing the behavior tree nodes the pipeline is
  allowed to use.

Note

Context files should be read together with the actor and object schema files. The context provides
the concrete scene data, while the schema defines the metadata fields and structure that give that
data planner-visible meaning.

## Advanced direct inputs

These inputs shape metadata interpretation and runtime model routing:

* **Actor schema file**: Defines the structure of actor metadata used by the pipeline.
* **Object schema file**: Defines the structure of object metadata used by the pipeline.
* **Model selection config**: Selects the default chat model and embedding model and can define
  per-node overrides that drive runtime behavior.
* **Embedding model configs**: Defines the named embedding profiles referenced by the model
  selection config during RAG and retriever preparation.
* **Named model configs**: Defines the named chat-model profiles referenced by model selection and
  per-node routing.
* **Node-to-model map**: Provides explicit routing from planner nodes to named chat models when
  runtime behavior must be controlled per node.

## Conditional inputs

The following input is optional, but important when the workflow depends on it:

* **Blackboard file**: Preloads blackboard metadata and variables into the workspace when
  blackboard-driven planning data should be available.

## Relationship between schema and context

The schema files and context files work together as a connected input set:

* **Context** provides the instance data for actors, objects, identifiers, and metadata values.
* **Schema** provides the structure and meaning of that metadata.
* During workspace setup, the pipeline loads the actor and object schemas first, builds typed
  models from them, and then loads the context JSON into those typed models.
* During runtime preparation, schema-derived terms are reused for grounding, parameter generation,
  and Action IR preparation.

## Where these inputs usually come from

* The examples window can load the bundled `simple` or `warehouse` scene and prefill the
  **Behavior Tree Gen** panels from a scene configuration JSON.
* The **Context Cache Files** panel is where context files, node catalogs, blackboard data, and
  metadata schemas are selected.
* The **Network Config** panel is where the API key and model-related JSON files are selected.
* The **Planner** panel is where the scenario text is entered.

## Bundled example inputs

For the built-in `simple` example, the extension automatically resolves inputs such as:

* actor and object context JSON files.
* actor and common node catalog JSON files.
* a blackboard JSON file.
* actor and object metadata schema JSON files.
* model selection, embedding-model, and named-model JSON files.

If you use the example flow, the main values you still need to confirm are the NVIDIA API key, the
output folder, the scenario text, and any additional runtime routing inputs required by your model
selection setup.

On this page

* [Base inputs for every run](#base-inputs-for-every-run)
* [Advanced direct inputs](#advanced-direct-inputs)
* [Conditional inputs](#conditional-inputs)
* [Relationship between schema and context](#relationship-between-schema-and-context)
* [Where these inputs usually come from](#where-these-inputs-usually-come-from)
* [Bundled example inputs](#bundled-example-inputs)

---

### BT Three API Functions

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/action_and_event_data_generation/ext_behavior_tree_gen/three_api_functions.html

* [Synthetic Data Generation](../../synthetic_data_generation/index.html)
* [Action and Event Data Generation](../index.html)
* [Behavior Tree Generation](../tutorial_behavior_tree_gen.html)
* Using the API Functions

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Using the API Functions

The **Behavior Tree Gen** UI in `omni.ai.behavior_tree_gen.bridge` is a thin wrapper around the
three-step public API in `omni.ai.behavior_tree_gen.core.api`:

1. `setup_workspace(...)`.
2. `await prepare_runtime(...)`.
3. `await generate_behavior_tree(...)`.

Use them in that exact order.

This page keeps the examples next to each API description because each call prepares state that the
next call consumes.

## Shared Example Setup

The snippets below use helper functions from `omni.ai.behavior_tree_gen.bridge.utils` only to
resolve the bundled `simple` example files. Replace those helper calls with your own file paths
when using custom planner data.

```python
import os
from pathlib import Path

from omni.ai.behavior_tree_gen.core import api as core_api
from omni.ai.behavior_tree_gen.bridge.utils import (
    get_example_scene_context_files,
    get_extension_path,
    load_example_scene_config,
    resolve_example_scene_file_path,
)

# Change these inputs to match your environment.
ROOT_DIR = Path("Your/Output/Folder/Path") / "behavior_tree_gen_output"
OUTPUT_DIR = ROOT_DIR / "output"
API_KEY = "Your_NVIDIA_API_key"
SCENARIO = "Anna picks up the CardBox_A and places it on the Table."

ext_path = get_extension_path()
scene_config = load_example_scene_config("simple")
context_files = get_example_scene_context_files("simple")

if ext_path is None or scene_config is None:
    raise RuntimeError("Could not load the bundled example scene configuration.")
if not API_KEY:
    raise RuntimeError("Set NVIDIA_API_KEY before running this example.")

node_catalog_paths = []
for path in (scene_config.get("node_catalogs") or {}).values():
    resolved_path = resolve_example_scene_file_path(path, ext_path=ext_path)
    if resolved_path:
        node_catalog_paths.append(resolved_path)

metadata_schemas = scene_config.get("metadata_schemas", {})
actor_schema_path = resolve_example_scene_file_path(
    metadata_schemas.get("actor"),
    ext_path=ext_path,
)
object_schema_path = resolve_example_scene_file_path(
    metadata_schemas.get("object"),
    ext_path=ext_path,
)

model_info = scene_config.get("model_info", {})
model_selection_config_path = resolve_example_scene_file_path(
    model_info.get("model_selection_config"),
    ext_path=ext_path,
)
embedding_model_configs_path = resolve_example_scene_file_path(
    model_info.get("embedding_model_configs"),
    ext_path=ext_path,
)
named_model_configs_path = resolve_example_scene_file_path(
    model_info.get("model_configs"),
    ext_path=ext_path,
)
node_to_model_map_path = resolve_example_scene_file_path(
    model_info.get("node_to_model_map"),
    ext_path=ext_path,
)
```

## Step 1: setup\_workspace(â¦)

Use this function to create a reusable `PlannerSession` and load input data into the workspace.

The Python signature makes every argument optional, but real planner runs usually provide:

* `cache_dir`: Folder for reusable planner cache artifacts.
* `output_dir`: Folder where generated behavior tree files are written.
* `context_data_paths`: Actor and object context JSON files.
* `node_catalog_paths`: Behavior tree node catalog JSON files.

Common optional inputs:

* `vectorstore_dir`: Folder for RAG and vectorstore data. If omitted, the runtime derives it from
  `cache_dir` when possible.
* `actor_schema_path` and `object_schema_path`: Metadata schema files for typed planner-visible
  fields.
* `blackboard_data_paths` and `apply_blackboard_cache`: Optional blackboard preload controls.
* `refresh_cache`: Rebuild workspace caches before loading inputs.

What it returns:

* one `PlannerSession` object
* session fields such as `actors_loaded`, `objects_loaded`, `nodes_loaded`, and
  `workspace_ready`

Example:

```python
session = core_api.setup_workspace(
    cache_dir=str(OUTPUT_DIR / "planner_cache"),
    output_dir=str(OUTPUT_DIR),
    context_data_paths=context_files["actors"] + context_files["objects"],
    node_catalog_paths=node_catalog_paths,
    actor_schema_path=actor_schema_path,
    object_schema_path=object_schema_path,
)

print(session.workspace_ready)
print(session.actors_loaded, session.objects_loaded, session.nodes_loaded)
```

## Step 2: prepare\_runtime(â¦)

Use this function after workspace setup to configure model access, retrievers, and Action IR for
the session.

Required parameters:

* `session`: The `PlannerSession` returned by `setup_workspace(...)`.
* `api_key`: NVIDIA API key.

Common optional inputs:

* `model_selection_config_path`: Default LLM and embedding selection file.
* `embedding_model_configs_path`: Named embedding profiles.
* `named_model_configs_path`: Named chat-model profiles.
* `node_to_model_map_path`: Explicit node-to-model routing.
* `actor_types`: Warm only the listed actor types into Action IR.
* `prefer_cached_action_ir`: Reuse compatible prepared Action IR when available.
* Direct overrides such as `llm_model`, `embedding_model`, `rag_top_k`, and
  `rag_similarity_threshold`.

What it does:

* configures NVIDIA model access
* prepares the context retriever and RAG state
* prepares or reuses Action IR for the current actor types

What it returns:

* a `PlannerRuntimeResult`
* fields such as `success`, `message`, `chat_model_name`, `retriever_ready`,
  `action_ir_ready`, and `warmed_actor_types`

Example:

```python
runtime_result = await core_api.prepare_runtime(
    session,
    api_key=API_KEY,
    model_selection_config_path=model_selection_config_path,
    embedding_model_configs_path=embedding_model_configs_path,
    named_model_configs_path=named_model_configs_path,
    node_to_model_map_path=node_to_model_map_path,
)

if not runtime_result.success:
    raise RuntimeError(runtime_result.message)

print(runtime_result.chat_model_name)
print(runtime_result.retriever_ready, runtime_result.action_ir_ready)
```

## Step 3: generate\_behavior\_tree(â¦)

Use this function only after the session has a ready workspace and a prepared runtime.

Required parameters:

* `session`: The prepared `PlannerSession`.
* `scenario`: A natural-language instruction or goal.

Common optional inputs:

* `skip_phase3`: Skip the phase-3 tree-construction stage when debugging the earlier pipeline
  stages.

What it returns:

* a `PipelineResult`
* `success`
* `duration_seconds`
* `behavior_tree_folder_path`
* `error_message`

Example:

```python
result = await core_api.generate_behavior_tree(
    session,
    SCENARIO,
)

if not result.success:
    raise RuntimeError(result.error_message)

print(result.success)
print(result.behavior_tree_folder_path)
```

## Async Execution Note

`setup_workspace(...)` is synchronous, but `prepare_runtime(...)` and
`generate_behavior_tree(...)` are coroutines. In Script Editor, put the shared setup and the three
step snippets inside one async function and schedule it:

```python
import asyncio
import os
from pathlib import Path

from omni.ai.behavior_tree_gen.core import api as core_api
from omni.ai.behavior_tree_gen.bridge.utils import (
    get_example_scene_context_files,
    get_extension_path,
    load_example_scene_config,
    resolve_example_scene_file_path,
)

# Change these inputs to match your environment.
ROOT_DIR = Path("Your/Output/Folder/Path") / "behavior_tree_gen_output"
OUTPUT_DIR = ROOT_DIR / "output"
API_KEY = "Your_NVIDIA_API_key"
SCENARIO = "Anna picks up the CardBox_A and places it on the Table."

async def run_planner_example():
    ext_path = get_extension_path()
    scene_config = load_example_scene_config("basic")
    context_files = get_example_scene_context_files("basic")

    if ext_path is None or scene_config is None:
        raise RuntimeError("Could not load the bundled example scene configuration.")
    if not API_KEY:
        raise RuntimeError("Set NVIDIA_API_KEY before running this example.")

    node_catalog_paths = []
    for path in (scene_config.get("node_catalogs") or {}).values():
        resolved_path = resolve_example_scene_file_path(path, ext_path=ext_path)
        if resolved_path:
            node_catalog_paths.append(resolved_path)

    metadata_schemas = scene_config.get("metadata_schemas", {})
    actor_schema_path = resolve_example_scene_file_path(
        metadata_schemas.get("actor"),
        ext_path=ext_path,
    )
    object_schema_path = resolve_example_scene_file_path(
        metadata_schemas.get("object"),
        ext_path=ext_path,
    )

    model_info = scene_config.get("model_info", {})
    model_selection_config_path = resolve_example_scene_file_path(
        model_info.get("model_selection_config"),
        ext_path=ext_path,
    )
    embedding_model_configs_path = resolve_example_scene_file_path(
        model_info.get("embedding_model_configs"),
        ext_path=ext_path,
    )
    named_model_configs_path = resolve_example_scene_file_path(
        model_info.get("model_configs"),
        ext_path=ext_path,
    )
    node_to_model_map_path = resolve_example_scene_file_path(
        model_info.get("node_to_model_map"),
        ext_path=ext_path,
    )

    session = core_api.setup_workspace(
        cache_dir=str(OUTPUT_DIR / "planner_cache"),
        output_dir=str(OUTPUT_DIR),
        context_data_paths=context_files["actors"] + context_files["objects"],
        node_catalog_paths=node_catalog_paths,
        actor_schema_path=actor_schema_path,
        object_schema_path=object_schema_path,
    )

    print(session.workspace_ready)
    print(session.actors_loaded, session.objects_loaded, session.nodes_loaded)

    runtime_result = await core_api.prepare_runtime(
        session,
        api_key=API_KEY,
        model_selection_config_path=model_selection_config_path,
        embedding_model_configs_path=embedding_model_configs_path,
        named_model_configs_path=named_model_configs_path,
        node_to_model_map_path=node_to_model_map_path,
    )

    if not runtime_result.success:
        raise RuntimeError(runtime_result.message)

    print(runtime_result.chat_model_name)
    print(runtime_result.retriever_ready, runtime_result.action_ir_ready)

    result = await core_api.generate_behavior_tree(
        session,
        SCENARIO,
    )

    if not result.success:
        raise RuntimeError(result.error_message)

    print(result.success)
    print(result.behavior_tree_folder_path)

asyncio.ensure_future(run_planner_example())
```

## Practical Notes

* `omni.ai.behavior_tree_gen.bridge` performs the same three calls automatically.
* `prepare_runtime(...)` must complete successfully before `generate_behavior_tree(...)` can
  work.
* `prepare_runtime(...)` can reuse compatible Action IR cached under `cache_dir`.
* If you need a simpler one-call helper for testing, the bridge also provides
  `omni.ai.behavior_tree_gen.bridge.test_pipeline.run(...)`.

On this page

* [Shared Example Setup](#shared-example-setup)
* [Step 1: setup\_workspace(â¦)](#step-1-setup-workspace)
* [Step 2: prepare\_runtime(â¦)](#step-2-prepare-runtime)
* [Step 3: generate\_behavior\_tree(â¦)](#step-3-generate-behavior-tree)
* [Async Execution Note](#async-execution-note)
* [Practical Notes](#practical-notes)

---

### BT Gen Tutorial

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/action_and_event_data_generation/tutorial_behavior_tree_gen.html

* [Synthetic Data Generation](../synthetic_data_generation/index.html)
* [Action and Event Data Generation](index.html)
* Behavior Tree Generation

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Behavior Tree Generation

The behavior tree generation workflow is packaged under the `omni.ai.behavior_tree_gen` namespace.
`omni.ai.behavior_tree_gen.bridge` provides the Kit UI, and
`omni.ai.behavior_tree_gen.core` provides the reusable scripted API that turns natural-language
scenarios into behavior tree outputs.

Before using this workflow, read [What Is Isaac Sim?](../index.html#isaac-sim-app-overview) to learn about
Isaac Sim and follow [Installation](../installation/index.html) to install Isaac Sim.

## Enable Extensions

1. Follow the [Omniverse Extension Manager guide](https://docs.omniverse.nvidia.com/extensions/latest/ext_core/ext_extension-manager.html)
   to enable `omni.ai.behavior_tree_gen.bridge`. The bridge loads
   `omni.ai.behavior_tree_gen.core` as a dependency.
2. Open **Behavior Tree Gen** from **Tools > Behavior Tree Gen**.
3. Optional: open the examples window from **Window > Examples > Behavior Tree Gen Examples** to
   load the bundled `simple` or `warehouse` scenes and prefill the main workflow window.

Note

The workflow expects scene context files, node catalogs, model configuration files, a writable
output directory, and a valid NVIDIA API key before a generation run can succeed.

## What the Bridge Does

`omni.ai.behavior_tree_gen.bridge` integrates the core pipeline with the Kit user experience.

* The **Behavior Tree Gen** window lets you review input files, set output and runtime options,
  enter a natural-language scenario, and run the pipeline.

* The examples window helps you load bundled demo stages, such as `simple` and `warehouse`.

* The bridge connects scene and cache data to the runtime so actor and object context, node
  catalogs, blackboard data, and model configuration files are available to the pipeline.
* The bridge tracks file snapshots so unchanged runs can reuse the loaded workspace and prepared
  runtime instead of rebuilding everything from scratch.

## Supported Workflows

Behavior tree generation supports both of the following workflows:

* **Interactive testing and demos** inside Kit, where you want a UI-driven workflow.
* **Scripted usage**, where the same flow is called directly from Python APIs.

## Workflow Overview

A typical UI session starts from the examples window or from manually selected input files. The
examples flow is the fastest way to begin because it loads a sample stage and pre-fills the
workflow panels, while manual usage lets you point the pipeline at your own context, catalog,
schema, and model configuration files.

After the inputs are available, use the **Behavior Tree Gen** window to review the loaded files,
choose the output location, provide a valid NVIDIA API key, and enter the natural-language scenario
that should be converted into behavior tree output.

For the full step-by-step UI flow, expected outputs, and example scenario, review
[Example Walkthrough](ext_behavior_tree_gen/example_walkthrough.html).

## Core API

`omni.ai.behavior_tree_gen.core` provides the reusable pipeline used by both the UI and Python
callers. Its public API intentionally exposes `setup_workspace(...)`,
`prepare_runtime(...)`, and `generate_behavior_tree(...)` for the same workflow used by the
bridge UI.

For a tutorial on authoring context files and metadata schemas, refer to
[Context Files and Metadata Schemas](ext_behavior_tree_gen/context_files_and_schemas.html).
For the full API sequence and script example, refer to
[Using the API Functions](ext_behavior_tree_gen/three_api_functions.html).

## Detailed Guides

For more detailed guidance on the workflow, schema-based context authoring, required inputs,
example usage, and API sequence, refer to the following pages:

* [Context Files and Metadata Schemas](ext_behavior_tree_gen/context_files_and_schemas.html)
* [Required inputs](ext_behavior_tree_gen/required_inputs.html)
* [Example Walkthrough](ext_behavior_tree_gen/example_walkthrough.html)
* [Using the API Functions](ext_behavior_tree_gen/three_api_functions.html)

## Terminology

omni.ai.behavior\_tree\_gen.bridge

The bridge extension provides the Kit and Omniverse user experience for behavior tree
generation. It exposes the UI windows, example loaders, and pipeline execution entry points
used by interactive workflows.

omni.ai.behavior\_tree\_gen.core

The core extension provides the reusable pipeline and public API used to prepare runtime state
and generate behavior tree output from natural-language scenarios.

PlannerSession

`PlannerSession` is the reusable workspace state returned by `setup_workspace(...)`. The
same session can be reused across runs when the tracked workflow inputs do not change.

On this page

* [Enable Extensions](#enable-extensions)
* [What the Bridge Does](#what-the-bridge-does)
* [Supported Workflows](#supported-workflows)
* [Workflow Overview](#workflow-overview)
* [Core API](#core-api)
* [Detailed Guides](#detailed-guides)
* [Terminology](#terminology)

---

