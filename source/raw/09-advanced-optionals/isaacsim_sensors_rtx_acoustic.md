---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/sensors/isaacsim_sensors_rtx_acoustic.html
title: "RTX Acoustic"
section: "Sensors"
module: "09-advanced-optionals"
checksum: "47a62ef0f4f74b39"
fetched: "2026-06-21T13:05:44"
---

* [Sensors](index.html)
* [RTX Sensors](isaacsim_sensors_rtx.html)
* RTX Acoustic Sensor

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# RTX Acoustic Sensor

RTX Acoustic sensors simulate ultrasonic wave propagation at render time on the GPU with RTX hardware.
Their results are written to the `GenericModelOutput` AOV, similar to RTX Lidar and Radar sensors.

## Overview

RTX Acoustic sensors are rendered using `OmniAcoustic` prims, with the `OmniSensorGenericAcousticWpmAPI`
schema applied. After attaching a render product to the `OmniAcoustic` prim, and setting the
`GenericModelOutput` AOV on the render product, the RTXSensor renderer writes acoustic simulation
results to the AOV.

For complete documentation on all acoustic schema attributes and the underlying Wave Propagation Model (WPM),
see the [Omniverse Acoustic Extension documentation](https://docs.omniverse.nvidia.com/kit/docs/omni.sensors.nv.acoustic/3.0.0/acoustic_extension.html).

Note

Earlier releases referred to this sensor as the âUltrasonicâ sensor (or âUSSâ). The Omniverse plugin
has been renamed to âAcousticâ; if you previously used `omni.kit.commands.execute("IsaacSensorCreateRtxUltrasonic", ...)`
in `isaacsim.sensors.rtx`, see [RTX Sensors](../migration_guides/isaac_sim_6_0/sensors_rtx_to_experimental_rtx.html#isaacsim-sensors-rtx-migration) for the migration to
`Acoustic` / `AcousticSensor`.

Unlike Lidar and Radar sensors, acoustic sensors do not produce a 3D point cloud. Instead, they produce
**signal ways** â amplitude samples for each transmitterâreceiver pair on each channel. The
`GenericModelOutput` element fields have the following meaning for acoustic sensors:

| Field | Meaning |
| --- | --- |
| `x` | Transmitter sensor mount ID |
| `y` | Receiver sensor mount ID |
| `z` | Channel ID |
| `scalar` | Amplitude sample value |

### Sensor Mounts and Receiver Groups

Acoustic sensors use **multi-apply schemas** to define sensor mounts and receiver groups:

* **Sensor mounts** (`OmniSensorWpmAcousticSensorMountAPI`) define the physical positions and
  orientations of transducers (transmitters and receivers). Each mount is an instance with a unique
  name (for example, `m001`, `m002`).
* **Receiver groups** (`OmniSensorWpmAcousticRxGroupAPI`) define logical groupings of receivers
  by specifying which mount indices belong to the group. Each group is an instance with a unique
  name (for example, `g001`).

These schemas are applied automatically when the corresponding attribute prefixes are provided
in the `attributes` dictionary.

## How to Create an RTX Acoustic Sensor

The `isaacsim.sensors.experimental.rtx` extension provides the `Acoustic` class for creating RTX
Acoustic sensors. An equivalent menu entry is also registered by the `isaacsim.sensors.rtx.ui`
extension for UI-driven creation.

### Create an RTX Acoustic Sensor From the Create Menu

To create a generic RTX Acoustic sensor from the Isaac Sim UI:

* **Main menu**: *Create > Sensors > RTX Acoustic > NVIDIA > Generic RTX Acoustic*
* **Viewport context menu** (right-click in the viewport): *Create > Isaac > Sensors > RTX Acoustic > NVIDIA > Generic RTX Acoustic*

Both entries create an `OmniAcoustic` prim with the `OmniSensorGenericAcousticWpmAPI` schema applied,
at the next available path. If a prim is selected at creation time, the new sensor is parented under
the selected prim; otherwise it is created at the stage root.

The menu entry creates a bare prim with no sensor mounts or receiver groups configured. To author the
multi-apply schemas (`OmniSensorWpmAcousticSensorMountAPI`, `OmniSensorWpmAcousticRxGroupAPI`)
and tune attributes such as `omni:sensor:WpmAcoustic:centerFrequency`, either edit the prim in the
property panel after creation, or use the `Acoustic` class for programmatic setup as shown below.

The RTX Acoustic submenu also auto-populates additional vendor entries from the
`SUPPORTED_ACOUSTIC_CONFIGS` dict in `isaacsim.sensors.experimental.rtx`, so OEM acoustic asset
USDs registered there appear in the menu automatically.

### Create an RTX Acoustic Sensor Using the `Acoustic` Class

The `Acoustic` class creates or wraps an `OmniAcoustic` prim with the appropriate schemas applied.

Run this snippet in the **Script Editor** (**Window > Script Editor**).

```python
import numpy as np
from isaacsim.sensors.experimental.rtx import Acoustic

# Create an RTX Acoustic sensor with a center frequency and two sensor mounts.
acoustic = Acoustic(
    path="/World/acoustic",
    tick_rate=20.0,
    translations=np.array([0.0, 0.0, 1.0]),
    attributes={
        "omni:sensor:WpmAcoustic:centerFrequency": 40000.0,
        # Sensor mount positions (transmitter/receiver locations)
        "omni:sensor:WpmAcoustic:sensorMount:m001:position": (0.0, 0.0, 0.0),
        "omni:sensor:WpmAcoustic:sensorMount:m002:position": (0.1, 0.0, 0.0),
        # Receiver group combining both mounts
        "omni:sensor:WpmAcoustic:rxGroup:g001:receiverIndices": [0, 1],
    },
)
```

The snippet above creates an `OmniAcoustic` prim at `/World/acoustic` with:

* A center frequency of 40,000 Hz (ultrasonic)
* Two sensor mounts at positions `(0, 0, 0)` and `(0.1, 0, 0)`
* A receiver group combining both mounts

Note

`Acoustic.create()` accepts `config` (from
`isaacsim.sensors.experimental.rtx.SUPPORTED_ACOUSTIC_CONFIGS`) or `usd_path` (mutually
exclusive), plus `attributes` for prim-attribute overrides â including the multi-apply
`OmniSensorWpmAcousticSensorMountAPI` / `OmniSensorWpmAcousticRxGroupAPI` /
`OmniSensorWpmAcousticFiringSeqAPI` schema attributes â and the plural transform arrays
(`positions=[[...]]` / `translations=[[...]]` / `orientations=[[...]]` / `scales=[[...]]`;
`N=1`). Additional USD schemas via `schemas=[...]` are accepted by the `Acoustic(...)`
constructor â pass them through `Acoustic(...)` directly if you need them, since
`Acoustic.create()` does not currently forward `schemas`.

### Tick Rate

Warning

In Isaac Sim 6.0 GA, RTX Acoustic autotriggers regardless of `omni:sensor:tickRate` attribute. This will be corrected in a future release.

The `tick_rate` parameter (Hz) controls how frequently the sensor renders. A value of `0`
(the default) enables autotrigger mode, where the sensor renders every simulation frame. This maps to the `omni:sensor:tickRate` prim attribute.

Run this snippet in the **Script Editor** (**Window > Script Editor**).

```python
from isaacsim.sensors.experimental.rtx import Acoustic

# Render at 10 Hz regardless of simulation frame rate.
acoustic = Acoustic.create("/World/Acoustic", tick_rate=10.0)
```

### Auxiliary Output Level

RTX Acoustic exposes auxiliary data through the `aux_output_level` constructor parameter.
Valid values are `"NONE"` (default) and `"BASIC"`.

Run this snippet in the **Script Editor** (**Window > Script Editor**).

```python
from isaacsim.sensors.experimental.rtx import Acoustic

acoustic = Acoustic.create("/World/Acoustic", aux_output_level="BASIC")
```

See [Auxiliary Output Level and the GenericModelOutput RenderVar](isaacsim_sensors_rtx.html#isaacsim-sensors-rtx-aux-output-level) for the full attribute-flow explanation and the
migration from the removed per-modality `auxOutputType` attribute, and
[Known issue: last-attach-wins propagation of GMO channels](isaacsim_sensors_rtx.html#isaacsim-sensors-rtx-known-issue-gmo-channels) for a known issue when multiple RTX sensors
with different auxiliary levels share a stage. See [RTX Sensor Annotators](isaacsim_sensors_rtx_annotators.html#rtx-sensor-annotator-descriptions) for
the per-level field listing.

## How to Collect Data from an RTX Acoustic Sensor

Use the `AcousticSensor` runtime class to attach annotators and retrieve data:

Run this snippet in the **Script Editor** (**Window > Script Editor**).

```python
from isaacsim.sensors.experimental.rtx import Acoustic, AcousticSensor, parse_generic_model_output_data

acoustic = Acoustic.create("/World/Acoustic")

sensor = AcousticSensor(acoustic, annotators=["generic-model-output"])
data, info = sensor.get_data("generic-model-output")
gmo = parse_generic_model_output_data(data)

# gmo.x      -> transmitter mount IDs
# gmo.y      -> receiver mount IDs
# gmo.z      -> channel IDs
# gmo.scalar -> amplitude values
```

Refer to [Reading Data from the GenericModelOutput Buffer](isaacsim_sensors_rtx_annotators.html#rtx-sensor-reading-gmo-buffer) for more details on the `GenericModelOutput` buffer.

## Standalone Examples

**Basic Creation**

```python
# Create an acoustic sensor with two mounts and a receiver group
./python.sh standalone_examples/api/isaacsim.sensors.experimental.rtx/create_acoustic_basic.py
```

**Data Inspection**

```python
# Inspect acoustic GenericModelOutput data and signal ways
./python.sh standalone_examples/api/isaacsim.sensors.experimental.rtx/inspect_acoustic_gmo.py
```

Note

Refer to the [Isaac Sim Conventions](../reference_material/reference_conventions.html#isaac-sim-conventions) documentation for a complete list of Isaac Sim conventions.

On this page

* [Overview](#overview)
  + [Sensor Mounts and Receiver Groups](#sensor-mounts-and-receiver-groups)
* [How to Create an RTX Acoustic Sensor](#how-to-create-an-rtx-acoustic-sensor)
  + [Create an RTX Acoustic Sensor From the Create Menu](#create-an-rtx-acoustic-sensor-from-the-create-menu)
  + [Create an RTX Acoustic Sensor Using the `Acoustic` Class](#create-an-rtx-acoustic-sensor-using-the-acoustic-class)
  + [Tick Rate](#tick-rate)
  + [Auxiliary Output Level](#auxiliary-output-level)
* [How to Collect Data from an RTX Acoustic Sensor](#how-to-collect-data-from-an-rtx-acoustic-sensor)
* [Standalone Examples](#standalone-examples)