---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/py/source/extensions/isaacsim.sensors.experimental.rtx/docs/index.html
title: "sensors.experimental.rtx Docs"
section: "Sensors"
module: "05-python-api-quickref"
checksum: "184646f3fb2da626"
fetched: "2026-06-21T12:48:17"
---

* [isaacsim.sensors.experimental.rtx] Isaac Sim RTX Sensor Simulation

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# [isaacsim.sensors.experimental.rtx] Isaac Sim RTX Sensor Simulation

**Version**: 1.4.3

## Overview

The isaacsim.sensors.experimental.rtx extension provides experimental Python APIs for RTX-based sensor simulation in Isaac Sim, covering lidar, radar, acoustic (ultrasonic), and camera sensors. Each sensor type is split into an **authoring** class for USD prim creation and configuration, and a **runtime sensor** class for attaching annotators and retrieving data at simulation time.

### Key Components

#### Authoring classes

Authoring classes inherit from `_SensorAuthoring` (which inherits `XformPrim`) and manage the underlying USD sensor prim. They handle prim creation (or wrapping existing prims), schema application, attribute setting, and transform operations.

* [`Lidar`](#isaacsim.sensors.experimental.rtx.Lidar "isaacsim.sensors.experimental.rtx.Lidar") â Creates or wraps `OmniLidar` prims. Supports creating from known configurations via [`SUPPORTED_LIDAR_CONFIGS`](#isaacsim.sensors.experimental.rtx.SUPPORTED_LIDAR_CONFIGS "isaacsim.sensors.experimental.rtx.SUPPORTED_LIDAR_CONFIGS"). Accepts `accumulate_outputs` (default `True`).
* [`Radar`](#isaacsim.sensors.experimental.rtx.Radar "isaacsim.sensors.experimental.rtx.Radar") â Creates or wraps `OmniRadar` prims. Requires Motion BVH to be enabled (`/renderer/raytracingMotion/enabled`).
* [`Acoustic`](#isaacsim.sensors.experimental.rtx.Acoustic "isaacsim.sensors.experimental.rtx.Acoustic") â Creates or wraps `OmniAcoustic` prims. Automatically applies multi-instance schemas (`OmniSensorWpmAcousticSensorMountAPI`, `OmniSensorWpmAcousticRxGroupAPI`) when attributes with matching prefixes are provided.
* [`RtxCamera`](#isaacsim.sensors.experimental.rtx.RtxCamera "isaacsim.sensors.experimental.rtx.RtxCamera") â Creates or wraps USD Camera prims with `OmniSensorAPI` applied. Provides a `.camera` property for accessing optical parameters (focal length, clipping range, aperture, etc.).

All authoring classes accept:

* `tick_rate` â Sensor tick rate in Hz (default `0` for autotrigger).
* `aux_output_level` â Auxiliary data level for GenericModelOutput (default `"NONE"`). Valid values are modality-specific: `NONE`/`BASIC`/`EXTRA`/`FULL` for Lidar, `NONE`/`BASIC` for Radar and Acoustic. RtxCamera only supports `NONE`.
* `schemas` â Additional API schemas to apply to the prim (e.g. `["OmniLensDistortionOpenCvFisheyeAPI"]`). Supports multi-instance schemas via `"SchemaName:instanceName"` syntax.
* `attributes` â USD attributes to set on the prim after schema application.

#### Runtime sensor classes

Runtime sensor classes wrap an authoring object, create a Replicator render product, and manage annotator attachment and data retrieval.

**RTX sensors** (lidar, radar, acoustic) support `generic-model-output` and `stable-id-map` annotators:

* [`LidarSensor`](#isaacsim.sensors.experimental.rtx.LidarSensor "isaacsim.sensors.experimental.rtx.LidarSensor") â Wraps a `Lidar` object (or creates one from a path).
* [`RadarSensor`](#isaacsim.sensors.experimental.rtx.RadarSensor "isaacsim.sensors.experimental.rtx.RadarSensor") â Wraps a `Radar` object (or creates one from a path).
* [`AcousticSensor`](#isaacsim.sensors.experimental.rtx.AcousticSensor "isaacsim.sensors.experimental.rtx.AcousticSensor") â Wraps an `Acoustic` object (or creates one from a path).

**Camera sensors** support standard rendering annotators (RGB, depth, normals, segmentation, bounding boxes, etc.):

* [`CameraSensor`](#isaacsim.sensors.experimental.rtx.CameraSensor "isaacsim.sensors.experimental.rtx.CameraSensor") â Wraps a `RtxCamera` object. Requires a `resolution` parameter (`(height, width)`).
* [`TiledCameraSensor`](#isaacsim.sensors.experimental.rtx.TiledCameraSensor "isaacsim.sensors.experimental.rtx.TiledCameraSensor") â Batched rendering of multiple cameras into a single tiled texture. Supports both tiled and per-camera batched output.
* [`SingleViewDepthCameraSensor`](#isaacsim.sensors.experimental.rtx.SingleViewDepthCameraSensor "isaacsim.sensors.experimental.rtx.SingleViewDepthCameraSensor") â Extends `CameraSensor` with stereoscopic depth simulation via `OmniSensorDepthSensorSingleViewAPI`.

#### Lidar configuration registry

**Supported USD lidar assets and variants.** The package exports [`SUPPORTED_LIDAR_CONFIGS`](#isaacsim.sensors.experimental.rtx.SUPPORTED_LIDAR_CONFIGS "isaacsim.sensors.experimental.rtx.SUPPORTED_LIDAR_CONFIGS") (paths to known Isaac Sim lidar assets mapped to optional variant names) and [`SUPPORTED_LIDAR_VARIANT_SET_NAME`](#isaacsim.sensors.experimental.rtx.SUPPORTED_LIDAR_VARIANT_SET_NAME "isaacsim.sensors.experimental.rtx.SUPPORTED_LIDAR_VARIANT_SET_NAME") (expected variant set name on those prims).

#### Parser utilities

* [`parse_generic_model_output_data`](#isaacsim.sensors.experimental.rtx.parse_generic_model_output_data "isaacsim.sensors.experimental.rtx.parse_generic_model_output_data") â Decodes `generic-model-output` annotator data into a `GenericModelOutput` structure provided by the bundled `isaacsim.sensors.experimental.rtx.generic_model_output` module.
* [`parse_stable_id_map_data`](#isaacsim.sensors.experimental.rtx.parse_stable_id_map_data "isaacsim.sensors.experimental.rtx.parse_stable_id_map_data") â Decodes `stable-id-map` data into a mapping from stable object IDs to prim paths.
* `parse_object_ids` â Extracts 128-bit object IDs from a `GenericModelOutput.objId` buffer as Python ints matching the keys from `parse_stable_id_map_data`.
* `draw_annotator_data_to_image` â Converts camera annotator data to BGR NumPy arrays for visualization.

#### Auxiliary modules

The extension ships `isaacsim.sensors.experimental.rtx.generic_model_output` and `isaacsim.sensors.experimental.rtx.sensor_checker` alongside the main package. The former defines the binary layout used by `parse_generic_model_output_data`; the latter provides helpers such as `SensorCheckerUtil` and `ModelInfo` for working with supported sensor assets (see extension tests for typical usage).

#### Settings

**Kit settings contributed by this extension.** Defaults and inline comments live in `config/extension.toml` under `[settings]`. The keys cover GPU-resident lidar and radar return buffers (`app.sensors.nv.lidar.outputBufferOnGPU`, `app.sensors.nv.radar.outputBufferOnGPU`), optional non-visual material semantics from USD (`rtx.materialDb.nonVisualMaterialCSV.enabled`, `rtx.materialDb.nonVisualMaterialSemantics.prefix`), and Hydra timeline use for RTX sensor models (`rtx.rtxsensor.useHydraTimeAlways`).

### Code examples

#### Lidar

```python
from isaacsim.sensors.experimental.rtx import Lidar, LidarSensor, parse_generic_model_output_data
import isaacsim.core.experimental.utils.app as app_utils

# authoring: create a lidar prim from a known config
lidar = Lidar.create(path="/World/lidar", config="OS1", variant="OS1_REV6_32ch20hz512res",
                     aux_output_level="FULL")

# runtime: attach annotators and retrieve data
sensor = LidarSensor(lidar, annotators=["generic-model-output"])
app_utils.play(commit=True)

data, _ = sensor.get_data("generic-model-output")
gmo = parse_generic_model_output_data(data)
```

#### Radar

```python
from isaacsim.sensors.experimental.rtx import Radar, RadarSensor

radar = Radar("/World/radar", tick_rate=20.0, aux_output_level="BASIC")
sensor = RadarSensor(radar, annotators=["generic-model-output"])
```

#### Acoustic

```python
from isaacsim.sensors.experimental.rtx import Acoustic, AcousticSensor

acoustic = Acoustic(
    "/World/acoustic",
    tick_rate=30.0,
    aux_output_level="BASIC",
    attributes={
        "omni:sensor:WpmAcoustic:centerFrequency": 51200.0,
        "omni:sensor:WpmAcoustic:sensorMount:m001:position": (0.0, 0.0, 0.0),
    },
)
sensor = AcousticSensor(acoustic, annotators=["generic-model-output"])
```

#### Camera

```python
from isaacsim.sensors.experimental.rtx import RtxCamera, CameraSensor

cam = RtxCamera("/World/cam", tick_rate=30.0)
cam.camera.set_focal_lengths(24.0)
cam.camera.set_clipping_ranges(0.01, 1000.0)

sensor = CameraSensor(cam, resolution=(480, 640), annotators=["rgb", "distance_to_image_plane"])
```

#### Camera with lens distortion

```python
from isaacsim.sensors.experimental.rtx import RtxCamera, CameraSensor
from pxr import Gf

cam = RtxCamera(
    "/World/cam",
    schemas=["OmniLensDistortionOpenCvFisheyeAPI"],
    attributes={
        "omni:lensdistortion:opencvFisheye:fx": 500.0,
        "omni:lensdistortion:opencvFisheye:fy": 500.0,
        "omni:lensdistortion:opencvFisheye:cx": 640.0,
        "omni:lensdistortion:opencvFisheye:cy": 360.0,
        "omni:lensdistortion:opencvFisheye:k1": 0.05,
        "omni:lensdistortion:opencvFisheye:imageSize": Gf.Vec2i(1280, 720),
    },
)
```

### Known warnings

When `aux_output_level` is set, the following warning may appear in the log:

```python
[usdrt.population.plugin] [UsdNoticeHandler] Unhandled attribute type VtArray<std::string>
    (prim attribute: _replicator:rendervar:GenericModelOutput:channels)
```

This is harmless. The `usdrt` Fabric cache does not mirror `VtArray<std::string>` attributes, but the attribute is correctly set on the USD prim and read by the Replicator pipeline.

### Integration

Dependencies include **isaacsim.core.experimental.prims** (transform and prim utilities), **isaacsim.core.experimental.objects** (Camera prim wrapper), **omni.replicator.core** (annotators and writers), **omni.sensors.nv.lidar**, **omni.sensors.nv.radar**, **omni.sensors.nv.acoustic**, **omni.sensors.nv.common**, **omni.sensors.nv.ids**, **omni.usd.schema.omni\_sensors**, and **isaacsim.storage.native** for asset paths. Enable the extension from **Window > Extensions** and turn on `isaacsim.sensors.experimental.rtx`.

## Enable Extension

The extension can be enabled (if not already) in one of the following ways:

Command-line interface

Define the next entry as an application argument from a terminal.

```python
APP_SCRIPT.(sh|bat) --enable isaacsim.sensors.experimental.rtx
```

Experience/extension configuration

Define the next entry under `[dependencies]` in an experience (`.kit`) file or an extension configuration (`extension.toml`) file.

```python
[dependencies]
"isaacsim.sensors.experimental.rtx" = {}
```

Extension Manager UI

Open the *Window > Extensions* menu in a running application instance and search for `isaacsim.sensors.experimental.rtx`.
Then, toggle the enable control button if it is not already active.

|  |  |
| --- | --- |
| **Extension**: {{ extension\_version }} | **Documentation Generated**: Jun 05, 2026 |

### Settings

#### Settings Provided by the Extension

##### app.sensors.nv.lidar.outputBufferOnGPU

* **Default Value**: false
* **Description**: Renderer keeps Lidar return buffer on GPU for post-processing.

##### app.sensors.nv.radar.outputBufferOnGPU

* **Default Value**: false
* **Description**: Renderer keeps Radar return buffer on GPU for post-processing.

##### rtx.materialDb.nonVisualMaterialCSV.enabled

* **Default Value**: false
* **Description**: Enable non-visual materials using USD attributes.

##### rtx.materialDb.nonVisualMaterialSemantics.prefix

* **Default Value**: âomni:simready:nonvisualâ
* **Description**: Specify the non-visual material USD attribute prefix.

##### rtx.rtxsensor.useHydraTimeAlways

* **Default Value**: true
* **Description**: Use Hydra time (`omni.timeline`) in RTX sensor models. Applies only if multi-tick rendering is disabled.

## Annotators

The sensor classes included in this extension support, depending on the implementation,
a subset of the following annotators (outputs/data products generated by the sensors):

### Standard Annotators

Annotatorâs description and outputs are listed in the table below.

| Annotator | Description | Type / Dtype |
| --- | --- | --- |
| `"generic-model-output"` | Bytes encoding a `GenericModelOutput` structure. | `wp.array` / `uint8` |
| `"stable-id-map"` | Bytes encoding a Stable ID map (mapping of stable object IDs to prim paths). | `wp.array` / `uint8` |

## Python API

Warning

**The API featured in this extension is experimental and subject to change without deprecation cycles.**
Although we will try to maintain backward compatibility in the event of a change, it may not always be possible.

The following table summarizes the available classes.

authoring (USD prim wrappers)

|  |  |
| --- | --- |
| [`Lidar`](#isaacsim.sensors.experimental.rtx.Lidar "isaacsim.sensors.experimental.rtx.Lidar") | High level class for creating/wrapping USD OmniLidar prims. |
| [`Radar`](#isaacsim.sensors.experimental.rtx.Radar "isaacsim.sensors.experimental.rtx.Radar") | High level class for creating/wrapping USD OmniRadar prims. |
| [`Acoustic`](#isaacsim.sensors.experimental.rtx.Acoustic "isaacsim.sensors.experimental.rtx.Acoustic") | High level class for creating/wrapping USD OmniAcoustic prims. |
| [`RtxCamera`](#isaacsim.sensors.experimental.rtx.RtxCamera "isaacsim.sensors.experimental.rtx.RtxCamera") | High level class for creating/wrapping USD Camera prims as RTX sensors. |
| [`StructuredLightCamera`](#isaacsim.sensors.experimental.rtx.StructuredLightCamera "isaacsim.sensors.experimental.rtx.StructuredLightCamera") | Structured light camera sensor: an [`RtxCamera`](#isaacsim.sensors.experimental.rtx.RtxCamera "isaacsim.sensors.experimental.rtx.RtxCamera") with cycling projectors. |

sensors (runtime)

|  |  |
| --- | --- |
| [`LidarSensor`](#isaacsim.sensors.experimental.rtx.LidarSensor "isaacsim.sensors.experimental.rtx.LidarSensor") | Runtime class for operating a single RTX-based lidar sensor. |
| [`RadarSensor`](#isaacsim.sensors.experimental.rtx.RadarSensor "isaacsim.sensors.experimental.rtx.RadarSensor") | Runtime class for operating a single RTX-based radar sensor. |
| [`AcousticSensor`](#isaacsim.sensors.experimental.rtx.AcousticSensor "isaacsim.sensors.experimental.rtx.AcousticSensor") | Runtime class for operating a single RTX-based acoustic sensor. |
| [`CameraSensor`](#isaacsim.sensors.experimental.rtx.CameraSensor "isaacsim.sensors.experimental.rtx.CameraSensor") | High level class for creating/wrapping and operating single camera sensor. |
| [`SingleViewDepthCameraSensor`](#isaacsim.sensors.experimental.rtx.SingleViewDepthCameraSensor "isaacsim.sensors.experimental.rtx.SingleViewDepthCameraSensor") | High level class for creating/wrapping and operating single view depth camera sensor. |
| [`TiledCameraSensor`](#isaacsim.sensors.experimental.rtx.TiledCameraSensor "isaacsim.sensors.experimental.rtx.TiledCameraSensor") | High level class for creating/wrapping and operating tiled (batched) camera sensors. |

utils

|  |  |
| --- | --- |
| [`parse_generic_model_output_data`](#isaacsim.sensors.experimental.rtx.parse_generic_model_output_data "isaacsim.sensors.experimental.rtx.parse_generic_model_output_data") | Parse generic model output structure from annotator data. |
| [`parse_stable_id_map_data`](#isaacsim.sensors.experimental.rtx.parse_stable_id_map_data "isaacsim.sensors.experimental.rtx.parse_stable_id_map_data") | Parse Stable ID Map data from annotator data. |

lidar configuration

* [`SUPPORTED_LIDAR_CONFIGS`](#isaacsim.sensors.experimental.rtx.SUPPORTED_LIDAR_CONFIGS "isaacsim.sensors.experimental.rtx.SUPPORTED_LIDAR_CONFIGS")
* [`SUPPORTED_LIDAR_VARIANT_SET_NAME`](#isaacsim.sensors.experimental.rtx.SUPPORTED_LIDAR_VARIANT_SET_NAME "isaacsim.sensors.experimental.rtx.SUPPORTED_LIDAR_VARIANT_SET_NAME")

### Authoring

*class* Lidar( : *path: str*, : *\**, : *accumulate\_outputs: bool | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = True*, : *aux\_output\_level: str = 'NONE'*, : *tick\_rate: float | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *schemas: list[str] | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *attributes: dict[str, Any] | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *positions: list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *translations: list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *orientations: list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *scales: list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *reset\_xform\_op\_properties: bool = True*, )
:   Bases: `_SensorAuthoring`

    High level class for creating/wrapping USD OmniLidar prims.

    This class uses `omni.replicator.core.functional.create.omni_lidar` to create new lidar prims,
    which handles defining the prim, applying schemas, and setting attributes.

    Note

    This class creates or wraps (one of both) USD OmniLidar prims according to the following rules:

    * If the prim path exists, a wrapper is placed over the USD OmniLidar prim.
    * If the prim path does not exist, a USD OmniLidar prim is created at the path and a wrapper is placed over it.

    Parameters:
    :   * **path** â Single path to existing or non-existing (one of both) USD OmniLidar prim.
          Can include regular expression for matching a prim.
        * **accumulate\_outputs** â Set the `omni:sensor:Core:accumulateOutputs` attribute on the OmniLidar prim.
          When `True` (the default), the lidar model accumulates a full scan before generating an output.
          When `None`, the attribute is left untouched on the prim (useful for preserving values
          authored on a USD asset that is being wrapped).
        * **aux\_output\_level** â Auxiliary data level for GenericModelOutput. Valid values:
          `"NONE"` (default), `"BASIC"`, `"EXTRA"`, `"FULL"`.
        * **tick\_rate** â Sensor tick rate in Hz. When `None` (the default), the primâs
          `omni:sensor:tickRate` attribute is left untouched, so any value already authored on
          the prim (e.g. from a USD asset) is preserved. For newly-created prims, the
          `OmniSensorGenericLidarCoreAPI` schema default of `10` Hz applies.
        * **schemas** â Additional API schemas to apply to the prim.
        * **attributes** â Attributes to set on the OmniLidar prim.
        * **positions** â Positions in the world frame (shape `(N, 3)`).
          If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
        * **translations** â Translations in the local frame (shape `(N, 3)`).
          If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
        * **orientations** â Orientations in the world frame (shape `(N, 4)`, quaternion `wxyz`).
          If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
        * **scales** â Scales to be applied to the prims (shape `(N, 3)`).
          If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
        * **reset\_xform\_op\_properties** â Whether to reset the transformation operation attributes of the prims to a standard set.
          See [`reset_xform_op_properties()`](#isaacsim.sensors.experimental.rtx.Lidar.reset_xform_op_properties "isaacsim.sensors.experimental.rtx.Lidar.reset_xform_op_properties") for more details.

    Raises:
    :   * **ValueError** â If no prim is found matching the specified path.
        * **ValueError** â If the input argument refers to more than one prim.

    Example:

    ```python
    >>> from isaacsim.sensors.experimental.rtx import Lidar
    >>>
    >>> # given a USD stage with the OmniLidar prim: /World/prim_0
    >>> lidar = Lidar("/World/prim_0")
    ```

    apply\_visual\_materials( : *materials: type['VisualMaterial'] | list[type['VisualMaterial']]*, : *\**, : *weaker\_than\_descendants: bool | list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *indices: int | list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, ) → [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None")
    :   Apply visual materials to the prims, and optionally, to their descendants.

        Backends: usd.

        Parameters:
        :   * **materials** â Visual materials to be applied to the prims (shape `(N,)`).
              If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
            * **weaker\_than\_descendants** â Boolean flags to indicate whether descendant materials should be overridden (shape `(N, 1)`).
              If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
            * **indices** â Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

        Raises:
        :   **AssertionError** â Wrapped prims are not valid.

        Example:

        ```python
        >>> from isaacsim.core.experimental.materials import OmniGlassMaterial
        >>>
        >>> # create a dark-red glass visual material
        >>> material = OmniGlassMaterial("/World/material/glass")
        >>> material.set_input_values("glass_ior", [1.25])
        >>> material.set_input_values("depth", [0.001])
        >>> material.set_input_values("thin_walled", [False])
        >>> material.set_input_values("glass_color", [0.5, 0.0, 0.0])
        >>>
        >>> prims.apply_visual_materials(material)
        ```

    *static* create( : *path: str*, : *\**, : *accumulate\_outputs: bool | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *aux\_output\_level: str = 'NONE'*, : *tick\_rate: float | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *schemas: list[str] | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *attributes: dict[str, Any] | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *positions: list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *translations: list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *orientations: list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *scales: list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *reset\_xform\_op\_properties: bool = True*, : *config: str | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *usd\_path: str | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *variant: str | dict[str, str] | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, ) → [Lidar](#isaacsim.sensors.experimental.rtx.Lidar "isaacsim.sensors.experimental.rtx.Lidar")
    :   Create a Lidar instance from a config name or USD file path.

        Parameters:
        :   * **path** â Single path to existing or non-existing (one of both) USD OmniLidar prim.
            * **accumulate\_outputs** â Set the `omni:sensor:Core:accumulateOutputs` attribute on the OmniLidar prim.
              When `None` (the default), the attribute authored on the loaded asset is preserved.
              Pass `True`/`False` to override.
            * **aux\_output\_level** â Auxiliary output level to author on the OmniLidar prim.
            * **tick\_rate** â Sensor tick rate in Hz. When `None` (the default), the assetâs
              `omni:sensor:tickRate` attribute is preserved. Pass an explicit value to override.
            * **schemas** â Optional schema API names to apply to the created OmniLidar prim.
            * **attributes** â Attributes to set on the OmniLidar prim.
            * **positions** â Positions in the world frame (shape `(N, 3)`).
            * **translations** â Translations in the local frame (shape `(N, 3)`).
            * **orientations** â Orientations in the world frame (shape `(N, 4)`, quaternion `wxyz`).
            * **scales** â Scales to be applied to the prims (shape `(N, 3)`).
            * **reset\_xform\_op\_properties** â Whether to reset the transformation operation attributes of the prims.
            * **config** â Configuration name for the sensor (from `SUPPORTED_LIDAR_CONFIGS`).
            * **usd\_path** â Path to a USD file containing the sensor asset.
            * **variant** â Variant name for the sensor configuration. Nested variants
              supported via dictionary; pairs applied in dict insertion order,
              so outer variant sets must come first.

        Returns:
        :   Lidar instance.

        Raises:
        :   * **ValueError** â If both âconfigâ and âusd\_pathâ are provided.
            * **ValueError** â If the specified config is not found.

        Example:

        ```python
        >>> from isaacsim.sensors.experimental.rtx import Lidar
        >>>
        >>> lidar = Lidar.create(
        ...     path="/World/lidar",
        ...     config="OS1",
        ...     variant="OS1_REV6_32ch20hz512res",
        ... )
        ```

    *static* ensure\_api( : *prims: list[Usd.Prim]*, : *api: type*, : *\*args: Any*, : *\*\*kwargs: Any*, ) → list[type['UsdAPISchemaBase']]
    :   Ensure that all prims have the specified API schema applied.

        Backends: usd.

        If a prim doesnât have the API schema, it will be applied.
        If it already has it, the existing API schema will be returned.

        Parameters:
        :   * **prims** â List of USD Prims to ensure API schema on.
            * **api** â The API schema type to ensure.
            * **\*args** â Additional positional arguments passed to API schema when applying it.
            * **\*\*kwargs** â Additional keyword arguments passed to API schema when applying it.

        Returns:
        :   List of API schema objects, one for each input prim.

        Example:

        ```python
        >>> import isaacsim.core.experimental.utils.prim as prim_utils
        >>> from pxr import UsdPhysics
        >>> from isaacsim.core.experimental.prims import Prim
        >>>
        >>> # given a USD stage with 3 prims at paths /World/prim_0, /World/prim_1, /World/prim_2,
        >>> # ensure all prims have physics API schema
        >>> usd_prims = [prim_utils.get_prim_at_path(f"/World/prim_{i}") for i in range(3)]
        >>> physics_apis = Prim.ensure_api(usd_prims, UsdPhysics.RigidBodyAPI)
        ```

    get\_applied\_visual\_materials( : *\**, : *indices: int | list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, ) → list[type['VisualMaterial'] | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None")]
    :   Get the applied visual materials.

        Backends: usd.

        Parameters:
        :   **indices** â Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

        Returns:
        :   List of applied visual materials (shape `(N,)`). If a prim does not have a material, `None` is returned.

        Raises:
        :   **AssertionError** â Wrapped prims are not valid.

        Example:

        ```python
        >>> # get the applied visual material of the last wrapped prim
        >>> prims.get_applied_visual_materials(indices=[2])[0]
        <isaacsim.core.experimental.materials.impl.visual_materials.omni_glass.OmniGlassMaterial object at 0x...>
        ```

    get\_default\_state( : *\**, : *indices: int | list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, ) → tuple[wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None"), wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None")]
    :   Get the default state (positions and orientations) of the prims.

        Backends: usd.

        Parameters:
        :   **indices** â Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

        Returns:
        :   Two-elements tuple. 1) The default positions in the world frame (shape `(N, 3)`).
            2) The default orientations in the world frame (shape `(N, 4)`, quaternion `wxyz`).
            If the default state is not set using the [`set_default_state()`](#isaacsim.sensors.experimental.rtx.Lidar.set_default_state "isaacsim.sensors.experimental.rtx.Lidar.set_default_state") method, `None` is returned.

        Raises:
        :   * **AssertionError** â Wrapped prims are not valid.
            * **AssertionError** â If prims are non-root articulation links.

    get\_local\_poses( : *\**, : *indices: int | list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, ) → tuple[wp.array, wp.array]
    :   Get the poses (translations and orientations) in the local frame of the prims.

        Backends: usd, usdrt, fabric.

        Parameters:
        :   **indices** â Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

        Returns:
        :   Two-elements tuple. 1) The translations in the local frame (shape `(N, 3)`).
            2) The orientations in the local frame (shape `(N, 4)`, quaternion `wxyz`).

        Raises:
        :   **AssertionError** â Wrapped prims are not valid.

        Example:

        ```python
        >>> # get the local poses of all prims
        >>> translations, orientations = prims.get_local_poses()
        >>> translations.shape, orientations.shape
        ((3, 3), (3, 4))
        >>>
        >>> # get the local pose of the first prim
        >>> translations, orientations = prims.get_local_poses(indices=[0])
        >>> translations.shape, orientations.shape
        ((1, 3), (1, 4))
        ```

    get\_local\_scales( : *\**, : *indices: int | list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, ) → wp.array
    :   Get the local scales of the prims.

        Backends: usd, usdrt, fabric.

        Parameters:
        :   **indices** â Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

        Returns:
        :   Scales of the prims (shape `(N, 3)`).

        Raises:
        :   **AssertionError** â Wrapped prims are not valid.

        Example:

        ```python
        >>> # get local scales of all prims
        >>> scales = prims.get_local_scales()
        >>> scales.shape
        (3, 3)
        ```

    get\_visibilities( : *\**, : *indices: int | list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, ) → wp.array
    :   Get the visibility state (whether prims are visible or invisible during rendering) of the prims.

        Backends: usd.

        Parameters:
        :   **indices** â Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

        Returns:
        :   Boolean flags indicating the visibility state (shape `(N, 1)`).

        Raises:
        :   **AssertionError** â Wrapped prims are not valid.

        Example:

        ```python
        >>> # get the visibility states of all prims
        >>> visibilities = prims.get_visibilities()
        >>> print(visibilities)
        [[ True] [ True] [ True]]
        >>>
        >>> # get the visibility states of the first and last prims
        >>> visibilities = prims.get_visibilities(indices=[0, 2])
        >>> print(visibilities)
        [[ True] [ True]]
        ```

    get\_world\_poses( : *\**, : *indices: int | list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, ) → tuple[wp.array, wp.array]
    :   Get the poses (positions and orientations) in the world frame of the prims.

        Backends: usd, usdrt, fabric.

        Parameters:
        :   **indices** â Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

        Returns:
        :   Two-elements tuple. 1) The positions in the world frame (shape `(N, 3)`).
            2) The orientations in the world frame (shape `(N, 4)`, quaternion `wxyz`).

        Raises:
        :   **AssertionError** â Wrapped prims are not valid.

        Example:

        ```python
        >>> # get the world poses of all prims
        >>> positions, orientations = prims.get_world_poses()
        >>> positions.shape, orientations.shape
        ((3, 3), (3, 4))
        >>>
        >>> # get the world pose of the first prim
        >>> positions, orientations = prims.get_world_poses(indices=[0])
        >>> positions.shape, orientations.shape
        ((1, 3), (1, 4))
        ```

    reset\_to\_default\_state( : *\**, : *warn\_on\_non\_default\_state: bool = False*, ) → [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None")
    :   Reset the prims to the specified default state.

        Backends: usd, usdrt, fabric.

        This method applies the default state defined using the [`set_default_state()`](#isaacsim.sensors.experimental.rtx.Lidar.set_default_state "isaacsim.sensors.experimental.rtx.Lidar.set_default_state") method.

        Note

        This method *teleports* prims to the specified default state (positions and orientations).

        Warning

        This method has no effect on non-root articulation links or when no default state is set.
        In this case, a warning message is logged if `warn_on_non_default_state` is `True`.

        Parameters:
        :   **warn\_on\_non\_default\_state** â Whether to log a warning message when no default state is set.

        Raises:
        :   **AssertionError** â Wrapped prims are not valid.

        Example:

        ```python
        >>> # get default state (no default state set at this point)
        >>> prims.get_default_state()
        (None, None)
        >>>
        >>> # set default state
        >>> # - random positions for each prim
        >>> # - same fixed orientation for all prim
        >>> positions = np.random.uniform(low=-1, high=1, size=(3, 3))
        >>> prims.set_default_state(positions, orientations=[1.0, 0.0, 0.0, 0.0])
        >>>
        >>> # get default state (default state is set)
        >>> prims.get_default_state()
        (array(shape=(3, 3), dtype=float32), array(shape=(3, 4), dtype=float32))
        >>>
        >>> # reset prims to default state
        >>> prims.reset_to_default_state()
        ```

    reset\_xform\_op\_properties() → [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None")
    :   Reset the transformation operation attributes of the prims to a standard set.

        Backends: usd.

        USD Xform schema supports a wide range of transformation operation types.
        This method ensures that each wrapped prim has only the following transformations in the specified order.
        Any other transformation operations are removed, so they are not consumed.

        1. `xformOp:translate` (double precision)
        2. `xformOp:orient` (double precision)
        3. `xformOp:scale` (double precision)

        Note

        This method preserves the poses of the prims in the world frame while reorganizing the transformation operations.

        Raises:
        :   **AssertionError** â Wrapped prims are not valid.

        Example:

        ```python
        >>> # reset transform operations of all prims
        >>> prims.reset_xform_op_properties()
        >>>
        >>> # verify transform operations of the first wrapped prim
        >>> prims.prims[0].GetPropertyNames()
        [... 'xformOp:orient', 'xformOp:scale', 'xformOp:translate', 'xformOpOrder']
        ```

    *static* resolve\_paths( : *paths: str | list[str]*, : *raise\_on\_mixed\_paths: bool = True*, ) → tuple[list[str], list[str]]
    :   Resolve paths to prims in the stage to get existing and non-existing paths.

        Backends: usd.

        Parameters:
        :   * **paths** â Single path or list of paths to USD prims. Paths may contain regular expressions to match multiple prims.
            * **raise\_on\_mixed\_paths** â Whether to raise an error if resulting paths are mixed or invalid.

        Returns:
        :   Two-elements tuple. 1) List of existing paths. 2) List of non-existing paths.

        Raises:
        :   **ValueError** â If resulting paths are mixed or invalid and `raise_on_mixed_paths` is True.

    set\_default\_state( : *positions: list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *orientations: list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *\**, : *indices: int | list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, ) → [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None")
    :   Set the default state (positions and orientations) of the prims.

        Backends: usd.

        Hint

        Prims can be reset to their default state by calling the [`reset_to_default_state()`](#isaacsim.sensors.experimental.rtx.Lidar.reset_to_default_state "isaacsim.sensors.experimental.rtx.Lidar.reset_to_default_state") method.

        Parameters:
        :   * **positions** â Default positions in the world frame (shape `(N, 3)`).
              If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
            * **orientations** â Default orientations in the world frame (shape `(N, 4)`, quaternion `wxyz`).
              If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
            * **indices** â Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

        Raises:
        :   * **AssertionError** â If neither positions nor orientations are specified.
            * **AssertionError** â Wrapped prims are not valid.
            * **AssertionError** â If prims are non-root articulation links.

    set\_local\_poses( : *translations: list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *orientations: list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *\**, : *indices: int | list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, ) → [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None")
    :   Set the poses (translations and orientations) in the local frame of the prims.

        Backends: usd, usdrt, fabric.

        Note

        This method *teleports* prims to the specified poses.

        Parameters:
        :   * **translations** â Translations in the local frame (shape `(N, 3)`).
              If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
            * **orientations** â Orientations in the local frame (shape `(N, 4)`, quaternion `wxyz`).
              If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
            * **indices** â Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

        Raises:
        :   * **AssertionError** â If neither translations nor orientations are specified.
            * **AssertionError** â Wrapped prims are not valid.

        Example:

        ```python
        >>> # set random poses for all prims
        >>> translations = np.random.uniform(low=-1, high=1, size=(3, 3))
        >>> orientations = np.random.randn(3, 4)
        >>> orientations = orientations / np.linalg.norm(orientations, axis=-1, keepdims=True)  # normalize quaternions
        >>> prims.set_local_poses(translations, orientations)
        ```

    set\_local\_scales( : *scales: list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *\**, : *indices: int | list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, ) → [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None")
    :   Set the local scales of the prims.

        Backends: usd, usdrt, fabric.

        Parameters:
        :   * **scales** â Scales to be applied to the prims (shape `(N, 3)`).
              If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
            * **indices** â Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

        Raises:
        :   **AssertionError** â Wrapped prims are not valid.

        Example:

        ```python
        >>> # set random positive scales for all prims
        >>> scales = np.random.uniform(low=0.5, high=1.5, size=(3, 3))
        >>> prims.set_local_scales(scales)
        ```

    set\_visibilities( : *visibilities: bool | list | np.ndarray | wp.array*, : *\**, : *indices: int | list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, ) → [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None")
    :   Set the visibility state (whether prims are visible or invisible during rendering) of the prims.

        Backends: usd.

        Parameters:
        :   * **visibilities** â Boolean flags to set the visibility state (shape `(N, 1)`).
              If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
            * **indices** â Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

        Raises:
        :   **AssertionError** â Wrapped prims are not valid.

        Example:

        ```python
        >>> # make all prims invisible
        >>> prims.set_visibilities([False])
        >>>
        >>> # make first and last prims invisible
        >>> prims.set_visibilities([True])  # restore visibility from previous call
        >>> prims.set_visibilities([False], indices=[0, 2])
        ```

    set\_world\_poses( : *positions: list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *orientations: list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *\**, : *indices: int | list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, ) → [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None")
    :   Set the poses (positions and orientations) in the world frame of the prims.

        Backends: usd, usdrt, fabric.

        Note

        This method *teleports* prims to the specified poses.

        Parameters:
        :   * **positions** â Positions in the world frame (shape `(N, 3)`).
              If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
            * **orientations** â Orientations in the world frame (shape `(N, 4)`, quaternion `wxyz`).
              If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
            * **indices** â Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

        Raises:
        :   * **AssertionError** â If neither positions nor orientations are specified.
            * **AssertionError** â Wrapped prims are not valid.

        Example:

        ```python
        >>> # set random poses for all prims
        >>> positions = np.random.uniform(low=-1, high=1, size=(3, 3))
        >>> orientations = np.random.randn(3, 4)
        >>> orientations = orientations / np.linalg.norm(orientations, axis=-1, keepdims=True)  # normalize quaternions
        >>> prims.set_world_poses(positions, orientations)
        ```

    *property* aux\_output\_level*: str*
    :   The auxiliary output level configured on the GenericModelOutput RenderVar.

        Returns:
        :   The configured level (e.g. `"NONE"`, `"BASIC"`, `"EXTRA"`, `"FULL"`).

    *property* is\_non\_root\_articulation\_link*: bool*
    :   Indicate if the wrapped prims are a non-root link in an articulation tree.

        Backends: usd.

        Warning

        Transformation of the poses of non-root links in an articulation tree are not supported.

        Returns:
        :   Whether the prims are a non-root link in an articulation tree.

    *property* paths*: list[str]*
    :   Prim paths in the stage encapsulated by the wrapper.

        Returns:
        :   List of prim paths as strings.

        Example:

        ```python
        >>> prims.paths
        ['/World/prim_0', '/World/prim_1', '/World/prim_2']
        ```

    *property* prims*: list[pxr.Usd.Prim]*
    :   USD Prim objects encapsulated by the wrapper.

        Returns:
        :   List of USD Prim objects.

        Example:

        ```python
        >>> prims.prims
        [Usd.Prim(</World/prim_0>), Usd.Prim(</World/prim_1>), Usd.Prim(</World/prim_2>)]
        ```

    *property* valid*: bool*
    :   Whether all prims in the wrapper are valid.

        Returns:
        :   True if all prim paths specified in the wrapper correspond to valid prims in stage, False otherwise.

        Example:

        ```python
        >>> prims.valid
        True
        ```

*class* Radar( : *path: str*, : *\**, : *aux\_output\_level: str = 'NONE'*, : *tick\_rate: float | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *schemas: list[str] | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *attributes: dict[str, Any] | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *positions: list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *translations: list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *orientations: list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *scales: list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *reset\_xform\_op\_properties: bool = True*, )
:   Bases: `_SensorAuthoring`

    High level class for creating/wrapping USD OmniRadar prims.

    This class uses `omni.replicator.core.functional.create.omni_radar` to create new radar prims,
    which handles defining the prim, applying schemas, and setting attributes.

    Note

    RTX Radar requires Motion BVH to be enabled. The setting
    `/renderer/raytracingMotion/enabled` must be set to `True` before creating a radar prim.

    Note

    This class creates or wraps (one of both) USD OmniRadar prims according to the following rules:

    * If the prim path exists, a wrapper is placed over the USD OmniRadar prim.
    * If the prim path does not exist, a USD OmniRadar prim is created at the path and a wrapper is placed over it.

    Parameters:
    :   * **path** â Single path to existing or non-existing (one of both) USD OmniRadar prim.
          Can include regular expression for matching a prim.
        * **aux\_output\_level** â Auxiliary data level for GenericModelOutput. Valid values:
          `"NONE"` (default), `"BASIC"`.
        * **tick\_rate** â Sensor tick rate in Hz. A value of `0` (the default) enables autotrigger mode.
        * **attributes** â Attributes to set on the OmniRadar prim.
        * **positions** â Positions in the world frame (shape `(N, 3)`).
          If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
        * **translations** â Translations in the local frame (shape `(N, 3)`).
          If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
        * **orientations** â Orientations in the world frame (shape `(N, 4)`, quaternion `wxyz`).
          If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
        * **scales** â Scales to be applied to the prims (shape `(N, 3)`).
          If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
        * **reset\_xform\_op\_properties** â Whether to reset the transformation operation attributes of the prims to a standard set.
          See [`reset_xform_op_properties()`](#isaacsim.sensors.experimental.rtx.Radar.reset_xform_op_properties "isaacsim.sensors.experimental.rtx.Radar.reset_xform_op_properties") for more details.

    Raises:
    :   * **ValueError** â If no prim is found matching the specified path.
        * **ValueError** â If the input argument refers to more than one prim.
        * **RuntimeError** â If Motion BVH is not enabled when creating a new radar prim.

    Example:

    ```python
    >>> from isaacsim.sensors.experimental.rtx import Radar
    >>>
    >>> # given a USD stage with the OmniRadar prim: /World/prim_0
    >>> radar = Radar("/World/prim_0")
    ```

    apply\_visual\_materials( : *materials: type['VisualMaterial'] | list[type['VisualMaterial']]*, : *\**, : *weaker\_than\_descendants: bool | list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *indices: int | list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, ) → [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None")
    :   Apply visual materials to the prims, and optionally, to their descendants.

        Backends: usd.

        Parameters:
        :   * **materials** â Visual materials to be applied to the prims (shape `(N,)`).
              If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
            * **weaker\_than\_descendants** â Boolean flags to indicate whether descendant materials should be overridden (shape `(N, 1)`).
              If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
            * **indices** â Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

        Raises:
        :   **AssertionError** â Wrapped prims are not valid.

        Example:

        ```python
        >>> from isaacsim.core.experimental.materials import OmniGlassMaterial
        >>>
        >>> # create a dark-red glass visual material
        >>> material = OmniGlassMaterial("/World/material/glass")
        >>> material.set_input_values("glass_ior", [1.25])
        >>> material.set_input_values("depth", [0.001])
        >>> material.set_input_values("thin_walled", [False])
        >>> material.set_input_values("glass_color", [0.5, 0.0, 0.0])
        >>>
        >>> prims.apply_visual_materials(material)
        ```

    *static* create( : *path: str*, : *\**, : *aux\_output\_level: str = 'NONE'*, : *tick\_rate: float | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *attributes: dict[str, Any] | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *positions: list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *translations: list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *orientations: list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *scales: list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *reset\_xform\_op\_properties: bool = True*, : *config: str | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *usd\_path: str | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *variant: str | dict[str, str] | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, ) → [Radar](#isaacsim.sensors.experimental.rtx.Radar "isaacsim.sensors.experimental.rtx.Radar")
    :   Create a Radar instance from a config name or USD file path.

        Parameters:
        :   * **path** â Single path to existing or non-existing (one of both) USD OmniRadar prim.
            * **aux\_output\_level** â Auxiliary data level for GenericModelOutput. Valid values:
              `"NONE"` (default), `"BASIC"`.
            * **tick\_rate** â Sensor tick rate in Hz. When `None` (the default), the assetâs
              `omni:sensor:tickRate` attribute is preserved. Pass an explicit value to override.
            * **attributes** â Attributes to set on the OmniRadar prim.
            * **positions** â Positions in the world frame (shape `(N, 3)`).
            * **translations** â Translations in the local frame (shape `(N, 3)`).
            * **orientations** â Orientations in the world frame (shape `(N, 4)`, quaternion `wxyz`).
            * **scales** â Scales to be applied to the prims (shape `(N, 3)`).
            * **reset\_xform\_op\_properties** â Whether to reset the transformation operation attributes of the prims.
            * **config** â Configuration name for the sensor (from `SUPPORTED_RADAR_CONFIGS`).
            * **usd\_path** â Path to a USD file containing the sensor asset.
            * **variant** â Variant name for the sensor configuration. Nested variants
              supported via dictionary; pairs applied in dict insertion order,
              so outer variant sets must come first.

        Returns:
        :   Radar instance.

        Raises:
        :   * **ValueError** â If both âconfigâ and âusd\_pathâ are provided.
            * **ValueError** â If the specified config is not found.
            * **RuntimeError** â If Motion BVH is not enabled.

        Example:

        ```python
        >>> from isaacsim.sensors.experimental.rtx import Radar
        >>>
        >>> radar = Radar.create(path="/World/radar", config="IWRL6432AOP")
        ```

    *static* ensure\_api( : *prims: list[Usd.Prim]*, : *api: type*, : *\*args: Any*, : *\*\*kwargs: Any*, ) → list[type['UsdAPISchemaBase']]
    :   Ensure that all prims have the specified API schema applied.

        Backends: usd.

        If a prim doesnât have the API schema, it will be applied.
        If it already has it, the existing API schema will be returned.

        Parameters:
        :   * **prims** â List of USD Prims to ensure API schema on.
            * **api** â The API schema type to ensure.
            * **\*args** â Additional positional arguments passed to API schema when applying it.
            * **\*\*kwargs** â Additional keyword arguments passed to API schema when applying it.

        Returns:
        :   List of API schema objects, one for each input prim.

        Example:

        ```python
        >>> import isaacsim.core.experimental.utils.prim as prim_utils
        >>> from pxr import UsdPhysics
        >>> from isaacsim.core.experimental.prims import Prim
        >>>
        >>> # given a USD stage with 3 prims at paths /World/prim_0, /World/prim_1, /World/prim_2,
        >>> # ensure all prims have physics API schema
        >>> usd_prims = [prim_utils.get_prim_at_path(f"/World/prim_{i}") for i in range(3)]
        >>> physics_apis = Prim.ensure_api(usd_prims, UsdPhysics.RigidBodyAPI)
        ```

    get\_applied\_visual\_materials( : *\**, : *indices: int | list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, ) → list[type['VisualMaterial'] | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None")]
    :   Get the applied visual materials.

        Backends: usd.

        Parameters:
        :   **indices** â Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

        Returns:
        :   List of applied visual materials (shape `(N,)`). If a prim does not have a material, `None` is returned.

        Raises:
        :   **AssertionError** â Wrapped prims are not valid.

        Example:

        ```python
        >>> # get the applied visual material of the last wrapped prim
        >>> prims.get_applied_visual_materials(indices=[2])[0]
        <isaacsim.core.experimental.materials.impl.visual_materials.omni_glass.OmniGlassMaterial object at 0x...>
        ```

    get\_default\_state( : *\**, : *indices: int | list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, ) → tuple[wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None"), wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None")]
    :   Get the default state (positions and orientations) of the prims.

        Backends: usd.

        Parameters:
        :   **indices** â Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

        Returns:
        :   Two-elements tuple. 1) The default positions in the world frame (shape `(N, 3)`).
            2) The default orientations in the world frame (shape `(N, 4)`, quaternion `wxyz`).
            If the default state is not set using the [`set_default_state()`](#isaacsim.sensors.experimental.rtx.Radar.set_default_state "isaacsim.sensors.experimental.rtx.Radar.set_default_state") method, `None` is returned.

        Raises:
        :   * **AssertionError** â Wrapped prims are not valid.
            * **AssertionError** â If prims are non-root articulation links.

    get\_local\_poses( : *\**, : *indices: int | list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, ) → tuple[wp.array, wp.array]
    :   Get the poses (translations and orientations) in the local frame of the prims.

        Backends: usd, usdrt, fabric.

        Parameters:
        :   **indices** â Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

        Returns:
        :   Two-elements tuple. 1) The translations in the local frame (shape `(N, 3)`).
            2) The orientations in the local frame (shape `(N, 4)`, quaternion `wxyz`).

        Raises:
        :   **AssertionError** â Wrapped prims are not valid.

        Example:

        ```python
        >>> # get the local poses of all prims
        >>> translations, orientations = prims.get_local_poses()
        >>> translations.shape, orientations.shape
        ((3, 3), (3, 4))
        >>>
        >>> # get the local pose of the first prim
        >>> translations, orientations = prims.get_local_poses(indices=[0])
        >>> translations.shape, orientations.shape
        ((1, 3), (1, 4))
        ```

    get\_local\_scales( : *\**, : *indices: int | list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, ) → wp.array
    :   Get the local scales of the prims.

        Backends: usd, usdrt, fabric.

        Parameters:
        :   **indices** â Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

        Returns:
        :   Scales of the prims (shape `(N, 3)`).

        Raises:
        :   **AssertionError** â Wrapped prims are not valid.

        Example:

        ```python
        >>> # get local scales of all prims
        >>> scales = prims.get_local_scales()
        >>> scales.shape
        (3, 3)
        ```

    get\_visibilities( : *\**, : *indices: int | list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, ) → wp.array
    :   Get the visibility state (whether prims are visible or invisible during rendering) of the prims.

        Backends: usd.

        Parameters:
        :   **indices** â Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

        Returns:
        :   Boolean flags indicating the visibility state (shape `(N, 1)`).

        Raises:
        :   **AssertionError** â Wrapped prims are not valid.

        Example:

        ```python
        >>> # get the visibility states of all prims
        >>> visibilities = prims.get_visibilities()
        >>> print(visibilities)
        [[ True] [ True] [ True]]
        >>>
        >>> # get the visibility states of the first and last prims
        >>> visibilities = prims.get_visibilities(indices=[0, 2])
        >>> print(visibilities)
        [[ True] [ True]]
        ```

    get\_world\_poses( : *\**, : *indices: int | list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, ) → tuple[wp.array, wp.array]
    :   Get the poses (positions and orientations) in the world frame of the prims.

        Backends: usd, usdrt, fabric.

        Parameters:
        :   **indices** â Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

        Returns:
        :   Two-elements tuple. 1) The positions in the world frame (shape `(N, 3)`).
            2) The orientations in the world frame (shape `(N, 4)`, quaternion `wxyz`).

        Raises:
        :   **AssertionError** â Wrapped prims are not valid.

        Example:

        ```python
        >>> # get the world poses of all prims
        >>> positions, orientations = prims.get_world_poses()
        >>> positions.shape, orientations.shape
        ((3, 3), (3, 4))
        >>>
        >>> # get the world pose of the first prim
        >>> positions, orientations = prims.get_world_poses(indices=[0])
        >>> positions.shape, orientations.shape
        ((1, 3), (1, 4))
        ```

    reset\_to\_default\_state( : *\**, : *warn\_on\_non\_default\_state: bool = False*, ) → [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None")
    :   Reset the prims to the specified default state.

        Backends: usd, usdrt, fabric.

        This method applies the default state defined using the [`set_default_state()`](#isaacsim.sensors.experimental.rtx.Radar.set_default_state "isaacsim.sensors.experimental.rtx.Radar.set_default_state") method.

        Note

        This method *teleports* prims to the specified default state (positions and orientations).

        Warning

        This method has no effect on non-root articulation links or when no default state is set.
        In this case, a warning message is logged if `warn_on_non_default_state` is `True`.

        Parameters:
        :   **warn\_on\_non\_default\_state** â Whether to log a warning message when no default state is set.

        Raises:
        :   **AssertionError** â Wrapped prims are not valid.

        Example:

        ```python
        >>> # get default state (no default state set at this point)
        >>> prims.get_default_state()
        (None, None)
        >>>
        >>> # set default state
        >>> # - random positions for each prim
        >>> # - same fixed orientation for all prim
        >>> positions = np.random.uniform(low=-1, high=1, size=(3, 3))
        >>> prims.set_default_state(positions, orientations=[1.0, 0.0, 0.0, 0.0])
        >>>
        >>> # get default state (default state is set)
        >>> prims.get_default_state()
        (array(shape=(3, 3), dtype=float32), array(shape=(3, 4), dtype=float32))
        >>>
        >>> # reset prims to default state
        >>> prims.reset_to_default_state()
        ```

    reset\_xform\_op\_properties() → [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None")
    :   Reset the transformation operation attributes of the prims to a standard set.

        Backends: usd.

        USD Xform schema supports a wide range of transformation operation types.
        This method ensures that each wrapped prim has only the following transformations in the specified order.
        Any other transformation operations are removed, so they are not consumed.

        1. `xformOp:translate` (double precision)
        2. `xformOp:orient` (double precision)
        3. `xformOp:scale` (double precision)

        Note

        This method preserves the poses of the prims in the world frame while reorganizing the transformation operations.

        Raises:
        :   **AssertionError** â Wrapped prims are not valid.

        Example:

        ```python
        >>> # reset transform operations of all prims
        >>> prims.reset_xform_op_properties()
        >>>
        >>> # verify transform operations of the first wrapped prim
        >>> prims.prims[0].GetPropertyNames()
        [... 'xformOp:orient', 'xformOp:scale', 'xformOp:translate', 'xformOpOrder']
        ```

    *static* resolve\_paths( : *paths: str | list[str]*, : *raise\_on\_mixed\_paths: bool = True*, ) → tuple[list[str], list[str]]
    :   Resolve paths to prims in the stage to get existing and non-existing paths.

        Backends: usd.

        Parameters:
        :   * **paths** â Single path or list of paths to USD prims. Paths may contain regular expressions to match multiple prims.
            * **raise\_on\_mixed\_paths** â Whether to raise an error if resulting paths are mixed or invalid.

        Returns:
        :   Two-elements tuple. 1) List of existing paths. 2) List of non-existing paths.

        Raises:
        :   **ValueError** â If resulting paths are mixed or invalid and `raise_on_mixed_paths` is True.

    set\_default\_state( : *positions: list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *orientations: list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *\**, : *indices: int | list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, ) → [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None")
    :   Set the default state (positions and orientations) of the prims.

        Backends: usd.

        Hint

        Prims can be reset to their default state by calling the [`reset_to_default_state()`](#isaacsim.sensors.experimental.rtx.Radar.reset_to_default_state "isaacsim.sensors.experimental.rtx.Radar.reset_to_default_state") method.

        Parameters:
        :   * **positions** â Default positions in the world frame (shape `(N, 3)`).
              If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
            * **orientations** â Default orientations in the world frame (shape `(N, 4)`, quaternion `wxyz`).
              If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
            * **indices** â Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

        Raises:
        :   * **AssertionError** â If neither positions nor orientations are specified.
            * **AssertionError** â Wrapped prims are not valid.
            * **AssertionError** â If prims are non-root articulation links.

    set\_local\_poses( : *translations: list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *orientations: list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *\**, : *indices: int | list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, ) → [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None")
    :   Set the poses (translations and orientations) in the local frame of the prims.

        Backends: usd, usdrt, fabric.

        Note

        This method *teleports* prims to the specified poses.

        Parameters:
        :   * **translations** â Translations in the local frame (shape `(N, 3)`).
              If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
            * **orientations** â Orientations in the local frame (shape `(N, 4)`, quaternion `wxyz`).
              If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
            * **indices** â Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

        Raises:
        :   * **AssertionError** â If neither translations nor orientations are specified.
            * **AssertionError** â Wrapped prims are not valid.

        Example:

        ```python
        >>> # set random poses for all prims
        >>> translations = np.random.uniform(low=-1, high=1, size=(3, 3))
        >>> orientations = np.random.randn(3, 4)
        >>> orientations = orientations / np.linalg.norm(orientations, axis=-1, keepdims=True)  # normalize quaternions
        >>> prims.set_local_poses(translations, orientations)
        ```

    set\_local\_scales( : *scales: list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *\**, : *indices: int | list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, ) → [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None")
    :   Set the local scales of the prims.

        Backends: usd, usdrt, fabric.

        Parameters:
        :   * **scales** â Scales to be applied to the prims (shape `(N, 3)`).
              If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
            * **indices** â Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

        Raises:
        :   **AssertionError** â Wrapped prims are not valid.

        Example:

        ```python
        >>> # set random positive scales for all prims
        >>> scales = np.random.uniform(low=0.5, high=1.5, size=(3, 3))
        >>> prims.set_local_scales(scales)
        ```

    set\_visibilities( : *visibilities: bool | list | np.ndarray | wp.array*, : *\**, : *indices: int | list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, ) → [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None")
    :   Set the visibility state (whether prims are visible or invisible during rendering) of the prims.

        Backends: usd.

        Parameters:
        :   * **visibilities** â Boolean flags to set the visibility state (shape `(N, 1)`).
              If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
            * **indices** â Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

        Raises:
        :   **AssertionError** â Wrapped prims are not valid.

        Example:

        ```python
        >>> # make all prims invisible
        >>> prims.set_visibilities([False])
        >>>
        >>> # make first and last prims invisible
        >>> prims.set_visibilities([True])  # restore visibility from previous call
        >>> prims.set_visibilities([False], indices=[0, 2])
        ```

    set\_world\_poses( : *positions: list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *orientations: list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *\**, : *indices: int | list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, ) → [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None")
    :   Set the poses (positions and orientations) in the world frame of the prims.

        Backends: usd, usdrt, fabric.

        Note

        This method *teleports* prims to the specified poses.

        Parameters:
        :   * **positions** â Positions in the world frame (shape `(N, 3)`).
              If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
            * **orientations** â Orientations in the world frame (shape `(N, 4)`, quaternion `wxyz`).
              If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
            * **indices** â Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

        Raises:
        :   * **AssertionError** â If neither positions nor orientations are specified.
            * **AssertionError** â Wrapped prims are not valid.

        Example:

        ```python
        >>> # set random poses for all prims
        >>> positions = np.random.uniform(low=-1, high=1, size=(3, 3))
        >>> orientations = np.random.randn(3, 4)
        >>> orientations = orientations / np.linalg.norm(orientations, axis=-1, keepdims=True)  # normalize quaternions
        >>> prims.set_world_poses(positions, orientations)
        ```

    *property* aux\_output\_level*: str*
    :   The auxiliary output level configured on the GenericModelOutput RenderVar.

        Returns:
        :   The configured level (e.g. `"NONE"`, `"BASIC"`, `"EXTRA"`, `"FULL"`).

    *property* is\_non\_root\_articulation\_link*: bool*
    :   Indicate if the wrapped prims are a non-root link in an articulation tree.

        Backends: usd.

        Warning

        Transformation of the poses of non-root links in an articulation tree are not supported.

        Returns:
        :   Whether the prims are a non-root link in an articulation tree.

    *property* paths*: list[str]*
    :   Prim paths in the stage encapsulated by the wrapper.

        Returns:
        :   List of prim paths as strings.

        Example:

        ```python
        >>> prims.paths
        ['/World/prim_0', '/World/prim_1', '/World/prim_2']
        ```

    *property* prims*: list[pxr.Usd.Prim]*
    :   USD Prim objects encapsulated by the wrapper.

        Returns:
        :   List of USD Prim objects.

        Example:

        ```python
        >>> prims.prims
        [Usd.Prim(</World/prim_0>), Usd.Prim(</World/prim_1>), Usd.Prim(</World/prim_2>)]
        ```

    *property* valid*: bool*
    :   Whether all prims in the wrapper are valid.

        Returns:
        :   True if all prim paths specified in the wrapper correspond to valid prims in stage, False otherwise.

        Example:

        ```python
        >>> prims.valid
        True
        ```

*class* Acoustic( : *path: str*, : *\**, : *aux\_output\_level: str = 'NONE'*, : *tick\_rate: float | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *schemas: list[str] | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *attributes: dict[str, Any] | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *positions: list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *translations: list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *orientations: list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *scales: list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *reset\_xform\_op\_properties: bool = True*, )
:   Bases: `_SensorAuthoring`

    High level class for creating/wrapping USD OmniAcoustic prims.

    Note

    This class creates or wraps (one of both) USD OmniAcoustic prims according to the following rules:

    * If the prim path exists, a wrapper is placed over the USD OmniAcoustic prim.
    * If the prim path does not exist, a USD OmniAcoustic prim is created at the path and a wrapper is placed over it.

    Parameters:
    :   * **path** â Single path to existing or non-existing (one of both) USD OmniAcoustic prim.
          Can include regular expression for matching a prim.
        * **aux\_output\_level** â Auxiliary data level for GenericModelOutput. Valid values:
          `"NONE"` (default), `"BASIC"`.
        * **tick\_rate** â Sensor tick rate in Hz. A value of `0` (the default) enables autotrigger mode.
        * **attributes** â Attributes to set on the OmniAcoustic prim.
        * **positions** â Positions in the world frame (shape `(N, 3)`).
          If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
        * **translations** â Translations in the local frame (shape `(N, 3)`).
          If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
        * **orientations** â Orientations in the world frame (shape `(N, 4)`, quaternion `wxyz`).
          If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
        * **scales** â Scales to be applied to the prims (shape `(N, 3)`).
          If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
        * **reset\_xform\_op\_properties** â Whether to reset the transformation operation attributes of the prims to a standard set.
          See [`reset_xform_op_properties()`](#isaacsim.sensors.experimental.rtx.Acoustic.reset_xform_op_properties "isaacsim.sensors.experimental.rtx.Acoustic.reset_xform_op_properties") for more details.

    Raises:
    :   * **ValueError** â If no prim is found matching the specified path.
        * **ValueError** â If the input argument refers to more than one prim.

    Example:

    ```python
    >>> from isaacsim.sensors.experimental.rtx import Acoustic
    >>>
    >>> # given a USD stage with the OmniAcoustic prim: /World/prim_0
    >>> acoustic = Acoustic("/World/prim_0")
    ```

    apply\_visual\_materials( : *materials: type['VisualMaterial'] | list[type['VisualMaterial']]*, : *\**, : *weaker\_than\_descendants: bool | list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *indices: int | list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, ) → [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None")
    :   Apply visual materials to the prims, and optionally, to their descendants.

        Backends: usd.

        Parameters:
        :   * **materials** â Visual materials to be applied to the prims (shape `(N,)`).
              If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
            * **weaker\_than\_descendants** â Boolean flags to indicate whether descendant materials should be overridden (shape `(N, 1)`).
              If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
            * **indices** â Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

        Raises:
        :   **AssertionError** â Wrapped prims are not valid.

        Example:

        ```python
        >>> from isaacsim.core.experimental.materials import OmniGlassMaterial
        >>>
        >>> # create a dark-red glass visual material
        >>> material = OmniGlassMaterial("/World/material/glass")
        >>> material.set_input_values("glass_ior", [1.25])
        >>> material.set_input_values("depth", [0.001])
        >>> material.set_input_values("thin_walled", [False])
        >>> material.set_input_values("glass_color", [0.5, 0.0, 0.0])
        >>>
        >>> prims.apply_visual_materials(material)
        ```

    *static* create( : *path: str*, : *\**, : *aux\_output\_level: str = 'NONE'*, : *tick\_rate: float | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *attributes: dict[str, Any] | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *positions: list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *translations: list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *orientations: list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *scales: list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *reset\_xform\_op\_properties: bool = True*, : *config: str | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *usd\_path: str | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *variant: str | dict[str, str] | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, ) → [Acoustic](#isaacsim.sensors.experimental.rtx.Acoustic "isaacsim.sensors.experimental.rtx.Acoustic")
    :   Create an Acoustic instance from a config name or USD file path.

        Parameters:
        :   * **path** â Single path to existing or non-existing (one of both) USD OmniAcoustic prim.
            * **aux\_output\_level** â Auxiliary data level for GenericModelOutput. Valid values:
              `"NONE"` (default), `"BASIC"`.
            * **tick\_rate** â Sensor tick rate in Hz. When `None` (the default), the assetâs
              `omni:sensor:tickRate` attribute is preserved. Pass an explicit value to override.
            * **attributes** â Attributes to set on the OmniAcoustic prim.
            * **positions** â Positions in the world frame (shape `(N, 3)`).
            * **translations** â Translations in the local frame (shape `(N, 3)`).
            * **orientations** â Orientations in the world frame (shape `(N, 4)`, quaternion `wxyz`).
            * **scales** â Scales to be applied to the prims (shape `(N, 3)`).
            * **reset\_xform\_op\_properties** â Whether to reset the transformation operation attributes of the prims.
            * **config** â Configuration name for the sensor (from `SUPPORTED_ACOUSTIC_CONFIGS`).
            * **usd\_path** â Path to a USD file containing the sensor asset.
            * **variant** â Variant name for the sensor configuration. Nested variants
              supported via dictionary; pairs applied in dict insertion order,
              so outer variant sets must come first.

        Returns:
        :   Acoustic instance.

        Raises:
        :   * **ValueError** â If both âconfigâ and âusd\_pathâ are provided.
            * **ValueError** â If the specified config is not found.

        Example:

        ```python
        >>> from isaacsim.sensors.experimental.rtx import Acoustic
        >>>
        >>> acoustic = Acoustic.create(path="/World/acoustic")
        ```

    *static* ensure\_api( : *prims: list[Usd.Prim]*, : *api: type*, : *\*args: Any*, : *\*\*kwargs: Any*, ) → list[type['UsdAPISchemaBase']]
    :   Ensure that all prims have the specified API schema applied.

        Backends: usd.

        If a prim doesnât have the API schema, it will be applied.
        If it already has it, the existing API schema will be returned.

        Parameters:
        :   * **prims** â List of USD Prims to ensure API schema on.
            * **api** â The API schema type to ensure.
            * **\*args** â Additional positional arguments passed to API schema when applying it.
            * **\*\*kwargs** â Additional keyword arguments passed to API schema when applying it.

        Returns:
        :   List of API schema objects, one for each input prim.

        Example:

        ```python
        >>> import isaacsim.core.experimental.utils.prim as prim_utils
        >>> from pxr import UsdPhysics
        >>> from isaacsim.core.experimental.prims import Prim
        >>>
        >>> # given a USD stage with 3 prims at paths /World/prim_0, /World/prim_1, /World/prim_2,
        >>> # ensure all prims have physics API schema
        >>> usd_prims = [prim_utils.get_prim_at_path(f"/World/prim_{i}") for i in range(3)]
        >>> physics_apis = Prim.ensure_api(usd_prims, UsdPhysics.RigidBodyAPI)
        ```

    get\_applied\_visual\_materials( : *\**, : *indices: int | list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, ) → list[type['VisualMaterial'] | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None")]
    :   Get the applied visual materials.

        Backends: usd.

        Parameters:
        :   **indices** â Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

        Returns:
        :   List of applied visual materials (shape `(N,)`). If a prim does not have a material, `None` is returned.

        Raises:
        :   **AssertionError** â Wrapped prims are not valid.

        Example:

        ```python
        >>> # get the applied visual material of the last wrapped prim
        >>> prims.get_applied_visual_materials(indices=[2])[0]
        <isaacsim.core.experimental.materials.impl.visual_materials.omni_glass.OmniGlassMaterial object at 0x...>
        ```

    get\_default\_state( : *\**, : *indices: int | list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, ) → tuple[wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None"), wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None")]
    :   Get the default state (positions and orientations) of the prims.

        Backends: usd.

        Parameters:
        :   **indices** â Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

        Returns:
        :   Two-elements tuple. 1) The default positions in the world frame (shape `(N, 3)`).
            2) The default orientations in the world frame (shape `(N, 4)`, quaternion `wxyz`).
            If the default state is not set using the [`set_default_state()`](#isaacsim.sensors.experimental.rtx.Acoustic.set_default_state "isaacsim.sensors.experimental.rtx.Acoustic.set_default_state") method, `None` is returned.

        Raises:
        :   * **AssertionError** â Wrapped prims are not valid.
            * **AssertionError** â If prims are non-root articulation links.

    get\_local\_poses( : *\**, : *indices: int | list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, ) → tuple[wp.array, wp.array]
    :   Get the poses (translations and orientations) in the local frame of the prims.

        Backends: usd, usdrt, fabric.

        Parameters:
        :   **indices** â Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

        Returns:
        :   Two-elements tuple. 1) The translations in the local frame (shape `(N, 3)`).
            2) The orientations in the local frame (shape `(N, 4)`, quaternion `wxyz`).

        Raises:
        :   **AssertionError** â Wrapped prims are not valid.

        Example:

        ```python
        >>> # get the local poses of all prims
        >>> translations, orientations = prims.get_local_poses()
        >>> translations.shape, orientations.shape
        ((3, 3), (3, 4))
        >>>
        >>> # get the local pose of the first prim
        >>> translations, orientations = prims.get_local_poses(indices=[0])
        >>> translations.shape, orientations.shape
        ((1, 3), (1, 4))
        ```

    get\_local\_scales( : *\**, : *indices: int | list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, ) → wp.array
    :   Get the local scales of the prims.

        Backends: usd, usdrt, fabric.

        Parameters:
        :   **indices** â Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

        Returns:
        :   Scales of the prims (shape `(N, 3)`).

        Raises:
        :   **AssertionError** â Wrapped prims are not valid.

        Example:

        ```python
        >>> # get local scales of all prims
        >>> scales = prims.get_local_scales()
        >>> scales.shape
        (3, 3)
        ```

    get\_visibilities( : *\**, : *indices: int | list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, ) → wp.array
    :   Get the visibility state (whether prims are visible or invisible during rendering) of the prims.

        Backends: usd.

        Parameters:
        :   **indices** â Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

        Returns:
        :   Boolean flags indicating the visibility state (shape `(N, 1)`).

        Raises:
        :   **AssertionError** â Wrapped prims are not valid.

        Example:

        ```python
        >>> # get the visibility states of all prims
        >>> visibilities = prims.get_visibilities()
        >>> print(visibilities)
        [[ True] [ True] [ True]]
        >>>
        >>> # get the visibility states of the first and last prims
        >>> visibilities = prims.get_visibilities(indices=[0, 2])
        >>> print(visibilities)
        [[ True] [ True]]
        ```

    get\_world\_poses( : *\**, : *indices: int | list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, ) → tuple[wp.array, wp.array]
    :   Get the poses (positions and orientations) in the world frame of the prims.

        Backends: usd, usdrt, fabric.

        Parameters:
        :   **indices** â Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

        Returns:
        :   Two-elements tuple. 1) The positions in the world frame (shape `(N, 3)`).
            2) The orientations in the world frame (shape `(N, 4)`, quaternion `wxyz`).

        Raises:
        :   **AssertionError** â Wrapped prims are not valid.

        Example:

        ```python
        >>> # get the world poses of all prims
        >>> positions, orientations = prims.get_world_poses()
        >>> positions.shape, orientations.shape
        ((3, 3), (3, 4))
        >>>
        >>> # get the world pose of the first prim
        >>> positions, orientations = prims.get_world_poses(indices=[0])
        >>> positions.shape, orientations.shape
        ((1, 3), (1, 4))
        ```

    reset\_to\_default\_state( : *\**, : *warn\_on\_non\_default\_state: bool = False*, ) → [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None")
    :   Reset the prims to the specified default state.

        Backends: usd, usdrt, fabric.

        This method applies the default state defined using the [`set_default_state()`](#isaacsim.sensors.experimental.rtx.Acoustic.set_default_state "isaacsim.sensors.experimental.rtx.Acoustic.set_default_state") method.

        Note

        This method *teleports* prims to the specified default state (positions and orientations).

        Warning

        This method has no effect on non-root articulation links or when no default state is set.
        In this case, a warning message is logged if `warn_on_non_default_state` is `True`.

        Parameters:
        :   **warn\_on\_non\_default\_state** â Whether to log a warning message when no default state is set.

        Raises:
        :   **AssertionError** â Wrapped prims are not valid.

        Example:

        ```python
        >>> # get default state (no default state set at this point)
        >>> prims.get_default_state()
        (None, None)
        >>>
        >>> # set default state
        >>> # - random positions for each prim
        >>> # - same fixed orientation for all prim
        >>> positions = np.random.uniform(low=-1, high=1, size=(3, 3))
        >>> prims.set_default_state(positions, orientations=[1.0, 0.0, 0.0, 0.0])
        >>>
        >>> # get default state (default state is set)
        >>> prims.get_default_state()
        (array(shape=(3, 3), dtype=float32), array(shape=(3, 4), dtype=float32))
        >>>
        >>> # reset prims to default state
        >>> prims.reset_to_default_state()
        ```

    reset\_xform\_op\_properties() → [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None")
    :   Reset the transformation operation attributes of the prims to a standard set.

        Backends: usd.

        USD Xform schema supports a wide range of transformation operation types.
        This method ensures that each wrapped prim has only the following transformations in the specified order.
        Any other transformation operations are removed, so they are not consumed.

        1. `xformOp:translate` (double precision)
        2. `xformOp:orient` (double precision)
        3. `xformOp:scale` (double precision)

        Note

        This method preserves the poses of the prims in the world frame while reorganizing the transformation operations.

        Raises:
        :   **AssertionError** â Wrapped prims are not valid.

        Example:

        ```python
        >>> # reset transform operations of all prims
        >>> prims.reset_xform_op_properties()
        >>>
        >>> # verify transform operations of the first wrapped prim
        >>> prims.prims[0].GetPropertyNames()
        [... 'xformOp:orient', 'xformOp:scale', 'xformOp:translate', 'xformOpOrder']
        ```

    *static* resolve\_paths( : *paths: str | list[str]*, : *raise\_on\_mixed\_paths: bool = True*, ) → tuple[list[str], list[str]]
    :   Resolve paths to prims in the stage to get existing and non-existing paths.

        Backends: usd.

        Parameters:
        :   * **paths** â Single path or list of paths to USD prims. Paths may contain regular expressions to match multiple prims.
            * **raise\_on\_mixed\_paths** â Whether to raise an error if resulting paths are mixed or invalid.

        Returns:
        :   Two-elements tuple. 1) List of existing paths. 2) List of non-existing paths.

        Raises:
        :   **ValueError** â If resulting paths are mixed or invalid and `raise_on_mixed_paths` is True.

    set\_default\_state( : *positions: list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *orientations: list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *\**, : *indices: int | list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, ) → [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None")
    :   Set the default state (positions and orientations) of the prims.

        Backends: usd.

        Hint

        Prims can be reset to their default state by calling the [`reset_to_default_state()`](#isaacsim.sensors.experimental.rtx.Acoustic.reset_to_default_state "isaacsim.sensors.experimental.rtx.Acoustic.reset_to_default_state") method.

        Parameters:
        :   * **positions** â Default positions in the world frame (shape `(N, 3)`).
              If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
            * **orientations** â Default orientations in the world frame (shape `(N, 4)`, quaternion `wxyz`).
              If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
            * **indices** â Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

        Raises:
        :   * **AssertionError** â If neither positions nor orientations are specified.
            * **AssertionError** â Wrapped prims are not valid.
            * **AssertionError** â If prims are non-root articulation links.

    set\_local\_poses( : *translations: list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *orientations: list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *\**, : *indices: int | list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, ) → [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None")
    :   Set the poses (translations and orientations) in the local frame of the prims.

        Backends: usd, usdrt, fabric.

        Note

        This method *teleports* prims to the specified poses.

        Parameters:
        :   * **translations** â Translations in the local frame (shape `(N, 3)`).
              If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
            * **orientations** â Orientations in the local frame (shape `(N, 4)`, quaternion `wxyz`).
              If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
            * **indices** â Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

        Raises:
        :   * **AssertionError** â If neither translations nor orientations are specified.
            * **AssertionError** â Wrapped prims are not valid.

        Example:

        ```python
        >>> # set random poses for all prims
        >>> translations = np.random.uniform(low=-1, high=1, size=(3, 3))
        >>> orientations = np.random.randn(3, 4)
        >>> orientations = orientations / np.linalg.norm(orientations, axis=-1, keepdims=True)  # normalize quaternions
        >>> prims.set_local_poses(translations, orientations)
        ```

    set\_local\_scales( : *scales: list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *\**, : *indices: int | list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, ) → [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None")
    :   Set the local scales of the prims.

        Backends: usd, usdrt, fabric.

        Parameters:
        :   * **scales** â Scales to be applied to the prims (shape `(N, 3)`).
              If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
            * **indices** â Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

        Raises:
        :   **AssertionError** â Wrapped prims are not valid.

        Example:

        ```python
        >>> # set random positive scales for all prims
        >>> scales = np.random.uniform(low=0.5, high=1.5, size=(3, 3))
        >>> prims.set_local_scales(scales)
        ```

    set\_visibilities( : *visibilities: bool | list | np.ndarray | wp.array*, : *\**, : *indices: int | list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, ) → [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None")
    :   Set the visibility state (whether prims are visible or invisible during rendering) of the prims.

        Backends: usd.

        Parameters:
        :   * **visibilities** â Boolean flags to set the visibility state (shape `(N, 1)`).
              If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
            * **indices** â Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

        Raises:
        :   **AssertionError** â Wrapped prims are not valid.

        Example:

        ```python
        >>> # make all prims invisible
        >>> prims.set_visibilities([False])
        >>>
        >>> # make first and last prims invisible
        >>> prims.set_visibilities([True])  # restore visibility from previous call
        >>> prims.set_visibilities([False], indices=[0, 2])
        ```

    set\_world\_poses( : *positions: list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *orientations: list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *\**, : *indices: int | list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, ) → [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None")
    :   Set the poses (positions and orientations) in the world frame of the prims.

        Backends: usd, usdrt, fabric.

        Note

        This method *teleports* prims to the specified poses.

        Parameters:
        :   * **positions** â Positions in the world frame (shape `(N, 3)`).
              If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
            * **orientations** â Orientations in the world frame (shape `(N, 4)`, quaternion `wxyz`).
              If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
            * **indices** â Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

        Raises:
        :   * **AssertionError** â If neither positions nor orientations are specified.
            * **AssertionError** â Wrapped prims are not valid.

        Example:

        ```python
        >>> # set random poses for all prims
        >>> positions = np.random.uniform(low=-1, high=1, size=(3, 3))
        >>> orientations = np.random.randn(3, 4)
        >>> orientations = orientations / np.linalg.norm(orientations, axis=-1, keepdims=True)  # normalize quaternions
        >>> prims.set_world_poses(positions, orientations)
        ```

    *property* aux\_output\_level*: str*
    :   The auxiliary output level configured on the GenericModelOutput RenderVar.

        Returns:
        :   The configured level (e.g. `"NONE"`, `"BASIC"`, `"EXTRA"`, `"FULL"`).

    *property* is\_non\_root\_articulation\_link*: bool*
    :   Indicate if the wrapped prims are a non-root link in an articulation tree.

        Backends: usd.

        Warning

        Transformation of the poses of non-root links in an articulation tree are not supported.

        Returns:
        :   Whether the prims are a non-root link in an articulation tree.

    *property* paths*: list[str]*
    :   Prim paths in the stage encapsulated by the wrapper.

        Returns:
        :   List of prim paths as strings.

        Example:

        ```python
        >>> prims.paths
        ['/World/prim_0', '/World/prim_1', '/World/prim_2']
        ```

    *property* prims*: list[pxr.Usd.Prim]*
    :   USD Prim objects encapsulated by the wrapper.

        Returns:
        :   List of USD Prim objects.

        Example:

        ```python
        >>> prims.prims
        [Usd.Prim(</World/prim_0>), Usd.Prim(</World/prim_1>), Usd.Prim(</World/prim_2>)]
        ```

    *property* valid*: bool*
    :   Whether all prims in the wrapper are valid.

        Returns:
        :   True if all prim paths specified in the wrapper correspond to valid prims in stage, False otherwise.

        Example:

        ```python
        >>> prims.valid
        True
        ```

*class* RtxCamera( : *path: str*, : *\**, : *tick\_rate: float | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *schemas: list[str] | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *attributes: dict[str, Any] | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *positions: list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *translations: list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *orientations: list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *scales: list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *reset\_xform\_op\_properties: bool = True*, )
:   Bases: `_SensorAuthoring`

    High level class for creating/wrapping USD Camera prims as RTX sensors.

    Applies the `OmniSensorAPI` schema to the underlying `UsdGeom.Camera` prim,
    enabling tick-rate-controlled rendering. Optical parameters (focal length,
    clipping range, aperture, etc.) are accessible via the [`camera`](#isaacsim.sensors.experimental.rtx.RtxCamera.camera "isaacsim.sensors.experimental.rtx.RtxCamera.camera") property.

    Note

    This class creates or wraps (one of both) USD Camera prims according to the following rules:

    * If the prim path exists, a wrapper is placed over the USD Camera prim.
    * If the prim path does not exist, a USD Camera prim is created at the path and a wrapper is placed over it.

    Parameters:
    :   * **path** â Single path to existing or non-existing (one of both) USD Camera prim.
          Can include regular expression for matching a prim.
        * **tick\_rate** â Sensor tick rate in Hz. When `None` (the default), the primâs
          `omni:sensor:tickRate` attribute is left untouched, so any value already authored on
          the prim (e.g. from a USD asset) is preserved. For newly-created prims, the
          `OmniSensorAPI` schema default of `0` Hz applies (autotrigger mode).
        * **schemas** â Additional API schemas to apply to the prim (e.g. `["OmniLensDistortionOpenCvFisheyeAPI"]`).
          Supports multi-instance schemas via `"SchemaName:instanceName"` syntax.
        * **attributes** â Attributes to set on the Camera prim (applied after schemas, so schema-specific
          attributes can be set in the same call).
        * **positions** â Positions in the world frame (shape `(N, 3)`).
          If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
        * **translations** â Translations in the local frame (shape `(N, 3)`).
          If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
        * **orientations** â Orientations in the world frame (shape `(N, 4)`, quaternion `wxyz`).
          If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
        * **scales** â Scales to be applied to the prims (shape `(N, 3)`).
          If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
        * **reset\_xform\_op\_properties** â Whether to reset the transformation operation attributes of the prims to a standard set.
          See [`reset_xform_op_properties()`](#isaacsim.sensors.experimental.rtx.RtxCamera.reset_xform_op_properties "isaacsim.sensors.experimental.rtx.RtxCamera.reset_xform_op_properties") for more details.

    Raises:
    :   * **ValueError** â If no prim is found matching the specified path.
        * **ValueError** â If the input argument refers to more than one prim.

    Example:

    ```python
    >>> from isaacsim.sensors.experimental.rtx import RtxCamera
    >>>
    >>> cam = RtxCamera("/World/cam", tick_rate=30.0)
    >>> cam.camera.set_focal_lengths(24.0)
    >>> cam.camera.set_clipping_ranges(0.1, 100.0)
    ```

    apply\_visual\_materials( : *materials: type['VisualMaterial'] | list[type['VisualMaterial']]*, : *\**, : *weaker\_than\_descendants: bool | list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *indices: int | list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, ) → [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None")
    :   Apply visual materials to the prims, and optionally, to their descendants.

        Backends: usd.

        Parameters:
        :   * **materials** â Visual materials to be applied to the prims (shape `(N,)`).
              If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
            * **weaker\_than\_descendants** â Boolean flags to indicate whether descendant materials should be overridden (shape `(N, 1)`).
              If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
            * **indices** â Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

        Raises:
        :   **AssertionError** â Wrapped prims are not valid.

        Example:

        ```python
        >>> from isaacsim.core.experimental.materials import OmniGlassMaterial
        >>>
        >>> # create a dark-red glass visual material
        >>> material = OmniGlassMaterial("/World/material/glass")
        >>> material.set_input_values("glass_ior", [1.25])
        >>> material.set_input_values("depth", [0.001])
        >>> material.set_input_values("thin_walled", [False])
        >>> material.set_input_values("glass_color", [0.5, 0.0, 0.0])
        >>>
        >>> prims.apply_visual_materials(material)
        ```

    *static* create( : *path: str*, : *\**, : *tick\_rate: float | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *schemas: list[str] | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *attributes: dict[str, Any] | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *positions: list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *translations: list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *orientations: list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *scales: list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *reset\_xform\_op\_properties: bool = True*, : *config: str | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *usd\_path: str | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *variant: str | dict[str, str] | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, ) → [RtxCamera](#isaacsim.sensors.experimental.rtx.RtxCamera "isaacsim.sensors.experimental.rtx.RtxCamera")
    :   Create an RtxCamera instance, optionally from a known config or USD file.

        Parameters:
        :   * **path** â Single path to existing or non-existing (one of both) USD Camera prim.
            * **tick\_rate** â Sensor tick rate in Hz. When `None` (the default), the assetâs
              `omni:sensor:tickRate` attribute is preserved. Pass an explicit value to override.
            * **schemas** â Additional API schemas to apply to the prim (e.g. `["OmniLensDistortionOpenCvFisheyeAPI"]`).
              Supports multi-instance schemas via `"SchemaName:instanceName"` syntax.
            * **attributes** â Attributes to set on the Camera prim (applied after schemas, so schema-specific
              attributes can be set in the same call).
            * **positions** â Positions in the world frame (shape `(N, 3)`).
            * **translations** â Translations in the local frame (shape `(N, 3)`).
            * **orientations** â Orientations in the world frame (shape `(N, 4)`, quaternion `wxyz`).
            * **scales** â Scales to be applied to the prims (shape `(N, 3)`).
            * **reset\_xform\_op\_properties** â Whether to reset the transformation operation attributes of the prims.
            * **config** â Configuration name for the sensor (from `SUPPORTED_CAMERA_CONFIGS`).
            * **usd\_path** â Path to a USD file containing the camera asset.
            * **variant** â Variant name for the camera configuration. Nested variants
              supported via dictionary; pairs applied in dict insertion order,
              so outer variant sets must come first.

        Returns:
        :   RtxCamera instance.

        Raises:
        :   * **ValueError** â If both `config` and `usd_path` are provided.
            * **ValueError** â If the specified `config` is not found in `SUPPORTED_CAMERA_CONFIGS`.

        Example:

        ```python
        >>> from isaacsim.sensors.experimental.rtx import RtxCamera
        >>>
        >>> cam = RtxCamera.create(path="/World/cam", tick_rate=30.0)
        >>> cam.camera.set_focal_lengths(24.0)
        ```

    *static* ensure\_api( : *prims: list[Usd.Prim]*, : *api: type*, : *\*args: Any*, : *\*\*kwargs: Any*, ) → list[type['UsdAPISchemaBase']]
    :   Ensure that all prims have the specified API schema applied.

        Backends: usd.

        If a prim doesnât have the API schema, it will be applied.
        If it already has it, the existing API schema will be returned.

        Parameters:
        :   * **prims** â List of USD Prims to ensure API schema on.
            * **api** â The API schema type to ensure.
            * **\*args** â Additional positional arguments passed to API schema when applying it.
            * **\*\*kwargs** â Additional keyword arguments passed to API schema when applying it.

        Returns:
        :   List of API schema objects, one for each input prim.

        Example:

        ```python
        >>> import isaacsim.core.experimental.utils.prim as prim_utils
        >>> from pxr import UsdPhysics
        >>> from isaacsim.core.experimental.prims import Prim
        >>>
        >>> # given a USD stage with 3 prims at paths /World/prim_0, /World/prim_1, /World/prim_2,
        >>> # ensure all prims have physics API schema
        >>> usd_prims = [prim_utils.get_prim_at_path(f"/World/prim_{i}") for i in range(3)]
        >>> physics_apis = Prim.ensure_api(usd_prims, UsdPhysics.RigidBodyAPI)
        ```

    get\_applied\_visual\_materials( : *\**, : *indices: int | list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, ) → list[type['VisualMaterial'] | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None")]
    :   Get the applied visual materials.

        Backends: usd.

        Parameters:
        :   **indices** â Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

        Returns:
        :   List of applied visual materials (shape `(N,)`). If a prim does not have a material, `None` is returned.

        Raises:
        :   **AssertionError** â Wrapped prims are not valid.

        Example:

        ```python
        >>> # get the applied visual material of the last wrapped prim
        >>> prims.get_applied_visual_materials(indices=[2])[0]
        <isaacsim.core.experimental.materials.impl.visual_materials.omni_glass.OmniGlassMaterial object at 0x...>
        ```

    get\_default\_state( : *\**, : *indices: int | list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, ) → tuple[wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None"), wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None")]
    :   Get the default state (positions and orientations) of the prims.

        Backends: usd.

        Parameters:
        :   **indices** â Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

        Returns:
        :   Two-elements tuple. 1) The default positions in the world frame (shape `(N, 3)`).
            2) The default orientations in the world frame (shape `(N, 4)`, quaternion `wxyz`).
            If the default state is not set using the [`set_default_state()`](#isaacsim.sensors.experimental.rtx.RtxCamera.set_default_state "isaacsim.sensors.experimental.rtx.RtxCamera.set_default_state") method, `None` is returned.

        Raises:
        :   * **AssertionError** â Wrapped prims are not valid.
            * **AssertionError** â If prims are non-root articulation links.

    get\_local\_poses( : *\**, : *indices: int | list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, ) → tuple[wp.array, wp.array]
    :   Get the poses (translations and orientations) in the local frame of the prims.

        Backends: usd, usdrt, fabric.

        Parameters:
        :   **indices** â Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

        Returns:
        :   Two-elements tuple. 1) The translations in the local frame (shape `(N, 3)`).
            2) The orientations in the local frame (shape `(N, 4)`, quaternion `wxyz`).

        Raises:
        :   **AssertionError** â Wrapped prims are not valid.

        Example:

        ```python
        >>> # get the local poses of all prims
        >>> translations, orientations = prims.get_local_poses()
        >>> translations.shape, orientations.shape
        ((3, 3), (3, 4))
        >>>
        >>> # get the local pose of the first prim
        >>> translations, orientations = prims.get_local_poses(indices=[0])
        >>> translations.shape, orientations.shape
        ((1, 3), (1, 4))
        ```

    get\_local\_scales( : *\**, : *indices: int | list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, ) → wp.array
    :   Get the local scales of the prims.

        Backends: usd, usdrt, fabric.

        Parameters:
        :   **indices** â Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

        Returns:
        :   Scales of the prims (shape `(N, 3)`).

        Raises:
        :   **AssertionError** â Wrapped prims are not valid.

        Example:

        ```python
        >>> # get local scales of all prims
        >>> scales = prims.get_local_scales()
        >>> scales.shape
        (3, 3)
        ```

    get\_visibilities( : *\**, : *indices: int | list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, ) → wp.array
    :   Get the visibility state (whether prims are visible or invisible during rendering) of the prims.

        Backends: usd.

        Parameters:
        :   **indices** â Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

        Returns:
        :   Boolean flags indicating the visibility state (shape `(N, 1)`).

        Raises:
        :   **AssertionError** â Wrapped prims are not valid.

        Example:

        ```python
        >>> # get the visibility states of all prims
        >>> visibilities = prims.get_visibilities()
        >>> print(visibilities)
        [[ True] [ True] [ True]]
        >>>
        >>> # get the visibility states of the first and last prims
        >>> visibilities = prims.get_visibilities(indices=[0, 2])
        >>> print(visibilities)
        [[ True] [ True]]
        ```

    get\_world\_poses( : *\**, : *indices: int | list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, ) → tuple[wp.array, wp.array]
    :   Get the poses (positions and orientations) in the world frame of the prims.

        Backends: usd, usdrt, fabric.

        Parameters:
        :   **indices** â Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

        Returns:
        :   Two-elements tuple. 1) The positions in the world frame (shape `(N, 3)`).
            2) The orientations in the world frame (shape `(N, 4)`, quaternion `wxyz`).

        Raises:
        :   **AssertionError** â Wrapped prims are not valid.

        Example:

        ```python
        >>> # get the world poses of all prims
        >>> positions, orientations = prims.get_world_poses()
        >>> positions.shape, orientations.shape
        ((3, 3), (3, 4))
        >>>
        >>> # get the world pose of the first prim
        >>> positions, orientations = prims.get_world_poses(indices=[0])
        >>> positions.shape, orientations.shape
        ((1, 3), (1, 4))
        ```

    reset\_to\_default\_state( : *\**, : *warn\_on\_non\_default\_state: bool = False*, ) → [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None")
    :   Reset the prims to the specified default state.

        Backends: usd, usdrt, fabric.

        This method applies the default state defined using the [`set_default_state()`](#isaacsim.sensors.experimental.rtx.RtxCamera.set_default_state "isaacsim.sensors.experimental.rtx.RtxCamera.set_default_state") method.

        Note

        This method *teleports* prims to the specified default state (positions and orientations).

        Warning

        This method has no effect on non-root articulation links or when no default state is set.
        In this case, a warning message is logged if `warn_on_non_default_state` is `True`.

        Parameters:
        :   **warn\_on\_non\_default\_state** â Whether to log a warning message when no default state is set.

        Raises:
        :   **AssertionError** â Wrapped prims are not valid.

        Example:

        ```python
        >>> # get default state (no default state set at this point)
        >>> prims.get_default_state()
        (None, None)
        >>>
        >>> # set default state
        >>> # - random positions for each prim
        >>> # - same fixed orientation for all prim
        >>> positions = np.random.uniform(low=-1, high=1, size=(3, 3))
        >>> prims.set_default_state(positions, orientations=[1.0, 0.0, 0.0, 0.0])
        >>>
        >>> # get default state (default state is set)
        >>> prims.get_default_state()
        (array(shape=(3, 3), dtype=float32), array(shape=(3, 4), dtype=float32))
        >>>
        >>> # reset prims to default state
        >>> prims.reset_to_default_state()
        ```

    reset\_xform\_op\_properties() → [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None")
    :   Reset the transformation operation attributes of the prims to a standard set.

        Backends: usd.

        USD Xform schema supports a wide range of transformation operation types.
        This method ensures that each wrapped prim has only the following transformations in the specified order.
        Any other transformation operations are removed, so they are not consumed.

        1. `xformOp:translate` (double precision)
        2. `xformOp:orient` (double precision)
        3. `xformOp:scale` (double precision)

        Note

        This method preserves the poses of the prims in the world frame while reorganizing the transformation operations.

        Raises:
        :   **AssertionError** â Wrapped prims are not valid.

        Example:

        ```python
        >>> # reset transform operations of all prims
        >>> prims.reset_xform_op_properties()
        >>>
        >>> # verify transform operations of the first wrapped prim
        >>> prims.prims[0].GetPropertyNames()
        [... 'xformOp:orient', 'xformOp:scale', 'xformOp:translate', 'xformOpOrder']
        ```

    *static* resolve\_paths( : *paths: str | list[str]*, : *raise\_on\_mixed\_paths: bool = True*, ) → tuple[list[str], list[str]]
    :   Resolve paths to prims in the stage to get existing and non-existing paths.

        Backends: usd.

        Parameters:
        :   * **paths** â Single path or list of paths to USD prims. Paths may contain regular expressions to match multiple prims.
            * **raise\_on\_mixed\_paths** â Whether to raise an error if resulting paths are mixed or invalid.

        Returns:
        :   Two-elements tuple. 1) List of existing paths. 2) List of non-existing paths.

        Raises:
        :   **ValueError** â If resulting paths are mixed or invalid and `raise_on_mixed_paths` is True.

    set\_default\_state( : *positions: list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *orientations: list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *\**, : *indices: int | list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, ) → [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None")
    :   Set the default state (positions and orientations) of the prims.

        Backends: usd.

        Hint

        Prims can be reset to their default state by calling the [`reset_to_default_state()`](#isaacsim.sensors.experimental.rtx.RtxCamera.reset_to_default_state "isaacsim.sensors.experimental.rtx.RtxCamera.reset_to_default_state") method.

        Parameters:
        :   * **positions** â Default positions in the world frame (shape `(N, 3)`).
              If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
            * **orientations** â Default orientations in the world frame (shape `(N, 4)`, quaternion `wxyz`).
              If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
            * **indices** â Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

        Raises:
        :   * **AssertionError** â If neither positions nor orientations are specified.
            * **AssertionError** â Wrapped prims are not valid.
            * **AssertionError** â If prims are non-root articulation links.

    set\_local\_poses( : *translations: list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *orientations: list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *\**, : *indices: int | list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, ) → [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None")
    :   Set the poses (translations and orientations) in the local frame of the prims.

        Backends: usd, usdrt, fabric.

        Note

        This method *teleports* prims to the specified poses.

        Parameters:
        :   * **translations** â Translations in the local frame (shape `(N, 3)`).
              If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
            * **orientations** â Orientations in the local frame (shape `(N, 4)`, quaternion `wxyz`).
              If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
            * **indices** â Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

        Raises:
        :   * **AssertionError** â If neither translations nor orientations are specified.
            * **AssertionError** â Wrapped prims are not valid.

        Example:

        ```python
        >>> # set random poses for all prims
        >>> translations = np.random.uniform(low=-1, high=1, size=(3, 3))
        >>> orientations = np.random.randn(3, 4)
        >>> orientations = orientations / np.linalg.norm(orientations, axis=-1, keepdims=True)  # normalize quaternions
        >>> prims.set_local_poses(translations, orientations)
        ```

    set\_local\_scales( : *scales: list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *\**, : *indices: int | list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, ) → [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None")
    :   Set the local scales of the prims.

        Backends: usd, usdrt, fabric.

        Parameters:
        :   * **scales** â Scales to be applied to the prims (shape `(N, 3)`).
              If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
            * **indices** â Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

        Raises:
        :   **AssertionError** â Wrapped prims are not valid.

        Example:

        ```python
        >>> # set random positive scales for all prims
        >>> scales = np.random.uniform(low=0.5, high=1.5, size=(3, 3))
        >>> prims.set_local_scales(scales)
        ```

    set\_visibilities( : *visibilities: bool | list | np.ndarray | wp.array*, : *\**, : *indices: int | list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, ) → [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None")
    :   Set the visibility state (whether prims are visible or invisible during rendering) of the prims.

        Backends: usd.

        Parameters:
        :   * **visibilities** â Boolean flags to set the visibility state (shape `(N, 1)`).
              If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
            * **indices** â Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

        Raises:
        :   **AssertionError** â Wrapped prims are not valid.

        Example:

        ```python
        >>> # make all prims invisible
        >>> prims.set_visibilities([False])
        >>>
        >>> # make first and last prims invisible
        >>> prims.set_visibilities([True])  # restore visibility from previous call
        >>> prims.set_visibilities([False], indices=[0, 2])
        ```

    set\_world\_poses( : *positions: list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *orientations: list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *\**, : *indices: int | list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, ) → [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None")
    :   Set the poses (positions and orientations) in the world frame of the prims.

        Backends: usd, usdrt, fabric.

        Note

        This method *teleports* prims to the specified poses.

        Parameters:
        :   * **positions** â Positions in the world frame (shape `(N, 3)`).
              If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
            * **orientations** â Orientations in the world frame (shape `(N, 4)`, quaternion `wxyz`).
              If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
            * **indices** â Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

        Raises:
        :   * **AssertionError** â If neither positions nor orientations are specified.
            * **AssertionError** â Wrapped prims are not valid.

        Example:

        ```python
        >>> # set random poses for all prims
        >>> positions = np.random.uniform(low=-1, high=1, size=(3, 3))
        >>> orientations = np.random.randn(3, 4)
        >>> orientations = orientations / np.linalg.norm(orientations, axis=-1, keepdims=True)  # normalize quaternions
        >>> prims.set_world_poses(positions, orientations)
        ```

    *property* aux\_output\_level*: str*
    :   The auxiliary output level configured on the GenericModelOutput RenderVar.

        Returns:
        :   The configured level (e.g. `"NONE"`, `"BASIC"`, `"EXTRA"`, `"FULL"`).

    *property* camera*: [Camera](../../isaacsim.core.experimental.objects/docs/index.html#isaacsim.core.experimental.objects.Camera "isaacsim.core.experimental.objects.impl.camera.Camera")*
    :   Camera object for accessing optical parameters.

        Returns a [`Camera`](../../isaacsim.core.experimental.objects/docs/index.html#isaacsim.core.experimental.objects.Camera "isaacsim.core.experimental.objects.Camera") wrapper over
        the same USD prim, providing access to focal length, clipping range, aperture,
        and other optical properties.

        Returns:
        :   Camera object wrapping the sensor prim.

        Example:

        ```python
        >>> cam = RtxCamera("/World/cam")
        >>> cam.camera.set_focal_lengths(50.0)
        >>> cam.camera.get_focal_lengths()
        ```

    *property* is\_non\_root\_articulation\_link*: bool*
    :   Indicate if the wrapped prims are a non-root link in an articulation tree.

        Backends: usd.

        Warning

        Transformation of the poses of non-root links in an articulation tree are not supported.

        Returns:
        :   Whether the prims are a non-root link in an articulation tree.

    *property* paths*: list[str]*
    :   Prim paths in the stage encapsulated by the wrapper.

        Returns:
        :   List of prim paths as strings.

        Example:

        ```python
        >>> prims.paths
        ['/World/prim_0', '/World/prim_1', '/World/prim_2']
        ```

    *property* prims*: list[pxr.Usd.Prim]*
    :   USD Prim objects encapsulated by the wrapper.

        Returns:
        :   List of USD Prim objects.

        Example:

        ```python
        >>> prims.prims
        [Usd.Prim(</World/prim_0>), Usd.Prim(</World/prim_1>), Usd.Prim(</World/prim_2>)]
        ```

    *property* valid*: bool*
    :   Whether all prims in the wrapper are valid.

        Returns:
        :   True if all prim paths specified in the wrapper correspond to valid prims in stage, False otherwise.

        Example:

        ```python
        >>> prims.valid
        True
        ```

*class* StructuredLightCamera( : *path: str*, : *projector\_light\_patterns: list[str | Path]*, : *projector\_direction\_texture: str | Path*, : *\**, : *projector\_prim\_path: str | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *projector\_position: np.ndarray | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *projector\_orientation: np.ndarray | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *projector\_timestamps: list[tuple[int, int]] | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *projector\_cycle\_period: tuple[int, int] | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *projector\_intensity: float = 150000.0*, : *projector\_width: float = 1.0*, : *projector\_height: float = 1.0*, : *tick\_rate: float | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *schemas: list[str] | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *attributes: dict[str, Any] | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *positions: list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *translations: list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *orientations: list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *scales: list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *reset\_xform\_op\_properties: bool = True*, )
:   Bases: [`RtxCamera`](#isaacsim.sensors.experimental.rtx.RtxCamera "isaacsim.sensors.experimental.rtx.impl.rtx_camera.RtxCamera")

    Structured light camera sensor: an [`RtxCamera`](#isaacsim.sensors.experimental.rtx.RtxCamera "isaacsim.sensors.experimental.rtx.RtxCamera") with cycling projectors.

    Extends [`RtxCamera`](#isaacsim.sensors.experimental.rtx.RtxCamera "isaacsim.sensors.experimental.rtx.RtxCamera") by creating a set of `UsdLux.RectLight` prims
    (one per projector pattern) under a shared parent Xform and cycling through them
    based on the current simulation time and a list of user-supplied rational
    timestamps.

    Note

    This class is an authoring class â it creates and manages USD prims. For
    data acquisition, wrap an instance in [`CameraSensor`](#isaacsim.sensors.experimental.rtx.CameraSensor "isaacsim.sensors.experimental.rtx.CameraSensor"):

    ```python
    cam = StructuredLightCamera(...)
    sensor = CameraSensor(cam, resolution=(720, 1280), annotators=["rgb"])
    ```

    **Timestamps**

    `projector_timestamps` is a list of `(numerator, denominator)` rational
    tuples, one per pattern. Each tuple represents the simulation time (in seconds)
    at which that pattern becomes active. The first entry **must** represent
    \(t = 0\) (typically `(0, 1)`, though any `(0, k)` is accepted) and
    the list **must** be strictly increasing. Rational tuples avoid the
    floating-point precision issues that arise when timestamps span nanoseconds to
    milliseconds.

    After the last timestamp, the cycle repeats with period
    `projector_cycle_period`. If not supplied at construction, the period is
    inferred as `timestamps[-1] + (timestamps[1] - timestamps[0])` for
    \(N \\geq 2\) or `Fraction(1, 30)` for \(N = 1\). Calling
    [`set_projector_timestamps()`](#isaacsim.sensors.experimental.rtx.StructuredLightCamera.set_projector_timestamps "isaacsim.sensors.experimental.rtx.StructuredLightCamera.set_projector_timestamps") preserves an explicitly-supplied period and
    re-infers an implicit one.

    **Warnings**

    * If the observed simulation `dt` exceeds the minimum projector timestamp
      interval (patterns would be impossible to resolve), a warning is logged
      once.
    * If a single tick advances the active pattern by more than one index (mod
      `N`), a warning is logged once per tick where this occurs.

    Parameters:
    :   * **path** â Prim path of the USD Camera prim to create or wrap.
        * **projector\_light\_patterns** â Paths to projector pattern images (e.g. PNG
          files). One `UsdLux.RectLight` prim is created per pattern.
        * **projector\_direction\_texture** â Path to the projector direction texture
          (typically an EXR file) that defines the per-pixel projection
          direction. Applied to every patternâs RectLight prim.
        * **projector\_prim\_path** â Prim path of the projector parent Xform. Defaults to
          `f"{path}/projectors"`.
        * **projector\_position** â World-frame position of the projector Xform (shape
          `(3,)`). Defaults to the cameraâs world position.
        * **projector\_orientation** â World-frame quaternion (`wxyz`) of the projector
          Xform (shape `(4,)`). Defaults to the cameraâs world orientation.
        * **projector\_timestamps** â Activation times for each pattern as
          `list[tuple[int, int]]`. First entry must be `(0, 1)`; the list
          must be strictly increasing. Defaults to
          `[(i, 30) for i in range(N)]`.
        * **projector\_cycle\_period** â Explicit cycle period as `(numerator,
          denominator)`. Defaults to an inferred value (see above).
        * **projector\_intensity** â RectLight intensity. Defaults to `150000.0`.
        * **projector\_width** â RectLight width. Defaults to `1.0`.
        * **projector\_height** â RectLight height. Defaults to `1.0`.
        * **tick\_rate** â RTX camera tick rate in Hz. See [`RtxCamera`](#isaacsim.sensors.experimental.rtx.RtxCamera "isaacsim.sensors.experimental.rtx.RtxCamera").
        * **schemas** â Additional API schemas to apply. See [`RtxCamera`](#isaacsim.sensors.experimental.rtx.RtxCamera "isaacsim.sensors.experimental.rtx.RtxCamera").
        * **attributes** â Additional attributes to set on the Camera prim. See
          [`RtxCamera`](#isaacsim.sensors.experimental.rtx.RtxCamera "isaacsim.sensors.experimental.rtx.RtxCamera").
        * **positions** â Camera world-frame positions (shape `(1, 3)`). See
          [`RtxCamera`](#isaacsim.sensors.experimental.rtx.RtxCamera "isaacsim.sensors.experimental.rtx.RtxCamera").
        * **translations** â Camera local-frame translations (shape `(1, 3)`). See
          [`RtxCamera`](#isaacsim.sensors.experimental.rtx.RtxCamera "isaacsim.sensors.experimental.rtx.RtxCamera").
        * **orientations** â Camera world-frame orientations (shape `(1, 4)`,
          `wxyz`). See [`RtxCamera`](#isaacsim.sensors.experimental.rtx.RtxCamera "isaacsim.sensors.experimental.rtx.RtxCamera").
        * **scales** â Camera scales (shape `(1, 3)`). See [`RtxCamera`](#isaacsim.sensors.experimental.rtx.RtxCamera "isaacsim.sensors.experimental.rtx.RtxCamera").
        * **reset\_xform\_op\_properties** â Whether to reset the Cameraâs xformOp stack.
          See [`RtxCamera`](#isaacsim.sensors.experimental.rtx.RtxCamera "isaacsim.sensors.experimental.rtx.RtxCamera").

    Raises:
    :   * **ValueError** â If `projector_light_patterns` is empty.
        * **ValueError** â If `projector_direction_texture` is `None`.
        * **ValueError** â If `projector_timestamps` is invalid (wrong length, first
          entry not zero, not strictly increasing).
        * **ValueError** â If `projector_cycle_period` is not strictly greater than
          the last timestamp.

    Example:

    ```python
    >>> from pathlib import Path
    >>> from isaacsim.sensors.experimental.rtx import StructuredLightCamera
    >>>
    >>> patterns = [Path(f"patterns/image_{i:02d}.png") for i in range(10)]
    >>> timestamps = [(i, 1000) for i in range(10)]  # 1 ms spacing
    >>> cam = StructuredLightCamera(
    ...     "/World/camera",
    ...     projector_light_patterns=patterns,
    ...     projector_direction_texture=Path("direction_texture.exr"),
    ...     projector_timestamps=timestamps,
    ... )
    ```

    apply\_visual\_materials( : *materials: type['VisualMaterial'] | list[type['VisualMaterial']]*, : *\**, : *weaker\_than\_descendants: bool | list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *indices: int | list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, ) → [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None")
    :   Apply visual materials to the prims, and optionally, to their descendants.

        Backends: usd.

        Parameters:
        :   * **materials** â Visual materials to be applied to the prims (shape `(N,)`).
              If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
            * **weaker\_than\_descendants** â Boolean flags to indicate whether descendant materials should be overridden (shape `(N, 1)`).
              If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
            * **indices** â Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

        Raises:
        :   **AssertionError** â Wrapped prims are not valid.

        Example:

        ```python
        >>> from isaacsim.core.experimental.materials import OmniGlassMaterial
        >>>
        >>> # create a dark-red glass visual material
        >>> material = OmniGlassMaterial("/World/material/glass")
        >>> material.set_input_values("glass_ior", [1.25])
        >>> material.set_input_values("depth", [0.001])
        >>> material.set_input_values("thin_walled", [False])
        >>> material.set_input_values("glass_color", [0.5, 0.0, 0.0])
        >>>
        >>> prims.apply_visual_materials(material)
        ```

    *static* create( : *path: str*, : *\**, : *tick\_rate: float | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *schemas: list[str] | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *attributes: dict[str, Any] | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *positions: list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *translations: list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *orientations: list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *scales: list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *reset\_xform\_op\_properties: bool = True*, : *config: str | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *usd\_path: str | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *variant: str | dict[str, str] | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, ) → [RtxCamera](#isaacsim.sensors.experimental.rtx.RtxCamera "isaacsim.sensors.experimental.rtx.RtxCamera")
    :   Create an RtxCamera instance, optionally from a known config or USD file.

        Parameters:
        :   * **path** â Single path to existing or non-existing (one of both) USD Camera prim.
            * **tick\_rate** â Sensor tick rate in Hz. When `None` (the default), the assetâs
              `omni:sensor:tickRate` attribute is preserved. Pass an explicit value to override.
            * **schemas** â Additional API schemas to apply to the prim (e.g. `["OmniLensDistortionOpenCvFisheyeAPI"]`).
              Supports multi-instance schemas via `"SchemaName:instanceName"` syntax.
            * **attributes** â Attributes to set on the Camera prim (applied after schemas, so schema-specific
              attributes can be set in the same call).
            * **positions** â Positions in the world frame (shape `(N, 3)`).
            * **translations** â Translations in the local frame (shape `(N, 3)`).
            * **orientations** â Orientations in the world frame (shape `(N, 4)`, quaternion `wxyz`).
            * **scales** â Scales to be applied to the prims (shape `(N, 3)`).
            * **reset\_xform\_op\_properties** â Whether to reset the transformation operation attributes of the prims.
            * **config** â Configuration name for the sensor (from `SUPPORTED_CAMERA_CONFIGS`).
            * **usd\_path** â Path to a USD file containing the camera asset.
            * **variant** â Variant name for the camera configuration. Nested variants
              supported via dictionary; pairs applied in dict insertion order,
              so outer variant sets must come first.

        Returns:
        :   RtxCamera instance.

        Raises:
        :   * **ValueError** â If both `config` and `usd_path` are provided.
            * **ValueError** â If the specified `config` is not found in `SUPPORTED_CAMERA_CONFIGS`.

        Example:

        ```python
        >>> from isaacsim.sensors.experimental.rtx import RtxCamera
        >>>
        >>> cam = RtxCamera.create(path="/World/cam", tick_rate=30.0)
        >>> cam.camera.set_focal_lengths(24.0)
        ```

    destroy() → [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None")
    :   Unregister the app-update observer and release references.

        Safe to call multiple times. After `destroy()`, the instance will no
        longer update the active pattern on simulation-time changes.

    *static* ensure\_api( : *prims: list[Usd.Prim]*, : *api: type*, : *\*args: Any*, : *\*\*kwargs: Any*, ) → list[type['UsdAPISchemaBase']]
    :   Ensure that all prims have the specified API schema applied.

        Backends: usd.

        If a prim doesnât have the API schema, it will be applied.
        If it already has it, the existing API schema will be returned.

        Parameters:
        :   * **prims** â List of USD Prims to ensure API schema on.
            * **api** â The API schema type to ensure.
            * **\*args** â Additional positional arguments passed to API schema when applying it.
            * **\*\*kwargs** â Additional keyword arguments passed to API schema when applying it.

        Returns:
        :   List of API schema objects, one for each input prim.

        Example:

        ```python
        >>> import isaacsim.core.experimental.utils.prim as prim_utils
        >>> from pxr import UsdPhysics
        >>> from isaacsim.core.experimental.prims import Prim
        >>>
        >>> # given a USD stage with 3 prims at paths /World/prim_0, /World/prim_1, /World/prim_2,
        >>> # ensure all prims have physics API schema
        >>> usd_prims = [prim_utils.get_prim_at_path(f"/World/prim_{i}") for i in range(3)]
        >>> physics_apis = Prim.ensure_api(usd_prims, UsdPhysics.RigidBodyAPI)
        ```

    get\_active\_pattern\_index() → int
    :   Return the index of the currently active projector pattern (0-based).

    get\_applied\_visual\_materials( : *\**, : *indices: int | list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, ) → list[type['VisualMaterial'] | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None")]
    :   Get the applied visual materials.

        Backends: usd.

        Parameters:
        :   **indices** â Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

        Returns:
        :   List of applied visual materials (shape `(N,)`). If a prim does not have a material, `None` is returned.

        Raises:
        :   **AssertionError** â Wrapped prims are not valid.

        Example:

        ```python
        >>> # get the applied visual material of the last wrapped prim
        >>> prims.get_applied_visual_materials(indices=[2])[0]
        <isaacsim.core.experimental.materials.impl.visual_materials.omni_glass.OmniGlassMaterial object at 0x...>
        ```

    get\_default\_state( : *\**, : *indices: int | list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, ) → tuple[wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None"), wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None")]
    :   Get the default state (positions and orientations) of the prims.

        Backends: usd.

        Parameters:
        :   **indices** â Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

        Returns:
        :   Two-elements tuple. 1) The default positions in the world frame (shape `(N, 3)`).
            2) The default orientations in the world frame (shape `(N, 4)`, quaternion `wxyz`).
            If the default state is not set using the [`set_default_state()`](#isaacsim.sensors.experimental.rtx.StructuredLightCamera.set_default_state "isaacsim.sensors.experimental.rtx.StructuredLightCamera.set_default_state") method, `None` is returned.

        Raises:
        :   * **AssertionError** â Wrapped prims are not valid.
            * **AssertionError** â If prims are non-root articulation links.

    get\_local\_poses( : *\**, : *indices: int | list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, ) → tuple[wp.array, wp.array]
    :   Get the poses (translations and orientations) in the local frame of the prims.

        Backends: usd, usdrt, fabric.

        Parameters:
        :   **indices** â Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

        Returns:
        :   Two-elements tuple. 1) The translations in the local frame (shape `(N, 3)`).
            2) The orientations in the local frame (shape `(N, 4)`, quaternion `wxyz`).

        Raises:
        :   **AssertionError** â Wrapped prims are not valid.

        Example:

        ```python
        >>> # get the local poses of all prims
        >>> translations, orientations = prims.get_local_poses()
        >>> translations.shape, orientations.shape
        ((3, 3), (3, 4))
        >>>
        >>> # get the local pose of the first prim
        >>> translations, orientations = prims.get_local_poses(indices=[0])
        >>> translations.shape, orientations.shape
        ((1, 3), (1, 4))
        ```

    get\_local\_scales( : *\**, : *indices: int | list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, ) → wp.array
    :   Get the local scales of the prims.

        Backends: usd, usdrt, fabric.

        Parameters:
        :   **indices** â Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

        Returns:
        :   Scales of the prims (shape `(N, 3)`).

        Raises:
        :   **AssertionError** â Wrapped prims are not valid.

        Example:

        ```python
        >>> # get local scales of all prims
        >>> scales = prims.get_local_scales()
        >>> scales.shape
        (3, 3)
        ```

    get\_num\_patterns() → int
    :   Return the number of projector patterns.

    get\_projector\_cycle\_period() → tuple[int, int]
    :   Return the projector cycle period as a rational tuple.

    get\_projector\_direction\_texture() → str | Path
    :   Return the projector direction texture identifier as supplied at construction.

    get\_projector\_prim\_path() → str
    :   Return the prim path of the projector parent Xform.

    get\_projector\_timestamps() → list[tuple[int, int]]
    :   Return the projector activation timestamps as rational tuples.

    get\_rect\_light\_prims() → list[pxr.Usd.Prim]
    :   Return the list of `UsdLux.RectLight` prims, one per pattern.

    get\_visibilities( : *\**, : *indices: int | list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, ) → wp.array
    :   Get the visibility state (whether prims are visible or invisible during rendering) of the prims.

        Backends: usd.

        Parameters:
        :   **indices** â Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

        Returns:
        :   Boolean flags indicating the visibility state (shape `(N, 1)`).

        Raises:
        :   **AssertionError** â Wrapped prims are not valid.

        Example:

        ```python
        >>> # get the visibility states of all prims
        >>> visibilities = prims.get_visibilities()
        >>> print(visibilities)
        [[ True] [ True] [ True]]
        >>>
        >>> # get the visibility states of the first and last prims
        >>> visibilities = prims.get_visibilities(indices=[0, 2])
        >>> print(visibilities)
        [[ True] [ True]]
        ```

    get\_world\_poses( : *\**, : *indices: int | list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, ) → tuple[wp.array, wp.array]
    :   Get the poses (positions and orientations) in the world frame of the prims.

        Backends: usd, usdrt, fabric.

        Parameters:
        :   **indices** â Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

        Returns:
        :   Two-elements tuple. 1) The positions in the world frame (shape `(N, 3)`).
            2) The orientations in the world frame (shape `(N, 4)`, quaternion `wxyz`).

        Raises:
        :   **AssertionError** â Wrapped prims are not valid.

        Example:

        ```python
        >>> # get the world poses of all prims
        >>> positions, orientations = prims.get_world_poses()
        >>> positions.shape, orientations.shape
        ((3, 3), (3, 4))
        >>>
        >>> # get the world pose of the first prim
        >>> positions, orientations = prims.get_world_poses(indices=[0])
        >>> positions.shape, orientations.shape
        ((1, 3), (1, 4))
        ```

    post\_reset() → [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None")
    :   Reset projector state so the next tick starts fresh.

        Clears the previous-tick simulation-time cache, resets the coarse-dt
        warning flag, and activates pattern 0.

    reset\_to\_default\_state( : *\**, : *warn\_on\_non\_default\_state: bool = False*, ) → [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None")
    :   Reset the prims to the specified default state.

        Backends: usd, usdrt, fabric.

        This method applies the default state defined using the [`set_default_state()`](#isaacsim.sensors.experimental.rtx.StructuredLightCamera.set_default_state "isaacsim.sensors.experimental.rtx.StructuredLightCamera.set_default_state") method.

        Note

        This method *teleports* prims to the specified default state (positions and orientations).

        Warning

        This method has no effect on non-root articulation links or when no default state is set.
        In this case, a warning message is logged if `warn_on_non_default_state` is `True`.

        Parameters:
        :   **warn\_on\_non\_default\_state** â Whether to log a warning message when no default state is set.

        Raises:
        :   **AssertionError** â Wrapped prims are not valid.

        Example:

        ```python
        >>> # get default state (no default state set at this point)
        >>> prims.get_default_state()
        (None, None)
        >>>
        >>> # set default state
        >>> # - random positions for each prim
        >>> # - same fixed orientation for all prim
        >>> positions = np.random.uniform(low=-1, high=1, size=(3, 3))
        >>> prims.set_default_state(positions, orientations=[1.0, 0.0, 0.0, 0.0])
        >>>
        >>> # get default state (default state is set)
        >>> prims.get_default_state()
        (array(shape=(3, 3), dtype=float32), array(shape=(3, 4), dtype=float32))
        >>>
        >>> # reset prims to default state
        >>> prims.reset_to_default_state()
        ```

    reset\_xform\_op\_properties() → [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None")
    :   Reset the transformation operation attributes of the prims to a standard set.

        Backends: usd.

        USD Xform schema supports a wide range of transformation operation types.
        This method ensures that each wrapped prim has only the following transformations in the specified order.
        Any other transformation operations are removed, so they are not consumed.

        1. `xformOp:translate` (double precision)
        2. `xformOp:orient` (double precision)
        3. `xformOp:scale` (double precision)

        Note

        This method preserves the poses of the prims in the world frame while reorganizing the transformation operations.

        Raises:
        :   **AssertionError** â Wrapped prims are not valid.

        Example:

        ```python
        >>> # reset transform operations of all prims
        >>> prims.reset_xform_op_properties()
        >>>
        >>> # verify transform operations of the first wrapped prim
        >>> prims.prims[0].GetPropertyNames()
        [... 'xformOp:orient', 'xformOp:scale', 'xformOp:translate', 'xformOpOrder']
        ```

    *static* resolve\_paths( : *paths: str | list[str]*, : *raise\_on\_mixed\_paths: bool = True*, ) → tuple[list[str], list[str]]
    :   Resolve paths to prims in the stage to get existing and non-existing paths.

        Backends: usd.

        Parameters:
        :   * **paths** â Single path or list of paths to USD prims. Paths may contain regular expressions to match multiple prims.
            * **raise\_on\_mixed\_paths** â Whether to raise an error if resulting paths are mixed or invalid.

        Returns:
        :   Two-elements tuple. 1) List of existing paths. 2) List of non-existing paths.

        Raises:
        :   **ValueError** â If resulting paths are mixed or invalid and `raise_on_mixed_paths` is True.

    set\_active\_pattern\_manual( : *pattern\_index: int*, ) → [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None")
    :   Manually activate the pattern at `pattern_index`.

        Bypasses time-based cycling until the next app-update tick, at which
        point the pattern will be re-selected based on the current simulation
        time. Useful for offline tests and deterministic capture loops.

        Parameters:
        :   **pattern\_index** â Index of the pattern to activate.

        Raises:
        :   **IndexError** â If `pattern_index` is out of range.

    set\_default\_state( : *positions: list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *orientations: list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *\**, : *indices: int | list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, ) → [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None")
    :   Set the default state (positions and orientations) of the prims.

        Backends: usd.

        Hint

        Prims can be reset to their default state by calling the [`reset_to_default_state()`](#isaacsim.sensors.experimental.rtx.StructuredLightCamera.reset_to_default_state "isaacsim.sensors.experimental.rtx.StructuredLightCamera.reset_to_default_state") method.

        Parameters:
        :   * **positions** â Default positions in the world frame (shape `(N, 3)`).
              If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
            * **orientations** â Default orientations in the world frame (shape `(N, 4)`, quaternion `wxyz`).
              If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
            * **indices** â Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

        Raises:
        :   * **AssertionError** â If neither positions nor orientations are specified.
            * **AssertionError** â Wrapped prims are not valid.
            * **AssertionError** â If prims are non-root articulation links.

    set\_local\_poses( : *translations: list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *orientations: list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *\**, : *indices: int | list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, ) → [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None")
    :   Set the poses (translations and orientations) in the local frame of the prims.

        Backends: usd, usdrt, fabric.

        Note

        This method *teleports* prims to the specified poses.

        Parameters:
        :   * **translations** â Translations in the local frame (shape `(N, 3)`).
              If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
            * **orientations** â Orientations in the local frame (shape `(N, 4)`, quaternion `wxyz`).
              If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
            * **indices** â Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

        Raises:
        :   * **AssertionError** â If neither translations nor orientations are specified.
            * **AssertionError** â Wrapped prims are not valid.

        Example:

        ```python
        >>> # set random poses for all prims
        >>> translations = np.random.uniform(low=-1, high=1, size=(3, 3))
        >>> orientations = np.random.randn(3, 4)
        >>> orientations = orientations / np.linalg.norm(orientations, axis=-1, keepdims=True)  # normalize quaternions
        >>> prims.set_local_poses(translations, orientations)
        ```

    set\_local\_scales( : *scales: list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *\**, : *indices: int | list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, ) → [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None")
    :   Set the local scales of the prims.

        Backends: usd, usdrt, fabric.

        Parameters:
        :   * **scales** â Scales to be applied to the prims (shape `(N, 3)`).
              If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
            * **indices** â Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

        Raises:
        :   **AssertionError** â Wrapped prims are not valid.

        Example:

        ```python
        >>> # set random positive scales for all prims
        >>> scales = np.random.uniform(low=0.5, high=1.5, size=(3, 3))
        >>> prims.set_local_scales(scales)
        ```

    set\_projector\_cycle\_period( : *period: tuple[int, int] | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None")*, ) → [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None")
    :   Set the projector cycle period.

        Parameters:
        :   **period** â New cycle period as `(numerator, denominator)`, or `None`
            to mark the period as implicit and re-infer from the current
            timestamps.

        Raises:
        :   **ValueError** â If `period` is not strictly greater than the last timestamp.

    set\_projector\_timestamps( : *timestamps: list[tuple[int, int]]*, ) → [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None")
    :   Replace the projector activation timestamps.

        Behavior depends on how the cycle period was originally set:

        * If the cycle period was **implicit** (inferred from the original
          timestamps), it is re-inferred from the new timestamps.
        * If the cycle period was **explicit** (supplied at construction or via
          [`set_projector_cycle_period()`](#isaacsim.sensors.experimental.rtx.StructuredLightCamera.set_projector_cycle_period "isaacsim.sensors.experimental.rtx.StructuredLightCamera.set_projector_cycle_period")), it is preserved. The call raises
          `ValueError` if the explicit cycle period is no longer strictly
          greater than the new last timestamp.

        After a successful call, the coarse-dt warning is rearmed, the previous
        simulation-time cache is cleared, and pattern 0 is re-activated so the
        next tick starts in a consistent state.

        Parameters:
        :   **timestamps** â New activation times. See class docstring for the schema.

        Raises:
        :   **ValueError** â If `timestamps` is invalid or if an explicit cycle
            period becomes inconsistent with the new timestamps.

    set\_visibilities( : *visibilities: bool | list | np.ndarray | wp.array*, : *\**, : *indices: int | list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, ) → [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None")
    :   Set the visibility state (whether prims are visible or invisible during rendering) of the prims.

        Backends: usd.

        Parameters:
        :   * **visibilities** â Boolean flags to set the visibility state (shape `(N, 1)`).
              If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
            * **indices** â Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

        Raises:
        :   **AssertionError** â Wrapped prims are not valid.

        Example:

        ```python
        >>> # make all prims invisible
        >>> prims.set_visibilities([False])
        >>>
        >>> # make first and last prims invisible
        >>> prims.set_visibilities([True])  # restore visibility from previous call
        >>> prims.set_visibilities([False], indices=[0, 2])
        ```

    set\_world\_poses( : *positions: list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *orientations: list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *\**, : *indices: int | list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, ) → [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None")
    :   Set the poses (positions and orientations) in the world frame of the prims.

        Backends: usd, usdrt, fabric.

        Note

        This method *teleports* prims to the specified poses.

        Parameters:
        :   * **positions** â Positions in the world frame (shape `(N, 3)`).
              If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
            * **orientations** â Orientations in the world frame (shape `(N, 4)`, quaternion `wxyz`).
              If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
            * **indices** â Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

        Raises:
        :   * **AssertionError** â If neither positions nor orientations are specified.
            * **AssertionError** â Wrapped prims are not valid.

        Example:

        ```python
        >>> # set random poses for all prims
        >>> positions = np.random.uniform(low=-1, high=1, size=(3, 3))
        >>> orientations = np.random.randn(3, 4)
        >>> orientations = orientations / np.linalg.norm(orientations, axis=-1, keepdims=True)  # normalize quaternions
        >>> prims.set_world_poses(positions, orientations)
        ```

    *property* aux\_output\_level*: str*
    :   The auxiliary output level configured on the GenericModelOutput RenderVar.

        Returns:
        :   The configured level (e.g. `"NONE"`, `"BASIC"`, `"EXTRA"`, `"FULL"`).

    *property* camera*: [Camera](../../isaacsim.core.experimental.objects/docs/index.html#isaacsim.core.experimental.objects.Camera "isaacsim.core.experimental.objects.impl.camera.Camera")*
    :   Camera object for accessing optical parameters.

        Returns a [`Camera`](../../isaacsim.core.experimental.objects/docs/index.html#isaacsim.core.experimental.objects.Camera "isaacsim.core.experimental.objects.Camera") wrapper over
        the same USD prim, providing access to focal length, clipping range, aperture,
        and other optical properties.

        Returns:
        :   Camera object wrapping the sensor prim.

        Example:

        ```python
        >>> cam = RtxCamera("/World/cam")
        >>> cam.camera.set_focal_lengths(50.0)
        >>> cam.camera.get_focal_lengths()
        ```

    *property* is\_non\_root\_articulation\_link*: bool*
    :   Indicate if the wrapped prims are a non-root link in an articulation tree.

        Backends: usd.

        Warning

        Transformation of the poses of non-root links in an articulation tree are not supported.

        Returns:
        :   Whether the prims are a non-root link in an articulation tree.

    *property* paths*: list[str]*
    :   Prim paths in the stage encapsulated by the wrapper.

        Returns:
        :   List of prim paths as strings.

        Example:

        ```python
        >>> prims.paths
        ['/World/prim_0', '/World/prim_1', '/World/prim_2']
        ```

    *property* prims*: list[pxr.Usd.Prim]*
    :   USD Prim objects encapsulated by the wrapper.

        Returns:
        :   List of USD Prim objects.

        Example:

        ```python
        >>> prims.prims
        [Usd.Prim(</World/prim_0>), Usd.Prim(</World/prim_1>), Usd.Prim(</World/prim_2>)]
        ```

    *property* valid*: bool*
    :   Whether all prims in the wrapper are valid.

        Returns:
        :   True if all prim paths specified in the wrapper correspond to valid prims in stage, False otherwise.

        Example:

        ```python
        >>> prims.valid
        True
        ```

### Sensors

*class* LidarSensor( : *path: str | \_SensorAuthoring*, : *\**, : *annotators: Literal['generic-model-output', 'stable-id-map'] | list[Literal['generic-model-output', 'stable-id-map']] | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *writers: str | list[str] | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *render\_vars: list[str] | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, )
:   Bases: `_SensorRuntime`

    Runtime class for operating a single RTX-based lidar sensor.

    Wraps a [`Lidar`](#isaacsim.sensors.experimental.rtx.Lidar "isaacsim.sensors.experimental.rtx.Lidar") authoring object, attaches Replicator annotators,
    and provides `get_data()` to retrieve sensor output at simulation time.

    Parameters:
    :   * **path** â [`Lidar`](#isaacsim.sensors.experimental.rtx.Lidar "isaacsim.sensors.experimental.rtx.Lidar") object or single path to an existing or non-existing USD OmniLidar prim.
          If a string path is provided, a [`Lidar`](#isaacsim.sensors.experimental.rtx.Lidar "isaacsim.sensors.experimental.rtx.Lidar") instance is created internally.
        * **annotators** â Annotator/sensor types to configure.

    Raises:
    :   * **ValueError** â If no prim is found matching the specified path.
        * **ValueError** â If the input argument refers to more than one prim.
        * **ValueError** â If an unsupported annotator type is specified.

    Example:

    ```python
    >>> import isaacsim.core.experimental.utils.app as app_utils
    >>> from isaacsim.sensors.experimental.rtx import LidarSensor
    >>>
    >>> # given a USD stage with the OmniLidar prim: /World/prim_0
    >>> # and a USD Cube prim: /World/cube
    >>> sensor = LidarSensor(
    ...     "/World/prim_0",
    ...     annotators=["generic-model-output"],
    ... )  
    >>>
    >>> # play the simulation so the sensor can fetch data
    >>> app_utils.play(commit=True)
    ```

    *property* lidar*: [Lidar](#isaacsim.sensors.experimental.rtx.Lidar "isaacsim.sensors.experimental.rtx.impl.lidar.Lidar")*
    :   Lidar object encapsulated by the sensor.

        Returns:
        :   Lidar object encapsulated by the sensor.

        Example:

        ```python
        >>> sensor.lidar
        <isaacsim.sensors.experimental.rtx.impl.lidar.Lidar object at 0x...>
        ```

*class* RadarSensor( : *path: str | \_SensorAuthoring*, : *\**, : *annotators: Literal['generic-model-output', 'stable-id-map'] | list[Literal['generic-model-output', 'stable-id-map']] | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *writers: str | list[str] | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *render\_vars: list[str] | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, )
:   Bases: `_SensorRuntime`

    Runtime class for operating a single RTX-based radar sensor.

    Wraps a [`Radar`](#isaacsim.sensors.experimental.rtx.Radar "isaacsim.sensors.experimental.rtx.Radar") authoring object, attaches Replicator annotators,
    and provides `get_data()` to retrieve sensor output at simulation time.

    Note

    RTX Radar requires Motion BVH to be enabled. The setting
    `/renderer/raytracingMotion/enabled` must be set to `True` before creating the radar prim.

    Parameters:
    :   * **path** â [`Radar`](#isaacsim.sensors.experimental.rtx.Radar "isaacsim.sensors.experimental.rtx.Radar") object or single path to an existing or non-existing USD OmniRadar prim.
          If a string path is provided, a [`Radar`](#isaacsim.sensors.experimental.rtx.Radar "isaacsim.sensors.experimental.rtx.Radar") instance is created internally.
        * **annotators** â Annotator/sensor types to configure.

    Raises:
    :   * **ValueError** â If no prim is found matching the specified path.
        * **ValueError** â If the input argument refers to more than one prim.
        * **ValueError** â If an unsupported annotator type is specified.
        * **RuntimeError** â If Motion BVH is not enabled when creating a new radar prim.

    Example:

    ```python
    >>> import isaacsim.core.experimental.utils.app as app_utils
    >>> from isaacsim.sensors.experimental.rtx import RadarSensor
    >>>
    >>> # given a USD stage with the OmniRadar prim: /World/prim_0
    >>> # and a USD Cube prim: /World/cube
    >>> sensor = RadarSensor(
    ...     "/World/prim_0",
    ...     annotators=["generic-model-output"],
    ... )  
    >>>
    >>> # play the simulation so the sensor can fetch data
    >>> app_utils.play(commit=True)
    ```

    *property* radar*: [Radar](#isaacsim.sensors.experimental.rtx.Radar "isaacsim.sensors.experimental.rtx.impl.radar.Radar")*
    :   Radar object encapsulated by the sensor.

        Returns:
        :   Radar object encapsulated by the sensor.

        Example:

        ```python
        >>> sensor.radar
        <isaacsim.sensors.experimental.rtx.impl.radar.Radar object at 0x...>
        ```

*class* AcousticSensor( : *path: str | \_SensorAuthoring*, : *\**, : *annotators: Literal['generic-model-output', 'stable-id-map'] | list[Literal['generic-model-output', 'stable-id-map']] | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *writers: str | list[str] | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *render\_vars: list[str] | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, )
:   Bases: `_SensorRuntime`

    Runtime class for operating a single RTX-based acoustic sensor.

    Wraps an [`Acoustic`](#isaacsim.sensors.experimental.rtx.Acoustic "isaacsim.sensors.experimental.rtx.Acoustic") authoring object, attaches Replicator annotators,
    and provides `get_data()` to retrieve sensor output at simulation time.

    Parameters:
    :   * **path** â [`Acoustic`](#isaacsim.sensors.experimental.rtx.Acoustic "isaacsim.sensors.experimental.rtx.Acoustic") object or single path to an existing or non-existing USD OmniAcoustic prim.
          If a string path is provided, an [`Acoustic`](#isaacsim.sensors.experimental.rtx.Acoustic "isaacsim.sensors.experimental.rtx.Acoustic") instance is created internally.
        * **annotators** â Annotator/sensor types to configure.

    Raises:
    :   * **ValueError** â If no prim is found matching the specified path.
        * **ValueError** â If the input argument refers to more than one prim.
        * **ValueError** â If an unsupported annotator type is specified.

    Example:

    ```python
    >>> import isaacsim.core.experimental.utils.app as app_utils
    >>> from isaacsim.sensors.experimental.rtx import Acoustic, AcousticSensor
    >>>
    >>> # given a USD stage with the OmniAcoustic prim: /World/prim_0
    >>> # and a USD Cube prim: /World/cube
    >>> acoustic = Acoustic("/World/prim_0", aux_output_level="BASIC")
    >>> sensor = AcousticSensor(
    ...     acoustic,
    ...     annotators=["generic-model-output"],
    ... )  
    >>>
    >>> # play the simulation so the sensor can fetch data
    >>> app_utils.play(commit=True)
    ```

    *property* acoustic*: [Acoustic](#isaacsim.sensors.experimental.rtx.Acoustic "isaacsim.sensors.experimental.rtx.impl.acoustic.Acoustic")*
    :   Acoustic object encapsulated by the sensor.

        Returns:
        :   Acoustic object encapsulated by the sensor.

        Example:

        ```python
        >>> sensor.acoustic
        <isaacsim.sensors.experimental.rtx.impl.acoustic.Acoustic object at 0x...>
        ```

*class* CameraSensor( : *path: str | [RtxCamera](#isaacsim.sensors.experimental.rtx.RtxCamera "isaacsim.sensors.experimental.rtx.impl.rtx_camera.RtxCamera")*, : *\**, : *resolution: tuple[int, int]*, : *annotators: Literal['bounding\_box\_2d\_loose', 'bounding\_box\_2d\_tight', 'bounding\_box\_3d', 'distance\_to\_camera', 'distance\_to\_image\_plane', 'instance\_id\_segmentation', 'instance\_segmentation', 'motion\_vectors', 'normals', 'pointcloud', 'rgb', 'rgba', 'semantic\_segmentation'] | list[Literal['bounding\_box\_2d\_loose', 'bounding\_box\_2d\_tight', 'bounding\_box\_3d', 'distance\_to\_camera', 'distance\_to\_image\_plane', 'instance\_id\_segmentation', 'instance\_segmentation', 'motion\_vectors', 'normals', 'pointcloud', 'rgb', 'rgba', 'semantic\_segmentation']] | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *writers: str | list[str] | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *render\_vars: list[str] | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, )
:   Bases: `_SensorRuntime`

    High level class for creating/wrapping and operating single camera sensor.

    Parameters:
    :   * **path** â [`RtxCamera`](#isaacsim.sensors.experimental.rtx.RtxCamera "isaacsim.sensors.experimental.rtx.RtxCamera") object or single path to existing or non-existing USD Camera prim.
          If a string path is provided, a [`RtxCamera`](#isaacsim.sensors.experimental.rtx.RtxCamera "isaacsim.sensors.experimental.rtx.RtxCamera") instance is created internally.
        * **resolution** â Resolution of the sensor (following OpenCV/NumPy convention: `(height, width)`).
        * **annotators** â Annotator/sensor types to configure.

    Raises:
    :   * **ValueError** â If no prim is found matching the specified path.
        * **ValueError** â If the input argument refers to more than one camera prim.
        * **ValueError** â If an unsupported annotator type is specified.

    Example:

    ```python
    >>> import isaacsim.core.experimental.utils.app as app_utils
    >>> from isaacsim.sensors.experimental.rtx import CameraSensor
    >>>
    >>> # given a USD stage with the Camera prim: /World/prim_0
    >>> resolution = (240, 320)  # following OpenCV/NumPy convention `(height, width)`
    >>> camera_sensor = CameraSensor(
    ...     "/World/prim_0",
    ...     resolution=resolution,
    ...     annotators=["rgb", "distance_to_image_plane"],
    ... )  
    >>>
    >>> # play the simulation so the sensor can fetch data
    >>> app_utils.play(commit=True)
    ```

    attach\_annotators(*annotators: str | list[str]*) → [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None")
    :   Attach annotators to the sensor.

        Parameters:
        :   **annotators** â Annotator/sensor types to attach.

        Raises:
        :   **ValueError** â If the specified annotator is not supported.

    get\_data( : *annotator: str*, : *\**, : *out: wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, ) → tuple[wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None"), dict[str, Any]]
    :   Fetch the specified annotator/sensor data for the camera.

        Parameters:
        :   * **annotator** â Annotator/sensor type from which fetch the data.
            * **out** â Pre-allocated array to fill with the fetched data.

        Returns:
        :   Two-elements tuple. 1) Array containing the fetched data.
            If no data is available at the moment of calling the method, `None` is returned.
            2) Dictionary containing additional information according to the requested annotator/sensor.

        Raises:
        :   * **ValueError** â If the specified annotator is not supported.
            * **ValueError** â If the specified annotator is not configured.

    *property* camera*: Any*
    :   Camera object for accessing optical parameters.

        Returns:
        :   Camera object wrapping the sensor prim.

    *property* resolution*: tuple[int, int]*
    :   Resolution of the sensor.

        Returns:
        :   `(height, width)`).

        Return type:
        :   Resolution of sensor frames (following OpenCV/NumPy convention

*class* SingleViewDepthCameraSensor( : *path: str | [RtxCamera](#isaacsim.sensors.experimental.rtx.RtxCamera "isaacsim.sensors.experimental.rtx.impl.rtx_camera.RtxCamera")*, : *\**, : *resolution: tuple[int, int]*, : *annotators: Literal['bounding\_box\_2d\_loose', 'bounding\_box\_2d\_tight', 'bounding\_box\_3d', 'distance\_to\_camera', 'distance\_to\_image\_plane', 'instance\_id\_segmentation', 'instance\_segmentation', 'motion\_vectors', 'normals', 'pointcloud', 'semantic\_segmentation', 'depth\_sensor\_distance', 'depth\_sensor\_imager', 'depth\_sensor\_point\_cloud\_color', 'depth\_sensor\_point\_cloud\_position'] | list[Literal['bounding\_box\_2d\_loose', 'bounding\_box\_2d\_tight', 'bounding\_box\_3d', 'distance\_to\_camera', 'distance\_to\_image\_plane', 'instance\_id\_segmentation', 'instance\_segmentation', 'motion\_vectors', 'normals', 'pointcloud', 'semantic\_segmentation', 'depth\_sensor\_distance', 'depth\_sensor\_imager', 'depth\_sensor\_point\_cloud\_color', 'depth\_sensor\_point\_cloud\_position']]*, )
:   Bases: [`CameraSensor`](#isaacsim.sensors.experimental.rtx.CameraSensor "isaacsim.sensors.experimental.rtx.impl.camera_sensor.CameraSensor")

    High level class for creating/wrapping and operating single view depth camera sensor.

    The sensor is modeled using a single camera view to simulate a stereo camera pair and compute disparity and depth.
    The sensor is implemented as a post-process operation in the renderer, where the OmniSensorDepthSensorSingleViewAPI
    schema is applied to the USD render product prim rather than to the camera prim.

    Parameters:
    :   * **path** â `Camera` object or single path to existing or non-existing (one of both) USD Camera prim.
          Can include regular expression for matching a prim.
        * **resolution** â Resolution of the sensor (following OpenCV/NumPy convention: `(height, width)`).
        * **annotators** â Annotator/sensor types to configure.

    Raises:
    :   * **ValueError** â If no prim is found matching the specified path.
        * **ValueError** â If the input argument refers to more than one camera prim.
        * **ValueError** â If an unsupported annotator type is specified.

    Example:

    ```python
    >>> import isaacsim.core.experimental.utils.app as app_utils
    >>> from isaacsim.sensors.experimental.rtx import SingleViewDepthCameraSensor
    >>>
    >>> # given a USD stage with the Camera prim: /World/prim_0
    >>> resolution = (240, 320)  # following OpenCV/NumPy convention `(height, width)`
    >>> camera_sensor = SingleViewDepthCameraSensor(
    ...     "/World/prim_0",
    ...     resolution=resolution,
    ...     annotators="depth_sensor_distance",
    ... )  
    >>>
    >>> # play the simulation so the sensor can fetch data
    >>> app_utils.play(commit=True)
    ```

    *static* add\_template\_render\_product( : *parent\_prim\_path: str*, : *camera\_prim\_path: str*, : *\*\*kwargs: Any*, ) → pxr.Usd.Prim
    :   Add a template render product for a depth sensor to the USD stage.

        Creates a `RenderProduct` prim with `OmniSensorDepthSensorSingleViewAPI` applied and a
        `camera` relationship pointing to the given camera prim. The render product is created as
        a child of `parent_prim_path` and is named `<camera_name>_render_product`.

        This is used when building a depth camera USD asset for later use with
        [`SingleViewDepthCameraSensor`](#isaacsim.sensors.experimental.rtx.SingleViewDepthCameraSensor "isaacsim.sensors.experimental.rtx.SingleViewDepthCameraSensor"). When the asset is loaded via
        [`RtxCamera.create()`](#isaacsim.sensors.experimental.rtx.RtxCamera.create "isaacsim.sensors.experimental.rtx.RtxCamera.create"), `SingleViewDepthCameraSensor` automatically detects the
        embedded render product and copies its depth sensor attributes onto the dynamically
        created render product.

        Parameters:
        :   * **parent\_prim\_path** â USD path to the parent prim under which the `RenderProduct` will
              be created (trailing slash is stripped automatically).
            * **camera\_prim\_path** â USD path to the `Camera` prim to associate with the
              `RenderProduct`.
            * **\*\*kwargs** â Depth sensor attribute names and values to set on the `RenderProduct`
              (e.g. `omni:rtx:post:depthSensor:baselineMM=42`). A warning is logged for
              any key that does not correspond to an existing attribute on the prim.

        Returns:
        :   The created `RenderProduct` prim, or an invalid `pxr.Usd.Prim` if
            creation failed.

        Example:

        ```python
        >>> SingleViewDepthCameraSensor.add_template_render_product(
        ...     parent_prim_path="/root/TemplateRenderProduct",
        ...     camera_prim_path="/root/Camera",
        ...     **{"omni:rtx:post:depthSensor:baselineMM": 42},
        ... )
        ```

    get\_enabled\_outlier\_removal() → bool
    :   Get the enabled state of the outlier removal filter of the depth sensor.

        Filter out single pixel samples caused by antialiasing jitter and reprojection resolution.

        Returns:
        :   Boolean flag indicating if the outlier removal filter is enabled.

        Example:

        ```python
        >>> camera_sensor.get_enabled_outlier_removal()
        True
        ```

    get\_enabled\_post\_processing() → bool
    :   Get the enabled state of the post-process operation for depth sensing in the renderer of the prims.

        Returns:
        :   Boolean flag indicating if the depth sensor post-process is enabled.

        Example:

        ```python
        >>> camera_sensor.get_enabled_post_processing()
        True
        ```

    get\_sensor\_baseline() → float
    :   Get the distance between the simulated depth camera sensor, in millimeters.

        Larger positive/negative values will increase the unknown black/hole regions around objects
        where the depth camera sensor cannot see.

        Returns:
        :   The distance between the simulated depth camera sensor, in millimeters.

        Example:

        ```python
        >>> camera_sensor.get_sensor_baseline()
        55.0
        ```

    get\_sensor\_disparity\_confidence() → float
    :   Get the confidence threshold for the depth sensor.

        Control how likely a depth sample is considered valid. Higher values make depth values vary wider across
        the quantization (noise mean) range.

        Returns:
        :   The confidence threshold for the depth sensor.

        Example:

        ```python
        >>> camera_sensor.get_sensor_disparity_confidence()
         0.6999...
        ```

    get\_sensor\_disparity\_noise\_downscale() → float
    :   Get the coarseness of the disparity noise, in pixels, of the depth sensor.

        Higher values reduce the spatial resolution of the noise.

        Returns:
        :   The disparity noise downscale factor, in pixels.

        Example:

        ```python
        >>> camera_sensor.get_sensor_disparity_noise_downscale()
        1.0
        ```

    get\_sensor\_distance\_cutoffs() → tuple[float, float]
    :   Get the cutoff range (minimum and maximum distance) of the depth sensor.

        Returns:
        :   The minimum cutoff distance.
            The maximum cutoff distance.

        Example:

        ```python
        >>> camera_sensor.get_sensor_distance_cutoffs()
        (0.5, 10000000.0)
        ```

    get\_sensor\_focal\_length() → float
    :   Get the simulated focal length of the depth sensor, in pixels.

        Combined with the sensor size, this sets the field of view for the disparity calculation.
        Since the actual FOV is controlled on the camera prim, this only adjusts the amount of
        left/right disparity. Lower focal length decreases disparity.

        Returns:
        :   The sensor focal length, in pixels.

        Example:

        ```python
        >>> camera_sensor.get_sensor_focal_length()
        897.0
        ```

    get\_sensor\_maximum\_disparity() → float
    :   Get the maximum number of disparity pixels for the depth sensor.

        Higher values allow the sensor to resolve closer (more disparate) objects.
        Lower values reduce the depth sensing range.

        Returns:
        :   The maximum number of disparity pixels for the depth sensor.

        Example:

        ```python
        >>> camera_sensor.get_sensor_maximum_disparity()
        110.0
        ```

    get\_sensor\_noise\_parameters() → tuple[float, float]
    :   Get the quantization factor (mean and sigma) for the disparity noise, in pixels, of the depth sensor.

        Returns:
        :   Two-elements tuple. 1) The disparity noise mean value, in pixels.
            2) The disparity noise sigma value, in pixels.

        Example:

        ```python
        >>> camera_sensor.get_sensor_noise_parameters()
        (0.25, 0.25)
        ```

    get\_sensor\_output\_mode() → int
    :   Get the output mode used to override the LDRColor buffer with a debug visualization of the depth sensor.

        Supported modes:

        * `0`: Pass through LDRColor.
        * `1`: Repeated 1 meter grayscale gradient.
        * `2`: Grayscale gradient over min/max distance.
        * `3`: Rainbow gradient over min/max distance.
        * `4`: Input Depth values in grayscale.
        * `5`: Reprojected depth with confidence culling applied.
        * `6`: Confidence Map with Disparity.
        * `7`: Disparity values in grayscale.

        Returns:
        :   The output mode.

        Example:

        ```python
        >>> camera_sensor.get_sensor_output_mode()
        0
        ```

    get\_sensor\_size() → float
    :   Get the size of the sensor, in pixels, of the depth sensor.

        Combined with focal length, this affects the amount of disparity. Higher values decrease disparity.

        Returns:
        :   The sensor size, in pixels.

        Example:

        ```python
        >>> camera_sensor.get_sensor_size()
        1280.0
        ```

    set\_enabled\_outlier\_removal( : *enabled: bool*, ) → [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None")
    :   Enable or disable the outlier removal filter of the depth sensor.

        Filter out single pixel samples caused by antialiasing jitter and reprojection resolution.

        Parameters:
        :   **enabled** â Boolean flag to enable/disable outlier removal.

        Example:

        ```python
        >>> camera_sensor.set_enabled_outlier_removal(True)
        ```

    set\_enabled\_post\_processing( : *enabled: bool*, ) → [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None")
    :   Enable or disable the post-process operation for depth sensing in the renderer.

        Parameters:
        :   **enabled** â Boolean flag to enable/disable the depth sensor post-process.

        Example:

        ```python
        >>> camera_sensor.set_enabled_post_processing(True)
        ```

    set\_sensor\_baseline( : *baseline: float*, ) → [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None")
    :   Set the distance between the simulated depth camera sensor, in millimeters.

        Larger positive/negative values will increase the unknown black/hole regions around objects
        where the camera sensor cannot see.

        Parameters:
        :   **baseline** â Sensor baseline in millimeters.

        Example:

        ```python
        >>> camera_sensor.set_sensor_baseline(50.0)
        ```

    set\_sensor\_disparity\_confidence( : *confidence\_threshold: float*, ) → [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None")
    :   Set the confidence threshold for the depth sensor.

        Control how likely a depth sample is considered valid. Higher values make depth values vary wider across
        the quantization (noise mean) range.

        Parameters:
        :   **confidence\_threshold** â Confidence threshold.

        Example:

        ```python
        >>> camera_sensor.set_sensor_disparity_confidence(0.75)
        ```

    set\_sensor\_disparity\_noise\_downscale( : *downscale: float*, ) → [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None")
    :   Set the coarseness of the disparity noise, in pixels, of the depth sensor.

        Higher values reduce the spatial resolution of the noise.

        Parameters:
        :   **downscale** â Disparity noise downscale factor in pixels.

        Example:

        ```python
        >>> camera_sensor.set_sensor_disparity_noise_downscale(1.5)
        ```

    set\_sensor\_distance\_cutoffs( : *minimum\_distance: float = None*, : *maximum\_distance: float = None*, ) → [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None")
    :   Set the cutoff range (minimum and maximum distance) of the depth sensor.

        Parameters:
        :   * **minimum\_distance** â Minimum cutoff distance.
            * **maximum\_distance** â Maximum cutoff distance.

        Raises:
        :   **ValueError** â If both `minimum_distance` and `maximum_distance` are not defined.

        Example:

        ```python
        >>> camera_sensor.set_sensor_distance_cutoffs(minimum_distance=0.1, maximum_distance=1000000.0)
        ```

    set\_sensor\_focal\_length( : *focal\_length: float*, ) → [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None")
    :   Set the simulated focal length of the depth sensor, in pixels.

        Combined with the sensor size, this sets the field of view for the disparity calculation.
        Since the actual FOV is controlled on the camera prim, this only adjusts the amount of
        left/right disparity. Lower focal length decreases disparity.

        Parameters:
        :   **focal\_length** â Sensor focal length in pixels.

        Example:

        ```python
        >>> camera_sensor.set_sensor_focal_length(800.0)
        ```

    set\_sensor\_maximum\_disparity( : *maximum\_disparity: float*, ) → [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None")
    :   Set the maximum number of disparity pixels for the depth sensor.

        Higher values allow the sensor to resolve closer (more disparate) objects.
        Lower values reduce the depth sensing range.

        Parameters:
        :   **maximum\_disparity** â Maximum disparity.

        Example:

        ```python
        >>> camera_sensor.set_sensor_maximum_disparity(120.0)
        ```

    set\_sensor\_noise\_parameters( : *noise\_mean: float = None*, : *noise\_sigma: float = None*, ) → [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None")
    :   Set the quantization factor (mean and sigma) for the disparity noise, in pixels, of the depth sensor.

        Higher mean values reduce depth resolution. Higher sigma values make depth values vary wider
        across the quantization (noise mean) range.

        Parameters:
        :   * **noise\_mean** â Disparity noise mean value in pixels.
            * **noise\_sigma** â Disparity noise sigma value in pixels.

        Raises:
        :   **AssertionError** â If neither `noise_mean` nor `noise_sigma` are specified.

        Example:

        ```python
        >>> camera_sensor.set_sensor_noise_parameters(noise_mean=0.5, noise_sigma=0.1)
        ```

    set\_sensor\_output\_mode(*mode: int*) → [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None")
    :   Set the output mode to override the LDRColor buffer with a debug visualization of the depth sensor.

        Supported modes:

        * `0`: Pass through LDRColor.
        * `1`: Repeated 1 meter grayscale gradient.
        * `2`: Grayscale gradient over min/max distance.
        * `3`: Rainbow gradient over min/max distance.
        * `4`: Input Depth values in grayscale.
        * `5`: Reprojected depth with confidence culling applied.
        * `6`: Confidence Map with Disparity.
        * `7`: Disparity values in grayscale.

        Parameters:
        :   **mode** â Output mode.

        Example:

        ```python
        >>> camera_sensor.set_sensor_output_mode(0)  # pass through LDRColor
        ```

    set\_sensor\_size(*size: float*) → [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None")
    :   Set the size of the sensor, in pixels, of the depth sensor.

        Combined with focal length, this affects the amount of disparity. Higher values decrease disparity.

        Parameters:
        :   **size** â Sensor size, in pixels.

        Example:

        ```python
        >>> camera_sensor.set_sensor_size(1920.0)
        ```

*class* TiledCameraSensor( : *paths: str | list[str] | [Camera](../../isaacsim.core.experimental.objects/docs/index.html#isaacsim.core.experimental.objects.Camera "isaacsim.core.experimental.objects.impl.camera.Camera")*, : *\**, : *resolution: tuple[int, int]*, : *annotators: Literal['distance\_to\_camera', 'distance\_to\_image\_plane', 'instance\_id\_segmentation', 'instance\_segmentation', 'motion\_vectors', 'normals', 'rgb', 'rgba', 'semantic\_segmentation'] | list[Literal['distance\_to\_camera', 'distance\_to\_image\_plane', 'instance\_id\_segmentation', 'instance\_segmentation', 'motion\_vectors', 'normals', 'rgb', 'rgba', 'semantic\_segmentation']]*, : *render\_vars: list[str] | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, )
:   Bases: `object`

    High level class for creating/wrapping and operating tiled (batched) camera sensors.

    Parameters:
    :   * **paths** â `Camera` object, single path or list of paths to existing or non-existing (one of both) USD Camera prims.
          Can include regular expressions for matching multiple prims.
        * **resolution** â Resolution of each individual sensor (following OpenCV/NumPy convention: `(height, width)`).
        * **annotators** â Annotator/sensor types to configure.

    Raises:
    :   * **ValueError** â If no prims are found matching the specified paths.
        * **ValueError** â If an unsupported annotator type is specified.

    Example:

    ```python
    >>> import isaacsim.core.experimental.utils.app as app_utils
    >>> from isaacsim.sensors.experimental.rtx import TiledCameraSensor
    >>>
    >>> # given a USD stage with the Camera prims: /World/prim_0, /World/prim_1, and /World/prim_2
    >>> resolution = (240, 320)  # following OpenCV/NumPy convention `(height, width)`
    >>> tiled_camera_sensor = TiledCameraSensor(
    ...     "/World/prim_.*",
    ...     resolution=resolution,
    ...     annotators=["rgb", "distance_to_image_plane"],
    ... )  
    >>>
    >>> # play the simulation so the sensor can fetch data
    >>> app_utils.play(commit=True)
    ```

    attach\_annotators( : *annotators: str | list[str]*, ) → [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None")
    :   Attach annotators to the sensor.

        Parameters:
        :   **annotators** â Annotator/sensor types to attach.

        Raises:
        :   **ValueError** â If the specified annotator is not supported.

        Example:

        ```python
        >>> tiled_camera_sensor.annotators
        ['distance_to_image_plane', 'rgb']
        >>> tiled_camera_sensor.attach_annotators("normals")
        >>> tiled_camera_sensor.annotators
        ['distance_to_image_plane', 'normals', 'rgb']
        ```

    detach\_annotators( : *annotators: str | list[str]*, ) → [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None")
    :   Detach annotators from the sensor.

        Parameters:
        :   **annotators** â Annotator/sensor types to detach. If the annotator is not attached,
            or it has already been detached, a warning is logged and the method does nothing.

        Raises:
        :   **ValueError** â If the specified annotator is not supported.

        Example:

        ```python
        >>> tiled_camera_sensor.annotators
        ['distance_to_image_plane', 'normals', 'rgb']
        >>> tiled_camera_sensor.detach_annotators(["distance_to_image_plane", "normals"])
        >>> tiled_camera_sensor.annotators
        ['rgb']
        ```

    get\_data( : *annotator: str*, : *\**, : *tiled: bool = False*, : *out: wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, ) → tuple[wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None"), dict[str, Any]]
    :   Fetch the specified annotator/sensor data for all cameras as a batch of frames or as a single tiled frame.

        Parameters:
        :   * **annotator** â Annotator/sensor type from which fetch the data.
            * **tiled** â Whether to get annotator/sensor data as a single tiled frame.
            * **out** â Pre-allocated array to fill with the fetched data.

        Returns:
        :   Two-elements tuple. 1) Array containing the fetched data. If `out` is defined, such instance is returned
            filled with the data. If no data is available at the moment of calling the method, `None` is returned.
            2) Dictionary containing additional information according to the requested annotator/sensor.

        Raises:
        :   * **ValueError** â If the specified annotator is not supported.
            * **ValueError** â If the specified annotator is not configured when instantiating the object.

        Example:

        ```python
        >>> data, info = tiled_camera_sensor.get_data("rgb")  
        >>> data.shape  
        (3, 240, 320, 3)
        >>> info
        {}
        ```

    *property* annotators*: list[str]*
    :   Annotators.

        Returns:
        :   Sorted list of registered annotators.

        Example:

        ```python
        >>> tiled_camera_sensor.annotators
        ['distance_to_image_plane', 'rgb']
        ```

    *property* camera*: [Camera](../../isaacsim.core.experimental.objects/docs/index.html#isaacsim.core.experimental.objects.Camera "isaacsim.core.experimental.objects.impl.camera.Camera")*
    :   Camera object encapsulated by the sensor.

        Returns:
        :   Camera object encapsulated by the sensor.

        Example:

        ```python
        >>> tiled_camera_sensor.camera
        <isaacsim.core.experimental.objects.impl.camera.Camera object at 0x...>
        ```

    *property* render\_product*: pxr.UsdRender.Product*
    :   Render product.

        Returns:
        :   Render product of the tiled camera sensor.

        Example:

        ```python
        >>> tiled_camera_sensor.render_product
        UsdRender.Product(Usd.Prim(</Render/OmniverseKit/HydraTextures/tiled_camera_sensor_...>))
        ```

    *property* resolution*: tuple[int, int]*
    :   Resolution of individual batched frames.

        Returns:
        :   `(height, width)`).

        Return type:
        :   Resolution of individual batched frames (following OpenCV/NumPy convention

        Example:

        ```python
        >>> tiled_camera_sensor.resolution
        (240, 320)
        ```

    *property* tiled\_resolution*: tuple[int, int]*
    :   Resolution of tiled frames.

        Returns:
        :   `(height, width)`).

        Return type:
        :   Resolution of tiled frames (following OpenCV/NumPy convention

        Example:

        ```python
        >>> tiled_camera_sensor.tiled_resolution
        (480, 640)
        ```

### Utils

parse\_generic\_model\_output\_data( : *data: warp.array*, ) → GenericModelOutput
:   Parse generic model output structure from annotator data.

    Parameters:
    :   **data** â generic-model-output data from an annotator.

    Returns:
    :   Generic model output structure.

    Example:

    ```python
    >>> import isaacsim.core.experimental.utils.app as app_utils
    >>> import isaacsim.core.experimental.utils.stage as stage_utils
    >>> from isaacsim.sensors.experimental.rtx import LidarSensor, parse_generic_model_output_data
    >>>
    >>> stage_utils.define_prim("/World/sphere", "Sphere") 
    >>> sensor = LidarSensor("/World/lidar", annotators=["generic-model-output"]) 
    >>>
    >>> # play the simulation so the sensor can fetch data
    >>> app_utils.play(commit=True)
    >>>
    >>> data, _ = sensor.get_data("generic-model-output") 
    >>> parse_generic_model_output_data(data) 
    <generic_model_output.GenericModelOutput object at 0x...>
    ```

parse\_stable\_id\_map\_data(*data: warp.array*) → dict
:   Parse Stable ID Map data from annotator data.

    Parameters:
    :   **data** â stable-id-map annotator data.

    Returns:
    :   Dictionary mapping stable IDs to their prim paths.

    Warning

    Some object IDs returned by the LiDAR may not have an entry in
    this map. The renderer emits each 128-bit stable ID as a
    per-instance base ID combined with an âupper indexâ in the high
    32 bits â the submesh index for mesh geometry and the per-triangle
    primitive index for procedural geometry. The map registers per-
    instance entries and (when `subsetCount > 1`) per-`GeomSubset`
    entries, but it does **not** register per-primitive entries, so
    hits on procedural geometry, on submeshes that werenât expanded,
    or on renderer-internal instances without a USD prim path will
    produce IDs with no map entry, and a direct `map[id]` lookup
    will raise `KeyError`. Use `map.get(id, "<unknown>")` to
    handle missing IDs gracefully â see the bundled
    `resolve_lidar_object_ids.py` example for the recommended
    pattern.

    Example:

    ```python
    >>> import isaacsim.core.experimental.utils.app as app_utils
    >>> import isaacsim.core.experimental.utils.stage as stage_utils
    >>> from isaacsim.sensors.experimental.rtx import LidarSensor, parse_stable_id_map_data
    >>>
    >>> stage_utils.define_prim("/World/sphere", "Sphere") 
    >>> sensor = LidarSensor("/World/lidar", annotators=["stable-id-map"]) 
    >>>
    >>> # play the simulation so the sensor can fetch data
    >>> app_utils.play(commit=True)
    >>>
    >>> data, _ = sensor.get_data("stable-id-map") 
    >>> parse_stable_id_map_data(data) 
    {0: '/World/sphere'}
    ```

### Lidar configuration registry

SUPPORTED\_LIDAR\_CONFIGS
:   Mapping from known Isaac Sim lidar asset paths to optional variant name sets.

SUPPORTED\_LIDAR\_VARIANT\_SET\_NAME
:   Variant set name expected on supported lidar prims.

On this page

* [Overview](#overview)
  + [Key Components](#key-components)
    - [Authoring classes](#authoring-classes)
    - [Runtime sensor classes](#runtime-sensor-classes)
    - [Lidar configuration registry](#lidar-configuration-registry)
    - [Parser utilities](#parser-utilities)
    - [Auxiliary modules](#auxiliary-modules)
    - [Settings](#settings)
  + [Code examples](#code-examples)
    - [Lidar](#lidar)
    - [Radar](#radar)
    - [Acoustic](#acoustic)
    - [Camera](#camera)
    - [Camera with lens distortion](#camera-with-lens-distortion)
  + [Known warnings](#known-warnings)
  + [Integration](#integration)
* [Enable Extension](#enable-extension)
  + [Settings](#settings)
    - [Settings Provided by the Extension](#settings-provided-by-the-extension)
      * [app.sensors.nv.lidar.outputBufferOnGPU](#app-sensors-nv-lidar-outputbufferongpu)
      * [app.sensors.nv.radar.outputBufferOnGPU](#app-sensors-nv-radar-outputbufferongpu)
      * [rtx.materialDb.nonVisualMaterialCSV.enabled](#rtx-materialdb-nonvisualmaterialcsv-enabled)
      * [rtx.materialDb.nonVisualMaterialSemantics.prefix](#rtx-materialdb-nonvisualmaterialsemantics-prefix)
      * [rtx.rtxsensor.useHydraTimeAlways](#rtx-rtxsensor-usehydratimealways)
* [Annotators](#annotators)
  + [Standard Annotators](#standard-annotators)
* [Python API](#python-api)
  + [Authoring](#authoring)
    - [`Lidar`](#isaacsim.sensors.experimental.rtx.Lidar)
      * [`apply_visual_materials()`](#isaacsim.sensors.experimental.rtx.Lidar.apply_visual_materials)
      * [`create()`](#isaacsim.sensors.experimental.rtx.Lidar.create)
      * [`ensure_api()`](#isaacsim.sensors.experimental.rtx.Lidar.ensure_api)
      * [`get_applied_visual_materials()`](#isaacsim.sensors.experimental.rtx.Lidar.get_applied_visual_materials)
      * [`get_default_state()`](#isaacsim.sensors.experimental.rtx.Lidar.get_default_state)
      * [`get_local_poses()`](#isaacsim.sensors.experimental.rtx.Lidar.get_local_poses)
      * [`get_local_scales()`](#isaacsim.sensors.experimental.rtx.Lidar.get_local_scales)
      * [`get_visibilities()`](#isaacsim.sensors.experimental.rtx.Lidar.get_visibilities)
      * [`get_world_poses()`](#isaacsim.sensors.experimental.rtx.Lidar.get_world_poses)
      * [`reset_to_default_state()`](#isaacsim.sensors.experimental.rtx.Lidar.reset_to_default_state)
      * [`reset_xform_op_properties()`](#isaacsim.sensors.experimental.rtx.Lidar.reset_xform_op_properties)
      * [`resolve_paths()`](#isaacsim.sensors.experimental.rtx.Lidar.resolve_paths)
      * [`set_default_state()`](#isaacsim.sensors.experimental.rtx.Lidar.set_default_state)
      * [`set_local_poses()`](#isaacsim.sensors.experimental.rtx.Lidar.set_local_poses)
      * [`set_local_scales()`](#isaacsim.sensors.experimental.rtx.Lidar.set_local_scales)
      * [`set_visibilities()`](#isaacsim.sensors.experimental.rtx.Lidar.set_visibilities)
      * [`set_world_poses()`](#isaacsim.sensors.experimental.rtx.Lidar.set_world_poses)
      * [`aux_output_level`](#isaacsim.sensors.experimental.rtx.Lidar.aux_output_level)
      * [`is_non_root_articulation_link`](#isaacsim.sensors.experimental.rtx.Lidar.is_non_root_articulation_link)
      * [`paths`](#isaacsim.sensors.experimental.rtx.Lidar.paths)
      * [`prims`](#isaacsim.sensors.experimental.rtx.Lidar.prims)
      * [`valid`](#isaacsim.sensors.experimental.rtx.Lidar.valid)
    - [`Radar`](#isaacsim.sensors.experimental.rtx.Radar)
      * [`apply_visual_materials()`](#isaacsim.sensors.experimental.rtx.Radar.apply_visual_materials)
      * [`create()`](#isaacsim.sensors.experimental.rtx.Radar.create)
      * [`ensure_api()`](#isaacsim.sensors.experimental.rtx.Radar.ensure_api)
      * [`get_applied_visual_materials()`](#isaacsim.sensors.experimental.rtx.Radar.get_applied_visual_materials)
      * [`get_default_state()`](#isaacsim.sensors.experimental.rtx.Radar.get_default_state)
      * [`get_local_poses()`](#isaacsim.sensors.experimental.rtx.Radar.get_local_poses)
      * [`get_local_scales()`](#isaacsim.sensors.experimental.rtx.Radar.get_local_scales)
      * [`get_visibilities()`](#isaacsim.sensors.experimental.rtx.Radar.get_visibilities)
      * [`get_world_poses()`](#isaacsim.sensors.experimental.rtx.Radar.get_world_poses)
      * [`reset_to_default_state()`](#isaacsim.sensors.experimental.rtx.Radar.reset_to_default_state)
      * [`reset_xform_op_properties()`](#isaacsim.sensors.experimental.rtx.Radar.reset_xform_op_properties)
      * [`resolve_paths()`](#isaacsim.sensors.experimental.rtx.Radar.resolve_paths)
      * [`set_default_state()`](#isaacsim.sensors.experimental.rtx.Radar.set_default_state)
      * [`set_local_poses()`](#isaacsim.sensors.experimental.rtx.Radar.set_local_poses)
      * [`set_local_scales()`](#isaacsim.sensors.experimental.rtx.Radar.set_local_scales)
      * [`set_visibilities()`](#isaacsim.sensors.experimental.rtx.Radar.set_visibilities)
      * [`set_world_poses()`](#isaacsim.sensors.experimental.rtx.Radar.set_world_poses)
      * [`aux_output_level`](#isaacsim.sensors.experimental.rtx.Radar.aux_output_level)
      * [`is_non_root_articulation_link`](#isaacsim.sensors.experimental.rtx.Radar.is_non_root_articulation_link)
      * [`paths`](#isaacsim.sensors.experimental.rtx.Radar.paths)
      * [`prims`](#isaacsim.sensors.experimental.rtx.Radar.prims)
      * [`valid`](#isaacsim.sensors.experimental.rtx.Radar.valid)
    - [`Acoustic`](#isaacsim.sensors.experimental.rtx.Acoustic)
      * [`apply_visual_materials()`](#isaacsim.sensors.experimental.rtx.Acoustic.apply_visual_materials)
      * [`create()`](#isaacsim.sensors.experimental.rtx.Acoustic.create)
      * [`ensure_api()`](#isaacsim.sensors.experimental.rtx.Acoustic.ensure_api)
      * [`get_applied_visual_materials()`](#isaacsim.sensors.experimental.rtx.Acoustic.get_applied_visual_materials)
      * [`get_default_state()`](#isaacsim.sensors.experimental.rtx.Acoustic.get_default_state)
      * [`get_local_poses()`](#isaacsim.sensors.experimental.rtx.Acoustic.get_local_poses)
      * [`get_local_scales()`](#isaacsim.sensors.experimental.rtx.Acoustic.get_local_scales)
      * [`get_visibilities()`](#isaacsim.sensors.experimental.rtx.Acoustic.get_visibilities)
      * [`get_world_poses()`](#isaacsim.sensors.experimental.rtx.Acoustic.get_world_poses)
      * [`reset_to_default_state()`](#isaacsim.sensors.experimental.rtx.Acoustic.reset_to_default_state)
      * [`reset_xform_op_properties()`](#isaacsim.sensors.experimental.rtx.Acoustic.reset_xform_op_properties)
      * [`resolve_paths()`](#isaacsim.sensors.experimental.rtx.Acoustic.resolve_paths)
      * [`set_default_state()`](#isaacsim.sensors.experimental.rtx.Acoustic.set_default_state)
      * [`set_local_poses()`](#isaacsim.sensors.experimental.rtx.Acoustic.set_local_poses)
      * [`set_local_scales()`](#isaacsim.sensors.experimental.rtx.Acoustic.set_local_scales)
      * [`set_visibilities()`](#isaacsim.sensors.experimental.rtx.Acoustic.set_visibilities)
      * [`set_world_poses()`](#isaacsim.sensors.experimental.rtx.Acoustic.set_world_poses)
      * [`aux_output_level`](#isaacsim.sensors.experimental.rtx.Acoustic.aux_output_level)
      * [`is_non_root_articulation_link`](#isaacsim.sensors.experimental.rtx.Acoustic.is_non_root_articulation_link)
      * [`paths`](#isaacsim.sensors.experimental.rtx.Acoustic.paths)
      * [`prims`](#isaacsim.sensors.experimental.rtx.Acoustic.prims)
      * [`valid`](#isaacsim.sensors.experimental.rtx.Acoustic.valid)
    - [`RtxCamera`](#isaacsim.sensors.experimental.rtx.RtxCamera)
      * [`apply_visual_materials()`](#isaacsim.sensors.experimental.rtx.RtxCamera.apply_visual_materials)
      * [`create()`](#isaacsim.sensors.experimental.rtx.RtxCamera.create)
      * [`ensure_api()`](#isaacsim.sensors.experimental.rtx.RtxCamera.ensure_api)
      * [`get_applied_visual_materials()`](#isaacsim.sensors.experimental.rtx.RtxCamera.get_applied_visual_materials)
      * [`get_default_state()`](#isaacsim.sensors.experimental.rtx.RtxCamera.get_default_state)
      * [`get_local_poses()`](#isaacsim.sensors.experimental.rtx.RtxCamera.get_local_poses)
      * [`get_local_scales()`](#isaacsim.sensors.experimental.rtx.RtxCamera.get_local_scales)
      * [`get_visibilities()`](#isaacsim.sensors.experimental.rtx.RtxCamera.get_visibilities)
      * [`get_world_poses()`](#isaacsim.sensors.experimental.rtx.RtxCamera.get_world_poses)
      * [`reset_to_default_state()`](#isaacsim.sensors.experimental.rtx.RtxCamera.reset_to_default_state)
      * [`reset_xform_op_properties()`](#isaacsim.sensors.experimental.rtx.RtxCamera.reset_xform_op_properties)
      * [`resolve_paths()`](#isaacsim.sensors.experimental.rtx.RtxCamera.resolve_paths)
      * [`set_default_state()`](#isaacsim.sensors.experimental.rtx.RtxCamera.set_default_state)
      * [`set_local_poses()`](#isaacsim.sensors.experimental.rtx.RtxCamera.set_local_poses)
      * [`set_local_scales()`](#isaacsim.sensors.experimental.rtx.RtxCamera.set_local_scales)
      * [`set_visibilities()`](#isaacsim.sensors.experimental.rtx.RtxCamera.set_visibilities)
      * [`set_world_poses()`](#isaacsim.sensors.experimental.rtx.RtxCamera.set_world_poses)
      * [`aux_output_level`](#isaacsim.sensors.experimental.rtx.RtxCamera.aux_output_level)
      * [`camera`](#isaacsim.sensors.experimental.rtx.RtxCamera.camera)
      * [`is_non_root_articulation_link`](#isaacsim.sensors.experimental.rtx.RtxCamera.is_non_root_articulation_link)
      * [`paths`](#isaacsim.sensors.experimental.rtx.RtxCamera.paths)
      * [`prims`](#isaacsim.sensors.experimental.rtx.RtxCamera.prims)
      * [`valid`](#isaacsim.sensors.experimental.rtx.RtxCamera.valid)
    - [`StructuredLightCamera`](#isaacsim.sensors.experimental.rtx.StructuredLightCamera)
      * [`apply_visual_materials()`](#isaacsim.sensors.experimental.rtx.StructuredLightCamera.apply_visual_materials)
      * [`create()`](#isaacsim.sensors.experimental.rtx.StructuredLightCamera.create)
      * [`destroy()`](#isaacsim.sensors.experimental.rtx.StructuredLightCamera.destroy)
      * [`ensure_api()`](#isaacsim.sensors.experimental.rtx.StructuredLightCamera.ensure_api)
      * [`get_active_pattern_index()`](#isaacsim.sensors.experimental.rtx.StructuredLightCamera.get_active_pattern_index)
      * [`get_applied_visual_materials()`](#isaacsim.sensors.experimental.rtx.StructuredLightCamera.get_applied_visual_materials)
      * [`get_default_state()`](#isaacsim.sensors.experimental.rtx.StructuredLightCamera.get_default_state)
      * [`get_local_poses()`](#isaacsim.sensors.experimental.rtx.StructuredLightCamera.get_local_poses)
      * [`get_local_scales()`](#isaacsim.sensors.experimental.rtx.StructuredLightCamera.get_local_scales)
      * [`get_num_patterns()`](#isaacsim.sensors.experimental.rtx.StructuredLightCamera.get_num_patterns)
      * [`get_projector_cycle_period()`](#isaacsim.sensors.experimental.rtx.StructuredLightCamera.get_projector_cycle_period)
      * [`get_projector_direction_texture()`](#isaacsim.sensors.experimental.rtx.StructuredLightCamera.get_projector_direction_texture)
      * [`get_projector_prim_path()`](#isaacsim.sensors.experimental.rtx.StructuredLightCamera.get_projector_prim_path)
      * [`get_projector_timestamps()`](#isaacsim.sensors.experimental.rtx.StructuredLightCamera.get_projector_timestamps)
      * [`get_rect_light_prims()`](#isaacsim.sensors.experimental.rtx.StructuredLightCamera.get_rect_light_prims)
      * [`get_visibilities()`](#isaacsim.sensors.experimental.rtx.StructuredLightCamera.get_visibilities)
      * [`get_world_poses()`](#isaacsim.sensors.experimental.rtx.StructuredLightCamera.get_world_poses)
      * [`post_reset()`](#isaacsim.sensors.experimental.rtx.StructuredLightCamera.post_reset)
      * [`reset_to_default_state()`](#isaacsim.sensors.experimental.rtx.StructuredLightCamera.reset_to_default_state)
      * [`reset_xform_op_properties()`](#isaacsim.sensors.experimental.rtx.StructuredLightCamera.reset_xform_op_properties)
      * [`resolve_paths()`](#isaacsim.sensors.experimental.rtx.StructuredLightCamera.resolve_paths)
      * [`set_active_pattern_manual()`](#isaacsim.sensors.experimental.rtx.StructuredLightCamera.set_active_pattern_manual)
      * [`set_default_state()`](#isaacsim.sensors.experimental.rtx.StructuredLightCamera.set_default_state)
      * [`set_local_poses()`](#isaacsim.sensors.experimental.rtx.StructuredLightCamera.set_local_poses)
      * [`set_local_scales()`](#isaacsim.sensors.experimental.rtx.StructuredLightCamera.set_local_scales)
      * [`set_projector_cycle_period()`](#isaacsim.sensors.experimental.rtx.StructuredLightCamera.set_projector_cycle_period)
      * [`set_projector_timestamps()`](#isaacsim.sensors.experimental.rtx.StructuredLightCamera.set_projector_timestamps)
      * [`set_visibilities()`](#isaacsim.sensors.experimental.rtx.StructuredLightCamera.set_visibilities)
      * [`set_world_poses()`](#isaacsim.sensors.experimental.rtx.StructuredLightCamera.set_world_poses)
      * [`aux_output_level`](#isaacsim.sensors.experimental.rtx.StructuredLightCamera.aux_output_level)
      * [`camera`](#isaacsim.sensors.experimental.rtx.StructuredLightCamera.camera)
      * [`is_non_root_articulation_link`](#isaacsim.sensors.experimental.rtx.StructuredLightCamera.is_non_root_articulation_link)
      * [`paths`](#isaacsim.sensors.experimental.rtx.StructuredLightCamera.paths)
      * [`prims`](#isaacsim.sensors.experimental.rtx.StructuredLightCamera.prims)
      * [`valid`](#isaacsim.sensors.experimental.rtx.StructuredLightCamera.valid)
  + [Sensors](#sensors)
    - [`LidarSensor`](#isaacsim.sensors.experimental.rtx.LidarSensor)
      * [`lidar`](#isaacsim.sensors.experimental.rtx.LidarSensor.lidar)
    - [`RadarSensor`](#isaacsim.sensors.experimental.rtx.RadarSensor)
      * [`radar`](#isaacsim.sensors.experimental.rtx.RadarSensor.radar)
    - [`AcousticSensor`](#isaacsim.sensors.experimental.rtx.AcousticSensor)
      * [`acoustic`](#isaacsim.sensors.experimental.rtx.AcousticSensor.acoustic)
    - [`CameraSensor`](#isaacsim.sensors.experimental.rtx.CameraSensor)
      * [`attach_annotators()`](#isaacsim.sensors.experimental.rtx.CameraSensor.attach_annotators)
      * [`get_data()`](#isaacsim.sensors.experimental.rtx.CameraSensor.get_data)
      * [`camera`](#isaacsim.sensors.experimental.rtx.CameraSensor.camera)
      * [`resolution`](#isaacsim.sensors.experimental.rtx.CameraSensor.resolution)
    - [`SingleViewDepthCameraSensor`](#isaacsim.sensors.experimental.rtx.SingleViewDepthCameraSensor)
      * [`add_template_render_product()`](#isaacsim.sensors.experimental.rtx.SingleViewDepthCameraSensor.add_template_render_product)
      * [`get_enabled_outlier_removal()`](#isaacsim.sensors.experimental.rtx.SingleViewDepthCameraSensor.get_enabled_outlier_removal)
      * [`get_enabled_post_processing()`](#isaacsim.sensors.experimental.rtx.SingleViewDepthCameraSensor.get_enabled_post_processing)
      * [`get_sensor_baseline()`](#isaacsim.sensors.experimental.rtx.SingleViewDepthCameraSensor.get_sensor_baseline)
      * [`get_sensor_disparity_confidence()`](#isaacsim.sensors.experimental.rtx.SingleViewDepthCameraSensor.get_sensor_disparity_confidence)
      * [`get_sensor_disparity_noise_downscale()`](#isaacsim.sensors.experimental.rtx.SingleViewDepthCameraSensor.get_sensor_disparity_noise_downscale)
      * [`get_sensor_distance_cutoffs()`](#isaacsim.sensors.experimental.rtx.SingleViewDepthCameraSensor.get_sensor_distance_cutoffs)
      * [`get_sensor_focal_length()`](#isaacsim.sensors.experimental.rtx.SingleViewDepthCameraSensor.get_sensor_focal_length)
      * [`get_sensor_maximum_disparity()`](#isaacsim.sensors.experimental.rtx.SingleViewDepthCameraSensor.get_sensor_maximum_disparity)
      * [`get_sensor_noise_parameters()`](#isaacsim.sensors.experimental.rtx.SingleViewDepthCameraSensor.get_sensor_noise_parameters)
      * [`get_sensor_output_mode()`](#isaacsim.sensors.experimental.rtx.SingleViewDepthCameraSensor.get_sensor_output_mode)
      * [`get_sensor_size()`](#isaacsim.sensors.experimental.rtx.SingleViewDepthCameraSensor.get_sensor_size)
      * [`set_enabled_outlier_removal()`](#isaacsim.sensors.experimental.rtx.SingleViewDepthCameraSensor.set_enabled_outlier_removal)
      * [`set_enabled_post_processing()`](#isaacsim.sensors.experimental.rtx.SingleViewDepthCameraSensor.set_enabled_post_processing)
      * [`set_sensor_baseline()`](#isaacsim.sensors.experimental.rtx.SingleViewDepthCameraSensor.set_sensor_baseline)
      * [`set_sensor_disparity_confidence()`](#isaacsim.sensors.experimental.rtx.SingleViewDepthCameraSensor.set_sensor_disparity_confidence)
      * [`set_sensor_disparity_noise_downscale()`](#isaacsim.sensors.experimental.rtx.SingleViewDepthCameraSensor.set_sensor_disparity_noise_downscale)
      * [`set_sensor_distance_cutoffs()`](#isaacsim.sensors.experimental.rtx.SingleViewDepthCameraSensor.set_sensor_distance_cutoffs)
      * [`set_sensor_focal_length()`](#isaacsim.sensors.experimental.rtx.SingleViewDepthCameraSensor.set_sensor_focal_length)
      * [`set_sensor_maximum_disparity()`](#isaacsim.sensors.experimental.rtx.SingleViewDepthCameraSensor.set_sensor_maximum_disparity)
      * [`set_sensor_noise_parameters()`](#isaacsim.sensors.experimental.rtx.SingleViewDepthCameraSensor.set_sensor_noise_parameters)
      * [`set_sensor_output_mode()`](#isaacsim.sensors.experimental.rtx.SingleViewDepthCameraSensor.set_sensor_output_mode)
      * [`set_sensor_size()`](#isaacsim.sensors.experimental.rtx.SingleViewDepthCameraSensor.set_sensor_size)
    - [`TiledCameraSensor`](#isaacsim.sensors.experimental.rtx.TiledCameraSensor)
      * [`attach_annotators()`](#isaacsim.sensors.experimental.rtx.TiledCameraSensor.attach_annotators)
      * [`detach_annotators()`](#isaacsim.sensors.experimental.rtx.TiledCameraSensor.detach_annotators)
      * [`get_data()`](#isaacsim.sensors.experimental.rtx.TiledCameraSensor.get_data)
      * [`annotators`](#isaacsim.sensors.experimental.rtx.TiledCameraSensor.annotators)
      * [`camera`](#isaacsim.sensors.experimental.rtx.TiledCameraSensor.camera)
      * [`render_product`](#isaacsim.sensors.experimental.rtx.TiledCameraSensor.render_product)
      * [`resolution`](#isaacsim.sensors.experimental.rtx.TiledCameraSensor.resolution)
      * [`tiled_resolution`](#isaacsim.sensors.experimental.rtx.TiledCameraSensor.tiled_resolution)
  + [Utils](#utils)
    - [`parse_generic_model_output_data()`](#isaacsim.sensors.experimental.rtx.parse_generic_model_output_data)
    - [`parse_stable_id_map_data()`](#isaacsim.sensors.experimental.rtx.parse_stable_id_map_data)
  + [Lidar configuration registry](#lidar-configuration-registry)
    - [`SUPPORTED_LIDAR_CONFIGS`](#isaacsim.sensors.experimental.rtx.SUPPORTED_LIDAR_CONFIGS)
    - [`SUPPORTED_LIDAR_VARIANT_SET_NAME`](#isaacsim.sensors.experimental.rtx.SUPPORTED_LIDAR_VARIANT_SET_NAME)