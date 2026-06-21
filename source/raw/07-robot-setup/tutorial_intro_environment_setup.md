---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/robot_setup_tutorials/tutorial_intro_environment_setup.html
title: "Intro: Environment Setup"
section: "Setup 教程"
module: "07-robot-setup"
checksum: "9ec2002929a7013c"
fetched: "2026-06-21T13:40:07"
---

* [Robot Setup](../robot_setup/index.html)
* [Robot Setup Tutorials Series](index.html)
* Tutorial 1: Stage Setup

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Tutorial 1: Stage Setup

Isaac Sim is built on [NVIDIA Omniverse](https://docs.omniverse.nvidia.com/) using tools provided in [Omniverse Kit](https://docs.omniverse.nvidia.com/dev-guide/latest/index.html "(in Omniverse Developer Guide)"). Omniverse Kit comes with a default UI that
allows you to edit a USD stage with ease. In this tutorial, you learn the basic steps for setting up an environment, adding and editing simple objects and their properties on a USD stage,
rigging rigid bodies with joints and articulations, and adding cameras and sensors.
The goal is to build your basic skills in navigating Isaac Sim, becoming familiar with frequently used terms, and using the GUI to build an environment and set up your robots.

## Learning Objectives

This tutorial teaches you to build a physics-enabled virtual world using the tools provided in the Isaac Sim GUI, including:

* Setup global stage properties
* Setup global physics properties
* Add ground plane
* Add lighting

## Prerequisites

To start with a clean Isaac Sim stage, go to the File menu and click on **New**.
The stage provided has a default `World` [Xform](https://docs.omniverse.nvidia.com/utilities/latest/common/glossary-of-terms.html#term-XForm "(in Omniverse Utilities)"), and a `defaultLight`. Both can be found on the stage tree on the right of the viewport.

## Setting up Stage Properties

Before anything is added onto the stage, verify that the current stage property setup matches the your expected conventions.

1. Go to **Edit > Preferences** to open up the Preference panel.
2. Browse the many types of settings inside Omniverse Kit grouped into categories in the column on the left of the panel.
3. Select **Stage** from the left column and review the properties such as:

   * The axis that determines *Up*. The default in Isaac Sim is Z. If your asset is created in a program with a different up-axis, it causes your assets to be imported rotated.
   * Stage units. Isaac Sim versions prior to 2022.1 have stage units in centimeters, but the default is now meters. However, the default units for Omniverse Kit is still in centimeters. Keep that in mind if you see USD units that are seemingly off by 100x.
   * Default rotation order. The default is set to execute rotation in Z, then Y, and last X.

## Creating the Physics Scene

To add a **Physics Scene** to simulate real world physics, including gravity and physics time steps:

1. Go to the Menu Bar and click **Create > Physics > Physics Scene**.
2. Validate that a **PhysicsScene** is added to the stage tree.
3. Click on it to examine its properties.
   You can see that gravity is set to the magnitude of `Earth Gravity`, or `9.8` meters per second squared. Remember that the default unit of length is meters.
4. Unless you are simulating hundreds of rigid bodies and robots, it is more efficient to use CPU physics
   :   * Open Physics Scene’s **Property** tab
       * Uncheck **Enable GPU dynamics**
       * Set the **Broadphase** type to **MBP**.

## Adding a Ground Plane

The ground plane prevents any physics-enabled objects from falling below it.
The ground plane’s collision property extends indefinitely even though the plane is only visible up to 25 meters in each direction.

To add a ground plane to the virtual environment:

1. Go to the top Menu Bar and click **Create > Physics > Ground Plane**.
2. Turn on the grid by clicking on  and selecting **Grid** to make the ground plane easier to see.

## Lighting

Every new [Stage](../reference_material/reference_glossary.html#isaac-sim-glossary-stage) is pre-populated with a `defaultLight`, otherwise you wouldn’t see anything. This default light is a child of the `Environment` Xform in the stage and can be found in the stage context tree.

To create additional spotlights:

1. Add a ground plane, if there isn’t already one, so we can see the reflection of the light. **Create > Physics > Ground Plane**.
2. Go to **Create > Light > Sphere Light**.
3. Pose the light on the stage.
   - In the **Stage** tab on the top right, select the newly created light in the stage tree.
   - In the **Property** tab on the bottom , in the **Transform** section use the **Translate** tool to move it to a position above the ground plane, such as `(0, 0, 7)`.
   - In the **Property** tab, in the **Transform** section, use the **Orient** tool to set the rotation to `(0, 0, 0)`.
4. Modify light color, brightness, and scope properties:
   - Inside the **Property** tab, change its color in **Main > Color** by clicking on the color bar and pick a color of your choice. For example a light green color `(RGB: 0.5, 1.0, 0.5)`.
   - Also inside the **Property** tab, change its intensity **Main > Intensity** to **1e6**; **Main > Radius** to **0.05**
   - In the **Shaping** section, change the **cone:angle** to **45** degrees and **cone:softness** to **0.05**.
5. To make the new spotlight easier to see, we will reduce the intensity of the default light by going to its **Property** tab and set **Main > Intensity** to **300**.

## Summary

This tutorial begins the necessary steps to create a virtual world suitable for physics simulation and testing Isaac Sim.
The following topics were covered:

* Adding a ground plane, lighting, and physics scene.

### Next Steps

Continue on to [Tutorial 2: Assemble a Simple Robot](tutorial_intro_assemble_robot.html#isaac-sim-app-tutorial-intro-assemble-robot) to learn how to add simple objects to Isaac Sim and edit their properties.

### Further Learning

For more in-depth and creative world-building tools, refer to our sister Omniverse tool [Composer](https://docs.omniverse.nvidia.com/composer/latest/index.html "(in Omniverse USD Composer)").

On this page

* [Learning Objectives](#learning-objectives)
* [Prerequisites](#prerequisites)
* [Setting up Stage Properties](#setting-up-stage-properties)
* [Creating the Physics Scene](#creating-the-physics-scene)
* [Adding a Ground Plane](#adding-a-ground-plane)
* [Lighting](#lighting)
* [Summary](#summary)
  + [Next Steps](#next-steps)
  + [Further Learning](#further-learning)