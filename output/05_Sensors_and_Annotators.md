# Sensors and Annotators

> 相机/传感器配置 + RTX 标注器 + Writer 输出格式
> Isaac Sim 版本: 6.0
> 最后组装: 2026-06-21 11:55 UTC
> 来源页数: 9

---

## 来源链接

- [RTX Camera](https://docs.isaacsim.omniverse.nvidia.com/latest/sensors/isaacsim_sensors_camera.html)
- [Camera Depth](https://docs.isaacsim.omniverse.nvidia.com/latest/sensors/isaacsim_sensors_camera_depth.html)
- [RTX Annotators](https://docs.isaacsim.omniverse.nvidia.com/latest/sensors/isaacsim_sensors_rtx_annotators.html)
- [Multitick Rendering](https://docs.isaacsim.omniverse.nvidia.com/latest/sensors/isaacsim_sensors_multitick_rendering.html)
- [Camera Calibration](https://docs.isaacsim.omniverse.nvidia.com/latest/action_and_event_data_generation/ext_sensors_rtx_placement/camera_calibration.html)
- [Camera Placement](https://docs.isaacsim.omniverse.nvidia.com/latest/action_and_event_data_generation/ext_sensors_rtx_placement/camera_placement.html)
- [Sensors RTX Placement Tutorial](https://docs.isaacsim.omniverse.nvidia.com/latest/action_and_event_data_generation/tutorial_sensors_rtx_placement.html)
- [Menu Replicator (GUI)](https://docs.isaacsim.omniverse.nvidia.com/latest/gui/menu_replicator.html)
- [Sensors Index](https://docs.isaacsim.omniverse.nvidia.com/latest/sensors/index.html)

---


## 相机

### RTX Camera

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/sensors/isaacsim_sensors_camera.html

* [Sensors](index.html)
* Camera Sensors

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Camera Sensors

Cameras are modeled using the Camera USD prim type. Camera data is acquired from camera prims using render products, which can be created by multiple different extensions in Omniverse,
including the [omni.replicator](https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator.html "(in Omniverse Extensions)") extension.

Note

Isaac Sim camera functionality is based on [Omniverse cameras](https://docs.omniverse.nvidia.com/materials-and-rendering/latest/cameras.html).

Deprecated since version 6.0: The `isaacsim.sensors.camera` extension is deprecated. Use `isaacsim.sensors.experimental.rtx` instead.
The new extension provides `RtxCamera`, `CameraSensor`, `TiledCameraSensor`,
`SingleViewDepthCameraSensor`, and `StructuredLightCamera` with a uniform authoring/runtime
split. See [Camera Sensors](../migration_guides/isaac_sim_6_0/sensors_camera_to_experimental_rtx.html#isaacsim-sensors-camera-migration).

## Overview

Isaac Sim cameras are USD `Camera` prims rendered by the RTX renderer. The
`isaacsim.sensors.experimental.rtx` extension wraps these prims with two paired classes:

* **Authoring** â `RtxCamera` creates or wraps a USD `Camera` prim, applies the
  `OmniSensorAPI` schema, and exposes the optical parameters (focal length, aperture,
  clipping range) through its `.camera` property.
* **Runtime** â `CameraSensor` wraps an `RtxCamera` object, creates a Replicator render
  product at a specified resolution, attaches annotators (`rgb`, `distance_to_camera`,
  `semantic_segmentation`, etc.), and provides `get_data()` for retrieving rendered frames
  as numpy/warp arrays.

Two specialized camera variants extend this base â `SingleViewDepthCameraSensor` for
stereoscopic depth simulation and `StructuredLightCamera` for projected-pattern depth
recovery. See [Specialized Camera Types](#isaacsim-sensors-camera-specialized-types) below.

## How to Create a Camera

Isaac Sim supports creating camera prims through the GUI **Create** menu or
programmatically via the `RtxCamera` class.

### Create from the Create Menu

1. Create a cube by selecting **Create > Shape > Cube** and change its location and scale through the property panel as indicated in the screenshot below.
2. Create a camera prim by selecting **Create > Camera** and then select it from the stage window to view its field of view as indicated below.
3. To render the frames from the camera, switch the default viewport (which is a render product itself) to the camera prim that you just created.
   Select the video icon at the top of the viewport window and then select the camera prim you just created under the `Cameras` menu.

### Create with the `RtxCamera` Class

The `RtxCamera` authoring class creates (or wraps) a `Camera` prim with the `OmniSensorAPI` schema applied,
sets transforms via plural-array constructor parameters (`positions`, `translations`, `orientations`, `scales`),
and exposes optical parameters through its `.camera` property. The standalone example
`standalone_examples/api/isaacsim.sensors.experimental.rtx/create_camera_basic.py` demonstrates
the full create-and-read workflow:

```python
./python.sh standalone_examples/api/isaacsim.sensors.experimental.rtx/create_camera_basic.py
```

The example loads a warehouse environment, creates an `RtxCamera` at `/World/camera`, attaches
`rgb` and `distance_to_image_plane` annotators via `CameraSensor`, and saves a rendered
RGB frame to disk every 100 ticks under
`_example_output_isaacsim.sensors.experimental.rtx/create_camera_basic/`. The frame at tick 100
looks like:

RGB frame saved by `create_camera_basic.py` (tick 100, 480x640).

### Tick Rate

The `tick_rate` parameter (Hz) on `RtxCamera` controls how frequently the camera renders. A value
of `0` (the default) enables autotrigger mode, where the camera renders every simulation frame.
Setting a nonzero value causes the camera to render at the specified frequency independently of the
simulation step rate. This maps to the `omni:sensor:tickRate` prim attribute and requires the
`OmniSensorAPI` schema to be applied to the Camera prim â `RtxCamera` does this automatically.

```python
from isaacsim.sensors.experimental.rtx import RtxCamera

# Render the Camera at 30 Hz independently of the simulation frame rate.
camera = RtxCamera(path="/World/Camera", tick_rate=30.0)
```

`tick_rate` is the recommended replacement for the deprecated `frameSkipCount` input on
`ROS2 Camera Helper`, `ROS2 Camera Info Helper`, and `UCX Camera Helper` nodes. See
[Multi-Tick Rendering](isaacsim_sensors_multitick_rendering.html#isaac-sim-sensors-multitick-rendering) for the full migration guide and the list of
related known issues.

## How to Collect Data from a Camera

The recommended method for collecting data from a camera is to use the `CameraSensor` runtime class,
which wraps an `RtxCamera` authoring object and manages Replicator annotators on its render product.
For batched multi-camera workflows, use `TiledCameraSensor`. For stereoscopic depth simulation, use
`SingleViewDepthCameraSensor` (see
[Specialized Camera Types](#isaacsim-sensors-camera-specialized-types) for the full sub-page).

### Annotators

`CameraSensor` accepts a list of annotator names (`rgb`, `distance_to_camera`,
`distance_to_image_plane`, `semantic_segmentation`, `motion_vectors`, etc.) at construction
time and exposes the latest data through `get_data("annotator-name")`, which returns a
`(warp.array, info_dict)` tuple. Run the basic example to see `rgb` and
`distance_to_image_plane` collection end-to-end:

```python
./python.sh standalone_examples/api/isaacsim.sensors.experimental.rtx/create_camera_basic.py
```

To select between CPU- and CUDA-resident annotator buffers, see the standalone example
`standalone_examples/api/isaacsim.sensors.experimental.rtx/camera_annotator_devices.py`.

### Tiled / Batched Cameras

`TiledCameraSensor` packs many cameras into a single tiled render product, which is significantly
more efficient than one render product per camera for reinforcement-learning and multi-environment
workflows. Pass an explicit list of camera prim paths (or an `isaacsim.core.experimental.objects.Camera`
instance) plus a per-tile `resolution`:

```python
./python.sh standalone_examples/api/isaacsim.sensors.experimental.rtx/camera_tiled.py
```

### Single-View Depth Cameras

`SingleViewDepthCameraSensor` extends `CameraSensor` with stereoscopic-depth simulation
post-processing (disparity, baseline, noise, outlier removal). See the
[Single-View Post-Processing Pipeline](isaacsim_sensors_camera_depth.html#isaacsim-sensors-camera-depth-stereoscopic-pipeline) sub-page for the full pipeline
description. End-to-end example:

```python
./python.sh standalone_examples/api/isaacsim.sensors.experimental.rtx/camera_stereoscopic_depth.py
```

## Specialized Camera Types

Two specialized camera sensors build on `RtxCamera` and `CameraSensor` for depth and structured-light workflows:

* [Depth Sensors](isaacsim_sensors_camera_depth.html)
* [Structured Light Cameras](isaacsim_sensors_camera_structured_light.html)

## Advanced Topics

### Calibration and Camera Lens Distortion Models

Omniverse cameras support a variety of lens distortion models, described [here](https://docs.omniverse.nvidia.com/materials-and-rendering/latest/cameras.html#omniverse-cameras).
The `RtxCamera` class from `isaacsim.sensors.experimental.rtx` supports applying lens distortion schemas (e.g. `OmniLensDistortionOpenCvFisheyeAPI`, `OmniLensDistortionOpenCvPinholeAPI`) via the `schemas` parameter and setting distortion coefficients via the `attributes` parameter.

Calibration toolkits like OpenCV normally provide the calibration parameters as an intrinsic matrix and distortion coefficients. Omniverse includes native renderer support for the OpenCV pinhole and
OpenCV fisheye lens distortion models. Isaac Sim provides two standalone examples demonstrating the use of `RtxCamera` with OpenCV lens distortion models,
located at `standalone_examples/api/isaacsim.sensors.experimental.rtx/camera_opencv_pinhole.py` and `standalone_examples/api/isaacsim.sensors.experimental.rtx/camera_opencv_fisheye.py`.

Note

* Previously, the `Camera` class included APIs to approximate OpenCV pinhole and fisheye models distortion parameters by setting coefficients for the `fisheyePolynomial` distortion model. Now that OpenCV lens distortion models are natively supported, those APIs have been deprecated.
* [Omniverse RTX Camera Projection Attributes](https://docs.omniverse.nvidia.com/materials-and-rendering/latest/cameras.html#rtx-camera-projection-attributes-deprecated) have been deprecated as of Isaac Sim 5.0, in favor of the `OmniLensDistortion` [schemata](https://docs.omniverse.nvidia.com/materials-and-rendering/latest/cameras.html#omnilensdistortion-schemata). The deprecated attributes are still visible in the UI in the `Fisheye Lens` panel when selecting a Camera prim, but will be ignored if you have set an `OmniLensDistortion` schema instead. Follow the instructions in [âHow To Add Schemata to Camerasâ](https://docs.omniverse.nvidia.com/materials-and-rendering/latest/cameras.html#omnilensdistortion-schemata) to see how to update Camera prim attributes for the new schemata in the UI.

Warning

In Isaac Sim 6.0, enabling arbitrary distortion models using a generalized projection model by
applying the `OmniLensDistortionLutAPI` schema to Camera prims does not correctly function, and if set,
the renderer will fallback to the default pinhole model. Instead, use the deprecated Omniverse RTX Camera
Projection Attributes referenced above to specify an arbitrary distortion model. This will be fixed in a future release.

#### OpenCV Fisheye

Run the standalone example to create an `RtxCamera` with the `OmniLensDistortionOpenCvFisheyeAPI` schema applied:

```python
./python.sh standalone_examples/api/isaacsim.sensors.experimental.rtx/camera_opencv_fisheye.py
```

After running the example and setting the viewport to the newly-created camera, validate that you see an image like the one below.

#### OpenCV Pinhole

Run the standalone example to create an `RtxCamera` with the `OmniLensDistortionOpenCvPinholeAPI` schema applied:

```python
./python.sh standalone_examples/api/isaacsim.sensors.experimental.rtx/camera_opencv_pinhole.py
```

After running the example and setting the viewport to the newly-created camera, you should see an image like the one below.

#### Extrinsic Calibration

Extrinsic calibration parameters are normally provided by the calibration toolkits in a form of a transformation matrix. The convention between the axis and rotation order is important and it varies between the toolkits.

To set the extrinsic parameters for the individual camera sensor, use the following example to convert the transformation matrix from the calibration toolkit to the Isaac Sim units:

```python
# Pseudocode -- adapt axis remapping and quaternion reordering to your calibration toolkit.
import numpy as np
from isaacsim.sensors.experimental.rtx import RtxCamera

dX, dY, dZ = _, _, _  # Extrinsics translation vector from the calibration toolkit
rW, rX, rY, rZ = _, _, _, _  # Note the order of the rotation parameters, it depends on the toolkit

RtxCamera(
    "/rig/camera_color",
    positions=np.array([-dZ, dX, dY]),  # Translation in the local frame of the prim
    orientations=np.array([rW, -rZ, rX, rY]),  # Quaternion orientation (wxyz) in the world/local frame
    # (depends if translations or positions is specified)
)
```

As an alternative, the camera sensor can be attached to a prim. In that case, the camera sensor will inherit the position and orientation from the prim.

```python
from isaacsim.sensors.experimental.rtx import RtxCamera

# Create a camera prim with the OmniSensorAPI schema
cam = RtxCamera(
    "/World/camera",
    # translations = ...
    # orientations = ...
)
```

### Exposing the ISP Camera Pipeline

The `omni.sensors.nv.camera` extension [simulates the camera sensor and Image Signal Processor (ISP) pipeline](https://docs.omniverse.nvidia.com/materials-and-rendering/latest/cameras.html#omni-sensors-nv-camera-extension).
Isaac Sim includes a standalone example that configures the ISP pipeline via the `OmniSensorGenericCameraCoreAPI` USD schema and saves the introspection output from every pipeline stage as viewable images.
You can use these outputs to test your own ISP against images rendered in RTX, or compare them with the Omniverse-simulated ISP output.

Refer to the [extension documentation](https://docs.omniverse.nvidia.com/materials-and-rendering/latest/cameras.html#omni-sensors-nv-camera-extension) for details on individual pipeline stages and schema attributes.

Note

The sample ISP program bundled with `omni.sensors.nv.camera` is only available on Linux x86\_64.
Running the example on any other platform will print an informative message and exit early.
If you have your own ISP program for a different platform, update the `_isp_program_path`
variable in the script to point to it, and comment-out the platform check.

Run the example:

```python
./python.sh standalone_examples/api/isaacsim.sensors.experimental.rtx/camera_isp_pipeline.py
```

The example renders 20 frames and saves output from each ISP stage to the `camera_isp_pipeline_outputs` directory.
The pipeline stages, in order, are described below.

**HDR texture read** â the raw HDR radiance buffer read from the renderer before any sensor processing.

**Color correction** â applies black-level subtraction, white-balance gains, a 3x3 color-correction matrix, and sensor-response scaling.

**CFA encoding** â encodes the RGB image into a single-channel Bayer mosaic using the configured Color Filter Array pattern (GRBG in this example).

**Noise simulation** â adds Gaussian and shot noise to the Bayer image to approximate real sensor behavior.

**Companding** â applies a piecewise-linear tone curve that compresses the high-dynamic-range Bayer data into a lower bit depth.

**ISP output** â the fully processed image after the on-chip ISP program runs (demosaic, denoise, tone-map, and color grading).

**YUV conversion** â the final ISP output converted from RGB to YUV color space.

### Camera Sensor Rigs

The camera sensor rig is a collection of camera sensors that are attached to a single prim. It can be assembled from the individual sensors, that are either created manually or derived from the calibration parameters.

This will be a short discussion on how we created a digital twin of the RealSenseâ¢ Depth Camera D455. The USD for the camera can be found in the content folder as: `/Isaac/Sensors/RealSense/D455/rsd455.usd`.

There are three visual sensors, and one IMU sensor on the RealSense. Their placement relative to the camera origin was taken from the layout diagram in
the [TechSpec document](https://www.intelrealsense.com/wp-content/uploads/2023/07/Intel-RealSense-D400-Series-Datasheet-July-2023.pdf) from [Intelâs web site](https://www.intelrealsense.com/depth-camera-d455/).

Most camera parameters were also found in the TechSpec, for example, the USD parameter `fStop` is the denominator of the F Number from the TechSpec; the `focalLength` is the Focal Length, and the `ftheatMaxFov`
is the Diagonal Field of View. However, some parameters, like the `focusDistance` were estimated by comparing real output and informed guesses.

The `horizontalAperture` and `verticalAperture` in that example are derived from the technical specification. From the TechSpec, the left, right, and color sensors are listed as a OmniVision Technologies OV9782, and
the [Tech Spec](https://www.ovt.com/products/ov09782-ga4a/) for that sensor lists the image area as 3896 x 2453 Âµm. We used that as the aperture sizes.

The resolution for the depth and color cameras are 1280 x 800, but itâs up to you to attach a render product of that size to the outputs.

The `Pseudo Depth` camera is a stand in for the depth image created by the cameraâs firmware. We donât attempt to copy the algorithms that create the image from stereo, but the `Camera_Pseudo_Depth` component
is a convenience camera that can return the scene depth as seen from that camera position between the left and right stereo cameras. It would be more accurate to create a depth image from stereo, and if
the same algorithm that is used in the RealSense was used then the same results (including artifacts) would be produced.

### Camera Inspector Extension

The Camera Inspector Extension allows you to:

* Create multiple viewports for each camera
* Check camera coverage
* Get and set camera poses in the desired frames

#### Launching Extension

To open the Camera Inspector extension:

1. Go to the Menu Bar.
2. Select **Tools > Sensors > Camera Inspector**.
3. After launching the extension, verify that you can see your camera in the dropdown.
4. When adding a new camera, you must click the Refresh button to ensure that the extension finds this new camera.
5. Select the camera you want to inspect.

#### Camera State Textbox

The **Camera State** textbox near the top of the extension provides a convenient way to copy the position and orientation of your camera directly into code.
Click the copy icon on the right of the textbox to copy to your clipboard.

#### Creating a Viewport

With the camera selected, you can create a new viewport for your camera.

1. Click on the **Create Viewport** button to the right of the camera dropdown menu.

   > By default, this creates a new viewport and assigns the current selected Camera to it.
2. Assign different cameras to different viewports using the two dropdown menus and buttons in the extension:
3. After launching your viewport, you can change the resolution using the menu in the top left and going to **Viewport**.

   > Note
   >
   > When changing the resolution, Omniverse Kit only supports square pixels. This means that the resolution aspect ratio must be the same as the aperture ratio.

## Standalone Examples

For end-to-end examples of creating and collecting data from camera sensors, refer to the following.

**Basic Creation and Visualization**

```python
# Basic camera creation with rgb + distance_to_image_plane annotators in a warehouse scene
./python.sh standalone_examples/api/isaacsim.sensors.experimental.rtx/create_camera_basic.py
```

**Specialized Cameras**

```python
# Single-view stereoscopic depth sensor
./python.sh standalone_examples/api/isaacsim.sensors.experimental.rtx/create_camera_depth_sensor.py
./python.sh standalone_examples/api/isaacsim.sensors.experimental.rtx/camera_stereoscopic_depth.py

# Structured light camera
./python.sh standalone_examples/api/isaacsim.sensors.experimental.rtx/camera_structured_light.py
```

**Batched / Tiled**

```python
# TiledCameraSensor for multi-camera batched rendering
./python.sh standalone_examples/api/isaacsim.sensors.experimental.rtx/camera_tiled.py
```

**Calibration**

```python
# OpenCV pinhole and fisheye lens distortion models on RtxCamera
./python.sh standalone_examples/api/isaacsim.sensors.experimental.rtx/camera_opencv_pinhole.py
./python.sh standalone_examples/api/isaacsim.sensors.experimental.rtx/camera_opencv_fisheye.py
```

**Annotator Device Selection**

```python
# CPU vs CUDA-resident annotator buffers
./python.sh standalone_examples/api/isaacsim.sensors.experimental.rtx/camera_annotator_devices.py
```

**ISP Pipeline**

```python
# Per-stage ISP pipeline introspection (Linux x86_64 only)
./python.sh standalone_examples/api/isaacsim.sensors.experimental.rtx/camera_isp_pipeline.py
```

**ROS 2 Integration**

```python
# Publish camera frames over ROS 2
./python.sh standalone_examples/api/isaacsim.sensors.experimental.rtx/camera_ros.py
```

On this page

* [Overview](#overview)
* [How to Create a Camera](#how-to-create-a-camera)
  + [Create from the Create Menu](#create-from-the-create-menu)
  + [Create with the `RtxCamera` Class](#create-with-the-rtxcamera-class)
  + [Tick Rate](#tick-rate)
* [How to Collect Data from a Camera](#how-to-collect-data-from-a-camera)
  + [Annotators](#annotators)
  + [Tiled / Batched Cameras](#tiled-batched-cameras)
  + [Single-View Depth Cameras](#single-view-depth-cameras)
* [Specialized Camera Types](#specialized-camera-types)
* [Advanced Topics](#advanced-topics)
  + [Calibration and Camera Lens Distortion Models](#calibration-and-camera-lens-distortion-models)
    - [OpenCV Fisheye](#opencv-fisheye)
    - [OpenCV Pinhole](#opencv-pinhole)
    - [Extrinsic Calibration](#extrinsic-calibration)
  + [Exposing the ISP Camera Pipeline](#exposing-the-isp-camera-pipeline)
  + [Camera Sensor Rigs](#camera-sensor-rigs)
  + [Camera Inspector Extension](#camera-inspector-extension)
    - [Launching Extension](#launching-extension)
    - [Camera State Textbox](#camera-state-textbox)
    - [Creating a Viewport](#creating-a-viewport)
* [Standalone Examples](#standalone-examples)

---

### Camera Depth

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/sensors/isaacsim_sensors_camera_depth.html

* [Sensors](index.html)
* [Camera Sensors](isaacsim_sensors_camera.html)
* Depth Sensors

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Depth Sensors

## Stereoscopic Depth Cameras

### Single-View Post-Processing Pipeline

Isaac Sim models stereoscopic depth cameras using a single camera view through the `isaacsim.sensors.experimental.rtx.SingleViewDepthCameraSensor` class. This class wraps around `isaacsim.sensors.experimental.rtx.RtxCamera`, and
includes APIs for configuring a post-processing pipeline for stereoscopic depth estimation from a single Camera prim. The process by which the renderer models disparity and noise from a single camera view
is described in detail [here](http://omniverse-docs.s3-website-us-east-1.amazonaws.com/omni.sensors.nv.camera/0.21.0-coreapi/camera_extension.html#single-view-depth-camera).

#### Standalone Python

Check out the standalone example located at `standalone_examples/api/isaacsim.sensors.experimental.rtx/camera_stereoscopic_depth.py` for an example of how to use the `SingleViewDepthCameraSensor` class from `isaacsim.sensors.experimental.rtx`
and the [new Annotators provided in Replicator](https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator/annotators_details.html).

When running the standalone example, a basic set of colored shapes in the Black Grid environment are in the viewport, like below:

Now, examine the disparity map generated by the depth sensor as follows:

1. Select the camera render product in the viewport.
2. Click **Render Settings > Post Processing > Depth Sensor** to examine the depth sensor post-processing pipeline settings.
3. Tick the checkbox for **Depth Sensor**.
4. Select **Disparity** from the **RGB Depth Output Mode** dropdown.

The settings will look like the following:

Note

To learn more about these Post Processing settings, visit [Single View Depth Camera documentation](http://omniverse-docs.s3-website-us-east-1.amazonaws.com/omni.sensors.nv.camera/0.21.0-coreapi/camera_extension.html#single-view-depth-camera).

Verify that you see the disparity map in the viewport, like below:

Note

Any settings under **Render Settings > Post Processing > Depth Sensor** will be applied to all render products in the scene (including the viewport). The `isaacsim.sensors.experimental.rtx.SingleViewDepthCameraSensor` class
enables configuration of individual render products as depth sensors.

Close the Isaac Sim UI and rerun the standalone example as follows:

```python
./python.sh standalone_examples/api/isaacsim.sensors.experimental.rtx/camera_stereoscopic_depth.py --test
```

Isaac Sim will now run the standalone example in headless mode and generate the following output from Annotators
attached to the `camera` render product. The first image is output from the `DepthSensorDistance` Annotator (`depth_sensor_distance.png`), and the
second image is output from the `DistanceToImagePlane` Annotator (`distance_to_image_plane.png`).

### Depth Camera Asset Wrapper

Isaac Sim supports several official [Depth Sensors](../assets/usd_assets_camera_depth_sensors.html#isaac-assets-camera-depth-sensors-depth-sensors). These can be loaded as USD references on a stage
using `RtxCamera.create()` from `isaacsim.sensors.experimental.rtx`. When `SingleViewDepthCameraSensor` subsequently wraps the resulting `RtxCamera`,
it automatically detects any `RenderProduct` prims embedded in the asset that have `OmniSensorDepthSensorSingleViewAPI` applied and are linked to the
loaded camera, then copies their depth sensor attributes onto the dynamically created render product. This gives you full control over the post-processing
pipeline for each depth sensor in the asset and allows any number of annotators to be attached through the `SingleViewDepthCameraSensor` API.

Note

Attribute specification for `Camera` prims in the official assets linked above are tentative, and can change in future asset updates or releases.

#### Script Editor

As an example, you can load the Realsense D455 depth camera asset and attach an annotator to the depth sensor by running the
following snippet in the Script Editor:

```python
from isaacsim.sensors.experimental.rtx import RtxCamera, SingleViewDepthCameraSensor
from isaacsim.storage.native import get_assets_root_path

assets_root_path = get_assets_root_path()

# Load the Realsense D455 depth camera asset as a USD reference.
# RtxCamera.create() discovers the Camera prim inside the asset automatically.
cam = RtxCamera.create(
    "/World/D455",
    usd_path=assets_root_path + "/Isaac/Sensors/RealSense/D455/rsd455.usd",
)

# Wrap with SingleViewDepthCameraSensor. Depth sensor attributes (baseline,
# focal length, noise, etc.) are automatically copied from the RenderProduct
# prims already embedded in the asset.
sensor = SingleViewDepthCameraSensor(
    cam,
    resolution=(720, 1280),
    annotators=["depth_sensor_distance"],
)
sensor.set_enabled_post_processing(True)
```

Observe the Stage window indicates the Realsense D455 depth camera asset has been loaded.

Next, observer the Layer window indicates the appropriate `RenderProduct` prim has been created, with a
HydraTexture and `DepthSensorDistance` `RenderVar` attached:

### Building a Depth Sensor Model in Isaac Sim

#### Updating Existing Assets to Use Depth Sensors

Isaac Sim provides a convenient API to build a depth camera USD asset using `RtxCamera` and
`SingleViewDepthCameraSensor.add_template_render_product` from `isaacsim.sensors.experimental.rtx`.
The following example creates an `RtxCamera` prim, embeds a template `RenderProduct` with
`OmniSensorDepthSensorSingleViewAPI` applied, and exports the result as a USD asset:

```python
./python.sh standalone_examples/api/isaacsim.sensors.experimental.rtx/create_camera_depth_sensor.py
```

Running the example will create a new `example_camera_with_depth_sensor.usd` asset under
`_example_output_isaacsim.sensors.experimental.rtx/create_camera_depth_sensor/` in the working directory.

Then, open the new asset in Isaac Sim, and observe the following in the **Stage** window:

Observe the new render product prim has been created and associated to the `Camera` prim, with the custom
value set for the `omni:rtx:post:depthSensor:baselineMM` attribute.

Open a new stage, and run the following snippet in the **Script Editor** to load the exported asset as a
reference using `RtxCamera.create`. `SingleViewDepthCameraSensor` will automatically detect the embedded
template render product and copy its depth sensor attributes onto the dynamically created render product:

```python
import os

from isaacsim.sensors.experimental.rtx import RtxCamera, SingleViewDepthCameraSensor

usd_path = os.path.join(
    os.getcwd(),
    "_example_output_isaacsim.sensors.experimental.rtx",
    "create_camera_depth_sensor",
    "example_camera_with_depth_sensor.usd",
)

cam = RtxCamera.create("/World/depth_sensor", usd_path=usd_path)
sensor = SingleViewDepthCameraSensor(cam, resolution=(720, 1280), annotators=["depth_sensor_distance"])
sensor.set_enabled_post_processing(True)
```

Observe in the Layer window the new render product is appropriately created and named `camera_sensor_[random number]`,
with the custom value set for the `omni:rtx:post:depthSensor:baselineMM` attribute.

#### Creating a New Depth Sensor Asset

As noted earlier, the [Single-View Post-Processing Pipeline](#isaacsim-sensors-camera-depth-stereoscopic-pipeline) is intended to model stereoscopic depth cameras specifically, not (eg.) time-of-flight
sensors or structured light sensors. This section will link to other sections of Isaac Sim documentation to describe a general process for building a new stereoscopic
depth sensor model, but should not be used as a template for other types of depth sensors.

1. Use any of the supported Isaac Sim [Importers and Exporters](../importer_exporter/importers_exporters.html#isaac-sim-importers-and-exporters) to import an existing model of the depth sensor into USD.
2. Add `Camera` prims to appropriate locations in the model and save the asset.
3. Build a test environment in USD, positioning objects and the depth sensor in the environment to accurately model a real-world test rig.
4. If using OpenCV to calibrate the real-world cameras, apply the OpenCV lens distortion schemas to the `Camera` prims, as described in [Calibration and Camera Lens Distortion Models](isaacsim_sensors_camera.html#isaacsim-sensors-camera-calibration-and-camera-lens-distortion-models).
5. Calibrate camera intrinsics and extrinsics for each Camera prim by comparing rendered images to real-world images and tuning Camera prim attributes.
6. When the camera intrinsics and extrinsics are calibrated, refer to examples in [Standalone Python](#isaacsim-sensors-camera-depth-stereoscopic-standalone) to script the post-processing pipeline: apply the depth sensor schema to a render product
   attached to the depth sensor `Camera` prim, set attributes, render a depth image, and compare the rendered depth image to the real-world depth image. Update depth sensor schema attributes, and repeat the process until the
   rendered depth image matches the real-world depth image within some acceptable threshold.

On this page

* [Stereoscopic Depth Cameras](#stereoscopic-depth-cameras)
  + [Single-View Post-Processing Pipeline](#single-view-post-processing-pipeline)
    - [Standalone Python](#standalone-python)
  + [Depth Camera Asset Wrapper](#depth-camera-asset-wrapper)
    - [Script Editor](#script-editor)
  + [Building a Depth Sensor Model in Isaac Sim](#building-a-depth-sensor-model-in-isaac-sim)
    - [Updating Existing Assets to Use Depth Sensors](#updating-existing-assets-to-use-depth-sensors)
    - [Creating a New Depth Sensor Asset](#creating-a-new-depth-sensor-asset)

---


## 标注

### RTX Annotators

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/sensors/isaacsim_sensors_rtx_annotators.html

* [Sensors](index.html)
* [RTX Sensors](isaacsim_sensors_rtx.html)
* RTX Sensor Annotators

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# RTX Sensor Annotators

The `isaacsim.sensors.experimental.rtx` and `isaacsim.sensors.rtx.nodes` extensions use Omniverse Replicator to provide Annotators for RTX Lidar and Radar data collection.

The recommended approach is to use the `LidarSensor` or `RadarSensor` classes, which manage annotators and render products automatically:

Note

This snippet will not run in the script editor window.

```python
from isaacsim import SimulationApp

kit = SimulationApp()

import numpy as np
import omni
from isaacsim.sensors.experimental.rtx import Lidar, LidarSensor, parse_generic_model_output_data

# Create the RTX Lidar.
lidar = Lidar.create(
    path="/World/lidar",
    config="Example_Rotary",
    translations=np.array([0.0, 0.0, 1.0]),
    orientations=np.array([1.0, 0.0, 0.0, 0.0]),
)

# Create a LidarSensor to attach annotators and retrieve data.
sensor = LidarSensor(lidar, annotators=["generic-model-output"])

# Play the timeline to begin collecting data.
timeline = omni.timeline.get_timeline_interface()
timeline.play()

# Collect data from the sensor on each simulation frame.
for _ in range(100):
    kit.update()
    data, info = sensor.get_data("generic-model-output")
    if data is not None:
        gmo = parse_generic_model_output_data(data)
        print(f"Points: {gmo.numElements}")

timeline.stop()
kit.close()
```

## Time Behavior of RTX Sensor Annotators

Warning

RTX Sensor Annotators rely on the simulation timeline to collect data. If the timeline is not playing (for example, if the simulation is paused or stopped), the annotators will not collect data.

The `GenericModelOutput` AOV produced by RTX Sensors contains an internal timestamp. When multi-tick rendering is enabled (default behavior), the timestamp advances every time the sensor ticks, and respects
`omni.timeline` Play/Pause/Stop controls since those controls affect the physics simulation, which drives the clock the renderer references. Driving the simulation via `omni.kit.app.get_app().update()`,
`omni.kit.app.get_app().next_update_async()`, `omni.replicator.core.orchestrator.step()`, or `omni.replicator.core.orchestrator.step_async()` is supported and should result in expected timestamp behavior.

When multi-tick rendering is disabled, the timestamp increases monotonically starting when `App Ready` appears in the simulation logs. This timestamp is independent of the animation timeline (`omni.timeline`),
so the sensor timestamp will continue to increase even if the timeline is paused or stopped. This AOV feeds into all other RTX Sensor Annotators. If the user pauses the timeline, then resumes, timestamps in the
`GenericModelOutput` point cloud (for example, the `timestamp` field of `IsaacCreateRTXLidarScanBuffer` below) may be discontinuous. This also means the simulation must be stepped using `omni.kit.app.get_app().update`
or `omni.kit.app.get_app().next_update_async()` rather than `omni.replicator.core.orchestrator.step()` or `omni.replicator.core.orchestrator.step_async()`
when collecting data using these Annotators.

Note

The `omni.replicator.core.orchestrator.step()` / `step_async()` methods are preferred when driving the simulation, to guarantee that any Writers attached to OmniSensor prims trigger correctly.

## Annotators

### IsaacExtractRTXSensorPointCloud

The `IsaacExtractRTXSensorPointCloud` Annotator extracts the `GenericModelOutput` bufferâs point cloud data
into a Cartesian (x, y, z) buffer every frame. It is provided by the `isaacsim.sensors.rtx.nodes` extension.

This annotator works with both `OmniLidar` (RTX Lidar) and `OmniRadar` (RTX Radar) prims.
It performs spherical-to-Cartesian conversion when the `GenericModelOutput` buffer contains spherical coordinates,
and outputs a sensor-to-world transform matrix.

The `RtxSensorDebugDrawPointCloud` Replicator Writer (also from `isaacsim.sensors.rtx.nodes`)
can be used to visualize the point cloud in the viewport.

**Using with the runtime sensor classes**

When `isaacsim.sensors.rtx.nodes` is enabled, a writer named `"draw-point-cloud"`
becomes available on `LidarSensor`, `RadarSensor`, and `AcousticSensor`.
Pass `writers=["draw-point-cloud"]` to attach the debug draw writer:

Run this snippet in the **Script Editor** (**Window > Script Editor**).

```python
import omni.kit.app
from isaacsim.sensors.experimental.rtx import Lidar, LidarSensor

# The "draw-point-cloud" writer is registered by isaacsim.sensors.rtx.nodes.
# Make sure that extension is enabled before constructing the sensor.
omni.kit.app.get_app().get_extension_manager().set_extension_enabled_immediate("isaacsim.sensors.rtx.nodes", True)

# Create the underlying lidar prim that the sensor will wrap.
Lidar.create("/World/lidar", config="Example_Rotary")

sensor = LidarSensor("/World/lidar", annotators=[], writers=["draw-point-cloud"])
```

**Using with RTX Radar**

The annotator works identically with `OmniRadar` prims. Remember that Motion BVH must be enabled for RTX Radar:

Run this snippet in the **Script Editor** (**Window > Script Editor**).

```python
import carb
import numpy as np
import omni.kit.app
import omni.replicator.core as rep
from isaacsim.sensors.experimental.rtx import Radar

# RTX Radar requires Motion BVH to be enabled.
settings = carb.settings.get_settings()
settings.set("/renderer/raytracingMotion/enabled", True)
settings.set("/renderer/raytracingMotion/enableHydraEngineMasking", True)
settings.set("/renderer/raytracingMotion/enabledForHydraEngines", "0,1,2,3,4")

# The debug draw writer is registered by isaacsim.sensors.rtx.nodes.
omni.kit.app.get_app().get_extension_manager().set_extension_enabled_immediate("isaacsim.sensors.rtx.nodes", True)

radar = Radar(path="/Radar", tick_rate=20, translations=np.array([0, 0, 1.0]))
render_product = rep.create.render_product(radar.paths[0], resolution=(1, 1))

writer = rep.writers.get("RtxSensorDebugDrawPointCloud")
writer.initialize(size=0.2, color=[1.0, 0.3, 0.1, 1.0])  # orange, larger points
writer.attach([render_product.path])
```

**Auxiliary data**

When using the `LidarSensor` or `RadarSensor` classes, auxiliary data (intensity, emitter IDs, material IDs, etc.)
is available directly through the `GenericModelOutput` buffer via `parse_generic_model_output_data`.
The `_replicator:rendervar:GenericModelOutput:channels` attribute on the sensor prim controls which auxiliary fields are populated:

Run this snippet in the **Script Editor** (**Window > Script Editor**).

```python
import numpy as np
from isaacsim.sensors.experimental.rtx import Lidar, LidarSensor

# Set aux_output_level to BASIC (or higher) to enable emitterId and other auxiliary fields.
lidar = Lidar.create(
    path="/World/lidar",
    config="Example_Rotary",
    aux_output_level="BASIC",
    translations=np.array([0.0, 0.0, 1.0]),
    orientations=np.array([1.0, 0.0, 0.0, 0.0]),
)

# Create a LidarSensor with the generic-model-output annotator.
# Auxiliary fields are included in the GenericModelOutput buffer based on the aux_output_level.
sensor = LidarSensor(lidar, annotators=["generic-model-output"])
```

## Reading Data from the `GenericModelOutput` Buffer

Deprecated since version 5.0: Isaac Sim 4.5 included the `OgnIsaacReadRTXLidarData` node, which provided an example of
reading data from the `GenericModelOutput` buffer in Python. This node was removed in
Isaac Sim 5.0 and is replaced by the `parse_generic_model_output_data`,
`parse_object_ids`, and `parse_stable_id_map_data` utilities (re-exported from
`isaacsim.sensors.experimental.rtx`) described below.

The `isaacsim.sensors.experimental.rtx.generic_model_output` Python module provides APIs for inspecting the
`GenericModelOutput` buffer, generated by the `GenericModelOutput` annotator. The `parse_generic_model_output_data`
utility function from `isaacsim.sensors.experimental.rtx` provides a convenient way to parse annotator output.

For more information on the `GenericModelOutput` buffer, see [the API documentation.](../py/docs/source/generic_model_output/generic_model_output.html).

For an example of reading data from the `GenericModelOutput` buffer from Isaac Sim, checkout the
standalone examples:

```python
# Lidar GMO inspection
./python.sh standalone_examples/api/isaacsim.sensors.experimental.rtx/inspect_lidar_gmo.py --aux-data-level FULL

# Radar GMO inspection
./python.sh standalone_examples/api/isaacsim.sensors.experimental.rtx/inspect_radar_gmo.py
```

### Semantic Segmentation with RTX Sensor using Object IDs

The `GenericModelOutput` struct includes an `objId` field containing per-return object identifiers.

The data is provided as a `numpy` array of `dtype` `np.uint8`, and is only populated if `--/rtx-transient/stableIds/enabled=true` is set.
This data is meant to be interpreted as a sequence of 128-bit unsigned integers (effectively `stride` 16), which are stable, unique IDs corresponding to
unique prim paths in the scene. In other words, the `i`-th 128-bit unsigned integer in the array corresponds to prim generating the `i`-th return from the sensor.
This can be used for semantic segmentation of the scene, by mapping the object IDs to prim paths and then retrieving semantic labels from the prims.

The `isaacsim.sensors.experimental.rtx` extension provides two utility functions for resolving object IDs as prim paths.

`parse_stable_id_map_data` resolves the output of the `StableIdMap` AOV (which can be generated from an `OmniLidar` or `OmniRadar` prim)
as a Python `dict` mapping stable IDs to prim paths.

`parse_generic_model_output_data` provides access to the `objId` field in the `GenericModelOutput` buffer, which contains 128-bit object IDs.

Refer to `standalone_examples/api/isaacsim.sensors.experimental.rtx/resolve_lidar_object_ids.py` for an example of using these functions to resolve object IDs as prim paths.

Note

**Not every returned object ID has a map entry.**

The renderer constructs each 128-bit object ID by combining a per-instance
base stable ID with an *upper index* placed in the high 32 bits â the
submesh index for mesh geometry, and the per-triangle primitive index for
procedural geometry. `StableIdMap` registers per-instance entries (only
for instances with a USD prim path) plus per-`GeomSubset` entries when
an instance has more than one subset, but it does **not** register
per-primitive entries.

As a result, hits on procedural geometry, on submeshes that werenât
expanded into the map, or on renderer-internal instances without a prim
path will return object IDs with no map entry. Direct `map[id]` lookups
on those IDs raise `KeyError`. Use `map.get(id, "<unknown>")` (as the
bundled example does) to handle missing IDs gracefully.

## Deprecated Annotators

Deprecated since version 6.0: The following annotators ship with the deprecated `isaacsim.sensors.rtx` extension and will
be removed in a future release: `IsaacCreateRTXLidarScanBuffer`,
`IsaacComputeRTXLidarFlatScan`, and `IsaacExtractRTXSensorPointCloudNoAccumulator`.

Use `IsaacExtractRTXSensorPointCloud` from the still-active `isaacsim.sensors.rtx.nodes`
extension instead. Most users should consume it indirectly through `LidarSensor` /
`RadarSensor` from `isaacsim.sensors.experimental.rtx`, which attach this annotator under
the hood. See [RTX Sensors](../migration_guides/isaac_sim_6_0/sensors_rtx_to_experimental_rtx.html#isaacsim-sensors-rtx-migration) for the broader migration story.

### IsaacCreateRTXLidarScanBuffer *(deprecated)*

The `IsaacCreateRTXLidarScanBuffer` Annotator accumulates frames of data from an `OmniLidar` prim into a single scan,
and provides the accumulated scan data as outputs. It is associated with the [IsaacCreateRTXLidarScanBuffer](../py/source/extensions/isaacsim.sensors.rtx/docs/ogn/OgnIsaacCreateRTXLidarScanBuffer.html) node.

Warning

The `IsaacCreateRTXLidarScanBuffer` Annotator only works with `OmniLidar` prims (RTX Lidar). It does not work with `OmniRadar` prims (RTX Radar).

By default the node outputs a 3D Cartesian point cloud, and
can optionally output the following data if the user sets the corresponding input flag to `True` when initializing the Annotator.

If creating the Annotator directly using the Replicator API, this can be done as follows:

Run this snippet in the **Script Editor** (**Window > Script Editor**).

```python
import omni.replicator.core as rep

annotator = rep.AnnotatorRegistry.get_annotator("IsaacCreateRTXLidarScanBuffer")
# Initialize the Annotator with the desired outputs.
# Note: This must be done before attaching the Annotator to a render product.
annotator.initialize(outputTimestamp=True, outputMaterialId=True)
```

The node outputs data as pointers to buffers and the table below specifies the data type of each buffer, as well as any attributes to set on the `OmniLidar` prim or carb settings that are required for the desired output(s).
If the user does not set the required attributes or carb settings, the annotator will print a warning and will not output the desired data.

| Output | Type | Description | Notes |
| --- | --- | --- | --- |
| `data` | `float3` | 3D Cartesian point cloud. | Always provided. |
| `azimuth` | `float` | Azimuth of each return, in degrees. | Provided if `outputAzimuth` is set to `true`. |
| `elevation` | `float` | Elevation of each return, in degrees. | Provided if `outputElevation` is set to `true`. |
| `distance` | `float` | Range of each return, in world units (by default, meters). | Provided if `outputDistance` is set to `true`. |
| `intensity` | `float` | Intensity of each return, normalized as described [here](https://docs.omniverse.nvidia.com/kit/docs/omni.sensors.nv.lidar/latest/lidar_extension.html#intensity-defining-attributes). | Provided if `outputIntensity` is set to `true`. |
| `timestamp` | `uint64` | Timestamp of each return, in nanoseconds since the start of the simulation. | Provided if `outputTimestamp` is set to `true`. |
| `emitterId` | `uint32` | ID of the emitter that emitted the return. | Provided if `outputEmitterId` is set to `true`, and the OmniLidarâs `aux_output_level` is `BASIC` (or higher). |
| `channelId` | `uint32` | ID of the channel the return was generated on. | Provided if `outputChannelId` is set to `true`, and the OmniLidarâs `aux_output_level` is `BASIC` (or higher). |
| `materialId` | `uint32` | ID of the material of the object that generated the return. | Provided if `outputMaterialId` is set to `true`, and the OmniLidarâs `aux_output_level` is `EXTRA` (or higher). Refer to [RTX Sensor Non-Visual Materials](isaacsim_sensors_rtx_materials.html#isaacsim-sensors-rtx-materials) for more details on how material IDs are computed. |
| `tickId` | `uint32` | ID of the tick the return was generated on. | Provided if `outputTickId` is set to `true`, and the OmniLidarâs `aux_output_level` is `BASIC` (or higher). |
| `hitNormal` | `float3` | Normal to the surface of the object that generated the return. | Provided if `outputHitNormal` is set to `true`, the OmniLidarâs `aux_output_level` is `FULL`, and `--/app/sensors/nv/lidar/publishNormals=true` is set. |
| `velocity` | `float3` | Velocity of the object that generated the return. | Provided if `outputVelocity` is set to `true`, and the OmniLidarâs `aux_output_level` is `FULL`. |
| `objectId` | `uint8` | ID of the object that generated the return. | Provided if `outputObjectId` is set to `true`, the OmniLidarâs `aux_output_level` is `EXTRA` (or higher), and `--/rtx-transient/stableIds/enabled=true` is set. Object ID is a stable, unique 128-bit unsigned integer mapping to the prim path of the object that generated the corresponding return. See [Semantic Segmentation with RTX Sensor using Object IDs](#rtx-sensor-resolving-object-ids) for more details. |
| `echoId` | `uint8` | Indicates which echo the return represents in a multi-echo Lidar configuration. | Provided if `outputEchoId` is set to `true`, and the OmniLidarâs `aux_output_level` is `BASIC` (or higher). |
| `tickState` | `uint8` | Indicates the state of the tick the return was generated on. | Provided if `outputTickState` is set to `true`, and the OmniLidarâs `aux_output_level` is `BASIC` (or higher). |

Note

`aux_output_level` is a constructor parameter on
`isaacsim.sensors.experimental.rtx.Lidar` that authors
`_replicator:rendervar:GenericModelOutput:channels` on the prim. See
[Auxiliary Output Level and the GenericModelOutput RenderVar](isaacsim_sensors_rtx.html#isaacsim-sensors-rtx-aux-output-level) for the attribute-flow explanation and how to
set the channels attribute via the UI.

Warning

Enabling nonzero `normal` output by setting `--/app/sensors/nv/lidar/publishNormals=true` will increase VRAM usage and might negatively impact performance.

### IsaacComputeRTXLidarFlatScan *(deprecated)*

The `IsaacComputeRTXLidarFlatScan` Annotator extracts depth and azimuth data from an accumulated 2D RTX Lidar scan.
It is associated with the [IsaacComputeRTXLidarFlatScan](../py/source/extensions/isaacsim.sensors.rtx/docs/ogn/OgnIsaacComputeRTXLidarFlatScan.html) node.

Warning

The `IsaacComputeRTXLidarFlatScan` Annotator only works with `OmniLidar` prims (RTX Lidar) configured as 2D lidars, defined as having emitters only at elevation angle zero (0). It does not work with `OmniRadar` prims (RTX Radar) or 3D Lidars.

### IsaacExtractRTXSensorPointCloudNoAccumulator *(deprecated)*

Per-frame point cloud extraction from the `GenericModelOutput` buffer. Works with `OmniLidar` and `OmniRadar` prims.
Replaced by `IsaacExtractRTXSensorPointCloud` from `isaacsim.sensors.rtx.nodes`.

On this page

* [Time Behavior of RTX Sensor Annotators](#time-behavior-of-rtx-sensor-annotators)
* [Annotators](#annotators)
  + [IsaacExtractRTXSensorPointCloud](#isaacextractrtxsensorpointcloud)
* [Reading Data from the `GenericModelOutput` Buffer](#reading-data-from-the-genericmodeloutput-buffer)
  + [Semantic Segmentation with RTX Sensor using Object IDs](#semantic-segmentation-with-rtx-sensor-using-object-ids)
* [Deprecated Annotators](#deprecated-annotators)
  + [IsaacCreateRTXLidarScanBuffer *(deprecated)*](#isaaccreatertxlidarscanbuffer-deprecated)
  + [IsaacComputeRTXLidarFlatScan *(deprecated)*](#isaaccomputertxlidarflatscan-deprecated)
  + [IsaacExtractRTXSensorPointCloudNoAccumulator *(deprecated)*](#isaacextractrtxsensorpointcloudnoaccumulator-deprecated)

---


## 渲染

### Multitick Rendering

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/sensors/isaacsim_sensors_multitick_rendering.html

* [Sensors](index.html)
* [RTX Sensors](isaacsim_sensors_rtx.html)
* Multi-Tick Rendering

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Multi-Tick Rendering

Multi-tick rendering decouples each sensorâs render rate from the main simulation frame rate.
Instead of rendering every sensor every frame, each sensor ticks independently at its
own configurable rate. This significantly improves performance in scenes with many sensors
by avoiding redundant rendering work.

Multi-tick rendering is **enabled by default** in Isaac Sim 6.0 and later.

On this page

* [Overview](#overview)

  + [Performance Benefits](#performance-benefits)
* [Configuring Per-Sensor Tick Rates](#configuring-per-sensor-tick-rates)

  + [Using the Isaac Sim Extension API](#using-the-isaac-sim-extension-api)
  + [Using OmniGraph](#using-omnigraph)
  + [OmniLidar Tick Rate Must Equal `scanRateBaseHz`](#omnilidar-tick-rate-must-equal-scanratebasehz)
* [Architecture: Timeline, Physics, and the Renderer](#architecture-timeline-physics-and-the-renderer)

  + [The three clocks](#the-three-clocks)
  + [Per-frame ordering](#per-frame-ordering)
  + [Behavior depends on the ratio of `physics_dt` to `loop_dt`](#behavior-depends-on-the-ratio-of-physics-dt-to-loop-dt)
  + [When `useFixedTimeStepping=true` (the full Isaac Sim GUI default)](#when-usefixedtimestepping-true-the-full-isaac-sim-gui-default)
  + [Practical implications](#practical-implications)
* [Settings Reference](#settings-reference)
* [Migration from Previous Releases](#migration-from-previous-releases)

  + [General changes](#general-changes)
  + [frameSkipCount Deprecation](#frameskipcount-deprecation)
  + [Multi-tick scheduling migration](#multi-tick-scheduling-migration)
* [Known Issues](#known-issues)

  + [RTX Radar autotriggers in 6.0 GA](#rtx-radar-autotriggers-in-6-0-ga)
  + [OmniLidar partial-scan fallback](#omnilidar-partial-scan-fallback)
  + [Radar + Lidar frames-in-flight race](#radar-lidar-frames-in-flight-race)

## [Overview](#id1)

Before Isaac Sim-6.0, every camera and RTX sensor rendered at the simulation
frame rate. With multi-tick rendering enabled, the renderer maintains independent tick
counters for each sensor and only renders a sensor when its tick interval has elapsed.

The `omni:sensor:tickRate` attribute on each sensor prim controls the render frequency
in Hz. A value of `0` (the default) puts the sensor in *autotrigger* mode, where it
renders every frame, as if multi-tick rendering was disabled.

### [Performance Benefits](#id2)

* **Reduced GPU load**: Sensors that do not need to update every frame skip rendering
  entirely, freeing GPU resources for other sensors or simulation work.
* **Independent rates**: A stereoscopic depth camera running at 60 Hz no longer forces a
  30 Hz RGB camera to also render at the same rate.
* **Better scaling**: Scenes with many sensors (for example multi-robot fleets) see
  proportionally larger improvements because each sensor only consumes GPU time when it
  actually ticks.

## [Configuring Per-Sensor Tick Rates](#id3)

Sensor tick rates are controlled by the `omni::sensor::tickRate` attribute in the `OmniSensorAPI`
USD schema, which is applied to Camera and OmniLidar prims. The shipped USD assets in Isaac Sim 6.0
already have this schema applied with appropriate default tick rates.

Note

The `OmniSensorAPI` schema is also applied to `OmniRadar` prims, but in
Isaac Sim 6.0 GA the RTX Radar renderer ignores `omni:sensor:tickRate`
and always autotriggers. See [RTX Radar autotriggers in 6.0 GA](#isaac-sim-sensors-multitick-known-issue-radar-autotrigger).

### [Using the Isaac Sim Extension API](#id4)

The `isaacsim.sensors.experimental.rtx` extension provides Python APIs for authoring sensor prims and configuring their tick rates.
For example, to author an OmniLidar prim at `/World/Lidar` with a tick rate of 10 Hz:

```python
from isaacsim.sensors.experimental.rtx import Lidar

# Render the Lidar at 10 Hz independently of the simulation frame rate.
lidar = Lidar(path="/World/Lidar", tick_rate=10.0)
```

For cameras:

```python
from isaacsim.sensors.experimental.rtx import RtxCamera

# Render the Camera at 30 Hz independently of the simulation frame rate.
camera = RtxCamera(path="/World/Camera", tick_rate=30.0)
```

### [Using OmniGraph](#id5)

When using the ROS2, UCX, or HSB helper OmniGraph nodes, the sensor tick rate is read
from the `omni:sensor:tickRate` attribute on the sensor prim. No additional node
configuration is needed.

For a worked ROS2 example that scales sensor and graph publish rates with simulation frame
rate, see [ROS2 Setting Publish Rates](../ros2_tutorials/tutorial_ros2_publish_rate.html#isaac-sim-app-tutorial-ros2-publish-rate).

### [OmniLidar Tick Rate Must Equal `scanRateBaseHz`](#id6)

Warning

For `OmniLidar` prims, `omni:sensor:tickRate` **must** be set equal to
`omni:sensor:Core:scanRateBaseHz` for scan accumulation and multi-tick rendering to
behave correctly.

If the two values differ, the Lidar model falls back to producing **partial scans every
frame** instead of accumulating to a full rotation (rotary Lidars) or full azimuth sweep
(solid-state Lidars). Downstream pipelines that assume a full scan per tick - including
`ROS2 RTX Lidar Helper` `laser_scan` publishers, `IsaacComputeRTXLidarFlatScan`, and
any consumer of accumulated `GenericModelOutput` data - silently see truncated output.
The renderer does not log an error in this case.

For example, the shipped `Example_Rotary` Lidar config has `scanRateBaseHz = 10`, so
the sensor must tick at 10 Hz:

```python
from isaacsim.sensors.experimental.rtx import Lidar

# Render at 10 Hz regardless of simulation frame rate.
lidar = Lidar.create("/World/Lidar", config="Example_Rotary", tick_rate=10.0)
```

The same constraint applies to `Example_Solid_State` and to vendor configs in
[RTX Lidars](../assets/usd_assets_nonvisual_sensors.html#isaac-assets-nonvisual-sensors-rtx-lidar). When wrapping an existing `OmniLidar`
prim, read `omni:sensor:Core:scanRateBaseHz` from the prim and pass that value as
`tick_rate`.

## [Architecture: Timeline, Physics, and the Renderer](#id7)

With multi-tick rendering enabled, three clocks advance independently per `omni.kit.app` update.
This section explains what each clock is, how each one advances,
and how they interact. Code that mixes `omni.timeline` time with physics or sensor time can
produce inconsistent timestamps in some configurations, so these relationships matter
when configuring deterministic simulations or interpreting sensor output.

### [The three clocks](#id8)

| Clock | Source of advance | Controlled by | Read by |
| --- | --- | --- | --- |
| Run-loop / `omni.timeline` time | Wall-clock dt per app update, or a fixed manual dt when set | `RenderingManager.set_dt(...)` (manual mode), `/app/runLoops/main/rateLimitFrequency` | Timeline UI, `timeCodesPerSecond`, stage update scheduling |
| Physics simulation time | Recomputed on every physics step as `stepCount / stepsPerSecond` | `PhysicsScene.set_dt(...)` or `SimulationManager.setup_simulation(dt=...)` | `SimulationManager.get_simulation_time()`, `IsaacReadSimulationTime`, ROS 2 / UCX / HSB timestamps |
| Renderer simulation time | Mirror of physics time, written to the Fabric prim `/ExternalSimulationTime.omni:time` after each physics step | Driven by `isaacsim.core.simulation_manager`; seeded by `RenderingManager` when the simulation manager is absent | The multi-tick rendererâs per-sensor tick scheduler at `eHydraRendering` |

The renderer no longer reads `omni.timeline` to obtain the current simulation time;
it reads the `omni:time` attribute on the `/ExternalSimulationTime` prim from Fabric. Physics writes that attribute on
every `onPhysicsStep` callback at stage-update order `-10`, so the latest value is
available to Hydra at order `30` within the same app update.

### [Per-frame ordering](#id9)

For one `App.update()` with the timeline playing:

1. The run loop computes `loop_dt` (manual or wall-clock) and `omni.timeline`
   advances by `loop_dt`.
2. The physics stage-update phase runs `N >= 0` substeps of `physics_dt` to catch
   the loop time. Each substep recomputes the physics simulation time and writes it to
   `/ExternalSimulationTime`.
3. Hydra reads `/ExternalSimulationTime` once. The per-sensor tick scheduler compares
   that value to each sensorâs last-rendered time and its `omni:sensor:tickRate` to
   decide which sensors render this frame.
4. OmniGraph nodes such as `IsaacReadSimulationTime` read the same simulation time,
   either directly or, when given a reference frame `RationalTime`, via interpolation
   from the `TimeSampleStorage` ring buffer maintained by
   `isaacsim.core.simulation_manager`.

### [Behavior depends on the ratio of `physics_dt` to `loop_dt`](#id10)

| Configuration | Physics steps per app update | End-of-frame `/ExternalSimulationTime` | Timeline vs physics time | Per-sensor ticking |
| --- | --- | --- | --- | --- |
| `physics_dt == loop_dt` | 1 | Equal to loop time | Equal each frame | As scheduled |
| `physics_dt < loop_dt` | `N >= 1` | Equal to loop time within one substep | Equal each frame | As scheduled |
| `physics_dt > loop_dt` | `0` or `1` | Lags loop time by up to one `physics_dt` | Drifts within a physics step, resyncs when physics advances | Only on frames where `/ExternalSimulationTime` advanced |

In the `physics_dt <= loop_dt` cases, multiple physics substeps in the same frame all
write to `/ExternalSimulationTime`, but only the last value is what the renderer
reads. `TimeSampleStorage` collapses these writes to a single sample per frame, keyed
by the frameâs `RationalTime`, holding the cumulative physics time.

In the `physics_dt > loop_dt` case, frames where no physics step runs leave
`/ExternalSimulationTime` unchanged. The render pipeline still runs every app update,
but per-sensor tick counters do not advance and no sensor produces a new output on those
frames. When physics finally steps, the prim jumps forward by `physics_dt` and due
sensors render on that frame.

### [When `useFixedTimeStepping=true` (the full Isaac Sim GUI default)](#id11)

The table above describes the substep-to-catch-up behavior that applies when
`/app/player/useFixedTimeStepping` is **false** (the default in standalone Python).
The full Isaac Sim GUI app sets this carb setting to **true** in
`source/apps/isaacsim.exp.full.kit`. With it true, the timeline ignores the run-loopâs
measured `dt` and forces `dt = 1 / timeCodesPerSecond` per accepted update inside
`Timeline::update()`. Sensor and timeline time then advance at:

```python
sim_advance_per_wall_sec  =  (1 / timeCodesPerSecond)  *  loop_hz_wall
```

Consequences:

* If `loop_hz_wall == timeCodesPerSecond` (the default 60 Hz on both), `sim/wall = 1.0`
  and the system runs in real time. This is what
  `isaacsim.core.rendering_manager.RenderingManager.set_dt()` configures when called
  alone - it aligns `rateLimitFrequency`, `targetFramerate`, and `timeCodesPerSecond`
  to the same value.
* If `loop_hz_wall < timeCodesPerSecond` (e.g. the loop is rate-limited below the
  timelineâs per-tick rate), the simulation runs in **slow motion** at ratio
  `loop_hz_wall / timeCodesPerSecond`. RTX sensors gated by
  `/ExternalSimulationTime` publish proportionally slower; OnPlaybackTick-driven
  publishers (`/clock`, OmniGraph ticks) still fire at `loop_hz_wall`. This is the
  trap when users only set `/app/runLoops/main/rateLimitFrequency` without updating
  `timeCodesPerSecond`: physics step time and wall clock decouple in a non-obvious way.
* If `loop_hz_wall > timeCodesPerSecond`, the behavior depends on
  `/app/player/useFastMode` (also exposed as `timeline.set_play_every_frame(...)`):

  + **``useFastMode = false`` (the default)**: the timeline subsamples (advances time on
    every Nth run-loop tick where `N = ceil(targetFramerate / timeCodesPerSecond)`) so
    the timeline stays at its configured rate while the run loop ticks faster. This is
    used to drive higher render-product / OnPlaybackTick rates without speeding up
    sim time.
  + **``useFastMode = true``** (set when, for example, `timeline.set_play_every_frame(True)`
    is called - some Replicator examples and benchmarks do this): the subsample gate is
    bypassed. Every run-loop tick advances the timeline by `1 / timeCodesPerSecond`,
    so sim time runs **faster than wall time** (fast-forward) at ratio
    `loop_hz_wall / timeCodesPerSecond`. This is the intended behavior for offline
    data generation where you want to ingest as much simulated time as possible per
    wall second, but it breaks any code that assumes sim time tracks wall time.

The reference example in
[Setting the Simulation Rate (Advanced)](../ros2_tutorials/tutorial_ros2_publish_rate.html#isaac-sim-app-tutorial-ros2-publish-rate-set-simulation-frame-rates) uses
`isaacsim.core.simulation_manager.SimulationManager.setup_simulation()` plus
`isaacsim.core.rendering_manager.RenderingManager.set_dt()` to keep all three
clocks coherent - avoiding all of the above modes by construction. It leaves
`useFastMode` at its default of `false`.

### [Practical implications](#id12)

* Always read simulation time through `SimulationManager.get_simulation_time()`,
  `IsaacReadSimulationTime`, or the per-frame `getSimulationTimeAtTime(rtime)`
  lookup. These return the physics-driven value that the renderer also sees, so sensor
  stamps, TF stamps, and downstream consumers stay consistent.
* Do not use `omni.timeline` current time as a sensor or message timestamp. In the
  `physics_dt > loop_dt` configuration the two clocks drift each frame and only
  resync on physics steps, producing inconsistent stamps.
* To keep physics, the renderer, and downstream pipelines all advancing once per
  frame, set `physics_dt == loop_dt` via
  `SimulationManager.setup_simulation(dt=1.0 / hz)` and
  `RenderingManager.set_dt(1.0 / hz)`. The `isaacsim.exp.base.zero_delay.kit`
  experience configures this and is the reference setup for deterministic single-frame
  TF / image pairing.

## [Settings Reference](#id13)

The settings, APIs, and USD attributes below configure multi-tick rendering, per-sensor
tick rates, and the underlying loop / physics clocks discussed in
[Architecture: Timeline, Physics, and the Renderer](#isaac-sim-sensors-multitick-clock-relationships).

| Setting / API / Attribute | Kind | Default | Effect |
| --- | --- | --- | --- |
| `/rtx/hydra/supportMultiTickRate` | carb setting | `true` | Enables multi-tick rendering. When `false`, the renderer reverts to per-frame rendering and does not consult `/ExternalSimulationTime`. |
| `/rtx/rendering/perSensorTickTlas` | carb setting | `true` | Builds a per-sensor Top-Level Acceleration Structure (TLAS) on each sensor tick instead of once per frame. |
| `/app/player/playSimulations` | carb setting | `true` | When `false`, `App.update()` does not step physics, so `/ExternalSimulationTime` is frozen even though `omni.timeline` may continue to advance. `RenderingManager.render()` toggles this around its update to render without ticking the simulation clock. |
| `RenderingManager.set_dt(dt)` | Python API | n/a | Sets `loop_dt`. Switches the Isaac loop runner to manual mode, sets `/app/runLoops/main/rateLimitFrequency`, and updates `omni.timeline.set_target_framerate` and the stageâs `timeCodesPerSecond`. |
| `PhysicsScene.set_dt(dt)` / `SimulationManager.setup_simulation(dt=...)` | Python API | 1/60 s | Sets `physics_dt` on the physics scene. The physics engine uses an internal accumulator to decide how many substeps to take each app update. |
| `RenderingManager.render()` | Python API | n/a | Render the stage without stepping physics. Temporarily sets `/app/player/playSimulations=false` for one app update. |
| `omni:sensor:tickRate` (Hz) | USD attribute | `0` (autotrigger) | Per-sensor render rate. Compared against `/ExternalSimulationTime` by the per-sensor tick scheduler. Applied to `Camera` and `OmniLidar` prims; ignored on `OmniRadar` in 6.0 GA (see [RTX Radar autotriggers in 6.0 GA](#isaac-sim-sensors-multitick-known-issue-radar-autotrigger)). |
| `omni:sensor:Core:scanRateBaseHz` (Hz) | USD attribute | Config-dependent (for example `10` for `Example_Rotary`) | OmniLidar scan rate. Must equal `omni:sensor:tickRate` - see [OmniLidar Tick Rate Must Equal scanRateBaseHz](#isaac-sim-sensors-multitick-lidar-tickrate-must-match-scanrate). |
| `omni:sensor:Core:accumulateOutputs` | USD attribute | `true` | OmniLidar scan accumulation. When `true`, full scans accumulate over multiple frames; when `false`, the GMO carries the per-frame partial scan. |

The `/rtx/hydra/supportMultiTickRate` and `/rtx/rendering/perSensorTickTlas` settings
are configured in `isaacsim.exp.base.kit` and are also passed as standard test
arguments to all extension tests.

Note

To reproduce the Isaac Sim 5.x render-every-frame behavior in 6.0 (for
example to debug a regression), launch with
`--/rtx/hydra/supportMultiTickRate=false`. Most other code paths in 6.0 assume the
global default and have not been validated with the setting disabled.

## [Migration from Previous Releases](#id14)

If you are upgrading from a release where multi-tick rendering was not enabled by
default, the following changes may affect your workflow.

### [General changes](#id15)

1. **Update Camera and OmniSensor prims to work with multi-tick rendering.** Apply the
   `OmniSensorAPI` schema to `Camera` prims. This schema is already applied by
   default to `OmniLidar`/`OmniRadar` prims. Set the `omni:sensor:tickRate`
   attribute to control render frequency. Multi-tick rendering is transparent when
   sensors use the default `omni:sensor:tickRate` of `0` (autotrigger), which
   renders every frame.
2. **USD assets updated.** Shipped sensor assets now have the `OmniSensorAPI` schema
   applied. If you have custom USD assets with `Camera` or `OmniLidar`/`OmniRadar`
   prims, apply the `OmniSensorAPI` schema and set `omni:sensor:tickRate` to control
   render frequency.
3. **frameSkipCount is deprecated.** Replace usage of `frameSkipCount` on
   ROS2/UCX/HSB helper nodes with `omni:sensor:tickRate` on the sensor prim. See
   [frameSkipCount Deprecation](#isaac-sim-sensors-multitick-frameskipcount-deprecation) below.
4. **RTX Lidar accumulation moved to a USD attribute.** Lidar scan accumulation is now
   controlled by the `omni:sensor:Core:accumulateOutputs` attribute on the
   `OmniLidar` prim. The deprecated `isaacsim.sensors.rtx` extensionâs
   `IsaacExtractRTXSensorPointCloudNoAccumulator` annotator and its
   `IsaacCreateRTXLidarScanBuffer` and `IsaacComputeRTXLidarFlatScan` nodes have
   been updated to read this attribute. The newer `IsaacExtractRTXSensorPointCloud`
   annotator and OmniGraph node live in `isaacsim.sensors.rtx.nodes` and assume the
   GMO buffer already contains either a full scan or a per-frame partial scan based on
   `accumulateOutputs`.
5. **Replace single-render-product waits with full app updates.** The
   `omni.syntheticdata.sensors.next_render_simulation_async` helper (and any other
   helper that targets a single render product) does not advance per-sensor tick
   counters correctly under multi-tick rendering. Use
   `isaacsim.core.experimental.utils.app.update_app_async` instead, which performs
   full application update steps and ensures all sensor ticks are processed.

   *Before:*

   ```python
   import omni.syntheticdata

   # Example values for an attached render product and a per-product wait count.
   render_product_path = "/Render/RenderProduct_Replicator"
   N = 1

   # Deprecated: does not advance per-sensor tick counters under multi-tick rendering.
   await omni.syntheticdata.sensors.next_render_simulation_async([render_product_path], N)
   ```

   *After:*

   ```python
   import isaacsim.core.experimental.utils.app as app_utils

   # Number of full application update steps to perform.
   N = 1

   await app_utils.update_app_async(steps=N)
   ```

### [frameSkipCount Deprecation](#id16)

In previous releases, publish rates for the ROS2 and UCX helper nodes were controlled by
the `frameSkipCount` input on each helper node. This parameter is now **deprecated**.

With multi-tick rendering enabled globally, the correct way to control how often a
sensor publishes data is to set `omni:sensor:tickRate` on the sensor prim itself. This
is more efficient because the sensor does not render at all during skipped ticks, rather
than rendering and discarding the output.

The `frameSkipCount` parameter still works for backward compatibility, but a
deprecation warning is logged when a non-zero value is used. It will be removed in a
future release.

The deprecation applies to every helper node that previously exposed `frameSkipCount`:

* `ROS2 Camera Helper` (`isaacsim.ros2.bridge.ROS2CameraHelper`)
* `ROS2 Camera Info Helper` (`isaacsim.ros2.bridge.ROS2CameraInfoHelper`)
* `ROS2 RTX Lidar Helper` (`isaacsim.ros2.bridge.ROS2RtxLidarHelper`)
* `UCX Camera Helper` (`isaacsim.ucx.bridge.UCXCameraHelper`)

The newer `ROS2 RTX Radar Helper` (`isaacsim.ros2.bridge.ROS2RtxRadarHelper`) was
introduced after this deprecation and does not expose `frameSkipCount` at all.

### [Multi-tick scheduling migration](#id17)

The table below lists 5.x rate-control inputs and the recommended 6.0 replacement for
each sensor type. For the broader extension API migration (Kit-command-based sensor
creation, class renames, annotator attach styles, GMO-helper changes), see
[RTX Sensors](../migration_guides/isaac_sim_6_0/sensors_rtx_to_experimental_rtx.html#isaacsim-sensors-rtx-migration). For the deprecated `isaacsim.sensors.camera`
extension, see [Camera Sensors](../migration_guides/isaac_sim_6_0/sensors_camera_to_experimental_rtx.html#isaacsim-sensors-camera-migration). For `auxOutputType` ->
`GenericModelOutput` channels, see [Auxiliary Output Level and the GenericModelOutput RenderVar](isaacsim_sensors_rtx.html#isaacsim-sensors-rtx-aux-output-level).

| Sensor type | 5.x input | 6.0 replacement | Notes |
| --- | --- | --- | --- |
| RTX Lidar | `frameSkipCount` on `ROS2 RTX Lidar Helper` | `omni:sensor:tickRate` on the `OmniLidar` prim | Must equal `omni:sensor:Core:scanRateBaseHz`. See [OmniLidar Tick Rate Must Equal scanRateBaseHz](#isaac-sim-sensors-multitick-lidar-tickrate-must-match-scanrate). |
| RTX Lidar | `fullScan` input on `ROS2 RTX Lidar Helper` | `omni:sensor:Core:accumulateOutputs` on the `OmniLidar` prim | Helper input is now ignored and logs a deprecation warning when set to `False`. |
| Camera (ROS 2) | `frameSkipCount` on `ROS2 Camera Helper` / `ROS2 Camera Info Helper` | `omni:sensor:tickRate` on the `Camera` prim | Camera prim must have `OmniSensorAPI` applied. `RtxCamera` applies it automatically. |
| Camera (UCX) | `frameSkipCount` on `UCX Camera Helper` | `omni:sensor:tickRate` on the `Camera` prim | Helper still accepts `frameSkipCount` and logs a deprecation warning. |

RTX Radar is intentionally omitted: `omni:sensor:tickRate` is ignored on
`OmniRadar` in 6.0 GA (see
[RTX Radar autotriggers in 6.0 GA](#isaac-sim-sensors-multitick-known-issue-radar-autotrigger)). Gate Radar publish
rates downstream instead.

## [Known Issues](#id18)

### [RTX Radar autotriggers in 6.0 GA](#id19)

In Isaac Sim 6.0 GA, the RTX Radar renderer ignores `omni:sensor:tickRate`
on `OmniRadar` prims and renders every simulation frame. Setting `tick_rate` on
`isaacsim.sensors.experimental.rtx.Radar` has no effect on the actual
render cadence; the attribute is still authored on the prim, but the multi-tick
scheduler skips Radar prims. This is expected to be corrected in a future release.

The autotrigger limitation does not affect `OmniLidar` or `Camera` prims.

### [OmniLidar partial-scan fallback](#id20)

If `omni:sensor:tickRate` is not equal to `omni:sensor:Core:scanRateBaseHz` on an
`OmniLidar` prim, the sensor falls back to emitting partial scans every frame. See
[OmniLidar Tick Rate Must Equal scanRateBaseHz](#isaac-sim-sensors-multitick-lidar-tickrate-must-match-scanrate) for details and
the recommended remediation.

### [Radar + Lidar frames-in-flight race](#id21)

A fatal crash from `rtx.sensors.lidar.core.plugin` may occur during the first 1-2
wall-clock seconds after starting simulation when a scene combines RTX Radar, RTX Lidar,
and Motion BVH. The crash is caused by a timing-dependent race in the RTX sensor
frameworkâs frames-in-flight (FIF) scheduling, where the Lidarâs per-frame trace begins
before its sensor profile has been initialized. Affected configurations crash
deterministically; unaffected hardware does not see the issue. The error appears as a
floating-point exception inside `LidarRotary::openTrace` or, less commonly, a
segmentation fault in the v3.0 sensor scheduler:

> ```python
> [Fatal] [carb.crashreporter-breakpad.plugin] Crashing: SIGFPE
> at rtx.sensors.lidar.core.plugin::LidarRotary::openTrace
> ```

Once the simulation has been running for ~1-2 wall-clock seconds without crashing, the
session is stable for the remainder of its lifetime.

#### Standalone Python workaround

In standalone Python workflows, delay creating the render product for the Radar and
attaching any Annotators or Writers until after the frames-in-flight have stabilized.
Construct the Lidars normally before `timeline.play()`, but construct only the
Radarâs USD authoring object pre-play and defer the `RadarSensor` wrap until after a
short warmup window:

```python
from isaacsim import SimulationApp

simulation_app = SimulationApp({"headless": True, "enable_motion_bvh": True})

import carb
import numpy as np
import omni
from isaacsim.core.experimental.objects import Cube
from isaacsim.sensors.experimental.rtx import (
    Lidar,
    LidarSensor,
    Radar,
    RadarSensor,
    parse_generic_model_output_data,
)

Cube("/cube", sizes=2.0, positions=np.array([10.0, 0.0, 0.0]))

# Lidars: full wrap pre-play (USD prim + render product + annotators).
lidar_sensor_1 = LidarSensor(Lidar("/lidar_1"), annotators=["generic-model-output"])
lidar_sensor_2 = LidarSensor(Lidar("/lidar_2"), annotators=["generic-model-output"])

# Radar: USD authoring object only. Defer the RadarSensor wrap until after the
# Lidar frames-in-flight slots have stabilized post-play.
radar = Radar("/radar")

# Start playback and let the Lidars warm up for a few frames before wrapping
# the Radar. 5 frames is one full rotation of the default 3-slot
# frames-in-flight buffer plus a small margin; heavier scenes may need more.
timeline = omni.timeline.get_timeline_interface()
timeline.play()
for _ in range(5):
    simulation_app.update()

# Now safe to wrap the Radar. This call creates the Radar's render product and
# binds annotators - the operation that would open the FIF race window if done
# concurrently with Lidar attachment.
radar_sensor = RadarSensor(radar, annotators=["generic-model-output"])

# Continue running and verify every sensor is producing output.
for _ in range(60):
    simulation_app.update()

    for sensor, name in [
        (lidar_sensor_1, "lidar_1"),
        (lidar_sensor_2, "lidar_2"),
        (radar_sensor, "radar"),
    ]:
        data, _ = sensor.get_data("generic-model-output")
        gmo = parse_generic_model_output_data(data)
        carb.log_warn(f"{name}: numElements={gmo.numElements}")

timeline.stop()
simulation_app.close()
```

The 5-frame warmup is conservative: it is one full rotation of the default 3-slot
frames-in-flight buffer plus a small margin. Heavier scenes may require a larger value.

#### OmniGraph workaround

In OmniGraph workflows using the `ROS2RtxRadarHelper` node, you can stagger creating
the Radarâs render product until after the Lidars have stabilized. Place an
`omni.graph.action.Countdown` node between the `OnPlaybackTick` and the
`ROS2RtxRadarHelper` node, setting its `duration` to `5` and its `period` to
`1`. The `Countdown` nodeâs `finished` output triggers downstream graph execution
after `duration` ticks have elapsed, analogous to the 5-frame warmup in the standalone
Python workflow. You may need to increase the `duration` value based on your sceneâs
complexity and your hardware configuration.

On this page

* [Overview](#overview)
  + [Performance Benefits](#performance-benefits)
* [Configuring Per-Sensor Tick Rates](#configuring-per-sensor-tick-rates)
  + [Using the Isaac Sim Extension API](#using-the-isaac-sim-extension-api)
  + [Using OmniGraph](#using-omnigraph)
  + [OmniLidar Tick Rate Must Equal `scanRateBaseHz`](#omnilidar-tick-rate-must-equal-scanratebasehz)
* [Architecture: Timeline, Physics, and the Renderer](#architecture-timeline-physics-and-the-renderer)
  + [The three clocks](#the-three-clocks)
  + [Per-frame ordering](#per-frame-ordering)
  + [Behavior depends on the ratio of `physics_dt` to `loop_dt`](#behavior-depends-on-the-ratio-of-physics-dt-to-loop-dt)
  + [When `useFixedTimeStepping=true` (the full Isaac Sim GUI default)](#when-usefixedtimestepping-true-the-full-isaac-sim-gui-default)
  + [Practical implications](#practical-implications)
* [Settings Reference](#settings-reference)
* [Migration from Previous Releases](#migration-from-previous-releases)
  + [General changes](#general-changes)
  + [frameSkipCount Deprecation](#frameskipcount-deprecation)
  + [Multi-tick scheduling migration](#multi-tick-scheduling-migration)
* [Known Issues](#known-issues)
  + [RTX Radar autotriggers in 6.0 GA](#rtx-radar-autotriggers-in-6-0-ga)
  + [OmniLidar partial-scan fallback](#omnilidar-partial-scan-fallback)
  + [Radar + Lidar frames-in-flight race](#radar-lidar-frames-in-flight-race)
    - [Standalone Python workaround](#standalone-python-workaround)
    - [OmniGraph workaround](#omnigraph-workaround)

---


## 传感器配置

### Camera Calibration

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/action_and_event_data_generation/ext_sensors_rtx_placement/camera_calibration.html

* [Synthetic Data Generation](../../synthetic_data_generation/index.html)
* [Action and Event Data Generation](../index.html)
* [RTX Sensors Placement and Calibration](../tutorial_sensors_rtx_placement.html)
* Camera Calibration

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Camera Calibration

The Camera Calibration Tool (`isaacsim.sensors.rtx.calibration` extension) generates camera calibration data for deployed cameras in the scene.

## Enable the Extension

Follow the [Omniverse Extension Manager guide](https://docs.omniverse.nvidia.com/extensions/latest/ext_core/ext_extension-manager.html) to enable the `isaacsim.sensors.rtx.calibration` extension.

## Open the Calibration Tool Panel

The **Calibration Tool** UI will automatically be opened on the right side of the screen. It is accessible by **Tools > Sensors > Camera Calibration**.

### Input Fields

**Place Info**: A string that describes the location of the scene, including city, building, and room. This information is converted and stored in `calibration.json`. Review the output example for more details.

> * Input Format: `city=[city name]/building=[building name]/room=[room name]`
> * Example:
>
>   > + Input: `city=Santa Clara/building=NVIDIA Voyager/room=Visitor Lobby`
>   > + Output: in `calibration.json`:
>   >
>   > ```python
>   > {
>   >     "place": [
>   >         {
>   >         "name": "city",
>   >         "value": "Santa Clara"
>   >         },
>   >         {
>   >             "name": "building",
>   >             "value": "NVIDIA Voyager"
>   >         },
>   >         {
>   >             "name": "room",
>   >             "value": "Visitor Lobby"
>   >         }
>   >     ],
>   > }
>   > ```

**Scene Root Prim Path**: The path to the root prim of the scene. This is used to approximate the top view cameraâs position. The top view camera will look at the scene root primâs center.

**Floor & Ceiling Height**: The floor and ceiling height values for the scene.

> Note
>
> * The ceiling height adjusts the clipping range of the top view camera, making it easier to create accurate top views.
> * By default, the ceiling height is set to `-1`, which means the top view cameraâs clipping range will use its default value.
> * By customizing the ceiling height, you can clip out prims or objects above the specified value when creating a top view camera.

**Top View Camera**: This camera will be used to render the `top_view` images.

> * **Create**: After **Scene Root Prim Path** is set, clicking this button will automatically generate a top view camera that looks at the scene rootâs center. The top view camera will be generated under `/World/Top_Camera`.
> * **Path**: After clicking **Create**, the top view cameraâs path will be shown here. You can also use this field to select existing top view cameras in the stage.

> Note
>
> * The **Top View Camera** must be vertical to the ground and it must cover the position of all the calibration dots under `World/Calibration_Dots` and cameras under the `World/Cameras`.
> * The **Top View Camera** must have a rotation of `[0,0,0]` with the projection type set to `orthographic`.

**Raycast Density**: The density of the raycast. The higher this value, the more detailed the FOV contour will be. A density value of `N` indicates that `N * N` rays will be cast and they are uniformly distributed for each camera.

> * Default value: 100

**Minimum FOV Polygon Edge Length (meter)**: The minimum length of edges in the polygonâs contour. Edges shorter than this length are ignored and the vertices are connected to the next point that meets this criteria. The unit is meter.

> * Default value: 0 (no simplification in drawing the contour)

**Minimum Area of FOV Polygon Hole to Ignore**: When generating data, holes in the FOV polygon that are smaller than this threshold value are ignored. Holes are the areas that are not included in the FOV polygon.

> * Default value: 0 (donât ignore any holes in FOV polygons)

**Create Camera View Images**: Whether to include camera view images in the output folder.

**Create FOV Polygon Images**: Whether to render top view images with FOV polygons in the debug data folder.

**Show FOV Polygon**: Whether to show FOV polygons from the currently selected camera.

**Output Folder Path**: The path to the output folder. Click on the folder icon to select the output folder path.

#### Buttons and Functions

Note

Before starting to generate the calibration file, the following prerequisites must be met:

> * **Top View Camera Path** field is set up with a valid camera prim path to a [valid top view camera](#valid-topview-camera-path).
> * The output folder path value must be valid.
> * The **Place Info** must have the correct format and input.
> * The cameras must be under `/World/Cameras`.

* **Create Dot Prims**: Generate calibration dot prims for each camera. Calibration dots will be randomly generated and they are used to sample the polygons contour that each camera can view.
* **Generate Calibration File**: Create `calibration.json` that stores all the camera calibration data.

  > Note
  >
  > You must run **Create Dot Prims** before generating the calibration file.
* **Generate Top View Image**: Generates the top view image and stores the image in the output folder. An `imageMetadata.json` file will be generated to store the image metadata.

  > Note
  >
  > If the `Create FOV Polygon Images` is checked, the FOV polygon is visualized on the top view layout. The FOV images are generated in a debug data folder within the output folder.

## Using the Camera Calibration Tool Tutorial

To use the **Camera Calibration** tool. This tutorial makes use of the [Isaac Sim Full Warehouse](../../assets/usd_assets_environments.html#isaac-assets-environments-warehouse) for demonstration.

Note

* Stage unit must be in meters.
* A valid [NavMesh](https://docs.omniverse.nvidia.com/extensions/latest/ext_navigation-mesh.html "(in Omniverse Extensions)") is required.

### Enable the Extension

1. [Enable the isaacsim.sensors.rtx.calibration extension](#enabling-camera-calibration-extension).
2. [Open the camera calibration tool panel](#activate-camera-calibration-tool-panel).

### Create Cameras

Cameras under `/World/Cameras` are used to generate the calibration file. Ideally, the cameras are able to view the walkable area of the scene.

> Tip
>
> To add cameras to the stage, follow the [Isaac Sim Camera tutorial](../../robot_setup_tutorials/tutorial_gui_camera_sensors.html#isaac-sim-app-tutorial-gui-camera-sensors).
>
> Alternatively, you can [use IRA to spawn cameras](../tutorial_replicator_agent.html#actor-sim-getting-started).

### Create Top View Camera

The **Top View Camera** supports the following features:

* Capture top view images of the scene.
* Generate FOV polygons of the scene.
* Generate 2D camera locations of each camera within the top view image.

The extension provides a UI to help you create the top view camera:

1. Set the **Scene Root Prim Path**. The top view camera generated by this tool will look at this scene root. In this case, set it to `/Root`.
2. Set the **Floor & Ceiling Height** values to clip the ceiling from the top view cameraâs view.

   > Note
   >
   > * In this tutorial, set **Ceiling Height** to `6` to clip the warehouse ceiling.
   > * Because the warehouse floor height is `0`, thereâs no need to change the **Floor Height**.
3. Click **Create**. The top view camera will be generated and its path will be shown in the text field.
4. Switch the viewport to the new top view camera to verify that it covers the floorplan.

Tip

To switch the viewport to the top-view camera, click the Camera icon, then click **Cameras > Calibration\_Top\_Camera**.

### Set Up the Calibration Tool Attributes

This step is to enter the information needed for camera calibration.

1. Enter the place information in **Place Info**. In this case, itâs `city=Santa Clara/building=Isaac Sim Warehouse/room=Warehouse`.
2. Set **Raycast Density**, **Minimum FOV Polygon Edge Length**, and **Minimum Area of FOV Polygon Hole to Ignore**. See the [Input Field](#ira-calibration-attribute) for more details. In this case, use the default values.
3. Check the **Create Camera View Images**, **Create FOV Polygon Images**, and **Show FOV Polygon** boxes if these [additional data](#ira-calibration-additional-attribute) are needed.
4. Set **Output Folder Path** by either entering the path or clicking the folder picker icon.

### Generate Calibration Dots

Generate calibration dots for each camera by clicking the **Create Dot Prims** button.

Note

* Calibration dot prims are generated under `/World/Calibration_Dots/[Camera Name]/`, where `[Camera Name]` is the name of the camera.
* For each camera prim under `/World/Cameras`, six calibration dots are generated. The dot prims are used to calculate the projection matrix for each camera.
* You can switch your viewport to any cameraâs view to check whether all calibration dots are visible.

### Generate the Calibration File

1. Generate the calibration file by clicking on the **Generate Calibration File** button. This generates a `calibration.json` file to **Output Folder Path**.
2. After the `calibration.json` file is generated. You can visualize the FOV in the stage by selecting the target camera.

Note

Your result might look different because it depends on the camera parameters. In this tutorial, the translate of the camera is `(-13.02311, 7.20828, 5.0)`, the orient is `(-55.253, -56.035, -150.088)`, and the camera focal length is `20.94`.

### Generate Top View Image

To visualize the generated FOV polygon top view image, generate the image by clicking on **Generate Top View Image** button.

> The Top View Cameraâs view will be rendered and output to the `[Output Folder Path]`.
> An `imageMetadata.json` file is also generated to store image metadata.

Note

If **Create FOV Polygon Images** is checked, for each camera there will be an image with a white-shaded FOV polygon from the top view.
The FOV polygon images will be generated under `[Output Folder Path]/Debug/fieldOfViewPolygon`.

On this page

* [Enable the Extension](#enable-the-extension)
* [Open the Calibration Tool Panel](#open-the-calibration-tool-panel)
  + [Input Fields](#input-fields)
    - [Buttons and Functions](#buttons-and-functions)
* [Using the Camera Calibration Tool Tutorial](#using-the-camera-calibration-tool-tutorial)
  + [Enable the Extension](#id1)
  + [Create Cameras](#create-cameras)
  + [Create Top View Camera](#create-top-view-camera)
  + [Set Up the Calibration Tool Attributes](#set-up-the-calibration-tool-attributes)
  + [Generate Calibration Dots](#generate-calibration-dots)
  + [Generate the Calibration File](#generate-the-calibration-file)
  + [Generate Top View Image](#generate-top-view-image)

---

### Camera Placement

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/action_and_event_data_generation/ext_sensors_rtx_placement/camera_placement.html

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
>   :   Determines whether the cameraâs field of view should be restricted based on its **Camera Distance Range**.
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

**Stage Processing Parameters** allows you to configure the camera placement method according to the stageâs size, height, and complexity.
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

---

### Sensors RTX Placement Tutorial

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/action_and_event_data_generation/tutorial_sensors_rtx_placement.html

* [Synthetic Data Generation](../synthetic_data_generation/index.html)
* [Action and Event Data Generation](index.html)
* RTX Sensors Placement and Calibration

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# RTX Sensors Placement and Calibration

Optimizing camera placement is a crucial technique, particularly in indoor or enclosed spaces such as warehouses, retail stores, hospitals, and other similar environments, to ensure comprehensive coverage while minimizing camera deployment costs.

Isaac Sim provides two separate extensions to help you optimize camera placement and extract calibration data:

* **Camera Placement** (`isaacsim.sensors.rtx.placement`): Automatically determines optimal camera locations based on scene layout and coverage requirements.

  > + [Camera Placement](ext_sensors_rtx_placement/camera_placement.html)
* **Camera Calibration** (`isaacsim.sensors.rtx.calibration`): Extracts and manages camera calibration data, including position, orientation, and field of view information.

  > + [Camera Calibration](ext_sensors_rtx_placement/camera_calibration.html)

---


## GUI

### Menu Replicator (GUI)

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/gui/menu_replicator.html

* [GUI Reference](index.html)
* Replicator Menu

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Replicator Menu

The Replicator (Tools > Replicator) menu has a suite of useful tools and extensions for [omni.replicator](https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator.html "(in Omniverse Extensions)") and generating, visualizing, and recording synthetic data.

| UI Element | Reference |
| --- | --- |
| Semantics Schema Editor | Add semantic information. Refer to the [Semantics Schema Editor](https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator/semantics_schema_editor.html "(in Omniverse Extensions)") docs for more details. |
| Synthetic Data Recorder | Synthetic Data Recorder. Refer to the [Synthetic Data Recorder](../replicator_tutorials/tutorial_replicator_recorder.html) docs for more details. |
| ReplicatorYAML | Generating dataset using [Replicator YAML](https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator/yaml_manual.html#replicator-yaml-manual "(in Omniverse Extensions)"). |
| Start | Starts the randomizations and writing to disk [omni.replicator](https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator.html "(in Omniverse Extensions)"). |
| Step | Performs a single randomization operations with writing to disk [omni.replicator](https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator.html "(in Omniverse Extensions)"). |
| Preview | Performs a singe randomization iteration without writing to disk [omni.replicator](https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator.html "(in Omniverse Extensions)"). |

---


## 概览

### Sensors Index

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/sensors/index.html

* Sensors

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Sensors

Isaac Sim sensor simulation extensions simulate ground truth perception and physics-based sensors and provide a library of realistic sensor models.

* [Camera Sensors](isaacsim_sensors_camera.html)
  + [Overview](isaacsim_sensors_camera.html#overview)
  + [How to Create a Camera](isaacsim_sensors_camera.html#how-to-create-a-camera)
  + [How to Collect Data from a Camera](isaacsim_sensors_camera.html#how-to-collect-data-from-a-camera)
  + [Specialized Camera Types](isaacsim_sensors_camera.html#specialized-camera-types)
  + [Advanced Topics](isaacsim_sensors_camera.html#advanced-topics)
  + [Standalone Examples](isaacsim_sensors_camera.html#standalone-examples)
* [RTX Sensors](isaacsim_sensors_rtx.html)
  + [Getting Started](isaacsim_sensors_rtx.html#getting-started)
  + [Sensor Types](isaacsim_sensors_rtx.html#sensor-types)
  + [Data Collection and Materials](isaacsim_sensors_rtx.html#data-collection-and-materials)
  + [Advanced Topics](isaacsim_sensors_rtx.html#advanced-topics)
  + [Extension Architecture](isaacsim_sensors_rtx.html#extension-architecture)
  + [Important Settings](isaacsim_sensors_rtx.html#important-settings)
  + [Motion BVH](isaacsim_sensors_rtx.html#motion-bvh)
  + [Auxiliary Output Level and the GenericModelOutput RenderVar](isaacsim_sensors_rtx.html#auxiliary-output-level-and-the-genericmodeloutput-rendervar)
  + [Troubleshooting and Known Issues](isaacsim_sensors_rtx.html#troubleshooting-and-known-issues)
  + [Related Tutorials](isaacsim_sensors_rtx.html#related-tutorials)
* [Physics-based sensors](isaacsim_sensors_physics.html)
  + [Articulation joint sensors](isaacsim_sensors_physics_articulation_force.html)
  + [Contact sensor](isaacsim_sensors_physics_contact.html)
  + [Effort sensor](isaacsim_sensors_physics_effort.html)
  + [IMU sensor](isaacsim_sensors_physics_imu.html)
  + [Joint state sensor](isaacsim_sensors_physics_joint_state.html)
  + [Physics raycast sensor](isaacsim_sensors_physics_raycast.html)
* [PhysX SDK sensors](isaacsim_sensors_physx.html)
  + [PhysX SDK generic sensor](isaacsim_sensors_physx_generic.html)
  + [PhysX SDK lidar](isaacsim_sensors_physx_lidar.html)
  + [PhysX SDK lightbeam sensor](isaacsim_sensors_physx_lightbeam.html)
  + [Proximity sensor](isaacsim_sensors_physx_proximity.html)
* [Sensor Assets](../assets/usd_assets_sensors.html)
  + [Camera and Depth Sensors](../assets/usd_assets_camera_depth_sensors.html)
  + [Non-Visual Sensors](../assets/usd_assets_nonvisual_sensors.html)

---

