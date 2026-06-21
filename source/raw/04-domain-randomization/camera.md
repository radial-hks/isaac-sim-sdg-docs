---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/action_and_event_data_generation/ext_replicator-object/camera.html
title: "Camera Randomizer"
section: "Replicator Object"
module: "04-domain-randomization"
checksum: "22fb6ea9adf1e718"
fetched: "2026-06-21T13:58:02"
---

* [Synthetic Data Generation](../../synthetic_data_generation/index.html)
* [Action and Event Data Generation](../index.html)
* [Object Simulation and Synthetic Data Generation](../tutorial_replicator_object.html)
* Camera

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Camera

If a mutable has an attribute `type` of `camera`, it’s a camera. Typically, a basic pinhole camera model is used.

Required attributes of a camera:

| Name | Type |
| --- | --- |
| camera\_parameters | dict |

`camera_parameters` is a dictionary with the following six required keys:

| Name | Type |
| --- | --- |
| screen\_width | int |
| screen\_height | int |
| focal\_length | numeric |
| horizontal\_aperture | numeric |
| near\_clip | numeric |
| far\_clip | numeric |

## Pinhole Model

3D objects are projected onto a 2D plane, like this:

Looking from a top view, towards the negative Y-axis:

In the picture, f, which is the distance from the camera to the projection plane, is `focal_length`. hA is the distance from the left edge (upper end) to the right edge (lower end) and stands for `horizontal_aperture`.

`near_clip` and `far_clip` define two planes perpendicular to the line of vision between which you can observe things.

## Assumptions

The following assumptions are made for the frame of reference and conversion from/to other common representations.

If no transform operator is applied on the camera, the Y-axis points upwards and X-axis points to the right. The camera looks towards negative direction of the Z-axis.

On this page

* [Pinhole Model](#pinhole-model)
* [Assumptions](#assumptions)