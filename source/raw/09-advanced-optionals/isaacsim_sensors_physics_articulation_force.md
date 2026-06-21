---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/sensors/isaacsim_sensors_physics_articulation_force.html
title: "Articulation Force"
section: "Sensors"
module: "09-advanced-optionals"
checksum: "83500adcff0e36e5"
fetched: "2026-06-21T13:05:43"
---

* [Sensors](index.html)
* [Physics-based sensors](isaacsim_sensors_physics.html)
* Articulation joint sensors

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Articulation joint sensors

Articulation sensors allow reading the active and passive components of the joint forces using the
[Articulation](../py/source/extensions/isaacsim.core.experimental.prims/docs/index.html#isaacsim.core.experimental.prims.Articulation) class
from the `isaacsim.core.experimental.prims` extension.
See [Robot Simulation Snippets](../python_scripting/robots_simulation.html#isaac-robot-simulation-how-to) for more details about the Articulation class. Specifically,

* `get_link_incoming_joint_force()` returns the 6D force and torque (shape `(N, L, 3)` each) for each linkâs incoming joint.
  This provides the total spatial force at each joint and can be used to mimic force-torque sensors by reading forces from a fixed joint.
* `get_dof_projected_joint_forces()` returns the active component of the joint forces projected onto the motion direction for each DOF.
  This is useful for reading the measured effort at each actuated joint.

Note

In an articulation tree, each link can have a single parent link.
The joint forces reported by `get_link_incoming_joint_force` and `get_dof_projected_joint_forces` correspond to the forces,
torques, or efforts exerted by the joint connecting the child link to the parent link.
In short, the forces reported by these APIs denote the link incoming joint forces.

## GUI

### Script Editor

This section describes how to read articulation joint forces through the Script Editor, opened from **Window > Script Editor**.

```python
import asyncio

import omni
import omni.timeline
from isaacsim.core.experimental.objects import GroundPlane
from isaacsim.core.experimental.prims import Articulation
from isaacsim.core.experimental.utils.stage import (
    add_reference_to_stage,
    create_new_stage_async,
)
from isaacsim.storage.native import get_assets_root_path
from pxr import UsdPhysics

async def joint_force():
    await create_new_stage_async()
    await omni.kit.app.get_app().next_update_async()

    # Set up the physics scene
    stage = omni.usd.get_context().get_stage()
    UsdPhysics.Scene.Define(stage, "/World/PhysicsScene")

    # Load the Ant robot and add a ground plane
    assets_root_path = get_assets_root_path()
    asset_path = assets_root_path + "/Isaac/Robots/IsaacSim/Ant/ant.usd"
    add_reference_to_stage(usd_path=asset_path, path="/World/Ant")
    GroundPlane("/World/GroundPlane")
    await omni.kit.app.get_app().next_update_async()

    # Wrap the articulation
    arti = Articulation("/World/Ant/torso")

    # Start the simulation so that the physics tensor API becomes available
    timeline = omni.timeline.get_timeline_interface()
    timeline.play()
    await omni.kit.app.get_app().next_update_async()

    # Read 6D joint forces (forces and torques per link)
    forces, torques = arti.get_link_incoming_joint_force()
    # Read DOF projected joint forces (active force component per DOF)
    projected_forces = arti.get_dof_projected_joint_forces()

    # Convert to numpy for inspection
    forces_np = forces.numpy()
    torques_np = torques.numpy()
    projected_np = projected_forces.numpy()

    # Map joint names to their link indices using the built-in API
    print("Joint names:", arti.joint_names)
    print("Link names:", arti.link_names)

    # Get the link and joint index for front_left_leg
    link_idx = int(arti.get_link_indices("front_left_leg").numpy()[0])
    joint_idx = int(arti.get_joint_indices("front_left_leg").numpy()[0])

    print("front_left_leg link forces:", forces_np[0, link_idx])
    print("front_left_leg link torques:", torques_np[0, link_idx])
    print("front_left_leg projected force:", projected_np[0, joint_idx])

    timeline.stop()

asyncio.ensure_future(joint_force())
```

## API documentation

See the [isaacsim.core.experimental.prims API Documentation](../py/source/extensions/isaacsim.core.experimental.prims/docs/index.html) for the full `Articulation` class reference.

On this page

* [GUI](#gui)
  + [Script Editor](#script-editor)
* [API documentation](#api-documentation)