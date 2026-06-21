---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/python_scripting/environment_setup.html
title: "Environment Setup"
section: "Python 脚本"
module: "02-fundamentals-dev"
checksum: "56a11eea1f742059"
fetched: "2026-06-21T14:14:20"
---

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

To verify that collision meshes have been successfully enabled, click the “eye” icon > “Show By Type” >
“Physics Mesh” > “All”. This will show the collision meshes as pink outlines on the objects.

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
The output of the query can be used to access the object’s reference, and its distance from the raycast origin.

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