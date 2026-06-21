---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/omniverse_usd/intro_to_usd.html
title: "Intro to USD"
section: "OpenUSD"
module: "01-concepts"
checksum: "1f7eedbcb43e333d"
fetched: "2026-06-21T13:39:51"
---

* [Omniverse and USD](index.html)
* Working with USD

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Working with USD

## Learning Objectives

This tutorial covers how to:

* save USD stages
* load and reference existing USD stages
* Organize stage tree hierarchy

## Saving Options

* **Save**: To save the current USD stage, go to the Menu Bar and click *Files > Save* or *Files > Save As ..* to save as a new file.
* **Save Flattened As**: Saves the current USD file while merging all components to one mesh.
* **as .usda files**: You have the option to save as `.usda` file instead of `.usd` file. `.usda` file is a human-readable text file format for the given USD stage.
* **Collect Assets**: If your current stage used many reference USD stages, materials, and textures from other folders and servers, you must *Collect Assets* to make sure all the external references that are used in your stage get collected in one folder. To do so, save the current USD locally, then find it in the *Content* tab, right-click on it, and select *Collect Asset*.

try {
var kalturaPlayer = KalturaPlayer.setup({
targetId: "kaltura\_player\_1",
provider:
{ partnerId: 2935771, uiConfId: 46302491 }
});
kalturaPlayer.loadMedia(
{entryId: '1\_rhc2d1dw'}
);
} catch (e)
{ console.error(e.message) }

## Loading Options

* **Open**: To load a USD stage, go to Menu Bar and click *Files > Open*. This opens the USD stage for direct editing.
* **Add Reference**: *Files > Add Reference* adds a USD file as a reference. Or find the file in the *Content* Tab and drag it into the viewport. You can not edit the referenced USD.

### Set the Stage for a Reference

To demonstrate adding a file as reference, save the current stage with the cube and cylinders as a mock robot.
First, you must rearrange the rigid bodies on the stage into a hierarchical structure with meaningful names.
Put all the rigid body parts of the robot under a single [Prim](../reference_material/reference_glossary.html#isaac-sim-glossary-prim).

1. Right click inside the *Stage* tab, select *Create > Xform*.
2. Rename the newly added [Xform](https://docs.omniverse.nvidia.com/utilities/latest/common/glossary-of-terms.html#term-XForm "(in Omniverse Utilities)") to *mock\_robot*. The Prim appears under the *World* prim.
3. Drag and drop the Cube, both Cylinders, Physics Material, and Looks folder under *mock\_robot*.
4. Rename the Cube and Cylinders to the body, wheel\_left, and wheel\_right.
5. Save the stage as an USD file.

   > try {
   > var kalturaPlayer = KalturaPlayer.setup({
   > targetId: "kaltura\_player\_2",
   > provider:
   > { partnerId: 2935771, uiConfId: 46302491 }
   > });
   > kalturaPlayer.loadMedia(
   > {entryId: '1\_szx9q5qp'}
   > );
   > } catch (e)
   > { console.error(e.message) }
6. Open a new stage.
7. Load the USD file as a reference, either *Files > Add Reference* or drag the file from *Content* on to the stage. It loads the referenced USD under a Prim withe the same name as the USD filename.
8. Validate that it loaded everything under the original `World(defaultPrim)`, including `PhysicsScene`, `defaultLight`, and `GroundPlane`. This may not be optimal if you are loading multiple USD references that all have their own version of PhysicsScenes and defaultLights. You cannot delete them on the new stage because they are loaded by reference, but deleting them in the original USD would make it difficult to work within those USD stages.

To have the necessary environment set up in the USD stages but not export them when they are being referenced, you need to move non-referenced items out of the default Prim:

* Select the robot’s parent prim on stage, in this tutorial /mock\_robot.
* Open the menu *Edit* while the prim is selected, and click on *unparent*.
* Validate that instead of being under World, mock\_robot is parallel to World.
* Right-click on the robot prim again on stage, and *Set as a Default Prim*. Save.
* Open a new stage and load the same file again as a reference, verify that only the robot is imported.

try {
var kalturaPlayer = KalturaPlayer.setup({
targetId: "OVK1624\_Isaac-tutorial-gui-set-default-prim",
provider: {
partnerId: 2935771,
uiConfId: 53712482
}
});
kalturaPlayer.loadMedia({entryId: '1\_01lzd38n'});
} catch (e) {
console.error(e.message)
}

## Summary

In this tutorial, you learned how to save and open USD files.

### Further Readings

More on [File Menu](https://docs.omniverse.nvidia.com/composer/latest/menu_file.html "(in Omniverse USD Composer)"), [Collect Assets](https://docs.omniverse.nvidia.com/extensions/latest/ext_collect.html "(in Omniverse Extensions)"), and others in [Composer](https://docs.omniverse.nvidia.com/composer/latest/index.html "(in Omniverse USD Composer)").

On this page

* [Learning Objectives](#learning-objectives)
* [Saving Options](#saving-options)
* [Loading Options](#loading-options)
  + [Set the Stage for a Reference](#set-the-stage-for-a-reference)
* [Summary](#summary)
  + [Further Readings](#further-readings)