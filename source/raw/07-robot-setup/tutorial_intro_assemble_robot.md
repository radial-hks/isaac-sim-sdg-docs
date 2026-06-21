---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/robot_setup_tutorials/tutorial_intro_assemble_robot.html
title: "Intro: Assemble Robot"
section: "Setup 教程"
module: "07-robot-setup"
checksum: "8630fb28fa3ae6d5"
fetched: "2026-06-21T13:05:36"
---

* [Robot Setup](../robot_setup/index.html)
* [Robot Setup Tutorials Series](index.html)
* Tutorial 2: Assemble a Simple Robot

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Tutorial 2: Assemble a Simple Robot

This tutorial guides you through the basic GUI functions that add objects to the stage. It also introduces inspecting and modifying their physics and material properties.

## Learning Objectives

This tutorial covers how to:

* Add and manipulate basic shapes
* Enable physics properties in objects
* Examine collision properties
* Edit physics properties such as friction
* Edit material properties such as color and reflectivity

## Prerequisites

* Complete [Tutorial 1: Stage Setup](tutorial_intro_environment_setup.html#isaac-sim-app-tutorial-intro-environment-setup) prior to beginning this tutorial.

## Adding Objects to the Scene

There are many ways to âadd objectsâ to the stage, but all of them fundamentally do the same thing, which is to define a USD primitive in the stage context tree. The goal is to create a basic, two wheeled robot. Start by creating some basic shapes and modifying their properties. For the body, use a cube and for the wheels use cylinders.

To create the body of the robot:

1. Create an Xform by right clicking on the stage, selecting **Create > Xform**.
2. Rename it to **body** by right clicking on it and selecting **Rename**.
3. Fix the translation of the Xform to `(0, 0, 1)` by clicking on the **Translate** section in the property panel and setting the **X** to `0`, **Y** to `0`, and **Z** to `1`.
4. Create a cube clicking **Create > Shape > Cube** in the top menu bar. You should see the cube and the **Move** **gizmo** (the red, blue, and green arrows) appear in the viewport window
5. Click and drag on the blue arrow to raise the cube above the ground plane.
6. On the left side of the app, click the Scale icon (or press the R key while the cube is selected) to activate the scale widget.
7. Click and drag on the red part of the widget to scale the cube in the x direction
8. Place the cube in a specific location. Navigate to **Transform > Scale** in the property pane, and set the scale to `(2, 1, 0.5)`.
9. Drag the cube to the **Body** Xform.

To create the wheels of the robot:

1. Create a Xform by right clicking on the stage, selecting **Create > Xform**. Set the **Translate** to `(0, 1.5, 1)` and the **Orient** to `90, 0, 0` to rotate the wheel Xform 90 degrees around the x axis.
2. Rename it to **wheel\_left** by right clicking on it and selecting **Rename**.
3. Create a cylinder by clicking **Create > Shape > Cylinder** in the top menu bar.
4. In the property panel on the bottom right corner, scroll down to the **Geometry** section. Change its **Radius** to `0.5` and **Height** to `1.0`.
5. Drag the cylinder to the **wheel\_left** Xform.
6. Rename the cylinder to **wheel\_left** by right clicking on it and selecting **Rename**.
7. Duplicate the `wheel_left` by right clicking the `wheel_left` Xform on the stage tree, select **Duplicate**, and move it to `y = -1.5` while keeping all other parameters the same.
8. Rename the duplicated Xform to **wheel\_right** by right clicking on it and selecting **Rename**.
9. Rename the duplicated cylinder to **wheel\_right** by right clicking on it and selecting **Rename**.

## Adding Physics Properties

The cubes and cylinders added so far are strictly visual prims, with no physics or collision properties attached to them.
When you start the simulation by pressing **Play** and gravity is applied, these objects do not move because they are unaffected by physics.

To make the robot have physics, turn it into a rigid body with collision properties:

1. Select the Cube and both Cylinders on the stage tree by clicking while holding down the `Ctrl + Shift` key to select each object, or just `Shift` if they are consecutively listed on the tree.
2. In the **Property** tab, click on the `+ Add` button.
3. Select **Physics > Rigid Body with Colliders Preset**.
4. Press **Play** and verify that all three objects fall to the ground.

**Rigid Body with Colliders Preset** automatically adds the Rigid Body API and the Collision API to the objects.
These two APIs can be applied separately because you can have objects that:

* have mass and are affected by gravity, but have no collision properties so you can pass through them
* can be run into but hang in the air and are not affected by gravity

To validate, add, or remove APIs assigned to the selected object:

1. Go to its **Property** tab, and scroll down to find sections labeled **Rigid Body** and **Collider**.
2. To add the APIs separately, find them under the same **+ Add** button.
3. To remove APIs, click on the `X` to delete the section.

Hint

Dynamic objects can only select from Convex Hull, Convex Decomposition, Sphere Approximation, SDF mesh (GPU backend only) for collision shapes.
Triangle mesh collision shapes are only available for static objects.

### Examine Collision Meshes

To visually examine the outlines of collision meshes for the objects:

1. Find the eye icon on top of the viewport.
2. Click **Show By Type > Physics > Colliders > All**.
3. Verify that purple outlines show up surrounding any objects that have collision APIs applied. For example, verify that it is the cuboid, the cylinders, and the ground plane.

### Adding Contact and Friction Parameters

For modifying frictional properties, you must create a different physics material and then assign it to the desired object.

1. Go to the Menu Bar and click **Create > Physics > Physics Material**.
2. Select **Rigid Body Material** in the popup box. A new `PhysicsMaterial` appears on the stage tree.
3. Tune the parameters such as friction coefficients and restitution in its property tab.

To apply the assigned physics material to an object:

1. Select the object in the stage tree.
2. Find the menu item **Materials on Selected Model** in the **Property** tab.
3. Select the desired material in the drop-down menu.

## Material Properties

The objects may reflect the color of the spotlight added earlier, but it doesnât actually have any colors assigned. You can confirm this by turning off the spotlight.

To change the color of the object, create a different material and then assign it to the objects, just like with the physics materials.
For example, create two different materials, one for the body of the car and one for the wheels.

1. Click **Create > Materials > OmniPBR** twice.
2. Right-click on the newly added materials on the stage tree and rename them to **body** and **wheel**.
3. Assign the corresponding rigid bodies to the newly created materials by going to the **Materials on selected models** item in its **Property** tab, and select the matching material from the dropdown.
4. Change the property of the new materials. Select one of them on the stage tree, change its base color in *Material and Shader/Albedo* and play with its reflectivity roughness and whatever else you find interesting.
5. Verify that you see the color of the corresponding parts on the car change accordingly.

## Summary

By the end of this tutorial, you should have a robot with a body and two wheels, similar to the `mock_robot_no_joints` asset, located in the **Samples > Rigging > MockRobot** folder.

This tutorial explained how to add and manipulate object properties in the GUI, including:

> 1. Adding primitive shapes onto the [Stage](../reference_material/reference_glossary.html#isaac-sim-glossary-stage).
> 2. Editing material properties, physics properties, and collision properties.

### Next Steps

* Continue to [Working with USD](../omniverse_usd/intro_to_usd.html#isaac-sim-app-tutorial-intro-usd) to learn how to save your world and load assets in USD format inside Isaac Sim.
* Go to [Tutorial 3: Articulate a Basic Robot](tutorial_gui_simple_robot.html#isaac-sim-app-tutorial-gui-simple-robot) to learn how to turn these geometries into a moving car.

On this page

* [Learning Objectives](#learning-objectives)
* [Prerequisites](#prerequisites)
* [Adding Objects to the Scene](#adding-objects-to-the-scene)
* [Adding Physics Properties](#adding-physics-properties)
  + [Examine Collision Meshes](#examine-collision-meshes)
  + [Adding Contact and Friction Parameters](#adding-contact-and-friction-parameters)
* [Material Properties](#material-properties)
* [Summary](#summary)
  + [Next Steps](#next-steps)