---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/omniverse_usd/sensor_schema.html
title: "Sensor Schema"
section: "OpenUSD"
module: "01-concepts"
checksum: "82bda23a33d29e80"
fetched: "2026-06-21T14:14:17"
---

* [Omniverse and USD](index.html)
* Sensor Schema

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Sensor Schema

The Sensor Schema extends OpenUSD with typed prim schemas for the physics-based sensors in Isaac Sim. All sensor schemas inherit from a common `IsaacBaseSensor` base class and are defined in the `isaacsim.robot.schema` extension alongside the [Robot Schema](robot_schema.html#isaac-sim-robot-schema).

The schema source lives in `source/extensions/isaacsim.robot.schema/sensor_schema/SensorSchema.usda`.

## Base Sensor

`IsaacBaseSensor` is the abstract base class for all typed sensor prims. It inherits from `Xformable`, so every sensor has a position and orientation on the stage.

| Attribute | Type | Description |
| --- | --- | --- |
| `enabled` | Bool | Set to `True` to enable this sensor, `False` to disable. |

## Contact Sensor (`IsaacContactSensor`)

`IsaacContactSensor` measures contact forces between the prim it is attached to and other prims in the scene. It inherits from `IsaacBaseSensor`.

See [Contact sensor](../sensors/isaacsim_sensors_physics_contact.html#isaacsim-sensors-physics-contact) for usage documentation.

| Attribute | Type | Description |
| --- | --- | --- |
| `threshold` | Float2 | Min and max force detected by this sensor, in (kg) \* (stage length unit) / (second)^2. |
| `radius` | Float | Radius of the contact sensor sphere, in stage length units. A value of `-1` uses the prim’s collision geometry. |
| `color` | Float4 | Color of the contact sensor visualization sphere (R, G, B, A). |
| `sensorPeriod` | Float | **Deprecated** since `isaacsim.robot.schema` 6.2.0. Only used by the deprecated `isaacsim.sensors.physx` extension. Time between measurements in simulator seconds. |

## IMU Sensor (`IsaacImuSensor`)

`IsaacImuSensor` measures linear acceleration, angular velocity, and orientation of the prim it is attached to. It inherits from `IsaacBaseSensor`.

See [IMU sensor](../sensors/isaacsim_sensors_physics_imu.html#isaacsim-sensors-physics-imu) for usage documentation.

| Attribute | Type | Description |
| --- | --- | --- |
| `sensorPeriod` | Float | **Deprecated** since `isaacsim.robot.schema` 6.2.0. Only used by the deprecated `isaacsim.sensors.physx` extension. Time between measurements in simulator seconds. |
| `linearAccelerationFilterWidth` | Int | Number of linear acceleration measurements used in the rolling average filter. |
| `angularVelocityFilterWidth` | Int | Number of angular velocity measurements used in the rolling average filter. |
| `orientationFilterWidth` | Int | Number of orientation measurements used in the rolling average filter. |

## Raycast Sensor (`IsaacRaycastSensor`)

`IsaacRaycastSensor` is a physics-raycast-based sensor with explicit per-ray origin offsets, direction vectors, and optional time offsets. It inherits from `IsaacBaseSensor` and is used by the `isaacsim.sensors.experimental.physics` extension.

See [Physics raycast sensor](../sensors/isaacsim_sensors_physics_raycast.html#isaacsim-sensors-physics-raycast) for usage documentation.

Origins and directions are specified in the sensor prim’s local coordinate frame. At each physics step the sensor’s world transform is computed from the current rigid-body pose, optionally extrapolated forward using linear/angular velocity when a non-zero `rayTimeOffset` is specified. Each ray’s local origin and direction are then transformed into world space for the raycast.

All attributes are read once when the sensor is first evaluated after simulation starts. Changing attribute values while the simulation is playing has no effect; stop and restart the simulation to pick up changes.

| Attribute | Type | Description |
| --- | --- | --- |
| `numRays` | UInt | Number of rays cast by this sensor. `rayOrigins` and `rayDirections` must each have exactly this many elements. |
| `minRange` | Float | Minimum detection range in stage length units. Rays start at `origin + direction * minRange`. |
| `maxRange` | Float | Maximum detection range in stage length units. |
| `rayOrigins` | Float3[] | Per-ray origin translations in the sensor’s local coordinate frame. |
| `rayDirections` | Float3[] | Per-ray cast direction vectors in the sensor’s local coordinate frame. Vectors are normalized before use. |
| `rayTimeOffsets` | Float[] | Per-ray time offsets in seconds. When provided, only rays whose time offsets fall within the current physics step’s time window are fired. The sweep period equals `max(rayTimeOffsets)`. If empty, all rays fire every step. |
| `outputFrameOfReference` | Token | Coordinate frame for hit positions and normals: `SENSOR` (default) or `WORLD`. |
| `reportHitPrimPaths` | Bool | When `True`, the sensor reading includes the USD prim path of each hit surface. |

## Deprecated Sensor Schemas

The following sensor schemas are defined in `SensorSchema.usda` but are deprecated:

* **IsaacLightBeamSensor** – Deprecated since `isaacsim.robot.schema` 6.2.0. Use `IsaacRaycastSensor` with `isaacsim.sensors.experimental.physics` instead. See [Migrating to the physics raycast sensor](../sensors/isaacsim_sensors_physx_lightbeam.html#isaacsim-sensors-physx-lightbeam-migration).

The `IsaacRtxLidarSensorAPI` and `IsaacRtxRadarSensorAPI` are applied API schemas for the RTX sensor pipeline and are not physics-based sensors. See [RTX Sensors](../sensors/isaacsim_sensors_rtx.html#isaacsim-sensors-rtx) for RTX sensor documentation.

On this page

* [Base Sensor](#base-sensor)
* [Contact Sensor (`IsaacContactSensor`)](#contact-sensor-isaaccontactsensor)
* [IMU Sensor (`IsaacImuSensor`)](#imu-sensor-isaacimusensor)
* [Raycast Sensor (`IsaacRaycastSensor`)](#raycast-sensor-isaacraycastsensor)
* [Deprecated Sensor Schemas](#deprecated-sensor-schemas)