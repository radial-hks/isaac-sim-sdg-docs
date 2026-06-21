---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/action_and_event_data_generation/ext_replicator-object/light.html
title: "Light"
section: "Replicator Object"
module: "04-domain-randomization"
checksum: "847622277d4d17ce"
fetched: "2026-06-21T13:57:59"
---

* [Synthetic Data Generation](../../synthetic_data_generation/index.html)
* [Action and Event Data Generation](../index.html)
* [Object Simulation and Synthetic Data Generation](../tutorial_replicator_object.html)
* Light

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Light

If a mutable has attribute `type` of `light`, it’s a light. There are directional lights and dome lights. A light has an `intensity` attribute. Specifically, a dome light has a `texture_path` attribute.

Aside from ordinary attributes of mutables, additional available attributes of lights are:

| Name | Type |
| --- | --- |
| intensity | numeric |
| color | numeric, dimension three list |

**Direct light**

In the default pose, a direct light shines towards negative Z-direction.

**Dome light**

A dome light has light beams coming from all directions.

Additionally, available attributes of dome light are:

| Name | Type |
| --- | --- |
| texture\_path | string |

`texture_path` is a path to a spherical image that is a skybox. It has a color value in all directions, so that when the camera is rotated, you can observe different parts of the image.