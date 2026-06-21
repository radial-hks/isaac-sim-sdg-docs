---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/core_api_tutorials/tutorial_core_hello_world.html
title: "Hello World"
section: "Core API"
module: "02-fundamentals-dev"
checksum: "61d9e00ebb001502"
fetched: "2026-06-21T13:39:54"
---

* [Python Scripting and Tutorials](../python_scripting/index.html)
* [Core API Tutorial Series](index.html)
* Hello World

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Hello World

[NVIDIA Omniverse™ Kit](https://docs.omniverse.nvidia.com/dev-guide/latest/kit-architecture.html "(in Omniverse Developer Guide)"), the toolkit that NVIDIA Isaac Sim uses to build its applications, provides a Python interpreter for scripting. This means every single GUI command, as well as many additional functions are available as Python APIs. However, the learning curve for interfacing with Omniverse Kit using Pixar’s USD Python API is steep and steps are frequently tedious. Therefore we’ve provided a set of APIs that are designed to be used in robotics applications, APIs that abstract away the complexity of USD APIs and merge multiple steps into one for frequently performed tasks.

In this tutorial, we will present the concepts of Core APIs and how to use them. We will start with adding a cube to an empty stage, and we’ll build upon it to create a scene with multiple robots executing multiple tasks simultaneously, as seen below.

## Learning Objectives

This tutorial series introduces the Core API. After this tutorial, you learn:

* How to use the Core APIs to manipulate the USD stage.
* How to add a rigid body to the [Stage](../reference_material/reference_glossary.html#isaac-sim-glossary-stage) and simulate it using Python in NVIDIA Isaac Sim.
* The difference between running Python in an **Extension Workflow** vs a **Standalone Workflow**.

*10-15 Minute Tutorial*

## Getting Started

**Prerequisites**

* Intermediate knowledge in Python and asynchronous programming is required for this tutorial.
* Please download and install [Visual Studio Code](https://code.visualstudio.com/download) prior to beginning this tutorial.
* Please review [Quick Tutorials](../introduction/quickstart_index.html#isaac-sim-intro-quickstart-series) and [Workflows](../introduction/workflows.html#isaac-sim-app-tutorial-intro-workflows) prior to beginning this tutorial.

Begin by opening the *Hello World* example. First activate **Windows** > **Examples** > **Robotics Examples** which will open the `Robotics Examples` tab.

1. Click **Robotics Examples > General > Hello World**.
2. Verify that the window for the *Hello World* example extension is visible in the workspace.
3. Click the **Open Source Code** button to launch the source code for editing in [Visual Studio Code](https://code.visualstudio.com/download).
4. Click the **Open Containing Folder** button to open the directory containing the example files.

This folder contains three files: `hello_world.py`, `hello_world_extension.py`, and `__init__.py`.

The `hello_world.py` script is where the logic of the application will be added, while the UI
elements of the application will be added in `hello_world_extension.py` script and thus
linked to the logic.

1. Click **File > New From Stage Template > Empty** to create a new stage, click **Don’t Save** when prompted to save the current stage.
2. Click the **LOAD** button to load the World.
3. Open `hello_world.py` and press “Ctrl+S” to use the hot-reload feature. You will
   notice that the menu disappears from the workspace (because it was restarted).
4. Open the example menu again and click the **LOAD** button.

Now you can begin adding to this example.

## Code Overview

This example inherits from BaseSample, which is a boilerplate extension application that
sets up the basics for every robotics extension application. The following are a few examples of the
actions BaseSample performs:

1. Loading assets into the stage using a button.
2. Clearing the stage when a new stage is created.
3. Resetting objects to their default states.
4. Handling hot reloading.

Import packages:

```python
1import isaacsim.core.experimental.utils.stage as stage_utils
2from isaacsim.examples.base.base_sample_experimental import BaseSample
3from isaacsim.storage.native import get_assets_root_path
4
```

Setup scene:

```python
1    # This function is called to setup the assets in the scene for the first time
2    def setup_scene(self):
3        # Add ground plane directly to the stage
4        ground_plane = stage_utils.add_reference_to_stage(
5            usd_path=get_assets_root_path() + "/Isaac/Environments/Grid/default_environment.usd",
6            path="/World/ground",
7        )
8
```

Complete code:

```python
 1# -- Import Isaac sim packages -- #
 2import isaacsim.core.experimental.utils.stage as stage_utils
 3from isaacsim.examples.base.base_sample_experimental import BaseSample
 4from isaacsim.storage.native import get_assets_root_path
 5
 6# -- End of import Isaac sim packages -- #
 7
 8
 9class HelloWorld(BaseSample):
10    def __init__(self) -> None:
11        super().__init__()
12
13    # -- Set up scene -- #
14    # This function is called to setup the assets in the scene for the first time
15    def setup_scene(self):
16        # Add ground plane directly to the stage
17        ground_plane = stage_utils.add_reference_to_stage(
18            usd_path=get_assets_root_path() + "/Isaac/Environments/Grid/default_environment.usd",
19            path="/World/ground",
20        )
21
22    # -- End of set up scene -- #
```

### Key Concepts

**Stage Utilities**: The `stage_utils` module provides functions for directly manipulating the USD stage,
such as adding references, creating prims, and managing stage hierarchy.

**Prim Classes**: The API provides prim wrapper classes like `RigidPrim`, `GeomPrim`,
and `Articulation` that give you direct control over USD prims with physics capabilities.

**SimulationManager**: For callbacks and simulation events, the `SimulationManager` class provides
methods to register and deregister callbacks for various simulation events.

## Adding to the Scene

Use the Python API to add a cube as a rigid body to the scene. With the Core APIs,
create the geometry first, then apply collision and rigid body properties.

Import packages:

```python
1import isaacsim.core.experimental.utils.stage as stage_utils
2import numpy as np
3from isaacsim.core.experimental.materials import PreviewSurfaceMaterial
4from isaacsim.core.experimental.objects import Cube
5from isaacsim.core.experimental.prims import GeomPrim, RigidPrim
6from isaacsim.examples.base.base_sample_experimental import BaseSample
7from isaacsim.storage.native import get_assets_root_path
8
```

Adding a cube:

```python
 1        # Create a blue visual material for the cube
 2        visual_material = PreviewSurfaceMaterial("/World/Materials/blue")
 3        visual_material.set_input_values("diffuseColor", [0.0, 0.0, 1.0])
 4
 5        # Create the cube geometry
 6        self._cube_shape = Cube(
 7            paths="/World/fancy_cube",
 8            positions=np.array([[0.0, 0.0, 1.0]]),  # Starting position 1m above ground
 9            sizes=[1.0],
10            scales=np.array([[0.5015, 0.5015, 0.5015]]),  # Scale the cube
11            reset_xform_op_properties=True,
12        )
13
14        # Apply collision APIs to enable physics collision
15        GeomPrim(paths=self._cube_shape.paths, apply_collision_apis=True)
16
17        # Make it a rigid body (dynamic object that responds to physics)
18        self._cube = RigidPrim(paths=self._cube_shape.paths)
19
20        # Apply the blue material
21        self._cube_shape.apply_visual_materials(visual_material)
```

Complete code:

```python
 1# -- Import Isaac sim packages -- #
 2import isaacsim.core.experimental.utils.stage as stage_utils
 3import numpy as np
 4from isaacsim.core.experimental.materials import PreviewSurfaceMaterial
 5from isaacsim.core.experimental.objects import Cube
 6from isaacsim.core.experimental.prims import GeomPrim, RigidPrim
 7from isaacsim.examples.base.base_sample_experimental import BaseSample
 8from isaacsim.storage.native import get_assets_root_path
 9
10# -- End of import Isaac sim packages -- #
11
12
13class HelloWorld(BaseSample):
14    def __init__(self) -> None:
15        super().__init__()
16
17    def setup_scene(self):
18        # Add ground plane
19        ground_plane = stage_utils.add_reference_to_stage(
20            usd_path=get_assets_root_path() + "/Isaac/Environments/Grid/default_environment.usd",
21            path="/World/ground",
22        )
23
24        # -- Creating a cube and apply materials -- #
25        # Create a blue visual material for the cube
26        visual_material = PreviewSurfaceMaterial("/World/Materials/blue")
27        visual_material.set_input_values("diffuseColor", [0.0, 0.0, 1.0])
28
29        # Create the cube geometry
30        self._cube_shape = Cube(
31            paths="/World/fancy_cube",
32            positions=np.array([[0.0, 0.0, 1.0]]),  # Starting position 1m above ground
33            sizes=[1.0],
34            scales=np.array([[0.5015, 0.5015, 0.5015]]),  # Scale the cube
35            reset_xform_op_properties=True,
36        )
37
38        # Apply collision APIs to enable physics collision
39        GeomPrim(paths=self._cube_shape.paths, apply_collision_apis=True)
40
41        # Make it a rigid body (dynamic object that responds to physics)
42        self._cube = RigidPrim(paths=self._cube_shape.paths)
43
44        # Apply the blue material
45        self._cube_shape.apply_visual_materials(visual_material)
46        # -- End of creating a cube and apply materials -- #
```

1. Press **Ctrl+S** to save the code and hot-reload NVIDIA Isaac Sim.
2. Open the menu again.
3. Click the **LOAD** button.
4. See the dynamic cube falling as the simulation starts automatically.

Note

Every time the code is edited or changed, press **Ctrl+S** to save the code and hot-reload
NVIDIA Isaac Sim.

### Understanding the Prim Classes

The experimental API uses a layered approach to create physics-enabled objects:

1. **Cube** (or other shape classes): Creates the visual geometry on the USD stage.
2. **GeomPrim**: Wraps the geometry and can apply collision APIs for physics interactions.
3. **RigidPrim**: Adds rigid body dynamics, making the object respond to gravity and forces.

This modular approach gives you fine-grained control - you can create static colliders
(GeomPrim without RigidPrim) or fully dynamic objects (with both).

## Inspecting Object Properties

Print the world pose and velocity of the cube. The following lines show how you can query object properties.

```python
 1        # Query cube properties using RigidPrim methods
 2        positions, orientations = self._cube.get_world_poses()
 3        # get_velocities() returns a tuple: (linear_velocities, angular_velocities)
 4        linear_velocities, angular_velocities = self._cube.get_velocities()
 5
 6        # Convert from warp arrays to numpy for printing
 7        # Note: experimental APIs return batched results (even for single objects)
 8        print("Cube position is : " + str(positions.numpy()[0]))
 9        print("Cube's orientation is : " + str(orientations.numpy()[0]))
10        print("Cube's linear velocity is : " + str(linear_velocities.numpy()[0]))
```

Note

The experimental APIs return batched results as warp arrays. Use `.numpy()` to convert
them to numpy arrays, and index with `[0]` to get the first (and only) element when
working with a single object.

Complete code:

```python
 1import isaacsim.core.experimental.utils.stage as stage_utils
 2import numpy as np
 3from isaacsim.core.experimental.materials import PreviewSurfaceMaterial
 4from isaacsim.core.experimental.objects import Cube
 5from isaacsim.core.experimental.prims import GeomPrim, RigidPrim
 6from isaacsim.examples.base.base_sample_experimental import BaseSample
 7from isaacsim.storage.native import get_assets_root_path
 8
 9
10class HelloWorld(BaseSample):
11    def __init__(self) -> None:
12        super().__init__()
13
14    def setup_scene(self):
15        # Add ground plane
16        ground_plane = stage_utils.add_reference_to_stage(
17            usd_path=get_assets_root_path() + "/Isaac/Environments/Grid/default_environment.usd",
18            path="/World/ground",
19        )
20
21        # Create a blue visual material for the cube
22        visual_material = PreviewSurfaceMaterial("/World/Materials/blue")
23        visual_material.set_input_values("diffuseColor", [0.0, 0.0, 1.0])
24
25        # Create the cube geometry
26        self._cube_shape = Cube(
27            paths="/World/fancy_cube",
28            positions=np.array([[0.0, 0.0, 1.0]]),
29            sizes=[1.0],
30            scales=np.array([[0.5015, 0.5015, 0.5015]]),
31            reset_xform_op_properties=True,
32        )
33
34        # Apply collision and rigid body
35        GeomPrim(paths=self._cube_shape.paths, apply_collision_apis=True)
36        self._cube = RigidPrim(paths=self._cube_shape.paths)
37        self._cube_shape.apply_visual_materials(visual_material)
38
39    # This function is called after load button is pressed
40    # It's called once, after both setup_scene and one physics time step has finished
41    # to propagate physics handles needed to retrieve physical properties
42    async def setup_post_load(self):
43        # -- Begin query properties -- #
44        # Query cube properties using RigidPrim methods
45        positions, orientations = self._cube.get_world_poses()
46        # get_velocities() returns a tuple: (linear_velocities, angular_velocities)
47        linear_velocities, angular_velocities = self._cube.get_velocities()
48
49        # Convert from warp arrays to numpy for printing
50        # Note: experimental APIs return batched results (even for single objects)
51        print("Cube position is : " + str(positions.numpy()[0]))
52        print("Cube's orientation is : " + str(orientations.numpy()[0]))
53        print("Cube's linear velocity is : " + str(linear_velocities.numpy()[0]))
54        # -- End of query properties -- #
```

### Continuously Inspecting the Object Properties during Simulation

Print the world pose and velocity of the cube during simulation at every physics step
executed. As mentioned in [Workflows](../introduction/workflows.html#isaac-sim-app-tutorial-intro-workflows), in this workflow the
application is running asynchronously and can’t control when to step physics. However, you can add
callbacks to ensure certain things happen before certain events.

Import SimulationManager:

```python
1from isaacsim.core.simulation_manager import SimulationManager
2
```

Add a physics callback using the SimulationManager:

```python
1        # Register a physics callback using SimulationManager
2        from isaacsim.core.simulation_manager.impl.isaac_events import IsaacEvents
3
4        self._physics_callback_id = SimulationManager.register_callback(
5            self.print_cube_info, IsaacEvents.POST_PHYSICS_STEP
6        )
```

Deregister the callback during clean up:

```python
1        # Clean up callback when the extension is unloaded
2        if self._physics_callback_id is not None:
3            SimulationManager.deregister_callback(self._physics_callback_id)
4            self._physics_callback_id = None
```

Complete code:

```python
 1import isaacsim.core.experimental.utils.stage as stage_utils
 2import numpy as np
 3from isaacsim.core.experimental.materials import PreviewSurfaceMaterial
 4from isaacsim.core.experimental.objects import Cube
 5from isaacsim.core.experimental.prims import GeomPrim, RigidPrim
 6
 7# -- Begin loading SimulationManager -- #
 8from isaacsim.core.simulation_manager import SimulationManager
 9
10# -- End of loading SimulationManager -- #
11from isaacsim.examples.base.base_sample_experimental import BaseSample
12from isaacsim.storage.native import get_assets_root_path
13
14
15class HelloWorld(BaseSample):
16    def __init__(self) -> None:
17        super().__init__()
18        self._physics_callback_id = None
19
20    def setup_scene(self):
21        # Add ground plane
22        ground_plane = stage_utils.add_reference_to_stage(
23            usd_path=get_assets_root_path() + "/Isaac/Environments/Grid/default_environment.usd",
24            path="/World/ground",
25        )
26
27        # Create a blue visual material for the cube
28        visual_material = PreviewSurfaceMaterial("/World/Materials/blue")
29        visual_material.set_input_values("diffuseColor", [0.0, 0.0, 1.0])
30
31        # Create the cube geometry
32        self._cube_shape = Cube(
33            paths="/World/fancy_cube",
34            positions=np.array([[0.0, 0.0, 1.0]]),
35            sizes=[1.0],
36            scales=np.array([[0.5015, 0.5015, 0.5015]]),
37            reset_xform_op_properties=True,
38        )
39
40        # Apply collision and rigid body
41        GeomPrim(paths=self._cube_shape.paths, apply_collision_apis=True)
42        self._cube = RigidPrim(paths=self._cube_shape.paths)
43        self._cube_shape.apply_visual_materials(visual_material)
44
45    async def setup_post_load(self):
46        # -- Begin registering callback -- #
47        # Register a physics callback using SimulationManager
48        from isaacsim.core.simulation_manager.impl.isaac_events import IsaacEvents
49
50        self._physics_callback_id = SimulationManager.register_callback(
51            self.print_cube_info, IsaacEvents.POST_PHYSICS_STEP
52        )
53        # -- End of registering callback -- #
54
55    # Physics callback function - called after each physics step
56    # Takes dt (delta time) and context as arguments
57    def print_cube_info(self, dt, context):
58        positions, orientations = self._cube.get_world_poses()
59        linear_velocities, angular_velocities = self._cube.get_velocities()
60
61        print("Cube position is : " + str(positions.numpy()[0]))
62        print("Cube's orientation is : " + str(orientations.numpy()[0]))
63        print("Cube's linear velocity is : " + str(linear_velocities.numpy()[0]))
64
65    def physics_cleanup(self):
66        # -- Begin deregistering callback -- #
67        # Clean up callback when the extension is unloaded
68        if self._physics_callback_id is not None:
69            SimulationManager.deregister_callback(self._physics_callback_id)
70            self._physics_callback_id = None
71        # -- End of deregistering callback -- #
```

## Converting the Example to a Standalone Application

Note

* On windows use python.bat instead of python.sh
* The details of how python.sh works below are similar to how python.bat works

As mentioned in [Workflows](../introduction/workflows.html#isaac-sim-app-tutorial-intro-workflows), in this workflow, the robotics
application is started when launched from Python right away.

1. Open a new `my_application.py` file and add the following:

```python
 1# Launch Isaac Sim before any other imports
 2# Default first two lines in any standalone application
 3from isaacsim import SimulationApp
 4
 5simulation_app = SimulationApp({"headless": False})  # we can also run as headless
 6
 7# Now import Isaac Sim modules
 8import isaacsim.core.experimental.utils.stage as stage_utils
 9import numpy as np
10import omni.timeline
11from isaacsim.core.experimental.materials import PreviewSurfaceMaterial
12from isaacsim.core.experimental.objects import Cube
13from isaacsim.core.experimental.prims import GeomPrim, RigidPrim
14from isaacsim.core.simulation_manager import SimulationManager
15from isaacsim.storage.native import get_assets_root_path
16
17# Add ground plane
18ground_plane = stage_utils.add_reference_to_stage(
19    usd_path=get_assets_root_path() + "/Isaac/Environments/Grid/default_environment.usd",
20    path="/World/ground",
21)
22
23# Create a blue visual material for the cube
24visual_material = PreviewSurfaceMaterial("/World/Materials/blue")
25visual_material.set_input_values("diffuseColor", [0.0, 0.0, 1.0])
26
27# Create the cube geometry
28cube_shape = Cube(
29    paths="/World/fancy_cube",
30    positions=np.array([[0.0, 0.0, 1.0]]),
31    sizes=[1.0],
32    scales=np.array([[0.5, 0.5, 0.5]]),
33    reset_xform_op_properties=True,
34)
35
36# Apply collision and rigid body
37GeomPrim(paths=cube_shape.paths, apply_collision_apis=True)
38cube = RigidPrim(paths=cube_shape.paths)
39cube_shape.apply_visual_materials(visual_material)
40
41# Start the timeline (physics simulation)
42omni.timeline.get_timeline_interface().play()
43simulation_app.update()
44
45# Run the simulation loop
46for i in range(50):
47    # Only query when physics is actively simulating
48    if SimulationManager.is_simulating():
49        positions, orientations = cube.get_world_poses()
50        linear_velocities, angular_velocities = cube.get_velocities()
51
52        # Will be shown on terminal
53        print("Cube position is : " + str(positions.numpy()[0]))
54        print("Cube's orientation is : " + str(orientations.numpy()[0]))
55        print("Cube's linear velocity is : " + str(linear_velocities.numpy()[0]))
56
57    # Step the app (physics + rendering)
58    simulation_app.update()
59
60simulation_app.close()  # close Isaac Sim
```

1. Run it using `./python.sh ./exts/isaacsim.examples.interactive/isaacsim/examples/interactive/user_examples/my_application.py`.

## Summary

This tutorial covered the following topics:

1. Overview of the Core APIs for direct stage manipulation.
2. Using `stage_utils` to add assets to the stage.
3. Creating dynamic objects with `Cube`, `GeomPrim`, and `RigidPrim`.
4. Registering physics callbacks with `SimulationManager`.
5. Accessing dynamic properties for objects using prim wrapper methods.
6. The main differences in a standalone application.

### Next Steps

Continue to [Hello Robot](tutorial_core_hello_robot.html#isaac-sim-app-tutorial-core-hello-robot) to learn how to add a robot to the simulation.

Note

The next tutorials will be developed mainly using the extensions application workflow.
However, conversion to other workflows is similar given what was covered
in this tutorial.

On this page

* [Learning Objectives](#learning-objectives)
* [Getting Started](#getting-started)
* [Code Overview](#code-overview)
  + [Key Concepts](#key-concepts)
* [Adding to the Scene](#adding-to-the-scene)
  + [Understanding the Prim Classes](#understanding-the-prim-classes)
* [Inspecting Object Properties](#inspecting-object-properties)
  + [Continuously Inspecting the Object Properties during Simulation](#continuously-inspecting-the-object-properties-during-simulation)
* [Converting the Example to a Standalone Application](#converting-the-example-to-a-standalone-application)
* [Summary](#summary)
  + [Next Steps](#next-steps)