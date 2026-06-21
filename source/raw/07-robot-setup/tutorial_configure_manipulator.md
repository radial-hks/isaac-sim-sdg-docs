---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/robot_setup_tutorials/tutorial_configure_manipulator.html
title: "Configure Manipulator"
section: "Setup 教程"
module: "07-robot-setup"
checksum: "e73e712716158997"
fetched: "2026-06-21T13:05:35"
---

* [Robot Setup](../robot_setup/index.html)
* [Robot Setup Tutorials Series](index.html)
* Tutorial 7: Configure a Manipulator

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Tutorial 7: Configure a Manipulator

## Learning Objectives

This is the second manipulator tutorial in a series of four tutorials. This tutorial shows how to configure physics, joint effort limits, and gains for the UR10e robot from Universal Robots and the 2F-140 gripper from Robotiq.

*30 Minutes Tutorial*

## Prerequisites

* Review [Tutorial 6: Setup a Manipulator](tutorial_import_assemble_manipulator.html) tutorial prior to beginning this tutorial. The steps here continue from the asset built in the previous tutorial.

Note

If you have not completed the previous tutorial, you can find the prebuilt asset in the content browser at `Isaac Sim/Samples/Rigging/Manipulator/configure_manipulator/ur10e/ur_gripper/ur.usda`.
We highly recommend downloading the prebuilt asset to your local machine for easier access.

## Adjust the Articulation for Manipulation Tasks

Adjust the articulation for the UR10e robot to make it more stable and accurate for manipulation tasks. Letâs first open the physx layer, and create a physx articulation root.

1. Open the interface file, `ur.usda`, and select the layer lab on the top right corner
2. Click âInsert Sublayerâ icon at the bottom of the layer panel. (orange arrow with stacked layers icon)
3. In the file dialog, navigate to `path/to/Manipulator/configure_manipulator/ur10e/ur_gripper/payloads/Physics/`, select `physx.usda`, and click **Open** to insert it as a sublayer.

1. Left click on physx.usda layer, then right click to select âSet Authoring Layerâ. Now all your changes will be saved to the physx.usda layer.

1. In the Stage panel, select the **ur/Geometry/World** prim.
2. In the Property Editor at the bottom right, scroll down to the **Physics/Articulation** section. If you do not see an Articulation(PhysX), create a new one by clicking the **add** > **Physics** > **Articulation(PhysX)**.
3. Select **Articulation Enabled**.
4. Increase the **Solver Position Iterations Count** to `64`.
5. Increase the **Solver Velocity Iterations Count** to `4`.

   Note

   The **Solver Position Iterations Count** and **Solver Velocity Iterations Count** are used to control the accuracy of the simulation.

   For a complex robot with many degrees of freedoms and mimic joints, increasing these values will make the simulation more accurate at the cost of performance.
   See [articulation documentation](https://nvidia-omniverse.github.io/PhysX/physx/5.6.0/docs/Articulations.html#articulation-drive-stability) for more information.
6. Decrease **Sleep Threshold** to `0.00005`, this lowers the threshold for the robot to go to sleep when it is not moving. see [rigid body dynamics documentation](https://nvidia-omniverse.github.io/PhysX/physx/5.6.0/docs/RigidBodyDynamics.html#sleeping) for more information.
7. Decrease the **Stabilization Threshold** to `0.00001`, this lowers the threshold for the robot to start stabilizing itself when it is not moving. see [articulation documentation](https://nvidia-omniverse.github.io/PhysX/physx/5.6.0/docs/Articulations.html#articulation-drive-stability) for more information.
8. Next to the physx.usda (Authoring Layer) label, click the blue files icon to save the changes to the physx.usda layer.
9. Verify that in physx.usda layer, the Articulation(PhysX) prim is created and the properties are set correctly.

```python
over "Geometry"
 {
     over "world" (
         prepend apiSchemas = ["PhysxArticulationAPI"]
     )
     {
         float physxArticulation:sleepThreshold = 0.00005
         int physxArticulation:solverPositionIterationCount = 64
         int physxArticulation:solverVelocityIterationCount = 4
         float physxArticulation:stabilizationThreshold = 0.00001

         over "base_link"
         {
             string isaac:nameOverride (
                 displayName = "Name Override"
             )
         }
     }
 }
```

Note

See [PhysX Best Practice Guide](https://nvidia-omniverse.github.io/PhysX/physx/5.6.0/docs/BestPractices.html#jointed-objects-are-unstable) for tuning the articulation for manipulation tasks.

## Add Physics Materials

Add physics materials to the robot gripper to make it more realistic and stable for manipulation tasks.

1. Open the physics layer from the 2F-140 gripper asset from the last tutorial. It is located in the `configuration` folder with suffix `_physics`.

   Note

   If you have not completed the previous tutorial, you can find the prebuilt asset in the content browser at `Isaac Sim/Samples/Rigging/Manipulator/import_manipulator/robotiq_2f_140/configuration/robotiq_2f_140_physics.usd`.
2. Right click on the **robotiq\_arg2f\_140\_model** prim and select **Create** > **Physics** > **Physics Material**, select **Rigid Body Material**. This will add a physics material attribute to the gripper.
3. In the properties panel, scroll down to the **Physics/Rigid Body Material** section and set the **static friction** to **1.0** and **dynamic friction** to **1.0**. For your robot, match the friction values to the robotâs surface friction coefficients.
4. Apply the physics material to the gripper finger tip.
   - Select the `colliders/left_inner_finger/mesh_1/box` and in the properties panel, scroll down to the **Physics/Physics material on selected Material** section.
   - Select the **Physics Material** you just created at `/World/robotiq_arg2f_140_model/Looks/finger`.
5. Repeat the same process for the `colliders/right_inner_finger/mesh_1/box` prim.

Note

See [Adding Props](../core_api_tutorials/tutorial_core_adding_props.html#isaac-sim-app-tutorial-core-adding-props) for more information on how to add physics materials to the robot.

## Configure Joint Effort Limits

In the physics layer of the robotiq\_arg2f\_140\_model asset from the previous step, letâs configure the joint effort limits for the gripper.

1. In the **Stage** panel, select the `robotiq_arg2f_140_model/joints/finger_joint` prim. This is the joint that controls the gripper fingers, all other gripper joints are `Mimic` joints.
2. In the **Property Editor** at the bottom right, scroll down to the `Drive/Angular/Max Force` section.
3. Set the **Max Force** to `200`. This is the maximum force that can be applied to the gripper fingers. For your robot, match the max force to the robotâs joint torque limits.
4. **Ctrl + S** to save the changes.

Note

When the max force is very high, you might need to increase the physics step frequency (`Time Step per Second`) to avoid penetration and instabilities.

## Inspect the Robot Articulation

Letâs inspect the robot articulation to verify the joint effort limits are applied correctly. Open the top level `ur` asset that you built in the previous tutorial.
This asset references the physics layers that you modified, so all the changes you made to the physics layer will be reflected in this asset.

Note

You can find the prebuilt asset in the content browser at `Isaac Sim/Samples/Rigging/Manipulator/configure_manipulator/ur10e/ur_set_physx/ur.usda`.

1. Open the **Physics Inspector** through **Tools** > **Physics** > **Physics Inspector**.
2. Select the UR articulation in the stage, click on the circular arrow icon to refresh the articulation.
3. Try changing the target position with the blue slider and verify that the DOF position reaches the target specified.
4. Close the **Physics Inspector** window/panel (discarding any changes authored by this tool, if prompted).

   Warning

   Since the Physics Inspector partially initializes `omni.physx`, it is expected for general simulations to not behave properly when the tool is opened.

## Summary

In this tutorial, you learned how to configure the physics, joint effort limits, and gains for the UR10e robot from Universal Robots and the 2F-140 gripper from Robotiq using the Gain Tuner.
You added physics materials to the robot gripper to make it more realistic and stable for manipulation tasks.
You inspected the robot articulation and tuned the gains for the robot and the gripper fingers joints using the Physics Inspector.

On this page

* [Learning Objectives](#learning-objectives)
* [Prerequisites](#prerequisites)
* [Adjust the Articulation for Manipulation Tasks](#adjust-the-articulation-for-manipulation-tasks)
* [Add Physics Materials](#add-physics-materials)
* [Configure Joint Effort Limits](#configure-joint-effort-limits)
* [Inspect the Robot Articulation](#inspect-the-robot-articulation)
* [Summary](#summary)