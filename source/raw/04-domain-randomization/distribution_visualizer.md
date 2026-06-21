---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/action_and_event_data_generation/ext_replicator-object/distribution_visualizer.html
title: "Distribution Visualizer"
section: "Replicator Object"
module: "04-domain-randomization"
checksum: "fabb50d97c77feb8"
fetched: "2026-06-21T13:57:59"
---

* [Synthetic Data Generation](../../synthetic_data_generation/index.html)
* [Action and Event Data Generation](../index.html)
* [Object Simulation and Synthetic Data Generation](../tutorial_replicator_object.html)
* Distribution Visualizer

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Distribution Visualizer

The distribution visualizer is a tool that allows you to visualize the distribution of a mutable attribute. It gives a visual clue through a dynamic point cloud, showing how possible an object is to be generated at a particular pose.

## Concept

A prim has its scene graph described by a list of `xformOps`. It can be a rotation followed by a translation, and then another rotation, for example. In IRO, each `xformOp` can be a mutable attribute. By controlling the distribution of each `xformOp`, we obtain an understanding of the global spatial probability distribution of the prim by visualization.

## To Run

Here is a step-by-step guide to using the distribution visualizer on a basic prim.

1. Click **Tools** > **Action and Event Data Generation** > **Distribution Visualizer** to open the distribution visualizer as shown below.
2. Create a torus, a dome light; focus on the torus by pressing “F”; and switch to path tracing mode, as shown below.
3. Click on blank space to deselect.
4. Click on the torus again so that the distribution visualizer is in sync with the selected prim and its `xformOps` will be visible in the distribution visualizer. By default, it has translate, `rotateZYX`, and scale.
5. Apply preset `xformOps` to the torus, by clicking on `Apply Preset xformOps`. This step is not needed for an ordinary prim; this is only to demonstrate the concept. You can observe the torus is now transformed to a new pose.

   > Note
   >
   > If the torus is not visible, press “F” on the keyboard to focus the active camera to look at it. If it’s still not visible, go to the stage tab and click on the torus to make sure it’s selected.
6. Click on blank space to deselect, and then click on the torus again. From global to local, the new `xformOps` are `rotateY`, `rotateX`, and `translate`.

   > Each `xformOp` has three lines:
   >
   > * value
   > * start
   > * end
   >
   > The value is the current value of the `xformOp` and the start and end are the range of the value.
7. Change the value of rotateY and rotateX to observe how the torus rotates. More information about the scene graph can be found in [Transformation](transformation.html#transformation).

   > So far, the steps are shown below:
8. Adjust the range by changing the start and end of the `xformOps`: rotateY, rotateX, and the Z-component of translate.
9. Observe an animated shell that shows the distribution range of the torus:
10. To randomize a prim in IRO this way, insert a section like this in our description file:

```python
basic_shape:
  type: geometry
  subtype: torus
  transform_operators:
  - rotateY:
      distribution_type: range
      start: -120
      end: 120
  - rotateX:
      distribution_type: range
      start: -30
      end: 30
  - translate:
      distribution_type: range
      start:
      - 0
      - 0
      - 200
      end:
      - 0
      - 0
      - 500
```

On this page

* [Concept](#concept)
* [To Run](#to-run)