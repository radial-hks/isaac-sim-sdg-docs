# 开发基础 (Development Fundamentals)

> 开发工具、Python 脚本、Core API 教程 — 日常开发必备
> Isaac Sim 版本: 6.0
> 最后组装: 2026-06-21 12:48 UTC
> 来源页数: 21

---

## 来源链接

- [Development Tools Index](https://docs.isaacsim.omniverse.nvidia.com/latest/development_tools/index.html)
- [VS Code](https://docs.isaacsim.omniverse.nvidia.com/latest/development_tools/vscode.html)
- [Python Server](https://docs.isaacsim.omniverse.nvidia.com/latest/development_tools/python_server.html)
- [Jupyter Notebook](https://docs.isaacsim.omniverse.nvidia.com/latest/development_tools/jupyter_notebook.html)
- [Script Editor](https://docs.isaacsim.omniverse.nvidia.com/latest/development_tools/omniverse_script_editor.html)
- [Isaac Sim MCP Server](https://docs.isaacsim.omniverse.nvidia.com/latest/development_tools/isaac_sim_mcp.html)
- [Carb Settings](https://docs.isaacsim.omniverse.nvidia.com/latest/development_tools/carb_settings.html)
- [Python Scripting Index](https://docs.isaacsim.omniverse.nvidia.com/latest/python_scripting/index.html)
- [Scripting Concepts](https://docs.isaacsim.omniverse.nvidia.com/latest/python_scripting/python_scripting_concepts.html)
- [Core API Overview](https://docs.isaacsim.omniverse.nvidia.com/latest/python_scripting/core_api_overview.html)
- [Environment Setup](https://docs.isaacsim.omniverse.nvidia.com/latest/python_scripting/environment_setup.html)
- [Standalone Python](https://docs.isaacsim.omniverse.nvidia.com/latest/python_scripting/manual_standalone_python.html)
- [Robots Simulation](https://docs.isaacsim.omniverse.nvidia.com/latest/python_scripting/robots_simulation.html)
- [Util Snippets](https://docs.isaacsim.omniverse.nvidia.com/latest/python_scripting/util_snippets.html)
- [Core API Tutorials Index](https://docs.isaacsim.omniverse.nvidia.com/latest/core_api_tutorials/index.html)
- [Hello World](https://docs.isaacsim.omniverse.nvidia.com/latest/core_api_tutorials/tutorial_core_hello_world.html)
- [Hello Robot](https://docs.isaacsim.omniverse.nvidia.com/latest/core_api_tutorials/tutorial_core_hello_robot.html)
- [Adding Manipulator](https://docs.isaacsim.omniverse.nvidia.com/latest/core_api_tutorials/tutorial_core_adding_manipulator.html)
- [Adding Multiple Robots](https://docs.isaacsim.omniverse.nvidia.com/latest/core_api_tutorials/tutorial_core_adding_multiple_robots.html)
- [Multiple Tasks](https://docs.isaacsim.omniverse.nvidia.com/latest/core_api_tutorials/tutorial_core_multiple_tasks.html)
- [Adding Props](https://docs.isaacsim.omniverse.nvidia.com/latest/core_api_tutorials/tutorial_core_adding_props.html)

---


## Core API

### Core API Tutorials Index

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/development_tools/index.html

* [Python Scripting and Tutorials](../python_scripting/index.html)
* Core API Tutorial Series

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Core API Tutorial Series

The Core API tutorials is for beginner NVIDIA Isaac Sim users. This tutorial series details how to control wheeled robots and manipulators with controllers while logging robot and environment data.

* [Hello World](tutorial_core_hello_world.html)
* [Hello Robot](tutorial_core_hello_robot.html)
* [Adding a Manipulator Robot](tutorial_core_adding_manipulator.html)
* [Adding Multiple Robots](tutorial_core_adding_multiple_robots.html)
* [Multiple Robot Scenarios](tutorial_core_multiple_tasks.html)
* [Adding Props](tutorial_core_adding_props.html)

---

### Core API Tutorials Index

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/python_scripting/index.html

* [Python Scripting and Tutorials](../python_scripting/index.html)
* Core API Tutorial Series

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Core API Tutorial Series

The Core API tutorials is for beginner NVIDIA Isaac Sim users. This tutorial series details how to control wheeled robots and manipulators with controllers while logging robot and environment data.

* [Hello World](tutorial_core_hello_world.html)
* [Hello Robot](tutorial_core_hello_robot.html)
* [Adding a Manipulator Robot](tutorial_core_adding_manipulator.html)
* [Adding Multiple Robots](tutorial_core_adding_multiple_robots.html)
* [Multiple Robot Scenarios](tutorial_core_multiple_tasks.html)
* [Adding Props](tutorial_core_adding_props.html)

---

### Core API Tutorials Index

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/core_api_tutorials/index.html

* [Python Scripting and Tutorials](../python_scripting/index.html)
* Core API Tutorial Series

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Core API Tutorial Series

The Core API tutorials is for beginner NVIDIA Isaac Sim users. This tutorial series details how to control wheeled robots and manipulators with controllers while logging robot and environment data.

* [Hello World](tutorial_core_hello_world.html)
* [Hello Robot](tutorial_core_hello_robot.html)
* [Adding a Manipulator Robot](tutorial_core_adding_manipulator.html)
* [Adding Multiple Robots](tutorial_core_adding_multiple_robots.html)
* [Multiple Robot Scenarios](tutorial_core_multiple_tasks.html)
* [Adding Props](tutorial_core_adding_props.html)

---

### Hello World

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/core_api_tutorials/tutorial_core_hello_world.html

* [Python Scripting and Tutorials](../python_scripting/index.html)
* [Core API Tutorial Series](index.html)
* Hello World

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Hello World

[NVIDIA Omniverseâ¢ Kit](https://docs.omniverse.nvidia.com/dev-guide/latest/kit-architecture.html "(in Omniverse Developer Guide)"), the toolkit that NVIDIA Isaac Sim uses to build its applications, provides a Python interpreter for scripting. This means every single GUI command, as well as many additional functions are available as Python APIs. However, the learning curve for interfacing with Omniverse Kit using Pixarâs USD Python API is steep and steps are frequently tedious. Therefore weâve provided a set of APIs that are designed to be used in robotics applications, APIs that abstract away the complexity of USD APIs and merge multiple steps into one for frequently performed tasks.

In this tutorial, we will present the concepts of Core APIs and how to use them. We will start with adding a cube to an empty stage, and weâll build upon it to create a scene with multiple robots executing multiple tasks simultaneously, as seen below.

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

1. Click **File > New From Stage Template > Empty** to create a new stage, click **Donât Save** when prompted to save the current stage.
2. Click the **LOAD** button to load the World.
3. Open `hello_world.py` and press âCtrl+Sâ to use the hot-reload feature. You will
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
application is running asynchronously and canât control when to step physics. However, you can add
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

---

### Hello Robot

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/core_api_tutorials/tutorial_core_hello_robot.html

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

---

### Adding Manipulator

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/core_api_tutorials/tutorial_core_adding_manipulator.html

* [Python Scripting and Tutorials](../python_scripting/index.html)
* [Core API Tutorial Series](index.html)
* Adding a Manipulator Robot

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Adding a Manipulator Robot

## Learning Objectives

This tutorial introduces a manipulator robot to the simulation, a Franka Panda.
It describes how to add the robot to the scene and execute a pick-and-place operation.
After this tutorial, you will have more experience using manipulator robots and
controlling them with inverse kinematics in NVIDIA Isaac Sim.

*15-20 Minute Tutorial*

## Getting Started

**Prerequisites**

* Review [Hello Robot](tutorial_core_hello_robot.html#isaac-sim-app-tutorial-core-hello-robot) prior to beginning this tutorial.

This tutorial uses **standalone Python scripts**. Run them with a Python environment where Isaac Sim is installed:

## Creating the Scene with a Franka Robot

Add a Franka robot and a cube for the robot to pick up using the `Franka` class.
This class inherits from `Articulation` and provides high-level control methods including
inverse kinematics and gripper control.

When you set `create_robot=True` in the constructor, `Franka` automatically
spawns the Franka robot USD asset at the specified path.

```python
 1"""Create a scene with ground, Franka robot, and blue cube."""
 2
 3import argparse
 4
 5parser = argparse.ArgumentParser()
 6parser.add_argument("--test", action="store_true")
 7args, _ = parser.parse_known_args()
 8
 9from isaacsim import SimulationApp
10
11simulation_app = SimulationApp({"headless": False})
12
13import isaacsim.core.experimental.utils.app as app_utils
14
15app_utils.enable_extension("isaacsim.robot.experimental.manipulators.examples")
16
17from isaacsim.core.experimental.objects import Cube, DomeLight, GroundPlane
18from isaacsim.core.experimental.prims import GeomPrim, RigidPrim
19from isaacsim.core.simulation_manager import SimulationManager
20from isaacsim.robot.experimental.manipulators.examples.franka import Franka
21
22DEVICE = "cpu"
23
24GroundPlane("/World/ground_plane")
25dome_light = DomeLight("/World/DomeLight")
26dome_light.set_intensities(1000)
27
28# Create the Franka robot
29robot = Franka(robot_path="/World/robot", create_robot=True)
30
31# Create a blue cube for the robot to pick up
32cube_shape = Cube(
33    paths="/World/Cube",
34    positions=[0.5, 0.0, 0.0258],
35    sizes=1.0,
36    scales=[0.0515, 0.0515, 0.0515],
37    colors="blue",
38)
39GeomPrim(paths=cube_shape.paths, apply_collision_apis=True)
40RigidPrim(paths=cube_shape.paths)
41
42SimulationManager.setup_simulation(dt=1.0 / 60.0, device=DEVICE)
43physics_scene = SimulationManager.get_physics_scenes()[0]
44physics_scene.set_enabled_gpu_dynamics(False)
45app_utils.play()
46app_utils.update_app(steps=20)
47
48step_count = 0
49max_test_steps = 60
50while simulation_app.is_running():
51    simulation_app.update()
52    step_count += 1
53    if args.test and step_count >= max_test_steps:
54        break
55
56app_utils.stop()
57simulation_app.close()
```

Run the script. A window opens with the Franka robot and cube in the scene; the simulation runs until you close the window.

The `Franka` class provides these key methods for robot control:

* `set_end_effector_pose(position, orientation)` - Move end-effector using inverse kinematics
* `open_gripper()` / `close_gripper()` - Control the gripper
* `get_current_state()` - Get DOF positions and end-effector pose
* `get_downward_orientation()` - Get quaternion for downward-facing orientation
* `reset_to_default_pose()` - Reset robot to home position

## Using FrankaPickPlace for Complete Pick-and-Place

For a complete pick-and-place operation, use the `FrankaPickPlace` class. This class has a
`setup_scene()` method that spawns everything needed for pick-and-place: the Franka robot,
ground plane, and a cube to manipulate.

```python
 1"""Pick-and-place using FrankaPickPlace."""
 2
 3import argparse
 4
 5parser = argparse.ArgumentParser()
 6parser.add_argument("--test", action="store_true")
 7args, _ = parser.parse_known_args()
 8
 9from isaacsim import SimulationApp
10
11simulation_app = SimulationApp({"headless": False})
12
13import isaacsim.core.experimental.utils.app as app_utils
14
15app_utils.enable_extension("isaacsim.robot.experimental.manipulators.examples")
16
17from isaacsim.core.experimental.objects import DomeLight, GroundPlane
18from isaacsim.core.simulation_manager import SimulationManager
19from isaacsim.robot.experimental.manipulators.examples.franka import FrankaPickPlace
20
21DEVICE = "cpu"
22
23GroundPlane("/World/ground_plane")
24dome_light = DomeLight("/World/DomeLight")
25dome_light.set_intensities(1000)
26
27# FrankaPickPlace spawns robot and cube, and provides the pick-place state machine
28controller = FrankaPickPlace()
29controller.setup_scene()
30
31SimulationManager.setup_simulation(dt=1.0 / 60.0, device=DEVICE)
32physics_scene = SimulationManager.get_physics_scenes()[0]
33physics_scene.set_enabled_gpu_dynamics(False)
34app_utils.play()
35# Run a few steps so the articulation's physics tensor entity is valid before `controller.reset()`
36app_utils.update_app(steps=20)
37controller.reset()
38
39# Main loop: run one pick-place step each physics frame until done
40step_count = 0
41max_test_steps = sum(controller.events_dt) + 60
42while simulation_app.is_running():
43    simulation_app.update()
44    step_count += 1
45    if app_utils.is_playing():
46        if not controller.is_done():
47            controller.forward()
48        else:
49            print("Pick-and-place completed")
50            app_utils.pause()
51            if args.test:
52                break
53    if args.test and step_count >= max_test_steps:
54        raise RuntimeError("Pick-and-place did not complete within the test step budget")
55
56app_utils.stop()
57simulation_app.close()
```

Run the script. The robot automatically executes all phases of picking up and placing the cube.

## Understanding the Pick-and-Place State Machine

The `FrankaPickPlace` class uses a state machine with the following phases:

Pick-and-Place Phases

| Phase | Description | Default Steps |
| --- | --- | --- |
| 0 | Move to x,y position above cube | 60 |
| 1 | Approach down to cube | 40 |
| 2 | Close gripper to grasp | 20 |
| 3 | Lift cube upward | 40 |
| 4 | Move cube to target location | 80 |
| 5 | Open gripper to release | 20 |
| 6 | Move up and away | 20 |

You can customize the phase durations by passing `events_dt` to the constructor, and change the cube starting position using `setup_scene`:

```python
1# Custom phase durations (steps for each phase)
2controller = FrankaPickPlace(events_dt=[80, 60, 30, 60, 100, 30, 30])
3# Customize cube position, size, and target position
4controller.setup_scene(
5    cube_initial_position=[0.4, 0.2, 0.0258], cube_size=[0.05, 0.05, 0.05], target_position=[-0.4, 0.2, 0.12]
6)
```

Complete code:

```python
 1"""Pick-and-place using FrankaPickPlace."""
 2
 3import argparse
 4
 5parser = argparse.ArgumentParser()
 6parser.add_argument("--test", action="store_true")
 7args, _ = parser.parse_known_args()
 8
 9from isaacsim import SimulationApp
10
11simulation_app = SimulationApp({"headless": False})
12
13import isaacsim.core.experimental.utils.app as app_utils
14
15app_utils.enable_extension("isaacsim.robot.experimental.manipulators.examples")
16
17from isaacsim.core.experimental.objects import DomeLight, GroundPlane
18from isaacsim.core.simulation_manager import SimulationManager
19from isaacsim.robot.experimental.manipulators.examples.franka import FrankaPickPlace
20
21DEVICE = "cpu"
22
23GroundPlane("/World/ground_plane")
24dome_light = DomeLight("/World/DomeLight")
25dome_light.set_intensities(1000)
26
27# -- Begin custom setup -- #
28# Custom phase durations (steps for each phase)
29controller = FrankaPickPlace(events_dt=[80, 60, 30, 60, 100, 30, 30])
30# Customize cube position, size, and target position
31controller.setup_scene(
32    cube_initial_position=[0.4, 0.2, 0.0258], cube_size=[0.05, 0.05, 0.05], target_position=[-0.4, 0.2, 0.12]
33)
34# -- End of custom setup -- #
35
36SimulationManager.setup_simulation(dt=1.0 / 60.0, device=DEVICE)
37physics_scene = SimulationManager.get_physics_scenes()[0]
38physics_scene.set_enabled_gpu_dynamics(False)
39app_utils.play()
40# Run a few steps so the articulation's physics tensor entity is valid before `controller.reset()`
41app_utils.update_app(steps=20)
42controller.reset()
43
44# Main loop: run one pick-place step each physics frame until done
45step_count = 0
46max_test_steps = sum(controller.events_dt) + 60
47while simulation_app.is_running():
48    simulation_app.update()
49    step_count += 1
50    if app_utils.is_playing():
51        if not controller.is_done():
52            controller.forward()
53        else:
54            print("Pick-and-place completed")
55            app_utils.pause()
56            if args.test:
57                break
58    if args.test and step_count >= max_test_steps:
59        raise RuntimeError("Pick-and-place did not complete within the test step budget")
60
61app_utils.stop()
62simulation_app.close()
```

## See Also

For a complete standalone pick-and-place example with `--device`, `--ik-method`, and `--test` options, see
`standalone_examples/api/isaacsim.robot.experimental.manipulators/franka/pick_place.py`.

## Summary

This tutorial covered the following topics:

1. Adding a Franka manipulator robot using `Franka` with `create_robot=True`
2. Using the `FrankaPickPlace.setup_scene()` method to spawn a complete pick-and-place scene
3. Executing pick-and-place operations with the `forward()` method
4. Understanding and customizing the pick-and-place state machine phases

### Next Steps

Continue to the next tutorial in our Essential Tutorials series, [Adding Multiple Robots](tutorial_core_adding_multiple_robots.html#isaac-sim-app-tutorial-core-adding-multiple-robots),
to learn how to add multiple robots to the simulation.

On this page

* [Learning Objectives](#learning-objectives)
* [Getting Started](#getting-started)
* [Creating the Scene with a Franka Robot](#creating-the-scene-with-a-franka-robot)
* [Using FrankaPickPlace for Complete Pick-and-Place](#using-frankapickplace-for-complete-pick-and-place)
* [Understanding the Pick-and-Place State Machine](#understanding-the-pick-and-place-state-machine)
* [See Also](#see-also)
* [Summary](#summary)
  + [Next Steps](#next-steps)

---

### Adding Multiple Robots

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/core_api_tutorials/tutorial_core_adding_multiple_robots.html

* [Python Scripting and Tutorials](../python_scripting/index.html)
* [Core API Tutorial Series](index.html)
* Adding Multiple Robots

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Adding Multiple Robots

## Learning Objectives

This tutorial integrates two different types of robots into the same simulation:
a mobile robot (Jetbot) and a manipulator (Franka), working together to accomplish a task.
The Jetbot pushes a cube towards the Franka, which then picks it up.
After this tutorial, you will have experience building multi-robot simulations with object interaction.

*15-20 Minute Tutorial*

## Getting Started

**Prerequisites**

* Review [Adding a Manipulator Robot](tutorial_core_adding_manipulator.html#isaac-sim-app-tutorial-core-adding-manipulator) prior to beginning this tutorial.

Begin with the source code open from the previous tutorial, [Adding a Manipulator Robot](tutorial_core_adding_manipulator.html#isaac-sim-app-tutorial-core-adding-manipulator).

Note

Pressing **STOP**, then **PLAY** in this workflow might not reset the world properly. Use
the **RESET** button instead.

## Creating the Scene

Begin by adding the Jetbot, Franka Panda, and the Cube from the previous tutorials to the scene.

```python
 1import isaacsim.core.experimental.utils.stage as stage_utils
 2import numpy as np
 3from isaacsim.core.experimental.materials import PreviewSurfaceMaterial
 4from isaacsim.core.experimental.objects import Cube
 5from isaacsim.core.experimental.prims import Articulation, GeomPrim, RigidPrim, XformPrim
 6from isaacsim.examples.base.base_sample_experimental import BaseSample
 7from isaacsim.storage.native import get_assets_root_path
 8
 9
10class HelloWorld(BaseSample):
11    def __init__(self) -> None:
12        super().__init__()
13
14    # -- Begin setup_scene -- #
15    def setup_scene(self):
16        assets_root_path = get_assets_root_path()
17
18        # Add ground plane
19        stage_utils.add_reference_to_stage(
20            usd_path=assets_root_path + "/Isaac/Environments/Grid/default_environment.usd",
21            path="/World/ground",
22        )
23
24        # Add Jetbot mobile robot
25        stage_utils.add_reference_to_stage(
26            usd_path=assets_root_path + "/Isaac/Robots/NVIDIA/Jetbot/jetbot.usd",
27            path="/World/Jetbot",
28        )
29
30        # Add a cube in front of Jetbot for it to push
31        visual_material = PreviewSurfaceMaterial("/World/Materials/red")
32        visual_material.set_input_values("diffuseColor", [1.0, 0.0, 0.0])
33        cube_shape = Cube(
34            paths="/World/Cube",
35            positions=np.array([[0.15, 0.0, 0.025]]),  # In front of Jetbot
36            sizes=[1.0],
37            scales=np.array([[0.05, 0.05, 0.05]]),
38            reset_xform_op_properties=True,
39        )
40        GeomPrim(paths=cube_shape.paths, apply_collision_apis=True)
41        RigidPrim(paths=cube_shape.paths)
42        cube_shape.apply_visual_materials(visual_material)
43
44        # Add Franka manipulator at a position the Jetbot will push the cube to
45        stage_utils.add_reference_to_stage(
46            usd_path=assets_root_path + "/Isaac/Robots/FrankaRobotics/FrankaPanda/franka.usd",
47            path="/World/Franka",
48        )
49
50        # Position Franka so the cube will be pushed into its workspace
51        franka_xform = XformPrim("/World/Franka")
52        franka_xform.set_world_poses(positions=np.array([[0.8, -0.5, 0.0]]))
53
54    # -- End of setup_scene -- #
55
56    async def setup_post_load(self):
57        # Create Articulation handles for both robots
58        self._jetbot = Articulation("/World/Jetbot")
59        self._franka = Articulation("/World/Franka")
60
61        # Print robot info
62        print(f"Jetbot DOFs: {self._jetbot.num_dofs}, names: {self._jetbot.dof_names}")
63        print(f"Franka DOFs: {self._franka.num_dofs}, names: {self._franka.dof_names}")
```

Click the **LOAD** button to see both robots and the cube in the scene.

## Controlling Multiple Robots

Now add physics callbacks to control both robots simultaneously. The Jetbot will push the cube
forward while the Franka prepares to receive it.

```python
1        self._step_counter += 1
2        if self._step_counter < 300:
3            # Drive Jetbot forward to push the cube
4            self._jetbot.set_dof_velocity_targets([[10.0, 10.0]])
5        else:
6            # Stop the Jetbot after pushing
7            self._jetbot.set_dof_velocity_targets([[0.0, 0.0]])
```

Complete code:

```python
 1import isaacsim.core.experimental.utils.stage as stage_utils
 2import numpy as np
 3from isaacsim.core.experimental.materials import PreviewSurfaceMaterial
 4from isaacsim.core.experimental.objects import Cube
 5from isaacsim.core.experimental.prims import Articulation, GeomPrim, RigidPrim, XformPrim
 6from isaacsim.core.simulation_manager import SimulationManager
 7from isaacsim.examples.base.base_sample_experimental import BaseSample
 8from isaacsim.storage.native import get_assets_root_path
 9
10
11class HelloWorld(BaseSample):
12    def __init__(self) -> None:
13        super().__init__()
14        self._physics_callback_id = None
15        self._step_counter = 0
16
17    def setup_scene(self):
18        assets_root_path = get_assets_root_path()
19
20        # Add ground plane
21        stage_utils.add_reference_to_stage(
22            usd_path=assets_root_path + "/Isaac/Environments/Grid/default_environment.usd",
23            path="/World/ground",
24        )
25
26        # Add Jetbot mobile robot
27        stage_utils.add_reference_to_stage(
28            usd_path=assets_root_path + "/Isaac/Robots/NVIDIA/Jetbot/jetbot.usd",
29            path="/World/Jetbot",
30        )
31
32        # Add a cube in front of Jetbot for it to push
33        visual_material = PreviewSurfaceMaterial("/World/Materials/red")
34        visual_material.set_input_values("diffuseColor", [1.0, 0.0, 0.0])
35        cube_shape = Cube(
36            paths="/World/Cube",
37            positions=np.array([[0.15, 0.0, 0.025]]),
38            sizes=[1.0],
39            scales=np.array([[0.05, 0.05, 0.05]]),
40            reset_xform_op_properties=True,
41        )
42        GeomPrim(paths=cube_shape.paths, apply_collision_apis=True)
43        RigidPrim(paths=cube_shape.paths)
44        cube_shape.apply_visual_materials(visual_material)
45
46        # Add Franka manipulator
47        stage_utils.add_reference_to_stage(
48            usd_path=assets_root_path + "/Isaac/Robots/FrankaRobotics/FrankaPanda/franka.usd",
49            path="/World/Franka",
50        )
51
52        # Position Franka forward and to the right of Jetbot's path
53        franka_xform = XformPrim("/World/Franka")
54        franka_xform.set_world_poses(positions=np.array([[0.8, -0.5, 0.0]]))
55
56    async def setup_post_load(self):
57        # Create Articulation handles
58        self._jetbot = Articulation("/World/Jetbot")
59        self._franka = Articulation("/World/Franka")
60        self._cube = RigidPrim("/World/Cube")
61        self._step_counter = 0
62
63        # Register physics callback
64        from isaacsim.core.simulation_manager.impl.isaac_events import IsaacEvents
65
66        self._physics_callback_id = SimulationManager.register_callback(
67            self.physics_step, IsaacEvents.POST_PHYSICS_STEP
68        )
69
70    def physics_step(self, dt, context):
71        # -- Begin control Jetbot -- #
72        self._step_counter += 1
73        if self._step_counter < 300:
74            # Drive Jetbot forward to push the cube
75            self._jetbot.set_dof_velocity_targets([[10.0, 10.0]])
76        else:
77            # Stop the Jetbot after pushing
78            self._jetbot.set_dof_velocity_targets([[0.0, 0.0]])
79        # -- End of control Jetbot -- #
80
81    def physics_cleanup(self):
82        if self._physics_callback_id is not None:
83            SimulationManager.deregister_callback(self._physics_callback_id)
84            self._physics_callback_id = None
```

Watch as the Jetbot pushes the cube towards the Franka!

## Adding State Machine Logic

Create a state machine to coordinate the robots: first the Jetbot pushes the cube towards Franka,
then backs up to give space, and finally Franka executes a full pick-and-place sequence using
the `Franka` class for IK-based end-effector control:

```python
 1        if self._state == 0:
 2            # Jetbot pushes cube to Franka
 3            cube_pos = self._cube.get_world_poses()[0].numpy()[0]
 4            if np.linalg.norm(cube_pos[:2] - self._cube_goal[:2]) > 0.05:
 5                self._jetbot.set_dof_velocity_targets([[10.0, 10.0]])
 6            else:
 7                self._jetbot.set_dof_velocity_targets([[0.0, 0.0]])
 8                print("Cube delivered! Backing up...")
 9                self._state = 1
10                self._step_counter = 0
11
12        elif self._state == 1:
13            # Jetbot backs up
14            self._jetbot.set_dof_velocity_targets([[-8.0, -8.0]])
15            self._step_counter += 1
16            if self._step_counter > 100:
17                self._jetbot.set_dof_velocity_targets(np.array([[0.0, 0.0]]))
18                print("Franka starting pick-and-place...")
19                self._state = 2
20                self._step_counter = 0
21                self._franka.open_gripper()
22
23        elif self._state == 2:
24            # Franka pick-and-place sequence using step counter
25            cube_pos = self._cube.get_world_poses()[0].numpy()[0]
26            down_orient = self._franka.get_downward_orientation()
27            self._step_counter += 1
28
29            if self._pick_phase == 0:
30                # Move above cube (wait 120 steps)
31                self._franka.set_end_effector_pose(
32                    np.array([[cube_pos[0], cube_pos[1], cube_pos[2] + 0.2]]), down_orient
33                )
34                if self._step_counter > 120:
35                    self._pick_phase = 1
36                    self._step_counter = 0
37            elif self._pick_phase == 1:
38                # Lower to cube (wait 100 steps)
39                self._franka.set_end_effector_pose(
40                    np.array([[cube_pos[0], cube_pos[1], cube_pos[2] + 0.1]]), down_orient
41                )
42                if self._step_counter > 100:
43                    self._franka.close_gripper()
44                    self._pick_phase = 2
45                    self._step_counter = 0
46            elif self._pick_phase == 2:
47                # Close the gripper (wait 50 steps)
48                self._franka.close_gripper()
49                if self._step_counter > 50:
50                    self._pick_phase = 3
51                    self._step_counter = 0
52            elif self._pick_phase == 3:
53                # Lift cube (wait 100 steps)
54                self._franka.set_end_effector_pose(
55                    np.array([[cube_pos[0], cube_pos[1], cube_pos[2] + 0.25]]), down_orient
56                )
57                if self._step_counter > 100:
58                    self._pick_phase = 4
59                    self._step_counter = 0
60            elif self._pick_phase == 4:
61                # Move to target (wait 150 steps)
62                self._franka.set_end_effector_pose(np.array([[0.3, 0.3, 0.15]]), down_orient)
63                if self._step_counter > 150:
64                    self._franka.open_gripper()
65                    self._pick_phase = 5
66                    self._step_counter = 0
67            elif self._pick_phase == 5:
68                # Lift the arm (wait 150 steps)
69                self._franka.set_end_effector_pose(
70                    np.array([[cube_pos[0], cube_pos[1], cube_pos[2] + 0.5]]), down_orient
71                )
72                if self._step_counter > 150:
73                    self._step_counter = 0
```

Complete code:

```python
  1import isaacsim.core.experimental.utils.stage as stage_utils
  2import numpy as np
  3from isaacsim.core.experimental.materials import PreviewSurfaceMaterial
  4from isaacsim.core.experimental.objects import Cube
  5from isaacsim.core.experimental.prims import Articulation, GeomPrim, RigidPrim, XformPrim
  6from isaacsim.core.simulation_manager import SimulationManager
  7from isaacsim.examples.base.base_sample_experimental import BaseSample
  8from isaacsim.robot.experimental.manipulators.examples.franka import Franka
  9from isaacsim.storage.native import get_assets_root_path
 10
 11
 12class HelloWorld(BaseSample):
 13    def __init__(self) -> None:
 14        super().__init__()
 15        self._physics_callback_id = None
 16        self._state = 0
 17
 18    def setup_scene(self):
 19        assets_root_path = get_assets_root_path()
 20
 21        # Add ground plane
 22        stage_utils.add_reference_to_stage(
 23            usd_path=assets_root_path + "/Isaac/Environments/Grid/default_environment.usd",
 24            path="/World/ground",
 25        )
 26
 27        # Add Jetbot at origin
 28        stage_utils.add_reference_to_stage(
 29            usd_path=assets_root_path + "/Isaac/Robots/NVIDIA/Jetbot/jetbot.usd",
 30            path="/World/Jetbot",
 31        )
 32
 33        # Add cube in front of Jetbot
 34        visual_material = PreviewSurfaceMaterial("/World/Materials/blue")
 35        visual_material.set_input_values("diffuseColor", [0.0, 0.0, 1.0])
 36        cube_shape = Cube(
 37            paths="/World/Cube",
 38            positions=np.array([[0.15, 0.0, 0.0258]]),
 39            sizes=[1.0],
 40            scales=np.array([[0.05, 0.05, 0.05]]),
 41            reset_xform_op_properties=True,
 42        )
 43        GeomPrim(paths=cube_shape.paths, apply_collision_apis=True)
 44        RigidPrim(paths=cube_shape.paths)
 45        cube_shape.apply_visual_materials(visual_material)
 46
 47        # Add Franka using Franka for IK and gripper control
 48        self._franka = Franka(robot_path="/World/Franka", create_robot=True)
 49        franka_xform = XformPrim("/World/Franka")
 50        franka_xform.set_world_poses(positions=[[0.8, -0.3, 0.0]])
 51
 52    async def setup_post_load(self):
 53        self._jetbot = Articulation("/World/Jetbot")
 54        self._cube = RigidPrim("/World/Cube")
 55        self._cube_goal = np.array([1.2, 0.0, 0.0])  # Target: Franka reaches from the side
 56        self._step_counter = 0
 57        self._pick_phase = 0
 58
 59        from isaacsim.core.simulation_manager.impl.isaac_events import IsaacEvents
 60
 61        self._physics_callback_id = SimulationManager.register_callback(
 62            self.physics_step, IsaacEvents.POST_PHYSICS_STEP
 63        )
 64        self._state = 0
 65
 66    def physics_step(self, dt, context):
 67        # -- Begin state machine -- #
 68        if self._state == 0:
 69            # Jetbot pushes cube to Franka
 70            cube_pos = self._cube.get_world_poses()[0].numpy()[0]
 71            if np.linalg.norm(cube_pos[:2] - self._cube_goal[:2]) > 0.05:
 72                self._jetbot.set_dof_velocity_targets([[10.0, 10.0]])
 73            else:
 74                self._jetbot.set_dof_velocity_targets([[0.0, 0.0]])
 75                print("Cube delivered! Backing up...")
 76                self._state = 1
 77                self._step_counter = 0
 78
 79        elif self._state == 1:
 80            # Jetbot backs up
 81            self._jetbot.set_dof_velocity_targets([[-8.0, -8.0]])
 82            self._step_counter += 1
 83            if self._step_counter > 100:
 84                self._jetbot.set_dof_velocity_targets(np.array([[0.0, 0.0]]))
 85                print("Franka starting pick-and-place...")
 86                self._state = 2
 87                self._step_counter = 0
 88                self._franka.open_gripper()
 89
 90        elif self._state == 2:
 91            # Franka pick-and-place sequence using step counter
 92            cube_pos = self._cube.get_world_poses()[0].numpy()[0]
 93            down_orient = self._franka.get_downward_orientation()
 94            self._step_counter += 1
 95
 96            if self._pick_phase == 0:
 97                # Move above cube (wait 120 steps)
 98                self._franka.set_end_effector_pose(
 99                    np.array([[cube_pos[0], cube_pos[1], cube_pos[2] + 0.2]]), down_orient
100                )
101                if self._step_counter > 120:
102                    self._pick_phase = 1
103                    self._step_counter = 0
104            elif self._pick_phase == 1:
105                # Lower to cube (wait 100 steps)
106                self._franka.set_end_effector_pose(
107                    np.array([[cube_pos[0], cube_pos[1], cube_pos[2] + 0.1]]), down_orient
108                )
109                if self._step_counter > 100:
110                    self._franka.close_gripper()
111                    self._pick_phase = 2
112                    self._step_counter = 0
113            elif self._pick_phase == 2:
114                # Close the gripper (wait 50 steps)
115                self._franka.close_gripper()
116                if self._step_counter > 50:
117                    self._pick_phase = 3
118                    self._step_counter = 0
119            elif self._pick_phase == 3:
120                # Lift cube (wait 100 steps)
121                self._franka.set_end_effector_pose(
122                    np.array([[cube_pos[0], cube_pos[1], cube_pos[2] + 0.25]]), down_orient
123                )
124                if self._step_counter > 100:
125                    self._pick_phase = 4
126                    self._step_counter = 0
127            elif self._pick_phase == 4:
128                # Move to target (wait 150 steps)
129                self._franka.set_end_effector_pose(np.array([[0.3, 0.3, 0.15]]), down_orient)
130                if self._step_counter > 150:
131                    self._franka.open_gripper()
132                    self._pick_phase = 5
133                    self._step_counter = 0
134            elif self._pick_phase == 5:
135                # Lift the arm (wait 150 steps)
136                self._franka.set_end_effector_pose(
137                    np.array([[cube_pos[0], cube_pos[1], cube_pos[2] + 0.5]]), down_orient
138                )
139                if self._step_counter > 150:
140                    self._step_counter = 0
141        # -- End of state machine -- #
142
143    async def setup_post_reset(self):
144        self._state = 0
145        self._step_counter = 0
146        self._pick_phase = 0
147        self._franka.reset_to_default_pose()
148
149    def physics_cleanup(self):
150        if self._physics_callback_id is not None:
151            SimulationManager.deregister_callback(self._physics_callback_id)
152            self._physics_callback_id = None
```

## Summary

This tutorial covered the following topics:

1. Adding multiple robots and objects (cube) to the scene
2. Using `Cube`, `GeomPrim`, and `RigidPrim` to create pushable objects
3. Using the `Articulation` class to control different robot types
4. Having a mobile robot (Jetbot) push objects towards a manipulator (Franka)
5. Building state machine logic to coordinate pushing, backing up, and picking
6. Using `Franka` for IK-based end-effector control and gripper operations

### Next Steps

Continue on to the next tutorial in our Essential Tutorials series, [Multiple Robot Scenarios](tutorial_core_multiple_tasks.html#isaac-sim-app-tutorial-core-multiple-tasks),
to learn how to add multiple tasks and manage them.

On this page

* [Learning Objectives](#learning-objectives)
* [Getting Started](#getting-started)
* [Creating the Scene](#creating-the-scene)
* [Controlling Multiple Robots](#controlling-multiple-robots)
* [Adding State Machine Logic](#adding-state-machine-logic)
* [Summary](#summary)
  + [Next Steps](#next-steps)

---

### Multiple Tasks

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/core_api_tutorials/tutorial_core_multiple_tasks.html

* [Python Scripting and Tutorials](../python_scripting/index.html)
* [Core API Tutorial Series](index.html)
* Multiple Robot Scenarios

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Multiple Robot Scenarios

## Learning Objectives

This tutorial describes how to create and manage multiple robot scenarios in NVIDIA Isaac Sim.
It explains how to use parameterization and Python classes to scale your simulations with
multiple instances of robots performing similar tasks. After this tutorial, you will have
more experience building scalable multi-robot simulations in NVIDIA Isaac Sim.

*15-20 Minute Tutorial*

## Getting Started

**Prerequisites**

* Review [Adding Multiple Robots](tutorial_core_adding_multiple_robots.html#isaac-sim-app-tutorial-core-adding-multiple-robots) prior to beginning this tutorial.

Begin with the source code open from the previous tutorial, [Adding Multiple Robots](tutorial_core_adding_multiple_robots.html#isaac-sim-app-tutorial-core-adding-multiple-robots).

Note

Pressing **STOP**, then **PLAY** in this workflow might not reset the world properly. Use
the **RESET** button instead.

## Organizing Robot Scenarios with Classes

When working with multiple robots performing similar tasks, itâs helpful to encapsulate the
robot setup and control logic into reusable classes. This approach allows you to easily
create multiple instances with different parameters (like position offsets).

Create a `RobotScenario` class that manages a Jetbot pushing a cube to a Franka:

```python
  1import isaacsim.core.experimental.utils.stage as stage_utils
  2import numpy as np
  3from isaacsim.core.experimental.objects import Cube, DomeLight, GroundPlane
  4from isaacsim.core.experimental.prims import Articulation, GeomPrim, RigidPrim, XformPrim
  5from isaacsim.core.simulation_manager import SimulationEvent, SimulationManager
  6from isaacsim.examples.base.base_sample_experimental import BaseSample
  7from isaacsim.robot.experimental.manipulators.examples.franka import Franka
  8from isaacsim.storage.native import get_assets_root_path
  9
 10
 11class RobotScenario:
 12    """Encapsulates a Jetbot + Franka + Cube scenario with an offset."""
 13
 14    def __init__(self, name: str, offset: np.ndarray = np.array([0.0, 0.0, 0.0])):
 15        self.name = name
 16        self.offset = offset
 17        self.state = 0
 18        self.step_counter = 0
 19        self.pick_phase = 0
 20        self.jetbot = None
 21        self.franka = None
 22        self.cube = None
 23        self.cube_goal = np.array([1.2, 0.0, 0.0]) + offset
 24
 25    def setup_scene(self):
 26        """Create the robots and cube for this scenario."""
 27        assets_root_path = get_assets_root_path()
 28        base_path = f"/World/{self.name}"
 29
 30        # Add Jetbot
 31        stage_utils.add_reference_to_stage(
 32            usd_path=assets_root_path + "/Isaac/Robots/NVIDIA/Jetbot/jetbot.usd",
 33            path=f"{base_path}/Jetbot",
 34        )
 35        jetbot_xform = XformPrim(f"{base_path}/Jetbot")
 36        jetbot_xform.reset_xform_op_properties()
 37        jetbot_xform.set_world_poses(positions=self.offset.tolist())
 38
 39        # Add cube in front of Jetbot
 40        cube_pos = self.offset + np.array([0.15, 0.0, 0.025])
 41        cube_shape = Cube(
 42            paths=f"{base_path}/Cube",
 43            positions=cube_pos.tolist(),
 44            sizes=1.0,
 45            scales=[0.05, 0.05, 0.05],
 46            colors="red",
 47        )
 48        GeomPrim(paths=cube_shape.paths, apply_collision_apis=True)
 49        RigidPrim(paths=cube_shape.paths)
 50
 51        # Add Franka
 52        franka_pos = self.offset + np.array([0.8, -0.3, 0.0])
 53        self.franka = Franka(robot_path=f"{base_path}/Franka", create_robot=True)
 54        franka_xform = XformPrim(f"{base_path}/Franka")
 55        franka_xform.reset_xform_op_properties()
 56        franka_xform.set_world_poses(positions=franka_pos.tolist())
 57
 58    def initialize(self):
 59        """Initialize articulation handles after scene load."""
 60        base_path = f"/World/{self.name}"
 61        self.jetbot = Articulation(f"{base_path}/Jetbot")
 62        self.cube = RigidPrim(f"{base_path}/Cube")
 63
 64    def reset(self):
 65        """Reset the scenario state."""
 66        self.state = 0
 67        self.step_counter = 0
 68        self.pick_phase = 0
 69        self.franka.reset_to_default_pose()
 70
 71    def step(self):
 72        """Execute one step of the scenario logic."""
 73        if self.state == 0:
 74            # Jetbot pushes cube
 75            cube_pos = self.cube.get_world_poses()[0].numpy()[0]
 76            if np.linalg.norm(cube_pos[:2] - self.cube_goal[:2]) > 0.05:
 77                self.jetbot.set_dof_velocity_targets([10.0, 10.0])
 78            else:
 79                self.jetbot.set_dof_velocity_targets([0.0, 0.0])
 80                self.state = 1
 81                self.step_counter = 0
 82
 83        elif self.state == 1:
 84            # Jetbot backs up
 85            self.jetbot.set_dof_velocity_targets([-8.0, -8.0])
 86            self.step_counter += 1
 87            if self.step_counter > 100:
 88                self.jetbot.set_dof_velocity_targets([0.0, 0.0])
 89                self.state = 2
 90                self.step_counter = 0
 91                self.franka.open_gripper()
 92
 93        elif self.state == 2:
 94            # Franka pick-and-place
 95            self._franka_pick_place()
 96
 97    def _franka_pick_place(self):
 98        """Execute Franka pick-and-place state machine."""
 99        cube_pos = self.cube.get_world_poses()[0].numpy()[0]
100        down_orient = self.franka.get_downward_orientation()
101        self.step_counter += 1
102
103        if self.pick_phase == 0:
104            self.franka.set_end_effector_pose(np.array([cube_pos[0], cube_pos[1], cube_pos[2] + 0.2]), down_orient)
105            if self.step_counter > 120:
106                self.pick_phase = 1
107                self.step_counter = 0
108        elif self.pick_phase == 1:
109            self.franka.set_end_effector_pose(np.array([cube_pos[0], cube_pos[1], cube_pos[2] + 0.1]), down_orient)
110            if self.step_counter > 100:
111                self.pick_phase = 2
112                self.step_counter = 0
113        elif self.pick_phase == 2:
114            self.franka.close_gripper()
115            if self.step_counter > 100:
116                self.pick_phase = 3
117                self.step_counter = 0
118        elif self.pick_phase == 3:
119            _, current_position, _ = self.franka.get_current_state()
120            target = current_position + np.array([0.1, 0.0, 0.08])
121            self.franka.set_end_effector_pose(position=target, orientation=down_orient)
122            if self.step_counter > 150:
123                self.step_counter = 0
124                self.pick_phase = 4
125        elif self.pick_phase == 4:
126            _, current_position, _ = self.franka.get_current_state()
127            target = current_position + np.array([0.1, 0.0, 0.01])
128            self.franka.set_end_effector_pose(position=target, orientation=down_orient)
129            if self.step_counter > 150:
130                self.step_counter = 0
131                self.pick_phase = 5
132        elif self.pick_phase == 5:
133            self.franka.open_gripper()
134            if self.step_counter > 150:
135                self.step_counter = 0
136                self.state = 6  # Done
137
138
139class HelloWorld(BaseSample):
140    def __init__(self) -> None:
141        super().__init__()
142        self._physics_callback_id = None
143        self._scenarios = []
144
145    def setup_scene(self):
146        GroundPlane("/World/ground_plane")
147        dome_light = DomeLight("/World/DomeLight")
148        dome_light.set_intensities(1000)
149
150        # Create a single scenario
151        self._scenario = RobotScenario(name="scenario_0", offset=np.array([0.0, 0.0, 0.0]))
152        self._scenario.setup_scene()
153
154    async def setup_post_load(self):
155        self._scenario.initialize()
156
157        self._physics_callback_id = SimulationManager.register_callback(
158            self.physics_step, event=SimulationEvent.PHYSICS_POST_STEP
159        )
160
161    def physics_step(self, dt, context):
162        self._scenario.step()
163
164    async def setup_post_reset(self):
165        self._scenario.reset()
166
167    def physics_cleanup(self):
168        if self._physics_callback_id is not None:
169            SimulationManager.deregister_callback(self._physics_callback_id)
170            self._physics_callback_id = None
```

## Scaling to Multiple Scenarios

Adding the following operations:

Set number of scenarios:

```python
1        self._num_scenarios = 3  # Number of parallel scenarios
```

Creating scenarios:

```python
1        # Create multiple scenarios with Y-axis offsets
2        for i in range(self._num_scenarios):
3            offset = np.array([0.0, (i - 1) * 2.0, 0.0])  # Spread along Y-axis
4            scenario = RobotScenario(name=f"scenario_{i}", offset=offset, randomize=False)
5            scenario.setup_scene()
6            self._scenarios.append(scenario)
```

Initializing scenarios:

```python
1        # Initialize all scenarios
2        for scenario in self._scenarios:
3            scenario.initialize()
```

Stepping all scenarios:

```python
1        # Step all scenarios
2        for scenario in self._scenarios:
3            scenario.step()
```

Resetting all scenarios:

```python
1        # Reset all scenarios
2        for scenario in self._scenarios:
3            scenario.reset()
```

Clean up:

```python
1        self._scenarios = []
```

Complete code:

```python
  1import isaacsim.core.experimental.utils.stage as stage_utils
  2import numpy as np
  3from isaacsim.core.experimental.objects import Cube, DomeLight, GroundPlane
  4from isaacsim.core.experimental.prims import Articulation, GeomPrim, RigidPrim, XformPrim
  5from isaacsim.core.simulation_manager import SimulationEvent, SimulationManager
  6from isaacsim.examples.base.base_sample_experimental import BaseSample
  7from isaacsim.robot.experimental.manipulators.examples.franka import Franka
  8from isaacsim.storage.native import get_assets_root_path
  9
 10
 11class RobotScenario:
 12    """Encapsulates a Jetbot + Franka + Cube scenario with an offset."""
 13
 14    def __init__(self, name: str, offset: np.ndarray = np.array([0.0, 0.0, 0.0]), randomize: bool = False):
 15        self.name = name
 16        self.offset = offset
 17        self.state = 0
 18        self.step_counter = 0
 19        self.randomize = randomize
 20        self.pick_phase = 0
 21        self.jetbot = None
 22        self.franka = None
 23        self.cube = None
 24        self.cube_goal = np.array([1.2, 0.0, 0.0]) + offset
 25
 26        # Randomize cube goal position if enabled
 27        if self.randomize:
 28            random_x = np.random.uniform(1.0, 1.6)
 29            self.cube_goal = np.array([random_x, 0.0, 0.0]) + offset
 30        else:
 31            self.cube_goal = np.array([1.2, 0.0, 0.0]) + offset
 32
 33    def setup_scene(self):
 34        """Create the robots and cube for this scenario."""
 35        assets_root_path = get_assets_root_path()
 36        base_path = f"/World/{self.name}"
 37
 38        # Add Jetbot
 39        stage_utils.add_reference_to_stage(
 40            usd_path=assets_root_path + "/Isaac/Robots/NVIDIA/Jetbot/jetbot.usd",
 41            path=f"{base_path}/Jetbot",
 42        )
 43        jetbot_xform = XformPrim(f"{base_path}/Jetbot")
 44        jetbot_xform.reset_xform_op_properties()
 45        jetbot_xform.set_world_poses(positions=self.offset.tolist())
 46
 47        # Add cube in front of Jetbot
 48        cube_pos = self.offset + np.array([0.15, 0.0, 0.025])
 49        cube_shape = Cube(
 50            paths=f"{base_path}/Cube",
 51            positions=cube_pos.tolist(),
 52            sizes=1.0,
 53            scales=[0.05, 0.05, 0.05],
 54            colors="red",
 55        )
 56        GeomPrim(paths=cube_shape.paths, apply_collision_apis=True)
 57        RigidPrim(paths=cube_shape.paths)
 58
 59        # Add Franka
 60        franka_pos = self.offset + np.array([0.8, -0.3, 0.0])
 61        self.franka = Franka(robot_path=f"{base_path}/Franka", create_robot=True)
 62        franka_xform = XformPrim(f"{base_path}/Franka")
 63        franka_xform.reset_xform_op_properties()
 64        franka_xform.set_world_poses(positions=franka_pos.tolist())
 65
 66    def initialize(self):
 67        """Initialize articulation handles after scene load."""
 68        base_path = f"/World/{self.name}"
 69        self.jetbot = Articulation(f"{base_path}/Jetbot")
 70        self.cube = RigidPrim(f"{base_path}/Cube")
 71
 72    def reset(self):
 73        """Reset the scenario state."""
 74        self.state = 0
 75        self.step_counter = 0
 76        self.pick_phase = 0
 77        self.franka.reset_to_default_pose()
 78
 79    def step(self):
 80        """Execute one step of the scenario logic."""
 81        if self.state == 0:
 82            # Jetbot pushes cube
 83            cube_pos = self.cube.get_world_poses()[0].numpy()[0]
 84            if np.linalg.norm(cube_pos[:2] - self.cube_goal[:2]) > 0.05:
 85                self.jetbot.set_dof_velocity_targets([10.0, 10.0])
 86            else:
 87                self.jetbot.set_dof_velocity_targets([0.0, 0.0])
 88                self.state = 1
 89                self.step_counter = 0
 90
 91        elif self.state == 1:
 92            # Jetbot backs up
 93            self.jetbot.set_dof_velocity_targets([-8.0, -8.0])
 94            self.step_counter += 1
 95            if self.step_counter > 100:
 96                self.jetbot.set_dof_velocity_targets([0.0, 0.0])
 97                self.state = 2
 98                self.step_counter = 0
 99                self.franka.open_gripper()
100
101        elif self.state == 2:
102            # Franka pick-and-place
103            self._franka_pick_place()
104
105    def _franka_pick_place(self):
106        """Execute Franka pick-and-place state machine."""
107        cube_pos = self.cube.get_world_poses()[0].numpy()[0]
108        down_orient = self.franka.get_downward_orientation()
109        self.step_counter += 1
110
111        if self.pick_phase == 0:
112            self.franka.set_end_effector_pose(np.array([cube_pos[0], cube_pos[1], cube_pos[2] + 0.2]), down_orient)
113            if self.step_counter > 120:
114                self.pick_phase = 1
115                self.step_counter = 0
116        elif self.pick_phase == 1:
117            self.franka.set_end_effector_pose(np.array([cube_pos[0], cube_pos[1], cube_pos[2] + 0.1]), down_orient)
118            if self.step_counter > 100:
119                self.pick_phase = 2
120                self.step_counter = 0
121        elif self.pick_phase == 2:
122            self.franka.close_gripper()
123            if self.step_counter > 100:
124                self.pick_phase = 3
125                self.step_counter = 0
126        elif self.pick_phase == 3:
127            _, current_position, _ = self.franka.get_current_state()
128            target = current_position + np.array([0.1, 0.0, 0.08])
129            self.franka.set_end_effector_pose(position=target, orientation=down_orient)
130            if self.step_counter > 150:
131                self.step_counter = 0
132                self.pick_phase = 4
133        elif self.pick_phase == 4:
134            _, current_position, _ = self.franka.get_current_state()
135            target = current_position + np.array([0.1, 0.0, 0.01])
136            self.franka.set_end_effector_pose(position=target, orientation=down_orient)
137            if self.step_counter > 150:
138                self.step_counter = 0
139                self.pick_phase = 5
140        elif self.pick_phase == 5:
141            self.franka.open_gripper()
142            if self.step_counter > 150:
143                self.step_counter = 0
144                self.state = 6  # Done
145
146
147class HelloWorld(BaseSample):
148    def __init__(self) -> None:
149        super().__init__()
150        self._physics_callback_id = None
151        self._scenarios = []
152        # -- Begin setting scenario number -- #
153        self._num_scenarios = 3  # Number of parallel scenarios
154        # -- End of setting scenario number -- #
155
156    def setup_scene(self):
157        GroundPlane("/World/ground_plane")
158        dome_light = DomeLight("/World/DomeLight")
159        dome_light.set_intensities(1000)
160
161        # -- Begin creating scenarios -- #
162        # Create multiple scenarios with Y-axis offsets
163        for i in range(self._num_scenarios):
164            offset = np.array([0.0, (i - 1) * 2.0, 0.0])  # Spread along Y-axis
165            scenario = RobotScenario(name=f"scenario_{i}", offset=offset, randomize=False)
166            scenario.setup_scene()
167            self._scenarios.append(scenario)
168        # -- End of creating scenarios -- #
169
170    async def setup_post_load(self):
171        # -- Begin initializing scenarios -- #
172        # Initialize all scenarios
173        for scenario in self._scenarios:
174            scenario.initialize()
175        # -- End of initializing scenarios -- #
176
177        self._physics_callback_id = SimulationManager.register_callback(
178            self.physics_step, event=SimulationEvent.PHYSICS_POST_STEP
179        )
180
181    def physics_step(self, dt, context):
182        # -- Begin stepping scenarios -- #
183        # Step all scenarios
184        for scenario in self._scenarios:
185            scenario.step()
186        # -- End of stepping scenarios -- #
187
188    async def setup_post_reset(self):
189        # -- Begin resetting scenarios -- #
190        # Reset all scenarios
191        for scenario in self._scenarios:
192            scenario.reset()
193        # -- End of resetting scenarios -- #
194
195    def physics_cleanup(self):
196        if self._physics_callback_id is not None:
197            SimulationManager.deregister_callback(self._physics_callback_id)
198            self._physics_callback_id = None
199        # -- Begin remove all scenarios -- #
200        self._scenarios = []
201        # -- End of remove all scenarios -- #
```

## Adding Randomization

To make simulations more interesting, you can add randomization to the scenario parameters.
In the `setup_scene` method above, set `randomize=True` when creating each scenario:

```python
1for i in range(self._num_scenarios):
2    offset = np.array([0.0, (i - 1) * 2.0, 0.0])  # Spread along Y-axis
3    scenario = RobotScenario(name=f"scenario_{i}", offset=offset, randomize=True)
4    scenario.setup_scene()
5    self._scenarios.append(scenario)
```

## Best Practices for Scaling

When creating large-scale multi-robot simulations:

1. **Use unique paths**: Each scenario should use unique USD prim paths to avoid conflicts.
   The `RobotScenario` class uses the scenario name to create unique paths like
   `/World/scenario_0/Jetbot`.
2. **Manage state independently**: Each scenario instance maintains its own state variables,
   allowing scenarios to progress independently.
3. **Clean up properly**: The `physics_cleanup` method ensures callbacks are deregistered
   and scenario lists are cleared when the simulation is stopped.
4. **Consider performance**: With many scenarios, consider reducing physics step frequency
   or using GPU-accelerated simulation for better performance.

## Summary

This tutorial covered the following topics:

1. Organizing robot scenarios into reusable Python classes
2. Using the `offset` parameter to position multiple scenarios in the world
3. Scaling to multiple parallel scenarios with a simple loop
4. Adding randomization to scenario parameters
5. Best practices for managing multiple robot instances

On this page

* [Learning Objectives](#learning-objectives)
* [Getting Started](#getting-started)
* [Organizing Robot Scenarios with Classes](#organizing-robot-scenarios-with-classes)
* [Scaling to Multiple Scenarios](#scaling-to-multiple-scenarios)
* [Adding Randomization](#adding-randomization)
* [Best Practices for Scaling](#best-practices-for-scaling)
* [Summary](#summary)

---

### Adding Props

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/core_api_tutorials/tutorial_core_adding_props.html

* [Python Scripting and Tutorials](../python_scripting/index.html)
* [Core API Tutorial Series](index.html)
* Adding Props

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Adding Props

## Learning Objectives

This tutorial shows how to add objects to the scene and configure them for simulation.

*10-15 Minute Tutorial*

## Adding Rubikâs Cube

Start by adding a Rubikâs Cube to the scene.

1. Create a new stage on Isaac Sim by clicking on the **File** tab and then clicking on **New Stage**.
2. In the Content Browser, go to `Isaac Sim` > `Props` > `Rubiks_Cube` > `rubiks_cube.usd` and drag and drop the `rubiks_cube.usd` file into the stage. This will add a Rubikâs Cube to the scene as a payload.
3. Left click on the Rubikâs Cube and in the properties panel, set the `Position` to `(0, 0, 0.1)`.
4. On the stage, right click `Create` > `Isaac` > `Environment` > `Flat Grid` to create a flat ground.
5. Click `PLAY` to start the simulation, you will see the Rubikâs Cube is not falling to the ground. This is because the Rubikâs Cube is not a rigid body.
6. Click `STOP` to stop the simulation.

## Configure Physics Properties

### Add Rigid Body Properties

1. Right click on the Rubikâs Cube and select `Add` > `Physics` > `Rigid Body`. This will add a rigid body attribute to the Rubikâs Cube and it will be affected by physics.
2. Now, click `PLAY` to start the simulation, you will see the Rubikâs Cube fall through the ground, this is because the Rubikâs Cube does not have a collision shape. Click `STOP` to stop the simulation.

### Add Collision Properties

1. Right click on the Rubikâs Cube and select `Add` > `Physics` > `Collider Presets`. This will add a collision attribute to the Rubikâs Cube and it will collide with other objects.
2. Now, click `PLAY` to start the simulation, you will see the Rubikâs Cube fall on the ground. Click `STOP` to stop the simulation.

### Add Mass

In addition to collision, you can also add mass, inertia, and center of mass to the Rubikâs Cube to configure its physical properties.

1. Right click on the Rubikâs Cube and select `Add` > `Physics` > `Mass`. This will add a mass attribute to the Rubikâs Cube.
2. In the properties panel, scroll down to the `Mass` section and set the `Mass` to `0.1` to make it weigh 100 grams.

Note

In addition to mass, you can also set the `Density`, `Center of Mass`, `Diagonal Inertia`, and `Principal Axes` of the object.

Setting the mass to 0 will make the simulation to compute it at runtime based on its volume (assuming 1000 kg/m^3 if density is not specified).

### Visualize Collision Shapes

Right click on the `Eye` on the top left of the viewport and select `Show By Type` > `Physics` > `Coliders` > `All`. This will show the collision shapes everything in the scene.

The ground planeâs collider is pink to denote it is a static object. The Rubikâs Cube is a dynamic object, so it falls to the ground and its collider is green.

Note

You can adjust the collider type by left clicking on the `RubikCube` mesh at `World/rubiks_cube/RubikCube` and scroll down to the `Physics/Collider` section, and select a different approximate type in the `Approximation` tab.

### Customize Collider

Letâs customize the collider for the Rubikâs Cube, by making it a sphere and easier to roll

1. Left click on the `RubikCube` mesh at `World/rubiks_cube/RubikCube` and scroll down to the `Physics/Collider` section, press the `x` on the right to delete the current collider.
2. Left click on the `rubiks_cube` Xform and select `Create` > `Shape` > `Sphere`. This will add a sphere shape around the Rubikâs Cube.
3. Scroll down to the `Geometry` section and set the `Radius` to `0.07` to make the sphere smaller to match the Rubikâs Cube.
4. Add a Collider to the sphere by selecting `Add` > `Physics` > `Collider Presets`.
5. Hide the Sphere by unckecking the eye icon to the right of the sphere on the stage.
6. Slant the groundplane by going to `FlatGrid` and Click on `Toggle Offset Mode` icon on the right of `Transform` in the Properties panel, then setting the `Rotation` to `(10, 0, 0)` to give it a 10 degree slope.
7. Click `PLAY` to start the simulation, you will see the Rubikâs Cube rolls on the ground. Click `STOP` to stop the simulation.

### Add Physics Materials

You can also apply surface properties to the Rubikâs Cube by adding a physics material.

1. Left click on the Rubikâs Cube and in the properties panel, set the `Position` to `(0, 0, 1)` to move it up.
2. Right click on the Rubikâs Cube and select `Create` > `Physics` > `Physics Material`. Check `Rigid Body Material`. This will add a physics material attribute to the Rubikâs Cube. Drag it to the `World/rubiks_cube/Looks` scope.
3. In the properties panel, scroll down to the `Physics Material` section and set the `Restitution` to `1` to make it bounce.
4. Select the `Sphere` collider we created earlier and in the properties panel, scroll down to the `Physics/Physics material on selected Material` section and select the `Physics Material` we just created at `/World/rubiks_cube/Looks/PhysicsMaterial`.
5. Click `PLAY` to start the simulation, you will see the Rubikâs Cube rolls on the ground and bounces. Click `STOP` to stop the simulation.

Note

You can also set the `Static Friction` and `Dynamic Friction` as well.

Note

The completed asset is available at `Isaac Sim` > `Samples` > `Rigging` > `RubiksCube` > `rubiks_cube.usd` in the Content Browser.

### Tips

* Object rigid body api should be applied to the default prim of the object.
* collision API should be applied to the mesh prim of the object, and it should be applied as a **physXSchema**

### Whatâs Next?

Extending from the concepts above, you assemble more complex collision shapes using basic shapes. For example, in the image below, we approximated a bearing collider using cylinders and rectangles.

## Summary

This tutorial covered the following topics:

1. Adding objects to the scene.
2. Configuring object physics properties.
3. Customize object collision shapes.
4. Apply physics materials to objects.

On this page

* [Learning Objectives](#learning-objectives)
* [Adding Rubikâs Cube](#adding-rubik-s-cube)
* [Configure Physics Properties](#configure-physics-properties)
  + [Add Rigid Body Properties](#add-rigid-body-properties)
  + [Add Collision Properties](#add-collision-properties)
  + [Add Mass](#add-mass)
  + [Visualize Collision Shapes](#visualize-collision-shapes)
  + [Customize Collider](#customize-collider)
  + [Add Physics Materials](#add-physics-materials)
  + [Tips](#tips)
  + [Whatâs Next?](#what-s-next)
* [Summary](#summary)

---


## 开发工具

### VS Code

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/development_tools/vscode.html

* [Development Tools](index.html)
* Visual Studio Code (VS Code)

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Visual Studio Code (VS Code)

## Isaac Sim VS Code Edition

[Isaac Sim VS Code Edition](https://marketplace.visualstudio.com/items?itemName=NVIDIA.isaacsim-vscode-edition) is an extension for Visual Studio Code that provides development support for NVIDIA Omniverse in general and Isaac Sim in particular.

Key Features:

* Execute Python code, in the Python environment of a running application, locally or remotely from VS Code and show the output in the *Isaac Sim VS Code Edition* panel.
* Browse and insert snippets of code related to Isaac Sim, Omniverse Kit and Universal Scene Description (USD).
* Create templates for Omniverse/Isaac Sim extensions and other development approaches.
* Quick access to the most relevant Omniverse/Isaac Sim documentation sources and resources without leaving the editor.

**Install it now to get started**: [Isaac Sim VS Code Edition](https://marketplace.visualstudio.com/items?itemName=NVIDIA.isaacsim-vscode-edition)

---

## Interactive Scripting

The `isaacsim.code_editor.vscode` extension adds VS Code launcher and menu integration to Isaac Sim.
It depends on the `isaacsim.code_editor.python_server` extension which provides the TCP server for remote Python code execution (see [Python Server (Remote Code Execution)](python_server.html#isaac-sim-app-python-server) for full protocol details and usage examples).

Both extensions can be enabled or disabled using the [Extension Manager](https://docs.omniverse.nvidia.com/extensions/latest/ext_core/ext_extension-manager.html "(in Omniverse Extensions)") by searching for `isaacsim.code_editor.vscode`.
Enabling the VS Code extension automatically enables the Python server.

> Note
>
> This extension requires its Visual Studio Code pair extension: [Isaac Sim VS Code Edition](https://marketplace.visualstudio.com/items?itemName=NVIDIA.isaacsim-vscode-edition) to be installed and enabled, in the VS Code editor, in order to execute Python scripts on a running Isaac Sim instance.

1. To begin, enable this extension using the [Extension Manager](https://docs.omniverse.nvidia.com/extensions/latest/ext_core/ext_extension-manager.html "(in Omniverse Extensions)") by searching for `isaacsim.code_editor.vscode`.
2. Once the extension is enabled, go to the top menu bar and click on Window > VS Code to open the Isaac Sim folder in a VS Code application.
3. Open a stored file or write the code you want to run in a VS Code editor tab.
4. From the VS Code editor, click on the *Isaac Sim VS Code Edition* container in the Activity Bar (the one with the Isaac Sim logo) to open it.
   Then, click on *Run* (or *Run selected text* if you have selected code statements), in the *Commands* tree view, to execute it.
5. Inspect the execution output, if any, in the *Isaac Sim VS Code Edition* output panel.

Tip

The Python server can also be used independently of VS Code, for example by LLM agents or custom scripts.
See [Python Server (Remote Code Execution)](python_server.html#isaac-sim-app-python-server) for details on the wire protocol and programmatic usage.

---

## VS Code Configuration Files

The Isaac Sim installation provides a `.vscode` workspace with a pre-configured environment under the following three files:

```python
.vscode/launch.json
.vscode/settings.json
.vscode/tasks.json
```

### launch.json

This file provides three different configurations that can be executed using the `Run & Debug` section in VSCode.

* **Python: Current File**: Debug the currently open standalone Python file, should not be used with extension examples/code.
* **Python: Attach**: Attach to a running Isaac Sim application for debugging purposes, most useful when running an interactive GUI application. See [Attaching the Debugger to a Running App](../utilities/debugging/tutorial_advanced_python_debugging.html#isaac-sim-app-tutorial-advanced-attach-debugger) for usage information.
* **(Linux) isaac-sim** Run the main Isaac Sim application with an attached debugger.

### settings.json

This file sets the default Python executable that comes with Isaac Sim:

```python
# "python.pythonPath": "${workspaceFolder}/kit/python/bin/python3",
```

As well as a configuration for `"python.analysis.extraPaths"` which by default includes all of the extensions that are provided by default. You can add additional paths here if needed.

### tasks.json

This is a helper file that contains a task used to automatically setup the Python environment when using the `Python: Current File` option in `Run & Debug`.

```python
# "tasks": [
#     {
#         "label": "setup_python_env",
#         "type": "shell",
#         "linux": {
#             "command": "source ${workspaceFolder}/setup_python_env.sh && printenv >${workspaceFolder}/.vscode/.standalone_examples.env"
#         }
#     }
# ]
```

Once executed, the task generates the `.standalone_examples.env` file used by VS Code to launch the Python debug process.
Refer to [Debugging With Visual Studio Code](../utilities/debugging/tutorial_advanced_python_debugging.html#isaac-sim-app-tutorial-advanced-debug-vscode) for more details.

On this page

* [Isaac Sim VS Code Edition](#id1)
* [Interactive Scripting](#interactive-scripting)
* [VS Code Configuration Files](#vs-code-configuration-files)
  + [launch.json](#launch-json)
  + [settings.json](#settings-json)
  + [tasks.json](#tasks-json)

---

### Python Server

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/development_tools/python_server.html

* [Development Tools](index.html)
* Python Server (Remote Code Execution)

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Python Server (Remote Code Execution)

## Overview

The `isaacsim.code_editor.python_server` extension provides a TCP socket server that enables remote Python code execution within a running Isaac Sim instance.
Any client â VS Code, LLM agents, custom automation scripts â can connect over TCP, send Python source code, and receive structured JSON results.

The extension is automatically loaded as a dependency of `isaacsim.code_editor.vscode`, but it can also be enabled independently for headless or programmatic workflows.

---

## Enabling the Extension

Enable the extension using the [Extension Manager](https://docs.omniverse.nvidia.com/extensions/latest/ext_core/ext_extension-manager.html "(in Omniverse Extensions)") by searching for `isaacsim.code_editor.python_server`.

By default the server listens on `127.0.0.1:8226`.
These values can be changed through the Carbonite settings (see [Settings](#python-server-settings) below).

---

## Wire Protocol

The wire protocol is intentionally simple so that any TCP client can use it:

**Request**

Send raw UTF-8 Python source code over a TCP connection to the configured host and port.
After sending all code, the client **must** signal end-of-input by performing a TCP half-close
(`write_eof()` in Python, `shutdown(SHUT_WR)` at the socket level, or `-q 0` with netcat).
The server buffers incoming data until EOF is received, ensuring that TCP-fragmented payloads
are fully reassembled before execution.

Warning

If the client does not signal EOF, the server will wait indefinitely for more data and
the connection will hang until the client disconnects or a timeout occurs.

**Response**

A single JSON object is returned, then the connection is closed by the server.

| Field | Description |
| --- | --- |
| `status` | `"ok"` on success, `"error"` on failure. |
| `output` | Captured standard output (`stdout`) from the executed code. |
| `result` | *(present only for expression evaluation)* The evaluated expression value. JSON-native types (`str`, `int`, `float`, `bool`, `None`, `list`, `dict`) are returned directly. Non-serializable objects fall back to their `repr()` string. |
| `traceback` | *(present only on error)* List of traceback strings. |
| `ename` | *(present only on error)* Exception class name. |
| `evalue` | *(present only on error)* Exception message string. |

---

## Usage Examples

### Python Client

Connect from any Python script or LLM tool to execute code in the running Isaac Sim instance:

```python
import asyncio
import json

async def execute_in_isaac(source: str, host: str = "127.0.0.1", port: int = 8226) -> dict:
    """Send Python source to a running Isaac Sim instance and return the result."""
    reader, writer = await asyncio.open_connection(host, port)
    writer.write(source.encode())
    writer.write_eof()
    data = await reader.read()
    writer.close()
    return json.loads(data.decode())

# Execute a statement
result = asyncio.run(execute_in_isaac('print("Hello from Isaac Sim!")'))
print(result)
# {'status': 'ok', 'output': 'Hello from Isaac Sim!'}

# Evaluate an expression
result = asyncio.run(execute_in_isaac("1 + 1"))
print(result)
# {'status': 'ok', 'output': '', 'result': 2}

# Handle errors
result = asyncio.run(execute_in_isaac("1 / 0"))
print(result["status"])   # 'error'
print(result["ename"])    # 'ZeroDivisionError'
```

### Command-line (netcat)

For quick testing, use `netcat` or similar tools:

```python
echo 'print("Hello")' | nc 127.0.0.1 8226
```

---

## Async Code Support

The server supports top-level `await` expressions.
When submitted code contains `await`, the server compiles it as an async coroutine,
schedules it on the Kit event loop, and awaits the result before sending the JSON response.

```python
# Top-level await is supported
import asyncio
await asyncio.sleep(0.1)
print("this output is captured")
```

Standard output from `print()` calls inside awaited coroutines is captured and included in the
JSON response `output` field, just like synchronous code.

---

## State Persistence

The server maintains a shared Python globals dictionary across all connections within a session.
Variables, imports, and function definitions from one request are available in subsequent requests.
This enables incremental workflows such as building a scene step by step:

```python
# Request 1: Create a stage
import isaacsim.core.experimental.utils.stage as stage_utils
await stage_utils.create_new_stage_async(template="empty")

# Request 2: Uses stage_utils from the previous request
stage_utils.define_prim("/World", "Xform")
```

Each new TCP connection reuses the same globals, so there is no need to re-import modules
or re-define variables between calls.

---

## LLM Integration

The Python server is designed to be easy for LLM agents to use.
An LLM tool implementation needs only to:

1. Open a TCP connection to the configured host and port.
2. Send the Python code as UTF-8 bytes.
3. Signal end-of-input by calling `write_eof()` (required â the server buffers until EOF).
4. Read the JSON response.
5. Parse `status` to determine success or failure, `output` for printed text, and `result` for expression values.

Because the protocol is a single request/response per connection, there is no connection-level state to manage.
However, Python-level state (variables, imports) persists across connections within a session
(see [State Persistence](#python-server-state-persistence) above).

---

## Settings

The extension is configured through Carbonite settings under `/exts/isaacsim.code_editor.python_server/`.

| Setting | Default | Description |
| --- | --- | --- |
| `host` | `"127.0.0.1"` | IP address the server listens on. Set to `"0.0.0.0"` to accept remote connections. |
| `port` | `8226` | TCP port number. |
| `carb_logs` | `false` | Enable UDP broadcasting of Carbonite log messages to connected clients. May cause the application to freeze in certain circumstances. |

Warning

Setting `host` to `"0.0.0.0"` allows **any** machine on the network to execute arbitrary Python code
in your Isaac Sim session. Only do this in trusted network environments.

---

## Carbonite Log Broadcasting (UDP)

When `carb_logs` is enabled, the extension opens a UDP socket on the same host and port.
Clients register by sending any datagram to that address, after which all Carbonite log messages
(Info, Warning, Error, Fatal) are broadcast to registered clients as UTF-8 strings in the format:

```python
[Level][Source] Message
```

This is primarily used by the [Isaac Sim VS Code Edition](https://marketplace.visualstudio.com/items?itemName=NVIDIA.isaacsim-vscode-edition) extension to display Isaac Sim logs in the VS Code output panel.

On this page

* [Overview](#overview)
* [Enabling the Extension](#enabling-the-extension)
* [Wire Protocol](#wire-protocol)
* [Usage Examples](#usage-examples)
  + [Python Client](#python-client)
  + [Command-line (netcat)](#command-line-netcat)
* [Async Code Support](#async-code-support)
* [State Persistence](#state-persistence)
* [LLM Integration](#llm-integration)
* [Settings](#settings)
* [Carbonite Log Broadcasting (UDP)](#carbonite-log-broadcasting-udp)

---

### Jupyter Notebook

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/development_tools/jupyter_notebook.html

* [Development Tools](index.html)
* Jupyter Notebook

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Jupyter Notebook

## Interactive Scripting

The `isaacsim.code_editor.jupyter` extension allows you to to open a [JupyterLab](https://jupyter.org) (or [Jupyter Notebook](https://jupyter.org)) app in the current Isaac Sim application scope and edit and execute Python code interactively.

1. To begin, enable this extension using the [Extension Manager](https://docs.omniverse.nvidia.com/extensions/latest/ext_core/ext_extension-manager.html "(in Omniverse Extensions)") by searching for `isaacsim.code_editor.jupyter`.

   > Note
   >
   > This may take several seconds (and Isaac Sim will freeze) if this is the first time the `isaacsim.code_editor.jupyter` is enabled.
   > Several Python dependencies will be installed.
2. Once the extension is enabled, go to the top menu bar and click on Window > Jupyter Notebook to open a Jupyter app in the default web browser.
3. In the Jupyter app, click on the *Omniverse (Python 3)* kernel (the one with the Omniverse logo) to create a new Untitled notebook.
4. Execute code by clicking the Run button at the top of the notebook. Try it yourself with the same code snippet from above!

   > Warning
   >
   > * The *Omniverse (Python 3)* kernel is designed to run Python code, via the `isaacsim.code_editor.jupyter` extension, on a running Isaac Sim instance (where the Kit application has control over the update/simulation loop).
   > * The *Isaac Sim Python 3* kernel is used to run standalone applications (see [Running Standalone Isaac Sim from Jupyter Notebook](#isaac-sim-python-jupyter-notebook-config) for more details).

Warning

Execution of blocking code freezes Isaac Sim.

Hint

* Use the Tab key for code autocompletion.
* Use the Ctrl + I keys for code introspection (display docstring if available).

Note

The notebooks are saved, by default, in a folder within the extension itself: `exts/isaacsim.code_editor.jupyter/data/notebooks`. See the location for Isaac Sim packages/extensions in [Location for Isaac Sim app](../installation/install_faq.html#isaac-sim-misc-paths).

**Limitations**

* IPython magic commands are not available.
* Matplotlib plotting is not available in the notebooks.
* Printing, inside callbacks, is not displayed in the notebooks but in the Omniverse terminal.

---

## Running Standalone Isaac Sim from Jupyter Notebook

Warning

* This workflow is only supported on Linux.

### Configuration Files

In order for Isaac Sim to work inside of a Jupyter Notebook we provide a custom Jupyter kernel that is installed the first time you run `./jupyter_notebook.sh`.
The kernel.json itself is fairly simple:

```python
{
    "argv": ["AUTOMATICALLY_REPLACED", "-m", "ipykernel_launcher", "-f", "{connection_file}"],
    "display_name": "Isaac Sim Python 3",
    "language": "python",
    "env": {"ISAAC_JUPYTER_KERNEL": "1"},
    "metadata": {"debugger": true}
}
```

The important part is that `AUTOMATICALLY_REPLACED` gets replaced by `jupyter_notebook.sh` with the absolute path to the Python executable that is located in the kit/python directory at runtime. Once the variable is replaced, the kernel is installed and the notebook is started. There is an extra variable `ISAAC_JUPYTER_KERNEL` that is used inside of Isaac Sim to setup for notebook usage properly.

Because notebooks require asyncio support, and Isaac Sim itself uses asyncio internally, we automatically execute the following two lines when loading the `isaacsim` module (or the `isaacsim.simulation_app` extension) which provides the `SimulationApp` class:

```python
import nest_asyncio

nest_asyncio.apply()
```

This ensures that asyncio calls can be nested inside of the Jupyter Notebook properly.

When writing code in notebooks, it is necessary to first instantiate the `SimulationApp` class (from `isaacsim` or `isaacsim.simulation_app`) after perform any Isaac Sim / Omniverse imports:

```python
from isaacsim import SimulationApp

simulation_app = SimulationApp({"headless": True})
# perform any Isaac Sim / Omniverse imports after instantiating the class
```

Then, to run the notebook just execute the following commands and play the notebook cells:

```python
./jupyter_notebook.sh PATH_TO_NOTEBOOK.ipynb
```

On this page

* [Interactive Scripting](#interactive-scripting)
* [Running Standalone Isaac Sim from Jupyter Notebook](#running-standalone-isaac-sim-from-jupyter-notebook)
  + [Configuration Files](#configuration-files)

---

### Script Editor

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/development_tools/omniverse_script_editor.html

* [Development Tools](index.html)
* Omniverse Script Editor

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Omniverse Script Editor

Script Editor is a Python editing environment internal to Omniverse Kit. It can be used to run snippets of Python code to interact with the stage.

1. To open the Script Editor window, go to the Menu Bar and click *Window > Script Editor*.
2. Open multiple tabs by going to the *Tab* Menu in the Script Editor window. All the tabs share the same environment, so libraries that are imported or variables defined in one environment can be accessed and used in other environments.

Refer to [Script Editor](https://docs.omniverse.nvidia.com/extensions/latest/ext_script-editor.html "(in Omniverse Extensions)") in the Omniverse docs for more details.

---

### Isaac Sim MCP Server

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/development_tools/isaac_sim_mcp.html

* [Development Tools](index.html)
* Isaac Sim MCP Server

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Isaac Sim MCP Server

The Isaac Sim MCP Server is a Model Context Protocol (MCP) server that gives AI coding assistants deep knowledge of NVIDIA Isaac Sim â extensions, code examples, settings, and developer instructions â via semantic search.

For installation, MCP client setup, deployment options, and troubleshooting, see the [Isaac Sim MCP Server README](https://github.com/NVIDIA-Omniverse/kit-usd-agents/blob/main/source/mcp/isaacsim_mcp/README.md).

For developer documentation â key concepts, integration examples, performance notes, and pointers to the architecture and prompt-design references â see the [Isaac Sim MCP Server docs README](https://github.com/NVIDIA-Omniverse/kit-usd-agents/blob/main/source/mcp/isaacsim_mcp/docs/README.md).

---

### Carb Settings

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/development_tools/carb_settings.html

* [Development Tools](index.html)
* Modify Carb Settings

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Modify Carb Settings

[Carbonite (carb)](../reference_material/reference_glossary.html#isaac-sim-glossary-carb) settings are used to configure default behaviors of Omniverse and Isaac Sim. They can control a wide ranges of features, such as window properties, ROS versions, browser folders, and more. You may wish to change these settings to suit your needs. Here we show the four ways to change the Carb settings in Isaac Sim.

For this tutorial, we will set a parameter inside extension `isaacsim.code_editor.python_server` named `keepalive_interval` to the value `5`. Replace these with your actual extension name, setting parameter, and value when you are working with your project.

## Script Editor Snippet

You can temporarily and quickly change the Carb settings in the [Script Editor](https://docs.omniverse.nvidia.com/extensions/latest/ext_script-editor.html "(in Omniverse Extensions)"). This is useful for testing and debugging, and can be done while Isaac Sim is open. The changes made this way will not be saved after you close the application, and relaunching the simulator will reset the settings.

```python
import carb.settings
import omni.kit

## Set Carb Setting
settings = carb.settings.get_settings()
settings.set("/exts/isaacsim.code_editor.python_server/keepalive_interval", 5)

## Restart Extension to Apply Changes
extension_manager = omni.kit.app.get_app().get_extension_manager()
extension_manager.set_extension_enabled_immediate("isaacsim.code_editor.python_server", False)
extension_manager.set_extension_enabled_immediate("isaacsim.code_editor.python_server", True)
```

## Command-Line Argument

You can launch Isaac Sim with a command-line argument to change the Carb settings. The changes made this way will not be saved after you close the application, and relaunching the simulator without the arguments will reset the settings.

At the root of your Isaac Sim installation, run the following command:

> Linux
>
> ```python
> ./isaac-sim.sh --/exts/isaacsim.code_editor.python_server/keepalive_interval=5
> ```
>
>
> Windows
>
> ```python
> .\isaac-sim.bat --/exts/isaacsim.code_editor.python_server/keepalive_interval=5
> ```

## Edit .toml File

For more permanent changes, you can edit the extensionâs .toml file. The changes made this way will persist after you close the application.

1. Navigate to the extensionâs folder. For example, if you are changing the settings for the `isaacsim.code_editor.python_server` extension, navigate to `<isaac-sim-root_dir>/exts/isaacsim.code_editor.python_server/config`.
2. Open the .toml file with a text editor, and add the following line to the file:

   > ```python
   > [settings]
   > exts."isaacsim.code_editor.python_server".keepalive_interval = 5
   > ```
3. Launch Isaac Sim to see the changes.

## Customize .kit File

If you have multiple settings in multiple extensions that you want to change, you can edit the .kit file for your application. The changes made this way will persist after you close the application.

1. From the root of your Isaac Sim installation, navigate to <isaac-sim-root\_dir>/apps/. Locate the Kit experience app file you are using in this folder. By default, it is the isaacsim.exp.full.kit.
2. Open the app file and add the following line to the file:

   > ```python
   > [settings]
   > exts."isaacsim.code_editor.python_server".keepalive_interval = 5
   > ```
3. Launch Isaac Sim to see the changes.

On this page

* [Script Editor Snippet](#script-editor-snippet)
* [Command-Line Argument](#command-line-argument)
* [Edit .toml File](#edit-toml-file)
* [Customize .kit File](#customize-kit-file)

---


## Python 脚本

### Scripting Concepts

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/python_scripting/python_scripting_concepts.html

* [Python Scripting and Tutorials](index.html)
* Python Scripting Concepts

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Python Scripting Concepts

## Standalone vs Interactive Python

Python scripting in NVIDIA Isaac Sim can be done in two ways: standalone and interactive. Standalone Python scripts are executed from the command line and are used to automate tasks or run simulations. Interactive Python scripts are executed in the Python console and are used to explore the NVIDIA Isaac Sim API and test code snippets. Both types of scripts can be used to create custom extensions, such as new robot controllers or sensors, and to interact with the Omniverse application.

On this page

* [Standalone vs Interactive Python](#standalone-vs-interactive-python)

---

### Core API Overview

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/python_scripting/core_api_overview.html

* [Python Scripting and Tutorials](index.html)
* Core API Overview

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Core API Overview

Important

Isaac Sim 5.0.0 has introduced the [Core Experimental API](../py/docs/overview/experimental.html): a rewritten implementation of the current Core API
designed to be more robust, flexible, and powerful, yet still maintain the core utilities and wrapper concepts.

Going forward, it will become the base API used in all Isaac Sim source code.
The current Core API will be deprecated and removed in future releases.

Therefore, **we strongly encourage early adoption and use of the Core Experimental API**.

## Core API is a Wrapper

Isaac Sim Core API are wrappers for raw USD and physics engine APIs, tailored to suit robotics applications. Here is adding a cube and apply physics properties to it using the raw USD

```python
import omni
from pxr import Gf, PhysicsSchemaTools, PhysxSchema, UsdGeom, UsdPhysics

stage = omni.usd.get_context().get_stage()

# Setting up Physics Scene
gravity = 9.8
scene = UsdPhysics.Scene.Define(stage, "/World/physics")
scene.CreateGravityDirectionAttr().Set(Gf.Vec3f(0.0, 0.0, -1.0))
scene.CreateGravityMagnitudeAttr().Set(gravity)
PhysxSchema.PhysxSceneAPI.Apply(stage.GetPrimAtPath("/World/physics"))
physxSceneAPI = PhysxSchema.PhysxSceneAPI.Get(stage, "/World/physics")
physxSceneAPI.CreateEnableCCDAttr(True)
physxSceneAPI.CreateEnableStabilizationAttr(True)
physxSceneAPI.CreateEnableGPUDynamicsAttr(False)
physxSceneAPI.CreateBroadphaseTypeAttr("MBP")
physxSceneAPI.CreateSolverTypeAttr("TGS")

# Setting up Ground Plane
PhysicsSchemaTools.addGroundPlane(stage, "/World/groundPlane", "Z", 15, Gf.Vec3f(0, 0, 0), Gf.Vec3f(0.7))

# Adding a Cube
path = "/World/Cube"
cubeGeom = UsdGeom.Cube.Define(stage, path)
cubePrim = stage.GetPrimAtPath(path)
size = 0.5
offset = Gf.Vec3f(0.5, 0.2, 1.0)
cubeGeom.CreateSizeAttr(size)
cubeGeom.AddTranslateOp().Set(offset)

# Attach Rigid Body and Collision Preset
rigid_api = UsdPhysics.RigidBodyAPI.Apply(cubePrim)
rigid_api.CreateRigidBodyEnabledAttr(True)
UsdPhysics.CollisionAPI.Apply(cubePrim)
```

Here is adding a cube with physics and material properties to stage using Core API.

```python
import numpy as np
from isaacsim.core.api.objects import DynamicCuboid

DynamicCuboid(
    prim_path="/new_cube_2",
    name="cube_1",
    position=np.array([0, 0, 1.0]),
    scale=np.array([0.6, 0.5, 0.2]),
    size=1.0,
    color=np.array([255, 0, 0]),
)
```

## Application vs Simulation vs World vs Scene vs Stage

Everything in USD is a primitive (prim) with attributes.

A **Simulation** (the sim) moves these prims forward through time by literally changing these attributes programmatically.

The **Application** is the thing that manages the gross aspects of the simulation (how things are rendered, for example) and how the user interacts with it. If there is a GUI for the sim, it is a part of the application.

A **Stage** is a USD concept, and defines the logical and relational context for prims in the simulation. If a mug prim is on a table prim then that relationship is expressed by the relative locations of those prims on the stage, and the specific attributes each has. In this way, the stage provides context for the application: prims cannot exist without a stage and so an application concerned with prims requires a stage to function.

Similarly, the **World** is what provides context to the simulation, defining which prims are relevant to the ongoing flow of time, the **scene**, and managing the aspects of the simulation that are most important to the user.

For example, imagine you are going to see a play at a theater. The theater is like the **application**, your gateway to the play, while the **simulation** is the play itself, defined by a program. You take your seat and you can see the **stage**, where the play will take place. When the play starts, the curtain rises and reveals a **scene** composed props and actors that then act out that part of the play. When itâs time to move to the next scene, the curtain falls, the scene is reset, and then the curtain rises again, revealing the next part of the play. The stage crew and all the mechanical devices behind the scene that manages the curtain and the props is the **world** of the play.

On this page

* [Core API is a Wrapper](#core-api-is-a-wrapper)
* [Application vs Simulation vs World vs Scene vs Stage](#application-vs-simulation-vs-world-vs-scene-vs-stage)

---

### Environment Setup

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/python_scripting/environment_setup.html

* [Python Scripting and Tutorials](index.html)
* Scene Setup Snippets

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Scene Setup Snippets

## Objects Creation and Manipulation

Note

The following scripts should only be run on the default new stage and only once. You can try these by creating a new stage via File > New and running from Window > Script Editor

### Rigid Object Creation

The following snippet adds a dynamic cube with given properties and a ground plane to the scene.

```python
import isaacsim.core.experimental.utils.stage as stage_utils
import numpy as np
from isaacsim.core.experimental.objects import Cube, GroundPlane
from isaacsim.core.experimental.prims import GeomPrim, RigidPrim

stage_utils.define_prim("/World/physicsScene", "PhysicsScene")
GroundPlane("/World/groundPlane", sizes=10, colors=np.array([0.5, 0.5, 0.5]), templates=None)
cube = Cube(
    "/World/cube",
    positions=np.array([-0.5, -0.2, 1.0]),
    scales=np.array([0.5, 0.5, 0.5]),
    colors=np.array([0.2, 0.3, 0.0]),
)
RigidPrim(cube.paths, masses=[1.0])
GeomPrim(cube.paths, apply_collision_apis=True)
```

### View Objects

View classes in this extension are collections of similar prims. View classes manipulate the underlying objects in a vectorized way.
Many View APIs can operate directly on USD data after the wrapper is created.

```python
from isaacsim.core.experimental.objects import Cube
from isaacsim.core.experimental.prims import GeomPrim, RigidPrim

cube = Cube("/World/cube_0")
GeomPrim(cube.paths, apply_collision_apis=True)
rigid_prim = RigidPrim("/World/cube_[0-100]", masses=[1.0])
# rigid_prim can now be used for USD-backed batched operations
```

Tensor-backed physics APIs require the timeline to be playing before they can be queried. When using Window > Script Editor, initialize them asynchronously as follows:

```python
import asyncio

import isaacsim.core.experimental.utils.app as app_utils
import isaacsim.core.experimental.utils.stage as stage_utils
from isaacsim.core.experimental.objects import Cube, GroundPlane
from isaacsim.core.experimental.prims import GeomPrim, RigidPrim

async def init():
    stage_utils.define_prim("/World/physicsScene", "PhysicsScene")
    GroundPlane("/World/groundPlane", positions=[0.0, 0.0, -1.0])
    cube = Cube("/World/cube_0")
    GeomPrim(cube.paths, apply_collision_apis=True)
    rigid_prim = RigidPrim("/World/cube_[0-100]", masses=[1.0])
    app_utils.play()
    await app_utils.update_app_async()
    print("Physics tensor view initialized:", rigid_prim.is_physics_tensor_entity_valid())
    app_utils.stop()

asyncio.ensure_future(init())
```

See [Workflows](../introduction/workflows.html#isaac-sim-app-tutorial-intro-workflows) tutorial for more details about various workflows for developing in Isaac Sim.

### Create RigidPrim

The following snippet adds three cubes to the scene and creates a RigidPrim (formerly RigidPrimView) to manipulate the batch.

```python
import asyncio

import isaacsim.core.experimental.utils.stage as stage_utils
import numpy as np
from isaacsim.core.experimental.objects import Cube, GroundPlane
from isaacsim.core.experimental.prims import GeomPrim, RigidPrim

async def example():
    stage_utils.define_prim("/World/physicsScene", "PhysicsScene")
    GroundPlane("/World/groundPlane", positions=[0.0, 0.0, -1.0])

    # create rigid cubes
    cube_paths = [f"/World/cube_{i}" for i in range(3)]
    Cube(cube_paths)
    GeomPrim(cube_paths, apply_collision_apis=True)

    # create the view object to batch manipulate the cubes
    rigid_prim = RigidPrim("/World/cube_[0-2]", masses=[1.0])
    # set world poses
    rigid_prim.set_world_poses(positions=np.array([[0, 0, 2], [0, -2, 2], [0, 2, 2]]))

asyncio.ensure_future(example())
```

See the [API Documentation](../py/source/extensions/isaacsim.core.experimental.prims/docs/index.html#isaacsim.core.experimental.prims.RigidPrim) for all the possible operations supported by `RigidPrim`.

### Create RigidPrim With Contact Filters

There are scenarios where you are interested in net contact forces on each body and contact forces between specific bodies. This can be achieved by constructing a RigidPrim with contact filters.

```python
import asyncio

import isaacsim.core.experimental.utils.app as app_utils
import isaacsim.core.experimental.utils.stage as stage_utils
import numpy as np
from isaacsim.core.experimental.objects import Cube, GroundPlane
from isaacsim.core.experimental.prims import GeomPrim, RigidPrim

async def example():
    stage_utils.define_prim("/World/physicsScene", "PhysicsScene")
    GroundPlane("/World/groundPlane")

    # create three rigid cubes sitting on top of three others
    bottom_box_paths = [f"/World/bottom_box_{i+1}" for i in range(3)]
    top_box_paths = [f"/World/top_box_{i+1}" for i in range(3)]
    Cube(bottom_box_paths, sizes=2, colors=np.array([0.5, 0, 0]))
    Cube(top_box_paths, sizes=2, colors=np.array([0, 0, 0.5]))
    GeomPrim(bottom_box_paths + top_box_paths, apply_collision_apis=True)

    # Specify top boxes as filters to receive contact forces between the bottom and top boxes.
    bottom_box = RigidPrim(
        bottom_box_paths,
        masses=[1.0],
        positions=np.array([[0, 0, 1.0], [-5.0, 0, 1.0], [5.0, 0, 1.0]]),
        contact_filter_paths=top_box_paths,
        max_contact_count=30,
    )
    top_box = RigidPrim(
        top_box_paths,
        masses=[1.0],
        positions=np.array([[0.0, 0, 3.0], [-5.0, 0, 3.0], [5.0, 0, 3.0]]),
    )
    bottom_box.set_enabled_contact_tracking([True])
    top_box.set_enabled_contact_tracking([True])

    app_utils.play()
    await app_utils.update_app_async(steps=10)

    # net contact forces acting on the bottom boxes
    print(bottom_box.get_net_contact_forces().numpy())
    # contact forces between the top and the bottom boxes
    print(bottom_box.get_contact_force_matrix().numpy())
    app_utils.stop()

asyncio.ensure_future(example())
```

More detailed information about the friction and contact forces can be obtained from the `get_friction_data` and `get_contact_force_data` respectively.
These APIs provide all the contact forces and contact points between pairs of the sensor prims and filter prims. `get_contact_force_data` API provides the contact distances and contact normal vectors as well.

In the example below, we add three boxes to the scene and apply a tangential force of magnitude 10 to each. Then we use the aforementioned APIs to receive all the contact information and sum across all the contact points to find the friction/normal forces between the boxes and the ground plane.

```python
import asyncio

import isaacsim.core.experimental.utils.app as app_utils
import isaacsim.core.experimental.utils.stage as stage_utils
import numpy as np
from isaacsim.core.experimental.materials import RigidBodyMaterial
from isaacsim.core.experimental.objects import Cube, GroundPlane
from isaacsim.core.experimental.prims import GeomPrim, RigidPrim
from isaacsim.core.simulation_manager import SimulationManager
from pxr import PhysxSchema

async def contact_force_example():
    g = 10
    await stage_utils.create_new_stage_async()
    stage_utils.define_prim("/World/physicsScene", "PhysicsScene")
    ground_plane = GroundPlane("/World/GroundPlane")
    material = RigidBodyMaterial(
        "/World/PhysicsMaterials",
        static_frictions=[0.5],
        dynamic_frictions=[0.5],
    )
    # create three rigid cubes sitting on top of three others
    cube_paths = [f"/World/Box_{i+1}" for i in range(3)]
    Cube(cube_paths, sizes=2, colors=np.array([0, 0, 0.5]))
    cube_geoms = GeomPrim(cube_paths, apply_collision_apis=True)
    cube_geoms.apply_physics_materials(material)

    # Creating RigidPrim with contact relevant keywords allows receiving contact information
    # In the following we indicate that we are interested in receiving up to 30 contact points data between the boxes and the ground plane
    box_view = RigidPrim(
        cube_paths,
        masses=[1.0],
        positions=np.array([[0, 0, 1.0], [-5.0, 0, 1.0], [5.0, 0, 1.0]]),
        contact_filter_paths=["/World/GroundPlane/collisionPlane"],
        max_contact_count=3 * 10,  # we don't expect more than 10 contact points for each box
    )
    if SimulationManager.get_active_physics_engine() == "physx":
        box_view.set_sleep_thresholds([0.0])
        box_view.set_enabled_contact_tracking([True])
        GeomPrim.ensure_api(ground_plane.planes.prims, PhysxSchema.PhysxContactReportAPI)

    app_utils.play()
    await app_utils.update_app_async()

    forces = np.array([[g, 0, 0], [g, 0, 0], [g, 0, 0]])
    box_view.apply_forces(forces)
    await app_utils.update_app_async(steps=5)

    # tangential forces
    friction_forces, friction_points, friction_pair_contacts_count, friction_pair_contacts_start_indices = (
        box_view.get_friction_data(dt=1 / 60)
    )
    # normal forces
    forces, points, normals, distances, pair_contacts_count, pair_contacts_start_indices = (
        box_view.get_contact_force_data(dt=1 / 60)
    )
    friction_forces = friction_forces.numpy()
    forces = forces.numpy()
    normals = normals.numpy()
    pair_contacts_count = pair_contacts_count.numpy()
    pair_contacts_start_indices = pair_contacts_start_indices.numpy()
    friction_pair_contacts_count = friction_pair_contacts_count.numpy()
    friction_pair_contacts_start_indices = friction_pair_contacts_start_indices.numpy()
    # pair_contacts_count, pair_contacts_start_indices are tensors of size num_sensors x num_filters
    # friction_pair_contacts_count, friction_pair_contacts_start_indices are tensors of size num_sensors x num_filters
    # use the following tensors to sum across all the contact points
    force_aggregate = np.zeros((len(box_view), box_view.num_contact_filters, 3))
    friction_force_aggregate = np.zeros((len(box_view), box_view.num_contact_filters, 3))

    # process contacts for each pair i, j
    for i in range(pair_contacts_count.shape[0]):
        for j in range(pair_contacts_count.shape[1]):
            start_idx = pair_contacts_start_indices[i, j]
            friction_start_idx = friction_pair_contacts_start_indices[i, j]
            count = pair_contacts_count[i, j]
            friction_count = friction_pair_contacts_count[i, j]
            # sum/average across all the contact points for each pair
            pair_forces = forces[start_idx : start_idx + count]
            pair_normals = normals[start_idx : start_idx + count]
            force_aggregate[i, j] = np.sum(pair_forces * pair_normals, axis=0)

            # sum/average across all the friction pairs
            pair_forces = friction_forces[friction_start_idx : friction_start_idx + friction_count]
            friction_force_aggregate[i, j] = np.sum(pair_forces, axis=0)

    print("friction forces: \n", friction_force_aggregate)
    print("contact forces: \n", force_aggregate)
    # get_contact_force_matrix API is equivalent to the summation of the individual contact forces computed above
    print("contact force matrix: \n", box_view.get_contact_force_matrix(dt=1 / 60).numpy())
    # get_net_contact_forces API is the summation of the all forces
    # in the current example because all the potential contacts are captured by the choice of our filter prims (/World/GroundPlane/collisionPlane)
    # the following is similar to the reduction of the contact force matrix above across the filters
    print("net contact force: \n", box_view.get_net_contact_forces(dt=1 / 60).numpy())
    app_utils.stop()

asyncio.ensure_future(contact_force_example())
```

See the [API Documentation](../py/source/extensions/isaacsim.core.experimental.prims/docs/index.html#isaacsim.core.experimental.prims.RigidPrim) for more information about contact APIs on `RigidPrim`.

### Set Mass Properties for a Mesh

The snippet below shows how to set the mass of a physics object. Density can also be specified as an alternative

```python
from isaacsim.core.experimental.objects import Cube
from isaacsim.core.experimental.prims import GeomPrim, RigidPrim

cube = Cube("/World/Cube")
# Make it a rigid body
geom_prim = GeomPrim(cube.paths, apply_collision_apis=True)
geom_prim.set_collision_approximations(["convexHull"])

rigid_prim = RigidPrim(cube.paths)
rigid_prim.set_masses([10.0])
### Alternatively set the density
rigid_prim.set_densities([1000.0])
```

### Get Size of a Mesh

The snippet below shows how to get the size of a mesh.

```python
import isaacsim.core.experimental.utils.bounds as bounds_utils
from isaacsim.core.experimental.objects import Cone

cone = Cone("/World/Cone")
# Get the size
aabb = bounds_utils.compute_aabb(cone.paths[0])
prim_size = aabb[3:] - aabb[:3]
print(prim_size)
```

### Apply Semantic Data on Entire Stage

The snippet below shows how to programmatically apply semantic data on objects by iterating the entire stage.

```python
import isaacsim.core.experimental.utils.semantics as semantics_utils
import omni.usd

def remove_prefix(name, prefix):
    if name.startswith(prefix):
        return name[len(prefix) :]
    return name

def remove_numerical_suffix(name):
    suffix = name.split("_")[-1]
    if suffix.isnumeric():
        return name[: -len(suffix) - 1]
    return name

def remove_underscores(name):
    return name.replace("_", "")

stage = omni.usd.get_context().get_stage()
for prim in stage.Traverse():
    if prim.GetTypeName() == "Mesh":
        label = str(prim.GetPrimPath()).split("/")[-1]
        label = remove_prefix(label, "SM_")
        label = remove_numerical_suffix(label)
        label = remove_underscores(label)
        semantics_utils.add_labels(prim, labels=[label], taxonomy="class")
```

### Convert Asset to USD

The below script will convert a non-USD asset like OBJ/STL/FBX to USD. This is meant to be used inside the [Script Editor](../development_tools/omniverse_script_editor.html#script-editor). For running it as a [Standalone Application](../introduction/workflows.html#standalone-application), Check [Python Environment](manual_standalone_python.html#isaac-sim-python-environment).
The input mesh path is illustrative and should be replaced with the asset path you want to convert.

```python
import asyncio
import tempfile
from pathlib import Path

import carb
import omni

async def convert_asset_to_usd(input_obj: str, output_usd: str):
    import omni.kit.asset_converter

    def progress_callback(progress, total_steps):
        pass

    converter_context = omni.kit.asset_converter.AssetConverterContext()
    # setup converter and flags
    # converter_context.ignore_material = False
    # converter_context.ignore_animation = False
    # converter_context.ignore_cameras = True
    # converter_context.single_mesh = True
    # converter_context.smooth_normals = True
    # converter_context.preview_surface = False
    # converter_context.support_point_instancer = False
    # converter_context.embed_mdl_in_usd = False
    # converter_context.use_meter_as_world_unit = True
    # converter_context.create_world_as_default_root_prim = False
    instance = omni.kit.asset_converter.get_instance()
    task = instance.create_converter_task(input_obj, output_usd, progress_callback, converter_context)
    success = await task.wait_until_finished()
    if not success:
        carb.log_error(f"{task.get_status()}, {task.get_error_message()}")
    print("converting done")

demo_dir = Path(tempfile.gettempdir()) / "isaacsim_asset_converter_demo"
demo_dir.mkdir(parents=True, exist_ok=True)

# This repo mesh path is illustrative; replace it with the path to your own OBJ/STL/FBX asset.
input_asset = Path("source/standalone_examples/data/torus/torus.stl")
output_usd = demo_dir / "torus.usd"
asyncio.ensure_future(convert_asset_to_usd(str(input_asset), str(output_usd)))
```

The details about the optional import options in the converter context can be found [here](https://docs.omniverse.nvidia.com/extensions/latest/ext_asset-converter.html "(in Omniverse Extensions)").

## Physics How-Tos

### Create A Physics Scene

```python
from isaacsim.core.simulation_manager import PhysxScene

# Add a physics scene prim to stage
physics_scene = PhysxScene("/World/physicsScene")
# Set gravity vector
physics_scene.set_gravity([0.0, 0.0, -9.81])
```

The following can be added to set specific settings, in this case use CPU physics and the TGS solver

```python
from isaacsim.core.simulation_manager import PhysxScene, SimulationManager

physics_scene = PhysxScene("/World/physicsScene")
physics_scene.set_gravity([0.0, 0.0, -9.81])

SimulationManager.set_device("cpu")
physics_scene.set_enabled_ccd(True)
physics_scene.set_enabled_stabilization(True)
physics_scene.set_enabled_gpu_dynamics(False)
physics_scene.set_broadphase_type("MBP")
physics_scene.set_solver_type("TGS")
```

Adding a ground plane to a stage can be done via the following code:
It creates a Z up plane with a size of 100 cm at a Z coordinate of -100

```python
from isaacsim.core.experimental.objects import GroundPlane

GroundPlane("/World/groundPlane", sizes=100.0, positions=[0.0, 0.0, -100.0], colors=[1.0, 1.0, 1.0], templates=None)
```

### Enable Physics And Collision For a Mesh

The script below assumes there is a physics scene in the stage.

```python
from isaacsim.core.experimental.objects import Cube
from isaacsim.core.experimental.prims import GeomPrim, RigidPrim

# Create a cube mesh in the stage
cube = Cube("/World/Cube")
# Enable physics on prim
# If a tighter collision approximation is desired use convexDecomposition instead of convexHull
geom_prim = GeomPrim(cube.paths, apply_collision_apis=True)
geom_prim.set_collision_approximations(["convexHull"])
RigidPrim(cube.paths)
```

If a tighter collision approximation is desired use convexDecomposition

```python
from isaacsim.core.experimental.objects import Cube
from isaacsim.core.experimental.prims import GeomPrim, RigidPrim

# Create a cube mesh in the stage
cube = Cube("/World/Cube")
# Enable physics on prim
# If a tighter collision approximation is desired use convexDecomposition instead of convexHull
geom_prim = GeomPrim(cube.paths, apply_collision_apis=True)
geom_prim.set_collision_approximations(["convexDecomposition"])
RigidPrim(cube.paths)
```

To verify that collision meshes have been successfully enabled, click the âeyeâ icon > âShow By Typeâ >
âPhysics Meshâ > âAllâ. This will show the collision meshes as pink outlines on the objects.

### Traverse a stage and assign collision meshes to children

```python
import isaacsim.core.experimental.utils.stage as stage_utils
from isaacsim.core.experimental.objects import Cube, Mesh
from isaacsim.core.experimental.prims import GeomPrim
from pxr import Usd, UsdGeom

stage = stage_utils.get_current_stage()

def add_cube(path, size: float = 10, offset=None):
    if offset is None:
        offset = [0.0, 0.0, 0.0]
    Cube(path, sizes=size, positions=offset)

### The following prims are added for illustrative purposes
Mesh("/World/Torus", primitives="Torus")
# all prims under AddCollision will get collisions assigned
add_cube("/World/Cube_0", offset=[100.0, 100.0, 0.0])
# create a prim nested under without a parent
stage_utils.define_prim("/World/Nested", "Xform")
add_cube("/World/Nested/Cube", offset=[100.0, 0.0, 100.0])
###

# Traverse all prims in the stage starting at this path
curr_prim = stage.GetPrimAtPath("/")
shape_types = (UsdGeom.Cylinder, UsdGeom.Capsule, UsdGeom.Cone, UsdGeom.Sphere, UsdGeom.Cube)

for prim in Usd.PrimRange(curr_prim):
    # only process shapes and meshes
    if any(prim.IsA(shape_type) for shape_type in shape_types):
        # use a ConvexHull for regular prims
        geom_prim = GeomPrim(str(prim.GetPath()), apply_collision_apis=True)
        geom_prim.set_collision_approximations(["convexHull"])
    elif prim.IsA(UsdGeom.Mesh):
        # "none" will use the base triangle mesh if available
        # Can also use "convexDecomposition", "convexHull", "boundingSphere", "boundingCube"
        geom_prim = GeomPrim(str(prim.GetPath()), apply_collision_apis=True)
        geom_prim.set_collision_approximations(["none"])
```

### Do Overlap Test

These snippets detect and report when objects overlap with a specified cubic/spherical region.
The following is assumed: the stage contains a physics scene, all objects have collision meshes enabled,
and the play button has been clicked.

The parameters: extent, origin and rotation (or origin and radius) define the cubic/spherical region to check overlap against.
The output of the physX query is the number of objects that overlaps with this cubic/spherical region.

```python
import carb
import omni
import omni.physx
from omni.physx import get_physx_scene_query_interface
from pxr import Gf, UsdGeom, Vt

def report_hit(hit):
    # When a collision is detected, the object color changes to red.
    hitColor = Vt.Vec3fArray([Gf.Vec3f(180.0 / 255.0, 16.0 / 255.0, 0.0)])
    usdGeom = UsdGeom.Mesh.Get(omni.usd.get_context().get_stage(), hit.rigid_body)
    usdGeom.GetDisplayColorAttr().Set(hitColor)
    return True

def check_overlap():
    # Defines a cubic region to check overlap with
    extent = carb.Float3(20.0, 20.0, 20.0)
    origin = carb.Float3(0.0, 0.0, 0.0)
    rotation = carb.Float4(0.0, 0.0, 1.0, 0.0)
    # physX query to detect number of hits for a cubic region
    numHits = get_physx_scene_query_interface().overlap_box(extent, origin, rotation, report_hit, False)
    # physX query to detect number of hits for a spherical region
    # numHits = get_physx_scene_query_interface().overlap_sphere(radius, origin, report_hit, False)
    return numHits > 0
```

### Do Raycast Test

This snippet detects the closest object that intersects with a specified ray.
The following is assumed: the stage contains a physics scene, all objects have collision meshes enabled,
and the play button has been clicked.

The parameters: origin, rayDir and distance define a ray along which a ray hit might be detected.
The output of the query can be used to access the objectâs reference, and its distance from the raycast origin.

```python
import carb
import omni
import omni.physx
from omni.physx import get_physx_scene_query_interface
from pxr import Gf, UsdGeom, Vt

def check_raycast():
    # Projects a raycast from 'origin', in the direction of 'rayDir', for a length of 'distance' cm
    # Parameters can be replaced with real-time position and orientation data  (e.g. of a camera)
    origin = carb.Float3(0.0, 0.0, 0.0)
    rayDir = carb.Float3(1.0, 0.0, 0.0)
    distance = 100.0
    # physX query to detect closest hit
    hit = get_physx_scene_query_interface().raycast_closest(origin, rayDir, distance)
    if hit["hit"]:
        # Change object color to yellow and record distance from origin
        usdGeom = UsdGeom.Mesh.Get(omni.usd.get_context().get_stage(), hit["rigidBody"])
        hitColor = Vt.Vec3fArray([Gf.Vec3f(255.0 / 255.0, 255.0 / 255.0, 0.0)])
        usdGeom.GetDisplayColorAttr().Set(hitColor)
        distance = hit["distance"]
        return usdGeom.GetPath().pathString, distance
    return None, 10000.0

print(check_raycast())
```

## USD How-Tos

### Creating, Modifying, Assigning Materials

```python
from isaacsim.core.experimental.materials import OmniGlassMaterial
from isaacsim.core.experimental.objects import Cube

# Create a new material using OmniGlass.mdl
material = OmniGlassMaterial("/World/OmniGlassMaterial")
# Set material inputs, these can be determined by looking at the .mdl file
# or by selecting the Shader attached to the Material in the stage window and looking at the details panel
material.set_input_values("glass_color", [0.0, 1.0, 0.0])
material.set_input_values("glass_ior", [1.0])
# Create a prim to apply the material to
cube = Cube("/World/Cube")
# Bind the material to the prim
cube.apply_visual_materials(material)
```

Assigning a texture to a material that supports it can be done as follows:

```python
from isaacsim.core.experimental.materials import OmniPbrMaterial
from isaacsim.core.experimental.objects import Cube
from isaacsim.storage.native import get_assets_root_path

texture_path = get_assets_root_path(skip_check=True) + "/Isaac/Samples/DR/Materials/Textures/marble_tile.png"

# Create a new material using OmniPBR.mdl
material = OmniPbrMaterial("/World/OmniPBRMaterial")
# Set material inputs, these can be determined by looking at the .mdl file
# or by selecting the Shader attached to the Material in the stage window and looking at the details panel
material.set_input_values("diffuse_texture", texture_path)
# Create a prim to apply the material to
cube = Cube("/World/Cube")
# Bind the material to the prim
cube.apply_visual_materials(material)
```

### Set World Pose on a Prim

```python
import isaacsim.core.experimental.utils.transform as transform_utils
from isaacsim.core.experimental.objects import Cube
from isaacsim.core.experimental.prims import XformPrim

# Create a cube mesh in the stage to demonstrate setting a world pose on a prim
cube = Cube("/World/Cube")

# Get the prim and set its world pose
orientation = transform_utils.euler_angles_to_quaternion([0.0, 290.0, 0.0], degrees=True)
XformPrim(cube.paths).set_world_poses(positions=[[0.10, 1.0, 1.5]], orientations=orientation)
```

### Align two USD prims

```python
import isaacsim.core.experimental.utils.transform as transform_utils
from isaacsim.core.experimental.objects import Cube
from isaacsim.core.experimental.prims import XformPrim

# Create a cube
cube_a = Cube("/World/CubeA")
# change the cube pose
orientation = transform_utils.euler_angles_to_quaternion([0.0, 290.0, 0.0], degrees=True)
prim_a = XformPrim(cube_a.paths)
prim_a.set_world_poses(positions=[[0.10, 1.0, 1.5]], orientations=orientation)
# Create a second cube
cube_b = Cube("/World/CubeB")
# Get the transform of the first cube
positions, orientations = prim_a.get_world_poses()
# Set the pose of prim_b to that of prim_a
XformPrim(cube_b.paths).set_world_poses(positions=positions, orientations=orientations)
```

### Get World Transform At Current Timestamp For Selected Prims

```python
import isaacsim.core.experimental.utils.transform as transform_utils
import omni
from isaacsim.core.experimental.objects import Cube
from isaacsim.core.experimental.prims import XformPrim

usd_context = omni.usd.get_context()

#### For testing purposes we create and select a prim
#### This section can be removed if you already have a prim selected
cube = Cube("/World/Cube")
# change the cube pose
orientation = transform_utils.euler_angles_to_quaternion([0.0, 290.0, 0.0], degrees=True)
XformPrim(cube.paths).set_world_poses(positions=[[0.10, 1.0, 1.5]], orientations=orientation)
omni.usd.get_context().get_selection().set_prim_path_selected(cube.paths[0], True, True, True, False)
####

# Get list of selected primitives
selected_prims = usd_context.get_selection().get_selected_prim_paths()
# Loop through all prims and print their transforms
for prim_path in selected_prims:
    print("Selected", prim_path)
    positions, orientations = XformPrim(prim_path).get_world_poses()
    rotation_matrices = transform_utils.quaternion_to_rotation_matrix(orientations)
    print("Translation: ", positions.numpy()[0])
    print("Rotation: ", orientations.numpy()[0])
    print("Rotation matrix:", rotation_matrices.numpy()[0])
```

### Save current stage to USD

This can be useful if generating a stage in Python and you want to store it to reload later for debugging.

```python
import tempfile
from pathlib import Path

import omni
from isaacsim.core.experimental.objects import Cube

# Create a prim
Cube("/World/Cube")
# Change the path as needed.
output_path = Path(tempfile.gettempdir()) / "isaacsim_saved_stage.usd"
omni.usd.get_context().save_as_stage(str(output_path), None)
print(f"Saved stage to {output_path}")
```

On this page

* [Objects Creation and Manipulation](#objects-creation-and-manipulation)
  + [Rigid Object Creation](#rigid-object-creation)
  + [View Objects](#view-objects)
  + [Create RigidPrim](#create-rigidprim)
  + [Create RigidPrim With Contact Filters](#create-rigidprim-with-contact-filters)
  + [Set Mass Properties for a Mesh](#set-mass-properties-for-a-mesh)
  + [Get Size of a Mesh](#get-size-of-a-mesh)
  + [Apply Semantic Data on Entire Stage](#apply-semantic-data-on-entire-stage)
  + [Convert Asset to USD](#convert-asset-to-usd)
* [Physics How-Tos](#physics-how-tos)
  + [Create A Physics Scene](#create-a-physics-scene)
  + [Enable Physics And Collision For a Mesh](#enable-physics-and-collision-for-a-mesh)
  + [Traverse a stage and assign collision meshes to children](#traverse-a-stage-and-assign-collision-meshes-to-children)
  + [Do Overlap Test](#do-overlap-test)
  + [Do Raycast Test](#do-raycast-test)
* [USD How-Tos](#usd-how-tos)
  + [Creating, Modifying, Assigning Materials](#creating-modifying-assigning-materials)
  + [Set World Pose on a Prim](#set-world-pose-on-a-prim)
  + [Align two USD prims](#align-two-usd-prims)
  + [Get World Transform At Current Timestamp For Selected Prims](#get-world-transform-at-current-timestamp-for-selected-prims)
  + [Save current stage to USD](#save-current-stage-to-usd)

---

### Standalone Python

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/python_scripting/manual_standalone_python.html

* [Python Scripting and Tutorials](index.html)
* Python Environment

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Python Environment

This document will cover:

* Details about how running standalone Python scripts works.
* A short list of interesting/useful standalone Python scripts to try.
* Resources to develop Python scripts for NVIDIA Isaac Sim, such as VSCode and Jupyter Notebook support.

## Details: How `python.sh` works

Note

* On Windows use python.bat instead of python.sh
* The details of how python.sh works below are similar to how python.bat works

This script first defines the location of the apps folder so the contained .kit files can be located at runtime.

```python
# Get path to the script
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
# The apps directory is relative to where the script lives
export EXP_PATH=$SCRIPT_DIR/apps
```

Then we source the NVIDIA Isaac Sim Python environment so all extension interfaces can be loaded correctly.

```python
source ${SCRIPT_DIR}/setup_python_env.sh
```

The setup\_python\_env.sh script update/defined the following environment variables:

* ISAAC\_PATH: Path to the main isaac folder
* PYTHONPATH: Paths to each extensions Python interfaces
* LD\_LIBRARY\_PATH: Paths to binary interfaces required to find symbols at runtime
* CARB\_APP\_PATH: path to the core Omniverse kit executable

Finally, we execute the Python interpreter that is packaged with Omniverse:

```python
python_exe=${PYTHONEXE:-"${SCRIPT_DIR}/kit/python/bin/python3"}
...
$python_exe $@
```

## SimulationApp

The [SimulationApp Class](../py/source/extensions/isaacsim.simulation_app/docs/index.html) provides convenience functions to manage the lifetime of a NVIDIA Isaac Sim application.

### Usage Example:

The following code provides a usage example for how SimulationApp can be used to create an app, step forward in time and then exit.

Note

Any Omniverse level imports **must** occur after the class is instantiated.
Because APIs are provided by the extension/runtime plugin system, it must be loaded before they will be available to import.

Important

When running headless:

* Set `"headless": True` in the config when initializing `SimulationApp`
* Any calls that create/open a matplotlib window need to be commented out

```python
from isaacsim import SimulationApp

# Simple example showing how to start and stop the helper
simulation_app = SimulationApp({"headless": True})

### Perform any omniverse imports here after the helper loads ###

simulation_app.update()  # Render a single frame
simulation_app.close()  # Cleanup application
```

### Details: How `SimulationApp` works

Although `SimulationApp` further configures the application and exposes APIs, there are some fundamental steps in any Omniverse Kit-based implementation that must be executed.

The first is to get the carbonite framework.
Here the environment variables (e.g.: `CARB_APP_PATH`, `ISAAC_PATH` and `EXP_PATH`) were defined when running the python.sh script.

```python
import carb
import omni.kit.app

framework = carb.get_framework()
framework.load_plugins(
    loaded_file_wildcards=["omni.kit.app.plugin"],
    search_paths=[os.path.abspath(f'{os.environ["CARB_APP_PATH"]}/kernel/plugins')],
)
```

After loading the framework, it is possible to configure the start arguments before loading the application. For example:

```python
# Inject a experience config
sys.argv.insert(1, f'{os.environ["EXP_PATH"]}/isaacsim.exp.base.python.kit')

# Add paths to extensions
sys.argv.append(f"--ext-folder")
sys.argv.append(f'{os.path.abspath(os.environ["ISAAC_PATH"])}/exts')

# Run headless
sys.argv.append("--no-window")
```

And then start the application.

```python
app = omni.kit.app.get_app()
app.startup("Isaac-Sim", os.environ["CARB_APP_PATH"], sys.argv)
```

Shutting down a running application is done by calling `shutdown` and then unloading the framework:

```python
app.shutdown()
framework.unload_all_plugins()
```

### Enabling additional extensions

There are two methods for adding additional extensions:

1. Under `[dependencies]` section in an experience file (e.g.: `apps/isaacsim.exp.base.python.kit`):

   > ```python
   > # [dependencies]
   > # # Enable the layers and stage windows in the UI
   > # "omni.kit.window.stage" = {}
   > # "omni.kit.widget.layers" = {}
   > ```
2. From Python code:

   ```python
   from isaacsim import SimulationApp

   # Start the application
   simulation_app = SimulationApp({"headless": False})

   # Get the utility to enable extensions
   from isaacsim.core.utils.extensions import enable_extension

   # Enable the layers and stage windows in the UI
   enable_extension("omni.kit.widget.stage")
   enable_extension("omni.kit.widget.layers")

   simulation_app.update()
   ```

## Standalone Example Scripts

### Time Stepping

This sample shows how to start an Omniverse Kit Python app and then create callbacks which get called each rendering frame and each physics timestep. It also shows the different ways to step physics and rendering.

The sample can be executed by running the following:

```python
./python.sh standalone_examples/deprecated/api/isaacsim.core.api/time_stepping.py
```

### Load USD Stage

This sample demonstrates how to load a USD stage and start simulating it.

The sample can be executed by running the following, specify `usd_path` to a location on your nucleus server:

```python
./python.sh standalone_examples/api/isaacsim.simulation_app/load_stage.py --usd_path /Isaac/Environments/Simple_Room/simple_room.usd
```

### URDF Import

This sample demonstrates how to use the URDF Python API, configure its physics and then simulate it for a fixed number of frames.

The sample can be executed by running the following:

```python
./python.sh standalone_examples/api/isaacsim.asset.importer.urdf/urdf_import.py
```

### Change Resolution

This sample demonstrates how to change the resolution of the viewport at runtime.

The sample can be executed by running the following:

```python
./python.sh standalone_examples/api/isaacsim.simulation_app/change_resolution.py
```

### Convert Assets to USD

This sample demonstrates how to batch convert OBJ/STL/FBX assets to USD.

To execute it with sample data, run the following:

```python
./python.sh standalone_examples/api/omni.kit.asset_converter/asset_usd_converter.py --folders standalone_examples/data/cube standalone_examples/data/torus
```

The input folders containing OBJ/STL/FBX assets are specified as argument
and it will output in terminal the path to converted USD files.

```python
Converting folder standalone_examples/data/cube...
---Added standalone_examples/data/cube_converted/cube_fbx.usd

Converting folder standalone_examples/data/torus...
---Added standalone_examples/data/torus_converted/torus_stl.usd
```

This sample leverages Python APIs from the [Asset Importer](https://docs.omniverse.nvidia.com/extensions/latest/ext_asset-converter.html "(in Omniverse Extensions)") extension.

The details about the import options can be found [here](https://docs.omniverse.nvidia.com/extensions/latest/ext_asset-importer.html "(in Omniverse Extensions)").

### Livestream

This sample demonstrates how to enable livestreaming when running in native Python.

See [Isaac Sim WebRTC Streaming Client](../installation/manual_livestream_clients.html#isaac-sim-setup-livestream-webrtc) for more information on running the client.

```python
./python.sh standalone_examples/api/isaacsim.simulation_app/livestream.py
```

Note

* Running livestream.py will not have all of the default Isaac Sim extensions enabled. See [enabling additional extensions](#isaac-sim-python-additional-extensions) for more information.

On this page

* [Details: How `python.sh` works](#details-how-python-sh-works)
* [SimulationApp](#simulationapp)
  + [Usage Example:](#usage-example)
  + [Details: How `SimulationApp` works](#details-how-simulationapp-works)
  + [Enabling additional extensions](#enabling-additional-extensions)
* [Standalone Example Scripts](#standalone-example-scripts)
  + [Time Stepping](#time-stepping)
  + [Load USD Stage](#load-usd-stage)
  + [URDF Import](#urdf-import)
  + [Change Resolution](#change-resolution)
  + [Convert Assets to USD](#convert-assets-to-usd)
  + [Livestream](#livestream)

---

### Robots Simulation

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/python_scripting/robots_simulation.html

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
The resulting movements may not respect the robotâs kinematic limitations.

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

---

### Util Snippets

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/python_scripting/util_snippets.html

* [Python Scripting and Tutorials](index.html)
* Util Snippets

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Util Snippets

## Simple Async Task

```python
import asyncio

import omni

# Async task that pauses simulation once the incoming task is complete
async def pause_sim(task):
    done, pending = await asyncio.wait({task})
    if task in done:
        print("Waited until next frame, pausing")
        omni.timeline.get_timeline_interface().pause()

# Start simulation, then wait a frame and run the pause_sim task
omni.timeline.get_timeline_interface().play()
task = asyncio.ensure_future(omni.kit.app.get_app().next_update_async())
asyncio.ensure_future(pause_sim(task))
```

## Get Camera Parameters

The below script show how to get the camera parameters associated with a viewport.

```python
import math

import omni
from omni.syntheticdata import helpers

stage = omni.usd.get_context().get_stage()
viewport_api = omni.kit.viewport.utility.get_active_viewport()
# Set viewport resolution, changes will occur on next frame
viewport_api.set_texture_resolution((512, 512))
# get resolution
width, height = viewport_api.get_texture_resolution()
aspect_ratio = width / height
# get camera prim attached to viewport
camera = stage.GetPrimAtPath(viewport_api.get_active_camera())
focal_length = camera.GetAttribute("focalLength").Get()
horiz_aperture = camera.GetAttribute("horizontalAperture").Get()
vert_aperture = camera.GetAttribute("verticalAperture").Get()
# Pixels are square so we can also do:
# vert_aperture = height / width * horiz_aperture
near, far = camera.GetAttribute("clippingRange").Get()
fov = 2 * math.atan(horiz_aperture / (2 * focal_length))
# helper to compute projection matrix
proj_mat = helpers.get_projection_matrix(fov, aspect_ratio, near, far)

# compute focal point and center
focal_x = height * focal_length / vert_aperture
focal_y = width * focal_length / horiz_aperture
center_x = height * 0.5
center_y = width * 0.5
```

## Rendering

There are three primary APIs you should use when making frequent updates to large amounts of geometry: `UsdGeom.Points`,
`UsdGeom.PointInstancer`, and `DebugDraw`. The different advantages and limitations of each of these methods are explained
below, and can help guide you on which method to use.

### UsdGeom.Points

Use the `UsdGeom.Points` API when the geometry needs to interact with the renderer.
The `UsdGeom.Points` API is the most efficient method to render large amounts of point geometry.

> ```python
> import random
>
> import omni.usd
> from pxr import UsdGeom
>
>
> class Example:
>     def create(self):
>         # Create Point List
>         N = 500
>         self.point_list = [
>             (random.uniform(-2.0, 2.0), random.uniform(-0.1, 0.1), random.uniform(-1.0, 1.0)) for _ in range(N)
>         ]
>         self.sizes = [0.05 for _ in range(N)]
>
>         points_path = "/World/Points"
>         stage = omni.usd.get_context().get_stage()
>         self.points = UsdGeom.Points.Define(stage, points_path)
>         self.points.CreatePointsAttr().Set(self.point_list)
>         self.points.CreateWidthsAttr().Set(self.sizes)
>         self.points.CreateDisplayColorPrimvar("constant").Set([(1, 0, 1)])
>
>     def update(self):
>         # modify the point list
>         for i in range(len(self.point_list)):
>             self.point_list[i] = (random.uniform(-2.0, 2.0), random.uniform(-0.1, 0.1), random.uniform(-1.0, 1.0))
>         # update the points
>         self.points.GetPointsAttr().Set(self.point_list)
>
>
> import asyncio
>
> import omni
>
> example = Example()
> example.create()
>
>
> async def update_points():
>     # Update 10 times, waiting 10 frames between each update
>     for _ in range(10):
>         for _ in range(10):
>             await omni.kit.app.get_app().next_update_async()
>         example.update()
>
>
> asyncio.ensure_future(update_points())
> ```

### UsdGeom.PointInstancer

Use the `UsdGeom.PointInstancer` API when the geometry needs to interact with the physics scene.
The `UsdGeom.PointInstancer` API lets you efficiently replicate an instance of a prim â with all of its USD properties â
and update all instances with a list of positions, colors, and sizes.

See the [PointInstancer Reference](https://openusd.org/release/api/class_usd_geom_point_instancer.html) for more information regarding the PointInstancer API.

Below are code snippets for how to create and update geometry with `UsdGeom.PointInstancer`:

> ```python
> import random
>
> import omni.usd
> from pxr import Gf, UsdGeom
>
>
> class Example:
>     def create(self):
>         # Create Point List
>         N = 500
>         scale = 0.05
>         self.point_list = [
>             (random.uniform(-2.0, 2.0), random.uniform(-0.1, 0.1), random.uniform(-1.0, 1.0)) for _ in range(N)
>         ]
>         self.colors = [(1, 1, 1, 1) for _ in range(N)]
>         self.sizes = [(1.0, 1.0, 1.0) for _ in range(N)]
>
>         # Set up Geometry to be Instanced
>         cube_path = "/World/Cube"
>         stage = omni.usd.get_context().get_stage()
>         cube = UsdGeom.Cube(stage.DefinePrim(cube_path, "Cube"))
>         cube.AddScaleOp().Set(Gf.Vec3d(1, 1, 1) * scale)
>         cube.CreateDisplayColorPrimvar().Set([(0, 1, 1)])
>         # Set up Point Instancer
>
>         instance_path = "/World/PointInstancer"
>         self.point_instancer = UsdGeom.PointInstancer(stage.DefinePrim(instance_path, "PointInstancer"))
>         # Create & Set the Positions Attribute
>         self.positions_attr = self.point_instancer.CreatePositionsAttr()
>         self.positions_attr.Set(self.point_list)
>         self.scale_attr = self.point_instancer.CreateScalesAttr()
>         self.scale_attr.Set(self.sizes)
>         # Set the Instanced Geometry
>         self.point_instancer.CreatePrototypesRel().SetTargets([cube.GetPath()])
>
>         self.proto_indices_attr = self.point_instancer.CreateProtoIndicesAttr()
>         self.proto_indices_attr.Set([0] * len(self.point_list))
>
>     def update(self):
>         # modify the point list
>         for i in range(len(self.point_list)):
>             self.point_list[i] = (random.uniform(-2.0, 2.0), random.uniform(-0.1, 0.1), random.uniform(-1.0, 1.0))
>         # update the points
>         self.positions_attr.Set(self.point_list)
>
>
> import asyncio
>
> import omni
>
> example = Example()
> example.create()
>
>
> async def update_points():
>     # Update 10 times, waiting 10 frames between each update
>     for _ in range(10):
>         for _ in range(10):
>             await omni.kit.app.get_app().next_update_async()
>         example.update()
>
>
> asyncio.ensure_future(update_points())
> ```

### DebugDraw

The [Debug Drawing Extension API](../utilities/debugging/ext_isaacsim_util_debug_draw.html#isaac-debug-draw) API is useful for purely visualizing geometry in the Viewport. Geometry drawn with the `debug_draw_interface`
cannot be rendered and does not interact with the physics scene. However, it is the most performance-efficient method of visualizing geometry.

> See the [API documentation](../py/docs/extsbuild/isaacsim.util.debug_draw/docs/index.html) for complete usage information.

Below are code snippets for how to create and update geometry visualed with `DebugDraw`:

> ```python
> import random
>
> from isaacsim.util.debug_draw import _debug_draw
>
>
> class Example:
>     def create(self):
>         self.draw = _debug_draw.acquire_debug_draw_interface()
>         N = 500
>         self.point_list = [
>             (random.uniform(-2.0, 2.0), random.uniform(-0.1, 0.1), random.uniform(-1.0, 1.0)) for _ in range(N)
>         ]
>         self.color_list = [(random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1), 1) for _ in range(N)]
>         self.size_list = [10.0 for _ in range(N)]
>
>     def update(self):
>         # modify the point list
>         for i in range(len(self.point_list)):
>             self.point_list[i] = (random.uniform(-2.0, 2.0), random.uniform(-0.1, 0.1), random.uniform(-1.0, 1.0))
>
>         # draw the points
>         self.draw.clear_points()
>         self.draw.draw_points(self.point_list, self.color_list, self.size_list)
>
>
> import asyncio
>
> import omni
>
> example = Example()
> example.create()
>
>
> async def update_points():
>     # Update 10 times, waiting 10 frames between each update
>     for _ in range(10):
>         for _ in range(10):
>             await omni.kit.app.get_app().next_update_async()
>         example.update()
>
>
> asyncio.ensure_future(update_points())
> ```

### Rendering Frame Delay

The default rendering pipeline in the app experiences have upto 3 frames in flight to be rendered, which results in higher FPS since the simulation is not blocked until the latest state is rendered completely.

For applications that need the rendered data to correspond to the latest simulation state with no delay, the following experience file should be used `apps/omni.isaac.sim.zero_delay.python.kit`. Below is an example of how to use the experience file in a standlone workflow.

```python
import os

from isaacsim import SimulationApp

SimulationApp({"headless": True}, experience=f"{os.environ['EXP_PATH']}/isaacsim.exp.base.zero_delay.kit")
```

Alternatively, if you would like to use the specific settings instead, you can set them with extra\_args as well:

```python
from isaacsim import SimulationApp

SimulationApp(
    {
        "headless": True,
        "extra_args": [
            "--/app/hydraEngine/waitIdle=1",
            "--/app/updateOrder/checkForHydraRenderComplete=1000",
            "--/exts/isaacsim.ros2.bridge/publish_multithreading_disabled=1",
        ],
    },
)
```

On this page

* [Simple Async Task](#simple-async-task)
* [Get Camera Parameters](#get-camera-parameters)
* [Rendering](#rendering)
  + [UsdGeom.Points](#usdgeom-points)
  + [UsdGeom.PointInstancer](#usdgeom-pointinstancer)
  + [DebugDraw](#debugdraw)
  + [Rendering Frame Delay](#rendering-frame-delay)

---

