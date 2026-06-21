---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/sensors/isaacsim_sensors_rtx_annotators.html
title: "RTX Annotators"
section: "标注"
module: "05-sensors-annotators"
checksum: "57d367a5865f50a7"
fetched: "2026-06-21T14:14:54"
---

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

The `IsaacExtractRTXSensorPointCloud` Annotator extracts the `GenericModelOutput` buffer’s point cloud data
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
base stable ID with an *upper index* placed in the high 32 bits — the
submesh index for mesh geometry, and the per-triangle primitive index for
procedural geometry. `StableIdMap` registers per-instance entries (only
for instances with a USD prim path) plus per-`GeomSubset` entries when
an instance has more than one subset, but it does **not** register
per-primitive entries.

As a result, hits on procedural geometry, on submeshes that weren’t
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
| `emitterId` | `uint32` | ID of the emitter that emitted the return. | Provided if `outputEmitterId` is set to `true`, and the OmniLidar’s `aux_output_level` is `BASIC` (or higher). |
| `channelId` | `uint32` | ID of the channel the return was generated on. | Provided if `outputChannelId` is set to `true`, and the OmniLidar’s `aux_output_level` is `BASIC` (or higher). |
| `materialId` | `uint32` | ID of the material of the object that generated the return. | Provided if `outputMaterialId` is set to `true`, and the OmniLidar’s `aux_output_level` is `EXTRA` (or higher). Refer to [RTX Sensor Non-Visual Materials](isaacsim_sensors_rtx_materials.html#isaacsim-sensors-rtx-materials) for more details on how material IDs are computed. |
| `tickId` | `uint32` | ID of the tick the return was generated on. | Provided if `outputTickId` is set to `true`, and the OmniLidar’s `aux_output_level` is `BASIC` (or higher). |
| `hitNormal` | `float3` | Normal to the surface of the object that generated the return. | Provided if `outputHitNormal` is set to `true`, the OmniLidar’s `aux_output_level` is `FULL`, and `--/app/sensors/nv/lidar/publishNormals=true` is set. |
| `velocity` | `float3` | Velocity of the object that generated the return. | Provided if `outputVelocity` is set to `true`, and the OmniLidar’s `aux_output_level` is `FULL`. |
| `objectId` | `uint8` | ID of the object that generated the return. | Provided if `outputObjectId` is set to `true`, the OmniLidar’s `aux_output_level` is `EXTRA` (or higher), and `--/rtx-transient/stableIds/enabled=true` is set. Object ID is a stable, unique 128-bit unsigned integer mapping to the prim path of the object that generated the corresponding return. See [Semantic Segmentation with RTX Sensor using Object IDs](#rtx-sensor-resolving-object-ids) for more details. |
| `echoId` | `uint8` | Indicates which echo the return represents in a multi-echo Lidar configuration. | Provided if `outputEchoId` is set to `true`, and the OmniLidar’s `aux_output_level` is `BASIC` (or higher). |
| `tickState` | `uint8` | Indicates the state of the tick the return was generated on. | Provided if `outputTickState` is set to `true`, and the OmniLidar’s `aux_output_level` is `BASIC` (or higher). |

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