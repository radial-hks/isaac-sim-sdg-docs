---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/core_api_tutorials/tutorial_core_hello_robot.html
title: "Hello Robot"
section: "Core API"
module: "02-fundamentals-dev"
checksum: "73ae89d892cbc447"
fetched: "2026-06-21T12:48:08"
---

* [Python Scripting and Tutorials](../python_scripting/index.html)
* [Core API Tutorial Series](index.html)
* Hello Robot

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Hello Robot

## Learning Objectives

This tutorial details how to add and move a mobile robot in NVIDIA Isaac Sim in an extension application.
After this tutorial, you will understand how to add a robot to the simulation and apply actions to
its wheels using Python.

*10-15 Minute Tutorial*

## Getting Started

**Prerequisites**

* Review [Hello World](tutorial_core_hello_world.html#isaac-sim-app-tutorial-core-hello-world) prior to beginning this tutorial.

Begin with the source code of the **Hello World** example developed in the previous tutorial:
[Hello World](tutorial_core_hello_world.html#isaac-sim-app-tutorial-core-hello-world).

## Adding a Robot

Begin by adding a NVIDIA Jetbot to the scene. You can do so by accessing the library of NVIDIA Isaac Sim
robots, sensors, and environments located on a [Omniverse Nucleus](../reference_material/reference_glossary.html#isaac-sim-glossary-nucleus) Server using Python,
as well as navigate through it using the **Content** window, under **Isaac Sim > robots > NVIDIA > jetbot.usd**.

Note

The server shown in these steps has been connected to in [Workstation Setup](../installation/install_workstation.html#isaac-sim-install-workstation). Follow these steps first before proceeding.

1. Add the assets by simply dragging them to the stage window or the viewport.
2. Try to do the same thing through Python in the **Hello World** example.
3. Create a new stage: **File > new > Donât Save**
4. Open the `hello_world.py` file by clicking the **Open Source Code**
   button in the **Hello World** window.

Import packages:

```python
1import carb
2import isaacsim.core.experimental.utils.stage as stage_utils
3from isaacsim.core.experimental.prims import Articulation
4from isaacsim.examples.base.base_sample_experimental import BaseSample
5from isaacsim.storage.native import get_assets_root_path
6
```

Setup scene:

```python
1        # Add the Jetbot robot to the stage
2        asset_path = assets_root_path + "/Isaac/Robots/NVIDIA/Jetbot/jetbot.usd"
3        stage_utils.add_reference_to_stage(usd_path=asset_path, path="/World/Fancy_Robot")
```

Articulate the robot:

```python
1        # Wrap the Jetbot with the Articulation class for control
2        self._jetbot = Articulation("/World/Fancy_Robot")
```

Complete code:

```python
 1# -- Begin importing Isaac packages -- #
 2import carb
 3import isaacsim.core.experimental.utils.stage as stage_utils
 4from isaacsim.core.experimental.prims import Articulation
 5from isaacsim.examples.base.base_sample_experimental import BaseSample
 6from isaacsim.storage.native import get_assets_root_path
 7
 8# -- End of importing Isaac packages -- #
 9
10
11class HelloWorld(BaseSample):
12    def __init__(self) -> None:
13        super().__init__()
14
15    def setup_scene(self):
16        # Add ground plane
17        ground_plane = stage_utils.add_reference_to_stage(
18            usd_path=get_assets_root_path() + "/Isaac/Environments/Grid/default_environment.usd",
19            path="/World/ground",
20        )
21
22        # Get the assets root path from the Nucleus server
23        assets_root_path = get_assets_root_path()
24        if assets_root_path is None:
25            carb.log_error("Could not find nucleus server with /Isaac folder")
26            return
27
28        # -- Begin adding Jetbot -- #
29        # Add the Jetbot robot to the stage
30        asset_path = assets_root_path + "/Isaac/Robots/NVIDIA/Jetbot/jetbot.usd"
31        stage_utils.add_reference_to_stage(usd_path=asset_path, path="/World/Fancy_Robot")
32        # -- End of adding Jetbot -- #
33
34    async def setup_post_load(self):
35        # -- Begin articulation -- #
36        # Wrap the Jetbot with the Articulation class for control
37        self._jetbot = Articulation("/World/Fancy_Robot")
38        # -- End of articulation -- #
39
40        # Print info about the Jetbot
41        print("Number of DOFs: " + str(self._jetbot.num_dofs))
42        print("DOF names: " + str(self._jetbot.dof_names))
43        print("Joint Positions: " + str(self._jetbot.get_dof_positions().numpy()))
```

Click the **LOAD** button to load the scene and see the Jetbot appear. Although it is being simulated,
it is not moving. The next section walks through how to make the robot move.

## Move the Robot

In NVIDIA Isaac Sim, Robots are constructed of physically accurate articulated joints. Applying actions
to these articulations make them move.

Next, apply random velocities to the Jetbotâs wheel joints to get it moving.

Importing SimulationManager:

```python
1from isaacsim.core.simulation_manager import SimulationManager
2
```

Registering callbacks:

```python
1        # Register a physics callback to send actions every physics step
2        from isaacsim.core.simulation_manager.impl.isaac_events import IsaacEvents
3
4        self._physics_callback_id = SimulationManager.register_callback(
5            self.send_robot_actions, IsaacEvents.POST_PHYSICS_STEP
6        )
```

Define command function:

```python
1    def send_robot_actions(self, dt, context):
2        # Apply random velocity targets to the wheel joints
3        # Jetbot has 2 DOFs: left_wheel_joint and right_wheel_joint
4        random_velocities = 5 * np.random.rand(1, 2)  # Shape: (1, num_dofs)
5        self._jetbot.set_dof_velocity_targets(random_velocities)
6
```

Complete code:

```python
 1import carb
 2import isaacsim.core.experimental.utils.stage as stage_utils
 3import numpy as np
 4from isaacsim.core.experimental.prims import Articulation
 5
 6# -- Begin importing SimulationManager -- #
 7from isaacsim.core.simulation_manager import SimulationManager
 8
 9# -- End of importing SimulationManager -- #
10from isaacsim.examples.base.base_sample_experimental import BaseSample
11from isaacsim.storage.native import get_assets_root_path
12
13
14class HelloWorld(BaseSample):
15    def __init__(self) -> None:
16        super().__init__()
17        self._physics_callback_id = None
18
19    def setup_scene(self):
20        # Add ground plane
21        ground_plane = stage_utils.add_reference_to_stage(
22            usd_path=get_assets_root_path() + "/Isaac/Environments/Grid/default_environment.usd",
23            path="/World/ground",
24        )
25
26        # Get the assets root path from the Nucleus server
27        assets_root_path = get_assets_root_path()
28        if assets_root_path is None:
29            carb.log_error("Could not find nucleus server with /Isaac folder")
30            return
31
32        # Add the Jetbot robot to the stage
33        asset_path = assets_root_path + "/Isaac/Robots/NVIDIA/Jetbot/jetbot.usd"
34        stage_utils.add_reference_to_stage(usd_path=asset_path, path="/World/Fancy_Robot")
35
36    async def setup_post_load(self):
37        # Wrap the Jetbot with the Articulation class for control
38        self._jetbot = Articulation("/World/Fancy_Robot")
39
40        # -- Begin registering callback -- #
41        # Register a physics callback to send actions every physics step
42        from isaacsim.core.simulation_manager.impl.isaac_events import IsaacEvents
43
44        self._physics_callback_id = SimulationManager.register_callback(
45            self.send_robot_actions, IsaacEvents.POST_PHYSICS_STEP
46        )
47        # -- End of registering callback -- #
48
49    # -- Begin sending actions -- #
50    def send_robot_actions(self, dt, context):
51        # Apply random velocity targets to the wheel joints
52        # Jetbot has 2 DOFs: left_wheel_joint and right_wheel_joint
53        random_velocities = 5 * np.random.rand(1, 2)  # Shape: (1, num_dofs)
54        self._jetbot.set_dof_velocity_targets(random_velocities)
55
56    # -- End of sending actions -- #
57
58    def physics_cleanup(self):
59        # Clean up callback when the extension is unloaded
60        if self._physics_callback_id is not None:
61            SimulationManager.deregister_callback(self._physics_callback_id)
62            self._physics_callback_id = None
```

Click the **LOAD** button to load the scene and watch the Jetbot move with random velocities.

Note

Pressing **STOP**, then **PLAY** in this workflow might not reset the world properly. Use
the **RESET** button instead.

### Extra Practice

This example applies random velocities to the Jetbot articulation controller. Try the following
exercises:

1. Make the Jetbot move backwards (hint: use negative velocities).
2. Make the Jetbot turn right (hint: apply different velocities to each wheel).
3. Make the Jetbot stop after 5 seconds (hint: track elapsed time in the callback).

## Controlling Specific Joints

You can also control specific joints by their names or indices. Hereâs how to get the wheel
joint indices and apply velocities only to specific joints:

Getting wheel indices:

```python
1        # Print available DOF names
2        print("Available DOFs:", self._jetbot.dof_names)
3
4        # Get indices for specific wheel joints
5        self._wheel_indices = self._jetbot.get_dof_indices(["left_wheel_joint", "right_wheel_joint"]).numpy()
6        print("Wheel indices:", self._wheel_indices)
```

Setting wheel velocities using indices:

```python
1        # Apply velocity targets to specific DOF indices
2        wheel_velocities = np.array([[10.0, 10.0]])  # Both wheels same speed = forward
3        self._jetbot.set_dof_velocity_targets(wheel_velocities, dof_indices=self._wheel_indices)
```

Complete code:

```python
 1import carb
 2import isaacsim.core.experimental.utils.stage as stage_utils
 3import numpy as np
 4from isaacsim.core.experimental.prims import Articulation
 5from isaacsim.core.simulation_manager import SimulationManager
 6from isaacsim.examples.base.base_sample_experimental import BaseSample
 7from isaacsim.storage.native import get_assets_root_path
 8
 9
10class HelloWorld(BaseSample):
11    def __init__(self) -> None:
12        super().__init__()
13        self._physics_callback_id = None
14
15    def setup_scene(self):
16        # Add ground plane
17        ground_plane = stage_utils.add_reference_to_stage(
18            usd_path=get_assets_root_path() + "/Isaac/Environments/Grid/default_environment.usd",
19            path="/World/ground",
20        )
21
22        # Add the Jetbot robot to the stage
23        assets_root_path = get_assets_root_path()
24        asset_path = assets_root_path + "/Isaac/Robots/NVIDIA/Jetbot/jetbot.usd"
25        stage_utils.add_reference_to_stage(usd_path=asset_path, path="/World/Fancy_Robot")
26
27    async def setup_post_load(self):
28        # Wrap the Jetbot with the Articulation class
29        self._jetbot = Articulation("/World/Fancy_Robot")
30
31        # -- Begin getting indices -- #
32        # Print available DOF names
33        print("Available DOFs:", self._jetbot.dof_names)
34
35        # Get indices for specific wheel joints
36        self._wheel_indices = self._jetbot.get_dof_indices(["left_wheel_joint", "right_wheel_joint"]).numpy()
37        print("Wheel indices:", self._wheel_indices)
38        # -- End of getting indices -- #
39
40        # Register physics callback
41        from isaacsim.core.simulation_manager.impl.isaac_events import IsaacEvents
42
43        self._physics_callback_id = SimulationManager.register_callback(
44            self.send_robot_actions, IsaacEvents.POST_PHYSICS_STEP
45        )
46
47    def send_robot_actions(self, dt, context):
48        # -- Begin setting wheel velocity -- #
49        # Apply velocity targets to specific DOF indices
50        wheel_velocities = np.array([[10.0, 10.0]])  # Both wheels same speed = forward
51        self._jetbot.set_dof_velocity_targets(wheel_velocities, dof_indices=self._wheel_indices)
52        # -- End of setting wheel velocity -- #
53
54    def physics_cleanup(self):
55        if self._physics_callback_id is not None:
56            SimulationManager.deregister_callback(self._physics_callback_id)
57            self._physics_callback_id = None
```

## Summary

This tutorial covered the following topics:

1. Adding NVIDIA Isaac Sim library components from a Nucleus Server
2. Adding a robot to the stage using `stage_utils.add_reference_to_stage()`
3. Wrapping a robot with the `Articulation` class for control
4. Using `set_dof_velocity_targets()` to apply velocity control
5. Registering physics callbacks with `SimulationManager`
6. Controlling specific joints by name or index

### Next Steps

Continue on to the next tutorial in the Essential Tutorials series, [Adding a Manipulator Robot](tutorial_core_adding_manipulator.html#isaac-sim-app-tutorial-core-adding-manipulator),
to learn how to add a manipulator robot to the simulation.

### Further Learning

**Nucleus Server**

* For an overview of how to best leverage a Nucleus Server, see the [Nucleus Overview in NVIDIA Omniverse](https://youtu.be/JaoIQ4YBnBE)
  tutorial.

**Robot Specific Extensions**

* NVIDIA Isaac Sim provides several robot extensions, including `isaacsim.robot.experimental.wheeled_robots`,
  and `isaacsim.robot.experimental.manipulators.examples`.
  To learn more, check out the standalone examples located at `standalone_examples/api/isaacsim.robot.experimental.manipulators/franka`
  and `standalone_examples/api/isaacsim.robot.experimental.manipulators/universal_robots/`.

On this page

* [Learning Objectives](#learning-objectives)
* [Getting Started](#getting-started)
* [Adding a Robot](#adding-a-robot)
* [Move the Robot](#move-the-robot)
  + [Extra Practice](#extra-practice)
* [Controlling Specific Joints](#controlling-specific-joints)
* [Summary](#summary)
  + [Next Steps](#next-steps)
  + [Further Learning](#further-learning)