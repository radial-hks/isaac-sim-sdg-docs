---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/replicator_tutorials/tutorial_replicator_custom_og_randomizer.html
title: "Custom OG Randomizer"
section: "教程"
module: "01-replicator-core"
checksum: "1efe6ef1d1a065e0"
fetched: "2026-06-21T13:40:17"
---

* [Synthetic Data Generation](../synthetic_data_generation/index.html)
* [Perception Data Generation (Replicator)](index.html)
* Custom Replicator Randomization Nodes

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Custom Replicator Randomization Nodes

This tutorial provides an example of how to create custom randomization nodes for the [omni.replicator](https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator.html "(in Omniverse Extensions)") extension.

## Learning Objectives

The goal of this tutorial is to demonstrate how to create custom [OmniGraph](https://docs.omniverse.nvidia.com/extensions/latest/ext_omnigraph.html "(in Omniverse Extensions)") randomization nodes. These nodes can then be further integrated into the Synthetic Data Generation (SDG) pipeline graph of [Replicator](https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator.html "(in Omniverse Extensions)").

This tutorial will showcase how to:

* Create custom scene randomization Python scripts.
* Wrap the scripts as OmniGraph nodes and manually add them to an existing SDG pipeline graph.
* Encapsulate the OmniGraph nodes as **ReplicatorItems** to be automatically added to the SDG pipeline graph using Replicator’s API.

## Prerequisites

* Familiarity with USD / Isaac Sim APIs for creating custom scene randomizers. See [Randomization Snippets](tutorial_replicator_isaac_randomizers.html#isaac-sim-app-tutorial-replicator-isaac-randomizers) for more details.
* Familiarity with [omni.replicator](https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator.html "(in Omniverse Extensions)") and its randomization API [replicator randomizers](https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator/randomizer_details.html "(in Omniverse Extensions)").
* Basic knowledge of [OmniGraph](https://docs.omniverse.nvidia.com/extensions/latest/ext_omnigraph.html "(in Omniverse Extensions)") and how to create [OmniGraph Nodes](https://docs.omniverse.nvidia.com/kit/docs/omni.graph.docs/latest/dev/WritingNodes.html#omnigraph-nodes).
* Experience running simulations via the [Script Editor](../development_tools/omniverse_script_editor.html#script-editor).

## Implementation

This tutorial will showcase how to create custom scene randomization Python scripts. These scripts will create prims in a new stage and randomize their rotation and locations: **in a sphere**, **on a sphere**, and **between two spheres**.

The following image shows the result after running the randomization in the Script Editor:

Code Explanation

The following functions take as input the radius (or radii) of the spheres and generate a random 3D point on the surface of a sphere, within a sphere, and between two spheres. These points will determine the prim locations.

Randomization Functions

```python
# Generate a random 3D point on the surface of a sphere of a given radius.
def random_point_on_sphere(radius):
    # Generate a random direction by spherical coordinates (phi, theta)
    phi = random.uniform(0, 2 * math.pi)
    # Sample costheta to ensure uniform distribution of points on the sphere (surface is proportional to sin(theta))
    costheta = random.uniform(-1, 1)
    theta = math.acos(costheta)

    # Convert from spherical to Cartesian coordinates
    x = radius * math.sin(theta) * math.cos(phi)
    y = radius * math.sin(theta) * math.sin(phi)
    z = radius * math.cos(theta)

    return x, y, z

# Generate a random 3D point within a sphere of a given radius, ensuring a uniform distribution throughout the volume.
def random_point_in_sphere(radius):
    # Generate a random direction by spherical coordinates (phi, theta)
    phi = random.uniform(0, 2 * math.pi)
    # Sample costheta to ensure uniform distribution of points on the sphere (surface is proportional to sin(theta))
    costheta = random.uniform(-1, 1)
    theta = math.acos(costheta)

    # Scale the radius uniformly within the sphere, applying the cube root to a random value
    # to account for volume's cubic growth with radius (r^3), ensuring spatial uniformity.
    r = radius * (random.random() ** (1 / 3))

    # Convert from spherical to Cartesian coordinates
    x = r * math.sin(theta) * math.cos(phi)
    y = r * math.sin(theta) * math.sin(phi)
    z = r * math.cos(theta)

    return x, y, z

# Generate a random 3D point between two spheres, ensuring a uniform distribution throughout the volume.
def random_point_between_spheres(radius1, radius2):
    # Ensure radius1 < radius2
    if radius1 > radius2:
        radius1, radius2 = radius2, radius1

    # Generate a random direction by spherical coordinates (phi, theta)
    phi = random.uniform(0, 2 * math.pi)
    # Sample costheta to ensure uniform distribution of points on the sphere (surface is proportional to sin(theta))
    costheta = random.uniform(-1, 1)
    theta = math.acos(costheta)

    # Uniformly distribute points between two spheres by weighting the radius to match volume growth (r^3),
    # ensuring spatial uniformity by taking the cube root of a value between the radii cubed.
    r = (random.uniform(radius1**3, radius2**3)) ** (1 / 3.0)

    # Convert from spherical to Cartesian coordinates
    x = r * math.sin(theta) * math.cos(phi)
    y = r * math.sin(theta) * math.sin(phi)
    z = r * math.cos(theta)

    return x, y, z
```

The following snippet creates prims in a new stage and randomizes their rotation and locations using the previously defined functions.

Spawning and Randomizing Prims

```python
stage = omni.usd.get_context().get_stage()
prim_count = 500
prim_scale = 0.1
rad_in = 0.5
rad_on = 1.5
rad_bet1 = 2.5
rad_bet2 = 3.5

# Create the default prims
on_sphere_prims = [stage.DefinePrim(f"/World/sphere_{i}", "Sphere") for i in range(prim_count)]
in_sphere_prims = [stage.DefinePrim(f"/World/cube_{i}", "Cube") for i in range(prim_count)]
between_spheres_prims = [stage.DefinePrim(f"/World/cylinder_{i}", "Cylinder") for i in range(prim_count)]

# Add xformOps and scale to the prims
for prim in chain(on_sphere_prims, in_sphere_prims, between_spheres_prims):
    if not prim.HasAttribute("xformOp:translate"):
        UsdGeom.Xformable(prim).AddTranslateOp()
    if not prim.HasAttribute("xformOp:scale"):
        UsdGeom.Xformable(prim).AddScaleOp()
    if not prim.HasAttribute("xformOp:rotateXYZ"):
        UsdGeom.Xformable(prim).AddRotateXYZOp()
    prim.GetAttribute("xformOp:scale").Set((prim_scale, prim_scale, prim_scale))

# Randomize the prims
for _ in range(10):
    for in_sphere_prim in in_sphere_prims:
        rand_rot = (random.uniform(0, 360), random.uniform(0, 360), random.uniform(0, 360))
        in_sphere_prim.GetAttribute("xformOp:rotateXYZ").Set(rand_rot)
        rand_loc = random_point_in_sphere(rad_in)
        in_sphere_prim.GetAttribute("xformOp:translate").Set(rand_loc)

    for on_sphere_prim in on_sphere_prims:
        rand_rot = (random.uniform(0, 360), random.uniform(0, 360), random.uniform(0, 360))
        on_sphere_prim.GetAttribute("xformOp:rotateXYZ").Set(rand_rot)
        rand_loc = random_point_on_sphere(rad_on)
        on_sphere_prim.GetAttribute("xformOp:translate").Set(rand_loc)

    for between_spheres_prim in between_spheres_prims:
        rand_rot = (random.uniform(0, 360), random.uniform(0, 360), random.uniform(0, 360))
        between_spheres_prim.GetAttribute("xformOp:rotateXYZ").Set(rand_rot)
        rand_loc = random_point_between_spheres(rad_bet1, rad_bet2)
        between_spheres_prim.GetAttribute("xformOp:translate").Set(rand_loc)
```

Script Editor

Snippet to run in the Script Editor:

Full Script Editor Script

```python
import math
import random
from itertools import chain

import omni.replicator.core as rep
import omni.usd
from pxr import UsdGeom

# Generate a random 3D point on the surface of a sphere of a given radius.
def random_point_on_sphere(radius):
    # Generate a random direction by spherical coordinates (phi, theta)
    phi = random.uniform(0, 2 * math.pi)
    # Sample costheta to ensure uniform distribution of points on the sphere (surface is proportional to sin(theta))
    costheta = random.uniform(-1, 1)
    theta = math.acos(costheta)

    # Convert from spherical to Cartesian coordinates
    x = radius * math.sin(theta) * math.cos(phi)
    y = radius * math.sin(theta) * math.sin(phi)
    z = radius * math.cos(theta)

    return x, y, z

# Generate a random 3D point within a sphere of a given radius, ensuring a uniform distribution throughout the volume.
def random_point_in_sphere(radius):
    # Generate a random direction by spherical coordinates (phi, theta)
    phi = random.uniform(0, 2 * math.pi)
    # Sample costheta to ensure uniform distribution of points on the sphere (surface is proportional to sin(theta))
    costheta = random.uniform(-1, 1)
    theta = math.acos(costheta)

    # Scale the radius uniformly within the sphere, applying the cube root to a random value
    # to account for volume's cubic growth with radius (r^3), ensuring spatial uniformity.
    r = radius * (random.random() ** (1 / 3))

    # Convert from spherical to Cartesian coordinates
    x = r * math.sin(theta) * math.cos(phi)
    y = r * math.sin(theta) * math.sin(phi)
    z = r * math.cos(theta)

    return x, y, z

# Generate a random 3D point between two spheres, ensuring a uniform distribution throughout the volume.
def random_point_between_spheres(radius1, radius2):
    # Ensure radius1 < radius2
    if radius1 > radius2:
        radius1, radius2 = radius2, radius1

    # Generate a random direction by spherical coordinates (phi, theta)
    phi = random.uniform(0, 2 * math.pi)
    # Sample costheta to ensure uniform distribution of points on the sphere (surface is proportional to sin(theta))
    costheta = random.uniform(-1, 1)
    theta = math.acos(costheta)

    # Uniformly distribute points between two spheres by weighting the radius to match volume growth (r^3),
    # ensuring spatial uniformity by taking the cube root of a value between the radii cubed.
    r = (random.uniform(radius1**3, radius2**3)) ** (1 / 3.0)

    # Convert from spherical to Cartesian coordinates
    x = r * math.sin(theta) * math.cos(phi)
    y = r * math.sin(theta) * math.sin(phi)
    z = r * math.cos(theta)

    return x, y, z

stage = omni.usd.get_context().get_stage()
prim_count = 500
prim_scale = 0.1
rad_in = 0.5
rad_on = 1.5
rad_bet1 = 2.5
rad_bet2 = 3.5

# Create the default prims
on_sphere_prims = [stage.DefinePrim(f"/World/sphere_{i}", "Sphere") for i in range(prim_count)]
in_sphere_prims = [stage.DefinePrim(f"/World/cube_{i}", "Cube") for i in range(prim_count)]
between_spheres_prims = [stage.DefinePrim(f"/World/cylinder_{i}", "Cylinder") for i in range(prim_count)]

# Add xformOps and scale to the prims
for prim in chain(on_sphere_prims, in_sphere_prims, between_spheres_prims):
    if not prim.HasAttribute("xformOp:translate"):
        UsdGeom.Xformable(prim).AddTranslateOp()
    if not prim.HasAttribute("xformOp:scale"):
        UsdGeom.Xformable(prim).AddScaleOp()
    if not prim.HasAttribute("xformOp:rotateXYZ"):
        UsdGeom.Xformable(prim).AddRotateXYZOp()
    prim.GetAttribute("xformOp:scale").Set((prim_scale, prim_scale, prim_scale))

# Randomize the prims
for _ in range(10):
    for in_sphere_prim in in_sphere_prims:
        rand_rot = (random.uniform(0, 360), random.uniform(0, 360), random.uniform(0, 360))
        in_sphere_prim.GetAttribute("xformOp:rotateXYZ").Set(rand_rot)
        rand_loc = random_point_in_sphere(rad_in)
        in_sphere_prim.GetAttribute("xformOp:translate").Set(rand_loc)

    for on_sphere_prim in on_sphere_prims:
        rand_rot = (random.uniform(0, 360), random.uniform(0, 360), random.uniform(0, 360))
        on_sphere_prim.GetAttribute("xformOp:rotateXYZ").Set(rand_rot)
        rand_loc = random_point_on_sphere(rad_on)
        on_sphere_prim.GetAttribute("xformOp:translate").Set(rand_loc)

    for between_spheres_prim in between_spheres_prims:
        rand_rot = (random.uniform(0, 360), random.uniform(0, 360), random.uniform(0, 360))
        between_spheres_prim.GetAttribute("xformOp:rotateXYZ").Set(rand_rot)
        rand_loc = random_point_between_spheres(rad_bet1, rad_bet2)
        between_spheres_prim.GetAttribute("xformOp:translate").Set(rand_loc)
```

As a next step, custom [OmniGraph Nodes](https://docs.omniverse.nvidia.com/kit/docs/omni.graph.docs/latest/dev/WritingNodes.html#omnigraph-nodes) are created for the randomization functions. The node descriptions and implementations can be found in the following code snippets:

Node Descriptions

OgnSampleInSphere.ogn

```python
{
    "OgnSampleInSphere": {
        "version": 1,
        "description": "Assigns uniformly sampled location in a sphere.",
        "language": "Python",
        "categoryDefinitions": "config/CategoryDefinition.json",
        "categories": ["isaacReplicatorExamples"],
        "icon": "icons/isaac-sim.svg",
        "metadata": {
            "uiName": "Sample In Sphere"
        },
        "inputs": {
            "prims": {
                "type": "target",
                "description": "prims to randomize",
                "default": []
            },
            "execIn": {
                "type": "execution",
                "description": "exec",
                "default": 0
            },
            "radius": {
                "type": "float",
                "description": "sphere radius",
                "default": 1.0
            }
        },
        "outputs": {
            "execOut": {
                "type": "execution",
                "description": "exec"
            }
        }
    }
}
```

OgnSampleOnSphere.ogn

```python
{
    "OgnSampleOnSphere": {
        "version": 1,
        "description": "Assigns uniformly sampled location on a sphere.",
        "language": "Python",
        "categoryDefinitions": "config/CategoryDefinition.json",
        "categories": ["isaacReplicatorExamples"],
        "icon": "icons/isaac-sim.svg",
        "metadata": {
            "uiName": "Sample On Sphere"
        },
        "inputs": {
            "prims": {
                "type": "target",
                "description": "prims to randomize",
                "default": []
            },
            "execIn": {
                "type": "execution",
                "description": "exec",
                "default": 0
            },
            "radius": {
                "type": "float",
                "description": "sphere radius",
                "default": 1.0
            }
        },
        "outputs": {
            "execOut": {
                "type": "execution",
                "description": "exec"
            }
        }
    }
}
```

OgnSampleBetweenSpheres.ogn

```python
{
    "OgnSampleBetweenSpheres": {
        "version": 1,
        "description": "Assigns uniformly sampled between two spheres",
        "language": "Python",
        "categoryDefinitions": "config/CategoryDefinition.json",
        "categories": ["isaacReplicatorExamples"],
        "icon": "icons/isaac-sim.svg",
        "metadata": {
            "uiName": "Sample Between Spheres"
        },
        "inputs": {
            "prims": {
                "type": "target",
                "description": "prims to randomize",
                "default": []
            },
            "execIn": {
                "type": "execution",
                "description": "exec",
                "default": 0
            },
            "radius1": {
                "type": "float",
                "description": "inner sphere radius",
                "default": 0.5
            },
            "radius2": {
                "type": "float",
                "description": "outer sphere radius",
                "default": 1.0
            }
        },
        "outputs": {
            "execOut": {
                "type": "execution",
                "description": "exec"
            }
        }
    }
}
```

Node Implementations

OgnSampleInSphere.py

```python
# SPDX-FileCopyrightText: Copyright (c) 2024-2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import numpy as np
import omni.graph.core as og
import omni.usd
from pxr import Sdf, UsdGeom

class OgnSampleInSphere:
    @staticmethod
    def compute(db) -> bool:
        prim_paths = db.inputs.prims
        if len(prim_paths) == 0:
            db.outputs.execOut = og.ExecutionAttributeState.DISABLED
            return False

        stage = omni.usd.get_context().get_stage()
        prims = [stage.GetPrimAtPath(str(path)) for path in prim_paths]

        radius = db.inputs.radius

        try:
            for prim in prims:
                if not UsdGeom.Xformable(prim):
                    prim_type = prim.GetTypeName()
                    raise ValueError(
                        f"Expected prim at {prim.GetPath()} to be an Xformable prim but got type {prim_type}"
                    )
                if not prim.HasAttribute("xformOp:translate"):
                    UsdGeom.Xformable(prim).AddTranslateOp()
            if radius <= 0:
                raise ValueError(f"Radius must be positive, got {radius}")

        except Exception as error:
            db.log_error(str(error))
            db.outputs.execOut = og.ExecutionAttributeState.DISABLED
            return False

        samples = []
        for _ in range(len(prims)):
            # Generate a random direction by spherical coordinates (phi, theta)
            phi = np.random.uniform(0, 2 * np.pi)
            # Sample costheta to ensure uniform distribution of points on the sphere (surface is proportional to sin(theta))
            costheta = np.random.uniform(-1, 1)
            theta = np.arccos(costheta)

            # Scale the radius uniformly within the sphere, applying the cube root to a random value
            # to account for volume's cubic growth with radius (r^3), ensuring spatial uniformity.
            r = radius * (np.random.random() ** (1 / 3))

            # Convert from spherical to Cartesian coordinates
            x = r * np.sin(theta) * np.cos(phi)
            y = r * np.sin(theta) * np.sin(phi)
            z = r * np.cos(theta)

            samples.append((x, y, z))

        with Sdf.ChangeBlock():
            for prim, sample in zip(prims, samples):
                prim.GetAttribute("xformOp:translate").Set(sample)

        db.outputs.execOut = og.ExecutionAttributeState.ENABLED
        return True
```

OgnSampleOnSphere.py

```python
# SPDX-FileCopyrightText: Copyright (c) 2024-2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import numpy as np
import omni.graph.core as og
import omni.usd
from pxr import Sdf, UsdGeom

class OgnSampleOnSphere:
    @staticmethod
    def compute(db) -> bool:
        prim_paths = db.inputs.prims
        if len(prim_paths) == 0:
            db.outputs.execOut = og.ExecutionAttributeState.DISABLED
            return False

        stage = omni.usd.get_context().get_stage()
        prims = [stage.GetPrimAtPath(str(path)) for path in prim_paths]

        radius = db.inputs.radius

        try:
            for prim in prims:
                if not UsdGeom.Xformable(prim):
                    prim_type = prim.GetTypeName()
                    raise ValueError(
                        f"Expected prim at {prim.GetPath()} to be an Xformable prim but got type {prim_type}"
                    )
                if not prim.HasAttribute("xformOp:translate"):
                    UsdGeom.Xformable(prim).AddTranslateOp()
            if radius <= 0:
                raise ValueError(f"Radius must be positive, got {radius}")

        except Exception as error:
            db.log_error(str(error))
            db.outputs.execOut = og.ExecutionAttributeState.DISABLED
            return False

        samples = []
        for _ in range(len(prims)):
            # Generate a random direction by spherical coordinates (phi, theta)
            phi = np.random.uniform(0, 2 * np.pi)
            # Sample costheta to ensure uniform distribution of points on the sphere (surface is proportional to sin(theta))
            costheta = np.random.uniform(-1, 1)
            theta = np.arccos(costheta)

            # Convert from spherical to Cartesian coordinates
            x = radius * np.sin(theta) * np.cos(phi)
            y = radius * np.sin(theta) * np.sin(phi)
            z = radius * np.cos(theta)

            samples.append((x, y, z))

        with Sdf.ChangeBlock():
            for prim, sample in zip(prims, samples):
                prim.GetAttribute("xformOp:translate").Set(sample)

        db.outputs.execOut = og.ExecutionAttributeState.ENABLED
        return True
```

OgnSampleBetweenSpheres.py

```python
# SPDX-FileCopyrightText: Copyright (c) 2024-2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import numpy as np
import omni.graph.core as og
import omni.usd
from pxr import Sdf, UsdGeom

class OgnSampleBetweenSpheres:
    @staticmethod
    def compute(db) -> bool:
        prim_paths = db.inputs.prims
        if len(prim_paths) == 0:
            db.outputs.execOut = og.ExecutionAttributeState.DISABLED
            return False

        stage = omni.usd.get_context().get_stage()
        prims = [stage.GetPrimAtPath(str(path)) for path in prim_paths]

        radius1 = db.inputs.radius1
        radius2 = db.inputs.radius2

        # Ensure radius1 < radius2
        if radius1 > radius2:
            radius1, radius2 = radius2, radius1

        try:
            for prim in prims:
                if not UsdGeom.Xformable(prim):
                    prim_type = prim.GetTypeName()
                    raise ValueError(
                        f"Expected prim at {prim.GetPath()} to be an Xformable prim but got type {prim_type}"
                    )
                if not prim.HasAttribute("xformOp:translate"):
                    UsdGeom.Xformable(prim).AddTranslateOp()
            if radius1 < 0 or radius2 <= 0:
                raise ValueError(
                    f"Radius must be positive and larger radius larger than 0, got {radius1} and {radius2}"
                )

        except Exception as error:
            db.log_error(str(error))
            db.outputs.execOut = og.ExecutionAttributeState.DISABLED
            return False

        samples = []
        for _ in range(len(prims)):
            # Generate a random direction by spherical coordinates (phi, theta)
            phi = np.random.uniform(0, 2 * np.pi)
            # Sample costheta to ensure uniform distribution of points on the sphere (surface is proportional to sin(theta))
            costheta = np.random.uniform(-1, 1)
            theta = np.arccos(costheta)

            # Uniformly distribute points between two spheres by weighting the radius to match volume growth (r^3),
            # ensuring spatial uniformity by taking the cube root of a value between the radii cubed.
            r = (np.random.uniform(radius1**3, radius2**3)) ** (1 / 3.0)

            # Convert from spherical to Cartesian coordinates
            x = r * np.sin(theta) * np.cos(phi)
            y = r * np.sin(theta) * np.sin(phi)
            z = r * np.cos(theta)

            samples.append((x, y, z))

        with Sdf.ChangeBlock():
            for prim, sample in zip(prims, samples):
                prim.GetAttribute("xformOp:translate").Set(sample)

        db.outputs.execOut = og.ExecutionAttributeState.ENABLED
        return True
```

After this step, the randomizers will be available as nodes in the graph editor. For this tutorial the nodes are already added to the built-in `isaacsim.replicator.examples` extension and are available by default. Other custom nodes created through the OmniGraph tutorial will be accessible through the `omni.new.extension` extension (if the default tutorial-provided extension name was used). An example of accessing the nodes in an action graph is depicted below:

Note

If the custom nodes are not available, the newly created extension needs to be enabled. This can be done by navigating to **Window > Extensions > THIRD PARTY > ``omni.new.extension`` > ENABLED**:

After the OmniGraph randomization nodes are created, they can be manually added to a pre-existing SDG pipeline graph. To create a basic SDG graph, the following snippet can be used in the Script Editor to randomize the rotations of the created cubes every frame.

Basic SDG Pipeline

```python
import omni.replicator.core as rep

cube = rep.create.cube(count=50, scale=0.1)
with rep.trigger.on_frame():
    with cube:
        rep.randomizer.rotation()
```

After the snippet is executed in the Script Editor, the generated graph can be opened at `/Replicator/SDGPipeline` and the custom nodes can be added to the graph. The following image shows the result after the custom nodes are added to the SDG pipeline graph together with the resulting randomization (from the UI using `Tools` > `Replicator` > `Preview` or `Step`):

To avoid manually adding the custom nodes to the SDG pipeline graph, the Replicator API can be used to automatically insert the nodes into the graph. For this purpose, the nodes need to be encapsulated as **ReplicatorItems** using the `@ReplicatorWrapper` decorator. The following code snippet demonstrates how **ReplicatorItems** can be created for the custom nodes:

ReplicatorWrapper

```python
import omni.replicator.core as rep
from omni.replicator.core.scripts.utils import (
    ReplicatorItem,
    ReplicatorWrapper,
    create_node,
    set_target_prims,
)

@ReplicatorWrapper
def on_sphere(
    radius: float = 1.0,
    input_prims: ReplicatorItem | list[str] | None = None,
) -> ReplicatorItem:

    node = create_node("isaacsim.replicator.examples.OgnSampleOnSphere", radius=radius)
    if input_prims:
        set_target_prims(node, "inputs:prims", input_prims)
    return node

@ReplicatorWrapper
def in_sphere(
    radius: float = 1.0,
    input_prims: ReplicatorItem | list[str] | None = None,
) -> ReplicatorItem:

    node = create_node("isaacsim.replicator.examples.OgnSampleInSphere", radius=radius)
    if input_prims:
        set_target_prims(node, "inputs:prims", input_prims)
    return node

@ReplicatorWrapper
def between_spheres(
    radius1: float = 0.5,
    radius2: float = 1.0,
    input_prims: ReplicatorItem | list[str] | None = None,
) -> ReplicatorItem:

    node = create_node("isaacsim.replicator.examples.OgnSampleBetweenSpheres", radius1=radius1, radius2=radius2)
    if input_prims:
        set_target_prims(node, "inputs:prims", input_prims)
    return node

prim_count = 50
prim_scale = 0.1
rad_in = 0.5
rad_on = 1.5
rad_bet1 = 2.5
rad_bet2 = 3.5

# Create the default prims
sphere = rep.create.sphere(count=prim_count, scale=prim_scale)
cube = rep.create.cube(count=prim_count, scale=prim_scale)
cylinder = rep.create.cylinder(count=prim_count, scale=prim_scale)

# Create the randomization graph
with rep.trigger.on_frame():
    with sphere:
        rep.randomizer.rotation()
        in_sphere(rad_in)

    with cube:
        rep.randomizer.rotation()
        on_sphere(rad_on)

    with cylinder:
        rep.randomizer.rotation()
        between_spheres(rad_bet1, rad_bet2)
```

Note

For this tutorial the `create_node` function uses `"isaacsim.replicator.examples.OgnSampleInSphere"` as the node path, this path needs to be replaced in case the custom nodes are not part of the built-in `isaacsim.replicator.examples` extension.

After the snippet is executed in the Script Editor, the custom nodes will be automatically added to the SDG pipeline graph. To trigger the randomization, `Tools` > `Replicator` > `Preview` (or `Step`) can be called from the UI. The following image shows the generated graph and the resulting randomization:

On this page

* [Learning Objectives](#learning-objectives)
* [Prerequisites](#prerequisites)
* [Implementation](#implementation)