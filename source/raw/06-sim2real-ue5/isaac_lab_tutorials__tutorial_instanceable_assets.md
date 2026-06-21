---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/isaac_lab_tutorials/tutorial_instanceable_assets.html
title: "Instanceable Assets"
section: "Isaac Lab (RL)"
module: "06-sim2real-ue5"
checksum: "7df94f615bb36623"
fetched: "2026-06-21T14:14:30"
---

* [Isaac Lab](index.html)
* Instanceable Assets

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Instanceable Assets

Reinforcement learning often requires training in large simulation scenes with multiple clones of the same robots. As we add more and more robots into the simulation environment, the memory consumption also increases for each additional set of robot and mesh assets added. To reduce memory consumption, we can take advantage of USD’s [Scenegraph Instancing](https://graphics.pixar.com/usd/dev/api/_usd__page__scenegraph_instancing.html) functionality to mark common meshes shared by different copies of the same robots as instanceable.

By doing so, each copy of the robot will reference a single copy of meshes, avoiding the need to create multiple copies of the same meshes in the scene, thus reducing memory usage in the overall simulation environment.

## Learning Objectives

In this tutorial, we will show how to create instanceable assets in Isaac Sim. We will

1. Explain requirements for making assets instanceable
2. Use the URDF and MJCF importers to create instanceable assets
3. Show utility methods to convert existing assets to instanceable assets

*10-15 Minute Tutorial*

## Getting Started

* Please refer to USD Documentation on [Scenegraph Instancing](https://graphics.pixar.com/usd/dev/api/_usd__page__scenegraph_instancing.html) for more details on instancing.
* Please refer to [Tutorial: Import URDF](../importer_exporter/import_urdf.html#isaac-sim-app-tutorial-advanced-import-urdf) and [Tutorial: Import MJCF](../importer_exporter/import_mjcf.html#isaac-sim-app-tutorial-advanced-import-mjcf) for more details on importer functionalities.

## Hierarchy Requirement for Instanceable Assets

USD prohibits modifying properties of prims on descendants of instanced prims. Therefore, we generally only perform instancing on mesh prims for robot assets, since properties on meshes will not differ across different environments during simulation. However, the transforms of the meshes may be different during simulation when robots in each environment are being moved in varying ways. Thus, we have to define the topology of our robot hierarchy in a specific structure in the asset tree definition in order for the instanceable flag to take action.

To mark any mesh or primitive geometry prim in the asset as instanceable, the mesh prim requires a parent Xform prim to be present, which will be used to add a reference to a master USD file containing definition of the mesh prim.

For example, the following definition cannot be marked instanceable:

```python
World
  |_ Robot
       |_ Collisions
               |_ Sphere
               |_ Box
```

Instead, it will have to be modified to:

```python
World
  |_ Robot
       |_ Collisions
               |_ Sphere_Xform
               |      |_ Sphere
               |_ Box_Xform
                      |_ Box
```

Any references that exist on the original Sphere and Box prims would have to be moved to Sphere\_Xform and Box\_Xform prims.

## Using URDF and MJCF Importers

Isaac Sim provides two importers - URDF and MJCF - for converting robot assets to USD format to be used in Isaac Sim. Both importers support the option to import robot assets directly as instanceable assets. By selecting this option, imported assets will be split into two separate USD files that follow the above hierarchy definition. Any mesh data will be written to an USD stage to be referenced by the main USD stage, which contains the main robot definition.

To use the Instanceable option in the importers, first check the Create Instanceable Asset option. Then, specify a file path to indicate the location for saving the mesh data in the Instanceable USD Path textbox. This will default to ./instanceable\_meshes.usd, which will generate a file instanceable\_meshes.usd that is saved to the current directory.

Once the asset is imported with these options enabled, you will see the robot definition in the stage - we will refer to this stage as the master stage. If we expand the robot hierarchy in the Stage, we will notice that the parent prims that have mesh descendants have been marked as Instanceable and they reference a prim in our Instanceable USD Path USD file. We are also no longer able to modify attributes of descendant meshes.

To add our instanced asset into a new stage, we will simply need to add our master USD file.

## Modifying Existing Assets

Due to limitations of the topology requirement for making assets instanceable, it is not as straightforward to convert existing non-instanceable assets to become instanceable. Here, we will try to provide a few small utility methods to help make the process simpler.

All utilities should be copied into and run from the script editor, which can be opened from Window > Script Editor.

First, we need to make sure our existing asset follows the hierarchy constraint defined above, where all mesh prims have a parent XForm prim present that can be used to mark the prim as instanceable. To help with the process of creating new parent prims, we provide a utility method create\_parent\_xforms() below to automatically insert a new Xform prim as a parent of every mesh prim in the stage.

```python
import omni.client
import omni.usd
from pxr import Sdf, UsdGeom

def create_parent_xforms(asset_usd_path, source_prim_path, save_as_path=None):
    """Adds a new UsdGeom.Xform prim for each Mesh/Geometry prim under source_prim_path.
    Moves material assignment to new parent prim if any exists on the Mesh/Geometry prim.

    Args:
        asset_usd_path (str): USD file path for asset
        source_prim_path (str): USD path of root prim
        save_as_path (str): USD file path for modified USD stage. Defaults to None, will save in same file.
    """
    omni.usd.get_context().open_stage(asset_usd_path)
    stage = omni.usd.get_context().get_stage()

    prims = [stage.GetPrimAtPath(source_prim_path)]
    edits = Sdf.BatchNamespaceEdit()
    while len(prims) > 0:
        prim = prims.pop(0)
        print(prim)
        if prim.GetTypeName() in ["Mesh", "Capsule", "Sphere", "Box"]:
            new_xform = UsdGeom.Xform.Define(stage, str(prim.GetPath()) + "_xform")
            print(prim, new_xform)
            edits.Add(Sdf.NamespaceEdit.Reparent(prim.GetPath(), new_xform.GetPath(), 0))
            continue

        children_prims = prim.GetChildren()
        prims = prims + children_prims

    stage.GetRootLayer().Apply(edits)

    if save_as_path is None:
        omni.usd.get_context().save_stage()
    else:
        omni.usd.get_context().save_as_stage(save_as_path)
```

This method can be run on an existing non-instanced USD file for an asset from the script editor, where:

* asset\_usd\_path is the file path to the current existing USD asset
* source\_prim\_path is the USD prim path to the root prim of the asset
* save\_as\_path is a different file path to same the modified asset to. This can be left unspecified to overwrite the existing file.

```python
create_parent_xforms(asset_usd_path=ASSET_USD_PATH, source_prim_path=SOURCE_PRIM_PATH, save_as_path=SAVE_AS_PATH)
```

It is worth noting that any [USD Relationships](https://graphics.pixar.com/usd/dev/api/class_usd_relationship.html) on the referenced meshes will be removed. This is because those USD Relationships originally have targets set to prims in the original prim that may no longer be valid and hence cannot be accessed from the new stage. Common examples of USD Relationships that could exist on the meshes are visual materials, physics materials, and filtered collision pairs. Therefore, it is recommended to set these USD Relationships on the meshes’ parent Xforms instead of the meshes themselves.

The above method can also be run as part of an overall conversion process, which is defined in the utility below. This utility will first insert new parent prims if create\_xforms=True is specified, and generate a new USD file that is used for referencing. It will then traverse through the asset tree and mark the parent prim of any mesh or primitive type prims as instanceable, along with inserting a reference to the mesh USD stage.

```python
def convert_asset_instanceable(asset_usd_path, source_prim_path, save_as_path=None, create_xforms=True):
    """Makes all mesh/geometry prims instanceable.
    Can optionally add UsdGeom.Xform prim as parent for all mesh/geometry prims.
    Makes a copy of the asset USD file, which will be used for referencing.
    Updates asset file to convert all parent prims of mesh/geometry prims to reference cloned USD file.

    Args:
        asset_usd_path (str): USD file path for asset
        source_prim_path (str): USD path of root prim
        save_as_path (str): USD file path for modified USD stage. Defaults to None, will save in same file.
        create_xforms (bool): Whether to add new UsdGeom.Xform prims to mesh/geometry prims.
    """

    if create_xforms:
        create_parent_xforms(asset_usd_path, source_prim_path, save_as_path)
        asset_usd_path = save_as_path

    instance_usd_path = ".".join(asset_usd_path.split(".")[:-1]) + "_meshes.usd"
    omni.client.copy(asset_usd_path, instance_usd_path)
    omni.usd.get_context().open_stage(asset_usd_path)
    stage = omni.usd.get_context().get_stage()

    prims = [stage.GetPrimAtPath(source_prim_path)]
    while len(prims) > 0:
        prim = prims.pop(0)
        if prim:
            if prim.GetTypeName() in ["Mesh", "Capsule", "Sphere", "Box"]:
                parent_prim = prim.GetParent()
                if parent_prim and not parent_prim.IsInstance():
                    parent_prim.GetReferences().AddReference(
                        assetPath=instance_usd_path, primPath=str(parent_prim.GetPath())
                    )
                    parent_prim.SetInstanceable(True)
                    continue

            children_prims = prim.GetChildren()
            prims = prims + children_prims

    if save_as_path is None:
        omni.usd.get_context().save_stage()
    else:
        omni.usd.get_context().save_as_stage(save_as_path)
```

## Summary

This tutorial covered the following topics:

1. Requirements for creating instanceable assets
2. Using the URDF and MJCF Importers to create instanceable assets
3. Making existing assets instanceable

On this page

* [Learning Objectives](#learning-objectives)
* [Getting Started](#getting-started)
* [Hierarchy Requirement for Instanceable Assets](#hierarchy-requirement-for-instanceable-assets)
* [Using URDF and MJCF Importers](#using-urdf-and-mjcf-importers)
* [Modifying Existing Assets](#modifying-existing-assets)
* [Summary](#summary)