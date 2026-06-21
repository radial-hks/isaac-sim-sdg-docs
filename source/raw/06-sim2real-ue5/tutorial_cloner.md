---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/isaac_lab_tutorials/tutorial_cloner.html
title: "Tutorial Cloner"
section: "Isaac Lab (RL)"
module: "06-sim2real-ue5"
checksum: "7fabd8de76d28cf6"
fetched: "2026-06-21T12:48:20"
---

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