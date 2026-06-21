---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/action_and_event_data_generation/ext_replicator-object/mutable.html
title: "Mutable"
section: "Replicator Object"
module: "04-domain-randomization"
checksum: "02a31d60140ff5aa"
fetched: "2026-06-21T13:40:25"
---

* [Synthetic Data Generation](../../synthetic_data_generation/index.html)
* [Action and Event Data Generation](../index.html)
* [Object Simulation and Synthetic Data Generation](../tutorial_replicator_object.html)
* Mutable

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Mutable

If the pair is a dictionary with a key `type`, it’s a mutable. There are four types of mutables:

* [Camera](camera.html#camera) where we are
* [Geometry](geometry.html#geometry) the things we want to observe
* [Light](light.html#light) how we observe things
* [Force](force.html#force) forces applied to rigid bodies

Each mutable consists of attributes. Each key-value pair of a mutable is an attribute. An attribute can be a [Mutable Attribute](mutable_attribute.html#mutable-attribute), which mutates per frame.

Available attributes of mutables are:

| Name | Type | Description |
| --- | --- | --- |
| type | string | The type of the mutable, `camera`, `geometry`, `light`, or `force`. |
| count | int | The number of identically defined mutables |
| tracked | bool | If the mutable is tracked, its 2d/3D bounding boxes will be output, and it will have a corresponding highlighted color on the segmentation mask. |
| transform\_operators | list | The transformation of the object. |

**Transform operators**

Specially, to define its pose in space, the mutable can define a sequenced list of [transform operators](transformation.html#transformation). A transform operator is also a key-value pair, in which the value can be a mutable attribute.

**Shader attributes**

In Omniverse, a shader has many attributes describing how a mesh is shaded. For example, `diffuse_texture` that points to the RGB image, and `texture_rotate` that specifies how its texture should be rotated. In ORO, you can control these attributes just like any other mutable attributes. For example, the following description randomizes the tint, and rotates and scales the texture:

```python
mesh:
  type: geometry
  subtype: mesh
  usd_path: https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/ArchVis/Residential/Furniture/Desks/Desk_01.usd
  transform_operators:
  - rotateXYZ:
    - -90
    - 0
    - 0
  shader_attributes:
    texture_rotate:
      distribution_type: range
      start: -180
      end: 180
    diffuse_tint:
      distribution_type: range
      start:
      - 0
      - 0
      - 0
      end:
      - 2
      - 2
      - 2
    texture_scale:
      distribution_type: range
      start:
      - 0.2
      - 0.2
      end:
      - 0.7
      - 0.7
```

Specifically, you can do common computer vision operations, such as color mapping to a mesh that has an RGB image as diffuse texture, by doing:

```python
shader_attributes:
  diffuse_texture:
    distribution_type: texture
    operation: color_map
```

Available options are: `color_map`, `transform`, `add_noise`, `apply_blur`, `color_shift`, `invert_color`, `sobel_edges`, and `random_mutation`.

**Name, count, and index**

A mutable has a `name`, which is the key in the key-value pair and potentially an index, if defined in group with a `count` attribute. For example:

```python
mesh:
  count: 2
  ...
```

During initialization stage, two mutables are initialized after the description is parsed. For example:

```python
mesh_0:
  count: 2
  index: 0
  name: mesh_0
  ...

mesh_1:
  count: 2
  index: 1
  name: mesh_1
  ...
```

The `count` is still there so that you can access how many mutables are in the group. You can use these values to define macros.