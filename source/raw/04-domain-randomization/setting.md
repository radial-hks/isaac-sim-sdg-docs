---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/action_and_event_data_generation/ext_replicator-object/setting.html
title: "Setting"
section: "Replicator Object"
module: "04-domain-randomization"
checksum: "afa5adf8852a1414"
fetched: "2026-06-21T11:55:29"
---

* [Synthetic Data Generation](../../synthetic_data_generation/index.html)
* [Action and Event Data Generation](../index.html)
* [Object Simulation and Synthetic Data Generation](../tutorial_replicator_object.html)
* Setting

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Setting

If the key-value pair in the description file is neither a [Mutable](mutable.html#mutable) nor a [Harmonizer](harmonizer.html#harmonizer), itâs a setting. You can define a description with only settings.

## Required Keys

There are several required keys for settings:

| Required Key | Type | Description |
| --- | --- | --- |
| output\_path | string | The output folders in which folders corresponding to  each [output switch](#output-switches) are created |
| num\_frames | int | Number of frames to output |
| screen\_width | int | Screen width of output images |
| screen\_height | int | Screen height of output images |
| seed | int | Global randomization seed |
| version | string | Version number of isaacsim.replicator.object.core |

output\_switches

The setting output\_path controls what is output to disk per frame. It has these switches:

| Switch | Data |
| --- | --- |
| images | The RGB image of the frame |
| labels | 2D tight bounding box and the occlusion rate information for each visible tracked object. Each line corresponds to an object, and it has Kitti format `usd_base_name 0 occlusion 0 x_min y_min x_max y_max 0 0 0 0 0 0 0` |
| 3d\_labels | 3D bounding box information stored as Objectron format |
| descriptions | A description file logging the current state of the scene - Using this file as input description, the same graphics content is output |
| segmentation | The segmentation mask of tracked mutables |
| depth | The depth map of the scene, showing the distance to image plane |
| normal | The normal map of the frame |

Setting a switch to True or not setting the switch creates the corresponding folder under `output_path` and writes corresponding data into it.

`usd_base_name` is the mutable name or the USD file base name of USD file when a geometry `mesh` is loaded, which means itâs not allowed to load different USD files with the same base name. Using `${resource_root_1}/apple.usd` and `${resource_root_1}/inner/apple.usd` in the same simulation causes unexpected behavior.

For example, an output switch could be:

```python
output_switches:
  images: True
  labels: True
  descriptions: True
  3d_labels: True
  segmentation: True
  depth: False
```

To also write per-frame scene captions alongside this output, the `Isaacsim.Replicator.Caption` extensionâs `CombinedIROSceneGraphWriter` can replace the default writer, refer to [Use Isaacsim.Replicator.Caption in Isaacsim.Replicator.Object](../tutorial_replicator_caption.html#using-iro-extension).

## Optional Keys

There are also optional keys, where if not set, have default values:

| Optional Keys with Default Value | Type | Default value | Description |
| --- | --- | --- | --- |
| parent\_config | string | None | Specifies the description file that this description file inherits from, in the same parent folder. Values re-defined in the current description file override values defined in parent configs. |
| path\_tracing | bool | False | Render mode selection |
| inter\_frame\_time/simulation\_time | numeric | 0 | The simulation time between 2 frames |
| extra\_rendering\_time | numeric | 0 | Extra rendering time per frame |
| output\_name | string | `$[seed]_$[camera]` | The output name of a frame that can be customized. Seed, camera, and frame macros are available. |
| skip\_frames\_with\_no\_visible\_tracked\_mutables | bool | False | If set to true, and if there are no visible tracked mutables in the scene, the frame is skipped |
| gravity | numeric | 0 | Resolves gravity during [physics resolution stage](../tutorial_replicator_object.html#simulation-workflow) |
| friction | numeric | 1 | Friction among objects during physics resolution stage. Lower values indicate that the object is more slippery. |
| linear\_damping | numeric | 0 | Linear damping of objects during physics resolution stage. |
| angular\_damping | numeric | 0 | Angular damping of objects during physics resolution stage. |
| occlusion\_threshold | numeric | 1 | If the occlusion of an object is bigger than this threshold, the object will be skipped in the labels. |
| max\_area\_threshold | numeric | None | If the bounding box area of an object as a percentage of the screen area is bigger than this threshold, the object will be skipped in the labels. |
| min\_area\_threshold | numeric | None | If the bounding box area of an object as a percentage of the screen area is smaller than this threshold, the object will be skipped in the labels. |

**Suggestions and More Information**

**path\_tracing**

Turning it on uses the path tracer, which makes simulation slower but image quality higher. Turning it off uses real-time RTX.

**inter\_frame\_time/simulation\_time and extra\_rendering\_time**

For complex scenes, leave more time for physics resolution and rendering.

**output\_name**

Three macros are available:

* $[seed] evaluates to the seed of the current frame
* $[camera] evaluates to the camera name
* $[frame] evaluates to the frame index. Refer to seed for details.

**$[seed]**

Each frame is randomized with its own seed, which equals the global seed plus the frame index. For example, if global seed is `2`, and three images are output, the frame indices for these three images are `0, 1, 2`; and the seeds are `2, 3, 4`, respectively.

**Physics simulation explained**

When objects are randomized in the scene for each frame, they can start at an overlapping position. Resolution of physics de-penetrates these objects. The de-penetration accelerates the objects, such that they can start off with a high speed. Increase linear/angular damping to keep object movement contained.

However, if linear or angular damping is set too high, objects get lazy and they donât move much. This can be bad in a gravity enabled setting, where we want objects to be in close contact with a surface. Because different objects have different sizes and shapes, itâs good to tune these physics properties to reach a good appearance.

Similarly, too high of a value for friction makes objects cluster if they are in close contact; while too low of a value for friction makes them slippery and glide off surfaces.

Note

If there is no object in the scene when you are expecting some objects, one reason might be that they flew away from the view frustum. Check your physics settings.

On this page

* [Required Keys](#required-keys)
* [Optional Keys](#optional-keys)