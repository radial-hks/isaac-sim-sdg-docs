---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/python_scripting/robots_simulation.html
title: "Robots Simulation"
section: "Python 脚本"
module: "02-fundamentals-dev"
checksum: "ae5efd24d6541a83"
fetched: "2026-06-21T14:14:20"
---

* [Python Scripting and Tutorials](index.html)
* Robot Simulation Snippets

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Robot Simulation Snippets

Hint

Refer to the [Articulation](../py/source/extensions/isaacsim.core.experimental.prims/docs/index.html#isaacsim.core.experimental.prims.Articulation) class documentation for more details on the API.

## Wrapping Articulations

Note

The following snippets should only be run once on a new stage.
Create a new stage (File > New menu) and run the snippets in the Script Editor (Window > Script Editor menu).

Adds two Franka robots to the stage and wraps them via an [Articulation](../py/source/extensions/isaacsim.core.experimental.prims/docs/index.html#isaacsim.core.experimental.prims.Articulation) object to control them simultaneously.

```python
 1import isaacsim.core.experimental.utils.app as app_utils
 2import isaacsim.core.experimental.utils.stage as stage_utils
 3from isaacsim.core.experimental.prims import Articulation
 4from isaacsim.storage.native import get_assets_root_path
 5
 6# Add Franka robots to the stage
 7usd_path = get_assets_root_path() + "/Isaac/Robots/FrankaRobotics/FrankaPanda/franka.usd"
 8variants = [("Gripper", "AlternateFinger"), ("Mesh", "Quality")]
 9stage_utils.add_reference_to_stage(usd_path, path="/World/Franka_1", variants=variants)
10stage_utils.add_reference_to_stage(usd_path, path="/World/Franka_2", variants=variants)
11
12# Wrap Franka robots via an Articulation object
13articulations = Articulation(
14    "/World/Franka_.*",
15    positions=[[-1, -1, 0], [1, 1, 0]],
16    reset_xform_op_properties=True,
17)
```

Play the simulation.
Then, open a new tab in the Script Editor window (Tab > Add Tab menu) and execute the following code to set the DOF positions for each articulation.

```python
 1
 2from isaacsim.core.experimental.prims import Articulation
 3
 4# Wrap the existing Franka robots while the simulation is playing
 5articulations = Articulation("/World/Franka_.*")
 6
 7# Set the joint positions for each articulation
 8articulations.set_dof_position_targets(
 9    [
10        [1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 0.0, 0.0],
11        [-1.5, -1.5, -1.5, -1.5, -1.5, -1.5, -1.5, 0.04, 0.04],
12    ]
13)
14
```

## DOF Control

Note

The following snippets should only be run once on a new stage that has the Franka robot at the `/Franka` prim path,
and while the simulation is playing.

Prepare the scene:

1. Add a Franka robot to the stage via the Create > Robots > Franka Emika Panda Arm menu.
2. Play the simulation.

Warning

The snippets are disparate examples, running them out of order may have unintended consequences.
The resulting movements may not respect the robot’s kinematic limitations.

Make sure there is a Franka robot at the `/Franka` prim path and that the simulation is playing.
Then, open the Script Editor window (Window > Script Editor menu) and run the following snippets.

### Query Articulation

```python
 1from isaacsim.core.experimental.prims import Articulation
 2
 3articulation = Articulation("/Franka")
 4# Get articulation information
 5print("DOF count:", articulation.num_dofs)
 6print("DOF names:", articulation.dof_names)
 7print("DOF paths:", articulation.dof_paths)
 8print("DOF types:", articulation.dof_types)
 9print("Link count:", articulation.num_links)
10print("Link names:", articulation.link_names)
11print("Link paths:", articulation.link_paths)
```

### Read DOF States

```python
1from isaacsim.core.experimental.prims import Articulation
2
3articulation = Articulation("/Franka")
4# Get all DOF states
5print("DOF positions:", articulation.get_dof_positions())
6print("DOF velocities:", articulation.get_dof_velocities())
7print("DOF efforts:", articulation.get_dof_efforts())
```

### DOF Position Control

```python
1import numpy as np
2from isaacsim.core.experimental.prims import Articulation
3
4articulation = Articulation("/Franka")
5# Set all DOF positions to random values between -1 and 1
6articulation.set_dof_position_targets(np.random.rand(9) * 2 - 1)
```

### Single DOF Position Control

```python
1from isaacsim.core.experimental.prims import Articulation
2
3articulation = Articulation("/Franka")
4# Set the 'panda_finger_joint1' DOF position to 0.04.
5# The 'panda_finger_joint2' will mimic the value, as they are linked
6articulation.set_dof_position_targets(0.04, dof_indices=articulation.get_dof_indices("panda_finger_joint1"))
```

### DOF Velocity Control

```python
1import numpy as np
2from isaacsim.core.experimental.prims import Articulation
3
4articulation = Articulation("/Franka")
5# Switch to velocity control mode
6articulation.switch_dof_control_mode("velocity")
7# Set all DOF velocities to random values between -10 and 10
8articulation.set_dof_velocity_targets(10 * (np.random.rand(9) * 2 - 1))
```

### Single DOF Velocity Control

```python
1from isaacsim.core.experimental.prims import Articulation
2
3articulation = Articulation("/Franka")
4# Switch to velocity control mode
5articulation.switch_dof_control_mode("velocity")
6# Set the 'panda_joint4' DOF velocity to 0.25
7articulation.set_dof_velocity_targets(0.25, dof_indices=articulation.get_dof_indices("panda_joint4"))
```

### DOF Effort Control

```python
1import numpy as np
2from isaacsim.core.experimental.prims import Articulation
3
4articulation = Articulation("/Franka")
5# Switch to effort control mode
6articulation.switch_dof_control_mode("effort")
7# Set all DOF efforts to random values between -100 and 100
8articulation.set_dof_efforts(100 * (np.random.rand(9) * 2 - 1))
```

On this page

* [Wrapping Articulations](#wrapping-articulations)
* [DOF Control](#dof-control)
  + [Query Articulation](#query-articulation)
  + [Read DOF States](#read-dof-states)
  + [DOF Position Control](#dof-position-control)
  + [Single DOF Position Control](#single-dof-position-control)
  + [DOF Velocity Control](#dof-velocity-control)
  + [Single DOF Velocity Control](#single-dof-velocity-control)
  + [DOF Effort Control](#dof-effort-control)