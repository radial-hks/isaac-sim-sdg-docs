# Sim2Real & UE5 对照

> 数字孪生、Sim2Real 概念框架 + Isaac Sim ↔ UE5 概念映射
> Isaac Sim 版本: 6.0
> 最后组装: 2026-06-21 13:05 UTC
> 来源页数: 15

---

## 来源链接

- [Digital Twin Index](https://docs.isaacsim.omniverse.nvidia.com/latest/digital_twin/index.html)
- [Occupancy Map Generator](https://docs.isaacsim.omniverse.nvidia.com/latest/digital_twin/ext_isaacsim_asset_generator_occupancy_map.html)
- [Static Assets](https://docs.isaacsim.omniverse.nvidia.com/latest/digital_twin/warehouse_logistics/tutorial_static_assets.html)
- [cuOpt Logistics Tutorial](https://docs.isaacsim.omniverse.nvidia.com/latest/digital_twin/warehouse_logistics/logistics_tutorial_cuopt.html)
- [Warehouse Creator](https://docs.isaacsim.omniverse.nvidia.com/latest/digital_twin/warehouse_logistics/ext_omni_warehouse_creator.html)
- [Conveyor Extension](https://docs.isaacsim.omniverse.nvidia.com/latest/digital_twin/warehouse_logistics/ext_isaacsim_asset_gen_conveyor.html)
- [RTSP Camera Streaming](https://docs.isaacsim.omniverse.nvidia.com/latest/digital_twin/rtsp_camera_streaming.html)
- [Digital Twin Troubleshooting](https://docs.isaacsim.omniverse.nvidia.com/latest/digital_twin/troubleshooting.html)
- [Isaac Lab Index](https://docs.isaacsim.omniverse.nvidia.com/latest/isaac_lab_tutorials/index.html)
- [Tutorial Cloner](https://docs.isaacsim.omniverse.nvidia.com/latest/isaac_lab_tutorials/tutorial_cloner.html)
- [Instanceable Assets](https://docs.isaacsim.omniverse.nvidia.com/latest/isaac_lab_tutorials/tutorial_instanceable_assets.html)
- [Policy Deployment](https://docs.isaacsim.omniverse.nvidia.com/latest/isaac_lab_tutorials/tutorial_policy_deployment.html)
- [Isaac Lab Troubleshooting](https://docs.isaacsim.omniverse.nvidia.com/latest/isaac_lab_tutorials/troubleshooting.html)
- [Reference Architecture (re-fetch for Sim2Real context)](https://docs.isaacsim.omniverse.nvidia.com/latest/introduction/reference_architecture.html)
- [Robot Simulation Core Concepts](https://docs.isaacsim.omniverse.nvidia.com/latest/robot_simulation/robot_simulation_core_concepts.html)

---


## Isaac Lab (RL)

### Isaac Lab Index

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/digital_twin/index.html

* Isaac Lab

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Isaac Lab

## Overview

Isaac Lab is the official robot learning framework for Isaac Sim, providing APIs and examples for reinforcement learning,
imitation learning, and more. The framework provides the ability to design tasks in different workflows, including
a modular design to easily and efficiently create robot learning environments, while leveraging the latest simulation capabilities.

Some of its core features include:

* Modular configuration-driven system to easily create and modify environments
* Flexible user-designed workflow for optimized performance
* Suite of robot learning environments for training and evaluation
* Support for different reinforcement learning and imitation learning libraries
* Connection to peripheral devices, such as game-pads and keyboards, for collecting demonstrations
* Ability to augment simulation with custom actuator models for sim-to-real transfer

## Isaac Lab Resources

For more information and documentation for Isaac Lab, see the following external references:

* [Isaac Lab Repository](https://github.com/isaac-sim/IsaacLab)
* [Isaac Lab Documentation](https://isaac-sim.github.io/IsaacLab)

## Suggested Isaac Sim Tutorials

The following set of tutorials details usage of reinforcement learning related components in Isaac Sim.

**Robot Setup**

* [Importing URDF](../importer_exporter/import_urdf.html#isaac-sim-app-tutorial-advanced-import-urdf)
* [Importing MJCF](../importer_exporter/import_mjcf.html#isaac-sim-app-tutorial-advanced-import-mjcf)
* [Simulation Fundamentals](../physics/simulation_fundamentals.html#simulation-fundamentals)

**Deploying Policies**

* [Rigging a Legged Robot for Policy Inference](../robot_setup_tutorials/tutorial_rig_legged_robot.html#isaac-sim-app-tutorial-rig-legged-robot)
* [Policy Deployment](tutorial_policy_deployment.html#isaac-sim-app-tutorial-policy-deployment)
* [Policy Deployment in ROS 2](../ros2_tutorials/tutorial_ros2_rl_controller.html#isaac-sim-app-tutorial-ros2-rl-controller)

**Data Generation**

* [Getting Started with Cloner](tutorial_cloner.html#isaac-sim-app-tutorial-cloner)
* [Instanceable Assets](tutorial_instanceable_assets.html#isaac-sim-app-tutorial-instanceable-assets)

**Python Scripting**

* [Python Scripting](../core_api_tutorials/index.html#isaac-sim-core-api-tutorials-page)

## Troubleshooting

* [Isaac Lab Troubleshooting](troubleshooting.html)

Common Isaac Lab issues and their solutions are documented in the [Isaac Lab Troubleshooting](troubleshooting.html#isaac-sim-isaac-lab-troubleshooting) page. For general simulation troubleshooting, see [Troubleshooting](../overview/troubleshooting.html#isaac-sim-troubleshooting).

## Deprecated Frameworks

Isaac Lab will be replacing previously released frameworks for robot learning and reinforcement learning,
including [IsaacGymEnvs](https://github.com/isaac-sim/IsaacGymEnvs) for the
[Isaac Gym Preview Release](https://developer.nvidia.com/isaac-gym), [OmniIsaacGymEnvs](https://github.com/isaac-sim/OmniIsaacGymEnvs) for
Isaac Sim, and [Orbit](https://isaac-orbit.github.io) for Isaac Sim.

These frameworks are now deprecated in favor of continuing development in Isaac Lab.
We encourage users of these frameworks to migrate your work over to Isaac Lab.
Migration guides are available to support the migration process:

* Migrating from IsaacGymEnvs and Isaac Gym Preview Release: [link](https://isaac-sim.github.io/IsaacLab/main/source/migration/migrating_from_isaacgymenvs.html)
* Migrating from OmniIsaacGymEnvs: [link](https://isaac-sim.github.io/IsaacLab/main/source/migration/migrating_from_omniisaacgymenvs.html)
* Migrating from Orbit: [link](https://isaac-sim.github.io/IsaacLab/main/source/migration/migrating_from_orbit.html)

On this page

* [Overview](#overview)
* [Isaac Lab Resources](#isaac-lab-resources)
* [Suggested Isaac Sim Tutorials](#suggested-isaac-sim-tutorials)
* [Troubleshooting](#troubleshooting)
* [Deprecated Frameworks](#deprecated-frameworks)

---

### Isaac Lab Troubleshooting

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/digital_twin/troubleshooting.html

* [Help & FAQ](../overview/help.html)
* [Troubleshooting](../overview/troubleshooting.html)
* Isaac Lab Troubleshooting

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Isaac Lab Troubleshooting

This page consolidates troubleshooting information for Isaac Lab components in Isaac Sim.

## Common Issues

### Installation Issues

* Make sure you have the correct Python version (3.9+) when setting up Isaac Lab
* If encountering ModuleNotFoundError, ensure all dependencies are installed via pip install -e . in the Isaac Lab repository
* For GPU compatibility issues, verify that your CUDA version matches the requirements for Isaac Lab

### Performance Issues

* For slow training performance, try reducing the number of environments or the complexity of the scene
* Memory issues can be resolved by setting smaller batch sizes or reducing environment complexity
* To improve frame rates during training, consider using fewer sensors or reducing their resolution

### Environment Setup Issues

* If robots fail to initialize, check that the URDF/USD files are correctly specified
* For task initialization failures, ensure your task configuration files are properly formatted
* Make sure reward terms and observations are correctly defined in your environment configurations

### Policy Deployment Issues

* When deploying trained policies, verify the observation space matches the training environment
* For poor policy performance after deployment, check if the simulation parameters match the training settings
* If policy files fail to load, verify they are in the correct format supported by Isaac Lab

On this page

* [Common Issues](#common-issues)
  + [Installation Issues](#installation-issues)
  + [Performance Issues](#performance-issues)
  + [Environment Setup Issues](#environment-setup-issues)
  + [Policy Deployment Issues](#policy-deployment-issues)

---

### Isaac Lab Index

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/isaac_lab_tutorials/index.html

* Isaac Lab

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Isaac Lab

## Overview

Isaac Lab is the official robot learning framework for Isaac Sim, providing APIs and examples for reinforcement learning,
imitation learning, and more. The framework provides the ability to design tasks in different workflows, including
a modular design to easily and efficiently create robot learning environments, while leveraging the latest simulation capabilities.

Some of its core features include:

* Modular configuration-driven system to easily create and modify environments
* Flexible user-designed workflow for optimized performance
* Suite of robot learning environments for training and evaluation
* Support for different reinforcement learning and imitation learning libraries
* Connection to peripheral devices, such as game-pads and keyboards, for collecting demonstrations
* Ability to augment simulation with custom actuator models for sim-to-real transfer

## Isaac Lab Resources

For more information and documentation for Isaac Lab, see the following external references:

* [Isaac Lab Repository](https://github.com/isaac-sim/IsaacLab)
* [Isaac Lab Documentation](https://isaac-sim.github.io/IsaacLab)

## Suggested Isaac Sim Tutorials

The following set of tutorials details usage of reinforcement learning related components in Isaac Sim.

**Robot Setup**

* [Importing URDF](../importer_exporter/import_urdf.html#isaac-sim-app-tutorial-advanced-import-urdf)
* [Importing MJCF](../importer_exporter/import_mjcf.html#isaac-sim-app-tutorial-advanced-import-mjcf)
* [Simulation Fundamentals](../physics/simulation_fundamentals.html#simulation-fundamentals)

**Deploying Policies**

* [Rigging a Legged Robot for Policy Inference](../robot_setup_tutorials/tutorial_rig_legged_robot.html#isaac-sim-app-tutorial-rig-legged-robot)
* [Policy Deployment](tutorial_policy_deployment.html#isaac-sim-app-tutorial-policy-deployment)
* [Policy Deployment in ROS 2](../ros2_tutorials/tutorial_ros2_rl_controller.html#isaac-sim-app-tutorial-ros2-rl-controller)

**Data Generation**

* [Getting Started with Cloner](tutorial_cloner.html#isaac-sim-app-tutorial-cloner)
* [Instanceable Assets](tutorial_instanceable_assets.html#isaac-sim-app-tutorial-instanceable-assets)

**Python Scripting**

* [Python Scripting](../core_api_tutorials/index.html#isaac-sim-core-api-tutorials-page)

## Troubleshooting

* [Isaac Lab Troubleshooting](troubleshooting.html)

Common Isaac Lab issues and their solutions are documented in the [Isaac Lab Troubleshooting](troubleshooting.html#isaac-sim-isaac-lab-troubleshooting) page. For general simulation troubleshooting, see [Troubleshooting](../overview/troubleshooting.html#isaac-sim-troubleshooting).

## Deprecated Frameworks

Isaac Lab will be replacing previously released frameworks for robot learning and reinforcement learning,
including [IsaacGymEnvs](https://github.com/isaac-sim/IsaacGymEnvs) for the
[Isaac Gym Preview Release](https://developer.nvidia.com/isaac-gym), [OmniIsaacGymEnvs](https://github.com/isaac-sim/OmniIsaacGymEnvs) for
Isaac Sim, and [Orbit](https://isaac-orbit.github.io) for Isaac Sim.

These frameworks are now deprecated in favor of continuing development in Isaac Lab.
We encourage users of these frameworks to migrate your work over to Isaac Lab.
Migration guides are available to support the migration process:

* Migrating from IsaacGymEnvs and Isaac Gym Preview Release: [link](https://isaac-sim.github.io/IsaacLab/main/source/migration/migrating_from_isaacgymenvs.html)
* Migrating from OmniIsaacGymEnvs: [link](https://isaac-sim.github.io/IsaacLab/main/source/migration/migrating_from_omniisaacgymenvs.html)
* Migrating from Orbit: [link](https://isaac-sim.github.io/IsaacLab/main/source/migration/migrating_from_orbit.html)

On this page

* [Overview](#overview)
* [Isaac Lab Resources](#isaac-lab-resources)
* [Suggested Isaac Sim Tutorials](#suggested-isaac-sim-tutorials)
* [Troubleshooting](#troubleshooting)
* [Deprecated Frameworks](#deprecated-frameworks)

---

### Tutorial Cloner

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/isaac_lab_tutorials/tutorial_cloner.html

* [Isaac Lab](index.html)
* Getting Started with Cloner

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Getting Started with Cloner

Training reinforcement learning policies can often benefit from collecting trajectories from vectorized copies of environments performing the same task. The Cloner interface is designed to simplify the environment design process for such a scene by providing APIs that allow users to clone a given environment as many times as desired.

In addition to providing cloning functionality, the Cloner interface also provides utilities to generate target paths, automatically compute target transforms, as well as filtering out collisions between clones.

## Learning Objectives

In this tutorial, we will walk through the Cloner interface:

1. Set up an example using the Cloner class
2. Set up an example using the GridCloner class
3. Use APIs from isaacsim.core.api to access cloned objects
4. Understand advanced cloning with physics replication and additional parameters

*10-15 Minute Tutorial*

## Getting Started

We will first launch Isaac Sim and enable the Cloner extension. Open the Extensions window from the UI by navigating to Window > Extensions from the top menu bar. Find the Isaac Sim Cloner extension, or isaacsim.core.cloner and enable the extension via the toggle switch on the right side of the extension name.

Next, open the Script Editor window from the UI by navigating to Window > Script Editor from the top menu bar. All example code in this tutorial can be pasted into the Script Editor window and executed by clicking on Run.

## Introduction to Cloner

Please make sure isaacsim.core.cloner is enabled from the Extensions window before running the snippets.

Letâs first start with a simple use case of the Cloner interface. In this example, we will create a scene with 4 cubes.

```python
from isaacsim.core.cloner import Cloner  # import Cloner interface
from isaacsim.core.experimental.utils.stage import get_current_stage
from pxr import UsdGeom

# create our base environment with one cube
base_env_path = "/World/Cube_0"
UsdGeom.Cube.Define(get_current_stage(), base_env_path)

# create a Cloner instance
cloner = Cloner()

# generate 4 paths that begin with "/World/Cube" - path will be appended with _{index}
target_paths = cloner.generate_paths("/World/Cube", 4)

# clone the cube at target paths
cloner.clone(source_prim_path="/World/Cube_0", prim_paths=target_paths)
```

We should now have 4 cubes in our stage: â/World/Cube\_0â, â/World/Cube\_1â, â/World/Cube\_2â, â/World/Cube\_3â. But you may have noticed that the cubes have all been created at the same position.

We can add a transform to each cube, simply replace the last line of the previous code with the following:

```python
import numpy as np

cube_positions = np.array([[0, 0, 0], [3, 0, 0], [6, 0, 0], [9, 0, 0]])

# clone the cube at target paths at specified positions
cloner.clone(source_prim_path="/World/Cube_0", prim_paths=target_paths, positions=cube_positions)
```

It is also possible to specify the orientations of each clone by passing in an orientations argument, which should also be a np.ndarray.

## Grid Cloner

Grid Cloner is a specialized Cloner class that automatically places clones in a grid, without requiring pre-computed translations and orientations from the user.

To use the Grid Cloner, we will need to specify the spacing we would like between each clone at initialization.

```python
from isaacsim.core.cloner import GridCloner  # import GridCloner interface
from isaacsim.core.experimental.utils.stage import get_current_stage
from pxr import UsdGeom

# create our base environment with one cube
base_env_path = "/World/Cube_0"
UsdGeom.Cube.Define(get_current_stage(), base_env_path)

# create a GridCloner instance
cloner = GridCloner(spacing=3)

# generate 4 paths that begin with "/World/Cube" - path will be appended with _{index}
target_paths = cloner.generate_paths("/World/Cube", 4)

# clone the cube at target paths
cloner.clone(source_prim_path="/World/Cube_0", prim_paths=target_paths)
```

Now we have a scene with 4 cubes placed in a grid!

## Accessing Cloned Objects

Now that we have created our scene with the Cloner interface, we can access states for the cloned objects using APIs from isaacsim.core.experimental.prims. These APIs allow us to collect and apply data as vectorized tensors to all or a subset of objects at once, avoiding iterating through objects in loops.

We will show a simple example of retrieving the global transforms of all of the boxes in the scene, as well as setting a new translation on the boxes.

```python
# import the XformPrim interface from isaacsim.core.experimental.prims for APIs for Xform prims
import numpy as np
from isaacsim.core.experimental.prims import XformPrim

# retrieve a prim wrapping all 4 boxes by using a regex expression that matches the prim paths for all boxes
boxes = XformPrim("/World/Cube_.*")

# retrieve the global transforms of all boxes
#   - positions will be a vector of shape (4, 3) for X, Y, Z axes of translation
#   - orientations will be a vector of shape (4, 4) for W, X, Y, Z axes of quaternion
positions, orientations = boxes.get_world_poses()
positions = positions.numpy()
orientations = orientations.numpy()

# increase positions on the Z axis to move boxes up by 1.5 units
positions[:, 2] += 1.5
# apply the new positions
boxes.set_world_poses(positions, orientations)
```

## Physics Replication

The cloning process can take advantage of faster physics parsing by replicating physics directly in PhysX, avoiding copying of USD physics properties. This feature can be enabled by passing in a new parameter replicate\_physics=True when cloning objects in the scene. Note that to use this feature, the user must also specify some additional parameters: base\_env\_paths and root\_path. base\_env\_paths points to the ancestry prim of all clones and root\_path specifies the prefix of each target clone path before the index. This also imposes the limitation that all target clone paths must be appended by an incremental index. If both define\_base\_env() and generate\_paths() APIs have already been called before cloning, the user can avoid specifying base\_env\_paths and root\_path parameters as the information has already been provided to the Cloner class.

```python
cloner.clone(
    source_prim_path="/World/Ants/Ant_0",
    prim_paths=target_paths,
    positions=position_offsets,
    replicate_physics=True,
    base_env_path="/World/Ants",
    root_path="/World/Ants/Ant_",
)
```

A full example using physics replication can be found at standalone\_examples/api/isaacsim.core.cloner/cloner\_ants.py.

There are currently some features that are not supported by physics replication. For example, runtime modification of shape properties are not allowed on prims that have been created using physics replication. For scenes that require randomization or modification of shape properties (such as materials, friction, restitution, etc.) at run time, please do not enable physics replication when cloning objects.

## Additional Parameters

In addition to physics replication, the Cloner also provides an option to copy from the source prim. This flag can be set with the copy\_from\_source argument.

```python
cloner.clone(
    source_prim_path="/World/Ants/Ant_0",
    prim_paths=target_paths,
    positions=position_offsets,
    replicate_physics=True,
    base_env_path="/World/Ants",
    root_path="/World/Ants/Ant_",
    copy_from_source=True,
)
```

By default, copy\_from\_source is set to False, in which case the cloned prims will be defined as [USD Inherits](https://openusd.org/release/api/class_usd_inherits.html) of the source prim. The cloning process will be faster when USD Inherits are used for cloning. However, any changes that are made to the source prim *after* cloning will also reflect in the cloned prims.

If this behavior is undesired, please set copy\_from\_source to True. When copy\_from\_source is set to True, the cloned prims will be defined as **copies** of the source prim. After cloning, each cloned prim will be an individual entity and any changes in the source prim **will not** be reflected on the cloned prims. This setting can be useful in cases where cloned environments are not designed to be identical.

## Summary

This tutorial covered the following topics:

1. How to use the Cloner interface
2. How to use the GridCloner interface
3. How to access states of cloned objects with isaacsim.core.api APIs
4. Advanced cloning with physics replication and additional parameters

### Next Steps

Continue on to the next tutorial in our Reinforcement Learning Tutorials series, [Instanceable Assets](tutorial_instanceable_assets.html#isaac-sim-app-tutorial-instanceable-assets), to learn about instanceable assets for improving memory efficiency.

On this page

* [Learning Objectives](#learning-objectives)
* [Getting Started](#getting-started)
* [Introduction to Cloner](#introduction-to-cloner)
* [Grid Cloner](#grid-cloner)
* [Accessing Cloned Objects](#accessing-cloned-objects)
* [Physics Replication](#physics-replication)
* [Additional Parameters](#additional-parameters)
* [Summary](#summary)
  + [Next Steps](#next-steps)

---

### Instanceable Assets

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/isaac_lab_tutorials/tutorial_instanceable_assets.html

* [Isaac Lab](index.html)
* Instanceable Assets

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Instanceable Assets

Reinforcement learning often requires training in large simulation scenes with multiple clones of the same robots. As we add more and more robots into the simulation environment, the memory consumption also increases for each additional set of robot and mesh assets added. To reduce memory consumption, we can take advantage of USDâs [Scenegraph Instancing](https://graphics.pixar.com/usd/dev/api/_usd__page__scenegraph_instancing.html) functionality to mark common meshes shared by different copies of the same robots as instanceable.

By doing so, each copy of the robot will reference a single copy of meshes, avoiding the need to create multiple copies of the same meshes in the scene, thus reducing memory usage in the overall simulation environment.

## Learning Objectives

In this tutorial, we will show how to create instanceable assets in Isaac Sim. We will

1. Explain requirements for making assets instanceable
2. Use the URDF and MJCF importers to create instanceable assets
3. Show utility methods to convert existing assets to instanceable assets

*10-15 Minute Tutorial*

## Getting Started

* Please refer to USD Documentation on [Scenegraph Instancing](https://graphics.pixar.com/usd/dev/api/_usd__page__scenegraph_instancing.html) for more details on instancing.
* Please refer to [Tutorial: Import URDF](../importer_exporter/import_urdf.html#isaac-sim-app-tutorial-advanced-import-urdf) and [Tutorial: Import MJCF](../importer_exporter/import_mjcf.html#isaac-sim-app-tutorial-advanced-import-mjcf) for more details on importer functionalities.

## Hierarchy Requirement for Instanceable Assets

USD prohibits modifying properties of prims on descendants of instanced prims. Therefore, we generally only perform instancing on mesh prims for robot assets, since properties on meshes will not differ across different environments during simulation. However, the transforms of the meshes may be different during simulation when robots in each environment are being moved in varying ways. Thus, we have to define the topology of our robot hierarchy in a specific structure in the asset tree definition in order for the instanceable flag to take action.

To mark any mesh or primitive geometry prim in the asset as instanceable, the mesh prim requires a parent Xform prim to be present, which will be used to add a reference to a master USD file containing definition of the mesh prim.

For example, the following definition cannot be marked instanceable:

```python
World
  |_ Robot
       |_ Collisions
               |_ Sphere
               |_ Box
```

Instead, it will have to be modified to:

```python
World
  |_ Robot
       |_ Collisions
               |_ Sphere_Xform
               |      |_ Sphere
               |_ Box_Xform
                      |_ Box
```

Any references that exist on the original Sphere and Box prims would have to be moved to Sphere\_Xform and Box\_Xform prims.

## Using URDF and MJCF Importers

Isaac Sim provides two importers - URDF and MJCF - for converting robot assets to USD format to be used in Isaac Sim. Both importers support the option to import robot assets directly as instanceable assets. By selecting this option, imported assets will be split into two separate USD files that follow the above hierarchy definition. Any mesh data will be written to an USD stage to be referenced by the main USD stage, which contains the main robot definition.

To use the Instanceable option in the importers, first check the Create Instanceable Asset option. Then, specify a file path to indicate the location for saving the mesh data in the Instanceable USD Path textbox. This will default to ./instanceable\_meshes.usd, which will generate a file instanceable\_meshes.usd that is saved to the current directory.

Once the asset is imported with these options enabled, you will see the robot definition in the stage - we will refer to this stage as the master stage. If we expand the robot hierarchy in the Stage, we will notice that the parent prims that have mesh descendants have been marked as Instanceable and they reference a prim in our Instanceable USD Path USD file. We are also no longer able to modify attributes of descendant meshes.

To add our instanced asset into a new stage, we will simply need to add our master USD file.

## Modifying Existing Assets

Due to limitations of the topology requirement for making assets instanceable, it is not as straightforward to convert existing non-instanceable assets to become instanceable. Here, we will try to provide a few small utility methods to help make the process simpler.

All utilities should be copied into and run from the script editor, which can be opened from Window > Script Editor.

First, we need to make sure our existing asset follows the hierarchy constraint defined above, where all mesh prims have a parent XForm prim present that can be used to mark the prim as instanceable. To help with the process of creating new parent prims, we provide a utility method create\_parent\_xforms() below to automatically insert a new Xform prim as a parent of every mesh prim in the stage.

```python
import omni.client
import omni.usd
from pxr import Sdf, UsdGeom

def create_parent_xforms(asset_usd_path, source_prim_path, save_as_path=None):
    """Adds a new UsdGeom.Xform prim for each Mesh/Geometry prim under source_prim_path.
    Moves material assignment to new parent prim if any exists on the Mesh/Geometry prim.

    Args:
        asset_usd_path (str): USD file path for asset
        source_prim_path (str): USD path of root prim
        save_as_path (str): USD file path for modified USD stage. Defaults to None, will save in same file.
    """
    omni.usd.get_context().open_stage(asset_usd_path)
    stage = omni.usd.get_context().get_stage()

    prims = [stage.GetPrimAtPath(source_prim_path)]
    edits = Sdf.BatchNamespaceEdit()
    while len(prims) > 0:
        prim = prims.pop(0)
        print(prim)
        if prim.GetTypeName() in ["Mesh", "Capsule", "Sphere", "Box"]:
            new_xform = UsdGeom.Xform.Define(stage, str(prim.GetPath()) + "_xform")
            print(prim, new_xform)
            edits.Add(Sdf.NamespaceEdit.Reparent(prim.GetPath(), new_xform.GetPath(), 0))
            continue

        children_prims = prim.GetChildren()
        prims = prims + children_prims

    stage.GetRootLayer().Apply(edits)

    if save_as_path is None:
        omni.usd.get_context().save_stage()
    else:
        omni.usd.get_context().save_as_stage(save_as_path)
```

This method can be run on an existing non-instanced USD file for an asset from the script editor, where:

* asset\_usd\_path is the file path to the current existing USD asset
* source\_prim\_path is the USD prim path to the root prim of the asset
* save\_as\_path is a different file path to same the modified asset to. This can be left unspecified to overwrite the existing file.

```python
create_parent_xforms(asset_usd_path=ASSET_USD_PATH, source_prim_path=SOURCE_PRIM_PATH, save_as_path=SAVE_AS_PATH)
```

It is worth noting that any [USD Relationships](https://graphics.pixar.com/usd/dev/api/class_usd_relationship.html) on the referenced meshes will be removed. This is because those USD Relationships originally have targets set to prims in the original prim that may no longer be valid and hence cannot be accessed from the new stage. Common examples of USD Relationships that could exist on the meshes are visual materials, physics materials, and filtered collision pairs. Therefore, it is recommended to set these USD Relationships on the meshesâ parent Xforms instead of the meshes themselves.

The above method can also be run as part of an overall conversion process, which is defined in the utility below. This utility will first insert new parent prims if create\_xforms=True is specified, and generate a new USD file that is used for referencing. It will then traverse through the asset tree and mark the parent prim of any mesh or primitive type prims as instanceable, along with inserting a reference to the mesh USD stage.

```python
def convert_asset_instanceable(asset_usd_path, source_prim_path, save_as_path=None, create_xforms=True):
    """Makes all mesh/geometry prims instanceable.
    Can optionally add UsdGeom.Xform prim as parent for all mesh/geometry prims.
    Makes a copy of the asset USD file, which will be used for referencing.
    Updates asset file to convert all parent prims of mesh/geometry prims to reference cloned USD file.

    Args:
        asset_usd_path (str): USD file path for asset
        source_prim_path (str): USD path of root prim
        save_as_path (str): USD file path for modified USD stage. Defaults to None, will save in same file.
        create_xforms (bool): Whether to add new UsdGeom.Xform prims to mesh/geometry prims.
    """

    if create_xforms:
        create_parent_xforms(asset_usd_path, source_prim_path, save_as_path)
        asset_usd_path = save_as_path

    instance_usd_path = ".".join(asset_usd_path.split(".")[:-1]) + "_meshes.usd"
    omni.client.copy(asset_usd_path, instance_usd_path)
    omni.usd.get_context().open_stage(asset_usd_path)
    stage = omni.usd.get_context().get_stage()

    prims = [stage.GetPrimAtPath(source_prim_path)]
    while len(prims) > 0:
        prim = prims.pop(0)
        if prim:
            if prim.GetTypeName() in ["Mesh", "Capsule", "Sphere", "Box"]:
                parent_prim = prim.GetParent()
                if parent_prim and not parent_prim.IsInstance():
                    parent_prim.GetReferences().AddReference(
                        assetPath=instance_usd_path, primPath=str(parent_prim.GetPath())
                    )
                    parent_prim.SetInstanceable(True)
                    continue

            children_prims = prim.GetChildren()
            prims = prims + children_prims

    if save_as_path is None:
        omni.usd.get_context().save_stage()
    else:
        omni.usd.get_context().save_as_stage(save_as_path)
```

## Summary

This tutorial covered the following topics:

1. Requirements for creating instanceable assets
2. Using the URDF and MJCF Importers to create instanceable assets
3. Making existing assets instanceable

On this page

* [Learning Objectives](#learning-objectives)
* [Getting Started](#getting-started)
* [Hierarchy Requirement for Instanceable Assets](#hierarchy-requirement-for-instanceable-assets)
* [Using URDF and MJCF Importers](#using-urdf-and-mjcf-importers)
* [Modifying Existing Assets](#modifying-existing-assets)
* [Summary](#summary)

---

### Policy Deployment

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/isaac_lab_tutorials/tutorial_policy_deployment.html

* [Isaac Lab](index.html)
* Deploying Policies in Isaac Sim

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Deploying Policies in Isaac Sim

The objective of this tutorial is to explain the process of deploying a policy trained in Isaac Lab by going through an example and exploring robot definition files.

There are many use cases in which you might want to deploy your policy in Isaac Sim; such as enabling robots to accomplish more complex locomotion, testing and integrating the policy with other stacks such as navigation and localization in simulated environments, and interfacing it using with existing bridges such as ROS 2.

## Learning Objectives

In this tutorial, you will walk through the policy based robot examples:

1. H1 and Spot flat terrain policy controller demo
2. Training and exporting policies in Isaac Lab
3. Reading the environment parameter file from Isaac Lab
4. Robot definition class
5. Position to torque conversion
6. Debugging tips
7. Sim to Real deployment

## Demos

First activate **Windows** > **Examples** > **Robotics Examples** which will open the `Robotics Examples` tab.

### Unitree H1 Humanoid Example

1. The Unitree H1 humanoid example can be accessed by creating a empty stage.
2. Open the example using **Robotics Examples** > **POLICY** > **Humanoid**.
3. Press **LOAD** to open the scene.

This example uses the H1 Flat Terrain Policy trained in Isaac Lab to control the humanoidâs locomotion.

Controls:

* Forward: UP ARROW / NUM 8
* Turn Left: LEFT ARROW / NUM 4
* Turn Right: RIGHT ARROW / NUM 6

### Boston Dynamics Spot Quadruped Example

1. The Boston Dynamics Spot quadruped example can be accessed by creating a empty stage.
2. Open the example using **Robotics Examples** > **POLICY** > **Quadruped**.
3. Press **LOAD** to open the scene.

This example uses the Spot Flat Terrain Policy trained in Isaac Lab to control the quadrupedâs locomotion.

Controls:

* Forward: UP ARROW / NUM 8
* Backward: BACK ARROW / NUM 2
* Move Left: LEFT ARROW / NUM 4
* Move Right: RIGHT ARROW / NUM 6
* Turn Left: N / NUM 7
* Turn Right: M / NUM 9

Note

See [isaac sim policy example extension document](../robot_simulation/ext_isaacsim_robot_policy_example.html#isaac-sim-policy-example) for standalone example workflow and the policy files used in the examples.

## Training and Exporting Policies in Isaac Lab

### Training

Training the policy from Isaac Lab is the first step to deploying the policy.
Consult the [Isaac Lab tutorials](https://isaac-sim.github.io/IsaacLab/main/source/tutorials/03_envs/run_rl_training.html) for training an existing or custom policy.

The policies trained used in the examples above are Isaac-Velocity-Flat-H1-v0 for the Unitree H1 humanoid and Isaac-Velocity-Flat-Spot-v0 for the Boston Dynamics Spot robot.

Note

For example, in Isaac Lab 2.0, use the following command to train the H1 flat terrain policy:

```python
./isaaclab.sh -p scripts/reinforcement_learning/rsl_rl/train.py --task Isaac-Velocity-Flat-H1-v0 --headless
```

### Exporting

Policies trained using `RSL_rl`, the policies can be exported using the `scripts/reinforcement_learning/rsl_rl/play.py` inside the Isaac Lab workspace. The exported files are generated in the `exported` folder.

It is also possible to inference using a policy trained in a different framework or with an iteration snapshot, however additional data such as neural network structure may be required.
Follow the documentation of your desired framework for more information.

Note

For example, in Isaac Lab 2.0, use the following command to export the H1 flat terrain policy:

```python
./isaaclab.sh -p scripts/reinforcement_learning/rsl_rl/play.py --task Isaac-Velocity-Flat-H1-v0 --num_envs 32
```

Note

The trained policy files used in the examples are available to download [here](../robot_simulation/ext_isaacsim_robot_policy_example.html#isaac-sim-policy-example-policies).

## Understanding the Environment Parameter File

The `agent.yaml` and `env.yaml` are generated with trained policies to describe the policy configurations and they are located in the `logs/rsl_rl/<task_name>/<time>/params/` folder.

* `agent.yaml` describes the neural network parameters.
* `env.yaml` describes the environment and robot configurations.

The below snippets are taken from Isaac-Velocity-Flat-H1-v0.

### Simulation Setup

```python
sim:
physics_prim_path: /physicsScene
dt: 0.005
render_interval: 4
gravity: !!python/tuple
- 0.0
- 0.0
- -9.81
enable_scene_query_support: false
use_fabric: true
disable_contact_processing: true
use_gpu_pipeline: true
device: cuda:0
```

The first snippet describes the simulation environment, the simulation physics is required to run at 0.005s (200hz), with gravity pointing downwards at 9.81m/s^2

### Robot Setup

The `scene:robot:init_state` section describes the robotâs initial position, orientation, velocity, as well as default joint position and velocity.

```python
init_state:
  pos: !!python/tuple
  - 0.0
  - 0.0
  - 1.05
  rot: &id003 !!python/tuple
  - 1.0
  - 0.0
  - 0.0
  - 0.0
  lin_vel: &id001 !!python/tuple
  - 0.0
  - 0.0
  - 0.0
  ang_vel: *id001
  joint_pos:
    .*_hip_yaw: 0.0
    .*_hip_roll: 0.0
    .*_hip_pitch: -0.28
    .*_knee: 0.79
    .*_ankle: -0.52
    torso: 0.0
    .*_shoulder_pitch: 0.28
    .*_shoulder_roll: 0.0
    .*_shoulder_yaw: 0.0
    .*_elbow: 0.52
  joint_vel:
    .*: 0.0
```

The `scene:robot:init_state:actuators` section below describes the robot joint properties such as effort and velocity limit, stiffness and dampening.

```python
actuators:
  legs:
    class_type: omni.isaac.lab.actuators.actuator_pd:ImplicitActuator
    joint_names_expr:
    - .*_hip_yaw
    - .*_hip_roll
    - .*_hip_pitch
    - .*_knee
    - torso
    effort_limit: 300
    velocity_limit: 100.0
    stiffness:
      .*_hip_yaw: 150.0
      .*_hip_roll: 150.0
      .*_hip_pitch: 200.0
      .*_knee: 200.0
      torso: 200.0
    damping:
      .*_hip_yaw: 5.0
      .*_hip_roll: 5.0
      .*_hip_pitch: 5.0
      .*_knee: 5.0
      torso: 5.0
    armature: null
    friction: null
```

### Observations Parameters

The observation parameters describes the observations required by the policy, as well as scale or clipping factors that need to be applied to the observation.

```python
observations:
    policy:
        concatenate_terms: true
        enable_corruption: true
        base_lin_vel:
        func: omni.isaac.lab.envs.mdp.observations:base_lin_vel
        params: {}
        noise:
            func: omni.isaac.lab.utils.noise.noise_model:uniform_noise
            operation: add
            n_min: -0.1
            n_max: 0.1
        clip: null
        scale: null
```

### Actions Parameters

The actions parameters describes the action outputted by the policy, as well as scaling factors and offsets that need to be applied to the actions.

```python
actions:
    joint_pos:
        class_type: omni.isaac.lab.envs.mdp.actions.joint_actions:JointPositionAction
        asset_name: robot
        debug_vis: false
        joint_names:
        - .*
        scale: 0.5
        offset: 0.0
        use_default_offset: true
```

### Commands Parameters

Finally, the command section describers the type of command for the policy, as well as acceptable command ranges for the policy.

```python
commands:
    base_velocity:
        class_type: omni.isaac.lab.envs.mdp.commands.velocity_command:UniformVelocityCommand
        resampling_time_range: !!python/tuple
        - 10.0
        - 10.0
        debug_vis: true
        asset_name: robot
        heading_command: true
        heading_control_stiffness: 0.5
        rel_standing_envs: 0.02
        rel_heading_envs: 1.0
        ranges:
            lin_vel_x: !!python/tuple
            - 0.0
            - 1.0
            lin_vel_y: *id006
            ang_vel_z: !!python/tuple
            - -1.0
            - 1.0
            heading: !!python/tuple
            - -3.141592653589793
            - 3.141592653589793
```

## Policy Controller Class

The robot definition class defines the robot prim, imports the robot policy, sets up the robot configurations, builds the observation tensor, and finally applies the policy control action to the robot.

### Constructor

The Constructor will spawn the robot USD, and create a single articulation object for controlling the robot.

### Load Policy

This class will load in the policy file and the corresponding environment file which the policy controller will use to set up the Isaac Sim environment.

### Initialize

The initialize function must be called once after simulation started. The purpose of this function is to match the robot configurations to the policy, by setting the robot effort mode, control mode, joint gains, joint max effort, joint max velocity, and articulation root.

### `_set_articulation_prop`

This function parses the articulation root property and set these properties to the robot.

### `_compute_action`

This function will compute the action from the observation.

### `_compute_observation`

This function must be overload by the inherited class and it is called by `advance()` during every physics step. The purpose of this function is to create an observation tensor in the format expected by the policy.
For example, the code snippet below creates the observation tensor for the H1 flat terrain policy.

```python
obs = torch.zeros(69, device=torch.device(str(self.robot._device)))
# Base lin vel
obs[:3] = lin_vel_b.squeeze()
# Base ang vel
obs[3:6] = ang_vel_b.squeeze()
# Gravity
obs[6:9] = gravity_b.squeeze()
# Command
obs[9:12] = command
# Joint states
current_joint_pos = wp.to_torch(self.robot.get_dof_positions())
current_joint_vel = wp.to_torch(self.robot.get_dof_velocities())
obs[12:31] = current_joint_pos - self.default_pos
obs[31:50] = current_joint_vel - self.default_vel
# Previous Action
obs[50:69] = self._previous_action
```

Note

Remember to multiply the observation terms by the observation scale specified in the `env.yaml`.

### Forward

This function must be overload by the inherited class and is called every physics step to generate control action for the robot.
For example, the code snippet below creates the controls for the H1 flat terrain policy.

```python
if self._policy_counter % self._decimation == 0:
    obs = self._compute_observation(command)
    self.action = self._compute_action(obs)
    self._previous_action = self.action.clone()

self.robot.set_dof_position_targets(positions=wp.from_torch(self.default_pos + (self.action * self._action_scale)))
self._policy_counter += 1
```

Note

* The policy does not need to be called every step, refer to the decimation parameter in `env.yaml`.
* Remember to multiply the action output by the action scale specified in `env.yaml`.

Warning

For position based controls, do not use `set_joint_position()` as that will teleport the joint to the desired position.

## Position to Torque Controls

Some robots may require torque control as output. If the policy generates position as an output, then you must convert position to torque. There are many ways to do this, here an actuator network is used to convert position to torque.

The actuator network class is defined in `source/extensions/isaacsim.robot.policy.examples/isaacsim/robot/policy/examples/utils/actuator_network.py`.
The actuator network policy for the Anymal robot is stored on the Content Browser at *SAMPLES* > *POLICY* > *ANYMAL\_POLICIES*

### Import Policy

For our LSTMSeaNetwork implementation, the policy file is loaded into the helper actuator network using the snippet below from the Anymal Flat Terrain Policy class:

```python
def initialize(self, physics_sim_view=None) -> None:
    """
    Initialize the articulation interface and set up drive mode.

    Args:
        physics_sim_view: The physics simulation view
    """
    super().initialize(physics_sim_view=physics_sim_view, control_mode="effort")

    # Actuator network
    assets_root_path = get_assets_root_path()
    file_content = omni.client.read_file(
        assets_root_path + "/Isaac/IsaacLab/ActuatorNets/ANYbotics/anydrive_3_lstm_jit.pt"
    )[2]
    file = io.BytesIO(memoryview(file_content).tobytes())
    self._actuator_network = LstmSeaNetwork()
    self._actuator_network.setup(file, self.default_pos)
    self._actuator_network.reset()
```

### Run the Actuator Network

In the advance function, insert the position outputs from the locomotion policy into the actuator network and apply the torque to the robot using the snippet below:

```python
current_joint_pos = self.get_joint_positions()
current_joint_vel = self.get_joint_velocities()

joint_torques, _ = self._actuator_network.compute_torques(
    current_joint_pos, current_joint_vel, self._action_scale * self.action
)

self.set_joint_efforts(joint_torques)
```

## Debugging Tips

If your robot doesnât work right away, you can use the following tips to start debugging:

### Verify Your Policy

You can start by verifying that your policy is working properly by [playing it in Isaac Lab.](https://isaac-sim.github.io/IsaacLab/main/source/tutorials/03_envs/run_rl_training.html#playing-the-trained-agent)

Remember to use the correct `play.py` for your workflow and select the correct task.

### Verify the Robot Joint Properties

#### Robot Joint Order

If the policy is working on Isaac Lab, then you should verify is the joint order of the robot, joint properties, and default joint positions.

To see the joint order, open your asset USD, create an articulation with the robot prim, start the simulation, initialize articulation, and call the `dof_names` function.

```python
# Open your USD and PLAY the simulation before running this snippet
# Change the path to the robot you want to inspect
prim = Articulation(paths="/World/Robot")
print(str(prim.dof_names))
```

Print out the `dof_names` for both the Isaac Sim asset and the asset you used to train in Isaac Lab, make sure that the names and orders match exactly.

The ANYmal robot below has control commands in the wrong order, as a result the robot is falling over.

#### Default Joint Position

After you have the joint positions, verify that your default joint positions are inserted correctly. If the joint positions are incorrect, the robot joints will not go to the correct position.

For example, in the video below, the ankle joint was set incorrectly and the H1 humanoid was tip toeing, doing a âmoonwalkâ.

#### Robot Joint Properties

If you observe the joints are moving too much or not enough, then the joint properties may not be set up correctly.

```python
# Open your USD and PLAY the simulation before running this snippet
# Change the path to the robot you want to inspect
prim = Articulation(paths="/World/Robot")
print("DOF names:", prim.dof_names)
print("DOF types:", prim.dof_types)
print("DOF limits:", prim.get_dof_limits())
print("DOF gains (stiffness, damping):", prim.get_dof_gains())
print("DOF max efforts:", prim.get_dof_max_efforts())
print("DOF max velocities:", prim.get_dof_max_velocities())
print("DOF drive types:", prim.get_dof_drive_types())
print("DOF friction:", prim.get_dof_friction_properties())
print("DOF armatures:", prim.get_dof_armatures())
```

Then, you can compare the joint properties with the env YAML file generated by Isaac Lab. Check the articulation API documentation for the properties for the DOFs.

For example, in the video below, the spot robotâs stiffness and dampening are set too high, resulting in underactuated movement.

For example, in the video below, the H1 robotâs arm stiffness and dampening are set too low, resulting in over movement.

### Verify the Simulation Environment

If the robot matches exactly and the inference examples are still not working, then itâs time to check the simulation parameters.

#### Physics Scene

Physics scene describes the time stepping with `Time Steps Per Second (Hz)`, so take the inverse of the `dt` parameter in the `env.yaml` and set this correctly.
Also match the physics scene properties with the physx section of the `env.yaml` file.

For example, in the video below, time step was set to 60Hz, instead of the 500Hz expected by the controller.

### Verify the Observation and Action Tensor

Finally, verify the observation and action tensors, and make sure your tensor structures are correct, the data passed in to the tensors are correct, and the correct scale factors are applied to the input and outputs.

Also, make sure the actions output from the policy matches the expected type of inputs of articulation and are in the correct order to correctly power the robot.

## Sim To Real Deployment

Congratulations, your robot and policy are working correctly in Isaac Sim now and you have tested it with the rest of your stack. Now itâs time to deploy it on a real robot.

Please read this [article](https://developer.nvidia.com/blog/closing-the-sim-to-real-gap-training-spot-quadruped-locomotion-with-nvidia-isaac-lab/) on deploying an reinforcement learning policy to a spot robot.

On this page

* [Learning Objectives](#learning-objectives)
* [Demos](#demos)
  + [Unitree H1 Humanoid Example](#unitree-h1-humanoid-example)
  + [Boston Dynamics Spot Quadruped Example](#boston-dynamics-spot-quadruped-example)
* [Training and Exporting Policies in Isaac Lab](#training-and-exporting-policies-in-isaac-lab)
  + [Training](#training)
  + [Exporting](#exporting)
* [Understanding the Environment Parameter File](#understanding-the-environment-parameter-file)
  + [Simulation Setup](#simulation-setup)
  + [Robot Setup](#robot-setup)
  + [Observations Parameters](#observations-parameters)
  + [Actions Parameters](#actions-parameters)
  + [Commands Parameters](#commands-parameters)
* [Policy Controller Class](#policy-controller-class)
  + [Constructor](#constructor)
  + [Load Policy](#load-policy)
  + [Initialize](#initialize)
  + [`_set_articulation_prop`](#set-articulation-prop)
  + [`_compute_action`](#compute-action)
  + [`_compute_observation`](#compute-observation)
  + [Forward](#forward)
* [Position to Torque Controls](#position-to-torque-controls)
  + [Import Policy](#import-policy)
  + [Run the Actuator Network](#run-the-actuator-network)
* [Debugging Tips](#debugging-tips)
  + [Verify Your Policy](#verify-your-policy)
  + [Verify the Robot Joint Properties](#verify-the-robot-joint-properties)
    - [Robot Joint Order](#robot-joint-order)
    - [Default Joint Position](#default-joint-position)
    - [Robot Joint Properties](#robot-joint-properties)
  + [Verify the Simulation Environment](#verify-the-simulation-environment)
    - [Physics Scene](#physics-scene)
  + [Verify the Observation and Action Tensor](#verify-the-observation-and-action-tensor)
* [Sim To Real Deployment](#sim-to-real-deployment)

---

### Isaac Lab Troubleshooting

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/isaac_lab_tutorials/troubleshooting.html

* [Help & FAQ](../overview/help.html)
* [Troubleshooting](../overview/troubleshooting.html)
* Isaac Lab Troubleshooting

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Isaac Lab Troubleshooting

This page consolidates troubleshooting information for Isaac Lab components in Isaac Sim.

## Common Issues

### Installation Issues

* Make sure you have the correct Python version (3.9+) when setting up Isaac Lab
* If encountering ModuleNotFoundError, ensure all dependencies are installed via pip install -e . in the Isaac Lab repository
* For GPU compatibility issues, verify that your CUDA version matches the requirements for Isaac Lab

### Performance Issues

* For slow training performance, try reducing the number of environments or the complexity of the scene
* Memory issues can be resolved by setting smaller batch sizes or reducing environment complexity
* To improve frame rates during training, consider using fewer sensors or reducing their resolution

### Environment Setup Issues

* If robots fail to initialize, check that the URDF/USD files are correctly specified
* For task initialization failures, ensure your task configuration files are properly formatted
* Make sure reward terms and observations are correctly defined in your environment configurations

### Policy Deployment Issues

* When deploying trained policies, verify the observation space matches the training environment
* For poor policy performance after deployment, check if the simulation parameters match the training settings
* If policy files fail to load, verify they are in the correct format supported by Isaac Lab

On this page

* [Common Issues](#common-issues)
  + [Installation Issues](#installation-issues)
  + [Performance Issues](#performance-issues)
  + [Environment Setup Issues](#environment-setup-issues)
  + [Policy Deployment Issues](#policy-deployment-issues)

---


## 数字孪生

### Occupancy Map Generator

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/digital_twin/ext_isaacsim_asset_generator_occupancy_map.html

* [Digital Twin](index.html)
* Mapping

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Mapping

NVIDIA Isaac Sim mapping extension supports 2D occupancy map generation for a specified height.

## Occupancy Map Generator

The [Mapping](#ext-isaacsim-asset-generator-occupancy-map) Extension is used to generate a binary map of whether or not an area in the scene is occupied at a given height. It uses physics collision geometry in the [Stage](../reference_material/reference_glossary.html#isaac-sim-glossary-stage) to determine if a location is occupied or not.

This extension is enabled by default. If it is ever disabled, it can be re-enabled from the [Extension Manager](https://docs.omniverse.nvidia.com/extensions/latest/ext_core/ext_extension-manager.html "(in Omniverse Extensions)") by searching for `isaacsim.asset.gen.omap`.

To access this Extension, go to the top menu bar and click **Tools** > **Robotics** >> **Occupancy Map**.

### Conventions

* All geometry must have Collisions Enabled to be detected by the Occupancy Map Generator. Otherwise the geometry will not appear in the final map.
* The Start location of the map cannot be occupied.

Note

If mapping does not work correctly make sure the start location is not occupied. You can view the physics geometry by clicking the Show/Hide (eye icon) in the viewport window and selecting **Show By Type** > **Physics Mesh** > **All**.

### API Documentation

See the [API Documentation](../py/source/extensions/isaacsim.asset.gen.omap/docs/index.html) for usage information.

### User Interface

The user interface is composed of two parts, the configuration window (named *Occupancy Map*) and the *Occupancy Map Visualization* window.

#### Occupancy Map window

* **Origin**: An open location inside of the area you wish to map.
* **Lower/Upper Bound**: Areas outside of these bounds will not be mapped. These are maximal bounds, the mapped area may be smaller than these limits.
* **Positioning**:

  > + **CENTER TO SELECTION**: The origin will be moved to the center of a selected prim or prims.
  > + **BOUND SELECTION**: The bounds will updated to incorporate the selected prim or prims.

* **Cell Size**: The number of meters each pixel in the final image represents.
* **Occupancy Map**:

  > + **CALCULATE**: Compute the occupancy map.
  > + **VISUALIZE IMAGE**: Open a new window to preview and save the resulting map as an image.
* **Use PhysX Collision Geometry**: When set to True (default), the current collision approximations are used by the PhysX based Lidar to generate the occupancy map. If set to False, the collision approximations are temporarily removed and the RTX Lidar uses the original triangle meshes to generate the occupancy map.

**Example:**

The following steps show how to create and visualize an occupancy map of a certain scene:

> 1. Create a new Cone shape (**Create > Shape > Cone** menu) and add the physics Collision property to it (right click and **Add > Physics > Collider Preset**, or in the *Property* panel).
> 2. Translate the shape 0.3 meters in the X-axis and orient it 90Âº in the X-axis Euler angles by modifying its *Transform* in the *Property* panel.
> 3. Click on the **Tools > Robotics > Occupancy Map** menu to open the *Occupancy Map* window docked to the *Property* panel.
> 4. Set the Occupancy Mapâs Origin Z-axis value to 0.1 meters to map the area at that height
> 5. Click on **CALCULATE** followed by **VISUALIZE IMAGE**. The *Occupancy Map Visualization* window will appear as shown in the image in the next subsection.
> 6. Finally, click **Save Image** to save the map to an easily accessible location. You will need it for later steps in this guide!

#### Occupancy Map Visualization window

* **Occupied Color**: The color chosen to represent space that is âoccupiedâ.
* **Freespace Color**: The color chosen to represent space that is âfreeâ.
* **Unknown Color**: The color chosen to represent space that is interstitial or âunknownâ.
* **Rotate Image**: Rotates the coordinates of the image space. A rotation of \(\text{180}^{\circ}\) will result in a Heightmap orientation that matches that of the original source stage of the occupancy map.
* **Coordinate Type**: Determines the format of the output in the information window. Stage Space coordinates reports values in the space of the stage, while the âROS Occupancy Map Parameters Fileâ returns the needed parameters for the ROS Occupancy Map.
* **Filename**: Base name used when saving the PNG image or YAML file, and written into the YAML `image` field. Defaults to the stage name.
* **RE-GENERATE IMAGE**: This will regenerate the image and information window if you changed the stage.
* **Save Image**: Opens a file dialog pre-filled with the Filename to save the occupancy map as a `.png` file.
* **Save YAML**: Opens a file dialog pre-filled with the Filename to save the ROS occupancy map parameters as a `.yaml` file.

## Heightmap Importer

### Heightmap Importer

The Heightmap Importer Extension converts a 2D occupancy map into a 3D heightmap terrain.
In this extension black pixels in the occupancy map are considered occupied and white pixels are considered free space.
The generated 3D terrain automatically has a collision mesh applied for all the occupied pixels.

To access this Extension, go to the top menu bar and click **Tools** > **Robotics** > **Heightmap Importer**.

* **Cell Size**: Real-world units represented by a single pixel in the 2D occupancy image. The default unit in Isaac Sim is in meters.
* **Load** : Load the desired occupancy image.
* **Generate**: Button to generate the 3D heightmap terrain.

### Heightmap Usage Example

To run the Example:

1. Save the following image to disk:

2. Go to the top menu bar and click **Tools** > **Robotics** > **Heightmap Importer**.
3. Press the **Load Image** button and open the saved image. A window titled **Visualization** will appear.
4. Press the **Generate Heightmap** button to create geometry corresponding to the input occupancy map in the [Stage](../reference_material/reference_glossary.html#isaac-sim-glossary-stage).

On this page

* [Occupancy Map Generator](#occupancy-map-generator)
  + [Conventions](#conventions)
  + [API Documentation](#api-documentation)
  + [User Interface](#user-interface)
    - [Occupancy Map window](#occupancy-map-window)
    - [Occupancy Map Visualization window](#occupancy-map-visualization-window)
* [Heightmap Importer](#heightmap-importer)
  + [Heightmap Importer](#ext-omni-isaac-heightmap-tool)
  + [Heightmap Usage Example](#heightmap-usage-example)

---

### Static Assets

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/digital_twin/warehouse_logistics/tutorial_static_assets.html

* [Digital Twin](../index.html)
* Static Warehouse Assets

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Static Warehouse Assets

Isaac Sim comes with a multitude of assets for you to build your own application. Additionally, there are extra asset libraries provided by NVIDIA that you can use. Open **Window** > **Browsers** > **NVIDIA Assets**, and the window **NVIDIA Assets** will show, where you can browse for all content to build your environment.

Letâs start by setting up the warehouse building. click on the **+** Icon next to **Industrial**, then on **Buildings**, and select **Warehouse**. By dragging **Warehouse01** to the scene, youâll load a reference to the asset on your stage. Alternatively, you can also [build a custom warehouse](ext_omni_warehouse_creator.html).

Note

If you drag on the viewport window, it will let you place it at an arbitrary position, If instead you want it placed at the origin or on a given xform, drag it into the Stage window on top of the desired Prim.

Depending on which assets you goals, you may find **NVIDIA Assets** that are currently on a centimeter scale. This is because **NVIDIA Assets** are created by our art team, while **Isaac Sim Assets** have been curated with intent. Be mindful of the units! When importing certain assets, you may need to manually scale them down to units of 0.01. To do this, select the asset prim, click on âAdd Transformâ on the Properties pane, and set the scale to 0.01 on all directions.

Note

You can add a 0.01 scale on the parent prim you are adding the assets to instead (for example create a prim at /World/Warehouse\_Import and always drag the assets into it), and then all assets will be imported already scaled.

Now you can add some shelves for empty shelves, or racks for shelves filled with boxes.

Any asset in **NVIDIA Assets** can be used to compose your scene, browse around the categories to find the asset you need, or search by name.

## Simulation Needs

These assets are purely visual, so any simulation needs you may have need to be authored on top of it. In that case, the recommendation is to create a new stage, and drag one single asset to it and perform the desired authoring as a variation of the original asset, and save it on your nucleus. Then, on your environment, drag the asset you saved that contains the modifications.

## SimReady Assets

Omniverse also contains a suite of [SimReady Assets](https://docs.omniverse.nvidia.com/simready/latest/index.html), which are assets curated for machine learning and digital twins. These assets come fully annotated for Semantic Labeling, and also contains a preset physics setup so you can get started with your digital twin operation. For more details, visit the [NVIDIA On Demand session: SimReady Specification](https://www.nvidia.com/en-us/on-demand/session/omniverse2020-om1742/?playlistId=playList-63b157fe-95fe-4b93-8b9b-d731be32ec29)

### Example

Letâs make a variation of WarehousePile\_A04 that contains physics properties, with boxes being individual rigid bodies.

We start with a brand new Stage, and create an Xform under World with the name âImportâ, and set its scale to 0.01

Then we drag the WarehousePile\_A04 into it.

To simplify the tree, we can bring the imported prim at the root. Click on the Option button on the stage, and select Show Root, then drag WareHousePile\_A04 on the Root, then right-click it, and select Set as Default Prim. Delete /World and /Environment. Next, select all children of /WareHousePile\_A04, and on the Properties pane, press **Add** > **Physics** > **Rigid Body with Colliders preset**. To see the effect of the rigid body API, add a ground plane by going to **Create** > **Physics** > **Ground Plane**, and start simulation. Try shift-click to drag one of the lower boxes, they should all fall over each other.

You can now go back to the previously saved asset to customize it to contain physics material properties, different mass properties, and so on. All changes will be stored locally and be applied on top of the original asset. To see the local changes, you can go to the Layer tab, right click the Root layer, and click on Edit.

You will see that the USD file opens in edit mode on your text editor, containing the reference to the original asset, and all âdeltasâ that are being applied to it.

On this page

* [Simulation Needs](#simulation-needs)
* [SimReady Assets](#simready-assets)
  + [Example](#example)

---

### cuOpt Logistics Tutorial

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/digital_twin/warehouse_logistics/logistics_tutorial_cuopt.html

* [Digital Twin](../index.html)
* NVIDIA cuOpt

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# NVIDIA cuOpt

## Learning Objectives

Demonstrate and provide a reference for the use of [NVIDIA cuOpt](https://developer.nvidia.com/cuopt-logistics-optimization) to solve routing
optimization problems in simulation.

**Topics include:**

* Creation of waypoint network
* Basic interaction with the cuOpt service
* Visualization and processing of optimization specific data
* Intra-warehouse transport use case demonstration

*15-20 Minute Tutorial*

## Getting Started

**Prerequisites**

* Access to the NVIDIA [cuOpt server](https://docs.nvidia.com/cuopt/user-guide/latest/cuopt-server/index.html) and follow the [cuOpt Quickstart Guide](https://docs.nvidia.com/cuopt/user-guide/latest/cuopt-server/quick-start.html) to setup the cuOpt server.
* Review the Core API [Hello World](../../core_api_tutorials/tutorial_core_hello_world.html#isaac-sim-app-tutorial-core-hello-world) and introductory Tutorial series [Robot Setup Tutorials Series](../../robot_setup_tutorials/index.html#isaac-sim-robot-setup-tutorials).
* NVIDIA cuOpt sample extensions are disabled by default. Enable the extensions required for this tutorial from the [Extension Manager](https://docs.omniverse.nvidia.com/extensions/latest/ext_core/ext_extension-manager.html "(in Omniverse Extensions)")
  by searching for `omni.cuopt.examples`. Enabling `omni.cuopt.examples` will automatically enable `omni.cuopt.service` and `omni.cuopt.visualization`

## NVIDIA cuOpt Examples

This tutorial is based around a set of three examples from the `omni.cuopt.examples` extension.
These examples are arranged in increasing fidelity from simple randomized routing problems
with only basic visualization, to an intra-warehouse transport scenario complete with high fidelity
warehouse assets. Each example leverages supporting extensions in order to interact with the cuOpt service
and visualize optimization data. The code for all examples and supporting extensions is available and
can be extended for use in other applications.

### Example Overview

* **Create Network** : An example demonstrating use of visualization tools to create a network. This network can be saved
  and re-used to represent the waypoint graph for optimization problems. Utilities from the `omni.cuopt.visualization` extension
  are used to create and display the waypoint graph.
* **Simple Cost Matrix** : A minimal example using simple primitives to represent a depot based fleet routing problem
  where vehicles start from a depot (Cone) and must fulfill the demand across all locations (Spheres). A cost Matrix
  representing the cost of travel between locations is created by measuring Euclidean distance between points. `omni.cuopt.service`
  is used for communication between scene data and a running cuOpt service instance.
* **Simple Waypoint Graph** : cuOpt also supports a weighted waypoint graph representation of the optimization environment,
  which is the focus of this example. Waypoint graphs are a common representation for interior environments where the cost
  between locations might not be predetermined and straight line distance is not sufficient. Here the waypoint graph represents
  the travel network, and target locations (a subset of graph nodes) represent the locations to be visited and the location
  of the fleet. In addition to using `omni.cuopt.service`, utilities from the `omni.cuopt.visualization` extension are used
  to process and display the waypoint graph as well as the resulting optimized routes. The waypoint graph, order data, and vehicle
  data are all loaded from JSON files that exist alongside the source code for this example and can be modified as needed.
* **Intra-warehouse Transport Demo** : In this example a more complex waypoint graph is generated to represent the transportation network
  for a warehouse environment. You are able to create and place semantic zones to denote high cost areas of travel to be avoided.
  In addition to the utilities used in the Simple Waypoint Graph example, additional functionality from the `omni.cuopt.visualization`
  extension is used to generate the warehouse environment from a JSON configuration files alongside the source code for the example.

### Supporting Extension Overview

* `omni.cuopt.service`: This extension contains a thin wrapper around the cuOpt service that is used for preprocessing
  scene data as well as formatting and sending requests to the cuOpt service. This extension also contains utilities for representing
  the optimization data and formatting text results to be displayed in the UI for the examples.
* `omni.cuopt.visualization`: This extension contains utilities for generating scene data including the waypoint graph, semantics zones
  and the warehouse environment. This extension also contains helper functions for adjusting the weight of graph edges based
  on proximity to a given semantic zone.

## Running cuOpt Examples

### Create Network

1. Starting from a New Isaac Sim Session (`CTRL + N`) navigate to the cuOpt menu item now present in the Isaac Sim interface and select Create Network.
2. In the Create Node section, click CREATE NODE:

   * **Create Node**: Creates a network node at default location. Move the node around to desired position. Multiple network nodes can be created
     one by one.
3. In the Create Edge section, click CREATE EDGE:

   * **Create Edge**: Creates an edge between two nodes. Select two nodes and click on create edge. Multiple edges between nodes can be created in
     the network one by one.
4. The created network will have Nodes and Edges that looks like:
5. Save the network file as USD for future use in optimization problems.
6. Click **Open Source Code** to view the reference implementation.

### Simple Cost Matrix

1. Starting from a New Isaac Sim Session (`CTRL + N`) navigate to the cuOpt menu item now present in the Isaac Sim interface and select Simple Cost Matrix.
2. Enter the credentials assigned to you for the NVIDIA cuOpt managed service.

   > See [Running cuOpt Examples](#credentials-cuopt).
3. In the Optimization Problem Setup section, select values (or use defaults) for the following, then click SETUP PROBLEM:

   * **Fleet Size**: The maximum number of vehicles available. **Note** If a solution can be found using fewer vehicles that solution will be returned.
   * **Vehicle Capacity**: The number of stops (of demand=1) each vehicle can visit.
   * **Number of Locations**: The number of non-depot locations that must be visited.
   * **Solver Time Limit**: The amount of time the cuOpt solver is given to find an optimized solution. **Note** To maintain solution quality additional time should be given for larger problems.
4. In the Run cuOpt section, click SOLVE to return optimized routes. A text representation of the routes is displayed in the UI and results are also shown in the viewport.
5. Click **Open Source Code** to view the reference implementation.

### Simple Waypoint Graph

1. Starting from a New Isaac Sim Session (`CTRL + N`) navigate to the cuOpt menu item now present in the Isaac Sim interface and select Simple Waypoint Graph.
2. Enter the credentials assigned to you for the NVIDIA cuOpt managed service.

   > See [Running cuOpt Examples](#credentials-cuopt).
3. In the Optimization Problem Setup section, click the LOAD buttons from top to bottom (Waypoint Graph, Orders, Vehicles) to setup the problem:

   * **Load Waypoint Graph** Clicking LOAD JSON loads a sample waypoint graph from `/extension_data/waypoint_graph.json`, which exists alongside
     the source code for this example. To load a network from a USD file created using the Create Network tools, drop the file into Stage window
     and click LOAD SCENE. A sample Network.usda is provided in `/extension_data/Network.usda`, which exists alongside
     the source code for this example.
   * **Load Orders** loads sample order data from `/extension_data/order_data.json`, which exists alongside the source code for this example.
     Order locations now appear in green.
   * **Load Vehicles** loads sample vehicle data from `/extension_data/vehicle_data.json`, which exists alongside the source code for this example.
     **Note** Vehicles are assigned to start from Node\_0 position, but are not shown in the viewport.
4. In the Run cuOpt section, click SOLVE to return optimized routes. A text representation of the routes is displayed in the UI and results are also shown in the viewport.
5. Click **Open Source Code** to view the reference implementation.

### Intra-warehouse Transport Demo

1. Starting from a New Isaac Sim Session (`CTRL + N`), navigate to the cuOpt menu item now present in the Isaac Sim interface and select Intra-warehouse Transport Demo.
2. Enter the credentials assigned to you for the NVIDIA cuOpt managed service.

   > See [Running cuOpt Examples](#credentials-cuopt).
3. In the Optimization Problem Setup section, click the LOAD buttons from top to bottom (Sample Warehouse, Waypoint Graph, Orders, Vehicles, Semantic Zone) to setup the problem:

   * **Load Sample Warehouse** loads a sample warehouse defined by `/extension_data/warehouse_building_data.json`, conveyors defined by
     `/extension_data/warehouse_conveyors_data.json` and shelves defined by `/extension_data/warehouse_shelves_data.json`.
     All JSON files can be found alongside the source code for this example.
   * **Load Waypoint Graph** loads a sample waypoint graph from `/extension_data/waypoint_graph.json`, which exists alongside
     the source code for this example.
   * **Load Orders** loads sample order data from `/extension_data/order_data.json`, which exists alongside the source code for this example.
     Order locations now appear in green.
   * **Load Vehicles** loads sample vehicle data from `/extension_data/vehicle_data.json`, which exists alongside the source code for this example.
     **Note** Vehicles are assigned to start from Node\_0 position but are not shown in the viewport.
   * **(OPTIONAL) Create Semantic Zone** creates a semantic zone of user defined size starting at location `(0,0,0)`. If the generated semantic zone
     is placed over one or more edges in the waypoint graph, the edge within that semantic zone is assigned a very high travel cost. cuOpt attempts
     to avoid these edges if possible in the optimized solution. **Note** Each time the Generate button is clicked a new semantic zone is created.
4. In the Run cuOpt section, if a semantic zone has been created or moved, click UPDATE to capture the current weights. Then
   click SOLVE to return optimized routes. A text representation of the routes is displayed in the UI and results is also shown in the viewport.
5. Click **Open Source Code** to view the reference implementation.

## Additional Information

The examples shown here demonstrate only a small subset of cuOpt functionality. For additional features and advanced usage
see the [cuOpt Documentation](https://docs.nvidia.com/cuopt/) and the [cuOpt-Resources Repository](https://github.com/NVIDIA/cuOpt-Resources).

On this page

* [Learning Objectives](#learning-objectives)
* [Getting Started](#getting-started)
* [NVIDIA cuOpt Examples](#nvidia-cuopt-examples)
  + [Example Overview](#example-overview)
  + [Supporting Extension Overview](#supporting-extension-overview)
* [Running cuOpt Examples](#running-cuopt-examples)
  + [Create Network](#create-network)
  + [Simple Cost Matrix](#simple-cost-matrix)
  + [Simple Waypoint Graph](#simple-waypoint-graph)
  + [Intra-warehouse Transport Demo](#intra-warehouse-transport-demo)
* [Additional Information](#additional-information)

---

### Warehouse Creator

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/digital_twin/warehouse_logistics/ext_omni_warehouse_creator.html

* [Digital Twin](../index.html)
* Warehouse Creator Extension

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Warehouse Creator Extension

The Warehouse Creator is an interactive plan builder that converts a 2D grid layout into a USD warehouse
built from the Modular Warehouse asset pack. Sketch the floor plan in a top-down editor, place tiles from a
block library, and generate the corresponding USD prims on the active stage.

The feature ships as two extensions:

* `omni.warehouse.creator.api` â headless logic (grid engine, auto-tiling, plan-to-stage sync, and the
  column editing controller). Use it from scripts and tests with no UI dependency.
* `omni.warehouse.creator.ui` â the **Warehouse Builder** window, toolbar, block library palette,
  variant property widget, and column placement workflow.

## Installing and enabling the extension

1. Open **Window > Extensions** from the top menu.
2. Search for `omni.warehouse.creator.ui` in the **Extension Manager** window.
3. Click **Install** or **Update** if needed.
4. Toggle the extension on. Enable **Autoload** to start it on every launch.

The UI extension pulls in `omni.warehouse.creator.api` automatically. Enabling the API extension on its
own is supported for headless / scripted workflows.

## Opening the editor

Open **Window > Warehouse Creator** to show the **Warehouse Builder** window. The window contains:

* An **overhead 2D viewport** centered on the grid origin.
* A **floating toolbar** along the bottom of the viewport with all editing tools.
* A **block library palette** docked to the side of the window.
* A **Warehouse Creator** panel with the **Generate Warehouse** button and the collapsible **Column
  Editor** section.

The window builds on first open and stays in memory after you close it, so reopening is instantaneous.

## Configuring the dataset source

Configure asset paths from **Edit > Preferences > Warehouse Creator**. The page exposes:

| Setting | Purpose |
| --- | --- |
| **Cell Size (world units)** | World-space size of a single grid cell. Controls both the editor grid and the generated tile spacing. |
| **Wall Height (world units)** | Height applied to the wall asset preset. |
| **Center (floor) Asset** | File name of the center/floor USD asset relative to the asset root. |
| **Wall Asset** | File name of the wall USD asset relative to the asset root. |
| **Asset Root Path** | Local or Nucleus root folder containing the warehouse assets. Point this at your downloaded Isaac Sim assets folder for the fastest editor and generation experience. |
| **Cloud Assets URL** | HTTPS fallback used when **Asset Root Path** is unset or unreachable. |

Note

The **Cell Size**, **Wall Height**, and asset name settings depend on the asset pack you use. The
default values match the Isaac Sim assets pack; for a custom pack, set the values manually. An asset
pack is a collection of Center/Floor and Wall assets that share a variant system exposing every
available option of each asset type as a reference. See the Modular Warehouse pack for an example of
how to structure one.

For local performance, download the Isaac Sim assets pack (see [Latest Release](../../installation/download.html#isaac-sim-latest-release)) and point
**Asset Root Path** at `[Isaac Sim Assets Path]/Isaac/Environments/Modular_Warehouse_New/`. The block
library palette and the warehouse generator both read from this location.

## Editor workflow

The editor operates on a logical grid. At generation time, each occupied cell becomes a center/floor
prim and each exposed cell edge becomes a wall prim. The generator omits walls between two adjacent
occupied cells.

The toolbar uses three categories of buttons:

* **Modal tools** â mutually exclusive. Activating one deactivates the previously active modal tool.

  + **Select**
  + **Move**
  + **Rotate**
  + **Draw**
  + **Line**
  + **Box**
  + **Erase**
* **Toggles** â coexist with any modal tool. Activating symmetry mirrors every drawing or erasing
  action across the chosen axis.

  + **Symmetry Horizontal**
  + **Symmetry Vertical**
* **Immediate actions** â one-shot operations. They execute on click without becoming the active tool.

  + **Flip Horizontal**
  + **Flip Vertical**
  + **Group**
  + **Ungroup**
  + **Merge**
  + **Subtract**
  + **Zoom In**
  + **Zoom Out**

Selection-dependent actions ( **Flip**,  **Group**,  **Ungroup**,
 **Merge**, and  **Subtract**) are disabled in the toolbar when the current
selection does not meet their requirements.

### Drawing tiles

1. Pick an asset in the **Block Library Palette**. The next drawing operation places this asset as the
   manual tile.
2. Activate  **Draw** for free-form painting,  **Line** for a straight-line drag, or
    **Box** for filled rectangles.
3. Click and drag inside the viewport to add cells.  **Erase** removes cells with the same
   gestures.

To drop a single tile at the cursor without changing the active tool, drag a palette card directly onto
the viewport.

**Symmetry Horizontal** and  **Symmetry Vertical** mirror every drawing or erasing
action across the world origin on the selected axis. Toggle them at any time without leaving the active
drawing tool.

### Selecting and editing

* **Select** â click a cell to select it. Click and drag to draw a selection box.
  Selecting a grouped cell selects the entire group.
* **Move** â drag selected cells or groups to a new grid location.
* **Rotate** â click to rotate the selection 90 degrees clockwise. Use the keyboard
  shortcuts below for finer control.
* **Flip Horizontal** /  **Flip Vertical** â mirror the selection across the
  corresponding axis in place.

### Hotkeys

The window owns its hotkey scope, so the shortcuts only fire while the cursor is over the
**Warehouse Builder** window.

| Shortcut | Action |
| --- | --- |
| `Delete` / `Backspace` | Delete the current selection (cells and groups). |
| `Esc` | Clear the current selection. |
| `Ctrl+Z` / `Ctrl+Y` | Undo / redo the last grid command. |
| `Left` / `Right` | Rotate the selected cells 90 degrees counter-clockwise / clockwise. Hold `Shift` to rotate in place. |
| `Space` | Cycle to the next tool (when `enable_hotkeys` is enabled in the extension settings). |

### Grouping cells

A group treats a set of cells as a single floating object. You can move, rotate, and flip a group as a
unit, and the generator emits each group as a separate warehouse root prim.

* **Group** â combine the selection into a new group. Requires at least two ungrouped cells
  or existing groups.
* **Ungroup** â stamp a selected groupâs cells back onto the grid as ungrouped cells.
* **Merge** â combine two or more selected groups into one.
* **Subtract** â remove the cells of later-selected groups from the first-selected
  group.

At generation time, each group becomes its own `/Warehouse_group_<id>` root prim with walls derived
from its boundary. Adjacent groups can sit next to ungrouped cells without sharing walls.

### Variant property widget

The generator emits two tile types â **Wall** and **Center** â and each tile ships with a set of
visual variants such as a loading dock, an access panel, or a window. After generation, select one or
more tile prims in the stage and use the **Warehouse Tiles** section of the **Property** panel to switch
the variant on every selected tile of that type.

Tip

In the viewport, set **Select Mode** to **Component** (right-click the toolbar) so individual tiles
are selectable instead of the whole warehouse hierarchy.

## Generating the warehouse

The **Generate Warehouse** button in the **Warehouse Creator** panel converts the current plan into USD
prims on the active stage:

* All ungrouped cells go under `/Warehouse`.
* Each group goes under its own `/Warehouse_group_<id>`.
* A center/floor prim is placed at every occupied cell, and a wall prim is added on every exposed edge,
  rotated to face outward.

A modal **Generating Warehouse** popup blocks input until the USD layers settle. This keeps the editor
responsive while large layouts stream in.

Re-running **Generate Warehouse** replaces the existing root prims with a fresh layout, so you can
iterate on the plan and regenerate without manual cleanup.

## Editing column placement

Each warehouse block carries a quarter-column at every corner. Adjacent blocks combine their
quarter-columns into a single full column. The **Column Editor** toggles individual full columns on or
off after the warehouse is generated, without manually authoring per-block variants.

1. Generate the warehouse, then select any prim under one of the warehouse roots. The **Edit Column
   Placement** button becomes available when the selection sits under a generated warehouse.
2. Click **Edit Column Placement** to enter edit mode. The editor hides the ceiling and non-column
   geometry, highlights each column (green for kept, red for pending removal), and forces the viewport
   outline overlay on so the highlights remain visible.
3. Click columns in the viewport to toggle each between **Enabled** (green) and **Disabled** (red). Drag
   a marquee to toggle multiple at once. Use the **Enable All**, **Disable All**, and **Flip All**
   buttons for bulk operations.
4. Click **Confirm** to author the variant selections on the root layer, or **Cancel** to discard the
   pending changes. Both actions exit edit mode and clear the temporary visibility overrides.

## Headless API

For scripts, batch jobs, and tests, `omni.warehouse.creator.api` exposes the same generation pipeline
without any UI:

```python
import omni.usd
from omni.warehouse.creator.api import CellData, GridConfig, GridEngine, StageSyncer

cells = {
    (0, 0): CellData(),
    (1, 0): CellData(),
    (1, 1): CellData(),
}

engine = GridEngine(GridConfig(cell_size=10.0))
stage = omni.usd.get_context().get_stage()

placed = StageSyncer().sync(cells, engine, stage)
```

The `ColumnEditorController` mirrors the **Column Editor** workflow for headless use. Call
`enter()` to begin a session, mutate the pending-disabled set with `set_all()`,
`flip_all()`, or `toggle_keys()`, then call `leave()` with `commit=True` to author the
selections.

On this page

* [Installing and enabling the extension](#installing-and-enabling-the-extension)
* [Opening the editor](#opening-the-editor)
* [Configuring the dataset source](#configuring-the-dataset-source)
* [Editor workflow](#editor-workflow)
  + [Drawing tiles](#drawing-tiles)
  + [Selecting and editing](#selecting-and-editing)
  + [Hotkeys](#hotkeys)
  + [Grouping cells](#grouping-cells)
  + [Variant property widget](#variant-property-widget)
* [Generating the warehouse](#generating-the-warehouse)
* [Editing column placement](#editing-column-placement)
* [Headless API](#headless-api)

---

### Conveyor Extension

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/digital_twin/warehouse_logistics/ext_isaacsim_asset_gen_conveyor.html

* [Digital Twin](../index.html)
* Conveyor Belt Utility

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Conveyor Belt Utility

## About

The Conveyor Belt Utility extension turns rigid bodies into conveyors in NVIDIA Isaac Sim.

Note

For a more customizable approach to conveyor belt simulation, see [Custom conveyor belt simulation](#isaac-conveyor-custom-sim).

## Usage

To enable the extension:

1. Select **Window > Extensions**.
2. Search for `conveyor`.
3. Select `isaacsim.asset.gen.conveyor.ui` and click **Enable**. This enables both the extension and its UI.

To load the extension automatically on startup, click **Autoload** near the top of the `isaacsim.asset.gen.conveyor.ui` information pane in the extension manager.

To create a conveyor:

1. Select a rigid body or a mesh in the stage.
2. Choose **Create > Isaac Sim > Warehouse Items > Conveyor** to create an Omniverse OmniGraph node that drives conveyor speed and animation. The node exposes the following properties:

   * **conveyorPrim**: The target prim that receives the conveyor velocity. If the prim is not a rigid body, it is configured as one automatically with default collision models. Only a single prim is allowed per `ConveyorNode`.
   * **Animate Direction**: Texture animation direction in the UV map.
   * **Animate Scale**: Ratio between conveyor velocity and texture animation speed.
   * **Animate Texture**: Enables texture animation.
   * **Curved**: Marks the conveyor as curved. When set, the node applies angular velocity instead of linear velocity. The angular velocity is applied along the **Direction** vector, which acts as the rotation axis. Scaling the **Direction** vector adjusts the velocity: values greater than 1 increase the effective curvature radius and values less than 1 decrease it. For example, `(0, 0, 1)` rotates about the Z axis.
   * **Direction**: Conveyor velocity direction in local coordinates.
   * **Enabled**: Enables or disables the conveyor.
   * **Velocity**: Conveyor velocity.

The generated Omniverse OmniGraph is preconfigured with a velocity variable that you can edit by selecting the Omniverse OmniGraph prim. To synchronize multiple conveyors in a scene, point each conveyorâs read-variable node (`read_speed`) at the same Omniverse OmniGraph variable.

To emulate belt motion visually, apply a tiled texture and set the **Animate** properties so the texture translates along the same direction as the conveyor and at a matching speed.

Alternatively, define your own Omniverse OmniGraph and add `ConveyorNode` instances to it. This lets you manage multiple conveyors from a single graph.

For convenience, the Isaac Sim assets package includes prebuilt conveyor pieces at `Isaac/Props/Conveyors`.

When authoring conveyor behavior for these assets, select the `Belt` or `Rollers` prim. Those prims contain the meshes that define the conveyor surface.

## Digital twin library conveyor system generator

To support digital twin authoring, a conveyor system generator is available at **Tools > Conveyor Track Builder**. The utility ships with the Digital Twin asset pack for conveyors, and it also accepts custom datasets by pointing the configuration file at a different asset folder.

When the current selection is a component from the conveyor dataset, the builder attempts to connect the new piece to one of the existing conveyor endpoints defined by the configuration. Otherwise, it parents the new piece under the current selection.

The builder integrates loosely with the assets to keep system creation flexible while applying a minimal rule set. As a tradeoff, completed systems may require small manual cleanup, but the loose coupling lets you fully customize each track after it has been placed.

### User interface

| Ref # | Option | Description |
| --- | --- | --- |
| 1 | Conveyor Style | Available conveyor styles: Roller, Belt, or Dual. |
| 2 | Track Type | Available track types: Start, straight, T-split, Y-split, or end. |
| 3 | Curvature | Track curvature: None, Half (typically 90 degrees), or Full (typically 180 degrees), to the left or right. |
| 4 | Elevation | Track elevation, measured in levels relative to the entry point, either up or down. |
| 5 | Selected Track | Shows the currently selected track, its endpoints, and a Delete button that removes the track from the system. |
| 6 | New Track | Shows the piece queued for insertion. Lets you choose the input endpoint and the track variant, and, when applicable, mirror the piece. |
| 7 | Track Variants | Shows additional variants matching the current filter selection. |
| 8 | Selected Endpoint | Each option corresponds to one of the trackâs endpoints. Endpoints that are already in use are hidden unless all endpoints are connected. |
| 9 | Mirror | Mirrors the selected piece along the primary belt direction. |

### Dataset

The dataset is a collection of USD files used to assemble conveyor systems. Each USD file must:

* Define a default prim. That prim and all of its children load when the asset is referenced.
* Use an identity transform on the default prim (translate and rotate components set to zero).
* Define each conveyor track as an `Xform` prim, with all visual and collision meshes parented under it.
* Place the trackâs entry point at the origin, aligned with the X axis, centered on the Y axis.
* Place anchor points at the end of the track at `Z = 0`, centered on the Y axis. The X axis must be aligned with the base direction of the track.
* Assign individual materials per track. Meshes that share the same conveyor base prim may share materials.
* Live under a single base folder. Assets may still reference files outside that folder.

A JSON file accompanies the asset dataset. It provides the metadata required by the UI workflow and the parameters used to configure conveyor physics when the source assets do not already embed them.

> ```python
> {
>     "assets": {
>         "ConveyorBelt_A01": {  // File name of the asset, without the extension.
>             "style": "DUAL",  // Conveyor style, can be ROLLER, BELT, or DUAL
>             "start_level": 0,  // Conveyor level for the track, can be any positive number
>             "angle": "HALF",  // Conveyor turn type, can be NONE, HALF, FULL"
>             "curvature": "SMALL",  // Conveyor radius of curvature, can be NONE, SMALL, MEDIUM, LARGE. Currently not used by the filter.
>             "ramp": "FLAT",  // Ramp level. How many levels it increases or decreases start level, can be FLAT, ONE, TWO, THREE, FOUR.
>             "type": "STRAIGHT",  // Track Type, can be START, STRAIGHT (used for all single track types, including curves and ramps), Y_MERGE, T_MERGE, FORK_MERGE, END.
>             "anchors": [  // All Prim children paths that correspond to  endpoints on the asset.
>                 "",  // This is the root of the conveyor, which is also an endpoint.
>                 "/Anchorpoint"  // For all the other anchors, keep the trailing / on the child prim name
>             ],
>             "conveyor_nodes": {  // All Child Prims to be configured as conveyors using the OmniGraph node. Each track should have its own configuration (in the case of merge and splits), even if it's of the same style
>                 "Rollers": {
>                     "animate_scale": 0.01,
>                     "animate_direction": [0.0, 1.0],
>                     "direction": [1.0, 0.0, -37.0],
>                     "curved": true
>                 },
>                 "Belt": {
>                     "animate_scale": 0.5,
>                     "animate_direction": [1.0, 0.0],
>                     "direction": [0, 0.0, -37.0],
>                     "curved": true
>                 }
>             }
>         }
>     }
> }
> ```

Note

Strict JSON does not allow comments. The snippet above includes inline comments only to explain each field. Remove the comments before using the file, otherwise the extension will fail to load it.
For a complete reference, see the JSON file in the extensionâs `data` folder.

### Changing the configuration and dataset source

To replace the dataset and configuration file with your own:

1. Go to **Edit > Preferences > Conveyor Builder**.
2. Set the configuration file path and the **Conveyor Assets Location**. The assets must reside directly inside the folder listed in **Conveyor Assets Location**.

To restore the original settings, click **Reset To Default**.

### Improving load time

By default, the tool reads assets from the cloud-hosted assets folder and downloads each asset the first time it is used. This can introduce noticeable load times. To reduce them, download the assets locally and point the **Conveyor Assets Location** at the local folder.

#### Available tracks

|  |  |  |
| --- | --- | --- |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |

## Custom conveyor belt simulation

As an alternative to the built-in physics simulation, you can compute the friction forces between conveyor belt surfaces and the rigid bodies they transport with custom logic. This approach gives you direct control over the friction model and makes it easier to handle cases where a rigid body contacts multiple conveyor belts running at different speeds.

The conveyor belt standalone example demonstrates one such implementation. It is located in `standalone_examples/conveyor_belt`. To run the sample, use the NVIDIA Isaac Sim Python launcher (`python.sh` on Linux or `python.bat` on Windows). The entry point is `cb_app.py`:

```python
./python.sh ./standalone_examples/conveyor_belt/cb_app.py
```

The sample registers transported rigid bodies and conveyor belt sections up front. Two helper classes manage the registration: `BodyManager` and `ConveyorBeltManager`. Once all rigid bodies and conveyor belt sections are registered, these classes allocate the data buffers required for the custom force computation. The registration sequence is shown in `cb_scene.py`, which builds the conveyor belt circuit and the transported rigid bodies.

Register a rigid body to be transported by the conveyor belts as follows:

```python
body_manager.add_body(
    "/World/body0",
    body_material0_index
)
```

The method takes the rigid bodyâs USD prim path and a material index. Material indices come from another helper class, `MaterialPairManager`. Because the sample computes friction forces itself, the physics materials used by the built-in simulation must use a friction coefficient of zero. Otherwise, the built-in friction forces would compound with the custom forces. The sample sidesteps this by defining its own material system and assigning friction coefficients to material pairs:

```python
body_material0_index = material_pair_manager.add_transported_body_material_index()

conveyor_belt_material0_index = material_pair_manager.add_conveyor_belt_material_index()

material_pair_manager.set_material_pair_friction(body_material0_index, conveyor_belt_material0_index, 0.9)
```

Belt motion is described by velocity fields. The sample implements two field types:

* A constant velocity field for straight conveyor belt sections.
* A pivot-point velocity field for curved (turning) conveyor belt sections.

The helper class `VelocityFieldActuator` creates these fields. Given a velocity field, register a conveyor belt section as follows:

```python
target_velocity = wp.vec3(0.0, 0.5, 0.0)

velocity_field_id = velocity_field_actuator.add_constant_velocity_field(
    target_velocity,
)

surface_normal = wp.vec3(0.0, 0.0, 1.0)

conveyor_belt_manager.add_conveyor_belt(
    "/World/conveyor_belt0",
    VELOCITY_FIELD_TYPE_CONSTANT_VELOCITY,
    velocity_field_id,
    surface_normal,
    conveyor_belt_contact_processing_threshold,
    conveyor_belt_material0_index,
)
```

This call requires the USD path of the geometry prim representing the conveyor belt section, the velocity field type, and the velocity field ID. As with rigid body registration, a material index is required. See the sample source for details on the remaining parameters.

After all rigid bodies and conveyor belt sections are registered, the helper classes allocate the buffers used to compute the friction forces. The full set of registered prims is also used to construct an `isaacsim.core.prims.RigidPrim` view. This view exposes the rigid body simulation state and, in particular, the detailed contact information needed to derive the custom friction forces. The sample uses Omniverse Warp to implement the force computation, which keeps most of the data on the GPU.

For a deeper walkthrough, including a per-file summary, advantages, disadvantages, current limitations, and proposed extensions, see `standalone_examples/conveyor_belt/README.md`.

On this page

* [About](#about)
* [Usage](#usage)
* [Digital twin library conveyor system generator](#digital-twin-library-conveyor-system-generator)
  + [User interface](#user-interface)
  + [Dataset](#dataset)
  + [Changing the configuration and dataset source](#changing-the-configuration-and-dataset-source)
  + [Improving load time](#improving-load-time)
    - [Available tracks](#available-tracks)
* [Custom conveyor belt simulation](#custom-conveyor-belt-simulation)

---

### RTSP Camera Streaming

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/digital_twin/rtsp_camera_streaming.html

* [Digital Twin](index.html)
* Live Camera Streaming over RTSP

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Live Camera Streaming over RTSP

NVIDIA Isaac Sim can publish a live video feed of a camera in the scene over the
Real Time Streaming Protocol (RTSP). Frames captured from a render product are
encoded with NVIDIAâs hardware video encoder (NVENC) and pushed to an in-process
RTSP server, which any standard client (VLC, `ffplay`, GStreamer, OpenCV) can
connect to. This is the recommended path for piping simulated camera output
into perception stacks, recording rigs, broadcast pipelines, or downstream
analytics services that already speak RTSP.

The streaming pipeline ships in the `isaacsim.streaming.rtsp` extension. Enable
the extension when you need RTSP streaming. It exposes two entry points: an
OmniGraph node for declarative scene-graph authoring, and a Replicator
writer for fully programmatic setups.

## Prerequisites

Ensure you have the following:

* An NVIDIA GPU with NVENC support (required for H.264 encoding).
* Enable the `isaacsim.streaming.rtsp` extension in the **Extension Manager**
  window by navigating to **Window** > **Extensions**, or launch NVIDIA Isaac Sim
  with `--enable isaacsim.streaming.rtsp`.

## Streaming a Camera

The `isaacsim.streaming.rtsp.RTSPCameraHelper` OmniGraph node
publishes a cameraâs render product over RTSP. A complete pipeline consists
of this node and two supporting nodes wired in a single execution chain:

* `OnPlaybackTick` â runs the graph once per timeline frame while
  playback is running.
* `IsaacCreateRenderProduct` â creates (or reuses) a render product
  for the target camera at the requested resolution and emits its USD
  path on `renderProductPath`.
* `RTSPCameraHelper` â attaches the streaming writer to that render
  product and brings up the RTSP server on the configured port and mount
  path.

### Building the Graph in the Editor

The recommended way to author the pipeline is the OmniGraph editor.
To build the graph:

1. Open **Window > Graph Editors > Action Graph** and click **New Action
   Graph**.
2. Add the three nodes listed above. To find them, search for `RTSP`,
   `Isaac Create Render Product`, and `On Playback Tick`.
3. Connect `OnPlaybackTick.tick` to `IsaacCreateRenderProduct.execIn`,
   then `IsaacCreateRenderProduct.execOut` to `RTSPCameraHelper.execIn`.
4. Connect `IsaacCreateRenderProduct.renderProductPath` to
   `RTSPCameraHelper.renderProductPath` so the helper attaches to the
   render product the previous node created.
5. On the `IsaacCreateRenderProduct` node, set **cameraPrim** to the
   camera you want to stream.
6. On the `RTSPCameraHelper` node, set **port** (default `8554`) and
   **mountPath** (default `/stream`).
7. Press **Play** in the timeline. The RTSP server starts lazily on the
   first rendered frame and the stream becomes available at
   `rtsp://localhost:8554/<mountPath>`. The server shuts down cleanly when
   you press **Stop**.

Refer to [Stream Parameters](#isaac-sim-rtsp-streaming-parameters) for the full set of node
inputs. The screencast below shows the full sequence end-to-end:

### Building the Graph from a Script

The same pipeline can be authored programmatically using
`omni.graph.core.Controller`. This is useful for headless setups,
batch jobs, and tests. The snippet below builds the equivalent graph against
a camera at `/Camera` and configures the stream at
`rtsp://localhost:8554/stream`. Press **Play** or start Replicator capture
to produce frames and start the RTSP server.

```python
import omni.graph.core as og
import omni.kit.app
import omni.usd
from pxr import UsdGeom

ext_mgr = omni.kit.app.get_app().get_extension_manager()
ext_mgr.set_extension_enabled_immediate("isaacsim.core.nodes", True)
ext_mgr.set_extension_enabled_immediate("isaacsim.streaming.rtsp", True)

stage = omni.usd.get_context().get_stage()
UsdGeom.Camera.Define(stage, "/Camera")

og.Controller.edit(
    {"graph_path": "/RTSPGraph", "evaluator_name": "execution"},
    {
        og.Controller.Keys.CREATE_NODES: [
            ("OnPlaybackTick", "omni.graph.action.OnPlaybackTick"),
            ("CreateRenderProduct", "isaacsim.core.nodes.IsaacCreateRenderProduct"),
            ("RTSPHelper", "isaacsim.streaming.rtsp.RTSPCameraHelper"),
        ],
        og.Controller.Keys.SET_VALUES: [
            ("CreateRenderProduct.inputs:cameraPrim", "/Camera"),
            ("CreateRenderProduct.inputs:width", 1280),
            ("CreateRenderProduct.inputs:height", 720),
            ("RTSPHelper.inputs:port", 8554),
            ("RTSPHelper.inputs:mountPath", "/stream"),
            ("RTSPHelper.inputs:useRawEncoding", False),
        ],
        og.Controller.Keys.CONNECT: [
            ("OnPlaybackTick.outputs:tick", "CreateRenderProduct.inputs:execIn"),
            ("CreateRenderProduct.outputs:execOut", "RTSPHelper.inputs:execIn"),
            ("CreateRenderProduct.outputs:renderProductPath", "RTSPHelper.inputs:renderProductPath"),
        ],
    },
)
```

### Connecting a Client

Any standard RTSP client (such as VLC, `ffplay`, or GStreamer) can
subscribe to the stream at `rtsp://<host>:<port><mountPath>`.

When connecting from another machine, replace `localhost` with the
simulator hostâs IP and make sure the port is reachable through any
firewalls.

## Stream Parameters

The `RTSPCameraHelper` node exposes the following inputs:

| Input | Default | Description |
| --- | --- | --- |
| `renderProductPath` | â | Path of the render product whose `LdrColor` Arbitrary Output Variable (AOV) is streamed. Wire it to the `renderProductPath` output of `IsaacCreateRenderProduct` or set it to a pre-authored render product prim. |
| `port` | `8554` | TCP port the RTSP server listens on. Must be in `1`â`65535`. Each simultaneous stream needs a unique port. |
| `mountPath` | `/stream` | Path appended to the server URL (for example `/front`, `/cam_1`). Must start with `/`. |
| `useRawEncoding` | `false` | When `false`, frames are pre-encoded as H.264 in the render pipeline (NVENC) and Supplemental Enhancement Information (SEI) metadata is injected per frame. When `true`, raw RGBA CUDA buffers are streamed and the RTSP server encodes them. Refer to [Encoding Modes](#isaac-sim-rtsp-encoding-modes). |
| `enabled` | `true` | Toggle the stream at runtime. Setting it to `false` after attachment tears down the server and releases the port. |

## Encoding Modes

The writer supports two encoding paths, controlled by `useRawEncoding`:

### H.264 (Default, Recommended)

The render pipeline produces H.264-encoded bytes directly using NVENC and
hands them to the RTSP server already compressed. This mode:

* Minimizes copies (no CPU readback, no double-encode).
* Supports per-frame SEI metadata. Refer to [Frame Metadata](#isaac-sim-rtsp-frame-metadata).
* Sends the simulation timestamp with each streamed frame so downstream
  consumers can align frames to the sim time.

Use this mode unless you have a specific reason to bypass NVENC.

### Raw

The writer streams uncompressed RGBA CUDA buffers and lets the RTSP server
encode them internally.

The render productâs resolution is read from the CUDA buffer shape on the
first frame. SEI metadata injection is **not** supported in raw mode.

## Streaming Multiple Cameras

To publish several cameras simultaneously, instantiate one `RTSPCameraHelper`
per camera and give each helper a unique `port`. The `mountPath` can be
shared across streams, but using a descriptive mount path per camera (such as
`/front` and `/rear`) makes the URLs self-documenting:

```python
import omni.graph.core as og
import omni.kit.app
import omni.usd
from pxr import UsdGeom

ext_mgr = omni.kit.app.get_app().get_extension_manager()
ext_mgr.set_extension_enabled_immediate("isaacsim.core.nodes", True)
ext_mgr.set_extension_enabled_immediate("isaacsim.streaming.rtsp", True)

stage = omni.usd.get_context().get_stage()
UsdGeom.Camera.Define(stage, "/CameraFront")
UsdGeom.Camera.Define(stage, "/CameraRear")

og.Controller.edit(
    {"graph_path": "/MultiStreamGraph", "evaluator_name": "execution"},
    {
        og.Controller.Keys.CREATE_NODES: [
            ("OnPlaybackTick", "omni.graph.action.OnPlaybackTick"),
            ("FrontRP", "isaacsim.core.nodes.IsaacCreateRenderProduct"),
            ("RearRP", "isaacsim.core.nodes.IsaacCreateRenderProduct"),
            ("FrontRTSP", "isaacsim.streaming.rtsp.RTSPCameraHelper"),
            ("RearRTSP", "isaacsim.streaming.rtsp.RTSPCameraHelper"),
        ],
        og.Controller.Keys.SET_VALUES: [
            ("FrontRP.inputs:cameraPrim", "/CameraFront"),
            ("FrontRP.inputs:width", 1280),
            ("FrontRP.inputs:height", 720),
            ("RearRP.inputs:cameraPrim", "/CameraRear"),
            ("RearRP.inputs:width", 1280),
            ("RearRP.inputs:height", 720),
            ("FrontRTSP.inputs:port", 8554),
            ("FrontRTSP.inputs:mountPath", "/front"),
            ("RearRTSP.inputs:port", 8555),
            ("RearRTSP.inputs:mountPath", "/rear"),
        ],
        og.Controller.Keys.CONNECT: [
            ("OnPlaybackTick.outputs:tick", "FrontRP.inputs:execIn"),
            ("OnPlaybackTick.outputs:tick", "RearRP.inputs:execIn"),
            ("FrontRP.outputs:execOut", "FrontRTSP.inputs:execIn"),
            ("RearRP.outputs:execOut", "RearRTSP.inputs:execIn"),
            ("FrontRP.outputs:renderProductPath", "FrontRTSP.inputs:renderProductPath"),
            ("RearRP.outputs:renderProductPath", "RearRTSP.inputs:renderProductPath"),
        ],
    },
)
```

The two streams above are addressable as `rtsp://localhost:8554/front` and
`rtsp://localhost:8555/rear`. Each helper owns its own RTSP server, so a
client connecting to one stream does not affect the other.

## Frame Metadata

In H.264 mode, each frame carries a Supplemental Enhancement Information
(SEI) Network Abstraction Layer (NAL) unit with a JSON payload. The payload uses the fixed UUID
`aa71e48f-0711-5d80-a247-cd31ca6fa49c`, derived from
`isaacsim.streaming.rtsp.sei_metadata`, so consumers can identify and filter
the metadata stream. The schema is:

```python
{
    "publish_sim_time_ns": 1500000000,
    "timestamp_iso8601": "2026-01-01T12:00:01.500Z",
    "timestamp": 1767268801500000000,
    "frame_num": 42
}
```

* `publish_sim_time_ns` â simulation time at frame capture, in
  nanoseconds. Reset to zero when the timeline stops and restarts.
* `timestamp_iso8601` â wall-clock timestamp anchored to the moment the
  RTSP server started, advanced by `publish_sim_time_ns`. Useful for
  correlating with logs and other wall-clock-stamped streams.
* `timestamp` â the same instant as `timestamp_iso8601`, expressed as
  nanoseconds since the Unix epoch.
* `frame_num` â monotonically increasing frame counter, starting at `1`
  and reset on detach.

Downstream tools that parse SEI NAL units (for example a custom
`rtspsrc` callback in GStreamer, or NVIDIA DeepStreamâs metadata API) can
recover the payload by matching the UUID and decoding the JSON bytes.

## Attaching the Writer Directly

For workflows that already drive Replicator from Python and donât need the
OmniGraph layer (custom SDG scripts, batch jobs, headless services),
`isaacsim.streaming.rtsp.RTSPStreamWriter` can be attached to a
render product directly. The writer is registered with Replicatorâs
`WriterRegistry` on extension startup and accepts `port`, `mountPath`,
`encoding`, `width`, and `height` parameters. Author the SRTX
`LdrColor` `RenderVar` on the render product first via
`isaacsim.streaming.rtsp.impl.render_var_utils.ensure_render_var_on_product`,
then attach the writer:

```python
import omni.kit.app
import omni.replicator.core as rep
import omni.usd
from pxr import UsdGeom

ext_mgr = omni.kit.app.get_app().get_extension_manager()
ext_mgr.set_extension_enabled_immediate("isaacsim.core.nodes", True)
ext_mgr.set_extension_enabled_immediate("isaacsim.streaming.rtsp", True)

from isaacsim.streaming.rtsp import RTSPStreamWriter
from isaacsim.streaming.rtsp.impl.render_var_utils import ensure_render_var_on_product

stage = omni.usd.get_context().get_stage()
UsdGeom.Camera.Define(stage, "/Camera")

render_product = rep.create.render_product("/Camera", (1280, 720))

success, _rv_path = ensure_render_var_on_product(stage, render_product.path, "LdrColor", "h264")
if not success:
    raise RuntimeError(f"Failed to create LdrColor render var on {render_product.path}")

writer = RTSPStreamWriter(
    port=8554,
    mountPath="/stream",
    encoding="h264",
    width=1280,
    height=720,
)
writer.attach([render_product])
```

After attaching the writer, start Replicator capture or play the timeline to
produce frames. The RTSP server starts when the writer receives the first
frame.

## Server Lifecycle

The RTSP server starts the first time the writer receives a frame and stops
when the writer detaches. `RTSPCameraHelper` ties this lifecycle to the
timeline:

* **Play** â the action graph runs, the writer attaches to the render
  product, and the server starts on the first frame.
* **Stop** â the writer detaches, the server is torn down, and the port
  is released.
* **Setting** `enabled` **to** `false` â same effect as **Stop** for
  that helper.

If the RTSP server encounters an unrecoverable error during streaming (for
example a connection failure or NVENC error), the writer logs the error,
shuts down its server, and silently skips subsequent frames until the
timeline restarts. This prevents a broken stream from spamming the log or
blocking the simulation loop.

## Troubleshooting

The stream URL refuses connections
:   The RTSP server starts only after the first rendered frame. Press
    **Play** and confirm the timeline is advancing. If the writer logged a
    setup error (for example ârender product has no resolution attributeâ),
    the server never started. Check the carb log for details.

Port already in use
:   Another process (or another `RTSPCameraHelper` in the same scene) is
    already bound to the port. Pick a unique port per helper and verify that
    nothing else is listening with `ss -ltnp | grep 8554`.

Stream stops mid-run and never recovers
:   The writer enters a âfailedâ state on the first encoder or transport
    error, drops further frames silently, and waits for the timeline to
    restart. Stop and restart the timeline (or toggle `enabled`) to retry it.

SEI metadata is missing
:   SEI metadata is only injected in H.264 mode. Set `useRawEncoding` to
    `false` (the default).

On this page

* [Prerequisites](#prerequisites)
* [Streaming a Camera](#streaming-a-camera)
  + [Building the Graph in the Editor](#building-the-graph-in-the-editor)
  + [Building the Graph from a Script](#building-the-graph-from-a-script)
  + [Connecting a Client](#connecting-a-client)
* [Stream Parameters](#stream-parameters)
* [Encoding Modes](#encoding-modes)
  + [H.264 (Default, Recommended)](#h-264-default-recommended)
  + [Raw](#raw)
* [Streaming Multiple Cameras](#streaming-multiple-cameras)
* [Frame Metadata](#frame-metadata)
* [Attaching the Writer Directly](#attaching-the-writer-directly)
* [Server Lifecycle](#server-lifecycle)
* [Troubleshooting](#troubleshooting)

---


## 架构参考

### Reference Architecture (re-fetch for Sim2Real context)

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/introduction/reference_architecture.html

* Reference Architecture and Task Groupings

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Reference Architecture and Task Groupings

Isaac Sim is typically installed and used as one part of a larger solution. Depending on your use case and requirements, this document provides a reference architecture. Almost all use-cases involve some commonalities, which are highlighted as task groupings in the diagrams below. Within each task grouping your product architecture could include one or more of the products or components that are listed.

Regardless of your product components, most Isaac Sim use cases involve the following high level task groupings that occur in roughly the same order:

1. Geometry Authoring

* [SimReady Assets](https://developer.nvidia.com/omniverse/simready-assets)
* [Isaac Sim Assets](../assets/usd_assets_overview.html#isaac-assets-overview)

2. Importing Assets

* [Importers and Exporters](../importer_exporter/importers_exporters.html#isaac-sim-importers-and-exporters)
* [USD Tools](../omniverse_usd/index.html#isaac-sim-app-omniverse-usd-tools)

3. Scene Setup

* [Robot Setup Tools and Standards](../robot_setup/index.html#isaac-sim-robot-setup)
* [Robot Setup Tutorials](../robot_setup_tutorials/index.html#isaac-sim-robot-setup-tutorials)
* [Synthetic Sensors](../sensors/index.html#isaac-sim-sensor-simulation)

4. Interaction with the Digital Twin

* [Robot Simulation and Controllers](../robot_simulation/index.html#isaac-sim-robot-simulation)
* [Robot Articulation and Physics Tools](../physics/index.html#isaac-sim-physics)
* [Motion Generation](../manipulators/concepts/index.html#isaac-sim-motion-generation)
* [OmniGraph](../omnigraph/index.html#isaac-sim-omnigraph-overview-page)

5. Use Cases

* [Isaac Lab](../isaac_lab_tutorials/index.html#isaac-lab-tutorials-page)
* [Synthetic Data Generation](../synthetic_data_generation/index.html#isaac-synthetic-data-generation-page)
* [ROS 2 Bridge](../ros2_tutorials/index.html#isaac-ros2-tutorials-page)
* [Isaac ROS](../nvidia_isaac_ros/isaac_ros_tutorials.html#isaac-sim-app-isaac-ros-tutorials)

Typical use-cases are summarized in [Use Cases](#isaac-sim-ra-consumption).

## Geometry Authoring

The simulation environment (scene) is composed of various components including robots,
static, and dynamic objects. The mechanical and geometrical design for these components
is usually done with CAD software like Solidworks, Pro-E, Catia, AutoCad, or Creo. Parts and
components of varying complexity can be designed and assembled.

Developers can also leverage existing 3D asset libraries, which provide a vast collection of
existing 3D assets. Omniverse and Isaac Sim leverage a file format called [Universal Scene
Description (OpenUSD)](https://www.nvidia.com/en-us/omniverse/usd/).

All assets need to be converted to OpenUSD before they can be used with Isaac Sim, and the default unit for Isaac Sim is meters.

NVIDIA provides a vast collection of OpenUSD âSimReadyâ assets. [SimReady](https://developer.nvidia.com/omniverse/simready-assets), or
simulation-ready, assets are physically accurate 3D objects that have accurate
physical properties, behavior, and connected data streams that are used to represent the real world in
simulated digital worlds. Developers can use these building blocks to construct scenes and
generate data per their requirements. The Warehouse asset collection includes over
800 3D assets of commonly available tools, equipment, and items in a warehouse including
forklifts, pallets, racks, and shelves.

## Importing Assets

There are extensions that enable importing CAD (Computer Aided Design) files into Isaac Sim
that handle conversion to OpenUSD. Extensions are core building blocks that
interact with and add or extend the functionality of Isaac Sim.

### Importing and Creating Environments

The [asset importer](https://docs.omniverse.nvidia.com/extensions/latest/ext_asset-importer.html#asset-importer)
can be leveraged for importing OBJ, FBX, and glTF formats. The [CAD converter](https://docs.omniverse.nvidia.com/extensions/latest/ext_cad-converter.html#cad-converter)
extension supports a variety of popular CAD files from applications including
Catia, Solidworks, AutoCad, and Creo. This enables you to quickly convert and
import your environment into Isaac Sim.

OpenUSD Connections and Data Exchange, formerly Omniverse Connect, is a collection of
[importers](https://docs.omniverse.nvidia.com/connect/latest/catalog.html#importers-exporters),
[exporters](https://docs.omniverse.nvidia.com/connect/latest/catalog.html#exporters),
[converters](https://docs.omniverse.nvidia.com/connect/latest/catalog.html#converters), and
[USD file format](https://docs.omniverse.nvidia.com/connect/latest/catalog.html#file-format-plugins) plug-ins. They enable various 3D applications, products, and file formats to exchange data using OpenUSD.

Some CAD applications have connectors with Omniverse, which allows them to bring over more relevant
and contextual information when converting to USD. For example, PTC Creo, Autodesk Revit, or Autodesk Alias have corresponding connectors. The files generated
from their CAD converters will have all the visual meshes represented in OpenUSD.

### Importing Robots

Isaac Sim comes with a variety of robots already imported. The pre-imported robots can be found on the [Robot Assets](../assets/usd_assets_robots.html#isaac-assets-robots) page. Isaac Sim also provides advanced options for importing other robots.

If your robot is in [URDF](https://wiki.ros.org/urdf), you can use the [URDF Importer Extension](../importer_exporter/ext_isaacsim_asset_importer_urdf.html#isaac-sim-urdf-importer) extension from the GUI or from Python. This extension will import the visual meshes and the prim hierarchies (child-parent relationships), along with extra information about how the collision meshes, joints, and sensors are encoded.

You could also use the [Onshape Importer](https://docs.omniverse.nvidia.com/extensions/latest/ext_onshape.html) and [MJCF Importer Extension](../importer_exporter/ext_isaacsim_asset_importer_mjcf.html#isaac-sim-mjcf-importer). With these importers, you will have to add the joint drives in
and may have to tune them. The [Gain Tuner Extension](../robot_setup/ext_isaacsim_robot_setup_gain_tuner.html#isaac-gain-tuner) allows you to visualize and tune the joints.

## Scene Setup

You can set up the scene after all the necessary assets are converted to OpenUSD and
imported into Isaac Sim.

To properly simulate real world situations, you must have physics characteristics defined. For example, physics characteristics define if an object is subject to gravity or how solid it is.

### Adding Physics

After importing the required assets into Isaac Sim, make sure they have appropriate
Physics for accurate simulations. Some asset importers like the URDF and Onshape Importer carry over
most Physics parameters and configurations, for the rest of the imported assets adding
physics before proceeding would be necessary. The [NVIDIA Omniverseâ¢ Physics simulation
extension](https://docs.omniverse.nvidia.com/extensions/latest/ext_physics.html#physics-core)
is powered by the NVIDIA PhysX SDK. It supports Rigid Body Simulation,
Character Control, Deformable Body Simulation, Particle Simulation, and Articulations. The
important steps for adding Physics to your scene are:

> 1. Creating the physics scene
> 2. Assigning collision settings
> 3. Adding joints and drives.

#### Creating the Physics Scene

The first step is to create a Physics Scene and ensure that the default parameters
for it are acceptable. For example, verify the direction and magnitude of gravity in
the scene. If the imported scene does not contain a ground plane, make sure to add
one before proceeding. It will prevent any physics-enabled objects from falling
below it. Unless you are simulating hundreds of rigid bodies and robots, it is more
efficient to use the CPU solver instead of the GPU solver.
Refer to the [Tutorial 1: Stage Setup](../robot_setup_tutorials/tutorial_intro_environment_setup.html#isaac-sim-app-tutorial-intro-environment-setup) tutorial

#### Assigning Collision Settings

[Collision](https://docs.omniverse.nvidia.com/kit/docs/omni_physics/latest/dev_guide/rigid_bodies_articulations/rigid_bodies.html#create-a-rigid-body-with-a-collider)
enables rigid bodies to interact with each other in an environment. The
geometry of the object can be approximated by convex hull, convex decomposition,
bounding sphere, bounding box, and SDF collision meshes. Each of them
approximates the geometry using different methods and may be better suited for
specific use cases. PhysX supports exact representations for Cube, Capsule, and
Sphere shapes. Cones and Cylinders are supported through the custom geometry
flag and are particularly useful when setting collision approximations for wheels of
robots. [Rigid-body physics materials](https://docs.omniverse.nvidia.com/kit/docs/omni_physics/latest/dev_guide/rigid_bodies_articulations/rigid_bodies.html#configure-rigid-body-s-material-properties)
provide friction, restitution (a.k.a. âbouncinessâ), and material density properties

#### Adding Joints and Drives

After adding the appropriate collision meshes to prims in the scene, we need to
ensure that they interact correctly with one another. We can do this by defining
appropriate joints between prims connected to each other. Joints give you the
ability to connect physics objects by defining how the objects may move relative to
each other. There are various [joints types](https://docs.omniverse.nvidia.com/kit/docs/omni_physics/latest/dev_guide/rigid_bodies_articulations/joints.html)
to select from including revolute, prismatic, spherical, fixed, etc.

### Adding Sensors

Isaac Sim sensor simulation extensions can simulate ground truth perception and
physics-based sensors, and has a library of realistic sensor models. You can simulate
camera, lidar, radar, and physics-based sensors. It is possible to use camera calibration
parameters obtained from OpenCV or ROS by converting them to Isaac Sim units, refer to the [Camera Sensors](../sensors/isaacsim_sensors_camera.html#isaacsim-sensors-camera) page.
RTX Lidar and Radar sensors are simulated at render time on the GPU with RTX hardware. A variety of physics-based sensors
like contact sensors, IMUs sensor, force sensor, effort sensor, and proximity sensor are also included. These sensors can be added
at the appropriate locations in the stage hierarchy (for example, a camera or lidar might be
added near the front/top of the robot). The [Camera and Depth Sensors](../assets/usd_assets_camera_depth_sensors.html#isaac-assets-camera-depth-sensors) and [Non-Visual Sensors](../assets/usd_assets_nonvisual_sensors.html#isaac-assets-nonvisual-sensors) pages
highlight all the available physical sensor assets available with Isaac Sim

### Import and Create Materials

[Materials](https://docs.omniverse.nvidia.com/materials-and-rendering/latest/materials.html#omniverse-materials) in Isaac Sim
are supported using [NVIDIA Material Definition Language (MDL)](https://www.nvidia.com/en-us/design-visualization/technologies/material-definition-language/) ,
a shading language designed for defining and describing the appearance
of materials in computer graphics. It allows artists and developers to create highly realistic
materials by specifying their physical properties, surface characteristics, and how they
interact with light. Omniverse comes with several template materials, including a physically
based glass; several general purpose multi-lobed materials useful for dielectric and
non-dielectric materials, skin, hair, liquids and other materials requiring subsurface
scattering or transmissive effects; and USDâs UsdPreviewSurface.

## Interaction with Digital Twin

Once the assets have been imported and the scene has been set up, there are various ways
to interact with the simulated environment, which are summarized below.

### GUI

The GUI provides intuitive controls for scene management, object manipulation, and
real-time monitoring, providing a streamlined interface for developing and testing robotic
systems. Pre-packaged examples, robots and environments can easily be accessed and
added to the scene via the GUI. Create tools make it easy to assemble, illuminate, simulate,
and render scenes large and small, therefore making it the ideal place to build your virtual
worlds, assemble robots, and examine physics. Refer to the [GUI Reference](../gui/index.html#isaac-sim-gui-tutorials-page) for
getting started with the GUI tutorials.

### Standalone Python

Isaac Sim provides a built-in [Python Environment](../python_scripting/manual_standalone_python.html#isaac-sim-python-environment) that packages can use, like a
system-level Python install. This is the recommended environment for running Python
Scripts with Isaac Sim. All Isaac Sim libraries and dependencies can be imported and
accessed through this Python environment. It also allows users to script and run their
entire worflkow headlessly. For using libraries and tools which are not a part of Isaac Sim,
ensure that they work with Python 3.11 first. A collection of standalone python examples is
provided with Isaac Sim and serves as a good starting point to understand the overall
steps involved. Jupyter notebook and Visual Studio Code support is also available. Workflows from the GUI
can be completely scripted in Python and can be run in headless mode too.

### Extensions

Extensions enable developers to add functionality and integrate other tools for Isaac Sim.
They are individually built application modules. All the tools used in Isaac Sim are built as
extensions. Various extensions enable easier interaction with sensors, robots and prims in
the scene. The ROS 2 Bridge extension can be used to connect your ROS packages and
code to Isaac Sim. Developers can write their own extensions in C++, Python or a
combination of both.

### OmniGraph

[OmniGraph](https://docs.omniverse.nvidia.com/extensions/latest/ext_omnigraph.html) is the visual scripting language
for Omniverse. It is not a single type of graph, but a composition of many different graph systems
under a single framework. Many Isaac Sim extensions provide nodes for building graphs for common
use cases. Core, sensor, and ROS extensions are a few examples that contain such OmniGraph Nodes.

## Use Cases

### Synthetic Data Generation (SDG)

Developers can generate physically accurate synthetic data that can enhance the training
and performance of AI perception networks used for robotics using
[Omniverse Replicator](https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator.html).
Replicator is a collection of extensions, Python APIs, workflows, and tools that enable
synthetic data generation tasks.

Once the scene has been set up, Replicator can be used to modify and randomize various
features like position, rotation, lighting, size, and textures of assets in the scene. A wide
range of annotations are supported including 2D bounding boxes, 3D bounding boxes,
semantic and instance segmentation masks, normals, depth, pointclouds, and more, with
data being written in common formats like COCO and KITTI formats. Custom annotators
and writers can also be implemented for advanced use cases like pose estimation. This
enables developers to seamlessly integrate the generated data with their training pipelines

To get started, developers can leverage the Python API provided by Omniverse Replicator
for generating synthetic data. The same scripts can be used to generate data headlessly in
the cloud through the Isaac Sim docker container (instructions [Container Installation](../installation/install_container.html#isaac-sim-app-install-container))
on a developerâs preferred CSP (AWS, Alibaba, Azure, GCP) with the [Cloud Deployment](../installation/install_cloud.html#isaac-sim-app-install-cloud) guide.
[Replicator YAML](https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator/yaml_workflow.html#replicator-yaml)
can be used for low-code situations where scripts can easily be edited by non-technical experts.
They offer a high level of portability and care suitable for cloud use cases.

### Software in the Loop (SIL)

Once the simulation scenario has been set up, developers can tune and test various
aspects of their robotics software stack. The insights gained after varying parameters and
configurations of the software stack and the simulated robot enable an easier and
accurate transition to the physical real-world robot. A few common use cases are
highlighted below:

#### Single and Multi-Robot Navigation

The navigation stack for a robot can be easily tested in various scenarios. The assets in the
environment can be randomized to come up with these scenarios. For running navigation
with multiple robots, a multi-GPU setup can be leveraged. Isaac Sim supports the ROS 2
Nav2 stack via the ROS 2 Bridge.

#### AI Model Evaluation

Evaluating models is easy in simulation because of direct access to ground truth which
could be through Physics, the state of a robot, or reading of a sensor. These can then be
compared with the model predictions to obtain the evaluation metrics.

For example, in computer vision tasks, the rendered image from the simulated camera can
be passed through the model for obtaining predictions. This can then be compared with
the ground truth (available directly from simulation or via Replicator) to obtain evaluation
metrics. This can also be done for other sensors like Lidars and can be easily extended to
multimodal applications

#### Perception

[Isaac Perceptor](https://developer.nvidia.com/isaac/perceptor) is a reference workflow of
NVIDIA-accelerated libraries and AI models that helps you quickly build robust autonomous
mobile robots (AMRs) to perceive, localize, and operate in unstructured environments like
warehouses or factories. It works with inputs from simulated environments in Isaac Sim

#### Manipulation

[Isaac Manipulator](https://nvidia-isaac-ros.github.io/reference_workflows/isaac_manipulator/index.html)
can be leveraged for manipulation tasks and verified in simulation. It is a
collection of GPU-accelerated packages for perception driven manipulation, providing
capabilities such as object detection and pose estimation. Time optimal collision-free
motion can be generated with cuMotion. Nvblox can be used for local 3D reconstruction
and obstacle detection. MoveIt is also supported via the ROS Bridge in Isaac Sim.

#### Reinforcement Learning

[Isaac Lab](../isaac_lab_tutorials/index.html#isaac-lab-tutorials-page) is a united and modular framework for robot learning that aims to simplify
common workflows in robotics research (such as RL, learning from demonstrations, and
motion planning). It is built upon NVIDIA Isaac Sim.

### Hardware in the Loop (HIL)

Hardware in the loop testing and evaluation can be done with Isaac Sim. The target
deployment device will receive all the data from the simulated robot and sensors which can
be fed to the needed software stacks/algorithms. ROS 2 can be leveraged as the
middleware which handles sending and receiving all the data from the simulation computer
to the target device. For example, a simulated camera from Isaac Sim will stream over all
the image data via the ROS 2 bridge from Isaac Sim to an
[NVIDIA Jetson Orin](https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-orin/), the
embedded device on the robot which will run the computer vision application. This is
particularly useful when selecting the target deployment device to verify it can run the
software stack needed before physically setting up the robot.

### CI/CD

#### OSMO

[OSMO](https://developer.nvidia.com/osmo)
is a cloud-native workow orchestration platform that lets you easily scale your
workloads across distributed environments â from on-premises to private and public
cloud. You can now apply for early access.

#### Sizing Calculator

Please refer to the [Isaac Sim Benchmarks](../reference_material/benchmarks.html#isaac-sim-benchmarks) page for Isaac Sim performance benchmarks
across multiple consumer and enterprise hardware configurations.

## Further Reading

Follow the relevant tutorials for a deeper dive into a corresponding section.

On this page

* [Geometry Authoring](#geometry-authoring)
* [Importing Assets](#importing-assets)
  + [Importing and Creating Environments](#importing-and-creating-environments)
  + [Importing Robots](#importing-robots)
* [Scene Setup](#scene-setup)
  + [Adding Physics](#adding-physics)
    - [Creating the Physics Scene](#creating-the-physics-scene)
    - [Assigning Collision Settings](#assigning-collision-settings)
    - [Adding Joints and Drives](#adding-joints-and-drives)
  + [Adding Sensors](#adding-sensors)
  + [Import and Create Materials](#import-and-create-materials)
* [Interaction with Digital Twin](#interaction-with-digital-twin)
  + [GUI](#gui)
  + [Standalone Python](#standalone-python)
  + [Extensions](#extensions)
  + [OmniGraph](#omnigraph)
* [Use Cases](#use-cases)
  + [Synthetic Data Generation (SDG)](#synthetic-data-generation-sdg)
  + [Software in the Loop (SIL)](#software-in-the-loop-sil)
    - [Single and Multi-Robot Navigation](#single-and-multi-robot-navigation)
    - [AI Model Evaluation](#ai-model-evaluation)
    - [Perception](#perception)
    - [Manipulation](#manipulation)
    - [Reinforcement Learning](#reinforcement-learning)
  + [Hardware in the Loop (HIL)](#hardware-in-the-loop-hil)
  + [CI/CD](#ci-cd)
    - [OSMO](#osmo)
    - [Sizing Calculator](#sizing-calculator)
* [Further Reading](#further-reading)

---

### Robot Simulation Core Concepts

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/robot_simulation/robot_simulation_core_concepts.html

* [Robot Simulation](index.html)
* Useful Links

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Useful Links

Some important concepts that are useful to understand when working with robot simulation in Isaac Sim are located in the following sections:

* [Physics Simulation Fundamentals](../physics/simulation_fundamentals.html#simulation-fundamentals): Provides basic summary about rigid bodies, colliders, joints, articulation, as well as simulation timelines and steps.
* [Core API Overview](../python_scripting/core_api_overview.html#isaac-sim-app-python-core-api-overview): Provides an overview of how the core API in Isaac Sim interfaces with the physics backend.

---

