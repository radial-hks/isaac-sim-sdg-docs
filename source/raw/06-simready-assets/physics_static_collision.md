---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/physics/physics_static_collision.html
title: "Static Collision"
section: "物理"
module: "06-simready-assets"
checksum: "9efd03117732503b"
fetched: "2026-06-21T11:55:35"
---

* [Physics](index.html)
* Physics Static Collision Extension

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Physics Static Collision Extension

The [Physics Static Collision Extension](#isaac-static-collision-utils) Extension is used to visualize collision meshes. Use this Utility extension to add static collision APIs to an entire [Stage](../reference_material/reference_glossary.html#isaac-sim-glossary-stage). The extension can also be used to remove all physics related APIs for testing purposes.

This extension is enabled by default. If it is ever disabled, it can be re-enabled from the [Extension Manager](https://docs.omniverse.nvidia.com/extensions/latest/ext_core/ext_extension-manager.html "(in Omniverse Extensions)") by searching for `isaacsim.utils.physics`.

To access this Extension, go to the top menu bar and click **Tools** > **Physics API Editor**.

Note

Dynamic objects are currently not supported.

## User Interface

The User Interface provides options to add or clear static collision on selected static objects.

### Configuration Options

* **Apply to children**: Recursively create collision on all selected children; otherwise, create collision for just the selected object.
* **Visible only**: Ensure the prim is visible before creating collision. (Ignores hidden prims)
* **Collision Type**: Type of collision approximation to use
* **Apply Static**: Applies collision to the current selection.
* **Remove Collision API**: Clears the collision from the current selection.
* **Remove All Physics APIs**: Remove all Physics-related APIs (including collision) from the current selection.

### Enable Visualization

To visualize collision in any viewport:

1. **Select**: the  eye icon.
2. **Select**: Show by type.
3. **Select**: Physics Mesh.
4. **Check**: All.

Note

Enable visualization **after** collision APIs have been applied or removed. Otherwise there will be a loss in performance while the extension traverses the desired subtree.

On this page

* [User Interface](#user-interface)
  + [Configuration Options](#configuration-options)
  + [Enable Visualization](#enable-visualization)