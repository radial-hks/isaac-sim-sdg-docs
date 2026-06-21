---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/robot_setup/asset_transformer_tutorials.html
title: "Asset Transformer Tutorials"
section: "Setup 工具"
module: "07-robot-setup"
checksum: "028374d282bb4c9e"
fetched: "2026-06-21T13:40:05"
---

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