---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/robot_setup_tutorials/tutorial_generate_robot_config.html
title: "Generate Robot Config"
section: "Setup 教程"
module: "07-robot-setup"
checksum: "e657554dab03344c"
fetched: "2026-06-21T14:14:34"
---

* [Robot Setup](../robot_setup/index.html)
* [Robot Setup Tutorials Series](index.html)
* Tutorial 8: Generate Robot Configuration File

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Tutorial 8: Generate Robot Configuration File

## Learning Objectives

This is the third manipulator tutorial in a series of four tutorials. This tutorial will show you how to generate the robot configuration file for the UR10e robot from Universal Robots and the 2F-140 gripper from Robotiq.
These robot configuration files provide information about the robot’s kinematics, dynamics, and other properties that are used in RMPFlow and [cuMotion](https://nvidia-isaac.github.io/cumotion/) motion planners.

*30 Minutes Tutorial*

## Prerequisites

* Review [Tutorial 7: Configure a Manipulator](tutorial_configure_manipulator.html) tutorial prior to beginning this tutorial, continue the following steps from the asset built in the previous tutorial.

Note

If you have not completed the previous tutorial, you can find the prebuilt asset in the content browser at `Isaac Sim/Samples/Rigging/Manipulator/configure_manipulator/ur10e/ur/ur_gripper.usd`.

## Generate Robot URDF

Generate the robot URDF file from the UR10e robot and the 2F-140 gripper.

### Enable the Isaac Sim USD to URDF Exporter Extension

1. Go to **Window** > **Extensions**.
2. Type **URDF** in the search box, and find the **Isaac Sim USD to URDF Exporter Extension**.
3. If you can’t find it, remove the **@feature** filter from the search box.
4. Enable the extension by clicking the toggle button labeled **ENABLE**.
5. Check the box for **AUTOLOAD**, just to the right of **ENABLE**.

### Export the URDF File

1. Open the `ur_gripper.usd` asset you made in the previous tutorial, or use the completed asset provided above.
2. Click **File** > **Export URDF**.
3. In File name on the bottom left corner, save the file name to `robot.urdf`.

   Tip

   Using `robot.urdf` matches the default `--urdf` value in the pick-and-place tutorial scripts, so you won’t need to pass `--urdf` explicitly when running them.
4. In the **Mesh Directory Path** field, select the correct folder path to save the URDF meshes.
5. Click **Export**.

Note

Learn more about the USD to URDF Exporter Extension in the [USD to URDF Exporter Extension](../importer_exporter/ext_omni_exporter_urdf.html#isaac-sim-app-extension-urdf-exporter) manual.

## Generate Robot Description Files and Collision Spheres

Generate the XRDF file and collision spheres for the UR10e robot and the 2F-140 gripper.

### Enable the Robot Description Editor Extension

1. Go to **Window** > **Extensions**.
2. Search for `isaacsim.robot_setup.xrdf_editor` and find the **cuMotion/Lula Robot Description Editor** extension.
3. If you can’t find it, remove the **@feature** filter from the search box.
4. Enable the extension by clicking the toggle button labeled **ENABLE**.
5. Check the box for **AUTOLOAD**, just to the right of **ENABLE**.

### Prepare the Robot Asset

The Robot Description Editor does not support instanceable meshes. You must prepare the robot asset by disabling instanceable meshes.

1. Open the `ur_gripper.usd` asset you made in the previous tutorial, or use the completed asset provided above.
2. Select all `visuals` and `collisions` prims on the stage.
3. In the **Property** panel, uncheck the **Instanceable** checkbox for each.

   Hint

   You can use the search feature to find the `visuals` and `collisions` prims by searching for `visuals` and `collisions` respectively.

The **Instanceable** checkbox (highlighted in red) should be unchecked for all geometry prims.

### Configure Joint Properties

1. Press **Play** to start the simulation.
2. Open the editor via **Tools** > **Robotics** > **cuMotion/Lula Robot Description Editor**.
3. In the **Selection Panel**, set **Select Articulation** to the **ur** articulation prim path.
4. In **Set Joint Properties**, assign each joint a **Joint Status**:

   * Mark each Universal Robots arm joint as **Active Joint**. These joints are directly controlled by cuMotion.
   * Keep the Robotiq 2F-140 gripper joints as **Fixed Joint**. cuMotion holds these joints at the specified default position.

Important

**Do not stop the simulation**, you will need it to generate the collision spheres.

Pay attention to the default joint positions for fixed joints. They should match the initial pose defined in the manipulator USD, or you will need to reset the robot to those positions during task initialization.

### Generate Collision Spheres

Important

**Do not stop the simulation** or exit the Robot Description Editor during this step, or you will need to redo the previous steps.

Repeat the following for each link in the **ur** articulation, including gripper links:

1. In the **Selection Panel**, select the link under **Select Link**. Use **upper\_arm\_link** as an example.
2. In **Link Sphere Editor** > **Generate Spheres**, select a mesh from the **Select Mesh** dropdown (e.g. `/collisions/upperarm/mesh`).
3. Set the **Radius Offset** and **Number of Spheres** (e.g. `0.03` and `8` respectively).
4. Optionally adjust sphere positions by clicking and dragging them in the viewport.
5. Click **GENERATE SPHERES**. The spheres will turn cyan when finalized.

Suggested per-link sphere settings (ur10e + Robotiq 2F-140)

For links with multiple mesh entries, generate spheres for each mesh and combine them on the same link.

| Select Link | Number of Spheres | Radius Offset | Select Mesh |
| --- | --- | --- | --- |
| `/shoulder_link` | 1 | 0.03 | `/collisions/shoulder/mesh` |
| `/upper_arm_link` | 8 | 0.03 | `/visuals/upperarm/mesh` |
| `/forearm_link` | 8 | 0.03 | `/visuals/forearm/mesh` |
| `/wrist_1_link` | 1 | 0.03 | `/visuals/wrist1/mesh` |
| `/wrist_2_link` | 1 | 0.02 | `/visuals/wrist3/mesh` |
| `/wrist_3_link` | 1 | 0.02 | `/visuals/wrist3/mesh` |
| `/ee_link/robotiq_arg2f_base_link` | 1 | 0.02 | `/visuals/robotiq_arg2f_base_link/mesh` |
| `/ee_link/left_outer_knuckle` | 2 | 0.02 | `/visuals/robotiq_arg2f_140_outer_knuckle/mesh` |
| `/ee_link/left_outer_knuckle` | 2 | 0.02 | `/visuals/robotiq_arg2f_140_outer_finger/mesh` |
| `/ee_link/left_inner_finger` | 2 | 0.02 | `/collisions/robotiq_arg2f_140_inner_finger/mesh` |
| `/ee_link/right_inner_finger` | 2 | 0.02 | `/collisions/robotiq_arg2f_140_inner_finger/mesh` |
| `/ee_link/left_inner_knuckle` | 2 | 0.02 | `/visuals/robotiq_arg2f_140_inner_knuckle/mesh` |
| `/ee_link/right_inner_knuckle` | 2 | 0.02 | `/visuals/robotiq_arg2f_140_inner_knuckle/mesh` |
| `/ee_link/right_outer_knuckle` | 2 | 0.02 | `/visuals/robotiq_arg2f_140_outer_knuckle/mesh` |
| `/ee_link/right_outer_knuckle` | 2 | 0.02 | `/visuals/robotiq_arg2f_140_outer_finger/mesh` |

Spheres generated for the upper\_arm\_link.

Spheres generated for the full ur10e robot.

General tuning tips

* Size spheres to cover the link without being oversized — large spheres cause solver conservatism.
* More spheres improves collision accuracy but reduces solver performance.
* For long cylindrical links, generate spheres on the ends and use **Connect Spheres** to fill the middle evenly.
* Use **Scale Spheres in Link** to resize spheres uniformly across a link.
* The auto-generator requires water-tight triangle meshes. If it fails for a link, add and connect spheres manually.

### Export to XRDF

Important

**Do not stop the simulation** before exporting.

1. At the bottom of the Robot Description Editor, expand **Export To File** > **Export to cuMotion XRDF**.
2. Click the file icon and specify the file name as `robot.xrdf`.
3. Select the XRDF version to export (version 2.0 is recommended).
4. Click **Save**. Save to the same directory as the robot URDF file.
5. Stop the simulation after the file is exported.

### Adding a Tool to the Robot Configuration

[cuMotion](https://nvidia-isaac.github.io/cumotion/) requires a tool frame defined in the XRDF file. The tool frame is used to specify the end-effector frame for the robot.

1. Open the `robot.xrdf` file in a text editor.
2. Add the following line to the file:

   ```python
   tool_frames: ["wrist_3_link"]
   ```

See [Robot Configuration Tutorial](../cumotion/tutorial_robot_configuration.html#isaac-sim-cumotion-tutorial-robot-configuration) for more information on XRDF files and loading robot configurations into cuMotion.

## Assemble the Robot Configuration Directory

The pick-and-place tutorial scripts and the `load_cumotion_robot` API expect all robot configuration files to live in a single directory. After completing the export steps above, your directory should look like this:

```python
/path/to/robot/config/
├── robot.urdf
├── robot.xrdf
├── rmp_flow.yaml
└── meshes/
    └── ...
```

Pass this directory to the tutorial scripts with `--xrdf-dir /path/to/robot/config`. For a full description of these files and how they are used by cuMotion, see the [Robot Configuration Files](../cumotion/tutorial_robot_configuration.html#isaac-sim-cumotion-tutorial-robot-configuration) section of the cuMotion tutorial.

The `rmp_flow.yaml` file configures the RMPflow reactive motion controller. Save the text below in a file named `rmp_flow.yaml` and save it to the same directory as your `robot.urdf` and `robot.xrdf` files.

rmp\_flow.yaml — RMPflow configuration example

```python
format: rmpflow
api_version: 2.0

joint_limit_buffers: [.01, .01, .01, .01, .01, .01]

rmp_params:
    cspace_target_rmp:
        metric_scalar: 50.
        position_gain: 100.
        damping_gain: 50.
        robust_position_term_thresh: .5
        inertia: 1.
    cspace_trajectory_rmp:
        p_gain: 80.
        d_gain: 10.
        ff_gain: .25
        weight: 50.
    cspace_affine_rmp:
        final_handover_time_std_dev: .25
        weight: 2000.
    joint_limit_rmp:
        metric_scalar: 1000.
        metric_length_scale: .01
        metric_exploder_eps: 1e-3
        metric_velocity_gate_length_scale: .01
        accel_damper_gain: 200.
        accel_potential_gain: 1.
        accel_potential_exploder_length_scale: .1
        accel_potential_exploder_eps: 1e-2
    joint_velocity_cap_rmp:
        max_velocity: 2.15
        velocity_damping_region: 0.5
        damping_gain: 300.
        metric_weight: 100.
    target_rmp:
        accel_p_gain: 80.
        accel_d_gain: 120.
        accel_norm_eps: .075
        metric_alpha_length_scale: .05
        min_metric_alpha: .01
        max_metric_scalar: 10000.
        min_metric_scalar: 2500.
        proximity_metric_boost_scalar: 20.
        proximity_metric_boost_length_scale: .02
        accept_user_weights: false
    axis_target_rmp:
        accel_p_gain: 200.
        accel_d_gain: 40.
        metric_scalar: 10.
        proximity_metric_boost_scalar: 3000.
        proximity_metric_boost_length_scale: .05
        accept_user_weights: false
    collision_rmp:
        damping_gain: 50.
        damping_std_dev: .04
        damping_robustness_eps: 1e-2
        damping_velocity_gate_length_scale: .01
        repulsion_gain: 1000.
        repulsion_std_dev: .01
        metric_modulation_radius: .5
        metric_scalar: 500.
        metric_exploder_std_dev: .02
        metric_exploder_eps: .001
    damping_rmp:
        accel_d_gain: 30.
        metric_scalar: 50.
        inertia: 100.

canonical_resolve:
    max_acceleration_norm: 50.
    projection_tolerance: .01
    verbose: false

body_capsules:
    - name: base_link
      pt1: [0, 0, 0.22]
      pt2: [0, 0, 0]
      radius: .09

body_collision_controllers:
  - name: wrist_2_link
    radius: .04
  - name: wrist_3_link
    radius: .04
```

## Summary

In this tutorial, you have learned how to generate the robot configuration files for the UR10e robot and the 2F-140 gripper using the [Robot Description Editor](../manipulators/manipulators_robot_description_editor.html#isaac-sim-app-tutorial-motion-generation-robot-description-editor) and the [USD to URDF Exporter Extension](../importer_exporter/ext_omni_exporter_urdf.html#isaac-sim-app-extension-urdf-exporter) extensions. The resulting XRDF file can be loaded directly into cuMotion motion planners as described in [Robot Configuration Tutorial](../cumotion/tutorial_robot_configuration.html#isaac-sim-cumotion-tutorial-robot-configuration).

On this page

* [Learning Objectives](#learning-objectives)
* [Prerequisites](#prerequisites)
* [Generate Robot URDF](#generate-robot-urdf)
  + [Enable the Isaac Sim USD to URDF Exporter Extension](#enable-the-isaac-sim-usd-to-urdf-exporter-extension)
  + [Export the URDF File](#export-the-urdf-file)
* [Generate Robot Description Files and Collision Spheres](#generate-robot-description-files-and-collision-spheres)
  + [Enable the Robot Description Editor Extension](#enable-the-robot-description-editor-extension)
  + [Prepare the Robot Asset](#prepare-the-robot-asset)
  + [Configure Joint Properties](#configure-joint-properties)
  + [Generate Collision Spheres](#generate-collision-spheres)
  + [Export to XRDF](#export-to-xrdf)
  + [Adding a Tool to the Robot Configuration](#adding-a-tool-to-the-robot-configuration)
* [Assemble the Robot Configuration Directory](#assemble-the-robot-configuration-directory)
* [Summary](#summary)