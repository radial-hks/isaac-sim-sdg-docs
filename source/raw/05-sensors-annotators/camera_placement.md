---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/action_and_event_data_generation/ext_sensors_rtx_placement/camera_placement.html
title: "Camera Placement"
section: "传感器配置"
module: "05-sensors-annotators"
checksum: "37320e8aea4171b1"
fetched: "2026-06-21T13:40:27"
---

* [Synthetic Data Generation](../../synthetic_data_generation/index.html)
* [Action and Event Data Generation](../index.html)
* [RTX Sensors Placement and Calibration](../tutorial_sensors_rtx_placement.html)
* Camera Placement

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Camera Placement

The Camera Placement Tool (`isaacsim.sensors.rtx.placement` extension) automatically optimizes camera placement in a stage according to user customized requirements.

## Enable the Extension

Follow the [Omniverse Extension Manager guide](https://docs.omniverse.nvidia.com/extensions/latest/ext_core/ext_extension-manager.html) to enable the `isaacsim.sensors.rtx.placement` extension.

## Open the Camera Placement Tool Panel

The Camera Placement Tool is accessible by **Tools > Sensors > Camera Placement**.

### Input Fields

**Camera Placement Output Path**:
The folder path where the generated camera placement data will be saved.
The file `camera_info_payload.json` will be output to this folder, containing information about all cameras relevant to the current camera placement task.

**Cached data would include**:

> * Camera Path
> * Camera Position
> * Focus Point Position
>
> * Example
>   :   + Output: in `camera_info_payload.json`
>         :   ```python
>             {
>                 "X_Positive": [
>                     {
>                     "camera_path": "/World/Cameras/Camera",
>                     "camera_position": [
>                         -25.48988914489746,
>                         -14.219901084899902,
>                         3.319734811782837
>                     ],
>                     "focus_point": [
>                         -20.801025390625,
>                         -18.900035858154297,
>                         0.5
>                     ]
>                     }
>                 ]
>             }
>             ```

**Total Camera Number**:
The total number of cameras to be placed in the scene.

**Camera Range Parameters**:

> * **Camera Height Range**:
>   :   + Define the allowable height range for camera placement above the ground.
> * **Camera Distance Range**:
>   :   + Set the distance range within which a camera can be placed from any point P on the stage.
>       + Ensures:
>         :   - For any point P, there exists a camera C such that the distance between C and P is within this range.
> * **Camera Look Down Angle Range**:
>   :   + Define the downward tilt angle range for the cameras.
>
>         > - Zero degrees means the camera is parallel to the ground (horizontal view).
>         > - 90 degrees means the camera is pointing straight down (top-down view, perpendicular to the ground).

**Stage Processing Parameters**:

> * **Patch Size**:
>   :   The stage is divided into patches of this size for estimating coverage.
>
>       > + The smaller size means more detailed stage analysis when calculate camera coverage.
>       > + On the other hand, It also means more computation time.
> * **Ground Height**:
>   :   Height of the ground surface in the stage.
> * **Stage Scope**:
>   :   Defines the spatial boundaries of the stage for camera placement when navmesh is unavailable.
>
>       > + **X Scope**: Minimum and maximum X-axis boundaries.
>       > + **Y Scope**: Minimum and maximum Y-axis boundaries.
>
>       Warning
>
>       This parameter is not recommended for normal use. Only use it in edge cases when a valid navmesh cannot be built for the stage.

**Other Tuning Parameters**:

> * **Random Seed**:
>   :   Controls the random seed for the camera placement process. For a given random seed, the camera placement result will be deterministic.
> * **Border Checking Index**:
>   :   Controls how close cameras can be placed to the boundary of the stage.
>       Prevents invalid placements that can result from proximity to obstacles or being outside the stage bounds.
> * **Camera On Navmesh**:
>   :   Whether cameras must be placed only on the navigation mesh.
> * **Minimum Coverage Increase**:
>   :   The minimum additional patch a camera must cover for it to be considered valid.
>       If the new camera increases coverage less than this value, placement will stop.
> * **Limit FOV by Distance**:
>   :   Determines whether the camera’s field of view should be restricted based on its **Camera Distance Range**.
>       - If enabled, the estimated camera coverage will be further limited according to the distance between each visible area and the target camera.
> * **Coverage Density**:
>   :   Specifies how many cameras must cover each patch at a minimum.
> * **Target Coverage Ratio**:
>   :   The desired overall ratio of the stage that must be covered by cameras **according to the requirements**.
>       Placement stops if this target is not met.

#### Buttons and Functions

* **Place Cameras**:
  :   Begin the automated camera placement process using the parameters defined above.

      Note

      + After clicking the **Place Cameras** button, the process can take some time to complete. The duration depends on the number of cameras to be placed and the complexity of the stage.
      + At the end of the placement the number of the camera number of the camera in each direction would summarized and output in the console as a carb warning message.
* **Show Selected Camera Coverage**:
  :   Visualize the coverage area of the currently selected camera.

      Note

      + The **Show Selected Camera Coverage** button displays the coverage areas of all *selected* cameras.
      + Points with different levels of coverage will be shown in distinct colors.

        > - If the required **Coverage Density** is set to `N`, then `N` distinct colors will be used to represent coverage levels.
      + Example:

        > - [Camera Coverage Visualization Example](#camera-coverage-visualization-example)

* **Show all Camera Coverage**:
  :   Visualize the coverage area of all cameras in the scene, regardless of selection status.

      Note

      + This button displays the combined coverage areas of all generated cameras.
      + Use this to quickly verify overall scene coverage without manually selecting individual cameras.
      + Points with different levels of coverage will be shown in distinct colors based on the **Coverage Density** setting.
* **Hide Coverage**:
  :   Hide the camera coverage visualization from the stage view.

## Camera Placement Tool Tutorial

To use the **Camera Placement Tool**. Ensure the scene has valid navmesh baked before proceeding. The tutorial uses the [Isaac Sim Full Warehouse](../../assets/usd_assets_environments.html#isaac-assets-environments-warehouse) for demonstration.

Note

* Stage unit must be in meters.
* A valid [NavMesh](https://docs.omniverse.nvidia.com/extensions/latest/ext_navigation-mesh.html "(in Omniverse Extensions)") is required.
* Z axis is up.

### Enable the Extension

1. [Enable the isaacsim.sensors.rtx.placement extension](#enabling-camera-placement-extension).
2. [Open the camera placement tool panel](#activate-camera-placement-tool-panel).

### Open the Target Stage

Open the [Isaac Sim Full Warehouse](../../assets/usd_assets_environments.html#isaac-assets-environments-warehouse)

> Note
>
> * Verify that the navmesh is baked successfully
> * Access **Window > Navigation > Navmesh** and click on **Bake** button if you need to rebake the navmesh.
>
>   > + Before proceeding, ensure that the `omni.anim.navigation.bundle extension` is enabled according to [instruction](https://docs.omniverse.nvidia.com/extensions/latest/ext_navigation-mesh/installation.html "(in Omniverse Extensions)").

### Configure Camera Placement

In the **Camera Placement** section of the UI:

1. Set the **Camera Placement Output Path**, by entering your cache folder path.
2. Set the **Total Camera Number**. Use -1 to auto-compute the minimum number of cameras needed.

### (Optional) Adjust Camera Range

If needed, configure the **Camera Range Parameters** such as height, look-down angles, and target distance.
Refer to the [Camera Range Input Fields](#camera-range-parameters) for more details. This example uses the default values.

### (Optional) Adjust Stage Processing

**Stage Processing Parameters** allows you to configure the camera placement method according to the stage’s size, height, and complexity.
Tune **Stage Processing Parameters** to set patch size or ground height, if applicable.
Refer to the [Stage Processing Parameters Field](#stage-processing-parameters) for more details. This example uses the default values.

### Fine-tune Placement

Multiple configurable parameters have been added to help user check and refine the camera placement logic.

In this case, modify these two parameters:

> * Set **Coverage Density** to `2`, which means for each patch in the stage, you need two cameras to cover it.
> * Set **Target Coverage Ratio** to `0.99`, which means 99 percent of the patch needs to be covered according to the set requirements.
>
> * In this example, use the default values for other parameters.
> * You are free to modify more **Other Tuning Parameters** to adjust placement logic if finer control is needed.
> * Refer to the [Fine Tuning Parameters Field](#fine-tuning-processing-parameters) for more details.

### Run Camera Placement

Click the **Place Cameras** button to begin automatic placement. Wait for the process to complete.

> * The process can take some time to complete. The duration depends on the number of cameras to be placed and the complexity of the stage.

### Check Coverage

1. Get a top view of the stage to make the camera coverage visualization more clear.

   > * [Create Top View Camera With Camera Calibration Panel](camera_calibration.html#create-top-view-camera-with-section-tool).
   > * Switch you view port camera to the created top view camera.
   > * Visualize Navmesh by clicking on **Visibility Menu (eye icon on viewport) > Show By Type > Navmesh**.
2. In the **Camera Placement Tool** panel, click **Show all Camera Coverage** to visualize the coverage of all generated cameras.

   > * [How Camera Coverage Visualization Works](#show-all-camera-coverage)

> * In this example, points covered once are shown in red, while points covered twice are shown in green.
>
>   > + From the visualization result, most points are covered as our expectation.

### Hide Coverage

Click the **Hide Coverage** button to remove the coverage overlay.

### (Optional)Save Your Work

**Save** or **Save as** the updated USD file to preserve camera placements for further SDG workflows.

On this page

* [Enable the Extension](#enable-the-extension)
* [Open the Camera Placement Tool Panel](#open-the-camera-placement-tool-panel)
  + [Input Fields](#input-fields)
    - [Buttons and Functions](#buttons-and-functions)
* [Camera Placement Tool Tutorial](#camera-placement-tool-tutorial)
  + [Enable the Extension](#id1)
  + [Open the Target Stage](#open-the-target-stage)
  + [Configure Camera Placement](#configure-camera-placement)
  + [(Optional) Adjust Camera Range](#optional-adjust-camera-range)
  + [(Optional) Adjust Stage Processing](#optional-adjust-stage-processing)
  + [Fine-tune Placement](#fine-tune-placement)
  + [Run Camera Placement](#run-camera-placement)
  + [Check Coverage](#check-coverage)
  + [Hide Coverage](#hide-coverage)
  + [(Optional)Save Your Work](#optional-save-your-work)