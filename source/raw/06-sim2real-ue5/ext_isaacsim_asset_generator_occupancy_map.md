---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/digital_twin/ext_isaacsim_asset_generator_occupancy_map.html
title: "Occupancy Map Generator"
section: "数字孪生"
module: "06-sim2real-ue5"
checksum: "958eb623d9b331ff"
fetched: "2026-06-21T12:48:19"
---

* [Digital Twin](index.html)
* Mapping

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Mapping

NVIDIA Isaac Sim mapping extension supports 2D occupancy map generation for a specified height.

## Occupancy Map Generator

The [Mapping](#ext-isaacsim-asset-generator-occupancy-map) Extension is used to generate a binary map of whether or not an area in the scene is occupied at a given height. It uses physics collision geometry in the [Stage](../reference_material/reference_glossary.html#isaac-sim-glossary-stage) to determine if a location is occupied or not.

This extension is enabled by default. If it is ever disabled, it can be re-enabled from the [Extension Manager](https://docs.omniverse.nvidia.com/extensions/latest/ext_core/ext_extension-manager.html "(in Omniverse Extensions)") by searching for `isaacsim.asset.gen.omap`.

To access this Extension, go to the top menu bar and click **Tools** > **Robotics** >> **Occupancy Map**.

### Conventions

* All geometry must have Collisions Enabled to be detected by the Occupancy Map Generator. Otherwise the geometry will not appear in the final map.
* The Start location of the map cannot be occupied.

Note

If mapping does not work correctly make sure the start location is not occupied. You can view the physics geometry by clicking the Show/Hide (eye icon) in the viewport window and selecting **Show By Type** > **Physics Mesh** > **All**.

### API Documentation

See the [API Documentation](../py/source/extensions/isaacsim.asset.gen.omap/docs/index.html) for usage information.

### User Interface

The user interface is composed of two parts, the configuration window (named *Occupancy Map*) and the *Occupancy Map Visualization* window.

#### Occupancy Map window

* **Origin**: An open location inside of the area you wish to map.
* **Lower/Upper Bound**: Areas outside of these bounds will not be mapped. These are maximal bounds, the mapped area may be smaller than these limits.
* **Positioning**:

  > + **CENTER TO SELECTION**: The origin will be moved to the center of a selected prim or prims.
  > + **BOUND SELECTION**: The bounds will updated to incorporate the selected prim or prims.

* **Cell Size**: The number of meters each pixel in the final image represents.
* **Occupancy Map**:

  > + **CALCULATE**: Compute the occupancy map.
  > + **VISUALIZE IMAGE**: Open a new window to preview and save the resulting map as an image.
* **Use PhysX Collision Geometry**: When set to True (default), the current collision approximations are used by the PhysX based Lidar to generate the occupancy map. If set to False, the collision approximations are temporarily removed and the RTX Lidar uses the original triangle meshes to generate the occupancy map.

**Example:**

The following steps show how to create and visualize an occupancy map of a certain scene:

> 1. Create a new Cone shape (**Create > Shape > Cone** menu) and add the physics Collision property to it (right click and **Add > Physics > Collider Preset**, or in the *Property* panel).
> 2. Translate the shape 0.3 meters in the X-axis and orient it 90Âº in the X-axis Euler angles by modifying its *Transform* in the *Property* panel.
> 3. Click on the **Tools > Robotics > Occupancy Map** menu to open the *Occupancy Map* window docked to the *Property* panel.
> 4. Set the Occupancy Mapâs Origin Z-axis value to 0.1 meters to map the area at that height
> 5. Click on **CALCULATE** followed by **VISUALIZE IMAGE**. The *Occupancy Map Visualization* window will appear as shown in the image in the next subsection.
> 6. Finally, click **Save Image** to save the map to an easily accessible location. You will need it for later steps in this guide!

#### Occupancy Map Visualization window

* **Occupied Color**: The color chosen to represent space that is âoccupiedâ.
* **Freespace Color**: The color chosen to represent space that is âfreeâ.
* **Unknown Color**: The color chosen to represent space that is interstitial or âunknownâ.
* **Rotate Image**: Rotates the coordinates of the image space. A rotation of \(\text{180}^{\circ}\) will result in a Heightmap orientation that matches that of the original source stage of the occupancy map.
* **Coordinate Type**: Determines the format of the output in the information window. Stage Space coordinates reports values in the space of the stage, while the âROS Occupancy Map Parameters Fileâ returns the needed parameters for the ROS Occupancy Map.
* **Filename**: Base name used when saving the PNG image or YAML file, and written into the YAML `image` field. Defaults to the stage name.
* **RE-GENERATE IMAGE**: This will regenerate the image and information window if you changed the stage.
* **Save Image**: Opens a file dialog pre-filled with the Filename to save the occupancy map as a `.png` file.
* **Save YAML**: Opens a file dialog pre-filled with the Filename to save the ROS occupancy map parameters as a `.yaml` file.

## Heightmap Importer

### Heightmap Importer

The Heightmap Importer Extension converts a 2D occupancy map into a 3D heightmap terrain.
In this extension black pixels in the occupancy map are considered occupied and white pixels are considered free space.
The generated 3D terrain automatically has a collision mesh applied for all the occupied pixels.

To access this Extension, go to the top menu bar and click **Tools** > **Robotics** > **Heightmap Importer**.

* **Cell Size**: Real-world units represented by a single pixel in the 2D occupancy image. The default unit in Isaac Sim is in meters.
* **Load** : Load the desired occupancy image.
* **Generate**: Button to generate the 3D heightmap terrain.

### Heightmap Usage Example

To run the Example:

1. Save the following image to disk:

2. Go to the top menu bar and click **Tools** > **Robotics** > **Heightmap Importer**.
3. Press the **Load Image** button and open the saved image. A window titled **Visualization** will appear.
4. Press the **Generate Heightmap** button to create geometry corresponding to the input occupancy map in the [Stage](../reference_material/reference_glossary.html#isaac-sim-glossary-stage).

On this page

* [Occupancy Map Generator](#occupancy-map-generator)
  + [Conventions](#conventions)
  + [API Documentation](#api-documentation)
  + [User Interface](#user-interface)
    - [Occupancy Map window](#occupancy-map-window)
    - [Occupancy Map Visualization window](#occupancy-map-visualization-window)
* [Heightmap Importer](#heightmap-importer)
  + [Heightmap Importer](#ext-omni-isaac-heightmap-tool)
  + [Heightmap Usage Example](#heightmap-usage-example)