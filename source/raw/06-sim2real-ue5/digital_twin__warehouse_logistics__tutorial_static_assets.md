---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/digital_twin/warehouse_logistics/tutorial_static_assets.html
title: "Static Assets"
section: "数字孪生"
module: "06-sim2real-ue5"
checksum: "c6e7bff5f44674d7"
fetched: "2026-06-21T14:14:29"
---

* [Digital Twin](../index.html)
* Static Warehouse Assets

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Static Warehouse Assets

Isaac Sim comes with a multitude of assets for you to build your own application. Additionally, there are extra asset libraries provided by NVIDIA that you can use. Open **Window** > **Browsers** > **NVIDIA Assets**, and the window **NVIDIA Assets** will show, where you can browse for all content to build your environment.

Let’s start by setting up the warehouse building. click on the **+** Icon next to **Industrial**, then on **Buildings**, and select **Warehouse**. By dragging **Warehouse01** to the scene, you’ll load a reference to the asset on your stage. Alternatively, you can also [build a custom warehouse](ext_omni_warehouse_creator.html).

Note

If you drag on the viewport window, it will let you place it at an arbitrary position, If instead you want it placed at the origin or on a given xform, drag it into the Stage window on top of the desired Prim.

Depending on which assets you goals, you may find **NVIDIA Assets** that are currently on a centimeter scale. This is because **NVIDIA Assets** are created by our art team, while **Isaac Sim Assets** have been curated with intent. Be mindful of the units! When importing certain assets, you may need to manually scale them down to units of 0.01. To do this, select the asset prim, click on “Add Transform” on the Properties pane, and set the scale to 0.01 on all directions.

Note

You can add a 0.01 scale on the parent prim you are adding the assets to instead (for example create a prim at /World/Warehouse\_Import and always drag the assets into it), and then all assets will be imported already scaled.

Now you can add some shelves for empty shelves, or racks for shelves filled with boxes.

Any asset in **NVIDIA Assets** can be used to compose your scene, browse around the categories to find the asset you need, or search by name.

## Simulation Needs

These assets are purely visual, so any simulation needs you may have need to be authored on top of it. In that case, the recommendation is to create a new stage, and drag one single asset to it and perform the desired authoring as a variation of the original asset, and save it on your nucleus. Then, on your environment, drag the asset you saved that contains the modifications.

## SimReady Assets

Omniverse also contains a suite of [SimReady Assets](https://docs.omniverse.nvidia.com/simready/latest/index.html), which are assets curated for machine learning and digital twins. These assets come fully annotated for Semantic Labeling, and also contains a preset physics setup so you can get started with your digital twin operation. For more details, visit the [NVIDIA On Demand session: SimReady Specification](https://www.nvidia.com/en-us/on-demand/session/omniverse2020-om1742/?playlistId=playList-63b157fe-95fe-4b93-8b9b-d731be32ec29)

### Example

Let’s make a variation of WarehousePile\_A04 that contains physics properties, with boxes being individual rigid bodies.

We start with a brand new Stage, and create an Xform under World with the name “Import”, and set its scale to 0.01

Then we drag the WarehousePile\_A04 into it.

To simplify the tree, we can bring the imported prim at the root. Click on the Option button on the stage, and select Show Root, then drag WareHousePile\_A04 on the Root, then right-click it, and select Set as Default Prim. Delete /World and /Environment. Next, select all children of /WareHousePile\_A04, and on the Properties pane, press **Add** > **Physics** > **Rigid Body with Colliders preset**. To see the effect of the rigid body API, add a ground plane by going to **Create** > **Physics** > **Ground Plane**, and start simulation. Try shift-click to drag one of the lower boxes, they should all fall over each other.

You can now go back to the previously saved asset to customize it to contain physics material properties, different mass properties, and so on. All changes will be stored locally and be applied on top of the original asset. To see the local changes, you can go to the Layer tab, right click the Root layer, and click on Edit.

You will see that the USD file opens in edit mode on your text editor, containing the reference to the original asset, and all “deltas” that are being applied to it.

On this page

* [Simulation Needs](#simulation-needs)
* [SimReady Assets](#simready-assets)
  + [Example](#example)