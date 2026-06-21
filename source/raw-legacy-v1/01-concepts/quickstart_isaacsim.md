---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/introduction/quickstart_isaacsim.html
title: "Quick Start Isaac Sim"
section: "入门"
module: "01-concepts"
checksum: "b528a9a791c6069d"
fetched: "2026-06-21T13:39:50"
---

* [Quick Tutorials](quickstart_index.html)
* Isaac Sim Basic Usage Tutorial

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Isaac Sim Basic Usage Tutorial

This tutorial covers the basics of Isaac Sim, including navigating the GUI, adding objects to the stage, looking up basic properties of objects, and running simulations.

In this tutorial, you will go from a blank stage to a moving robot using your choice of three different workflows. The purpose of including the three different workflows is to illustrate that Isaac Sim can be used in different ways depending on your needs.

You can review the scripts in both workflows to see how they differ. Comparing and contrasting can help you understand how to perform the exact same tasks:

* The **extension script** can be found in **Window > Examples > Robotics Examples**, then click on **Open Script** on the right upper corner of the browser.
* The **standalone script** can be found in the `<isaac-sim-root-dir>/standalone_examples/tutorials/` folder.

You can try the “hot-reloading” feature out by editing any of the scripts in the Extension examples. Save the file and see the changes reflected immediately without shutting down the simulator.

For a description of workflow concepts, see [Workflows](workflows.html#isaac-sim-app-tutorial-intro-workflows).

## Tutorial

There are three tabs for this tutorial, all three perform the same actions and reach the same outcome. Go through the full page under the same tab to learn about each workflow. Toggle between tabs to compare the different workflows or to perform the tutorial steps for your environment.

* GUI
* Extensions
* Standalone Python

GUI

Launch

1. Launch Isaac Sim from installation root folder.

   Linux

   ```python
   cd ~/isaacsim
   ./isaac-sim.sh
   ```

   Windows

   ```python
   cd C:\isaacsim
   isaac-sim.bat
   ```

   After the simulator is fully loaded, create a new scene:
2. From the top Menu Bar, click **File > New**. The first time you launch Isaac Sim, it may take a five - ten minutes to complete.

Add a Ground Plane

Add a ground plane to the scene:

1. From the top Menu Bar, click **Create > Physics > Ground Plane**.

Add a Light Source

You can add a light source to the scene to illuminate the objects in the scene. If you have a light source in the scene, but no object to reflect the light, the scene will still be dark.

Add a Distant Light source to the scene:

1. From the top Menu Bar, click **Create > Lights > Distant Light**.

Add a Visual Cube

A “visual” cube is a cube with no physics properties attached, for example, no mass, no collision. This cube will not fall under gravity or collide with other objects.

Add a cube to the scene:

1. From the top Menu Bar, click **Create > Shape > Cube**.
2. From the far left side of the UI locate the arrow icon and press **Play**. The cube does not do anything when simulation is running.

Move, Rotate, and Scale the Cube

Use the various gizmos on the left hand side toolbar to manipulate the cube.

1. Press “W” or click on the Move Gizmo to drag and move the cube. You can move it in only one axis by clicking on the arrows and drag, in two axes by clicking on the colored squares and drag, or in all three axes by clicking on the dot in the center of the gizmo and drag.
2. Press “E” or click on the Rotate Gizmo to rotate the cube.
3. Press “R” or click on the Scale Gizmo to scale the cube. You can scale it in one dimension by clicking on the the arrows and drag, two dimensions by clicking on the colored squares and drag, or in all three dimensions by clicking on the circle in the center of the gizmo and drag.
4. Press “esc” to deselect the cube.

For “Move” and “Rotate”, you can indicate if you are maneuvering in local or world coordinates. Click and hold on the gizmos to see the options.

You can make more precise modifications to the cube through its **Property** panel by typing in the exact numbers in the corresponding boxes. Click on the blue square next to the boxes to reset the values to default.

Add Physics and Collision Properties

Common physics properties are mass and inertia matrix, which are the properties that allow the object to fall under gravity. Collision Properties are the properties that allow the object to collide with other objects.

Physics and collision properties can be added separately, so you can have an object that collides with other objects but does not fall under gravity, or falls under gravity but does not collide with other objects. But in many cases, they are added together.

To add physics and collision properties to the cube:

1. Find the object (“/World/Cube”) on the stage tree and highlight it.
2. From the **Property** panel on the bottom right of the Workspace, click on the **Add** button and select **Physics** on the dropdown menu. This will show a list of properties that can be added to the object.
3. Select **Rigid Body with Colliders Preset** to add both physics and collision meshes to the object.
4. Press the **Play** button to see the cube fall under gravity and collide with the ground plane.

Extension

Launch

We will demonstrate the property of an Extension workflow using an existing Extension module called the “Script Editor”. The Script Editor allows the users to interact with the stage using Python. You will see that we will be mostly using the same Python APIs as in the Standalone Python workflow. The difference between the two workflows will become clear when we start to interact with the simulation timeline, especially in the [next tutorial](quickstart_isaacsim_robot.html#isaac-sim-app-intro-quickstart-robot).

Launch a fresh instance of Isaac Sim, go the top Menu Bar and click **Window > Script Editor**.
The code snippets in this tab are sections from one runnable script and should be executed in order.

Add a Ground Plane

To add a ground plane using the interactive Python, copy paste the following snippet in the Script Editor and run it by clicking the **Run** button on the bottom.

```python
import isaacsim.core.experimental.utils.stage as stage_utils
from isaacsim.core.experimental.objects import GroundPlane

stage_utils.create_new_stage()
GroundPlane("/World/GroundPlane", positions=[0, 0, 0])
```

Add a Light Source

You can add a light source to the scene to illuminate the objects in the scene. If you have a light source in the scene, but no object to reflect the light, the scene will still be dark.

1. Open a new tab in the Script Editor (**Tab > Add Tab**).
2. Add a light source by copy-pasting the following snippet in the Script Editor and running it.

```python
from isaacsim.core.experimental.objects import DistantLight

distant_light = DistantLight("/DistantLight")
distant_light.set_intensities(300)
```

Add a Visual Cube

A “visual” cube is a cube with no physics properties attached. No mass, no collision. This cube will not fall under gravity or collide with other objects. You can press **Play** to see that the cube does not do anything when the simulation is running.

1. Open a new tab in the Script Editor (**Tab > Add Tab**).
2. Add two cubes by copy-pasting the following snippet in the Script Editor and run it. We’ll keep one as visual-only, and add physics and collision properties to the other for comparison.

```python
from isaacsim.core.experimental.materials import PreviewSurfaceMaterial
from isaacsim.core.experimental.objects import Cube

yellow_material = PreviewSurfaceMaterial("/Materials/yellow")
yellow_material.set_input_values("diffuseColor", [1.0, 1.0, 0.0])

cyan_material = PreviewSurfaceMaterial("/Materials/cyan")
cyan_material.set_input_values("diffuseColor", [0.0, 1.0, 1.0])

visual_cube = Cube(
    paths="/visual_cube",
    positions=[0, 0.5, 0.5],
    sizes=0.3,
)
visual_cube.apply_visual_materials(yellow_material)

test_cube = Cube(
    paths="/test_cube",
    positions=[0, -0.5, 0.5],
    sizes=0.3,
)
test_cube.apply_visual_materials(cyan_material)
```

Isaac Sim Core API are wrappers for raw USD and physics engine APIs. You can add a visual cube (without physics and color properties) using raw USD API. Notice that the raw USD API is more verbose, but gives you more control over each property.

```python
import omni.usd
from pxr import Gf, UsdGeom

stage = omni.usd.get_context().get_stage()

path = "/visual_cube_usd"
cube_geom = UsdGeom.Cube.Define(stage, path)
cube_prim = stage.GetPrimAtPath(path)
size = 0.5
offset = Gf.Vec3f(1.5, -0.2, 1.0)
cube_geom.CreateSizeAttr(size)
if not cube_prim.HasAttribute("xformOp:translate"):
    UsdGeom.Xformable(cube_prim).AddTranslateOp().Set(offset)
else:
    cube_prim.GetAttribute("xformOp:translate").Set(offset)
```

Add Physics and Collision Properties

Common physics properties are mass and inertia matrix, which are the properties that allow the object to fall under gravity. Collision Properties are the properties that allow the object to collide with other objects.

Physics and collision properties can be added separately, so that you can have an object that collides with other objects but does not fall under gravity, or falls under gravity but does not collide with other objects. But in many cases, they are added together.

With the core APIs, you can add a new cube with physics and collision by creating a cube and then applying rigid body and collision APIs.

```python
from isaacsim.core.experimental.materials import PreviewSurfaceMaterial
from isaacsim.core.experimental.objects import Cube
from isaacsim.core.experimental.prims import GeomPrim, RigidPrim

red_material = PreviewSurfaceMaterial("/Materials/red")
red_material.set_input_values("diffuseColor", [1.0, 0.0, 0.0])

dynamic_cube = Cube(
    paths="/dynamic_cube",
    positions=[0, -1.0, 1.0],
    sizes=0.3,
    scales=[0.6, 0.5, 0.2],
)
dynamic_cube.apply_visual_materials(red_material)
RigidPrim(paths="/dynamic_cube")
GeomPrim(paths="/dynamic_cube", apply_collision_apis=True)
```

Alternatively, if you want to modify an existing object to have physics and collision properties, you can use the following snippet.

```python
from isaacsim.core.experimental.prims import GeomPrim, RigidPrim

RigidPrim(paths="/test_cube")
GeomPrim(paths="/test_cube", apply_collision_apis=True)
```

Click the **Play** button to see the cubes fall under gravity and collide with the ground plane.

Move, Rotate, and Scale the Cube

Moving an object using core API:

```python
from isaacsim.core.experimental.prims import XformPrim

translate_offset = [1.5, 1.2, 1.0]
orientation_offset = [0.7, 0.7, 0, 1]
scale = [1, 1.5, 0.2]

cube_prim = XformPrim(paths="/test_cube")
cube_prim.set_world_poses(translate_offset, orientation_offset)
cube_prim.set_local_scales(scale)
```

Moving an object using raw USD API:

```python
import omni.usd
from pxr import Gf, UsdGeom

stage = omni.usd.get_context().get_stage()
cube_prim = stage.GetPrimAtPath("/visual_cube_usd")
translate_offset = Gf.Vec3f(1.5, -0.2, 1.0)
rotate_offset = Gf.Vec3f(90, -90, 180)  # Note this is in degrees.
scale = Gf.Vec3f(1, 1.5, 0.2)

if not cube_prim.HasAttribute("xformOp:translate"):
    UsdGeom.Xformable(cube_prim).AddTranslateOp().Set(translate_offset)
else:
    cube_prim.GetAttribute("xformOp:translate").Set(translate_offset)

if not cube_prim.HasAttribute("xformOp:rotateXYZ"):
    UsdGeom.Xformable(cube_prim).AddRotateXYZOp().Set(rotate_offset)
else:
    cube_prim.GetAttribute("xformOp:rotateXYZ").Set(rotate_offset)

if not cube_prim.HasAttribute("xformOp:scale"):
    UsdGeom.Xformable(cube_prim).AddScaleOp().Set(scale)
else:
    cube_prim.GetAttribute("xformOp:scale").Set(scale)
```

Standalone Python

Launch

The script that runs Part I, [Isaac Sim Basic Usage Tutorial](#isaac-sim-app-intro-quickstart), is located in `standalone_examples/tutorials/getting_started/getting_started.py`.

To run the script, open a terminal, navigate to the root of the Isaac Sim installation, and run the following command:

Linux

```python
./python.sh standalone_examples/tutorials/getting_started/getting_started.py
```

Windows

```python
python.bat standalone_examples\tutorials\getting_started\getting_started.py
```

Code Explained

**Add a Ground Plane**

The lines inside `getting_started.py` that are relevant to adding a ground plane to the scene are below.

```python
from isaacsim.core.experimental.objects import GroundPlane

GroundPlane("/World/GroundPlane", positions=[0, 0, 0])
```

**Add a Light Source**

You can add a light source to the scene to illuminate the objects in the scene. If you have a light source in the scene, but no object to reflect the light, the scene will still be dark.

The lines inside `getting_started.py` that add a Distant Light are:

```python
from isaacsim.core.experimental.objects import DistantLight

distantLight = DistantLight("/DistantLight")
distantLight.set_intensities(300)
```

**Add a Visual Cube**

A “visual” cube is a cube with no physics properties attached. No mass, no collision. This cube will not fall under gravity or collide with other objects. You can press **Play** to see that the cube does not do anything when the simulation is running.

The lines inside `getting_started.py` that add a visual cube to the scene are:

```python
from isaacsim.core.experimental.materials import PreviewSurfaceMaterial
from isaacsim.core.experimental.objects import Cube

yellow_material = PreviewSurfaceMaterial("/Materials/yellow")
yellow_material.set_input_values("diffuseColor", [1.0, 1.0, 0.0])

visual_cube = Cube(
    paths="/visual_cube",
    positions=[0, 0.5, 1.0],
    sizes=0.3,
)
visual_cube.apply_visual_materials(yellow_material)
```

**Add Physics and Collision Properties**

Common physics properties are mass and inertia matrix, which are the properties that allow the object to fall under gravity. Collision properties are the properties that allow the object to collide with other objects.

Physics and collision properties can be added separately, so you can have an object that collides with other objects but does not fall under gravity, or falls under gravity but does not collide with other objects. But in many cases, they are added together.

With the experimental APIs, you spawn a cube with `Cube`, then apply rigid body and collision by wrapping the prim with `RigidPrim` and `GeomPrim`. The script creates a cube at `/dynamic_cube` and then applies physics and collision to it:

```python
from isaacsim.core.experimental.materials import PreviewSurfaceMaterial
from isaacsim.core.experimental.objects import Cube
from isaacsim.core.experimental.prims import GeomPrim, RigidPrim

cyan_material = PreviewSurfaceMaterial("/Materials/cyan")
cyan_material.set_input_values("diffuseColor", [0.0, 1.0, 1.0])

cube = Cube(
    paths="/dynamic_cube",
    positions=[0, -0.5, 1.5],
    sizes=0.3,
)
cube.apply_visual_materials(cyan_material)
RigidPrim(paths="/dynamic_cube")
GeomPrim(paths="/dynamic_cube", apply_collision_apis=True)
```

Move, Rotate, and Scale the Cube

The snippet below shows the lines that moved the objects in the scene using the core API.

```python
translate_offset = [1.5, 1.2, 1.0]
orientation_offset = [0.7, 0.7, 0, 1]  # quaternion wxyz
scale = [1, 1.5, 0.2]

cube_prim = XformPrim(paths="/visual_cube")
cube_prim.set_world_poses(translate_offset, orientation_offset)
cube_prim.set_local_scales(scale)
```

Save your work.

You can now proceed to [the next tutorial](quickstart_isaacsim_robot.html#isaac-sim-app-intro-quickstart-robot).

On this page

* [Tutorial](#tutorial)