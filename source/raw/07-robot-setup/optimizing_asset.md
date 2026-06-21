---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/robot_setup_tutorials/optimizing_asset.html
title: "Optimizing Asset"
section: "Setup 教程"
module: "07-robot-setup"
checksum: "464d44f54c80d2bc"
fetched: "2026-06-21T13:40:07"
---

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