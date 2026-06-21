---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/core_api_tutorials/tutorial_core_adding_props.html
title: "Adding Props"
section: "Core API"
module: "02-fundamentals-dev"
checksum: "bfd1c47e4a8cfc5e"
fetched: "2026-06-21T13:39:54"
---

* [Python Scripting and Tutorials](../python_scripting/index.html)
* [Core API Tutorial Series](index.html)
* Adding Props

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Adding Props

## Learning Objectives

This tutorial shows how to add objects to the scene and configure them for simulation.

*10-15 Minute Tutorial*

## Adding Rubik’s Cube

Start by adding a Rubik’s Cube to the scene.

1. Create a new stage on Isaac Sim by clicking on the **File** tab and then clicking on **New Stage**.
2. In the Content Browser, go to `Isaac Sim` > `Props` > `Rubiks_Cube` > `rubiks_cube.usd` and drag and drop the `rubiks_cube.usd` file into the stage. This will add a Rubik’s Cube to the scene as a payload.
3. Left click on the Rubik’s Cube and in the properties panel, set the `Position` to `(0, 0, 0.1)`.
4. On the stage, right click `Create` > `Isaac` > `Environment` > `Flat Grid` to create a flat ground.
5. Click `PLAY` to start the simulation, you will see the Rubik’s Cube is not falling to the ground. This is because the Rubik’s Cube is not a rigid body.
6. Click `STOP` to stop the simulation.

## Configure Physics Properties

### Add Rigid Body Properties

1. Right click on the Rubik’s Cube and select `Add` > `Physics` > `Rigid Body`. This will add a rigid body attribute to the Rubik’s Cube and it will be affected by physics.
2. Now, click `PLAY` to start the simulation, you will see the Rubik’s Cube fall through the ground, this is because the Rubik’s Cube does not have a collision shape. Click `STOP` to stop the simulation.

### Add Collision Properties

1. Right click on the Rubik’s Cube and select `Add` > `Physics` > `Collider Presets`. This will add a collision attribute to the Rubik’s Cube and it will collide with other objects.
2. Now, click `PLAY` to start the simulation, you will see the Rubik’s Cube fall on the ground. Click `STOP` to stop the simulation.

### Add Mass

In addition to collision, you can also add mass, inertia, and center of mass to the Rubik’s Cube to configure its physical properties.

1. Right click on the Rubik’s Cube and select `Add` > `Physics` > `Mass`. This will add a mass attribute to the Rubik’s Cube.
2. In the properties panel, scroll down to the `Mass` section and set the `Mass` to `0.1` to make it weigh 100 grams.

Note

In addition to mass, you can also set the `Density`, `Center of Mass`, `Diagonal Inertia`, and `Principal Axes` of the object.

Setting the mass to 0 will make the simulation to compute it at runtime based on its volume (assuming 1000 kg/m^3 if density is not specified).

### Visualize Collision Shapes

Right click on the `Eye` on the top left of the viewport and select `Show By Type` > `Physics` > `Coliders` > `All`. This will show the collision shapes everything in the scene.

The ground plane’s collider is pink to denote it is a static object. The Rubik’s Cube is a dynamic object, so it falls to the ground and its collider is green.

Note

You can adjust the collider type by left clicking on the `RubikCube` mesh at `World/rubiks_cube/RubikCube` and scroll down to the `Physics/Collider` section, and select a different approximate type in the `Approximation` tab.

### Customize Collider

Let’s customize the collider for the Rubik’s Cube, by making it a sphere and easier to roll

1. Left click on the `RubikCube` mesh at `World/rubiks_cube/RubikCube` and scroll down to the `Physics/Collider` section, press the `x` on the right to delete the current collider.
2. Left click on the `rubiks_cube` Xform and select `Create` > `Shape` > `Sphere`. This will add a sphere shape around the Rubik’s Cube.
3. Scroll down to the `Geometry` section and set the `Radius` to `0.07` to make the sphere smaller to match the Rubik’s Cube.
4. Add a Collider to the sphere by selecting `Add` > `Physics` > `Collider Presets`.
5. Hide the Sphere by unckecking the eye icon to the right of the sphere on the stage.
6. Slant the groundplane by going to `FlatGrid` and Click on `Toggle Offset Mode` icon on the right of `Transform` in the Properties panel, then setting the `Rotation` to `(10, 0, 0)` to give it a 10 degree slope.
7. Click `PLAY` to start the simulation, you will see the Rubik’s Cube rolls on the ground. Click `STOP` to stop the simulation.

### Add Physics Materials

You can also apply surface properties to the Rubik’s Cube by adding a physics material.

1. Left click on the Rubik’s Cube and in the properties panel, set the `Position` to `(0, 0, 1)` to move it up.
2. Right click on the Rubik’s Cube and select `Create` > `Physics` > `Physics Material`. Check `Rigid Body Material`. This will add a physics material attribute to the Rubik’s Cube. Drag it to the `World/rubiks_cube/Looks` scope.
3. In the properties panel, scroll down to the `Physics Material` section and set the `Restitution` to `1` to make it bounce.
4. Select the `Sphere` collider we created earlier and in the properties panel, scroll down to the `Physics/Physics material on selected Material` section and select the `Physics Material` we just created at `/World/rubiks_cube/Looks/PhysicsMaterial`.
5. Click `PLAY` to start the simulation, you will see the Rubik’s Cube rolls on the ground and bounces. Click `STOP` to stop the simulation.

Note

You can also set the `Static Friction` and `Dynamic Friction` as well.

Note

The completed asset is available at `Isaac Sim` > `Samples` > `Rigging` > `RubiksCube` > `rubiks_cube.usd` in the Content Browser.

### Tips

* Object rigid body api should be applied to the default prim of the object.
* collision API should be applied to the mesh prim of the object, and it should be applied as a **physXSchema**

### What’s Next?

Extending from the concepts above, you assemble more complex collision shapes using basic shapes. For example, in the image below, we approximated a bearing collider using cylinders and rectangles.

## Summary

This tutorial covered the following topics:

1. Adding objects to the scene.
2. Configuring object physics properties.
3. Customize object collision shapes.
4. Apply physics materials to objects.

On this page

* [Learning Objectives](#learning-objectives)
* [Adding Rubik’s Cube](#adding-rubik-s-cube)
* [Configure Physics Properties](#configure-physics-properties)
  + [Add Rigid Body Properties](#add-rigid-body-properties)
  + [Add Collision Properties](#add-collision-properties)
  + [Add Mass](#add-mass)
  + [Visualize Collision Shapes](#visualize-collision-shapes)
  + [Customize Collider](#customize-collider)
  + [Add Physics Materials](#add-physics-materials)
  + [Tips](#tips)
  + [What’s Next?](#what-s-next)
* [Summary](#summary)