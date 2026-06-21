---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/action_and_event_data_generation/ext_replicator-object/harmonizer.html
title: "Harmonizer"
section: "Replicator Object"
module: "04-domain-randomization"
checksum: "5f61b1876710200b"
fetched: "2026-06-21T14:14:52"
---

* [Synthetic Data Generation](../../synthetic_data_generation/index.html)
* [Action and Event Data Generation](../index.html)
* [Object Simulation and Synthetic Data Generation](../tutorial_replicator_object.html)
* Harmonizer

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Harmonizer

A harmonizer defines the relationship among randomized [mutable attributes](mutable_attribute.html#mutable-attribute).

If the key-value pair in the description file has a key of `harmonizer_type`, it defines a harmonizer. A harmonizer constrains how a mutable attribute randomizes.

**Permutation harmonizer**

If `harmonizer_type` is `permutate`, it is a permutation harmonizer. When you [free randomize](../tutorial_replicator_object.html#simulation-workflow) a `harmonized` mutable attribute, you can specify a `pitch` as the input to the permutation harmonizer. Then the permutation harmonizer shuffles these inputs and sends back the value to the harmonized attribute, which in turn can be used in a transform operator in the [harmonized randomize stage](../tutorial_replicator_object.html#simulation-workflow).

For example, to define three OROs, facing in three directions:

```python
oro:
  count: 3
  type: geometry
  subtype: mesh
  usd_path: [PATH_TO_ORO]
  transform_operators:
  - translate:
    - ($[../index] % $[../count] - 1) * 600
    - 0
    - 0
  - rotateY: ($[../index] - 1) * 60
```

These three OROs have X-axis position `-600, 0, 600`; and they are rotated around Y-axis by `-60, 0, 60` degrees.

To shuffle the positions of these OROs, so that the ORO that rotates `-60` degrees can appear to the right:

Define a mutable attribute `permutated_index` as `harmonized`. During the free randomize stage, it submits its index as its `pitch` to the harmonizer `permutate_H`, which is a permutation harmonizer.

```python
oro:
  ...
  permutated_index:
    distribution_type: harmonized
    harmonizer_name: permutate_H
    pitch: $[index]
permutate_H:
  harmonizer_type: permutate
```

During the harmonize stage, `permutate_H` shuffles the received pitches from all relevant harmonized mutable attributes and resonates them back to each of them.

During the harmonized randomize stage, `permutated_index` gets the shuffled value back. You can use it in transform operators, like using an index.

```python
oro:
  ...
  transform_operators:
  - translate:
    - ($[permutated_index] % $[../count] - 1) * 600
    - 0
    - 0
  - rotateY: ($[../index] - 1) * 60
```

This feature can be used with any values within scope.

**Bin pack harmonizer**

If `harmonizer_type` is `bin_pack`, it is a bin pack harmonizer that packs objects into a cuboid space according to their axis-aligned bounding boxes. You can define a cuboid with custom dimensions like this:

```python
bin_pack_H:
  harmonizer_type: bin_pack
  bin_size:
  - 480
  - 260
  - 700
```

You can define many OROs, and pack them into this cuboid:

```python
oro:
  count: 200
  physics: rigidbody
  type: geometry
  subtype: mesh
  tracked: true
  transform_operators:
  - translate:
    - 0
    - 300
    - 0
  - transform:
      distribution_type: harmonized
      harmonizer_name: bin_pack_H
      pitch: local_aabb
  - scale:
    - 30
    - 30
    - 30
  usd_path: PATH_TO_ORO
```

For example, with many OROs densely packed together:

In this example, `200` OROs are spawned during initialization.

Here are some of the examples of randomized scenes generated using the bin pack harmonizer:

More insights can be found in the [harmonization example](randomization_dependency.html#harmonization-example).