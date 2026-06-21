---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/sensors/isaacsim_sensors_physx_proximity.html
title: "PhysX Proximity"
section: "Sensors"
module: "09-advanced-optionals"
checksum: "361f8a70dd0bde54"
fetched: "2026-06-21T13:05:44"
---

* [Sensors](index.html)
* [PhysX SDK sensors](isaacsim_sensors_physx.html)
* Proximity sensor

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Proximity sensor

Deprecated since version 6.0: The Proximity Sensor (`isaacsim.sensors.physx.ProximitySensor`) is part of the deprecated `isaacsim.sensors.physx` extension.
For collision detection, consider using the [Contact Sensor](isaacsim_sensors_physics_contact.html#isaacsim-sensors-physics-contact) or physics contact callbacks directly.

The proximity sensor wraps a physics callback that can be attached to any prim in the scene. During simulation execution,
the sensor records collisions between the prim it is attached to and other prims in the scene each frame; you can access that data
using a callback function.

## Standalone Python

Note

The code below uses the deprecated `isaacsim.sensors.physx` extension. See the deprecation notice above for the replacement API.

Execute the following script using `python.sh`. This creates a scene with two cubes and attaches a proximity sensor to one of the cubes.
At the start of the simulation, the two cubes overlap and then move apart; the callback function in the script prints the proximity
sensorâs output to the screen.

```python
import numpy as np
from isaacsim import SimulationApp

simulation_app = SimulationApp({"headless": False})

import carb
import omni
from isaacsim.core.api.world import World
from isaacsim.core.experimental.objects import Cube, GroundPlane
from isaacsim.core.utils.extensions import enable_extension
from pxr import Sdf, UsdLux, UsdPhysics

# Set up scene
world = World()
GroundPlane("/World/GroundPlane")

# Add lighting
stage = omni.usd.get_context().get_stage()
distantLight = UsdLux.DistantLight.Define(stage, Sdf.Path("/DistantLight"))
distantLight.CreateIntensityAttr(500)

# Add cubes with collision and rigid body for physics simulation
cube_1 = Cube("/cube_1", sizes=1.0, positions=np.array([0.4, 0, 5.0]), colors=np.array([1.0, 0, 0]))
UsdPhysics.CollisionAPI.Apply(cube_1.prims[0])
UsdPhysics.RigidBodyAPI.Apply(cube_1.prims[0])

cube_2 = Cube("/cube_2", sizes=1.0, positions=np.array([-0.4, 0, 5.0]), colors=np.array([0, 0, 1.0]))
UsdPhysics.CollisionAPI.Apply(cube_2.prims[0])
UsdPhysics.RigidBodyAPI.Apply(cube_2.prims[0])

# Enable isaacsim.sensors.physx extension
enable_extension("isaacsim.sensors.physx")
simulation_app.update()

# Attach sensor to cube 1
from isaacsim.sensors.physx import ProximitySensor, clear_sensors, register_sensor

s = ProximitySensor(cube_1.prims[0])
register_sensor(s)

# Add callback to print proximity sensor data
def print_proximity_sensor_data_on_update(_):
    data = s.get_data()
    if "/cube_2" in data:
        # /cube_1 is colliding with /cube_2
        distance = data["/cube_2"]["distance"]
        duration = data["/cube_2"]["duration"]
        carb.log_warn(f"distance: {distance}, duration: {duration}")

# Play simulation
world.add_physics_callback("print_sensor_data", print_proximity_sensor_data_on_update)
simulation_app.update()
simulation_app.update()
world.play()

for i in range(100):
    # Run with a fixed step size
    world.step(render=True)
```

Example proximity sensor output is shown below; there might be small numerical differences in your output run-to-run.

```python
distance: 0.8995118804137266, duration: 0.03952527046203613
distance: 0.9490971672498862, duration: 0.04244112968444824
distance: 0.9978315307718298, duration: 0.045195579528808594
distance: 1.0952793930211249, duration: 0.00010466575622558594
distance: 1.0952880909233123, duration: 0.004382610321044922
distance: 1.0952874949586842, duration: 0.008539199829101562
distance: 1.095288806188406, duration: 0.012722015380859375
```

After the cubes land, the scene looks like the following image:

On this page

* [Standalone Python](#standalone-python)