---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/action_and_event_data_generation/ext_replicator-object/mutable_attribute.html
title: "Mutable Attribute"
section: "Replicator Object"
module: "04-domain-randomization"
checksum: "a1aa7394cfcdf01d"
fetched: "2026-06-21T13:40:25"
---

* [Synthetic Data Generation](../../synthetic_data_generation/index.html)
* [Action and Event Data Generation](../index.html)
* [Object Simulation and Synthetic Data Generation](../tutorial_replicator_object.html)
* Mutable Attribute

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Mutable Attribute

A value in the description file is a mutable attribute if it is a dictionary that has a key `distribution_type`, or a string that contains [macros](macro.html#macro) (`$[...]`). A mutable attribute does not have to be part of a mutable; you can have standalone mutable attributes.

You can define mutable attributes with `distribution_type` as `folder`, `set`, `range`, `frustum`, and `harmonized`.

**Folder**

A `folder` mutable attribute uniformly samples a file from the specified folder with the specified suffix. To define a `folder` type, there are two additional required keys, `suffix` and `value`.

```python
distractor:
  type: geometry
  subtype: mesh
  usd_path:
    distribution_type: folder
    suffix: usd
    value: $[/resources_root]/distractors
```

In this example, a geometry named `distractor`, which is a mesh loaded from a USD file, is defined. And the USD file is randomly selected from all files in `$[/resources_root]/distractors` that has a `.usd` extension.

Note

Some example description files have [placeholders](../tutorial_replicator_object.html#placeholders).

**Set**

A `set` attribute randomly selects a value from a set.

```python
dome_light:
  type: light
  subtype: dome
  texture_path:
    distribution_type: set
    values:
    - $[/skies]/adams_place_bridge_4k.hdr
    - $[/skies]/autoshop_01_4k.hdr
```

In this example, a dome light is defined with a texture of either `$[/skies]/adams_place_bridge_4k.hdr` or `$[/skies]/autoshop_01_4k.hdr`, selected randomly.

**Range**

A `range` attribute specifies the range of randomization for a numeric value.

```python
dome_light:
  type: light
  subtype: dome
  intensity:
    distribution_type: range
    start: 1000
    end: 3000
```

Here the dome light defined has an intensity as a random number within `[1000, 3000]`.

**Camera frustum**

A `camera_frustum` attribute is specially used for sampling a value for the translate operator (Refer to [Transformation](transformation.html#transformation)). It samples a position in a view frustum defined by `camera_parameters`, which is the same as in [Camera](camera.html#camera).

```python
main_object:
  ...
  transform_operators:
  - translate:
      distribution_type: camera_frustum
      camera_parameters: $[/camera_parameters]
      distance_min: 200
      distance_max: 600
      screen_space_range: 0.5
```

`distance_min` and `distance_max` are the minimum and maximum distance from the view point. `screen_space_range` is the range in screen space on which to scatter objects. For example, if you set it to `0.5`, the objects are only scattered in the space projected to the area specified within the dotted lines:

Camera frustum doesn’t scatter objects uniformly along the line of vision. It’s scattered more often in the near field and the far field, such that the probability density of projected area is constant. For example, below is a uniformly sampled in (a) while sampling more in the near field in (b). In (b), the projected areas are more evenly spaced compared to (a).

For the same object, it’s more likely to be sampled near `distance_min` than `distance_max` such that a position that gives a projection ten pixels wide has the same possibility to be sampled with a position that gives a projection twenty pixels wide.

Such a distance is given by:

\[distance = \frac{distanceMin \cdot distanceMax}{distanceMin + (distanceMax - distanceMin) \cdot randomUnit}\]

in which \(randomUnit\) is uniformly sampled within `[0,1]`.

**Harmonized**

A `harmonized` attribute defines an attribute that retrieves its value from a [Harmonizer](harmonizer.html#harmonizer) after [harmonization](../tutorial_replicator_object.html#simulation-workflow). More details can be found in the [harmonization example](randomization_dependency.html#harmonization-example).