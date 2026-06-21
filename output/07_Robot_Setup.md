# 机器人配置工具与实战教程

> Robot Setup 工具链（Wizard/Poser/Inspector/GainTuner）+ 配置实战教程
> Isaac Sim 版本: 6.0
> 最后组装: 2026-06-21 14:14 UTC
> 来源页数: 32

---

## 来源链接

- [Robot Setup Index](https://docs.isaacsim.omniverse.nvidia.com/latest/robot_setup/index.html)
- [Assemble Robots](https://docs.isaacsim.omniverse.nvidia.com/latest/robot_setup/assemble_robots.html)
- [Asset Transformer](https://docs.isaacsim.omniverse.nvidia.com/latest/robot_setup/asset_transformer.html)
- [Asset Transformer API](https://docs.isaacsim.omniverse.nvidia.com/latest/robot_setup/asset_transformer_api.html)
- [Asset Transformer Rules](https://docs.isaacsim.omniverse.nvidia.com/latest/robot_setup/asset_transformer_rules.html)
- [Asset Transformer Tutorials](https://docs.isaacsim.omniverse.nvidia.com/latest/robot_setup/asset_transformer_tutorials.html)
- [Asset Validation](https://docs.isaacsim.omniverse.nvidia.com/latest/robot_setup/asset_validation.html)
- [Editing Tools](https://docs.isaacsim.omniverse.nvidia.com/latest/robot_setup/editing_tools.html)
- [Collision Detector](https://docs.isaacsim.omniverse.nvidia.com/latest/robot_setup/ext_isaacsim_robot_setup_collision_detector.html)
- [Gain Tuner](https://docs.isaacsim.omniverse.nvidia.com/latest/robot_setup/ext_isaacsim_robot_setup_gain_tuner.html)
- [Merge Mesh Utility](https://docs.isaacsim.omniverse.nvidia.com/latest/robot_setup/ext_isaacsim_util_merge_mesh.html)
- [Inspector Tools](https://docs.isaacsim.omniverse.nvidia.com/latest/robot_setup/inspector_tools.html)
- [Joint Inspector](https://docs.isaacsim.omniverse.nvidia.com/latest/robot_setup/joint_inspector.html)
- [Robot Inspector](https://docs.isaacsim.omniverse.nvidia.com/latest/robot_setup/robot_inspector.html)
- [Robot Poser](https://docs.isaacsim.omniverse.nvidia.com/latest/robot_setup/robot_poser.html)
- [Robot Wizard](https://docs.isaacsim.omniverse.nvidia.com/latest/robot_setup/robot_wizard.html)
- [Robot Wizard Tutorials](https://docs.isaacsim.omniverse.nvidia.com/latest/robot_setup/robot_wizard_tutorials.html)
- [Robot Setup Troubleshooting](https://docs.isaacsim.omniverse.nvidia.com/latest/robot_setup/troubleshooting.html)
- [Setup Tutorials Index](https://docs.isaacsim.omniverse.nvidia.com/latest/robot_setup_tutorials/index.html)
- [Joint Tuning](https://docs.isaacsim.omniverse.nvidia.com/latest/robot_setup_tutorials/joint_tuning.html)
- [Optimizing Asset](https://docs.isaacsim.omniverse.nvidia.com/latest/robot_setup_tutorials/optimizing_asset.html)
- [Rig Closed Loop Structures](https://docs.isaacsim.omniverse.nvidia.com/latest/robot_setup_tutorials/rig_closed_loop_structures.html)
- [Rig Mobile Robot](https://docs.isaacsim.omniverse.nvidia.com/latest/robot_setup_tutorials/rig_mobile_robot.html)
- [Configure Manipulator](https://docs.isaacsim.omniverse.nvidia.com/latest/robot_setup_tutorials/tutorial_configure_manipulator.html)
- [Generate Robot Config](https://docs.isaacsim.omniverse.nvidia.com/latest/robot_setup_tutorials/tutorial_generate_robot_config.html)
- [GUI Camera Sensors](https://docs.isaacsim.omniverse.nvidia.com/latest/robot_setup_tutorials/tutorial_gui_camera_sensors.html)
- [GUI Simple Robot](https://docs.isaacsim.omniverse.nvidia.com/latest/robot_setup_tutorials/tutorial_gui_simple_robot.html)
- [Import & Assemble Manipulator](https://docs.isaacsim.omniverse.nvidia.com/latest/robot_setup_tutorials/tutorial_import_assemble_manipulator.html)
- [Intro: Assemble Robot](https://docs.isaacsim.omniverse.nvidia.com/latest/robot_setup_tutorials/tutorial_intro_assemble_robot.html)
- [Intro: Environment Setup](https://docs.isaacsim.omniverse.nvidia.com/latest/robot_setup_tutorials/tutorial_intro_environment_setup.html)
- [Pick-Place Example](https://docs.isaacsim.omniverse.nvidia.com/latest/robot_setup_tutorials/tutorial_pickplace_example.html)
- [Rig Legged Robot](https://docs.isaacsim.omniverse.nvidia.com/latest/robot_setup_tutorials/tutorial_rig_legged_robot.html)

---


## Setup 概览

### Robot Setup Index

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/robot_setup/index.html

* Robot Setup

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Robot Setup

These tools and tutorials details the different importer and exporter for converting assets to and from the USD (Universal Scene Description) format and how you can build custom robots in the simulator.

## Tools

* [Robot Wizard [Deprecated]](robot_wizard.html)
* [Robot Wizard Tutorial [Deprecated]](robot_wizard_tutorials.html)
* [Robot Inspector Window](robot_inspector.html)
* [UI Utility Functions](robot_inspector.html#ui-utility-functions)
* [Masking Operations API](robot_inspector.html#masking-operations-api)
* [Robot Poser](robot_poser.html)
* [Robot Poser Window](robot_poser.html#robot-poser-window)
* [Named Pose Properties Panel](robot_poser.html#named-pose-properties-panel)
* [Example: Authoring Named Poses](robot_poser.html#example-authoring-named-poses)
* [Named Pose Schema Reference](robot_poser.html#named-pose-schema-reference)

* [Editor Tools](editing_tools.html)
  + [Mesh merge tool](ext_isaacsim_util_merge_mesh.html)
  + [Gain Tuner Extension](ext_isaacsim_robot_setup_gain_tuner.html)
  + [Robot Self-Collision Detector](ext_isaacsim_robot_setup_collision_detector.html)
  + [Robot Assembler](assemble_robots.html)
* [Inspector Tools](inspector_tools.html)
  + [Joint Inspector](joint_inspector.html)
  + [Physics Inspector](../physics/joint_inspector.html)
  + [Simulation Data Visualizer](../physics/ext_isaacsim_inspect_physics.html)

## Asset Structure

* [Asset Structure](asset_structure.html)
* [Asset Transformer](asset_transformer.html)
* [Asset Transformer API](asset_transformer_api.html)
* [Asset Transformer Rules Reference](asset_transformer_rules.html)

## Tutorials

* [Robot Setup Tutorials Series](../robot_setup_tutorials/index.html)
* [OpenUSD and Tuning Best Practices Tutorial Series](../openusd_tuning_tutorials/index.html)
* [Asset Transformer Tutorials](asset_transformer_tutorials.html)

## Troubleshooting

* [Robot Setup Troubleshooting](troubleshooting.html)

## Validation

* [Asset Validation](asset_validation.html)
* [IsaacSim.PhysicsRules](asset_validation.html#isaacsim-physicsrules)
* [IsaacSim.RobotRules](asset_validation.html#isaacsim-robotrules)
* [IsaacSim.SimReadyAssetRules](asset_validation.html#isaacsim-simreadyassetrules)
* [Running the Validation Rules](asset_validation.html#running-the-validation-rules)

On this page

* [Tools](#tools)
* [Asset Structure](#asset-structure)
* [Tutorials](#tutorials)
* [Troubleshooting](#troubleshooting)
* [Validation](#validation)

---

### Assemble Robots

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/robot_setup/assemble_robots.html

* [Robot Setup](index.html)
* [Editor Tools](editing_tools.html)
* Robot Assembler

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Robot Assembler

## Learning Objectives

This tutorial shows how to use the isaacsim.robot\_setup.assembler extension to assemble two USD assets into a single rigid body.
This tutorial will primarily demonstrate the use of the Robot Assembler UI tool. By the end of this tutorial, you will understand
the physical mechanics of assembled bodies, when to use the Robot Assembler,
and the current limitations with assembling rigid bodies in NVIDIA Isaac Sim.

*5-10 Minutes Tutorial*

## Getting Started

To find this tutorial of use, you must have two USD assets to assemble into one. This can include:

* A robot arm that needs to be attached to a gripper.
* A robot that needs to be fixed to a moving base.

The use of the word ‘robot’ here indicates a USD asset that Contains the [Robot Schema](../omniverse_usd/robot_schema.html#isaac-sim-robot-schema) Applied.

## Understanding the Mechanics of Assembled Bodies

The Robot Assembler tool allows you to combine two USD assets together by a physically simulated fixed joint. The result is a USD
asset that can be saved and loaded without needing to use the Robot Assembler each time. The fact that the fixed joint is physically
simulated is key in understanding proper application of the Robot Assembler extension. In Omniverse, physics is only simulated
while the timeline is playing. When physics is not active, the fixed joint will not have any effect. Only use the Robot Assembler to combine USD assets that are going to be moving while the timeline is playing. For example, a robot that is fixed in place
on a static table does not need to have a fixed joint connecting it to the table; you can place both the robot and the table
independently of each other and they will stay in place after the timeline is played.

Additionally, because two assembled assets are attached using a physically simulated fixed joint, the position of one asset relative to another
is resolved by a physics solver. This solution is easy if the assets are already placed correctly relative to each other while the timeline is
stopped, but you might experience instability if, on a stopped timeline, you move one part of an assembled asset far away from the other and
start the timeline.

## Using the Robot Assembler Tool

### Assembling Robots

The Robot Assembler UI tool can be found in the NVIDIA Isaac Sim toolbar by under **Tools > Robotics > Asset Editors > Robot Assembler**.

To use the Robot Assembler, start by loading the assets you want to assemble on the USD stage. There are two editing modes for the Robot Assembler. The workflow is the same for both modes, but the final result will be slightly different:

-**Direct Asset editing**: Open the robot that will serve as a base of the assembly directly, and add a reference to the components to be assembled. This will configure the attached component as a configuration option in the original asset.
-**Stage Editing**: Add both components to be assembled together as a reference to the stage. This will connect both components together at the current stage and will not modify the original assets.

With the **Robot Assembler** window open and both Robots available in the current stage, you can select a **Base Robot** and an **Attach Robot**.

Each robot has an “Attach Point” frame that can be used to specify the point on the robot that will be attached to the other robot. This attach point should be a [Robot Link](../omniverse_usd/robot_schema.html#isaac-sim-robot-schema-link-api) or a [Site](../omniverse_usd/robot_schema.html#isaac-sim-robot-schema-site-api).

The Assembler also expects an assembly namespace, which defaults to “Gripper”, but can be changed to any string. This namespace is used to identify the attachment point on the base robot when making the assembly directly on the base robot asset.

After selections are made, click on the **Begin Assembly** button to begin the assembly process. This will move the “Attach Robot” to the “Attach Point” of the “Base Robot”, and let you make any final adjustments to the transform. For convenience, a set of Buttons will be shown to allow you to rotate the “Attach Robot” around the X, Y, and Z axes, by increments of 90 degrees. You can also move it through the viewport gizmos however you choose. If you de-select the “attach robot”, the **Select Attach Point Prim** button will re-select it so you can manually move it to the desired position.

After you are happy with the transform, you can click on the **Assemble and Simulate** button to verify the assembly and check if the resulting robot is stable.

At any point, you can click on the **Cancel Assemble** button to undo the assembly and start over.

After assembly and simulation, you can click on the **End Simulation and Finish** button to save the assembly.

If the assembly is performed on the Base asset stage, the resulting assembly is saved as a configuration option under `configuration/<robot_name>_<assembly_namespace>_<attach_robot_name>.usd`, and the `<assembly_namespace>` will be used to create a Variant set on the robot interface layer, such that the new attachment can be selected for use wherever the base robot is used. While the configuration file is automatically saved, you must save the stage to keep the changes.

If the base robot is loaded as a reference, the attachment will be available on the open stage directly, without configuration through variants, and you can save the stage to keep the changes.

With the robot assembled, you might need to execute additional tests to verify simulation stability, given that the articulation system is changed. For a complete guide in tuning articulations, refer to [Articulation Stability Guide](https://docs.omniverse.nvidia.com/kit/docs/omni_physics/latest/dev_guide/guides/articulation_stability_guide.html).

## Robot Assembler API

The Robot Assembler can also be accessed by a Python API, where the assembly settings can be specified programmatically.

```python
import omni
from isaacsim.robot_setup.assembler import RobotAssembler

# Prerequisites: Have both the base robot and the attach robot loaded in the stage at the paths specified below (or change the paths to where the assets are loaded in your stage)

# Prim path to the base robot
robot_base = "/World/BaseRobot"
# Prim path to the mount point of the base robot
robot_base_mount = "/World/BaseRobot/Mount"
# Prim path to the attach robot
robot_attach = "/World/AttachRobot"
# Prim path to the mount point of the attach robot
robot_attach_mount = "/World/AttachRobot/Mount"
# Assembly namespace
assembly_namespace = "Gripper"
variant_name = "my_assembled_robot"

stage = omni.usd.get_context().get_stage()
assembler = RobotAssembler()

# Begin the Assembly process - Creates a session layer and attach it to the current stage, where all the modifications necessary for the assembly will be made.
assembler.begin_assembly(
    stage, robot_base, robot_base_mount, robot_attach, robot_attach_mount, assembly_namespace, variant_name
)

# Perform any Additional transformations on the Attach robot pose here directly through USD.

assembler.assemble()

# That's where the Robot Assembler will create the fixed joint between the two robots.
# It will also remove Physic's Articualtion Root from the attached robot, and disable the root joint that attaches 	robot to the world, if it exists.
# If you need to perform any physics simulation test - this is the time to do it.
# If the assembly is successful, and you are ready to finish the assembly, you can call the following function.
# Otherwise at any point you can call the `assembler.cancel_assemble()` function to cancel the assembly process.
# It will remove the session layer from the stage, undoing any changes made to the stage.

assembler.finish_assemble()

# This function will finish the assembly process by adding the attachment link to the parent robot joint and link lists, and then either merge the session layer into the current stage, or save a configuration file, and remove the session layer from the stage.
# If modifing a robot asset directly, it will also create the variant set to load the configuration for the assembled component through a payload.
```

## Summary

In this tutorial, you learned that:

1. The Robot Assembler tool exists to attach two robots or rigid bodies using a user-specified fixed joint.
2. The Robot Assembler creates a fixed joint that is physically simulated, and so it will only be active while the timeline is playing.
3. The Robot Assembler is only needed to attach Robot components together.
4. The Robot Assembler can also be accessed by a Python API that is demonstrated on the example code above.

On this page

* [Learning Objectives](#learning-objectives)
* [Getting Started](#getting-started)
* [Understanding the Mechanics of Assembled Bodies](#understanding-the-mechanics-of-assembled-bodies)
* [Using the Robot Assembler Tool](#using-the-robot-assembler-tool)
  + [Assembling Robots](#assembling-robots)
* [Robot Assembler API](#robot-assembler-api)
* [Summary](#summary)

---


## Setup 工具

### Asset Transformer

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/robot_setup/asset_transformer.html

* [Robot Setup](index.html)
* Asset Transformer

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Asset Transformer

The Asset Transformer is a framework for transforming USD assets in Isaac Sim. It provides utilities for batch transforms, schema routing, mesh deduplication, material optimization, and structural reorganization. The transformer operates through a rule-based pipeline where each rule performs a specific transformation on the USD stage, enabling complex multi-step asset optimization workflows.

The following sections explain the UI and functions behind each part of the Asset Transformer. To see the tool in action with step-by-step walkthroughs, refer to [Asset Transformer Tutorials](asset_transformer_tutorials.html#isaac-sim-app-asset-transformer-tutorials).

## Purpose

The Asset Transformer addresses key challenges when preparing assets for simulation:

* **Schema Separation**: Extracting physics, robot, and other API schemas into dedicated layers for modularity.
* **Performance Optimization**: Deduplicating geometries and materials to reduce memory usage and improve rendering performance.
* **Structural Reorganization**: Flattening complex hierarchies, routing variants, and creating standardized asset structures.
* **Composition Setup**: Generating interface layers with proper USD composition arcs (references, payloads, sublayers).

The result is a modular, simulation-ready asset structure that follows the [Isaac Sim Asset Structure](asset_structure.html#isaac-sim-app-reference-asset-structure) guidelines.

**Related Documentation**:

* [Asset Transformer Tutorials](asset_transformer_tutorials.html#isaac-sim-app-asset-transformer-tutorials) - Step-by-step practical walkthroughs
* [Asset Transformer Rules Reference](asset_transformer_rules.html#isaac-sim-app-asset-transformer-rules) - Complete reference of available transformation rules
* [Asset Transformer API](asset_transformer_api.html#isaac-sim-app-asset-transformer-api) - Programmatic usage and custom rule development

## Opening the Asset Transformer

The Asset Transformer UI is accessible from the menu bar: **Tools > Robotics > Asset Editors > Asset Transformer**.

## User Interface

The window contains three main sections described below. Each section controls a stage of the transformation workflow: selecting input, configuring actions, and executing the pipeline.

### Input Section

Configure the source asset and output location:

* **Active Stage / Pick File**: Choose between transforming the currently open stage or selecting a file from disk.
* **Output Directory**: Destination folder for the transformed asset package.
* **Load Restructured File**: Automatically open the output file after execution.

### Actions Section

Configure the transformation pipeline:

* **Load Preset**: Load a saved rule profile from a JSON file. Recent presets appear in a quick-access menu.
* **Save Preset**: Save the current configuration as a JSON preset file.
* **Clear All Actions**: Remove all rules from the action list.
* **Profile Settings** (collapsible): Configure profile metadata:

  + **Profile Name**: Display name for the profile
  + **Version**: Version string
  + **Interface Asset**: Output interface asset name
  + **Base Name**: Base stage filename
  + **Flatten Source**: Whether to flatten the source stage before processing
* **Action List**: Ordered list of rules to execute. Each action row shows:

  + Drag handle for reordering
  + Enable/disable checkbox
  + Expansion triangle to reveal configuration
  + Rule name
  + Remove button
* **Add Action**: Add a new rule to the pipeline. Review [Asset Transformer Rules Reference](asset_transformer_rules.html#isaac-sim-app-asset-transformer-rules) for available rules.

When an action is expanded, the following configuration options appear:

* **Rule Type**: Searchable dropdown to select the rule implementation. The dropdown lists each rule by its short class name in the **Rule Name** column and bundles rules by scope in the **Package** column.
* **Destination**: Output path for the rule (relative to package root).
* **Parameters**: Dynamic parameter editors generated from the rule’s configuration parameters.

Note

The **Rule Type** dropdown shows the short class name (for example, `SchemaRoutingRule`), while the documentation and saved profiles identify a rule by its *fully qualified type*. The fully qualified type combines the scope shown in the **Package** column with the class name: `isaacsim.asset.transformer.rules.<package>.<module>.<ClassName>`. For example, the **Rule Name** `SchemaRoutingRule` in the **Package** `core` corresponds to `isaacsim.asset.transformer.rules.core.schemas.SchemaRoutingRule`.

Use the filter icon next to the search field to show only rules from selected packages (`core`, `perf`, `structure`, `isaac_sim`). Refer to the [Asset Transformer Rules Reference](asset_transformer_rules.html#isaac-sim-app-asset-transformer-rules) for the fully qualified type of each rule.

### Execute Section

* **Execute Actions**: Run the transformation pipeline. The button is enabled when at least one action is enabled and an output directory is set.

## Transformer Manager Process

The `AssetTransformerManager` coordinates execution of a rule profile over USD stages.

**Process Flow**:

1. **Initialize**: Create an execution report to track results.
2. **Open Source Stage**: Load the input USD stage from the specified path.
3. **Create Base Copy**: Export the source stage to `{package_root}/payloads/{base_name}`. If `flatten_source` is enabled, the stage is flattened first.
4. **Collect External Assets**: Copy external assets (textures, materials) to `{package_root}/source_assets/` and update paths to local references.
5. **Execute Rules**: For each enabled rule in the profile:

   * Instantiate the rule with the working stage
   * Execute `process_rule()`
   * If the rule returns a new stage path, switch to that stage for subsequent rules
   * Collect operation logs and affected stages
6. **Save Working Stage**: Save any unsaved changes to the root layer.
7. **Return Report**: Generate an execution report with per-rule logs and status.

Note

The Asset Transformer is meant to be used with atomic assets (assets that are not composed of other assets, or with external references). If the asset is composed of other assets, or has external references, the Asset Transformer will collect the external assets and include them in the output package.

Example:

* Asset is composed of a base asset and a secondary asset (A robot and a Gripper or Sensor).
* The base asset is the atomic asset.
* The Asset Transformer will collect the referenced asset (Gripper or Sensor) and include it in the output package.
* The output package will contain the base asset, and the referenced asset on a single new atomic asset.
* If the secondary asset is loaded from a variant, it will be included in the variant structure of the new atomic asset.

## Rule Profiles

A rule profile defines a complete transformation pipeline. Profiles are stored as JSON files with the following structure:

```python
{
  "profile_name": "My Profile",
  "version": "1.0",
  "rules": [
    {
      "name": "Rule Display Name",
      "type": "fully.qualified.rule.ClassName",
      "destination": "output/path",
      "params": {
        "param_name": "value"
      },
      "enabled": true
    }
  ],
  "interface_asset_name": "asset",
  "output_package_root": "/path/to/output",
  "flatten_source": false,
  "base_name": "base.usd"
}
```

**Profile Fields**:

| Field | Description |
| --- | --- |
| `profile_name` | Display name for the profile (required) |
| `version` | Version string |
| `rules` | Ordered list of rule specifications |
| `interface_asset_name` | Output interface asset identifier |
| `output_package_root` | Default output directory |
| `flatten_source` | Flatten source stage before processing |
| `base_name` | Base stage filename |

**Rule Specification Fields**:

| Field | Description |
| --- | --- |
| `name` | Display name for the rule (required) |
| `type` | Fully qualified rule class name (required). Review [Asset Transformer Rules Reference](asset_transformer_rules.html#isaac-sim-app-asset-transformer-rules). |
| `destination` | Output path relative to package root |
| `params` | Dictionary of parameter overrides |
| `enabled` | Whether the rule is active |

### Managing Profiles

**Loading a Profile**:

1. Click the **Load Preset** button in the Actions section.
2. Select a preset from the recent presets menu, or choose **Browse…** to open a file picker.
3. The profile loads and populates the action list.

**Saving a Profile**:

1. Configure the desired rules and parameters.
2. Click the **Save Preset** button.
3. Choose a filename and location in the file picker.
4. The profile is saved as JSON and added to recent presets.

**Editing a Profile**:

1. Expand the **Profile Settings** frame to edit metadata.
2. Expand individual rules to modify their parameters.
3. Drag rules to reorder execution.
4. Use checkboxes to enable or disable rules.
5. Save the modified profile using **Save Preset**.

## Transform Report

The Asset Transformer generates a comprehensive execution report that documents every operation performed during the transformation process. This report is saved as `transform_report.json` in the output package root directory.

### Report Structure

The execution report contains the following information:

**Top-Level Fields**:

| Field | Description |
| --- | --- |
| `profile` | The complete profile configuration used for the transformation |
| `input_stage` | Path to the original input USD stage |
| `package_root` | Output directory where transformed assets are written |
| `started_at` | ISO 8601 timestamp when execution started |
| `finished_at` | ISO 8601 timestamp when execution completed |
| `results` | Array of per-rule execution results |
| `output_stage_path` | Path to the final transformed asset |

**Per-Rule Results**:

Each rule’s execution result includes:

| Field | Description |
| --- | --- |
| `rule` | The rule specification (name, type, parameters, enabled status) |
| `success` | Boolean indicating whether the rule completed successfully |
| `log` | Array of log entries recorded during rule execution |
| `affected_stages` | List of USD layer identifiers created or modified by the rule |
| `error` | Error message if the rule failed (null on success) |
| `started_at` | Timestamp when the rule started |
| `finished_at` | Timestamp when the rule completed |

Example Report

```python
{
  "profile": {
    "profile_name": "Isaac Sim Structure",
    "version": "1.0",
    "rules": ["...truncated..."]
  },
  "input_stage": "/path/to/robot.usd",
  "package_root": "/output/robot_package",
  "started_at": "2024-01-15T10:30:00.000Z",
  "finished_at": "2024-01-15T10:30:45.123Z",
  "output_stage_path": "/output/robot_package/robot.usda",
  "results": [
    {
      "rule": {
        "name": "Route Physics Schemas",
        "type": "isaacsim.asset.transformer.rules.core.schemas.SchemaRoutingRule",
        "destination": "payloads/Physics",
        "params": {"schemas": ["Physics*"], "stage_name": "physics.usda"},
        "enabled": true
      },
      "success": true,
      "log": [
        {"message": "SchemaRoutingRule start destination=payloads/Physics/physics.usda"},
        {"message": "Schema patterns: Physics*"},
        {"message": "Using schemas layer: /output/robot_package/payloads/Physics/physics.usda"},
        {"message": "Moved 3 schema(s) from /World/Robot: PhysicsArticulationRootAPI, PhysicsRigidBodyAPI, PhysicsMassAPI"},
        {"message": "Processed 15 prim(s), moved 42 schema instance(s)"},
        {"message": "SchemaRoutingRule completed"}
      ],
      "affected_stages": ["payloads/Physics/physics.usda"],
      "error": null,
      "started_at": "2024-01-15T10:30:05.000Z",
      "finished_at": "2024-01-15T10:30:08.500Z"
    }
  ]
}
```

### Using the Report

The transform report serves multiple purposes:

* **Debugging**: Identify the rule that failed and why it failed by examining log entries and error messages
* **Auditing**: Review exactly what transformations were applied to an asset
* **Verification**: Confirm that expected schemas, properties, or prims were routed to the correct layers
* **Automation**: Parse the report programmatically to validate the transformation results in CI/CD pipelines

For programmatic access to reports, refer to the [Asset Transformer API](asset_transformer_api.html#isaac-sim-app-asset-transformer-api).

## Isaac Sim Asset Structure Profile

Isaac Sim includes a default profile called **Isaac Sim Structure** that transforms assets into the recommended [Isaac Sim Asset Structure](asset_structure.html#isaac-sim-app-reference-asset-structure). This profile is automatically available in the recent presets menu.

The profile executes the following transformation pipeline:

1. **Route Variants**: Extract variant sets to separate files, excluding `none`, `default`, and `physx` variants.
2. **Flatten Base**: Create a flattened base stage with specific variant selections (for example, Physics: PhysX).
3. **Route Isaac Robot Schemas**: Move Isaac robot schemas (`IsaacRobotAPI`, `IsaacLinkAPI`, `IsaacJointAPI`) to `robot.usda`.
4. **Route Isaac Robot Properties**: Move Isaac robot properties to `robot.usda`.
5. **Route Geometries**: Deduplicate geometries and create instanceable references in `geometries.usd` and `instances.usda`.
6. **Fix Physics Joint Poses**: Correct physics joint local poses (`localPos0/1`, `localRot0/1`) that may have been invalidated by the geometry routing step combining parent/child transforms.
7. **Route Materials**: Deduplicate visual materials, download textures, and create `materials.usda`. Physics materials (those with `PhysicsMaterialAPI`) are left in the base layer.
8. **Route PhysX Schemas**: Move PhysX schemas to `Physics/physx.usda`.
9. **Route MuJoCo Schemas/Prims/Properties**: Move MuJoCo-related opinions to `Physics/mujoco.usda`.
10. **Route Physics Schemas/Prims**: Move general physics schemas and prims to `Physics/physics.usda`.
11. **Make Robot Schema**: Apply Isaac Sim robot schema and populate robot relationships.
12. **Make API Schemas Non-Explicit**: Convert explicit apiSchemas lists to prepended list ops.
13. **Generate Interface**: Create the final interface layer with:

    * Reference to the base layer
    * Variant sets generated from folder structure
    * Sublayer connections for physics engines (PhysX, MuJoCo)
    * Default variant selections
    * Recovery of extraneous root-level prims (e.g. `Render`, camera definitions) from the base layer into the interface layer so they remain reachable in the composed stage

**Output Structure**:

The resulting output follows the modular asset structure documented in [Asset Structure](asset_structure.html#isaac-sim-app-reference-asset-structure), with:

* Base geometry and hierarchy in `payloads/base.usd`
* Robot schema in `payloads/robot.usda`
* Deduplicated geometries in `payloads/geometries.usd`
* Materials and textures in `payloads/materials.usda` and `payloads/Textures/`
* Physics layers in `payloads/Physics/`
* Variant options in individual files
* Final composed asset in the interface layer

## Tutorials

[Asset Transformer Tutorials](asset_transformer_tutorials.html#isaac-sim-app-asset-transformer-tutorials)

On this page

* [Purpose](#purpose)
* [Opening the Asset Transformer](#opening-the-asset-transformer)
* [User Interface](#user-interface)
  + [Input Section](#input-section)
  + [Actions Section](#actions-section)
  + [Execute Section](#execute-section)
* [Transformer Manager Process](#transformer-manager-process)
* [Rule Profiles](#rule-profiles)
  + [Managing Profiles](#managing-profiles)
* [Transform Report](#transform-report)
  + [Report Structure](#report-structure)
  + [Using the Report](#using-the-report)
* [Isaac Sim Asset Structure Profile](#isaac-sim-asset-structure-profile)
* [Tutorials](#tutorials)

---

### Asset Transformer API

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/robot_setup/asset_transformer_api.html

* [Robot Setup](index.html)
* Asset Transformer API

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Asset Transformer API

This page covers programmatic usage of the Asset Transformer, including API classes, custom rule development, and integration patterns.

For UI-based usage, refer to [Asset Transformer](asset_transformer.html#isaac-sim-app-asset-transformer). For available rules, review [Asset Transformer Rules Reference](asset_transformer_rules.html#isaac-sim-app-asset-transformer-rules).

## Rule Interface

All transformation rules implement the `RuleInterface` abstract base class. This interface defines the contract for rule implementations:

```python
from abc import ABC, abstractmethod
from typing import Any

from pxr import Usd

class RuleInterface(ABC):
    def __init__(
        self,
        source_stage: Usd.Stage,
        package_root: str,
        destination_path: str,
        args: dict[str, Any],
    ) -> None: ...

    @abstractmethod
    def process_rule(self) -> str | None:
        """Execute the rule logic. Return a stage path to switch stages, or None."""
        ...

    @abstractmethod
    def get_configuration_parameters(self) -> list:
        """Return the configuration parameters for this rule."""
        ...

    def log_operation(self, message: str) -> None:
        """Append a message to the operation log."""
        ...

    def add_affected_stage(self, stage_identifier: str) -> None:
        """Record an identifier for a stage affected by this rule."""
        ...
```

**Key Methods**:

| Method | Description |
| --- | --- |
| `process_rule()` | Execute the rule logic. Return `None` to continue with the current working stage, or return a file path to switch the working stage for subsequent rules. |
| `get_configuration_parameters()` | Return a list of `RuleConfigurationParam` objects describing the rule’s configurable parameters. |
| `log_operation()` | Record human-readable log messages for the execution report. |
| `add_affected_stage()` | Record identifiers for stages or layers modified by the rule. |

### Rule Logging

Every rule implementation must provide adequate logging through the `log_operation()` method. This creates a detailed audit trail of transformations:

```python
def process_rule(self) -> str | None:
    self.log_operation("SchemaRoutingRule start destination=payloads/physics.usda")
    self.log_operation("Schema patterns: Physics*, Physx*")

    # ... processing ...

    self.log_operation("Moved 5 schema(s) from /World/Robot: PhysicsRigidBodyAPI, PhysicsMassAPI, ...")
    self.log_operation("Processed 12 prim(s), moved 24 schema instance(s)")
    self.log_operation("SchemaRoutingRule completed")
```

**Logging Best Practices**:

* Log the rule start with key configuration parameters
* Log pattern matches and filter criteria
* Log each significant operation (schema moves, property copies, prim transfers)
* Log summary statistics (counts of processed items)
* Log affected stages using `add_affected_stage()`
* Log completion status

## Rule Registration

The `RuleRegistry` is a singleton class that maintains a mapping of rule type names to their implementation classes. When the `AssetTransformerManager` executes a profile, it looks up each rule’s `type` string in the registry to find the corresponding implementation class.

The `RuleRegistry` uses a singleton pattern, meaning there is only one global instance shared across all code. This allows rules registered by any extension or module to be available to all transformation profiles.

**Registry Methods**:

| Method | Description |
| --- | --- |
| `register(rule_cls)` | Register a rule class. The key is computed as `{module}.{qualname}`. Raises `TypeError` if the class does not inherit from `RuleInterface`. |
| `get(rule_type)` | Look up a rule class by its fully qualified type name. Returns `None` if not found. |
| `list_rules()` | Return a dictionary mapping all registered type names to their implementation classes. |
| `list_rule_types()` | Return a sorted list of all registered rule type names. |
| `clear()` | Remove all registered rules. Primarily used for testing. |

## Creating Custom Rules

To create a custom transformation rule, implement the `RuleInterface` abstract base class and register it with the `RuleRegistry`.

Complete Custom Rule Example

```python
from isaacsim.asset.transformer import RuleConfigurationParam, RuleInterface, RuleRegistry
from pxr import Usd

class MyCustomRule(RuleInterface):
    """A custom transformation rule."""

    def get_configuration_parameters(self) -> list:
        return [
            RuleConfigurationParam(
                name="my_param",
                display_name="My Parameter",
                param_type=str,
                description="Description of the parameter",
                default_value="default_value",
            ),
            RuleConfigurationParam(
                name="scope",
                display_name="Scope",
                param_type=str,
                description="Root prim path to process",
                default_value="/",
            ),
        ]

    def process_rule(self) -> str | None:
        params = self.args.get("params", {}) or {}
        my_param = params.get("my_param", "default_value")
        scope = params.get("scope", "/")

        self.log_operation(f"MyCustomRule start my_param={my_param} scope={scope}")
        stage = self.source_stage

        scope_prim = stage.GetPrimAtPath(scope)
        if not scope_prim.IsValid():
            self.log_operation(f"Scope prim not found: {scope}")
            return None

        processed_count = 0
        for prim in Usd.PrimRange(scope_prim):
            processed_count += 1

        self.log_operation(f"Processed {processed_count} prim(s)")
        self.log_operation("MyCustomRule completed")
        self.add_affected_stage("my_output.usda")

        return None

registry = RuleRegistry()
registry.register(MyCustomRule)
```

**Referencing a Custom Rule in a Profile**:

The rule is registered using its fully qualified class name (`{module}.{class_name}`), which becomes the `type` string in rule specifications:

```python
from isaacsim.asset.transformer import RuleSpec

# type = fully qualified class name used when registering the rule
rule_spec = RuleSpec(
    name="My Custom Transformation",
    type="my_extension.rules.MyCustomRule",
    destination="payloads",
    params={"my_param": "custom_value", "scope": "/World/Robot"},
    enabled=True,
)
```

### Extension-Based Registration

For Isaac Sim extensions, register rules when the extension loads:

```python
import omni.ext
from isaacsim.asset.transformer import RuleRegistry

from .rules import AnotherRule, MyCustomRule

class MyExtension(omni.ext.IExt):
    def on_startup(self, ext_id):
        registry = RuleRegistry()
        registry.register(MyCustomRule)
        registry.register(AnotherRule)

    def on_shutdown(self):
        pass
```

## Programmatic API Usage

The Asset Transformer can be invoked programmatically using the Python API. This enables integration into automated pipelines, batch processing, and custom tooling.

### Basic Usage

```python
from isaacsim.asset.transformer import (
    AssetTransformerManager,
    RuleProfile,
    RuleSpec,
)

# input_stage = "/path/to/robot.usd"
# package_root = "/output/robot_package"

profile = RuleProfile(
    profile_name="My Transform Profile",
    version="1.0",
    rules=[
        RuleSpec(
            name="Route Physics Schemas",
            type="isaacsim.asset.transformer.rules.core.schemas.SchemaRoutingRule",
            destination="payloads/Physics",
            params={
                "schemas": ["Physics*", "Physx*"],
                "stage_name": "physics.usda",
            },
            enabled=True,
        ),
        RuleSpec(
            name="Route Materials",
            type="isaacsim.asset.transformer.rules.perf.materials.MaterialsRoutingRule",
            destination="payloads",
            params={
                "materials_layer": "materials.usda",
                "deduplicate": True,
            },
            enabled=True,
        ),
    ],
)

manager = AssetTransformerManager()
report = manager.run(
    input_stage=input_stage,
    profile=profile,
    package_root=package_root,
)

print(f"Transform completed: {report.output_stage_path}")
for result in report.results:
    status = "SUCCESS" if result.success else "FAILED"
    print(f"  {result.rule.name}: {status}")
    if result.error:
        print(f"    Error: {result.error}")
```

### Loading a Profile from JSON

```python
import json

from isaacsim.asset.transformer import AssetTransformerManager, RuleProfile

# profile_path = "/path/to/profile.json"
# input_stage = "/path/to/robot.usd"
# package_root = "/output/robot_package"

with open(profile_path, "r") as f:
    profile_data = json.load(f)

profile = RuleProfile.from_dict(profile_data)

manager = AssetTransformerManager()
report = manager.run(
    input_stage=input_stage,
    profile=profile,
    package_root=package_root,
)
```

### Saving the Execution Report

```python
import json

# report = manager.run(input_stage, profile, package_root)

report_path = f"{report.package_root}/transform_report.json"
with open(report_path, "w") as f:
    json.dump(report.to_dict(), f, indent=2)
```

### Accessing Rule Logs

```python
# report = manager.run(input_stage, profile, package_root)

# Iterate through rule results
for result in report.results:
    print(f"\n=== {result.rule.name} ===")
    print(f"Type: {result.rule.type}")
    print(f"Success: {result.success}")
    print(f"Duration: {result.started_at} to {result.finished_at}")
    print(f"Affected stages: {result.affected_stages}")

    print("Log:")
    for entry in result.log:
        print(f"  {entry['message']}")
```

### Querying Registered Rules

```python
from isaacsim.asset.transformer import RuleRegistry

registry = RuleRegistry()
rule_types = registry.list_rule_types()
for rule_type in rule_types:
    print(rule_type)

rule_cls = registry.get("isaacsim.asset.transformer.rules.core.schemas.SchemaRoutingRule")
if rule_cls:
    temp_rule = rule_cls.__new__(rule_cls)
    temp_rule._log = []
    params = temp_rule.get_configuration_parameters()
    for param in params:
        print(f"  {param.name}: {param.param_type.__name__} = {param.default_value}")
```

## API Classes Reference

| Class | Description |
| --- | --- |
| `AssetTransformerManager` | Coordinates execution of rule profiles over USD stages. Call `run()` to execute a transformation. |
| `RuleProfile` | Defines a complete transformation pipeline with profile metadata and ordered rule specifications. |
| `RuleSpec` | Specification for a single rule including name, type, destination, parameters, and enabled state. |
| `ExecutionReport` | Contains the results of a transformation run including per-rule logs, timestamps, and the output stage path. |
| `RuleExecutionResult` | Result of executing a single rule including success status, log entries, affected stages, and error information. |
| `RuleRegistry` | Singleton registry mapping rule type names to implementation classes. Rules are registered automatically when their extensions load. |
| `RuleInterface` | Abstract base class for all transformation rules. Implement this to create custom rules. |
| `RuleConfigurationParam` | Describes a configurable parameter for a rule, including name, type, default value, and description. |

## Error Handling

```python
from isaacsim.asset.transformer import AssetTransformerManager, RuleProfile

# input_stage, profile, package_root from your context

manager = AssetTransformerManager()

try:
    report = manager.run(input_stage, profile, package_root)
except RuntimeError as e:
    print(f"Transformation failed to start: {e}")
    raise

for result in report.results:
    if not result.success:
        print(f"Rule '{result.rule.name}' failed: {result.error}")
```

**Common Errors**:

| Error | Cause |
| --- | --- |
| `RuntimeError: Failed to open source stage` | The input USD file does not exist or is corrupted |
| `RuntimeError: Failed to export base stage` | Cannot write to the output directory (permissions, disk full) |
| `TypeError: rule_cls must subclass RuleInterface` | Attempting to register a class that does not inherit from `RuleInterface` |
| Rule `error` field populated | Exception raised during `process_rule()` execution |

On this page

* [Rule Interface](#rule-interface)
  + [Rule Logging](#rule-logging)
* [Rule Registration](#rule-registration)
* [Creating Custom Rules](#creating-custom-rules)
  + [Extension-Based Registration](#extension-based-registration)
* [Programmatic API Usage](#programmatic-api-usage)
  + [Basic Usage](#basic-usage)
  + [Loading a Profile from JSON](#loading-a-profile-from-json)
  + [Saving the Execution Report](#saving-the-execution-report)
  + [Accessing Rule Logs](#accessing-rule-logs)
  + [Querying Registered Rules](#querying-registered-rules)
* [API Classes Reference](#api-classes-reference)
* [Error Handling](#error-handling)

---

### Asset Transformer Rules

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/robot_setup/asset_transformer_rules.html

* [Robot Setup](index.html)
* Asset Transformer Rules Reference

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Asset Transformer Rules Reference

This page provides a reference of all available transformation rules for the Asset Transformer.

For general usage, refer to [Asset Transformer](asset_transformer.html#isaac-sim-app-asset-transformer). For API and custom rule development, refer to [Asset Transformer API](asset_transformer_api.html#isaac-sim-app-asset-transformer-api).

## Rules Overview

Rules are organized into four packages based on their function:

| Package | Rules | Purpose |
| --- | --- | --- |
| **Core Routing** | SchemaRoutingRule, PropertyRoutingRule, PrimRoutingRule, RemoveSchemaRule | Route USD opinions to dedicated layers |
| **Performance** | MaterialsRoutingRule, GeometriesRoutingRule | Optimize assets through deduplication and instancing |
| **Structure** | FlattenRule, VariantRoutingRule, InterfaceConnectionRule | Reorganize USD composition structure |
| **Isaac Sim** | RobotSchemaRule, MakeListsNonExplicitRule, PhysicsJointPoseFixRule, MergeMeshRule, MjcToPhysxConversionRule, UrdfToMjcPhysxConversionRule | Apply Isaac Sim-specific transformations |

Note

In the Asset Transformer UI, the **Rule Type** dropdown lists each rule by its short class name (for example, `SchemaRoutingRule`) and bundles rules by scope in the **Package** column. The scope token shown there maps to the categories on this page as follows: **Core Routing** to `core`, **Performance** to `perf`, **Structure** to `structure`, and **Isaac Sim** to `isaac_sim`. The **Fully Qualified Type** listed for each rule below is the value stored in profile JSON and passed to the API; the UI composes it from the selected scope and class name.

## Available Rules

Select a category tab to view available rules. Expand each rule for detailed parameters and execution logic.

Core Routing

These rules route USD opinions (schemas, properties, prims) from source layers to dedicated destination layers. The routing process preserves composition semantics by creating override opinions in the destination layer while removing the original opinions from source layers.

SchemaRoutingRule

Routes applied API schemas and their associated properties to a separate layer. This enables modular organization where physics schemas, robot schemas, or other API schemas can be selectively loaded.

**Fully Qualified Type**: `isaacsim.asset.transformer.rules.core.schemas.SchemaRoutingRule`

**Parameters**:

| Parameter | Type | Description |
| --- | --- | --- |
| `schemas` | list | List of API schema patterns to route. Supports wildcards (for example, `Physics*` matches `PhysicsRigidBodyAPI`, `PhysicsMassAPI`) |
| `ignore_schemas` | list | Schema patterns to exclude from routing. Overrides positive matches from `schemas`. |
| `stage_name` | str | Output USD filename (default: `schemas.usda`) |
| `prim_names` | list | Wildcard patterns to filter which prim names to process (default: `["*"]` matches all) |
| `ignore_prim_names` | list | Prim name patterns to exclude from processing |

**Execution Logic**:

1. **Schema Discovery**: Traverses all prims in the stage and collects applied API schemas matching the specified patterns.
2. **Property Namespace Resolution**: For each matched schema, determines the property namespace prefix (for example, `PhysicsRigidBodyAPI` uses `physics:` namespace, `PhysicsDriveAPI:angular` uses `drive:angular:`).
3. **Schema Transfer**: Uses USD’s `TokenListOp` to remove the schema token from the source layer’s `apiSchemas` metadata and prepend it to the destination layer.
4. **Property Transfer**: Copies all properties belonging to the schema namespace from the source layer to the destination layer using `Sdf.CopySpec`, then removes them from the source.
5. **Layer Management**: Sets the destination layer’s default prim to match the source and saves both layers.

PropertyRoutingRule

Routes properties matching name patterns to a separate layer. This allows organizing specific property namespaces (for example, physics properties, custom attributes) into modular layers.

**Fully Qualified Type**: `isaacsim.asset.transformer.rules.core.properties.PropertyRoutingRule`

**Parameters**:

| Parameter | Type | Description |
| --- | --- | --- |
| `properties` | list | Regular expression patterns to match property names (for example, `physics:.*` matches all physics namespace properties) |
| `ignore_properties` | list | Regex patterns to exclude from routing |
| `stage_name` | str | Output USD filename (default: `properties.usda`) |
| `scope` | str | Root prim path to limit the search scope (default: `/` searches entire stage) |
| `prim_names` | list | Wildcard patterns to filter which prim names to process |
| `ignore_prim_names` | list | Prim name patterns to exclude |

**Execution Logic**:

1. **Pattern Compilation**: Compiles the provided regex patterns for efficient matching.
2. **Property Discovery**: Iterates through all attributes and relationships on prims within the scope, checking names against the compiled patterns.
3. **Property Copy**: For each matching property, copies the spec from the strongest opinion in the prim stack to the destination layer using `Sdf.CopySpec`.
4. **Source Removal**: Removes the property spec from all source layers in the prim stack (except the destination layer) to prevent duplicate opinions.
5. **Layer Finalization**: Exports the destination layer and saves all modified source layers.

PrimRoutingRule

Routes entire prims matching type patterns to a separate layer. This enables organizing physics prims, render prims, or other typed prims into modular layers.

**Fully Qualified Type**: `isaacsim.asset.transformer.rules.core.prims.PrimRoutingRule`

**Parameters**:

| Parameter | Type | Description |
| --- | --- | --- |
| `prim_types` | list | Prim type patterns to route. Supports wildcards (for example, `Physics*` matches `PhysicsJoint`, `PhysicsScene`) |
| `ignore_prim_types` | list | Prim type patterns to exclude from routing |
| `stage_name` | str | Output USD filename (default: `prims.usda`) |
| `scope` | str | Root prim path to limit the search scope (default: `/`) |
| `prim_names` | list | Wildcard patterns to filter which prim names to process |
| `ignore_prim_names` | list | Prim name patterns to exclude |

**Execution Logic**:

1. **Type Matching**: Collects all prims within the scope whose type name matches the specified patterns using `fnmatch`.
2. **Composed Copy**: Copies the complete composed prim definition (including all properties, metadata, and applied schemas) to the destination layer.
3. **Complete Removal**: Removes the prim spec from all source layers, including explicitly deleting all property specs (to handle override properties authored by other rules like `SchemaRoutingRule`), clearing `apiSchemas` metadata, and deleting the prim spec from parent namespaces.
4. **Layer Management**: Exports the destination layer and saves modified source layers.

RemoveSchemaRule

Removes specific applied API schemas (and optionally their associated properties) from a target layer. Useful for stripping simulator-specific schemas when preparing an asset for a different physics backend.

**Fully Qualified Type**: `isaacsim.asset.transformer.rules.core.remove_schema.RemoveSchemaRule`

**Parameters**:

| Parameter | Type | Description |
| --- | --- | --- |
| `stage_name` | str | Target USD filename to edit (for example, `mujoco.usda`) |
| `schema_patterns` | list | Wildcard patterns matching API schema names to remove (for example, `PhysicsDriveAPI.*`) |
| `prim_path_patterns` | list | Regex patterns limiting which prim paths are affected (default: `[".*"]`) |
| `clear_properties` | bool | Also remove properties belonging to the matched schema namespaces (default: `False`) |

**Execution Logic**:

1. **Pattern Matching**: Iterates over all prims in the target layer, matching applied API schemas against the specified wildcard patterns.
2. **Schema Removal**: Removes matching schema tokens from each prim’s `apiSchemas` metadata using `TokenListOp` manipulation.
3. **Property Cleanup**: If `clear_properties` is enabled, removes all properties in the matched schema namespace from the prim spec.
4. **Layer Save**: Saves the modified layer.

Performance

These rules optimize assets for better simulation and rendering performance through deduplication and instancing.

MaterialsRoutingRule

Routes material prims to a shared layer with global deduplication, creates instanceable references at original locations, and transfers texture/MDL assets to a designated folder.

**Fully Qualified Type**: `isaacsim.asset.transformer.rules.perf.materials.MaterialsRoutingRule`

**Parameters**:

| Parameter | Type | Description |
| --- | --- | --- |
| `scope` | str | Root prim path to limit material search (default: `/`) |
| `materials_layer` | str | Output USD filename for the materials layer (default: `materials.usda`) |
| `textures_folder` | str | Folder name for texture assets relative to destination (default: `Textures`) |
| `deduplicate` | bool | Enable material deduplication based on content hash (default: `True`) |
| `download_textures` | bool | Download remote textures (for example, from Nucleus) to local folder (default: `False`) |

**Execution Logic**:

1. **Material Discovery**: Finds all material prims (`UsdShade.Material`) within the scope, tracking which layer defines each material. Materials with `PhysicsMaterialAPI` applied are skipped — these physics-specific materials remain in the base layer at their original paths so that `material:binding:physics` relationships continue to resolve.
2. **Asset Collection**: Resolves all texture and MDL file paths referenced by materials, handling both local and remote (Nucleus) assets. Parses MDL files to discover embedded texture references.
3. **Content Hashing**: Computes SHA-256 hashes of each material’s content (type, attributes, connections, relationships) using resolved asset paths for consistent deduplication.
4. **Asset Transfer**: Copies all unique assets to the textures folder with global deduplication. Handles filename collisions by appending numeric suffixes. Updates MDL files to point to transferred textures.
5. **Material Layer Creation**: Creates a `/Materials` scope in the materials layer. For each unique material (by hash), copies the material definition with updated asset paths.
6. **Instanceable References**: Updates each original material location with an instanceable reference to the deduplicated material in the materials layer.
7. **Binding Update**: Ensures `MaterialBindingAPI` is applied to all prims with material bindings.
8. **Cleanup**: Removes instanceable references for materials that are not bound to any surface.

GeometriesRoutingRule

Routes geometry prims to a shared layer with deduplication and creates a separate instances layer for per-instance overrides. Operates on a fully flattened stage (references and instances already resolved).

**Fully Qualified Type**: `isaacsim.asset.transformer.rules.perf.geometries.GeometriesRoutingRule`

**Parameters**:

| Parameter | Type | Description |
| --- | --- | --- |
| `scope` | str | Root prim path to limit geometry search (default: `/`) |
| `geometries_layer` | str | Output USD filename for base geometry definitions (default: `geometries.usd`) |
| `instance_layer` | str | Output USD filename for instance-specific overrides (default: `instances.usda`) |
| `deduplicate` | bool | Reuse identical geometry definitions (default: `True`) |
| `save_base_as_usda` | bool | Save the base stage as USD ASCII format (default: `True`) |
| `verbose` | bool | Log detailed transform decomposition information (default: `False`) |

**Execution Logic**:

1. **Geometry Discovery**: Identifies all geometry prims (Mesh, Gprim types) within the scope.
2. **Content Hashing**: Computes geometry hashes based on mesh data (points, face counts, indices), transforms, and intrinsic properties (type-specific attributes like `subdivisionScheme`, `orientation`).
3. **Intrinsic vs Instance Properties**: Separates intrinsic geometry properties (mesh data, UVs, normals, tangents) from instance-specific properties (visual material bindings, applied schemas like CollisionAPI, custom attributes). Physics-purpose material bindings (`material:binding:physics`) are preserved as-is in the instance delta, pointing to their original target paths in the base layer rather than being rerouted through `VisualMaterials`.
4. **Geometry Layer Creation**: Creates geometry definitions under `/Geometries/{name}/{name}` in the geometries layer. Identical geometries share the same definition.
5. **Instance Layer Creation**: Creates instance entries capturing per-instance deltas: material bindings, applied API schemas, transform overrides, and custom properties.
6. **Base Stage Update**: Updates the base stage to reference the geometry definitions, replacing original geometry prims with instanceable references.
7. **Delta Coalescing**: Groups instances with identical deltas to reduce redundancy in the instances layer.

Structure

These rules reorganize USD composition structure for modular asset organization.

FlattenRule

Flattens the original input stage into a single layer with optional variant selection. This creates a neutral base representation suitable for subsequent transformation rules.

**Fully Qualified Type**: `isaacsim.asset.transformer.rules.structure.flatten.FlattenRule`

**Parameters**:

| Parameter | Type | Description |
| --- | --- | --- |
| `output_path` | str | Relative output path within the destination (default: `base.usda`) |
| `clear_variants` | bool | Clear all variant selections before flattening to produce a neutral base (default: `True`) |
| `selected_variants` | dict | Dictionary mapping variant set names to variant selections. Only applies to variant sets on the default prim. Example: `{"Physics": "PhysX", "Gripper": "None"}` |
| `case_insensitive` | bool | Match variant names case-insensitively when applying selections (default: `True`) |

**Execution Logic**:

1. **Original Stage Access**: Opens the original input stage (before any processing) to preserve relative asset paths that would be broken after initial manager processing.
2. **Variant Selection Application**: If `selected_variants` is specified, applies the variant selections to the default prim’s variant sets. Case-insensitive matching finds variants like `physx` when `PhysX` is requested.
3. **Variant Clearing**: If `clear_variants` is enabled, iterates through all prims and clears their `variantSelections` metadata to ensure a neutral base.
4. **Stage Flattening**: Uses `Usd.Stage.Flatten()` to compose all layers, references, and payloads into a single layer.
5. **Export**: Exports the flattened layer to the destination path. Handles USD layer caching by transferring content to cached layers when necessary.
6. **Stage Switch**: Returns the output path so the manager switches subsequent rules to operate on the flattened stage.

VariantRoutingRule

Routes variant set contents to separate layer files. Each variant is extracted into an individual USDA file organized by variant set folder. Handles composition arcs within variants by copying source assets and remapping dependencies.

**Fully Qualified Type**: `isaacsim.asset.transformer.rules.structure.variants.VariantRoutingRule`

**Parameters**:

| Parameter | Type | Description |
| --- | --- | --- |
| `variant_sets` | list | Optional list of variant set names to process. If empty, all variant sets on the default prim are processed. |
| `case_insensitive` | bool | Convert variant option names to lowercase for output filenames and references (default: `True`) |
| `collect_dependencies` | bool | Collect external dependencies (referenced assets, textures) into a `dependencies` folder (default: `True`) |
| `excluded_variants` | list | Variant names to exclude from full processing. Excluded variants get empty USDA files created but contents are not processed. Useful for variants like `none`, `default`. |

**Execution Logic**:

1. **Variant Set Analysis**: Examines the default prim’s variant sets and builds a map of variant assets (payloads/references within each variant) to variant names.
2. **Variant File Mapping**: Creates a mapping from original variant asset paths to new output file paths (`{VariantSetName}/{variant_name}.usda`).
3. **Dependency Collection**: Uses `UsdUtils.ComputeAllDependencies` to discover all assets referenced by each variant’s source (sublayers, references, payloads, textures). Copies dependencies to a `dependencies` folder.
4. **Asset Copy with Remapping**: For variants with payloads/references, copies the source asset to the variant output file. Uses `UsdUtils.ModifyAssetPaths` to remap all internal paths to point to new variant files or collected dependencies.
5. **Delta Application**: Applies any direct overrides from the variant spec (attributes, relationships, child prims, composition arcs) as the strongest opinion on top of the copied content.
6. **Inter-Variant Remapping**: Updates references between variants to point to the new variant files. Remaps paths in collected dependencies to ensure consistency.
7. **Excluded Variant Handling**: Creates empty USDA files with just the default prim for excluded variants.

InterfaceConnectionRule

Generates the final interface layer with composition arcs to organize USD assets. Creates the top-level asset file that references/payloads the base asset and optionally generates variant sets from folder structure.

**Fully Qualified Type**: `isaacsim.asset.transformer.rules.structure.interface.InterfaceConnectionRule`

**Parameters**:

| Parameter | Type | Description |
| --- | --- | --- |
| `base_layer` | str | Relative path to the base USD layer to connect (default: `payloads/base.usda`) |
| `base_connection_type` | str | How to connect the base layer: `Reference` (default), `Payload`, or `Sublayer` |
| `generate_folder_variants` | bool | Generate variant sets from payloads folder structure (default: `False`). Each subfolder becomes a variant set, each USD file becomes a variant option. |
| `payloads_folder` | str | Folder to scan for variant set organization (default: `payloads`) |
| `connections` | list | List of custom connection specifications. Each spec is a dictionary with `asset_path` (layer to modify, empty for interface layer), `target_path` (layer to connect), and `connection_type` (`Reference`, `Payload`, `Sublayer`, or `Inherit`). |
| `default_variant_selections` | dict | Dictionary mapping variant set names to default variant selections. Unspecified variant sets default to `none`. |

**Execution Logic**:

1. **Interface Layer Creation**: Creates the interface layer at the package root, named after the original input asset.
2. **Default Prim Setup**: Ensures the default prim exists as an Xform in the interface layer.
3. **Base Connection**: Connects the base layer to the default prim using the specified connection type (prepends Reference or Payload to the prim’s list, or inserts Sublayer).
4. **Folder Variant Generation**: If enabled, scans the payloads folder for subfolders containing USD files. Each subfolder becomes a variant set, with a `none` variant (no payload) and variants for each USD file (payloaded).
5. **Custom Connections**: Applies custom connection specifications. For Sublayer connections, adds to the layer’s sublayer paths. For Reference/Payload connections, adds to the default prim. Can modify the interface layer or any specified asset layer.
6. **Extraneous Prim Recovery**: Scans the base layer for root-level prims outside `defaultPrim` (e.g. `/Render`, `/PhysicsScene`). Copies each into the interface layer at the same root level using `Sdf.CopySpec`, then removes them from the base layer and saves it. This keeps those prims reachable in the composed stage and makes the pipeline idempotent — prims that would not survive a reference-based round-trip are promoted to the interface layer where they persist across re-transforms.
7. **Variant Selection Defaults**: Sets default variant selections on the interface layer’s default prim.

Isaac Sim

These rules apply Isaac Sim-specific transformations for robot assets.

RobotSchemaRule

Applies the Isaac Sim robot schema to a target prim. Uses the robot schema utilities to detect articulation structure and populate robot relationships (links, joints, sites).

**Fully Qualified Type**: `isaacsim.asset.transformer.rules.isaac_sim.robot_schema.RobotSchemaRule`

**Parameters**:

| Parameter | Type | Description |
| --- | --- | --- |
| `prim_path` | str | Target prim path to apply the Robot schema. Defaults to the stage default prim if not specified. |
| `stage_name` | str | Output USD filename for robot schema opinions (default: `robot_schema.usda`) |
| `add_sites` | bool | Add sites to the robot by scanning child Xforms with no children under Link prims (default: `True`) |
| `sites_last` | bool | If `False`, sites are added after their parent link in the relationship order. If `True`, all sites are added at the end. (default: `False`) |
| `sublayer` | str | Optional sublayer path to include on the working stage prior to applying the robot schema. Useful for including physics layers that define joints. |

**Execution Logic**:

1. **Destination Layer Setup**: Creates or opens the destination layer for robot schema opinions. Adds it as a sublayer to the source stage.
2. **Sublayer Insertion**: If a sublayer is specified (e.g., physics layer), inserts it as the strongest sublayer on the source stage.
3. **Schema Detection**: Checks if `RobotAPI` is already applied to the target prim.
4. **Schema Application**:

   * **New Schema**: Applies `RobotAPI` to the target prim, then calls `PopulateRobotSchemaFromArticulation` to detect the articulation structure and populate `isaac:links`, `isaac:joints`, and optionally `isaac:sites` relationships.
   * **Existing Schema**: Calls `RecalculateRobotSchema` to update the schema while preserving existing relationship order. Removes invalid entries and appends newly discovered links/joints/sites.
5. **Schema Update**: Updates deprecated schema versions if necessary.
6. **Layer Isolation**: Saves the edit layer and discards any changes to the root layer (since edits are isolated to the robot schema layer).

MakeListsNonExplicitRule

Converts explicit list ops on prim metadata and properties to non-explicit list ops (prepended or appended). This is important for USD composition because explicit lists override all weaker opinions, while prepended/appended lists combine with weaker opinions.

**Fully Qualified Type**: `isaacsim.asset.transformer.rules.isaac_sim.make_lists_non_explicit.MakeListsNonExplicitRule`

**Parameters**:

| Parameter | Type | Description |
| --- | --- | --- |
| `metadata_names` | list | Prim metadata names to convert. Supports wildcards (for example, `api*` matches `apiSchemas`). |
| `property_names` | list | Prim property names to convert. Supports wildcards (for example, `material:*`). |
| `list_op_type` | str | Target list operation type: `prepend` (items go before weaker opinions) or `append` (items go after). Default: `prepend`. |

**Execution Logic**:

1. **Pattern Matching**: Uses `fnmatch` to match metadata and property names against the specified patterns.
2. **Metadata Conversion**: For matching prim metadata (like `apiSchemas`):

   * Extracts explicit items from the `TokenListOp`
   * Creates a new `TokenListOp` with items as prepended or appended (not explicit)
   * Sets the new list op on the prim spec
3. **Relationship Conversion**: For matching relationships:

   * Extracts explicit target paths from the `targetPathList`
   * Recreates the relationship spec (preserving other metadata like variability, custom flag)
   * Re-authors targets using `Prepend()` or `Append()` calls instead of explicit list
4. **Attribute Connection Conversion**: For matching attribute connections:

   * Extracts explicit connection paths
   * Clears the connection list and re-authors using `Prepend()` or `Append()`
5. **Layer Management**: Saves all modified layers.

PhysicsJointPoseFixRule

Corrects physics joint local poses after upstream rules (such as GeometriesRoutingRule) change body world transforms. Compares joint world poses computed from the original input asset against the current working stage and updates `localPos0/1` and `localRot0/1` attributes on any joint whose world pose has drifted.

**Fully Qualified Type**: `isaacsim.asset.transformer.rules.isaac_sim.physics_joint_pose_fix.PhysicsJointPoseFixRule`

**Parameters**:

| Parameter | Type | Description |
| --- | --- | --- |
| `original_composition_path` | str | Optional `Usd.Stage` object or explicit path to the original composition stage. Defaults to the `input_stage` passed by the transformer manager (the unmodified source asset). |
| `tolerance_position` | float | Maximum allowed position difference (Euclidean distance) when comparing joint world poses (default: `1e-6`) |
| `tolerance_orientation` | float | Minimum quaternion dot-product deviation from 1.0 when comparing joint world poses (default: `1e-6`) |

**Execution Logic**:

1. **Original Stage**: Opens the original input asset (before any transformer rules ran) via `input_stage`.
2. **Joint Discovery**: Traverses the working stage for all `UsdPhysics.Joint` prims.
3. **World Pose Comparison**: For each joint, computes the joint world pose from both `body0` and `body1` on the original stage and on the working stage using `local_pose * body_world_transform`.
4. **Drift Detection**: If the working stage’s joint world pose differs from the original beyond the configured tolerance, the affected body side is flagged for correction.
5. **Local Pose Fix**: Computes the corrective local pose as `joint_world_orig * inverse(body_world_entry)` and writes the resulting translation and rotation back to the joint’s `localPos` and `localRot` attributes.
6. **Layer Save**: Saves the modified edit layer if any corrections were applied.

MergeMeshRule

Merges visual mesh prims that share a common rigid-body parent using the Scene Optimizer merge operation. This reduces the number of geometry prims and can improve rendering and simulation performance.

**Fully Qualified Type**: `isaacsim.asset.transformer.rules.isaac_sim.merge_mesh.MergeMeshRule`

**Parameters**: None

**Execution Logic**:

1. **Rigid Body Discovery**: Traverses the stage for all prims with `RigidBodyAPI` applied.
2. **Mesh Grouping**: For each rigid body, collects child geometry prims (Mesh, Cube, Sphere, etc.) with `default` or `render` purpose, stopping at nested rigid body boundaries.
3. **Scene Optimizer Merge**: For each non-empty mesh group, invokes the Scene Optimizer `merge` command to combine the meshes into a single geometry prim while preserving material attributes.

MjcToPhysxConversionRule

Converts MJCF actuator and joint attributes to PhysX drive and joint schemas. This enables multi-physics engine support by translating MJCF gain/bias parameters into PhysX stiffness/damping.

**Fully Qualified Type**: `isaacsim.asset.transformer.rules.isaac_sim.mjc_to_physx_conversion.MjcToPhysxConversionRule`

**Parameters**: None

**Execution Logic**:

1. **Actuator Conversion**: For each `MjcActuator` prim, reads `gainPrm`, `biasPrm`, `gainType`, `biasType`, and `forceRange` attributes. Converts position-control (kp/kd) and velocity-control (kd) patterns to `DriveAPI` stiffness and damping.
2. **Joint Conversion**: For each revolute/prismatic joint, converts MJCF-specific attributes (`frictionloss` → `PhysxJointAPI.jointFriction`, `armature` → `PhysxJointAPI.armature`, `ref` → `DriveAPI.targetPosition`).

Mimic joints are left as `NewtonMimicAPI` on the joint prim and consumed directly by the runtime; no equivalent `PhysxMimicJointAPI` is authored.

UrdfToMjcPhysxConversionRule

Converts URDF joint attributes to both MJCF actuators and PhysX joint schemas. This is the multi-physics conversion step for URDF-imported assets that creates the dual-backend representation.

**Fully Qualified Type**: `isaacsim.asset.transformer.rules.isaac_sim.urdf_to_mjc_physx_conversion.UrdfToMjcPhysxConversionRule`

**Parameters**: None

**Execution Logic**:

1. **Physics Scope Creation**: Ensures a `Physics` scope exists under the default prim for actuator prims.
2. **URDF to PhysX Conversion**: For each revolute/prismatic joint, converts URDF attributes (`effort` → `DriveAPI.maxForce`, `velocity` → `PhysxJointAPI.maxJointVelocity`, `damping` → `DriveAPI.damping`, `friction` → `PhysxJointAPI.jointFriction`, `calibration` → `DriveAPI.targetPosition`).
3. **MjcActuator Creation**: Creates `MjcActuator` prims with `gainPrm`/`biasPrm` arrays derived from drive stiffness and damping for position or velocity control modes.
4. **PhysX to MJC Conversion**: Converts PhysX joint attributes back to MJCF attributes (`targetPosition` → `mjc:ref`, `jointFriction` → `mjc:frictionloss`, `armature` → `mjc:armature`).

Mimic joints are left as `NewtonMimicAPI` on the joint prim and consumed directly by the runtime; no equivalent `PhysxMimicJointAPI` is authored.

## Idempotency Requirement

All transformation rules **must** be idempotent: running the full profile twice on the same asset (once on the original, then on the first run’s output) must produce identical USD layers, with the sole exception of the `doc` metadata field which embeds absolute paths. The extension includes an idempotency test (`test_profile_idempotency.py`) that enforces this requirement.

Common sources of non-idempotency to watch for when developing new rules:

* **Floating-point drift** – Matrix composition/decomposition round-trips introduce noise. Quantize values to a fixed number of significant digits, or read canonical xformOp values directly when possible.
* **Stale composition arcs** – Extracting content from variant specs can leave behind self-referencing payloads or references on the destination prim. Strip any arcs that were not present in the source.
* **Inconsistent defaultPrim** – Use `self.source_stage.GetDefaultPrim()` (composed stage) rather than `self.source_stage.GetRootLayer().defaultPrim` (root layer only) to reliably resolve the default prim across re-transforms.
* **Non-deterministic merge decisions** – When deciding whether to merge a child into its parent, account for scaffolding prims (e.g. `VisualMaterials` scopes, empty overs) left behind by previous runs.
* **Extraneous root-level prims** – After flattening, root-level prims outside the `defaultPrim` hierarchy (e.g. viewport/render artifacts) do not survive a reference-based round-trip. The `InterfaceConnectionRule` handles this automatically by moving such prims from the base layer into the interface layer, but custom rules that introduce root-level prims should be aware of this composition constraint.

## Rule Type Quick Reference

Use these fully qualified type names in rule profiles:

```python
# Core Routing
isaacsim.asset.transformer.rules.core.schemas.SchemaRoutingRule
isaacsim.asset.transformer.rules.core.properties.PropertyRoutingRule
isaacsim.asset.transformer.rules.core.prims.PrimRoutingRule
isaacsim.asset.transformer.rules.core.remove_schema.RemoveSchemaRule

# Performance
isaacsim.asset.transformer.rules.perf.materials.MaterialsRoutingRule
isaacsim.asset.transformer.rules.perf.geometries.GeometriesRoutingRule

# Structure
isaacsim.asset.transformer.rules.structure.flatten.FlattenRule
isaacsim.asset.transformer.rules.structure.variants.VariantRoutingRule
isaacsim.asset.transformer.rules.structure.interface.InterfaceConnectionRule

# Isaac Sim
isaacsim.asset.transformer.rules.isaac_sim.robot_schema.RobotSchemaRule
isaacsim.asset.transformer.rules.isaac_sim.make_lists_non_explicit.MakeListsNonExplicitRule
isaacsim.asset.transformer.rules.isaac_sim.physics_joint_pose_fix.PhysicsJointPoseFixRule
isaacsim.asset.transformer.rules.isaac_sim.merge_mesh.MergeMeshRule
isaacsim.asset.transformer.rules.isaac_sim.mjc_to_physx_conversion.MjcToPhysxConversionRule
isaacsim.asset.transformer.rules.isaac_sim.urdf_to_mjc_physx_conversion.UrdfToMjcPhysxConversionRule
```

On this page

* [Rules Overview](#rules-overview)
* [Available Rules](#available-rules)
* [Idempotency Requirement](#idempotency-requirement)
* [Rule Type Quick Reference](#rule-type-quick-reference)

---

### Asset Transformer Tutorials

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/robot_setup/asset_transformer_tutorials.html

* [Robot Setup](index.html)
* Asset Transformer Tutorials

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Asset Transformer Tutorials

These tutorials walk through common Asset Transformer workflows step by step. Each tutorial builds on the previous one, so it is recommended to follow them in order.

For an in-depth explanation of the UI and concepts, refer to [Asset Transformer](asset_transformer.html#isaac-sim-app-asset-transformer).

Open the Asset Transformer from **Tools > Robotics > Asset Editors > Asset Transformer** before starting.

## Tutorial 1: Transform an Asset Using the Isaac Sim Structure Profile

This tutorial demonstrates how to transform a robot USD asset into the recommended Isaac Sim asset structure using the built-in **Isaac Sim Structure** profile.

### Prerequisites

* A robot USD asset loaded in the stage, or available on disk. This tutorial uses a sample robot from `Isaac/Robots/` in the Isaac Sim assets. For this tutorial, we will use the `Isaac/Robots/Fraunhofer/Evobot/evobot.usd` asset.

### Instructions

#### Select the Input Asset

1. In the **Input Section**, select **Active Stage** to transform the currently open stage, or select **Pick File** and browse to a robot USD file on disk.
2. Set the **Output Directory** to a writable folder where the transformed asset package will be saved (for example, `/tmp/my_robot_transformed/`).
3. Check **Load Restructured File** if you want the output file to open automatically after execution.

#### Load the Built-in Profile

1. In the **Actions Section**, click the **Load Preset** button.
2. From the recent presets menu, select **Isaac Sim Structure**.
3. The action list populates with all the rules defined in the Isaac Sim Structure profile.

1. Expand one or two rules in the action list to inspect their parameters. Each rule shows its **Rule Type**, **Destination**, and **Parameters**.

#### Execute the Transformation

1. Click **Execute Actions** in the Execute Section. The button is enabled when at least one action is enabled and an output directory is set.
2. Wait for the pipeline to complete. The console log displays progress for each rule.

#### Verify the Output

1. Since **Load Restructured File** was checked, the transformed asset opens automatically. Notice the loaded asset does not contain the ground plane anymore, as it was not in the default prim of the original robot asset. This is expected and desired.
2. Inspect the output folder structure. It should follow the [Isaac Sim Asset Structure](asset_structure.html#isaac-sim-app-reference-asset-structure):

```python
output_directory/
├── payloads/
│   ├── base.usd
│   ├── robot.usda
│   ├── geometries.usd
│   ├── instances.usda
│   ├── materials.usda
│   ├── Textures/
│   │   └── ...
│   └── Physics/
│       ├── physics.usda
│       ├── physx.usda
│       └── mujoco.usda
├── <asset_name>.usda          (interface layer)
└── transform_report.json
```

1. Inspect the robot prim structure, and verify that all meshes are now added through a reference, and the former looks scope is now empty, since all materials are now added to the materials.usda layer, and added through the meshes.
2. Inspect the default prim properties, and verify that there is a Variant set for the physics engine, with the physx variant selected.
3. Open `transform_report.json` to review per-rule execution logs and confirm all rules completed successfully.

## Tutorial 2: Creating a New Profile

This tutorial demonstrates how to build a custom transformation profile from scratch. The example profile routes physics schemas and materials into dedicated layers, a common workflow for assets that do not need the full Isaac Sim Structure treatment.

### Instructions

#### Clear the Action List

1. Click **Clear All Actions** to start with an empty pipeline.
2. Expand the **Profile Settings** frame and fill in the metadata:

   * **Profile Name**: `My Custom Profile`
   * **Version**: `1.0`
   * **Base Name**: `base.usd`
   * **Flatten Source**: Leave unchecked unless your source asset has complex sublayer composition you want to flatten first.

#### Add a Schema Routing Rule

1. Click **Add Action** to add a new rule to the pipeline.
2. Expand the new action and set:

   * **Rule Type**: Search for `SchemaRoutingRule` and select `isaacsim.asset.transformer.rules.core.schemas.SchemaRoutingRule`.
   * **Name**: `Route Physics Schemas`
   * **Destination**: `payloads/Physics`
   * **Parameters**:

     + `stage_name`: `physics.usda`
     + `schemas`: `["Physics*", "Newton*"]` (Click on the [+] button to add a new schema line per item in the list)

#### Add a Materials Routing Rule

1. Click **Add Action** again to add a second rule.
2. Expand it and set:

   * **Rule Type**: Search for `MaterialsRoutingRule` and select `isaacsim.asset.transformer.rules.perf.materials.MaterialsRoutingRule`.
   * **Name**: `Route Materials`
   * **Destination**: `payloads`
   * **Parameters**:

     + `materials_layer`: `materials.usda`
     + `textures_folder`: `Textures`
     + `deduplicate`: `true`
     + `download_textures`: `true`

#### Add a Geometry Deduplication Rule

1. Click **Add Action** one more time.
2. Expand and set:

   * **Rule Type**: Search for `GeometriesRoutingRule` and select `isaacsim.asset.transformer.rules.perf.geometries.GeometriesRoutingRule`.
   * **Name**: `Deduplicate Geometries`
   * **Destination**: `payloads`
   * **Parameters**:

     + `geometries_layer`: `geometries.usd`
     + `instance_layer`: `instances.usda`
     + `deduplicate`: `true`
     + `save_base_as_usda`: `true`

#### Review the Pipeline

The action list now contains three rules in order:

1. Route Physics Schemas
2. Route Materials
3. Deduplicate Geometries

Verify execution order is correct. Drag actions to reorder if needed. Use the checkboxes to disable individual rules during testing.

Note

Rule execution order matters. Rules execute sequentially and each rule operates on the working stage as modified by the previous rule. Place schema routing rules before material and geometry rules so that schemas are separated before deduplication occurs.

## Tutorial 3: Saving a Profile

After building the custom profile in [Tutorial 2](#asset-transformer-tutorial-create-profile), save it for reuse.

### Instructions

1. Verify the profile metadata by expanding the **Profile Settings** frame. Confirm the **Profile Name**, **Version**, and other fields are correct.
2. Click the **Save Preset** button in the Actions Section.
3. In the file picker, navigate to the desired save location and enter a filename (for example, `my_custom_profile.json`).
4. Click **Save**.

The profile is saved as a JSON file and added to the recent presets list for quick loading in the future.

Verify the saved file by opening it in a text editor. The structure matches the [Rule Profile format](asset_transformer.html#isaac-sim-app-asset-transformer):

```python
{
   "profile_name": "My Custom Profile",
   "version": "1.0",
   "rules": [
      {
         "name": "Route Physics Schemas",
         "type": "isaacsim.asset.transformer.rules.core.schemas.SchemaRoutingRule",
         "destination": "payloads/Physics",
         "params": {
         "schemas": [
            "Physics*",
            "Newton*"
         ],
         "ignore_schemas": [],
         "stage_name": "physics.usda",
         "prim_names": [
            ".*"
         ],
         "ignore_prim_names": []
         },
         "enabled": true
      },
      {
         "name": "Route Materials",
         "type": "isaacsim.asset.transformer.rules.perf.materials.MaterialsRoutingRule",
         "destination": "payloads",
         "params": {
         "scope": "/",
         "materials_layer": "materials.usda",
         "textures_folder": "Textures",
         "deduplicate": true,
         "download_textures": true
         },
         "enabled": true
      },
      {
         "name": "Deduplicate Geometries",
         "type": "isaacsim.asset.transformer.rules.perf.geometries.GeometriesRoutingRule",
         "destination": "payloads",
         "params": {
         "scope": "/",
         "geometries_layer": "geometries.usd",
         "instance_layer": "instances.usda",
         "deduplicate": true,
         "save_base_as_usda": true,
         "verbose": false
         },
         "enabled": true
      }
   ],
   "flatten_source": false,
   "base_name": "base.usd"
}
```

## Tutorial 4: Modifying a Rule Profile

This tutorial demonstrates how to load an existing profile, modify its rules and parameters, and re-save it. The example modifies the profile saved in [Tutorial 3](#asset-transformer-tutorial-save-profile) to add the Interface Connection Rule and change geometry deduplication settings.

### Instructions

#### Load the Existing Profile

1. Click **Load Preset** and select the `my_custom_profile.json` file saved previously. The action list populates with the three rules from Tutorial 3.

#### Add a New Rule

1. Click **Add Action** to add a fourth rule.
2. Expand it and set:

   * **Rule Type**: `Interface Connection Rule`
   * **Name**: `Connect Interfaces`
   * **Destination**: `payloads`
   * **Parameters**:

     + `Base Layer`: `payloads/base.usda`
     + `Base Connection Type`: `Reference`
     + `Generate Folder Variants`: `true`
     + `Payloads Folder`: `payloads`
     + `Custom Connections`: `[]`
     + `Default Variant Selections`: `{}`

#### Modify an Existing Rule

1. Expand the **Deduplicate Geometries** rule.
2. Change the `deduplicate` parameter from `true` to `false` to disable deduplication while keeping the geometry routing active.

#### Reorder the Rules

1. Drag the **Deduplicate Geometries** rule to the second position, so that it is executed before the **Route Materials** rule.

#### Disable a Rule

1. Uncheck the enable checkbox next to **Route Materials** to disable it without removing it from the pipeline. This is useful for iterating on specific transformations.

#### Update Profile Metadata

1. Expand **Profile Settings**.
2. Change the **Version** to `1.1` to track the modification.

#### Save the Modified Profile

1. Click **Save Preset**.
2. Overwrite the existing file or choose a new filename.

The final action list now contains four rules:

| # | Rule Name | Enabled | Change |
| --- | --- | --- | --- |
| 1 | Route Physics Schemas | Yes | (unchanged) |
| 2 | Deduplicate Geometries | Yes | (`deduplicate` set to `false`) |
| 3 | Route Materials | No | (disabled) |
| 4 | Connect Interfaces | Yes | (new rule added) |

## Tutorial 5: Adding an Asset Transform Pipeline Through Code

This tutorial demonstrates how to use the Asset Transformer API to run a transformation pipeline programmatically. This is useful for batch processing, CI/CD integration, or embedding asset transformation into custom extensions and workflows.

The code blocks below are taken from a single script, `docs/isaacsim/snippets/robot_setup/asset_transformer_tutorials.py`, which you can run as a standalone app (for example, to list registered rule types) using Isaac Sim’s `python.sh`.

### Load and Run a Saved Profile

The simplest approach is to load an existing profile JSON file and execute it against an input asset.

```python
import json

from isaacsim.asset.transformer import AssetTransformerManager, RuleProfile

# profile_path = "/path/to/my_custom_profile.json"
# input_stage = "/path/to/my_robot.usd"
# package_root = "/output/my_robot_package"
# Load a saved profile from disk
with open(profile_path, "r") as f:
    profile_data = json.load(f)

profile = RuleProfile.from_dict(profile_data)

# Create the manager and run the transformation
manager = AssetTransformerManager()
report = manager.run(
    input_stage=input_stage,
    profile=profile,
    package_root=package_root,
)

# Inspect results
print(f"Output asset: {report.output_stage_path}")
for result in report.results:
    status = "OK" if result.success else "FAILED"
    print(f"  [{status}] {result.rule.name}")
    if result.error:
        print(f"    Error: {result.error}")
```

### Build a Profile Programmatically

To define a profile entirely in code without a JSON file:

```python
from isaacsim.asset.transformer import (
    AssetTransformerManager,
    RuleProfile,
    RuleSpec,
)

# input_stage = "/path/to/my_robot.usd"
# package_root = "/output/my_robot_package"

profile = RuleProfile(
    profile_name="Code-Defined Profile",
    version="1.0",
    base_name="base.usd",
    flatten_source=False,
    rules=[
        RuleSpec(
            name="Route Physics Schemas",
            type="isaacsim.asset.transformer.rules.core.schemas.SchemaRoutingRule",
            destination="payloads/Physics",
            params={
                "stage_name": "physics.usda",
                "schemas": ["Physics*", "Newton*"],
            },
        ),
        RuleSpec(
            name="Route Materials",
            type="isaacsim.asset.transformer.rules.perf.materials.MaterialsRoutingRule",
            destination="payloads",
            params={
                "materials_layer": "materials.usda",
                "assets_folder": "Textures",
                "download_textures": True,
            },
        ),
        RuleSpec(
            name="Deduplicate Geometries",
            type="isaacsim.asset.transformer.rules.perf.geometries.GeometriesRoutingRule",
            destination="payloads",
            params={
                "geometries_layer": "geometries.usd",
                "instance_layer": "instances.usda",
                "deduplicate": True,
            },
        ),
    ],
)

manager = AssetTransformerManager()
report = manager.run(
    input_stage=input_stage,
    profile=profile,
    package_root=package_root,
)

print(f"Transformation complete: {report.output_stage_path}")
```

### Use the Isaac Sim Structure Profile in Code

To use the built-in Isaac Sim Structure profile programmatically, load it from the extension’s data directory:

```python
import json
from pathlib import Path

from isaacsim.asset.transformer import AssetTransformerManager, RuleProfile
from isaacsim.core.utils.extensions import get_extension_path_from_name

# input_stage = "/path/to/my_robot.usd"
# package_root = "/output/my_robot_isaacsim_structure"
# Locate the built-in profile shipped with the rules extension (use get_extension_path_from_name so the path is absolute)
ext_path = Path(get_extension_path_from_name("isaacsim.asset.transformer.rules"))
profile_path = ext_path / "data" / "isaacsim_structure.json"

with open(profile_path, "r") as f:
    profile = RuleProfile.from_dict(json.load(f))

manager = AssetTransformerManager()
report = manager.run(
    input_stage=input_stage,
    profile=profile,
    package_root=package_root,
)
```

### Batch-Process Multiple Assets

Combine the API with standard Python to transform multiple assets:

```python
import json
from pathlib import Path

from isaacsim.asset.transformer import AssetTransformerManager, RuleProfile

# profile_path = "/path/to/my_custom_profile.json"
# asset_paths = ["/assets/robot_a.usd", "/assets/robot_b.usd", "/assets/robot_c.usd"]
# output_base_dir = "/output"

with open(profile_path, "r") as f:
    profile = RuleProfile.from_dict(json.load(f))

manager = AssetTransformerManager()

for asset_path in asset_paths:
    asset_name = Path(asset_path).stem
    output_dir = f"{output_base_dir.rstrip('/')}/{asset_name}_transformed"

    report = manager.run(
        input_stage=asset_path,
        profile=profile,
        package_root=output_dir,
    )

    all_ok = all(r.success for r in report.results)
    print(f"{asset_name}: {'PASS' if all_ok else 'FAIL'} -> {report.output_stage_path}")
```

### Save and Inspect the Execution Report

The `ExecutionReport` returned by `manager.run()` can be serialized to JSON for logging or CI validation:

```python
import json
from pathlib import Path

# report = <ExecutionReport from manager.run() in any example above>
# After running the transformation (report from any example above)
report_path = Path(report.package_root) / "transform_report.json"
with open(report_path, "w") as f:
    json.dump(report.to_dict(), f, indent=2)

print(f"Report saved to: {report_path}")
```

### Discover Available Rule Types

To list all registered transformation rules at runtime:

```python
from isaacsim.asset.transformer import RuleRegistry

registry = RuleRegistry()
for rule_type in registry.list_rule_types():
    print(rule_type)
```

This prints all fully qualified rule class names that can be used in `RuleSpec.type`. Refer to [Asset Transformer Rules Reference](asset_transformer_rules.html#isaac-sim-app-asset-transformer-rules) for documentation on each rule.

On this page

* [Tutorial 1: Transform an Asset Using the Isaac Sim Structure Profile](#tutorial-1-transform-an-asset-using-the-isaac-sim-structure-profile)
  + [Prerequisites](#prerequisites)
  + [Instructions](#instructions)
    - [Select the Input Asset](#select-the-input-asset)
    - [Load the Built-in Profile](#load-the-built-in-profile)
    - [Execute the Transformation](#execute-the-transformation)
    - [Verify the Output](#verify-the-output)
* [Tutorial 2: Creating a New Profile](#tutorial-2-creating-a-new-profile)
  + [Instructions](#id1)
    - [Clear the Action List](#clear-the-action-list)
    - [Add a Schema Routing Rule](#add-a-schema-routing-rule)
    - [Add a Materials Routing Rule](#add-a-materials-routing-rule)
    - [Add a Geometry Deduplication Rule](#add-a-geometry-deduplication-rule)
    - [Review the Pipeline](#review-the-pipeline)
* [Tutorial 3: Saving a Profile](#tutorial-3-saving-a-profile)
  + [Instructions](#id2)
* [Tutorial 4: Modifying a Rule Profile](#tutorial-4-modifying-a-rule-profile)
  + [Instructions](#id3)
    - [Load the Existing Profile](#load-the-existing-profile)
    - [Add a New Rule](#add-a-new-rule)
    - [Modify an Existing Rule](#modify-an-existing-rule)
    - [Reorder the Rules](#reorder-the-rules)
    - [Disable a Rule](#disable-a-rule)
    - [Update Profile Metadata](#update-profile-metadata)
    - [Save the Modified Profile](#save-the-modified-profile)
* [Tutorial 5: Adding an Asset Transform Pipeline Through Code](#tutorial-5-adding-an-asset-transform-pipeline-through-code)
  + [Load and Run a Saved Profile](#load-and-run-a-saved-profile)
  + [Build a Profile Programmatically](#build-a-profile-programmatically)
  + [Use the Isaac Sim Structure Profile in Code](#use-the-isaac-sim-structure-profile-in-code)
  + [Batch-Process Multiple Assets](#batch-process-multiple-assets)
  + [Save and Inspect the Execution Report](#save-and-inspect-the-execution-report)
  + [Discover Available Rule Types](#discover-available-rule-types)

---

### Asset Validation

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/robot_setup/asset_validation.html

* [Robot Setup](index.html)
* Asset Validation

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Asset Validation

Isaac Sim comes with the [isaacsim.asset.validation](#isaac-sim-app-reference-asset-validation) extension that provides a set of validation rules to ensure that USD assets are properly configured for use in Isaac Sim.

While some of the rules are related to recommended guidelines, such as the [Asset Structure](asset_structure.html#isaac-sim-app-reference-asset-structure), many are fundamental for the asset to work properly in Isaac Sim.

This document provides a comprehensive overview of all validation rules available in the Isaac Sim Asset Validation extension. The rules are organized by their registration categories and help ensure that USD assets are properly configured for use in Isaac Sim.

The Isaac Sim asset validation comes enabled by default. If it is ever disabled, it can be re-enabled from the [Extension Manager](https://docs.omniverse.nvidia.com/extensions/latest/ext_core/ext_extension-manager.html "(in Omniverse Extensions)") by searching for `isaacsim.asset.validation`.

To open the **Asset Validation** window, navigate to **Window > Asset Validator**. For more information on the Asset Validation window, refer to [Asset Validator](https://docs.omniverse.nvidia.com/kit/docs/asset-validator/latest/index.html).

There are many validation rules available in the Asset validation window. You can choose to run all validation rules, but specifically for Isaac Sim, there are three categories of rules to review.

The Isaac Simvalidation rules are grouped into the following categories:

* IsaacSim.PhysicsRules
  :   + Fundamental rules related to physics simulation
* IsaacSim.RobotRules
  :   + Rules related to robot assets
* IsaacSim.SimReadyAssetRules
  :   + Rules related to sim ready assets

This document will go through each of the rules and provide a detailed explanation of what it checks.

# IsaacSim.PhysicsRules

Physics Validation Rules

| Rule Name | Description and Checks |
| --- | --- |
| **PhysicsJointHasDriveOrMimicAPI** | Validates that joints have a drive or mimic API.   * Non-fixed joints must have either a drive API or mimic API * Joints excluded from articulation are exempt from this requirement * When both drive and mimic APIs are present, drive stiffness and damping must be 0.0 |
| **PhysicsJointMaxVelocity** | Validates that joints have a positive max velocity set.   * Max joint velocity attribute is defined on joints with PhysxJointAPI * Max joint velocity value is greater than zero |
| **PhysicsDriveAndJointState** | Validates that joint drives have proper force limits and matching state values.   * Drive max force is defined and positive (not zero or infinite) * Drive target positions match joint state positions within tolerance (1e-2) * Drive target velocities match joint state velocities within tolerance (1e-2) |
| **DriveJointValueReasonable** | Validates that joint drive stiffness values are within reasonable ranges.   * Drive stiffness is within range (0.0 to 1,000,000.0) * Mimic joints have stiffness and damping set to 0.0 * Non-mimic joints have stiffness values defined * Maximum natural frequency warning threshold: 500.0 Hz |
| **JointHasCorrectTransformAndState** | Validates that joint transforms and states are consistent with the connected bodies.   * Joint position consistency between connected bodies * Joint orientation consistency between connected bodies * Joint state values match the robot pose configuration * Applies to revolute and prismatic joints |
| **JointHasJointStateAPI** | Validates that joints have the JointStateAPI applied.   * Prismatic joints have JointStateAPI with “linear” type * Revolute joints have JointStateAPI with “angular” type * Provides automatic fix suggestion to apply missing APIs |
| **MimicAPICheck** | Validates proper configuration of mimic joint APIs.   * Reference joint relationship has exactly one target * Gear ratio, natural frequency, and damping ratio are defined and non-zero * Joint limits are properly configured relative to reference joint limits * Limit compatibility based on gear ratio sign (positive/negative) |
| **RigidBodyHasMassAPI** | Validates that rigid bodies have properly configured mass properties.   * Rigid bodies have MassAPI applied * Mass attribute is authored and non-zero * Diagonal inertia is authored and non-zero * Principal axes are authored and normalized |
| **RigidBodyHasCollider** | Validates that enabled rigid bodies have collision geometry.   * Enabled rigid bodies have collision geometry in their hierarchy * Searches through prim range including instance proxies |
| **NonAdjacentCollisionMeshesDoNotClash** | Validates that non-adjacent collision meshes don’t intersect.   * Performs physics simulation to detect colliding pairs * Verifies that colliding bodies are connected by joints * Reports errors for non-adjacent colliding meshes |
| **InvisibleCollisionMeshHasPurposeGuide** | Validates that invisible collision meshes have purpose set to ‘guide’.   * Collision meshes with invisible visibility * Purpose attribute is set to ‘guide’ for invisible collision meshes |
| **HasArticulationRoot** | Validates that at least one prim in the stage has the ArticulationRootAPI.   * At least one prim in the stage has ArticulationRootAPI applied |

# IsaacSim.RobotRules

Robot Validation Rules

| Rule Name | Description and Checks |
| --- | --- |
| RobotNaming | Validates that robot assets follow the standard naming convention.   * Minimum folder nesting depth (at least 3 levels) * Folder name matches robot filename * Supports versioned folder structure: <Manufacturer>/<robot>/<robot.usd> or <Manufacturer>/<robot>/<version>/<robot.usd> |
| **CleanFolder** | Validates that robot asset folders don’t contain unexpected files.   * Robot asset folders only contain expected files * Warns about unexpected files in the asset directory |
| **NoOverrides** | Validates that prims don’t have overridden attributes.   * Prims don’t have overridden attributes (excluding /Render paths) * Detects attributes with authored values in layer stack * Only applies for the open stage |
| **RobotSchema** | Validates that robot assets have the required RobotAPI and relationships.   * Default prim is set on the stage * Default prim has RobotAPI applied * robotLinks relationship exists and has targets * robotJoints relationship exists and has targets |
| **JointsExist** | Validates that robot assets contain at least one joint.   * At least one prim in the stage has JointAPI applied |
| **LinksExist** | Validates that robot assets contain at least one link.   * At least one prim in the stage has LinkAPI applied |
| **ThumbnailExists** | Validates that robot assets have a thumbnail image.   * Thumbnail image exists at expected path: `<folder>/.thumbs/256x256/<filename>.png` |
| **CheckRobotRelationships** | Validates that robot relationships are properly defined and prepended.   * robotLinks and robotJoints relationships exist * Relationships are prepended for proper USD composition * Provides automatic fix suggestions for missing or non-prepended relationships |
| **VerifyRobotPhysicsAttributesSourceLayer** | Validates that physics attributes are authored in the physics layer.   * Physics attributes (starting with “physics:”) are authored in \_physics.usd layer * Warns when physics attributes are found in other layers |
| **VerifyRobotPhysicsSchemaSourceLayer** | Validates that physics schemas are applied in the physics layer.   * Physics schemas (starting with “Physx” or “Physics”) are applied in \_physics.usd layer * Warns when physics schemas are found in other layers |

# IsaacSim.SimReadyAssetRules

Sim Ready Asset Validation Rules

| Rule Name | Description and Checks |
| --- | --- |
| **NoNestedMaterials** | Validates that materials don’t contain nested materials.   * Material prims don’t contain child materials in their hierarchy * Warns about nested material configurations |
| **MaterialsOnTopLevelOnly** | Validates that materials are only defined in the top-level Looks prim.   * All materials are children of the top-level Looks prim * Materials are not scattered throughout the stage hierarchy * Skips materials in referenced/payload content |

# Running the Validation Rules

See video below for a demonstration of running the validation rules. We navigate to **Window > Asset Validator**, then select the **Isaac Sim** category rules. We can then select individual rules to run, but we chose to select all rules for each category.

kWidget.embed({
"targetId": "kaltura\_player\_1759965147",
"wid": "\_2935771",
"uiconf\_id": 56632652,
"flashvars": {},
"cache\_st": 1759965147,
"entry\_id": "1\_ty9ztcof"
});

On this page

* [Asset Validation](#)
* [IsaacSim.PhysicsRules](#isaacsim-physicsrules)
* [IsaacSim.RobotRules](#isaacsim-robotrules)
* [IsaacSim.SimReadyAssetRules](#isaacsim-simreadyassetrules)
* [Running the Validation Rules](#running-the-validation-rules)

---

### Editing Tools

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/robot_setup/editing_tools.html

* [Robot Setup](index.html)
* Editor Tools

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Editor Tools

* [Mesh merge tool](ext_isaacsim_util_merge_mesh.html)
* [Gain Tuner Extension](ext_isaacsim_robot_setup_gain_tuner.html)
* [Robot Self-Collision Detector](ext_isaacsim_robot_setup_collision_detector.html)
* [Robot Assembler](assemble_robots.html)

---

### Collision Detector

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/robot_setup/ext_isaacsim_robot_setup_collision_detector.html

* [Robot Setup](index.html)
* [Editor Tools](editing_tools.html)
* Robot Self-Collision Detector

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Robot Self-Collision Detector

## About

The [Robot Self-Collision Detector](#isaac-collision-detector) extension detects and manages self-collision pairs between the rigid body links of a robot articulation.
During physics simulation, pairs of colliders that overlap in their initial configuration generate unwanted contact forces that destabilize the robot.
This tool enumerates those pairs and lets you mark them as **Filtered Pairs** using the `UsdPhysics.FilteredPairsAPI`, so the physics engine ignores contact between them.

To access this extension, go to the top menu bar and click **Tools > Robotics > Asset Editors > Robot Self-Collision Detector**.
This extension is enabled by default. If it is ever disabled, it can be re-enabled from the [Extension Manager](https://docs.omniverse.nvidia.com/extensions/latest/ext_core/ext_extension-manager.html "(in Omniverse Extensions)")
by searching for `isaacsim.robot_setup.collision_detector`.

### When to Use

Use this tool after importing or authoring a robot asset whose collision meshes overlap at rest.
Common scenarios include:

* Newly imported URDF/MJCF robots that have adjacent-link colliders intersecting at joint boundaries.
* Robots with dense collision geometry (e.g. dexterous hands) where many links are in close proximity.
* Adding collision filtering as a physics feature layer on an existing asset following the [asset structure guidelines](asset_structure.html#isaac-sim-app-reference-asset-structure).

## User Interface

### Robot Selection

* **Robot dropdown**: Lists all prims on the stage that have the Robot Schema applied. Select the robot you want to inspect.
* **Check Collisions button**: Runs collision detection on the selected robot and populates the results table.

### Options

* **Include environment collisions**: When enabled, the results also include collision pairs between robot links and non-robot bodies in the scene (e.g. a table or ground plane).

### Collision Pairs Table

The table has three columns:

| Column | Content | Description |
| --- | --- | --- |
| **Rigid Body A** | Color swatch + link name | First body in the collision pair. Click the focal icon to select its collision prims in the Stage window. |
| **Rigid Body B** | Color swatch + link name | Second body in the collision pair. Same focal-icon behavior. |
| **Filtered Pair** | Checkbox | Toggle on to add a `FilteredPairsAPI` relationship so the physics engine ignores this contact. Toggle off to remove it. |

Additional table interactions:

* **Search bar**: Filter rows by body name (case-insensitive).
* **Column sorting**: Click the header sort icon to toggle alphabetical ordering.
* **Row selection**: Click a row to highlight both bodies in the viewport with distinct colors, making it easy to visually locate the pair. Clicking elsewhere in the viewport clears the table selection.
* **Keyboard navigation**: Press `Ctrl+Up` / `Ctrl+Down` to move the row selection up or down. When multiple rows are selected the entire block shifts together.
* **Batch toggle**: Select multiple rows and toggle one checkbox to apply the same filtered state to all selected pairs.
* **No collisions**: When no self-collisions are detected an overlay message is shown in place of the table.

### Viewport Highlighting

When a collision pair row is selected, the two rigid bodies are highlighted in the viewport using distinct colors from a 64-color palette. Each body receives a colored selection-group outline so you can distinguish them at a glance. If the viewport selection outline setting is disabled, the panel temporarily enables it for the duration of the selection and restores the original setting when the selection is cleared, the panel is hidden, or the extension shuts down.

## Example Usage: Unitree Dex5 Hand

This walkthrough uses the **Isaac/Robots/Unitree/Dex5/Dex5-URDF-R.usda** asset from the Isaac Sim asset library.

### 1. Open the Robot Asset

Open or reference the Dex5 hand asset onto your stage:

**File > Open** or drag it from the Content Browser at `Isaac/Robots/Unitree/Dex5/Dex5-URDF-R.usda`.

### 2. Open the Self-Collision Detector

Navigate to **Tools > Robotics > Asset Editors > Robot Self-Collision Detector**.

The panel opens docked at the bottom-left of the editor, adjacent to the Content window.

### 3. Select the Robot and Detect Collisions

The robot dropdown auto-populates with every prim on the stage that has the Robot Schema applied. It automatically selects the first robot on the stage, and checks collisions. If you made modifications to the robot, click **Check Collisions** to update the results.

The tool queries the physics engine for all collider pairs that overlap in the robot’s current configuration, maps each collider to its owning rigid body link, and populates the table.

### 4. Inspect a Collision Pair

Click a row to highlight both bodies in the viewport. Each body is drawn with a unique color so you can visually confirm whether the overlap is expected (e.g. adjacent finger segments) or unintended.

Click the **focal icon** (crosshair) next to a body name to select only that body in the viewport and the Stage window. The table row is selected (or kept selected if it already was), but only the clicked body receives the colored outline, making it easy to isolate one side of the pair. Clicking the focal icon on the other body in the same row switches the viewport highlight without changing the selected row.

### 5. Filter Collision Pairs

For each pair that should be ignored by the physics engine, check the **Filtered Pair** checkbox. This writes a `UsdPhysics.FilteredPairsAPI` relationship to the stage.

To filter multiple pairs at once, select the desired rows (hold `Ctrl` or `Shift` while clicking), then toggle one checkbox. All selected rows are updated together.

Note

Other ways to resolve for the collision pairs are to adjust the collision geometry, or modify the robot starting pose using the [Robot Poser](robot_poser.html#isaac-sim-robot-poser) extension. Filtered pairs are displayed in the self-collision detector, so you can easily see which pairs are being ignored, but whenever a pair is not filtered nor is detected by the collision engine, it will not be displayed in the self-collision detector. When the robot has the self-collision disabled in the articulation root, no collision pairs will be detected by the collision engine, and a message will be displayed on the table.

### 6. Inspect Multiple Collision Pairs

You can select multiple rows to highlight multiple pairs in the viewport. Hold `Ctrl` or `Shift` while clicking to select multiple rows.
To quickly move the selection up or down, press `Ctrl+Up` or `Ctrl+Down`.

## Further Learning

* [Asset Structure](asset_structure.html#isaac-sim-app-reference-asset-structure) for the recommended robot asset layering structure.
* [UsdPhysics.FilteredPairsAPI](https://openusd.org/release/api/class_usd_physics_filtered_pairs_a_p_i.html) reference in the OpenUSD documentation.
* [Robot Schema](../omniverse_usd/robot_schema.html#isaac-sim-robot-schema) for details on the Robot Schema used to identify robots on stage.

On this page

* [About](#about)
  + [When to Use](#when-to-use)
* [User Interface](#user-interface)
  + [Robot Selection](#robot-selection)
  + [Options](#options)
  + [Collision Pairs Table](#collision-pairs-table)
  + [Viewport Highlighting](#viewport-highlighting)
* [Example Usage: Unitree Dex5 Hand](#example-usage-unitree-dex5-hand)
  + [1. Open the Robot Asset](#open-the-robot-asset)
  + [2. Open the Self-Collision Detector](#open-the-self-collision-detector)
  + [3. Select the Robot and Detect Collisions](#select-the-robot-and-detect-collisions)
  + [4. Inspect a Collision Pair](#inspect-a-collision-pair)
  + [5. Filter Collision Pairs](#filter-collision-pairs)
  + [6. Inspect Multiple Collision Pairs](#inspect-multiple-collision-pairs)
* [Further Learning](#further-learning)

---

### Gain Tuner

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/robot_setup/ext_isaacsim_robot_setup_gain_tuner.html

* [Robot Setup](index.html)
* [Editor Tools](editing_tools.html)
* Gain Tuner Extension

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Gain Tuner Extension

The Gain Tuner tunes the stiffness and damping gains of a selected Articulation. Use it when importing a new robot or when fine-tuning the gains of an existing one.

This extension is enabled by default. If it is ever disabled, re-enable it from the [Extension Manager](https://docs.omniverse.nvidia.com/extensions/latest/ext_core/ext_extension-manager.html "(in Omniverse Extensions)") by searching for `isaacsim.robot_setup.gain_tuner`. To open it, go to **Tools** > **Robotics** > **Asset Editors** > **Gain Tuner**. Robots on the stage that have the [Robot Schema](../omniverse_usd/robot_schema.html#isaac-sim-robot-schema) applied automatically appear in the **Select Robot** dropdown.

For a hands-on walkthrough that uses the UR10 manipulator, see the [Tutorial 11: Tuning Joint Drive Gains](../robot_setup_tutorials/joint_tuning.html#isaac-sim-app-tutorial-advanced-joint-tuning) tutorial.

## Overview

The purpose of the Gain Tuner is to find a pair of stiffness and damping gains for each robot joint so that the robot is able to follow commanded trajectories according to the robot’s expected behavior.

The Gain Tuner offers a set of tests that allow you to quickly assess the quality of the current set of gains and a utility for tuning gains manually.

* **Tuning Gains**: A utility for tuning the gains for the robot.
* **Gains Tests**: A suite of tests for evaluating joint behavior:

  + *Snap-to-Limits* — commands joints to their lower and upper limits to verify they can reach their full range of motion.
  + *Sinusoidal* — drives joints with continuous sinusoidal trajectories.
  + *Step Function* — drives joints with step-function trajectories.
  + *Stress Test* — drives joints with extreme random commands to surface instabilities that can appear during reinforcement learning training.
* **Test Results**: A plot of the results of the gains tests on the tracked joint positions and velocities, compared against the commanded trajectory.

### Understanding Joint Drives

Joint Drives are dual-proportional controllers used to set a joint to a given target. One proportional gain is moderating the error in position, while the other gain is moderating the error in velocity. For historical reasons, these gains are called Stiffness and Damping, respectively.

Note

These Joint drives are *implicit* - meaning the position and velocity constraints are imposed by the drive with respect to the current time-step. In engineering this is typically done where it uses a closed loop control with readings of the previous time-step of position and velocity and reacting to it for future control. Refer to [Articulation Joint Drives](https://nvidia-omniverse.github.io/PhysX/physx/5.3.0/docs/Articulations.html#articulation-joint-drives).

**Stiffness** is similar to a spring stiffness constant multiplying the error in position, as if the spring was stretched by that amount. **Damping** comes from the effect of targeting zero velocity and therefore any movement would result in a reaction that attempts to stop it. You can actually have it track a velocity that is different than zero and the effect is the same as stiffness would be in position.

\[\tau = \text{stiffness} \* (q - q\_{\text{target}}) + \text{damping} \* (\dot{q} - \dot{q}\_{\text{target}})\]

where \(q\) and \(\dot{q}\) are the joint position and velocity, respectively. When \(\dot{q}\_{target} = 0\), the system reduces to a conventional PD controller on the joint position.

This formula applies for both revolute and prismatic joints.

The joint max force will act as a clamp for \(\tau\), and finally, the drive type will dictate if the effort will be applied directly as a torque or force, or if it will be converted into an acceleration applied to the bodies connected to the joint.

#### Drive Modes

This dual-proportional controller provides two main ways to control the robot:

> * **Position target** - used for controlled joints that are driven by defining a target distance/angle that the connected bodies should be.
> * **Velocity target** - usually done for wheels or other free-spinning objects.

To have a position-controlled joint: set Stiffness to something greater than zero and Damping can be any value.
To have a velocity-controlled joint: set Stiffness to zero and Damping to any value greater than zero.

## Tools

### Tuning Gains

The Joint Gains are a pair of Stiffness and Damping values that are used to drive the joint. They are applied to the joint in the form of a drive that applies an effort (Force/Torque) to the joint, based on the error between the desired position and velocity or both. This Effort is computed as:

\[Effort = K\_p \* (Position\_{Desired} - Position\_{Current}) + K\_d \* (Velocity\_{Desired} - Velocity\_{Current})\]

Where \(K\_p\) is the Stiffness and \(K\_d\) is the Damping.

From this formula, you can describe the different modes of the joint drive:

* Position Drive: When the joint drive is in position mode, the desired position is the target position. This requires the stiffness to be greater than `0`, and the damping to be any value.
* Velocity Drive: When the joint drive is in velocity mode, the desired position is the current position, and the desired velocity is the target velocity. This requires the stiffness to be `0` and the damping to be any value.
* None: When the joint drive is in none mode, the joint drive is not active. The joint can still be controlled by applying a direct effort. This requires the stiffness to be `0` and the damping to be `0`.
* Mimic: When the joint drive is in mimic mode, the joint drive is driven by the mimic joint. This means that the joint drive will not be active, but the mimic joint’s attributes of Natural Frequency and Damping Ratio can still be configured through the Tuner.

This Dampener-Spring model can also be described in terms of the natural frequency and damping ratio:

\[ \begin{align}\begin{aligned}\omega\_n = \sqrt{\frac{K\_p}{m}}\\\zeta = \frac{K\_d}{2 m \omega\_n}\end{aligned}\end{align} \]

Where \(\omega\_n\) is the natural frequency and \(\zeta\) is the damping ratio, and \(m\) is the computed joint inertia based on the mass of the robot at both sides of the joint. The damping ratio is such that \(\zeta = 1.0\) is a critically damped system, \(\zeta < 1.0\) is underdamped, and \(\zeta > 1.0\) is overdamped.

From the above formula, observe that there are two ways to Tune Gains:

* Directly editing Stiffness and Damping values: On the joints table, you can directly edit the Stiffness and Damping values for each joint.
* Natural Frequency: The Gain tuner can also automatically compute the Stiffness and Damping values for each joint based on the desired natural frequency and damping ratio.

Note

Because the robot is a structure that is made of multiple links and moving joints, the natural frequency of each joint is dependent on the robot’s configuration. To establish a standard, the natural frequency of the robot at its home configuration is used.

#### Tuning Options

In the Tuning Options, you can select the tuning mode between Stiffness and Natural Frequency. On the joints table, observe the following options:

* **Mode**: The mode of the joint drive (Position, Velocity, None, Mimic)
* **Type**: The type of the joint drive (Force, Acceleration). In Force, the effort is applied directly to the joint. In Acceleration, the effort is Normalized by the joint’s mass, and is thus invariant to the robot’s configuration, behaving as an ideal actuator.
* **Stiffness** (Stiffness Mode): The stiffness of the joint drive. Changing this will lead to a change in the natural frequency of the joint.
* **Damping** (Stiffness Mode): The damping of the joint drive. Changing this will lead to a change in the damping ratio of the joint.
* **Natural Frequency** (Natural Frequency Mode): The natural frequency of the joint drive.
* **Damping Ratio** (Natural Frequency Mode): The damping ratio of the joint drive.

The configurable Degrees of Freedom (DOF) of the robot are displayed in accordance with what is defined in the Robot’s Joints list.

## Tuning Workflow

Gain tuning is an iterative process. The recommended workflow moves through two stages:

1. **Set initial gains** using the position or velocity drive heuristics below.
2. **Tune and evaluate** using the built-in test modes, each targeting a different aspect of joint behavior:

   * **Snap-to-Limits** *(default)* — commands joints to their lower and upper limits. Use this to verify that gains are strong enough to reach the full range of motion and that limits, gains, and collision geometry are mutually consistent.
   * **Sinusoidal** — drives joints with a continuous repeating waveform. Use this to evaluate how well gains track smooth motion and to identify underdamping or overdamping from the shape of the tracking curve.
   * **Step Function** — drives joints with sudden position changes. Use this to evaluate how quickly and accurately gains respond to discrete commands, as a closer approximation of how a policy issues targets during training.

Once gains are satisfactory across all three test modes, run the **Stress Test** to confirm they are robust under the extreme commands typical of reinforcement learning training before moving to Isaac Lab.

Note

The specific tuning process may vary based on the characteristics of the robot and its control system.

### Position Drive

For each joint of the robot:

1. Start by setting the damping to zero and only tuning the stiffness. This will help you establish a stable response without the influence of the derivative term.
2. Increase the stiffness until the joint is able to converge near the target position.
3. Reduce the stiffness by one order of magnitude.
4. After setting the stiffness, add damping with one order of magnitude lower than stiffness. This will be your baseline for the parameters and in general should not overshoot. If you want a faster response, reduce damping further.
5. Fine-tune both gains around this established baseline to achieve the desired performance, considering factors such as stability, response time, and overshoot.
6. If you want to emulate a control that includes gravity compensation, select all rigid bodies of the robot and check **Disable Gravity** in the properties panel.

#### Velocity Limit and Industrial Robots

Many robots, including the majority of industrial robots, come with pre-tuned PD control for their joint drives and can be set up to have a perfect position control response, always driving at the given joint velocity limit. To reproduce this behavior, increase the joint stiffness from the previous tuning heuristic by a factor of two and define the maximum joint velocity in **Joint** > **Advanced** > **Maximum Joint Velocity** in the **Properties** panel. Run the simulation to verify the joint velocity is meeting the specification and fine-tune the stiffness until the joint max velocity limit is within tolerance. If stiffness is too high, the max velocity may still be violated, so it is not advised to add infinite stiffness to the joint — instead operate with stiffness similar to the values calibrated without a max joint velocity.

### Velocity Drive

For each joint of the robot:

1. Start by setting the **Stiffness** to zero and only tuning the damping.
2. Increase the damping until the joint is able to converge near the target velocity.
3. If the robot may carry additional load, slightly increase the damping (for example, add 10% extra) to account for the extra load.
4. You can limit the joint’s output by either setting the max joint velocity, or restricting the max joint force to impose a maximum joint load effort.

### Saving Gains to the Asset

Following the NVIDIA Isaac Sim [Asset Structure](asset_structure.html#isaac-sim-app-reference-asset-structure), joint gains are a physics configuration and ideally should be saved on the physics layer. To facilitate this, the **Save Gains to Physics Layer** button on the UI searches for the asset’s physics layer where the joint is defined and applies the updated gains to that layer.

### Gains Tests

The Gains Tests are a suite of tests that allow you to quickly assess the quality of the current set of gains under different conditions. Each test is divided by *sequences*, where a sequence is a group of joints tested together. The sequence is defined per joint and is an index of the order in which the test runs. For each sequence the robot resets to its initial configuration before the test begins.

All tests send position commands for position drives and velocity commands for velocity drives. In position commands the target velocities are always zero, so that joint damping is properly evaluated. In a real control scenario a proper trajectory command should be sent, where the velocity command is equivalent to the integrated positions of the designated trajectory.

The three tuning test modes share the same setup steps:

1. Enable the **Test** checkbox for the joints you want to evaluate in the joint table.
2. Assign joints to sequences. Joints in the same sequence are tested simultaneously; joints in different sequences are tested one group at a time, with the robot resetting to its home configuration between sequences. Group joints that are expected to move together.
3. Select the desired test mode in the test mode selector, configure parameters, and press **Play**, then **Run Test**.

Repeat — adjust gains, re-run, observe — until results are satisfactory. Each test mode surfaces different information, so it is useful to work across all three rather than treating any one as definitive.

Note

If you do not see all available columns in the Gains Tuner table, try expanding the Gain Tuner panel or increasing the overall width of the Isaac Sim application window. Some columns may be hidden if the window is too narrow.

#### Snap-to-Limits

The recommended starting point for evaluating a new or modified robot. It commands each joint to its lower limit, holds, then to its upper limit, holds, and finally returns to the home position. The test validates that authored joint limits, drive gains, and collision geometry are all mutually consistent.

Each joint approaches its target and waits to stabilize before the hold phase begins. If a joint does not settle within ten seconds, the test proceeds to the hold phase regardless. During the hold phase, position error is sampled continuously and reported as mean and maximum error over the full hold duration, making the metric robust to residual oscillation.

After the hold, each joint receives one of three classifications:

* **Pass**: Both limits reached within tolerance.
* **Fail**: A limit was not reached and the joint was still moving or oscillating, indicating a gains or dynamics issue.
* **Blocked**: A limit was not reached and the joint was stalled, typically caused by self-collisions or other physical constraints rather than a gains issue.

The total test time is variable: fast robots settle quickly and the test finishes in seconds, while slow or weak drives consume the full timeout per phase.

Per-joint results include settling time (reported separately for the lower and upper limit phases) and mean and maximum hold error at each limit.

**Parameters:**

| Parameter | Description | Default |
| --- | --- | --- |
| **Hold Duration** | Seconds to hold at each target after the joints have settled. | 1.0 |
| **Tolerance** | Position error threshold (rad or m) for the settling check and pass/fail determination. | 0.01 |
| **Disable Self-Collisions** | Temporarily disable self-collisions on the articulation during the test. Useful for distinguishing a Blocked result caused by collision geometry from a Fail result caused by insufficient gains. | Off |
| **Disable Velocity Limits** | Temporarily set joint max velocity limits to a very large value for the test duration. Useful for isolating whether a Fail result is caused by insufficient gains or by velocity limits preventing the joint from reaching its target in time. | Off |

**Interpreting Results:**

Each classification points to a different part of the system and suggests a different remedy.

* **Pass with long settling time**: The joint reaches its target but slowly, indicating the system is overdamped. Try increasing stiffness or reducing damping, then re-run to confirm settling time improves without introducing oscillation. Residual oscillation will appear as elevated mean hold error even on a passing joint.
* **Pass with high hold error**: The joint reached the limit closely enough to pass the tolerance check but is not holding cleanly — likely underdamped with residual oscillation. Try increasing damping.
* **Fail**: The joint did not reach its target and was still moving at the end of the timeout. First re-run with **Disable Velocity Limits** enabled. If the joint passes, the velocity limit is preventing the joint from reaching its target in time and the remedy is raising the velocity limit rather than adjusting gains. If the joint still fails, stiffness is insufficient and should be increased.
* **Blocked**: The joint stalled before reaching its limit. Re-run with **Disable Self-Collisions** enabled. If the joint passes, the limit is set beyond what the collision geometry allows — tighten the joint limit in USD rather than adjusting gains. If the joint remains blocked with collisions disabled, examine whether a mimic joint coupling, another joint in the same sequence, or an incorrectly authored limit is constraining motion.

Note

These tests identify that something is wrong and roughly where, but the magnitude of any gain adjustment still requires iteration: change gains, re-run, and observe whether the metric improves. The tests are diagnostic tools, not optimizers.

#### Sinusoidal

Drives joints with a continuous sinusoidal trajectory for the test duration. Useful for evaluating how well gains track smooth, repeating motion across a joint’s range.

**Parameters:**

* **Test**: Check to include the joint in the test.
* **Period**: The period of the waveform.
* **Phase**: The phase of the waveform.
* **Amplitude**: The amplitude of the waveform, from 0 to 100%.
* **Offset**: The offset of the waveform, from 0 to 100%.

**Interpreting Results:**

Use the result plots to guide adjustments:

* **Measured position closely tracks commanded position**: gains are well-tuned for this waveform. Consider tightening the period or increasing amplitude to stress the joint further.
* **Measured position lags the command or undershoots**: stiffness is likely too low. Increase stiffness and re-run.
* **Measured position oscillates or overshoots**: damping is likely too low. Increase damping and re-run.
* **Measured position is offset from the command at steady state**: the joint drive may be saturating at its max force limit. Check the joint max force setting in the Properties panel.

#### Step Function

Drives joints with a repeating step-function trajectory, alternating between a minimum and maximum position. Useful for evaluating how quickly and accurately gains respond to sudden position changes.

**Parameters:**

* **Test**: Check to include the joint in the test.
* **Period**: The period of the waveform.
* **Phase**: The phase of the waveform.
* **Step Minimum**: The minimum value of the waveform, in the joint value units of measurement.
* **Step Maximum**: The maximum value of the waveform, in the joint value units of measurement.

**Interpreting Results:**

Use the result plots to guide adjustments:

* **Measured position reaches the step target and holds cleanly**: gains are well-tuned for this step size and period.
* **Measured position overshoots and oscillates before settling**: damping is too low. Increase damping.
* **Measured position approaches the target slowly or does not reach it within the period**: stiffness is too low, or the period is shorter than the joint’s velocity limit allows. Try increasing stiffness or lengthening the period.
* **Measured position reaches the step target but with a consistent steady-state offset**: the joint drive may be saturating. Check the joint max force setting.

Note

A reasonable goal across all three test modes is to find gains that reach the commanded position with overshoot within 1% of the target. The specific tolerance depends on your application.

#### Stress Test

The stress test subjects joints to extreme random commands to surface PhysX solver instabilities that may appear during reinforcement learning training but are invisible during normal GUI testing. When training a policy with many parallel environments, the exploration space is large and joints may receive rapid, unconstrained commands across their full range. Finding these instabilities in the GUI — where iteration time is fast and the robot inspector is available — is significantly easier than diagnosing them during a training run.

Two sub-modes are available:

**Random Walk** — Every physics step, a Gaussian-distributed delta is added to each joint’s current position target. Commands are clamped to joint limits. This simulates unconstrained neural-net exploration during early policy training. The standard deviation (sigma) is expressed as a percentage of each joint’s range, so wider joints receive proportionally larger perturbations.

**Adversarial** — Every *N* physics steps, all active joints are simultaneously snapped to randomly chosen lower or upper limits (50/50 per joint). This maximizes worst-case solver load by driving extreme correlated configurations that the random walk would only hit rarely, targeting the same failure modes that arise when many parallel training environments simultaneously drive a robot to opposing extremes.

Per-joint instability detection runs every step:

* Velocity exceeding the configurable threshold marks the joint as **Unstable**.
* NaN in position or velocity marks the joint as **Unstable**.
* If neither occurs over the full duration the joint is classified as **Stable**.

The RNG seed is logged so destabilizing runs can be reproduced exactly.

**Parameters:**

| Parameter | Description | Default |
| --- | --- | --- |
| **Sub-mode** | Random Walk or Adversarial. | Random Walk |
| **Duration** | Simulation-time seconds to run. | 10.0 |
| **Velocity Threshold** | Absolute velocity (rad/s or m/s) above which a joint is flagged as Unstable. | 100.0 |
| **Sigma (% range)** | Standard deviation of the per-step Gaussian delta in Random Walk mode, expressed as a percentage of each joint’s range. | 1.0 |
| **Snap Interval** | Physics steps between random snaps in Adversarial mode. | 10 |
| **Seed** | RNG seed for reproducibility. Logged in results so a destabilizing run can be reproduced exactly. | 42 |
| **Disable Self-Collisions** | Temporarily disable self-collisions on the articulation during the test. Useful for distinguishing instabilities caused by contact events from those caused by gains. | Off |
| **Disable Velocity Limits** | Temporarily set joint max velocity limits to a very large value for the test duration. Useful for isolating whether instabilities are caused by gains or by velocity limits producing large per-step correction errors. | Off |

**Interpreting Results:**

* **Stable across both modes**: Positive evidence that the gains are unlikely to cause solver instabilities during Isaac Lab training at the configured sigma and snap interval. Document the test parameters alongside the result — a robot that is stable at 1% sigma may not be stable at 5% sigma, and this distinction matters when estimating safety margins for policy training.
* **Unstable with self-collisions enabled, Stable with them disabled**: The instability is contact-driven rather than gains-driven. Do not adjust gains in response to this result. Instead, examine whether the joint limits allow configurations where self-contact occurs and tighten limits or adjust collision geometry accordingly.
* **Unstable with self-collisions disabled**: Gains are implicated. Examine the logged time-to-instability and triggering command. A very short time-to-instability at low sigma indicates the gains are marginal even under mild perturbation and significant adjustment is needed. A long time-to-instability at high sigma indicates the gains are robust under realistic conditions and the instability is only reachable at perturbation levels a trained policy would rarely produce.
* **Unstable in Random Walk but Stable in Adversarial (or vice versa)**: The failure mode differs between the two sub-modes and the results can help narrow the diagnosis. Random Walk instabilities tend to arise from the target drifting into a problematic region incrementally. Adversarial instabilities tend to arise from the solver struggling with simultaneous extreme configurations across coupled joints.

**Isolating the responsible joints:**

When an instability is found, use the logged RNG seed to reproduce the run exactly. Then use the sequencer to re-run the test on progressively smaller subsets of the articulation, binary searching toward the minimal set of joints that reproduces the instability. This isolates which part of the kinematic chain is responsible and is significantly faster than reasoning about the full-robot result. The Robot Inspector can assist in examining the isolated subsystem.

Note

A Stable result is meaningful only at the sigma and snap interval values used. Record these parameters alongside results when assessing readiness for Isaac Lab training.

## Visualizing Results

The results of the tests are visualized as plots, where tracked joint positions and velocities are compared against the commanded trajectory. Select the desired joint in the left panel to display its results in the plots. Results are color-coded by joint, with measured values shown as a faded version of the commanded trajectory’s color.

Even if a joint is not listed in the Robot Schema, it is still visualized in the plots if it is part of the physical robot.

To select more than one joint, hold **Ctrl** and click on the desired joints, or select the first joint and hold **Shift** and click the last joint to select all joints between them.

Note

Visualization results are only available after tests have finished running. Depending on test configuration, this may take some time.

## Tips

* Disable gravity if your robot has built-in gravity compensation or a separate gravity compensation controller.
* Group joints that are expected to move together and tune each group individually first, then combine them for a final test. For a humanoid robot, for example, you may want to separate the legs and arms.
* Reduce the maximum speed of a joint that you are tuning if it is not expected to be commanded to move that fast in practice. Most default maximum velocities in USD are likely impractically high.
* When running the Stress Test, document the highest sigma at which all joints are Stable — this is a practical safety margin for your Isaac Lab training configuration.
* If a joint is Blocked in Snap-to-Limits, use **Disable Self-Collisions** to confirm the cause before adjusting gains.

## Further Learning

* The [Tutorial 11: Tuning Joint Drive Gains](../robot_setup_tutorials/joint_tuning.html#isaac-sim-app-tutorial-advanced-joint-tuning) tutorial for a hands-on walkthrough using the UR10 manipulator.

On this page

* [Overview](#overview)
  + [Understanding Joint Drives](#understanding-joint-drives)
    - [Drive Modes](#drive-modes)
* [Tools](#tools)
  + [Tuning Gains](#tuning-gains)
    - [Tuning Options](#tuning-options)
* [Tuning Workflow](#tuning-workflow)
  + [Position Drive](#position-drive)
    - [Velocity Limit and Industrial Robots](#velocity-limit-and-industrial-robots)
  + [Velocity Drive](#velocity-drive)
  + [Saving Gains to the Asset](#saving-gains-to-the-asset)
  + [Gains Tests](#gains-tests)
    - [Snap-to-Limits](#snap-to-limits)
    - [Sinusoidal](#sinusoidal)
    - [Step Function](#step-function)
    - [Stress Test](#stress-test)
* [Visualizing Results](#visualizing-results)
* [Tips](#tips)
* [Further Learning](#further-learning)

---

### Merge Mesh Utility

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/robot_setup/ext_isaacsim_util_merge_mesh.html

* [Robot Setup](index.html)
* [Editor Tools](editing_tools.html)
* Mesh merge tool

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Mesh merge tool

Deprecated since version 6.0: The standalone `isaacsim.util.merge_mesh` extension is deprecated and will be removed in a future release. Use the **Scene Optimizer** `merge` operation instead, through the URDF/MJCF importer’s **Merge Mesh** option, the **Scene Optimizer** panel (**Window > Utilities > Scene Optimizer**), the [Asset Transformer](asset_transformer.html#isaac-sim-app-asset-transformer) `MergeMeshRule`, or by calling the operation directly from Python.

## About

Mesh merging combines multiple visual geometry prims that share a common rigid-body parent into a single mesh. Reducing the number of geometry prims lowers draw-call overhead and improves both rendering and physics performance.

NVIDIA Isaac Sim performs mesh merging through the **Scene Optimizer** Kit extension (`omni.scene.optimizer.core`). The Scene Optimizer `merge` operation preserves materials as `GeomSubset` entries on the resulting mesh, supports vertex deduplication, and can group meshes spatially.

Four integration paths expose the Scene Optimizer merge operation in NVIDIA Isaac Sim:

| Integration | Where to use it | Best for |
| --- | --- | --- |
| URDF / MJCF importer | **File > Import** > **Merge Mesh** checkbox | One-shot import-time merging of robot assets |
| Scene Optimizer panel | **Window > Utilities > Scene Optimizer** | Interactive merging on existing assets, ad-hoc presets |
| Asset Transformer profile | [Asset Transformer](asset_transformer.html#isaac-sim-app-asset-transformer) > `MergeMeshRule` | Repeatable, version-controlled asset pipelines |
| Python API | `isaacsim.asset.importer.utils.merge_mesh_utils` | Custom scripts and headless asset preparation |

## Using the URDF / MJCF importer

Both the URDF and MJCF importers expose a **Merge Mesh** checkbox under the **Options** section of the importer UI. Enabling this option runs three Scene Optimizer operations in sequence on the converted USD stage:

1. `meshCleanup` — merges duplicate vertices, removes degenerate faces, fixes non-manifold geometry.
2. `generateNormals` and `generateProjectionUVs` — regenerates vertex normals and projected UVs.
3. `merge` — for each rigid body in the stage, merges all child visual mesh prims (those with `default` or `render` purpose) into a single mesh under that body.

The importer determines merge groups automatically by traversing each `UsdPhysics.RigidBodyAPI` prim and collecting its child geometry, stopping at nested rigid-body boundaries. No additional configuration is required.

Refer to [URDF Importer Extension](../importer_exporter/ext_isaacsim_asset_importer_urdf.html#isaac-sim-urdf-importer) and [MJCF Importer Extension](../importer_exporter/ext_isaacsim_asset_importer_mjcf.html#isaac-sim-mjcf-importer) for the full importer workflows.

## Using the Scene Optimizer UI

The Scene Optimizer extension ships its own UI panel that exposes the `merge` operation directly, with no intermediate Asset Transformer rule. Use this path for one-off interactive merges on an existing stage, or to combine `merge` with other Scene Optimizer operations such as deduplication and material consolidation.

GUI (Scene Optimizer panel)

Use the Scene Optimizer panel to merge meshes interactively.

1. **Enable the Scene Optimizer extension.** Scene Optimizer is not enabled by default in the standard NVIDIA Isaac Sim experiences. Open the [Extension Manager](https://docs.omniverse.nvidia.com/extensions/latest/ext_core/ext_extension-manager.html "(in Omniverse Extensions)") (**Window > Extensions**), search for `omni.scene.optimizer.bundle`, and toggle it on. The bundle pulls in the `core`, `ui`, `analysis`, and `validators` extensions.
2. **Load the asset to merge.** Use **File > Open** to load the USD into the active stage.
3. **Open the Scene Optimizer panel.** Select **Window > Utilities > Scene Optimizer**.
4. **Choose a workflow:**

   * To use a bundled preset, click **Load Preset** and pick one of the merge-related presets:

     + **Modify Stage - Merge Meshes** — flatten the hierarchy and merge meshes by material into `/World/Geometry/merged`.
     + **Modify Stage - Spatial Merge Meshes** — merge all meshes regardless of material based on a spatial bounding volume; useful for very dense scenes.
     + **Modify Instances - Merge Meshes** — merge meshes inside each prototype while preserving the instance hierarchy. Best when the asset uses scenegraph instancing.
   * To merge a hand-picked set of meshes, click **Add Scene Optimizer Process** and select **Merge Meshes** (the operation registered as `merge`). Configure:

     + **Mesh Prim Paths**: enter prim paths or path expressions (for example, `/World/Robot/left_wheel//Mesh*` — the leading `//` matches descendants at any depth under `left_wheel`). Click the **pencil** icon to pick paths from the stage, or click **Add** with prims selected in the viewport.
     + **Consider Materials**: enable to preserve per-material `GeomSubset` partitions on the merged mesh (Scene Optimizer equivalent of the legacy **Combine Materials** option).
     + **Original Geom Option**: `0` to keep the source meshes, `1` to deactivate them, `2` to delete them.
     + **Merge Point**: `0` to place the merged mesh at world origin, `1` to use the root prim’s transform.
     + **Root Path**: optional explicit path for the merged result; defaults to the first entry in **Mesh Prim Paths**.
     + **Spatial Mode** / **Spatial Threshold** / **Spatial Vertex Count**: leave at defaults unless you need spatial grouping.
5. **Add prerequisite cleanup steps (optional but recommended).** Click **Add Scene Optimizer Process** twice more and add **Mesh Cleanup** (`meshCleanup`) followed by **Generate Normals** (`generateNormals`). Drag the handles in the top-left of each process card so they execute before **Merge Meshes**. This matches the pipeline the URDF/MJCF importer runs internally.
6. **Execute and verify.**

   * Click **Execute All**. The console log reports the operations as they run.
   * Inspect the stage. Each merge group is replaced by a single mesh prim under the configured **Root Path**. If **Original Geom Option** was set to `1`, the source meshes remain in the stage as deactivated prims.
   * Save the result with **File > Save As**.
7. **Save the configuration for reuse (optional).** Click **Save Preset** to write the current process stack to a JSON file. The same JSON can be loaded later from this UI, or fed to the Scene Optimizer CLI for batch processing.

Note

The Scene Optimizer UI executes operations directly on the **active stage** in memory. Save the stage explicitly after merging — the panel does not write to disk on its own.

JSON preset (Scene Optimizer)

The Scene Optimizer panel reads and writes its own JSON preset format. A minimal preset that mirrors the importer’s pipeline (cleanup, normals + UVs, merge) looks like this:

```python
[
  {
    "operation": "meshCleanup",
    "paths": [],
    "mergeVertices": true,
    "tolerance": 0.0,
    "mergeBoundaries": true,
    "mergeNeighbors": true,
    "contractDegenerateEdges": true,
    "removeDegenerateFaces": true,
    "removeIsolatedVertices": true,
    "removeDuplicateFaces": true,
    "makeManifold": true
  },
  {
    "operation": "generateNormals",
    "paths": [],
    "binding": 0,
    "replaceExisting": true,
    "weightMode": 0,
    "sharpnessAngle": 60.0,
    "gpuThreshold": 500000
  },
  {
    "operation": "generateProjectionUVs",
    "paths": [],
    "projectionType": 4,
    "useWorldSpaceScales": true,
    "scaleFactor": 0.01,
    "overwriteExisting": true
  },
  {
    "operation": "merge",
    "meshPrimPaths": ["/World/Robot/left_wheel//Mesh*"],
    "considerMaterials": true,
    "materialAlbedoAsVertexColors": false,
    "originalGeomOption": 1,
    "mergePoint": 0,
    "rootPath": "",
    "considerAllAttributes": true,
    "allowSingleMeshes": false,
    "spatialMode": 0,
    "spatialThreshold": 10.0,
    "spatialMaxSize": 0.0,
    "spatialVertexCount": 10000,
    "spatialDebug": false
  }
]
```

Edit `meshPrimPaths` to target the meshes to merge. Use [USD path expressions](https://openusd.org/release/api/class_sdf_path_expression.html) — the `//` operator matches descendants at any depth, so `/World/Robot//Mesh*` finds every prim named `Mesh*` anywhere under `/World/Robot`.

Load this file via the Scene Optimizer panel’s **Load Preset > Browse…** button.

Refer to the [Scene Optimizer extension documentation](https://docs.omniverse.nvidia.com/extensions/latest/ext_scene-optimizer.html) for the full operation catalog, the bundled preset descriptions, and the Scene Optimizer CLI usage.

## Using the asset transformer

If you need to chain mesh merging with other USD restructuring rules — schema routing, geometry deduplication, material routing, interface generation — wrap the merge step in an Asset Transformer profile. The [Asset Transformer](asset_transformer.html#isaac-sim-app-asset-transformer) ships a **Merge Mesh** profile (`source/extensions/isaacsim.asset.transformer.rules/data/merge_mesh.json`) that runs the same rigid-body-aware merge as the importer:

```python
{
  "profile_name": "Merge Mesh",
  "version": "1.0",
  "rules": [
    {
      "name": "Merge Meshes",
      "type": "isaacsim.asset.transformer.rules.isaac_sim.merge_mesh.MergeMeshRule",
      "destination": "",
      "params": {},
      "enabled": true
    }
  ],
  "interface_asset_name": null,
  "output_package_root": null,
  "flatten_source": false,
  "base_name": null
}
```

The `MergeMeshRule` walks all rigid bodies in the stage and applies the Scene Optimizer `merge` operation to each body’s child visual meshes — no parameters required.

Chain it with `GeometriesRoutingRule` and `MaterialsRoutingRule` for a full cleanup + merge + dedupe pipeline:

```python
{
  "profile_name": "Cleanup + Merge + Dedupe",
  "version": "1.0",
  "rules": [
    {
      "name": "Merge Meshes",
      "type": "isaacsim.asset.transformer.rules.isaac_sim.merge_mesh.MergeMeshRule",
      "destination": "",
      "params": {},
      "enabled": true
    },
    {
      "name": "Route Geometries",
      "type": "isaacsim.asset.transformer.rules.perf.geometries.GeometriesRoutingRule",
      "destination": "payloads",
      "params": {
        "geometries_layer": "geometries.usd",
        "instance_layer": "instances.usda",
        "deduplicate": true
      },
      "enabled": true
    },
    {
      "name": "Route Materials",
      "type": "isaacsim.asset.transformer.rules.perf.materials.MaterialsRoutingRule",
      "destination": "payloads",
      "params": {
        "materials_layer": "materials.usda",
        "download_textures": true
      },
      "enabled": true
    }
  ],
  "interface_asset_name": null,
  "output_package_root": null,
  "flatten_source": false,
  "base_name": null
}
```

Load the profile via **Tools > Robotics > Asset Editors > Asset Transformer > Load Preset**, set the **Output Directory**, and click **Execute Actions**. Refer to [Asset Transformer Rules Reference](asset_transformer_rules.html#isaac-sim-app-asset-transformer-rules) for the complete rule catalog and to [Asset Transformer Tutorials](asset_transformer_tutorials.html#isaac-sim-app-asset-transformer-tutorials) for Asset Transformer GUI walkthroughs.

## Using the Python API

The `isaacsim.asset.importer.utils.merge_mesh_utils` module wraps the Scene Optimizer operations used by the importer. Use it for headless asset preparation, batch processing, or custom asset “massaging” that does not fit the importer or transformer flows.

The code blocks below are taken from a single runnable script, `docs/isaacsim/snippets/robot_setup/merge_mesh.py`, which you can execute with Isaac Sim’s `python.sh`. Pass `--test` to import the bundled `carter.urdf` test asset and exercise every snippet end-to-end.

Note

The `omni.scene.optimizer.core` extension must be enabled before calling these helpers. Standalone scripts must enable it explicitly:

```python
import omni.kit.app

omni.kit.app.get_app().get_extension_manager().set_extension_enabled_immediate("omni.scene.optimizer.core", True)
```

Available helpers:

| Function | Purpose |
| --- | --- |
| `clean_mesh_operation(stage)` | Run `meshCleanup`: merge duplicate vertices, remove degenerate faces, make manifold. |
| `generate_mesh_uv_normals_operation(stage)` | Run `generateNormals` and `generateProjectionUVs` to regenerate per-vertex normals and projected UVs. |
| `merge_meshes_operation(stage)` | Walk all rigid bodies and merge each body’s child visual meshes (returns the number of merged groups). |
| `merge_mesh(stage, mesh_paths)` | Merge an explicit list of mesh prim paths into a single mesh. |

Example: full importer-equivalent pipeline applied to an existing stage

```python
from isaacsim.asset.importer.utils import merge_mesh_utils
from pxr import Usd

# stage_path = "/path/to/robot.usd"
stage = Usd.Stage.Open(stage_path)

merge_mesh_utils.clean_mesh_operation(stage)
merge_mesh_utils.generate_mesh_uv_normals_operation(stage)
merged_groups = merge_mesh_utils.merge_meshes_operation(stage)

print(f"Merged {merged_groups} rigid-body mesh group(s)")
stage.Save()
```

Example: merge a hand-picked set of meshes (replaces the legacy “select prims, click Merge” workflow)

```python
from isaacsim.asset.importer.utils import merge_mesh_utils
from pxr import Usd

# stage_path = "/path/to/asset.usd"
# mesh_paths = [
#     "/World/Jetbot/left_wheel/visual_0",
#     "/World/Jetbot/left_wheel/visual_1",
#     "/World/Jetbot/left_wheel/visual_2",
# ]
stage = Usd.Stage.Open(stage_path)

merge_mesh_utils.merge_mesh(stage, mesh_paths)
stage.Save()
```

The first prim in the list is used as the merge root and origin, matching the legacy tool’s “first selection wins” behavior.

## Scene Optimizer operation reference

For finer control, call `omni.scene.optimizer.core` operations directly. Build a `SceneOptimizerCore` instance and an `ExecutionContext` bound to your stage, then dispatch operations by name with a configuration dict:

```python
from omni.scene.optimizer.core import ExecutionContext, SceneOptimizerCore
from pxr import Usd

# stage_path = "/path/to/asset.usd"
# mesh_paths = ["/World/A", "/World/B", "/World/C"]
stage = Usd.Stage.Open(stage_path)

context = ExecutionContext()
context.set_stage(stage)
context.generateReport = 0
context.captureStats = 0

core = SceneOptimizerCore.getInstance()

core.executeOperation(
    "merge",
    context,
    {
        "meshPrimPaths": list(mesh_paths),
        "considerMaterials": True,
        "materialAlbedoAsVertexColors": False,
        "originalGeomOption": 1,
        "mergePoint": 0,
        "rootPath": mesh_paths[0],
        "considerAllAttributes": True,
        "allowSingleMeshes": False,
        "spatialMode": 0,
        "spatialThreshold": 10.0,
        "spatialMaxSize": 0.0,
        "spatialVertexCount": 10000,
        "spatialDebug": False,
    },
)
stage.Save()
```

The default configurations the NVIDIA Isaac Sim importer uses are listed below for reference.

```python
MESH_CLEANUP_CONFIG = {
    "paths": [],
    "mergeVertices": True,
    "tolerance": 0.0,
    "mergeBoundaries": True,
    "mergeNeighbors": True,
    "contractDegenerateEdges": True,
    "removeDegenerateFaces": True,
    "removeIsolatedVertices": True,
    "removeDuplicateFaces": True,
    "makeManifold": True,
}

GENERATE_NORMALS_CONFIG = {
    "paths": [],
    "binding": 0,
    "replaceExisting": True,
    "weightMode": 0,
    "sharpnessAngle": 60.0,
    "gpuThreshold": 500000,
}

GENERATE_PROJECTION_UVS_CONFIG = {
    "paths": [],
    "projectionType": 4,
    "useWorldSpaceScales": True,
    "scaleFactor": 0.01,
    "overwriteExisting": True,
}

MERGE_CONFIG = {
    "meshPrimPaths": [],
    "considerMaterials": False,
    "materialAlbedoAsVertexColors": False,
    "originalGeomOption": 1,
    "mergePoint": 0,
    "rootPath": "",
    "considerAllAttributes": True,
    "allowSingleMeshes": False,
    "spatialMode": 0,
    "spatialThreshold": 10.0,
    "spatialMaxSize": 0.0,
    "spatialVertexCount": 10000,
    "spatialDebug": True,
}
```

The importer sets `considerMaterials` to `False` because material routing is handled separately by the asset transformer’s `MaterialsRoutingRule`. Set it to `True` when running `merge` standalone to preserve per-material `GeomSubset` partitioning on the merged mesh — this is the Scene Optimizer equivalent of the legacy tool’s **Combine Materials** option.

## Migrating from the legacy mesh merge tool

| Legacy option | Scene Optimizer equivalent |
| --- | --- |
| **Source Prim** (first selection = origin) | Pass mesh paths to `merge_mesh(stage, paths)`; first path is used as `rootPath`. |
| **Clear Parent Transform** | Set `mergePoint` to `0` (world origin) or `1` (root prim’s transform) in the `merge` config. |
| **Deactivate source assets** | Controlled by `originalGeomOption`: `0` keeps originals, `1` deactivates them, `2` deletes them. |
| **Combine Materials** | Set `considerMaterials = True` in the `merge` config. Material assignments are preserved as `GeomSubset` entries on the merged mesh. |
| Selecting an empty Xform first to set origin | Use `rootPath` to specify any prim path as the merge target/origin. |

## See also

* [URDF Importer Extension](../importer_exporter/ext_isaacsim_asset_importer_urdf.html#isaac-sim-urdf-importer) — URDF importer with built-in **Merge Mesh** option.
* [MJCF Importer Extension](../importer_exporter/ext_isaacsim_asset_importer_mjcf.html#isaac-sim-mjcf-importer) — MJCF importer with built-in **Merge Mesh** option.
* [Asset Transformer](asset_transformer.html#isaac-sim-app-asset-transformer) — Rule-based asset transformation framework.
* [Asset Transformer Rules Reference](asset_transformer_rules.html#isaac-sim-app-asset-transformer-rules) — `MergeMeshRule` reference and other available rules.
* [Scene Optimizer extension documentation](https://docs.omniverse.nvidia.com/extensions/latest/ext_scene-optimizer.html) — Full operation reference for `omni.scene.optimizer.core`.

On this page

* [About](#about)
* [Using the URDF / MJCF importer](#using-the-urdf-mjcf-importer)
* [Using the Scene Optimizer UI](#using-the-scene-optimizer-ui)
* [Using the asset transformer](#using-the-asset-transformer)
* [Using the Python API](#using-the-python-api)
* [Scene Optimizer operation reference](#scene-optimizer-operation-reference)
* [Migrating from the legacy mesh merge tool](#migrating-from-the-legacy-mesh-merge-tool)
* [See also](#see-also)

---

### Inspector Tools

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/robot_setup/inspector_tools.html

* [Robot Setup](index.html)
* Inspector Tools

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Inspector Tools

* [Joint Inspector](joint_inspector.html)
* [Physics Inspector](../physics/joint_inspector.html)
* [Simulation Data Visualizer](../physics/ext_isaacsim_inspect_physics.html)

---

### Joint Inspector

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/robot_setup/joint_inspector.html

* [Robot Setup](index.html)
* [Inspector Tools](inspector_tools.html)
* Joint Inspector

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Joint Inspector

The `isaacsim.gui.property` extension provides a standalone **Joint Inspector** window for Adjusting per-joint values across the robots present on the stage.

## Opening the Window

Open the inspector through **Tools > Robotics > Joint Inspector**.

The window docks to the left of the viewport.

## Selecting a Robot

The header exposes a robot picker, a refresh button, and a **+ New Inspector** button.

* **Robot drop-down** – lists every prim on the stage that has `IsaacRobotAPI` applied. Click the drop-down to open a searchable popup; type any substring of the prim path to narrow the list. Selecting a robot rebinds the table to that robot’s joints.
* **Refresh** – rescans the stage for prims with `IsaacRobotAPI`. Use this after authoring a new robot in a script editor or after switching layers.
* **+ New Inspector** – spawns an additional Joint Inspector window. Each window keeps an independent robot selection and column set, which is useful for side-by-side comparison of two robots or two views of the same robot.

The window listens to stage open/close and asset-load events so the robot list refreshes automatically when assets finish loading.

## Filtering Joints

A search field above the table filters the joint rows by name. Two matching modes are supported:

* **Substring (default)** – a case-insensitive substring match against the joint short name and the full prim path. `arm` matches `shoulder_arm_joint` as well as `/World/UR10/shoulder/arm`.
* **Glob (``\*`` or ``?`` in the query)** – `fnmatch`-style wildcards. The query is also matched in a substring-fenced form (`*pattern*`) so `hand*` finds anything that contains `hand`, mirroring the typical search-bar mental model.

A clear button on the right of the field removes the query and restores the full list.

## Choosing Columns

The hamburger button on the right of the toolbar opens a categorized columns popup.

The popup contains:

* **Backend pills** at the top – `PhysX` and `MuJoCo` toggle the visibility of every column belonging to that simulation backend. The pill state does not flip the per-column checkboxes, so re-enabling a backend restores the previously checked columns.
* **Categorized checkbox rows** for the available column groups.

The available column groups are summarized below.

| Group | Backend | Columns |
| --- | --- | --- |
| **Joint Limits** | USD / PhysX | `Position Min`, `Position Max`, `Velocity Max`. |
| **Drives** | USD | `Max Force`, `Target Position`, `Target Velocity`, `Stiffness`, `Damping`. |
| **Performance Envelope** | PhysX | `Max Actuator Velocity`, `Speed-Effort Gradient`, `Velocity-Dependent Resistance`. |
| **Joint State** | PhysX | `State Position`, `State Velocity`. |
| **MuJoCo Joint** | MuJoCo | `Armature`, `Damping`, `Stiffness`, `Friction Loss`, `Spring Ref`, `SolRef Limit (timeconst)`, `SolImp Limit (dmin)`. |

Column behavior:

* Items whose backing API is not applied on any joint of the current robot stay clickable but render dimmed; their tooltip explains why the column is currently empty.
* The user’s column selection persists across robot switches. A column reappears as soon as a robot whose joints back the column is selected.
* `Joint Limits` columns belong to USD core schemas and are not affected by the backend pills.

### Per-axis fan-out

When every joint authoring a multi-apply schema has at most one axis applied (the common case for revolute and prismatic chains), the per-axis dimension is collapsed and the column appears once. The cell automatically picks the joint’s authored axis or its natural axis (`angular` for revolute, `linear` for prismatic).

Multi-DOF (for example, `D6Joint`) joints make the column fan out: one column per distinct axis (`transX`, `transY`, `transZ`, `rotX`, `rotY`, `rotZ`) is rendered, with the axis token appended to the header label.

## Editing Values

Each cell is a free-form `ui.FloatDrag` bound directly to the underlying USD attribute. Drag horizontally to scrub the value or click to type a number. double-click or Ctrl-click to type a number.

Behavior of empty cells, multi-row edits, and array-typed attributes:

* Cells whose backing API is not applied on the joint render empty rather than as a disabled `0.0` field. This avoids implying a meaningful zero where no value is authored.
* Click rows to select them. `Ctrl` / `Cmd` and `Shift` allow multi-row selection. Editing one cell of a selected row mirrors the new value to the same column on every other selected row whose attribute exists.
* The MuJoCo `solreflimit` and `solimplimit` columns surface only the dominant element of the underlying array (`timeconst` and `dmin`); the rest of the array is preserved on write.

The status line above the table shows the number of joints currently displayed.

## Default Visible Columns

The first time the inspector is opened, the following columns are visible:

* `Position Min` and `Position Max` (Joint Limits)
* `Target Position`, `Stiffness`, `Damping` (Drives)
* `State Position` (Joint State)
* `Armature`, `Damping`, `Stiffness`, `Friction Loss` (MuJoCo Joint)

Use the columns menu to add or remove columns from this set.

On this page

* [Opening the Window](#opening-the-window)
* [Selecting a Robot](#selecting-a-robot)
* [Filtering Joints](#filtering-joints)
* [Choosing Columns](#choosing-columns)
  + [Per-axis fan-out](#per-axis-fan-out)
* [Editing Values](#editing-values)
* [Default Visible Columns](#default-visible-columns)

---

### Robot Inspector

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/robot_setup/robot_inspector.html

* [Robot Setup](index.html)
* Robot Inspector Window

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Robot Inspector Window

The `isaacsim.robot.schema.ui` extension provides an interactive **Robot Inspector** window for inspecting the kinematic structure of robots on the stage and selectively masking components for simulation.

## Opening the Window

The Robot Inspector window is accessible via **Window > Robot Inspector**. It docks next to the Stage panel by default.

## Hierarchy Display Modes

A mode selector at the top of the window controls how the robot hierarchy is displayed. Three modes are available:

| Mode | Description |
| --- | --- |
| **Flat** | Links and joints are listed as two flat scopes (`Links`, `Joints`) under each robot, ordered as they appear in the schema relationships. Useful for quickly reviewing the complete lists. |
| **Tree** (default) | Parent link → joint → child link chain. Matches the kinematic traversal order and is the most natural representation for articulated robots. |
| **MuJoCo** | Tree rooted at the base link. Each link’s children appear first, and the joint connecting the link to its own parent appears as the last child entry. Mirrors the body-centric layout used by MuJoCo MJCF files. |

|  |  |  |
| --- | --- | --- |
|  |  |  |
| **Flat** | **Tree** | **MuJoCo** |

.wy-table-responsive table td {
vertical-align: top;
}

## Component Masking

The Robot Inspector provides per-component masking controls that allow disabling individual joints and links for simulation without modifying the authored USD layers. All masking opinions are a debugging tool and are written to a dedicated anonymous sublayer inserted into the session layer stack, so they are transient and never saved to disk.

Three masking columns appear in the tree view:

| Column | Description |
| --- | --- |
| **Deactivate** () | Disables the joint or link for simulation. Joint deactivation sets `jointEnabled = False`. Link deactivation disables the rigid body, turns off collision meshes, and hides non-rigid child geometry. |
| **Bypass** () | Disables the element AND reconnects the kinematic chain around it. For joints, fixed joints are created bridging the nearest backward non-masked link to each forward non-masked link. For links, the backward joint is deactivated and forward joints are reparented to the nearest non-masked ancestor link with recalculated local-frame offsets. |
| **Anchor** () | Pins a link to the world at its current pose by creating a temporary fixed joint with no `body0`. Only available on links that have `RigidBodyAPI` applied. |

Masking operations support multi-selection: clicking a column icon while multiple prims are selected applies the action to all selected prims in a single batch.

Note

The masking sublayer is automatically cleared when a new stage is opened or the current stage is closed. Masking state does not persist across sessions.

## Viewport Joint Visualization

When the Robot Inspector window is active, joint connections are drawn as overlay lines in the 3D viewport, connecting parent and child links at joint locations. This visualization provides a quick visual check of the kinematic chain.

* Connection lines include directional arrows indicating the parent-to-child relationship.
* When multiple joints overlap at the same screen position (common at dense joint clusters), an **overlay circle** is drawn. Clicking the circle opens a context menu listing all joints at that location, allowing selection of any individual joint.
* Joint visualization is hidden during simulation playback and restored when playback stops.
* Visibility is controlled by the **Visibility Menu (Eye Icon on viewport) > Show by Type > Physics > Joints** setting.

# UI Utility Functions

The `isaacsim.robot.schema.ui` extension exposes additional utilities for hierarchy generation and component inspection. These are accessible via:

```python
from isaacsim.robot.schema.ui.utils import HierarchyMode, generate_robot_hierarchy_stage
```

## Hierarchy Mode

`HierarchyMode` is an enum controlling how the robot hierarchy is structured in the Robot Inspector and in the in-memory hierarchy stage:

| Value | Description |
| --- | --- |
| `HierarchyMode.FLAT` | Links under a `Links` scope and joints under a `Joints` scope, in schema relationship order. |
| `HierarchyMode.LINKED` | Parent link → joint → child link chain (default). |
| `HierarchyMode.MUJOCO` | Tree rooted at the base link. Child links appear first under each link; the joint connecting the link to its parent appears as the last child entry. |

## Hierarchy Stage Generation

| Function | Description |
| --- | --- |
| `generate_robot_hierarchy_stage(mode)` | Scans the current stage for prims with `IsaacRobotAPI`, builds a link tree for each robot, and creates an in-memory USD hierarchy stage. Returns `(hierarchy_stage, path_map, joint_connections)`. The `mode` parameter accepts a `HierarchyMode` value (default `LINKED`). |

The returned `PathMap` object provides bidirectional mapping between original stage paths and hierarchy stage paths:

```python
hierarchy_stage, path_map, connections = generate_robot_hierarchy_stage(HierarchyMode.FLAT)
# Map from original stage path to hierarchy path
hier_path = path_map.get_hierarchy_path(original_prim_path)
# Map back from hierarchy path to original stage path
orig_path = path_map.get_original_path(hier_prim_path)
```

Note

During hierarchy generation, any active masking sublayer is temporarily muted so the tree always reflects the unmodified robot structure.

# Masking Operations API

The `isaacsim.robot.schema.ui` extension provides a programmatic API for masking, bypassing, and anchoring robot components. The state is managed by the `MaskingState` singleton and the USD operations are performed by `MaskingOperations`.

```python
from isaacsim.robot.schema.ui.masking_state import MaskingState
from isaacsim.robot.schema.ui.masking_ops import MaskingOperations
```

## MaskingState

`MaskingState` is a singleton that tracks which prims are deactivated (masked), bypassed, or anchored. It maintains three independent sets and notifies subscribers when any state changes.

| Method | Description |
| --- | --- |
| `MaskingState.get_instance()` | Returns the singleton `MaskingState` instance. |
| `is_deactivated(original_path)` | Returns `True` if the prim is masked or bypassed. |
| `is_bypassed(original_path)` | Returns `True` only if the prim is in the bypassed state. |
| `is_anchored(original_path)` | Returns `True` if the link is anchored to the world. |
| `toggle_deactivated(original_path)` | Toggles plain mask. Unmasking a bypassed prim unbypasses it first. |
| `toggle_bypassed(original_path)` | Toggles bypass state (mask + reconnect chain). |
| `toggle_anchored(original_path)` | Toggles world-anchor on a link. |
| `set_deactivated_batch(paths, deactivated)` | Sets deactivation state for multiple prims with a single change notification. |
| `set_bypassed_batch(paths, bypassed)` | Sets bypass state for multiple prims with a single change notification. |
| `set_anchored_batch(paths, anchored)` | Sets anchor state for multiple links with a single change notification. |
| `clear()` | Clears all masking, bypass, and anchor state. |
| `subscribe_changed(callback)` | Registers a no-argument callback invoked when any state changes. |
| `unsubscribe_changed(callback)` | Unregisters a previously registered change callback. |

## MaskingOperations

`MaskingOperations` performs the actual USD edits on a dedicated anonymous sublayer. All opinions are transient and never written to the authored layers.

| Method | Description |
| --- | --- |
| `mask_prim(original_path)` | Disables a joint (`jointEnabled = False`) or link (rigid body, collisions, visibility) for simulation. |
| `unmask_prim(original_path)` | Removes mask opinions, restoring base-layer values. |
| `bypass_prim(original_path)` | Masks the element and reconnects the kinematic chain around it. For joints, creates fixed joints bridging the gap. For links, deactivates the backward joint and reparents forward joints. |
| `unbypass_prim(original_path)` | Removes the bypass, restoring the chain to its original state. |
| `anchor_link(original_path)` | Pins a link to the world by creating a fixed joint at its current pose. |
| `unanchor_link(original_path)` | Removes the anchor fixed joint. |
| `clear_all()` | Drops the masking sublayer entirely, reverting everything at once. |

On this page

* [Robot Inspector Window](#)
  + [Opening the Window](#opening-the-window)
  + [Hierarchy Display Modes](#hierarchy-display-modes)
  + [Component Masking](#component-masking)
  + [Viewport Joint Visualization](#viewport-joint-visualization)
* [UI Utility Functions](#ui-utility-functions)
  + [Hierarchy Mode](#hierarchy-mode)
  + [Hierarchy Stage Generation](#hierarchy-stage-generation)
* [Masking Operations API](#masking-operations-api)
  + [MaskingState](#maskingstate)
  + [MaskingOperations](#maskingoperations)

---

### Robot Poser

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/robot_setup/robot_poser.html

* [Robot Setup](index.html)
* Robot Poser

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Robot Poser

The Robot Poser creates, edits, and applies named poses for robots that carry the [Robot Schema](../omniverse_usd/robot_schema.html#isaac-sim-robot-schema). It combines an interactive IK-goal workflow with persistent USD storage so that authored poses travel with the robot asset and can be replayed both in the GUI and through code.

The functionality is split across two extensions:

* `isaacsim.robot.poser` – Headless API for IK solving, named-pose CRUD, joint-state application, and JSON import/export.
* `isaacsim.robot.poser.ui` – GUI comprising the Robot Poser window, the Named Pose properties panel, and a custom stage icon for `IsaacNamedPose` prims.

# Robot Poser Window

The Robot Poser window is accessible via **Tools > Robotics > Robot Poser**.

## Robot Selection

A dropdown at the top of the window lists every prim on the current stage that has `IsaacRobotAPI` applied. Selecting a robot loads its existing named poses into the table below and populates the available site candidates used for start/end link selection.

## Named Poses Table

The main area of the window displays a table of the robot’s named poses. Each row shows:

| Column | Description |
| --- | --- |
| **Named Pose** | Editable name of the pose. Renaming updates the underlying `IsaacNamedPose` prim. |
| **Start Site** | The start link of the kinematic chain. Can be a Link or a site. Typically the base of the robot. |
| **End Site** | The end link or site of the kinematic chain. Can be a Link or a site. Typically the end-effector frame or tool mount. |

Note

Selecting a site that is not a fixed frame of the robot, and that affect the robot’s origin in the course of the kinematic chain may result in the robot moving its base origin. If that needs to be fixed in the future, you can manually reset the pose of the robot’s origin link, and re-apply the named pose.

Note

tip: create a named pose for the robot’s base position, and you can use it to reset the robot to its initial position if any authoring cause the robot to move from its initial position.

### Row Actions

Each row provides action buttons:

* **Apply Pose** () – Sets the robot to the stored joint configuration. When simulation is stopped the joints are teleported directly; when running, the values are written as joint drive targets.
* **Track Target** () – Enables real-time IK tracking for the pose. While active, moving the `IsaacNamedPose` prim in the viewport (via its manipulator gizmo) continuously solves IK and updates the stored joint values. When IK fails to converge, a red outline is drawn on the end-effector link chain to indicate the failure.

### Managing Poses

* **Add** – Creates a new `IsaacNamedPose` prim under the robot’s `Named_Poses` scope, registers it in the `isaac:robot:namedPoses` relationship, and adds a row to the table. The new pose captures the robot’s current joint state for the selected start/end site pair.
* **Remove** – Deletes the selected pose prim from the stage and removes it from the robot’s relationship.
* **Search** – Filters the table rows by name.
* **Drag-and-drop** – Reorders rows, which also reorders the targets in the `namedPoses` relationship.

## Simulation Behavior

The Robot Poser behaves differently depending on whether the simulation timeline is playing.

**Simulation stopped** – Joint values are applied by directly teleporting the joint attributes on the USD stage. The robot jumps to the target pose instantly, and is authored to the active edit target layer. This is the expected mode during authoring: it lets you position the robot precisely without physics interference and produces clean USD opinions suitable for saving.

**Simulation running** – Joint values are written as joint drive targets. The physics engine then moves the robot toward the requested configuration over subsequent simulation steps, respecting dynamics, joint limits, and contact forces. The resulting motion is smooth but may not reach the exact target if forces or collisions prevent it. The target pose is not authored to the active edit target layer, instead it is authored to a session layer, and gets cleared once simulation stops. If you want to keep the pose after simulation stops, you can change the simulation setting to not reset the robot state on stop.

IK tracking follows the same rule: while tracking is active and simulation is stopped, joints are teleported each frame the target moves; while simulation is running, drive targets are updated instead.

## Asset Structure Recommendations

Named poses and the joint values they write to are authored on the current edit target layer. Following the [Asset Structure](asset_structure.html#isaac-sim-app-reference-asset-structure) guidelines:

* **Named pose prims** (`IsaacNamedPose`) should be authored in the **robot schema layer** alongside the rest of the Robot Schema. They describe the robot’s capabilities and travel with the asset.
* **Robot base pose** (the initial position and orientation of the robot on the stage) should be authored in the base layer, or a **dedicated authoring layer** applied on top of the asset base (to avoid data loss) and physics layers. This keeps scene-level placement separate from the robot definition itself and avoids modifying the source or physics layers.

When authoring named poses, if physics is not enabled, temporarily add the physics layer as a sublayer so the kinematic chain can be resolved, then remove it before saving – the same workflow used when applying the Robot Schema itself.

# Named Pose Properties Panel

When an `IsaacNamedPose` prim is selected in the Stage panel, The Named posed properties can be edited in the properties panel. This panel provides direct editing of the pose without requiring the Robot Poser window to be open.

Whenever a named pose is selected, its transform is automatically updated to the forward kinematics of the robot at the named pose values.

## Site Selection

Two combo boxes at the top of the panel control the **Start Link** and **End Link** relationships on the prim. Changing a site rebuilds the kinematic chain and recomputes the joint table below. The combo boxes support search filtering to quickly locate sites on complex robots.

## Action Buttons

| Button | Description |
| --- | --- |
| **Set Robot to Pose** () | Applies the stored joint values to the robot, matching the behavior of the Apply Pose button in the Robot Poser window. |
| **Track Target** () | Starts standalone IK tracking for this pose. The tracking loop runs independently of the Robot Poser window – no window needs to be open. While tracking, the named pose prim’s Xform (position and orientation) is used as the IK target each frame. Moving the prim via the viewport manipulator drives the robot in real time. |

## Joint Table

Below the action buttons, an editable joint table lists every joint in the kinematic chain between the start and end links:

| Column | Control | Description |
| --- | --- | --- |
| **Lock** | Toggle icon | Locks or unlocks the joint. A locked (fixed) joint is held constant during IK solving; its `jointFixed` flag is set to `True` in the stored pose. |
| **Joint** | Label | Joint prim name. |
| **Value** | Slider | Current joint value within the joint’s limits. Dragging the slider updates the stored `jointValues` attribute on the prim. When tracking is active, the FK is recomputed and the named pose prim’s transform is updated to reflect the new end-effector position. |

## IK Failure Visualization

When IK tracking is active and the solver fails to converge (the target pose is unreachable), a red outline is drawn on the geometry prims along the IK chain. The outline clears automatically when the solver succeeds again or tracking is stopped.

# Example: Authoring Named Poses

This walkthrough creates three named poses on a robot arm – a home position, a pick-ready stance, and a place target – using the Robot Poser window and IK tracking. Start with a stage that contains at least one robot prim with `IsaacRobotAPI` applied.
In This Example, we will use the `UR10e` robot from `UniversalRobots`, with the Robotiq 2F-85 gripper.
1. Find the `UR10e` robot in the `UniversalRobots` folder in the assets browser.
2. Add the `UR10e` robot to the stage by dragging it onto the stage.
3. Select the Robotiq 2F-85 gripper in Gripper Variants on the property panel.

## 1. Select the Robot

Open the Robot Poser window via **Tools > Robotics > Robot Poser**. In the **Active Robot** dropdown, ensure the UR10e is selected.

## 2. Add a “Home” Pose

With the robot in its default joint configuration, Select the start link as `` `base_link` `` and the end link as `` `grip_frame` ``. Notice there are two `` `base_link` `` items on the dropdown. Hover over the name to verify it is the base\_link for the ur10e, and not for the gripper. Click **Add** in the Robot Poser window. A new row appears in the Named Poses table. Rename it to `Home` by double-clicking the name cell. Select the desired **Start Site** and **End Site** for the kinematic chain.

This pose captures the robot’s current joint state and serves as a known-good reset position.

## 3. Add a “Pick Ready” Pose with IK Tracking

Click **Add** again to create a second pose and rename it to `PickReady`. Click the **Track Target** button () on the new row to enable IK tracking.

With tracking active, select the `PickReady` named pose prim in the viewport and use the translate/rotate gizmo to drag the end-effector to the desired pre-grasp position. You can also change the pose through the transform property panel. The robot updates its pose in real time as IK solves each frame.

Once the robot reaches the target pose, click **Track Target** again to stop tracking. The joint values are now stored in the `PickReady` prim.

## 4. Add a “Place” Pose

Repeat the process: click **Add**, rename the pose to `Place`, enable **Track Target**, and drag the named pose prim to the desired place location. Stop tracking when satisfied.

## 5. Verify the Poses

Click the **Apply Pose** button () on each row to cycle through the poses and confirm the robot reaches the expected configurations. Reorder rows by drag-and-drop if a different sequence is preferred.

See video below for a demonstration of the workflow.

## Things to try

* Enable tracking and move the named pose prim in the viewport while simulation is running. The robot will follow the named pose prim in real time.
* Use the Animation curve Editor to create a robot animation from the named poses by setting time-coded joint target values for the joints.
* Work on a Multi-end-effector robot by creating named poses for each end-effector.
* Try creating a named pose for the robot’s base position, and you can use it to reset the robot to its initial position if any authoring cause the robot to move from its initial position.
* Try creating a named pose between two different end-effectors that moves the robot’s base link to a new position. Reset the robot to the origin by resetting the base link transform, and re-apply the Zero-Pose named pose.

# Named Pose Schema Reference

Each named pose is stored as an [IsaacNamedPose](../omniverse_usd/robot_schema.html#isaac-sim-robot-schema-named-pose) typed prim on the USD stage. The schema, its relationships, attributes, and query utilities are documented in the [Robot Schema](../omniverse_usd/robot_schema.html#isaac-sim-robot-schema) reference.

The `isaacsim.robot.poser` extension provides the CRUD and I/O functions for working with named poses programmatically. See the [Named Pose CRUD](../omniverse_usd/robot_schema.html#isaac-sim-robot-schema-named-pose-crud) section in the Robot Schema documentation for the full API listing.

On this page

* [Robot Poser](#)
* [Robot Poser Window](#robot-poser-window)
  + [Robot Selection](#robot-selection)
  + [Named Poses Table](#named-poses-table)
    - [Row Actions](#row-actions)
    - [Managing Poses](#managing-poses)
  + [Simulation Behavior](#simulation-behavior)
  + [Asset Structure Recommendations](#asset-structure-recommendations)
* [Named Pose Properties Panel](#named-pose-properties-panel)
  + [Site Selection](#site-selection)
  + [Action Buttons](#action-buttons)
  + [Joint Table](#joint-table)
  + [IK Failure Visualization](#ik-failure-visualization)
* [Example: Authoring Named Poses](#example-authoring-named-poses)
  + [1. Select the Robot](#select-the-robot)
  + [2. Add a “Home” Pose](#add-a-home-pose)
  + [3. Add a “Pick Ready” Pose with IK Tracking](#add-a-pick-ready-pose-with-ik-tracking)
  + [4. Add a “Place” Pose](#add-a-place-pose)
  + [5. Verify the Poses](#verify-the-poses)
  + [Things to try](#things-to-try)
* [Named Pose Schema Reference](#named-pose-schema-reference)

---

### Robot Wizard

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/robot_setup/robot_wizard.html

* [Robot Setup](index.html)
* Robot Wizard [Deprecated]

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Robot Wizard [Deprecated]

Warning

**Deprecated:** The Robot Wizard extension (`isaacsim.robot_setup.wizard`) is deprecated since Isaac Sim 6.0.0 and will be removed in a future release.

The Robot Wizard was designed to speed up the process of setting up a robot in Isaac Sim. It allowed you to define the robot’s hierarchy, organize the meshes, add colliders, joints and joint drives. It automatically applied relevant Schemas and APIs without needing to manually edit the USD files. It separated the robot into different configurations based on the desired structure described in [Asset Structure](asset_structure.html#isaac-sim-app-reference-asset-structure).

The following sections explain the UI and functions behind each step in the wizard. To observe the wizard in action, refer to [Robot Wizard Tutorial [Deprecated]](robot_wizard_tutorials.html#isaac-sim-app-robot-wizard-tutorials).

## Overview

The Robot Wizard guides you through the following steps:

^ **File Preparation**: Load the robot model and allocate folders and files for the final robot files.

* **Organize Link Hierarchy**: Define the robot’s hierarchy and link the parent-mesh child relationships.
* **Colliders**: Examine colliders to the robot’s links.
* **Joints and Drives**: Add joints to the robot’s links and drives and configure their properties.

The resulting files of the Robot Wizard are all placed in a folder, which you will have a chance to indicate in the wizard. The folder contains the following files:

* <robot\_root\_folder>/configurations:
  :   + The folder that contains the robot’s configurations USD files. The configurations are the different variants of the robot, such as a robot with or without physics, with sensors, and different end-effectors.
* <robot\_root\_folder>/configurations/<robot-name>\_base.usd
  :   + The configuration file that contains the robot’s base mesh and hierarchy.
* <robot\_root\_folder>/configurations/<robot-name>\_physics.usd
  :   + The configuration file that contains the robot’s physics setup in a sublayer. This includes the rigid body definition, colliders, joints, and drives.
* <robot\_root\_folder>/configurations/<robot-name>\_robot.usd
  :   + The configuration file that contains the robot schema, labeling the robot and its components.
* <robot\_root\_folder>/<robot-name>.usd:
  :   + The file that contains all the variants of the robot. In this case, the option of a robot with or without physics.

## Wizard Steps

### Page Orientation

| Ref # | Panel Name | Description |
| --- | --- | --- |
| 1 | Wizard Steps | The Wizard Steps panel shows your progress. You can click on each step to navigate to it. It will also advance itself as you go through the wizard. The names of the steps will change to green when it’s completed. |
| 2 | Additional Tools | You may open other tools for robot setup here. |
| 3 | Step Pages | Each step in the wizard has a page. You can navigate through the pages by clicking on the step name in the Wizard Steps panel. |
| 4 | Next Button | The Next button will advance you to the next step in the wizard. |
| 5 | Start Over | The Button will reset the wizard to the first step. |
| 6 | Launch On Startup | When checked, the wizard will launch automatically when Isaac Sim is started. It’s defaulted to not start. |
| 7 | Help | Open the documentation page for the wizard in your browser. |

### Add Robot

This page allows you the select the starting point of the robot configuration. For the current iteration, the robot wizard only supports configuring robots that are already loaded in the stage. If you are starting with a URDF or MJCF file, go to **File > Import** can use the importer instead.

**Steps:**

1. Select **Configure a Robot on Stage**.
2. Indicate the type of the robot you are configuring from the dropdown menu. Pick **custom** if your robot does not fit into the other categories. This will automatically populate the links that are frequently used in the selected robot types in [Robot Hierarchy](#isaac-sim-app-tutorial-wizard-hierarchy).
3. Give your robot a name. You can change it later.
4. Select the parent link of the robot from stage.
5. Click **Prepare Files** to advance to the next step.

### Prepare Files

This page allows you to indicate the folder where the robot files will be saved. The resulting files are described in [Overview](#isaac-sim-app-robot-wizard-file-structure). While no files are created at this step, they will be created in the subsequent steps.

**Steps:**

1. The folder will be created in the format of `<Root Folder>/configurations/<robot-name>_base.usd`. You can change the name and the root folder.
2. The stage that is currently open will not be the final robot file. You may choose to save a copy of it in the `<Root Folder>/stage_copy.usd`. If it has unsaved changes, you will also have the choice to save it and overwrite the existing path.
3. The **Robot Files Allocated** displays the filepaths that will be created in the folder. If filepaths text turned purple in color, it means that the file already exists, proceeding without changing the filepath will overwrite the existing file. If it turns red, it means you do not have permission to write to the folder.
4. In the case where you are examining a robot that’s loaded to the stage as a reference or payload, the **Additional Information** section contains the path to the original file that the robot is loaded from.
5. Click **Robot Hierarchy** to advance to the next step.

### Robot Hierarchy

Assets in Isaac Sim are organized based on how the robot moves. All the components that move as a single link are grouped together under a single parent. This page allows you to organize your robot components accordingly.

| Ref # | Panel Name | Description |
| --- | --- | --- |
| 1 | New Link Structure | This section displays the new structure of the robot. This structure is based on the links. It might have existing links populated for you if you have chosen a robot type in [Add Robot](#isaac-sim-app-tutorial-wizard-add-robot). You can always add or remove links by using the buttons in the lower right hand corner. |
| 2 | Current Link Structure | This section displays the current structure of the robot that’s on stage. |
| 3 | Parent | The Parent button will be enabled after you’ve selected a target link from the window above and source links from the window below. Clicking on the button will parent the source link to the target link. |
| 4 | Unparent | The Unparent button will be enabled after you’ve selected a link from the window above. Clicking on the button will unparent the link from its parent. |
| 5 | Add/Remove Links | The Add/Remove buttons will add/remove links from the new link structure. |
| 6 | Clear All/Copy All | The Clear All button will clear all the links in the new link structure. The Copy All button will copy all the links in the current link structure to the new link structure. |
| 7 | Instructions | Expand to observe the instructions for the current step. |
| 8 | Add Colliders | The Next button will advance you to the add collider step. |

#### Notes

* The reorganization is focused on grouping different mesh components under a single parent when they belong to the same link. If you have robots where the mesh is nested under many layers of Xforms, choose only the mesh prim and move that to the top window, and delete (right click > delete) any leftover empty parent prims in the bottom window (old stage) where the mesh has been moved.
* It will also ignore any non-mesh prims, such as materials, joints, and textures. Those will be directly copied over to the new file under relevant parent prims.
* Any mesh that is not parented at the end will also get automatically copied over to the new file, unless explicitly deleted.
* The position of the links is set to align with a “reference child” prim. The reference child prim can be indicated by right clicking on the link in the top window, and selecting **Mark as Reference Child**. If no reference child is indicated through the stage, the link’s origin will be positioned at the origin of the first child. Consequently, the transform of all the child meshes will be recalculated to be relative to the parent link’s location.
* No actual prims are created or modified while on this page. All changes are implemented when clicking the **Add Colliders** button to move on to the next step.

### Add Colliders

This page allows you to examine and add the colliders of the robot.

At this point of the process, all the meshes are purely for visualization purposes. There are no colliders or rigid body physics applied to any of the meshes.

The table displays the existing meshes of the robot in the first column. The second column displays the collision approximation method that will be applied to the mesh after you complete the page and move on by clicking the **Add Joints & Drives** button. You can modify the approximation method using the dropdown menu.

For this iteration of the wizard, no new colliders can be created on this page. However, you can always manually add additional meshes and apply the necessary [Physics in USD Schemas](../physics/simulation_fundamentals.html#physics-schemas) directly in the USD file.

### Add Joints and Drives

This page allows you to add the joints and drives to the robot.

To add a joint, click on the **Create New Joint** button. A popup will appear.

Give the joint a name and select the type of the joint from the dropdown menu. Select the parent and child links the joint will connect, the axis that the joint will move along, and the driver type from the dropdown menu. Then **Create** or **Create & Close** to add the joint to the table on the main page.

To modify the settings for a particular joint, click on the joint name in the table. Two additional sections will appear. The first section allows you to modify the joint properties. The second section allows you to configure the drive. Selecting a different joint or moving to the next page will automatically save the settings for the previously edit joint.

No USD changes are made while on this page. All changes are implemented when clicking the **Save Robot** button to move on to the next step.

### Save Robot

This page finishes the process of creating the robot and creates the final robot files.

You must indicate the link or joint to be the “Articulation Root”. Think of this as the start of the joint chain. For fixed based robots, this is usually the fixed joint. For mobile robots, this is usually the chassis.

You can also choose to add a minimal environment to the main robot USD file. This can be a ground, a default light, and a PhysicsScene. These will be added outside of the Default Prim of the file, so that they will only show up when the original robot file is opened directly on stage, but not when the robot is added as a reference or payload into another scene. They are particularly useful for debugging purposes.

Click on the **Save Robot** button to finish the process.

## Tutorials

[Robot Wizard Tutorial [Deprecated]](robot_wizard_tutorials.html#isaac-sim-app-robot-wizard-tutorials)

On this page

* [Overview](#overview)
* [Wizard Steps](#wizard-steps)
  + [Page Orientation](#page-orientation)
  + [Add Robot](#add-robot)
  + [Prepare Files](#prepare-files)
  + [Robot Hierarchy](#robot-hierarchy)
    - [Notes](#notes)
  + [Add Colliders](#add-colliders)
  + [Add Joints and Drives](#add-joints-and-drives)
  + [Save Robot](#save-robot)
* [Tutorials](#tutorials)

---

### Robot Wizard Tutorials

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/robot_setup/robot_wizard_tutorials.html

* [Robot Setup](index.html)
* Robot Wizard Tutorial [Deprecated]

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Robot Wizard Tutorial [Deprecated]

Warning

**Deprecated:** The Robot Wizard extension (`isaacsim.robot_setup.wizard`) is deprecated since Isaac Sim 6.0.0 and will be removed in a future release.

This tutorial is a step-by-step guide for using the Robot Wizard to create a mock robot that contains a fixed base, a prismatic joint, and a revolute joint.
Load the prepared file for this tutorial onto stage. Go to `Isaac/Samples/Rigging/RobotWizard/` and open the original file for `raw_blocks.usd`.

For more in-depth explanation about the Wizard, refer to [Robot Wizard [Deprecated]](robot_wizard.html#isaac-sim-app-robot-wizard).

If the Wizard window is not already open, open it from **Window > Robot Wizard**. If you don’t observe the wizard under the Window menu, go to the **Window > Extensions** and enable **Isaac Sim Robot Wizard**.

## Instructions

### Add Robot Page

1. Select **Configure a Robot on Stage**.
2. Select **custom** in the dropdown list for Robot Type.
3. Give your robot a name. The name will be used as the robot’s parent prim name on stage.
4. If the robot prim is not already populated in the **Select Robot Parent Xform** field, click on the dropper and select **World** from the stage popup.
5. Click **Prepare Files** to complete this page.

### Prepare Files

1. Indicate the root folder to save the robot files. You can also modify the robot name here, if needed, for creating a new folder.
2. Check the **Save a Copy in Robot Root Folder** for the current stage and keep the default filepath when that field appears.
3. Click **Next** to move to the next page.

### Robot Hierarchy

1. Add a new link inside the **New Links Structure** window and name it “<robot\_name>/link3”.
2. Put Cube and Cone under `link1`, Cylinder under `link2`, and `Cylinder_01` and `Cube_01` under `link3`.
3. Click **Add Colliders** to finish this page.

Note

You are no longer looking at the original `raw_blocks.usd` file on stage. Instead, a new stage is opened with a robot that’s organized in the link structure you organized in the **Robot Hierarchy** page. This might look a little strange in the viewport.

Take a look at the **Stage** window, verify that in addition to the new robot with the new structure, there are also three new “Scopes” added to the stage:

* **meshes** scope contains the original meshes from the `raw_blocks.usd` file. Each link is a separate mesh, and each mesh has a (0,0,0) origin, that is why there are two copies of each shape, some of them appearing to be clustered in the center of the grid.
* **visuals** scope contains the visual meshes for each link. They are references pointing towards meshes inside the “meshes” scope that are being used for visual purposes.
* **colliders** scope contains the collision meshes for each link. They are also references, but pointing to the meshes inside the “meshes” scope that are used for collision detections. For basic shapes, the visual and collider meshes are often the same. For complex shapes, it is computationally performant to use an approximated version of the visual mesh, such as the bounding volume or convex hull. This allows for faster physics computation while retaining the visual accuracy.

Verify that the main robot prim contains the links as its immediate children, and that each link prims contains the visual and collider meshes as its immediate children. Additional scopes (folders) and a placeholder folder for the joints are created to organize the materials.

To observe what the new robot looks like without the original meshes distraction, hide the “meshes”, “visuals”, and “colliders” scopes.

### Add Colliders

1. For this particular asset, where the shapes are basic, there’s nothing to do on this page. If you are configuring a robot with more complex shapes, you can modify the collision approximation on the right hand column for level of accuracy.
2. Click **Add Joints & Drives** to move on to the next page.

Note

Everything prior to adding the colliders are considered fundamental to the definition of the robot, therefore are saved in the base layer. Rigid Body APIs, Collision APIs, and Joint and Drive APIs are specifically adding properties and setting for physics simulation, and therefore are applied to the physics sublayer of the robot. To inspect the layers, click on the **Layers** tab next to the **Stage** tab in the main Isaac Sim window. Verify that you are editing the physics layer, which has the base layer included as a sublayer.

### Add Joints and Drives

1. Click on the **Create New Joint** button to add a new joint.
2. Make three joints for this robot. Select **Create** to add the first two, and **Create & Close** to add the third.

| Joint Name | Joint Type | Axis | Parent Link | Child Link | Driver Type |
| --- | --- | --- | --- | --- | --- |
| fixed\_joint | Fixed | — | — | <robot\_name>/link1 | (not used) |
| slider\_joint | Prismatic | X | <robot\_name>/link1 | <robot\_name>/link2 | force |
| rotate\_joint | Revolute | Z | <robot\_name>/link2 | <robot\_name>/link3 | force |

3. Click on the joint name in the table to open the joint settings for the joint. Update the joint parameters for the `slider_joint` with the Prismatic Joint settings below, and for the `rotate_joint` with the Revolute Joint settings below.

**Prismatic joint**

> * set the joint limit to 0 to 3
> * set the target position to 1
> * set the stiffness to 1e5 and damping to 2e4

**Revolute joint**

> * uncheck the **Joint Range is Limited** checkbox so that this joint can rotate perpetually
> * set the target velocity to 100
> * set the stiffness to 0 to enable pure velocity drive

4. Click **Save Robot** to save the robot and move on to the next page.

Verify that the Joints folder is populated with the three created joints. You can confirm the settings for each joint by clicking on the joint name in the stage tree. Then use the property panel to validate the joint and drive parameters.

### Save Robot

1. Select the “fixed\_joint” as the “Articulation Root”.
2. Select to add a light and physics scene to the main robot file. The ground is optional because the robot has a fixed joint to the world.
3. Click **Save Robot** to finish the process.

After saving the robot, all the appropriate USD files are created in the robot root folder. Verify that the viewport has the robot from the main robot file with physics variant applied.

Click play to observe the joints move. Validate that the slider joint moves to a target position and that the revolute joint rotates perpetually.

## Final Product Summary

Here is summary of all the things that were done by the wizard. There is a final product for you to compare against your own results in the `Isaac/Samples/Rigging/RobotWizard/final/` folder.

**Robot Hierarchy**:

There is still a vestigial `/World` prim on stage, for now, you can manually move the content into the robot prim’s corresponding folders.

**Files and Folders created**:

```python
robot_root_folder/
├── configurations/
│   └── <robot-name>_robot.usd
│   └── <robot-name>_physics.usd
│   └── <robot-name>_robot.usd
└── <robot-name>.usd
└── stage_copy.usd
```

**APIs applied**:

The APIs applied can be found by selecting the prim on stage and examining the properties panel.

```python
robot_prim (RobotAPI)
├── link1 (RigidBodyAPI, LinkAPI)
│   └── visual
│   ├── collider
│       └── <mesh>  (ColliderAPI)
├── link2 (RigidBodyAPI, LinkAPI)
│   └── visual
│   ├── collider
│       └── <mesh>  (ColliderAPI)
├── link3 (RigidBodyAPI, LinkAPI)
│   └── visual
│   ├── collider
│       └── <mesh>  (ColliderAPI)
├── Joints
│   └── fixed_joint (JointAPI, ArticulationRootAPI)
│   └── slider_joint (JointAPI, DriveAPI, JointStateAPI)
│   └── rotate_joint (JointAPI, DriveAPI, JointStateAPI)
```

## Next Steps

* [Gain Tuner Extension](ext_isaacsim_robot_setup_gain_tuner.html#isaac-gain-tuner)
* [Robot Assembler](assemble_robots.html#isaac-sim-app-tutorial-advanced-assembling-robots)
* [Tutorial: Export URDF](../importer_exporter/export_urdf.html#isaac-sim-app-tutorial-export-urdf)

On this page

* [Instructions](#instructions)
  + [Add Robot Page](#add-robot-page)
  + [Prepare Files](#prepare-files)
  + [Robot Hierarchy](#robot-hierarchy)
  + [Add Colliders](#add-colliders)
  + [Add Joints and Drives](#add-joints-and-drives)
  + [Save Robot](#save-robot)
* [Final Product Summary](#final-product-summary)
* [Next Steps](#next-steps)

---

### Robot Setup Troubleshooting

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/robot_setup/troubleshooting.html

* [Help & FAQ](../overview/help.html)
* [Troubleshooting](../overview/troubleshooting.html)
* Robot Setup Troubleshooting

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Robot Setup Troubleshooting

This page consolidates troubleshooting information for robot setup and simulation in Isaac Sim.

## Reparenting Assets

You can change how reparenting behaves under **Edit > Preferences**, and on the **Stage Panel**, scroll down to authoring. The checkbox **Keep Prim world Transform when reparenting**, lets you decide when reparenting if the objects remain in place or if they get moved to the parent’s frame of reference. You can use this to your advantage to apply offsets or change the parent’s origin without impacting the children elements.

## Robot Rigging Issues

If your robot “explodes” during simulation or after some movements, check if any of the collision meshes are colliding with each other.

Common rigging issues and their solutions:

1. Colliding collision geometries - Ensure that collision geometries do not intersect or overlap, especially at joint pivot points
2. Joint limit violations - Verify that joint limits are set appropriately and not being exceeded during simulation
3. Incorrect joint ordering - Make sure that joint orderings in articulation chains are correct
4. Physics instabilities - Adjust physics timestep or solver iteration counts if experiencing vibrations or instabilities

Physics Inspector “failed to find internal joint” errors for robots with mimic joints does not affect the functionality of the mimic joints and can be ignored:

```python
[Error] [omni.physx.plugin] Usd Physics: failed to find internal joint object for PhysxMimicJointAPI at /Franka/panda_hand/panda_finger_joint2. Please ensure that the prim is a supported joint type and is part of an articulation.
```

## Robot Controller Issues

1. Gains produced by the gain turner may not perfectly track the robot’s commanded movements (for example, as seen in the Cobotta Pro robot). Manual tuning of gains may be necessary for optimal performance.
2. Some grippers with parallel mechanism (that is, Robotiq 2F-85 and 2F-C2) have links that do not move with rest of the gripper. This is a known issue and may require manual adjustment of the gripper joints.
3. When working with differential drive robots, make sure that wheel friction is appropriate. Too little friction can result in wheel slippage, while too much friction can cause erratic movement.

## Robot Import Issues

USD to URDF Exporter issues:

* The Collider meshes may be improperly included in the visuals. They can be manually removed from the URDF file.
* The Body and Joints are authored in the URDF file in alphabetical order. They can be manually reordered in the URDF file.
* Depending on the robot structure, some body names may be overridden due to the merging of different frames. Review the output and verify that it’s accurate.
* The URDF exporter adds joint effort and velocity limits as inf when unbounded. This may make the URDF not import correctly if the URDF parser does not support inf values in Float.

When importing a URDF:

1. If more than one asset in URDF contains the same material name, only one material is created regardless if the parameters in the material are different. For example, if two meshes have materials with the name “material”, one is blue and the other is red, both meshes will be either red or blue. This also applies for textured materials.
2. MJCF importer does not show the built-in bookmark in the file picker dialog. The bookmark is still available in the content pane and can be copy-pasted into the file picker dialog.

## Closed Loop Structure Issues

For robots with closed-loop kinematic chains:

1. Make sure that the constraints are properly defined and initialized
2. Check that all joints in the closed loop have appropriate drive settings
3. Consider simulating the closed loop as separate articulations with constraints rather than with a single complex closed-loop structure
4. Adjust solver settings for better convergence if experiencing stability issues

## Robot Importing tips

1. Sometimes the robot may have non-zero target positions. When the target position does not match the initial position, the robot will move to the target position on the first frame. To prevent this, either set the target position to zero or set the initial position to the target position.
2. Max forces may be high or low in the URDF, set them to a more reasonable value in the USD.
3. If the stiffness and damping values are too high, the robot may oscillate. If it’s too low, the robot may not move to the desired position. Use the gain tuner to test the stiffness and damping.
4. If the robot have overlapping collision meshes, use a filtered pair to ignore collisions between specific meshes.

## Common Issues

| Observation | Solution |
| --- | --- |
| Robot meshes are penetrating each other after importing | Verify the source file (MJCF or URDF) have the correct transforms for the meshes. Adjust the transforms in the source file or in the USD after importing. |
| Robot joints are not moving at all | Check the joint limits and ensure they are set correctly. Adjust the limits in the source file or in the USD after importing. Verify that the joint gains are non zero. If you have mimic joints, make sure the gear ratio and direction are set correctly. One suggestion is to disable all the joints first, and then add them back one by one to isolate the issue. |
| Robot joints are moving in the wrong direction | Check the joint axis and ensure they are set correctly. Adjust the joint axis in the source file or in the USD after importing. For mimic joints, verify that the direction is set correctly. |
| Robot shakes uncontrollably starting from the first frame | Usually, conflicting collisions can generate adnormal amount of force which cause the robot to behave incorrectly. Check for self overlapping collision geometries. Uncheck self collision enabled in Articulation Root if self collision is not needed. If self collision is required, apply contact filter to specific pairs of colliders that should not collide. |
| Robot shakes uncontrollably after some movements | This usually happens when the robot gains are too high and generating adnormal amount of torque. Try increasing the physics substeps and solver iteration counts in the Physics Settings window. You can also try reducing the robot’s maximum velocity and force limits to prevent extreme movements. |
| Robot experiences physX transform errors | This usually happens when the robot is under extreme forces or torques similar to the previous scenario and it can be induced by conflicting joint transformations. First disable all the joints and see if the issue persists. If the issue is resolved, re-enable the joints one by one to isolate the problematic joints. Check for conflicting joint limits or positions. |
| The robot is penetrating the ground or other objects on the first frame | Check the initial position of the robot and ensure it is above the ground plane and not intersecting with any meshes. Verify that the collision geometries are correctly defined and not intersecting with other objects at the start of the simulation. |
| The robot is penetrating the ground or other objects during simulation | Adjust the physics timestep and solver iteration counts to improve stability, modify the contact offset of the colliders to ensure proper collision detection, and verify that the robot’s mass and inertia properties are realistic. |
| The simulation performacne is slow at run time | Reduce the number of collision meshes and simplify their geometry by using simliar colliders, and adjust the physics timestep and solver settings for better performance. |
| The robot joints are not following the commanded positions accurately | Tune the joint gains using the [Gain Tuner Extension](ext_isaacsim_robot_setup_gain_tuner.html#isaac-gain-tuner), ensure that the maximum velocity and force limits are set appropriately, and verify that there are no conflicting forces acting on the robot. |

On this page

* [Reparenting Assets](#reparenting-assets)
* [Robot Rigging Issues](#robot-rigging-issues)
* [Robot Controller Issues](#robot-controller-issues)
* [Robot Import Issues](#robot-import-issues)
* [Closed Loop Structure Issues](#closed-loop-structure-issues)
* [Robot Importing tips](#robot-importing-tips)
* [Common Issues](#common-issues)

---


## Setup 教程

### Setup Tutorials Index

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/robot_setup_tutorials/index.html

* [Robot Setup](../robot_setup/index.html)
* Robot Setup Tutorials Series

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Robot Setup Tutorials Series

The GUI tutorials walk you through setting up your virtual world and building robot digital twins with various NVIDIA Isaac Sim features. In the process, you will learn where to find frequently used properties, settings, and tools, and familiarize yourself with the toolbars, icons, and OpenUSD standards.

**Important:** These tutorials are designed as a progressive learning path from beginner to advanced. We recommend starting with the *Setup a Wheeled Robot* section, as it covers essential beginner concepts like environment setup, basic robot assembly, and fundamental rigging techniques that are required for all robot types.

## **Beginner Level** - Setup a Wheeled Robot

Start here to learn fundamental concepts that apply to all robot types:

* [Tutorial 1: Stage Setup](tutorial_intro_environment_setup.html)
* [Tutorial 2: Assemble a Simple Robot](tutorial_intro_assemble_robot.html)
* [Tutorial 3: Articulate a Basic Robot](tutorial_gui_simple_robot.html)
* [Tutorial 4: Add Camera and Sensors to a Robot](tutorial_gui_camera_sensors.html)
* [Tutorial 5: Rig a Mobile Robot](rig_mobile_robot.html)

## **Intermediate Level** - Setup a Manipulator

Build upon the foundational knowledge to work with more complex robot structures:

* [Tutorial 6: Setup a Manipulator](tutorial_import_assemble_manipulator.html)
* [Tutorial 7: Configure a Manipulator](tutorial_configure_manipulator.html)
* [Tutorial 8: Generate Robot Configuration File](tutorial_generate_robot_config.html)
* [Tutorial 9: Pick and Place Example](tutorial_pickplace_example.html)

## **Advanced Level** - Asset Tuning and Optimization

Master advanced techniques for complex robot configurations:

* [Tutorial 10: Rig Closed-Loop Structures](rig_closed_loop_structures.html)
* [Tutorial 11: Tuning Joint Drive Gains](joint_tuning.html)
* [Tutorial 12: Asset Optimization](optimizing_asset.html)
* [Tutorial 13: Rigging a Legged Robot for a Locomotion Policy](tutorial_rig_legged_robot.html)

On this page

* [**Beginner Level** - Setup a Wheeled Robot](#beginner-level-setup-a-wheeled-robot)
* [**Intermediate Level** - Setup a Manipulator](#intermediate-level-setup-a-manipulator)
* [**Advanced Level** - Asset Tuning and Optimization](#advanced-level-asset-tuning-and-optimization)

---

### Joint Tuning

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/robot_setup_tutorials/joint_tuning.html

* [Robot Setup](../robot_setup/index.html)
* [Robot Setup Tutorials Series](index.html)
* Tutorial 11: Tuning Joint Drive Gains

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Tutorial 11: Tuning Joint Drive Gains

## Learning Objectives

In this tutorial, you use the Gain Tuner to bring an un-tuned UR10 manipulator from zero gains to a working set of stiffness and damping values. Along the way you learn how to:

* Diagnose missing or insufficient gains with the **Snap-to-Limits** test.
* Distinguish **Fail** from **Blocked** results using the **Disable Self-Collisions** toggle.
* Validate tuned gains with the **Stress Test** and observe how velocity limits contribute to solver stability.

For a full explanation of how the Gain Tuner works, the physics behind joint drives, and the complete parameter reference for each test, see [Gain Tuner Extension](../robot_setup/ext_isaacsim_robot_setup_gain_tuner.html#isaac-gain-tuner).

*10-15 Minute Tutorial*

## Prerequisites

* Complete the [Tutorial: Import URDF](../importer_exporter/import_urdf.html#isaac-sim-app-tutorial-advanced-import-urdf) tutorial to import the UR10 onto the stage. The URDF importer sets all joint stiffness and damping to zero by default, so the robot has no active drives.
* Read the [Gain Tuner Extension](../robot_setup/ext_isaacsim_robot_setup_gain_tuner.html#isaac-gain-tuner) reference for background on the parameters, physics, and detailed result interpretation guide.

## Step 1: Open the Gain Tuner and observe zero gains

1. Go to **Tools** > **Robotics** > **Asset Editors** > **Gain Tuner**.
2. Select the UR10 from the **Select Robot** dropdown.
3. Ensure that **Mode** is set to **Position** for each joint.
4. Observe that all six joints — `shoulder_pan_joint`, `shoulder_lift_joint`, `elbow_joint`, `wrist_1_joint`, `wrist_2_joint`, `wrist_3_joint` — have **Stiffness** and **Damping** set to `0`. With zero gains the robot has no active drives and will collapse under gravity when the simulation is played.

## Step 2: Snap-to-Limits with weak gains

Set initial gains to see how the robot responds with deliberately low stiffness and no damping:

1. In the **Stiffness** column, set all six joints to `10`. Leave **Damping** at `0`.
2. Select the **Snap-to-Limits** test mode (the default).
3. Enable the **Test** checkbox for all joints.
4. Press **Play**, then press **Run Test**.

With stiffness at only 10 Nm/rad and no damping, expect:

* `shoulder_lift_joint` and `elbow_joint` are likely to **Fail**. These joints bear the full weight of the arm and 10 Nm/rad of stiffness is far too low to drive them to their limits.
* Wrist joints may also **Fail** or show long settling times with oscillation, since there is no damping to absorb overshoot.
* Some joints may report **Blocked** if the collision geometry prevents them from reaching a limit.

Note

If a joint reports **Blocked**, re-run with **Disable Self-Collisions** enabled. If the joint then passes, the joint limit extends beyond what the collision geometry allows — tighten the joint limit in USD rather than adjusting gains.

## Step 3: Tuned parameters

Before adjusting gains, check the joint force limits. The UR10’s URDF defines max effort values (330 Nm for the shoulder joints, 150 Nm for the elbow, 56 Nm for the wrist joints) that are imported as the joint **Max Force** in USD. With high stiffness, the PD controller may need to apply forces that exceed these limits to drive the heavy shoulder and elbow links to their targets. If a joint still fails Snap-to-Limits after increasing stiffness, select the joint in the **Properties** panel and set **Max Force** to a higher value or to `inf` (infinite) under **Joint** > **Advanced** > **Maximum Force**. For the UR10, `shoulder_pan_joint` and `shoulder_lift_joint` require infinite max force to pass.

The following gains produce a UR10 that passes Snap-to-Limits. They were found using the position-drive tuning heuristic described in the [Tuning Workflow](../robot_setup/ext_isaacsim_robot_setup_gain_tuner.html#isaac-gain-tuner-tuning-workflow) section of the Gain Tuner reference:

| Joint | Stiffness | Damping |
| --- | --- | --- |
| `shoulder_pan_joint` | 500000 | 50 |
| `shoulder_lift_joint` | 500000 | 50 |
| `elbow_joint` | 50000 | 50 |
| `wrist_1_joint` | 500 | 0.5 |
| `wrist_2_joint` | 500 | 0.5 |
| `wrist_3_joint` | 50 | 0.0 |

Note

These values are starting-point examples. Fine-tune them for your specific application by iterating with the Gain Tuner tests. The shoulder and elbow joints require higher gains because they bear the weight of the full arm, while the lighter wrist joints respond well at lower values.

Enter these values, re-run the Snap-to-Limits test, and confirm that all joints now **Pass**.

You can further validate tracking quality with the **Sinusoidal** and **Step Function** test modes. For configuration details and result interpretation, see [Sinusoidal](../robot_setup/ext_isaacsim_robot_setup_gain_tuner.html#isaac-gain-tuner-sinusoidal) and [Step Function](../robot_setup/ext_isaacsim_robot_setup_gain_tuner.html#isaac-gain-tuner-step-function).

## Step 4: Stress Test with tuned gains

With the tuned gains from [Step 3: Tuned parameters](#tuned-ur10-gains-table) applied, run the Stress Test to verify the robot is stable under the extreme commands typical of reinforcement learning training:

1. Select the **Stress Test** mode and choose the **Random Walk** sub-mode.
2. Set **Sequence** for all joints to `1` so that the joints are tested in parallel.
3. Leave **Disable Velocity Limits** off (the default).
4. Press **Play**, then press **Run Test**.
5. All joints should report **Stable**.

Now observe what happens without velocity limits:

1. Enable **Disable Velocity Limits**.
2. Press **Run Test** again.
3. Some joints now report **Unstable**.

Without velocity limits, the PD controller responds to the stress test’s large position errors by generating forces that accelerate joints to extreme speeds within a single simulation timestep. At these speeds the discrete-time solver can fail to converge, leading to energy blowup or NaN values.

Velocity limits serve two purposes:

* **Physical fidelity** — real actuators have maximum speeds defined by the manufacturer. The UR10’s URDF specifies velocity limits of approximately 2–3 rad/s per joint. Setting these in simulation reproduces the real robot’s motion envelope.
* **Solver stability** — by capping joint speed, velocity limits keep per-step displacements within the range where the PhysX implicit integrator remains numerically stable.

If your application requires higher velocity limits than the manufacturer specification, increase them incrementally and re-run the Stress Test after each change to confirm the solver remains stable at the new limits.

Repeat the comparison in **Adversarial** sub-mode to confirm the same behavior under worst-case correlated configurations.

Note

A **Stable** result is meaningful only at the sigma and snap interval values used. When assessing readiness for Isaac Lab training, record these parameters alongside results. See [Stress Test](../robot_setup/ext_isaacsim_robot_setup_gain_tuner.html#isaac-gain-tuner-stress-test) for a full explanation of how to interpret each result combination.

### Summary

This tutorial covered:

1. Starting from an un-tuned UR10 imported from URDF with zero gains.
2. Using Snap-to-Limits to identify joints with insufficient stiffness and distinguishing Fail from Blocked results.
3. Applying tuned gains and confirming all joints pass Snap-to-Limits.
4. Using the Stress Test to demonstrate why velocity limits are important for solver stability.

On this page

* [Learning Objectives](#learning-objectives)
* [Prerequisites](#prerequisites)
* [Step 1: Open the Gain Tuner and observe zero gains](#step-1-open-the-gain-tuner-and-observe-zero-gains)
* [Step 2: Snap-to-Limits with weak gains](#step-2-snap-to-limits-with-weak-gains)
* [Step 3: Tuned parameters](#step-3-tuned-parameters)
* [Step 4: Stress Test with tuned gains](#step-4-stress-test-with-tuned-gains)
  + [Summary](#summary)

---

### Optimizing Asset

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/robot_setup_tutorials/optimizing_asset.html

* [Robot Setup](../robot_setup/index.html)
* [Robot Setup Tutorials Series](index.html)
* Tutorial 12: Asset Optimization

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Tutorial 12: Asset Optimization

## Learning Objectives

This tutorial details how to make robot assets more performant and where to find tradeoffs to achieve a faster simulation or rendering time.

*30 Minutes Tutorial*

## Getting Started

**Prerequisites**

* Complete the [Quick Tutorials](../introduction/quickstart_index.html#isaac-sim-intro-quickstart-series) series to learn the basic core concepts of how to navigate inside NVIDIA Isaac Sim.
* Complete the [Assemble a Simple Robots](tutorial_gui_simple_robot.html#isaac-sim-app-tutorial-gui-simple-robot) tutorial to learn the concepts of rigid body API, collision API, joints, drives, and articulations.
* Read [Onshape importer](https://docs.omniverse.nvidia.com/extensions/latest/ext_onshape.html "(in Omniverse Extensions)") and watch the videos on rigging the robot in Onshape.
* Familiarity with [Mesh Merge Tool](../robot_setup/ext_isaacsim_util_merge_mesh.html#isaac-merge-mesh).

**Loading the Robot**

This tutorial explores the NVIDIA Jetbot Robot asset which improve performance.
If you import the asset from a different source, for example from custom CAD, you might end up with numerous meshes per rigid body and this can severely impact performance.

From the recording of this Jetbot asset imported from CAD that on the right side we have an unoptimized asset, and it’s achieving 40 FPS, while the asset on the left was optimized, and now achieves 64 FPS.

## Asset Structure Optimization

In this activity, you use a workflow with the multi-layered asset structure introduced in an earlier module,
and create an optimized version of an asset.
Use the Jetbot robot as a starting place. This model was imported from a CAD model made in Onshape.
Although the physics layer is already in place, the bodies contain a significant number of meshes, which leads to suboptimal simulation performance.
Begin with an empty stage to learn several useful tricks for asset authoring.
By the end of this activity, you transform the initial Jetbot model into a well-structured, optimized asset ready for efficient simulation.

### Set Up Reparenting and Layers

1. In Isaac Sim, go to **Edit** > **Preferences** to open the Preferences panel.
2. Under **Stage** > **Authoring**, next to the \*\* Keep Prim World Transform When reparenting\*\*, ensure that **Inherit Parent Transform** is selected.
3. Open the Jetbot located at `Isaac Sim/Samples/Rigging/Jetbot/Jetbot_Optimized/Jetbot_optimized.usd`, verify that you have an empty USD.
4. Select the **Layers** panel, click the **Insert Sublayer** button at the bottom of the tab, select `Isaac Sim/Samples/Rigging/Jetbot/Jetbot_Base/Jetbot_base.usd`, and click **Open**.

### Create Asset Structure

The Jetbot asset is already close to the final goal, but to work on a retargeting of the structure to get the merged meshes,
create a new prim to be set as default.

1. On the right side menu of the Stage panel, select **Show Root**.
2. Create a new Xform called `Jetbot_Sim` and drag it onto Root.
3. Right click on `Jetbot_Sim` and choose **Set as Default Prim**.
4. Right click and choose **Create** > **Scope** and name it `Visuals`.
5. Drag this scope onto Root so it’s unparented from `Jetbot_Sim`.
6. Select the prims under `Jetbot` and drag them onto `Jetbot_Sim`.

   > Note
   >
   > To select multiple prims, use shift-select or control-select standards. For example: select one prim, then hold shift and another to choose all prims listed between them.
7. Verify that instead of being deleted from Jetbot, they were instead deactivated.
8. Select them all, then right-click and choose **Activate**.
9. Delete the contents inside the prims in `Jetbot_Sim`.

### Merge Meshes

With the stage ready, you can begin merging the meshes.

Note

The Mesh Merge Tool is deprecated and will be removed in a future release. Use the Scene Optimizer extension instead.

First, enable the merge mesh tool by going to **Window** > **Extensions** and search for **Isaac Sim Mesh Merge** or **isaacsim.util.merge\_mesh** in the deprecated extensions and toggle it on.

1. Open the Mesh Merge Tool by going to **Tools** > **Robotics** > **Asset Editors** > **Mesh Merge Tool**.
2. Select `Jetbot/left_wheel` prim.
3. Check the **Combine Materials** box, insert `Jetbot_Sim/Looks` to save the material in the Jetbot Sim xform.
4. Click on **Merge**.
5. Select the resulting mesh on `/Merged/left_wheel` and clear the transform on the properties panel.
6. Right-click on the **Visuals** scope, create an xform called `left_wheel` and drag the resulting mesh into it. Remove the `/Merged` xform from the stage.
7. To create an internal reference to the wheel, create a **Visuals** Xform inside `left_wheel`, then right-click it and choose **Add** > **Reference**.
8. Select `Isaac Sim/Samples/Rigging/Jetbot/Jetbot_Base/Jetbot_base.usd` in the dialog.
9. For `prim_path`, type in `/Visuals/left_wheel`.
10. Back in the **Stage** panel, select the `/Jetbot_Sim/Visuals/left_wheel` prim, which you just added a reference onto. Then in the **Property** panel, scroll down to the **References** section. The prim path is in red, select the Asset Path entry and **clear** it.
11. This will make the reference point to the internal `/Jetbot_Sim/Visuals/left_wheel` prim. The mesh for `left_wheel` shows as a child. Verify that a **Looks** scope was created in `Jetbot_Sim`, with the materials for this mesh.
12. Verify that the wheel is referenced correctly in place, along with the base mesh that is at the origin. You can hide the Visuals scope so base meshes won’t be visible.
13. Save the file with CTRL+S.
14. To complete the mesh optimization, repeat the previous steps for other bodies.

Note

The finished USD with all mesh merges is available for you at `Isaac Sim/Samples/Rigging/Jetbot/Jetbot_Optimized/Jetbot_optimized_post_merge.usd`.

## Scenegraph Instancing

Scenegraph instancing enables sharable, composed representations of subgraphs of prims. It is a directive that instructs the scene composer that a certain component of the scene is a repeatable pattern. While this allows for a leaner overall scene, it does require a few rules to be followed.

Any children of an instance cannot have attributes modified, because they all inherit from the same asset in memory.
Instances must be applied on Referenced assets, so that the scenegraph composer knows that from the reference and downwards, things are expected to remain the same and it needs to create a pointer to the asset data to be used anywhere it’s referenced.

1. Start by opening the USD file `Isaac Sim/Samples/Rigging/Jetbot/Jetbot_Optimized/Jetbot_optimized_post_merge.usd`, if you have not merged all the meshes.
2. The left and right wheel meshes are identical. Further simplify the asset by having left and right wheel reference the same mesh. Select `Visuals/left_wheel` and rename it to `Visuals/wheel`.
3. Delete `Visuals/right_wheel`. Verify that the Jetbot wheel disappears.
4. Select `Jetbot_Sim/right_wheel/Visuals`.
5. Under the References section of the **Property** panel, replace the reference Prim Path from `/Visuals/right_wheel` to `/Visuals/wheel`.

   At this point, all meshes are still considered unique elements because the assets are only defined as a reference.
6. To leverage memory savings, shift-select all Visuals prims under `/Jetbot_Sim` and check **Instanceable** in the Property panel.
7. On the Visuals prims, notice the reference icon now has a blue “I” on it. This indicates they are instantiable meshes and effectively applying any memory savings.
8. Save the file with CTRL+S.

Note

The finished USD with all mesh merges and scenegraph instancing is available for you at `Isaac Sim/Samples/Rigging/Jetbot/Jetbot_Optimized/Jetbot_optimized_final.usd`.

## Other Considerations

* **Minimize Number of Lights**: Each light negatively impacts the performance of the rendering. By default, if the scene has more than 10 lights, the rendering reverts to sample-based lighting to avoid severe slowdown in performance.
* **Reduce Translucent Materials**: Each translucent material generates a larger performance bottleneck than the default OmniPBR material.
* **Optimize Physics Performance**: Search for simulation aspects that you can modify to reduce computational cost. Typically, colliders have high computational costs. The more basic that you can make a collision shape, the more performant the simulation behaves. Reducing the number of contact points can also bring huge performance benefits. Tuning this can take several experiments to achieve the best precision versus performance point for your situation.
* **Approximate Wheel Colliders**: If you have a wheel collider, consider using a simple cylinder or sphere collider instead of a mesh collider. This can significantly improve performance and allows the robot to drive smoothly over terrains.

On this page

* [Learning Objectives](#learning-objectives)
* [Getting Started](#getting-started)
* [Asset Structure Optimization](#asset-structure-optimization)
  + [Set Up Reparenting and Layers](#set-up-reparenting-and-layers)
  + [Create Asset Structure](#create-asset-structure)
  + [Merge Meshes](#merge-meshes)
* [Scenegraph Instancing](#scenegraph-instancing)
* [Other Considerations](#other-considerations)

---

### Rig Closed Loop Structures

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/robot_setup_tutorials/rig_closed_loop_structures.html

* [Robot Setup](../robot_setup/index.html)
* [Robot Setup Tutorials Series](index.html)
* Tutorial 10: Rig Closed-Loop Structures

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Tutorial 10: Rig Closed-Loop Structures

Some models are challenging to represent. Robots and grippers still have unique features and structures that are uncommon. In this document you learn some techniques to model these unique features and learn a general approach for managing these unique configurations.

## Learning Objectives

In this tutorial, you will:

* Use USD Layers to edit and test assets
* Add materials and adjust joints post CAD import
* Break a closed loop articulation chain
* Add joint drives, including mimic joints
* Adjust collision shapes
* Test grippers by building a test setup and using a gripper controller OmniGraph

*30 Minutes Tutorial*

Start with a [Robotiq 2F-85 Parallel Gripper](https://robotiq.com/products/2f85-140-adaptive-robot-gripper) STP file imported into an [Onshape document](https://cad.onshape.com/documents/02712153b53a69118b4e5c99/w/e4160a7cfa8bb14f2585a92f/e/6d63d85251b40eee71da6b56) and with joints modeled. This tutorial does not directly cover tuning the joints. Instead, tuned parameters are provided when configuring the asset. To learn more about gains tuning see [Tutorial 11: Tuning Joint Drive Gains](joint_tuning.html#isaac-sim-app-tutorial-advanced-joint-tuning) and [Gain Tuner Extension](../robot_setup/ext_isaacsim_robot_setup_gain_tuner.html#isaac-gain-tuner).

## Getting Started

**Prerequisite**

* Complete the [Quick Tutorials](../introduction/quickstart_index.html#isaac-sim-intro-quickstart-series) series to learn the basic core concepts of how to navigate inside NVIDIA Isaac Sim.
* Complete the [Assemble a Simple Robot](tutorial_gui_simple_robot.html#isaac-sim-app-tutorial-gui-simple-robot) and [Adding Sensors and Cameras](tutorial_gui_camera_sensors.html#isaac-sim-app-tutorial-gui-camera-sensors) tutorials to learn the concepts of rigid body API, collision API, joints, drives, and articulations.
* Read [Onshape importer](https://docs.omniverse.nvidia.com/extensions/latest/ext_onshape.html "(in Omniverse Extensions)") and watch the videos on rigging the robot in Onshape.
* Have a version of the Robotiq 2F-85 Gripper imported in Onshape and model the joints that connect the fingers together and to the body.

Note

The Onshape document used in this tutorial is publicly available. The imported USD asset is located at `Samples/Rigging/Gripper/Robotiq 2F-85` to get started.

## Rigging the Robot

### Using Layers to Edit and Test an Asset

All the rigid body, masses, and joint definition are done in [Onshape](https://docs.omniverse.nvidia.com/extensions/latest/ext_onshape.html#configuring-mates-for-physics). After they are imported to Isaac Sim, the asset contains basic joint information and rigid body setup. You must complete a few additional steps to make the asset fully functional.

Instead of opening the original asset, edit the asset using **layers**. Layers allow for building a scene on top of a root asset and saving it without changing the underlying root layer assets. For example, you can add a ground plane and objects used to test the gripper, save the testing setup in the layers, while keeping the original gripper asset free of any extraneous items used for testing.

1. Create a new stage without the reference added during import.
2. Save this stage with the name `Robotiq_2F_85_config.usd` at the same folder as the imported assets (you can locate the source file in the Reference or Payload section on the Property panel, and click the “Locate file” icon).
3. Open the layer tab and drag the `Robotiq_2F_85_edit.usd` in the **Root Layer**.

There is also a file named `Robotiq_2F_85_base.usd` in the source folder. This is the clean stage post import from Onshape and must not be directly edited to facilitate updates when the asset is re-imported from Onshape.

The *Authoring layer* is where changes are saved. To switch between layers, double-click on the choice.

If changes are made in the wrong authoring layer, you can drag the prims with the delta between layers to merge them into the receiving layer. Use this to your benefit by first authoring everything in the Root layer. After you are satisfied, you can drag your updates to the `Robotiq_2F_85_edit.usd` layer.

This is how the joints were named for this asset:

Note

Remember to combine parts that make rigid bodies on Group Mates before importing, to simplify the rigid bodies on stage (also useful for renaming the fingers to `left_finger_...` and `right_finger_...`).

## Adjusting Joints Post Import

Sometimes a limitation with the Onshape Client API causes the joints to become flipped 180 degrees from the drawing. To fix that, select the joints that are flipped, and apply an equal 180 degrees offset in Rotation 0 and Rotation 1 X axis. With the asset you imported, this was the case on the four joints.

The joints `[left, right]_outer_finger_joint` require limits [0,180] and `[finger_joint, right_outer_knuckle_joint]` require limits [0, 75]. Leave all other joints unconstrained.

Add fingertip physics material to increase the friction contact:

1. Open the Menu **Create** > **Physics** > **Physics Material**.
2. Select **Rigid Body Material**.
3. Rename the material to `fingertip_material`.
4. Set both friction coefficients to 0.8 (default rubber) and **Friction Combine Mode** `max`.
5. Select `right_inner_finger` and `left_inner_finger`. In the **Property** tab, in **Materials on selected models** pick the created material.

Note

you may need to de-select instanceable for the two xforms in `right/left_inner_finger`, and set the physics materials on the mesh `Defeatured_2F_85_PAD_OPEN_fingertipsstep` directly.

## Breaking the Articulation Loop

If you try to simulate this asset now, you’ll get two big warnings on the screen:

For more information, see [Physics Simulation Fundamentals](../physics/simulation_fundamentals.html#simulation-fundamentals). Articulations must be kinematic trees, but there is no need to delete any joints. To eliminate those warnings, you must choose one joint to exclude from the Articulation and have it be treated as a maximal coordinate joint. Because maximal coordinate joints are treated with a lower priority by the solver, it is the joint that accumulates the most error in simulation.

In terms of simulation efficiency, the best choice of joint to exclude from articulation is the one that minimizes the length of articulations. However, you must also consider utility. The best joint to remove is the one that interferes the least with the robot functionality. In an ideal scenario, the joint to exclude from articulation only serves as a spatial constraint. Identify a joint with no limits, no resistance, and no drive. If there are no joints that meet this criterion, transfer these attributes to the adjacent joints before removing it from articulation.

In the case of this gripper, the best options to remove from the articulation are the joints that connect the inner shafts to the gripper body (the `inner_knuckle_joint`, highlighted in orange in the image).

1. To remove the joints from the articulation, select the `left_inner_knuckle_joint` and `right_inner_knuckle_joint` prims.
2. In the Joint section under physics, select **Exclude From Articulation**.

Note

The fully completed asset is located in the `Samples/Rigging/Gripper/Robotiq 2F-85_complete` folder.

## Preparing For Tests

Because the gripper is not connected to anything to move it and test its physical properties, add a structure to later help us test the stability of the gripper:

1. Create two Xforms and add the Rigid Body API to them.
2. Add a fixed joint from world to the first Xform.
3. Add a Prismatic Joint from the first Xform to the second Xform.
4. Add a second prismatic joint from the second Xform to base\_link.
5. Add a drive to the prismatic joints so that you can lift and move forward with a position command.
6. In the drives set the following:

   > * In the Advanced properties for the joint, set a maximum joint velocity of 5.0.
   > * Set the joint limits to [0, 1].
   > * In the joint drive, set the following:
   >
   >   > + Damping: 10000.0
   >   > + Stiffness: 10000.0

Make sure to move all joints that were just created outside of the Robotiq\_2f\_85 prim.

To assist in checking the grip:

1. Create a Cylinder and scale it to `[0.05, 0.05, 0.2]`.
2. Place the cylinder at `X=0.12`.
3. Set the cylinder collider to `Convex Hull`.
4. Create a ground plane and move it to `Z=-0.1`.

To assist in creating these prims, use the following script. You can run them by opening a Script Editor (**Window > Script Editor**) and pasting the code below.

```python
import omni.usd
from pxr import Gf, PhysicsSchemaTools, PhysxSchema, Sdf, Usd, UsdGeom, UsdPhysics

stage = omni.usd.get_context().get_stage()

# Create Xform nodes
xform = UsdGeom.Xform.Define(stage, "/World/Xform")
xform_1 = UsdGeom.Xform.Define(stage, "/World/Xform_1")

# Add Physics Rigid Body API to Xform nodes
for node in [xform, xform_1]:
    UsdPhysics.RigidBodyAPI.Apply(node.GetPrim())
    mass_api = UsdPhysics.MassAPI.Apply(node.GetPrim())
    mass_api.CreateMassAttr(0.1)

# Create Fixed Joint from Xform to Xform_1
fixed_joint = UsdPhysics.FixedJoint.Define(stage, xform.GetPath().AppendChild("fixed_joint"))
fixed_joint.CreateBody1Rel().SetTargets([str(xform.GetPath())])

# Create Prismatic Joints
prismatic_joint_1 = UsdPhysics.PrismaticJoint.Define(stage, "/World/Joint_Z")
prismatic_joint_1.CreateAxisAttr("Z")
prismatic_joint_1.CreateLowerLimitAttr(0.0)
prismatic_joint_1.CreateUpperLimitAttr(1.0)
prismatic_joint_1.CreateBody0Rel().SetTargets([str(xform.GetPath())])
prismatic_joint_1.CreateBody1Rel().SetTargets([str(xform_1.GetPath())])

prismatic_joint_2 = UsdPhysics.PrismaticJoint.Define(stage, "/World/Joint_X")
prismatic_joint_2.CreateAxisAttr("X")
prismatic_joint_2.CreateLowerLimitAttr(0.0)
prismatic_joint_2.CreateUpperLimitAttr(1.0)
prismatic_joint_2.CreateBody0Rel().SetTargets([str(xform_1.GetPath())])
prismatic_joint_2.CreateBody1Rel().SetTargets(
    ["/World/Robotiq_2F_85/base_link"]
)  # update this to match your robot's base_link prim path

# Add Prismatic Joint Drive with damping and stiffness
for joint in [prismatic_joint_1, prismatic_joint_2]:
    drive = UsdPhysics.DriveAPI.Apply(joint.GetPrim(), "linear")
    drive.CreateDampingAttr(10000)
    drive.CreateStiffnessAttr(10000)
    px_joint = PhysxSchema.PhysxJointAPI.Get(stage, str(joint.GetPath()))
    px_joint.CreateMaxJointVelocityAttr().Set(5.0)

# Add Ground Plane
PhysicsSchemaTools.addGroundPlane(stage, "/World/groundPlane", "Z", 100, Gf.Vec3f(0, 0, -0.1), Gf.Vec3f(1.0))

# Create cylinder mesh
result, path = omni.kit.commands.execute("CreateMeshPrimCommand", prim_type="Cylinder")
# Get the prim
cylinder_prim = stage.GetPrimAtPath(path)
cylinder_prim.GetAttribute("xformOp:scale").Set(
    (0.05, 0.05, 0.2)
)  # if your gripper is oriented differently, you may need to update the position and orientation of this cylinder or gripper accordingly to align them.  You can also do this post-creation.
cylinder_prim.GetAttribute("xformOp:translate").Set((0.12, 0, 0))

# Add Rigid Body and Mass API to cylinder
cylinder_body = UsdPhysics.RigidBodyAPI.Apply(cylinder_prim)
UsdPhysics.CollisionAPI.Apply(cylinder_prim)
mesh_collision = UsdPhysics.MeshCollisionAPI.Apply(cylinder_prim)
mesh_collision.CreateApproximationAttr().Set("convexHull")
massAPI = UsdPhysics.MassAPI.Apply(cylinder_body.GetPrim())
massAPI.CreateMassAttr(0.20)

# Create a Physics Scene
scene = UsdPhysics.Scene.Define(stage, Sdf.Path("/physicsScene"))
physxSceneAPI = PhysxSchema.PhysxSceneAPI.Apply(scene.GetPrim())
# This is a Small test scene, no need for GPU Dynamics
physxSceneAPI.CreateEnableGPUDynamicsAttr(False)
```

1. Set the target position for Joint X to 1 in the property panel, by going to the Joint Drive section and setting the target position to 1.
2. Set the target position for Joint Z to 1 in the property panel, by going to the Joint Drive section and setting the target position to 1.
3. Verify that you see the fingers ragdoll on the screen. It’s still necessary to Tune the Joint Drives for the fingers.

You can see in the video below that the gripper will move forward and lift up.

Until this point, if you start the simulation, you will see the fingers rotate freely, and also you will notice collision clipping between the fingers. This is because the fingers do not have drivers that tell them how to move, and because the finger components are connected with joints, there is a natural collision filter between them. This is normal and expected, and you fix it in the next sections.

## Adding Joint Drives

Add the Joint Drive API to all joints:

1. Select all joints on the gripper, then, in the Properties panel, **Add** > **Physics** > **Angular Drive** (or **Linear Drive** for prismatic joints).

   > * In this gripper, the joints that drive the fingers are `finger_joint` and `right_outer_knuckle_joint`.
   > * Additionally, you have to flip the direction of `finger_joint` and `right_outer_knuckle_joint`, by setting the lower limit to -75, and the upper limit to 0.
2. Select all the joints on the gripper, then, in the Properties panel, **Add** > **Physics** > **Joint State** (or **Joint State Linear** for prismatic joints).
3. Model this gripper as a force-driven grasp. For that, position control must be disabled. Select `finger_joint` and `right_outer_knuckle_joint`, then set **Stiffness** to 10. The **Damping** is set to 0.1.
4. To control how much pressure is applied when the grippers close, set the `Max Force` to 16.5 (N).

   > * These grippers also have a maximum speed at which they can operate. Converting from the data sheet to angular speed at the fingertips, the angular limit speed is 130 degrees per second.
5. In the joint section, under the **Advanced** tab, set the **Maximum Joint Velocity** to 130.0 (deg/s).

Summarizing the changes:

> * Maximum Joint Velocity: 130
> * Max Force: 16.5 (N)
> * Damping: 0.1
> * Stiffness: 10

When trying to control the fingers now, notice that they instantly bulge inwards instead of moving in parallel. The system still needs stability to maintain the parallel motion when closing without resistance.

The Robotiq hand has a spring mechanism at the outer knuckle to keep the fingers parallel until an object is grasped.

1. Set the stiffness of `[left, right]_inner_finger_joint` to 0.0002, damping to 0.00001 and max force to 0.5 (N) to achieve this behavior.

## Adding Mimic Joint

This gripper is controlled with a single input command that moves both fingers concurrently. This is achieved by combining the drive joints together with a Mimic Joint specification.

1. Select `right_outer_knuckle_joint`.
2. Remove or set all values to zero in the joint drive we just added.
3. On the Properties Panel, click on **Add** > **Physics** > **Mimic Joint**.

   > Note
   >
   > Because this is a single degree of freedom revolute joint, the schema axis is not relevant. The UI will show rotX as the default axis, despite the joint being defined in the Z axis.
4. In the Mimic settings, set gearing to -1.0 to make it act in the opposite direction of the reference joint.
5. Set the reference Joint to `finger_joint`.

   > All drive features are copied over from the reference joint, and having an authored joint drive would negatively impact the drive outcome.
   >
   > Note
   >
   > The Rotation Axis for the mimic joint only makes a difference, if the joint where mimic is applied contains multiple Degrees of Freedom (for Example Spherical Joint). For Prismatic and Revolute joints any selection will work just the same. It is still recommended to maintain it aligned with the DOF axis.
6. Run the simulation again.

## Collision Meshes

The default setting for collision meshes at import is Convex Hull. This is a good balance between performance and accuracy. However, for grippers, you often want the fingertips to have a collision mesh that closely follows the contour of the fingertip geometry, so that there won’t be any gaps between the fingertips and the objects being grasped.

To visualize the collision meshes:

1. Find the eye icon on top of the viewport, and click **Show By Type** > **Physics** > **Colliders** > **All**.
2. Verify that outlines show up surrounding any objects that have collision meshes.
3. Optionally, to change any collision meshes, select the part of the object associated with that mesh by clicking on it in the viewport, and then in the Physics section of the Property panel, change the Collider Approximation type to Convex Decomposition, or any other type that’s appropriate for your use case.
4. If you don’t see a Physics or Collider section, then you might need to go down or up the stage tree from the selected item.
5. The collision API can be applied to a nested child Xform, or the parent of the selected object.

### Self-Collision

During your tests you may notice that the fingers are not colliding against each other. This is the default behavior when importing from Onshape. To disable that:

1. Select `/World/Robotiq_2F85`.
2. Check **Self-Collision Enabled** in the Articulation Root Options.

Note

For more details on how to tune the articulation, refer to [Joint Parameter Tuning Example: 2F-85](https://docs.omniverse.nvidia.com/kit/docs/omni_physics/107.3/dev_guide/guides/gripper_tuning_example.html).

## Saving Results

After you are satisfied with the configuration, push the changes to the original asset:

1. Open the **Layer** tab.
2. Select the `Robotiq_2F_85` prim, and all child prims in it.
3. Drag the selection into `Robotiq_2F_85_edit.usd`.
4. Click the **Save Layer** button on both Layers.

Note

The fully completed asset is located in the `Samples/Rigging/Gripper/Robotiq 2F-85_complete` folder.

## Test the Gripper

Now we can test the gripping by lifting the gripper and moving it forward, while closing the gripper to grasp the cylinder.

1. Set the target position for
   :   * Joint X to 0.1 in the property panel, by going to the Joint Drive section and setting the target position to 0.1.
       * Joint Z to 0.1 in the property panel, by going to the Joint Drive section and setting the target position to 0.1.
       * Finger joints to -40 degrees in the property panel, by going to the Joint Drive section and setting the target position to -40.

You can see in the video below that the gripper will move forward and lift up.

## Control the Gripper with OmniGraph

We can also use an OmniGraph to control the gripper, by writing the target position of the finger joints directly in the graph.

We have already prepared the graph in the `Samples/Rigging/Gripper/Robotiq 2F-85/Robotiq_2F_85_complete/Robotiq_2F_75_controller.usd` file, insert it as a layer to your Robotiq\_2F\_85\_config.usd layer.

1. Open the **Layer** tab.
2. Select the Insert Sub-Layer layer.
3. Find the `Robotiq_2F_75_controller.usd` file in the `Samples/Rigging/Gripper/Robotiq 2F-85/Robotiq_2F_85_complete` folder, and click `Open`.

Explaining the graph:

In this graph, the upper and lower limits of the finger joints are used to calculate the range of motion of the gripper to map the input signal to the joint target position in degrees. The target position is set to the prim using the `Write Prim Attribute` (Write Target) node.

Variables:

> * `input_signal`: An input signal (float) where 1 means open the gripper and 0 means close the gripper.

Nodes:
:   * `Read Upper Limit` / `Read Lower Limit`: A node that reads the upper and lower limits of the finger joint.
    * `Isaac Read Simulation Time`: A node that reads the simulation time, with reset on stop enabled.
    * `On Playback Tick`: A node that ticks the graph on every frame.
    * `Write Prim Attribute`: A node that writes the target position to the finger joint prim.

Set the input signal to 0.5 and press the **Play** button to start the simulation. You should see the gripper move forward and lift up.

Note

The fully completed asset is located in the `Samples/Rigging/Gripper/Robotiq 2F-85_complete` folder.

## Summary

In this tutorial, you experienced a comprehensive workflow for importing assets from a rigged Onshape document, performed post-processing adjustments to enable correct simulation hierarchy, and configured effort drives with Mimic Joints. You conducted validation and troubleshooting to address simulation behavior issues, and optimized performance. Additionally, you utilized layered editing to prepare a ready-to-use asset while retaining a test environment for validating gripper functionality.

On this page

* [Learning Objectives](#learning-objectives)
* [Getting Started](#getting-started)
* [Rigging the Robot](#rigging-the-robot)
  + [Using Layers to Edit and Test an Asset](#using-layers-to-edit-and-test-an-asset)
* [Adjusting Joints Post Import](#adjusting-joints-post-import)
* [Breaking the Articulation Loop](#breaking-the-articulation-loop)
* [Preparing For Tests](#preparing-for-tests)
* [Adding Joint Drives](#adding-joint-drives)
* [Adding Mimic Joint](#adding-mimic-joint)
* [Collision Meshes](#collision-meshes)
  + [Self-Collision](#self-collision)
* [Saving Results](#saving-results)
* [Test the Gripper](#test-the-gripper)
* [Control the Gripper with OmniGraph](#control-the-gripper-with-omnigraph)
* [Summary](#summary)

---

### Rig Mobile Robot

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/robot_setup_tutorials/rig_mobile_robot.html

* [Robot Setup](../robot_setup/index.html)
* [Robot Setup Tutorials Series](index.html)
* Tutorial 5: Rig a Mobile Robot

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Tutorial 5: Rig a Mobile Robot

If you built a robot inside Omniverse USD Composer or used importers that do not carry over joint information, you’ll need to rig the robot before it can move like an articulated robot and be controlled by Isaac Sim APIs. This involves defining the types of joints between the body parts and setting the parameters that governs the joints’ behavior, such as stiffness and damping. This tutorial covers step-by-step instruction on how to rig a forklift.

## Learning Objectives

In this tutorial, an unrigged forklift USD asset is turned into a forklift that can move and be driven by Isaac Sim commands.

*30 Minutes Tutorial*

## Getting Started

**Prerequisite**

* Complete the [Quick Tutorials](../introduction/quickstart_index.html#isaac-sim-intro-quickstart-series) series to learn the basic core concepts of how to navigate inside Isaac Sim.
* Complete the [Assemble a Simple Robots](tutorial_gui_simple_robot.html#isaac-sim-app-tutorial-gui-simple-robot) and [Adding Sensors and Cameras](tutorial_gui_camera_sensors.html#isaac-sim-app-tutorial-gui-camera-sensors) tutorials to learn the concepts of rigid body API, collision API, joints, drives, and articulations.

**Reference USDs**

We provide USD assets relating to this tutorial in [Isaac Sim Assets](../assets/usd_assets_overview.html#isaac-assets-overview), and can be found in the Content Browser.

* Unrigged Forklift: `Isaac Sim/Samples/Rigging/Forklift/forklift_b_unrigged_cm.usd`
* Rigged Forklift: `Isaac Sim/Samples/Rigging/Forklift/forklift_b_rigged_cm.usd`

This tutorial guides you through the steps for going from file to file. The rigged assets serve as a reference for the final goal.

## Rigging the Robot

### Identify the Joints

Before making any modifications to the asset, the first step of rigging a robot is to identify the joints on the robot, both actuated and unactuated ones. The joints govern how all the mesh components are organized, and identifying the type and their degrees of freedom (DOF) are key in making sure the robot moves as expected once rigged.

For the forklift, there are seven DOF in total:

* There are four smaller roller wheels at the front. They have unactuated, revolute joints, and each has one degree of freedom for rotation about a single axis.
* The fork has linear motion relative to the main body of the forklift as it moves up and down to pick up objects stacked on the pellet, which means there is one actuated, prismatic joint between the fork and the body.
* The bigger wheel at the rear end is responsible for propelling the forklift and turning it. There are two actuated joints related to this wheel:

  > + A revolute joint that spins the wheel around its central axis to provide the forward and backward movement.
  > + A revolute joint between the rear wheelbase and the forklift body that provides the pivot to turn the forklift.

### Organize the Hierarchy

Open the unrigged forklift asset from the Content Browser: `Isaac Sim/Samples/Rigging/Forklift/forklift_b_unrigged_cm.usd`.
Depending on the importer used and the original asset’s setup, the unrigged structure of the USD could have no hierarchy in terms of how parts are organized. It could have every single component listed independently on the stage tree. This makes it difficult to read and navigate, but more importantly, it does not define which objects are moving as a group and how these groups are related to each other.

All meshes that are children of a parent prim are expected to move together when the parent prim moves. For example, the sticker and chains on the meshes are a part of the forklift body, and the entire body, no matter how many screws or blocks are used to make up the body, can be considered as a single link of this robot. Organize them all under a single parent ‘body’ prim. This ensures that when the ‘body’ moves, that all child parts that make up the body are moving together.

To organize prims for the forklift:

1. Create two XForms called `body` and `lift`.
2. Move all the meshes that make up the forklift body under the `body` Xform, and the operator cab meshes under the `lift` Xform. For ease of use, the meshes provided in the USD file are sorted according to their hierarchy. All meshes above `Looks` are a part of the `lift` XForm. Meshes below `Looks` (Right Chain Wheel to Body Glass) are a part of the `body` XForm. Remaining are for the wheelbase and wheels.
3. Create new Xforms for the `back wheel`, `back wheel swivel`, and separate prims for each of the front roller supports.
4. Create a new Xform for each of the four front roller wheels. Name them `roller_front_left`, `roller_front_right`, `roller_back_left`, and `roller_back_right`. Move the correct lead wheel mesh and cylinder collider under them.
5. Ensure that all the Xforms mentioned above have physics set to rigid body by clicking **Add** > **Physics > Rigid Body**.
   :   Note

       Rigid body prims cannot have children that are also rigid bodies.
6. It is easier to set the joints if they align the frame of the Xform to the frames of the respective wheels. To do so, for each wheel, select the mesh, and in its property tab under **Transform**, there are two components `Translate` and `Translate:pivot`. The newly created Xform’s transform must be the sum of those two components. For example, if `translate` is at \(X=x\_1, Y=y\_1, Z=z\_1\), and `translate:pivot` is at \(X=x\_p, Y=y\_p, Z=z\_p\), then the transform of the newly created Xform must be set to: \(X = x\_1+ x\_p , Y = y\_1 + y\_p , Z = z\_1 + z\_p\).
7. `Translate` of the wheel mesh needs to be set to the inverse of the `Translate:pivot` property of the corresponding mesh. For example, if `Translate` is \(X, Y, Z\) and `Translate:pivot` is \(X\_p, Y\_p, Z\_p\), so now, set the translate to \(-X\_p, -Y\_p, -Z\_p\).
8. Move the corresponding mesh under the XForm, this will define the parent-child relationship between them.

Verify that the resultant hierarchy looks like this:

Note

If you got stuck in this this section, review the Rigged Forklift from the Content Browser, `Isaac Sim/Samples/Rigging/Forklift/forklift_b_rigged_cm.usd`, for reference.

### Assign Collision Meshes

To ensure that the collision properties are set correctly for the meshes. If no collision properties are set, then as the robot moves, it can self penetrate depending on the joint configuration.

**The correct collision meshes for the body and the lift are already set for the USD provided, so you do not need to set them up manually.** But for reference, the steps to set the collision for the `SM_Forklift_Body_B01_01` are:

1. Select the `SM_Forklift_OperatorCab_B01_01` mesh under the `lift` Xform, right click and **Add > Physics > Collider Preset**. The default collision approximation is through Convex Hull, which can be found when you scroll under the property tab for the mesh selected and find the collision section.
2. To visualize the colliders, click on the **eye** icon near the top right of the Viewport, select Show By **Type > Physics > Colliders > Selected**. Verify that you can see a Pink outline when you select the mesh that was just added to the collision. This approximation is not suitable because the collision region covers large areas that are not part of the fork and are regions that are necessary to allow other objects to exist.
3. Different approximations can be used to define different collision meshes. To see this, select one of the meshes with a collision and navigate to the colliders section of its property pane. Select the **Convex Decomposition** approximation. Update the visualization for the collision mesh. Verify that the mesh generated, this time, covers more of the collidable surface because it has a tighter approximation. Try other approximations and to see what works best for you.

Follow the same process for other meshes that interact with each other using joints. Set the **Convex Decomposition** approximation for the `SM_Forklift_BackWheelbase_B01_01` mesh that is a part of the swivel.

The process for the wheels is a little different, any collision approximation that is not smooth and captures the exact shape and curvature of the wheel causes bumpy motion when attempting to drive the wheel. This can be avoided by using a cylinder to approximate the collision mesh.

1. Go to **Create > Shape > Cylinder**.
2. Set the scale to `X=0.16`, `Y=0.16`, ``` Z=0.08`,` and Orient along ``Y=90 ```.
3. Right click and create four duplicates of this cylinder, one for each of the four front roller wheels.
4. Drag the cylinders under the respective wheel’s Xform and change their transform about all axes to `0`. This aligns the cylinder axis and the Xform axis completely.
5. Right click on the cylinder and **Add > Physics > Collider**.
6. Following the same process for the back wheel, modify the cylinder scale to `X=0.3`, `Y=0.3`, `Z=0.1`, orient along `Y=90` because of its bigger size.

All the appropriate collision meshes and properties are set up and you can move on to adding the joints.

### Add Joints and Drives

In this step, add appropriate joints for the Forklift.

**Prismatic Joint**

The first joint is the joint between the forklift body and the fork. It needs linear motion between the two bodies, and the fork must move up and down relative to the body of the forklift.

1. Select the `lift` Xform and while holding the **Ctrl** key select the `body` Xform. While the two prims are highlighted, right click and **Create > Physics > Joints > Prismatic Joint**.
2. Find the newly created prismatic joint, select it. Under the properties tab, set the axis to **Z** axis, this denotes that the linear motion between the two bodies is in along the Z-axis.
3. Set the lower and upper limits for the joint in the **Property > Physics > Prismatic Joint** tab, for now set it to `-15` and `200`.
4. Add a Linear Drive for this joint by left clicking on the joint, and selecting **Add > Physics > Linear Drive**.
5. In the **Property > Physics > Drive > Linear** tab, set target position to `-15` so that the fork can start its initial position close to the ground, and set the Damping to `10000` and Stiffness to `100000`.
6. Create a Scope by right clicking on the stage and name it `lift_joint`. Drag the prismatic joint under the scope.

**Revolute Joints**

For all the roller support wheels, create revolute joints:

1. Select the `body` XForm, holding the **Ctrl** key select any of the roller wheel XForms. Right click **Create > Physics > Joint > Revolute Joint**. Verify that you see a Revolute joint added under the Xform for the wheel.
2. Verify that the joints appear in the expected location. If not, make sure that the location of the joint matches the with the rotation axis of the wheel, and make sure to set the rotation axis to “X”.
3. Follow the same process for the three remaining roller supports of the forklift.
4. Create a Scope by right clicking on the stage and name it `roller_joints`. Drag the roller joints under the scope.

Next, add the last two joints, which are responsible for driving and turning the forklift:

1. Select the `back_wheel_swivel` and `back_wheel` XForms and add a revolute joint between them. The location of this joint must match with the center of the back wheel.
2. Add an angular drive to this joint with the following properties: `Damping=10000`, `stiffness = 100`.
3. Select the `body` and `back_wheel_swivel` XForm and add a revolute joint between them. Make sure the axis of rotation is set to `Z`.
4. Change the axis of the joint to Z axis and lower with upper limits as `-60` and `60`, because this joint enables turning of the forklift. This is the range of the angles in degrees that the wheelbase would rotate.
5. Add an angular drive with the following properties: Damping = 100, stiffness = 100000.
6. Go to **Create > Scope**, name it `back_wheel_joints` and drag the rear wheel joints under the scope.
7. Remember to add a Physics Scene and Ground Plane before pressing **Play**.

### Add Articulations

The last step is adding articulation to the Forklift and putting all the joints into a single articulation chain, which makes it easier for the physics solver when solving for articulated objects such as a robot. **This has already been added for the prim in the reference USD assets**. But if not, to put select and right click on the ‘SMV\_Forklift\_B01\_01’ Xform and **Add > Physics > Articulation Root**. Under properties, disable the **Self collision** check box.

There are a few caveats for the placement of the articulation root.

If you place the articulation root on the root Xform prim of the asset, which is the standard for all Isaac Sim assets, then the simulation automatically assigns the articulation root to a rigid body in the robot, which minimizes the depth of the articulation tree.

However, if you want to manually determine the location of the articulation root, assign it to a rigid body component of the robot. It is recommended that you place the articulation root on the base or the chassis of a mobile robot or the fixed joint on a robotics arm.

Verify that the asset you have is similar to the Rigged Forklift asset provided.

### Converting Asset to a Different Unit

The original asset is in centimeters. The asset is automatically converted to meters when it is added into a scene that is in meters (see [Metrics Assembler](https://docs.omniverse.nvidia.com/extensions/latest/ext_metrics_assembler.html "(in Omniverse Extensions)")). When the asset is added to a stage, it must match the Rigged Forklift in Meters asset provided.

You can now try the Forklift, set the back wheel velocity to `-200` in the Angular Drive section for the joint. After pressing **play**, verify that you can see the forklift move forward.

## Summary

In this tutorial, you took an unrigged forklift USD asset:

* organized its structure
* added collision, joints, and drives
* turned it into a forklift that can move and driven by Isaac Sim commands

### Troubleshooting Tips

If when playing the simulation or after some movements, your robot explodes, check if any of the collision meshes are colliding with each other.

On this page

* [Learning Objectives](#learning-objectives)
* [Getting Started](#getting-started)
* [Rigging the Robot](#rigging-the-robot)
  + [Identify the Joints](#identify-the-joints)
  + [Organize the Hierarchy](#organize-the-hierarchy)
  + [Assign Collision Meshes](#assign-collision-meshes)
  + [Add Joints and Drives](#add-joints-and-drives)
  + [Add Articulations](#add-articulations)
  + [Converting Asset to a Different Unit](#converting-asset-to-a-different-unit)
* [Summary](#summary)
  + [Troubleshooting Tips](#troubleshooting-tips)

---

### Configure Manipulator

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/robot_setup_tutorials/tutorial_configure_manipulator.html

* [Robot Setup](../robot_setup/index.html)
* [Robot Setup Tutorials Series](index.html)
* Tutorial 7: Configure a Manipulator

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Tutorial 7: Configure a Manipulator

## Learning Objectives

This is the second manipulator tutorial in a series of four tutorials. This tutorial shows how to configure physics, joint effort limits, and gains for the UR10e robot from Universal Robots and the 2F-140 gripper from Robotiq.

*30 Minutes Tutorial*

## Prerequisites

* Review [Tutorial 6: Setup a Manipulator](tutorial_import_assemble_manipulator.html) tutorial prior to beginning this tutorial. The steps here continue from the asset built in the previous tutorial.

Note

If you have not completed the previous tutorial, you can find the prebuilt asset in the content browser at `Isaac Sim/Samples/Rigging/Manipulator/configure_manipulator/ur10e/ur_gripper/ur.usda`.
We highly recommend downloading the prebuilt asset to your local machine for easier access.

## Adjust the Articulation for Manipulation Tasks

Adjust the articulation for the UR10e robot to make it more stable and accurate for manipulation tasks. Let’s first open the physx layer, and create a physx articulation root.

1. Open the interface file, `ur.usda`, and select the layer lab on the top right corner
2. Click “Insert Sublayer” icon at the bottom of the layer panel. (orange arrow with stacked layers icon)
3. In the file dialog, navigate to `path/to/Manipulator/configure_manipulator/ur10e/ur_gripper/payloads/Physics/`, select `physx.usda`, and click **Open** to insert it as a sublayer.

1. Left click on physx.usda layer, then right click to select “Set Authoring Layer”. Now all your changes will be saved to the physx.usda layer.

1. In the Stage panel, select the **ur/Geometry/World** prim.
2. In the Property Editor at the bottom right, scroll down to the **Physics/Articulation** section. If you do not see an Articulation(PhysX), create a new one by clicking the **add** > **Physics** > **Articulation(PhysX)**.
3. Select **Articulation Enabled**.
4. Increase the **Solver Position Iterations Count** to `64`.
5. Increase the **Solver Velocity Iterations Count** to `4`.

   Note

   The **Solver Position Iterations Count** and **Solver Velocity Iterations Count** are used to control the accuracy of the simulation.

   For a complex robot with many degrees of freedoms and mimic joints, increasing these values will make the simulation more accurate at the cost of performance.
   See [articulation documentation](https://nvidia-omniverse.github.io/PhysX/physx/5.6.0/docs/Articulations.html#articulation-drive-stability) for more information.
6. Decrease **Sleep Threshold** to `0.00005`, this lowers the threshold for the robot to go to sleep when it is not moving. see [rigid body dynamics documentation](https://nvidia-omniverse.github.io/PhysX/physx/5.6.0/docs/RigidBodyDynamics.html#sleeping) for more information.
7. Decrease the **Stabilization Threshold** to `0.00001`, this lowers the threshold for the robot to start stabilizing itself when it is not moving. see [articulation documentation](https://nvidia-omniverse.github.io/PhysX/physx/5.6.0/docs/Articulations.html#articulation-drive-stability) for more information.
8. Next to the physx.usda (Authoring Layer) label, click the blue files icon to save the changes to the physx.usda layer.
9. Verify that in physx.usda layer, the Articulation(PhysX) prim is created and the properties are set correctly.

```python
over "Geometry"
 {
     over "world" (
         prepend apiSchemas = ["PhysxArticulationAPI"]
     )
     {
         float physxArticulation:sleepThreshold = 0.00005
         int physxArticulation:solverPositionIterationCount = 64
         int physxArticulation:solverVelocityIterationCount = 4
         float physxArticulation:stabilizationThreshold = 0.00001

         over "base_link"
         {
             string isaac:nameOverride (
                 displayName = "Name Override"
             )
         }
     }
 }
```

Note

See [PhysX Best Practice Guide](https://nvidia-omniverse.github.io/PhysX/physx/5.6.0/docs/BestPractices.html#jointed-objects-are-unstable) for tuning the articulation for manipulation tasks.

## Add Physics Materials

Add physics materials to the robot gripper to make it more realistic and stable for manipulation tasks.

1. Open the physics layer from the 2F-140 gripper asset from the last tutorial. It is located in the `configuration` folder with suffix `_physics`.

   Note

   If you have not completed the previous tutorial, you can find the prebuilt asset in the content browser at `Isaac Sim/Samples/Rigging/Manipulator/import_manipulator/robotiq_2f_140/configuration/robotiq_2f_140_physics.usd`.
2. Right click on the **robotiq\_arg2f\_140\_model** prim and select **Create** > **Physics** > **Physics Material**, select **Rigid Body Material**. This will add a physics material attribute to the gripper.
3. In the properties panel, scroll down to the **Physics/Rigid Body Material** section and set the **static friction** to **1.0** and **dynamic friction** to **1.0**. For your robot, match the friction values to the robot’s surface friction coefficients.
4. Apply the physics material to the gripper finger tip.
   - Select the `colliders/left_inner_finger/mesh_1/box` and in the properties panel, scroll down to the **Physics/Physics material on selected Material** section.
   - Select the **Physics Material** you just created at `/World/robotiq_arg2f_140_model/Looks/finger`.
5. Repeat the same process for the `colliders/right_inner_finger/mesh_1/box` prim.

Note

See [Adding Props](../core_api_tutorials/tutorial_core_adding_props.html#isaac-sim-app-tutorial-core-adding-props) for more information on how to add physics materials to the robot.

## Configure Joint Effort Limits

In the physics layer of the robotiq\_arg2f\_140\_model asset from the previous step, let’s configure the joint effort limits for the gripper.

1. In the **Stage** panel, select the `robotiq_arg2f_140_model/joints/finger_joint` prim. This is the joint that controls the gripper fingers, all other gripper joints are `Mimic` joints.
2. In the **Property Editor** at the bottom right, scroll down to the `Drive/Angular/Max Force` section.
3. Set the **Max Force** to `200`. This is the maximum force that can be applied to the gripper fingers. For your robot, match the max force to the robot’s joint torque limits.
4. **Ctrl + S** to save the changes.

Note

When the max force is very high, you might need to increase the physics step frequency (`Time Step per Second`) to avoid penetration and instabilities.

## Inspect the Robot Articulation

Let’s inspect the robot articulation to verify the joint effort limits are applied correctly. Open the top level `ur` asset that you built in the previous tutorial.
This asset references the physics layers that you modified, so all the changes you made to the physics layer will be reflected in this asset.

Note

You can find the prebuilt asset in the content browser at `Isaac Sim/Samples/Rigging/Manipulator/configure_manipulator/ur10e/ur_set_physx/ur.usda`.

1. Open the **Physics Inspector** through **Tools** > **Physics** > **Physics Inspector**.
2. Select the UR articulation in the stage, click on the circular arrow icon to refresh the articulation.
3. Try changing the target position with the blue slider and verify that the DOF position reaches the target specified.
4. Close the **Physics Inspector** window/panel (discarding any changes authored by this tool, if prompted).

   Warning

   Since the Physics Inspector partially initializes `omni.physx`, it is expected for general simulations to not behave properly when the tool is opened.

## Summary

In this tutorial, you learned how to configure the physics, joint effort limits, and gains for the UR10e robot from Universal Robots and the 2F-140 gripper from Robotiq using the Gain Tuner.
You added physics materials to the robot gripper to make it more realistic and stable for manipulation tasks.
You inspected the robot articulation and tuned the gains for the robot and the gripper fingers joints using the Physics Inspector.

On this page

* [Learning Objectives](#learning-objectives)
* [Prerequisites](#prerequisites)
* [Adjust the Articulation for Manipulation Tasks](#adjust-the-articulation-for-manipulation-tasks)
* [Add Physics Materials](#add-physics-materials)
* [Configure Joint Effort Limits](#configure-joint-effort-limits)
* [Inspect the Robot Articulation](#inspect-the-robot-articulation)
* [Summary](#summary)

---

### Generate Robot Config

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/robot_setup_tutorials/tutorial_generate_robot_config.html

* [Robot Setup](../robot_setup/index.html)
* [Robot Setup Tutorials Series](index.html)
* Tutorial 8: Generate Robot Configuration File

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Tutorial 8: Generate Robot Configuration File

## Learning Objectives

This is the third manipulator tutorial in a series of four tutorials. This tutorial will show you how to generate the robot configuration file for the UR10e robot from Universal Robots and the 2F-140 gripper from Robotiq.
These robot configuration files provide information about the robot’s kinematics, dynamics, and other properties that are used in RMPFlow and [cuMotion](https://nvidia-isaac.github.io/cumotion/) motion planners.

*30 Minutes Tutorial*

## Prerequisites

* Review [Tutorial 7: Configure a Manipulator](tutorial_configure_manipulator.html) tutorial prior to beginning this tutorial, continue the following steps from the asset built in the previous tutorial.

Note

If you have not completed the previous tutorial, you can find the prebuilt asset in the content browser at `Isaac Sim/Samples/Rigging/Manipulator/configure_manipulator/ur10e/ur/ur_gripper.usd`.

## Generate Robot URDF

Generate the robot URDF file from the UR10e robot and the 2F-140 gripper.

### Enable the Isaac Sim USD to URDF Exporter Extension

1. Go to **Window** > **Extensions**.
2. Type **URDF** in the search box, and find the **Isaac Sim USD to URDF Exporter Extension**.
3. If you can’t find it, remove the **@feature** filter from the search box.
4. Enable the extension by clicking the toggle button labeled **ENABLE**.
5. Check the box for **AUTOLOAD**, just to the right of **ENABLE**.

### Export the URDF File

1. Open the `ur_gripper.usd` asset you made in the previous tutorial, or use the completed asset provided above.
2. Click **File** > **Export URDF**.
3. In File name on the bottom left corner, save the file name to `robot.urdf`.

   Tip

   Using `robot.urdf` matches the default `--urdf` value in the pick-and-place tutorial scripts, so you won’t need to pass `--urdf` explicitly when running them.
4. In the **Mesh Directory Path** field, select the correct folder path to save the URDF meshes.
5. Click **Export**.

Note

Learn more about the USD to URDF Exporter Extension in the [USD to URDF Exporter Extension](../importer_exporter/ext_omni_exporter_urdf.html#isaac-sim-app-extension-urdf-exporter) manual.

## Generate Robot Description Files and Collision Spheres

Generate the XRDF file and collision spheres for the UR10e robot and the 2F-140 gripper.

### Enable the Robot Description Editor Extension

1. Go to **Window** > **Extensions**.
2. Search for `isaacsim.robot_setup.xrdf_editor` and find the **cuMotion/Lula Robot Description Editor** extension.
3. If you can’t find it, remove the **@feature** filter from the search box.
4. Enable the extension by clicking the toggle button labeled **ENABLE**.
5. Check the box for **AUTOLOAD**, just to the right of **ENABLE**.

### Prepare the Robot Asset

The Robot Description Editor does not support instanceable meshes. You must prepare the robot asset by disabling instanceable meshes.

1. Open the `ur_gripper.usd` asset you made in the previous tutorial, or use the completed asset provided above.
2. Select all `visuals` and `collisions` prims on the stage.
3. In the **Property** panel, uncheck the **Instanceable** checkbox for each.

   Hint

   You can use the search feature to find the `visuals` and `collisions` prims by searching for `visuals` and `collisions` respectively.

The **Instanceable** checkbox (highlighted in red) should be unchecked for all geometry prims.

### Configure Joint Properties

1. Press **Play** to start the simulation.
2. Open the editor via **Tools** > **Robotics** > **cuMotion/Lula Robot Description Editor**.
3. In the **Selection Panel**, set **Select Articulation** to the **ur** articulation prim path.
4. In **Set Joint Properties**, assign each joint a **Joint Status**:

   * Mark each Universal Robots arm joint as **Active Joint**. These joints are directly controlled by cuMotion.
   * Keep the Robotiq 2F-140 gripper joints as **Fixed Joint**. cuMotion holds these joints at the specified default position.

Important

**Do not stop the simulation**, you will need it to generate the collision spheres.

Pay attention to the default joint positions for fixed joints. They should match the initial pose defined in the manipulator USD, or you will need to reset the robot to those positions during task initialization.

### Generate Collision Spheres

Important

**Do not stop the simulation** or exit the Robot Description Editor during this step, or you will need to redo the previous steps.

Repeat the following for each link in the **ur** articulation, including gripper links:

1. In the **Selection Panel**, select the link under **Select Link**. Use **upper\_arm\_link** as an example.
2. In **Link Sphere Editor** > **Generate Spheres**, select a mesh from the **Select Mesh** dropdown (e.g. `/collisions/upperarm/mesh`).
3. Set the **Radius Offset** and **Number of Spheres** (e.g. `0.03` and `8` respectively).
4. Optionally adjust sphere positions by clicking and dragging them in the viewport.
5. Click **GENERATE SPHERES**. The spheres will turn cyan when finalized.

Suggested per-link sphere settings (ur10e + Robotiq 2F-140)

For links with multiple mesh entries, generate spheres for each mesh and combine them on the same link.

| Select Link | Number of Spheres | Radius Offset | Select Mesh |
| --- | --- | --- | --- |
| `/shoulder_link` | 1 | 0.03 | `/collisions/shoulder/mesh` |
| `/upper_arm_link` | 8 | 0.03 | `/visuals/upperarm/mesh` |
| `/forearm_link` | 8 | 0.03 | `/visuals/forearm/mesh` |
| `/wrist_1_link` | 1 | 0.03 | `/visuals/wrist1/mesh` |
| `/wrist_2_link` | 1 | 0.02 | `/visuals/wrist3/mesh` |
| `/wrist_3_link` | 1 | 0.02 | `/visuals/wrist3/mesh` |
| `/ee_link/robotiq_arg2f_base_link` | 1 | 0.02 | `/visuals/robotiq_arg2f_base_link/mesh` |
| `/ee_link/left_outer_knuckle` | 2 | 0.02 | `/visuals/robotiq_arg2f_140_outer_knuckle/mesh` |
| `/ee_link/left_outer_knuckle` | 2 | 0.02 | `/visuals/robotiq_arg2f_140_outer_finger/mesh` |
| `/ee_link/left_inner_finger` | 2 | 0.02 | `/collisions/robotiq_arg2f_140_inner_finger/mesh` |
| `/ee_link/right_inner_finger` | 2 | 0.02 | `/collisions/robotiq_arg2f_140_inner_finger/mesh` |
| `/ee_link/left_inner_knuckle` | 2 | 0.02 | `/visuals/robotiq_arg2f_140_inner_knuckle/mesh` |
| `/ee_link/right_inner_knuckle` | 2 | 0.02 | `/visuals/robotiq_arg2f_140_inner_knuckle/mesh` |
| `/ee_link/right_outer_knuckle` | 2 | 0.02 | `/visuals/robotiq_arg2f_140_outer_knuckle/mesh` |
| `/ee_link/right_outer_knuckle` | 2 | 0.02 | `/visuals/robotiq_arg2f_140_outer_finger/mesh` |

Spheres generated for the upper\_arm\_link.

Spheres generated for the full ur10e robot.

General tuning tips

* Size spheres to cover the link without being oversized — large spheres cause solver conservatism.
* More spheres improves collision accuracy but reduces solver performance.
* For long cylindrical links, generate spheres on the ends and use **Connect Spheres** to fill the middle evenly.
* Use **Scale Spheres in Link** to resize spheres uniformly across a link.
* The auto-generator requires water-tight triangle meshes. If it fails for a link, add and connect spheres manually.

### Export to XRDF

Important

**Do not stop the simulation** before exporting.

1. At the bottom of the Robot Description Editor, expand **Export To File** > **Export to cuMotion XRDF**.
2. Click the file icon and specify the file name as `robot.xrdf`.
3. Select the XRDF version to export (version 2.0 is recommended).
4. Click **Save**. Save to the same directory as the robot URDF file.
5. Stop the simulation after the file is exported.

### Adding a Tool to the Robot Configuration

[cuMotion](https://nvidia-isaac.github.io/cumotion/) requires a tool frame defined in the XRDF file. The tool frame is used to specify the end-effector frame for the robot.

1. Open the `robot.xrdf` file in a text editor.
2. Add the following line to the file:

   ```python
   tool_frames: ["wrist_3_link"]
   ```

See [Robot Configuration Tutorial](../cumotion/tutorial_robot_configuration.html#isaac-sim-cumotion-tutorial-robot-configuration) for more information on XRDF files and loading robot configurations into cuMotion.

## Assemble the Robot Configuration Directory

The pick-and-place tutorial scripts and the `load_cumotion_robot` API expect all robot configuration files to live in a single directory. After completing the export steps above, your directory should look like this:

```python
/path/to/robot/config/
├── robot.urdf
├── robot.xrdf
├── rmp_flow.yaml
└── meshes/
    └── ...
```

Pass this directory to the tutorial scripts with `--xrdf-dir /path/to/robot/config`. For a full description of these files and how they are used by cuMotion, see the [Robot Configuration Files](../cumotion/tutorial_robot_configuration.html#isaac-sim-cumotion-tutorial-robot-configuration) section of the cuMotion tutorial.

The `rmp_flow.yaml` file configures the RMPflow reactive motion controller. Save the text below in a file named `rmp_flow.yaml` and save it to the same directory as your `robot.urdf` and `robot.xrdf` files.

rmp\_flow.yaml — RMPflow configuration example

```python
format: rmpflow
api_version: 2.0

joint_limit_buffers: [.01, .01, .01, .01, .01, .01]

rmp_params:
    cspace_target_rmp:
        metric_scalar: 50.
        position_gain: 100.
        damping_gain: 50.
        robust_position_term_thresh: .5
        inertia: 1.
    cspace_trajectory_rmp:
        p_gain: 80.
        d_gain: 10.
        ff_gain: .25
        weight: 50.
    cspace_affine_rmp:
        final_handover_time_std_dev: .25
        weight: 2000.
    joint_limit_rmp:
        metric_scalar: 1000.
        metric_length_scale: .01
        metric_exploder_eps: 1e-3
        metric_velocity_gate_length_scale: .01
        accel_damper_gain: 200.
        accel_potential_gain: 1.
        accel_potential_exploder_length_scale: .1
        accel_potential_exploder_eps: 1e-2
    joint_velocity_cap_rmp:
        max_velocity: 2.15
        velocity_damping_region: 0.5
        damping_gain: 300.
        metric_weight: 100.
    target_rmp:
        accel_p_gain: 80.
        accel_d_gain: 120.
        accel_norm_eps: .075
        metric_alpha_length_scale: .05
        min_metric_alpha: .01
        max_metric_scalar: 10000.
        min_metric_scalar: 2500.
        proximity_metric_boost_scalar: 20.
        proximity_metric_boost_length_scale: .02
        accept_user_weights: false
    axis_target_rmp:
        accel_p_gain: 200.
        accel_d_gain: 40.
        metric_scalar: 10.
        proximity_metric_boost_scalar: 3000.
        proximity_metric_boost_length_scale: .05
        accept_user_weights: false
    collision_rmp:
        damping_gain: 50.
        damping_std_dev: .04
        damping_robustness_eps: 1e-2
        damping_velocity_gate_length_scale: .01
        repulsion_gain: 1000.
        repulsion_std_dev: .01
        metric_modulation_radius: .5
        metric_scalar: 500.
        metric_exploder_std_dev: .02
        metric_exploder_eps: .001
    damping_rmp:
        accel_d_gain: 30.
        metric_scalar: 50.
        inertia: 100.

canonical_resolve:
    max_acceleration_norm: 50.
    projection_tolerance: .01
    verbose: false

body_capsules:
    - name: base_link
      pt1: [0, 0, 0.22]
      pt2: [0, 0, 0]
      radius: .09

body_collision_controllers:
  - name: wrist_2_link
    radius: .04
  - name: wrist_3_link
    radius: .04
```

## Summary

In this tutorial, you have learned how to generate the robot configuration files for the UR10e robot and the 2F-140 gripper using the [Robot Description Editor](../manipulators/manipulators_robot_description_editor.html#isaac-sim-app-tutorial-motion-generation-robot-description-editor) and the [USD to URDF Exporter Extension](../importer_exporter/ext_omni_exporter_urdf.html#isaac-sim-app-extension-urdf-exporter) extensions. The resulting XRDF file can be loaded directly into cuMotion motion planners as described in [Robot Configuration Tutorial](../cumotion/tutorial_robot_configuration.html#isaac-sim-cumotion-tutorial-robot-configuration).

On this page

* [Learning Objectives](#learning-objectives)
* [Prerequisites](#prerequisites)
* [Generate Robot URDF](#generate-robot-urdf)
  + [Enable the Isaac Sim USD to URDF Exporter Extension](#enable-the-isaac-sim-usd-to-urdf-exporter-extension)
  + [Export the URDF File](#export-the-urdf-file)
* [Generate Robot Description Files and Collision Spheres](#generate-robot-description-files-and-collision-spheres)
  + [Enable the Robot Description Editor Extension](#enable-the-robot-description-editor-extension)
  + [Prepare the Robot Asset](#prepare-the-robot-asset)
  + [Configure Joint Properties](#configure-joint-properties)
  + [Generate Collision Spheres](#generate-collision-spheres)
  + [Export to XRDF](#export-to-xrdf)
  + [Adding a Tool to the Robot Configuration](#adding-a-tool-to-the-robot-configuration)
* [Assemble the Robot Configuration Directory](#assemble-the-robot-configuration-directory)
* [Summary](#summary)

---

### GUI Camera Sensors

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/robot_setup_tutorials/tutorial_gui_camera_sensors.html

* [Robot Setup](../robot_setup/index.html)
* [Robot Setup Tutorials Series](index.html)
* Tutorial 4: Add Camera and Sensors to a Robot

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Tutorial 4: Add Camera and Sensors to a Robot

Isaac Sim provides a variety of sensors that can be used to sense the environment and robot’s state.
This tutorial guides you through attaching a camera sensor to a mock robot, a process that can be generalized to other sensors.
Details regarding the camera and other types of sensors can be found in our Advanced Tutorials and Sensor Extensions.

## Learning Objectives

This tutorial details how to:

* Add cameras
* Attach cameras to geometries

## Prerequisites

* Complete [Tutorial 3: Articulate a Basic Robot](tutorial_gui_simple_robot.html#isaac-sim-app-tutorial-gui-simple-robot).
* Review the [introduction to camera frames and axes](../reference_material/reference_conventions.html#isaac-sim-cameras).

Start this tutorial using the `Isaac Sim/Samples/Rigging/MockRobot/mock_robot_rigged.usd` file provided, to have a standardized setup.

## Adding a Camera

To add a camera:

1. Go to the Menu Bar and select **Create > Camera**. A camera appears on the stage tree, and a grey wireframe representing the camera’s view appears on the stage.
2. You can move and rotate the camera’s transform just like any other objects on the stage.

Note

The camera icon is hidden by default in the viewport. To see the camera icon, go to the **eye** menu on the top edge of the viewport, and select **Show By Type > Cameras**. The camera icon appears in the viewport.

You can also add a camera by moving the current view in the viewport to a view of your choosing, and then go to the **Camera** button on the upper left hand corner of the viewport display, and select **Camera > Create from View**.
A new camera appears on the Stage tree, and the list of cameras that can be selected in the **Camera** button is provided.

## Inspect the Camera

Use the [Camera Inspector Extension](../sensors/isaacsim_sensors_camera.html#isaac-sim-app-tutorial-camera-inspector-extension) to inspect the camera image and modify the camera’s states as needed.

1. Select **Tools > Robotics > Camera Inspector**.
2. Verify that you can see the camera in the dropdown. Click the **Refresh** button to find new cameras.
3. Select the camera you want to inspect. Create new viewports if necessary, and get and set camera poses as needed.

## Attach a Camera to Robot

1. Rename the newly added camera to `car_camera`.
2. It is easier to place the camera if you can see the desired camera input stream and where it is relative to the robot from an outside camera.
   Open up a second viewport window by going to the Menu Bar and click **Window > Viewports > Viewport 2**. A new viewport appears. Dock it wherever you’d like.
3. Keep one of the viewports in **Perspective** camera view, and change the other one to *car\_camera* view. Find the **Cameras** menu on the top edge of the viewport, and switch to **Camera > car\_camera**.
4. Validate that you have a view of the onboard camera and an overview of the scene.
5. Attach the camera to the robot’s body by dragging the prim under `body`. The camera moves together with the body. You may need to switch the camera view for the viewport again.
6. Point the camera slightly down and make it face forward so you can see the car and the ground. Set the camera transform translation to `x=-6,y=0,z=2.2`, orientation to `x=0,y=-80,z=-90`, and scale to `x=1,y=1,z=1`.
7. Verify that you see the viewport showing the onboard camera view splitting the window between the robot’s body and the ground and the relative position and orientation of the camera to the robot in the *Perspective* camera viewport.
8. Press **Play**. The camera onboard the robot moves with the robot.

A similar strategy is used to apply other onboard sensors.

Note

If the view of the camera is moved while displaying, it changes the camera’s properties. Instead, affix a prim to the parent with the correct offset and affix the camera to that new prim. Then, if the camera position is accidentally moved, it can be reset by zeroing all its position and orientation parameters relative to the prim, which cannot be easily changed.

## Summary

In this tutorial, you learned how to use the Camera Inspector Extension. Additionally, you also learned how to add a camera to the robot.

### Next Steps

* Continue on to [Omniverse Script Editor](../development_tools/omniverse_script_editor.html#isaac-sim-app-omniverse-script-editor) to learn how to run Python APIs inside the GUI.
* For rigging a more complex robot, go to [Tutorial 5: Rig a Mobile Robot](rig_mobile_robot.html#isaac-sim-app-tutorial-advanced-rigging-robot).

On this page

* [Learning Objectives](#learning-objectives)
* [Prerequisites](#prerequisites)
* [Adding a Camera](#adding-a-camera)
* [Inspect the Camera](#inspect-the-camera)
* [Attach a Camera to Robot](#attach-a-camera-to-robot)
* [Summary](#summary)
  + [Next Steps](#next-steps)

---

### GUI Simple Robot

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/robot_setup_tutorials/tutorial_gui_simple_robot.html

* [Robot Setup](../robot_setup/index.html)
* [Robot Setup Tutorials Series](index.html)
* Tutorial 3: Articulate a Basic Robot

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Tutorial 3: Articulate a Basic Robot

NVIDIA Isaac Sim’s GUI interface features are the same ones used in NVIDIA Omniverse™ USD Composer, an application dedicated to world-building. This tutorial focuses on the GUI functions that are most relevant to robotic uses. For more sophisticated general world creation, see [Omniverse Composer](https://docs.omniverse.nvidia.com/composer/latest/index.html "(in Omniverse USD Composer)").

You will rig a basic “robot” with three links and two revolute joints to introduce the concepts of joints and articulations. You take the objects that were added to the stage in [Tutorial 2: Assemble a Simple Robot](tutorial_intro_assemble_robot.html#isaac-sim-app-tutorial-intro-assemble-robot) and turn them into a mock mobile robot with a rectangular body and two cylindrical wheels.

This is not needed for robots that are imported from [Importing your Onshape Document](https://docs.omniverse.nvidia.com/extensions/latest/ext_onshape.html#isaac-onshape-importer-tutorials-importing "(in Omniverse Extensions)") or [URDF Importer Extension](../importer_exporter/ext_isaacsim_asset_importer_urdf.html#isaac-sim-urdf-importer), these are important concepts to understand for tuning your robots and assembling objects with articulations.

## Learning Objectives

This tutorial details how to rig a two-wheel mobile robot and covers how to:

* Organize stage tree hierarchy
* Add joints between two rigid bodies
* Add joint drives and joint properties
* Add articulations
* Move the robot via a Articulation Velocity Controller

## Prerequisites

* Complete [Tutorial 2: Assemble a Simple Robot](tutorial_intro_assemble_robot.html#isaac-sim-app-tutorial-intro-assemble-robot).
* Or load the checkpoint asset provided in the Content Browser at `Isaac Sim/Samples/Rigging/MockRobot/mock_robot_no_joints`. Do not load it as a reference because you must make permanent modifications to the file.

## Add Joints

1. If you are continuing from the GUI Tutorials and have your own `mock_robot.usd` saved, open it using **File > Open**. Otherwise, load the asset provided in the Content Browser at `Isaac Sim/Samples/Rigging/MockRobot/mock_robot_no_joints`. Do not load it as a reference because you must make permanent modifications to the file.
2. For organization, create a Scope to store the joints by right clicking **Create > Scope**, rename it to **Joints**.
3. To add a joint between two bodies, you must first select them both. Begin by clicking on the body and wheel parent transforms in the context tree window. For our mock robot, select the the cube object `body`, then while holding `Ctrl`, select the cylinder object `wheel_left`.
4. With both bodies highlighted, right-click and select **Create > Physics > Joints > Revolute Joint**. `RevoluteJoint` appears under `wheel_left` on the stage tree. Rename it to `wheel_joint_left`.
5. Verify in the **Property** tab that **body0** is `/mock_robot/body/body` (the cube) and **body1** is `/mock_robot/wheel_left/wheel_left` (the cylinder).
6. Set the X axis of the joint to **Local Rotation 0** to `0.0` and **Local Rotation 1** to `-90.0` to account for the transformation between the body and the cylinder. This is because the cylinder is rotated 90 degrees in the X axis compared to the body.
7. Change the **Axis** of the joint to **Y**. Because there is no local rotation `0` for the robot, the joint is in the same pose as the body.
8. For organization, drag the joint you just created into the **Joints** scope.
9. Repeat the previous five steps with the right wheel joint.

Before the joints were added, the three rigid bodies fell to the ground separately after pressing **Play**. Now that there are joints attached, the bodies fall as if they are connected.
To see that they move together like they are connected with revolute joints, you can drag the robot around by holding down the `Shift` key and clicking and dragging on any part of the robot in the viewport.

## Add a Joint Drive

Adding the joint adds the mechanical connection. To be able to control and drive the joints, you must add a joint drive API.
Select both joints and click the `+ Add` button in the **Property** tab, and select **Physics > Angular Drive** to add drive to both joints simultaneously.

* **Position Control:** For position controlled joints, set a high stiffness and relatively low or zero damping.
* **Velocity Control:** For velocity controller joints, set a high damping and zero stiffness.

For joints on a wheel, it makes more sense to be velocity controlled, so set both wheels’ **Damping** to **1e4** and **Target Velocity** to **200** **rad/s**.
If you are working with joints with limited range, those can be set in the **Property** tab, under the **Raw USD Properties > Lower (Upper) Limit**.
Press **Play** to see the mock mobile robot drive off.

## Add Articulation

Even though directly driving the joints can move the robot, it is not the most computationally efficient way. Making things into *articulations* can achieve higher simulation fidelity, fewer joint errors, and can handle larger mass ratios between the jointed bodies. For more information on the physics simulation behind it, see [Physics Core: Articulation](https://docs.omniverse.nvidia.com/kit/docs/omni_physics/latest/dev_guide/rigid_bodies_articulations/articulations.html "(in Omni Physics)").

To turn a series of connected rigid bodies and joints into articulation, set an *articulation root* to anchor the articulation tree. According to instructions on defining articulation trees in [Physics Core: Articulation](https://docs.omniverse.nvidia.com/kit/docs/omni_physics/latest/dev_guide/rigid_bodies_articulations/articulations.html "(in Omni Physics)"):

> > > For a fixed-base articulation, add the Articulation Root Component either to:
> >
> > * the fixed joint that connects the articulation base to the world.
> > * an ancestor of the fixed joint in the USD hierarchy. This allows creating multiple articulations from a single root component added to the scene.
>
> Each descendant fixed joint defines an articulation base link.
>
> > > For a floating-base articulation, add the Articulation Root Component to either:
> >
> > * the root rigid-body link
> > * an ancestor of the root link in the USD hierarchy

For this tutorial, add the articulation root to the robot:

1. Select `mock_robot` on the tree.
2. Open **+ Add** in the **Property** tab.
3. Add **Physics > Articulation Root**.

Validate that the resulting robot matches the asset that is provided in the Content Browser at `Isaac Sim/Samples/Rigging/MockRobot/mock_robot_rigged`.

## Add Controller

After the joints are part of an articulation, you can use tools to test the robot’s movement.

1. Create another scope by right clicking **Create > Scope**, rename it to **Graphs**. This will be used to store the ActionGraphs.
2. Drag the **Graphs** scope under the `mock_robot` Xform in the stage tree.
3. Go to **Tools > Robotics > OmniGraph Controllers > Joint Velocity** to add a velocity controller graph to the stage. This graph will allow you to control the robot’s movement by setting the target velocity for each joint.
4. Click the **Add** button for “Robot Prim” and select the prim with the Articulation Root API, in this case, it’s `/mock_robot`.
5. For Graph Path, write `mock_robot/Graphs/Velocity_Controller` to place the ActionGraph in the **Graphs** scope above.
6. Click **OK** to create the graph.
7. To move the robot, press **Play** to start the simulation. If you have any default position or velocity targets set, the robot starts moving towards those targets immediately. To change the joint commands, select the `JointCommandArray` on the stage tree under **/Graphs/velocity\_controller**, and change the parameters `input0` and `input1` in the properties window.

Note

The articulation controllers use **radians**, the default USD properties you find under Drive API when you select the individual joints on the stage tree are in **degrees**.

For this particular robot, it can also be controlled using a Differential Controller. For more information about OmniGraph Controller shortcuts, go to [Commonly Used OmniGraph Shortcuts](../omnigraph/omnigraph_shortcuts.html#isaac-sim-app-tutorial-advanced-omnigraph-shortcuts).

Note

The Differential Controller outputs wheel velocities in left-wheel, right-wheel order. In the Articulation Controller joint names or indices array, place `wheel_joint_left` before `wheel_joint_right`.

## Summary

In this tutorial, you learned to connect rigid bodies using joints, add a joint drive to control the joints, turn a chain of joints into an articulation, and control the robot using an Articulation Velocity Controller.

By the end of this tutorial, you have a robot with a body and two wheels, similar to the `mock_robot_rigged` asset, located in the `Samples/Rigging/MockRobot` folder.

### Next Steps

* Continue on to [Tutorial 4: Add Camera and Sensors to a Robot](tutorial_gui_camera_sensors.html#isaac-sim-app-tutorial-gui-camera-sensors) to learn how to add a camera to the car.

### Further Reading

[Physics Core](https://docs.omniverse.nvidia.com/kit/docs/omni_physics/latest/index.html "(in Omni Physics)") for more details regarding joints and articulations.

On this page

* [Learning Objectives](#learning-objectives)
* [Prerequisites](#prerequisites)
* [Add Joints](#add-joints)
* [Add a Joint Drive](#add-a-joint-drive)
* [Add Articulation](#add-articulation)
* [Add Controller](#add-controller)
* [Summary](#summary)
  + [Next Steps](#next-steps)
  + [Further Reading](#further-reading)

---

### Import & Assemble Manipulator

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/robot_setup_tutorials/tutorial_import_assemble_manipulator.html

* [Robot Setup](../robot_setup/index.html)
* [Robot Setup Tutorials Series](index.html)
* Tutorial 6: Setup a Manipulator

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Tutorial 6: Setup a Manipulator

## Learning Objectives

This is the first manipulator tutorial in a series of four tutorials. This tutorial shows how to import the UR10e robot from Universal Robots and the 2F-140 gripper from Robotiq into NVIDIA Isaac Sim from URDF files and connect them together under one articulation.

*30 Minutes Tutorial*

Isaac Sim always uses Python 3.12, so the UR description package and any ROS packages used in this tutorial must be available in a Python 3.12 environment. How you obtain the package depends on your platform:

* **Ubuntu 24.04 + ROS 2 Jazzy** — install the prebuilt `ros-jazzy-ur-description` apt package; the system Python (3.12) already matches Isaac Sim.
* **Ubuntu 22.04 + ROS 2 Humble or Jazzy** — the system Python is 3.10, so the workspace must be cloned and rebuilt against Python 3.12 using the included `build_ros.sh` script.
* **Windows + Pixi-based ROS 2 Jazzy** — add the UR description package to your Pixi environment (`pixi add ros-jazzy-ur-description`); Pixi-managed ROS 2 Jazzy already runs on Python 3.12. See [ROS 2 Installation (Other Platforms)](../installation/install_ros_other_platforms.html#isaac-sim-app-install-ros-other-platforms) for Pixi setup. WSL2 is not supported for the ROS-based URDF import workflow — use the prebuilt USD files in the content browser instead.

Attention

ROS 2 Humble on Windows (Pixi) is not a supported configuration for this tutorial. On Windows, only ROS 2 Jazzy with Pixi is supported. Switch to ROS 2 Jazzy on Windows, or move to a Linux configuration, to follow this tutorial as written.

Verify or choose your configuration in the **Build Environment** banner at the top of this page to see the steps for your setup. Your selection drives the platform-specific commands throughout the rest of this page.

.config-selector {
position: fixed;
top: var(--pst-header-height, 60px);
left: 0;
right: 0;
z-index: 1020;
display: flex;
flex-wrap: wrap;
align-items: center;
justify-content: center;
gap: 12px 18px;
background-color: var(--pst-color-surface, rgba(248, 249, 250, 0.95));
border-bottom: 1px solid var(--pst-color-border, var(--color-border, #dee2e6));
border-radius: 0;
padding: 10px 24px;
margin: 0;
box-shadow: 0 4px 12px var(--pst-color-shadow, rgba(0,0,0,0.08));
backdrop-filter: saturate(180%) blur(6px);
-webkit-backdrop-filter: saturate(180%) blur(6px);
}
[data-theme="dark"] .config-selector {
background-color: var(--pst-color-surface, rgba(30, 30, 30, 0.92));
border-color: var(--pst-color-border, #404040);
box-shadow: 0 2px 8px rgba(0,0,0,0.3);
}
.config-selector h3 {
display: inline-block;
margin: 0 16px 0 0;
color: var(--pst-color-text-base, var(--color-foreground-primary, #212529));
font-size: 0.95em;
font-weight: 600;
vertical-align: middle;
}
[data-theme="dark"] .config-selector h3 {
color: var(--pst-color-text-base, #ffffff);
}
.config-options {
display: flex;
flex-direction: row;
flex-wrap: wrap;
gap: 10px 18px;
align-items: center;
}
.config-row {
display: flex;
flex-direction: row;
align-items: center;
gap: 8px;
}
.config-label {
font-weight: 600;
color: var(--pst-color-text-base, var(--color-foreground-primary, #212529));
font-size: 13px;
white-space: nowrap;
}
[data-theme="dark"] .config-label {
color: var(--pst-color-text-base, #ffffff);
}
.config-buttons {
display: flex;
flex-wrap: wrap;
gap: 6px;
}
.config-btn {
padding: 5px 10px;
border: 2px solid var(--pst-color-border, var(--color-border, #dee2e6));
border-radius: 6px;
background-color: var(--pst-color-surface, var(--color-background-primary, #ffffff));
color: var(--pst-color-text-base, var(--color-foreground-primary, #212529));
font-size: 12px;
font-weight: 500;
font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
cursor: pointer;
transition: all 0.2s ease-in-out;
white-space: nowrap;
user-select: none;
outline: none;
}
[data-theme="dark"] .config-btn {
border-color: var(--pst-color-border, #404040);
background-color: var(--pst-color-surface, #2d2d2d);
color: var(--pst-color-text-base, #cccccc);
}
.config-btn:hover {
border-color: var(--pst-color-primary, var(--color-brand-primary, #0d6efd));
background-color: var(--pst-color-primary-bg, var(--color-background-hover, #e9ecef));
color: var(--pst-color-text-base, var(--color-foreground-primary, #212529));
}
[data-theme="dark"] .config-btn:hover {
border-color: #666666;
background-color: #3d3d3d;
color: #ffffff;
}
.config-btn.active {
border-color: #76b900;
background-color: #76b900;
color: #ffffff;
font-weight: 600;
}
.config-btn.active:hover {
border-color: #669900;
background-color: #669900;
color: #ffffff;
}
.config-btn:focus {
box-shadow: 0 0 0 3px rgba(118, 185, 0, 0.2);
}
.config-content {
transition: opacity 0.3s ease-in-out;
}
.config-content.hidden {
display: none;
}
@media (max-width: 768px) {
.config-selector {
padding: 8px 10px;
}
.config-options {
flex-direction: column;
align-items: stretch;
gap: 8px;
}
}
@media print {
.config-selector {
position: static;
backdrop-filter: none;
}
}

### Build Environment

Platform:

LinuxWindows

Ubuntu Version:

Ubuntu 24.04Ubuntu 22.04

Ros Distro:

JazzyHumble

document.addEventListener('DOMContentLoaded', function() {
const buttons = document.querySelectorAll('.config-btn');
const contents = document.querySelectorAll('.config-content');
// Returns the active value for each visible config row.
// Rows hidden by a data-show-when dependency are excluded so their
// value does not accidentally filter out content blocks.
function getCurrentConfig() {
const config = {};
const buttonGroups = document.querySelectorAll('.config-buttons');
buttonGroups.forEach(group => {
const row = group.closest('.config-row');
if (row && row.style.display === 'none') return;
const activeBtn = group.querySelector('.config-btn.active');
if (activeBtn) {
config[group.dataset.configKey] = activeBtn.dataset.value;
}
});
return config;
}
// Show or hide config rows that have a data-show-when dependency.
// Must be called before updateVisibility() so getCurrentConfig() is correct.
function updateRowVisibility() {
const config = getCurrentConfig();
document.querySelectorAll('.config-row[data-show-when]').forEach(row => {
try {
const showWhen = JSON.parse(row.dataset.showWhen || '{}');
const visible = Object.entries(showWhen).every(([k, v]) => config[k] === v);
row.style.display = visible ? '' : 'none';
} catch (e) {
console.warn('Error parsing data-show-when for row:', e);
}
});
}
function updateVisibility() {
const currentConfig = getCurrentConfig();
contents.forEach(content => {
try {
const conditions = JSON.parse(content.dataset.conditions || '{}');
const shouldShow = Object.entries(conditions).every(
([key, value]) => currentConfig[key] === value
);
if (shouldShow) {
content.classList.remove('hidden');
content.style.display = 'block';
} else {
content.classList.add('hidden');
content.style.display = 'none';
}
} catch (e) {
console.warn('Error parsing conditions for content block:', e);
}
});
}
// Add click event listeners to buttons
buttons.forEach(button => {
button.addEventListener('click', function() {
this.parentNode.querySelectorAll('.config-btn').forEach(s => s.classList.remove('active'));
this.classList.add('active');
// Row visibility must be updated before content visibility.
updateRowVisibility();
updateVisibility();
});
button.addEventListener('keydown', function(e) {
if (e.key === 'Enter' || e.key === ' ') {
e.preventDefault();
this.click();
}
});
});
const banner = document.querySelector('.config-selector');
// Position the banner just below whatever is currently pinned to
// the top of the viewport (PyData navbar + version-warning + any
// announcement). Recomputed on scroll/resize so the banner shifts
// down when the version-warning is visible and up after it scrolls
// out of view.
const topElements = [
document.querySelector('.bd-header-announcement'),
document.querySelector('#bd-header-version-warning'),
document.querySelector('.bd-header.navbar'),
].filter(Boolean);
// Element that holds article content; padded down so its content
// is never overlapped by the fixed banner regardless of wrap.
const contentRoot = document.querySelector('.bd-main') ||
document.querySelector('main') ||
document.body;
function updateBannerTop() {
if (!banner) return;
let bottom = 0;
topElements.forEach(el => {
const rect = el.getBoundingClientRect();
if (rect.bottom > bottom) bottom = rect.bottom;
});
banner.style.top = Math.max(0, bottom) + 'px';
}
function updateContentOffset() {
if (!banner || !contentRoot) return;
const h = banner.offsetHeight;
contentRoot.style.paddingTop = h + 'px';
// Anchor links should land below the banner, not behind it.
document.documentElement.style.scrollPaddingTop = (h + 16) + 'px';
}
if (banner && 'ResizeObserver' in window) {
new ResizeObserver(() => {
updateContentOffset();
updateBannerTop();
}).observe(banner);
}
window.addEventListener('resize', () => {
updateContentOffset();
updateBannerTop();
});
window.addEventListener('scroll', updateBannerTop, { passive: true });
// Initial update
setTimeout(function() {
updateRowVisibility();
updateVisibility();
updateContentOffset();
updateBannerTop();
}, 100);
// Watch for theme changes
});

## Prerequisites

* If you are new to NVIDIA Isaac Sim, complete the [Wheeled Robot Set Up Tutorials](tutorial_intro_environment_setup.html#isaac-sim-app-tutorial-intro-environment-setup) tutorial prior to beginning this tutorial.
* Review the ROS 2 installations [ROS 2 Installation (Default)](../installation/install_ros.html#isaac-sim-app-install-ros) prior to beginning this tutorial.
* Review the URDF importer [URDF Importer Extension](../importer_exporter/ext_isaacsim_asset_importer_urdf.html#isaac-sim-urdf-importer) tutorial.
* In a ROS sourced terminal, install xacro for your selected configuration (see the **Build Environment** banner at the top of the page):

  ```python
  sudo apt install ros-$ROS_DISTRO-xacro
  ```

  ```python
  pixi add ros-$ROS_DISTRO-xacro
  ```

  Attention

  ROS 2 Humble on Windows (Pixi) is not a supported configuration. Switch to ROS 2 Jazzy on Windows, or move to a Linux configuration, to follow this tutorial as written.
* Locate the `import_manipulator` folder in the content browser at `Isaac Sim/Samples/Rigging/Manipulator/import_manipulator/`.

## Build and Install the UR Description Package

Follow the steps for the configuration you selected in the **Build Environment** selector at the top of this page.

Install the prebuilt UR description package and source ROS 2 Jazzy:

```python
sudo apt install ros-jazzy-ur-description
source /opt/ros/jazzy/setup.bash
```

Then launch Isaac Sim from the same terminal:

```python
./isaac-sim.sh
```

On Ubuntu 22.04, the system Python (3.10) does not match the Python 3.12 used by Isaac Sim, and the UR description package is not natively available for Python 3.12. Clone the package and rebuild it with the included `build_ros.sh` script.

Note

See [Isaac Sim ROS Workspaces](../installation/install_ros.html#isaac-sim-ros-workspace) for more information on setting up your custom ROS 2 package in your ROS workspace.

1. Change into your Isaac Sim ROS Workspace, then into the distro-specific workspace’s `src` folder:

   ```python
   cd <path to Isaac Sim ROS Workspace>
   cd jazzy_ws/src
   ```

   ```python
   cd <path to Isaac Sim ROS Workspace>
   cd humble_ws/src
   ```
2. Clone the branch of the [Universal Robots ROS 2 Description repository](https://github.com/UniversalRobots/Universal_Robots_ROS2_Description) that matches your ROS distribution:

   ```python
   git clone --branch jazzy https://github.com/UniversalRobots/Universal_Robots_ROS2_Description.git
   ```

   ```python
   git clone --branch humble https://github.com/UniversalRobots/Universal_Robots_ROS2_Description.git
   ```
3. Return to the Isaac Sim ROS Workspace root and build against Python 3.12:

   ```python
   cd ../..
   ./build_ros.sh
   ```
4. Source the Python 3.12 ROS environment and launch Isaac Sim.

   ```python
   source build_ws/jazzy/jazzy_ws/install/local_setup.bash
   source build_ws/jazzy/isaac_sim_ros_ws/install/local_setup.bash
   ./isaac-sim.sh
   ```

   ```python
   source build_ws/humble/humble_ws/install/local_setup.bash
   source build_ws/humble/isaac_sim_ros_ws/install/local_setup.bash
   ./isaac-sim.sh
   ```

Attention

ROS 2 Humble on Ubuntu 24.04 is not an officially supported configuration in [ROS 2 Installation (Default)](../installation/install_ros.html#isaac-sim-app-install-ros). Switch to ROS 2 Jazzy on Ubuntu 24.04, or move to ROS 2 Humble on Ubuntu 22.04, to follow this tutorial as written.

On Windows, the URDF import workflow in this tutorial is supported only with a [Pixi-based](https://pixi.sh/) ROS 2 Jazzy installation. Follow [ROS 2 Installation (Other Platforms)](../installation/install_ros_other_platforms.html#isaac-sim-app-install-ros-other-platforms) for Windows ROS 2 setup and to install or build the UR description package against the Pixi environment. If you are using WSL2, skip the ROS-based import steps and use the prebuilt USD files in the content browser at `Isaac Sim/Samples/Rigging/Manipulator/import_manipulator/`.

Attention

ROS 2 Humble on Windows (Pixi) is not a supported configuration in [ROS 2 Installation (Default)](../installation/install_ros.html#isaac-sim-app-install-ros). Switch to ROS 2 Jazzy on Windows, or move to a Linux configuration, to follow this tutorial as written. If you need to use the UR10e on Windows without ROS, use the prebuilt USD files in the content browser at `Isaac Sim/Samples/Rigging/Manipulator/import_manipulator/`.

## Import the UR10e Robot

### Enable the ROS 2 Robot Description URDF Importer Extension

1. Go to `Window` > `Extensions`.
2. Type `URDF` in the search box, and find the `ROS 2 Robot Description URDF Importer Extension`.
3. If you can’t find it, remove the `@feature` filter from the search box.
4. If you still can’t find it, make sure Isaac Sim was launched from the same terminal where ROS was sourced.
5. Enable the extension by clicking the toggle button labeled `ENABLE`.
6. Check the box for `AUTOLOAD`, just to the right of `ENABLE`.

### Launch the URDF Publisher Topic

1. Open a new terminal with a **native** ROS 2 environment, source ROS 2 for your configuration, and launch the UR10e description.

   Important

   Do not reuse the Python 3.12 `build_ws` shell used to launch Isaac Sim above. The `build_ws` paths exist only to source the matching ROS 2 bridge into Isaac Sim; for `ros2 launch` commands, use your OS-native ROS 2 install (or a Docker container for distros that are not natively available on your OS).

   ```python
   source /opt/ros/jazzy/setup.bash
   ros2 launch ur_description view_ur.launch.py ur_type:=ur10e
   ```

   Source your native ROS 2 Humble install. If `ur_description` is not already available, install it from apt:

   ```python
   sudo apt install ros-humble-ur-description
   source /opt/ros/humble/setup.bash
   ros2 launch ur_description view_ur.launch.py ur_type:=ur10e
   ```

   Alternatively, build `ur_description` natively (Python 3.10) into `humble_ws` with `colcon build`, then source `humble_ws/install/local_setup.bash` instead of using the apt package.

   ROS 2 Jazzy is not natively available on Ubuntu 22.04, so run the launch command from a ROS 2 Jazzy Docker container with `jazzy_ws` mounted and built natively. Follow [Running ROS in Docker Containers](../installation/install_ros_other_platforms.html#isaac-ros-docker-other-platforms) to start an `osrf/ros:jazzy-desktop` container, build `jazzy_ws` inside it, then from inside the container run:

   ```python
   source /jazzy_ws/install/local_setup.bash
   ros2 launch ur_description view_ur.launch.py ur_type:=ur10e
   ```

   Activate the Pixi environment, then run:

   ```python
   ros2 launch ur_description view_ur.launch.py ur_type:=ur10e
   ```

   Attention

   ROS 2 Humble on Windows (Pixi) is not a supported configuration. Switch to ROS 2 Jazzy on Windows, or move to a Linux configuration, to follow this tutorial as written.
2. Verify that you see a window similar to the image below:
3. Set up one more terminal for `rqt_graph`, to see ROS nodes and topics being published:

   ```python
   rqt_graph
   ```
4. Verify that you see a window similar to the image below:

Hint

If the nodes are not showing up in `rqt_graph`, press the refresh button next to the drop down menu.

### Import the UR10e Robot into Isaac Sim

1. Go to Isaac Sim.
2. Navigate to **File** > **Import from the ROS 2 URDF Node**.

   * In the **ROS2 Node** field, type `robot_state_publisher`, click **Find Node**.
   * In the **USD Output** field, select the desired output (for example, `~/Desktop/`).
   * In the **Robot Type** field, select `Manipulator`.
   * In the **Base Type** field, select `Fixed`.
3. Click **Import**, the importer should automatically open the ur robot.

For reference, the resulting USD file is available in the content browser at `Isaac Sim/Samples/Rigging/Manipulator/import_manipulator/ur10e/ur/ur.usda`.

## Set Gains Using the Gain Tuner

The importer does not set the gains for the UR robot automatically. You can use the Gain Tuner to set the gains for the UR robot.
In this tutorial, we will use the gain tuner to set the natural frequency and damping ratio for the UR robot, which are defined as:

\[ \begin{align}\begin{aligned}\omega\_n = \sqrt{\frac{K\_p}{m}}\\\zeta = \frac{K\_d}{2 m \omega\_n}\end{aligned}\end{align} \]

Where \(\omega\_n\) is the natural frequency and \(\zeta\) is the damping ratio, and \(m\) is the computed joint inertia based on the mass of the robot at both sides of the joint.
The damping ratio is such that \(\zeta = 1.0\) is a critically damped system, \(\zeta < 1.0\) is underdamped, and \(\zeta > 1.0\) is overdamped.

Use the [Gain Tuner Extension](../robot_setup/ext_isaacsim_robot_setup_gain_tuner.html#isaac-gain-tuner) to set and verify the gains for the UR robot.

1. Go to **Tools** > **Robotics** > **Asset Editors** > **Gain Tuner**.
2. On the **Gain Tuner** window, on the **Robot Selection** dropdown, select the **ur** articulation in the stage.
3. In the **Tune Gains** panel, you can adjust the gains for the robot and the gripper fingers joints. Test it with the **Test Gains Settings** panel. let’s start by setting the natural frequency to `300` and the damping ratio to `1.0`.

Hint

We recommend determining the gains for a small group of joints first, if it is difficult to tune the gains for the whole robot. Below are some tips for tuning the gains:

* Higher the natural frequency, the faster the robot will respond to the target position. Lower the damping ratio, the faster the robot will reach the target position.
* If the resulting plot shows the robot is undershooting the target position, you can increase the `Nat. Freq.` slightly.
* If the resulting plot shows the robot is overshooting the target position, you can decrease the `Nat. Freq.` slightly and increase the `Damping Ratio`.
* Disabling gravity can help you see the gains more clearly.
* Only gain test the joints that are expected to be moving together, the gain test order can be selected by the **Sequence** dropdown.
* Reduce the maximum speed of a joint that you are tuning, if it is not expected to be commanded to move that fast in practice. The default values in the Gains Test are the maximum velocity written into the USD.

Note

See [Gain Tuner Extension](../robot_setup/ext_isaacsim_robot_setup_gain_tuner.html#isaac-gain-tuner) for more information on the Gain Tuner and [Tutorial 11: Tuning Joint Drive Gains](joint_tuning.html#isaac-sim-app-tutorial-advanced-joint-tuning) for more information on how to tune the gains for the robot.

For reference, the resulting USD file is available in the content browser at `Isaac Sim/Samples/Rigging/Manipulator/import_manipulator/ur10e/ur_gains_tuner/ur.usda`.

## 2F-140 Gripper Parameters

In the next section of the tutorial, we will be connecting the UR10e robot with the 2F-140 gripper. Let’s review the expected parameters for the gripper joints.

### Expected Parameters for Finger and Knuckle Joints

| Joint Name | Lower Limit | Upper Limit | Gearing | Stiffness | Damping | Max Force |
| --- | --- | --- | --- | --- | --- | --- |
| Finger Joint | 0 | 40.107 | N/A | 37.51957 | 0.00125 | 1000 |
| Left inner Finger | -8.021 | 48.128 | -1 | N/A | N/A | N/A |
| Left Inner Knuckle | -48.128 | 8.021 | 1 | N/A | N/A | N/A |
| Right inner Knuckle | -48.128 | 8.021 | 1 | N/A | N/A | N/A |
| Right outer knuckle | -48.128 | 8.021 | 1 | N/A | N/A | N/A |
| Right inner Finger | -8.021 | 48.128 | -1 | N/A | N/A | N/A |

### Expected Parameters for Mimic Joints

* Reference Joint: `/robotiq_arg2f_140_model/joints/finger_joint`
* Reference Joint Axis: `rotX`
* Natural Frequency: `2500`
* Damping Ratio: `0.005`

## Connect the UR10e Robot with the Robotiq 2F-140 Gripper

Much like a real robot can have its tools changed for different tasks, simulated robots benefit from the same capability. This section outlines two methods to connect the UR10e robot with the Robotiq 2F-140 gripper

We will use the Robot Assembler to connect the UR10e robot with the 2F-140 gripper.

1. Open the UR10e USD file created from the last activity (`ur.usda`).
2. Drag and drop the `robotiq_2f_140.usd` file we created earlier into the stage.
3. Open the robot assembler by going to **Tools** > **Robotics** > **Asset Editor** > **Robot Assembler**.

   * In **Base Robot**, set **Select Base Robot** to `/ur`, **Attach Point** to `wrist_3_link`.
   * In **Attach Robot**, set **Select Attach Robot** to `/ur/robotiq_2f_140`, **Attach Point** to `robotiq_arg2f_base_link`.
   * Set **Assembly Namespace** to `Gripper`.
4. Click **Begin Assembling Process** to start the process.
5. Adjust the attachment point orientation to make sure the end effector is attached to the gripper correctly. Rotate the gripper 90 degrees around the z-axis by clicking **Z +90**.
6. Click **Assemble and Simulate** to test the process.
7. Click **End Simulation And Finish** to complete the process.
8. Save the asset by going to **File** > **Save** or press **Ctrl+S**.

### Run the Simulation

1. In the Stage panel, select the **ur** prim.
2. In the Property Editor at the bottom right, find the **Variants** section.
3. Beside **Gripper**, select **None** and the gripper will be removed from the robot.
4. Beside **Gripper**, select **robotiq\_2f\_140** and the gripper will be added to the robot.
5. Save the asset by going to **File** > **Save** or press **Ctrl+S**.

Note

The completed robotics arm asset with the gripper is available in the content browser at `Isaac Sim/Samples/Rigging/Manipulator/import_manipulator/ur10e/ur_gripper/ur.usda`.

## Summary

In this tutorial, you took the UR10e robot from Universal Robots and the 2F-140 gripper from Robotiq and imported them into NVIDIA Isaac Sim from URDF files and connected them together under one articulation using the GUI and Robot Assembler.

On this page

* [Learning Objectives](#learning-objectives)
* [Prerequisites](#prerequisites)
* [Build and Install the UR Description Package](#build-and-install-the-ur-description-package)
* [Import the UR10e Robot](#import-the-ur10e-robot)
  + [Enable the ROS 2 Robot Description URDF Importer Extension](#enable-the-ros-2-robot-description-urdf-importer-extension)
  + [Launch the URDF Publisher Topic](#launch-the-urdf-publisher-topic)
  + [Import the UR10e Robot into Isaac Sim](#import-the-ur10e-robot-into-isaac-sim)
* [Set Gains Using the Gain Tuner](#set-gains-using-the-gain-tuner)
* [2F-140 Gripper Parameters](#f-140-gripper-parameters)
  + [Expected Parameters for Finger and Knuckle Joints](#expected-parameters-for-finger-and-knuckle-joints)
  + [Expected Parameters for Mimic Joints](#expected-parameters-for-mimic-joints)
* [Connect the UR10e Robot with the Robotiq 2F-140 Gripper](#connect-the-ur10e-robot-with-the-robotiq-2f-140-gripper)
  + [Run the Simulation](#run-the-simulation)
* [Summary](#summary)

---

### Intro: Assemble Robot

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/robot_setup_tutorials/tutorial_intro_assemble_robot.html

* [Robot Setup](../robot_setup/index.html)
* [Robot Setup Tutorials Series](index.html)
* Tutorial 2: Assemble a Simple Robot

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Tutorial 2: Assemble a Simple Robot

This tutorial guides you through the basic GUI functions that add objects to the stage. It also introduces inspecting and modifying their physics and material properties.

## Learning Objectives

This tutorial covers how to:

* Add and manipulate basic shapes
* Enable physics properties in objects
* Examine collision properties
* Edit physics properties such as friction
* Edit material properties such as color and reflectivity

## Prerequisites

* Complete [Tutorial 1: Stage Setup](tutorial_intro_environment_setup.html#isaac-sim-app-tutorial-intro-environment-setup) prior to beginning this tutorial.

## Adding Objects to the Scene

There are many ways to “add objects” to the stage, but all of them fundamentally do the same thing, which is to define a USD primitive in the stage context tree. The goal is to create a basic, two wheeled robot. Start by creating some basic shapes and modifying their properties. For the body, use a cube and for the wheels use cylinders.

To create the body of the robot:

1. Create an Xform by right clicking on the stage, selecting **Create > Xform**.
2. Rename it to **body** by right clicking on it and selecting **Rename**.
3. Fix the translation of the Xform to `(0, 0, 1)` by clicking on the **Translate** section in the property panel and setting the **X** to `0`, **Y** to `0`, and **Z** to `1`.
4. Create a cube clicking **Create > Shape > Cube** in the top menu bar. You should see the cube and the **Move** **gizmo** (the red, blue, and green arrows) appear in the viewport window
5. Click and drag on the blue arrow to raise the cube above the ground plane.
6. On the left side of the app, click the Scale icon (or press the R key while the cube is selected) to activate the scale widget.
7. Click and drag on the red part of the widget to scale the cube in the x direction
8. Place the cube in a specific location. Navigate to **Transform > Scale** in the property pane, and set the scale to `(2, 1, 0.5)`.
9. Drag the cube to the **Body** Xform.

To create the wheels of the robot:

1. Create a Xform by right clicking on the stage, selecting **Create > Xform**. Set the **Translate** to `(0, 1.5, 1)` and the **Orient** to `90, 0, 0` to rotate the wheel Xform 90 degrees around the x axis.
2. Rename it to **wheel\_left** by right clicking on it and selecting **Rename**.
3. Create a cylinder by clicking **Create > Shape > Cylinder** in the top menu bar.
4. In the property panel on the bottom right corner, scroll down to the **Geometry** section. Change its **Radius** to `0.5` and **Height** to `1.0`.
5. Drag the cylinder to the **wheel\_left** Xform.
6. Rename the cylinder to **wheel\_left** by right clicking on it and selecting **Rename**.
7. Duplicate the `wheel_left` by right clicking the `wheel_left` Xform on the stage tree, select **Duplicate**, and move it to `y = -1.5` while keeping all other parameters the same.
8. Rename the duplicated Xform to **wheel\_right** by right clicking on it and selecting **Rename**.
9. Rename the duplicated cylinder to **wheel\_right** by right clicking on it and selecting **Rename**.

## Adding Physics Properties

The cubes and cylinders added so far are strictly visual prims, with no physics or collision properties attached to them.
When you start the simulation by pressing **Play** and gravity is applied, these objects do not move because they are unaffected by physics.

To make the robot have physics, turn it into a rigid body with collision properties:

1. Select the Cube and both Cylinders on the stage tree by clicking while holding down the `Ctrl + Shift` key to select each object, or just `Shift` if they are consecutively listed on the tree.
2. In the **Property** tab, click on the `+ Add` button.
3. Select **Physics > Rigid Body with Colliders Preset**.
4. Press **Play** and verify that all three objects fall to the ground.

**Rigid Body with Colliders Preset** automatically adds the Rigid Body API and the Collision API to the objects.
These two APIs can be applied separately because you can have objects that:

* have mass and are affected by gravity, but have no collision properties so you can pass through them
* can be run into but hang in the air and are not affected by gravity

To validate, add, or remove APIs assigned to the selected object:

1. Go to its **Property** tab, and scroll down to find sections labeled **Rigid Body** and **Collider**.
2. To add the APIs separately, find them under the same **+ Add** button.
3. To remove APIs, click on the `X` to delete the section.

Hint

Dynamic objects can only select from Convex Hull, Convex Decomposition, Sphere Approximation, SDF mesh (GPU backend only) for collision shapes.
Triangle mesh collision shapes are only available for static objects.

### Examine Collision Meshes

To visually examine the outlines of collision meshes for the objects:

1. Find the eye icon on top of the viewport.
2. Click **Show By Type > Physics > Colliders > All**.
3. Verify that purple outlines show up surrounding any objects that have collision APIs applied. For example, verify that it is the cuboid, the cylinders, and the ground plane.

### Adding Contact and Friction Parameters

For modifying frictional properties, you must create a different physics material and then assign it to the desired object.

1. Go to the Menu Bar and click **Create > Physics > Physics Material**.
2. Select **Rigid Body Material** in the popup box. A new `PhysicsMaterial` appears on the stage tree.
3. Tune the parameters such as friction coefficients and restitution in its property tab.

To apply the assigned physics material to an object:

1. Select the object in the stage tree.
2. Find the menu item **Materials on Selected Model** in the **Property** tab.
3. Select the desired material in the drop-down menu.

## Material Properties

The objects may reflect the color of the spotlight added earlier, but it doesn’t actually have any colors assigned. You can confirm this by turning off the spotlight.

To change the color of the object, create a different material and then assign it to the objects, just like with the physics materials.
For example, create two different materials, one for the body of the car and one for the wheels.

1. Click **Create > Materials > OmniPBR** twice.
2. Right-click on the newly added materials on the stage tree and rename them to **body** and **wheel**.
3. Assign the corresponding rigid bodies to the newly created materials by going to the **Materials on selected models** item in its **Property** tab, and select the matching material from the dropdown.
4. Change the property of the new materials. Select one of them on the stage tree, change its base color in *Material and Shader/Albedo* and play with its reflectivity roughness and whatever else you find interesting.
5. Verify that you see the color of the corresponding parts on the car change accordingly.

## Summary

By the end of this tutorial, you should have a robot with a body and two wheels, similar to the `mock_robot_no_joints` asset, located in the **Samples > Rigging > MockRobot** folder.

This tutorial explained how to add and manipulate object properties in the GUI, including:

> 1. Adding primitive shapes onto the [Stage](../reference_material/reference_glossary.html#isaac-sim-glossary-stage).
> 2. Editing material properties, physics properties, and collision properties.

### Next Steps

* Continue to [Working with USD](../omniverse_usd/intro_to_usd.html#isaac-sim-app-tutorial-intro-usd) to learn how to save your world and load assets in USD format inside Isaac Sim.
* Go to [Tutorial 3: Articulate a Basic Robot](tutorial_gui_simple_robot.html#isaac-sim-app-tutorial-gui-simple-robot) to learn how to turn these geometries into a moving car.

On this page

* [Learning Objectives](#learning-objectives)
* [Prerequisites](#prerequisites)
* [Adding Objects to the Scene](#adding-objects-to-the-scene)
* [Adding Physics Properties](#adding-physics-properties)
  + [Examine Collision Meshes](#examine-collision-meshes)
  + [Adding Contact and Friction Parameters](#adding-contact-and-friction-parameters)
* [Material Properties](#material-properties)
* [Summary](#summary)
  + [Next Steps](#next-steps)

---

### Intro: Environment Setup

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/robot_setup_tutorials/tutorial_intro_environment_setup.html

* [Robot Setup](../robot_setup/index.html)
* [Robot Setup Tutorials Series](index.html)
* Tutorial 1: Stage Setup

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Tutorial 1: Stage Setup

Isaac Sim is built on [NVIDIA Omniverse](https://docs.omniverse.nvidia.com/) using tools provided in [Omniverse Kit](https://docs.omniverse.nvidia.com/dev-guide/latest/index.html "(in Omniverse Developer Guide)"). Omniverse Kit comes with a default UI that
allows you to edit a USD stage with ease. In this tutorial, you learn the basic steps for setting up an environment, adding and editing simple objects and their properties on a USD stage,
rigging rigid bodies with joints and articulations, and adding cameras and sensors.
The goal is to build your basic skills in navigating Isaac Sim, becoming familiar with frequently used terms, and using the GUI to build an environment and set up your robots.

## Learning Objectives

This tutorial teaches you to build a physics-enabled virtual world using the tools provided in the Isaac Sim GUI, including:

* Setup global stage properties
* Setup global physics properties
* Add ground plane
* Add lighting

## Prerequisites

To start with a clean Isaac Sim stage, go to the File menu and click on **New**.
The stage provided has a default `World` [Xform](https://docs.omniverse.nvidia.com/utilities/latest/common/glossary-of-terms.html#term-XForm "(in Omniverse Utilities)"), and a `defaultLight`. Both can be found on the stage tree on the right of the viewport.

## Setting up Stage Properties

Before anything is added onto the stage, verify that the current stage property setup matches the your expected conventions.

1. Go to **Edit > Preferences** to open up the Preference panel.
2. Browse the many types of settings inside Omniverse Kit grouped into categories in the column on the left of the panel.
3. Select **Stage** from the left column and review the properties such as:

   * The axis that determines *Up*. The default in Isaac Sim is Z. If your asset is created in a program with a different up-axis, it causes your assets to be imported rotated.
   * Stage units. Isaac Sim versions prior to 2022.1 have stage units in centimeters, but the default is now meters. However, the default units for Omniverse Kit is still in centimeters. Keep that in mind if you see USD units that are seemingly off by 100x.
   * Default rotation order. The default is set to execute rotation in Z, then Y, and last X.

## Creating the Physics Scene

To add a **Physics Scene** to simulate real world physics, including gravity and physics time steps:

1. Go to the Menu Bar and click **Create > Physics > Physics Scene**.
2. Validate that a **PhysicsScene** is added to the stage tree.
3. Click on it to examine its properties.
   You can see that gravity is set to the magnitude of `Earth Gravity`, or `9.8` meters per second squared. Remember that the default unit of length is meters.
4. Unless you are simulating hundreds of rigid bodies and robots, it is more efficient to use CPU physics
   :   * Open Physics Scene’s **Property** tab
       * Uncheck **Enable GPU dynamics**
       * Set the **Broadphase** type to **MBP**.

## Adding a Ground Plane

The ground plane prevents any physics-enabled objects from falling below it.
The ground plane’s collision property extends indefinitely even though the plane is only visible up to 25 meters in each direction.

To add a ground plane to the virtual environment:

1. Go to the top Menu Bar and click **Create > Physics > Ground Plane**.
2. Turn on the grid by clicking on  and selecting **Grid** to make the ground plane easier to see.

## Lighting

Every new [Stage](../reference_material/reference_glossary.html#isaac-sim-glossary-stage) is pre-populated with a `defaultLight`, otherwise you wouldn’t see anything. This default light is a child of the `Environment` Xform in the stage and can be found in the stage context tree.

To create additional spotlights:

1. Add a ground plane, if there isn’t already one, so we can see the reflection of the light. **Create > Physics > Ground Plane**.
2. Go to **Create > Light > Sphere Light**.
3. Pose the light on the stage.
   - In the **Stage** tab on the top right, select the newly created light in the stage tree.
   - In the **Property** tab on the bottom , in the **Transform** section use the **Translate** tool to move it to a position above the ground plane, such as `(0, 0, 7)`.
   - In the **Property** tab, in the **Transform** section, use the **Orient** tool to set the rotation to `(0, 0, 0)`.
4. Modify light color, brightness, and scope properties:
   - Inside the **Property** tab, change its color in **Main > Color** by clicking on the color bar and pick a color of your choice. For example a light green color `(RGB: 0.5, 1.0, 0.5)`.
   - Also inside the **Property** tab, change its intensity **Main > Intensity** to **1e6**; **Main > Radius** to **0.05**
   - In the **Shaping** section, change the **cone:angle** to **45** degrees and **cone:softness** to **0.05**.
5. To make the new spotlight easier to see, we will reduce the intensity of the default light by going to its **Property** tab and set **Main > Intensity** to **300**.

## Summary

This tutorial begins the necessary steps to create a virtual world suitable for physics simulation and testing Isaac Sim.
The following topics were covered:

* Adding a ground plane, lighting, and physics scene.

### Next Steps

Continue on to [Tutorial 2: Assemble a Simple Robot](tutorial_intro_assemble_robot.html#isaac-sim-app-tutorial-intro-assemble-robot) to learn how to add simple objects to Isaac Sim and edit their properties.

### Further Learning

For more in-depth and creative world-building tools, refer to our sister Omniverse tool [Composer](https://docs.omniverse.nvidia.com/composer/latest/index.html "(in Omniverse USD Composer)").

On this page

* [Learning Objectives](#learning-objectives)
* [Prerequisites](#prerequisites)
* [Setting up Stage Properties](#setting-up-stage-properties)
* [Creating the Physics Scene](#creating-the-physics-scene)
* [Adding a Ground Plane](#adding-a-ground-plane)
* [Lighting](#lighting)
* [Summary](#summary)
  + [Next Steps](#next-steps)
  + [Further Learning](#further-learning)

---

### Pick-Place Example

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/robot_setup_tutorials/tutorial_pickplace_example.html

* [Robot Setup](../robot_setup/index.html)
* [Robot Setup Tutorials Series](index.html)
* Tutorial 9: Pick and Place Example

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Tutorial 9: Pick and Place Example

## Learning Objectives

This is the final manipulator tutorial in a series of four tutorials. It ties everything together by showing how to use the UR10e robot and the 2F-140 gripper to control the gripper, follow a Cartesian target, and perform a pick-and-place sequence.
We will be using the robot imported in [Tutorial 6: Setup a Manipulator](tutorial_import_assemble_manipulator.html) and the URDF and XRDF robot configuration files described in [Robot Configuration Tutorial](../cumotion/tutorial_robot_configuration.html#isaac-sim-cumotion-tutorial-robot-configuration).

This tutorial builds on top of the [Robot Motion (Experimental)](../robot_motion_experimental/index.html#isaac-sim-robot-motion-experimental) extension and demonstrates two motion controllers:

* **cuMotion RMPflow** — a GPU-accelerated reactive motion planner with collision avoidance. See the [cuMotion Integration](../cumotion/index.html#isaac-sim-cumotion) overview and the [RMPflow Tutorial](../cumotion/tutorial_rmpflow.html#isaac-sim-cumotion-tutorial-rmpflow) for full details.
* **PINK differential IK** — a CPU-based inverse kinematics solver using the [PINK](https://github.com/stephane-caron/pink) library. See the [PINK Integration](../pink/index.html#isaac-sim-pink) overview and the [IK Controller Tutorial](../pink/tutorial_ik_controller.html#isaac-sim-pink-tutorial-ik-controller) for full details.

*30 Minutes Tutorial*

## Prerequisites

* Review [Tutorial 6: Setup a Manipulator](tutorial_import_assemble_manipulator.html) and [Tutorial 7: Configure a Manipulator](tutorial_configure_manipulator.html) prior to beginning this tutorial to generate robot and the URDF and XRDF files required by the pick-and-place examples.

Note

If you have not completed the previous tutorial(s), you can find the prebuilt asset in the content browser at `Isaac Sim/Samples/Rigging/Manipulator/configure_manipulator/ur10e/ur/ur_gripper.usd`.

Additionally, pre-generated URDF, XRDF, and `rmp_flow.yaml` files can be found at `source/extensions/isaacsim.robot_motion.cumotion/robot_configurations/ur10/`.

## Overview

This tutorial is divided into four parts, each corresponding to a standalone example script:

| Part | Script | Description |
| --- | --- | --- |
| 1 | `tutorial_9_gripper_control.py` | Gripper control using the Articulation API |
| 2 | `tutorial_9_arm_trajectory.py` | Joint-space trajectory planning and execution |
| 3 | `tutorial_9_follow_target.py` | Real-time Cartesian target following with cuMotion RMPflow |
| 4 | `tutorial_9_pick_place_cumotion.py` / `tutorial_9_pick_place_pink.py` | Full pick-and-place sequence with cuMotion RMPflow or PINK differential IK |

All scripts are located at `standalone_examples/tutorials/manipulation/`.

## Part 1: Gripper Control

This example introduces the Articulation API by controlling the 2F-140 gripper joints directly with `set_dof_position_targets`. The gripper closes fully and then opens again.

```python
./python.sh standalone_examples/tutorials/manipulation/tutorial_9_gripper_control.py
```

**Key concepts:**

* `Articulation.dof_names` returns the list of all degrees of freedom in order. The gripper joint is named `finger_joint`.
* `set_dof_position_targets` sends a position target to one or more DOFs by index. Passing `dof_indices` restricts the command to only those joints.

tutorial\_9\_gripper\_control.py — gripper control loop

```python
    finger_idx = robot.dof_names.index("finger_joint")
    frame_count = 0

    while app.is_running():
        for target_pos, label in [(_CLOSED_POS, "closing"), (_OPEN_POS, "opening")]:
            print(f"Gripper {label}...")
            for _ in range(_HOLD_STEPS):
                robot.set_dof_position_targets(target_pos, dof_indices=finger_idx)
                app.update()
                frame_count += 1
                if args.test and frame_count >= _HOLD_STEPS * 2:
                    return
```

## Part 2: Arm Trajectory Following

This example plans and executes a joint-space trajectory using `mg.Path` and `mg.TrajectoryFollower` from the motion generation API. The robot follows a sequence of waypoints in minimal time subject to velocity and acceleration limits.

```python
./python.sh standalone_examples/tutorials/manipulation/tutorial_9_arm_trajectory.py
```

**Key concepts:**

* `mg.Path(waypoints)` wraps a sequence of joint-space configurations.
* `.to_minimal_time_joint_trajectory(max_velocities, max_accelerations, ...)` computes a time-optimal trajectory that respects joint limits.
* `mg.TrajectoryFollower` tracks the planned trajectory, calling `.forward(estimated_state, setpoint, t)` each physics step to obtain the desired joint state.
* `get_estimated_state` packages the current joint positions, velocities, and efforts into an `mg.RobotState`.
* `apply_desired_state` applies the position, velocity, and effort targets from the desired state back to the articulation.

tutorial\_9\_arm\_trajectory.py — trajectory setup

```python
    waypoints = np.array(
        [
            [0.00, -1.57, 1.57, -1.57, -1.57, 0.00],  # home
            [0.50, -1.00, 0.80, -1.30, -1.57, 0.00],  # reach-out
            [0.00, -1.57, 1.57, -1.57, -1.57, 0.00],  # back to home
        ],
    )

    max_velocities = np.array([1.0, 1.0, 1.0, 1.0, 1.0, 1.0])
    max_accelerations = np.array([0.5, 0.5, 0.5, 0.5, 0.5, 0.5])

    trajectory = mg.Path(waypoints).to_minimal_time_joint_trajectory(
        max_velocities=max_velocities,
        max_accelerations=max_accelerations,
        robot_joint_space=robot_joint_space,
        active_joints=arm_joints,
    )
    print(f"Trajectory duration: {trajectory.duration:.2f} s")

    follower = mg.TrajectoryFollower()
    follower.set_trajectory(trajectory)

    simulation_time = 0.0
    if not follower.reset(get_estimated_state(robot, robot_joint_space), None, simulation_time):
        raise RuntimeError("Failed to reset TrajectoryFollower")
```

tutorial\_9\_arm\_trajectory.py — trajectory execution loop

```python
    dt = SimulationManager.get_physics_dt()
    max_steps = int((trajectory.duration + 1.0) / dt)
    frame_count = 0

    while app.is_running():
        app.update()
        if not (app_utils.is_playing() and SimulationManager.is_simulating()):
            continue
        simulation_time = 0.0
        follower.reset(get_estimated_state(robot, robot_joint_space), None, simulation_time)
        for _ in range(max_steps):
            app.update()
            if not (app_utils.is_playing() and SimulationManager.is_simulating()):
                break
            simulation_time += dt
            desired_state = follower.forward(get_estimated_state(robot, robot_joint_space), None, simulation_time)
            if desired_state is None:
                print("Trajectory complete.")
                break
            apply_desired_state(robot, desired_state)
            frame_count += 1
            if args.test and frame_count >= 100:
                return
```

See also

* [Trajectory Planning and Execution](../motion_generation/trajectory_planning.html) — the `mg.Path` and `mg.TrajectoryFollower` API used in this part.
* [cuMotion Trajectory Generator Tutorial](../cumotion/tutorial_trajectory_generator.html#isaac-sim-cumotion-tutorial-trajectory-generator) — generating collision-aware trajectories with cuMotion.

## Part 3: Follow Target using cuMotion RMPflow

This example shows how to use the cuMotion `RmpFlowController` to make the robot track a draggable target cube in real time, with optional obstacle avoidance.

```python
./python.sh standalone_examples/tutorials/manipulation/tutorial_9_follow_target.py
```

To enable obstacle avoidance, pass `--with-obstacle`:

```python
./python.sh standalone_examples/tutorials/manipulation/tutorial_9_follow_target.py --with-obstacle
```

**Key concepts:**

* `load_cumotion_supported_robot("ur10")` loads the built-in cuMotion robot model for the UR10, which includes the kinematic chain and collision spheres.
* `mg.WorldBinding` connects the cuMotion world interface to the Isaac Sim stage. It uses `mg.SceneQuery` to find collision objects in the scene and registers them as obstacles.
* `RmpFlowController` is initialized with the robot model, world interface, joint space, and tool frame. It accepts an estimated robot state and a Cartesian setpoint each step, and returns desired joint positions.
* `create_setpoint_state` packages a target position and orientation into an `mg.RobotState` that the controller can track.
* `world_binding.synchronize_transforms()` must be called each step to update obstacle transforms before planning.

tutorial\_9\_follow\_target.py — scene and controller setup

```python
async def setup_scene_and_controller(
    with_obstacle: bool,
) -> tuple[RmpFlowController, CumotionRobot, Articulation, mg.WorldBinding, GeomPrim]:
    assets_root_path = await get_assets_root_path_async()
    stage_utils.add_reference_to_stage(
        usd_path=assets_root_path + "/Isaac/Samples/Rigging/Manipulator/configure_manipulator/ur10e/ur/ur_gripper.usd",
        path=_ROBOT_PRIM_PATH,
    )

    GroundPlane("/World/GroundPlane")
    DomeLight("/World/DomeLight").set_intensities(1000)

    target_cube = Cube(paths=_TARGET_PATH, positions=[[0.35, 0.25, 0.3]], sizes=1.0, scales=[0.05, 0.05, 0.05])
    target_object = GeomPrim(paths=target_cube.paths)

    await omni.kit.app.get_app().next_update_async()
    set_camera_view(eye=[1.5, 1.5, 1.0], target=[0.5, 0.0, 0.2], camera_prim_path="/OmniverseKit_Persp")

    articulation = Articulation(_ROBOT_PRIM_PATH)
    await omni.kit.app.get_app().next_update_async()

    if with_obstacle:
        Cube("/World/obstacle", sizes=0.05, positions=[0.35, 0.0, 0.55], colors=(1.0, 0.0, 0.0))
        GeomPrim("/World/obstacle", apply_collision_apis=True)

    robot_pos, robot_ori = articulation.get_world_poses()
    objects = mg.SceneQuery().get_prims_in_aabb(
        search_box_origin=robot_pos.numpy()[0],
        search_box_minimum=[-10.0, -10.0, -10.0],
        search_box_maximum=[10.0, 10.0, 10.0],
        tracked_api=mg.TrackableApi.PHYSICS_COLLISION,
        exclude_prim_paths=[_ROBOT_PRIM_PATH, _TARGET_PATH],
    )

    obstacle_strategy = mg.ObstacleStrategy()
    for prim_type in (Mesh, Cone, Cylinder, Cube):
        obstacle_strategy.set_default_configuration(prim_type, mg.ObstacleConfiguration("obb", 0.05))

    world_binding = mg.WorldBinding(
        world_interface=CumotionWorldInterface(),
        obstacle_strategy=obstacle_strategy,
        tracked_prims=objects,
        tracked_collision_api=mg.TrackableApi.PHYSICS_COLLISION,
    )
    world_binding.initialize()
    world_binding.get_world_interface().update_world_to_robot_root_transforms(poses=(robot_pos, robot_ori))
    world_binding.synchronize_transforms()

    if args.xrdf_dir is not None:
        cumotion_robot = load_cumotion_robot(
            directory=args.xrdf_dir,
            urdf_filename=args.urdf,
            xrdf_filename=args.xrdf,
        )
    else:
        cumotion_robot = load_cumotion_supported_robot("ur10")
    site_space = cumotion_robot.robot_description.tool_frame_names()
    controller = RmpFlowController(
        cumotion_robot=cumotion_robot,
        cumotion_world_interface=world_binding.get_world_interface(),
        robot_joint_space=articulation.dof_names,
        robot_site_space=site_space,
        tool_frame=site_space[0],
    )
    controller.get_rmp_flow_config().set_param("cspace_target_rmp/metric_scalar", 1.0)
    controller.get_rmp_flow_config().set_param("collision_rmp/metric_scalar", 10000.0)

    return controller, cumotion_robot, articulation, world_binding, target_object
```

tutorial\_9\_follow\_target.py — per-step control loop

```python
def run_step(
    controller: RmpFlowController,
    cumotion_robot: CumotionRobot,
    articulation: Articulation,
    world_binding: mg.WorldBinding,
    target_object: GeomPrim,
    t: float,
) -> None:
    world_binding.get_world_interface().update_world_to_robot_root_transforms(articulation.get_world_poses())
    world_binding.synchronize_transforms()

    estimated = get_estimated_state(articulation)
    setpoint = create_setpoint_state(cumotion_robot, target_object)
    desired = controller.forward(estimated, setpoint, t)

    if desired is not None and desired.joints.positions is not None:
        articulation.set_dof_position_targets(
            positions=desired.joints.positions,
            dof_indices=desired.joints.position_indices,
        )
```

See also

* [cuMotion RMPflow Tutorial](../cumotion/tutorial_rmpflow.html#isaac-sim-cumotion-tutorial-rmpflow) — in-depth walkthrough of `RmpFlowController` configuration and tuning.
* [cuMotion World Interface Tutorial](../cumotion/tutorial_world_interface.html#isaac-sim-cumotion-tutorial-world-interface) — details on `CumotionWorldInterface`, `SceneQuery`, and `WorldBinding`.
* [Scene Interaction](../motion_generation/scene_interaction.html) — the underlying Motion Generation API for discovering and synchronizing obstacles from the USD scene.

## Part 4: Pick and Place

This example puts it all together by implementing a pick-and-place sequence. Two example scripts are provided: one using cuMotion RMPflow and one using PINK differential IK.

### cuMotion RMPflow

Important

cuMotion requires a `tool_frames` entry in the XRDF. See [Adding a Tool to the Robot Configuration](tutorial_generate_robot_config.html#isaac-sim-app-tutorial-generate-robot-config-adding-tool).

```python
./python.sh standalone_examples/tutorials/manipulation/tutorial_9_pick_place_cumotion.py \
    --xrdf-dir /path/to/robot/config
```

Note

`--xrdf-dir` should point to the directory containing the robot URDF and XRDF files made in the previous tutorial. `--urdf` and `--xrdf` select the filenames within that directory and default to `robot.urdf` and `robot.xrdf`, respectively.

If no `--xrdf-dir` is provided, `load_cumotion_supported_robot("ur10")` will be used to load the built-in UR10 robot configuration.

**Key concepts:**

* `--xrdf-dir` (optional) points to the directory containing custom robot config files. `load_cumotion_robot` loads the URDF and XRDF from that directory using the filenames given by `--urdf` and `--xrdf`. If omitted, the built-in UR10 configuration is used via `load_cumotion_supported_robot("ur10")`.
* `RmpFlowController.get_rmp_flow_config().set_param(key, value)` allows tuning RMPflow parameters at runtime. For this example, `cspace_target_rmp/metric_scalar` is reduced to 1.0 to reduce the influence of the initial position error on the motion planning.
* `controller.reset(estimated_state, setpoint, t)` must be called at the start of each arm motion segment to re-initialize the planner from the current robot state.

tutorial\_9\_pick\_place\_cumotion.py — UR10ePickPlace state machine class

```python
class UR10ePickPlace:
    """Pick-and-place controller for the UR10e + 2F-140 gripper using cuMotion RMPflow.

    Phases:
        0  Pre-grasp  — arm moves above the cube
        1  Approach   — arm descends to grasp height
        2  Grasp      — gripper closes
        3  Lift       — arm rises with the cube
        4  Transport  — arm moves above the target location
        5  Lower      — arm descends to place height
        6  Release    — gripper opens
        7  Retract    — arm lifts away
    """

    _ROBOT_PRIM_PATH = "/World/ur10e_robot"
    _CUBE_PRIM_PATH = "/World/cube"
    _EE_LINK_NAME = "right_inner_finger"
    _GRIPPER_JOINT = "finger_joint"

    _OPEN_POS: float = 0.0
    _CLOSED_POS: float = 0.5

    _ABOVE_HEIGHT: float = 0.50
    _NEAR_HEIGHT: float = 0.185
    _TOOL_OFFSET: dict[str, float] = {
        "tool0": 0.0,
        "wrist_3_link": 0.04,
    }
    _EE_THRESHOLD: float = 0.02
    _GRIPPER_THRESHOLD: float = 0.04
    _MIN_STEPS: int = 60
    _WARMUP_FRAMES: int = 120
    _PHYSICS_DT: float = 1.0 / 60.0

    _DOWN_ORI: np.ndarray = transform_utils.euler_angles_to_quaternion(np.array([0.0, np.pi, 0.0])).numpy()

    _PHASE_LABELS: tuple[str, ...] = (
        "Pre-grasp: moving above cube",
        "Approach: descending to cube",
        "Grasp: closing gripper",
        "Lift: raising arm",
        "Transport: moving to target",
        "Lower: descending to place",
        "Release: opening gripper",
        "Retract: lifting arm away",
    )

    def __init__(
        self,
        xrdf_dir: str | None = None,
        urdf_filename: str = "robot.urdf",
        xrdf_filename: str = "robot.xrdf",
        cube_position: np.ndarray | None = None,
        target_position: np.ndarray | None = None,
        events_dt: list[int] | None = None,
    ) -> None:
        self._xrdf_dir = xrdf_dir
        self._urdf_filename = urdf_filename
        self._xrdf_filename = xrdf_filename

        self.cube_position = cube_position if cube_position is not None else np.array([0.5, 0.0, 0.025])
        self.target_position = target_position if target_position is not None else np.array([0.5, 0.5, 0.05])
        self.events_dt = events_dt or [250, 150, 100, 50, 150, 100, 100, 100]

        self._event: int = 0
        self._step: int = 0
        self._t: float = 0.0
        self._warmup_remaining: int = self._WARMUP_FRAMES

        self._articulation: Articulation | None = None
        self._ee_prim: GeomPrim | None = None
        self._finger_idx: int | None = None
        self._cumotion_robot: CumotionRobot | None = None
        self._controller: RmpFlowController | None = None
        self._world_binding: mg.WorldBinding | None = None
        self._tool_frame: str | None = None
        self._site_space: list[str] | None = None

    async def setup_scene(self) -> None:
        """Build the scene and initialize the RMPflow controller."""
        assets_root_path = await get_assets_root_path_async()
        stage_utils.add_reference_to_stage(
            usd_path=assets_root_path
            + "/Isaac/Samples/Rigging/Manipulator/configure_manipulator/ur10e/ur/ur_gripper.usd",
            path=self._ROBOT_PRIM_PATH,
        )

        GroundPlane("/World/GroundPlane")
        DomeLight("/World/DomeLight").set_intensities(1000)

        cube_obj = Cube(
            paths=self._CUBE_PRIM_PATH, positions=[self.cube_position], sizes=1.0, scales=[0.05, 0.05, 0.05]
        )
        RigidPrim(paths=cube_obj.paths)
        GeomPrim(paths=cube_obj.paths, apply_collision_apis=True)

        await omni.kit.app.get_app().next_update_async()
        set_camera_view(eye=[1.5, 1.5, 1.0], target=[0.5, 0.0, 0.2], camera_prim_path="/OmniverseKit_Persp")

        self._articulation = Articulation(self._ROBOT_PRIM_PATH)
        await omni.kit.app.get_app().next_update_async()

        robot_pos, robot_ori = self._articulation.get_world_poses()
        objects = mg.SceneQuery().get_prims_in_aabb(
            search_box_origin=robot_pos.numpy()[0],
            search_box_minimum=[-10.0, -10.0, -10.0],
            search_box_maximum=[10.0, 10.0, 10.0],
            tracked_api=mg.TrackableApi.PHYSICS_COLLISION,
            exclude_prim_paths=[self._ROBOT_PRIM_PATH, self._CUBE_PRIM_PATH],
        )

        obstacle_strategy = mg.ObstacleStrategy()
        for prim_type in (Mesh, Cone, Cylinder):
            obstacle_strategy.set_default_configuration(prim_type, mg.ObstacleConfiguration("obb", 0.01))

        self._world_binding = mg.WorldBinding(
            world_interface=CumotionWorldInterface(),
            obstacle_strategy=obstacle_strategy,
            tracked_prims=objects,
            tracked_collision_api=mg.TrackableApi.PHYSICS_COLLISION,
        )
        self._world_binding.initialize()
        self._world_binding.get_world_interface().update_world_to_robot_root_transforms(poses=(robot_pos, robot_ori))
        self._world_binding.synchronize_transforms()

        if self._xrdf_dir is not None:
            self._cumotion_robot = load_cumotion_robot(
                directory=self._xrdf_dir,
                urdf_filename=self._urdf_filename,
                xrdf_filename=self._xrdf_filename,
            )
        else:
            self._cumotion_robot = load_cumotion_supported_robot("ur10")
        tool_frames = self._cumotion_robot.robot_description.tool_frame_names()
        if len(tool_frames) == 0:
            raise ValueError("No tool frames found in the robot description.")
        self._tool_frame = tool_frames[0]
        if self._tool_frame not in self._TOOL_OFFSET:
            raise ValueError(
                f"Tool frame '{self._tool_frame}' has no entry in _TOOL_OFFSET. "
                f"Add it: {list(self._TOOL_OFFSET.keys())}"
            )
        self._site_space = tool_frames

        self._controller = RmpFlowController(
            cumotion_robot=self._cumotion_robot,
            cumotion_world_interface=self._world_binding.get_world_interface(),
            robot_joint_space=self._articulation.dof_names,
            robot_site_space=self._site_space,
            tool_frame=self._tool_frame,
        )
        cfg = self._controller.get_rmp_flow_config()
        # cspace_target_rmp weights delta error from initial position
        # doesn't really matter in our case so decrease from default 50 to 1.0
        cfg.set_param("cspace_target_rmp/metric_scalar", 1.0)

    def initialize_after_play(self) -> None:
        """Resolve EE link and gripper DOF index. Call once after physics starts."""
        link_names = self._articulation.link_names
        if self._EE_LINK_NAME in link_names:
            self._ee_prim = GeomPrim(paths=self._articulation.link_paths[0][link_names.index(self._EE_LINK_NAME)])
        else:
            print(f"WARNING: '{self._EE_LINK_NAME}' not found. Available: {link_names}")

        dof_names = self._articulation.dof_names
        if self._GRIPPER_JOINT in dof_names:
            self._finger_idx = dof_names.index(self._GRIPPER_JOINT)
        else:
            print(f"WARNING: '{self._GRIPPER_JOINT}' not found. Available: {dof_names}")

        n_dofs = len(dof_names)
        init_pos = np.zeros(n_dofs)
        self._articulation.set_dof_positions(init_pos.tolist())
        self._articulation.set_dof_position_targets(init_pos.tolist())

    def _phase_ee_target(self) -> np.ndarray:
        c, p = self.cube_position, self.target_position
        offset = self._TOOL_OFFSET[self._tool_frame]
        hi = self._ABOVE_HEIGHT + offset
        lo = self._NEAR_HEIGHT + offset
        targets = {
            0: [c[0], c[1], c[2] + hi],
            1: [c[0], c[1], c[2] + lo],
            2: [c[0], c[1], c[2] + lo],
            3: [c[0], c[1], c[2] + hi],
            4: [p[0], p[1], p[2] + hi],
            5: [p[0], p[1], p[2] + lo],
            6: [p[0], p[1], p[2] + lo],
            7: [p[0], p[1], p[2] + hi],
        }
        return np.array(targets[self._event], dtype=np.float32)

    def _make_setpoint(self, position: np.ndarray) -> mg.RobotState:
        return mg.RobotState(
            sites=mg.SpatialState.from_name(
                spatial_space=self._site_space,
                positions=([self._tool_frame], wp.array([position.tolist()], dtype=wp.float32)),
                orientations=([self._tool_frame], wp.array([self._DOWN_ORI.tolist()], dtype=wp.float32)),
            ),
        )

    def _estimated_state(self) -> mg.RobotState:
        names = self._articulation.dof_names
        return mg.RobotState(
            joints=mg.JointState.from_name(
                robot_joint_space=names,
                positions=(names, self._articulation.get_dof_positions()),
                velocities=(names, self._articulation.get_dof_velocities()),
            )
        )

    def _set_gripper(self, pos: float) -> None:
        if self._finger_idx is not None:
            self._articulation.set_dof_position_targets(
                wp.array([pos], dtype=wp.float32), dof_indices=[self._finger_idx]
            )

    def _ee_near_target(self) -> bool:
        if self._ee_prim is None:
            return False
        ee_pos = self._ee_prim.get_world_poses()[0].numpy()[0]
        return bool(np.linalg.norm(ee_pos - self._phase_ee_target()) < self._EE_THRESHOLD)

    def _gripper_at(self, target: float) -> bool:
        if self._finger_idx is None:
            return False
        pos = float(self._articulation.get_dof_positions().numpy().flatten()[self._finger_idx])
        return abs(pos - target) < self._GRIPPER_THRESHOLD

    def _phase_converged(self) -> bool:
        if self._step < self._MIN_STEPS:
            return False
        if self._event == 2:
            return self._gripper_at(self._CLOSED_POS)
        if self._event == 6:
            return self._gripper_at(self._OPEN_POS)
        return self._ee_near_target()

    def forward(self) -> bool:
        """Advance one simulation step. Returns False when the sequence is complete."""
        if self.is_done():
            return False

        if self._warmup_remaining > 0:
            n_dofs = len(self._articulation.dof_names)
            targets = np.zeros(n_dofs)
            self._articulation.set_dof_position_targets(
                wp.array(targets, dtype=wp.float32), dof_indices=list(range(n_dofs))
            )
            self._warmup_remaining -= 1
            if np.abs(self._articulation.get_dof_positions().numpy().flatten() - targets).max() < 0.1:
                self._warmup_remaining = 0
            return True

        if self._step == 0:
            print(f"  Phase {self._event}: {self._PHASE_LABELS[self._event]}")
            if self._event in (0, 3, 7):
                if not self._controller.reset(
                    self._estimated_state(), self._make_setpoint(self._phase_ee_target()), t=0.0
                ):
                    raise RuntimeError("RmpFlowController reset failed.")
                self._t = 0.0

        if self._event == 2:
            self._set_gripper(self._CLOSED_POS)
        elif self._event == 6:
            self._set_gripper(self._OPEN_POS)
        else:
            self._world_binding.get_world_interface().update_world_to_robot_root_transforms(
                self._articulation.get_world_poses()
            )
            self._world_binding.synchronize_transforms()
            desired = self._controller.forward(
                self._estimated_state(), self._make_setpoint(self._phase_ee_target()), self._t
            )
            if desired is not None and desired.joints.positions is not None:
                self._articulation.set_dof_position_targets(
                    positions=desired.joints.positions, dof_indices=desired.joints.position_indices
                )

        self._t += self._PHYSICS_DT
        self._step += 1
        if self._phase_converged() or self._step >= self.events_dt[self._event]:
            if self._step >= self.events_dt[self._event]:
                print(f"  Phase {self._event} timed out after {self.events_dt[self._event]} frames")
            self._event += 1
            self._step = 0

        return True

    def is_done(self) -> bool:
        return self._event >= len(self.events_dt)

    def reset(self) -> None:
        self._event = 0
        self._step = 0
        self._t = 0.0
        self._warmup_remaining = self._WARMUP_FRAMES
```

See also

* [cuMotion Integration](../cumotion/index.html#isaac-sim-cumotion) — overview of the [cuMotion](https://nvidia-isaac.github.io/cumotion/) integration and its components.
* [cuMotion Robot Configuration Tutorial](../cumotion/tutorial_robot_configuration.html#isaac-sim-cumotion-tutorial-robot-configuration) — generating the URDF and XRDF files used by `--xrdf-dir`, including `tool_frames`.
* [cuMotion RMPflow Tutorial](../cumotion/tutorial_rmpflow.html#isaac-sim-cumotion-tutorial-rmpflow) — full tutorial on `RmpFlowController`, including parameter tuning via `get_rmp_flow_config().set_param`.

### PINK Differential IK

This example demonstrates an alternative motion controller: **PINK differential IK**. The same pick-and-place sequence is implemented using the `PinkIKController`, which solves inverse kinematics using [PINK](https://github.com/stephane-caron/pink) and [Pinocchio](https://github.com/stack-of-tasks/pinocchio).

Run this example with:

```python
# Load the built-in PINK robot model for the UR10
./python.sh standalone_examples/tutorials/manipulation/tutorial_9_pick_place_pink.py
# Load a custom URDF
./python.sh standalone_examples/tutorials/manipulation/tutorial_9_pick_place_pink.py --urdf <path_to_urdf>
```

**Key concepts:**

* `load_pink_supported_robot("ur10")` loads the built-in PINK robot model for the UR10, backed by a Pinocchio model. Alternatively, a custom URDF can be loaded using `load_pink_robot` by passing in `--urdf <path_to_urdf>`.
* `PinkIKController` accepts a tool frame name, position and orientation costs, a posture cost, and a QP solver (`"osqp"`). It integrates Cartesian velocity commands into joint positions each step.
* `_init_pink_q0` sets `pink_robot.q0` to the elbow-up configuration. PINK’s PostureTask regularizes the IK solution toward this reference, steering the solver away from elbow-down or degenerate configurations.

tutorial\_9\_pick\_place\_pink.py — UR10ePickPlace state machine class

```python
class UR10ePickPlace:
    """Pick-and-place controller for the UR10e + 2F-140 gripper using PINK differential IK.

    Phases:
        0  Pre-grasp  — arm moves above the cube
        1  Approach   — arm descends to grasp height
        2  Grasp      — gripper closes
        3  Lift       — arm rises with the cube
        4  Transport  — arm moves above the target location
        5  Lower      — arm descends to place height
        6  Release    — gripper opens
        7  Retract    — arm lifts away
    """

    _ROBOT_PRIM_PATH = "/World/ur10e_robot"
    _CUBE_PRIM_PATH = "/World/cube"
    _EE_LINK_NAME = "tool0" if args.urdf is None else "wrist_3_link"
    _GRIPPER_JOINT = "finger_joint"
    _TOOL_FRAME = "tool0" if args.urdf is None else "wrist_3_link"

    _OPEN_POS: float = 0.0
    _CLOSED_POS: float = 0.5

    _ABOVE_HEIGHT: float = 0.30
    _NEAR_HEIGHT: float = 0.185
    _TOOL_OFFSET: dict[str, float] = {
        "tool0": 0.0,
        "wrist_3_link": 0.035,
    }
    _EE_THRESHOLD: float = 0.05
    _GRIPPER_THRESHOLD: float = 0.05
    _MIN_STEPS: int = 30
    _WARMUP_FRAMES: int = 120
    _PHYSICS_DT: float = 1.0 / 60.0

    _POSITION_COST: float = 0.5
    _ORIENTATION_COST: float = 1.0
    _POSTURE_COST: float = 1e-3

    _ELBOW_UP_ARM: np.ndarray = np.array([-np.pi, -np.pi / 2, -np.pi / 2, -np.pi / 2, np.pi / 2, 0.0])
    _DOWN_ORI: np.ndarray = np.array([0.0, 0.0, 1.0, 0.0])

    _PHASE_LABELS: tuple[str, ...] = (
        "Pre-grasp: moving above cube",
        "Approach: descending to cube",
        "Grasp: closing gripper",
        "Lift: raising arm",
        "Transport: moving to target",
        "Lower: descending to place",
        "Release: opening gripper",
        "Retract: lifting arm away",
    )

    def __init__(
        self,
        urdf_path: str | None = None,
        cube_position: np.ndarray | None = None,
        target_position: np.ndarray | None = None,
        events_dt: list[int] | None = None,
    ) -> None:
        self._urdf_path = urdf_path
        self.cube_position = cube_position if cube_position is not None else np.array([0.5, 0.0, 0.025])
        self.target_position = target_position if target_position is not None else np.array([0.5, 0.5, 0.05])
        self.events_dt = events_dt or [80, 80, 20, 40, 130, 40, 20, 40]

        self._event: int = 0
        self._step: int = 0
        self._t: float = 0.0
        self._warmup_remaining: int = self._WARMUP_FRAMES

        self._articulation: Articulation | None = None
        self._ee_prim: GeomPrim | None = None
        self._finger_idx: int | None = None
        self._pink_robot: PinkRobot | None = None
        self._controller: PinkIKController | None = None
        self._tool_frame: str | None = None

    async def setup_scene(self) -> None:
        """Build the scene and initialize the PINK IK controller."""
        assets_root_path = await get_assets_root_path_async()
        stage_utils.add_reference_to_stage(
            usd_path=assets_root_path
            + "/Isaac/Samples/Rigging/Manipulator/configure_manipulator/ur10e/ur/ur_gripper.usd",
            path=self._ROBOT_PRIM_PATH,
        )

        GroundPlane("/World/GroundPlane")
        DomeLight("/World/DomeLight").set_intensities(1000)

        cube_obj = Cube(
            paths=self._CUBE_PRIM_PATH, positions=[self.cube_position], sizes=1.0, scales=[0.05, 0.05, 0.05]
        )
        RigidPrim(paths=cube_obj.paths)
        GeomPrim(paths=cube_obj.paths, apply_collision_apis=True)

        await omni.kit.app.get_app().next_update_async()
        set_camera_view(eye=[1.5, 1.5, 1.0], target=[0.5, 0.0, 0.2], camera_prim_path="/OmniverseKit_Persp")

        self._articulation = Articulation(self._ROBOT_PRIM_PATH)
        await omni.kit.app.get_app().next_update_async()

        n_dofs = len(self._articulation.dof_names)
        self._articulation.set_default_state(
            dof_positions=np.concatenate([self._ELBOW_UP_ARM, np.zeros(max(0, n_dofs - 6))])
        )

        if self._urdf_path is not None:
            self._pink_robot = load_pink_robot(urdf_path=self._urdf_path)
        else:
            self._pink_robot = load_pink_supported_robot("ur10")
        if self._TOOL_FRAME not in self._TOOL_OFFSET:
            raise ValueError(
                f"Tool frame '{self._TOOL_FRAME}' has no entry in _TOOL_OFFSET. "
                f"Add it: {list(self._TOOL_OFFSET.keys())}"
            )
        self._init_pink_q0()

        self._controller = PinkIKController(
            pink_robot=self._pink_robot,
            robot_joint_space=self._articulation.dof_names,
            robot_site_space=[self._TOOL_FRAME],
            tool_frame=self._TOOL_FRAME,
            position_cost=self._POSITION_COST,
            orientation_cost=self._ORIENTATION_COST,
            posture_cost=self._POSTURE_COST,
            solver="osqp",
            dt=self._PHYSICS_DT,
        )

    def initialize_after_play(self) -> None:
        """Resolve EE link and gripper DOF index. Call once after physics starts."""
        link_names = self._articulation.link_names
        if self._EE_LINK_NAME in link_names:
            self._ee_prim = GeomPrim(paths=self._articulation.link_paths[0][link_names.index(self._EE_LINK_NAME)])
        else:
            print(f"WARNING: '{self._EE_LINK_NAME}' not found. Available: {link_names}")

        dof_names = self._articulation.dof_names
        if self._GRIPPER_JOINT in dof_names:
            self._finger_idx = dof_names.index(self._GRIPPER_JOINT)
        else:
            print(f"WARNING: '{self._GRIPPER_JOINT}' not found. Available: {dof_names}")

        self._articulation.reset_to_default_state()

    def _init_pink_q0(self) -> None:
        """Set pink_robot.q0 to elbow-up for PostureTask regularization."""
        import pinocchio as pin

        elbow_up_map = {
            "shoulder_pan_joint": -np.pi / 2,
            "shoulder_lift_joint": -np.pi / 2,
            "elbow_joint": -np.pi / 2,
            "wrist_1_joint": -np.pi / 2,
            "wrist_2_joint": np.pi / 2,
            "wrist_3_joint": 0.0,
        }
        q0 = pin.neutral(self._pink_robot.model)
        for name, angle in elbow_up_map.items():
            if self._pink_robot.model.existJointName(name):
                jid = self._pink_robot.model.getJointId(name)
                q0[self._pink_robot.model.joints[jid].idx_q] = angle
        self._pink_robot.q0 = q0

    def _phase_ee_target(self) -> np.ndarray:
        c, p = self.cube_position, self.target_position
        offset = self._TOOL_OFFSET[self._TOOL_FRAME]
        hi = self._ABOVE_HEIGHT + offset
        lo = self._NEAR_HEIGHT + offset
        targets = {
            0: [c[0], c[1], c[2] + hi],
            1: [c[0], c[1], c[2] + lo],
            2: [c[0], c[1], c[2] + lo],
            3: [c[0], c[1], c[2] + hi],
            4: [p[0], p[1], p[2] + hi],
            5: [p[0], p[1], p[2] + lo],
            6: [p[0], p[1], p[2] + lo],
            7: [p[0], p[1], p[2] + hi],
        }
        return np.array(targets[self._event], dtype=np.float32)

    def _make_setpoint(self, position: np.ndarray) -> mg.RobotState:
        return mg.RobotState(
            sites=mg.SpatialState.from_name(
                spatial_space=[self._TOOL_FRAME],
                positions=([self._TOOL_FRAME], wp.array([position.tolist()], dtype=wp.float32)),
                orientations=([self._TOOL_FRAME], wp.array([self._DOWN_ORI.tolist()], dtype=wp.float32)),
            ),
        )

    def _estimated_state(self) -> mg.RobotState:
        names = self._articulation.dof_names
        return mg.RobotState(
            joints=mg.JointState.from_name(
                robot_joint_space=names,
                positions=(names, self._articulation.get_dof_positions()),
                velocities=(names, self._articulation.get_dof_velocities()),
            )
        )

    def _set_gripper(self, pos: float) -> None:
        if self._finger_idx is not None:
            self._articulation.set_dof_position_targets(
                wp.array([pos], dtype=wp.float32), dof_indices=[self._finger_idx]
            )

    def _ee_near_target(self) -> bool:
        if self._ee_prim is None:
            return False
        ee_pos = self._ee_prim.get_world_poses()[0].numpy()[0]
        return bool(np.linalg.norm(ee_pos - self._phase_ee_target()) < self._EE_THRESHOLD)

    def _gripper_at(self, target: float) -> bool:
        if self._finger_idx is None:
            return False
        pos = float(self._articulation.get_dof_positions().numpy().flatten()[self._finger_idx])
        return abs(pos - target) < self._GRIPPER_THRESHOLD

    def _phase_converged(self) -> bool:
        if self._step < self._MIN_STEPS:
            return False
        if self._event == 2:
            return self._gripper_at(self._CLOSED_POS)
        if self._event == 6:
            return self._gripper_at(self._OPEN_POS)
        return self._ee_near_target()

    def forward(self) -> bool:
        """Advance one simulation step. Returns False when the sequence is complete."""
        if self.is_done():
            return False

        if self._warmup_remaining > 0:
            n_dofs = len(self._articulation.dof_names)
            targets = np.concatenate([self._ELBOW_UP_ARM, np.zeros(max(0, n_dofs - 6))])
            self._articulation.set_dof_position_targets(
                wp.array(targets, dtype=wp.float32), dof_indices=list(range(n_dofs))
            )
            self._warmup_remaining -= 1
            if np.abs(self._articulation.get_dof_positions().numpy().flatten()[:6] - self._ELBOW_UP_ARM).max() < 0.1:
                self._warmup_remaining = 0
            return True

        if self._step == 0:
            print(f"  Phase {self._event}: {self._PHASE_LABELS[self._event]}")
            if self._event in (0, 3, 7):
                if not self._controller.reset(
                    self._estimated_state(), self._make_setpoint(self._phase_ee_target()), t=0.0
                ):
                    raise RuntimeError("PinkIKController reset failed.")
                self._t = 0.0

        if self._event == 2:
            self._set_gripper(self._CLOSED_POS)
        elif self._event == 6:
            self._set_gripper(self._OPEN_POS)
        else:
            desired = self._controller.forward(
                self._estimated_state(), self._make_setpoint(self._phase_ee_target()), self._t
            )
            if desired is not None and desired.joints.positions is not None:
                self._articulation.set_dof_position_targets(
                    positions=desired.joints.positions, dof_indices=desired.joints.position_indices
                )

        self._t += self._PHYSICS_DT
        self._step += 1
        if self._phase_converged() or self._step >= self.events_dt[self._event]:
            if self._step >= self.events_dt[self._event]:
                print(f"  Phase {self._event} timed out after {self.events_dt[self._event]} frames")
            self._event += 1
            self._step = 0

        return True

    def is_done(self) -> bool:
        return self._event >= len(self.events_dt)

    def reset(self) -> None:
        self._event = 0
        self._step = 0
        self._t = 0.0
        self._warmup_remaining = self._WARMUP_FRAMES
```

See also

* [PINK Integration](../pink/index.html#isaac-sim-pink) — overview of the PINK integration and its weighted multi-task IK approach.
* [PINK IK Controller Tutorial](../pink/tutorial_ik_controller.html#isaac-sim-pink-tutorial-ik-controller) — in-depth walkthrough of `PinkIKController`, task weights, posture regularization, and QP solver selection.
* [PINK Robot Configuration Tutorial](../pink/tutorial_robot_configuration.html#isaac-sim-pink-tutorial-robot-configuration) — loading PINK robot models with `load_pink_supported_robot()` and `load_pink_robot()`.

## Summary

In this tutorial, you learned how to:

* Control the 2F-140 gripper using the Articulation API and `set_dof_position_targets`.
* Plan and execute joint-space trajectories using `mg.Path` and `mg.TrajectoryFollower`.
* Use the cuMotion `RmpFlowController` to track a Cartesian target in real time with obstacle avoidance.
* Implement an 8-phase pick-and-place sequence with cuMotion RMPflow.
* Implement the same sequence with PINK differential IK as an alternative CPU-based solver.

On this page

* [Learning Objectives](#learning-objectives)
* [Prerequisites](#prerequisites)
* [Overview](#overview)
* [Part 1: Gripper Control](#part-1-gripper-control)
* [Part 2: Arm Trajectory Following](#part-2-arm-trajectory-following)
* [Part 3: Follow Target using cuMotion RMPflow](#part-3-follow-target-using-cumotion-rmpflow)
* [Part 4: Pick and Place](#part-4-pick-and-place)
  + [cuMotion RMPflow](#cumotion-rmpflow)
  + [PINK Differential IK](#pink-differential-ik)
* [Summary](#summary)

---

### Rig Legged Robot

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/robot_setup_tutorials/tutorial_rig_legged_robot.html

* [Robot Setup](../robot_setup/index.html)
* [Robot Setup Tutorials Series](index.html)
* Tutorial 13: Rigging a Legged Robot for a Locomotion Policy

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Tutorial 13: Rigging a Legged Robot for a Locomotion Policy

This tutorial explains how to rig a legged robot to match the configuration specified by a locomotion policy.
The Isaac Sim [Policy Controller Class](../isaac_lab_tutorials/tutorial_policy_deployment.html#isaac-sim-policy-controller-class) already handles robot rigging at runtime for inference in Isaac Sim,
so this tutorial is only relevant when you want to run the robot policy from an external process, such as ROS.

## Learning Objectives

In this tutorial, you will walk through the process of rigging an H1 humanoid robot to match the configuration specified by the H1 flat terrain locomotion policy.

1. Setting the initial robot position
2. Setting the joint configuration
3. Verifying the joint configuration

Note

The H1 flat terrain policy environment definition file is available [here](https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Isaac/6.0/Isaac/Samples/Policies/H1_Policies/h1_env.yaml).

## Setting the Initial Robot Position

The initial joint position of the robot is specified under the `robot:init_state:joint_pos` section of the environment definition file. The joint names are specified using the `.*` wildcard.

```python
 1robot:
 2  init_state:
 3    joint_pos:
 4      .*_hip_yaw: 0.0
 5      .*_hip_roll: 0.0
 6      .*_hip_pitch: -0.28
 7      .*_knee: 0.79
 8      .*_ankle: -0.52
 9      torso: 0.0
10      .*_shoulder_pitch: 0.28
11      .*_shoulder_roll: 0.0
12      .*_shoulder_yaw: 0.0
13      .*_elbow: 0.52
14    joint_vel:
15      .*: 0.0
```

Note

The joint positions are specified in radians, whereas USD joint positions are specified in degrees.

To store the initial state of the robot:

1. Open the `h1.usd` file from the Content Browser at `Isaac Sim/Robots/Unitree/H1`.
2. In the upper-right corner of the stage, select the `funnel` icon and click `Physics Joints` to filter the joint list.
3. Left-click the first joint (`left_hip_yaw`), then Shift-left-click the last joint (`right_elbow`) to select all joints.
4. Right-click any selected joint and click **Add** > **Physics** > **Joint State Angular** to create a Joint State API attribute on the joints.
5. Right-click any selected joint and click **Add** > **Physics** > **Angular drive** to create a joint drive API attribute on the joints.

Note

The `Joint State Angular` API reports the joint position and velocity, and the `Angular drive` API drives the joint. If the joint already has a `Joint State Angular` API or `Angular drive` API, you can skip the previous two steps.

6. For each active joint, convert the `joint_pos` and `joint_vel` values from radians to degrees.
7. Left-click the joint you are changing.
8. In the Property panel, scroll down to the `Target Position` attribute.
9. Set the `Target Position` attribute to the converted value from the `joint_pos` attribute in the environment definition file.
10. Set the `Target Velocity` attribute to the converted value from the `joint_vel` attribute in the environment definition file.
11. Repeat the previous steps for each active joint.
12. Press play.

Note

When using Newton, physics initialization might fail because reversed joints are not supported for `/h1/Joints/torso`. If this happens, select the `torso` joint. In the Property panel, go to **Physics** > **Joint** and swap the joint bodies so `Body 0` is `/h1/torso_link` and `Body 1` is `/h1/pelvis`.

13. Verify that the robot moves to the initial position specified in the environment definition file. To make the robot start in the initial position when the simulation starts, store the data in the Joint State API.
14. To prevent the robot from falling indefinitely, add a fixed joint between the robot and the world by right-clicking `/h1/torso_link` and selecting **Create** > **Physics** > **Joint** > **Fixed Joint**.

To save the robot pose:

1. In the upper-left corner of the stage, click **Edit** > **Preferences**.
2. In the **Preferences** window, click the **Physics** tab in the left sidebar.
3. Uncheck **Reset Simulation on Stop**.
4. Play the simulation and stop it when the robot reaches the desired initial pose. Repeat this step once more to ensure the pose is saved even after reset.
5. Delete the fixed joint between the robot and the world.
6. Press **Ctrl+S** to save the USD file.
7. Check **Reset Simulation on Stop** again.

## Setting the Joint Configuration

Set the joint configuration to match the policy’s robot configuration. This may be different from the values stored in the USD file.
The joint drive configuration is specified under the `scene:robot:actuators` section of the environment definition file.

The following snippet shows the actuator configuration for the H1 robot legs.

```python
 1actuators:k
 2  legs:
 3    class_type: omni.isaac.lab.actuators.actuator_pd:ImplicitActuator
 4    joint_names_expr:
 5    - .*_hip_yaw
 6    - .*_hip_roll
 7    - .*_hip_pitch
 8    - .*_knee
 9    - torso
10    effort_limit: 300
11    velocity_limit: 100.0
12    stiffness:
13      .*_hip_yaw: 150.0
14      .*_hip_roll: 150.0
15      .*_hip_pitch: 200.0
16      .*_knee: 200.0
17      torso: 200.0
18    damping:
19      .*_hip_yaw: 5.0
20      .*_hip_roll: 5.0
21      .*_hip_pitch: 5.0
22      .*_knee: 5.0
23      torso: 5.0
24    armature: null
25    friction: null
```

The `joint_names_expr` is a list of joint names to be controlled by the actuator. The `class_type` is the actuator type.
The `effort_limit` is the maximum effort that can be applied to the joint. The `velocity_limit` is the maximum velocity that can be applied to the joint.
The `stiffness` defines the joint stiffness. The `damping` defines the joint damping. The `armature` defines the joint armature, and the `friction` defines the joint friction.

To set the joint configurations:

1. Left-click a joint, such as `left_hip_yaw`.
2. In the Property panel, scroll down to the `Joint Drive` attribute and set `stiffness` and `damping` to the values specified in the environment definition file.

Note

Remember to convert stiffness and damping to degree-based units.

The USD file stiffness is in \(\frac{kg \cdot m^2}{deg \cdot s^2}\) and the damping is in \(\frac{kg \cdot m^2}{deg \cdot s}\).
To convert radians to degrees, you can use the following formulas:

\[S\_{deg} = S\_{rad} \times \frac{\pi}{180}\]

\[D\_{deg} = D\_{rad} \times \frac{\pi}{180}\]

The `effort_limit` is the maximum effort that can be applied to the joint. Set that value to the `Max Force` attribute of the joint drive API.

Scroll down to **Raw USD Properties** under the **Advanced** tab, and set the **Armature** and **Joint Friction** attributes to the values specified in the environment definition file.

For the **Maximum Joint Velocity** attribute, set it to the **velocity\_limit** value specified in the environment definition file. Remember to convert it to degrees.

\[\omega\_{deg} = \omega\_{rad} \times \frac{180}{\pi}\]

Note

Remember to set the joint configurations for all active joints in the robot, such as the arms and legs.

## Verifying the Joint Configuration

To verify the joint configuration, you can play the simulation and run the following snippet in Script Editor to print the joint configuration.

1. Play the simulation.
2. Open Script Editor by clicking **Window** > **Script Editor**.
3. Copy and paste the following snippet into Script Editor.
4. Run the snippet by clicking the **Run** button.

   ```python
   from isaacsim.core.experimental.prims import Articulation

   prim = Articulation("/h1")
   print(prim.dof_names)
   lower, upper = prim.get_dof_limits()
   stiffnesses, dampings = prim.get_dof_gains()
   max_velocities = prim.get_dof_max_velocities()
   max_efforts = prim.get_dof_max_efforts()
   for i, name in enumerate(prim.dof_names):
       print(
           f"  {name}: lower={lower.numpy()[0][i]:.4f}, upper={upper.numpy()[0][i]:.4f}, "
           f"maxVelocity={max_velocities.numpy()[0][i]:.2f}, maxEffort={max_efforts.numpy()[0][i]:.0f}, "
           f"stiffness={stiffnesses.numpy()[0][i]:.2f}, damping={dampings.numpy()[0][i]:.2f}"
       )
   ```
5. Verify that you see console output similar to the following:

```python
['left_hip_yaw', 'right_hip_yaw', 'torso', 'left_hip_roll', 'right_hip_roll', 'left_shoulder_pitch', 'right_shoulder_pitch', 'left_hip_pitch', 'right_hip_pitch', 'left_shoulder_roll', 'right_shoulder_roll', 'left_knee', 'right_knee', 'left_shoulder_yaw', 'right_shoulder_yaw', 'left_ankle', 'right_ankle', 'left_elbow', 'right_elbow']
  left_hip_yaw: lower=-0.4300, upper=0.4300, maxVelocity=100.00, maxEffort=300, stiffness=149.54, damping=5.00
  right_hip_yaw: lower=-0.4300, upper=0.4300, maxVelocity=100.00, maxEffort=300, stiffness=149.54, damping=5.00
  torso: lower=-2.3500, upper=2.3500, maxVelocity=100.00, maxEffort=300, stiffness=200.00, damping=4.98
  left_hip_roll: lower=-0.4300, upper=0.4300, maxVelocity=100.00, maxEffort=300, stiffness=149.54, damping=5.00
  right_hip_roll: lower=-0.4300, upper=0.4300, maxVelocity=100.00, maxEffort=300, stiffness=149.54, damping=5.00
  left_shoulder_pitch: lower=-2.8700, upper=2.8700, maxVelocity=100.00, maxEffort=300, stiffness=40.00, damping=10.00
  right_shoulder_pitch: lower=-2.8700, upper=2.8700, maxVelocity=100.00, maxEffort=300, stiffness=40.00, damping=10.00
  left_hip_pitch: lower=-3.1400, upper=2.5300, maxVelocity=100.00, maxEffort=300, stiffness=199.96, damping=5.00
  right_hip_pitch: lower=-3.1400, upper=2.5300, maxVelocity=100.00, maxEffort=300, stiffness=199.96, damping=5.00
  left_shoulder_roll: lower=-0.3400, upper=3.1100, maxVelocity=100.00, maxEffort=300, stiffness=40.00, damping=10.00
  right_shoulder_roll: lower=-3.1100, upper=0.3400, maxVelocity=100.00, maxEffort=300, stiffness=40.00, damping=10.00
  left_knee: lower=-0.2600, upper=2.0500, maxVelocity=100.00, maxEffort=300, stiffness=200.00, damping=4.98
  right_knee: lower=-0.2600, upper=2.0500, maxVelocity=100.00, maxEffort=300, stiffness=200.00, damping=4.98
  left_shoulder_yaw: lower=-1.3000, upper=4.4500, maxVelocity=100.00, maxEffort=300, stiffness=40.00, damping=10.00
  right_shoulder_yaw: lower=-4.4500, upper=1.3000, maxVelocity=100.00, maxEffort=300, stiffness=40.00, damping=10.00
  left_ankle: lower=-0.8700, upper=0.5200, maxVelocity=100.00, maxEffort=100, stiffness=20.00, damping=4.00
  right_ankle: lower=-0.8700, upper=0.5200, maxVelocity=100.00, maxEffort=100, stiffness=20.00, damping=4.00
  left_elbow: lower=-1.2500, upper=2.6100, maxVelocity=100.00, maxEffort=300, stiffness=40.00, damping=10.00
  right_elbow: lower=-1.2500, upper=2.6100, maxVelocity=100.00, maxEffort=300, stiffness=40.00, damping=10.00
```

The limit values in the console output are in radians. Each line shows the properties for a single DOF.
Verify that the `maxVelocity`, `maxEffort`, `stiffness`, and `damping` values match the values specified in the environment definition file.

For example, for `left_hip_yaw`, the max velocity is `100.0`, the max effort is `300.0`, the stiffness is `150.0`, and the damping is `5.0`.

Note

The rigged H1 robot is available in the Content Browser at `Isaac/Samples/Rigging/H1/h1_rigged.usd`.

## Summary

This tutorial covers the following topics:

* Setting the initial robot position
* Setting the joint configuration
* Verifying the joint configuration

On this page

* [Learning Objectives](#learning-objectives)
* [Setting the Initial Robot Position](#setting-the-initial-robot-position)
* [Setting the Joint Configuration](#setting-the-joint-configuration)
* [Verifying the Joint Configuration](#verifying-the-joint-configuration)
* [Summary](#summary)

---

