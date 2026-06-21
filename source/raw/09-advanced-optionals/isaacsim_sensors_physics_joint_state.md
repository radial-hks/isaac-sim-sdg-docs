---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/sensors/isaacsim_sensors_physics_joint_state.html
title: "Joint State"
section: "Sensors"
module: "09-advanced-optionals"
checksum: "9952081d55c2007e"
fetched: "2026-06-21T13:05:43"
---

* [Sensors](index.html)
* [Physics-based sensors](isaacsim_sensors_physics.html)
* Joint state sensor

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Joint state sensor

The joint state sensor reads the full per-DOF state of an articulation in a single call: positions, velocities, and efforts for every degree of freedom, plus the DOF names and per-DOF type (revolute or prismatic). It is analogous to a ROS 2 `JointState` message and is backed by the C++ `IJointStateSensor` Carbonite interface in the `isaacsim.sensors.experimental.physics` extension.

Unlike the per-joint [Effort Sensor](isaacsim_sensors_physics_effort.html#isaacsim-sensors-physics-effort), a single joint state sensor returns data for the entire articulation. The sensor is attached to the articulation root prim, not to an individual joint.

See the [Isaac Sim Conventions](../reference_material/reference_conventions.html#isaac-sim-conventions) documentation for a complete list of Isaac Sim conventions.

**Joint state sensor properties**

1. `enabled` instance attribute determines whether the sensor returns data. When `False`, `get_sensor_reading()` and `get_data()` return invalid readings without touching the C++ backend.
2. The sensor binds to a single articulation root path provided at construction time. To re-target the sensor to a different articulation, construct a new `JointStateSensor`.

The `JointStateSensor` reads every physics step.

## Standalone Python

### Creating the joint state sensor

The following snippet adds a Simple Articulation reference and creates a `JointStateSensor` bound to the articulation root. The articulation must already be in the stage when the sensor is constructed.

```python
from isaacsim.sensors.experimental.physics import JointStateSensor

sensor = JointStateSensor(path="/World/simple_articulation", enabled=True)
```

Note

The articulation root prim you pass in **is** the sensorâs prim â `JointStateSensor` does not author a separate USD prim in the **Stage** panel on construction. DOF readings become available via `get_sensor_reading()` once the simulation is playing; check `reading.is_valid` after pressing **Play** to confirm the sensor is active.

### Reading sensor output

The sensor is created dynamically on **Play**. Moving or replacing the articulation root prim while the simulation is running invalidates the sensor; stop the simulator, make the changes, and restart.

There are two methods for reading the sensor output:

* `JointStateSensor.get_sensor_reading()` â returns a `JointStateSensorReading` object with the per-DOF arrays as attributes.
* `JointStateSensor.get_data()` â returns a structured dictionary with the same data plus `physics_step`, suitable for direct serialization.

**JointStateSensor.get\_sensor\_reading()**

Returns a `JointStateSensorReading` exposing `is_valid`, `time`, `dof_names` (`list[str]`), `positions` / `velocities` / `efforts` (`np.ndarray` of length `dof_count`), `dof_types` (`np.ndarray` of `uint8`: `0 = revolute`, `1 = prismatic`), and `stage_meters_per_unit`.

```python
reading = sensor.get_sensor_reading()
if reading.is_valid:
    for name, pos, vel, eff in zip(reading.dof_names, reading.positions, reading.velocities, reading.efforts):
        print(f"{name}: pos={pos:.4f} vel={vel:.4f} eff={eff:.4f}")
```

**JointStateSensor.get\_data()**

Returns a dictionary with keys `dof_names`, `positions`, `velocities`, `efforts`, `dof_types`, `stage_meters_per_unit`, `is_valid`, `time`, and `physics_step`. The numpy arrays in this dict are the same objects exposed by `get_sensor_reading()`; the dict form simply makes the data easier to log, plot, or pass to downstream consumers.

```python
frame = sensor.get_data()
if frame["is_valid"]:
    print(f"DOFs: {frame['dof_names']}")
    print(f"Positions: {frame['positions']}")
    print(f"Velocities: {frame['velocities']}")
    print(f"Efforts: {frame['efforts']}")
    print(f"Time: {frame['time']}, physics step: {frame['physics_step']}")
```

## API documentation

See the [isaacsim.sensors.experimental.physics API Documentation](../py/source/extensions/isaacsim.sensors.experimental.physics/docs/index.html) for the full `JointStateSensor` API.

On this page

* [Standalone Python](#standalone-python)
  + [Creating the joint state sensor](#creating-the-joint-state-sensor)
  + [Reading sensor output](#reading-sensor-output)
* [API documentation](#api-documentation)