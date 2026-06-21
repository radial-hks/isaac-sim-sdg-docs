---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/sensors/isaacsim_sensors_physx_lightbeam.html
title: "PhysX Lightbeam"
section: "Sensors"
module: "09-advanced-optionals"
checksum: "35d0a926b343201b"
fetched: "2026-06-21T13:40:13"
---

* [Sensors](index.html)
* [PhysX SDK sensors](isaacsim_sensors_physx.html)
* PhysX SDK lightbeam sensor

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# PhysX SDK lightbeam sensor

Deprecated since version 6.0: The PhysX SDK sensor extensions (`isaacsim.sensors.physx`) are deprecated. Use
`isaacsim.sensors.experimental.physics.RaycastSensor` as the replacement for raycast-based sensing.
For lightbeam/safety-curtain specific functionality, consider using the `RaycastSensor` with
appropriate configuration.
See [Migrating to the physics raycast sensor](#isaacsim-sensors-physx-lightbeam-migration) for step-by-step migration instructions, or the [isaacsim.sensors.experimental.physics API Documentation](../py/source/extensions/isaacsim.sensors.experimental.physics/docs/index.html) for the replacement APIs.

The PhysX SDK lightbeam sensor in Isaac Sim uses PhysX SDK raycasts to determine if an object has intersected a light beam.
You can specify the number of rays and height to create a safety light “curtain” of lightbeam sensors.

See the [Isaac Sim Conventions](../reference_material/reference_conventions.html#isaac-sim-conventions) documentation for a complete list of Isaac Sim conventions.

## Examples

* PhysX SDK Lightbeam Sensor example: **Robotics Examples > Sensors > Lightbeam**

To run the example:

1. Activate **Robotics Examples** tab from **Windows** > **Examples** > **Robotics Examples**.
2. Click **Robotics Examples > Sensors > Lightbeam**.
3. Verify that you have a window containing empty data for each lightbeam, which populates with data after you press **Play**. It shows if each beam was hit, the linear depth of the hit, and the exact hit position in `xyz`.
4. Press the **Play** button to begin simulating.
5. Press `SHIFT + LEFT_CLICK` to drag the cube or sensor around and see changes in the readings.

## Migrating to the physics raycast sensor

The PhysX SDK lightbeam sensor is deprecated. Use the [Physics Raycast Sensor](isaacsim_sensors_physics_raycast.html#isaacsim-sensors-physics-raycast) (`isaacsim.sensors.experimental.physics.RaycastSensor`) configured as a beam curtain to achieve the same functionality.

### Concept mapping

| PhysX SDK Lightbeam Sensor | Physics Raycast Sensor |
| --- | --- |
| `numRays` | Length of the `rayOrigins` / `rayDirections` arrays. Create one entry per beam. |
| `curtainLength` / `curtainAxis` | `rayOrigins`. Spread ray origins along the curtain axis. For example, for a vertical curtain of height *h* with *N* beams: `origins[i] = [0, 0, -h/2 + h * i / (N-1)]`. |
| `forwardAxis` | `rayDirections`. Set all direction vectors to the forward axis. For example, `[1, 0, 0]` for a curtain firing along the X axis. |
| `minRange` / `maxRange` | `minRange` / `maxRange`. Same semantics. |
| Per-beam hit / depth / position data | `RaycastSensor.get_sensor_reading()` returns per-ray depths, hit positions, and hit normals. |

### Interactive example

The **Physics Raycast Sensor** example includes a beam curtain sensor configuration with parallel vertical rays:

* **GUI**: Open **Robotics Examples > Sensors > Physics Raycast Sensor** and click **Load Scene**.
* **Source code**: `source/extensions/isaacsim.sensors.physics.examples/isaacsim/sensors/physics/examples/raycast_sensor.py`

See [Physics raycast sensor](isaacsim_sensors_physics_raycast.html#isaacsim-sensors-physics-raycast) for the full documentation, including Python API usage and OmniGraph workflows.

On this page

* [Examples](#examples)
* [Migrating to the physics raycast sensor](#migrating-to-the-physics-raycast-sensor)
  + [Concept mapping](#concept-mapping)
  + [Interactive example](#interactive-example)