---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/sensors/isaacsim_sensors_physics_effort.html
title: "Effort Sensor"
section: "Sensors"
module: "09-advanced-optionals"
checksum: "b2e915761b5d34fc"
fetched: "2026-06-21T13:40:13"
---

* [Sensors](index.html)
* [Physics-based sensors](isaacsim_sensors_physics.html)
* Effort sensor

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Effort sensor

Deprecated since version 6.0: The `isaacsim.sensors.physics` Effort Sensor extension is deprecated.
Use `isaacsim.sensors.experimental.physics.EffortSensor` instead.
See the [API Documentation](#api-documentation) section below for links.

The effort sensor in Isaac Sim tracks the torque or force applied to individual joints. Torque is measured for revolute joints and magnitude of force is measured for linear joints.

See the [Isaac Sim Conventions](../reference_material/reference_conventions.html#isaac-sim-conventions) documentation for a complete list of Isaac Sim conventions.

## GUI

### Scene setup

Begin by adding a Simple Articulation to the scene, which can be accessed in the Content Browser.

1. In the *Content Browser*, search for `simple_articulation` or navigate to `Isaac Sim/Robots/IsaacSim/SimpleArticulation/simple_articulation.usd`.
2. Drag `simple_articulation` onto the *World* prim in the **Stage** UI window on the right hand side to add an instance into the environment.
3. To drive the revolute joint, in the **Stage** window, select the RevoluteJoint prim at */World/simple\_articulation/Arm/RevoluteJoint*, and scroll down to **Drive** in the **Property** window. Set the target velocity to `90 deg/s`, and stiffness to `0`.

### Creating and modifying the effort sensor

The following section describes how to create the effort sensor using the **Script Editor**, opened from **Window > Script Editor**.
The effort sensor is created by constructing an `isaacsim.sensors.experimental.physics.EffortSensor` directly with the joint prim path. The class exposes `get_sensor_reading()` and `get_data()` for reading sensor output, plus `update_dof_name()` and `change_buffer_size()` for runtime reconfiguration. (Unlike the contact, IMU, and raycast sensors, `EffortSensor` has no separate authoring class because it has no schema-bearing prim of its own.)

```python
from isaacsim.sensors.experimental.physics import EffortSensor

sensor = EffortSensor(path="/World/simple_articulation/Arm/RevoluteJoint", enabled=True)
```

Note

The joint prim you pass in **is** the sensor’s prim — `EffortSensor` does not author a separate USD prim in the **Stage** panel on construction. Effort readings become available via `get_sensor_reading()` once the simulation is playing; check `reading.is_valid` after pressing **Play** to confirm the sensor is active.

To modify sensor parameters, change class member variables such as `enabled` directly. To change the `dof_name` and `buffer_size` for readings, use the corresponding member functions, `update_dof_name` and `change_buffer_size`.

### Reading sensor output with Python

There are two methods for reading the sensor output:

* `EffortSensor.get_sensor_reading()` — returns an `EffortSensorReading` object with `is_valid`, `time`, and `value`.
* `EffortSensor.get_data()` — returns a structured dictionary with `value`, `is_valid`, `time`, and `physics_step`.

After you create the effort sensor, press **Play** to start the simulation and call the function below to get the sensor reading for the current frame:

**EffortSensor.get\_sensor\_reading()**

```python
reading = sensor.get_sensor_reading()
```

**EffortSensor.get\_data()**

```python
frame = sensor.get_data()
print(f"Effort: {frame['value']}, valid: {frame['is_valid']}, time: {frame['time']}")
```

### OmniGraph workflow

Set up OmniGraph to create the effort sensor and collect readings from it:

1. Create the new action graph by navigating to **Window > Graph Editors > Action Graph**, and selecting **New Action Graph** in the new tab that opens.
2. Add the following nodes to the graph:

   > * **On Playback Tick**: Executes the graph nodes every simulation timestep.
   > * **Isaac Read Effort Node**: Reads the effort sensor. In the **Property** tab, set Effort Prim to the exact joint of measurement. For example */World/simple\_articulation/Arm/RevoluteJoint* in `simple_articulation.usd`.
   > * **To String**: Converts the effort sensor readings to string format.
   > * **Print Text**: Prints the string readings to console. In the **Property** tab, set Log Level to *Warning* so that messages are visible in the terminal/console by default. Additionally, check *To Screen* to print directly to screen.

Connect the nodes as follows to print the effort sensor reading:

Note

Configure the joints to the correct axis to get the expected readings.

## API documentation

Deprecated since version 6.0: The `isaacsim.sensors.physics` extension is deprecated. Use `isaacsim.sensors.experimental.physics.EffortSensor` instead.

See the [isaacsim.sensors.experimental.physics API Documentation](../py/source/extensions/isaacsim.sensors.experimental.physics/docs/index.html) for the current API and [isaacsim.sensors.physics API Documentation (deprecated)](../py/source/extensions/isaacsim.sensors.physics/docs/index.html) for the deprecated API.

On this page

* [GUI](#gui)
  + [Scene setup](#scene-setup)
  + [Creating and modifying the effort sensor](#creating-and-modifying-the-effort-sensor)
  + [Reading sensor output with Python](#reading-sensor-output-with-python)
  + [OmniGraph workflow](#omnigraph-workflow)
* [API documentation](#api-documentation)