---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/sensors/isaacsim_sensors_physics.html
title: "Physics Sensors Index"
section: "Sensors"
module: "09-advanced-optionals"
checksum: "c762c76977508592"
fetched: "2026-06-21T14:14:39"
---

* [Sensors](index.html)
* Physics-based sensors

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Physics-based sensors

Isaac Sim’s physics-based sensors use CPU physics simulations and run after rendering finishes. They have access to a prim’s physics properties, like mass and velocity.

These sensors output the exact measurements from the physics engine, and you can augment the sensor readings in post-processing.
By default, sensors output data at the physics rate. To generate data beyond this rate, provide additional interpolation options. Ground truth readings from the simulator might
already have some noise; you can add more noise in post-processing to make sensor readings more realistic.

The physics-based sensors are organized in the `isaacsim.sensors.experimental.physics` extension.

Deprecated since version 6.0: The `isaacsim.sensors.physics` extension is deprecated. Use `isaacsim.sensors.experimental.physics` instead.
The new extension provides equivalent sensor classes (`ContactSensor`, `IMUSensor`, `EffortSensor`, etc.) with the same core functionality.
See [Physics Sensors](../migration_guides/isaac_sim_6_0/sensors_physics_to_experimental_physics.html#isaacsim-sensors-physics-migration) for step-by-step migration instructions, or the [API Documentation](../py/source/extensions/isaacsim.sensors.experimental.physics/docs/index.html) for the replacement APIs.

Isaac Sim supports the following physics-based ground truth sensors:

* [Articulation joint sensors](isaacsim_sensors_physics_articulation_force.html)
* [Contact sensor](isaacsim_sensors_physics_contact.html)
* [Effort sensor](isaacsim_sensors_physics_effort.html)
* [IMU sensor](isaacsim_sensors_physics_imu.html)
* [Joint state sensor](isaacsim_sensors_physics_joint_state.html)
* [Physics raycast sensor](isaacsim_sensors_physics_raycast.html)