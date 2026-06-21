# 进阶可选项：机械臂运动 + 详细传感器 + USD 调优

> Manipulators motion planning + Physics/RTX sensors + OpenUSD tuning (按需采集)
> Isaac Sim 版本: 6.0
> 最后组装: 2026-06-21 13:40 UTC
> 来源页数: 44

---

## 来源链接

- [Manipulators Concepts](https://docs.isaacsim.omniverse.nvidia.com/latest/manipulators/concepts/index.html)
- [Kinematics Solver](https://docs.isaacsim.omniverse.nvidia.com/latest/manipulators/concepts/kinematics_solver.html)
- [Lula RRT](https://docs.isaacsim.omniverse.nvidia.com/latest/manipulators/concepts/lula_rrt.html)
- [Motion Gen API](https://docs.isaacsim.omniverse.nvidia.com/latest/manipulators/concepts/motion_gen_api.html)
- [Motion Policy](https://docs.isaacsim.omniverse.nvidia.com/latest/manipulators/concepts/motion_policy.html)
- [Path Planner](https://docs.isaacsim.omniverse.nvidia.com/latest/manipulators/concepts/path_planner.html)
- [RMPflow](https://docs.isaacsim.omniverse.nvidia.com/latest/manipulators/concepts/rmpflow.html)
- [RMPflow Tuning](https://docs.isaacsim.omniverse.nvidia.com/latest/manipulators/concepts/rmpflow_tuning_guide.html)
- [Trajectory Interface](https://docs.isaacsim.omniverse.nvidia.com/latest/manipulators/concepts/trajectory_interface.html)
- [Configure RMPflow Denso](https://docs.isaacsim.omniverse.nvidia.com/latest/manipulators/manipulators_configure_rmpflow_denso.html)
- [cuRobo](https://docs.isaacsim.omniverse.nvidia.com/latest/manipulators/manipulators_curobo.html)
- [Lula Kinematics](https://docs.isaacsim.omniverse.nvidia.com/latest/manipulators/manipulators_lula_kinematics.html)
- [Lula RRT Tutorial](https://docs.isaacsim.omniverse.nvidia.com/latest/manipulators/manipulators_lula_rrt.html)
- [Lula Trajectory Generator](https://docs.isaacsim.omniverse.nvidia.com/latest/manipulators/manipulators_lula_trajectory_generator.html)
- [RMPflow Tutorial](https://docs.isaacsim.omniverse.nvidia.com/latest/manipulators/manipulators_rmpflow.html)
- [Robot Description Editor](https://docs.isaacsim.omniverse.nvidia.com/latest/manipulators/manipulators_robot_description_editor.html)
- [Motion Generation Overview](https://docs.isaacsim.omniverse.nvidia.com/latest/manipulators/motion_generation_overview.html)
- [Camera Structured Light](https://docs.isaacsim.omniverse.nvidia.com/latest/sensors/isaacsim_sensors_camera_structured_light.html)
- [Physics Sensors Index](https://docs.isaacsim.omniverse.nvidia.com/latest/sensors/isaacsim_sensors_physics.html)
- [Articulation Force](https://docs.isaacsim.omniverse.nvidia.com/latest/sensors/isaacsim_sensors_physics_articulation_force.html)
- [Contact Sensor](https://docs.isaacsim.omniverse.nvidia.com/latest/sensors/isaacsim_sensors_physics_contact.html)
- [Effort Sensor](https://docs.isaacsim.omniverse.nvidia.com/latest/sensors/isaacsim_sensors_physics_effort.html)
- [IMU](https://docs.isaacsim.omniverse.nvidia.com/latest/sensors/isaacsim_sensors_physics_imu.html)
- [Joint State](https://docs.isaacsim.omniverse.nvidia.com/latest/sensors/isaacsim_sensors_physics_joint_state.html)
- [Raycast Sensor](https://docs.isaacsim.omniverse.nvidia.com/latest/sensors/isaacsim_sensors_physics_raycast.html)
- [PhysX Sensors Index](https://docs.isaacsim.omniverse.nvidia.com/latest/sensors/isaacsim_sensors_physx.html)
- [PhysX Generic](https://docs.isaacsim.omniverse.nvidia.com/latest/sensors/isaacsim_sensors_physx_generic.html)
- [PhysX Lidar](https://docs.isaacsim.omniverse.nvidia.com/latest/sensors/isaacsim_sensors_physx_lidar.html)
- [PhysX Lightbeam](https://docs.isaacsim.omniverse.nvidia.com/latest/sensors/isaacsim_sensors_physx_lightbeam.html)
- [PhysX Proximity](https://docs.isaacsim.omniverse.nvidia.com/latest/sensors/isaacsim_sensors_physx_proximity.html)
- [RTX Sensors Index](https://docs.isaacsim.omniverse.nvidia.com/latest/sensors/isaacsim_sensors_rtx.html)
- [RTX Acoustic](https://docs.isaacsim.omniverse.nvidia.com/latest/sensors/isaacsim_sensors_rtx_acoustic.html)
- [RTX Custom](https://docs.isaacsim.omniverse.nvidia.com/latest/sensors/isaacsim_sensors_rtx_custom.html)
- [RTX Lidar](https://docs.isaacsim.omniverse.nvidia.com/latest/sensors/isaacsim_sensors_rtx_lidar.html)
- [RTX Materials](https://docs.isaacsim.omniverse.nvidia.com/latest/sensors/isaacsim_sensors_rtx_materials.html)
- [RTX Radar](https://docs.isaacsim.omniverse.nvidia.com/latest/sensors/isaacsim_sensors_rtx_radar.html)
- [OpenUSD Tuning Index](https://docs.isaacsim.omniverse.nvidia.com/latest/openusd_tuning_tutorials/index.html)
- [Tutorial 01: Setup](https://docs.isaacsim.omniverse.nvidia.com/latest/openusd_tuning_tutorials/tutorial_01_setup.html)
- [Tutorial 02: Asset Structure](https://docs.isaacsim.omniverse.nvidia.com/latest/openusd_tuning_tutorials/tutorial_02_asset_structure.html)
- [Tutorial 03: Inspect Asset](https://docs.isaacsim.omniverse.nvidia.com/latest/openusd_tuning_tutorials/tutorial_03_inspect_asset.html)
- [Tutorial 04: Collider Pairs](https://docs.isaacsim.omniverse.nvidia.com/latest/openusd_tuning_tutorials/tutorial_04_collider_pairs.html)
- [Tutorial 05: Joint Drive Tuning](https://docs.isaacsim.omniverse.nvidia.com/latest/openusd_tuning_tutorials/tutorial_05_joint_drive_tuning.html)
- [Tutorial 06: Joint Gains Tuning](https://docs.isaacsim.omniverse.nvidia.com/latest/openusd_tuning_tutorials/tutorial_06_joint_gains_tuning.html)
- [Tutorial 07: Practice](https://docs.isaacsim.omniverse.nvidia.com/latest/openusd_tuning_tutorials/tutorial_07_practice.html)

---


## USD Tuning

### OpenUSD Tuning Index

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/manipulators/concepts/index.html

* [Robot Setup](../robot_setup/index.html)
* OpenUSD and Tuning Best Practices Tutorial Series

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# OpenUSD and Tuning Best Practices Tutorial Series

This tutorial series gives you the intuition and science of physics tuning for robotic assets in NVIDIA Isaac Sim so that your simulated robots behave realistically. Rigging and tuning complex assets—such as a dexterous hand—is foundational to successful robot learning and simulation. If the asset is not properly configured (collision meshes, mass properties, joint parameters), the simulation will be unstable, inaccurate, and unusable for training and validation.

Over this series, you work hands-on with the Inspire Hand asset in Isaac Sim to inspect the robot USD and asset structure, apply OpenUSD best practices for performance and stability, and tune joint parameters and control gains for stable, critically damped motion.

This series takes approximately 60–90 minutes to complete as a hands-on lab.

## Learning Objectives

By the end of this series, you will be able to:

* **Explain** the end-to-end process for inspecting and preparing robot USD assets for simulation.
* **Apply** best practices to optimize the robot USD for performance and stability.
* **Tune** joint parameters and control gains to achieve stable, critically damped, and realistic robot motion in simulation.

We start by inspecting the robot USD, then configuring collision filters to manage self-collision, and finally tuning joint parameters: drive limits (max force, max velocity) and stiffness and damping with the Gain Tuner. By the end, you will have a stable, functioning robotic hand ready to attach to an arm for a grasping controller.

## Tutorials in This Series

* [Tutorial 1: Setup](tutorial_01_setup.html)
* [Tutorial 2: Asset Structure](tutorial_02_asset_structure.html)
* [Tutorial 3: Inspect Asset](tutorial_03_inspect_asset.html)
* [Tutorial 4: Collider Pairs](tutorial_04_collider_pairs.html)
* [Tutorial 5: Joint Drive Tuning](tutorial_05_joint_drive_tuning.html)
* [Tutorial 6: Joint Gains Tuning](tutorial_06_joint_gains_tuning.html)
* [Tutorial 7: Using the Dexterous Hand in Practice](tutorial_07_practice.html)

To get started, see [Tutorial 1: Setup](tutorial_01_setup.html#isaac-sim-tutorial-tuning-openusd-setup).

On this page

* [Learning Objectives](#learning-objectives)
* [Tutorials in This Series](#tutorials-in-this-series)

---

### OpenUSD Tuning Index

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/openusd_tuning_tutorials/index.html

* [Robot Setup](../robot_setup/index.html)
* OpenUSD and Tuning Best Practices Tutorial Series

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# OpenUSD and Tuning Best Practices Tutorial Series

This tutorial series gives you the intuition and science of physics tuning for robotic assets in NVIDIA Isaac Sim so that your simulated robots behave realistically. Rigging and tuning complex assets—such as a dexterous hand—is foundational to successful robot learning and simulation. If the asset is not properly configured (collision meshes, mass properties, joint parameters), the simulation will be unstable, inaccurate, and unusable for training and validation.

Over this series, you work hands-on with the Inspire Hand asset in Isaac Sim to inspect the robot USD and asset structure, apply OpenUSD best practices for performance and stability, and tune joint parameters and control gains for stable, critically damped motion.

This series takes approximately 60–90 minutes to complete as a hands-on lab.

## Learning Objectives

By the end of this series, you will be able to:

* **Explain** the end-to-end process for inspecting and preparing robot USD assets for simulation.
* **Apply** best practices to optimize the robot USD for performance and stability.
* **Tune** joint parameters and control gains to achieve stable, critically damped, and realistic robot motion in simulation.

We start by inspecting the robot USD, then configuring collision filters to manage self-collision, and finally tuning joint parameters: drive limits (max force, max velocity) and stiffness and damping with the Gain Tuner. By the end, you will have a stable, functioning robotic hand ready to attach to an arm for a grasping controller.

## Tutorials in This Series

* [Tutorial 1: Setup](tutorial_01_setup.html)
* [Tutorial 2: Asset Structure](tutorial_02_asset_structure.html)
* [Tutorial 3: Inspect Asset](tutorial_03_inspect_asset.html)
* [Tutorial 4: Collider Pairs](tutorial_04_collider_pairs.html)
* [Tutorial 5: Joint Drive Tuning](tutorial_05_joint_drive_tuning.html)
* [Tutorial 6: Joint Gains Tuning](tutorial_06_joint_gains_tuning.html)
* [Tutorial 7: Using the Dexterous Hand in Practice](tutorial_07_practice.html)

To get started, see [Tutorial 1: Setup](tutorial_01_setup.html#isaac-sim-tutorial-tuning-openusd-setup).

On this page

* [Learning Objectives](#learning-objectives)
* [Tutorials in This Series](#tutorials-in-this-series)

---

### Tutorial 01: Setup

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/openusd_tuning_tutorials/tutorial_01_setup.html

* [Robot Setup](../robot_setup/index.html)
* [OpenUSD and Tuning Best Practices Tutorial Series](index.html)
* Tutorial 1: Setup

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Tutorial 1: Setup

This tutorial runs in NVIDIA Isaac Sim with the Inspire Hand USD asset. Complete the following setup before starting the tutorials in this series.

## Learning Objectives

In this tutorial, you will:

* Understand the hardware and software requirements for the OpenUSD and Tuning Best Practices series.
* Download the course USD files from **Content** to a local directory `/path/to/Inspire/`.
* Open the starting Inspire Hand scene in Isaac Sim.

## Prerequisites

* Basic familiarity with USD and Isaac Sim (stage, prims, layers).
* Understanding of rigid-body physics (mass, inertia, joints) is helpful but not required.

## Get the Course USD Files

In the file paths used in this tutorial series, replace `/path/to` with the directory that contains your copied `Inspire` folder.

1. In the **Content** browser, go to `IsaacSim/Samples/Rigging/Inspire/`.
2. In the **Content** browser, right-click on the `Inspire` folder and select “Download” to save it to your local machine. Place the downloaded folder so that its path is `/path/to/Inspire/`, replacing `/path/to` with your chosen directory.

In the Content browser, right-click the `Inspire` folder and select “Download” to save the course files locally.

Within `/path/to/Inspire/`, the course files are organized into multiple checkpoint folders:

* `/path/to/Inspire/module_1_start` — Initial Inspire Hand USD `inspire_hand.usda`.
* `/path/to/Inspire/module_3_end-checkpoint_1` — Checkpoint with collision filters configured.
* `/path/to/Inspire/module_4_end-checkpoint_2` — Checkpoint with mimic joints, joint drive maximums, and tuned gains for the finger joints configured.
* `/path/to/Inspire/module_5_end-checkpoint_3` — Checkpoint with all finger and thumb joint gains tuned and authored.

## Open the Starting Scene

1. Open `/path/to/Inspire/module_1_start/inspire_hand.usda` in Isaac Sim.
2. Select the `inspire_hand` prim.

## Summary

This tutorial covered:

* Where the samples live in **Content** and how to copy them so the course root is `/path/to/Inspire/`.
* How the checkpoint folders are laid out under `/path/to/Inspire/`.
* How to open the starting Inspire Hand scene in Isaac Sim.

### Next Steps

Continue to [Tutorial 2: Asset Structure](tutorial_02_asset_structure.html#isaac-sim-tutorial-tuning-openusd-module-1) to learn the USD Asset Structure 3.0 layout for the Inspire Hand.

On this page

* [Learning Objectives](#learning-objectives)
* [Prerequisites](#prerequisites)
* [Get the Course USD Files](#get-the-course-usd-files)
* [Open the Starting Scene](#open-the-starting-scene)
* [Summary](#summary)
  + [Next Steps](#next-steps)

---

### Tutorial 02: Asset Structure

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/openusd_tuning_tutorials/tutorial_02_asset_structure.html

* [Robot Setup](../robot_setup/index.html)
* [OpenUSD and Tuning Best Practices Tutorial Series](index.html)
* Tutorial 2: Asset Structure

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Tutorial 2: Asset Structure

Before you inspect, filter, or tune a robot in Isaac Sim, you need to know **where everything lives**. **USD Asset Structure 3.0** in Isaac Sim 6.0 is the standard layout for robot assets: it organizes geometry, materials, collision meshes, and physics into dedicated files and layers so that the same asset can be used with multiple physics backends (e.g. PhysX, MuJoCo) without clashing or duplication. Once you know this structure, you can open the right file for each task and keep the asset maintainable.

## Learning Objectives

In this tutorial, you will:

* **Understand** how Asset Structure 3.0 separates geometry, materials, metadata, instances, and physics into dedicated files.
* **See** how layers, payloads, and variants let you switch between no physics, generic physics, or PhysX without duplicating the asset.
* **Walk through** the Inspire Hand file hierarchy so you know exactly which file to open for inspection and tuning in later tutorials.

## Prerequisites

* Complete [Tutorial 1: Setup](tutorial_01_setup.html#isaac-sim-tutorial-tuning-openusd-setup) and have the Inspire Hand scene open in Isaac Sim.

## Module 1.1: USD Asset Structure 3.0

Isaac Sim 6.0 introduces multi-physics backend support (e.g., MuJoCo and PhysX). **USD Asset Structure 3.0** is the reference format for robot asset structure and organization. It provides:

* **Separation of USD components** into multiple files for easier reviewing and maintenance.
* **Use of layers, payloads, and variants** for different robot use cases (e.g., animation vs. simulation, different physics engines).
* **Isolation of attributes** for different physics engines to prevent clashing when the same asset is used with MuJoCo, PhysX, or other runtimes.
* **Storage of different physics tuning parameters** per physics engine in separate layers or payloads, so you can switch runtimes without overwriting shared geometry or metadata.

The result is a multi-layered structure where geometry, materials, and metadata are shared, while physics-specific data lives in dedicated files and is composed via payloads and variants. Once you know this layout, you can confidently open the right file for collision filtering (e.g. `physics.usda`) or PhysX-specific joint tuning (e.g. `physx.usda`) without touching the base geometry.

## Module 1.2: Inspire Hand Overview

The **Inspire Hand** (RH56DFX from Inspire Robotics) is the example digital twin used in this tutorial: a compact, underactuated dexterous hand with 6 actuated DOF and 12 joints, specifically chosen for its complexity compared to fully actuated dexterous hands.

| Property | Value |
| --- | --- |
| Model | RH56DFX |
| Degrees of Freedom | 6 |
| Number of joints | 12 |
| Weight | 540 g |
| Max thumb grip | 15 N |
| Max palm grip | 10 N |
| Thumb lateral rot. | 107 deg/s |
| Palm finger bend | 260 deg/s |

Below we see how this robot is represented in USD using the Asset Structure 3.0 layout: file hierarchy, asset stack, and physics stack.

### File Hierarchy and Stacks

* **Inspire Hand File Hierarchy** — The asset is split into multiple USD files (geometry, materials, robot metadata, instances, base scene, physics, and PhysX overrides), each with a clear role.
* **Inspire Hand Asset Stack** — Layers and references compose the visual and structural representation (meshes, materials, transforms, robot API).
* **Inspire Hand Physics Stack** — Payloads and variants add physics (rigid bodies, joints, drives) and engine-specific tuning (e.g., PhysX) without modifying the base asset.

Together, the **combined** stack gives a single `inspire_hand` prim that is simulation-ready and can switch between no physics, generic USD physics, or PhysX via a variant.

## Module 1.3: Asset Structure Walkthrough

Here we walk through each file in the Inspire Hand and how it contributes to the final asset. Knowing each file’s **role** and **format** (e.g. binary for geometry, ASCII for readability) will help you know where to author changes in later modules.

geometries.usd — Mesh file
geometries.usd — Mesh file
————————–

* **Role:** Stores all the **meshes** used by the robot.
* **Format:** Binary (`.usd` or `.usdc`) for efficiency.
* Contains only geometry (mesh data); no materials or physics.

### materials.usda — Material file

* **Role:** Stores all **materials** used by the robot (e.g., Plastic\_ABS).
* **Format:** ASCII (`.usda`) for readability.
* Defines materials and their MDL shader connections (e.g., `info:mdl:sourceAsset`, `inputs:diffuse_tint`). These materials are referenced by the instance file for both visual and collision meshes.

```python
def Material "Plastic_ABS"
{
token outputs:displacement (
    displayGroup = "Outputs"
)
prepend token outputs:mdl:displacement.connect = </Materials/Plastic_ABS/Shader.outputs:out>
prepend token outputs:mdl:surface.connect = </Materials/Plastic_ABS/Shader.outputs:out>
prepend token outputs:mdl:volume.connect = </Materials/Plastic_ABS/Shader.outputs:out>
token outputs:surface (
    displayGroup = "Outputs"
)
token outputs:volume (
    displayGroup = "Outputs"
)

def Shader "Shader" (
    apiSchemas = ["NodeDefAPI"]
)
{
    token info:implementationSource = "sourceAsset"
    asset info:mdl:sourceAsset = @../Materials/Plastic_ABS.mdl@
    token info:mdl:sourceAsset:subIdentifier = "Plastic_ABS"
    color3f inputs:diffuse_tint = (1, 1, 1)
    token outputs:out (
        renderType = "material"
    )
}
```

### robot.usda — Robot metadata

* **Role:** Contains **robot metadata** and the Isaac Robot API.
* Applied as an overlay over the `inspire_hand` prim with `apiSchemas = ["IsaacRobotAPI"]`.
* Typical attributes include: `isaac:changelog`, `isaac:description`, `isaac:license`, `isaac:namespace` (namespace of the prim in Isaac Sim), `isaac:physics:robotJoints` (relationship to robot joints).

This file does not define geometry or physics; it identifies the asset as a robot and attaches metadata.

```python
over "inspire_hand" (
    prepend apiSchemas = ["IsaacRobotAPI"]
)
{
    string[] isaac:changelog (
        displayName = "Changelog"
    )
    string isaac:description (
        displayName = "Description"
    )
    token isaac:license (
        displayName = "License"
    )
    string isaac:namespace (
        displayName = "Namespace"
        doc = "Namespace of the prim in Isaac Sim"
    )
    rel isaac:physics:robotJoints (
        displayName = "Robot Joints"
    )

...
}
```

### instances.usda — Mesh + materials + colliders

* **Role:** Builds **visual and collision** meshes by combining `materials.usda` and `geometries.usd`.
* References geometry from the mesh file and applies materials; adds collision by applying `PhysicsCollisionAPI` and `PhysicsMeshCollisionAPI` (or other collider APIs) on the same or child prims.
* Example pattern for a link (e.g., `r_base_link_1`): an `Xform` references the geometry prim, and a child over adds `physics:approximation` (e.g., `"convexHull"`) and `purpose = "guide"` for collision.

So this file is where “mesh + materials + colliders” are assembled per link.

```python
r_base_link_1 collision definition:

    def Xform "r_base_link_1" (
        prepend references = @geometries.usd@</Geometries/r_base_link>
    )
    {
        over "r_base_link" (
            apiSchemas = ["PhysicsCollisionAPI", "PhysicsMeshCollisionAPI"]
        )
        {
            token physics:approximation = "convexHull"
            token purpose = "guide"
        }
    }
```

### base.usda — Animation-ready scene

* **Role:** **Animation-ready** scene: loads visual/collision meshes as **instanceable** references and applies **transforms** (translate, orient, scale) for each link.
* References `instances.usda` (e.g., `@instances.usda@</Instances/right_thumb_1>`) and uses `instanceable = true` for efficiency.
* Typically sublayers or references `robot.usda` so the root has the robot metadata.
* Defines the kinematic tree and mesh placement; no joint or drive data here.

```python
Right thumb transform and mesh definition:

    def Xform "right_thumb_1"
    {
        quatf xformOp:orient = (1, 0, 0, 0)
        float3 xformOp:scale = (1, 1, 1)
        double3 xformOp:translate = (0.01696, 0.02045, 0.0667)
        uniform token[] xformOpOrder = ["xformOp:translate", "xformOp:orient", "xformOp:scale"]

        def Xform "right_thumb_1" (
            instanceable = true
            prepend references = @instances.usda@</Instances/right_thumb_1>
        )
}
```

### physics.usda — USD physics file

* **Role:** Stores **USD physics attributes**: rigid bodies, mass, and **joints** (with drive and state APIs).
* Links prims to: **PhysicsRigidBodyAPI**, **PhysicsMassAPI**, etc., for bodies; **PhysicsRevoluteJoint** (or other joint types) with **PhysicsDriveAPI** and **PhysicsJointStateAPI** for actuated joints.
* Example: a revolute joint defines `physics:axis`, `physics:body0`/`body1`, `physics:localPos0`/`localPos1`, `physics:localRot0`/`localRot1`, `physics:lowerLimit`/`upperLimit`, `state:angular:physics:position`/`velocity`, and optional URDF-style limits (`urdf:limit:effort`, `urdf:limit:velocity`).

This file is the engine-agnostic physics representation.

```python
def PhysicsRevoluteJoint "right_thumb_1_joint" (
    prepend apiSchemas = ["PhysicsDriveAPI:angular", "PhysicsJointStateAPI:angular"]
)
{
    uniform token physics:axis = "Z"
    custom rel physics:body0
    prepend rel physics:body0 = </inspire_hand/r_base_link>
    custom rel physics:body1
    prepend rel physics:body1 = </inspire_hand/right_thumb_1>
    point3f physics:localPos0 = (0.01696, 0.02045, 0.0667)
    point3f physics:localPos1 = (6.192923e-10, -2.8014183e-10, -3.4093857e-9)
    quatf physics:localRot0 = (-1.6081226e-16, 1, 0, 0)
    quatf physics:localRot1 = (-1.6081226e-16, 1, 0, 0)
    float physics:lowerLimit = 0
    float physics:upperLimit = 75.000175
    float state:angular:physics:position = 0
    float state:angular:physics:velocity = 0
    custom float urdf:limit:effort = 1
    custom float urdf:limit:velocity = 2
}
}
```

### physx.usda — PhysX file

* **Role:** Stores **PhysX-specific** attributes so the same asset can be tuned for PhysX without changing the generic physics file.
* Adds APIs such as **PhysxJointAPI** and **PhysxMimicJointAPI** on top of the joints defined in `physics.usda`.
* Example: a mimic joint uses `physxMimicJoint:rotX:dampingRatio`, `gearing`, `naturalFrequency`, `offset`, `referenceJoint`, and `referenceJointAxis` to drive one joint from another.

Keeps PhysX-only tuning (mimic ratios, solver settings, etc.) in one place and avoids clashing with other physics engines.

```python
over "right_thumb_4_joint" (
    prepend apiSchemas = ["PhysxJointAPI", "PhysxMimicJointAPI:rotX"]
)
{
    bool[] isaac:actuator (
        displayName = "Actuator"
    )
    string isaac:NameOverride (
        displayName = "Joint Name Override"
    )
    token[] isaac:physics:DofOffsetOpOrder (
        displayName = "Dof Offset Op Order"
    )
    float physxMimicJoint:rotX:dampingRatio = 0.005
    float physxMimicJoint:rotX:gearing = -0.7508
    float physxMimicJoint:rotX:naturalFrequency = 25
    float physxMimicJoint:rotX:offset = 0.1
    rel physxMimicJoint:rotX:referenceJoint = </inspire_hand/Physics/right_thumb_3_joint>
    uniform token physxMimicJoint:rotX:referenceJointAxis = "rotZ"
}
}
```

### inspire\_hand.usda — The interface

* **Role:** **The interface** that ties everything together: references the base scene and selects physics via **variants**.
* Root prim references the base (e.g., `prepend references = @payloads/base.usda@`) and declares `variantSet "Physics"` with options such as: `"none"` (no physics payload), `"physics"` (payload `payloads/Physics/physics.usda`), `"physx"` (payload `payloads/Physics/physx.usda`).

So a single asset can be loaded as animation-only, with generic physics, or with PhysX, by switching the variant.

```python
def Xform "inspire_hand" (
    prepend references = @payloads/base.usda@
    append variantSets = "Physics"
)
{
    variantSet "Physics" = {
        "none" {
        }
        "physics" (
            prepend payload = @payloads/Physics/physics.usda@
        ) {

        }
        "physx" (
            prepend payload = @payloads/Physics/physx.usda@
        ) {

        }
    }
}
}
```

## Summary

This tutorial covered:

* **USD Asset Structure 3.0**: geometry, materials, metadata, instances, base scene, and physics live in dedicated files so you can find and edit the right layer without clashing with others.
* How **layers, payloads, and variants** compose the Inspire Hand and let you switch between no physics, generic physics, or PhysX from a single asset.
* The role of each file—from **geometries.usd** and **materials.usda** through **physics.usda** and **physx.usda**—so you know where to author collision filters and joint parameters in later tutorials.

## Next Steps

Continue to [Tutorial 3: Inspect Asset](tutorial_03_inspect_asset.html#isaac-sim-tutorial-tuning-openusd-module-2) to enable the joint visualizer and verify mass, inertia, and collision meshes before collision filtering.

On this page

* [Learning Objectives](#learning-objectives)
* [Prerequisites](#prerequisites)
* [Module 1.1: USD Asset Structure 3.0](#module-1-1-usd-asset-structure-3-0)
* [Module 1.2: Inspire Hand Overview](#module-1-2-inspire-hand-overview)
  + [File Hierarchy and Stacks](#file-hierarchy-and-stacks)
* [Module 1.3: Asset Structure Walkthrough](#module-1-3-asset-structure-walkthrough)
  + [materials.usda — Material file](#materials-usda-material-file)
  + [robot.usda — Robot metadata](#robot-usda-robot-metadata)
  + [instances.usda — Mesh + materials + colliders](#instances-usda-mesh-materials-colliders)
  + [base.usda — Animation-ready scene](#base-usda-animation-ready-scene)
  + [physics.usda — USD physics file](#physics-usda-usd-physics-file)
  + [physx.usda — PhysX file](#physx-usda-physx-file)
  + [inspire\_hand.usda — The interface](#inspire-hand-usda-the-interface)
* [Summary](#summary)
* [Next Steps](#next-steps)

---

### Tutorial 03: Inspect Asset

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/openusd_tuning_tutorials/tutorial_03_inspect_asset.html

* [Robot Setup](../robot_setup/index.html)
* [OpenUSD and Tuning Best Practices Tutorial Series](index.html)
* Tutorial 3: Inspect Asset

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Tutorial 3: Inspect Asset

You’ve seen how the Inspire Hand is built from multiple USD files (Tutorial 2). Next we **inspect and validate** that asset: joints, mass and inertia, and collision meshes. Skipping this step means you’re tuning in the dark—wrong masses or misaligned inertia can cause unstable or unrealistic motion even when joint parameters look correct, and the wrong collider type can slow the simulation or produce confusing contact behavior. Isaac Sim’s **joint visualizer**, **Robot Inspector**, **Physics Debugger**, and **collider visualization** give you a clear picture of the asset before you filter collision pairs or tune drives.

## Learning Objectives

In this tutorial, you will:

* **Enable** the joint visualizer and interpret joint types.
* **Enable** mass and inertia visualization.
* **Verify** collision meshes and collider types.

## Prerequisites

* Complete [Tutorial 2: Asset Structure](tutorial_02_asset_structure.html#isaac-sim-tutorial-tuning-openusd-module-1).
* Have the Inspire Hand scene open in Isaac Sim with the PhysX variant selected.

## Module 2.1: Enable Joint Visualizer

Because we’re tuning for the PhysX backend, load the hand with the PhysX variant. Then enable joint visualization to see joint locations and types at a glance.

**Viewport Navigation in Isaac Sim**

* **Orbit the camera:** Hold **Alt** and left mouse button, then drag.
* **Rotate in place (look around):** Hold right mouse button and move the mouse.
* **Zoom:** Hold **Alt** and right mouse button (or use the scroll wheel).
* **Pan:** Hold the middle mouse button and drag.
* **Focus the camera on a prim:** Select the desired prim in the *Stage* panel, then press **F**.

Use these controls to efficiently explore and inspect the Inspire Hand model as you follow the instructions below.

1. Open `/path/to/Inspire/module_1_start/inspire_hand.usda` in Isaac Sim.
2. Select the top-level `inspire_hand` prim.
3. In the *Property* panel, scroll to **Variants** and select **PhysX**.

1. Go to **Eye > Show by Type > Physics > Joints** to enable joint visualization.

In the viewport, the Inspire Hand should now have gizmos identifying the locations and types of each joint.

**Examine the joints** — In the *Stage* panel, under the `/Physics` scope, find `right_index_1_joint`—a **Revolute** joint responsible for the base motion of the index finger, represented by a circular icon in the viewport. Also locate `right_index_rubber_1_joint`, which is a **Fixed** joint attaching the lower index rubber pad to its link, shown as a rectangular icon in the visualization. The `right_index_2_joint` is a mimic joint that references the movement of `right_index_1_joint` (we’ll cover mimic joints in more detail in Tutorial 5). Understanding how these joints function and their naming conventions will be valuable when tuning the drives in Tutorials 5 and 6.

## Module 2.2: Robot Inspector (hierarchy and session masking)

With joint gizmos visible in the viewport, the [Robot Inspector Window](../robot_setup/robot_inspector.html#isaac-sim-robot-inspector-window) gives you the same articulation as a structured **link â joint** tree—often easier to scan than hunting only under `/Physics` when payloads and scopes spread prims across layers.

1. Open **Window > Robot Inspector**. The window docks next to *Stage* by default.
2. In the robot list, select the entry for the **Inspire Hand**.
3. Set the hierarchy mode to **Tree** (default): parent link â joint â child link.
4. Optionally switch to **Flat** (all links, then all joints) or **MuJoCo** (base-rooted body tree) to compare layouts; the same underlying articulation can be shown in three different ways.

The **Deactivate**, **Bypass**, and **Anchor** columns apply **transient** opinions on a dedicated session sublayer—they are **not** saved to your USD files. That is useful for quick isolation during debugging.

See also

Icons and behavior for **Deactivate**, **Bypass**, and **Anchor** are documented under [Component Masking](../robot_setup/robot_inspector.html#isaac-sim-robot-inspector-masking).

When Robot Inspector is open, **joint connection lines** (parent to child, with direction cues) will appear in the viewport when the **Eye Icon > Show by Type > Physics > Joints** is enabled; they are hidden during simulation playback as described in [Robot Inspector Window](../robot_setup/robot_inspector.html#isaac-sim-robot-inspector-window).

## Module 2.3: Verify Mass and Inertia Properties

Mass and inertia define how each link responds to forces. If the principal inertia axes are misaligned with the link geometry, or if mass values are too small or too large, the hand can behave unrealistically. The **Physics Debugger** lets you visualize body axes and **Body Mass Axes** (principal inertia) so you can spot problems before running the simulation.

1. Open **Utilities > Physics Debugger**. The *Physics Debug* panel appears.

1. In **Simulation Debug Visualization**:

   * Check **Enabled**.
   * Check **Body Axes** to show coordinate frames.
   * Check **Body Mass Axes** to show principal inertia axes.
2. In **Simulation Control**, click **Step** to run one simulation frame and display the visualization.

Warning

Avoid pressing **Play** at this stage, as it may cause Isaac Sim to crash. Instead, use **Simulation Control** to either **Run** the physics simulation or **Step** through it one frame at a time.

1. For each link, you can now verify:

   * Mass centers sit appropriately within the link.
   * Principal inertia axes align with the link geometry.
   * Inertia values look plausible (not excessively small or large).

Note

Misaligned principal inertia axes can cause unstable or unrealistic motion. The image below shows an example of misalignment.

### Alternative Method: Inspecting Mass and Inertia via the Physics Toolbar

You can also inspect mass and inertia properties using the Physics Toolbar:

1. Go to **Tools > Physics Toolbar**.

1. In the toolbar, toggle on both the **Rigid Body Selection Mode** (cube icon) and the **Mass Distribution Manipulator** (balance icon).
2. In the viewport, select any rigid body prim on the hand. The **Mass Properties Info** will be displayed, providing details about the total mass, center of mass, principal axis, and diagonal inertia directly in the viewport.

This method lets you quickly inspect and debug mass distribution for any body in the scene without navigating to the *Property* panel.

## Module 2.4: Verify Collision Meshes

The shapes you see in the viewport aren’t necessarily what the physics engine uses for contact—that’s determined by the **collision meshes** (colliders). Before we filter collision pairs in Tutorial 4, we inspect and verify the colliders: colliders are color-coded **green** for rigid bodies and **magenta** for static bodies.

1. Go to **Eye > Show by Type > Physics > Colliders > All** to visualize all collision shapes.

Setting collider types affects performance and fidelity. You can mix types on one asset. For dexterous hands, **Convex Hull** is often used for parts that do not need high accuracy (e.g. palm), and **Convex Decomposition** for parts that need accurate contact (e.g. fingertips). Convex Decomposition gives the best shapes but costs more than Convex Hull or geometry-based colliders. In this tutorial we use **Convex Hull** for all parts.

## Summary

This tutorial covered:

* Enabling the **joint visualizer** and identifying joint types (Fixed, Revolute, Mimic) in the Stage—the same structure you’ll tune in Tutorials 5 and 6.
* Opening **Robot Inspector** to review the hand’s kinematic hierarchy (Flat / Tree / MuJoCo modes) and understanding **session masking**.
* Using the **Physics Debugger** to visualize body axes and principal inertia and verifying that mass centers and inertia alignment look correct for each link.
* Turning on **collider visualization** and confirming the collider strategy (Convex Hull for this series), so you know what shapes will collide when self-collisions are enabled in Tutorial 4.

## Next Steps

Continue to [Tutorial 4: Collider Pairs](tutorial_04_collider_pairs.html#isaac-sim-tutorial-tuning-openusd-module-3) to work through self-collision pairs with the Robot Self-Collision Detector, inspect collision geometry with the Physics Debugger as needed, and add filtered pairs.

On this page

* [Learning Objectives](#learning-objectives)
* [Prerequisites](#prerequisites)
* [Module 2.1: Enable Joint Visualizer](#module-2-1-enable-joint-visualizer)
* [Module 2.2: Robot Inspector (hierarchy and session masking)](#module-2-2-robot-inspector-hierarchy-and-session-masking)
* [Module 2.3: Verify Mass and Inertia Properties](#module-2-3-verify-mass-and-inertia-properties)
  + [Alternative Method: Inspecting Mass and Inertia via the Physics Toolbar](#alternative-method-inspecting-mass-and-inertia-via-the-physics-toolbar)
* [Module 2.4: Verify Collision Meshes](#module-2-4-verify-collision-meshes)
* [Summary](#summary)
* [Next Steps](#next-steps)

---

### Tutorial 04: Collider Pairs

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/openusd_tuning_tutorials/tutorial_04_collider_pairs.html

* [Robot Setup](../robot_setup/index.html)
* [OpenUSD and Tuning Best Practices Tutorial Series](index.html)
* Tutorial 4: Collider Pairs

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Tutorial 4: Collider Pairs

We inspected the asset structure and collision meshes. Now we tackle a question that makes or breaks this dexterous hand simulation: **which parts of the hand are allowed to collide with each other?** In the real world, a finger can’t pass through the palm, but in simulation, overlapping collision geometry between links can create phantom contacts, jitter, and forces that blow the hand apart. **Filtered Pairs** in Isaac Sim let you turn off collision between specific rigid bodies so you keep the contacts that matter (finger on object, intentional finger-to-finger) and remove the ones that cause instability.

## Learning Objectives

In this tutorial, you will:

* **Explain** how **Filtered Pairs** work and when to use them.
* **Identify** overlapping self-collision pairs with the **Robot Self-Collision Detector** and inspect collision geometry with the **Physics Debugger** as needed.
* **Add** filtered pairs for the palm and pinky using **Filtered Pair** in the detector or **Filtered Pairs** on the *Property* panel, on the **physics.usda** layer.

## Prerequisites

* Complete [Tutorial 3: Inspect Asset](tutorial_03_inspect_asset.html#isaac-sim-tutorial-tuning-openusd-module-2).
* Have the Inspire Hand scene open in Isaac Sim with joint and collider visualization familiar from the previous tutorial.

## Module 3.1: Understanding Filtered Pairs

**Filtered Pairs** explicitly tell the physics engine: “Do not detect collision between these two rigid bodies.” In Isaac Sim, adjacent links (two links connected by a joint) in an articulation don’t self-collide by default, but **non-adjacent** links do. As you will see, many of those non-adjacent links can have overlapping or very close collision geometry. In these scenarios, you can get:

* **Unrealistic forces** — The solver tries to resolve interpenetration between links that would never actually touch in the real mechanism.
* **Instability** — The hand can jitter, jump, or blow apart as conflicting contacts fight each other.
* **Wasted compute** — Simulating every anatomically possible self-contact is rarely necessary for grasping or manipulation.

So the goal is to **filter the problematic pairs** while keeping contacts that you care about (e.g. finger–object, or specific finger–finger contacts). Use filtered pairs judiciously: over-filtering can allow unrealistic interpenetration; under-filtering can cause instability. We’ll turn on self-collisions, run the [Robot Self-Collision Detector](../robot_setup/ext_isaacsim_robot_setup_collision_detector.html#isaac-collision-detector) to see which links overlap at rest, then author filters on **physics.usda**. The Physics Debugger is also available to view solid collision meshes in the viewport while you reason about a pair.

## Module 3.2: Enable self-collision and inspect pairs

**Which pairs should you filter?** At the current configuration, the self-collision detector queries the physics engine for overlapping colliders, maps them to rigid-body links, and shows them in a sortable, searchable table.

Note

For this tutorial we focus on the **pinky** (little finger) as a clear example; the same workflow applies to other fingers or links.

### Step 1: Reproduce the problem

1. Press **Play**. With self-collisions disabled, the simulation is stable. Press **Stop**.

1. Because enabling **Articulation Root** is a PhysX-specific API, we want to make sure we are authoring on the **physx.usda** layer. In the **Layer** tab, click the **Insert Sublayer** icon to add a new sublayer beneath the current layer stack.

1. In the file dialog, navigate to `/path/to/Inspire/module_1_start/payloads/Physics/`, select `physx.usda`, and click **Open** to insert it as a sublayer.

1. Once **physx.usda** appears in the layer stack, **Right-click on physx.usda** and select **Set Authoring Layer**.

You should now see the **physx.usda** layer highlighted green, indicating it is the active authoring layer.

1. In the *Stage* panel, select `r_base_link`. In the *Property* panel, scroll to **Articulation Root** and check **Self Collisions Enabled**.

1. Press **Play** again. Links move erratically as overlapping collision geometry between non-adjacent links is now colliding, and the solver can’t resolve it cleanly.

### Step 2: Run the Robot Self-Collision Detector

With **Self Collisions Enabled** on the articulation root, the physics engine can evaluate which collider pairs overlap in the hand’s current configuration. The detector surfaces those pairs in a docked panel so you can inspect them and conveniently toggle **Filtered Pair**.

Note

If **Self Collisions** on the articulation root are **disabled**, the tool reports no overlapping pairs from the collision engine—see [User Interface](../robot_setup/ext_isaacsim_robot_setup_collision_detector.html#isaac-collision-detector-ui). Keep self-collisions **on** for this tutorial.

1. Press **Stop** if the simulation is still running so the hand returns to a stable pose for analysis.
2. Open **Tools > Robotics > Asset Editors > Robot Self-Collision Detector**.
3. In the **Robot** dropdown, select the **Inspire Hand**.
4. Leave **Include environment collisions** off unless you have added props; we only need self-pairs for this exercise.
5. Click **Check Collisions**. The table fills with **Rigid Body A** and **Rigid Body B** for each overlapping pair.

1. Use the **search** field or column sort to find rows that involve the pinky and palm—for example pairs that include `r_base_link` with `right_little_rubber_1`, and `right_little_1` with `right_little_rubber_2`. You will enable **Filtered Pair** on those rows in the next module.
2. Click a row to **highlight both bodies** in the viewport with distinct outline colors so you can confirm which links the table refers to.

1. Use the **focal** (crosshair) icons next to a body name to select that body’s collision prims in the *Stage* when you need a closer look.

Sorting, batch checkbox toggles, multi-row selection, and keyboard navigation are described in [Robot Self-Collision Detector](../robot_setup/ext_isaacsim_robot_setup_collision_detector.html#isaac-collision-detector).

### Solid collision meshes (Physics Debugger)

The steps below walk through **Solid Collision Mesh Visualization** for the Inspire Hand so you can relate detector rows to concrete shapes in the viewport. Follow them when that extra view helps; otherwise continue to the next module.

We use the pinky as the example: visualize its collision meshes and relate them to the overlaps you saw in the detector.

1. Open **Utilities > Physics Debugger** to show the *Physics Debug* panel.

1. Have the root prim `inspire_hand` selected. In **Collision Mesh Debug Visualization**, enable **Solid Collision Mesh Visualization**.

Tip

**Solid Collision Mesh Visualization** shows only the collision meshes for the currently selected prim. Ensure the `inspire_hand` prim is selected in the *Stage* panel so all collision meshes are visible.

1. Open **Eye > Show by Type > Meshes** and turn **Meshes** off so the solid collision meshes are easier to see.

1. In the *Stage* panel, deactivate the `right_little_1` link (lower pinky) to expose the overlapping collision shapes underneath—the rubber pad and surrounding links.

1. Identify where `right_little_rubber_1` (lower pinky rubber pad) overlaps with `r_base_link` (palm)—that is where a problematic self-collision is likely to occur.

In the image above, with the lower pinky link hidden, the lower pinky rubber pad (tan/sand color) overlaps and collides with the palm (yellow). This is an example of a pair we will filter out to ensure stable simulation.

The schematic below shows which rigid body pairs of the pinky we will filter in this tutorial:

1. Open **Eye > Show by Type > Meshes** and toggle **Meshes** on to re-enable mesh visualization.

## Module 3.3: Adding Filtered Pairs

Next, we filter two specific self-collision pairs that drive pinky instability: (1) the palm `r_base_link` and the pinky’s lower rubber pad `right_little_rubber_1`, and (2) the lower pinky link `right_little_1` and the upper rubber pad `right_little_rubber_2`.

Note

It doesn’t matter whether the filtered pair is a parent or child link; USD’s Physics Filtered Pairs block collisions between the specified pairs in both directions.

To follow Asset Structure 3.0, filtered pairs use the neutral Physics API—author on **physics.usda**.

### Set **physics.usda** as the authoring layer

1. In the **Layer** tab, expand **physx.usda**. You should see **physics.usda** listed in the hierarchy.

1. **Right-click on physics.usda** and select **Set Authoring Layer**.

You should now see the **physics.usda** layer highlighted green, indicating it is the active authoring layer.

### Robot Self-Collision Detector: **Filtered Pair**

1. Open **Tools > Robotics > Asset Editors > Robot Self-Collision Detector** (or bring the panel forward if it is already open).
2. Click **Check Collisions** so the table matches the current stage.
3. Find the row whose two bodies are `r_base_link` and `right_little_rubber_1` (column order may vary). Enable **Filtered Pair** for that row.
4. Find the row for `right_little_1` and `right_little_rubber_2`. Enable **Filtered Pair** for that row.

Tip

Multi-select rows and toggle one **Filtered Pair** checkbox to apply the same state to every selected row; see [User Interface](../robot_setup/ext_isaacsim_robot_setup_collision_detector.html#isaac-collision-detector-ui).

Toggling **Filtered Pair** authors `UsdPhysics.FilteredPairsAPI` on the active layer—the **physics.usda** authoring layer you set above.

Note

If you use the detector checkboxes in this section, skip the *Property* panel subsection that follows.

### Verify and save

1. Click on the blue files icon next to **physics.usda (Authoring Layer)** to save the changes to **physics.usda**.

1. Press **Play**. The pinky (little finger) should move more stably; the other fingers will still be unstable until their collision pairs are filtered the same way.

Note

Before starting Tutorial 5, open `/path/to/Inspire/module_3_end-checkpoint_1/inspire_hand.usda`. It includes all collision filters for stability, plus additional filtered pairs (e.g. finger tips and pads) for computational performance.

### *Property* panel: **Filtered Pairs** on each prim

The following steps add the same two relationships by editing **Filtered Pairs** on `r_base_link` and `right_little_1`. Use them if you prefer prim-by-prim authoring or want to see where the targets appear in the *Property* panel. If you already enabled both pairs in the Robot Self-Collision Detector, skip this subsection.

#### Palm and lower pinky rubber pad

1. In the *Stage* tab, select the `r_base_link` prim. In the *Property* panel, click **Add > Physics > Filtered Pairs**.

1. With `r_base_link` still selected, go to the *Property* panel. Find the **Filtered Pairs** section and click **Add Target** to add a new filtered collision pair.

1. In the pop-up that appears, browse or type to select `right_little_rubber_1`.

After these steps, collisions between the palm (`r_base_link`) and the pinky’s lower rubber pad (`right_little_rubber_1`) are filtered out.

#### Lower pinky link and upper rubber pad

1. In the *Stage* panel, select the `right_little_1` prim (lower link of the pinky). In the *Property* panel, click **Add > Physics > Filtered Pairs**.

1. With `right_little_1` still selected, go to the *Property* panel. Find the **Filtered Pairs** section and click **Add Target** to add a new filtered collision pair.
2. In the pop-up window, browse or type to select `right_little_rubber_2` (the upper pinky rubber pad), and confirm the selection.

Save the layers as in **Verify and save** above and then press **Play** again to confirm the pinky moves more stably.

## Summary

This tutorial covered:

* How **Filtered Pairs** work and when to use them to prevent invalid self-collisions.
* Enabling self-collisions, running the **Robot Self-Collision Detector** to list overlapping pairs and mark **Filtered Pair**, and using the **Physics Debugger** for solid collision mesh visualization when helpful.
* Authoring the pinky’s two filters on **physics.usda** via the detector or the *Property* panel on `r_base_link` and `right_little_1`.

## Next Steps

Continue to [Tutorial 5: Joint Drive Tuning](tutorial_05_joint_drive_tuning.html#isaac-sim-tutorial-tuning-openusd-module-4) to set drive limits (max force, max velocity) from the Inspire Hand specs, then to [Tutorial 6: Joint Gains Tuning](tutorial_06_joint_gains_tuning.html#isaac-sim-tutorial-tuning-openusd-module-5) for stiffness and damping with the Gain Tuner.

On this page

* [Learning Objectives](#learning-objectives)
* [Prerequisites](#prerequisites)
* [Module 3.1: Understanding Filtered Pairs](#module-3-1-understanding-filtered-pairs)
* [Module 3.2: Enable self-collision and inspect pairs](#module-3-2-enable-self-collision-and-inspect-pairs)
  + [Step 1: Reproduce the problem](#step-1-reproduce-the-problem)
  + [Step 2: Run the Robot Self-Collision Detector](#step-2-run-the-robot-self-collision-detector)
  + [Solid collision meshes (Physics Debugger)](#solid-collision-meshes-physics-debugger)
* [Module 3.3: Adding Filtered Pairs](#module-3-3-adding-filtered-pairs)
  + [Set **physics.usda** as the authoring layer](#set-physics-usda-as-the-authoring-layer)
  + [Robot Self-Collision Detector: **Filtered Pair**](#robot-self-collision-detector-filtered-pair)
  + [Verify and save](#verify-and-save)
  + [*Property* panel: **Filtered Pairs** on each prim](#property-panel-filtered-pairs-on-each-prim)
    - [Palm and lower pinky rubber pad](#palm-and-lower-pinky-rubber-pad)
    - [Lower pinky link and upper rubber pad](#lower-pinky-link-and-upper-rubber-pad)
* [Summary](#summary)
* [Next Steps](#next-steps)

---

### Tutorial 05: Joint Drive Tuning

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/openusd_tuning_tutorials/tutorial_05_joint_drive_tuning.html

* [Robot Setup](../robot_setup/index.html)
* [OpenUSD and Tuning Best Practices Tutorial Series](index.html)
* Tutorial 5: Joint Drive Tuning

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Tutorial 5: Joint Drive Tuning

Collision pairs are filtered (Tutorial 4). The next question: **with how much torque and velocity can each joint move?** If the simulated hand can apply more torque than the real hardware, or spin faster than the real motors, your grasps and controllers will behave differently in sim than on the robot. Conversely, limits that are too low make the hand feel weak or sluggish. In this tutorial we set the **drive limits**—max torque and max velocity—from the Inspire Hand specs. Stiffness and damping (how the joint *responds* to position commands) are tuned in Tutorial 6.

## Learning Objectives

In this tutorial, you will:

* **Configure** mimic joints to be non-compliant for initial gains tuning.
* **Compute and set** max joint torque derived from Inspire specifications.
* **Set** max joint velocity directly from Inspire specifications.

Inspire Hand specs used in this tutorial (palm fingers): Max palm finger grip force 10 N; max palm finger bend speed 260 deg/s.

## Prerequisites

* Complete [Tutorial 4: Collider Pairs](tutorial_04_collider_pairs.html#isaac-sim-tutorial-tuning-openusd-module-3).
* Open `/path/to/Inspire/module_3_end-checkpoint_1/inspire_hand.usda` in Isaac Sim (or have your own filtered-pairs version open).

## Module 4.1: Mimic Joints

In the Inspire Hand model, the fingers use PhysX **mimic joints** to replicate the underactuated mechanism found in the real robotic hand. In this approach, a single motor drives multiple joints using a fixed gear ratio, allowing for coordinated finger movement and more realistic simulation of the physical hand.

A mimic joint links two degrees of freedom, establishing a relationship (via gear ratio and offset) so that when one joint moves, the other follows accordingly. These mimic joints can be either **compliant** (allowing some “softness” or flexibility, like a spring) or **non-compliant** (rigidly enforcing the kinematic constraint). For this tutorial, we’ll configure **non-compliant** mimic joints to initially tune the driven joints. (You can add compliance for “softer” mimic behavior later, if needed.)

Follow these steps to configure the mimic joints:

1. Open `/path/to/Inspire/module_3_end-checkpoint_1/inspire_hand.usda` in Isaac Sim if you haven’t already.
2. Mimic joints are a PhysX-specific feature, so set your authoring layer to **physx.usda**. In the **Layer** tab, click the **Insert Sublayer** icon if the sublayer is not already there.

1. In the file dialog, navigate to `/path/to/Inspire/module_3_end-checkpoint_1/payloads/Physics/`, select `physx.usda`, and click **Open**.

1. Once **physx.usda** appears in the layer stack, **Right-click on physx.usda** and select **Set Authoring Layer**.

You should now see the **physx.usda** layer highlighted green, indicating it is the active authoring layer.

1. In the *Stage* panel, multi-select the mimic joints for the Inspire Hand palm fingers (hold **CTRL** and left-click each):

   * `right_thumb_3_joint`
   * `right_thumb_4_joint`
   * `right_index_2_joint`
   * `right_middle_2_joint`
   * `right_ring_2_joint`
   * `right_little_2_joint`

1. With the joints selected, go to the *Property* panel. Find the **Mimic Joint** section and set **Damping Ratio** to **0.0** and **Natural Frequency** to **0.0** to make the constraint non-compliant.

Tip

Setting natural frequency or damping ratio to **0.0** tells PhysX to make this a non-compliant mimic joint. Setting both of them to **0.0** makes the intent clear.

1. Click on the blue files icon next to **physx.usda (Authoring Layer)** to save the changes to **physx.usda**.

After these steps, the mimic joints in your Inspire Hand model will behave as a stiff, non-compliant mechanism, giving you precise control for gains tuning in the next module.

## Module 4.2: Configure Max Joint Torque

The maximum drive force (torque for revolute joints) caps how much force the finger can apply at the contact. Too low and the hand cannot hold the specified load; too high and you risk unrealistic forces or instability. We derive the value from the manufacturer’s grip force and the distance from joint to fingertip so the sim matches the real hand’s capability.

**Torque = Force Ã Distance**

For the palm finger, max force is 10 N. The distance between `right_little_1_joint` and the tip of the little finger is 0.045 m + 0.039 m.

**Little finger:** Torque = 10 Ã (0.045 + 0.039) = 0.84 Nm

There are two joints in the mimic chain, so multiply by 2:

**Little finger max drive force:** 0.84 Ã 2 = 1.68 Nm

1. Max Force drive parameters are a neutral physics attribute, so author on the **physics.usda** layer. In the **Layer** tab, expand the **physx.usda** layer.

1. **Right-click on physics.usda** and select **Set Authoring Layer**.

You should now see the **physics.usda** layer highlighted green, indicating it is the active authoring layer.

1. In the *Stage* panel, find and select `inspire_hand/Physics/right_little_1_joint`.
2. In the *Property* panel, scroll to **Drive** and set **Max Force** to **1.68** based on our calculations.

1. Click on the blue files icon next to **physics.usda (Authoring Layer)** to save the changes to **physics.usda**.

## Module 4.3: Apply Max Velocity

Maximum joint velocity limits how fast the joint can move. Without a cap, the solver can command velocities that no real motor could achieve, leading to unrealistic motion or numerical instability. We set the limit from the Inspire Hand’s palm finger bend speed (260 deg/s) so the simulated hand moves within the same envelope as the hardware.

* **Realism** — Simulated motion matches real hardware.
* **Stability** — Avoids velocity spikes that cause instability.

1. Maximum joint velocity is a PhysX-specific attribute, so author on the **physx.usda** layer. In the **Layer** tab, **Right-click on physx.usda** and select **Set Authoring Layer**.

You should now see the **physx.usda** layer highlighted green, indicating it is the active authoring layer.

1. In the *Stage* panel, find and select `inspire_hand/Physics/right_little_1_joint`.
2. In the *Property* panel, scroll to **Raw USD Properties**, expand **Advanced**, and set **Maximum Joint Velocity** to **260** (deg/s).

1. Click on the blue files icon next to **physx.usda (Authoring Layer)** to save the changes to **physx.usda**.

Note

A checkpoint file with drive limits for all 6 joints derived using the same process is provided at `/path/to/Inspire/module_4_end-checkpoint_2/inspire_hand.usda`. Open this file before starting Tutorial 6.

## Summary

This tutorial covered:

* Configuring **mimic joints** as non-compliant so the solver enforces the finger kinematics without adding compliance—setting you up for clean gain tuning in Tutorial 6.
* **Computing and setting max joint torque** from Inspire Hand specs (force Ã distance, then Ã 2 for the mimic chain) so the hand’s grip capability matches the real robot.
* Setting **max joint velocity** from specs (260 deg/s) so motion is realistic and the simulation stays stable.

### Next Steps

Continue to [Tutorial 6: Joint Gains Tuning](tutorial_06_joint_gains_tuning.html#isaac-sim-tutorial-tuning-openusd-module-5) to tune drive stiffness and damping with the Gain Tuner and analyze the results.

On this page

* [Learning Objectives](#learning-objectives)
* [Prerequisites](#prerequisites)
* [Module 4.1: Mimic Joints](#module-4-1-mimic-joints)
* [Module 4.2: Configure Max Joint Torque](#module-4-2-configure-max-joint-torque)
* [Module 4.3: Apply Max Velocity](#module-4-3-apply-max-velocity)
* [Summary](#summary)
  + [Next Steps](#next-steps)

---

### Tutorial 06: Joint Gains Tuning

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/openusd_tuning_tutorials/tutorial_06_joint_gains_tuning.html

* [Robot Setup](../robot_setup/index.html)
* [OpenUSD and Tuning Best Practices Tutorial Series](index.html)
* Tutorial 6: Joint Gains Tuning

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Tutorial 6: Joint Gains Tuning

Max torque and max velocity are set (Tutorial 5). The remaining question: **how does each joint respond when you command a new position?** Too stiff and the hand can jitter or overshoot; too soft and it lags or never reaches the target. Stiffness and damping form a PD (Proportional-Derivative) controller: stiffness pulls the joint toward the target, damping resists velocity and reduces oscillation. This tutorial uses the **Gain Tuner** in Isaac Sim to tune these gains for the thumb, run step and sinewave tests, and analyze position and velocity with the built-in charts—so you can see underdamped, critically damped, and overdamped behavior and aim for responsive, stable motion.

## Learning Objectives

In this tutorial, you will:

* **Tune** drive stiffness and damping for the thumb using the Gain Tuner.
* **Run** step and sinewave tests and interpret underdamped, critically damped, and overdamped behavior.
* **Analyze** tuning results with the Gain Tuner charts and save gains to the physics layer.

## Prerequisites

* Complete [Tutorial 5: Joint Drive Tuning](tutorial_05_joint_drive_tuning.html#isaac-sim-tutorial-tuning-openusd-module-4).
* Open `/path/to/Inspire/module_4_end-checkpoint_2/inspire_hand.usda` in Isaac Sim if not already open.

## Module 5.1: Understanding Joint Drive Stiffness and Damping

Position control in Isaac Sim uses stiffness and damping:

**Force = (Stiffness Ã delta\_position) + (Damping Ã delta\_velocity)**

* **Stiffness** — Like a spring; force proportional to distance from target. Higher stiffness pulls the joint toward the target more strongly.
* **Damping** — Like a shock absorber; force proportional to velocity. Higher damping reduces oscillation and overshoot.

Together they form a PD (Proportional-Derivative) controller.

### Why Tuning Stiffness and Damping Matters

Stiffness and damping directly determine how the joint responds to position commands and how it behaves in contact. Poor tuning leads to:

* **Unrealistic motion** — Too stiff can look robotic or cause jitter; too soft makes the hand feel sluggish or weak.
* **Instability** — High stiffness with low damping causes oscillation and overshoot; in contact, this can produce chatter or unstable grasps.
* **Poor tracking** — If gains are too low, the joint never reaches the target in time or drifts under load.

The ratio of stiffness to damping defines the **damping regime** of the response. For a step to a target position, you will see one of three behaviors:

| Regime | What it looks like | Cause |
| --- | --- | --- |
| **Underdamped** | The joint overshoots the target, then oscillates (rings) before settling. You may see multiple overshoots. | Stiffness is high relative to damping; the “spring” dominates and there isn’t enough “shock absorber” to dissipate energy. |
| **Critically damped** | The joint approaches the target smoothly and reaches it in the shortest time **without** overshooting. | Stiffness and damping are balanced so that the system neither rings nor moves slowly. Often the goal for responsive, stable motion. |
| **Overdamped** | The joint approaches the target slowly and never overshoots. Response is sluggish; it may take a long time to settle. | Damping is high relative to stiffness; motion is heavily resisted. |

In the Gain Tuner, if you see **oscillation or overshoot** in the position chart, you are underdamped—increase damping (or reduce stiffness). If the joint **barely moves or creeps** toward the target, you are overdamped—increase stiffness or reduce damping. Aim for a response that reaches the target quickly with little or no overshoot (near critically damped).

## Module 5.2: Using Gain Tuner to Tune Joint Drive Stiffness and Damping

1. Open `/path/to/Inspire/module_4_end-checkpoint_2/inspire_hand.usda` in Isaac Sim if not already open.
2. Go to **Tools > Robotics > Asset Editors > Gain Tuner**.

1. In **Tune Gains**, set **Mode** to **Position** and **Type** to **Force**.

Note

In the **module\_4\_end-checkpoint\_2** file, the finger joints already have stiffness and damping set for you. We focus on tuning and verifying the **thumb** joints (`right_thumb_1_joint`, `right_thumb_2_joint`) in this tutorial.

### Tuning Guidelines (PhysX)

1. Set damping to zero and tune only stiffness to see the basic position response.
2. Increase stiffness until the joint converges close to the target.
3. Set damping one order of magnitude lower than stiffness as a baseline (should not overshoot); for a faster response, reduce damping.
4. Fine-tune both around this baseline for stability, response time, and overshoot.

### Run a Test

1. In the **Stiffness** column, set initial values for `right_thumb_1_joint` and `right_thumb_2_joint` (e.g. **0.01**).

1. In **Test Gains Settings**, enable the **Test** checkbox for `right_thumb_1_joint` and `right_thumb_2_joint`.

1. Set **Step Function** min and max so the thumb moves through a useful range: set `right_thumb_1_joint` **Step Min** to **10Â°** and **Step Max** to **60Â°**, and set `right_thumb_2_joint` **Step Min** to **5Â°** and **Step Max** to **20Â°**. Increase **Duration** to **2.0** so the joints can reach their targets within their maximum velocity limits.

Tip

The step function ranges (min/max) for the thumb joints are chosen to move through a substantial portion of their range of motion, but purposely avoid extreme or problematic poses (such as excessive curling without lateral movement, which could cause unrealistic contact).

If you want to precisely inspect and interactively move any joint through its full range, use the **Physics Inspector** tool:

1. Go to **Tools > Physics > Physics Inspector**.
2. In the Inspector window, select `r_base_link` as the **Articulation** in the dropdown.
3. Use the interface to directly set drive target positions for any joint and observe their behavior in the viewport.

Before commanding targets, make sure the joint’s stiffness is set to a nonzero value—otherwise the joint may not respond to target changes.

1. Press **Play**, then **Run Test** to apply the gains and run the evaluation.

Tip

If you see instabilities at higher stiffness values, open the *Property* panel, select **PhysicsScene**, and try increasing **Time Steps Per Second**.

## Module 5.3: Analyze Tuning Results

The Gain Tuner’s **Charts** let you compare actual position and velocity to the commanded values. Use them to spot overshoot, lag, or coupling: for example, `right_thumb_2_joint` tested alone can behave differently than when both thumb joints move together. We’ll adjust gains, run parallel tests for both thumb joints, then run all fingers in parallel to confirm the full hand tracks commands before saving to the physics layer.

1. Once the tests from *Run a Test* are completed, expand the **Charts** section and multi-select (**CTRL** + left-click) `right_thumb_1_joint` and `right_thumb_2_joint`.

You should see that `right_thumb_1_joint` is oscillating around the target and `right_thumb_2_joint` is struggling to reach the target.

1. To improve tracking, increase stiffness to **0.07** for `right_thumb_2_joint`.

1. Add damping **0.0001** to reduce oscillation. Set **Sequence** to **1** for both `right_thumb_1_joint` and `right_thumb_2_joint` so they run at the same time (parallel tests let the thumb’s lateral motion create space for the curling motion). Set **Step Min** to **0.0** and **Step Max** to **15** for `right_thumb_2_joint` to observe the effect of the range change.

1. Press **Play** if the simulation is not already playing. Click **Run Test**.

1. Once the tests are finished, expand the **Charts** section and multi-select (**CTRL** + left-click) `right_thumb_1_joint` and `right_thumb_2_joint`.

1. Run the **Sinewave** test to evaluate how each joint responds to a smooth, continuous motion command. Set the **Amplitude** parameter to **50** for `right_thumb_1_joint` and **30** for `right_thumb_2_joint` (feel free to experiment with these values to observe effects), then click **Run Test**.

1. Continue tuning by experimenting with different gain values (stiffness and damping) and various test parameters. As you tune, **monitor joint velocities** during the test to ensure none exceed the maximum joint velocity limits defined earlier. To do this:

   * Select any joint in the *Property* panel.
   * Scroll down to **Extra Properties > Velocity** to view its current velocity while the test is running.

If velocities approach or exceed the maximums, reduce gain values or adjust test parameters.

1. To evaluate the **entire hand’s coordinated tracking**, run a parallel step function test:

   * Enable **Test** for all joints in the Gain Tuner.
   * Set **Sequence** to **1** for each joint (this runs tests in parallel for all fingers).
   * Set **Step Min** and **Step Max** to **10** and **30**, respectively, for each joint.

Click **Run Test**. The resulting charts will reveal how well your current **Stiffness** and **Damping** settings allow the full hand to execute simultaneous step commands. You should see coordinated, stable motion across all joints. The expected results might look similar to the example below:

| Joint | Test | Sequencer | Step Min | Step Max | Period | Phase |
| --- | --- | --- | --- | --- | --- | --- |
| right\_thumb\_1\_joint | 1 | 1 | 10.0 deg | 60.0 deg | 2.0 s | 0.0 s |
| right\_index\_1\_joint | 1 | 1 | 10.0 deg | 30.0 deg | 2.0 s | 0.0 s |
| right\_middle\_1\_joint | 1 | 1 | 10.0 deg | 30.0 deg | 2.0 s | 0.0 s |
| right\_ring\_1\_joint | 1 | 1 | 10.0 deg | 30.0 deg | 2.0 s | 0.0 s |
| right\_little\_1\_joint | 1 | 1 | 10.0 deg | 30.0 deg | 2.0 s | 0.0 s |
| right\_thumb\_2\_joint | 1 | 1 | 0.0 deg | 10.0 deg | 2.0 s | 0.0 s |

Note

In the Gain Tuner, open `/path/to/Inspire/module_5_end-checkpoint_3/inspire_hand.usda` to review the final tuned stiffness and damping values.

## Summary

This tutorial covered:

* Using the **Gain Tuner** to tune stiffness and damping (Position, Force) for the thumb joints and saving gains to the **physics.usda** layer so the hand responds to position commands with stable, near–critically damped motion.
* Running **step** and **sinewave** tests and interpreting damping regimes (underdamped, critically damped, overdamped) in the Charts to diagnose overshoot or sluggishness.
* Verifying **parallel tests** for all joints; the same workflow applies to other digits or custom hands. The **module\_5\_end-checkpoint\_3** checkpoint contains the final tuned values.

## Next Steps

Continue to [Tutorial 7: Using the Dexterous Hand in Practice](tutorial_07_practice.html#isaac-sim-tutorial-tuning-openusd-practice) for next steps and further resources.

## Further Learning

* Read [Gain Tuner Extension](../robot_setup/ext_isaacsim_robot_setup_gain_tuner.html#isaac-gain-tuner) for more details on the physical mechanics relating joint gains to derived motions and how the Gain Tuner works.

On this page

* [Learning Objectives](#learning-objectives)
* [Prerequisites](#prerequisites)
* [Module 5.1: Understanding Joint Drive Stiffness and Damping](#module-5-1-understanding-joint-drive-stiffness-and-damping)
  + [Why Tuning Stiffness and Damping Matters](#why-tuning-stiffness-and-damping-matters)
* [Module 5.2: Using Gain Tuner to Tune Joint Drive Stiffness and Damping](#module-5-2-using-gain-tuner-to-tune-joint-drive-stiffness-and-damping)
  + [Tuning Guidelines (PhysX)](#tuning-guidelines-physx)
  + [Run a Test](#run-a-test)
* [Module 5.3: Analyze Tuning Results](#module-5-3-analyze-tuning-results)
* [Summary](#summary)
* [Next Steps](#next-steps)
* [Further Learning](#further-learning)

---

### Tutorial 07: Practice

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/openusd_tuning_tutorials/tutorial_07_practice.html

* [Robot Setup](../robot_setup/index.html)
* [OpenUSD and Tuning Best Practices Tutorial Series](index.html)
* Tutorial 7: Using the Dexterous Hand in Practice

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Tutorial 7: Using the Dexterous Hand in Practice

With asset structure verified, collision pairs filtered, and joint parameters tuned, the Inspire Hand in Isaac Sim is stable and ready for downstream use.

## Learning Objectives

In this tutorial, you will:

* **Review** what you accomplished across the OpenUSD and Tuning Best Practices series.
* **Learn** next steps for using the tuned Inspire Hand (attach to an arm, watch demos, fine tune, extend to other hands).
* **Find** additional documentation and resources for PhysX and articulation.

## Prerequisites

* Complete [Tutorial 6: Joint Gains Tuning](tutorial_06_joint_gains_tuning.html#isaac-sim-tutorial-tuning-openusd-module-5). You should have a tuned, stable Inspire Hand USD.

## What You Accomplished

* **Tutorial 2** — You inspected the multi-physics asset structure.
* **Tutorial 3** — You enabled joint and mass/inertia visualization, and verified collision meshes.
* **Tutorial 4** — You identified problematic self-collisions and added filtered pairs so the hand simulates without artifacts.
* **Tutorial 5** — You set mimic joints, max joint torque, and max velocity from specs.
* **Tutorial 6** — You tuned drive stiffness and damping with the Gain Tuner and analyzed results with the built-in charts.

You now have a tuned, stable robotic hand USD that can be attached to an arm and used with a grasping controller in Isaac Sim or Isaac Lab.

## Next Steps

* **Attach to an arm** — Use the hand as an end effector on a manipulator (e.g. Kuka) in Isaac Sim or Isaac Lab and run grasping or manipulation tasks.
* **Watch applied demos** — Look for Isaac Lab Kuka + Inspire Hand demos (e.g. from GTC) to see the same hand used in full workflows.
* **Fine Tune in Simple Scene Setups** — Bring the hand into simple scenes involving contact. Tune mimic joint compliance as needed for realistic and stable behavior in contact scenarios.
* **Extend tuning** — Apply the same process (collision filters, max force/velocity, stiffness/damping) to other digits or to custom dexterous hands.

## Additional Resources

* [NVIDIA Isaac Sim Documentation](https://docs.omniverse.nvidia.com/isaacsim/latest/)
* [Physics and Rigid Body Dynamics](https://docs.omniverse.nvidia.com/isaacsim/latest/core/physics_tutorials/tutorial_rigid_body_dynamics.html) — For deeper coverage of PhysX and articulation.

## Summary

This tutorial reviewed what you accomplished in the series, outlined next steps for using the tuned Inspire Hand (attach to an arm, demos, fine tuning, extending to other hands), and pointed to additional resources for further learning.

On this page

* [Learning Objectives](#learning-objectives)
* [Prerequisites](#prerequisites)
* [What You Accomplished](#what-you-accomplished)
* [Next Steps](#next-steps)
* [Additional Resources](#additional-resources)
* [Summary](#summary)

---


## Manipulators

### Kinematics Solver

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/manipulators/concepts/kinematics_solver.html

* [Robot Simulation](../../robot_simulation/index.html)
* [Motion Generation (Deprecated)](../motion_generation_overview.html)
* [Motion Generation](index.html)
* Kinematics Solvers

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Kinematics Solvers

Deprecated

For new development, consider using the newer [Robot Motion (Experimental)](../../robot_motion_experimental/index.html) API, which provides improved interfaces and additional features.

Like a [Motion Policy Algorithm](motion_policy.html#isaac-sim-motion-policy), a [Kinematics Solvers](#isaac-sim-kinematics-solver) is an interface class with a single provided implementation. A KinematicsSolver
is able to compute forward and inverse kinematics. A single implementation is provided using the NVIDIA-developed **Lula** library. (see [Lula Kinematics Solver](#isaac-sim-lula-kinematics-solver))

includes:

* Kinematics Solver
* Articulation Kinematics Solver
* Lula Kinematics Solver

## Kinematics Solver

The KinematicsSolver interface specifies functions for computing both forward and inverse kinematics at any available frame in the robot. Like a [Motion Policy Algorithm](motion_policy.html#isaac-sim-motion-policy),
an instance of the KinematicsSolver class is not expected to use the same USD robot representation as NVIDIA Isaac Sim. A KinematicsSolver can have its own internal
representation of the robot, and there are necessary interface functions for performing the mapping between the internal robot representation and the robot
Articulation.

### Joint Names

An instance of the KinematicsSolver class must fulfill a function KinematicsSolver.get\_joint\_names() that specifies the joints of interest to the solver, and the order in which it
expects them. Think of a robot arm mounted on a moving base. A KinematicsSolver can use only the URDF for the robot arm without knowing about the robot base. In this case, many of
the joints in the robot Articulation would not be recognized by the KinematicsSolver.

When computing forward kinematics, the joint positions that are passed to the solver must correspond to the output of KinematicsSolver.get\_joint\_names(). Likewise, the output of
inverse kinematics will have the same shape as KinematicsSolver.get\_joint\_names(). A mapping layer between the robot Articulation and the KinematicsSolver is provided in the
[Articulation Kinematics Solver](#isaac-sim-articulation-kinematics-solver) class.

### Frame Names

An instance of the KinematicsSolver class must fulfill a function KinematicsSolver.get\_all\_frame\_names() to provide a list of frames in the robot’s kinematics chain that can have their positions
referenced by name when solving either forward or inverse kinematics. The frame names returned by a KinematicsSolver do not have to match the frames present in the robot Articulation. Like joint names,
the frame names come from the individual solver’s config file structure.

### Robot Base Pose

As with a [Motion Policy Algorithm](motion_policy.html#isaac-sim-motion-policy), a the KinematicsSolver interface includes a function set\_robot\_base\_pose() that allows the caller to specify the location of the robot base. If this function has been called,
the KinematicsSolver must apply appropriate transformations when computing forward and inverse kinematics.
A KinematicsSolver operates in world coordinates. The solution to the forward kinematics will be translated and rotated according to the robot base pose to return the position of the end effector relative to the world frame,
and the input to the inverse kinematics will be provided in the world coordinates and transformed so that it is relative to the robot base frame. If you prefers that the solver inputs are relative to the robot base frame,
they can simply set the robot base pose to the origin.

### Collision Awareness

Implementations of the KinematicsSolver class do not need to be collision aware with external objects, but they have the option. A function KinematicsSolver.supports\_collision\_avoidance() -> bool must be implemented
to indicate whether a particular KinematicsSolver supports collision avoidance. If a KinematicsSolver supports collision avoidance, it can fulfill the same set of world functions as a MotionPolicy ([Inputs: World State](motion_policy.html#isaac-sim-motion-policy-world-state)).
If a solver is collision aware, it is especially important to specify the robot base pose correctly, as the positions of objects can only be queried relative to the world frame, and it is up to the solver to compute the positions of obstacles
relative to the robot.

## Articulation Kinematics Solver

The ArticulationKinematicsSolver class exists to handle the mapping between the robot Articulation and an implementation of a [Kinematics Solvers](#isaac-sim-kinematics-solver).

### Forward Kinematics

ArticulationKinematicsSolver wraps the forward kinematics function of a KinematicsSolver to query the joint positions of the robot Articulation and pass the appropriate joint positions to the KinematicsSolver in the order
specified by KinematicsSolver.get\_joint\_names(). This allows the current position of the simulated robot end effector to be queried easily.

### Inverse Kinematics

ArticulationKinematicsSolver wraps the inverse kinematics to return the resulting joint positions as an ArticulationAction that can be directly applied to the robot Articulation.
The current robot Articulation joint positions at the time this method is called are automatically used as a warm start in the IK calculation.

## Lula Kinematics Solver

The LulaKinematicsSolver implements the [Kinematics Solvers](#isaac-sim-kinematics-solver) interface. The solver does not support collision avoidance with objects in the world. In addition to the functions in the
KinematicsSolver interface, the LulaKinematicsSolver includes getters and setters for changing internal settings such as LulaKinematicsSolver.set\_max\_iterations() to set the maximum number
of iterations before the IK computation returns a failure.

### Lula Kinematics Solver Configuration

Two files are necessary to configure Lula Kinematics for use with a new robot:

> 1. A URDF (universal robot description file), used for specifying robot kinematics as well as joint and link names. Position limits for each joint are also required. Other properties in the URDF are ignored and can be omitted; these include masses, moments of inertia, visual and collision meshes.
> 2. A supplemental robot description file in YAML format. In addition to enumerating the list of actuated joints that define the configuration space (c-space) for the robot, this file also includes sections for specifying the default c-space configuration. This file can also be used to specify fixed positions for unactuated joints.

On this page

* [Kinematics Solver](#kinematics-solver)
  + [Joint Names](#joint-names)
  + [Frame Names](#frame-names)
  + [Robot Base Pose](#robot-base-pose)
  + [Collision Awareness](#collision-awareness)
* [Articulation Kinematics Solver](#articulation-kinematics-solver)
  + [Forward Kinematics](#forward-kinematics)
  + [Inverse Kinematics](#inverse-kinematics)
* [Lula Kinematics Solver](#lula-kinematics-solver)
  + [Lula Kinematics Solver Configuration](#lula-kinematics-solver-configuration)

---

### Lula RRT

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/manipulators/concepts/lula_rrt.html

* [Robot Simulation](../../robot_simulation/index.html)
* [Motion Generation (Deprecated)](../motion_generation_overview.html)
* [Motion Generation](index.html)
* Lula RRT

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Lula RRT

Deprecated

For new development, consider using the newer [Robot Motion (Experimental)](../../robot_motion_experimental/index.html) API, which provides improved interfaces and additional features over Lula.

We provide a **Lula** implementation of the classic Randomly-Exploring Random Tree (RRT) algorithm to fulfill the PathPlanner interface. Specifically, the c-space RRT is using RRT-Connect based on [[2]](#id3), and the task-space RRT is using Jacobian transpose RRT based on [[3]](#id4). The RRT implementation does not support orientation targets.

## Lula RRT Configuration

Three files are necessary to configure Lula RRT for use with a new robot:

> 1. A URDF (universal robot description file), used for specifying robot kinematics as well as joint and link names. Position limits for each joint are also required. Other properties in the URDF are ignored and can be omitted; these include masses, moments of inertia, visual and collision meshes.
> 2. A supplemental robot description file in YAML format. In addition to enumerating the list of actuated joints that define the configuration space (c-space) for the robot, this file also includes sections for specifying the default c-space configuration. This file can also be used to specify fixed positions for unactuated joints.
> 3. A configuration file in the YAML format specifying parameters for the RRT algorithm such as termination conditions, exploration weights, and step size. These parameters can be modified programmatically with the RRT.set\_param() function.

## References

[[2](#id1)]

J. J. Kuffner and S. M. LaValle, “RRT-connect: An efficient approach to single-query path planning,” Proceedings 2000 ICRA. Millennium Conference. IEEE International
Conference on Robotics and Automation. Symposia Proceedings (Cat. No.00CH37065), 2000, pp. 995-1001 vol.2, doi: 10.1109/ROBOT.2000.844730.

[[3](#id2)]

M. Vande Weghe, D. Ferguson and S. S. Srinivasa, “Randomized path planning for redundant manipulators without inverse kinematics,” 2007 7th IEEE-RAS International Conference
on Humanoid Robots, 2007, pp. 477-482, doi: 10.1109/ICHR.2007.4813913.

On this page

* [Lula RRT Configuration](#lula-rrt-configuration)
* [References](#references)

---

### Motion Gen API

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/manipulators/concepts/motion_gen_api.html

* [Robot Simulation](../../robot_simulation/index.html)
* [Motion Generation (Deprecated)](../motion_generation_overview.html)
* [Motion Generation](index.html)
* Motion Generation Extension API Documentation

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Motion Generation Extension API Documentation

Deprecated

For new development, consider using the newer [Robot Motion (Experimental)](../../robot_motion_experimental/index.html) API, which provides improved interfaces and additional features.

See the Isaac Sim Motion Generation Extension [API Documentation](../../py/source/deprecated/isaacsim.robot_motion.motion_generation/docs/index.html) for usage information. This API content is part of the broader Omniverse API documentation.

---

### Motion Policy

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/manipulators/concepts/motion_policy.html

* [Robot Simulation](../../robot_simulation/index.html)
* [Motion Generation (Deprecated)](../motion_generation_overview.html)
* [Motion Generation](index.html)
* Motion Policy Algorithm

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Motion Policy Algorithm

Deprecated

For new development, consider using the newer [Robot Motion (Experimental)](../../robot_motion_experimental/index.html) API, which provides improved interfaces and additional features.

An Isaac Sim motion policy is a collision aware algorithm that outputs actions on each frame to navigate a single robot to a single task-space target.
The MotionPolicy class is an interface that is designed to be basic to fulfill,
but complete enough that an implementation of a MotionPolicy can be used alongside the [Articulation Motion Policy](#isaac-sim-articulation-motion-policy) class
to start moving the simulated robot around with just a few lines of code.

A single flexible MotionPolicy is provided based on the implementation of **RMPflow**
in the NVIDIA-developed **Lula** library (see [RMPflow](rmpflow.html)).

Broadly defined, a *motion policy* is a mathematical function that takes the current
state of a robot (that is, position and velocity in generalized coordinates) and returns
a quantity representing a desired change in that state. Such a policy can depend
implicitly on variables representing one or more objectives or constraints, the state of
the environment. The MotionPolicy interface has two forms of state as input:

* [Inputs: World State](#isaac-sim-motion-policy-world-state)
* [Inputs: Robot State](#isaac-sim-motion-policy-robot-state)

The main output of a MotionPolicy are position and velocity targets for the robot on the next frame. A MotionPolicy is
expected to be able to perform an internal world update and compute joint targets in real time (a few ms per frame).

## Active and Watched Joints

The robot Articulation in Isaac Sim comes from a loaded USD file. This robot specification is not expected to perfectly match the specification used internally by a MotionPolicy.
To perform the appropriate mapping, a MotionPolicy has two functions it must fulfill:

* `MotionPolicy.get_active_joints()`: joints that the MotionPolicy is going to directly control to achieve the desired end effector target.
* `MotionPolicy.get_watched_joints()`: joints that the MotionPolicy observes to plan motions, but will not actively control.

Both functions return a list of joint names in the order that the MotionPolicy expects to receive them.

For example, the Franka robot has nine degrees of freedom (DOFs):

* seven revolute joints for controlling the arm
* two prismatic joints for controlling its gripper

The robot Articulation exposes all nine degrees of freedom, but [RMPflow](rmpflow.html#isaac-sim-motion-generation-rmpflow) only cares about the seven revolute joints when navigating the robot to a position target. It is not appropriate for RMPflow to take control of the gripper DOFs, because those DOFs can be controlled separately when performing a task such as pick-and-place. `RmpFlow.get_active_joints()` returns the names of the seven revolute joints
in the Franka robot. `RmpFlow.get_watched_joints()` returns an empty list because the joint states of the gripper DOFs are irrelevant when navigating the Franka’s hand to a target position.

Every time RmpFlow returns joint targets for the Franka, it is returning arrays of length seven. When RmpFlow is passed an argument such as active\_joint\_positions, it is expecting a vector of seven numbers that describe the joint positions of the Franka robot in the order specified by `RmpFlow.get_active_joints()`.

## Inputs: World State

NVIDIA Isaac Sim provides a set of objects in `isaacsim.core.api.objects` that are intended to fully describe the simulated world. Only object primitives such as sphere and cone
are supported. A MotionPolicy has an adder for each type of object that exists in
`isaacsim.core.api.objects` for example, `MotionPolicy.add_sphere(sphere: isaacsim.core.api.objects.sphere.*)`. Objects in `isaacsim.core.api.objects` wrap objects that exist on the USD stage.
As objects move around on the stage, their location can be retrieved on each frame using the representative object from `isaacsim.core.api.objects`. This means that after a
MotionPolicy has been passed an object, it can internally query the position of that object on the stage over time as needed. A MotionPolicy queries all relevant obstacle positions
from the `isaacsim.core.api.objects` that have been passed in when `MotionPolicy.update_world()` is called, and passes the information to its internal world state.

It is not required that a specific MotionPolicy actually implement an adder for every type of object that exists in `isaacsim.core.api.objects`. When a class inherits from MotionPolicy,
any unimplemented adder functions will throw warnings. For example, [RMPflow](rmpflow.html#isaac-sim-motion-generation-rmpflow) supports spheres, capsules, and cuboids in its world representation.
In environments with cones, RMPflow will ignore the cone objects, and a warning will be printed for each cone object that gets added.

## Inputs: Robot State

There are two methods for specifying robot state in a MotionPolicy:

* The base pose of the robot can be specified to a MotionPolicy using `MotionPolicy.set_robot_base_pose()`. If this function is never called, the policy implementation can make a reasonable assumption about the position of the robot. [RMPflow](rmpflow.html#isaac-sim-motion-generation-rmpflow) assumes that the robot is at the origin of the stage until it is told otherwise.
* `MotionPolicy.compute_joint_targets(active_joint_positions, active_joints_velocities, watched_joint_positions, watched_joint_velocities,...)` expects robot joint positions and velocities to be passed in using the order specified by `MotionPolicy.get_active_joints()` and `MotionPolicy.get_watched_joints()`.

## Outputs: Robot Joint Targets

`MotionPolicy.compute_joints_targets(active_joint_positions, active_joints_velocities, watched_joint_positions, watched_joint_velocities,...)` returns position and velocity targets for the robot Articulation
on the next frame. The joint targets are for the active joints, and so they will have the same shape as the active\_joint\_positions argument. By passing a MotionPolicy
to the [Articulation Motion Policy](#isaac-sim-articulation-motion-policy) helper class, the work of translating the robot state between the robot Articulation and the MotionPolicy is done automatically using the outputs of
`MotionPolicy.get_active_joints()` and `MotionPolicy.get_watched_joints()`. A MotionPolicy might expect joint targets to be used in a standard PD controller:

\[kp\*(joint\_position\_targets-joint\_positions) + kd\*(joint\_velocity\_targets-joint\_velocities)\]

Both position and velocity targets must always be returned by a MotionPolicy. NVIDIA Isaac Sim supports providing only position targets or only velocity targets.
To match the default behavior of the Isaac Sim controller when only one target is set, you can set the joint\_velocity\_targets to zero for pure damping,
and it can set the joint\_position\_targets to be equal to the current joint\_positions to effectively remove the position term from the PD equation.

### Articulation Motion Policy

An ArticulationMotionPolicy is initialized using a robot Articulation object that represents the simulated robot, and a MotionPolicy. The purpose of this class is to handle the mapping of joints
between the robot articulation and the policy automatically by using the outputs of `MotionPolicy.get_active_joints()` and `MotionPolicy.get_watched_joints()`. There is a single important function in
this class: `ArticulationMotionPolicy.get_next_articulation_action()`. Calling this function queries the robot state from the robot Articulation, extracts and arranges the appropriate joints from the joint state
to use the `MotionPolicy.compute_joint_targets()` function, and then creates a valid ArticulationAction that can be passed to the robot Articulation to generate motions.

In the Franka example discussed in [Active and Watched Joints](#isaac-sim-motion-policy-active-joints), the robot Articulation that represents the Franka expects nine DOF joint targets. RmpFlow only controls seven of the DOFs. The appropriate
seven DOFs are passed to RmpFlow, and seven DOF joint position and velocity targets are returned. This 7-vector is mapped to a 9-vector, padding with None when no action is supposed to be taken for a particular joint. The
ArticulationAction object that is returned contains a 9-vector for position and velocity targets, and this can be applied to the robot Articulation using `Articulation.get_articulation_controller().apply_action(articulation_action)`.

### Motion Policy Controller

The MotionPolicyController class wraps a motion policy into an instance of `isaacsim.core.api.controllers.BaseController`. Extensions representing individual robots such as `isaacsim.robot.manipulators.franka` have an instance of
a BaseController for moving the robot around. The Franka robot can be moved to a target by importing `isaacsim.robot.manipulators.franka.controllers.RMPFlowController` and using the forward function.

On this page

* [Active and Watched Joints](#active-and-watched-joints)
* [Inputs: World State](#inputs-world-state)
* [Inputs: Robot State](#inputs-robot-state)
* [Outputs: Robot Joint Targets](#outputs-robot-joint-targets)
  + [Articulation Motion Policy](#articulation-motion-policy)
  + [Motion Policy Controller](#motion-policy-controller)

---

### Path Planner

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/manipulators/concepts/path_planner.html

* [Robot Simulation](../../robot_simulation/index.html)
* [Motion Generation (Deprecated)](../motion_generation_overview.html)
* [Motion Generation](index.html)
* Path Planner Algorithm

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Path Planner Algorithm

Deprecated

For new development, consider using the newer [Robot Motion (Experimental)](../../robot_motion_experimental/index.html) API, which provides improved interfaces and additional features.

A [Path Planner](#isaac-sim-path-planner) is an algorithm that outputs a series of configuration space waypoints, which
when linearly interpolated, produce a collision-free path from a starting c-space pose to a c-space or task-space target pose.
The PathPlanner class provides an interface that specifies the necessary functions that must be fulfilled to specify a path planning algorithm that can interface with NVIDIA Isaac Sim.

An implementation is provided using the NVIDIA-developed **Lula** library (see [Lula RRT](lula_rrt.html#isaac-sim-motion-generation-rrt)).

## Path Planner

The PathPlanner interface specifies functions for computing a series of configuration space waypoints, which
when linearly interpolated, produce a collision-free path from a starting c-space pose to a c-space or task-space target pose.
A PathPlanner uses the same set of functions to interface with the USD world as a [Motion Policy Algorithm](motion_policy.html#isaac-sim-motion-policy).
Like a [Motion Policy Algorithm](motion_policy.html#isaac-sim-motion-policy),
an instance of the PathPlanner class is not expected to use the same USD robot representation as NVIDIA Isaac Sim. A PathPlanner can have its own internal
representation of the robot, and there are necessary interface functions for performing the mapping between the internal robot representation and the robot
Articulation.

### Active and Watched Joints

The robot Articulation in Isaac Sim comes from a loaded USD file. This robot specification is not expected to perfectly match the specification used internally by a PathPlanner.

To perform the appropriate mapping, a PathPlanner has two functions it must fulfill:

* `PathPlanner.get_active_joints()`: joints that the PathPlanner is going to directly control to achieve the desired end effector target.
* `PathPlanner.get_watched_joints()`: joints that the PathPlanner observes to plan motions, but will not actively control. These are assumed to remain constant when generating a path.

Both functions return a list of joint names in the order that the PathPlanner expects to receive them.

For example, the Franka robot has nine degrees of freedom (DOFs):

* seven revolute joints for controlling the arm
* two prismatic joints for controlling its gripper

The robot Articulation exposes all nine degrees of
freedom, but [Lula RRT](lula_rrt.html#isaac-sim-motion-generation-rrt) only cares about the seven revolute joints when navigating the robot to a position target. It is not appropriate for RRT to take
control of the gripper DOFs, because those DOFs can be controlled separately when performing a task such as pick-and-place. `RRT.get_active_joints()` returns the names of the seven revolute joints
in the Franka robot. `RRT.get_watched_joints()` returns an empty list because the joint states of the gripper DOFs are irrelevant when navigating the Franka’s hand to a target position.
Every time RRT returns joint targets for the Franka, it is returning arrays of length seven. When RRT is passed an argument such as `active_joint_positions`,
it is expecting a vector of seven numbers that describe the joint positions of the Franka robot in the order specified by `RRT.get_active_joints()`.

### Inputs: World State

NVIDIA Isaac Sim provides a set of objects in `isaacsim.core.api.objects` that are intended to fully describe the simulated world. Only object primitives such as sphere and cone
are supported. More advanced objects defined by meshes and point clouds will be added in a future release. A PathPlanner has an for each type of object that exists in
`isaacsim.core.api.objects` for example:

\[PathPlanner.add\_sphere(sphere: isaacsim.core.api.objects.sphere.\*)\]

Objects in isaacsim.core.api.objects wrap objects that exist on the USD stage.
As objects move around on the stage, their location can be retrieved on each frame using the representative object from `isaacsim.core.api.objects`. This means that after a
PathPlanner has been passed an object, it can internally query the position of that object on the stage over time as needed. A PathPlanner queries all relevant obstacle positions
from the `isaacsim.core.api.objects` that have been passed in when `PathPlanner.update_world()` is called, and passes the information to its internal world state.

It is not required that a specific PathPlanner actually implement an adder for every type of object that exists in `isaacsim.core.api.objects`. When a class inherits from PathPlanner,
any unimplemented adder functions will throw warnings. For example, [Lula RRT](lula_rrt.html#isaac-sim-motion-generation-rrt) supports spheres, capsules, and cuboids in its world representation.
In environments with cones, RRT will ignore the cone objects, and a warning will be printed for each cone object that gets added.

### Inputs: Robot State

There are two methods for specifying robot state in a PathPlanner:

> * The base pose of the robot can be specified to a PathPlanner using `PathPlanner.set_robot_base_pose()`. If this function is never called, the policy implementation can make a reasonable assumption about the position of the robot. [Lula RRT](lula_rrt.html#isaac-sim-motion-generation-rrt) assumes that the robot is at the origin of the stage until it is told otherwise.
> * `PathPlanner.compute_path(active_joint_positions, watched_joint_positions)` expects robot joint positions and velocities to be passed in using the order specified by `PathPlanner.get_active_joints()` and `PathPlanner.get_watched_joints()`.

### Outputs: Path

`PathPlanner.compute_path(active_joint_positions, watched_joint_positions)` returns a set of configuration space waypoints that can be linearly interpolated to produce a collision free trajectory to reach a target-pose. The c-space configurations output by a PathPlanner will correspond only to the active joints returned by `PathPlanner.get_active_joints()`. The path output by a PathPlanner is difficult to use on its own; a linearly interpolated path will have sharp corners in c-space. But, a PathPlanner can be a useful component in generating a high-quality trajectory through difficult environments.

A helper class is provided with the PathPlanner interface to enable easy visualization of planned paths connected by linear interpolation in the [Path Planner Visualizer](#isaac-sim-path-planner-visualizer) class.

## Path Planner Visualizer

The PathPlannerVisualizer class is provided to make it easy to visualize the path output by a PathPlanner. This class handles the mapping between controllable DOFs in the robot Articulation and the active joints considered by the PathPlanner.

The main function of the class is `PathPlannerVisualizer.compute_plan_as_articulation_actions(max_c-space_dist)`. Calling this function queries the robot state from the robot Articulation, extracts and arranges the appropriate joints from the joint state
to use the `PathPlanner.compute_path()` function, linearly interpolates the result, and then creates a valid list of ArticulationAction that can be passed to the robot Articulation one by one to produce the planned path. The max\_c-space\_dist function determines the density of the linear interpolation such that the L2 norm between any two c-space positions in the output is less than or equal to max\_c-space\_dist.

On this page

* [Path Planner](#path-planner)
  + [Active and Watched Joints](#active-and-watched-joints)
  + [Inputs: World State](#inputs-world-state)
  + [Inputs: Robot State](#inputs-robot-state)
  + [Outputs: Path](#outputs-path)
* [Path Planner Visualizer](#path-planner-visualizer)

---

### RMPflow

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/manipulators/concepts/rmpflow.html

* [Robot Simulation](../../robot_simulation/index.html)
* [Motion Generation (Deprecated)](../motion_generation_overview.html)
* [Motion Generation](index.html)
* RMPflow

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# RMPflow

Deprecated

For new development, consider using the newer [Robot Motion (Experimental)](../../robot_motion_experimental/index.html) API, which provides improved interfaces and additional features over Lula.

[Riemannian Motion Policy (RMP)](../../reference_material/reference_glossary.html#isaac-sim-glossary-rmp) is a set of motion generation tools that underlies most Isaac Sim manipulator controls.
It creates smooth trajectories for the robots with intelligent collision avoidance.

A **Riemannian Motion Policy**, or *RMP*, is an acceleration policy
accompanied by a matrix \(M(q, \dot{q})\) that is sometimes called an inertia matrix,
borrowing terminology from classical mechanics, but is also closely related to the concept
of a Riemannian metric.

Leveraging the machinery of Riemannian geometry, *RMPflow* is a
framework for combining RMPs representing multiple (possibly competing) objectives and
constraints into a single global acceleration policy. Within this framework, the local RMPs
can be defined on any number of intermediate task spaces (including the operational space of
the end effector, generalizing operational space control). For details, refer to
[\*RMPflow: A computational graph for automatic motion policy generation\*](https://arxiv.org/abs/1811.07049).

Broadly defined, a *motion policy* is a mathematical function that takes the current
state of a robot (for example, position and velocity in generalized coordinates) and returns
a quantity representing a desired change in that state. Such a policy can depend
implicitly on variables representing one or more objectives or constraints, the state of
the environment. An *acceleration policy* is a motion policy where the output is
desired acceleration, \(\ddot q = \pi(q, \dot{q})\), resulting in a second-order
differential equation.

For the purpose of controlling a robot by position or velocity control, typically motion policies are used
where the output is position or velocity. Such
policies can be produced from an acceleration policy using a numerical
integration scheme such as Euler integration.

The [RMPflow Debugging Features](#isaac-sim-motion-generation-rmpflow-debugging-features) section reviews functions belonging to RMPflow that are not part of the MotionPolicy interface.
You can interact with RMPflow to control a robot that is already supported. If you are interested in the internal
mechanics of RMPflow or want to configure RMPflow for an unsupported robot, continue reading the RMPflow documentation.

After reviewing the basics here, also see the [RMPflow Tuning Guide](rmpflow_tuning_guide.html) for practical advice on configuring RMPflow for a new robot.

## RMPflow Debugging Features

By directly interacting with an RmpFlow instance, you can access features that are not available in other MotionPolicy implementations.
It is common for developers to want to decouple a [Motion Policy Algorithm](motion_policy.html#isaac-sim-motion-policy) from the simulated robot Articulation in NVIDIA Isaac Sim.
For example, when the simulated robot is moving sluggishly, it is important to determine whether the MotionPolicy or the PD gains have been improperly tuned,
but this can be difficult when both the PD gains and the MotionPolicy play a role in driving the robot joints (see [Outputs: Robot Joint Targets](motion_policy.html#isaac-sim-motion-policy-joint-targets)).

RMPflow provides visualization functions to clearly show the internal state of the algorithm as part of the stage. RMPflow uses collision spheres internally to
avoid hitting obstacles in the world. These spheres can be visualized over time by calling `RmpFlow.visualize_collision_spheres()`. The visualization will stop when
`RmpFlow.stop_visualizing_collision_spheres()` is called. The nominal end effector position can likewise be visualized with
`RmpFlow.visualize_end_effector_position()` and `RmpFlow.stop_visualizing_end_effector()`.

On their own, the visualization functions can be used to make sure that RMPflow’s internal representation of the robot is reasonable, but it does not help to decouple the
simulated robot from the RmpFlow internal representation of the robot.

On each frame when `RmpFlow.compute_joint_targets(active_joint_positions,...)` is called,
the visualization is updated to use the `active_joint_positions`. This behavior can be turned off using `RmpFlow.set_ignore_state_updates(True)`. When RmpFlow
is “ignoring state updates”, it starts ignoring the `active_joint_positions` argument, and instead begins internally tracking the believed state of the robot by assuming
that is completely independent of the physical simulation of the robot. When RmpFlow is set to ignore state updates from the simulator, and the visualization functions are used,
it becomes simple to determine if an undesirable robot behavior
comes from RmpFlow or from the robot Articulation and its PD gains.

## RMPflow Configuration

Three files are necessary to configure RMPflow for use with a new robot:

> * A **URDF** (universal robot description file), used for specifying robot kinematics
>   :   as well as joint and link names. Position limits for each joint are also required.
>       Other properties in the URDF are ignored and can be omitted; these include masses,
>       moments of inertia, visual, and collision meshes.
> * A **supplementary robot description file** in YAML format. In addition to enumerating
>   :   the list of actuated joints that define the configuration space (c-space) for the robot,
>       this file includes sections for specifying the default c-space configuration
>       and sets of collision spheres used for collision avoidance. This file can also
>       be used to specify fixed positions for unactuated joints.
> * A **RMPflow configuration file** in YAML format, containing parameters for all enabled RMPs.

As a general mathematical framework, RMPflow does not prescribe the form that individual RMPs
must take. The particular implementation of RMPflow in Lula (and by extension NVIDIA Isaac Sim) does
however expose a pre-specified set of RMPs that have been constructed and empirically found
to produce smooth reactive behaviors for a variety of manipulation tasks.

## C-Space Target RMP (c-space\_target\_rmp)

**Purpose:** Specifies a default c-space configuration for the robot, used for redundancy resolution.

**Definition:** Acceleration for this RMP is given by an equation similar to a PD controller, with a
position gain and damping gain, but the magnitude of the position term is capped when the C-space
distance exceeds a threshold. This cap avoids excessive forces when the configuration is far away
from the target. Defining \(q\) to be the full configuration vector:

\[\ddot q = k\_p r(q\_0 - q) - k\_d \dot q\,,\]

where the “robust capping function” \(r(p)\) is given by:

\[\begin{split}r(p) = \left \{ \begin{array}{cl}
p, & ||p|| < \theta \\
\theta\, p / ||p|| & \textrm{otherwise.}
\end{array} \right.\end{split}\]

The inertia matrix is proportional to the identity:

\[M = \mu I\]

The c-space\_target\_rmp section of the RMPflow configuration file contains an additional
inertia parameter \(m\). When this parameter is nonzero, it results in the introduction of
a conceptually separate RMP corresponding to zero c-space acceleration, \(\ddot q = 0\), with inertia
matrix given by \(M = mI\).

**Parameters:**

Units assume revolute joints where \(q\) is expressed in radians. If joints are instead prismatic,
robust\_position\_term\_thresh will have units of meters.

| Name | Symbol | Units | Meaning |
| --- | --- | --- | --- |
| metric\_scalar | \(\mu\) | - | Priority weight relative to other RMPs |
| position\_gain | \(k\_p\) | s-2 | Position gain, determining how strongly configuration is pulled toward target |
| damping\_gain | \(k\_d\) | s-1 | Damping gain, determining amount of “drag” |
| robust\_position\_term\_thresh | \(\theta\) | rad | Distance in c-space at which the position correction vector is capped |
| inertia | \(m\) | - | Additional c-space inertia |

## Target RMP (target\_rmp)

**Purpose:** Drives end effector toward specified position target.

**Definition:** Similar to the c-space target RMP, acceleration for this RMP resembles a PD
controller, albeit with a slightly different strategy for capping the magnitude of the position
correction vector.

\[\ddot x = k\_p (x\_0 - x) / (||x\_0-x|| + \epsilon) - k\_d \dot x\]

The inertia matrix blends between a rank-deficient metric \(S = n n^T`\), where \(n\) is
the direction vector toward the target, and the identity \(I\).

Intuitively, \(S\) cares
only about the direction toward the target (letting other RMPs such as the obstacle avoidance RMP
control the orthogonal directions).

\(I\) cares about all directions.

The contribution of
\(S\) is larger farther from the goal, allowing obstacles to push the system more effectively,
while \(I\) dominates near the goal, encouraging faster convergence.

Blending is
controlled by a radial basis function, specifically a Gaussian, that transitions from a minimum
constant value far from the target to 1 near the target.

Near the target, an additional nonlinear “proximity boost” multiplier turns on. This
factor takes the form of a Gaussian:

\[M = \left[\beta(x) b + (1-\beta(x))\right] \left[\alpha(x) M\_\textrm{near} + (1-\alpha(x)) M\_\textrm{far} \right]\]

where

\[\begin{split}\begin{array}{l}
\alpha(x) = (1-\alpha\_\textrm{min})\exp \left(\frac{-||x\_0-x||^2}{2 \sigma\_a^2}\right) + \alpha\_\textrm{min} \\
\beta(x) = \exp \left(-\frac{||x\_0 - x||^2}{2 \sigma\_b^2}\right) \\
M\_\textrm{near} = \mu\_\textrm{near} I \\
M\_\textrm{far} = \mu\_\textrm{far} S = \frac{\mu\_\textrm{far}}{||x\_0-x||^2} (x\_0-x)(x\_0-x)^T\,.
\end{array}\end{split}\]

**Parameters:**

| Name | Symbol | Units | Meaning |
| --- | --- | --- | --- |
| accel\_p\_gain | \(k\_p\) | m/s2 | Position gain |
| accel\_d\_gain | \(k\_d\) | s-1 | Damping gain |
| accel\_norm\_eps | \(\epsilon\) | m | Length scale controlling transition between constant acceleration region far from target and linear region near target |
| metric\_alpha\_length\_scale | \(\sigma\_a\) | m | Length scale of the Gaussian controlling blending between \(S\) and \(I\) |
| min\_metric\_alpha | \(\alpha\_\textrm{min}\) | - | Controls the minimum contribution of the isotropic \(M\_\textrm{near}\) term to the metric (inertia matrix) |
| max\_metric\_scalar | \(\mu\_\textrm{near}\) | - | Metric scalar for the isotropic \(M\_\textrm{near}\) contribution to the metric (inertia matrix) |
| min\_metric\_scalar | \(\mu\_\textrm{far}\) | - | Metric scalar for the directional \(M\_\textrm{far}\) contribution to the metric (inertia matrix) |
| proximity\_metric\_boost\_scalar | \(b\) | - | Scale factor controlling the strength of boosting near the target |
| proximity\_metric\_boost\_length\_scale | \(\sigma\_b\) | m | Length scale of the Gaussian controlling boosting near the target |
| xi\_estimator\_gate\_std\_dev | - | - | Unused parameter (to be removed in a future release) |

## Axis Target RMP (axis\_target\_rmp)

**Purpose:** Drives x-, y-, or z-axis of end effector frame toward target orientation. This
RMP is used for general orientation targets (where an axis target RMP is added for each of the
three axes) as well as for “partial pose” targets where only alignment of a single axis is
desired.

Note

Partial pose targets are not supported by the Motion Generation extension.

**Definition:**

Similar to the (position) target RMP, the axis target RMP supports “proximity boosting,”
but only when a target RMP is active at the same time. In this case, it’s the distance to
the position target (\(||x\_0-x||\)) that controls the strength of boosting.

The current and desired axis orientations are represented by unit vectors, denoted
by \(n\) and \(n\_0\) respectively. Acceleration is given by:

\[\ddot n = k\_p (n\_0 - n) - k\_d \dot n\,\]

If a position target (that is, target RMP) is active, the metric has the form:

\[M\_\textrm{boosted} = \left[\beta(x) b + (1-\beta(x))\right] \mu I\,\]

where:

\[\beta(x) = \exp \left(-\frac{||x\_0 - x||^2}{2 \sigma\_b^2}\right)\,\]

When no position target is active, this simplifies to:

\[M = \mu I\,.\]

**Parameters:**

| Name | Symbol | Units | Meaning |
| --- | --- | --- | --- |
| accel\_p\_gain | \(k\_p\) | s-2 | Position gain |
| accel\_d\_gain | \(k\_d\) | s-1 | Damping gain |
| metric\_scalar | \(\mu\) | - | Priority weight relative to other RMPs |
| proximity\_metric\_boost\_scalar | \(b\) | - | Scale factor controlling the strength of boosting near the position target |
| proximity\_metric\_boost\_length\_scale | \(\sigma\_b\) | m | Length scale of the Gaussian controlling boosting near the position target |

## Joint Limit RMP (joint\_limit\_rmp)

**Purpose:** Avoids joint limits.

**Definition:** This is a one-dimensional RMP that depends on a single
c-space coordinate (joint) and a corresponding upper or lower joint limit as specified in
the URDF for the robot. If a robot has \(N\) joints, it follows that a total of \(2N\)
joint limit RMPs will be introduced. The joint limits specified in the URDF can be padded
(that is, made more conservative) by entering positive padding values in the joint\_limit\_buffers
array in the RMPflow configuration file. For a given joint, the same padding value is used
for both upper and lower limits.

The task space for this RMP consists of a shifted and scaled c-space coordinate, measuring
the scaled distance to either the upper or lower joint limit. Without loss of generality,
we consider a lower joint limit RMP. If \(q\) is the c-space coordinate for a given
joint, and \(q\_\textrm{upper}\) and \(q\_\textrm{lower}\) are the upper and lower
limits for that joint, respectively, we define:

\[x = \frac{q - q\_\textrm{lower}}{q\_\textrm{upper} - q\_\textrm{lower}}\,\]

The acceleration for that coordinate is then given by:

\[\ddot x = \frac{k\_p}{x^2/\ell\_p^2 + \epsilon\_p} - k\_d \dot x\,\]

The metric (inertia matrix) is a scalar given by:

\[m = \left(1 - \frac{1}{1+\exp(-\dot x/v\_m)}\right) \frac{\mu}{x/\ell\_m + \epsilon\_m}\,\]

**Parameters:**

| Name | Symbol | Units | Meaning |
| --- | --- | --- | --- |
| metric\_scalar | \(\mu\) | - | Overall priority weight relative to other RMPs |
| metric\_length\_scale | \(\ell\_m\) | - | Length scale controlling ramp-up of metric as joint limit is approached |
| metric\_exploder\_eps | \(\epsilon\_m\) | - | Offset determining \(x\) value at which metric diverges |
| metric\_velocity\_gate\_length\_scale | \(v\_m\) | s-1 | Scale determining rate at which metric increases with velocity in direction of barrier |
| accel\_damper\_gain | \(k\_d\) | s-1 | Damping gain |
| accel\_potential\_gain | \(k\_p\) | s-2 | Gain multiplying position barrier term |
| accel\_potential\_exploder\_length\_scale | \(\ell\_p\) | - | Length scale controlling steepness of position barrier |
| accel\_potential\_exploder\_eps | \(\epsilon\_p\) | - | Offset limiting divergence of position barrier strength |

## Joint Velocity Limit RMP (joint\_velocity\_cap\_rmp)

**Purpose:** Limits maximum joint velocity.

**Definition:** This RMP applies damping when the magnitude of the velocity of a given joint
approaches the specified limit.

This is a one-dimensional RMP with acceleration given by:

\[\ddot q = -k\_d\,\textrm{sgn}(\dot q) \left(|\dot q| - (v\_\textrm{max} - v\_r)\right)\,\]

The metric (inertia matrix) is a scalar given by:

\[\begin{split}m = \left \{ \begin{array}{cl}
0, & |\dot q| < (v\_\textrm{max} - v\_r) \\
\frac{\mu}{1 - \left(|\dot q| - (v\_\textrm{max} - v\_r)\right)^2 / v\_r^2} & \textrm{otherwise.}
\end{array} \right\end{split}\]

The metric is zero outside you-specified damping region, thereby disabling this RMP.
In addition, clipping is applied to avoid divergence of the metric as \(\dot q\) approaches \(v\_\textrm{max}\).

**Parameters:**

Units assume revolute joints where \(q\) is expressed in radians. If joints are instead prismatic,
max\_velocity and velocity\_damping\_region will have units of m/s.

| Name | Symbol | Units | Meaning |
| --- | --- | --- | --- |
| max\_velocity | \(v\_\textrm{max}\) | rad/s | Maximum allowed velocity magnitude |
| velocity\_damping\_region | \(v\_r\) | rad/s | Defines width of velocity region affect by damping |
| damping\_gain | \(k\_d\) | s-1 | Damping gain |
| metric\_weight | \(\mu\) | - | Overall priority weight relative to other RMPs |

## Collision Avoidance RMP (collision\_rmp)

**Purpose:** Avoids collision with obstacles in the environment.

**Definition:** This is a one-dimensional RMP where the task space consists of a single
coordinate measuring distance from a given collision sphere on the robot (specified in the
robot description YAML file) to an obstacle in the environment. Denoting that coordinate
as \(x\), the acceleration is given by:

\[\ddot x = k\_p \exp(-x / \ell\_p) - k\_d \left[1 - \frac{1}{1 + \exp(-\dot x/v\_d)} \right] \frac{\dot x}{x/\ell\_d + \epsilon\_d}\,\]

The metric (inertia matrix) is a scalar given by:

\[m = \left[1 - \frac{1}{1 + \exp(-\dot x/v\_d)} \right] g(x) \frac{\mu}{x / \ell\_m + \epsilon\_m}\,\]

where \(g(x)\) is a piecewise polynomial that varies smoothly from 1 to 0 as \(x\) varies from 0 to \(r\)

\[\begin{split}g(x) = \left \{ \begin{array}{cl}
x^2/r^2 -2s/r + 1, & x\le r \\
0, & x\gt r
\end{array} \right.\end{split}\]

**Parameters:**

| Name | Symbol | Units | Meaning |
| --- | --- | --- | --- |
| damping\_gain | \(k\_d\) | s-1 | Damping gain |
| damping\_std\_dev | \(\ell\_d\) | m | Length scale controlling increase in acceleration as obstacle is approached |
| damping\_robustness\_eps | \(\epsilon\_d\) | - | Offset determining \(x\) value at which acceleration diverges (before clipping) |
| damping\_velocity\_gate\_length\_scale | \(v\_d\) | m/s | Scale determining velocity dependence of “velocity gating” function |
| repulsion\_gain | \(k\_p\) | m/s2 | Gain for position repulsion term |
| repulsion\_std\_dev | \(\ell\_p\) | m | Length scale controlling distance dependence of repulsion |
| metric\_modulation\_radius | \(r\) | m | Length scale determining distance from obstacle at which RMP is disabled completely |
| metric\_scalar | \(\mu\) | - | Overall priority weight relative to other RMPs |
| metric\_exploder\_std\_dev | \(\ell\_m\) | m | Length scale controlling increase in metric as obstacle is approached |
| metric\_exploder\_eps | \(\epsilon\_m\) | - | Offset determining \(x\) value at which metric diverges (before clipping) |

## Damping RMP (damping\_rmp)

**Purpose:** Contributes additional nonlinear damping based on control frame
(for example, end effector) velocity relative to target.

**Definition:** This is a one-dimensional RMP where the task space consists of a single coordinate
\(x\) measuring distance from the origin of the control frame to the target.
The acceleration is given by:

\[\ddot x = -k\_d |\dot x|\dot x\]

and the metric by:

\[M = \mu |\dot x| I\,\]

The damping\_rmp section of the RMPflow configuration file contains an additional
inertia parameter \(m\). When this parameter is nonzero, it results in the introduction of
a conceptually separate RMP corresponding to zero acceleration, \(\ddot x = 0\), with inertia
matrix given by \(M = mI\).

**Parameters:**

| Name | Symbol | Units | Meaning |
| --- | --- | --- | --- |
| accel\_d\_gain | \(k\_d\) | m-1 | Nonlinear damping gain |
| metric\_scalar | \(\mu\) | (m/s)-1 | Priority weight relative to other RMPs |
| inertia | \(m\) | - | Additional inertia |

## Further Reading

Refer to the [RMPflow Tuning Guide](rmpflow_tuning_guide.html) for practical advice on configuring RMPflow for a new robot.

On this page

* [RMPflow Debugging Features](#rmpflow-debugging-features)
* [RMPflow Configuration](#rmpflow-configuration)
* [C-Space Target RMP (c-space\_target\_rmp)](#c-space-target-rmp-c-space-target-rmp)
* [Target RMP (target\_rmp)](#target-rmp-target-rmp)
* [Axis Target RMP (axis\_target\_rmp)](#axis-target-rmp-axis-target-rmp)
* [Joint Limit RMP (joint\_limit\_rmp)](#joint-limit-rmp-joint-limit-rmp)
* [Joint Velocity Limit RMP (joint\_velocity\_cap\_rmp)](#joint-velocity-limit-rmp-joint-velocity-cap-rmp)
* [Collision Avoidance RMP (collision\_rmp)](#collision-avoidance-rmp-collision-rmp)
* [Damping RMP (damping\_rmp)](#damping-rmp-damping-rmp)
* [Further Reading](#further-reading)

---

### RMPflow Tuning

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/manipulators/concepts/rmpflow_tuning_guide.html

* [Robot Simulation](../../robot_simulation/index.html)
* [Motion Generation (Deprecated)](../motion_generation_overview.html)
* [Motion Generation](index.html)
* RMPflow Tuning Guide

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# RMPflow Tuning Guide

Deprecated

For new development, consider using the newer [Robot Motion (Experimental)](../../robot_motion_experimental/index.html) API, which provides improved interfaces and additional features over Lula. This
page is still a valid tuning guide for RMPflow in [cuMotion](https://nvidia-isaac.github.io/cumotion/).

Given the number of parameters involved in fully specifying a complete set of RMPs,
tuning an RMPflow-based motion policy for a new robot or task can be intimidating.
In practice, however, parameters that work well for one robot are likely to work well
for other robots with similar morphology. Furthermore, for a given robot, it is
generally possible to choose a set of parameters that work well for a wide variety
of tasks.

To review RMPflow and its features see, [RMPflow](rmpflow.html).

NVIDIA Isaac Sim includes example RMPflow configuration files for multiple robot arms, including
the 7-DOF Franka Emika Panda and the 6-DOF Universal Robots UR10. When tuning RMPflow for a
new manipulator, it’s usually best to start with one of these two files. If the new robot
is significantly larger or smaller than the one used as a reference, it might be necessary
to rescale any parameters that have units of length. If the number of joints differ, the
c-space\_target\_rmp/robust\_position\_term\_thresh parameter might also have to be adjusted.
Often, these steps are sufficient to produce a working motion policy.

If adapting an existing RMPflow configuration fails to produce acceptable results, use
the following procedure to tune a new policy from scratch:

Hint

It can helpful to play with parameter values for an existing robot (for example, the Franka).

1. Turn off all RMPs.
2. Each RMP has a parameter called either metric\_weight or metric\_scalar. Setting this parameter to zero will disable the corresponding RMP. For the target RMP, set the parameters min\_metric\_scalar, max\_metric\_scalar, and min\_metric\_alpha all to zero.
3. Set all inertia terms to zero (that is, c-space\_target\_rmp/inertia and damping\_rmp/inertia).
4. Re-enable RMPs one at a time, in the following suggested order:

   1. **c-space\_target\_rmp:** To get the robot moving to a configuration in c-space robustly.
      The magnitude of the metric scalar should be kept relatively small (for example, in the range 1 to 100), because
      this sets the global scale of all RMPs.
      Remember to set the default configuration in the robot description file (YAML) to a reasonable natural
      “ready” posture. This will be the default posture that the robot will favor while moving from place to place.
   2. **target\_rmp:** To get the end effector moving to a target robustly while continuing
      to use the c-space target RMP for redundancy resolution.

      1. Set target\_rmp/min\_metric\_alpha to zero and target\_rmp/metric\_alpha\_length\_scale
         to a large value relative to the size of the robot (in meters), such as 100,000. This effectively turns
         off the directional \(S\) term in the metric, reducing \(M\) to a simpler isotropic metric.
      2. Set target\_rmp/proximity\_metric\_boost\_length\_scalar to 1 to turn off priority boosting.
      3. Set target\_rmp/max\_metric\_scalar to a large value relative to c-space\_target\_rmp/metric\_scalar
         so it dominates. This will effectively make the c-space target RMP operate purely in the
         nullspace of the target RMP.
      4. Tune target\_rmp/accel\_p\_gain, target\_rmp/accel\_d\_gain, and target\_rmp/accel\_norm\_eps until
         good attractor behavior for the end effector has been achieved.
      5. Experiment with reducing target\_rmp/max\_metric\_scalar to ensure that it’s not too large. As
         max\_metric\_scalar is increased toward a suitable value, convergence accuracy should progressively
         improve. If convergence accuracy saturates at small constant error before the chosen max\_metric\_scalar
         value is reached, then it is probably set too high. This will be relevant when re-enabling the directional
         term in the target RMP metric below, ensuring that it makes a difference when the metric scalar decreases.
   3. **collision\_rmp:** Enable the collision avoidance RMP by setting collision\_rmp/metric\_scalar to a value
      comparable to target\_rmp/max\_metric\_scalar. It can be useful to plot the formulas for the acceleration
      and metric to gain some understanding of the roles of the various parameters.
   4. **target\_rmp (redux):** After the collision RMP is enabled, the system will probably drag near obstacles
      more slowly than it usually moves because the target RMP is fighting with the collision RMPs.
      Turning on the directional term in the metric will correct that effect.

      1. Plot the target RMP metric (as a function of distance from target)
         to build understanding. Try this first without the boosting term, noting how the metric transitions
         from the reduced-rank far metric to the full-rank near metric.
      2. Set target\_rmp/min\_metric\_alpha to a non-zero value and reduce the value of
         target\_rmp/metric\_alpha\_length\_scale until good behavior is achieved.
   5. **axis\_target\_rmp:** If an orientation target is set, the axis target RMP will be used to bring
      the orientation of the control frame (for example, end effector) into alignment with the target orientation.
      This RMP includes a “priority boosting” factor that depends on distance to the current
      position target, if one is set. This allows the robot to make progress toward the position
      target before zeroing in on the desired orientation.
   6. **joint\_limit\_rmp:** When properly tuned, behavior should be unchanged, except that joint
      limits will be avoided.
   7. **damping\_rmp:** Enable the damping RMP as well as target\_rmp/inertia to reduce jerk as necessary.

Throughout this process, referring to an existing RMPflow configuration file is helpful.

---

### Trajectory Interface

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/manipulators/concepts/trajectory_interface.html

* [Robot Simulation](../../robot_simulation/index.html)
* [Motion Generation (Deprecated)](../motion_generation_overview.html)
* [Motion Generation](index.html)
* Trajectory Generation

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Trajectory Generation

Deprecated

For new development, consider using the newer [Robot Motion (Experimental)](../../robot_motion_experimental/index.html) API, which provides improved interfaces and additional features.

In the Motion Generation extension, a workflow is provided for defining c-space and task-space trajectories. An interface is provided for a [Trajectory Interface](#isaac-sim-trajectory) class:

* Trajectory Interface
* Articulation Trajectory
* Lula Trajectory Generator

## Trajectory Interface

An interface is provided in the Motion Generation extension for defining a robot trajectory.
An instance of the Trajectory interface must return robot c-space position as a continuous function of time within a specified time horizon. A Trajectory has four basic accessors:

* **start\_time**: The earliest time at which this Trajectory will return a robot c-space position.
* **end\_time**: The latest time at which this Trajectory will return a robot c-space position.
* **active\_joints**: The names of the joints that this Trajectory is intended to control corresponding to the order the joint targets are returned.
* **joint\_targets(time)**: Joint position/velocity targets as a function of time between start\_time and end\_time.

An instance of the Trajectory class can be used to directly control a robot by using it to initialize an [Articulation Trajectory](#isaac-sim-articulation-trajectory).

## Articulation Trajectory

The ArticulationTrajectory class is initialized using a robot Articulation and an instance of the Trajectory class.
This class handles the mapping from a defined Trajectory to controlling a simulated robot Articulation. The ArticulationTrajectory class has two main functions:

* **get\_action\_at\_time(time)**: Return an ArticulationAction at a time that is within the time horizon of the provided Trajectory object.
* **get\_action\_sequence(timestep)**: Return a list of ArticulationAction that interpolates between the provided Trajectory start\_time and end\_time by the specified timestep. This is a convenience method for when the timestep of the physics simulator is known to be fixed.

As a Trajectory only defines the robot behavior within the provided time horizon, it is necessary to bring the robot Articulation to the initial state of the Trajectory before attempting to follow a sequence of generated ArticultionAction.

## Lula Trajectory Generator

We provide a **Lula** implementation of a trajectory generator that can generate a Trajectory given c-space or task-space waypoints. Two classes are provided:

* LulaCSpaceTrajectoryGenerator
* LulaTaskSpaceTrajectoryGenerator

Both classes share the same required configuration information.

To configure Lula Trajectory Generators for a specific robot you must have the following files:

> * A URDF (universal robot description file), used for specifying robot kinematics as well as joint and link names. Position limits for each joint are also required. Other properties in the URDF are ignored and can be omitted; these include masses, moments of inertia, visual and collision meshes.
> * A supplemental robot description file in YAML format. In addition to enumerating the list of actuated joints that define the configuration space (c-space) for the robot, this file also includes sections for specifying the default c-space configuration, acceleration limits, or jerk limits. This file can also be used to specify fixed positions for unactuated joints.

### Lula C-Space Trajectory Generator

The `LulaCSpaceTrajectoryGenerator` class takes in a series of c-space waypoints that correspond to the c-space coordinates listed in the required robot description YAML file.
The generator will use spline-based interpolation to connect the waypoints with an initial and final velocity of 0.
The trajectory is time-optimal – that is, either the velocity, acceleration, or jerk limits are saturated at any given time to produce a trajectory with as short a duration as possible.
The generator will return an instance of the Trajectory interface.

### Lula Task-Space Trajectory Generator

The `LulaTaskSpaceTrajectoryGenerator` class takes in a sequence of task-space targets and an end effector frame name (which must be a valid frame in the provided URDF file), and it returns an instance of the Trajectory interface if possible.

Task-space trajectories can be defined as a series of position and orientation targets. In this case, the generated trajectory will linearly interpolate in task-space between the provided targets.

Task-space trajectories can also be defined using the `lula.TaskSpacePathSpec` class, which provides a set of useful primitives to connect task-space waypoints such as creating an arc, pure rotation, pure translation.

Internally, a task-space trajectory is converted to a c-space trajectory using the
[Lula Kinematics Solver](kinematics_solver.html#isaac-sim-lula-kinematics-solver), and is then passed through the `LulaCSpaceTrajectoryGenerator`. For this reason, the `LulaTaskSpaceTrajectoryGenerator` class shares the same set of parameters as the `LulaCSpaceTrajectoryGenerator` class, with added parameters that affect how the task-space trajectory is converted to c-space.

On this page

* [Trajectory Interface](#trajectory-interface)
* [Articulation Trajectory](#articulation-trajectory)
* [Lula Trajectory Generator](#lula-trajectory-generator)
  + [Lula C-Space Trajectory Generator](#lula-c-space-trajectory-generator)
  + [Lula Task-Space Trajectory Generator](#lula-task-space-trajectory-generator)

---

### Configure RMPflow Denso

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/manipulators/manipulators_configure_rmpflow_denso.html

* [Robot Simulation](../robot_simulation/index.html)
* [Motion Generation (Deprecated)](motion_generation_overview.html)
* Configuring RMPflow for a New Manipulator

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Configuring RMPflow for a New Manipulator

In this tutorial, you learn how the [RMPflow](concepts/rmpflow.html#isaac-sim-motion-generation-rmpflow) algorithm can be fully configured following the creation of a Robot Description File.

## Getting Started

**Prerequisites**

* **Complete** the [Lula Robot Description and XRDF Editor](manipulators_robot_description_editor.html#isaac-sim-app-tutorial-motion-generation-robot-description-editor) tutorial to create one of the two required configuration files for using RmpFlow.
* Review the [Tutorial 7: Configure a Manipulator](../robot_setup_tutorials/tutorial_configure_manipulator.html) prior to beginning this tutorial to obtain a robot Articulation USD asset.

This tutorial provides a URDF file and USD file describing the **Cobotta Pro 900** robot. The USD file was generated from the URDF using the process discussed in [Tutorial 6: Setup a Manipulator](../robot_setup_tutorials/tutorial_import_assemble_manipulator.html).

Open the tutorial assets from the Content Browser at this path: `Isaac Sim/Samples/Rigging/Cobotta_Pro_900_Assets`

## Using the Lula Test Widget

This tutorial demonstrates how RMPflow can be configured and tested on a new robot using the Lula Test Widget. The Lula Test Widget is an extension that can
be enabled in the Extensions menu as shown below, and then accessed under **Tools > Robotics > Lula Test Widget**.

This extension allows you to select their RMPflow config files along with a selected robot Articulation on the USD stage and run scenarios to verify that
RMPflow is working as intended. After each type of required config file is created, they can be loaded and used in the Lula Test Widget.

## Template RmpFlow Config File

There are three files to describe the robot and parameterize the
[RMPflow](concepts/rmpflow.html#isaac-sim-motion-generation-rmpflow) algorithm:

> * A **URDF** (universal robot description file), used for specifying robot kinematics
>   :   as well as joint and link names. Position limits for each joint are also required.
>       Other properties in the URDF are ignored and can be omitted; these include masses,
>       moments of inertia, visual and collision meshes.
> * A **supplementary robot description file** in YAML format. This file can be generated using the Lula Robot Description Editor UI tool.
> * A **RMPflow configuration file** in YAML format, containing parameters for all enabled RMPs.

This tutorial assumes that you is starting with a URDF file describing their robot and has created a Robot Description File using the
[Lula Robot Description and XRDF Editor](manipulators_robot_description_editor.html#isaac-sim-app-tutorial-motion-generation-robot-description-editor).
In this tutorial, a template files is provided for the remaining RMPflow configuration, which is
modified to match the **Cobotta Pro 900** robot. The tutorial assets contain a completed robot\_description.yaml for the **Cobotta Pro 900**.

### Template RmpFlow Config YAML File

The RMPflow algorithm has over 50 settable parameters, but these parameters tend to generalize between robots with similar kinematic structures
and length scales. The values in the template have been tuned specifically for the Franka Emika Panda,
but serve as a good starting point for many 6- and 7-dof robot arms. The template file can be found in
the tutorial assets as rmpflow\_configs/template\_rmpflow\_config.yaml.

```python
 1# Artificially limit the robot joints.  For example:
 2# A joint with range +-pi would be limited to +-(pi-.01)
 3joint_limit_buffers: [.01, .01, .01, .01, .01, .01, .01]
 4
 5# RMPflow has many modifiable parameters, but these serve as a great start.
 6# Most parameters will not need to be modified
 7rmp_params:
 8    cspace_target_rmp:
 9        metric_scalar: 50.
10        position_gain: 100.
11        damping_gain: 50.
12        robust_position_term_thresh: .5
13        inertia: 1.
14    cspace_trajectory_rmp:
15        p_gain: 100.
16        d_gain: 10.
17        ff_gain: .25
18        weight: 50.
19    cspace_affine_rmp:
20        final_handover_time_std_dev: .25
21        weight: 2000.
22    joint_limit_rmp:
23        metric_scalar: 1000.
24        metric_length_scale: .01
25        metric_exploder_eps: 1e-3
26        metric_velocity_gate_length_scale: .01
27        accel_damper_gain: 200.
28        accel_potential_gain: 1.
29        accel_potential_exploder_length_scale: .1
30        accel_potential_exploder_eps: 1e-2
31    joint_velocity_cap_rmp:
32        max_velocity: 4.
33        velocity_damping_region: 1.5
34        damping_gain: 1000.0
35        metric_weight: 100.
36    target_rmp:
37        accel_p_gain: 30.
38        accel_d_gain: 85.
39        accel_norm_eps: .075
40        metric_alpha_length_scale: .05
41        min_metric_alpha: .01
42        max_metric_scalar: 10000
43        min_metric_scalar: 2500
44        proximity_metric_boost_scalar: 20.
45        proximity_metric_boost_length_scale: .02
46        xi_estimator_gate_std_dev: 20000.
47        accept_user_weights: false
48    axis_target_rmp:
49        accel_p_gain: 210.
50        accel_d_gain: 60.
51        metric_scalar: 10
52        proximity_metric_boost_scalar: 3000.
53        proximity_metric_boost_length_scale: .08
54        xi_estimator_gate_std_dev: 20000.
55        accept_user_weights: false
56    collision_rmp:
57        damping_gain: 50.
58        damping_std_dev: .04
59        damping_robustness_eps: 1e-2
60        damping_velocity_gate_length_scale: .01
61        repulsion_gain: 800.
62        repulsion_std_dev: .01
63        metric_modulation_radius: .5
64        metric_scalar: 10000.
65        metric_exploder_std_dev: .02
66        metric_exploder_eps: .001
67    damping_rmp:
68        accel_d_gain: 30.
69        metric_scalar: 50.
70        inertia: 100.
71
72canonical_resolve:
73    max_acceleration_norm: 50.
74    projection_tolerance: .01
75    verbose: false
76
77
78# body_cylinders are used to promote self-collision avoidance between the robot and its base
79# The example below defines the robot base to be a capsule defined by the absolute coordinates pt1 and pt2.
80# The semantic name provided for each body_cylinder does not need to be present in the robot URDF.
81body_cylinders:
82     - name: base
83       pt1: [0,0,.333]
84       pt2: [0,0,0.]
85       radius: .05
86
87
88# body_collision_controllers defines spheres located at specified frames in the robot URDF
89# These spheres will not be allowed to collide with the capsules enumerated under body_cylinders
90# By design, most frames in industrial robots are kinematically unable to collide with the robot base.
91# It is often only necessary to define body_collision_controllers near the end effector
92body_collision_controllers:
93     - name: end_effector
94       radius: .05
```

This tutorial focuses on three fields in this file:

* `joint_limit_buffers` introduces artificial joint limits around the joint limits stated in the robot URDF. The shape of the provided `joint_limit_buffers` must match the c-space given in the `robot_description.yaml` file. Imagining that the template robot has seven revolute joints, the given buffers of .01 on the seven c-space joints mean that RMPflow will drive the robot up to .01 radians from the joint limits given in the robot URDF. If the robot has prismatic joints, a value of .01 would be expressed implicitly in meters.
* `body_cylinders` and `body_collision_controllers` help RMPflow to avoid self-collision between the end effector and the robot base. `body_cylinders` define an imagined robot base using a set of capsules.
* `body_collision_controllers` define collision spheres placed on different frames of the robot URDF. The template code above defines an unmoving capsule in absolute coordinates and a sphere centered around the “end\_effector” frame in the robot URDF. RMPflow will not allow a collision between the sphere and capsule.

Apart from preventing the end effector from colliding with the base, RMPflow does not directly avoid self-collisions based on collision geometry.

For most applications, however, joint limits are sufficient to prevent links in the middle of the kinematic chain from colliding with each other.

## Modifying the Template for the Cobotta Pro 900

### Doing the Bare Minimum

The minimum changes required to get the **Cobotta** to be able to use RMPflow to follow a target.

The `rmpflow_config` file requires little work to get started (rmpflow\_configs/rmpflow\_config\_basic.yaml in the tutorial assets):

```python
 1# Artificially limit the robot joints.  For example:
 2# A joint with range +-pi would be limited to +-(pi-.01)
 3joint_limit_buffers: [.01, .01, .01, .01, .01, .01]
 4
 5#Omitting `rmp_params` argument
 6
 7# body_cylinders are used to promote self-collision avoidance between the robot and its base
 8# The example below defines the robot base to be a capsule defined by the absolute coordinates pt1 and pt2.
 9# The semantic name provided for each body_cylinder does not need to be present in the robot URDF.
10body_cylinders:
11     - name: base
12       pt1: [0,0,.333]
13       pt2: [0,0,0.]
14       radius: .05
15
16
17# body_collision_controllers defines spheres located at specified frames in the robot URDF
18# These spheres will not be allowed to collide with the capsules enumerated under body_cylinders
19# By design, most frames in industrial robots are kinematically unable to collide with the robot base.
20# It is often only necessary to define body_collision_controllers near the end effector
21body_collision_controllers:
22     - name: right_inner_finger
23       radius: .05
```

To get the robot moving around, you can ignore the `rmp_params` argument for now. Modify the `joint_limit_buffers`
argument to represent that the robot only has six DOFs rather than the seven listed in the template. You have to provide
`body_cylinders`, you will represent the robot base later. One change was
required to the default `body_collision_controllers` argument, that was to change the frame at which you place a collision
sphere. There is no `end_effector` frame in the **Cobotta** URDF, so for now pick a frame that is near the end effector:
`right_inner_finger`.

In the Lula Test Widget, observe that the robot is able to follow the target and avoid obstacles.
Notice that the frame that RMPflow is moving to the target position is not in the center of the gripper. In the Lula Test Widget, the
`right_inner_finger` is selected as the end effector frame. The available end effector frames come from the robot URDF file, and there is not a frame resting
in the center of the gripper.

### Avoiding Self-Collision: Configuring Body Cylinders and Body Collision Controllers

With a completed Robot Description File, the robot will avoid collisions with external obstacles, but it will not avoid self-collision.
There is limited tooling available for avoiding self-collision because industrial robot arms typically remove most potential for self-collision
with joint limits. However, some exploration is required with a particular robot to learn what types of self-collision are possible.
With the preliminary configuration of body cylinders and body collision controllers. You set in the `Cobotta_Pro_900_Assets/rmpflow_configs/cobotta_rmpflow_config_basic.yaml` file,
it is easy to cause collisions between the robot end effector and the robot base.

`body_cylinders` define an imagined robot base using a set of capsules. `body_collision_controllers` define collision spheres placed
on different frames of the robot URDF.

RMPflow will not allow these spheres and capsules to come into contact with each other. In the basic `rmpflow` config, you defined the base as the capsule
connecting two spheres of radius `.05 m` at the absolute coordinates ([0,0,0], [0,0,.333]) (refer to [Doing the Bare Minimum](#isaac-sim-tutorial-configure-rmpflow-bare-minimum)),
and you define a single `body_collision_controller` at the `right_inner_finger` frame.

In the video above, you observe that the gripper will not pass directly
through the robot base, but it is easy to facilitate a self-collision with the edge of the robot base, or the base of the second link.

The self-collision tooling available in RMPflow does not allow you to avoid all self-collisions without sacrificing some acceptable robot configurations as well.

To make self collisions completely impossible for the **Cobotta**, you need a very conservative estimate of the robot base.
You would not allow the gripper to move close to the base at all. Choosing the best possible configuration is use-case dependent.
There is no reason to take away maneuverability around the robot base unless you observe that the robot is self-colliding.

One potential configuration in this tutorial covers the other frames in the gripper and exaggerates the size of the robot base to make it
harder for the gripper to intersect with the robot’s second link. The sizes and locations for the capsule and spheres are based on the collision spheres that
you’ve already added.

```python
 1# body_cylinders are used to promote self-collision avoidance between the robot and its base
 2# The example below defines the robot base to be a capsule defined by the absolute coordinates pt1 and pt2.
 3# The semantic name provided for each body_cylinder does not need to be present in the robot URDF.
 4body_cylinders:
 5     - name: base
 6       pt1: [0,0,.12]
 7       pt2: [0,0,0.]
 8       radius: .08
 9     - name: second_link
10       pt1: [0,0,.12]
11       pt2: [0,0,.12]
12       radius: .16
13
14
15# body_collision_controllers defines spheres located at specified frames in the robot URDF
16# These spheres will not be allowed to collide with the capsules enumerated under body_cylinders
17# By design, most frames in industrial robots are kinematically unable to collide with the robot base.
18# It is often only necessary to define body_collision_controllers near the end effector
19body_collision_controllers:
20     - name: J5
21       radius: .05
22     - name: J6
23       radius: .05
24     - name: right_inner_finger
25       radius: .02
26     - name: left_inner_finger
27       radius: .02
28     - name: right_inner_knuckle
29       radius: .02
30     - name: left_inner_knuckle
31       radius: .02
```

You represent the robot base link “J1” with a capsule of radius .08 m, which matches the size of the collision spheres in near the base of the robot.
You represent the robot’s second link with a large sphere of radius .12.
In the Lula Test Widget, you observe the robot does a much better job avoiding collisions with the first and second link.
As expected, it is still possible to cause a self-collision, but the cases are much more limited.

### Creating an End Effector Frame

Observe that the chosen end effector frame `right_inner_finger` does not directly
represent the position of the robot’s gripper. The frame that RMPflow considers to be the end effector must be present in the robot URDF.
In this tutorial, you selected a frame near the end of the robot as the best option. To directly control where the center of the gripper is, you have two options:

* Manually compute transforms between the desired target and the target you send to RMPflow at runtime.
* Add a frame to the robot’s URDF.

This tutorial covers the second option by adding a frame to the **Cobotta Pro 900** URDF. Typically, the end effector position is in
the center of the gripper, with two principal axes aligned with the gripper fingers.

Investigating the **Cobotta Pro 900** URDF, you observe how the “right\_inner\_finger” frame is connected to the robot arm.
In the URDF, you observe that the “right\_inner\_finger” joint is a grandchild of the “onrobot\_rg6\_base\_link” frame, which is at the gripper base.

```python
 1<joint name="right_inner_finger_joint" type="revolute">
 2    <origin rpy="0 0 0" xyz="0 -0.047334999999999995 0.064495"/>
 3    <parent link="right_outer_knuckle"/>
 4    <child link="right_inner_finger"/>
 5    <axis xyz="1 0 0"/>
 6    <limit effort="1000" lower="-0.872665" upper="0.872665" velocity="2.0"/>
 7    <mimic joint="finger_joint" multiplier="1" offset="0"/>
 8  </joint>
 9
10<joint name="right_outer_knuckle_joint" type="revolute">
11    <origin rpy="0 0 3.141592653589793" xyz="0 0.024112 0.136813"/>
12    <parent link="onrobot_rg6_base_link"/>
13    <child link="right_outer_knuckle"/>
14    <axis xyz="1 0 0"/>
15    <limit effort="1000" lower="-0.628319" upper="0.628319" velocity="2.0"/>
16    <mimic joint="finger_joint" multiplier="-1" offset="0"/>
17  </joint>
```

This tells us that you can create a frame that is offset from the “`onrobot_rg6_base_link`” frame by a pure Z offset of `.064495+.136813=.2013` to represent a point in the center of the gripper, aligned with the “`right_inner_finger_joint`” and “`left_inner_finger_joint`”. To get closer with the tips of the fingers, increase the Z offset to .24.

Add a link to the URDF called “gripper\_center”, whose offset from the parent link “`onrobot_rg6_base_link`” is defined by the connection
“`gripper_center_joint`”. In the tutorial file, the modified URDF is saved as `./cobotta_pro_900_gripper_frame.urdf`.

```python
1<link name="gripper_center"/>
2  <joint name="gripper_center_joint" type="fixed">
3    <origin rpy="0 0 0" xyz="0.0 0.0 .24"/>
4    <parent link="onrobot_rg6_base_link"/>
5    <child link="gripper_center"/>
6  </joint>
```

You observe in the video that the Z axis of the target lies along the center of the gripper and that the Y axis of the target is aligned with the gripper plane.

This video uses three of the provided config files:

```python
./robot_description.yaml
./cobotta_pro_900_gripper_frame.urdf
./rmpflow_configs/cobotta_rmpflow_config_basic.yaml
```

### Modifying RMPflow Parameters

There is one remaining piece of the RMPflow config files left to modify, the RMPflow parameters in `rmpflow_config.yaml`.
Typically not much modification of the parameters from the template is needed. RMPflow terms work well for robots with similar scales.
The template RMPflow config was tuned based on the **Franka Emika Panda** robot.

There is one RMPflow parameter that is robot-specific, `joint_velocity_cap_rmp`. This term sets a limit on the maximum velocity that is allowed by RMPflow for any joint in the specified configuration space.
Investigating the URDF, you observe that each joint in the **Cobotta Pro 900** has a velocity limit of `1 rad/s`.

```python
1<joint name="joint_6" type="revolute">
2    <parent link="J5"/>
3    <child link="J6"/>
4    <origin rpy="0.000000 0.000000 0.000000" xyz="0.000000 0.120000 0.160000"/>
5    <axis xyz="-0.000000 -0.000000 1.000000"/>
6    <limit effort="1" lower="-6.28318530717959" upper="6.28318530717959" velocity="1"/>
7    <dynamics damping="0" friction="0"/>
8  </joint>
```

To make sure that RMPflow respects these joint velocity limits, you can modify template parameters so that RMPflow will start damping the velocity of a joint when it comes within `.3 rad/s` of the `1 rad/sec` limit:

```python
1joint_velocity_cap_rmp:
2    max_velocity: 1.
3    velocity_damping_region: .3
4    damping_gain: 1000.0
5    metric_weight: 100.
```

Note

The PD gains from the provided Cobotta Pro 900 USD file are based off the PD gains that you chose for the Franka Emika Panda of P=10000 N\*m and D=1000 N\*m\*s. These values produced oscillations in the Cobotta Pro 900 when you reduced the `max_velocity joint_velocity_cap_rmp` term to `1 rad/sec`. The USD provided for the Cobotta robot in this tutorial has a proportional gain of 10000 N\*m damping gain of 10000 N\*m\*s.

Refer to [RMPflow Tuning Guide](concepts/rmpflow_tuning_guide.html#isaac-sim-motion-generation-rmpflow-tuning-guide) for more details about the meaning of each RMPflow parameter with and a description of how to improve RMPflow parameters for new robots.

## Summary

This tutorial builds on the Lula Robot Description Editor tutorial to complete the process of configuring RMPflow on a new robot. In it, you:

> 1. Modify a template rmpflow\_config.yaml file to fit a specific robot.
> 2. Tune self-collision avoidance behavior.
> 3. Create a new end effector frame that can be used by RMPflow.

### Further Learning

To understand the motivation behind the structure and usage of RmpFlow in NVIDIA Isaac Sim, reference the [Motion Generation](concepts/index.html#isaac-sim-motion-generation) page.

On this page

* [Getting Started](#getting-started)
* [Using the Lula Test Widget](#using-the-lula-test-widget)
* [Template RmpFlow Config File](#template-rmpflow-config-file)
  + [Template RmpFlow Config YAML File](#template-rmpflow-config-yaml-file)
* [Modifying the Template for the Cobotta Pro 900](#modifying-the-template-for-the-cobotta-pro-900)
  + [Doing the Bare Minimum](#doing-the-bare-minimum)
  + [Avoiding Self-Collision: Configuring Body Cylinders and Body Collision Controllers](#avoiding-self-collision-configuring-body-cylinders-and-body-collision-controllers)
  + [Creating an End Effector Frame](#creating-an-end-effector-frame)
  + [Modifying RMPflow Parameters](#modifying-rmpflow-parameters)
* [Summary](#summary)
  + [Further Learning](#further-learning)

---

### cuRobo

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/manipulators/manipulators_curobo.html

* [Robot Simulation](../robot_simulation/index.html)
* [Motion Generation (Deprecated)](motion_generation_overview.html)
* cuRobo and cuMotion

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# cuRobo and cuMotion

Note

The cuRobo and cuMotion tutorials here are no longer maintained. The [cuMotion integration](../cumotion/index.html#isaac-sim-cumotion)
contains much of the same functionality.

Note

This cuRobo tutorial is not supported on aarch64 platforms.

## Learning Objectives

[cuRobo](https://curobo.org) (also on [GitHub](https://github.com/NVlabs/curobo)) is a high-performance,
GPU-accelerated robotics motion generation library for robot manipulators, developed by NVIDIA Research.
It is a standalone Python library that interfaces directly with NVIDIA Isaac Sim, simplifying both testing in simulation
and deploying on physical robots.

[NVIDIA cuMotion](https://nvidia-isaac-ros.github.io/concepts/manipulation/index.html#nvidia-cumotion),
available as a Developer Preview in Isaac 3.0, is a production motion generation package for
manipulators. The current version leverages cuRobo as its backend, providing collision-free motion planning using a
plugin for [MoveIt 2](https://moveit.picknik.ai) and a set of supporting ROS 2 packages. For an example of using
cuMotion with NVIDIA Isaac Sim using the ROS 2 bridge, see the relevant
[section](https://nvidia-isaac-ros.github.io/concepts/manipulation/cumotion_moveit/tutorial_isaac_sim.html)
of the Isaac ROS documentation. This example is somewhat limited in Isaac 3.0 but will be expanded in a future
release.

In the remainder of this tutorial, we focus on direct integration of cuRobo into NVIDIA Isaac Sim, covering cuRobo
installation and use, with examples for collision-free inverse kinematics, motion planning, and reactive
control (MPPI).

## Getting Started

**Prerequisites**

* Complete the [Adding a Manipulator Robot](../core_api_tutorials/tutorial_core_adding_manipulator.html#isaac-sim-app-tutorial-core-adding-manipulator) tutorial prior to beginning this tutorial.

## Installation

Follow the [cuRobo installation instructions](https://curobo.org/get_started/1_install_instructions.html) for
installing cuRobo and required libraries. cuRobo supports NVIDIA Isaac Sim 2022.2.1 and later. Follow the
[workstation installation instructions](../installation/install_workstation.html#isaac-sim-app-install-workstation) to install NVIDIA Isaac Sim.

## Examples

### Using Isaac Sim with cuRobo

In the cuRobo documentation, refer to the
[“Using Isaac Sim” section](https://curobo.org/get_started/2b_isaacsim_examples.html) for an overview of how cuRobo
is interfaced to Isaac Sim, along with a series of standalone examples demonstrating collision checking, motion
generation, inverse kinematics, model-predictive control, and multi-arm reaching.

### Using Isaac Sim with cuRobo and nvblox

In the cuRobo documentation, refer to the
[“Using with Depth Camera” section](https://curobo.org/get_started/2d_nvblox_demo.html) for examples of
obstacle-aware motion generation in NVIDIA Isaac Sim, both with pre-generated signed distance fields (SDFs)
from [nvblox](https://github.com/nvidia-isaac/nvblox) and with online mapping leveraging nvblox with a
physical RealSense depth camera.

On this page

* [Learning Objectives](#learning-objectives)
* [Getting Started](#getting-started)
* [Installation](#installation)
* [Examples](#examples)
  + [Using Isaac Sim with cuRobo](#using-isaac-sim-with-curobo)
  + [Using Isaac Sim with cuRobo and nvblox](#using-isaac-sim-with-curobo-and-nvblox)

---

### Lula Kinematics

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/manipulators/manipulators_lula_kinematics.html

* [Robot Simulation](../robot_simulation/index.html)
* [Motion Generation (Deprecated)](motion_generation_overview.html)
* Lula Kinematics Solver

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Lula Kinematics Solver

Deprecated

For new development, consider using the newer [Robot Motion (Experimental)](../robot_motion_experimental/index.html) API, which provides improved interfaces and additional features over Lula.

This tutorial shows how the [Lula Kinematics Solver](concepts/kinematics_solver.html#isaac-sim-lula-kinematics-solver) class is used to compute forward and inverse kinematics on a robot in NVIDIA Isaac Sim.

## Getting Started

**Prerequisites**

* Complete the [Adding a Manipulator Robot](../core_api_tutorials/tutorial_core_adding_manipulator.html#isaac-sim-app-tutorial-core-adding-manipulator) tutorial prior to beginning this tutorial.
* You can reference the [Lula Robot Description and XRDF Editor](manipulators_robot_description_editor.html#isaac-sim-app-tutorial-motion-generation-robot-description-editor) to understand how to generate your own robot\_description.yaml file to be able to use `LulaKinematicsSolver` on unsupported robots.
* Review the [Loaded Scenario Extension Template](../utilities/extension_templates_tutorial.html#isaac-sim-app-tutorial-extension-templates-loaded-scenario) to understand how this tutorial is structured and run.

To follow along with the tutorial, run your Isaac Sim 6.0 instance. Then open **Window > Extensions**, search for **Motion Generation Examples** (`isaacsim.robot_motion.motion_generation.examples`), and enable it. If you cannot find it, remove `@feature` from the Extensions search bar and search again.
Within the isaacsim.robot\_motion.motion\_generation.examples extension, there is a fully functional example using a `LulaKinematicsSolver` to track a task-space target.
The sections of this tutorial build up the file `scenario.py` from basic functionality to the completed code.

Note

**Motion Generation Examples** (`isaacsim.robot_motion.motion_generation.examples`) are deprecated **since Isaac Sim 6.0.0**. In the Isaac Sim source repository they live under `source/deprecated/isaacsim.robot_motion.motion_generation.examples`; the extension id is unchanged.

**Replacement:** Use the `isaacsim.robot_motion.cumotion.examples` extension and the [cuMotion Integration](../cumotion/index.html) tutorials.

## Using the LulaKinematicsSolver to Compute Forward and Inverse Kinematics

The [Lula Kinematics Solver](concepts/kinematics_solver.html#isaac-sim-lula-kinematics-solver) is able to calculate forward and inverse kinematics for a robot that is defined
by two configuration files (see [Lula Kinematics Solver Configuration](concepts/kinematics_solver.html#isaac-sim-lula-kinematics-solver-configuration)). The `LulaKinematicsSolver` can be paired with
an [Articulation Kinematics Solver](concepts/kinematics_solver.html#isaac-sim-articulation-kinematics-solver) to compute kinematics in a way that can be directly applied to the robot `Articulation`.

The file `/Lula_Kinematics_python/scenario.py` uses the `LulaKinematicsSolver` to generate inverse kinematic solutions to move the robot to a target.

```python
import os

import carb
import numpy as np
from isaacsim.core.prims import SingleArticulation as Articulation
from isaacsim.core.prims import SingleXFormPrim as XFormPrim
from isaacsim.core.utils.extensions import get_extension_path_from_name
from isaacsim.core.utils.numpy.rotations import euler_angles_to_quats
from isaacsim.core.utils.stage import add_reference_to_stage
from isaacsim.robot_motion.motion_generation import (
    ArticulationKinematicsSolver,
    LulaKinematicsSolver,
    interface_config_loader,
)
from isaacsim.storage.native import get_assets_root_path

class FrankaKinematicsExample:
    def __init__(self):
        self._kinematics_solver = None
        self._articulation_kinematics_solver = None

        self._articulation = None
        self._target = None

    def load_example_assets(self):
        # Add the Franka and target to the stage

        robot_prim_path = "/panda"
        path_to_robot_usd = get_assets_root_path() + "/Isaac/Robots/FrankaRobotics/FrankaPanda/franka.usd"

        add_reference_to_stage(path_to_robot_usd, robot_prim_path)
        self._articulation = Articulation(robot_prim_path)

        add_reference_to_stage(get_assets_root_path() + "/Isaac/Props/UIElements/frame_prim.usd", "/World/target")
        self._target = XFormPrim("/World/target", scale=[0.04, 0.04, 0.04])
        self._target.set_default_state(np.array([0.3, 0, 0.5]), euler_angles_to_quats([0, np.pi, 0]))

        # Return assets that were added to the stage so that they can be registered with the core.World
        return self._articulation, self._target

    def setup(self):
        # Load a URDF and Lula Robot Description File for this robot:
        mg_extension_path = get_extension_path_from_name("isaacsim.robot_motion.motion_generation")
        kinematics_config_dir = os.path.join(mg_extension_path, "motion_policy_configs")

        self._kinematics_solver = LulaKinematicsSolver(
            robot_description_path=kinematics_config_dir + "/franka/rmpflow/robot_descriptor.yaml",
            urdf_path=kinematics_config_dir + "/franka/lula_franka_gen.urdf",
        )

        # Kinematics for supported robots can be loaded with a simpler equivalent
        # print("Supported Robots with a Lula Kinematics Config:", interface_config_loader.get_supported_robots_with_lula_kinematics())
        # kinematics_config = interface_config_loader.load_supported_lula_kinematics_solver_config("Franka")
        # self._kinematics_solver = LulaKinematicsSolver(**kinematics_config)

        print("Valid frame names at which to compute kinematics:", self._kinematics_solver.get_all_frame_names())

        end_effector_name = "right_gripper"
        self._articulation_kinematics_solver = ArticulationKinematicsSolver(
            self._articulation, self._kinematics_solver, end_effector_name
        )

    def update(self, step: float):
        target_position, target_orientation = self._target.get_world_pose()

        # Track any movements of the robot base
        robot_base_translation, robot_base_orientation = self._articulation.get_world_pose()
        self._kinematics_solver.set_robot_base_pose(robot_base_translation, robot_base_orientation)

        action, success = self._articulation_kinematics_solver.compute_inverse_kinematics(
            target_position, target_orientation
        )

        if success:
            self._articulation.apply_action(action)
        else:
            carb.log_warn("IK did not converge to a solution.  No action is being taken")

        # Unused Forward Kinematics:
        # ee_position,ee_rot_mat = articulation_kinematics_solver.compute_end_effector_pose()

    def reset(self):
        # Kinematics is stateless
        pass
```

The `LulaKinematicsSolver` is instantiated on lines 41-47 using file paths to the appropriate configuration files. The
`LulaKinematicsSolver` uses the same robot description files as the Lula-based [RMPflow](concepts/rmpflow.html#isaac-sim-motion-generation-rmpflow) [Motion Policy Algorithm](concepts/motion_policy.html#isaac-sim-motion-policy).
The `LulaKinematicsSolver` can solve forward and inverse kinematics at any frame that exists in the robot URDF file.
On line 54, the complete list of recognized frames in the Franka robot is printed:

```python
Valid frame names at which to compute kinematics:
['base_link', 'panda_link0', 'panda_link1', 'panda_link2', 'panda_link3', 'panda_link4', 'panda_forearm_end_pt', 'panda_forearm_mid_pt',
 'panda_forearm_mid_pt_shifted', 'panda_link5', 'panda_forearm_distal', 'panda_link6', 'panda_link7', 'panda_link8', 'panda_hand',
 'camera_bottom_screw_frame', 'camera_link', 'camera_depth_frame', 'camera_color_frame', 'camera_color_optical_frame', 'camera_depth_optical_frame',
 'camera_left_ir_frame', 'camera_left_ir_optical_frame', 'camera_right_ir_frame', 'camera_right_ir_optical_frame', 'panda_face_back_left',
 'panda_face_back_right', 'panda_face_left', 'panda_face_right', 'panda_leftfinger', 'panda_leftfingertip', 'panda_rightfinger', 'panda_rightfingertip', 'right_gripper', 'panda_wrist_end_pt']
```

Supported robots can be loaded directly by name as on lines 50-52. This is equivalent to lines 41-47.

On line 57, an [Articulation Kinematics Solver](concepts/kinematics_solver.html#isaac-sim-articulation-kinematics-solver) is instantiated with the Franka robot `Articulation`, the `LulaKinematicsSolver` instance,
and the end effector name. The `ArticulationKinematicsSolver` class allows you to
compute the end effector position and orientation for the robot `Articulation` in a single line (line 75).

The `ArticulationKinematicsSolver` also allows you to compute inverse kinematics.
The current position of the robot `Articulation` is used as a warm start in the IK calculation,
and the result is returned as an `ArticulationAction` that can be consumed by the robot `Articulation`
to move the specified end effector frame to a target position (lines 67 and 70).

The `LulaKinematicsSolver` returns a flag marking the success or failure of the inverse kinematics computation. On line
67, the script applies the inverse kinematics solution to the robot `Articulation` only if the kinematics converged
successfully to a solution, otherwise no new action is sent to the robot,
and a warning is thrown. The `LulaKinematicsSolver` exposes
settings that allow you to specify how quickly it terminates its search. These settings are outside the
scope of this tutorial.

The `LulaKinematicsSolver` assumes that the robot base is positioned at the origin unless another location is specified. On lines 64-65,
the `LulaKinematicsSolver` is given the current position of the robot base on every frame. This allows the forward
and inverse kinematics to operate using world coordinates. For example, the position of the target is queried in world
coordinates and passed to the `LulaKinematicsSolver`, which internally performs the necessary transformation to compute
accurate inverse kinematics.

The `LulaKinematicsSolver` can be used on its own to compute forward kinematics at any position and to compute
inverse kinematics with any warm start. A robot `Articulation` does not need to be present on the USD stage. See [Kinematics Solvers](concepts/kinematics_solver.html#isaac-sim-kinematics-solver) for more details.

Additionally, sending an inverse kinematic solution directly to the robot is not likely to be useful beyond demonstrations.
In a realistic scenario, you need to determine not only the end position of the robot, but also the path to get there. An IK solver on its own can make
for only a rudimentary trajectory through space that is not likely to be optimal.

## Summary

This tutorial reviews how to load the `LulaKinematicsSolver` class and use it alongside the `ArticulationKinematicsSolver`
helper class to compute forward and inverse kinematics at any frame specified in the robot URDF file.

### Further Learning

To understand the motivation behind the structure and usage of `LulaKinematicsSolver` in NVIDIA Isaac Sim, reference the [Motion Generation](concepts/index.html#isaac-sim-motion-generation)
page.

On this page

* [Getting Started](#getting-started)
* [Using the LulaKinematicsSolver to Compute Forward and Inverse Kinematics](#using-the-lulakinematicssolver-to-compute-forward-and-inverse-kinematics)
* [Summary](#summary)
  + [Further Learning](#further-learning)

---

### Lula RRT Tutorial

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/manipulators/manipulators_lula_rrt.html

* [Robot Simulation](../robot_simulation/index.html)
* [Motion Generation (Deprecated)](motion_generation_overview.html)
* Lula RRT

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Lula RRT

Deprecated

For new development, consider using the newer [Robot Motion (Experimental)](../robot_motion_experimental/index.html) API, which provides improved interfaces and additional features over Lula.

This tutorial shows how the [Lula RRT](concepts/lula_rrt.html#isaac-sim-motion-generation-rrt) class in the [Motion Generation](concepts/index.html#isaac-sim-motion-generation) extension can be used to
produce a collision free path from a starting configuration space (c-space) position to a c-space or task-space target.

## Getting Started

**Prerequisites**

* Complete the [Adding a Manipulator Robot](../core_api_tutorials/tutorial_core_adding_manipulator.html#isaac-sim-app-tutorial-core-adding-manipulator) tutorial prior to beginning this tutorial.
* You can reference the Lula Robot Description Editor to understand how to generate your own robot\_description.yaml file to be able to use RRT on unsupported robots.
* Review the [Loaded Scenario Extension Template](../utilities/extension_templates_tutorial.html#isaac-sim-app-tutorial-extension-templates-loaded-scenario) to understand how this tutorial is structured and run.

To follow along with the tutorial, run your Isaac Sim 6.0 instance. Then open **Window > Extensions**, search for **Motion Generation Examples** (`isaacsim.robot_motion.motion_generation.examples`), and enable it. If you cannot find it, remove `@feature` from the Extensions search bar and search again.
Within the isaacsim.robot\_motion.motion\_generation.examples extension, there is a fully functional example of RRT being used to plan to a task-space target.
The sections of this tutorial build up the file `scenario.py` from basic functionality to the completed code.

Note

**Motion Generation Examples** (`isaacsim.robot_motion.motion_generation.examples`) are deprecated **since Isaac Sim 6.0.0**. In the Isaac Sim source repository they live under `source/deprecated/isaacsim.robot_motion.motion_generation.examples`; the extension id is unchanged.

**Replacement:** Use the `isaacsim.robot_motion.cumotion.examples` extension and the [cuMotion Integration](../cumotion/index.html) tutorials.

## Generating a Path Using an RRT Instance

### Required Configuration Files

[Lula RRT](concepts/lula_rrt.html#isaac-sim-motion-generation-rrt) requires three configuration files to identify a specific robot in
[Lula RRT Configuration](concepts/lula_rrt.html#isaac-sim-motion-generation-rrt-configuration). Paths to these configuration files are used to initialize the `RRT`
class along with an end effector name matching a frame in the robot URDF.

One of the required files contains parameters for the RRT algorithm specifically, and is not shared with any other Lula algorithms.
This tutorial loads the following RRT config file for the Franka robot:

```python
 1seed: 123456
 2step_size: 0.05
 3max_iterations: 50000
 4max_sampling: 10000
 5distance_metric_weights: [3.0, 2.0, 2.0, 1.5, 1.5, 1.0, 1.0]
 6task_space_frame_name: "panda_rightfingertip"
 7task_space_limits: [[0.0, 0.7], [-0.6, 0.6], [0.0, 0.8]]
 8cuda_tree_params:
 9    max_num_nodes: 10000
10    max_buffer_size: 30
11    num_nodes_cpu_gpu_crossover: 3000
12c_space_planning_params:
13    exploration_fraction: 0.5
14task_space_planning_params:
15    translation_target_zone_tolerance: 0.05
16    orientation_target_zone_tolerance: 0.09
17    translation_target_final_tolerance: 1e-4
18    orientation_target_final_tolerance: 0.005
19    translation_gradient_weight: 1.0
20    orientation_gradient_weight: 0.125
21    nn_translation_distance_weight: 1.0
22    nn_orientation_distance_weight: 0.125
23    task_space_exploitation_fraction: 0.4
24    task_space_exploration_fraction: 0.1
25    max_extension_substeps_away_from_target: 6
26    max_extension_substeps_near_target: 50
27    extension_substep_target_region_scale_factor: 2.0
28    unexploited_nodes_culling_scalar: 1.0
29    gradient_substep_size: 0.025
```

You can reference the `docstring` to the function `RRT.set_param()` in our [API Documentation](../py/source/deprecated/isaacsim.robot_motion.motion_generation/docs/index.html) for a description of each parameter.

### RRT Example

The file `/RRT_Example_python/scenario.py` loads the Franka robot and uses `RRT` to move it around obstacles to a target.
Every 60 frames, the planner replans to move to the current target position (if possible). In this example, the planner does
not attempt to plan to the same target multiple times if a failure is encountered. The returned plan will be `None` and no actions will be taken.

Initialize RRT:

```python
 1        # Lula config files for supported robots are stored in the motion_generation extension under
 2        # "/path_planner_configs" and "/motion_policy_configs"
 3        mg_extension_path = get_extension_path_from_name("isaacsim.robot_motion.motion_generation")
 4        rmp_config_dir = os.path.join(mg_extension_path, "motion_policy_configs")
 5        rrt_config_dir = os.path.join(mg_extension_path, "path_planner_configs")
 6
 7        # Initialize an RRT object
 8        self._rrt = RRT(
 9            robot_description_path=rmp_config_dir + "/franka/rmpflow/robot_descriptor.yaml",
10            urdf_path=rmp_config_dir + "/franka/lula_franka_gen.urdf",
11            rrt_config_path=rrt_config_dir + "/franka/rrt/franka_planner_config.yaml",
12            end_effector_frame_name="right_gripper",
13        )
```

For supported robots, this can be simplified:

```python
1        # RRT for supported robots can also be loaded with a simpler equivalent:
2        # rrt_config = interface_config_loader.load_supported_path_planner_config("Franka", "RRT")
3        # self._rrt = RRT(**rrt_confg)
```

To make `RRT` aware of the obstacle it needs to watch the obstacles:

```python
1        self._rrt.add_obstacle(self._obstacle)
```

Any time `RRT.update_world()` is called, it will query the current position
of watched obstacles.

`RRT` outputs sparse plans that, when linearly interpolated, form a collision-free path to the goal position.
As an instance of the `PathPlanner` interface, `RRT` can be passed to a [Path Planner Visualizer](concepts/path_planner.html#isaac-sim-path-planner-visualizer) to convert its output
to a form that is directly usable by the robot `Articulation`:

```python
1        # Use the PathPlannerVisualizer wrapper to generate a trajectory of ArticulationActions
2        self._path_planner_visualizer = PathPlannerVisualizer(self._articulation, self._rrt)
```

Complete code:

```python
  1import os
  2
  3import numpy as np
  4from isaacsim.core.api.objects.cuboid import VisualCuboid
  5from isaacsim.core.prims import SingleArticulation as Articulation
  6from isaacsim.core.prims import SingleXFormPrim as XFormPrim
  7from isaacsim.core.utils.distance_metrics import rotational_distance_angle
  8from isaacsim.core.utils.extensions import get_extension_path_from_name
  9from isaacsim.core.utils.numpy.rotations import euler_angles_to_quats, quats_to_rot_matrices
 10from isaacsim.core.utils.stage import add_reference_to_stage
 11from isaacsim.robot_motion.motion_generation import PathPlannerVisualizer, interface_config_loader
 12from isaacsim.robot_motion.motion_generation.lula import RRT
 13from isaacsim.storage.native import get_assets_root_path
 14
 15
 16class FrankaRrtExample:
 17    def __init__(self):
 18        self._rrt = None
 19        self._path_planner_visualizer = None
 20        self._plan = []
 21
 22        self._articulation = None
 23        self._target = None
 24        self._target_position = None
 25
 26        self._frame_counter = 0
 27
 28    def load_example_assets(self):
 29        # Add the Franka and target to the stage
 30        # The position in which things are loaded is also the position in which they
 31
 32        robot_prim_path = "/panda"
 33        path_to_robot_usd = get_assets_root_path() + "/Isaac/Robots/FrankaRobotics/FrankaPanda/franka.usd"
 34
 35        add_reference_to_stage(path_to_robot_usd, robot_prim_path)
 36        self._articulation = Articulation(robot_prim_path)
 37
 38        add_reference_to_stage(get_assets_root_path() + "/Isaac/Props/UIElements/frame_prim.usd", "/World/target")
 39        self._target = XFormPrim("/World/target", scale=[0.04, 0.04, 0.04])
 40        self._target.set_default_state(np.array([0.45, 0.5, 0.7]), euler_angles_to_quats([3 * np.pi / 4, 0, np.pi]))
 41
 42        self._obstacle = VisualCuboid(
 43            "/World/Wall", position=np.array([0.3, 0.6, 0.6]), size=1.0, scale=np.array([0.1, 0.4, 0.4])
 44        )
 45
 46        # Return assets that were added to the stage so that they can be registered with the core.World
 47        return self._articulation, self._target
 48
 49    def setup(self):
 50        # -- Begin initializing RRT -- #
 51        # Lula config files for supported robots are stored in the motion_generation extension under
 52        # "/path_planner_configs" and "/motion_policy_configs"
 53        mg_extension_path = get_extension_path_from_name("isaacsim.robot_motion.motion_generation")
 54        rmp_config_dir = os.path.join(mg_extension_path, "motion_policy_configs")
 55        rrt_config_dir = os.path.join(mg_extension_path, "path_planner_configs")
 56
 57        # Initialize an RRT object
 58        self._rrt = RRT(
 59            robot_description_path=rmp_config_dir + "/franka/rmpflow/robot_descriptor.yaml",
 60            urdf_path=rmp_config_dir + "/franka/lula_franka_gen.urdf",
 61            rrt_config_path=rrt_config_dir + "/franka/rrt/franka_planner_config.yaml",
 62            end_effector_frame_name="right_gripper",
 63        )
 64        # -- End of initializing RRT -- #
 65
 66        # -- Begin simplified initialization of RRT -- #
 67        # RRT for supported robots can also be loaded with a simpler equivalent:
 68        # rrt_config = interface_config_loader.load_supported_path_planner_config("Franka", "RRT")
 69        # self._rrt = RRT(**rrt_confg)
 70        # -- End of simplified initialization of RRT -- #
 71
 72        # -- Begin adding obstacle -- #
 73        self._rrt.add_obstacle(self._obstacle)
 74        # -- End of adding obstacle -- #
 75
 76        # Set the maximum number of iterations of RRT to prevent it from blocking Isaac Sim for
 77        # too long.
 78        self._rrt.set_max_iterations(5000)
 79
 80        # -- Begin setting PathPlannerVisualizer -- #
 81        # Use the PathPlannerVisualizer wrapper to generate a trajectory of ArticulationActions
 82        self._path_planner_visualizer = PathPlannerVisualizer(self._articulation, self._rrt)
 83        # -- End of setting PathPlannerVisualizer -- #
 84
 85        self.reset()
 86
 87    def update(self, step: float):
 88        current_target_translation, current_target_orientation = self._target.get_world_pose()
 89        current_target_rotation = quats_to_rot_matrices(current_target_orientation)
 90
 91        translation_distance = np.linalg.norm(self._target_translation - current_target_translation)
 92        rotation_distance = rotational_distance_angle(current_target_rotation, self._target_rotation)
 93        target_moved = translation_distance > 0.01 or rotation_distance > 0.01
 94
 95        if self._frame_counter % 60 == 0 and target_moved:
 96            # -- Begin computing plan -- #
 97            # Replan every 60 frames if the target has moved
 98            self._rrt.set_end_effector_target(current_target_translation, current_target_orientation)
 99            self._rrt.update_world()
100            self._plan = self._path_planner_visualizer.compute_plan_as_articulation_actions(max_cspace_dist=0.01)
101            # -- End of computing plan -- #
102
103            self._target_translation = current_target_translation
104            self._target_rotation = current_target_rotation
105
106        if self._plan:
107            action = self._plan.pop(0)
108            self._articulation.apply_action(action)
109
110        self._frame_counter += 1
111
112    def reset(self):
113        self._target_translation = np.zeros(3)
114        self._target_rotation = np.eye(3)
115        self._frame_counter = 0
116        self._plan = []
```

In this example, `RRT` replans every second if the target has been moved. The replanning is performed as follows:

```python
1            # Replan every 60 frames if the target has moved
2            self._rrt.set_end_effector_target(current_target_translation, current_target_orientation)
3            self._rrt.update_world()
4            self._plan = self._path_planner_visualizer.compute_plan_as_articulation_actions(max_cspace_dist=0.01)
```

* First, `RRT` is informed of the new target position.
* Then it is told to query the position of watched obstacles.
* Finally, the `path_planner_visualizer` wrapping `RRT` is used to generate a plan in the form of a list of `ArticulationAction`.

The `max_cspace_dist` argument passed to the `path_planner_visualizer` interpolates the sparse output with a maximum l2 norm of `.01`
between any two commanded robot positions. On every frame, one of the actions in the plan is removed from the plan and sent to the
robot.

## Current Limitations

### Following a Plan with Exactness

The `PathPlannerVisualizer` class is called a “Visualizer” because it is only meant to give a visualization of an output plan, but it is not likely to be useful
beyond this. By densely linearly interpolating an `RRT` plan, the resulting trajectory is far from time-optimal or smooth. To follow a plan in a
more theoretically sound way, the output of `RRT` can be combined with the `LulaTrajectoryGenerator`. This is demonstrated in the NVIDIA Isaac Sim Path Planning Example
in the **Robotics Examples** tab. You can activate **Robotics Examples** tab from **Windows** > **Examples** > **Robotics Examples**.

## Summary

This tutorial reviews using the `RRT` class to generate a collision-free path through an environment from a starting position to a task-space target.

### Further Learning

To understand the motivation behind the structure and usage of `RRT` in NVIDIA Isaac Sim, reference the [Motion Generation](concepts/index.html#isaac-sim-motion-generation)
page.

On this page

* [Getting Started](#getting-started)
* [Generating a Path Using an RRT Instance](#generating-a-path-using-an-rrt-instance)
  + [Required Configuration Files](#required-configuration-files)
  + [RRT Example](#rrt-example)
* [Current Limitations](#current-limitations)
  + [Following a Plan with Exactness](#following-a-plan-with-exactness)
* [Summary](#summary)
  + [Further Learning](#further-learning)

---

### Lula Trajectory Generator

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/manipulators/manipulators_lula_trajectory_generator.html

* [Robot Simulation](../robot_simulation/index.html)
* [Motion Generation (Deprecated)](motion_generation_overview.html)
* Lula Trajectory Generator

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Lula Trajectory Generator

Deprecated

For new development, consider using the newer [Robot Motion (Experimental)](../robot_motion_experimental/index.html) API, which provides improved interfaces and additional features over Lula.

This tutorial explores how the [Lula Trajectory Generator](concepts/trajectory_interface.html#isaac-sim-lula-trajectory-generator) in the [Motion Generation](concepts/index.html#isaac-sim-motion-generation) extension can be used to create both task-space and c-space trajectories that can be easily applied to a simulated robot `Articulation`.

## Getting Started

**Prerequisites**

* Complete the [Adding a Manipulator Robot](../core_api_tutorials/tutorial_core_adding_manipulator.html#isaac-sim-app-tutorial-core-adding-manipulator) tutorial prior to beginning this tutorial.
* You can reference the [Lula Robot Description and XRDF Editor](manipulators_robot_description_editor.html#isaac-sim-app-tutorial-motion-generation-robot-description-editor) to understand how to generate your own `robot_description.yaml` file to be able to use the [Lula Trajectory Generator](concepts/trajectory_interface.html#isaac-sim-lula-trajectory-generator) on unsupported robots.
* Review the [Loaded Scenario Extension Template](../utilities/extension_templates_tutorial.html#isaac-sim-app-tutorial-extension-templates-loaded-scenario) to understand how this tutorial is structured and run.

To follow along with the tutorial, run your Isaac Sim 6.0 instance. Then open **Window > Extensions**, search for **Motion Generation Examples** (`isaacsim.robot_motion.motion_generation.examples`), and enable it. If you cannot find it, remove `@feature` from the Extensions search bar and search again.
Within the isaacsim.robot\_motion.motion\_generation.examples extension, there an example of the `LulaTaskSpaceTrajectorygenerator` and `LulaCSpaceTrajectoryGenerator` being used to generate trajectories
connecting specified c-space and task-space points.
The sections of this tutorial build up the file `scenario.py` from basic functionality to the completed code.

Note

**Motion Generation Examples** (`isaacsim.robot_motion.motion_generation.examples`) are deprecated **since Isaac Sim 6.0.0**. In the Isaac Sim source repository they live under `source/deprecated/isaacsim.robot_motion.motion_generation.examples`; the extension id is unchanged.

**Replacement:** Use the `isaacsim.robot_motion.cumotion.examples` extension and the [cuMotion Integration](../cumotion/index.html) tutorials.

## Generating a C-Space Trajectory

The `LulaCSpaceTrajectoryGenerator` class is able to generate a trajectory that connects a provided set of c-space waypoints.
The code snippet below demonstrates how, given appropriate config files,
the `LulaCSpaceTrajectoryGenerator` class can be initialized and used to create a sequence
of `ArticulationAction` that can be set on each frame to produce the desired trajectory.

The code snippet below shows the relevant contents of `/Trajectory_Generator_python/scenario.py` from the provided example.

```python
  1import os
  2
  3import carb
  4import lula
  5import numpy as np
  6from isaacsim.core.api.objects.cuboid import FixedCuboid
  7from isaacsim.core.prims import SingleArticulation as Articulation
  8from isaacsim.core.prims import SingleXFormPrim as XFormPrim
  9from isaacsim.core.utils.extensions import get_extension_path_from_name
 10from isaacsim.core.utils.numpy.rotations import rot_matrices_to_quats
 11from isaacsim.core.utils.prims import delete_prim, get_prim_at_path
 12from isaacsim.core.utils.stage import add_reference_to_stage
 13from isaacsim.robot_motion.motion_generation import (
 14    ArticulationTrajectory,
 15    LulaCSpaceTrajectoryGenerator,
 16    LulaKinematicsSolver,
 17    LulaTaskSpaceTrajectoryGenerator,
 18)
 19from isaacsim.storage.native import get_assets_root_path
 20
 21
 22class UR10TrajectoryGenerationExample:
 23    def __init__(self):
 24        self._c_space_trajectory_generator = None
 25        self._taskspace_trajectory_generator = None
 26        self._kinematics_solver = None
 27
 28        self._action_sequence = []
 29        self._action_sequence_index = 0
 30
 31        self._articulation = None
 32
 33    def load_example_assets(self):
 34        # Add the Franka and target to the stage
 35        # The position in which things are loaded is also the position in which they
 36
 37        robot_prim_path = "/ur10"
 38        path_to_robot_usd = get_assets_root_path() + "/Isaac/Robots/UniversalRobots/ur10/ur10.usd"
 39
 40        add_reference_to_stage(path_to_robot_usd, robot_prim_path)
 41        self._articulation = Articulation(robot_prim_path)
 42
 43        # Return assets that were added to the stage so that they can be registered with the core.World
 44        return [self._articulation]
 45
 46    def setup(self):
 47        # Config files for supported robots are stored in the motion_generation extension under "/motion_policy_configs"
 48        mg_extension_path = get_extension_path_from_name("isaacsim.robot_motion.motion_generation")
 49        rmp_config_dir = os.path.join(mg_extension_path, "motion_policy_configs")
 50
 51        # -- Begin LulaCSpaceTrajectoryGenerator -- #
 52        # Initialize a LulaCSpaceTrajectoryGenerator object
 53        self._c_space_trajectory_generator = LulaCSpaceTrajectoryGenerator(
 54            robot_description_path=rmp_config_dir + "/universal_robots/ur10/rmpflow/ur10_robot_description.yaml",
 55            urdf_path=rmp_config_dir + "/universal_robots/ur10/ur10_robot.urdf",
 56        )
 57        # -- End of LulaCSpaceTrajectoryGenerator -- #
 58
 59        self._taskspace_trajectory_generator = LulaTaskSpaceTrajectoryGenerator(
 60            robot_description_path=rmp_config_dir + "/universal_robots/ur10/rmpflow/ur10_robot_description.yaml",
 61            urdf_path=rmp_config_dir + "/universal_robots/ur10/ur10_robot.urdf",
 62        )
 63
 64        self._kinematics_solver = LulaKinematicsSolver(
 65            robot_description_path=rmp_config_dir + "/universal_robots/ur10/rmpflow/ur10_robot_description.yaml",
 66            urdf_path=rmp_config_dir + "/universal_robots/ur10/ur10_robot.urdf",
 67        )
 68
 69        self._end_effector_name = "ee_link"
 70
 71    def setup_cspace_trajectory(self):
 72        c_space_points = np.array(
 73            [
 74                [
 75                    -0.41,
 76                    0.5,
 77                    -2.36,
 78                    -1.28,
 79                    5.13,
 80                    -4.71,
 81                ],
 82                [
 83                    -1.43,
 84                    1.0,
 85                    -2.58,
 86                    -1.53,
 87                    6.0,
 88                    -4.74,
 89                ],
 90                [
 91                    -2.83,
 92                    0.34,
 93                    -2.11,
 94                    -1.38,
 95                    1.26,
 96                    -4.71,
 97                ],
 98                [
 99                    -0.41,
100                    0.5,
101                    -2.36,
102                    -1.28,
103                    5.13,
104                    -4.71,
105                ],
106            ]
107        )
108
109        # -- Begin time optimal -- #
110        trajectory_time_optimal = self._c_space_trajectory_generator.compute_c_space_trajectory(c_space_points)
111        # -- End of time optimal -- #
112        # -- Begin time stamped -- #
113        timestamps = np.array([0, 5, 10, 13])
114        trajectory_timestamped = self._c_space_trajectory_generator.compute_timestamped_c_space_trajectory(
115            c_space_points, timestamps
116        )
117        # -- End of time stamped -- #
118
119        # -- Begin visualization -- #
120        # Visualize c-space targets in task space
121        for i, point in enumerate(c_space_points):
122            position, rotation = self._kinematics_solver.compute_forward_kinematics(self._end_effector_name, point)
123            add_reference_to_stage(
124                get_assets_root_path() + "/Isaac/Props/UIElements/frame_prim.usd", f"/visualized_frames/target_{i}"
125            )
126            frame = XFormPrim(f"/visualized_frames/target_{i}", scale=[0.04, 0.04, 0.04])
127            frame.set_world_pose(position, rot_matrices_to_quats(rotation))
128        # -- End of visualization -- #
129
130        # -- Begin no trajectory handling -- #
131        if trajectory_time_optimal is None or trajectory_timestamped is None:
132            carb.log_warn("No trajectory could be computed")
133            self._action_sequence = []
134        # -- End of no trajectory handling -- #
135        else:
136            physics_dt = 1 / 60
137            self._action_sequence = []
138
139            # -- Begin trajectory following -- #
140            # Follow both trajectories in a row
141            articulation_trajectory_time_optimal = ArticulationTrajectory(
142                self._articulation, trajectory_time_optimal, physics_dt
143            )
144            self._action_sequence.extend(articulation_trajectory_time_optimal.get_action_sequence())
145
146            articulation_trajectory_timestamped = ArticulationTrajectory(
147                self._articulation, trajectory_timestamped, physics_dt
148            )
149            self._action_sequence.extend(articulation_trajectory_timestamped.get_action_sequence())
150            # -- End of trajectory following -- #
151
152    def update(self, step: float):
153        if len(self._action_sequence) == 0:
154            return
155
156        if self._action_sequence_index >= len(self._action_sequence):
157            self._action_sequence_index += 1
158            self._action_sequence_index %= (
159                len(self._action_sequence) + 10
160            )  # Wait 10 frames before repeating trajectories
161            return
162
163        if self._action_sequence_index == 0:
164            self._teleport_robot_to_position(self._action_sequence[0])
165
166        self._articulation.apply_action(self._action_sequence[self._action_sequence_index])
167
168        self._action_sequence_index += 1
169        self._action_sequence_index %= len(self._action_sequence) + 10  # Wait 10 frames before repeating trajectories
170
171    def reset(self):
172        # Delete any visualized frames
173        if get_prim_at_path("/visualized_frames"):
174            delete_prim("/visualized_frames")
175
176        self._action_sequence = []
177        self._action_sequence_index = 0
178
179    def _teleport_robot_to_position(self, articulation_action):
180        initial_positions = np.zeros(self._articulation.num_dof)
181        initial_positions[articulation_action.joint_indices] = articulation_action.joint_positions
182
183        self._articulation.set_joint_positions(initial_positions)
184        self._articulation.set_joint_velocities(np.zeros_like(initial_positions))
```

The `LulaCSpaceTrajectoryGenerator` class is initialized using a URDF and
[Lula Robot Description File](manipulators_robot_description_editor.html#isaac-sim-app-tutorial-motion-generation-robot-description-editor):

```python
1        # Initialize a LulaCSpaceTrajectoryGenerator object
2        self._c_space_trajectory_generator = LulaCSpaceTrajectoryGenerator(
3            robot_description_path=rmp_config_dir + "/universal_robots/ur10/rmpflow/ur10_robot_description.yaml",
4            urdf_path=rmp_config_dir + "/universal_robots/ur10/ur10_robot.urdf",
5        )
```

The `LulaCSpaceTrajectoryGenerator` takes in a series of waypoints, and it connects them in configuration space using spline-based interpolation.
There are two main objectives that can be fulfilled by the trajectory generator:

* time-optimal
* time-stamped

The provided example shows a trajectory that runs quickly, and then runs slowly.

A time-optimal trajectory is created in the form of a `LulaTrajectory` object, which fulfills the [Trajectory Interface](concepts/trajectory_interface.html#isaac-sim-trajectory):

```python
1        trajectory_time_optimal = self._c_space_trajectory_generator.compute_c_space_trajectory(c_space_points)
```

Next, a time-stamped trajectory is created that will hit the same waypoints at the times `[0,5,10,13]` seconds. Time optimality is
defined as saturating at least one of velocity, acceleration, or jerk limits of the robot throughout a trajectory:

```python
1        timestamps = np.array([0, 5, 10, 13])
2        trajectory_timestamped = self._c_space_trajectory_generator.compute_timestamped_c_space_trajectory(
3            c_space_points, timestamps
4        )
```

These `LulaTrajectory` objects are passed to `ArticulationTrajectory` to generate a sequence of `ArticulationAction` that can be passed directly to the
robot `Articulation`. The function `ArticulationTrajectory.get_action_sequence()` returns a list of `ArticulationAction` that is meant to be consumed at the specified
rate. In this case, the framerate of physics is assumed to be fixed at `1/60` seconds:

```python
 1            # Follow both trajectories in a row
 2            articulation_trajectory_time_optimal = ArticulationTrajectory(
 3                self._articulation, trajectory_time_optimal, physics_dt
 4            )
 5            self._action_sequence.extend(articulation_trajectory_time_optimal.get_action_sequence())
 6
 7            articulation_trajectory_timestamped = ArticulationTrajectory(
 8                self._articulation, trajectory_timestamped, physics_dt
 9            )
10            self._action_sequence.extend(articulation_trajectory_timestamped.get_action_sequence())
```

If no trajectory can be computed that connects the c-space waypoints, the trajectory returned by `LulaCSpaceTrajectoryGenerator.compute_c_space_trajectory`
will be `None`. This can occur when one of the specified c-space waypoints is not reachable or is very close to a joint limit:

```python
1        if trajectory_time_optimal is None or trajectory_timestamped is None:
2            carb.log_warn("No trajectory could be computed")
3            self._action_sequence = []
```

A visualization of the original `c_space_points` is created by converting them to task-space points.
This code is not functional, but it helps to verify that the robot is hitting every target:

```python
1        # Visualize c-space targets in task space
2        for i, point in enumerate(c_space_points):
3            position, rotation = self._kinematics_solver.compute_forward_kinematics(self._end_effector_name, point)
4            add_reference_to_stage(
5                get_assets_root_path() + "/Isaac/Props/UIElements/frame_prim.usd", f"/visualized_frames/target_{i}"
6            )
7            frame = XFormPrim(f"/visualized_frames/target_{i}", scale=[0.04, 0.04, 0.04])
8            frame.set_world_pose(position, rot_matrices_to_quats(rotation))
```

The `update()` function is programmed to play the sequence of `ArticulationActions` in a loop, taking a pause of `10 frames` for dramatic effect between trajectories.

## Generating a Task-Space Trajectory

### Simple Case: Linearly Connecting Waypoints

Generating a task-space trajectory is similar to generating a c-space trajectory.
In the simplest use-case, you can pass in a set of task-space position and quaternion orientation targets,
which will be linearly interpolated in task-space to produce the resulting trajectory.
An example is provided in the code snippet below:

```python
class UR10TrajectoryGenerationExample:
    def __init__(self):
        self._c_space_trajectory_generator = None
        self._taskspace_trajectory_generator = None
        self._kinematics_solver = None

        self._action_sequence = []
        self._action_sequence_index = 0

        self._articulation = None

    def load_example_assets(self):
        # Add the Franka and target to the stage
        # The position in which things are loaded is also the position in which they

        robot_prim_path = "/ur10"
        path_to_robot_usd = get_assets_root_path() + "/Isaac/Robots/UniversalRobots/ur10/ur10.usd"

        add_reference_to_stage(path_to_robot_usd, robot_prim_path)
        self._articulation = Articulation(robot_prim_path)

        # Return assets that were added to the stage so that they can be registered with the core.World
        return [self._articulation]

    def setup(self):
        # Config files for supported robots are stored in the motion_generation extension under "/motion_policy_configs"
        mg_extension_path = get_extension_path_from_name("isaacsim.robot_motion.motion_generation")
        rmp_config_dir = os.path.join(mg_extension_path, "motion_policy_configs")

        # Initialize a LulaCSpaceTrajectoryGenerator object
        self._c_space_trajectory_generator = LulaCSpaceTrajectoryGenerator(
            robot_description_path=rmp_config_dir + "/universal_robots/ur10/rmpflow/ur10_robot_description.yaml",
            urdf_path=rmp_config_dir + "/universal_robots/ur10/ur10_robot.urdf",
        )

        self._taskspace_trajectory_generator = LulaTaskSpaceTrajectoryGenerator(
            robot_description_path=rmp_config_dir + "/universal_robots/ur10/rmpflow/ur10_robot_description.yaml",
            urdf_path=rmp_config_dir + "/universal_robots/ur10/ur10_robot.urdf",
        )

        self._kinematics_solver = LulaKinematicsSolver(
            robot_description_path=rmp_config_dir + "/universal_robots/ur10/rmpflow/ur10_robot_description.yaml",
            urdf_path=rmp_config_dir + "/universal_robots/ur10/ur10_robot.urdf",
        )

        self._end_effector_name = "ee_link"

    def setup_taskspace_trajectory(self):
        task_space_position_targets = np.array(
            [[0.3, -0.3, 0.1], [0.3, 0.3, 0.1], [0.3, 0.3, 0.5], [0.3, -0.3, 0.5], [0.3, -0.3, 0.1]]
        )

        task_space_orientation_targets = np.tile(np.array([0, 1, 0, 0]), (5, 1))

        trajectory = self._taskspace_trajectory_generator.compute_task_space_trajectory_from_points(
            task_space_position_targets, task_space_orientation_targets, self._end_effector_name
        )

        # Visualize task-space targets in task space
        for i, (position, orientation) in enumerate(zip(task_space_position_targets, task_space_orientation_targets)):
            add_reference_to_stage(
                get_assets_root_path() + "/Isaac/Props/UIElements/frame_prim.usd", f"/visualized_frames/target_{i}"
            )
            frame = XFormPrim(f"/visualized_frames/target_{i}", scale=[0.04, 0.04, 0.04])
            frame.set_world_pose(position, orientation)

        if trajectory is None:
            carb.log_warn("No trajectory could be computed")
            self._action_sequence = []
        else:
            physics_dt = 1 / 60
            articulation_trajectory = ArticulationTrajectory(self._articulation, trajectory, physics_dt)

            # Get a sequence of ArticulationActions that are intended to be passed to the robot at 1/60 second intervals
            self._action_sequence = articulation_trajectory.get_action_sequence()

    def update(self, step: float):
        if len(self._action_sequence) == 0:
            return

        if self._action_sequence_index >= len(self._action_sequence):
            self._action_sequence_index += 1
            self._action_sequence_index %= (
                len(self._action_sequence) + 10
            )  # Wait 10 frames before repeating trajectories
            return

        if self._action_sequence_index == 0:
            self._teleport_robot_to_position(self._action_sequence[0])

        self._articulation.apply_action(self._action_sequence[self._action_sequence_index])

        self._action_sequence_index += 1
        self._action_sequence_index %= len(self._action_sequence) + 10  # Wait 10 frames before repeating trajectories

    def reset(self):
        # Delete any visualized frames
        if get_prim_at_path("/visualized_frames"):
            delete_prim("/visualized_frames")

        self._action_sequence = []
        self._action_sequence_index = 0

    def _teleport_robot_to_position(self, articulation_action):
        initial_positions = np.zeros(self._articulation.num_dof)
        initial_positions[articulation_action.joint_indices] = articulation_action.joint_positions

        self._articulation.set_joint_positions(initial_positions)
        self._articulation.set_joint_velocities(np.zeros_like(initial_positions))
```

In moving to the task-space trajectory generator, there are few code changes required. The initialization is nearly the same on line 36 as for the
c-space trajectory generator. The main changes are on lines 59-61 where a task-space trajectory is specified. When using the function
`LulaTaskSpaceTrajectoryGenerator.compute_task_space_trajectory_from_points`, a position and orientation target must be specified for each task-space waypoint.
Additionally, a frame from the robot URDF must be specified as the end effector frame.
If the waypoints cannot be connected to form a trajectory, the `compute_task_space_trajectory_from_points` function will return `None`.
This case is checked on line 69.

### Defining Complicated Trajectories

The `LulaTaskSpaceTrajectoryGenerator` can be used to create paths with more complicated specifications than to connect a set of task-space targets linearly.
Using the class `lula.TaskSpacePathSpec`, you can define paths with arcs and circles with multiple options for orientation targets.
The code snippet below demonstrates creating a `lula.TaskSpacePathSpec` and gives an example of each available function for adding to a task-space path.
Additionally, it shows how a `lula.TaskSpacePathSpec` can be combined with a `lula.CSpacePathSpec` in a `lula.CompositePathSpec` to specify trajectories
that contain both c-space and task-space waypoints.

```python
class UR10TrajectoryGenerationExample:
    def __init__(self):
        self._c_space_trajectory_generator = None
        self._taskspace_trajectory_generator = None
        self._kinematics_solver = None

        self._action_sequence = []
        self._action_sequence_index = 0

        self._articulation = None

    def load_example_assets(self):
        # Add the Franka and target to the stage
        # The position in which things are loaded is also the position in which they

        robot_prim_path = "/ur10"
        path_to_robot_usd = get_assets_root_path() + "/Isaac/Robots/UniversalRobots/ur10/ur10.usd"

        add_reference_to_stage(path_to_robot_usd, robot_prim_path)
        self._articulation = Articulation(robot_prim_path)

        # Return assets that were added to the stage so that they can be registered with the core.World
        return [self._articulation]

    def setup(self):
        # Config files for supported robots are stored in the motion_generation extension under "/motion_policy_configs"
        mg_extension_path = get_extension_path_from_name("isaacsim.robot_motion.motion_generation")
        rmp_config_dir = os.path.join(mg_extension_path, "motion_policy_configs")

        # Initialize a LulaCSpaceTrajectoryGenerator object
        self._c_space_trajectory_generator = LulaCSpaceTrajectoryGenerator(
            robot_description_path=rmp_config_dir + "/universal_robots/ur10/rmpflow/ur10_robot_description.yaml",
            urdf_path=rmp_config_dir + "/universal_robots/ur10/ur10_robot.urdf",
        )

        self._taskspace_trajectory_generator = LulaTaskSpaceTrajectoryGenerator(
            robot_description_path=rmp_config_dir + "/universal_robots/ur10/rmpflow/ur10_robot_description.yaml",
            urdf_path=rmp_config_dir + "/universal_robots/ur10/ur10_robot.urdf",
        )

        self._kinematics_solver = LulaKinematicsSolver(
            robot_description_path=rmp_config_dir + "/universal_robots/ur10/rmpflow/ur10_robot_description.yaml",
            urdf_path=rmp_config_dir + "/universal_robots/ur10/ur10_robot.urdf",
        )

        self._end_effector_name = "ee_link"

    def setup_advanced_trajectory(self):
        # The following code demonstrates how to specify a complicated cspace and taskspace path
        # using the lula.CompositePathSpec object

        initial_c_space_robot_pose = np.array([0, 0, 0, 0, 0, 0])

        # Combine a cspace and taskspace trajectory
        composite_path_spec = lula.create_composite_path_spec(initial_c_space_robot_pose)

        #############################################################################
        # Demonstrate all the available movements in a taskspace path spec:

        # Lula has its own classes for Rotations and 6 DOF poses: Rotation3 and Pose3
        r0 = lula.Rotation3(np.pi / 2, np.array([1.0, 0.0, 0.0]))
        t0 = np.array([0.3, -0.1, 0.3])
        task_space_spec = lula.create_task_space_path_spec(lula.Pose3(r0, t0))

        # Add path linearly interpolating between r0,r1 and t0,t1
        t1 = np.array([0.3, -0.1, 0.5])
        r1 = lula.Rotation3(np.pi / 3, np.array([1, 0, 0]))
        task_space_spec.add_linear_path(lula.Pose3(r1, t1))

        # Add pure translation.  Constant rotation is assumed
        task_space_spec.add_translation(t0)

        # Add pure rotation.
        task_space_spec.add_rotation(r0)

        # Add three-point arc with constant orientation.
        t2 = np.array(
            [
                0.3,
                0.3,
                0.3,
            ]
        )
        midpoint = np.array([0.3, 0, 0.5])
        task_space_spec.add_three_point_arc(t2, midpoint, constant_orientation=True)

        # Add three-point arc with tangent orientation.
        task_space_spec.add_three_point_arc(t0, midpoint, constant_orientation=False)

        # Add three-point arc with orientation target.
        task_space_spec.add_three_point_arc_with_orientation_target(lula.Pose3(r1, t2), midpoint)

        # Add tangent arc with constant orientation. Tangent arcs are circles that connect two points
        task_space_spec.add_tangent_arc(t0, constant_orientation=True)

        # Add tangent arc with tangent orientation.
        task_space_spec.add_tangent_arc(t2, constant_orientation=False)

        # Add tangent arc with orientation target.
        task_space_spec.add_tangent_arc_with_orientation_target(lula.Pose3(r0, t0))

        ###################################################
        # Demonstrate the usage of a c_space path spec:
        c_space_spec = lula.create_c_space_path_spec(np.array([0, 0, 0, 0, 0, 0]))

        c_space_spec.add_c_space_waypoint(np.array([0, 0.5, -2.0, -1.28, 5.13, -4.71]))

        ##############################################################
        # Combine the two path specs together into a composite spec:

        # specify how to connect initial_c_space and task_space points with transition_mode option
        transition_mode = lula.CompositePathSpec.TransitionMode.FREE
        composite_path_spec.add_task_space_path_spec(task_space_spec, transition_mode)

        transition_mode = lula.CompositePathSpec.TransitionMode.FREE
        composite_path_spec.add_c_space_path_spec(c_space_spec, transition_mode)

        # Transition Modes:
        # lula.CompositePathSpec.TransitionMode.LINEAR_TASK_SPACE:
        #      Connect cspace to taskspace points linearly through task space.  This mode is only available when adding a task_space path spec.
        # lula.CompositePathSpec.TransitionMode.FREE:
        #      Put no constraints on how cspace and taskspace points are connected
        # lula.CompositePathSpec.TransitionMode.SKIP:
        #      Skip the first point of the path spec being added, using the last pose instead

        trajectory = self._taskspace_trajectory_generator.compute_task_space_trajectory_from_path_spec(
            composite_path_spec, self._end_effector_name
        )

        if trajectory is None:
            carb.log_warn("No trajectory could be computed")
            self._action_sequence = []
        else:
            physics_dt = 1 / 60
            articulation_trajectory = ArticulationTrajectory(self._articulation, trajectory, physics_dt)

            # Get a sequence of ArticulationActions that are intended to be passed to the robot at 1/60 second intervals
            self._action_sequence = articulation_trajectory.get_action_sequence()

    def update(self, step: float):
        if len(self._action_sequence) == 0:
            return

        if self._action_sequence_index >= len(self._action_sequence):
            self._action_sequence_index += 1
            self._action_sequence_index %= (
                len(self._action_sequence) + 10
            )  # Wait 10 frames before repeating trajectories
            return

        if self._action_sequence_index == 0:
            self._teleport_robot_to_position(self._action_sequence[0])

        self._articulation.apply_action(self._action_sequence[self._action_sequence_index])

        self._action_sequence_index += 1
        self._action_sequence_index %= len(self._action_sequence) + 10  # Wait 10 frames before repeating trajectories

    def reset(self):
        # Delete any visualized frames
        if get_prim_at_path("/visualized_frames"):
            delete_prim("/visualized_frames")

        self._action_sequence = []
        self._action_sequence_index = 0

    def _teleport_robot_to_position(self, articulation_action):
        initial_positions = np.zeros(self._articulation.num_dof)
        initial_positions[articulation_action.joint_indices] = articulation_action.joint_positions

        self._articulation.set_joint_positions(initial_positions)
        self._articulation.set_joint_velocities(np.zeros_like(initial_positions))
```

The code snippet above creates a `lula.CompositePathSpec` on line 55 with an initial c-space position. It is combined with a
`lula.TaskSpacePathSpec` on lines 108-109 and it is combined with a `lula.CSpacePathSpec` on lines 111-112. The resulting path
is one that starts at the specified `initial_c_space_robot_pose`, then follows a series of taskspace targets, then hits two c-space
targets. When combining path specs, a transition mode must be specified to determine how c-space and task-space points should be connected
to each other. Reference lines 114-120 to see the possible options. In this case, no constraint is made on how the `LulaTrajectoryGenerator`
connects these points.

Each available option for specifying a `lula.TaskSpacePathSpec` is demonstrated between lines 63-94.
The code snippet above moves mainly between three translations: `t0, t1, t2` with possible rotations `r0, r1`.
The `lula.TaskSpacePathSpec` object is created with an initial position on line 63.
Each following `add` function that is called adds a path between the last position in the `path_spec` so far and a new position.
The basic possibilities are:

> 1. Linearly interpolate translation to a new point while keeping rotation fixed (line 71)
> 2. Linearly interpolate rotation to a new point while keeping translation fixed (line 74)
> 3. Linearly interpolate both rotation and translation to a new 6 DOF point (line 68)

The `lula.TaskSpacePathSpec` also makes it easy to define various arcs and circular paths that connect points in space.
A three-point arc can be defined that moves through a midpoint to a translation target.
There are three options for the orientation of the robot while moving along the path:

> 1. Keep rotation constant (line 79)
> 2. Always stay oriented tangent to the arc (line 82)
> 3. Linearly interpolate rotation to a rotation target (line 85)

Finally, a circular path can be specified without defining a midpoint as on lines 88, 91, and 94.
The same three options for specifying orientation are available.

## Summary

This tutorial shows how to use the [Lula Trajectory Generator](concepts/trajectory_interface.html#isaac-sim-lula-trajectory-generator) to generate c-space and task-space trajectories for a robot. Task-space trajectories can be specified using a series of task-space waypoints that will be connected linearly, or they can be defined piecewise with many different options for connecting each pair of points in space.

### Further Learning

Reference the [Motion Generation](concepts/index.html#isaac-sim-motion-generation) page for a complete description of trajectories in NVIDIA Isaac Sim.

On this page

* [Getting Started](#getting-started)
* [Generating a C-Space Trajectory](#generating-a-c-space-trajectory)
* [Generating a Task-Space Trajectory](#generating-a-task-space-trajectory)
  + [Simple Case: Linearly Connecting Waypoints](#simple-case-linearly-connecting-waypoints)
  + [Defining Complicated Trajectories](#defining-complicated-trajectories)
* [Summary](#summary)
  + [Further Learning](#further-learning)

---

### RMPflow Tutorial

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/manipulators/manipulators_rmpflow.html

* [Robot Simulation](../robot_simulation/index.html)
* [Motion Generation (Deprecated)](motion_generation_overview.html)
* Lula RMPflow

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Lula RMPflow

Deprecated

For new development, consider using the newer [Robot Motion (Experimental)](../robot_motion_experimental/index.html) API, which provides improved interfaces and additional features over Lula.

This tutorial shows how the [RMPflow](concepts/rmpflow.html#isaac-sim-motion-generation-rmpflow) class in the [Motion Generation](concepts/index.html#isaac-sim-motion-generation) can be used to
generate smooth motions to reach task-space targets while avoiding dynamic obstacles. This tutorial demonstrates how:

* `RmpFlow` can be directly instantiated and used to generate motions using a custom robot description file
* `RmpFlow` can be loaded and used on supported robots
* built-in debugging features can improve easy of use and integration

## Getting Started

**Prerequisites**

* Complete the [Adding a Manipulator Robot](../core_api_tutorials/tutorial_core_adding_manipulator.html#isaac-sim-app-tutorial-core-adding-manipulator) tutorial prior to beginning this tutorial.
* Review the [Loaded Scenario Extension Template](../utilities/extension_templates_tutorial.html#isaac-sim-app-tutorial-extension-templates-loaded-scenario) to understand how this tutorial is structured and run.

To follow along with the tutorial, run your Isaac Sim 6.0 instance. Then open **Window > Extensions**, search for **Motion Generation Examples** (`isaacsim.robot_motion.motion_generation.examples`), and enable it. If you cannot find it, remove `@feature` from the Extensions search bar and search again.
Within the isaacsim.robot\_motion.motion\_generation.examples extension, there is a fully functional example of RMPflow including following a target, world awareness,
and a debugging option. The sections of this tutorial build up the file `scenario.py` from basic functionality to the completed code.

Note

**Motion Generation Examples** (`isaacsim.robot_motion.motion_generation.examples`) are deprecated **since Isaac Sim 6.0.0**. In the Isaac Sim source repository they live under `source/deprecated/isaacsim.robot_motion.motion_generation.examples`; the extension id is unchanged.

**Replacement:** Use the `isaacsim.robot_motion.cumotion.examples` extension and the [cuMotion Integration](../cumotion/index.html) tutorials.

## Generating Motions with an RMPflow Instance

[RMPflow](concepts/rmpflow.html#isaac-sim-motion-generation-rmpflow) is used heavily throughout NVIDIA Isaac Sim for controlling robot manipulators. As documented
in [RMPflow Configuration](concepts/rmpflow.html#isaac-sim-motion-generation-rmpflow-configuration), there are three configuration files needed to directly instantiate the `RmpFlow` class directly.
After these configuration files are loaded and an end effector target has been specified, actions can be computed to move the robot to the desired target.

```python
import os

import numpy as np
from isaacsim.core.api.objects.cuboid import FixedCuboid
from isaacsim.core.prims import SingleArticulation as Articulation
from isaacsim.core.prims import SingleXFormPrim as XFormPrim
from isaacsim.core.utils.extensions import get_extension_path_from_name
from isaacsim.core.utils.numpy.rotations import euler_angles_to_quats
from isaacsim.core.utils.stage import add_reference_to_stage
from isaacsim.robot_motion.motion_generation import ArticulationMotionPolicy, RmpFlow
from isaacsim.storage.native import get_assets_root_path

class FrankaRmpFlowExample:
    def __init__(self):
        self._rmpflow = None
        self._articulation_rmpflow = None

        self._articulation = None
        self._target = None

    def load_example_assets(self):
        # Add the Franka and target to the stage
        # The position in which things are loaded is also the position in which they

        robot_prim_path = "/panda"
        path_to_robot_usd = get_assets_root_path() + "/Isaac/Robots/FrankaRobotics/FrankaPanda/franka.usd"

        add_reference_to_stage(path_to_robot_usd, robot_prim_path)
        self._articulation = Articulation(robot_prim_path)

        add_reference_to_stage(get_assets_root_path() + "/Isaac/Props/UIElements/frame_prim.usd", "/World/target")
        self._target = XFormPrim("/World/target", scale=[0.04, 0.04, 0.04])

        # Return assets that were added to the stage so that they can be registered with the core.World
        return self._articulation, self._target

    def setup(self):
        # RMPflow config files for supported robots are stored in the motion_generation extension under "/motion_policy_configs"
        mg_extension_path = get_extension_path_from_name("isaacsim.robot_motion.motion_generation")
        rmp_config_dir = os.path.join(mg_extension_path, "motion_policy_configs")

        # Initialize an RmpFlow object
        self._rmpflow = RmpFlow(
            robot_description_path=rmp_config_dir + "/franka/rmpflow/robot_descriptor.yaml",
            urdf_path=rmp_config_dir + "/franka/lula_franka_gen.urdf",
            rmpflow_config_path=rmp_config_dir + "/franka/rmpflow/franka_rmpflow_common.yaml",
            end_effector_frame_name="right_gripper",
            maximum_substep_size=0.00334,
        )

        # Use the ArticulationMotionPolicy wrapper object to connect rmpflow to the Franka robot articulation.
        self._articulation_rmpflow = ArticulationMotionPolicy(self._articulation, self._rmpflow)

        self._target.set_world_pose(np.array([0.5, 0, 0.7]), euler_angles_to_quats([0, np.pi, 0]))

    def update(self, step: float):
        # Step is the time elapsed on this frame
        target_position, target_orientation = self._target.get_world_pose()

        self._rmpflow.set_end_effector_target(target_position, target_orientation)

        action = self._articulation_rmpflow.get_next_articulation_action(step)
        self._articulation.apply_action(action)

    def reset(self):
        # Rmpflow is stateless unless it is explicitly told not to be

        self._target.set_world_pose(np.array([0.5, 0, 0.7]), euler_angles_to_quats([0, np.pi, 0]))
```

`RMPflow` is an implementation of the [Motion Policy Algorithm](concepts/motion_policy.html#isaac-sim-motion-policy) interface.
Any MotionPolicy can be passed to an [Articulation Motion Policy](concepts/motion_policy.html#isaac-sim-articulation-motion-policy)
to start moving a robot on the USD stage. On line 43, an instance of `RmpFlow` is instantiated
with the required configuration information. The `ArticulationMotionPolicy` created on line 52 acts as a
translational layer between `RmpFlow` and the simulated Franka robot `Articulation`. You can interact with
`RmpFlow` directly to communicate the world state, set an end effector target, or modify internal settings.
On each frame, an end effector target is passed directly to the `RmpFlow` object (line 60).
The `ArticulationMotionPolicy` is used on line 64 to compute an action that can be directly consumed by the
Franka `Articulation`.

Note

The RMPflow algorithm takes in consideration the robot structure provided by the configuration URDF file. If working on a robot with assembled components (for example, a UR10 with a gripper attached), the URDF file should be updated to reflect the correct robot structure and contain the offset of the gripper at the end effector frame, or additional control joints. The final assembly URDF can be exported with the [USD to URDF Exporter](../importer_exporter/ext_omni_exporter_urdf.html#isaac-sim-app-extension-urdf-exporter). When modifying the source URDF file, it is recommended to review and update the [Robot Description file](manipulators_robot_description_editor.html#isaac-sim-app-tutorial-motion-generation-robot-description-editor) to ensure that the correct supplemental file is being used.

### World State

As a [Motion Policy Algorithm](concepts/motion_policy.html#isaac-sim-motion-policy), `RmpFlow` is capable of dynamic collision avoidance
while navigating the end effector to a target. The world state can be
changing over time while `RmpFlow` is navigating to its target. Objects created with the `isaacsim.core.api.objects` package
(see [Inputs: World State](concepts/motion_policy.html#isaac-sim-motion-policy-world-state)) can be registered with `RmpFlow` and the policy will automatically avoid collisions with these obstacles.
`RmpFlow` is triggered to query the current state of all tracked objects whenever `RmpFlow.update_world()` is called.

`RmpFlow` can also be informed about a change in the robot base pose on a given frame by calling `RmpFlow.set_robot_base_pose()`.
As object positions are queried in world coordinates, it is critical to use this function, if the base of the robot is moved
within the USD stage.

```python
import os

import numpy as np
from isaacsim.core.api.objects.cuboid import FixedCuboid
from isaacsim.core.prims import SingleArticulation as Articulation
from isaacsim.core.prims import SingleXFormPrim as XFormPrim
from isaacsim.core.utils.extensions import get_extension_path_from_name
from isaacsim.core.utils.numpy.rotations import euler_angles_to_quats
from isaacsim.core.utils.stage import add_reference_to_stage
from isaacsim.robot_motion.motion_generation import ArticulationMotionPolicy, RmpFlow
from isaacsim.robot_motion.motion_generation.interface_config_loader import (
    get_supported_robot_policy_pairs,
    load_supported_motion_policy_config,
)
from isaacsim.storage.native import get_assets_root_path

class FrankaRmpFlowExample:
    def __init__(self):
        self._rmpflow = None
        self._articulation_rmpflow = None

        self._articulation = None
        self._target = None

    def load_example_assets(self):
        # Add the Franka and target to the stage
        # The position in which things are loaded is also the position in which they

        robot_prim_path = "/panda"
        path_to_robot_usd = get_assets_root_path() + "/Isaac/Robots/FrankaRobotics/FrankaPanda/franka.usd"

        add_reference_to_stage(path_to_robot_usd, robot_prim_path)
        self._articulation = Articulation(robot_prim_path)

        add_reference_to_stage(get_assets_root_path() + "/Isaac/Props/UIElements/frame_prim.usd", "/World/target")
        self._target = XFormPrim("/World/target", scale=[0.04, 0.04, 0.04])

        self._obstacle = FixedCuboid(
            "/World/obstacle", size=0.05, position=np.array([0.4, 0.0, 0.65]), color=np.array([0.0, 0.0, 1.0])
        )

        # Return assets that were added to the stage so that they can be registered with the core.World
        return self._articulation, self._target, self._obstacle

    def setup(self):
        # RMPflow config files for supported robots are stored in the motion_generation extension under "/motion_policy_configs"
        mg_extension_path = get_extension_path_from_name("isaacsim.robot_motion.motion_generation")
        rmp_config_dir = os.path.join(mg_extension_path, "motion_policy_configs")

        # Initialize an RmpFlow object
        self._rmpflow = RmpFlow(
            robot_description_path=rmp_config_dir + "/franka/rmpflow/robot_descriptor.yaml",
            urdf_path=rmp_config_dir + "/franka/lula_franka_gen.urdf",
            rmpflow_config_path=rmp_config_dir + "/franka/rmpflow/franka_rmpflow_common.yaml",
            end_effector_frame_name="right_gripper",
            maximum_substep_size=0.00334,
        )
        self._rmpflow.add_obstacle(self._obstacle)

        # Use the ArticulationMotionPolicy wrapper object to connect rmpflow to the Franka robot articulation.
        self._articulation_rmpflow = ArticulationMotionPolicy(self._articulation, self._rmpflow)

        self._target.set_world_pose(np.array([0.5, 0, 0.7]), euler_angles_to_quats([0, np.pi, 0]))

    def update(self, step: float):
        # Step is the time elapsed on this frame
        target_position, target_orientation = self._target.get_world_pose()

        self._rmpflow.set_end_effector_target(target_position, target_orientation)

        # Track any movements of the cube obstacle
        self._rmpflow.update_world()

        # Track any movements of the robot base
        robot_base_translation, robot_base_orientation = self._articulation.get_world_pose()
        self._rmpflow.set_robot_base_pose(robot_base_translation, robot_base_orientation)

        action = self._articulation_rmpflow.get_next_articulation_action(step)
        self._articulation.apply_action(action)

    def reset(self):
        # Rmpflow is stateless unless it is explicitly told not to be

        self._target.set_world_pose(np.array([0.5, 0, 0.7]), euler_angles_to_quats([0, np.pi, 0]))
```

On lines 22, an obstacle is added to the stage, and on line 40, it is registered as an obstacle with `RmpFlow`.
On each frame, `RmpFlow.update_world()` is called (line 56). This triggers `RmpFlow` to query the current position of the cube to account for any movement.

On lines 59-60, the current position of the robot base is queried and passed to `RmpFlow`.
This step is separated from other world state because
it is often unnecessary (when the robot base never moves from the origin), or this step might require extra consideration
(for example, `RmpFlow` is controlling an arm that is mounted on a moving base).

## Loading RMPflow for Supported Robots

In the previous sections, observe that `RmpFlow` requires five arguments to be initialized. Three of these arguments are file paths to required configuration files.
The `end_effector_frame_name` argument specifies what frame on the robot (from the frames found in the referenced URDF file) should be considered the end effector.
The `maximum_substep_size` argument specifies a maximum step-size when internally performing the Euler Integration.

For manipulators in the NVIDIA Isaac Sim library, appropriate config information for loading RmpFlow can be found in the `isaacsim.robot_motion.motion_generation` extension.
This information is indexed by robot name and can be accessed simply.
The following change shows how loading configs for supported robots can be simplified.

```python
import os

import numpy as np
from isaacsim.core.api.objects.cuboid import FixedCuboid
from isaacsim.core.prims import SingleArticulation as Articulation
from isaacsim.core.prims import SingleXFormPrim as XFormPrim
from isaacsim.core.utils.extensions import get_extension_path_from_name
from isaacsim.core.utils.numpy.rotations import euler_angles_to_quats
from isaacsim.core.utils.stage import add_reference_to_stage
from isaacsim.robot_motion.motion_generation import ArticulationMotionPolicy, RmpFlow
from isaacsim.robot_motion.motion_generation.interface_config_loader import (
    get_supported_robot_policy_pairs,
    load_supported_motion_policy_config,
)
from isaacsim.storage.native import get_assets_root_path

class FrankaRmpFlowExample:
    def __init__(self):
        self._rmpflow = None
        self._articulation_rmpflow = None

        self._articulation = None
        self._target = None

    def load_example_assets(self):
        # Add the Franka and target to the stage
        # The position in which things are loaded is also the position in which they

        robot_prim_path = "/panda"
        path_to_robot_usd = get_assets_root_path() + "/Isaac/Robots/FrankaRobotics/FrankaPanda/franka.usd"

        add_reference_to_stage(path_to_robot_usd, robot_prim_path)
        self._articulation = Articulation(robot_prim_path)

        add_reference_to_stage(get_assets_root_path() + "/Isaac/Props/UIElements/frame_prim.usd", "/World/target")
        self._target = XFormPrim("/World/target", scale=[0.04, 0.04, 0.04])

        self._obstacle = FixedCuboid(
            "/World/obstacle", size=0.05, position=np.array([0.4, 0.0, 0.65]), color=np.array([0.0, 0.0, 1.0])
        )

        # Return assets that were added to the stage so that they can be registered with the core.World
        return self._articulation, self._target, self._obstacle

    def setup(self):
        # Loading RMPflow can be done quickly for supported robots
        print("Supported Robots with a Provided RMPflow Config:", list(get_supported_robot_policy_pairs().keys()))
        rmp_config = load_supported_motion_policy_config("Franka", "RMPflow")

        # Initialize an RmpFlow object
        self._rmpflow = RmpFlow(**rmp_config)
        self._rmpflow.add_obstacle(self._obstacle)

        # Use the ArticulationMotionPolicy wrapper object to connect rmpflow to the Franka robot articulation.
        self._articulation_rmpflow = ArticulationMotionPolicy(self._articulation, self._rmpflow)

        self._target.set_world_pose(np.array([0.5, 0, 0.7]), euler_angles_to_quats([0, np.pi, 0]))

    def update(self, step: float):
        # Step is the time elapsed on this frame
        target_position, target_orientation = self._target.get_world_pose()

        self._rmpflow.set_end_effector_target(target_position, target_orientation)

        # Track any movements of the cube obstacle
        self._rmpflow.update_world()

        # Track any movements of the robot base
        robot_base_translation, robot_base_orientation = self._articulation.get_world_pose()
        self._rmpflow.set_robot_base_pose(robot_base_translation, robot_base_orientation)

        action = self._articulation_rmpflow.get_next_articulation_action(step)
        self._articulation.apply_action(action)

    def reset(self):
        # Rmpflow is stateless unless it is explicitly told not to be

        self._target.set_world_pose(np.array([0.5, 0, 0.7]), euler_angles_to_quats([0, np.pi, 0]))
```

A supported set of robots can have their RMPflow configs loaded by name.
Line 34 prints the names of every supported robot with a provided RMPflow config (at the time of writing this tutorial):

> [‘Franka’, ‘UR3’, ‘UR3e’, ‘UR5’, ‘UR5e’, ‘UR10’, ‘UR10e’, ‘UR16e’, ‘Rizon4’, ‘Cobotta\_Pro\_900’, ‘Cobotta\_Pro\_1300’, ‘RS007L’, ‘RS007N’, ‘RS013N’, ‘RS025N’, ‘RS080N’, ‘Techman\_TM12’, ‘Kuka\_KR210’, ‘Fanuc\_CRX10IAL’]

On lines 35,38, the RmpFlow class initializer is simplified to unpacking a dictionary of loaded keyword arguments.
The `load_supported_motion_policy_config()` function is the simplest way to load supported robots.

## Debugging Features

The `RmpFlow` class has contains debugging features that are not generally available in the [Motion Policy Algorithm](concepts/motion_policy.html#isaac-sim-motion-policy) interface.
These debugging features allow decoupling of the simulator from the RmpFlow algorithm to help diagnose any undesirable behaviors
that are encountered ([RMPflow Debugging Features](concepts/rmpflow.html#isaac-sim-motion-generation-rmpflow-debugging-features)).

`RmpFlow` uses collision spheres internally to avoid collisions with external objects. These spheres can be visualized with
the `RmpFlow.visualize_collision_spheres()` function. This helps to determine whether `RmpFlow` has a reasonable representation
of the simulated robot.

The visualization can be used alongside a flag `RmpFlow.set_ignore_state_updates(True)` to ignore state updates from the robot
`Articulation` and instead assume that robot joint targets returned by `RmpFlow` are always perfectly achieved. This causes `RmpFlow`
to compute a robot path over time that is independent of the simulated robot `Articulation`. At each timestep, `RmpFlow` returns joint
targets that are passed to the robot `Articulation`.

```python
import os

import numpy as np
from isaacsim.core.api.objects.cuboid import FixedCuboid
from isaacsim.core.prims import SingleArticulation as Articulation
from isaacsim.core.prims import SingleXFormPrim as XFormPrim
from isaacsim.core.utils.extensions import get_extension_path_from_name
from isaacsim.core.utils.numpy.rotations import euler_angles_to_quats
from isaacsim.core.utils.stage import add_reference_to_stage
from isaacsim.robot_motion.motion_generation import ArticulationMotionPolicy, RmpFlow
from isaacsim.robot_motion.motion_generation.interface_config_loader import (
    get_supported_robot_policy_pairs,
    load_supported_motion_policy_config,
)
from isaacsim.storage.native import get_assets_root_path

class FrankaRmpFlowExample:
    def __init__(self):
        self._rmpflow = None
        self._articulation_rmpflow = None

        self._articulation = None
        self._target = None

        self._dbg_mode = True

    def load_example_assets(self):
        # Add the Franka and target to the stage
        # The position in which things are loaded is also the position in which they

        robot_prim_path = "/panda"
        path_to_robot_usd = get_assets_root_path() + "/Isaac/Robots/FrankaRobotics/FrankaPanda/franka.usd"

        add_reference_to_stage(path_to_robot_usd, robot_prim_path)
        self._articulation = Articulation(robot_prim_path)

        add_reference_to_stage(get_assets_root_path() + "/Isaac/Props/UIElements/frame_prim.usd", "/World/target")
        self._target = XFormPrim("/World/target", scale=[0.04, 0.04, 0.04])

        self._obstacle = FixedCuboid(
            "/World/obstacle", size=0.05, position=np.array([0.4, 0.0, 0.65]), color=np.array([0.0, 0.0, 1.0])
        )

        # Return assets that were added to the stage so that they can be registered with the core.World
        return self._articulation, self._target, self._obstacle

    def setup(self):
        # Loading RMPflow can be done quickly for supported robots
        print("Supported Robots with a Provided RMPflow Config:", list(get_supported_robot_policy_pairs().keys()))
        rmp_config = load_supported_motion_policy_config("Franka", "RMPflow")

        # Initialize an RmpFlow object
        self._rmpflow = RmpFlow(**rmp_config)
        self._rmpflow.add_obstacle(self._obstacle)

        if self._dbg_mode:
            self._rmpflow.set_ignore_state_updates(True)
            self._rmpflow.visualize_collision_spheres()

            # Set the robot gains to be deliberately poor
            bad_proportional_gains = self._articulation.get_articulation_controller().get_gains()[0] / 50
            self._articulation.get_articulation_controller().set_gains(kps=bad_proportional_gains)

        # Use the ArticulationMotionPolicy wrapper object to connect rmpflow to the Franka robot articulation.
        self._articulation_rmpflow = ArticulationMotionPolicy(self._articulation, self._rmpflow)

        self._target.set_world_pose(np.array([0.5, 0, 0.7]), euler_angles_to_quats([0, np.pi, 0]))

    def update(self, step: float):
        # Step is the time elapsed on this frame
        target_position, target_orientation = self._target.get_world_pose()

        self._rmpflow.set_end_effector_target(target_position, target_orientation)

        # Track any movements of the cube obstacle
        self._rmpflow.update_world()

        # Track any movements of the robot base
        robot_base_translation, robot_base_orientation = self._articulation.get_world_pose()
        self._rmpflow.set_robot_base_pose(robot_base_translation, robot_base_orientation)

        action = self._articulation_rmpflow.get_next_articulation_action(step)
        self._articulation.apply_action(action)

    def reset(self):
        # Rmpflow is stateless unless it is explicitly told not to be
        if self._dbg_mode:
            # RMPflow was set to roll out robot state internally, assuming that all returned joint targets were hit exactly.
            self._rmpflow.reset()
            self._rmpflow.visualize_collision_spheres()

        self._target.set_world_pose(np.array([0.5, 0, 0.7]), euler_angles_to_quats([0, np.pi, 0]))
```

The collision sphere visualization can be very helpful to distinguish between behaviors that are coming from the simulator, and behaviors that are coming from `RmpFlow`.
In the image below, the Franka robot is given weak proportional gains (lines 43-44). Using the debugging visualization, it is easy to
determine that RmpFlow is producing reasonable motions, but the simulated robot is simply not able to follow the motions. When RMPflow moves the robot quickly,
the Franka robot `Articulation` lags significantly behind the commanded position.

## Summary

This tutorial reviews using the `RmpFlow` class to generate reactive motions in response to a dynamic environment. The `RmpFlow`
class can be used to generate motions directly alongside an [Articulation Motion Policy](concepts/motion_policy.html#isaac-sim-articulation-motion-policy).

This tutorial reviewed four of the main features of `RmpFlow`:

> 1. Navigating the robot through an environment to a target position and orientation.
> 2. Adapting to a dynamic world on every frame.
> 3. Adapting to a change in the robot’s position on the USD stage.
> 4. Using visualization to decouple the simulated robot `Articulation` from the RMPflow algorithm for quick and easy debugging.

### Further Learning

To learn how to configure RMPflow for a new robot, review the
[basic formalism](concepts/rmpflow.html#isaac-sim-motion-generation-rmpflow), and then read the
[RMPflow tuning guide](concepts/rmpflow_tuning_guide.html#isaac-sim-motion-generation-rmpflow-tuning-guide) for practical advice.

To understand the motivation behind the structure and usage of `RmpFlow` in NVIDIA Isaac Sim, reference
the [Motion Generation](concepts/index.html#isaac-sim-motion-generation) page.

On this page

* [Getting Started](#getting-started)
* [Generating Motions with an RMPflow Instance](#generating-motions-with-an-rmpflow-instance)
  + [World State](#world-state)
* [Loading RMPflow for Supported Robots](#loading-rmpflow-for-supported-robots)
* [Debugging Features](#debugging-features)
* [Summary](#summary)
  + [Further Learning](#further-learning)

---

### Robot Description Editor

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/manipulators/manipulators_robot_description_editor.html

* [Robot Simulation](../robot_simulation/index.html)
* [Motion Generation (Deprecated)](motion_generation_overview.html)
* Lula Robot Description and XRDF Editor

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Lula Robot Description and XRDF Editor

Deprecated

For new development, consider using the newer [Robot Motion (Experimental)](../robot_motion_experimental/index.html) API, which provides improved interfaces and additional features over Lula.

## Learning Objectives

This tutorial shows how to use the **Robot Description Editor** UI tool to generate a configuration file that supplements
the information available about a robot in its URDF. Two motion generation packages leverage the
**Robot Description Editor** to specify necessary configuration information:

* [cuMotion](https://nvidia-isaac.github.io/cumotion/)
* Lula

This tutorial describes the motivation for needing specific config files for `Lula` and `cuMotion` algorithms, and goes over the minimal set of data that needs to be written into a robot description file for each available Lula algorithm.

This tutorial then shows how to use the **Robot Description Editor** UI tool to automatically write the appropriate information into (or edit) a `robot_description.yaml` file for Lula or an
[XRDF](https://nvidia-isaac-ros.github.io/concepts/manipulation/xrdf.html) file for `cuMotion`.

The **Robot Description Editor** is used on a stage that already has an Articulation on it. To follow along with the steps in the tutorial, it is best to open a single asset by reference. That is,
drag and drop a USD file onto an empty stage rather than clicking on the USD file to open it directly.

## What is in a Robot Description File?

A robot description file is the main configuration file that is required along with the robot URDF to use all Lula algorithms. Creating a `robot_description.yaml` file is the first and most time-consuming step that a user must take when hoping to use Lula algorithms on a new robot.

### Defining the Robot C-Space: Active and Fixed Joints

A key aspect of a robot description file is defining the robot c-space. For example, suppose we have a seven DOF robot manipulator such as the Franka arm with an attached two DOF gripper. In the robot URDF file, there are a total of nine non-fixed joints that could be considered controllable. However, the set of Lula algorithms ([RMPflow](concepts/rmpflow.html#isaac-sim-motion-generation-rmpflow), [Lula RRT](concepts/lula_rrt.html#isaac-sim-motion-generation-rrt), [Lula Trajectory Generator](concepts/trajectory_interface.html#isaac-sim-lula-trajectory-generator)) are designed to move the robot into position but not to control the end effector. In a typical use case, you might use `RmpFlow` to move the robot end effector into position above a block and then separately open and close the gripper.

A robot description file must distinguish each joint as:

* Active Joint
* Fixed Joint

Anything marked as an Active Joint will be directly controlled, while anything marked as a Fixed Joint will be assumed to be fixed from the perspective of Lula algorithms. In the case of using `RmpFlow` on the Franka robot, the seven joints in the Franka’s arm are marked as Active Joints, and the gripper joints are marked as Fixed Joints.

In the **Robot Description Editor**, positions must be selected for both active and fixed joints. The positions of Fixed Joints are taken to be default positions. When RmpFlow is not given any target, it will move the robot towards the default position. And when it is given a target, it will use the default positions of the Fixed Joints to resolve null-space behavior; that is, there are many ways for a seven DOF robot to reach a single target, and RmpFlow will be biased towards a c-space position that is close to the default position.

There is no way of telling RmpFlow that the Fixed Joints are in any other position than the position written into the robot description file, and as such it is important to choose a reasonable value for the positions of fixed joints. In the Franka example, the gripper joint positions are given a fixed value corresponding to the gripper being open, as this best facilitates RmpFlow avoiding collisions between the gripper and obstacles no matter the gripper state (when closed, the gripper fingers are inside the convex hull of an open gripper).

### Collision Spheres

Lula algorithms use a custom configuration to perform efficient collision avoidance. For a given robot, a set of collision spheres must be defined that roughly cover the surface of the robot. Lula algorithms will not allow any collision sphere defined in the robot description file to intersect any obstacle in the USD world. The **Robot Description Editor** provides multiple tools that allow you to quickly define a complete set of collision spheres for any robot.

### What is the Difference between a Robot Description File and an XRDF file?

An [XRDF](https://nvidia-isaac-ros.github.io/concepts/manipulation/xrdf.html) file is the main configuration file that is required by cuMotion for a specific robot,
and it contains a superset of the data in a Lula Robot Description File.
The **Robot Description Editor** can be used to generate an XRDF file that contains the minimal data required to start using cuMotion.
The use of the **Robot Description Editor** need not change in any way when configuring a robot for use with cuMotion versus Lula.
In the future, Lula will fully support XRDF files and deprecate Robot Description Files.

**As of Isaac Sim 4.0.0, the Robot Description Editor was modified to support XRDF files and some parts of this tutorial reference UI components that have changed.**

## What Information is Required for Each Lula Algorithm?

Different Lula algorithms require different levels of completion of the robot description file.
Every algorithm requires you to appropriately choose active and fixed joints.
However, collision spheres are only necessary to configure when using algorithms that perform collision avoidance with external obstacles.
For example, the [Lula Kinematics Solver](concepts/kinematics_solver.html#isaac-sim-lula-kinematics-solver) is purely kinematic, and it does not interact with the outside world.
As such, the collision sphere representation can be omitted from the robot description file.
[RMPflow](concepts/rmpflow.html#isaac-sim-motion-generation-rmpflow) can function without any collision spheres being defined, but it will not be able to avoid obstacles.

## Using the Robot Description Editor

This section of the tutorial includes brief text descriptions of the different panels in the **Robot Description Editor** UI tool. A more step-by-step tutorial can be found in the [Generate Robot Description Files and Collision Spheres](../robot_setup_tutorials/tutorial_generate_robot_config.html#isaac-sim-app-tutorial-generate-robot-config-lula) tutorial.

Note

The **Robot Description Editor** is not compatible with [Instanceable Assets](../isaac_lab_tutorials/tutorial_instanceable_assets.html#isaac-sim-app-tutorial-instanceable-assets), but a robot description file generated
for an asset that was later converted to an instanceable asset will still work on the instanceable asset.

To use the **Robot Description Editor**, ensure that the `Instanceable` checkbox is unchecked for all geometry prims in the robot’s hierarchy. This setting can be found in the **Property** panel when a geometry prim is selected.

The `Instanceable` checkbox (highlighted in red) should be unchecked for all geometry prims when using the Robot Description Editor.

### Getting Started

The **Robot Description Editor** can be found from the tool bar under **Tools > Robotics > Lula Robot Description Editor**. To get started, open the USD file of your chosen robot and click the **Play** button on the left-hand side.

In the **Selection Panel**, after a robot is on the stage and the stage is playing, a drop-down menu will populate where your robot can be selected. Select the prim path of your robot Articulation from the **Select Articulation** field. After this is done, another drop-down labeled **Select Link** will populate with the names of each link in our robot. This will be needed later as we use the tool.

We have done everything we need to do to start making our robot description file. Other panels will populate with robot-specific information, and we can move on to the **Set Joint Properties**.

### Set Joint Properties

As of Isaac Sim 4.0.0, **Command Panel** was renamed to **Set Joint Properties**, and fields were added to each joint for jerk and acceleration limits.

After the robot **Articulation** has been selected from the **Select Articulation** menu, the **Set Joint Properties** will expand and populate. The **Set Joint Properties** requires you to supply critical information for the robot description file to be properly generated. You can refer to [Defining the Robot C-Space: Active and Fixed Joints](#isaac-sim-tutorial-robot-description-editor-active-vs-fixed) for details.

In the **Set Joint Properties** select a **Joint Position** and a **Joint Status** for each joint in the robot Articulation. Keep in mind the following:

> * Joints are marked as Fixed Joints if and only if you intend for that joint to be directly controlled by Lula algorithms. Typically this involves marking each joint in the robot arm as active while leaving the joints in the manipulator attached to the arm as Fixed Joints. **At least one joint must be marked as an `Active Joint`**.
> * The joint positions of Fixed Joints can matter, depending on the use case and are worth some thought. The positions of Fixed Joints will be assumed by Lula to be truly fixed; that is, there is no way override the positions at runtime.
> * The positions of Fixed Joints are considered to be the default configuration of the robot. This default configuration is used by a subset of Lula algorithms, with the main case being `RmpFlow`. A default configuration should be chosen that is in front of the robot (along the +X axis by convention in Isaac Sim) and is not near any joint limits.

### Adding Collision Spheres

Collision spheres are added to the robot one link at a time. You can select the link of interest from the “Select Link” field of the **Selection Panel**. The **Link Sphere Editor** panel contains functions that are within the scope of the selected link such as adding spheres, scaling spheres, and clearing spheres only within the link. The **Editor Tools** panel contains functions that are outside the scope of the selected link such as **Undo** and **Redo** buttons, changing the color of collision spheres, and toggling the visibility of the robot.

When spheres are added to a link, they are added to the USD stage as a prim that is nested under the selected link. You can click on and modify any sphere by moving it around on the stage or changing its radius. The position of a sphere relative to the origin of the link that contains it is written as a fixed value into the robot description file.

There are three main ways to add a sphere to a link:

> * **Add Sphere:** Add a single sphere with a specified relative translation from the origin of the link. This translation can be easily changed after creation by modifying the sphere prim.
> * **Connect Spheres:** Select two spheres that have already been created under a link and connect them with a specified number of spheres in between. The locations and sizes of the connecting spheres are interpolated to best fill the volume of the cone-section defined by the two spheres being connected.
> * **Generate Spheres:** Select a mesh that defines the volume of the link, and automatically generate a set of N spheres that best fill the volume of the mesh. When a number of generated spheres is specified, a preview of the generated spheres will automatically appear, which can be finalized by clicking the “Generate Spheres” button. Any visible robot must will at least one mesh defining its link. When there are more than one mesh, it is best to try each of them to figure out the minimal set of spheres that can be generated for good coverage. It is typically better to “Connect Spheres” by hand for links with simple cylindrical shapes. This utility is not guaranteed to work for all meshes. It only works for water-tight triangle meshes. If the automatic generator doesn’t work for a link, add the spheres and connect them to the links by hand.

### Exporting Configuration Files

#### Lula Robot Description File

After completing the **Set Joint Properties** and creating a collision sphere representation of the robot, the robot description file can be exported under
**Export To File > Export to Lula Robot Description File**.
A file path to your local machine must be selected with a file name ending in `.yaml`.
The **Save** button will become enabled when a valid file path has been typed.

#### XRDF File

After completing the **Set Joint Properties** and creating a collision sphere representation of the robot, an [XRDF](https://nvidia-isaac-ros.github.io/concepts/manipulation/xrdf.html)
file can be generated under **Export to File > Export to cuMotion XRDF.** The file path must end in `.yaml` or `.xrdf`.
The **Save** button will become enabled when a valid file path has been typed.
A version dropdown allows you to select XRDF format version 1.0 or 2.0 (version 1.0 uses `collision`, version 2.0 uses `world_collision`).
When exporting an XRDF file, the **Robot Description Editor** has the following behavior:

* Create a single collision group that is used for both the collision group (`collision` in version 1.0, `world_collision` in version 2.0) and `self_collision` that uses the spheres created in the editor.
* Under `self_collision`, set each link to ignore both its parent and other links that have the same parent.
* Do not write Tool Frames.
* Do not write Modifiers.

Because XRDF files can contain more information than is represented in the **Robot Description Editor**, it is possible to merge the data in the **Robot Description Editor** with
an existing XRDF file. By selecting a file path to an XRDF file that already exists, an option will appear to **Merge With Existing XRDF**.
When merging with an existing XRDF file, the **Robot Description Editor** has the following behavior:

* Copy Tool Frames from the existing file.
* Copy Modifiers from the existing file.
* Copy self\_collision > ignore from the existing file if self\_collision > geometry matches the collision group geometry (`collision > geometry` in version 1.0, `world_collision > geometry` in version 2.0).
* Copy collision spheres from the existing file for any frames that were not represented in the **Robot Description Editor**.

### Importing Configuration Files

#### Lula Robot Description File

A pre-existing robot description file can be imported into the editor under **Import From File > Import Lula Robot Description File**.
Importing will overwrite all information in the **Robot Description Editor**.

#### XRDF File

A pre-existing [XRDF](https://nvidia-isaac-ros.github.io/concepts/manipulation/xrdf.html) file can be imported under **Import From File > Import XRDF File**.
The **Robot Description Editor** imports XRDF files with the following behavior:

* Both format version 1.0 and 2.0 are supported (version 1.0 uses `collision`, version 2.0 uses `world_collision`).
* Only the collision group spheres are imported.
* Modifiers are not used.
* Tool Frames are not used.
* The `self_collision` group is not used.

Importing will overwrite all information in the **Robot Description Editor**.

## Summary

This tutorial shows how to use the Lula **Robot Description Editor** to efficiently generate a Lula robot description file. This covers most of the configuration information required for different Lula algorithms.

The **Robot Description Editor** also supports XRDF files for use with `cuMotion`.

### Further Learning

To get the robot moving around with Lula algorithms, review the following tutorials:

> [Configuring RMPflow for a New Manipulator](manipulators_configure_rmpflow_denso.html#isaac-sim-app-tutorial-configure-rmpflow-denso)
>
> [Lula Kinematics Solver](manipulators_lula_kinematics.html#isaac-sim-app-tutorial-motion-generation-lula-kinematics)
>
> [Lula Trajectory Generator](manipulators_lula_trajectory_generator.html#isaac-sim-app-tutorial-motion-generation-lula-trajectory-generator)

On this page

* [Learning Objectives](#learning-objectives)
* [What is in a Robot Description File?](#what-is-in-a-robot-description-file)
  + [Defining the Robot C-Space: Active and Fixed Joints](#defining-the-robot-c-space-active-and-fixed-joints)
  + [Collision Spheres](#collision-spheres)
  + [What is the Difference between a Robot Description File and an XRDF file?](#what-is-the-difference-between-a-robot-description-file-and-an-xrdf-file)
* [What Information is Required for Each Lula Algorithm?](#what-information-is-required-for-each-lula-algorithm)
* [Using the Robot Description Editor](#using-the-robot-description-editor)
  + [Getting Started](#getting-started)
  + [Set Joint Properties](#set-joint-properties)
  + [Adding Collision Spheres](#adding-collision-spheres)
  + [Exporting Configuration Files](#exporting-configuration-files)
    - [Lula Robot Description File](#lula-robot-description-file)
    - [XRDF File](#xrdf-file)
  + [Importing Configuration Files](#importing-configuration-files)
    - [Lula Robot Description File](#id3)
    - [XRDF File](#id4)
* [Summary](#summary)
  + [Further Learning](#further-learning)

---

### Motion Generation Overview

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/manipulators/motion_generation_overview.html

* [Robot Simulation](../robot_simulation/index.html)
* Motion Generation (Deprecated)

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Motion Generation (Deprecated)

Deprecated

For new development, consider using the newer [Robot Motion (Experimental)](../robot_motion_experimental/index.html) API, which provides improved interfaces and additional features.

Lula is a high-performance motion generation library for robotic manipulation. RMPflow provides
real-time, reactive local policies to guide a robot manipulator to a task space target while
avoiding dynamic obstacles. A suite of Rapidly-exploring Random Tree (RRT) algorithms,
including RRT-Connect and JT-RRT, deliver global planning solutions in static environments.
Additionally, the trajectory generation tools in Lula provide time-optimal trajectories for
paths described as a series of c-space and task-space moves. Finally, Lula provides interfaces
to the performant forward and inverse kinematic solvers underpinning the higher-level motion
generation tools.

NVIDIA Isaac Sim also interfaces with [cuRobo](https://curobo.org), a high-performance, GPU-accelerated robotics motion
generation library that adds additional features to NVIDIA Isaac Sim such as batched collision-free inverse kinematics,
collision-free motion planning, and reactive control in the presence of obstacles represented as meshes or Nvblox maps.
For more information, see the [cuRobo tutorial](manipulators_curobo.html#isaac-sim-app-tutorial-curobo).

* [Motion Generation](concepts/index.html)
* [Lula Robot Description and XRDF Editor](manipulators_robot_description_editor.html)
* [Lula RMPflow](manipulators_rmpflow.html)
* [Lula RRT](manipulators_lula_rrt.html)
* [Lula Kinematics Solver](manipulators_lula_kinematics.html)
* [Lula Trajectory Generator](manipulators_lula_trajectory_generator.html)
* [Configuring RMPflow for a New Manipulator](manipulators_configure_rmpflow_denso.html)
* [cuRobo and cuMotion](manipulators_curobo.html)

## Examples

**Interactive Examples**

To locate the interactive examples, go to **Windows** > **Examples** > **Robotics Examples** and open the **Robotics Examples** tab if it’s not already. Select one of the following examples from the browser, read the **Information** tab on the right hand side of the browser window for instructions on how to run it.

* Follow Target Example: **Manipulation > Follow Target**
* RoboFactory Example: **Multi-Robot > RoboFactory**
* RoboParty Example: **Multi-Robot > RoboParty**

Note

Pressing **STOP**, then **PLAY** in this workflow might not reset the world properly. Use
the **RESET** button instead.

**Standalone Examples**

To run a standalone example, navigate to your `<isaac_sim_root_dir>`, then use `./python.sh` for Linux or `python.bat` for Windows to run the example scripts listed here.

* Follow Target with RMPflow (Franka): `standalone_examples/api/isaacsim.robot.experimental.manipulators/franka/follow_target_with_rmpflow.py`
* Follow Target with RMPflow (UR10): `standalone_examples/api/isaacsim.robot.experimental.manipulators/universal_robots/follow_target_with_rmpflow.py`
* Follow Target with IK (UR10): `standalone_examples/api/isaacsim.robot.experimental.manipulators/universal_robots/follow_target_with_ik.py`

On this page

* [Examples](#examples)

---


## Sensors

### Camera Structured Light

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/sensors/isaacsim_sensors_camera_structured_light.html

* [Sensors](index.html)
* [Camera Sensors](isaacsim_sensors_camera.html)
* Structured Light Cameras

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Structured Light Cameras

Isaac Sim models structured light cameras through the `isaacsim.sensors.experimental.rtx.StructuredLightCamera` class. Structured light imaging works by projecting a known pattern onto a scene
and capturing the deformation of that pattern from a camera offset from the projector. Cycling through a sequence of patterns and reconstructing the deformation between projector and camera frames allows
fine-grained depth recovery. Real structured light rigs commonly use phase-shifting sinusoids, gray-code stripes, or De Bruijn patterns; the per-pattern exposure is typically on the order of microseconds to
milliseconds, which keeps the captured scene effectively static across the pattern sequence.

## Overview

`StructuredLightCamera` is a subclass of `isaacsim.sensors.experimental.rtx.RtxCamera`. In addition to the underlying USD `Camera` prim, it creates a parent `Xform` (default `{path}/projectors`) populated with one
`UsdLux.RectLight` per projector pattern. Each `RectLight` has the `ShapingAPI` schema applied, the projector pattern as its `inputs:texture:file`, the projector direction texture as its
`projector:directionTexture:file`, `isProjector=True`, and `visibleInPrimaryRay=False`. At any given simulation time exactly one `RectLight` is visible.

Pattern selection is **simulation-time-driven**:

* The constructor accepts a `projector_timestamps` list of rational tuples `(numerator, denominator)`, one per pattern. Each tuple is the simulation time (in seconds) at which that pattern becomes active.
  The first entry must represent \(t = 0\) (typically `(0, 1)`; any `(0, k)` is accepted), and the list must be strictly increasing. Rational tuples avoid the floating-point precision issues that
  arise when timestamps span sub-millisecond resolution. If `projector_timestamps` is omitted, the schedule defaults to `[(i, 30) for i in range(N)]` (a 30 Hz uniform cadence).
* On every Kit app-update tick, an observer reads the current timeline value, computes `current_time mod cycle_period`, and selects the pattern whose timestamp is the largest one less than or equal to the
  resulting phase. The cycle period defaults to `timestamps[-1] + (timestamps[1] - timestamps[0])` for \(N \geq 2\) patterns, or `Fraction(1, 30)` for \(N = 1\). It can be overridden via
  `projector_cycle_period`.

Because pattern intervals are typically much smaller than a single physics step, the class emits a one-time warning at the first observed simulation `dt` larger than the minimum interval between consecutive
patterns (including the wrap-around from the last pattern back to the first), and a per-tick warning whenever a single tick advances the active pattern by more than one index.

## Data acquisition

`StructuredLightCamera` is an authoring class — it creates and manages USD prims but does not retrieve image data on its own. To capture frames, wrap an instance in
`isaacsim.sensors.experimental.rtx.CameraSensor`:

```python
from pathlib import Path

import omni.kit.app
from isaacsim.sensors.experimental.rtx import CameraSensor, StructuredLightCamera

# Resolve the bundled structured-light test patterns shipped with the extension.
ext_root = (
    omni.kit.app.get_app().get_extension_manager().get_extension_path_by_module("isaacsim.sensors.experimental.rtx")
)
data_dir = Path(ext_root) / "isaacsim/sensors/experimental/rtx/tests/data/structured_light_camera"
patterns = [data_dir / "patterns" / f"image_{i:02d}.png" for i in range(10)]
direction_texture = data_dir / "projector_opencv_pinhole_4000x2880_2025_10_08_10_51_18.exr"

# 10 patterns spaced over 0 - 2 ms with variable intervals. Rational tuples
# avoid floating-point error at sub-millisecond resolution.
projector_timestamps = [
    (0, 1),
    (19, 100_000),
    (41, 100_000),
    (62, 100_000),
    (4, 5_000),
    (101, 100_000),
    (61, 50_000),
    (141, 100_000),
    (179, 100_000),
    (1, 500),
]

# Create the camera at a root-level path. The projector RectLight prims are
# created at ``/structured_light_camera/projectors`` and cycle automatically
# based on the current simulation time.
cam = StructuredLightCamera(
    "/structured_light_camera",
    projector_light_patterns=patterns,
    projector_direction_texture=direction_texture,
    projector_timestamps=projector_timestamps,
    projector_intensity=150_000.0,
)

# Wrap the camera in a CameraSensor with the rgb annotator to retrieve frames.
sensor = CameraSensor(cam, resolution=(720, 1280), annotators=["rgb"])
```

The `CameraSensor` owns a Replicator render product against the same Camera prim, and there are two complementary ways to get image data out of it:

* **Manual annotator pull** — construct the sensor with the desired annotators (`annotators=["rgb"]` above) and call `sensor.get_data("rgb")` from your own loop. The snippet above uses this pattern.
* **Replicator writer** — leave `annotators=[]` and call `sensor.attach_writer("BasicWriter", output_dir=..., rgb=True)` (or any other Replicator writer). Each `rep.orchestrator.step` then automatically
  dispatches a write to disk without any custom plumbing in your loop. See the [Standalone Python](#isaacsim-sensors-camera-structured-light-standalone) section for an end-to-end example of this pattern.

## Standalone Python

The standalone example at `standalone_examples/api/isaacsim.sensors.experimental.rtx/camera_structured_light.py` demonstrates capturing a 10-pattern sequence using the Replicator Orchestrator and a
`BasicWriter`. The example:

* Loads the bundled structured-light patterns and projector direction texture from the extension’s `tests/data/structured_light_camera/` directory.
* Builds a 1000-unit white PBR cube as an enclosure, with the camera and coincident projector at the origin.
* Drives `rep.orchestrator.step(rt_subframes=32, delta_time=<interval>)` once per pattern, where `<interval>` is the difference between consecutive timestamps. Because `timestamps[0]` is always zero,
  the first step’s `delta_time` is also zero, so the orchestrator captures pattern 0 at \(t = 0\) before advancing.
* Attaches a `BasicWriter` to the sensor so each step writes one `rgb_NNNN.png` to the example’s output directory.

Note

This example demonstrates the API plumbing — pattern cycling, RectLight cluster authoring, calibrated camera intrinsics, and Orchestrator capture. The camera and projector share an origin and so it
does **not** model a real depth-recovery rig (which would have a non-zero baseline between camera and projector). For a depth-recovery workflow, position the projector with `projector_position` /
`projector_orientation` offset from the camera and adjust the captured-pattern triangulation accordingly.

Run the example:

```python
./python.sh standalone_examples/api/isaacsim.sensors.experimental.rtx/camera_structured_light.py
```

After the script completes, the output directory `_example_output_isaacsim.sensors.experimental.rtx/camera_structured_light/` contains 10 RGB frames named `rgb_0000.png` through `rgb_0009.png`, plus a
`metadata.txt` file recording the writer name, version, and Replicator global seed.

Pattern 0

Pattern 1

Pattern 2

Pattern 3

Pattern 4

Pattern 5

Pattern 6

Pattern 7

Pattern 8

Pattern 9

Note

Your output images may differ from those shown above due to variance in the renderer across different hardware and driver configurations.

On this page

* [Overview](#overview)
* [Data acquisition](#data-acquisition)
* [Standalone Python](#standalone-python)

---

### Physics Sensors Index

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/sensors/isaacsim_sensors_physics.html

* [Sensors](index.html)
* Physics-based sensors

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Physics-based sensors

Isaac Sim’s physics-based sensors use CPU physics simulations and run after rendering finishes. They have access to a prim’s physics properties, like mass and velocity.

These sensors output the exact measurements from the physics engine, and you can augment the sensor readings in post-processing.
By default, sensors output data at the physics rate. To generate data beyond this rate, provide additional interpolation options. Ground truth readings from the simulator might
already have some noise; you can add more noise in post-processing to make sensor readings more realistic.

The physics-based sensors are organized in the `isaacsim.sensors.experimental.physics` extension.

Deprecated since version 6.0: The `isaacsim.sensors.physics` extension is deprecated. Use `isaacsim.sensors.experimental.physics` instead.
The new extension provides equivalent sensor classes (`ContactSensor`, `IMUSensor`, `EffortSensor`, etc.) with the same core functionality.
See [Physics Sensors](../migration_guides/isaac_sim_6_0/sensors_physics_to_experimental_physics.html#isaacsim-sensors-physics-migration) for step-by-step migration instructions, or the [API Documentation](../py/source/extensions/isaacsim.sensors.experimental.physics/docs/index.html) for the replacement APIs.

Isaac Sim supports the following physics-based ground truth sensors:

* [Articulation joint sensors](isaacsim_sensors_physics_articulation_force.html)
* [Contact sensor](isaacsim_sensors_physics_contact.html)
* [Effort sensor](isaacsim_sensors_physics_effort.html)
* [IMU sensor](isaacsim_sensors_physics_imu.html)
* [Joint state sensor](isaacsim_sensors_physics_joint_state.html)
* [Physics raycast sensor](isaacsim_sensors_physics_raycast.html)

---

### Articulation Force

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/sensors/isaacsim_sensors_physics_articulation_force.html

* [Sensors](index.html)
* [Physics-based sensors](isaacsim_sensors_physics.html)
* Articulation joint sensors

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Articulation joint sensors

Articulation sensors allow reading the active and passive components of the joint forces using the
[Articulation](../py/source/extensions/isaacsim.core.experimental.prims/docs/index.html#isaacsim.core.experimental.prims.Articulation) class
from the `isaacsim.core.experimental.prims` extension.
See [Robot Simulation Snippets](../python_scripting/robots_simulation.html#isaac-robot-simulation-how-to) for more details about the Articulation class. Specifically,

* `get_link_incoming_joint_force()` returns the 6D force and torque (shape `(N, L, 3)` each) for each link’s incoming joint.
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

---

### Contact Sensor

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/sensors/isaacsim_sensors_physics_contact.html

* [Sensors](index.html)
* [Physics-based sensors](isaacsim_sensors_physics.html)
* Contact sensor

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Contact sensor

Deprecated since version 6.0: The `isaacsim.sensors.physics` Contact Sensor extension is deprecated.
Use `isaacsim.sensors.experimental.physics.ContactSensor` instead.
See the [API Documentation](#api-documentation) section below for links.

The contact sensor uses the PhysX Contact Report API to generate a sensor reading similar to contact cells or pressure-based sensors placed on the surface of an object.
The Contact Sensor API builds on the Contact Report API by providing contact data filtered by the object it was placed in, along with an optional filter that only considers contacts in a specific region of the object. For example, imagine a quadruped robot with sensors in its feet. While the simulation treats the entire leg as a rigid body, you can only measure contact on the foot pads, so you can add a region filter that discards contacts outside that boundary.
The Contact Sensor API also provides persistent contact data, even when the PhysX engine stops streaming contacts to preserve compute time. While the simulation provides full information about contacts, such as contact pairs, normals, and contact points, the Contact Sensor API matches real data obtained by single-cell contact pads. If you need full contact data, the Contact Sensor API gets you filtered contact information without changes to the data acquired in PhysX.

See the [Isaac Sim Conventions](../reference_material/reference_conventions.html#isaac-sim-conventions) documentation for a complete list of Isaac Sim conventions.

**Contact sensor properties**

1. `radius` parameter specifies the distance of the contact force that it would detect. A value of `-1` uses the prim’s collision geometry.
2. `enabled` parameter determines if the sensor is running or not.
3. `min threshold` parameter specifies the minimum amount of force to trigger a contact.
4. `max threshold` parameter specifies the maximum amount of force the sensor outputs.
5. `sensorPeriod` parameter specifies the time in between sensor measurement. **Deprecated** since `isaacsim.robot.schema` 6.2.0 — only used by the deprecated `isaacsim.sensors.physics` extension. The new `isaacsim.sensors.experimental.physics` extension reads every physics step.

For the full USD attribute definitions, see the [Contact Sensor schema reference](../omniverse_usd/sensor_schema.html#isaac-sim-sensor-schema-contact).

## GUI

### Creating and modifying the contact sensor

To create and modify a contact sensor, start with a prim in the scene that you want to attach the sensor to.

1. To create a Physics Scene, go to the top Menu Bar and click **Create > Physics > Physics Scene**. Verify that there is now a `PhysicsScene` [Prim](../reference_material/reference_glossary.html#isaac-sim-glossary-prim) in the [Stage](../reference_material/reference_glossary.html#isaac-sim-glossary-stage) panel on the right.
2. To create a contact sensor, left click on the prim to attach the contact sensor on the stage, then go to the top Menu Bar and click **Create > Sensors > Contact\_sensor**.
3. To change the position and orientation of the contact sensor, use **Translate and Orientate** tab.
4. To change other contact sensor properties, click **Raw USD Properties** and modify properties such as min/max force threshold, enable/disable sensor, and sensor period.

### Contact sensor example

To run the Contact Sensor Example:

1. Activate **Robotics Examples** tab from **Windows** > **Examples** > **Robotics Examples**.
2. Click **Robotics Examples** > **Sensors** > **Contact Sensor**.
3. Verify that you see a window containing the sensor’s force readings color coded by each ant’s arm.
4. Press the **Open Source Code** button to view the source code. The source code illustrates how to load an Ant body into the scene and then add sensors to it using the Python API.
5. Press the **Play** button to begin simulating.
6. Press `SHIFT + LEFT_CLICK` to drag the ant around and see changes in the readings.

### OmniGraph workflow

The following tutorial shows how to use OmniGraph to interact with and visualize the contact sensor readings.

#### Scene setup

1. Add a cube to the stage by **Create > Mesh > Cube**, select the cube and drag it up. Then select the cube and right click **Add > Physics > Rigid Body with Colliders Preset**.
2. Add a physics scene by **Create > Physics > PhysicsScene**.
3. Add a ground plane by **Create> Physics > GroundPlane**.
4. Add a contact sensor by selecting the cube, and select on the top menu **Create > Sensors > Contact Sensor**.

#### OmniGraph setup

To set up the OmniGraph to collect readings from this sensor:

1. Create the new action graph by navigating to **Window > Graph Editors > Action Graph**, and selecting New Action Graph in the new tab that opens.
2. Add the following nodes to the graph:

> * *On Playback Tick*: Executes the graph every simulation timestep.
> * *Isaac Read Contact Sensor*: Reads the contact sensor. In the **Property** tab, set Contact Sensor Prim to */World/Cube/Contact\_Sensor* to point to the location of the contact sensor prim.
> * *To String*: Converts the contact sensor readings to string format.
> * *Print Text*: Prints the string readings to console. In the **Property** tab, set Log Level to *Warning* so that messages are visible in the terminal or console by default.

1. Connect the above nodes as follows to print out the contact sensor reading:
2. Press the **Play** button on the GUI. If set up correctly, verify that the Isaac Sim internal *Console* reads out the contact sensor’s force output.

**Contact sensor visualization**

You can visualize the contact sensor position and radius using the `Isaac xPrim Radius Visualizer Node`. Connect the xPrim input to the contact sensor prim and connect `Tick` to `Exec in`. Then set the radius, color, and line thickness. The contact sensor appears when you press **Play**.

Note

The spherical region only determines the boundary for contacts that are counted. All contacts still only happen at the surface of the object bounded by the spherical region.

## Standalone Python

### Creating and modifying the contact sensor

For the example snippets below, prepare the scene using the following snippet by adding a `PhysicsScene`, `GroundPlane`, and a `Cube` prim with collision and rigid body physics.
Attach the contact sensor to the latter.

```python
from isaacsim import SimulationApp

simulation_app = SimulationApp({"headless": False})

import numpy as np
import omni.usd
from isaacsim.core.experimental.objects import Cube, GroundPlane
from isaacsim.core.experimental.prims import GeomPrim, RigidPrim
from pxr import UsdPhysics

# Create physics scene
stage = omni.usd.get_context().get_stage()
UsdPhysics.Scene.Define(stage, "/World/PhysicsScene")

# Add ground plane and a dynamic cube with collision and rigid body
GroundPlane("/World/groundPlane", sizes=10, colors=np.array([0.5, 0.5, 0.5]))
Cube(
    "/World/Cube",
    positions=np.array([-0.5, -0.2, 1.0]),
    scales=np.array([0.5, 0.5, 0.5]),
    colors=np.array([0.2, 0.3, 0.0]),
)
RigidPrim("/World/Cube")
GeomPrim("/World/Cube", apply_collision_apis=True)
```

#### Using the Python API

Contact sensors are created with Python by calling `Contact.create()` (the authoring class) and wrapping the returned authoring object with `ContactSensor` for runtime data access. Available parameters and their defaults are listed below; the path must include the parent prim path.

```python
import numpy as np
from isaacsim.sensors.experimental.physics import Contact, ContactSensor

sensor = ContactSensor(
    Contact.create(
        "/World/Cube/Contact_Sensor",
        min_threshold=0.0001,
        max_threshold=100000,
        translations=np.array([[0.0, 0.0, 0.0]]),
    )
)
```

#### Using the Python wrapper

The contact sensor can also be created by constructing a `Contact` authoring object directly and wrapping it with `ContactSensor` for runtime data access. The `Contact` constructor wraps an existing sensor prim or creates a new one with default attributes; the `ContactSensor` runtime exposes `get_sensor_reading()`, `get_data()`, and `get_raw_data()` for reading sensor output. Property setters (`set_min_threshold` / `set_max_threshold` / `set_radius` / corresponding getters) live on the `Contact` authoring object, accessible as `sensor.contact` after construction.

```python
import numpy as np
from isaacsim.sensors.experimental.physics import Contact, ContactSensor

sensor = ContactSensor(
    Contact(
        "/World/Cube/Contact_Sensor",
        translations=np.array([[0.0, 0.0, 0.0]]),
    )
)
```

Note

`translations` (local-frame) and `positions` (world-frame) cannot both be defined — they are mutually exclusive.

Creating a contact sensor requires an enabled rigid-body ancestor, and the body depends on a Contact Report API. Contact-producing geometry still needs collision APIs. `Contact.create()` applies the Contact Report API on the rigid-body ancestor when it creates the sensor prim; when wrapping an existing sensor prim with `Contact(path)` the API is not applied by Python, but the C++ runtime ensures contact reporting is enabled when the sensor goes live on **Play**. You can also manually add a Contact Report API to a prim through:

```python
stage = omni.usd.get_context().get_stage()
parent_prim = stage.GetPrimAtPath("/World/Cube")
contact_report = PhysxSchema.PhysxContactReportAPI.Apply(parent_prim)
# Set a minimum threshold for the contact report to zero
contact_report.CreateThresholdAttr(0.0)
```

To modify sensor parameters at runtime, use the authoring object exposed via `sensor.contact`: `sensor.contact.set_min_threshold(value)`, `sensor.contact.set_max_threshold(value)`, `sensor.contact.set_radius(value)`. The previous shorthand methods on `ContactSensor` itself were removed in 3.0.0 — call them on `sensor.contact`.

### Reading sensor output

The contact sensors are created dynamically on **Play**. Moving the sensor prim while the simulation is running invalidates the sensor. If you need to make hierarchical changes to the contact sensor like changing its rigid body parent, stop the simulator, make the changes, and then restart the simulation.

There are three methods for reading the sensor output:

* `ContactSensor.get_sensor_reading()` — returns the cached `ContactSensorReading`
* `ContactSensor.get_data()` — returns a structured dictionary
* OmniGraph node `Isaac Read Contact Sensor`

The following snippets assume you have created a `/World/Cube` prim and contact sensor prim using one of the two snippets [above](#isaacsim-sensors-physics-contact-standalone-python-create-modify).

**ContactSensor.get\_sensor\_reading()**

Returns a `ContactSensorReading` with `is_valid`, `time`, `value` (force magnitude), and `in_contact`.

Sample usage to get the reading from the current frame:

```python
from isaacsim.sensors.experimental.physics import ContactSensor

sensor = ContactSensor("/World/Cube/Contact_Sensor")
sensor.get_sensor_reading()
```

**ContactSensor.get\_data()**

The `get_data()` member function on the `ContactSensor` runtime class returns a structured dictionary with `time`, `physics_step`, `in_contact`, `force`, and `number_of_contacts`. Internally it calls `get_sensor_reading()` for the contact state and `get_raw_data()` to compute `number_of_contacts`. When `add_raw_contact_data_to_frame()` has been called, the dictionary additionally contains a `contacts` list whose entries provide `body0`, `body1`, `position`, `normal`, and `impulse` per contact point.

Sample usage:

```python
import numpy as np
from isaacsim.sensors.experimental.physics import Contact, ContactSensor

sensor = ContactSensor(
    Contact(
        "/World/Cube/Contact_Sensor",
        translations=np.array([[0.0, 0.0, 0.0]]),
    )
)

value = sensor.get_data()
print(value)
```

**ContactSensor.get\_raw\_data()**

Returns a list of raw contact records (one per contact event in the current physics step). Each record contains `time`, `dt`, `body0`, `body1`, `position`, `normal`, and `impulse`. Raw data disregards the sensor’s `min_threshold`/`max_threshold` filtering: contacts that fall below the threshold are still reported here, even though they would be discarded by the filtered `ContactSensorReading`. To pass through to a frame call instead, enable the `contacts` list with `ContactSensor.add_raw_contact_data_to_frame()`.

```python
from isaacsim.sensors.experimental.physics import ContactSensor

sensor = ContactSensor("/World/Cube/Contact_Sensor")
raw_data = sensor.get_raw_data()
print(str(raw_data))
```

### API documentation

Deprecated since version 6.0: The `isaacsim.sensors.physics` extension is deprecated. Use `isaacsim.sensors.experimental.physics.ContactSensor` instead.

See the [isaacsim.sensors.experimental.physics API Documentation](../py/source/extensions/isaacsim.sensors.experimental.physics/docs/index.html) for the current API and [isaacsim.sensors.physics API Documentation (deprecated)](../py/source/extensions/isaacsim.sensors.physics/docs/index.html) for the deprecated API.

On this page

* [GUI](#gui)
  + [Creating and modifying the contact sensor](#creating-and-modifying-the-contact-sensor)
  + [Contact sensor example](#contact-sensor-example)
  + [OmniGraph workflow](#omnigraph-workflow)
    - [Scene setup](#scene-setup)
    - [OmniGraph setup](#omnigraph-setup)
* [Standalone Python](#standalone-python)
  + [Creating and modifying the contact sensor](#isaacsim-sensors-physics-contact-standalone-python-create-modify)
    - [Using the Python API](#using-the-python-api)
    - [Using the Python wrapper](#using-the-python-wrapper)
  + [Reading sensor output](#reading-sensor-output)
  + [API documentation](#api-documentation)

---

### Effort Sensor

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/sensors/isaacsim_sensors_physics_effort.html

* [Sensors](index.html)
* [Physics-based sensors](isaacsim_sensors_physics.html)
* Effort sensor

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Effort sensor

Deprecated since version 6.0: The `isaacsim.sensors.physics` Effort Sensor extension is deprecated.
Use `isaacsim.sensors.experimental.physics.EffortSensor` instead.
See the [API Documentation](#api-documentation) section below for links.

The effort sensor in Isaac Sim tracks the torque or force applied to individual joints. Torque is measured for revolute joints and magnitude of force is measured for linear joints.

See the [Isaac Sim Conventions](../reference_material/reference_conventions.html#isaac-sim-conventions) documentation for a complete list of Isaac Sim conventions.

## GUI

### Scene setup

Begin by adding a Simple Articulation to the scene, which can be accessed in the Content Browser.

1. In the *Content Browser*, search for `simple_articulation` or navigate to `Isaac Sim/Robots/IsaacSim/SimpleArticulation/simple_articulation.usd`.
2. Drag `simple_articulation` onto the *World* prim in the **Stage** UI window on the right hand side to add an instance into the environment.
3. To drive the revolute joint, in the **Stage** window, select the RevoluteJoint prim at */World/simple\_articulation/Arm/RevoluteJoint*, and scroll down to **Drive** in the **Property** window. Set the target velocity to `90 deg/s`, and stiffness to `0`.

### Creating and modifying the effort sensor

The following section describes how to create the effort sensor using the **Script Editor**, opened from **Window > Script Editor**.
The effort sensor is created by constructing an `isaacsim.sensors.experimental.physics.EffortSensor` directly with the joint prim path. The class exposes `get_sensor_reading()` and `get_data()` for reading sensor output, plus `update_dof_name()` and `change_buffer_size()` for runtime reconfiguration. (Unlike the contact, IMU, and raycast sensors, `EffortSensor` has no separate authoring class because it has no schema-bearing prim of its own.)

```python
from isaacsim.sensors.experimental.physics import EffortSensor

sensor = EffortSensor(path="/World/simple_articulation/Arm/RevoluteJoint", enabled=True)
```

Note

The joint prim you pass in **is** the sensor’s prim — `EffortSensor` does not author a separate USD prim in the **Stage** panel on construction. Effort readings become available via `get_sensor_reading()` once the simulation is playing; check `reading.is_valid` after pressing **Play** to confirm the sensor is active.

To modify sensor parameters, change class member variables such as `enabled` directly. To change the `dof_name` and `buffer_size` for readings, use the corresponding member functions, `update_dof_name` and `change_buffer_size`.

### Reading sensor output with Python

There are two methods for reading the sensor output:

* `EffortSensor.get_sensor_reading()` — returns an `EffortSensorReading` object with `is_valid`, `time`, and `value`.
* `EffortSensor.get_data()` — returns a structured dictionary with `value`, `is_valid`, `time`, and `physics_step`.

After you create the effort sensor, press **Play** to start the simulation and call the function below to get the sensor reading for the current frame:

**EffortSensor.get\_sensor\_reading()**

```python
reading = sensor.get_sensor_reading()
```

**EffortSensor.get\_data()**

```python
frame = sensor.get_data()
print(f"Effort: {frame['value']}, valid: {frame['is_valid']}, time: {frame['time']}")
```

### OmniGraph workflow

Set up OmniGraph to create the effort sensor and collect readings from it:

1. Create the new action graph by navigating to **Window > Graph Editors > Action Graph**, and selecting **New Action Graph** in the new tab that opens.
2. Add the following nodes to the graph:

   > * **On Playback Tick**: Executes the graph nodes every simulation timestep.
   > * **Isaac Read Effort Node**: Reads the effort sensor. In the **Property** tab, set Effort Prim to the exact joint of measurement. For example */World/simple\_articulation/Arm/RevoluteJoint* in `simple_articulation.usd`.
   > * **To String**: Converts the effort sensor readings to string format.
   > * **Print Text**: Prints the string readings to console. In the **Property** tab, set Log Level to *Warning* so that messages are visible in the terminal/console by default. Additionally, check *To Screen* to print directly to screen.

Connect the nodes as follows to print the effort sensor reading:

Note

Configure the joints to the correct axis to get the expected readings.

## API documentation

Deprecated since version 6.0: The `isaacsim.sensors.physics` extension is deprecated. Use `isaacsim.sensors.experimental.physics.EffortSensor` instead.

See the [isaacsim.sensors.experimental.physics API Documentation](../py/source/extensions/isaacsim.sensors.experimental.physics/docs/index.html) for the current API and [isaacsim.sensors.physics API Documentation (deprecated)](../py/source/extensions/isaacsim.sensors.physics/docs/index.html) for the deprecated API.

On this page

* [GUI](#gui)
  + [Scene setup](#scene-setup)
  + [Creating and modifying the effort sensor](#creating-and-modifying-the-effort-sensor)
  + [Reading sensor output with Python](#reading-sensor-output-with-python)
  + [OmniGraph workflow](#omnigraph-workflow)
* [API documentation](#api-documentation)

---

### IMU

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/sensors/isaacsim_sensors_physics_imu.html

* [Sensors](index.html)
* [Physics-based sensors](isaacsim_sensors_physics.html)
* IMU sensor

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# IMU sensor

Deprecated since version 6.0: The `isaacsim.sensors.physics` IMU Sensor extension is deprecated.
Use `isaacsim.sensors.experimental.physics.IMUSensor` instead.
See the [API Documentation](#api-documentation) section below for links.

The IMU sensor in Isaac Sim tracks body motion and outputs simulated accelerometer and gyroscope readings.
Like real IMU sensors, simulated IMUs give acceleration and angular velocity measurements in the local `x, y, z` axes with stage units.

See the [Isaac Sim Conventions](../reference_material/reference_conventions.html#isaac-sim-conventions) documentation for a complete list of Isaac Sim conventions.

**IMU sensor properties**

1. `enabled` parameter determines if the sensor is running or not.
2. `sensorPeriod` parameter specifies the time in between sensor measurement. **Deprecated** since `isaacsim.robot.schema` 6.2.0 — only used by the deprecated `isaacsim.sensors.physics` extension. The new `isaacsim.sensors.experimental.physics` extension reads every physics step.
3. `angularVelocityFilterWidth` parameter specifies the size of the angular velocity rolling average. Increasing this parameter smooths angular velocity output.
4. `linearAccelerationFilterWidth` parameter specifies the size of the linear acceleration rolling average. Increasing this parameter smooths linear acceleration output.
5. `orientationFilterWidth` parameter specifies the size of the orientation rolling average. Increasing this parameter smooths orientation output.

The size of the data buffer used in interpolation is two times the max of the filter width or 20, whichever is greater.

For the full USD attribute definitions, see the [IMU Sensor schema reference](../omniverse_usd/sensor_schema.html#isaac-sim-sensor-schema-imu).

## GUI

### Creating and modifying the IMU

To create and modify an IMU sensor, start with a prim in the scene that you want to attach the sensor to:

1. To create a Physics Scene, go to the top Menu Bar and click **Create > Physics > Physics Scene**. Verify that you have a `PhysicsScene` [Prim](../reference_material/reference_glossary.html#isaac-sim-glossary-prim) in the [Stage](../reference_material/reference_glossary.html#isaac-sim-glossary-stage) panel on the right.
2. To create an IMU, left click on the prim to attach the IMU on the stage, then go to the top Menu Bar and click **Create > Sensors > Imu Sensor**.
3. To change the position and orientation of the IMU, left click on the `Imu_Sensor` prim, then modify the **Transform** properties under the **Property** tab.
4. To change other IMU properties, expand the **Raw USD Properties** section and modify properties such as filter width, enable/disable sensor, and sensor period.

### IMU Example

To run the IMU example:

1. Activate **Robotics Examples** tab from **Windows** > **Examples** > **Robotics Examples**.
2. Click **Robotics Examples** > **Sensors** > **IMU Sensor** > **Load Scene**.
3. Verify that you have a window containing each axis of the accelerometer and gyro readings being displayed.
4. Press the **Open Source Code** button to view the source code. The source code illustrates how to load an Ant body into the scene and then add the sensor to it using the Python API.
5. Press the **Play** button to begin simulating.
6. Press `SHIFT + LEFT_CLICK` over the ant to drag it around and see changes in the readings.

### OmniGraph workflow

The following tutorial shows how to use OmniGraph to interact with the IMU sensor.

#### Scene setup

Begin by adding a Simple Articulation to the scene. Access the articulation file through a [Omniverse Nucleus](../reference_material/reference_glossary.html#isaac-sim-glossary-nucleus) server in the content window.
Connecting to this server gives you access to the library of Isaac Sim robots, sensors, and environments.

After connecting to the server:

1. Navigate to `Robots/IsaacSim/SimpleArticulation/simple_articulation.usd` in the **Content Browser**.
2. Drag `simple_articulation` onto the *World* prim in the **Stage** UI window on the right hand side to add an instance into the environment.
3. To drive the revolute joint, in the **Stage** window, select the RevoluteJoint prim at */World/simple\_articulation/Arm/RevoluteJoint*, and scroll down to **Drive** in the **Property** window. Set the target velocity to `90 deg/s` and stiffness to `0`.

To add an IMU sensor to your robot and collect some data:

1. In the **Stage** tab, navigate to the */World/simple\_articulation/Arm* prim and select it.
2. Add the sensor to the prim by **Create > Sensors > Imu Sensor**.
3. The newly added IMU sensor can be viewed by hitting the **+** button next to the Arm prim.

Note

In general, sensors must be added to rigid body prims to correctly report data. The prims in this robot are already rigid bodies, so no extra setup is required for this case.

#### OmniGraph setup

To set up the OmniGraph to collect readings from this sensor:

1. Create the new action graph by navigating to **Window > Graph Editors > Action Graph**, and selecting **New Action Graph** in the new tab that opens.
2. Add the following nodes to the graph, and set their properties as follows:

> * **On Playback Tick**: Executes the graph nodes every simulation timestep.
> * **Isaac Read IMU Node**: Reads the IMU sensor. In the **Property** tab, set IMU Prim to */World/simple\_articulation/Arm/Imu\_Sensor*, to point to the location of the IMU sensor prim. Select **read gravity** to read gravitational acceleration.
> * **To String**: Converts the IMU readings to string format.
> * **Print Text**: Prints the string readings to console. In the **Property** tab, set **Log Level** to **Warning** so that messages are visible in the terminal/console by default.

1. Connect the above nodes as follows to print out the IMU sensor reading:
2. Press the **Play** button on the GUI. If set up correctly, verify that the Isaac Sim internal *Console* reads out the IMU sensor’s angular velocity.

## Standalone Python

### Creating and modifying the IMU

There are two ways to create an IMU Sensor in Python:

* Use the `IMU.create()` authoring class method, then wrap with `IMUSensor` for runtime reads.
* Use the `IMU` authoring class constructor directly, then wrap with `IMUSensor`.

This section provides snippets to execute with standalone Python. Modify them to suit your use case. The following snippet adds a ground plane, cube prim with collision and rigid body physics, and physics scene to an Isaac Sim scene. The reference snippets below require these objects.

```python
from isaacsim import SimulationApp

simulation_app = SimulationApp({"headless": False})

import numpy as np
import omni.usd
from isaacsim.core.experimental.objects import Cube, GroundPlane
from isaacsim.core.experimental.prims import GeomPrim, RigidPrim
from pxr import UsdPhysics

# Create physics scene
stage = omni.usd.get_context().get_stage()
UsdPhysics.Scene.Define(stage, "/World/PhysicsScene")

# Add ground plane and a dynamic cube with collision and rigid body
GroundPlane("/World/groundPlane", sizes=10, colors=np.array([0.5, 0.5, 0.5]))
Cube(
    "/World/Cube",
    positions=np.array([-0.5, -0.2, 1.0]),
    scales=np.array([0.5, 0.5, 0.5]),
    colors=np.array([0.2, 0.3, 0.0]),
)
RigidPrim("/World/Cube")
GeomPrim("/World/Cube", apply_collision_apis=True)
```

#### Using the Python API

You can add an IMU to the cube prim created above using `IMU.create()` and then wrap it with `IMUSensor` for runtime data access, as demonstrated in the following snippet. The path must include the parent prim path; the remaining arguments are optional.

```python
import numpy as np
from isaacsim.sensors.experimental.physics import IMU, IMUSensor

sensor = IMUSensor(
    IMU.create(
        "/World/Cube/imu_sensor",
        linear_acceleration_filter_size=10,
        angular_velocity_filter_size=10,
        orientation_filter_size=10,
        translations=np.array([[0.0, 0.0, 0.0]]),
        orientations=np.array([[1.0, 0.0, 0.0, 0.0]]),
    )
)
```

#### Using the Python wrapper

You can also add an IMU to the cube prim, created above, by constructing an `IMU` authoring object directly and wrapping it with `IMUSensor` for runtime data access, as demonstrated in the following snippet. The `IMU` constructor wraps an existing sensor prim or creates a new one with default attributes; the `IMUSensor` runtime then exposes `get_sensor_reading()` and `get_data()` for reading sensor output. Modify USD attributes (e.g., filter widths) via the authoring object reachable as `sensor.imu` after construction.

```python
import numpy as np
from isaacsim.sensors.experimental.physics import IMU, IMUSensor

IMUSensor(
    IMU(
        "/World/Cube/Imu",
        translations=np.array([[0.0, 0.0, 0.0]]),  # or, positions=np.array([[0.0, 0.0, 0.0]]),
        orientations=np.array([[1.0, 0.0, 0.0, 0.0]]),
        linear_acceleration_filter_size=10,
        angular_velocity_filter_size=10,
        orientation_filter_size=10,
    )
)
```

Note

`translations` and `positions` cannot both be provided as input arguments — they are mutually exclusive (local-frame vs world-frame).
The `IMUSensor` Python API documentation specifies the usage of each input argument.

To set filter widths at construction time, pass them to `IMU.create()` (or `IMU(path, ...)`) — see the snippet above. To modify them after construction, set the underlying USD attributes (`linearAccelerationFilterWidth`, `angularVelocityFilterWidth`, `orientationFilterWidth`) on the sensor prim — the prim is reachable as `sensor.imu.prims[0]`. Filter widths are captured by the C++ runtime when the sensor is created at simulation start; stop and restart the simulation to pick up changes. The `IMUSensor` reads every physics step.

### Reading sensor output

The sensors are created dynamically on **Play**. Moving the sensor prim while the simulation is running invalidates the sensor. If you need to make hierarchical changes to the IMU, such as changing its rigid body parent, stop the simulator, make the changes, and then restart the simulation.

There are three methods for reading the sensor output:

* `IMUSensor.get_sensor_reading(read_gravity=True)` — returns the raw C++ struct directly
* `IMUSensor.get_data(read_gravity=True)` — returns a structured dictionary
* OmniGraph node `Isaac Read IMU Node`

The following snippets assume you have created a `/World/Cube` prim and IMU sensor prim using one of the two snippets [above](#isaacsim-sensors-physics-imu-standalone-python-create-modify).

**IMUSensor.get\_sensor\_reading(read\_gravity=True)**

Returns an `ImuSensorReading` C++ struct exposing `is_valid`, `time`, `linear_acceleration_x`/`_y`/`_z`, `angular_velocity_x`/`_y`/`_z`, and `orientation_w`/`_x`/`_y`/`_z` properties. The sensor reads the C++ backend every physics step; pass `read_gravity=False` to exclude gravitational acceleration.

Sample usage to get the reading from the current physics step with gravitational effects:

```python
from isaacsim.sensors.experimental.physics import IMUSensor

sensor = IMUSensor("/World/Cube/Imu")
sensor.get_sensor_reading(read_gravity=True)
```

Sample usage without gravitational effects:

```python
from isaacsim.sensors.experimental.physics import IMUSensor

sensor = IMUSensor("/World/Cube/Imu")
sensor.get_sensor_reading(read_gravity=False)
```

**IMUSensor.get\_data(read\_gravity=True)**

The `get_data()` member function on the `IMUSensor` runtime class wraps `get_sensor_reading()` and returns a dictionary with `time`, `physics_step`, `linear_acceleration` (`np.ndarray` shape `(3,)`), `angular_velocity` (`np.ndarray` shape `(3,)`), and `orientation` (`np.ndarray` shape `(4,)`, `wxyz`).

Sample usage:

```python
import numpy as np
from isaacsim.sensors.experimental.physics import IMU, IMUSensor

sensor = IMUSensor(
    IMU(
        "/World/Cube/Imu",
        translations=np.array([[0.0, 0.0, 0.0]]),
        orientations=np.array([[1.0, 0.0, 0.0, 0.0]]),
        linear_acceleration_filter_size=10,
        angular_velocity_filter_size=10,
        orientation_filter_size=10,
    )
)

value = sensor.get_data()
print(value)
```

### API documentation

Deprecated since version 6.0: The `isaacsim.sensors.physics` extension is deprecated. Use `isaacsim.sensors.experimental.physics.IMUSensor` instead.

See the [isaacsim.sensors.experimental.physics API Documentation](../py/source/extensions/isaacsim.sensors.experimental.physics/docs/index.html) for the current API and [isaacsim.sensors.physics API Documentation (deprecated)](../py/source/extensions/isaacsim.sensors.physics/docs/index.html) for the deprecated API.

On this page

* [GUI](#gui)
  + [Creating and modifying the IMU](#creating-and-modifying-the-imu)
  + [IMU Example](#imu-example)
  + [OmniGraph workflow](#omnigraph-workflow)
    - [Scene setup](#scene-setup)
    - [OmniGraph setup](#omnigraph-setup)
* [Standalone Python](#standalone-python)
  + [Creating and modifying the IMU](#isaacsim-sensors-physics-imu-standalone-python-create-modify)
    - [Using the Python API](#using-the-python-api)
    - [Using the Python wrapper](#using-the-python-wrapper)
  + [Reading sensor output](#reading-sensor-output)
  + [API documentation](#api-documentation)

---

### Joint State

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/sensors/isaacsim_sensors_physics_joint_state.html

* [Sensors](index.html)
* [Physics-based sensors](isaacsim_sensors_physics.html)
* Joint state sensor

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Joint state sensor

The joint state sensor reads the full per-DOF state of an articulation in a single call: positions, velocities, and efforts for every degree of freedom, plus the DOF names and per-DOF type (revolute or prismatic). It is analogous to a ROS 2 `JointState` message and is backed by the C++ `IJointStateSensor` Carbonite interface in the `isaacsim.sensors.experimental.physics` extension.

Unlike the per-joint [Effort Sensor](isaacsim_sensors_physics_effort.html#isaacsim-sensors-physics-effort), a single joint state sensor returns data for the entire articulation. The sensor is attached to the articulation root prim, not to an individual joint.

See the [Isaac Sim Conventions](../reference_material/reference_conventions.html#isaac-sim-conventions) documentation for a complete list of Isaac Sim conventions.

**Joint state sensor properties**

1. `enabled` instance attribute determines whether the sensor returns data. When `False`, `get_sensor_reading()` and `get_data()` return invalid readings without touching the C++ backend.
2. The sensor binds to a single articulation root path provided at construction time. To re-target the sensor to a different articulation, construct a new `JointStateSensor`.

The `JointStateSensor` reads every physics step.

## Standalone Python

### Creating the joint state sensor

The following snippet adds a Simple Articulation reference and creates a `JointStateSensor` bound to the articulation root. The articulation must already be in the stage when the sensor is constructed.

```python
from isaacsim.sensors.experimental.physics import JointStateSensor

sensor = JointStateSensor(path="/World/simple_articulation", enabled=True)
```

Note

The articulation root prim you pass in **is** the sensor’s prim — `JointStateSensor` does not author a separate USD prim in the **Stage** panel on construction. DOF readings become available via `get_sensor_reading()` once the simulation is playing; check `reading.is_valid` after pressing **Play** to confirm the sensor is active.

### Reading sensor output

The sensor is created dynamically on **Play**. Moving or replacing the articulation root prim while the simulation is running invalidates the sensor; stop the simulator, make the changes, and restart.

There are two methods for reading the sensor output:

* `JointStateSensor.get_sensor_reading()` — returns a `JointStateSensorReading` object with the per-DOF arrays as attributes.
* `JointStateSensor.get_data()` — returns a structured dictionary with the same data plus `physics_step`, suitable for direct serialization.

**JointStateSensor.get\_sensor\_reading()**

Returns a `JointStateSensorReading` exposing `is_valid`, `time`, `dof_names` (`list[str]`), `positions` / `velocities` / `efforts` (`np.ndarray` of length `dof_count`), `dof_types` (`np.ndarray` of `uint8`: `0 = revolute`, `1 = prismatic`), and `stage_meters_per_unit`.

```python
reading = sensor.get_sensor_reading()
if reading.is_valid:
    for name, pos, vel, eff in zip(reading.dof_names, reading.positions, reading.velocities, reading.efforts):
        print(f"{name}: pos={pos:.4f} vel={vel:.4f} eff={eff:.4f}")
```

**JointStateSensor.get\_data()**

Returns a dictionary with keys `dof_names`, `positions`, `velocities`, `efforts`, `dof_types`, `stage_meters_per_unit`, `is_valid`, `time`, and `physics_step`. The numpy arrays in this dict are the same objects exposed by `get_sensor_reading()`; the dict form simply makes the data easier to log, plot, or pass to downstream consumers.

```python
frame = sensor.get_data()
if frame["is_valid"]:
    print(f"DOFs: {frame['dof_names']}")
    print(f"Positions: {frame['positions']}")
    print(f"Velocities: {frame['velocities']}")
    print(f"Efforts: {frame['efforts']}")
    print(f"Time: {frame['time']}, physics step: {frame['physics_step']}")
```

## API documentation

See the [isaacsim.sensors.experimental.physics API Documentation](../py/source/extensions/isaacsim.sensors.experimental.physics/docs/index.html) for the full `JointStateSensor` API.

On this page

* [Standalone Python](#standalone-python)
  + [Creating the joint state sensor](#creating-the-joint-state-sensor)
  + [Reading sensor output](#reading-sensor-output)
* [API documentation](#api-documentation)

---

### Raycast Sensor

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/sensors/isaacsim_sensors_physics_raycast.html

* [Sensors](index.html)
* [Physics-based sensors](isaacsim_sensors_physics.html)
* Physics raycast sensor

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Physics raycast sensor

The physics raycast sensor uses physics raycasts to measure distances between a sensor prim and surrounding geometry.
Unlike the fixed-pattern sensors in Isaac Sim, the physics raycast sensor accepts explicit per-ray origin offsets, direction vectors, and optional time offsets, making it suitable for a wide range of configurations, including solid-state sensors, rotating sensors, and beam curtains.

Each physics step, the sensor casts rays from the prim’s world-space position (plus per-ray origin offsets) along the specified directions.
When `rayTimeOffsets` are provided, only the subset of rays whose time offsets fall within the current physics step’s time window are fired, producing a sweeping pattern over multiple steps.

See the [Isaac Sim Conventions](../reference_material/reference_conventions.html#isaac-sim-conventions) documentation for a complete list of Isaac Sim conventions.

**Physics raycast sensor properties**

1. `enabled` parameter determines if the sensor is running or not.
2. `numRays` (unsigned int) parameter specifies the authoritative ray count. `rayOrigins` and `rayDirections` must each have exactly this many elements. This is set automatically when using `Raycast.create()` or the `Raycast` authoring constructor.
3. `minRange` parameter specifies the minimum detection range in stage length units. Rays start at `origin + direction * minRange`.
4. `maxRange` parameter specifies the maximum detection range in stage length units.
5. `rayOrigins` parameter specifies per-ray origin translations in the sensor’s local coordinate frame.
6. `rayDirections` parameter specifies per-ray cast direction vectors in the sensor’s local coordinate frame. Vectors are normalized before use.
7. `rayTimeOffsets` parameter specifies per-ray time offsets in seconds. When provided, the sensor fires only rays whose offsets fall within the current physics step, enabling sweeping patterns. The sweep period is `max(rayTimeOffsets)`.
8. `outputFrameOfReference` parameter selects the coordinate frame for hit positions and normals. `SENSOR` returns results in the sensor’s local coordinate frame; `WORLD` returns results in world coordinates.
9. `reportHitPrimPaths` parameter enables resolving the USD prim path of each hit surface.

For the full USD attribute definitions, see the [Raycast Sensor schema reference](../omniverse_usd/sensor_schema.html#isaac-sim-sensor-schema-raycast).

Note

All sensor properties are read once when the simulation starts. Changing attribute values while the simulation is playing has no effect; stop and restart the simulation to pick up changes.

## GUI

### Creating a physics raycast sensor

To create a physics raycast sensor from the GUI:

1. To create a Physics Scene, go to the top Menu Bar and click **Create > Physics > Physics Scene**. Verify that there is now a `PhysicsScene` [Prim](../reference_material/reference_glossary.html#isaac-sim-glossary-prim) in the [Stage](../reference_material/reference_glossary.html#isaac-sim-glossary-stage) panel on the right.
2. Optionally select a parent prim in the **Stage** panel.
3. Go to the top Menu Bar and click **Create > Sensors > Physics Raycast Sensor** and choose one of the preset configurations:

   * **Solid State Physics Raycast Sensor**: A rectangular grid of rays with configurable horizontal and vertical field of view.
   * **Rotating Physics Raycast Sensor**: Rays distributed across 360 degrees with time offsets that produce a sweeping pattern at 1 Hz.
   * **Beam Curtain Physics Raycast Sensor**: Parallel rays spread vertically for proximity detection.
4. To change the position and orientation of the sensor, select the sensor prim and modify the **Transform** properties under the **Property** tab.
5. To change sensor properties, expand the **Raw USD Properties** section to modify range, ray geometry, and output frame settings.

### Physics raycast sensor example

To run the physics raycast sensor example:

1. Activate **Robotics Examples** tab from **Windows** > **Examples** > **Robotics Examples**.
2. Click **Robotics Examples** > **Sensors** > **Physics Raycast Sensor** > **Load Scene**.
3. Verify that three physics raycast sensors are created: a solid state sensor (green rays), a rotating sensor (blue rays), and a beam curtain sensor (red rays).
4. Press the **Play** button to begin simulating.
5. Observe the debug ray visualization in the viewport and the hit count / min depth readings in the example window.

### OmniGraph workflow

The following is a tutorial on using OmniGraph to read and visualize physics raycast sensor data.

#### Scene setup

1. Create a Physics Scene by **Create > Physics > Physics Scene**.
2. Add collision geometry (e.g., **Create > Mesh > Cube** and apply **Add > Physics > Colliders Preset**).
3. Add a ground plane by **Create > Physics > GroundPlane**.
4. Create a physics raycast sensor by **Create > Sensors > Physics Raycast Sensor > Solid State Physics Raycast Sensor**.

#### OmniGraph setup

To set up the OmniGraph to collect readings from this sensor:

1. Create a new action graph by navigating to **Window > Graph Editors > Action Graph**, and selecting **New Action Graph** in the new tab that opens.
2. Add the following nodes to the graph:

   * **On Playback Tick** (`omni.graph.action.OnPlaybackTick`): Executes the graph every simulation timestep.
   * **Isaac Read Physics Raycast Sensor** (`isaacsim.sensors.physics.IsaacReadRaycastSensor`): Reads the physics raycast sensor. In the **Property** tab, set `Physics Raycast Sensor Prim` to the path of your sensor prim (e.g., `/World/Sensors/Solid_State_Physics_Raycast_Sensor`).
   * **Debug Draw RayCast** (`isaacsim.util.debug_draw.DebugDrawRayCast`): Visualizes the rays in the viewport.
3. Configure the **Debug Draw RayCast** node:

   * Set `inputs:doTransform` to **False**. The read node already provides world-space beam origins and endpoints; applying an additional transform will produce incorrect visualization.
4. Connect the nodes with **all five** required connections:

   * **On Playback Tick** `outputs:tick` â **Isaac Read Physics Raycast Sensor** `inputs:execIn`
   * **Isaac Read Physics Raycast Sensor** `outputs:execOut` â **Debug Draw RayCast** `inputs:exec`
   * **Isaac Read Physics Raycast Sensor** `outputs:beamOrigins` â **Debug Draw RayCast** `inputs:beamOrigins`
   * **Isaac Read Physics Raycast Sensor** `outputs:beamEndPoints` â **Debug Draw RayCast** `inputs:beamEndPoints`
   * **Isaac Read Physics Raycast Sensor** `outputs:numRays` â **Debug Draw RayCast** `inputs:numRays`

   Important

   The `numRays` connection is required. Without it, the Debug Draw node defaults to 0 rays and renders nothing. Similarly, `doTransform` must be set to False because the beam origins and endpoints from the read node are already in world coordinates.
5. Press the **Play** button. If set up correctly, ray lines appear from the sensor to hit points in the viewport.

#### Programmatic OmniGraph setup

The same graph can be created programmatically using `og.Controller`:

```python
# Programmatic OmniGraph setup: Physics Raycast Sensor + Debug Draw visualization
import omni.graph.core as og

sensor_prim_path = "/World/Sensors/Solid_State_Physics_Raycast_Sensor"

action_graph, _, _, _ = og.Controller.edit(
    {"graph_path": "/World/ActionGraph", "evaluator_name": "execution"},
    {
        og.Controller.Keys.CREATE_NODES: [
            ("OnPlaybackTick", "omni.graph.action.OnPlaybackTick"),
            ("ReadRaycast", "isaacsim.sensors.physics.IsaacReadRaycastSensor"),
            ("DebugDraw", "isaacsim.util.debug_draw.DebugDrawRayCast"),
        ],
        og.Controller.Keys.SET_VALUES: [
            ("ReadRaycast.inputs:raycastSensorPrim", sensor_prim_path),
            ("DebugDraw.inputs:doTransform", False),
        ],
        og.Controller.Keys.CONNECT: [
            ("OnPlaybackTick.outputs:tick", "ReadRaycast.inputs:execIn"),
            ("ReadRaycast.outputs:execOut", "DebugDraw.inputs:exec"),
            ("ReadRaycast.outputs:beamOrigins", "DebugDraw.inputs:beamOrigins"),
            ("ReadRaycast.outputs:beamEndPoints", "DebugDraw.inputs:beamEndPoints"),
            ("ReadRaycast.outputs:numRays", "DebugDraw.inputs:numRays"),
        ],
    },
)
```

Note

Key differences from a naive setup that may cause visualization to fail:

* **``doTransform`` must be False**: The read node outputs world-space coordinates. The Debug Draw node’s `doTransform` input applies an additional matrix transform by default, which displaces the rays to incorrect positions.
* **``numRays`` must be connected**: Without this, the draw node doesn’t know how many rays to render and defaults to zero.
* **Execution chain must be complete**: `execIn` â `execOut` â `exec` ensures the draw node fires after the read node has populated its outputs.

## Standalone Python

### Creating a physics raycast sensor

For the example snippets below, prepare the scene using the following snippet by adding a `PhysicsScene`, collision geometry, and a sensor parent `Xform`.

```python
import omni.usd
from pxr import Gf, Sdf, UsdGeom, UsdPhysics

stage = omni.usd.get_context().get_stage()

UsdGeom.SetStageUpAxis(stage, UsdGeom.Tokens.z)
UsdGeom.SetStageMetersPerUnit(stage, 1.0)

UsdPhysics.Scene.Define(stage, Sdf.Path("/World/PhysicsScene"))

ground = UsdGeom.Cube.Define(stage, "/World/GroundPlane")
ground.GetSizeAttr().Set(1.0)
ground.AddTranslateOp().Set(Gf.Vec3d(0, 0, -0.05))
ground.AddScaleOp().Set(Gf.Vec3f(50, 50, 0.1))
UsdPhysics.CollisionAPI.Apply(ground.GetPrim())

wall = UsdGeom.Cube.Define(stage, "/World/Obstacles/Wall")
wall.GetSizeAttr().Set(1.0)
wall.AddTranslateOp().Set(Gf.Vec3d(5, 0, 1.5))
wall.AddScaleOp().Set(Gf.Vec3f(0.2, 8, 3))
UsdPhysics.CollisionAPI.Apply(wall.GetPrim())

UsdGeom.Xform.Define(stage, "/World/Sensors")
```

#### Using the Python API

Physics raycast sensors are created with `Raycast.create()` (the authoring class) and the returned authoring object is wrapped with `RaycastSensor` for runtime data access. You must provide `ray_origins` and `ray_directions` arrays of the same length. The path must include the parent prim path.

```python
import math

from isaacsim.sensors.experimental.physics import Raycast, RaycastSensor

# Generate a simple grid of ray directions for a solid state physics raycast sensor.
h_count, v_count = 10, 5
h_fov, v_fov = 60.0, 20.0
origins = []
directions = []
for vi in range(v_count):
    v_angle = math.radians(-v_fov / 2 + v_fov * vi / max(v_count - 1, 1))
    for hi in range(h_count):
        h_angle = math.radians(-h_fov / 2 + h_fov * hi / max(h_count - 1, 1))
        dx = math.cos(v_angle) * math.cos(h_angle)
        dy = math.cos(v_angle) * math.sin(h_angle)
        dz = math.sin(v_angle)
        origins.append([0.0, 0.0, 0.0])
        directions.append([dx, dy, dz])

sensor = RaycastSensor(
    Raycast.create(
        "/World/Sensors/Physics_Raycast_Sensor",
        min_range=0.4,
        max_range=100.0,
        ray_origins=origins,
        ray_directions=directions,
        output_frame="WORLD",
        translations=[[0.0, 0.0, 1.5]],
    )
)
```

#### Using time offsets

To create a sensor with a sweeping pattern, provide `ray_time_offsets`. Rays are only fired when their time offset falls within the current physics step’s time window. The sweep period equals `max(ray_time_offsets)`.

```python
import math

from isaacsim.sensors.experimental.physics import Raycast, RaycastSensor

# Generate rays for a rotating physics raycast sensor with time offsets.
# Each azimuthal column is assigned a time offset within the sweep period.
# Only rays whose offsets fall in the current physics step are fired.
v_count = 8
azimuth_steps = 36
v_fov = 30.0
rotation_rate = 1.0
period = 1.0 / rotation_rate

origins = []
directions = []
time_offsets = []
for ai in range(azimuth_steps):
    h_angle = math.radians(360.0 * ai / azimuth_steps)
    t_offset = period * ai / azimuth_steps
    for vi in range(v_count):
        v_angle = math.radians(-v_fov / 2 + v_fov * vi / max(v_count - 1, 1))
        dx = math.cos(v_angle) * math.cos(h_angle)
        dy = math.cos(v_angle) * math.sin(h_angle)
        dz = math.sin(v_angle)
        origins.append([0.0, 0.0, 0.0])
        directions.append([dx, dy, dz])
        time_offsets.append(t_offset)

sensor = RaycastSensor(
    Raycast.create(
        "/World/Sensors/Rotating_Physics_Raycast_Sensor",
        min_range=0.4,
        max_range=100.0,
        ray_origins=origins,
        ray_directions=directions,
        ray_time_offsets=time_offsets,
        output_frame="WORLD",
        translations=[[0.0, 0.0, 1.5]],
    )
)
```

### Using the RaycastSensor runtime

The `RaycastSensor` class wraps an existing `Raycast` authoring object or an existing `IsaacRaycastSensor` prim for runtime data access. Configure and create new prims with `Raycast.create()`.

```python
from isaacsim.sensors.experimental.physics import Raycast, RaycastSensor

sensor = RaycastSensor(
    Raycast.create(
        "/World/Sensors/My_Sensor",
        ray_origins=[[0, 0, 0], [0, 0, 0]],
        ray_directions=[[1, 0, 0], [0, 1, 0]],
        min_range=0.4,
        max_range=100.0,
        output_frame="WORLD",
    )
)

# After simulation starts:
frame = sensor.get_data()
print(f"Depths: {frame['depths']}")
print(f"Hit positions: {frame['hit_positions']}")
```

### Reading sensor output

The physics raycast sensor is created dynamically on **Play**. Use `RaycastSensor.get_sensor_reading()` to read raw sensor data, or `RaycastSensor.get_data()` for a structured dictionary. The reading includes depths, hit positions, hit normals, and optionally hit prim paths.

The following snippet assumes you have created a sensor prim using one of the snippets [above](#isaacsim-sensors-physics-raycast-standalone-python-create-modify).

```python
from isaacsim.sensors.experimental.physics import Raycast, RaycastSensor

sensor = RaycastSensor(
    Raycast.create(
        "/World/Sensors/Physics_Raycast_Sensor",
        ray_origins=[[0.0, 0.0, 0.0]],
        ray_directions=[[1.0, 0.0, 0.0]],
    )
)
reading = sensor.get_sensor_reading()

if reading.is_valid:
    print(f"Ray count: {reading.ray_count}")
    print(f"Depths: {reading.depths}")
    print(f"Hit positions: {reading.hit_positions}")
    print(f"Hit normals: {reading.hit_normals}")
```

The `get_sensor_reading()` function returns a `RaycastSensorReading` object with the following properties:

* `is_valid`: Whether the reading contains valid data.
* `ray_count`: Number of rays in the reading.
* `time`: Simulation time of this reading in seconds.
* `depths`: Per-ray hit distances in stage length units. Rays that miss return `maxRange`.
* `hit_positions`: Per-ray hit positions as an Nx3 array, in the frame specified by `outputFrameOfReference`.
* `hit_normals`: Per-ray surface normals at hit points as an Nx3 array.
* `hit_prim_paths`: Per-ray USD prim paths of hit surfaces (only populated when `reportHitPrimPaths` is enabled).
* `ray_origins_world`: Per-ray world-space origins as an Nx3 array.
* `ray_end_points_world`: Per-ray world-space end points as an Nx3 array (useful for debug visualization).

The `get_data()` function returns a structured dictionary with `depths`, `hit_positions`, `hit_normals`, `hit_prim_paths`, `time`, and `physics_step`. `ray_origins_world` and `ray_end_points_world` are only available on the raw `get_sensor_reading()` result.

### API documentation

See the [API Documentation](../py/source/extensions/isaacsim.sensors.experimental.physics/docs/index.html) for complete usage information.

On this page

* [GUI](#gui)
  + [Creating a physics raycast sensor](#creating-a-physics-raycast-sensor)
  + [Physics raycast sensor example](#physics-raycast-sensor-example)
  + [OmniGraph workflow](#omnigraph-workflow)
    - [Scene setup](#scene-setup)
    - [OmniGraph setup](#omnigraph-setup)
    - [Programmatic OmniGraph setup](#programmatic-omnigraph-setup)
* [Standalone Python](#standalone-python)
  + [Creating a physics raycast sensor](#isaacsim-sensors-physics-raycast-standalone-python-create-modify)
    - [Using the Python API](#using-the-python-api)
    - [Using time offsets](#using-time-offsets)
  + [Using the RaycastSensor runtime](#using-the-raycastsensor-runtime)
  + [Reading sensor output](#reading-sensor-output)
  + [API documentation](#api-documentation)

---

### PhysX Sensors Index

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/sensors/isaacsim_sensors_physx.html

* [Sensors](index.html)
* PhysX SDK sensors

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# PhysX SDK sensors

Isaac Sim’s PhysX SDK sensors use raycasts provided by the [PhysX SDK](https://nvidia-omniverse.github.io/PhysX/physx/5.3.0/) to measure the range between
objects in the simulation.

These sensors output the exact measurements from PhysX SDK. By default, the highest rate that the sensors can output data is the render rate.

The PhysX SDK sensors are organized in the `isaacsim.sensors.physx` extension.

Deprecated since version 6.0: The `isaacsim.sensors.physx` extension is deprecated. Use `isaacsim.sensors.experimental.physics` instead,
which provides the `RaycastSensor` as the replacement for PhysX-based range sensors.
See the [API Documentation](../py/source/extensions/isaacsim.sensors.experimental.physics/docs/index.html) for the replacement APIs.
See individual sensor pages below for specific migration guidance.

Isaac Sim supports the following PhysX SDK sensors:

* [PhysX SDK generic sensor](isaacsim_sensors_physx_generic.html)
* [PhysX SDK lidar](isaacsim_sensors_physx_lidar.html)
* [PhysX SDK lightbeam sensor](isaacsim_sensors_physx_lightbeam.html)
* [Proximity sensor](isaacsim_sensors_physx_proximity.html)

---

### PhysX Generic

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/sensors/isaacsim_sensors_physx_generic.html

* [Sensors](index.html)
* [PhysX SDK sensors](isaacsim_sensors_physx.html)
* PhysX SDK generic sensor

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# PhysX SDK generic sensor

Deprecated since version 6.0: The PhysX SDK sensor extensions (`isaacsim.sensors.physx`) are deprecated. Use
`isaacsim.sensors.experimental.physics.RaycastSensor` as the replacement.
See [PhysX Generic Sensor](../migration_guides/isaac_sim_6_0/sensors_physx_generic_to_physics_raycast.html#isaacsim-sensors-physx-generic-migration) for step-by-step migration instructions, or the [isaacsim.sensors.experimental.physics API Documentation](../py/source/extensions/isaacsim.sensors.experimental.physics/docs/index.html) for the replacement APIs.

The PhysX SDK generic sensor in Isaac Sim uses PhysX SDK raycasts to measure depth between two prims. It demonstrates
how to build a PhysX SDK-based sensor in Isaac Sim to measure ground truth depth.

See the [Isaac Sim Conventions](../reference_material/reference_conventions.html#isaac-sim-conventions) documentation for a complete list of Isaac Sim conventions.

## GUI

### PhysX SDK generic sensor example

To run the PhysX SDK generic sensor example:

1. Activate **Robotics Examples** tab from **Windows** > **Examples** > **Robotics Examples**.
2. Click **Robotics Examples** > **Sensors** > **Custom Pattern Range Sensor**.
3. Press the **Load Sensor** button.
4. Press the **Load Scene** button.
5. Press the **Set Sensor Pattern** button to load the example sensor pattern.
6. Press the **Open Source Code** button to view the source code. The source code illustrates how to create, add, and control the sensor using the Python API.
7. Press the **Play** button to begin simulating.

1. To visualize the pattern, save the image imprinted on the wall from the rays that hit it. Select or type the desired output directory and press **Save Pattern Image**. Open the saved image file and verify that you have a zigzag pattern.

### Script Editor

The following sections describe how to customize the PhysX SDK generic sensor through the **Script Editor**, opened from **Window > Script Editor**.

**Customizing scanning pattern**

To customize scanning patterns, fill or modify these parameters:

* **streaming:** Set to `True` if streaming data continuously, `False` if sending a batch of data once in the beginning and repeating it.
* **sampling\_rate:** Number of scans per second.
* **batch\_size:** The number of scans each batch of data contains. The size must be large enough to run a few rendering frames without running out. For example, if you scan at 2400 scans per second and render at 120 fps, each frame renders 20 scans. If you send a batch size of 12000, you can render 600 frames, or five seconds at 120 fps, before you run out of data. If `batch_size` is less than `sampling_rate/fps`, the sensor scans at a rate that equals `batch_size` per frame, which likely means you scan slower than desired.
* **sensor\_pattern:** An Nx2 NumPy array. N is `batch_size`, and the columns are [azimuth, zenith] angles of each scanning ray. Azimuth is the ray’s horizontal angle measured from the x-axis, and zenith angle is the vertical angle measured from the z-axis.
* **origin\_offsets:** Optional Nx3 NumPy array. N is the batch size, and each row is the individual ray’s offset from origin in [x, y, z] coordinates.

**Example scanning patterns**

Review the example code to see how to produce the zigzag scanning pattern.
The pattern in the example is generated programmatically inside the same script that runs the example. Click on the **Open Source Code** icon in the upper right-hand corner of the example window and open the Python source code for this example.

There are two test patterns in the script, one for testing continuous streaming data mode, the other one for testing a repeating pattern mode.

**Streaming generated pattern**

The pattern is sweeping horizontally 10 times for each round of up and down, resulting in the zigzag.

```python
def _test_streaming_data(self):
    batch_size = int(1e6)
    half_batch = int(batch_size / 2)
    frequency = 10
    N_pts = int(batch_size / frequency / 2)
    azimuth = np.tile(
        np.append(np.linspace(-np.pi / 4, np.pi / 4, N_pts), np.linspace(np.pi / 4, -np.pi / 4, N_pts)), frequency
    )
    zenith = np.append(np.linspace(-np.pi / 4, np.pi / 4, half_batch), np.linspace(np.pi / 4, -np.pi / 4, half_batch))
    self.sensor_pattern = np.stack((azimuth, zenith))
```

Origin offset is optional. For the example, a small random offset was added, as seen below. For no offsets, you can either use an array of zeros or skip setting the `origin_offsets` parameter.

```python
import numpy as np

# individual rays can have an offset at the origin
# adding random offsets to the origin for the example pattern
self.origin_offsets = 5 * np.random.random((batch_size, 3))
# self.origin_offsets = np.zeros((batch_size,3))                  # no offsets
```

**Streaming pattern through file**

If you do not have a programmatic way to generate the scanning pattern from scratch, or if you do not want to disclose the generation method of the scanning pattern, you can also import data from the file. The example below shows importing data from a `.csv` file and converting it to match the format of the **sensor\_pattern** parameter.

```python
import numpy as np

## import data from file
sensor_pattern = np.loadtxt("filename.csv", delimiter=",")
batch_size = np.shape(sensor_pattern)[0]
sensor_pattern = np.deg2rad(sensor_pattern).T.copy()  ##  MUST USE .copy()
```

**Repeating pattern**

To better visualize the repetitiveness of the pattern, you use a zigzag motion, but this time instead a smooth movement going up and down, it is split into two modes, one set scanning high and the other set scanning low. If correctly executed, verify that it repeats itself without any additional data being pulled in.

To change the example to run in non-streaming mode, set `self._streaming = False` and save the change. Verify that it then automatically uses the following code to generate the pattern. Wait for the example to restart and reload before trying to run it.

```python
def _test_repeating_data(self):

    batch_size = int(1e6)
    half_batch = int(batch_size / 2)
    frequency = 10
    N_pts = int(batch_size / frequency / 2)
    azimuth = np.tile(
        np.append(np.linspace(-np.pi / 4, np.pi / 4, N_pts), np.linspace(np.pi / 4, -np.pi / 4, N_pts)), frequency
    )
    zenith = np.append(-0.5 * np.ones(half_batch), 0.5 * np.ones(half_batch))
    sensor_pattern = np.stack((azimuth, zenith))

    origin_offsets = 0.05 * np.random.random((batch_size, 3))
```

**Setting scanning pattern**

When the sensor processes each batch of `[azimuth, zenith]` pairs and is about to run out of data, it sets `send_next_batch()` to `True`. You can then send the next batch through `set_next_batch_rays(prim_path, sensor_pattern)`, plus `set_next_batch_offsets(prim_path, sensor_pattern)` if there are origin offsets, as shown below.

```python
def _on_editor_step(self, step):
    if not self._timeline.is_playing():
        return

    if self._timeline.is_playing():
        if self._generic:
            if self._pattern_set:
                if self._sensor.send_next_batch(
                    self._genericPath
                ):  # send_next_batch will turn True if the sensor is running out data and needs more
                    self._sensor.set_next_batch_rays(
                        self._genericPath, self.sensor_pattern
                    )  # set the next batch data using set_next_batch_rays()
                    self._sensor.set_next_batch_offsets(
                        self._genericPath, self.origin_offsets
                    )  # (Optional) add individual ray offsets if there are any
```

On this page

* [GUI](#gui)
  + [PhysX SDK generic sensor example](#physx-generic-sensor-example)
  + [Script Editor](#script-editor)

---

### PhysX Lidar

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/sensors/isaacsim_sensors_physx_lidar.html

* [Sensors](index.html)
* [PhysX SDK sensors](isaacsim_sensors_physx.html)
* PhysX SDK lidar

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# PhysX SDK lidar

Deprecated since version 6.0: The PhysX SDK Lidar sensor (`isaacsim.sensors.physx`) is deprecated. Use
`isaacsim.sensors.experimental.physics.RaycastSensor` as the replacement, which provides
configurable raycast-based sensing.
See [PhysX Lidar](../migration_guides/isaac_sim_6_0/sensors_physx_lidar_to_physics_raycast.html#isaacsim-sensors-physx-lidar-migration) for step-by-step migration instructions, or the [isaacsim.sensors.experimental.physics API Documentation](../py/source/extensions/isaacsim.sensors.experimental.physics/docs/index.html) for the replacement APIs.

The PhysX SDK lidar sensor in Isaac Sim uses PhysX SDK raycasts to simulate a Lidar.
You can set horizontal and vertical beam resolution, rotation rate, and other Lidar parameters; the
PhysX SDK lidar then reports depth information from each beam. The PhysX SDK lidar cannot interact with
non-visual materials, and it always reports ground truth information. For example, the Lidar measures depth
of a transparent object with respect to the Lidar, even if a beam would normally pass through the transparent
object in real life.

See the [Isaac Sim Conventions](../reference_material/reference_conventions.html#isaac-sim-conventions) documentation for a complete list of Isaac Sim conventions.

## GUI

### PhysX SDK lidar sensor example

To run the example:

1. Activate `Robotics Examples` tab from **Windows** > **Examples** > **Robotics Examples**.
2. Click **Robotics Examples** > **Sensors** > **Physx Lidar Sensor**.
3. Press the **Load Sensor** button.
4. Press the **Load Scene** button.
5. Press the **Open Source Code** button to view the source code. The source code illustrates how to add and control the sensor using the Python API.
6. Press the **Play** button to begin simulating.

### Adding a PhysX SDK lidar sensor to a simulation

#### Scene setup

Begin setting up the scene by creating a `PhysicsScene` and a `PhysX Lidar` in the environment:

1. To create a Physics Scene, go to the top Menu Bar and click **Create > Physics > Physics Scene**. Verify that there is now a `PhysicsScene` [Prim](../reference_material/reference_glossary.html#isaac-sim-glossary-prim) in the [Stage](../reference_material/reference_glossary.html#isaac-sim-glossary-stage) panel on the right.
2. To create a Lidar, go to the top Menu Bar and click **Create > Sensors > PhysX Lidar > Rotating**.
   Next, set the Lidar properties for rotation and visualization:
3. Select the newly created Lidar prim from the [Stage](../reference_material/reference_glossary.html#isaac-sim-glossary-stage) panel.
4. After selecting it, the **Property** panel in the lower left populates with all available Lidar properties.
5. Scroll down in the **Property** panel to the **Raw USD Properties** section.
6. Enable the **drawLines** checkbox to enable line rendering.
7. Set the revolutions per second to `1 Hz` by setting `rotationRate` to `1.0`.

   * To fire LIDAR rays in all directions at once, set the `rotationRate` to `0.0`.

Note

You can update all of the Lidar parameters on the fly while the stage is running.
When the rotation rate reaches zero or less, the Lidar prim casts rays in all directions based on your FOV and resolution.

#### Set up collision detection

The Lidar can only detect objects with **Collisions Enabled**. Add an object for the Lidar to detect:

1. Go to the top Menu Bar and click **Create > Mesh > Cube**.
2. Translate the cube to `(2, 0, 0)`.

Next, add a Physics Collider to the Cube:

1. With the Cube selected, go to the **Property** panel and click the **+ Add** button.
2. Select **+ Add > Physics > Collider**.

* Use the mouse to move the Cube around the scene and see how the Lidar rays interact with the geometry.

#### Attach a Lidar to geometry

For most use cases, attach Lidars to more complex assemblies, such as cars or robots.
Use a Cylinder as a placeholder for a more complex prim.
Add a Cylinder to the scene and nest the Lidar prim under it:

1. Right click in the viewport and select **Create > Mesh > Cylinder**.
2. Set the translation of the Cylinder to `(0, 0, 0)`.
3. In the [Stage](../reference_material/reference_glossary.html#isaac-sim-glossary-stage) panel, drag-and-drop the `LIDAR` prim onto the `Cylinder`.
4. This makes the `Cylinder` the parent of the `LIDAR`. When the `Cylinder` moves, the `LIDAR` moves with it. All information reported by the LIDAR is now relative to the `Cylinder`.
5. Add an offset to `LIDAR` to precisely position it relative to the `Cylinder`. Select the `LIDAR` prim from the [Stage](../reference_material/reference_glossary.html#isaac-sim-glossary-stage) and move it to `(0.5, 0.5, 0)`.
6. Move the `Cylinder` around the environment. The LIDAR maintains this relative transform.
7. Re-select the `LIDAR` prim and reset its `Translate` value to its default setting `(0, 0, 0)`.

#### Attach a Lidar to a moving robot

You can attach a LIDAR prim to a robot. You can use the Carter V1 robot as an example.

1. Open the Isaac Sim **Content Browser**, navigate to `Robots/NVIDIA/Carter/carter_v1.usd`, and open the `carter_v1.usd` file.
2. Open the left wheel joint at carter/chassis\_link/left\_wheel, scroll down on the property panel, and set the Target Velocity to 100.
3. Repeat the same process for the right wheel joint at carter/chassis\_link/right\_wheel.
4. Press **Play** and the Carter robot drives forward automatically.
5. Create a `LIDAR` by going to the top Menu Bar and clicking **Create > Sensors > PhysX LIDAR > Rotating**. The `LIDAR` prim is created as a child of the selected prim.
6. In the [Stage](../reference_material/reference_glossary.html#isaac-sim-glossary-stage) panel, select your `LIDAR` prim and drag it onto `/carter/chassis_link`.
7. Set the translation of the PhysX lidar to -0.06, 0.0, 0.38 to move it to the correct location.
8. Enable draw lines and set the rotation rate to zero for easier debugging.

### Script Editor

Use the Lidar Python API to create, control, and query the sensor through scripts and extensions.
Use the **Script Editor** and Python API to retrieve data from the Lidar’s last sweep:

1. Go to the top menu bar and click **Window > Script Editor** to open the **Script Editor** window.
2. Add the necessary imports:

```python
import asyncio  # Used to run sample asynchronously to not block rendering thread

import omni  # Provides the core omniverse APIs
from isaacsim.sensors.physx import _range_sensor  # Imports the python bindings to interact with Lidar sensor
from pxr import Gf, UsdGeom, UsdPhysics  # pxr usd imports used to create the cube
```

3. Grab the Stage, Simulation Timeline, and LIDAR interface:

```python
import omni

stage = omni.usd.get_context().get_stage()  # Used to access Geometry
timeline = omni.timeline.get_timeline_interface()  # Used to interact with simulation
lidarInterface = _range_sensor.acquire_lidar_sensor_interface()  # Used to interact with the LIDAR

# These commands are the Python-equivalent of the first half of this tutorial
omni.kit.commands.execute("AddPhysicsSceneCommand", stage=stage, path="/World/PhysicsScene")
lidarPath = "/LidarName"
result, prim = omni.kit.commands.execute(
    "RangeSensorCreateLidar",
    path=lidarPath,
    parent="/World",
    min_range=0.4,
    max_range=100.0,
    draw_points=False,
    draw_lines=True,
    horizontal_fov=360.0,
    vertical_fov=30.0,
    horizontal_resolution=0.4,
    vertical_resolution=4.0,
    rotation_rate=0.0,
    high_lod=False,
    yaw_offset=0.0,
    enable_semantics=False,
)
```

4. Create an obstacle for the LIDAR:

```python
from isaacsim.core.experimental.utils.stage import get_current_stage
from pxr import Gf, UsdGeom, UsdPhysics

stage = get_current_stage()
CubePath = "/World/CubeName"  # Create a Cube
cubeGeom = UsdGeom.Cube.Define(stage, CubePath)
cubePrim = stage.GetPrimAtPath(CubePath)
cubeGeom.AddTranslateOp().Set(Gf.Vec3f(2.0, 0.0, 0.0))  # Move it away from the LIDAR
cubeGeom.CreateSizeAttr(1)  # Scale it appropriately
collisionAPI = UsdPhysics.CollisionAPI.Apply(cubePrim)  # Add a Physics Collider to it
```

5. Get the LIDAR data:

   > The Lidar needs one simulation frame to get data for the first frame, so start
   > the simulation by calling `timeline.play`, wait for a frame to complete, and then pause simulation using `timeline.pause()` to populate the depth buffers in the Lidar.
   > Because the simulation is running asynchronously with our script, use `asyncio` and `ensure_future` to wait for our script to complete
   > calling `timeline.pause()` is optional, data from the sensor can be gathered anytime while simulating.
   >
   > ```python
   > import asyncio
   >
   > import omni.timeline
   >
   >
   > async def get_lidar_param():  # Function to retrieve data from the LIDAR
   >     await omni.kit.app.get_app().next_update_async()  # wait one frame for data
   >     timeline.pause()  # Pause the simulation to populate the LIDAR's depth buffers
   >     depth = lidarInterface.get_linear_depth_data("/World" + lidarPath)
   >     zenith = lidarInterface.get_zenith_data("/World" + lidarPath)
   >     azimuth = lidarInterface.get_azimuth_data("/World" + lidarPath)
   >     print("depth", depth)  # Print the data
   >     print("zenith", zenith)
   >     print("azimuth", azimuth)
   >
   >
   > timeline = omni.timeline.get_timeline_interface()
   > timeline.play()  # Start the Simulation
   > asyncio.ensure_future(get_lidar_param())  # Only ask for data after sweep is complete
   > ```
6. Run the full script:

Expand to display full code

```python
# provides the core omniverse APIs
# used to run sample asynchronously to not block rendering thread
import asyncio

import omni

# import the python bindings to interact with Lidar sensor
from isaacsim.sensors.physx import _range_sensor

# pxr usd imports used to create cube
from pxr import Gf, UsdGeom, UsdPhysics

stage = omni.usd.get_context().get_stage()
lidarInterface = _range_sensor.acquire_lidar_sensor_interface()
timeline = omni.timeline.get_timeline_interface()
omni.kit.commands.execute("AddPhysicsSceneCommand", stage=stage, path="/World/PhysicsScene")
lidarPath = "/LidarName"
result, prim = omni.kit.commands.execute(
    "RangeSensorCreateLidar",
    path=lidarPath,
    parent="/World",
    min_range=0.4,
    max_range=100.0,
    draw_points=False,
    draw_lines=True,
    horizontal_fov=360.0,
    vertical_fov=30.0,
    horizontal_resolution=0.4,
    vertical_resolution=4.0,
    rotation_rate=0.0,
    high_lod=False,
    yaw_offset=0.0,
    enable_semantics=False,
)

CubePath = "/World/CubeName"
cubeGeom = UsdGeom.Cube.Define(stage, CubePath)
cubePrim = stage.GetPrimAtPath(CubePath)
cubeGeom.AddTranslateOp().Set(Gf.Vec3f(2.0, 0.0, 0.0))
cubeGeom.CreateSizeAttr(1)
collisionAPI = UsdPhysics.CollisionAPI.Apply(cubePrim)

async def get_lidar_param():
    await omni.kit.app.get_app().next_update_async()
    timeline.pause()
    depth = lidarInterface.get_linear_depth_data("/World" + lidarPath)
    zenith = lidarInterface.get_zenith_data("/World" + lidarPath)
    azimuth = lidarInterface.get_azimuth_data("/World" + lidarPath)
    print("depth", depth)
    print("zenith", zenith)
    print("azimuth", azimuth)

timeline.play()
asyncio.ensure_future(get_lidar_param())
```

Verify that you have the following:

#### Segment a Point Cloud

This code snippet shows how to add semantic labels to the depth data for segmenting its resulting point cloud.

```python
import asyncio  # Used to run sample asynchronously to not block rendering thread

import omni  # Provides the core omniverse APIs
from isaacsim.sensors.physx import _range_sensor  # Imports the python bindings to interact with Lidar sensor
from pxr import Gf, Semantics, UsdGeom, UsdPhysics  # pxr usd imports used to create cube

stage = omni.usd.get_context().get_stage()  # Used to access Geometry
timeline = omni.timeline.get_timeline_interface()  # Used to interact with simulation
lidarInterface = _range_sensor.acquire_lidar_sensor_interface()  # Used to interact with the LIDAR
# These commands are the Python-equivalent of the first half of this tutorial
omni.kit.commands.execute("AddPhysicsSceneCommand", stage=stage, path="/World/PhysicsScene")
lidarPath = "/LidarName"
# Create Lidar prim
result, prim = omni.kit.commands.execute(
    "RangeSensorCreateLidar",
    path=lidarPath,
    parent="/World",
    min_range=0.4,
    max_range=100.0,
    draw_points=True,
    draw_lines=False,
    horizontal_fov=360.0,
    vertical_fov=60.0,
    horizontal_resolution=0.4,
    vertical_resolution=0.4,
    rotation_rate=0.0,
    high_lod=True,
    yaw_offset=0.0,
    enable_semantics=True,
)
UsdGeom.XformCommonAPI(stage.GetPrimAtPath("/World" + lidarPath)).SetTranslate((2.0, 0.0, 0.0))

# Create a cube, sphere, add collision and different semantic labels
primType = ["Cube", "Sphere"]
for i in range(2):
    prim = stage.DefinePrim("/World/" + primType[i], primType[i])
    UsdGeom.XformCommonAPI(prim).SetTranslate((-2.0, -2.0 + i * 4.0, 0.0))
    UsdGeom.XformCommonAPI(prim).SetScale((1, 1, 1))
    collisionAPI = UsdPhysics.CollisionAPI.Apply(prim)

    # Add semantic label
    sem = Semantics.SemanticsAPI.Apply(prim, "Semantics")
    sem.CreateSemanticTypeAttr()
    sem.CreateSemanticDataAttr()
    sem.GetSemanticTypeAttr().Set("class")
    sem.GetSemanticDataAttr().Set(primType[i])

# Get point cloud and semantic id for Lidar hit points
async def get_lidar_param():
    await asyncio.sleep(1.0)
    timeline.pause()
    pointcloud = lidarInterface.get_point_cloud_data("/World" + lidarPath)
    semantics = lidarInterface.get_prim_data("/World" + lidarPath)

    print("Point Cloud", pointcloud)
    print("Semantic ID", semantics)

timeline.play()  # Start the Simulation
asyncio.ensure_future(get_lidar_param())  # Only ask for data after sweep is complete
```

The main differences between this example and the previous are as follows:

1. The LIDAR’s `enable_semantics` flag is set to `True` on creation.
2. The Cube and Sphere prims have different `semantic labels`.
3. Use `get_point_cloud_data` and `get_prim_data` to retrieve the point cloud data and semantic IDs.

The segmented point cloud from the Lidar sensor looks like the image below:

On this page

* [GUI](#gui)
  + [PhysX SDK lidar sensor example](#physx-lidar-sensor-example)
  + [Adding a PhysX SDK lidar sensor to a simulation](#adding-a-physx-lidar-sensor-to-a-simulation)
    - [Scene setup](#scene-setup)
    - [Set up collision detection](#set-up-collision-detection)
    - [Attach a Lidar to geometry](#attach-a-lidar-to-geometry)
    - [Attach a Lidar to a moving robot](#attach-a-lidar-to-a-moving-robot)
  + [Script Editor](#script-editor)
    - [Segment a Point Cloud](#segment-a-point-cloud)

---

### PhysX Lightbeam

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/sensors/isaacsim_sensors_physx_lightbeam.html

* [Sensors](index.html)
* [PhysX SDK sensors](isaacsim_sensors_physx.html)
* PhysX SDK lightbeam sensor

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# PhysX SDK lightbeam sensor

Deprecated since version 6.0: The PhysX SDK sensor extensions (`isaacsim.sensors.physx`) are deprecated. Use
`isaacsim.sensors.experimental.physics.RaycastSensor` as the replacement for raycast-based sensing.
For lightbeam/safety-curtain specific functionality, consider using the `RaycastSensor` with
appropriate configuration.
See [Migrating to the physics raycast sensor](#isaacsim-sensors-physx-lightbeam-migration) for step-by-step migration instructions, or the [isaacsim.sensors.experimental.physics API Documentation](../py/source/extensions/isaacsim.sensors.experimental.physics/docs/index.html) for the replacement APIs.

The PhysX SDK lightbeam sensor in Isaac Sim uses PhysX SDK raycasts to determine if an object has intersected a light beam.
You can specify the number of rays and height to create a safety light “curtain” of lightbeam sensors.

See the [Isaac Sim Conventions](../reference_material/reference_conventions.html#isaac-sim-conventions) documentation for a complete list of Isaac Sim conventions.

## Examples

* PhysX SDK Lightbeam Sensor example: **Robotics Examples > Sensors > Lightbeam**

To run the example:

1. Activate **Robotics Examples** tab from **Windows** > **Examples** > **Robotics Examples**.
2. Click **Robotics Examples > Sensors > Lightbeam**.
3. Verify that you have a window containing empty data for each lightbeam, which populates with data after you press **Play**. It shows if each beam was hit, the linear depth of the hit, and the exact hit position in `xyz`.
4. Press the **Play** button to begin simulating.
5. Press `SHIFT + LEFT_CLICK` to drag the cube or sensor around and see changes in the readings.

## Migrating to the physics raycast sensor

The PhysX SDK lightbeam sensor is deprecated. Use the [Physics Raycast Sensor](isaacsim_sensors_physics_raycast.html#isaacsim-sensors-physics-raycast) (`isaacsim.sensors.experimental.physics.RaycastSensor`) configured as a beam curtain to achieve the same functionality.

### Concept mapping

| PhysX SDK Lightbeam Sensor | Physics Raycast Sensor |
| --- | --- |
| `numRays` | Length of the `rayOrigins` / `rayDirections` arrays. Create one entry per beam. |
| `curtainLength` / `curtainAxis` | `rayOrigins`. Spread ray origins along the curtain axis. For example, for a vertical curtain of height *h* with *N* beams: `origins[i] = [0, 0, -h/2 + h * i / (N-1)]`. |
| `forwardAxis` | `rayDirections`. Set all direction vectors to the forward axis. For example, `[1, 0, 0]` for a curtain firing along the X axis. |
| `minRange` / `maxRange` | `minRange` / `maxRange`. Same semantics. |
| Per-beam hit / depth / position data | `RaycastSensor.get_sensor_reading()` returns per-ray depths, hit positions, and hit normals. |

### Interactive example

The **Physics Raycast Sensor** example includes a beam curtain sensor configuration with parallel vertical rays:

* **GUI**: Open **Robotics Examples > Sensors > Physics Raycast Sensor** and click **Load Scene**.
* **Source code**: `source/extensions/isaacsim.sensors.physics.examples/isaacsim/sensors/physics/examples/raycast_sensor.py`

See [Physics raycast sensor](isaacsim_sensors_physics_raycast.html#isaacsim-sensors-physics-raycast) for the full documentation, including Python API usage and OmniGraph workflows.

On this page

* [Examples](#examples)
* [Migrating to the physics raycast sensor](#migrating-to-the-physics-raycast-sensor)
  + [Concept mapping](#concept-mapping)
  + [Interactive example](#interactive-example)

---

### PhysX Proximity

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/sensors/isaacsim_sensors_physx_proximity.html

* [Sensors](index.html)
* [PhysX SDK sensors](isaacsim_sensors_physx.html)
* Proximity sensor

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Proximity sensor

Deprecated since version 6.0: The Proximity Sensor (`isaacsim.sensors.physx.ProximitySensor`) is part of the deprecated `isaacsim.sensors.physx` extension.
For collision detection, consider using the [Contact Sensor](isaacsim_sensors_physics_contact.html#isaacsim-sensors-physics-contact) or physics contact callbacks directly.

The proximity sensor wraps a physics callback that can be attached to any prim in the scene. During simulation execution,
the sensor records collisions between the prim it is attached to and other prims in the scene each frame; you can access that data
using a callback function.

## Standalone Python

Note

The code below uses the deprecated `isaacsim.sensors.physx` extension. See the deprecation notice above for the replacement API.

Execute the following script using `python.sh`. This creates a scene with two cubes and attaches a proximity sensor to one of the cubes.
At the start of the simulation, the two cubes overlap and then move apart; the callback function in the script prints the proximity
sensor’s output to the screen.

```python
import numpy as np
from isaacsim import SimulationApp

simulation_app = SimulationApp({"headless": False})

import carb
import omni
from isaacsim.core.api.world import World
from isaacsim.core.experimental.objects import Cube, GroundPlane
from isaacsim.core.utils.extensions import enable_extension
from pxr import Sdf, UsdLux, UsdPhysics

# Set up scene
world = World()
GroundPlane("/World/GroundPlane")

# Add lighting
stage = omni.usd.get_context().get_stage()
distantLight = UsdLux.DistantLight.Define(stage, Sdf.Path("/DistantLight"))
distantLight.CreateIntensityAttr(500)

# Add cubes with collision and rigid body for physics simulation
cube_1 = Cube("/cube_1", sizes=1.0, positions=np.array([0.4, 0, 5.0]), colors=np.array([1.0, 0, 0]))
UsdPhysics.CollisionAPI.Apply(cube_1.prims[0])
UsdPhysics.RigidBodyAPI.Apply(cube_1.prims[0])

cube_2 = Cube("/cube_2", sizes=1.0, positions=np.array([-0.4, 0, 5.0]), colors=np.array([0, 0, 1.0]))
UsdPhysics.CollisionAPI.Apply(cube_2.prims[0])
UsdPhysics.RigidBodyAPI.Apply(cube_2.prims[0])

# Enable isaacsim.sensors.physx extension
enable_extension("isaacsim.sensors.physx")
simulation_app.update()

# Attach sensor to cube 1
from isaacsim.sensors.physx import ProximitySensor, clear_sensors, register_sensor

s = ProximitySensor(cube_1.prims[0])
register_sensor(s)

# Add callback to print proximity sensor data
def print_proximity_sensor_data_on_update(_):
    data = s.get_data()
    if "/cube_2" in data:
        # /cube_1 is colliding with /cube_2
        distance = data["/cube_2"]["distance"]
        duration = data["/cube_2"]["duration"]
        carb.log_warn(f"distance: {distance}, duration: {duration}")

# Play simulation
world.add_physics_callback("print_sensor_data", print_proximity_sensor_data_on_update)
simulation_app.update()
simulation_app.update()
world.play()

for i in range(100):
    # Run with a fixed step size
    world.step(render=True)
```

Example proximity sensor output is shown below; there might be small numerical differences in your output run-to-run.

```python
distance: 0.8995118804137266, duration: 0.03952527046203613
distance: 0.9490971672498862, duration: 0.04244112968444824
distance: 0.9978315307718298, duration: 0.045195579528808594
distance: 1.0952793930211249, duration: 0.00010466575622558594
distance: 1.0952880909233123, duration: 0.004382610321044922
distance: 1.0952874949586842, duration: 0.008539199829101562
distance: 1.095288806188406, duration: 0.012722015380859375
```

After the cubes land, the scene looks like the following image:

On this page

* [Standalone Python](#standalone-python)

---

### RTX Sensors Index

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/sensors/isaacsim_sensors_rtx.html

* [Sensors](index.html)
* RTX Sensors

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# RTX Sensors

RTX sensors in Isaac Sim use the Omniverse RTX Renderer’s RTX Sensor SDK to sense the environment, enabling interaction with materials in visual and non-visual spectra.
This means an RTX-based Lidar can model returns from light interaction with transparent or reflective surfaces, and an RTX-based Radar can model returns accounting for
material emissivity and reflectivity in the radio spectrum.

Isaac Sim organizes utilities supporting RTX sensors into the `isaacsim.sensors.experimental.rtx` extension.

Deprecated since version 6.0: The `isaacsim.sensors.rtx` extension is deprecated. Use `isaacsim.sensors.experimental.rtx` instead.
The new extension provides equivalent sensor classes (`Lidar`/`LidarSensor`, `Radar`/`RadarSensor`,
plus the new `Acoustic`/`AcousticSensor`) with a uniform authoring/runtime split.
See [RTX Sensors](../migration_guides/isaac_sim_6_0/sensors_rtx_to_experimental_rtx.html#isaacsim-sensors-rtx-migration).

## Getting Started

To get started with RTX sensors:

1. **Add a sensor to your scene**: Use **Create** > **Isaac** > **Sensors** > **RTX Lidar** or **RTX Radar** from the menu, or use the Python APIs described in the sensor-specific pages below.
2. **Collect data**: Attach [annotators](isaacsim_sensors_rtx_annotators.html#rtx-sensor-annotator-descriptions) to the sensor to extract point cloud data, scan buffers, or raw `GenericModelOutput` data.
3. **Visualize output**: Use the [Debug Draw Extension](../utilities/debugging/ext_isaacsim_util_debug_draw.html#isaac-debug-draw) to visualize point clouds, or configure viewport debug views.
4. **Integrate with ROS2**: Follow the [RTX Lidar ROS2 Tutorial](../ros2_tutorials/tutorial_ros2_rtx_lidar.html#isaac-sim-app-tutorial-ros2-rtx-lidar) to publish sensor data as `PointCloud2` or `LaserScan` messages.

## Sensor Types

* [RTX Lidar Sensor](isaacsim_sensors_rtx_lidar.html)
* [RTX Radar Sensor](isaacsim_sensors_rtx_radar.html)
* [RTX Acoustic Sensor](isaacsim_sensors_rtx_acoustic.html)

## Data Collection and Materials

* [RTX Sensor Annotators](isaacsim_sensors_rtx_annotators.html)
* [RTX Sensor Non-Visual Materials](isaacsim_sensors_rtx_materials.html)

## Advanced Topics

* [Multi-Tick Rendering](isaacsim_sensors_multitick_rendering.html)
* [Creating Custom RTX Sensor Profiles](isaacsim_sensors_rtx_custom.html)

## Extension Architecture

RTX sensors are built using the `omni.sensors` extension suite. To understand more about how RTX sensors are modeled,
and how to build your own, review the following documentation:

* [Omniverse Common Extension](https://docs.omniverse.nvidia.com/kit/docs/omni.sensors.nv.common/latest/common_extension.html)
* [Omniverse Lidar Extension](https://docs.omniverse.nvidia.com/kit/docs/omni.sensors.nv.lidar/latest/lidar_extension.html)
* [Omniverse Radar Extension](https://docs.omniverse.nvidia.com/kit/docs/omni.sensors.nv.radar/latest/radar_extension.html)
* [Omniverse Acoustic Extension](https://docs.omniverse.nvidia.com/kit/docs/omni.sensors.nv.acoustic/3.0.0/acoustic_extension.html)
* [Omniverse Materials Extension](https://docs.omniverse.nvidia.com/kit/docs/omni.sensors.nv.materials/latest/materials_extension.html)

## Important Settings

The following settings affect RTX sensor behavior and performance:

| Setting | Default | Description |
| --- | --- | --- |
| `--/app/sensors/nv/lidar/outputBufferOnGPU` | `false` | Keep Lidar return buffer on GPU for post-processing. Must be `false` for annotators to work correctly. |
| `--/app/sensors/nv/radar/outputBufferOnGPU` | `false` | Keep Radar return buffer on GPU for post-processing. Must be `false` for annotators to work correctly. |
| `--/app/sensors/nv/lidar/publishNormals` | `false` | Enable hit normal output. Increases VRAM usage. |
| `--/rtx/materialDb/nonVisualMaterialCSV/enabled` | `false` | Enable non-visual materials using USD attributes. |
| `--/rtx/materialDb/nonVisualMaterialSemantics/prefix` | `omni:simready:nonvisual` | Specify the non-visual material USD attribute prefix. |
| `--/rtx/rtxsensor/useHydraTimeAlways` | `true` | Use Hydra time (`omni.timeline`) in RTX sensor models. Applies only if multi-tick rendering is disabled. |
| `--/rtx-transient/stableIds/enabled` | `false` | Enable stable 128-bit object IDs for semantic segmentation. |
| `--/renderer/raytracingMotion/enabled` | `false` | Enable Motion BVH for motion compensation and Doppler effects. |

## Motion BVH

RTX sensors use Motion BVH to improve accuracy when modeling motion-related sensor effects, for example, the motion of objects during sensor exposure, or the motion of the sensor itself as it collects data.

By default, Motion BVH is disabled in Isaac Sim to improve performance. The following RTX Sensor features are affected by Motion BVH:

* RTX Lidar

  + Motion BVH must be enabled for RTX Lidar motion compensation to work correctly.
* RTX Radar

  + Motion BVH must be enabled for the Doppler effect, and therefore RTX Radar entirely, to be modeled correctly.

### How to Enable Motion BVH

Note

Enabling Motion BVH can significantly increase rendering time by increasing VRAM usage for all sensors and must be left disabled when not needed.

There are two ways to enable Motion BVH:

1. In standalone Python workflows, you can enable Motion BVH by specifying `enable_motion_bvh` as `True` in the `SimulationApp` constructor:

> ```python
> from isaacsim import SimulationApp
>
> simulation_app = SimulationApp({"enable_motion_bvh": True})
>
> simulation_app.close()
> ```

2. In all workflows, you can enable Motion BVH by specifying the following settings on the command line:

> ```python
> --/renderer/raytracingMotion/enabled=true \
> --/renderer/raytracingMotion/enableHydraEngineMasking=true \
> --/renderer/raytracingMotion/enabledForHydraEngines='0,1,2,3,4'
> ```

## Auxiliary Output Level and the GenericModelOutput RenderVar

RTX Lidar, Radar, and Acoustic sensors emit a `GenericModelOutput` (GMO) AOV. The
amount of auxiliary data carried in each GMO frame is controlled by the
`_replicator:rendervar:GenericModelOutput:channels` attribute on the sensor prim.

### Setting the channels attribute in the UI

To set `_replicator:rendervar:GenericModelOutput:channels` on an OmniRadar prim from
the Isaac Sim UI:

1. Select the prim in the **Stage** window.
2. Open the **Property** tab.
3. Expand the **Array Properties** widget.
4. Click **Edit** on the `_replicator:rendervar:GenericModelOutput:channels` row.
5. Set the first field in the dialog to `BASIC`.
6. Close the dialog to save the change.

### How the attribute flows to the RenderVar

When `omni.replicator.core` adds a `GenericModelOutput` RenderVar to a render product
that is attached to an RTX sensor prim, it reads
`_replicator:rendervar:GenericModelOutput:channels` from the sensor prim and copies the
value onto the RenderVar’s `channels` attribute. The RTX Sensor SDK then uses that
value to decide which auxiliary fields to populate.

The `aux_output_level` constructor parameter on
`isaacsim.sensors.experimental.rtx.Lidar`,
`isaacsim.sensors.experimental.rtx.Radar`, and
`isaacsim.sensors.experimental.rtx.Acoustic` is a convenience that authors
`_replicator:rendervar:GenericModelOutput:channels = [level]` on the sensor prim. The
two paths are interchangeable; reading existing USD scenes is easier if you recognize
the underlying attribute.

Valid values are modality-specific:

| Modality | Valid values |
| --- | --- |
| Lidar | `NONE` (default), `BASIC`, `EXTRA`, `FULL` |
| Radar | `NONE` (default), `BASIC` |
| Acoustic | `NONE` (default), `BASIC` |

See [RTX Sensor Annotators](isaacsim_sensors_rtx_annotators.html#rtx-sensor-annotator-descriptions) for the per-level field listing.

### Migration from previous releases

Earlier releases used per-modality USD attributes for the same purpose. These attributes
have been removed from the schemas:

| Old attribute (removed) | Replacement |
| --- | --- |
| `omni:sensor:Core:auxOutputType` (Lidar) | `_replicator:rendervar:GenericModelOutput:channels` on the `OmniLidar` prim, or `Lidar(..., aux_output_level='FULL')`. |
| `omni:sensor:WpmDmat:auxOutputType` (Radar) | `_replicator:rendervar:GenericModelOutput:channels` on the `OmniRadar` prim, or `Radar(..., aux_output_level='BASIC')`. |

USD assets shipped with Isaac Sim 6.0 have already been updated. Custom USD
scenes carrying the old attributes need to be migrated; the old attributes are silently
ignored by the new schemas.

Note

`RtxCamera` removes `_replicator:rendervar:GenericModelOutput:channels` from the
Camera prim during construction because cameras do not produce a GMO AOV. Camera
prims therefore do not participate in the propagation behavior described in
[Known issue: last-attach-wins propagation of GMO channels](#isaacsim-sensors-rtx-known-issue-gmo-channels).

### Known issue: last-attach-wins propagation of GMO channels

Warning

The `_replicator:rendervar:GenericModelOutput:channels` attribute is currently
**effectively global per render-product-attach event**. When two RTX sensors on the
same stage author different values, only the **last** sensor to have a render product
attached “wins” - every subsequent `GenericModelOutput` RenderVar uses that
sensor’s channels value, regardless of which sensor prim it was created from.

Concrete example. Suppose you have one `Lidar` with `aux_output_level="FULL"` and
one `Radar` with `aux_output_level="BASIC"` on the same stage:

* If the **Radar** render product is created second, every GMO consumer (Lidar and
  Radar) sees `BASIC` channels. The Lidar silently loses its `FULL`-level fields.
* If the **Lidar** render product is created second, the Radar GMO RenderVar inherits
  `FULL`. The Radar pipeline does not recognize `FULL` and produces **no auxiliary
  data at all** for that Radar (no `rv_ms`, no intensity, etc.).

Recommended workarounds:

* Keep all RTX sensors on a stage at the same `aux_output_level`.
* Order render-product attachment so the sensor whose channels value you want to use is
  attached last.
* Split sensors with conflicting auxiliary-output requirements across separate stages
  or `SimulationApp` instances.

This issue is tracked separately and will be addressed in a future release. Cameras are
unaffected: `RtxCamera` removes the GMO channels attribute during construction because
Camera prims do not emit GMO AOVs.

## Troubleshooting and Known Issues

### Common Issues

**Annotators return empty data**
:   Ensure the simulation timeline is playing. RTX Sensor Annotators rely on the timeline to collect data.
    Also verify that `--/app/sensors/nv/lidar/outputBufferOnGPU` or `--/app/sensors/nv/radar/outputBufferOnGPU` is left at its default value of `false` — annotators read return data from host buffers, so forcing the GPU-resident path will leave the annotator outputs empty.

**Point cloud appears to “drag” behind moving objects**
:   If the Lidar rotation rate is slower than the frame rate, accumulated scan data may contain returns from multiple frames.
    This is expected behavior for rotating Lidars. Consider using per-frame output instead of accumulated scans.

**Lidar scans are incomplete**
:   Ensure `omni:sensor:Core:accumulateOutputs` is set to `true` on the `OmniLidar` prim. `omni:sensor:tickRate` must equal `omni:sensor:Core:scanRateBaseHz` on the `OmniLidar` prim.
    See [OmniLidar Tick Rate Must Equal scanRateBaseHz](isaacsim_sensors_multitick_rendering.html#isaac-sim-sensors-multitick-lidar-tickrate-must-match-scanrate).

**Radar simulation does not show Doppler effects**
:   Motion BVH must be enabled for Doppler effects to be modeled correctly. See [How to Enable Motion BVH](#isaac-sim-sensors-rtx-how-to-enable-motion-bvh).

**Timestamps are discontinuous after pause/resume**
:   This should not occur if multi-tick rendering is enabled. If multi-tick rendering is disabled, the `GenericModelOutput` AOV timestamp is independent of the animation timeline and continues to increase even when paused.

**One sensor’s auxiliary output level overrides another’s**
:   The `_replicator:rendervar:GenericModelOutput:channels` attribute is currently global
    per render-product-attach event. See [Known issue: last-attach-wins propagation of GMO channels](#isaacsim-sensors-rtx-known-issue-gmo-channels).

### Performance Considerations

* **VRAM Usage**: Each RTX sensor requires GPU memory. Multiple sensors or high-resolution configurations increase VRAM usage.
* **Motion BVH**: Enabling Motion BVH significantly increases VRAM usage and rendering time.
* **Normal Output**: Enabling `--/app/sensors/nv/lidar/publishNormals=true` increases VRAM usage.
* **Stable IDs**: Enabling `--/rtx-transient/stableIds/enabled=true` has minimal performance impact but requires additional processing for object ID resolution.

### Hardware Requirements

RTX sensors require an NVIDIA RTX GPU with ray tracing support. Performance scales with GPU capabilities, particularly:

* VRAM capacity (affects number of sensors and resolution)
* Ray tracing cores (affects simulation speed)

## Related Tutorials

* [RTX Lidar Sensors](../ros2_tutorials/tutorial_ros2_rtx_lidar.html#isaac-sim-app-tutorial-ros2-rtx-lidar) - Publishing RTX Lidar data to ROS2
* [RTX Radar Sensors](../ros2_tutorials/tutorial_ros2_rtx_radar.html#isaac-sim-app-tutorial-ros2-rtx-radar) - Publishing RTX Radar data to ROS2
* [Multi-Tick Rendering](isaacsim_sensors_multitick_rendering.html#isaac-sim-sensors-multitick-rendering) - Multi-tick rendering and 5.x â 6.0 migration
* [Debug Drawing Extension API](../utilities/debugging/ext_isaacsim_util_debug_draw.html#isaac-debug-draw) - Visualizing point clouds and geometry
* [Util Snippets](../python_scripting/util_snippets.html#isaac-sim-app-util-snippets) - Rendering and visualization utilities

On this page

* [Getting Started](#getting-started)
* [Sensor Types](#sensor-types)
* [Data Collection and Materials](#data-collection-and-materials)
* [Advanced Topics](#advanced-topics)
* [Extension Architecture](#extension-architecture)
* [Important Settings](#important-settings)
* [Motion BVH](#motion-bvh)
  + [How to Enable Motion BVH](#how-to-enable-motion-bvh)
* [Auxiliary Output Level and the GenericModelOutput RenderVar](#auxiliary-output-level-and-the-genericmodeloutput-rendervar)
  + [Setting the channels attribute in the UI](#setting-the-channels-attribute-in-the-ui)
  + [How the attribute flows to the RenderVar](#how-the-attribute-flows-to-the-rendervar)
  + [Migration from previous releases](#migration-from-previous-releases)
  + [Known issue: last-attach-wins propagation of GMO channels](#known-issue-last-attach-wins-propagation-of-gmo-channels)
* [Troubleshooting and Known Issues](#troubleshooting-and-known-issues)
  + [Common Issues](#common-issues)
  + [Performance Considerations](#performance-considerations)
  + [Hardware Requirements](#hardware-requirements)
* [Related Tutorials](#related-tutorials)

---

### RTX Acoustic

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/sensors/isaacsim_sensors_rtx_acoustic.html

* [Sensors](index.html)
* [RTX Sensors](isaacsim_sensors_rtx.html)
* RTX Acoustic Sensor

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# RTX Acoustic Sensor

RTX Acoustic sensors simulate ultrasonic wave propagation at render time on the GPU with RTX hardware.
Their results are written to the `GenericModelOutput` AOV, similar to RTX Lidar and Radar sensors.

## Overview

RTX Acoustic sensors are rendered using `OmniAcoustic` prims, with the `OmniSensorGenericAcousticWpmAPI`
schema applied. After attaching a render product to the `OmniAcoustic` prim, and setting the
`GenericModelOutput` AOV on the render product, the RTXSensor renderer writes acoustic simulation
results to the AOV.

For complete documentation on all acoustic schema attributes and the underlying Wave Propagation Model (WPM),
see the [Omniverse Acoustic Extension documentation](https://docs.omniverse.nvidia.com/kit/docs/omni.sensors.nv.acoustic/3.0.0/acoustic_extension.html).

Note

Earlier releases referred to this sensor as the “Ultrasonic” sensor (or “USS”). The Omniverse plugin
has been renamed to “Acoustic”; if you previously used `omni.kit.commands.execute("IsaacSensorCreateRtxUltrasonic", ...)`
in `isaacsim.sensors.rtx`, see [RTX Sensors](../migration_guides/isaac_sim_6_0/sensors_rtx_to_experimental_rtx.html#isaacsim-sensors-rtx-migration) for the migration to
`Acoustic` / `AcousticSensor`.

Unlike Lidar and Radar sensors, acoustic sensors do not produce a 3D point cloud. Instead, they produce
**signal ways** — amplitude samples for each transmitter–receiver pair on each channel. The
`GenericModelOutput` element fields have the following meaning for acoustic sensors:

| Field | Meaning |
| --- | --- |
| `x` | Transmitter sensor mount ID |
| `y` | Receiver sensor mount ID |
| `z` | Channel ID |
| `scalar` | Amplitude sample value |

### Sensor Mounts and Receiver Groups

Acoustic sensors use **multi-apply schemas** to define sensor mounts and receiver groups:

* **Sensor mounts** (`OmniSensorWpmAcousticSensorMountAPI`) define the physical positions and
  orientations of transducers (transmitters and receivers). Each mount is an instance with a unique
  name (for example, `m001`, `m002`).
* **Receiver groups** (`OmniSensorWpmAcousticRxGroupAPI`) define logical groupings of receivers
  by specifying which mount indices belong to the group. Each group is an instance with a unique
  name (for example, `g001`).

These schemas are applied automatically when the corresponding attribute prefixes are provided
in the `attributes` dictionary.

## How to Create an RTX Acoustic Sensor

The `isaacsim.sensors.experimental.rtx` extension provides the `Acoustic` class for creating RTX
Acoustic sensors. An equivalent menu entry is also registered by the `isaacsim.sensors.rtx.ui`
extension for UI-driven creation.

### Create an RTX Acoustic Sensor From the Create Menu

To create a generic RTX Acoustic sensor from the Isaac Sim UI:

* **Main menu**: *Create > Sensors > RTX Acoustic > NVIDIA > Generic RTX Acoustic*
* **Viewport context menu** (right-click in the viewport): *Create > Isaac > Sensors > RTX Acoustic > NVIDIA > Generic RTX Acoustic*

Both entries create an `OmniAcoustic` prim with the `OmniSensorGenericAcousticWpmAPI` schema applied,
at the next available path. If a prim is selected at creation time, the new sensor is parented under
the selected prim; otherwise it is created at the stage root.

The menu entry creates a bare prim with no sensor mounts or receiver groups configured. To author the
multi-apply schemas (`OmniSensorWpmAcousticSensorMountAPI`, `OmniSensorWpmAcousticRxGroupAPI`)
and tune attributes such as `omni:sensor:WpmAcoustic:centerFrequency`, either edit the prim in the
property panel after creation, or use the `Acoustic` class for programmatic setup as shown below.

The RTX Acoustic submenu also auto-populates additional vendor entries from the
`SUPPORTED_ACOUSTIC_CONFIGS` dict in `isaacsim.sensors.experimental.rtx`, so OEM acoustic asset
USDs registered there appear in the menu automatically.

### Create an RTX Acoustic Sensor Using the `Acoustic` Class

The `Acoustic` class creates or wraps an `OmniAcoustic` prim with the appropriate schemas applied.

Run this snippet in the **Script Editor** (**Window > Script Editor**).

```python
import numpy as np
from isaacsim.sensors.experimental.rtx import Acoustic

# Create an RTX Acoustic sensor with a center frequency and two sensor mounts.
acoustic = Acoustic(
    path="/World/acoustic",
    tick_rate=20.0,
    translations=np.array([0.0, 0.0, 1.0]),
    attributes={
        "omni:sensor:WpmAcoustic:centerFrequency": 40000.0,
        # Sensor mount positions (transmitter/receiver locations)
        "omni:sensor:WpmAcoustic:sensorMount:m001:position": (0.0, 0.0, 0.0),
        "omni:sensor:WpmAcoustic:sensorMount:m002:position": (0.1, 0.0, 0.0),
        # Receiver group combining both mounts
        "omni:sensor:WpmAcoustic:rxGroup:g001:receiverIndices": [0, 1],
    },
)
```

The snippet above creates an `OmniAcoustic` prim at `/World/acoustic` with:

* A center frequency of 40,000 Hz (ultrasonic)
* Two sensor mounts at positions `(0, 0, 0)` and `(0.1, 0, 0)`
* A receiver group combining both mounts

Note

`Acoustic.create()` accepts `config` (from
`isaacsim.sensors.experimental.rtx.SUPPORTED_ACOUSTIC_CONFIGS`) or `usd_path` (mutually
exclusive), plus `attributes` for prim-attribute overrides — including the multi-apply
`OmniSensorWpmAcousticSensorMountAPI` / `OmniSensorWpmAcousticRxGroupAPI` /
`OmniSensorWpmAcousticFiringSeqAPI` schema attributes — and the plural transform arrays
(`positions=[[...]]` / `translations=[[...]]` / `orientations=[[...]]` / `scales=[[...]]`;
`N=1`). Additional USD schemas via `schemas=[...]` are accepted by the `Acoustic(...)`
constructor — pass them through `Acoustic(...)` directly if you need them, since
`Acoustic.create()` does not currently forward `schemas`.

### Tick Rate

Warning

In Isaac Sim 6.0 GA, RTX Acoustic autotriggers regardless of `omni:sensor:tickRate` attribute. This will be corrected in a future release.

The `tick_rate` parameter (Hz) controls how frequently the sensor renders. A value of `0`
(the default) enables autotrigger mode, where the sensor renders every simulation frame. This maps to the `omni:sensor:tickRate` prim attribute.

Run this snippet in the **Script Editor** (**Window > Script Editor**).

```python
from isaacsim.sensors.experimental.rtx import Acoustic

# Render at 10 Hz regardless of simulation frame rate.
acoustic = Acoustic.create("/World/Acoustic", tick_rate=10.0)
```

### Auxiliary Output Level

RTX Acoustic exposes auxiliary data through the `aux_output_level` constructor parameter.
Valid values are `"NONE"` (default) and `"BASIC"`.

Run this snippet in the **Script Editor** (**Window > Script Editor**).

```python
from isaacsim.sensors.experimental.rtx import Acoustic

acoustic = Acoustic.create("/World/Acoustic", aux_output_level="BASIC")
```

See [Auxiliary Output Level and the GenericModelOutput RenderVar](isaacsim_sensors_rtx.html#isaacsim-sensors-rtx-aux-output-level) for the full attribute-flow explanation and the
migration from the removed per-modality `auxOutputType` attribute, and
[Known issue: last-attach-wins propagation of GMO channels](isaacsim_sensors_rtx.html#isaacsim-sensors-rtx-known-issue-gmo-channels) for a known issue when multiple RTX sensors
with different auxiliary levels share a stage. See [RTX Sensor Annotators](isaacsim_sensors_rtx_annotators.html#rtx-sensor-annotator-descriptions) for
the per-level field listing.

## How to Collect Data from an RTX Acoustic Sensor

Use the `AcousticSensor` runtime class to attach annotators and retrieve data:

Run this snippet in the **Script Editor** (**Window > Script Editor**).

```python
from isaacsim.sensors.experimental.rtx import Acoustic, AcousticSensor, parse_generic_model_output_data

acoustic = Acoustic.create("/World/Acoustic")

sensor = AcousticSensor(acoustic, annotators=["generic-model-output"])
data, info = sensor.get_data("generic-model-output")
gmo = parse_generic_model_output_data(data)

# gmo.x      -> transmitter mount IDs
# gmo.y      -> receiver mount IDs
# gmo.z      -> channel IDs
# gmo.scalar -> amplitude values
```

Refer to [Reading Data from the GenericModelOutput Buffer](isaacsim_sensors_rtx_annotators.html#rtx-sensor-reading-gmo-buffer) for more details on the `GenericModelOutput` buffer.

## Standalone Examples

**Basic Creation**

```python
# Create an acoustic sensor with two mounts and a receiver group
./python.sh standalone_examples/api/isaacsim.sensors.experimental.rtx/create_acoustic_basic.py
```

**Data Inspection**

```python
# Inspect acoustic GenericModelOutput data and signal ways
./python.sh standalone_examples/api/isaacsim.sensors.experimental.rtx/inspect_acoustic_gmo.py
```

Note

Refer to the [Isaac Sim Conventions](../reference_material/reference_conventions.html#isaac-sim-conventions) documentation for a complete list of Isaac Sim conventions.

On this page

* [Overview](#overview)
  + [Sensor Mounts and Receiver Groups](#sensor-mounts-and-receiver-groups)
* [How to Create an RTX Acoustic Sensor](#how-to-create-an-rtx-acoustic-sensor)
  + [Create an RTX Acoustic Sensor From the Create Menu](#create-an-rtx-acoustic-sensor-from-the-create-menu)
  + [Create an RTX Acoustic Sensor Using the `Acoustic` Class](#create-an-rtx-acoustic-sensor-using-the-acoustic-class)
  + [Tick Rate](#tick-rate)
  + [Auxiliary Output Level](#auxiliary-output-level)
* [How to Collect Data from an RTX Acoustic Sensor](#how-to-collect-data-from-an-rtx-acoustic-sensor)
* [Standalone Examples](#standalone-examples)

---

### RTX Custom

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/sensors/isaacsim_sensors_rtx_custom.html

* [Sensors](index.html)
* [RTX Sensors](isaacsim_sensors_rtx.html)
* Creating Custom RTX Sensor Profiles

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Creating Custom RTX Sensor Profiles

Note

This section is under development. Additional content will be added in a future update.

This page covers how to create custom RTX sensor configurations by setting attributes on `OmniLidar` and `OmniRadar` prims.

## Getting Started

When creating custom RTX sensor profiles, it is recommended to start with an existing Lidar or Radar configuration shipped with Isaac Sim as a reference:

* [RTX Lidar Asset Library](../assets/usd_assets_nonvisual_sensors.html#isaac-assets-nonvisual-sensors-rtx-lidar) - Pre-configured Lidar sensors from various vendors
* [RTX Radar Sensor](isaacsim_sensors_rtx_radar.html#isaacsim-sensors-rtx-radar) - RTX Radar documentation and examples

You can load an existing configuration, inspect its USD attributes in the *Property* panel, and modify them to suit your needs.

## Setting Lidar Attributes

RTX Lidar sensors are configured via USD attributes on `OmniLidar` prims using the `OmniSensorGenericLidarCoreAPI` schema.

Key configuration areas include:

* **Output configuration**: Setting coordinate systems, motion compensation, and auxiliary data detail levels
* **Scanning principle**: Configuring rotary vs. solid-state scanning
* **Firing pattern**: Defining scan rate, emitter patterns, and number of returns
* **Field of view**: Constraining azimuth and elevation ranges
* **Intensity modeling**: Configuring beam properties, detector sensitivity, and atmospheric effects

For complete documentation on all Lidar attributes and their values, see [Setting Lidar Attributes](https://docs.omniverse.nvidia.com/kit/docs/omni.sensors.nv.lidar/latest/lidar_extension.html#setting-lidar-attributes) in the Omniverse Lidar Extension documentation.

## Setting Radar Attributes

RTX Radar sensors are configured via USD attributes on `OmniRadar` prims using the `OmniSensorGenericRadarWpmDmatAPI` schema.

For complete documentation on all Radar attributes and their values, see [Setting Radar Attributes](https://docs.omniverse.nvidia.com/kit/docs/omni.sensors.nv.radar/latest/radar_extension.html#setting-radar-attributes) in the Omniverse Radar Extension documentation.

## Schema Reference

For the full USD schema definitions, refer to:

* [OmniSensorGenericLidarCoreAPI Schema](https://docs.omniverse.nvidia.com/kit/docs/omni.usd.schema.omni_sensors/107.3.1/omni_sensors_schema.html#omnisensorgenericlidarcoreapi)
* [OmniSensorGenericLidarCoreEmitterStateAPI Schema](https://docs.omniverse.nvidia.com/kit/docs/omni.usd.schema.omni_sensors/107.3.1/omni_sensors_schema.html#omnisensorgenericlidarcoreemitterstateapi)
* [OmniSensorGenericRadarWpmDmatAPI Schema](https://docs.omniverse.nvidia.com/kit/docs/omni.usd.schema.omni_sensors/107.3.1/omni_sensors_schema.html#omnisensorgenericradarwpmdmatapi)

## Validating Your Configuration

After creating a custom sensor configuration, you can validate it by:

1. Adding the sensor to a scene using the methods described in [RTX Lidar Sensor](isaacsim_sensors_rtx_lidar.html#isaacsim-sensors-rtx-lidar) or [RTX Radar Sensor](isaacsim_sensors_rtx_radar.html#isaacsim-sensors-rtx-radar).
2. Visualizing the sensor output using the [Debug Draw Extension](../utilities/debugging/ext_isaacsim_util_debug_draw.html#isaac-debug-draw) or the techniques described in [Visualizing RTX Lidar Output](isaacsim_sensors_rtx_lidar.html#isaacsim-sensors-rtx-lidar-visualization) and [Visualizing RTX Radar Output](isaacsim_sensors_rtx_radar.html#isaacsim-sensors-rtx-radar-visualization).
3. Collecting data using [RTX Sensor Annotators](isaacsim_sensors_rtx_annotators.html#rtx-sensor-annotator-descriptions) to verify the output matches your expectations.

On this page

* [Getting Started](#getting-started)
* [Setting Lidar Attributes](#setting-lidar-attributes)
* [Setting Radar Attributes](#setting-radar-attributes)
* [Schema Reference](#schema-reference)
* [Validating Your Configuration](#validating-your-configuration)

---

### RTX Lidar

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/sensors/isaacsim_sensors_rtx_lidar.html

* [Sensors](index.html)
* [RTX Sensors](isaacsim_sensors_rtx.html)
* RTX Lidar Sensor

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# RTX Lidar Sensor

RTX Lidar sensors are simulated at render time on the GPU with RTX hardware.
Their results are then copied to the `GenericModelOutput` AOV for use.

Warning

**Multi-GPU setups and RTX Lidar**

On systems with multiple GPUs (MGPU), some RTX Lidar assets can sometimes cause a fatal
application crash accompanied by CUDA error 700 messages in the log.

If you encounter this issue, switch to single-GPU rendering by launching
Isaac Sim with:

```python
./isaac-sim.sh --/renderer/multiGpu/enabled=false
```

In standalone Python, pass `multi_gpu=False` to the `SimulationApp` constructor.

## Overview

RTX Lidars are rendered using `OmniLidar` prims, with the `OmniSensorGenericLidarCoreAPI` schema applied,
as configured by attributes on the prim. After attaching a render product to the `OmniLidar` prim, and setting
the `GenericModelOutput` AOV on the render product, the RTXSensor renderer will write Lidar render results to the AOV.

The `OmniSensorGenericLidarCoreAPI` schema is defined in the `omni.usd.schema.omni_sensors` extension, documented [here](http://omniverse-docs.s3-website-us-east-1.amazonaws.com/omni.usd.schema.omni_sensors/107.3.0/omni_sensors_schema.html).

## How to Create an RTX Lidar

The `isaacsim.sensors.experimental.rtx` extension provides Python APIs for creating RTX Lidars. In addition, the `omni.replicator.core`
extension provides even lower-level APIs for creating `OmniLidar` prims (including batch creation) and attaching render
products to them.

### Create an RTX Lidar Using the `Lidar` Class

The `Lidar` class provides a high-level Python interface for creating and wrapping `OmniLidar` prims.
Use `Lidar.create()` to create a new sensor from a known configuration name or USD file, or `Lidar(path)`
to wrap an existing `OmniLidar` prim on the stage.

Run this snippet in the **Script Editor** (**Window > Script Editor**).

```python
import numpy as np
from isaacsim.sensors.experimental.rtx import Lidar

# Create an RTX Lidar from a known sensor configuration.
lidar = Lidar.create(
    path="/World/lidar",
    config="Example_Rotary",
    translations=np.array([0.0, 0.0, 1.0]),
    orientations=np.array([1.0, 0.0, 0.0, 0.0]),
    attributes={"omni:sensor:Core:scanRateBaseHz": 20},
)
```

The snippet above creates a reference to `Example_Rotary.usda` as an `OmniLidar` prim in the stage at the
specified `translations` with the specified `orientations`, at path `/World/lidar`. The `Example_Rotary`
config does not support variant sets, so `variant` is unused. The prim’s `omni:sensor:Core:scanRateBaseHz`
attribute is set from 10 Hz (default) to 20 Hz via the `attributes` dictionary.

Review the [OmniSensorGenericLidarCoreAPI](https://docs.omniverse.nvidia.com/kit/docs/omni.usd.schema.omni_sensors/107.3.1/omni_sensors_schema.html#omnisensorgenericlidarcoreapi)
schema and [OmniSensorGenericLidarCoreEmitterStateAPI](https://docs.omniverse.nvidia.com/kit/docs/omni.usd.schema.omni_sensors/107.3.1/omni_sensors_schema.html#omnisensorgenericlidarcoreemitterstateapi)
schema in the `omni.usd.schema.omni_sensors` extension to learn what attributes can be set on the `OmniLidar` prim.

Note

`Lidar.create()` accepts either `config` (a registered configuration name from
`isaacsim.sensors.experimental.rtx.SUPPORTED_LIDAR_CONFIGS`) **or** `usd_path` (a direct path
to an `OmniLidar` USD asset) — the two are mutually exclusive. Both `Lidar.create()` and
`Lidar(...)` accept `schemas` (a list of additional USD schemas to apply) and `attributes`
(a dict of prim attributes to author). Transforms are passed as plural arrays
(`positions=[[...]]` / `translations=[[...]]` / `orientations=[[...]]` / `scales=[[...]]`);
only `N=1` is supported per sensor.

### Tick Rate

The `tick_rate` parameter (Hz) controls how frequently the sensor renders. A value of `0`
(the default) enables autotrigger mode, where the sensor renders every simulation frame. Setting a
nonzero value causes the sensor to render at the specified frequency independently of the simulation
step rate. This maps to the `omni:sensor:tickRate` prim attribute.

Run this snippet in the **Script Editor** (**Window > Script Editor**).

```python
from isaacsim.sensors.experimental.rtx import Lidar

# Render at 10 Hz regardless of simulation frame rate.
lidar = Lidar.create("/World/Lidar", config="Example_Rotary", tick_rate=10.0)
```

Warning

For `OmniLidar` prims, `tick_rate` (i.e. `omni:sensor:tickRate`) **must** equal
`omni:sensor:Core:scanRateBaseHz` for scan accumulation and multi-tick rendering to behave
correctly. Mismatched values cause the lidar to emit partial scans every frame instead of
accumulating to a full scan, which silently breaks LaserScan publishing and any pipeline that
expects a full scan per tick. See
[OmniLidar Tick Rate Must Equal scanRateBaseHz](isaacsim_sensors_multitick_rendering.html#isaac-sim-sensors-multitick-lidar-tickrate-must-match-scanrate) for details.

Note

`tick_rate` is the recommended replacement for the deprecated `frameSkipCount` parameter
on ROS2 helper nodes. For the full migration story, see
[Multi-Tick Rendering](isaacsim_sensors_multitick_rendering.html#isaac-sim-sensors-multitick-rendering).

### Auxiliary Output Level

RTX Lidar exposes auxiliary data through the `aux_output_level` constructor parameter.
Valid values are `"NONE"` (default), `"BASIC"`, `"EXTRA"`, `"FULL"`.

Run this snippet in the **Script Editor** (**Window > Script Editor**).

```python
from isaacsim.sensors.experimental.rtx import Lidar

lidar = Lidar.create("/World/Lidar", config="Example_Rotary", aux_output_level="BASIC")
```

See [Auxiliary Output Level and the GenericModelOutput RenderVar](isaacsim_sensors_rtx.html#isaacsim-sensors-rtx-aux-output-level) for the full attribute-flow explanation and the
migration from the removed `omni:sensor:Core:auxOutputType` attribute, and
[Known issue: last-attach-wins propagation of GMO channels](isaacsim_sensors_rtx.html#isaacsim-sensors-rtx-known-issue-gmo-channels) for a known issue when multiple RTX sensors
with different auxiliary levels share a stage. See [RTX Sensor Annotators](isaacsim_sensors_rtx_annotators.html#rtx-sensor-annotator-descriptions) for
the per-level field listing.

### Scan Accumulation

The `accumulate_outputs` parameter (default `True`) controls the
`omni:sensor:Core:accumulateOutputs` prim attribute. When `True`, the lidar accumulates data
over multiple frames until a full scan is complete. For rotary lidars, a full scan corresponds to a
360-degree rotation; for solid-state lidars, a full scan covers the full azimuth sweep.

Run this snippet in the **Script Editor** (**Window > Script Editor**).

```python
from isaacsim.sensors.experimental.rtx import Lidar

# Disable accumulation to get per-frame partial scans.
lidar = Lidar.create("/World/Lidar", config="Example_Rotary", accumulate_outputs=False)
```

Warning

Scan accumulation only behaves correctly when `omni:sensor:tickRate` equals
`omni:sensor:Core:scanRateBaseHz` on the prim. With mismatched values the lidar produces
partial scans every frame regardless of `accumulate_outputs`. See
[OmniLidar Tick Rate Must Equal scanRateBaseHz](isaacsim_sensors_multitick_rendering.html#isaac-sim-sensors-multitick-lidar-tickrate-must-match-scanrate).

## How to Collect Data from an RTX Lidar

The recommended method for collecting data from an RTX Lidar is to use the `LidarSensor` runtime class,
which wraps a `Lidar` authoring object and manages Replicator Annotators.

Run this snippet in the **Script Editor** (**Window > Script Editor**).

```python
from isaacsim.sensors.experimental.rtx import Lidar, LidarSensor, parse_generic_model_output_data

lidar = Lidar.create("/World/Lidar", config="Example_Rotary")

sensor = LidarSensor(lidar, annotators=["generic-model-output"])
data, info = sensor.get_data("generic-model-output")
gmo = parse_generic_model_output_data(data)
```

Isaac Sim also offers lower-level [RTX Sensor Annotators](isaacsim_sensors_rtx_annotators.html#rtx-sensor-annotator-descriptions) that can be attached
directly to render products. Refer to [Reading Data from the GenericModelOutput Buffer](isaacsim_sensors_rtx_annotators.html#rtx-sensor-reading-gmo-buffer) for
more details on how to use the `GenericModelOutput` annotator.

## Visualizing RTX Lidar Output

There are several ways to visualize RTX Lidar point cloud data in Isaac Sim:

### Debug Draw

The [Debug Draw Extension](../utilities/debugging/ext_isaacsim_util_debug_draw.html#isaac-debug-draw) provides a performance-efficient method for visualizing point clouds directly in the viewport.
The geometry drawn with Debug Draw remains persistent across frames and does not interact with the physics scene.

The standalone example `create_lidar_basic.py` demonstrates using Debug Draw to visualize RTX Lidar output:

```python
# Basic lidar creation with debug draw visualization
./python.sh standalone_examples/api/isaacsim.sensors.experimental.rtx/create_lidar_basic.py
```

For more information on Debug Draw APIs, refer to [Debug Drawing Extension API](../utilities/debugging/ext_isaacsim_util_debug_draw.html#isaac-debug-draw) and [Util Snippets](../python_scripting/util_snippets.html#isaac-sim-app-util-snippets).

### Viewport Debug Views

You can visualize non-visual material IDs in the viewport by selecting **RTX - Real-Time** > **Debug View** > **Non-Visual Material ID**.
This shows how materials appear to RTX sensors, which is useful for debugging material configurations.
Refer to [RTX Sensor Non-Visual Materials](isaacsim_sensors_rtx_materials.html#isaacsim-sensors-rtx-materials) for details.

### RViz2 Visualization

When using ROS2, point cloud data can be visualized in RViz2. Refer to the [ROS2 Integration](#isaacsim-sensors-rtx-lidar-ros2) section below.

## ROS2 Integration

Isaac Sim provides full support for publishing RTX Lidar data to ROS2 as standard message types.

### Supported Message Types

* `sensor_msgs/PointCloud2` - Full 3D point cloud data
* `sensor_msgs/LaserScan` - 2D laser scan data (for 2D Lidar configurations)

For a comprehensive guide on integrating RTX Lidar sensors with ROS2, including:

* Adding RTX Lidar ROS2 bridge nodes via OmniGraph
* Publishing LaserScan and PointCloud2 messages
* Using the menu shortcut to create RTX Lidar sensor publishers
* Visualizing multiple sensors in RViz2
* Exposing RTX Lidar metadata (intensity, object IDs) in PointCloud2 messages

Refer to the [RTX Lidar ROS2 Tutorial](../ros2_tutorials/tutorial_ros2_rtx_lidar.html#isaac-sim-app-tutorial-ros2-rtx-lidar).

### Quick Start

To add ROS 2 publishing for an RTX Lidar sensor:

1. Create an RTX Lidar sensor using the methods described above.
2. Go to **Tools** > **Robotics** > **ROS 2 OmniGraphs** > **RTX Lidar**.
3. Configure the graph path, Lidar prim, frame ID, and select the data types to publish.
4. Press **Play** to begin publishing.

## RTX Lidar Asset Library

Isaac Sim includes a library of [RTX Lidars](../assets/usd_assets_nonvisual_sensors.html#isaac-assets-nonvisual-sensors-rtx-lidar) that can be loaded
onto the stage by specifying the `config` and `variant` parameters of `Lidar.create()`. The `config` parameter can be the following:

* The exact name of a Lidar model USD file without extension, as provided in the *Content Browser* and noted in the [RTX Lidars](../assets/usd_assets_nonvisual_sensors.html#isaac-assets-nonvisual-sensors-rtx-lidar) library (for example, `HESAI_XT32_SD10`).
* The exact name of a Lidar model USD file as noted above, omitting the vendor name (for example, `XT32_SD10`).

The optional `variant` parameter selects a specific variant of the provided Lidar configuration. `variant` accepts two forms:

* A flat string for USDs that author a single variant set named `sensor` (most configurations, including the Ouster OS family). The string is applied against that `sensor` set.
* A `dict[str, str]` mapping `{variant_set: variant_name, ...}` for USDs that author multiple variant sets (notably the SICK family, which uses `Product` and `Profile` sets). Pairs are applied in dict insertion order, so outer variant sets must come first.

The full set of supported configs and their variant shapes is exposed via `isaacsim.sensors.experimental.rtx.SUPPORTED_LIDAR_CONFIGS`; iterate over it to enumerate the available `(config, variant)` combinations programmatically.

The snippet below loads a SICK picoScan100 Lidar with the `picoScan150Pro` product and the `Profile11_15Hz_1p0deg` profile selected.

Run this snippet in the **Script Editor** (**Window > Script Editor**).

```python
from isaacsim.sensors.experimental.rtx import Lidar

# The SICK picoScan100 USD authors two variant sets ("Product" and "Profile"),
# so the variant must be passed as a dict mapping each variant set to its
# selection. For configs whose USD authors a single "sensor" variant set
# (e.g. Ouster OS1), pass a flat string instead -- e.g. variant="OS1_REV6_32ch20hz1024res".
lidar = Lidar.create(
    path="/World/lidar",
    config="picoScan100",
    variant={"Product": "picoScan150Pro", "Profile": "Profile11_15Hz_1p0deg"},
)
```

## Sensor Materials

The material system for RTX Lidar allows content creators to assign sensor material types to partial material prim names on a USD stage. Lidar return behavior depends on material properties (for example, emissivity, reflectivity),
as described below.

* [RTX Sensor Non-Visual Materials](isaacsim_sensors_rtx_materials.html)

## Standalone Examples

For examples of creating and/or collecting data from a RTX Lidar, refer to the following:

**Basic Creation and Visualization**

```python
# Basic lidar creation with debug draw visualization
./python.sh standalone_examples/api/isaacsim.sensors.experimental.rtx/create_lidar_basic.py

# Lidar with vendor configs (Ouster, SICK, HESAI) and variants
./python.sh standalone_examples/api/isaacsim.sensors.experimental.rtx/create_lidar_with_config_and_variants.py
```

**Data Collection and Inspection**

```python
# Inspect GenericModelOutput (GMO) data at different auxiliary levels
./python.sh standalone_examples/api/isaacsim.sensors.experimental.rtx/inspect_lidar_gmo.py --aux-data-level FULL

# Resolve object IDs to USD prim paths for semantic segmentation
./python.sh standalone_examples/api/isaacsim.sensors.experimental.rtx/resolve_lidar_object_ids.py
```

**Robot Integration**

```python
# Lidar + LidarSensor integration with a wheeled robot
./python.sh standalone_examples/api/isaacsim.sensors.experimental.rtx/lidar_robot_integration.py
```

**ROS2 Integration**

```python
./python.sh standalone_examples/api/isaacsim.ros2.bridge/rtx_lidar.py
```

Note

Refer to the [Isaac Sim Conventions](../reference_material/reference_conventions.html#isaac-sim-conventions) documentation for a complete list of Isaac Sim conventions.

On this page

* [Overview](#overview)
* [How to Create an RTX Lidar](#how-to-create-an-rtx-lidar)
  + [Create an RTX Lidar Using the `Lidar` Class](#create-an-rtx-lidar-using-the-lidar-class)
  + [Tick Rate](#tick-rate)
  + [Auxiliary Output Level](#auxiliary-output-level)
  + [Scan Accumulation](#scan-accumulation)
* [How to Collect Data from an RTX Lidar](#how-to-collect-data-from-an-rtx-lidar)
* [Visualizing RTX Lidar Output](#visualizing-rtx-lidar-output)
  + [Debug Draw](#debug-draw)
  + [Viewport Debug Views](#viewport-debug-views)
  + [RViz2 Visualization](#rviz2-visualization)
* [ROS2 Integration](#ros2-integration)
  + [Supported Message Types](#supported-message-types)
  + [Quick Start](#quick-start)
* [RTX Lidar Asset Library](#rtx-lidar-asset-library)
* [Sensor Materials](#sensor-materials)
* [Standalone Examples](#standalone-examples)

---

### RTX Materials

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/sensors/isaacsim_sensors_rtx_materials.html

* [Sensors](index.html)
* [RTX Sensors](isaacsim_sensors_rtx.html)
* [RTX Lidar Sensor](isaacsim_sensors_rtx_lidar.html)
* RTX Sensor Non-Visual Materials

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# RTX Sensor Non-Visual Materials

The `omni.sensors.nv.materials` extension, documented [here](http://omniverse-docs.s3-website-us-east-1.amazonaws.com/omni.sensors.nv.materials/1.6.0-coreapi/materials_extension.html), provides support for rendering materials, which are visible in non-visual spectra for RTX sensors. These materials
are referred to as “non-visual materials”.

As described in the extension documentation, non-visual materials are rendered using USD attributes, and can be specified in the USD file. Isaac Sim includes the `isaacsim.core.experimental.materials.NonVisualMaterial` class to simplify setting these attributes on `Material` prims. The renderer
will compute a material ID for each non-visual material, based on the combination of provided attributes. This material ID is provided by the `GenericModelOutput` AOV, and is exposed by multiple Annotators. Refer to [RTX Sensor Annotators](isaacsim_sensors_rtx_annotators.html#rtx-sensor-annotator-descriptions) for more details.

## Specifying Non-Visual Material Attributes

Valid non-visual material attribute names and values are specified [in Omniverse Kit documentation](https://docs.omniverse.nvidia.com/kit/docs/omni.sensors.nv.materials/latest/materials_extension.html#materials-coatings-and-attributes).

### User Interface

Attributes may be added to materials from the UI by right-clicking the material in the **Stage** window, then selecting **Add** > **Attribute**.
This will open a new window like the one below, enabling you to specify custom non-visual attributes.

After adding the new attribute, it will appear in the material’s properties, at which point it can be populated:

### Python

The `isaacsim.core.experimental.materials.NonVisualMaterial` class provides a Python API to simplify setting non-visual material attributes on `Material` prims. The following standalone example
demonstrates how to use this API. Examine the source code to learn more.

```python
./python.sh standalone_examples/api/isaacsim.sensors.experimental.rtx/apply_nonvisual_materials.py
```

After running this example, verify that you receive the following:

Observe each cube is colored differently in the visual spectrum. Select the `Non-Visual Material ID` Debug View in the viewport by selecting **RTX - Real-Time** > **Debug View** > **Non-Visual Material ID**. The following image
shows the menu selection:

After selecting the Debug View, verify that you receive the following:

The `Non-Visual Material ID` Debug View shows the material ID for each non-visual material as a color, which can be used to identify the material in the scene.
Observe each cube’s color changes compared to the default view to reflect the material ID, which is computed from the combination of non-visual material attributes applied to the visual material
applied to the cube.

Note

If you modify non-visual material attributes on a material prim, you must save and reload the stage for the changes to take effect.

## Mapping Visual Materials to RTX Sensor Non-Visual Materials (Removed)

Deprecated since version 5.1: Mapping visual materials to RTX Sensor non-visual materials via a CSV specification (the
`RtxSensorMaterialMap.csv` workflow paired with the `rtx.materialDb.rtSensorNameToIdMap`
and `rtx.materialDb.rtSensorMaterialLogs` carb settings) is no longer supported — those
settings and the CSV file are now ignored. Specify non-visual materials via USD attributes
instead — see [Specifying Non-Visual Material Attributes](#specifying-non-visual-material-attributes) above.

On this page

* [Specifying Non-Visual Material Attributes](#specifying-non-visual-material-attributes)
  + [User Interface](#user-interface)
  + [Python](#python)
* [Mapping Visual Materials to RTX Sensor Non-Visual Materials (Removed)](#mapping-visual-materials-to-rtx-sensor-non-visual-materials-removed)

---

### RTX Radar

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/sensors/isaacsim_sensors_rtx_radar.html

* [Sensors](index.html)
* [RTX Sensors](isaacsim_sensors_rtx.html)
* RTX Radar Sensor

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# RTX Radar Sensor

RTX Radar sensors are simulated at render time on the GPU with RTX hardware.
Their results are then copied to the `GenericModelOutput` AOV for use.

Warning

**Motion BVH Must Be Enabled for RTX Radar**

RTX Radar requires Motion BVH to be enabled for the Doppler effect—and therefore RTX Radar entirely—to be modeled correctly.
**Without Motion BVH enabled, RTX Radar will not produce accurate results.**

Motion BVH is disabled by default in Isaac Sim for performance reasons. You must explicitly enable it before using RTX Radar.

**To enable Motion BVH**, add the following command line arguments when launching Isaac Sim:

```python
--/renderer/raytracingMotion/enabled=true \
--/renderer/raytracingMotion/enableHydraEngineMasking=true \
--/renderer/raytracingMotion/enabledForHydraEngines='0,1,2,3,4'
```

Or in standalone Python, pass `enable_motion_bvh=True` to the `SimulationApp` constructor.

Refer to [How to Enable Motion BVH](isaacsim_sensors_rtx.html#isaac-sim-sensors-rtx-how-to-enable-motion-bvh) for complete instructions.

## Overview

RTX Radars are rendered using `OmniRadar` prims, with the `OmniSensorGenericRadarWpmDmatAPI` schema applied,
as configured by attributes on the prim. After attaching a render product to the `OmniRadar` prim, and setting
the `GenericModelOutput` AOV on the render product, the RTXSensor renderer will write Radar render results to the AOV.

## How to Create an RTX Radar

The `isaacsim.sensors.experimental.rtx` extension provides the `Radar` class for creating RTX Radars. In addition, the `omni.replicator.core`
extension provides even lower-level APIs for creating `OmniRadar` prims (including batch creation) and attaching render
products to them.

### Create an RTX Radar Using the `Radar` Class

The `Radar` class creates or wraps an `OmniRadar` prim with the appropriate schemas applied.

Run this snippet in the **Script Editor** (**Window > Script Editor**).

```python
import carb
import isaacsim.core.experimental.utils.stage as stage_utils
import numpy as np
from isaacsim.sensors.experimental.rtx import Radar

# RTX Radar requires Motion BVH to be enabled for Doppler velocity estimation.
settings = carb.settings.get_settings()
settings.set("/renderer/raytracingMotion/enabled", True)
settings.set("/renderer/raytracingMotion/enableHydraEngineMasking", True)
settings.set("/renderer/raytracingMotion/enabledForHydraEngines", "0,1,2,3,4")

# Ensure a /World Xform exists on the stage as the parent for the radar.
stage_utils.define_prim("/World", "Xform")

# Create an RTX Radar with a custom tick rate.
radar = Radar(
    path="/World/radar",
    tick_rate=10,
    translations=np.array([0.0, 0.0, 0.0]),
    orientations=np.array([1.0, 0.0, 0.0, 0.0]),
)
```

The snippet above creates an `OmniRadar` prim at path `/World/radar` with `omni:sensor:tickRate` set to 10 Hz.

Review the [OmniSensorGenericRadarWpmDmatAPI](https://docs.omniverse.nvidia.com/kit/docs/omni.usd.schema.omni_sensors/107.3.1/omni_sensors_schema.html#omnisensorgenericradarwpmdmatapi)
schema in the `omni.usd.schema.omni_sensors` extension to learn which attributes can be set on the `OmniRadar` prim.

Note

`Radar.create()` accepts `config` (from
`isaacsim.sensors.experimental.rtx.SUPPORTED_RADAR_CONFIGS`) or `usd_path` (mutually
exclusive), plus `attributes` for prim-attribute overrides and the plural transform arrays
(`positions=[[...]]` / `translations=[[...]]` / `orientations=[[...]]` / `scales=[[...]]`;
`N=1`). Additional USD schemas via `schemas=[...]` are accepted by the `Radar(...)`
constructor — pass them through `Radar(...)` directly if you need them, since
`Radar.create()` does not currently forward `schemas`.

Annotators can then be attached to the `OmniRadar` prim to collect and visualize the Radar results.
Details about available annotators can be explored [here](isaacsim_sensors_rtx_annotators.html#rtx-sensor-annotator-descriptions).

### Tick Rate

Warning

In Isaac Sim 6.0 GA, RTX Radar autotriggers regardless of `omni:sensor:tickRate` attribute. This will be corrected in a future release.

The `tick_rate` parameter (Hz) controls how frequently the sensor renders. A value of `0`
(the default) enables autotrigger mode, where the sensor renders every simulation frame. This maps to the `omni:sensor:tickRate` prim attribute.

Run this snippet in the **Script Editor** (**Window > Script Editor**).

```python
import carb
from isaacsim.sensors.experimental.rtx import Radar

# RTX Radar requires Motion BVH to be enabled.
settings = carb.settings.get_settings()
settings.set("/renderer/raytracingMotion/enabled", True)
settings.set("/renderer/raytracingMotion/enableHydraEngineMasking", True)
settings.set("/renderer/raytracingMotion/enabledForHydraEngines", "0,1,2,3,4")

# Render at 10 Hz regardless of simulation frame rate.
radar = Radar(path="/Radar", tick_rate=10.0)
```

### Auxiliary Output Level

RTX Radar exposes auxiliary data through the `aux_output_level` constructor parameter.
Valid values are `"NONE"` (default) and `"BASIC"`. Setting `"BASIC"` enables radial
velocity (`rv_ms`) in the GMO output.

Run this snippet in the **Script Editor** (**Window > Script Editor**).

```python
import carb
from isaacsim.sensors.experimental.rtx import Radar

# RTX Radar requires Motion BVH to be enabled.
settings = carb.settings.get_settings()
settings.set("/renderer/raytracingMotion/enabled", True)
settings.set("/renderer/raytracingMotion/enableHydraEngineMasking", True)
settings.set("/renderer/raytracingMotion/enabledForHydraEngines", "0,1,2,3,4")

radar = Radar(path="/Radar", aux_output_level="BASIC")
```

See [Auxiliary Output Level and the GenericModelOutput RenderVar](isaacsim_sensors_rtx.html#isaacsim-sensors-rtx-aux-output-level) for the full attribute-flow explanation and the
migration from the removed `omni:sensor:WpmDmat:auxOutputType` attribute, and
[Known issue: last-attach-wins propagation of GMO channels](isaacsim_sensors_rtx.html#isaacsim-sensors-rtx-known-issue-gmo-channels) for a known issue when multiple RTX sensors
with different auxiliary levels share a stage. See [RTX Sensor Annotators](isaacsim_sensors_rtx_annotators.html#rtx-sensor-annotator-descriptions) for
the per-level field listing.

## How to Collect Data from an RTX Radar

The recommended method for collecting data from an RTX Radar is to use the `RadarSensor` runtime class,
which wraps a `Radar` authoring object and manages Replicator Annotators, similar to `LidarSensor`.

Run this snippet in the **Script Editor** (**Window > Script Editor**).

```python
import carb
from isaacsim.sensors.experimental.rtx import Radar, RadarSensor, parse_generic_model_output_data

# RTX Radar requires Motion BVH to be enabled.
settings = carb.settings.get_settings()
settings.set("/renderer/raytracingMotion/enabled", True)
settings.set("/renderer/raytracingMotion/enableHydraEngineMasking", True)
settings.set("/renderer/raytracingMotion/enabledForHydraEngines", "0,1,2,3,4")

radar = Radar(path="/Radar")

sensor = RadarSensor(radar, annotators=["generic-model-output"])
data, info = sensor.get_data("generic-model-output")
gmo = parse_generic_model_output_data(data)
```

Refer to [RTX Sensor Annotators](isaacsim_sensors_rtx_annotators.html#rtx-sensor-annotator-descriptions) for the full list of available lower-level annotators.

## Visualizing RTX Radar Output

### Debug Draw

The [Debug Draw Extension](../utilities/debugging/ext_isaacsim_util_debug_draw.html#isaac-debug-draw) can be used to visualize RTX Radar point cloud output in the viewport.

The standalone example `create_radar_basic.py` demonstrates using Debug Draw to visualize RTX Radar output:

```python
./python.sh standalone_examples/api/isaacsim.sensors.experimental.rtx/create_radar_basic.py
```

For more information on Debug Draw APIs, refer to [Debug Drawing Extension API](../utilities/debugging/ext_isaacsim_util_debug_draw.html#isaac-debug-draw) and [Util Snippets](../python_scripting/util_snippets.html#isaac-sim-app-util-snippets).

### Doppler Effects

Important

Motion BVH must be enabled for the Doppler effect to be modeled correctly in RTX Radar simulations.
Refer to [How to Enable Motion BVH](isaacsim_sensors_rtx.html#isaac-sim-sensors-rtx-how-to-enable-motion-bvh) for instructions on enabling Motion BVH.

## Sensor Materials

The material system for RTX Radar allows content creators to assign sensor material types to partial material prim names on a USD stage. Radar return behavior depends on material properties (for example, emissivity, reflectivity),
as described below.

* [RTX Sensor Non-Visual Materials](isaacsim_sensors_rtx_materials.html)

## Standalone Examples

For examples of creating and collecting data from RTX Radar, refer to the following:

**Basic Creation and Visualization**

```python
# Basic radar creation with debug draw visualization
./python.sh standalone_examples/api/isaacsim.sensors.experimental.rtx/create_radar_basic.py
```

**Data Collection and Inspection**

```python
# Inspect radar GenericModelOutput (GMO) data
./python.sh standalone_examples/api/isaacsim.sensors.experimental.rtx/inspect_radar_gmo.py
```

**ROS 2 Integration**

For publishing RTX Radar data to ROS 2 as PointCloud2 messages, see the [RTX Radar Sensors](../ros2_tutorials/tutorial_ros2_rtx_radar.html#isaac-sim-app-tutorial-ros2-rtx-radar) tutorial.

Note

Refer to the [Isaac Sim Conventions](../reference_material/reference_conventions.html#isaac-sim-conventions) documentation for a complete list of Isaac Sim conventions.

On this page

* [Overview](#overview)
* [How to Create an RTX Radar](#how-to-create-an-rtx-radar)
  + [Create an RTX Radar Using the `Radar` Class](#create-an-rtx-radar-using-the-radar-class)
  + [Tick Rate](#tick-rate)
  + [Auxiliary Output Level](#auxiliary-output-level)
* [How to Collect Data from an RTX Radar](#how-to-collect-data-from-an-rtx-radar)
* [Visualizing RTX Radar Output](#visualizing-rtx-radar-output)
  + [Debug Draw](#debug-draw)
  + [Doppler Effects](#doppler-effects)
* [Sensor Materials](#sensor-materials)
* [Standalone Examples](#standalone-examples)

---

