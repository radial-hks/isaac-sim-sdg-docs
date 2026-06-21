---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/robot_setup/ext_isaacsim_util_merge_mesh.html
title: "Merge Mesh Utility"
section: "Setup 工具"
module: "07-robot-setup"
checksum: "45071ac96add937d"
fetched: "2026-06-21T13:40:06"
---

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