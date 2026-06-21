---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/physics/ext_isaacsim_inspect_physics.html
title: "Inspect Physics"
section: "物理"
module: "06-simready-assets"
checksum: "269acb17bc424056"
fetched: "2026-06-21T13:58:07"
---

* [Robot Setup](../robot_setup/index.html)
* [Inspector Tools](../robot_setup/inspector_tools.html)
* Simulation Data Visualizer

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Simulation Data Visualizer

The [Simulation Data Visualizer](#isaac-inspect-physics) is used to visualize information for the selected prim. You can use this tool to better understand the behaviors of physics-enabled geometry during simulation.

If a non-physics prim is selected, position changes over the course of simulation are tracked. However, when a physics element is selected, it shows more physics properties, including position and velocities (linear, angular).

## Conventions

The simulation data visualizer provides the following information:

* **Position**: in [Stage](../reference_material/reference_glossary.html#isaac-sim-glossary-stage) units [X, Y, Z]
* **Rotation**: in degrees [X, Y, Z]
* **Linear Velocity**: in [Stage](../reference_material/reference_glossary.html#isaac-sim-glossary-stage) units/s
* **Angular Velocity**: in degrees/s
* **Linear Acceleration**: in [Stage](../reference_material/reference_glossary.html#isaac-sim-glossary-stage) units/s^2
* **Mass**: in [Stage](../reference_material/reference_glossary.html#isaac-sim-glossary-stage) mass unit
* **Moment of Inertia**: in [Stage](../reference_material/reference_glossary.html#isaac-sim-glossary-stage) mass unit\*[Stage](../reference_material/reference_glossary.html#isaac-sim-glossary-stage) units^2

For velocities, there’s a fourth plot M, which is the magnitude of the vector.

## Inspect Physics Example

To run this utility:

1. Open the Simulation Data Visualizer by going to the **Visibility Menu (eye icon on viewport) > Show by Type > Physics > Simulation Data Visualizer**.
2. Activate **Windows** > **Examples** > **Robotics Examples** which will open the `Robotics Examples` tab.
3. Load some simulation-ready example, such as the Cortex Franka example, by clicking **Robotics Examples > Cortex > Franka Cortex Examples**.
4. Press the **Load Robot** button.
5. Select the **/World/Franka/panda\_hand** prim from the [Stage](../reference_material/reference_glossary.html#isaac-sim-glossary-stage).
6. Press the **START** button to begin simulating.

After simulation starts, the physics state of the selected rigid body updates in the **Inspect Physics** window.

On this page

* [Conventions](#conventions)
* [Inspect Physics Example](#inspect-physics-example)