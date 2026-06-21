---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/sensors/isaacsim_sensors_physx.html
title: "PhysX Sensors Index"
section: "Sensors"
module: "09-advanced-optionals"
checksum: "347dce485ef4a3da"
fetched: "2026-06-21T14:14:40"
---

* [Sensors](index.html)
* PhysX SDK sensors

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# PhysX SDK sensors

Isaac Sim’s PhysX SDK sensors use raycasts provided by the [PhysX SDK](https://nvidia-omniverse.github.io/PhysX/physx/5.3.0/) to measure the range between
objects in the simulation.

These sensors output the exact measurements from PhysX SDK. By default, the highest rate that the sensors can output data is the render rate.

The PhysX SDK sensors are organized in the `isaacsim.sensors.physx` extension.

Deprecated since version 6.0: The `isaacsim.sensors.physx` extension is deprecated. Use `isaacsim.sensors.experimental.physics` instead,
which provides the `RaycastSensor` as the replacement for PhysX-based range sensors.
See the [API Documentation](../py/source/extensions/isaacsim.sensors.experimental.physics/docs/index.html) for the replacement APIs.
See individual sensor pages below for specific migration guidance.

Isaac Sim supports the following PhysX SDK sensors:

* [PhysX SDK generic sensor](isaacsim_sensors_physx_generic.html)
* [PhysX SDK lidar](isaacsim_sensors_physx_lidar.html)
* [PhysX SDK lightbeam sensor](isaacsim_sensors_physx_lightbeam.html)
* [Proximity sensor](isaacsim_sensors_physx_proximity.html)