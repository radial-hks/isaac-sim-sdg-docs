# Domain Randomization

> Replicator Object API 随机化器 + Domain Randomization OGN 节点
> Isaac Sim 版本: 6.0
> 最后组装: 2026-06-21 14:14 UTC
> 来源页数: 15

---

## 来源链接

- [Camera Randomizer](https://docs.isaacsim.omniverse.nvidia.com/latest/action_and_event_data_generation/ext_replicator-object/camera.html)
- [Force](https://docs.isaacsim.omniverse.nvidia.com/latest/action_and_event_data_generation/ext_replicator-object/force.html)
- [Geometry](https://docs.isaacsim.omniverse.nvidia.com/latest/action_and_event_data_generation/ext_replicator-object/geometry.html)
- [Harmonizer](https://docs.isaacsim.omniverse.nvidia.com/latest/action_and_event_data_generation/ext_replicator-object/harmonizer.html)
- [Light](https://docs.isaacsim.omniverse.nvidia.com/latest/action_and_event_data_generation/ext_replicator-object/light.html)
- [Macro](https://docs.isaacsim.omniverse.nvidia.com/latest/action_and_event_data_generation/ext_replicator-object/macro.html)
- [Mutable](https://docs.isaacsim.omniverse.nvidia.com/latest/action_and_event_data_generation/ext_replicator-object/mutable.html)
- [Mutable Attribute](https://docs.isaacsim.omniverse.nvidia.com/latest/action_and_event_data_generation/ext_replicator-object/mutable_attribute.html)
- [Randomization Dependency](https://docs.isaacsim.omniverse.nvidia.com/latest/action_and_event_data_generation/ext_replicator-object/randomization_dependency.html)
- [Setting](https://docs.isaacsim.omniverse.nvidia.com/latest/action_and_event_data_generation/ext_replicator-object/setting.html)
- [Transformation](https://docs.isaacsim.omniverse.nvidia.com/latest/action_and_event_data_generation/ext_replicator-object/transformation.html)
- [Distribution Visualizer](https://docs.isaacsim.omniverse.nvidia.com/latest/action_and_event_data_generation/ext_replicator-object/distribution_visualizer.html)
- [Empty Space Detection](https://docs.isaacsim.omniverse.nvidia.com/latest/action_and_event_data_generation/ext_replicator-object/empty_space_detection.html)
- [Chat IRO](https://docs.isaacsim.omniverse.nvidia.com/latest/action_and_event_data_generation/ext_replicator-object/ext_chat_iro.html)
- [Replicator Object Tutorial](https://docs.isaacsim.omniverse.nvidia.com/latest/action_and_event_data_generation/tutorial_replicator_object.html)

---


## Replicator Object

### Camera Randomizer

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/action_and_event_data_generation/ext_replicator-object/camera.html

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

---

### Force

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/action_and_event_data_generation/ext_replicator-object/force.html

* [Synthetic Data Generation](../../synthetic_data_generation/index.html)
* [Action and Event Data Generation](../index.html)
* [Object Simulation and Synthetic Data Generation](../tutorial_replicator_object.html)
* Force

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Force

If a mutable has attribute `type` of `force`, it’s a force mutable that applies PhysX forces to rigid bodies. Forces can be used to create dynamic simulations with objects being pushed, pulled, or animated through physics.

Available attributes of `force`:

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| target | string | The name of the target mutable (must be a rigidbody). Do not use `$[...]` syntax - just use the mutable name directly (e.g., `target: rocket`). The target must be defined before the force in the YAML. |
| force | list | Force vector as [x, y, z]. Can be a constant value or animated using keyframes. |
| torque | list | Torque vector as [x, y, z]. Optional. Can be a constant value or animated using keyframes. |
| enabled | bool | Whether the force is enabled. Defaults to `True`. Can be animated using keyframes. |
| animation | dict | Keyframe animation for force, torque, enabled, and transform operators. See below for details. |
| transform\_operators | list | Transform operators for local offset of the force application point. Can be animated. |

**Constant Force**

A constant force applies the same force vector throughout the simulation:

```python
rocket_thrust:
  type: force
  target: rocket
  force: [0, 0, 2000]  # Upward force
  enabled: true
```

**Animated Force**

An animated force uses keyframes to change force properties over time. The animation dictionary contains keyframe sequences for `force`, `torque`, `enabled`, and transform operators like `translate`.

Example of animated force:

```python
rocket_thrust:
  type: force
  target: rocket
  animation:
    force:
      keyframes:
      - time: 0
        value:
        - distribution_type: range
          start: -50
          end: 50
        - 0
        - distribution_type: range
          start: 1500
          end: 1900
      - time: 20
        value:
        - distribution_type: range
          start: -50
          end: 50
        - 0
        - 1300
    enabled:
      keyframes:
      - time: 0
        value: true
      - time: 50
        value: false
    translate:
      keyframes:
      - time: 0
        value: [0, 0, 0]
      - time: 20
        value: [0, 2, 0]  # Vibrate effect
      - time: 25
        value: [0, 0, 0]
```

**Notes**

* The target must be a rigidbody geometry. The force is applied as a child prim of the target.
* For animated forces, the X component of the force vector is randomized once and shared across all keyframes (matching ForceDemo.py behavior).
* Transform operators in animation (like `translate`) can be used to create vibration or movement effects at the force application point.
* Forces are applied in local space relative to the target prim.

---

### Geometry

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/action_and_event_data_generation/ext_replicator-object/geometry.html

* [Synthetic Data Generation](../../synthetic_data_generation/index.html)
* [Action and Event Data Generation](../index.html)
* [Object Simulation and Synthetic Data Generation](../tutorial_replicator_object.html)
* Geometry

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Geometry

If a mutable has attribute `type` of `geometry`, it’s a geometry. A geometry is a substance in space.

Available attributes of `geometry`:

| Name | Type | Description |
| --- | --- | --- |
| subtype | string | refer to Basic shapes, Deformed shape, Room, Compound, Pyramid, and Mesh loaded from USD |
| physics | string | `collision` or `rigidbody` |
| is\_instance | bool | whether the geometry is instanced - default to true; required to be false for shader attribute randomization |

If `physics` is set to `rigidbody`, the object is a dynamic object that responds to physics. If it’s set to `collision`, the object is a static object that dynamic objects interact with. For example, a wall can have `collision` and a ping-pong ball bouncing off of it has `rigidbody`.

**Physics Properties Randomization**

When `physics` is set to `rigidbody` or `collision`, you can randomize various physics properties to create more diverse simulations. The following properties can be randomized using [distribution types](mutable_attribute.html#mutable-attribute):

| Property | Type | Description |
| --- | --- | --- |
| friction | numeric | Friction coefficient (both static and dynamic). Defaults to the global friction setting if not specified. |
| linear\_damping | numeric | Linear damping coefficient for rigidbody objects. Defaults to the global linear\_damping setting. |
| angular\_damping | numeric | Angular damping coefficient for rigidbody objects. Defaults to the global angular\_damping setting. |
| concave | bool | Whether to use convex decomposition for collision detection. Defaults to `False` (uses convex hull). |
| initial\_velocity | list | Initial linear velocity as [x, y, z]. Each component can be randomized using distribution types. |
| initial\_angular\_velocity | list | Initial angular velocity as [x, y, z]. Each component can be randomized using distribution types. |

Example of randomizing physics properties:

```python
box:
  type: geometry
  subtype: cube
  physics: rigidbody
  friction:
    distribution_type: range
    start: 0.1
    end: 0.9
  linear_damping:
    distribution_type: range
    start: 0
    end: 5
  initial_velocity:
  - 0.0
  - distribution_type: range
    start: 50.0
    end: 100.0
  - 0.0
```

**Basic shapes**

If `subtype` is one of `cone`, `cube`, `cylinder`, `disk`, `torus`, `plane`, or `sphere` it defines the corresponding basic geometry.

**Compound geometry**

If `subtype` is `compound`, it defines a compound geometry composed of multiple parts forming a single rigid body. Each part can be a basic shape (cube, sphere, cylinder, capsule, or cone). The compound geometry is useful for creating complex objects like rockets or multi-part assemblies.

Attributes of compound geometry:

| Name | Type | Description |
| --- | --- | --- |
| parts | dict | Dictionary of part definitions. Each part has a `subtype` (cube, sphere, cylinder, capsule, or cone) and optional attributes like `color`, `transform_operators`, and size parameters (e.g., `radius`, `height`, `size`). |

Example of compound geometry:

```python
rocket:
  type: geometry
  subtype: compound
  physics: rigidbody
  parts:
    main_capsule:
      subtype: capsule
      radius: 10.0
      height: 25.0
      color: [0.8, 0.1, 0.1]
      transform_operators:
      - translate: [0, 0, 30.0]
    side_booster:
      subtype: capsule
      radius: 5.0
      height: 10.0
      color: [0.8, 0.1, 0.1]
      transform_operators:
      - translate: [30.0, 0, 20.0]
```

**Pyramid geometry**

If `subtype` is `pyramid`, it defines a pyramid structure composed of multiple boxes arranged in a regular pyramid pattern. The pyramid creates a stable structure where row i (0 to pyramid\_size-1) has (pyramid\_size - i) boxes. Box sizes and colors can be randomized per box, but positions are regular/ordered for physics stability.

Attributes of pyramid geometry:

| Name | Type | Description |
| --- | --- | --- |
| pyramid\_size | numeric | Number of rows in the pyramid. Total boxes = pyramid\_size \* (pyramid\_size + 1) / 2. Can be randomized using distribution types. |
| y\_position | numeric | Y position (height) of the pyramid base. |
| offset | numeric | Spacing offset between boxes. Default: 1.0 |
| box\_size | numeric | Size of each box. Can be a constant value or a distribution (range) for per-box randomization. |
| color | list | Color of boxes. Can be randomized per box. |

Example of pyramid geometry:

```python
box_pyramid:
  type: geometry
  subtype: pyramid
  physics: rigidbody
  tracked: true
  pyramid_size:
    distribution_type: range
    start: 5
    end: 15
  y_position: -0.24377
  offset: 1.0
  box_size:
    distribution_type: range
    start: 7
    end: 17
  color:
  - distribution_type: range
    start: 0.3
    end: 1.0
  - distribution_type: range
    start: 0.3
    end: 1.0
  - distribution_type: range
    start: 0.3
    end: 1.0
```

**Deformed shape**

Physics simulation for bottles is not supported.

If `subtype` is `bottle`, it defines a bottle shape, which is a parameterized deformed geometry controlled by the following parameters:

| Name | Type | Description |
| --- | --- | --- |
| base\_effector | string | vertical position of the base effector |
| neck\_effector | string | vertical position of the neck effector |
| horizontal\_effector | string | horizontal position of the body effector |
| vertical\_effector | string | vertical position of the body effector |

This image illustrates how the shape of the bottle is controlled by these four effectors.

Note

We currently don’t yet have collision detection for deformed shapes; they don’t have physics.

**Room geometry**

If `subtype` is `room`, it defines a room geometry with optional table and walls created using RoomHelper from PhysX demos. This is useful for creating enclosed environments for physics simulations.

Attributes of room geometry:

| Name | Type | Description |
| --- | --- | --- |
| table\_width | numeric | Width of the table. Default: 500.0 |
| table\_depth | numeric | Depth of the table. Default: 500.0 |
| has\_table | bool | Whether to create a table. Default: True |
| has\_walls | bool | Whether to create walls. Default: True |
| zoom | numeric | Zoom factor for room size. Default: 0.5 |
| table\_rotation | numeric | Rotation of the table in degrees. Can be randomized using distribution types. |
| floor\_color | list | Color of the floor as [r, g, b]. Can be randomized using distribution types. |

Example of room geometry:

```python
demo_room:
  type: geometry
  subtype: room
  table_width: 500.0
  table_depth: 500.0
  has_table: true
  has_walls: true
  zoom: 0.5
  table_rotation:
    distribution_type: range
    start: 0
    end: 360
  floor_color:
  - 0.5
  - 0.75
  - 1.0
```

**Mesh loaded from USD**

If `subtype` is `mesh`, it defines a mesh loaded from USD.

Additional attribute of mesh:

| Name | Type | Description |
| --- | --- | --- |
| usd\_path | string | The path to the USD |

---

### Harmonizer

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/action_and_event_data_generation/ext_replicator-object/harmonizer.html

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

---

### Light

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/action_and_event_data_generation/ext_replicator-object/light.html

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

---

### Macro

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/action_and_event_data_generation/ext_replicator-object/macro.html

* [Synthetic Data Generation](../../synthetic_data_generation/index.html)
* [Action and Event Data Generation](../index.html)
* [Object Simulation and Synthetic Data Generation](../tutorial_replicator_object.html)
* Macro

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Macro

Macros can be used in [settings](setting.html#setting) and [mutable attributes](mutable_attribute.html#mutable-attribute) in certain ways to retrieve a value from another setting or mutable attribute. They are defined like `$[...]`. Macros are used everywhere to describe relationships among values to simulate complex scenes with compact descriptions.

**$[/absolute\_reference]**

Absolute references refer to values by their absolute paths.

> ```python
> bright_light:
>   type: light
>   subtype: dome
>   intensity:
>     distribution_type: range
>     start:
>       distribution_type: range
>       start: $[/dark_light/intensity]
>       end: $[/dark_light/intensity] + 200
>     end: $[/dark_light/intensity] + 1000
>   texture_path: https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Isaac/5.1/NVIDIA/Assets/Skies/2022_1/Skies/Clear/lakeside.hdr
>   transform_operators:
>   - rotateX: 270
> dark_light:
>   subtype: dome
>   intensity:
>     distribution_type: range
>     start: 100
>     end: 1000
> ```

In this example, the mutable attribute, `/bright_light/intensity`, is a range that ranges from `$[/dark_light/intensity]` to `$[/dark_light/intensity] + 200`. These limits depend on the resolution of another mutable attribute, `/dark_light/intensity`. Thus, in every frame `/dark_light/intensity` is resolved before `bright_light/intensity` is resolved.

**$[relative\_reference]** and **$[../relative\_reference]**

Relative references refer to values with the same parent. In the example below, `$[a1]` is the same as `$[/a/a1]`:

> ```python
> a:
>   a1: x
>   a2: $[a1]
> ```

You can also go to parenting attribute using `..`. In the example below, `$[../a1]` is the same as `$[/a/a1]`:

> ```python
> a:
>   a1: x
>   a2:
>     a21: $[../a1]
> ```

**$[reference\_to\_list\_element~index]**

References to list elements refer to values in lists. In the example below, `/bins` will be expanded to `/bins_0` to `/bins_7`, with `/bins_X/dimension` resolved to a three-element list. `$[/bins_$[index]/dimension~0]` in `/transform_global_X/pitch` will retrieve the resolved value from index zero.

> ```python
> bins: # dimensions of eight small bins
>   count: 8
>   dimension:
>     distribution_type: range
>     start:
>     - 100
>     - 200
>     - 300
>     end:
>     - 400
>     - 200
>     - 300
> transform_global: # transforms of eight small bins
>   count: 8
>   distribution_type: harmonized
>   harmonizer_name: bin_pack_global_H
>   pitch:
>   - - -$[/bins_$[index]/dimension~0] / 2 * 1.5
>     - -$[/bins_$[index]/dimension~1] / 2
>     - -$[/bins_$[index]/dimension~2] / 2 * 1.5
>   - - $[/bins_$[index]/dimension~0] / 2 * 1.5
>     - $[/bins_$[index]/dimension~1] / 2
>     - $[/bins_$[index]/dimension~2] / 2 * 1.5
> ```

**$[/as\_is\_reference]**

> As-is reference macro substitutes the whole value, supporting references to dictionaries. For example:
>
> ```python
> screen_width: 960
> screen_height: 544
> camera_parameters:
>   far_clip: 100000
>   focal_length: 14.228393962367306
>   horizontal_aperture: 20.955
>   near_clip: 0.1
>   screen_height: $[/screen_height]
>   screen_width: $[/screen_width]
> default_camera:
>   type: camera
>   camera_parameters: $[/camera_parameters]
> ```
>
> Evaluates to:
>
> ```python
> screen_width: 960
> screen_height: 544
> camera_parameters:
>   focal_length: 14.228393962367306
>   horizontal_aperture: 20.955
>   near_clip: 0.1
>   far_clip: 100000
>   screen_width: 960
>   screen_height: 544
> default_camera:
>   type: camera
>   camera_parameters:
>     focal_length: 14.228393962367306
>     horizontal_aperture: 20.955
>     near_clip: 0.1
>     far_clip: 100000
>     screen_width: 960
>     screen_height: 544
> ```

**$[special\_macros]**

`$[seed]` resolves to the current frame’s seed number, and `$[frame]` resolves to the frame index.

Note

An error is triggered if a cyclic reference is detected.

Some other examples are listed below:

> You can define a macro for the path to load a USD file:
>
> ```python
> resources_root: [PATH_TO_MAIN_OBJECTS]
> main_object:
>   ...
>   usd_path:
>     distribution_type: folder
>     suffix: usd
>     value: $[/resources_root]/main_objects
> ```
>
> At runtime, the folder to sample from is resolved as `[PATH_TO_MAIN_OBJECTS]/main_objects`, so that `usd_path` is `[PATH_TO_MAIN_OBJECTS]/main_objects/[SAMPLED_FILE].usd`.
>
> ```python
> seed: 3
> penguin:
>   ...
>   count: 2
>   transform_operators:
>   - rotateY: ($[../index] + $[seed]) % $[../count] * 60
> ```
>
> At frame two, this is equivalent to:
>
> ```python
> seed: 5
> penguin_0:
>   ...
>   count: 2
>   index: 0
>   transform_operators:
>   - rotateY: (0 + 5) % 2 * 60
> penguin_1:
>   ...
>   count: 2
>   index: 1
>   transform_operators:
>   - rotateY: (1 + 5) % 2 * 60
> ```
>
> Here, `$[../index]` and `$[../count]` retrieve values from the local scope of the mutable they are in, while `$[seed]` retrieves values from the global settings.
>
> Using macros, you can describe complex scenes that have a combination of randomized transform operators for each mutable.

---

### Mutable

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/action_and_event_data_generation/ext_replicator-object/mutable.html

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

---

### Mutable Attribute

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/action_and_event_data_generation/ext_replicator-object/mutable_attribute.html

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

---

### Randomization Dependency

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/action_and_event_data_generation/ext_replicator-object/randomization_dependency.html

* [Synthetic Data Generation](../../synthetic_data_generation/index.html)
* [Action and Event Data Generation](../index.html)
* [Object Simulation and Synthetic Data Generation](../tutorial_replicator_object.html)
* Randomization Dependency: Incremental Examples

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Randomization Dependency: Incremental Examples

IRO aims to provide flexible while accurate description of randomization and relationship among randomized values using fundamental building blocks:

* [mutable attributes](mutable_attribute.html#mutable-attribute)
* [harmonizers](harmonizer.html#harmonizer)

These elements can be wired up with macros to form a DAG-like dependency tree, such that a randomized element can depend on another randomization.

Note

The images in the following examples are generated using the [embedded interface](../tutorial_replicator_object.html#embedded-interface). In the viewport, you can focus on a selected prim by pressing “F”; and then you can press “Alt + Left Mouse Button” to rotate the active camera around the selected prim.

## A Basic Example

Let’s start with a basic example: “Randomly scatter ten randomly colored cubes on a plane”. The corresponding description file is:

```python
isaacsim.replicator.object:
  version: 0.x.y
  num_frames: 3
  seed: 0
  output_path: PATH_TO_OUTPUT
  simulation_time: 1
  gravity: 981

  dome_light:
    intensity: 3000
    subtype: dome
    type: light

  cube_size: 0.5
  basic_shape:
    count: 10
    type: geometry
    subtype: cube
    tracked: true
    physics: rigidbody
    color:
      distribution_type: range
      start:
        - 0.0
        - 0.0
        - 0.0
      end:
        - 1.0
        - 1.0
        - 1.0
    transform_operators:
      - translate:
          distribution_type: range
          start:
            - -300
            - $[/cube_size] / 2 * 100
            - -300
          end:
            - 300
            - $[/cube_size] / 2 * 100
            - 300
      - rotateY:
          distribution_type: range
          start: -180
          end: 180
      - scale:
        - $[/cube_size]
        - $[/cube_size]
        - $[/cube_size]

  plane:
    type: geometry
    subtype: plane
    tracked: true
    physics: collision
    color:
      - 0.5
      - 0.7
      - 0.7
    transform_operators:
      - scale:
        - 10
        - 10
        - 10

  screen_height: 2160
  screen_width: 3840
  focal_length: 14.228393962367306
  horizontal_aperture: 20.955
  camera_parameters:
    screen_width: $[/screen_width]
    screen_height: $[/screen_height]
    focal_length: $[/focal_length]
    horizontal_aperture: $[/horizontal_aperture]
    near_clip: 0.001
    far_clip: 100000
  default_camera:
    camera_parameters: $[/camera_parameters]
    transform_operators:
      - rotateY: 30
      - rotateX: -30
      - translate:
        - 0
        - 0
        - 500
    type: camera
```

By using the [embedded interface](../tutorial_replicator_object.html#embedded-interface), you can create such a scene:

## Randomization Dependency

To take a step further, to “Randomly scatter 10 randomly colored cubes on a plane, with varying sizes from 0.5 to 1.5, and varying color from red to blue, the bigger the size, the redder it is while the smaller the size, the bluer it is”, you can do:

```python
isaacsim.replicator.object:
  version: 0.x.y
  num_frames: 3
  seed: 0
  output_path: PATH_TO_OUTPUT
  simulation_time: 1
  gravity: 981

  dome_light:
    intensity: 3000
    subtype: dome
    type: light

  size_coef:
    count: 10
    distribution_type: range
    start: 0.0
    end: 1.0
  size_min: 0.5
  size_max: 1.5
  basic_shape:
    count: 10
    type: geometry
    subtype: cube
    tracked: true
    physics: rigidbody
    color:
    - 0.0 + $[/size_coef_$[index]] * 1.0
    - 0.0 + $[/size_coef_$[index]] * 0.0
    - 1.0 + $[/size_coef_$[index]] * -1.0
    size: $[/size_min] + $[/size_coef_$[index]] * ($[/size_max] - $[/size_min])
    transform_operators:
    - translate:
        distribution_type: range
        start:
        - -300
        - $[../size] / 2 * 100
        - -300
        end:
        - 300
        - $[../size] / 2 * 100
        - 300
    - rotateY:
        distribution_type: range
        start: -180
        end: 180
    - scale:
      - $[../size]
      - $[../size]
      - $[../size]

  plane:
    type: geometry
    subtype: plane
    tracked: true
    physics: collision
    color:
      - 0.5
      - 0.7
      - 0.7
    transform_operators:
    - scale:
      - 10
      - 10
      - 10

  screen_height: 2160
  screen_width: 3840
  focal_length: 14.228393962367306
  horizontal_aperture: 20.955
  camera_parameters:
    screen_width: $[/screen_width]
    screen_height: $[/screen_height]
    focal_length: $[/focal_length]
    horizontal_aperture: $[/horizontal_aperture]
    near_clip: 0.001
    far_clip: 100000
  default_camera:
    camera_parameters: $[/camera_parameters]
    transform_operators:
    - rotateY: 30
    - rotateX: -30
    - translate:
      - 0
      - 0
      - 1000
    type: camera
```

And we get:

The bigger the redder, the smaller the bluer. This is achieved by dependent mutable attributes. The color is determined by linear interpolation between red and blue:

```python
color:
- 0.0 + $[/size_coef_$[index]] * 1.0
- 0.0 + $[/size_coef_$[index]] * 0.0
- 1.0 + $[/size_coef_$[index]] * -1.0
```

Here:

```python
basic_shape:
  count: 10
```

Resolves to:

```python
basic_shape_0:
  index: 0
basic_shape_1:
  index: 1
basic_shape_2:
  index: 2
...
```

And that goes similarly for:

```python
size_coef:
  count: 10
  distribution_type: range
  start: 0.0
  end: 1.0
```

And then for `basic_shape_0`, for example, the R channel of color, `0.0 + $[/size_coef_$[index]] * 1.0`, will resolve to `0.0 + $[/size_coef_0] * 1.0` and `$/size_coef_0` will be replaced with a randomized value between `0` and `1`. Here is a DAG chart that shows the symbol resolution process:

## Harmonization

Try to “pack the above cubes into a big box and randomly place and rotate this big box around the up axis”:

The corresponding description file:

```python
isaacsim.replicator.object:
  version: 0.x.y
  num_frames: 3
  seed: 0
  output_path: PATH_TO_OUTPUT
  simulation_time: 1
  gravity: 981

  dome_light:
    intensity: 3000
    subtype: dome
    type: light

  bin_pack_H:
    harmonizer_type: bin_pack
    bin_size:
    - 400
    - 300
    - 400
  size_coef:
    count: 50
    distribution_type: range
    start: 0.0
    end: 1.0
  size_min: 0.5
  size_max: 1.5
  bin_translate:
    distribution_type: range
    start:
    - -100
    - 150
    - -100
    end:
    - 100
    - 150
    - 100
  bin_rotate_Y:
    distribution_type: range
    start: -180
    end: 180
  basic_shape:
    count: 50
    type: geometry
    subtype: cube
    tracked: true
    physics: rigidbody
    color:
    - 0.0 + $[/size_coef_$[index]] * 1.0
    - 0.0 + $[/size_coef_$[index]] * 0.0
    - 1.0 + $[/size_coef_$[index]] * -1.0
    size: $[/size_min] + $[/size_coef_$[index]] * ($[/size_max] - $[/size_min])
    transform_operators:
    - translate: $[/bin_translate]
    - rotateY: $[/bin_rotate_Y]
    - transform:
        distribution_type: harmonized
        harmonizer_name: bin_pack_H
        pitch:
        - - -$[../../size] / 2 * 100
          - -$[../../size] / 2 * 100
          - -$[../../size] / 2 * 100
        - - $[../../size] / 2 * 100
          - $[../../size] / 2 * 100
          - $[../../size] / 2 * 100
    - scale:
      - $[../size]
      - $[../size]
      - $[../size]

  plane:
    type: geometry
    subtype: plane
    tracked: true
    physics: collision
    color:
      - 0.5
      - 0.7
      - 0.7
    transform_operators:
    - scale:
      - 10
      - 10
      - 10

  screen_height: 2160
  screen_width: 3840
  focal_length: 14.228393962367306
  horizontal_aperture: 20.955
  camera_parameters:
    screen_width: $[/screen_width]
    screen_height: $[/screen_height]
    focal_length: $[/focal_length]
    horizontal_aperture: $[/horizontal_aperture]
    near_clip: 0.001
    far_clip: 100000
  default_camera:
    camera_parameters: $[/camera_parameters]
    transform_operators:
    - rotateY: 30
    - rotateX: -30
    - translate:
      - 0
      - 0
      - 1500
    type: camera
```

Here, `translate` and `rotateY` defines the global movement of the big box (the bin), and `transform` is a harmonized mutable attribute. The global `translate` and `rotateY` has the same value for all basic shapes, though randomized per frame. This is why the mutable attributes are defined outside of the basic shapes and then referenced through macros. Had it been defined inside the `xformOps` list, each basic shape would have a different randomized value.

## Insight into the Simulation Workflow

During initialization, mutable attributes and harmonizers are initialized, and a dependency tree with mutable elements (such as mutable attributes with different distribution types, expressions with macros, and more) is created based on the description file, and then the USD runtime scene is initialized, loading all the prims that are about to be randomized.

Each frame, all the mutable attributes resolve for their values. Mutable attributes with macros, like channels of color and size in our examples resolve their dependent mutable elements (like macro expressions) recursively. The symbol resolution procedures are totally in description level, so it’s as if we are doing randomization on text; in this stage, the USD environment is not involved.

### Harmonization Process

A harmonized mutable attribute is a special mutable attribute that can’t be resolved by running resolution one time, because it needs information from other mutable attributes sharing the same harmonizer. Run it the first time to resolve the symbols, the attribute gets into an `AWAITING_HARMONIZATION` state, and then the harmonizer absorbs its pitch (in this case, the size of the cube):

All non-harmonized attributes are resolved, which is necessary because harmonized attributes may depend on them. For example, an object can be randomized to use a different USD model with a different size bounding box, which can be the pitch to be absorbed by the harmonizer. The USD runtime is then updated based on non-harmonized attributes.

After getting all the information from the harmonized attributes, the harmonizer harmonizes. It now knows where each cube’s local transformations in the big box.

The system is in `AWAITING_HARMONIZATION` state if there is at least one attribute in this state, which means you need to resolve the whole description again. Now the corresponding values are propagated back to respective harmonized attributes.

All the numbers are fixed numbers, so you can use them to update the scene again. So, the whole workflow looks like:

On this page

* [A Basic Example](#a-basic-example)
* [Randomization Dependency](#id1)
* [Harmonization](#harmonization)
* [Insight into the Simulation Workflow](#insight-into-the-simulation-workflow)
  + [Harmonization Process](#harmonization-process)

---

### Setting

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/action_and_event_data_generation/ext_replicator-object/setting.html

* [Synthetic Data Generation](../../synthetic_data_generation/index.html)
* [Action and Event Data Generation](../index.html)
* [Object Simulation and Synthetic Data Generation](../tutorial_replicator_object.html)
* Setting

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Setting

If the key-value pair in the description file is neither a [Mutable](mutable.html#mutable) nor a [Harmonizer](harmonizer.html#harmonizer), it’s a setting. You can define a description with only settings.

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

`usd_base_name` is the mutable name or the USD file base name of USD file when a geometry `mesh` is loaded, which means it’s not allowed to load different USD files with the same base name. Using `${resource_root_1}/apple.usd` and `${resource_root_1}/inner/apple.usd` in the same simulation causes unexpected behavior.

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

To also write per-frame scene captions alongside this output, the `Isaacsim.Replicator.Caption` extension’s `CombinedIROSceneGraphWriter` can replace the default writer, refer to [Use Isaacsim.Replicator.Caption in Isaacsim.Replicator.Object](../tutorial_replicator_caption.html#using-iro-extension).

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

However, if linear or angular damping is set too high, objects get lazy and they don’t move much. This can be bad in a gravity enabled setting, where we want objects to be in close contact with a surface. Because different objects have different sizes and shapes, it’s good to tune these physics properties to reach a good appearance.

Similarly, too high of a value for friction makes objects cluster if they are in close contact; while too low of a value for friction makes them slippery and glide off surfaces.

Note

If there is no object in the scene when you are expecting some objects, one reason might be that they flew away from the view frustum. Check your physics settings.

On this page

* [Required Keys](#required-keys)
* [Optional Keys](#optional-keys)

---

### Transformation

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/action_and_event_data_generation/ext_replicator-object/transformation.html

* [Synthetic Data Generation](../../synthetic_data_generation/index.html)
* [Action and Event Data Generation](../index.html)
* [Object Simulation and Synthetic Data Generation](../tutorial_replicator_object.html)
* Transformation

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Transformation

This page discusses how to move things around.

The position, orientation, and size of an object in the scene must be defined by a sequence of transform operators (also known as a scene graph). This sequence is ordered such that global transforms are towards the top, while local transforms are towards the bottom. If you are not familiar with what “global” and “local” means, here is an example:

## Scene Graph Example

Imagine that there is an observatory that has a movable base, a dome that can rotate around and a retractable scope that can rotate up and down. Inside the observatory sits a bird, Oro. You are sitting at the scope head, looking at Oro. And assume that Oro is frozen in space, so that if the observatory moves, it moves relative to Oro and you want to see Oro from different perspectives. The whole setting is:

The scope head points towards the positive direction of the Z-axis, so we are looking towards the negative direction of Z-axis. Because the scope is retractable, start at zero length, so that we are inside Oro’s body. This is the starting pose, if no transform operators are defined at all.

Define these entities in your descriptions. A camera, with camera parameters defined as described in [Camera](camera.html#camera); A [Dome light](light.html#dome-light) so that you can see things; and Oro, which is a [Geometry](geometry.html#geometry). The observatory is only conceptual, you don’t need to see it.

```python
dome_light:
  type: light
  subtype: dome
  intensity: 1000

default_camera:
  type: camera
  camera_parameters: $[/camera_parameters]

penguin:
  type: geometry
  subtype: mesh
  usd_path: [PATH_TO_PENGUIN]
```

Note

If no camera is defined, no images are output, because nothing is there to see.

Extend the scope along the Z-axis using the `translate` operator, so that you are 1000 units way from Oro, and take a picture.

```python
default_camera:
  # ...
  transform_operators:
  - translate:
    - 0
    - 0
    - 1000
```

Then rotate the scope around the X-axis by 30 degrees. This applies a `rotateX` operator, before the original translate.

```python
transform_operators:
- rotateX: -30
- translate:
  - 0
  - 0
  - 1000
```

To go the other way around, rotate the muzzle itself, and translate it along the Z-axis. In this case the camera looks away from Oro, which is not the intention.

Rotate the turret, giving another operator `rotateY`:

```python
transform_operators:
- rotateY: 60
- rotateX: -30
- translate:
  - 0
  - 0
  - 1000
```

And eventually, drive the observatory forward, which is yet another translate, so that you don’t always have Oro at the center of the screen. Because you are defining two translates, add a suffix `translate_global`:

```python
transform_operators:
- translate_global:
  - 0
  - 0
  - 1000
- rotateY: 60
- rotateX: -30
- translate:
  - 0
  - 0
  - 1000
```

Note

Duplicated names of transform operators are not allowed. Add `_suffix` to differentiate.

To randomize all transform operators with mutable attributes and generate five images:

```python
transform_operators:
- translate_global:
    distribution_type: range
    start:
    - -500
    - 0
    - -500
    end:
    - 500
    - 0
    - 500
- rotateY:
    distribution_type: range
    start: -180
    end: 180
- rotateX:
    distribution_type: range
    start: -60
    end: 60
- translate:
    distribution_type: range
    start:
    - 0
    - 0
    - 800
    end:
    - 0
    - 0
    - 1200
```

Now you have different views of Oro. The AI model you are about to train will get a better understanding of Oro.

## Transform Operators

All available transform operators are:

**Translate operator**

| Operator Name | Required Format |
| --- | --- |
| translate, rotateXYZ, rotateXZY, rotateYXZ, rotateYZX, rotateZXY, rotateZYX, scale | numeric, list of three elements |
| orient | numeric, list of four elements |
| rotateX, rotateY, rotateZ | numeric |
| transform | numeric, list of lists of four by four elements |

Required format indicates the dimension and type of expected input. `numeric` means float or int, or a value evaluated to float or int by macro or mutable attribute. For example:

```python
rotateXYZ:
- $[../index]
- 5
- 10
```

is valid, while:

```python
rotateXYZ:
- True
- abc
```

is not valid.

Note

* `orient` is represented by a quaternion in wxyz order, in which w is the scalar part; all other rotate operators describe rotation in degrees.
* The Euler angle sequence is represented from local to global from left to right. For example, rotateXYZ means Y is global rotation relative to X, and Z is global rotation relative to Y.
* Scale operators appear at the bottom. It’s not recommended to define a scale above a translate or rotate, unless this is intended.

## Practical Example of Flexible xformOps

A translation applied globally to a rotation, is different than the other way around. In an ordinary setting, from global to local, you translate, rotate, and scale an object. In IRO, you can swap the order of linear transformations, because of the flexibility in USD xformOps. To scatter cubes on a section of a sphere using only combination of randomizations in translation and rotation in a different order:

```python
isaacsim.replicator.object:
  version: 0.x.y
  num_frames: 3
  seed: 0
  output_path: PATH_TO_OUTPUT
  simulation_time: 1
  gravity: 981

  dome_light:
    intensity: 3000
    subtype: dome
    type: light

  size_coef:
    count: 400
    distribution_type: range
    start: 0.0
    end: 1.0
  size_min: 0.5
  size_max: 0.8
  basic_shape:
    count: 400
    type: geometry
    subtype: cube
    tracked: true
    physics: rigidbody
    color:
    - 0.0 + $[/size_coef_$[index]] * 1.0
    - 0.0 + $[/size_coef_$[index]] * 0.0
    - 1.0 + $[/size_coef_$[index]] * -1.0
    size: $[/size_min] + $[/size_coef_$[index]] * ($[/size_max] - $[/size_min])
    transform_operators:
    - rotateY:
        distribution_type: range
        start: -160
        end: 160
    - rotateX:
        distribution_type: range
        start: -60
        end: 0
    - translate:
        distribution_type: range
        start:
        - 0
        - 0
        - 0
        end:
        - 0
        - 0
        - 500
    - rotateXYZ:
        distribution_type: range
        start:
        - -180
        - -180
        - -180
        end:
        - 180
        - 180
        - 180
    - scale:
      - $[../size]
      - $[../size]
      - $[../size]

  plane:
    type: geometry
    subtype: plane
    tracked: true
    physics: collision
    color:
    - 0.5
    - 0.7
    - 0.7
    transform_operators:
    - scale:
      - 10
      - 10
      - 10

  screen_height: 2160
  screen_width: 3840
  focal_length: 14.228393962367306
  horizontal_aperture: 20.955
  camera_parameters:
    screen_width: $[/screen_width]
    screen_height: $[/screen_height]
    focal_length: $[/focal_length]
    horizontal_aperture: $[/horizontal_aperture]
    near_clip: 0.001
    far_clip: 100000
  default_camera:
    camera_parameters: $[/camera_parameters]
    transform_operators:
    - rotateY: 30
    - rotateX: -30
    - translate:
      - 0
      - 0
      - 5000
    type: camera
```

The created scene with [embedded interface](../tutorial_replicator_object.html#embedded-interface):

The visualization using the [distribution visualizer](distribution_visualizer.html#distribution-visualizer):

On this page

* [Scene Graph Example](#scene-graph-example)
* [Transform Operators](#transform-operators)
* [Practical Example of Flexible xformOps](#practical-example-of-flexible-xformops)

---

### Distribution Visualizer

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/action_and_event_data_generation/ext_replicator-object/distribution_visualizer.html

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

---

### Empty Space Detection

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/action_and_event_data_generation/ext_replicator-object/empty_space_detection.html

* [Synthetic Data Generation](../../synthetic_data_generation/index.html)
* [Action and Event Data Generation](../index.html)
* [Object Simulation and Synthetic Data Generation](../tutorial_replicator_object.html)
* Empty Space Detection

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Empty Space Detection

The **empty space** detector is an optional scene analysis step in `isaacsim.replicator.object`. You declare it as a top-level key in the description file (alongside other [mutables](mutable.html#mutable)) with `detector_type: empty_space`. At runtime the extension creates a temporary detector volume, voxelizes the region using ray casts, classifies free space, and writes **3D bounding boxes** and **2D polygon footprints** of detected empty regions into per-detector metadata. The implementation lives in `EmptySpaceDetector` (`mutables/detector.py`) and `SpaceDetectManager` (`mutables/detector_internal/space_detect_manager.py`).

Use it for workflows that need explicit **free-space regions** (for example bin packing, placement, or annotating voids) in addition to tracked object geometry.

## When it Runs

Detectors are initialized and run during the normal simulation workflow after the USD scene for the frame has been updated. The detector prim is removed from the stage when detection finishes. Enable visualization flags (see below) if you want to see scope, voxels, or height-span debug drawing in the viewport for that frame.

## Scope geometry (required)

Each detector entry **must** define a 3D axis-aligned scope. You can use either naming style:

| Key | Meaning | Notes |
| --- | --- | --- |
| `translate` **or** `center` | 3-vector position of the detector volume | Same units as the stage (typically meters when `default_meters_per_unit` is `1`). |
| `scale` **or** `size` | 3-vector extent of the box | Values are interpreted in **centimeters**; internally they are converted to meters for the USD transform (refer to `EmptySpaceDetector` in the extension source). |

Example (excerpt):

```python
my_empty_space_detector:
  detector_type: empty_space
  translate: [0, 0, 0.25]
  scale: [500, 500, 200]   # centimeters: width, depth, height of the analysis region
```

## Detection Parameters

Detection Parameters are optional. These keys are read from the **same** detector block (the dictionary named after your detector, for example `my_empty_space_detector`). All numeric thresholds below are in **meters** unless your scene uses a different meters-per-unit convention. Defaults match `EmptySpaceDetector.detect` in the extension.

| Key | Type | Default | Description |
| --- | --- | --- | --- |
| `cell_size` | numeric | `0.05` | Voxel / grid resolution along X and Y. |
| `cell_height_threshold` | numeric | `0.2` | Minimum vertical clearance used when classifying empty height spans. |
| `x_length_threshold` | numeric | `0.2` | Minimum extent along X for a region to count as empty space. |
| `y_length_threshold` | numeric | `0.2` | Minimum extent along Y for a region to count as empty space. |
| `exclusive_ratio_threshold` | numeric | `0.8` | Ratio used when filtering candidate regions (higher tends to retain more regions; range `0.0`–`1.0`). |
| `top_tolerance` | numeric | `0.2` | Height tolerance at the top of a span. |
| `bottom_tolerance` | numeric | `0.1` | Height tolerance at the bottom of a span. |
| `max_stack_height` | numeric / null | `None` | Optional cap on stack height in meters; `None` means no limit. |

You can drive several of these from a single root-level macro (for example a shared `cell_size` in meters) using [Macro](macro.html#macro) expressions such as `$[/cell_size] * 2.0`.

## Visualization

Visualization is optional.

| Key | Type | Description |
| --- | --- | --- |
| `visualize` | bool | Draw 3D boxes for detected free regions and 2D polygon outlines when `True`. |
| `visualize_raycast` | bool | Draw raycast or height-span debug (for example yellow height-span visualization in the sample config). |
| `visualize_color` | list | RGBA for 3D bbox drawing; default `[1, 0, 0, 0.5]`. |
| `visualize_2d_color` | list | RGBA for 2D polygon outlines; default `[0, 1, 0, 0.5]`. |
| `visualize_scope` | bool | Show the detector scope as a wireframe when `True`; default `True` when visualization runs. |

## Visualization Color Legend

When debug draw is available (`isaacsim.util.debug_draw`), the viewport uses the following default colors. You can change the 3D box and 2D outline colors with `visualize_color` and `visualize_2d_color`. The other colors listed below are fixed in `space_detect_visualization.py`.

| Color (default) | Meaning | Notes |
| --- | --- | --- |
| **Yellow** wireframe (RGBA `1, 1, 0, 0.3`) | Detector **scope** (analysis volume) | The axis-aligned box you defined with `translate`/`center` and `scale`/`size`. Shown when `visualize` is `True` and `visualize_scope` is `True`. |
| **Red** wireframe (default `visualize_color`: `1, 0, 0, 0.5`) | **3D empty-space** result | One box per detected free region: edges of the 3D bounding boxes written to `detected_space_3d`. |
| **Green** polylines (default `visualize_2d_color`: `0, 1, 0, 0.5`) | **2D empty-space** result (footprint) | Outlines of free regions projected to the ground plane (near `min_height`), matching `detected_space_2d` outlines. |
| **Magenta** (`1, 0, 1, 0.5`) | **Holes** inside 2D regions | Fixed color for hole boundaries; not controlled by YAML. |

If `visualize_raycast` is `True`, raycast and height-span debug lines are
drawn in addition to the colors above:

| Color | Meaning | Notes |
| --- | --- | --- |
| **Yellow** vertical segments (`1, 1, 0, 0.5`) | Per-voxel **height span** along the cast direction | One vertical line per free height interval in the voxelization grid. |
| **Red** points (`1, 0, 0, 0.5`) | **Base** of each span | Lower bound of a height interval. |
| **Green** points (`0, 1, 0, 0.5`) | **Ceiling** of each span | Upper bound of a height interval. |

The raycast green points are not the same as the green 2D polygon outlines. Turn
off `visualize_raycast` if you only want the final 2D and 3D empty-space
overlays.

## Outputs

After `detect` completes, the extension stores results on the metadata entry for that detector key:

* `detected_space_3d`: list of dicts with `translate` and `scale` (each axis-aligned free region in world space).
* `detected_space_2d`: serialized polygons (`id`, `min_height`, `max_height`, `outline`, `holes`) suitable for logging or downstream tools.

Exact consumption of these fields in written outputs depends on your [output switches](setting.html#output-switches) and description logging pipeline.

## Example Configuration

The extension ships a full demo that uses a **Z-up** stage, basic primitives on a floor, and an `empty_space` detector with macros and visualization enabled:

`PATH_TO_CORE_EXTENSION/isaacsim/replicator/object/core/configs/demo_empty_space.yaml`

Select that YAML from the **Object SDG** panel, or pass it as
`--/config/file=...` when running headless, to reproduce the workflow
end to end.

Viewport with `demo_empty_space.yaml`. The following colors appear in the
viewport:

* **Yellow wireframe**: The detector scope.
* **Red boxes**: 3D empty-space results.
* **Green outlines**: 2D footprints.

When `visualize_raycast` is enabled, additional elements appear as described
in the preceding legend:

* **Yellow vertical segments**: Raycast lines.
* **Red and green span points**: Height-span sample points.

On this page

* [When it Runs](#when-it-runs)
* [Scope geometry (required)](#scope-geometry-required)
* [Detection Parameters](#detection-parameters)
* [Visualization](#visualization)
* [Visualization Color Legend](#visualization-color-legend)
* [Outputs](#outputs)
* [Example Configuration](#example-configuration)

---

### Chat IRO

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/action_and_event_data_generation/ext_replicator-object/ext_chat_iro.html

* [Synthetic Data Generation](../../synthetic_data_generation/index.html)
* [Action and Event Data Generation](../index.html)
* [Object Simulation and Synthetic Data Generation](../tutorial_replicator_object.html)
* Chat IRO: Natural Language Interface for Isaac Sim Replicator Object

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Chat IRO: Natural Language Interface for Isaac Sim Replicator Object

Vision-language and scene-generation workflows often require users to hand‑write
YAML configuration files for [Isaacsim.replicator.object](../tutorial_replicator_object.html#isaac-sim-app-tutorial-replicator-object) (IRO).
This can be error‑prone and slow, especially for complex layouts, harmonizers,
physics setups, and camera rigs.

`Chat IRO` is a natural‑language interface that converts plain English
descriptions into executable IRO YAML configurations and runs them directly
inside Isaac Sim. It sits on top of the IRO extension and automates
configuration authoring, validation, and execution.

Chat IRO has the following features:

* Convert English descriptions into IRO YAML scenes.
* Use a Retrieval‑Augmented Generation (RAG) system with thousands of
  production YAML examples to improve correctness and reuse best practices.
* Validate generated YAML for syntax and common structural issues before
  execution.
* Preview the generated scene immediately in the Isaac Sim viewport.
* Save and reload configuration files for iterative workflows.

## Workflow

Chat IRO uses the following workflow to generate scenes:

1. You type a natural‑language request such as
   `Create a scene with 10 random size and color cubes` into the
   Chat IRO window.
2. The extension optionally queries its RAG index of existing IRO YAML files
   and injects relevant examples into the LLM context.
3. The LLM generates a candidate YAML configuration for
   `isaacsim.replicator.object`.
4. Chat IRO validates the YAML, fixes common issues, and executes it through
   IRO to create or update the scene.
5. The resulting synthetic scene is rendered in the viewport. You can
   iteratively refine the configuration by sending follow‑up prompts.

### Prerequisites

Before using Chat IRO, ensure the following requirements are met:

* `isaacsim.replicator.object.ui` extension enabled
* A supported operating system (Linux is the primary platform; Windows is
  experimental).
* An NVIDIA GPU with CUDA support (recommended).
* At least 8 GB of RAM (16 GB or more is recommended for large scenes).
* The `omni.ai.langchain.agent.chat_iro` extension enabled.
* A valid NVIDIA API key for LLM access.

Note

The LLM features require a valid NVIDIA API key and sufficient
credits. Visit the [NVIDIA API portal](https://build.nvidia.com) to
obtain a key and manage credits. See the [NVIDIA API reference page](https://docs.api.nvidia.com/nim/reference/llm-apis) for more details.

## Enable `Chat IRO` Extension

1. Follow the [Omniverse Extension Manager guide](https://docs.omniverse.nvidia.com/extensions/latest/ext_core/ext_extension-manager.html)
   to enable the `omni.ai.langchain.agent.chat_iro` extension.
2. Launch Isaac Sim and open the Extension Manager if it is not already open:

   * In the main menu, select **Window > Extensions**.
   * Search for `Chat IRO`.
   * Enable the extension and optionally enable **AUTOLOAD** so it is loaded
     automatically on future launches.
3. Configure the NVIDIA API key by setting it as an environment variable.

   **Linux/macOS**

   ```python
   # Set API key for the current shell session
   export NVIDIA_API_KEY="nvapi-YOUR-KEY-HERE"

   # Make the setting persistent (for bash)
   echo 'export NVIDIA_API_KEY="nvapi-YOUR-KEY-HERE"' >> ~/.bashrc
   source ~/.bashrc
   ```

   **Windows (Command Prompt)**

   ```python
   REM Set API key for the current Command Prompt session
   set NVIDIA_API_KEY=nvapi-YOUR-KEY-HERE

   REM To make the setting persistent, add the variable in
   REM System Properties > Environment Variables.
   ```

Note

If LLM authentication fails, verify that `NVIDIA_API_KEY` is set
and has remaining credits.

### Accessing the Chat IRO Panel

Once the extension is enabled:

1. Open the main Chat IRO window:

   * From the menu bar, select **Window > Chat IRO**.
   * A dockable Chat IRO panel opens, typically on the right side of the
     viewport.
2. Select a model from the **Model** drop‑down menu. Verified working models include:

   * `meta/llama-4-maverick-17b-128e-instruct` (recommended, 256K context, default)
   * `qwen/qwen3-next-80b-a3b-instruct` (128K+ context)
   * `openai/gpt-oss-120b` (128K context)
   * `openai/gpt-oss-20b` (128K context)
3. After selecting a model, check the status line in the Chat IRO panel. If
   you see no errors, the model is ready and the extension is authenticated.

### Using Chat IRO

Chat IRO can be used in the following ways:

* [Using the UI panel](#chat-iro-using-ui-panel)
* [Generating new IRO scenes](#chat-iro-generate-scenes)
* [Editing existing IRO YAML files](#chat-iro-edit-yaml)

### Using the UI Panel

To create and preview scenes using the Chat IRO panel:

1. In the Chat IRO input box, type a prompt such as:

   ```python
   Create a scene with 7 cubes and 6 spheres. All objects are randomly positioned, random color, and sized.
   ```
2. Press `Enter` to send the prompt.
3. Chat IRO retrieves relevant YAML patterns from its RAG index, generates
   an IRO configuration, validates it, and executes it in Isaac Sim.
4. Inspect the viewport to verify that the generated scene matches the
   requested behavior (object counts, colors, positioning, lighting, and
   camera placement).
5. Refine the scene with follow‑up prompts that modify the existing
   configuration. For example:

   ```python
   Make all cubes blue and add rigidbody physics
   ```

   The extension updates the YAML configuration in place, reapplies it, and
   refreshes the viewport.
6. By default, configuration files are automatically stored in a directory similar to:

   `~/Documents/ChatIRO_Results/config_files/my_scene.yaml`

   You can also specify a custom path by asking Chat IRO to save the file to a different location.

### Generating New IRO Scenes

Chat IRO is optimized for generating complete IRO scenes from concise,
well‑specified prompts. Good prompts include:

* `Create 20 purple cubes arranged in a circular formation with radius 900 at Y = 50.`
* `Pack 8 cubes and 6 spheres scaled 1.2x into a bin sized (300, 400, 500) at (5, 0, 0).`

For example, the following prompt:

```python
Create a scene with 7 cubes and 6 spheres. All objects are randomly positioned,
random color, and sized.
```

will typically produce an IRO configuration similar to:

```python
isaacsim.replicator.object:
  version: 0.10.0
  parent_config: standard
  seed: 42
  num_frames: 10
  output_path: /Documents/ChatIRO_Results
  screen_height: 2160
  screen_width: 3840
  focal_length: 14.228393962367306
  horizontal_aperture: 20.955

  camera_parameters:
    screen_width: $[/screen_width]
    screen_height: $[/screen_height]
    focal_length: $[/focal_length]
    horizontal_aperture: $[/horizontal_aperture]
    near_clip: 0.001
    far_clip: 100000

  cube:
    count: 7
    type: geometry
    subtype: cube
    tracked: true
    color:
      distribution_type: range
      start:
      - 0
      - 0
      - 0
      end:
      - 1
      - 1
      - 1
    transform_operators:
    - rotateX: 0
    - rotateY: 0
    - rotateZ: 0
    - translate:
        distribution_type: range
        start:
        - -500
        - 50
        - -500
        end:
        - 500
        - 50
        - 500
    - scale:
        distribution_type: range
        start:
        - 0.5
        - 0.5
        - 0.5
        end:
        - 1.5
        - 1.5
        - 1.5

  sphere:
    count: 6
    type: geometry
    subtype: sphere
    tracked: true
    color:
      distribution_type: range
      start:
      - 0
      - 0
      - 0
      end:
      - 1
      - 1
      - 1
    transform_operators:
    - rotateX: 0
    - rotateY: 0
    - rotateZ: 0
    - translate:
        distribution_type: range
        start:
        - -500
        - 50
        - -500
        end:
        - 500
        - 50
        - 500
    - scale:
        distribution_type: range
        start:
        - 0.5
        - 0.5
        - 0.5
        end:
        - 1.5
        - 1.5
        - 1.5

  default_camera:
    camera_parameters: $[/camera_parameters]
    transform_operators:
    - rotateX: -30
    - rotateY: 45
    - rotateZ: 0
    - translate:
      - 0
      - 0
      - 1000
    - scale:
      - 1
      - 1
      - 1
    type: camera

  dome_light:
    intensity: 1500
    subtype: dome
    transform_operators:
    - rotateX: 270
    type: light
```

#### More Prompt Examples

Use these prompts to explore richer scenes:

**Bin packing**

```python
Create a scene that packs 8 spheres and 10 cubes scaled 1.2 times
into a bin sized (300, 400, 500) at position (5, 0, 0)
```

**Grid layout**

```python
Create 25 cubes arranged in a 5x5 grid with spacing of 100 units
```

**Physics**

```python
Create 20 spheres with rigidbody physics falling from height 500
onto a ground plane
```

Note

Complex mathematical layouts (for example, circular or grid‑based
arrangements) may require a few iterations. If object placement does not
match expectations, use a follow‑up prompt that focuses only on correcting
the formulas or spacing.

#### Using Existing USD Scenes

You can also reference existing USD stages or assets in your prompts:

**Create a warehouse stage**

```python
Create a warehouse environment with the following settings:

WAREHOUSE:
USD: /home/user/Assets/warehouse.usd
Apply collision physics.
Scale the warehouse to 100 times its original size.
Rotate the warehouse -90 degrees on the X-axis.

CAMERA:
Position randomly between 1800-2000 units away on Z-axis.
Rotate randomly -180 to 180 degrees on Y-axis.
Tilt -30 degrees on X-axis for overhead view.
Set the number of frames to 30.
```

Note

Prompts that reference existing USD stages or assets require those USD files
(and their dependencies) to be available locally. Chat IRO loads the stage
and assets into the scene so it can reference them in the generated YAML
configuration. The configuration options shown in the examples above are
illustrative; you can use any other settings supported by the IRO extension.

### Editing Existing IRO YAML Files

Chat IRO can also load and modify YAML configuration files that you have
created manually or with other tools.

Typical workflow:

1. Ask Chat IRO to load a file:

   ```python
   load /home/user/Documents/ChatIRO_Results/config_files/my_scene.yaml
   ```
2. Inspect the generated scene in the viewport.
3. Apply edits using natural language, such as:

   ```python
   Add 5 more cubes with random colors.

   Increase dome light intensity to 3000.

   Add a rotating camera that orbits the scene 360 degrees.
   ```
4. Save the updated configuration:

```python
save /absolute/path/to/my_scene_v2.yaml
```

Behind the scenes, Chat IRO reuses the same validation and execution pipeline
used for newly generated configurations.

### Managing Output Files and Directories

By default, Chat IRO saves generated configuration files and simulation
outputs to a structured directory under your home folder.

#### Default Output Location

All Chat IRO outputs are organized in:

```python
~/Documents/ChatIRO_Results/
├── config_files/              # YAML configuration files
├── simulation_results/        # IRO simulation outputs
└── .cache/                    # Temporary files (hidden)
```

* The `config_files/` directory contains YAML files that define scenes.
* The `simulation_results/` directory contains rendered images, sensor
  data, and other outputs generated when executing the YAML configurations.
* The `.cache/` directory stores temporary processing files.

Note

If `~/Documents/ChatIRO_Results/` does not exist, Chat IRO creates it
automatically on first use.

#### Changing the Output Directory

You can change the default output directory with an environment variable:

```python
# Linux/macOS
export CHAT_IRO_OUTPUT_DIR="~/MyProjects/IRO_Results"

# To make it persistent, add to your shell startup file, for example:
echo 'export CHAT_IRO_OUTPUT_DIR="~/MyProjects/IRO_Results"' >> ~/.bashrc
source ~/.bashrc
```

```python
REM Windows (Command Prompt)
set CHAT_IRO_OUTPUT_DIR=C:\Users\YourName\IRO_Results

REM Add to System Environment Variables for persistence
```

Note

Advanced users can also configure the default output directory in the
Chat IRO extension settings or via the Python APIs that ship with the
extension.

#### Natural‑Language File Commands

Chat IRO understands simple text commands for loading, saving, and running
configurations:

**Loading files**

```python
load /path/to/my_scene.yaml
```

**Saving files**

```python
save /absolute/path/to/my_warehouse_scene.yaml

save this as /absolute/path/to/production_config.yaml
```

**Simulating with specific parameters**

```python
simulate with seed 123
```

Note

For reliable behavior, always specify an absolute path when saving, for example:
`save /absolute/path/to/my_scene.yaml`. Using only a file name (for example,
`save my_scene.yaml`) is not recommended because the save location can vary
depending on your environment and configuration.

### Chat IRO RAG Configuration

Chat IRO includes a Retrieval‑Augmented Generation system that provides deep
knowledge of existing IRO scenes and best‑practice configurations.

The behavior of the RAG system can be customized in `extension.toml`:

```python
[settings.exts."omni.ai.langchain.agent.chat_iro"]
enable_rag = true                  # Enable/disable RAG (default: true)
rag_top_k = 15                     # Number of documents to retrieve
rag_max_tokens = 8000              # Maximum tokens for RAG context
enable_multi_query_rag = true      # Enable multi‑query decomposition
max_sub_queries = 3                # Maximum number of sub‑queries

# Optional cross‑encoder reranking
enable_rag_reranking = false
reranker_model = "BAAI/bge-reranker-large"
```

When enabled, RAG allows Chat IRO to:

* Break complex prompts into multiple focused sub‑queries.
* Retrieve relevant YAML snippets for geometry, harmonizers, and cameras.
* Merge and rerank results to provide higher‑quality configurations.

Note

Enabling cross‑encoder reranking typically improves retrieval accuracy by
10–30% at the cost of additional latency (around 100–200 ms per request).
For simple prompts or low‑latency environments, keep
`enable_rag_reranking = false`.

### Best Practices

Chat IRO relies on LLMs that interpret natural language. Clear, specific
prompts lead to more reliable IRO configurations.

Recommended prompting guidelines:

* Specify concrete numbers rather than vague terms.

  *Good:* `Create 20 cubes in a circular formation with radius 900 at Y = 50.`

  *Avoid:* `Create some objects in a circle.`
* Explicitly describe sizes, positions, and physics requirements.
* Build scenes iteratively and validate each step in the viewport.
* Save working configurations frequently and version them as you refine.

If the generated YAML does not execute or the scene appears empty:

* Ask Chat IRO to regenerate with corrected structure, for example:

  ```python
  Regenerate the configuration using valid YAML syntax and complete
  all missing parameters.
  ```
* Focus corrective prompts on specific errors (spacing, rotations, counts,
  physics flags) instead of rewriting the entire scene.

### Troubleshooting

Common issues and remedies:

**LLM authentication failed**

* Symptom: Error message about missing or invalid API key; no YAML generated.
* Action: Verify `NVIDIA_API_KEY` in your environment and `extension.toml`,
  confirm that your account has remaining credits, and restart Isaac Sim.

**No scene is rendered**

* Symptom: Chat IRO responds, but the viewport remains empty.
* Action:

  + Inspect the generated YAML in the Chat IRO window.
  + Look for error messages in the Isaac Sim console or logs.
  + Try a simple prompt such as `Create 5 cubes` to verify basic behavior.

**YAML syntax errors**

* Symptom: Messages such as `Failed to parse YAML`.
* Action:

  + Ask Chat IRO to fix the YAML syntax.
  + Simplify the prompt and ensure that you request a single, self‑contained
    configuration.

**Slow responses**

* Symptom: Noticeable delay between sending a prompt and receiving an answer.
* Action:

  + Reduce `rag_top_k` and disable reranking in `extension.toml`.
  + Split very complex scenes into multiple, smaller prompts.

### Session Management

Over very long sessions, the LLM may drift from the original constraints or
produce inconsistent configurations.

To reset the conversation:

* Click the \(+\) button in the upper‑left corner of the Chat IRO window to
  start a new session.
* Optionally restart Isaac Sim if behavior remains inconsistent.
* Begin the new session with a clear instruction such as:

  ```python
  You are a YAML configuration generator for Isaac Sim Replicator Object.
  Generate only valid YAML with proper structure. Create a scene with
  10 cubes in a grid layout.
  ```

On this page

* [Workflow](#workflow)
  + [Prerequisites](#prerequisites)
* [Enable `Chat IRO` Extension](#enable-chat-iro-extension)
  + [Accessing the Chat IRO Panel](#accessing-the-chat-iro-panel)
  + [Using Chat IRO](#using-chat-iro)
  + [Using the UI Panel](#using-the-ui-panel)
  + [Generating New IRO Scenes](#generating-new-iro-scenes)
    - [More Prompt Examples](#more-prompt-examples)
    - [Using Existing USD Scenes](#using-existing-usd-scenes)
  + [Editing Existing IRO YAML Files](#editing-existing-iro-yaml-files)
  + [Managing Output Files and Directories](#managing-output-files-and-directories)
    - [Default Output Location](#default-output-location)
    - [Changing the Output Directory](#changing-the-output-directory)
    - [Natural‑Language File Commands](#naturallanguage-file-commands)
  + [Chat IRO RAG Configuration](#chat-iro-rag-configuration)
  + [Best Practices](#best-practices)
  + [Troubleshooting](#troubleshooting)
  + [Session Management](#session-management)

---


## 教程

### Replicator Object Tutorial

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/action_and_event_data_generation/tutorial_replicator_object.html

* [Synthetic Data Generation](../synthetic_data_generation/index.html)
* [Action and Event Data Generation](index.html)
* Object Simulation and Synthetic Data Generation

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Object Simulation and Synthetic Data Generation

`isaacsim.replicator.object` (IRO) is a no-code-change-required tool that generates synthetic data for model training that can be used on a range of tasks from retail object detection to robotics. The extension can be run from the UI or the `isaac-sim` container.

It takes a YAML description file that describes a mutable scene, or a hierarchy of such stacked description files as input, and outputs a description file along with graphics content including RGB, 2D/3D bounding boxes, and segmentation masks.

## Motivation

Training deep learning models with synthetic data is in high demand, while 3D software that is used to generate synthetic data often take a long time to learn, including stages such as getting familiar with UI panels. IRO aims at providing you an easy way to compose scenes that are uniquely domain randomized. For example, a typical user for this product is a data scientist without experience in using 3D modeling software, such as Maya and 3ds Max.

In a domain randomization scenario, rather than the actual detailed content in the 3D scene, a data scientist often focuses more on the rules that governs how the scene is randomized, and the relationship among these randomized rules. IRO provides a set of tools, using macros, to abstractly, intuitively, and compactly describe a randomized 3D scene.

## Chat IRO: Natural Language Interface for IRO

Chat IRO is a new extension that lets you describe scenes in plain English and automatically generates IRO description files (YAML). It applies the configuration to the stage, shows an immediate viewport preview, can run simulations, and supports saving and loading YAML files enabling fast, iterative scene authoring without manual YAML editing.

* [Chat IRO: Natural Language Interface for Isaac Sim Replicator Object](ext_replicator-object/ext_chat_iro.html)

## End-to-end Pipeline

An end-to-end pipeline is made up of groupings of the larger steps that go into using IRO.

**Acquire Graphics Resources**

To compose a randomized scene, IRO requires imported 3D models to be in USD format. Common 3D formats such as Wavefront OBJ can be converted to USD using [asset converter](https://docs.omniverse.nvidia.com/extensions/latest/ext_asset-converter.html).

**Compose a Description File**

The specifications of a description file is described in this multi-page documentation. It’s recommended that you start with the video guides in [best practices](#best-practices).

**Generate Synthetic Data**

Follow the guidelines below to run IRO.

**Train a CV Model; Deployment and Real-World Application**

An example notebook showing steps to train an object detection model on the synthetic images created using IRO is in TAO 6.0.

## Run from the UI

1. Follow the [Omniverse Extension Manager guide](https://docs.omniverse.nvidia.com/extensions/latest/ext_core/ext_extension-manager.html) to enable the `isaacsim.replicator.object.core` and `isaacsim.replicator.object.ui` extensions.
2. If the extension is successfully enabled, Object SDG panel will be available at the top right, and **Tools** > **Action and Event Data Generation** will have options **Object SDG** and **Distribution Visualizer**.

   If not, disable and enable the extension again. The Object SDG panel is turned on by default, and you can turn it off or on again by **Tools** > **Action and Event Data Generation** > **Object SDG**.
3. Click on the folder icon or the Visual Studio Code icon on the right side of the opened extension panel as shown above. The root folder of the extension opens.
4. Under `PATH_TO_CORE_EXTENSION/isaacsim/replicator/object/core/configs` there are many description files in YAML format.
   It’s recommended that you start with `demo_kaleidoscope.yaml`. For [empty space detection](ext_replicator-object/empty_space_detection.html#empty-space-detection), use `demo_empty_space.yaml` and refer to the linked catalog page.
5. Go to `global.yaml` and update `output_path` to any local folder where you can store the simulation output.

Note

Select description files from the dropdown below the **Simulate** button. When the extension is loaded, all `.yaml` files in the configs folder will have their names included in this list.

**Placeholders in description files**

Some example description files have placeholders. The paths need to be replaced with valid paths.

For example:

* In `global.yaml` and `minimum.yaml`, replace `PATH_TO_OUTPUT` with a valid path.
* In `demo_bottle.yaml`, replace `PATH_TO_LABEL_IMAGES` with a folder that contains JPEG images.
* For `tutorial_harmonizer_permutate.yaml`, `demo_macro.yaml`, `tutorial_macro.yaml`, `tutorial_scene_graph.yaml` and `tutorial_scene_graph_randomized.yaml` to run:

  > + replace `PATH_TO_ORO` in `global.yaml` with the absolute path of `data/oro_tutorial_models/oro.usd` in the extension’s root folder.
* In `doc_observatory.yaml`:

  > + replace `PATH_TO_OBSERVATORY_SCOPE` with the absolute path of `data/oro_tutorial_models/observatory_scope.usd`
  > + replace `PATH_TO_OBSERVATORY_BASE` with the absolute path of `data/oro_tutorial_models/observatory_base.usd`
  > + replace `PATH_TO_OBSERVATORY_SHAFT` with the absolute path of `data/oro_tutorial_models/observatory_shaft.usd`.
* To make `demo_bin_pack.yaml`, `demo_bins_of_bins_rack_2_layers.yaml`, `demo_bins_of_bins_rack.yaml`, `demo_bins_of_bins.yaml`, `demo_table.yaml` and `demo_transform_operator.yaml` work:

  > + replace `PATH_TO_BOXES` with a folder containing USD files of boxes (or other USDs) in `global.yaml`.
* In `demo_shader_attributes.yaml`,
  :   + replace `PATH_TO_USD` with a path to a USD file.
* In `demo_frustum.yaml`:

  > + replace `PATH_TO_MAIN_OBJECTS` with a folder containing USD files to be used as main objects.
  > + replace `PATH_TO_DISTRACTORS` with a folder containing USD files to be used as distractors.
  > + replace `PATH_TO_BACKGROUND_IMAGES` with a folder containing JPEG images to be used as background images.

You can adjust the scale, if things are not showing up correctly, because different USD files have different sizes.

1. Select `demo_kaleidoscope` from the dropdown box; `demo_kaleidoscope` will appear in the **Description File** text box. You can also use the full absolute path `PATH_TO_CORE_EXTENSION/isaacsim/replicator/object/core/configs/demo_kaleidoscope.yaml` to load a description file.
2. Click **Simulate** to start the simulation. The progress bar will show the simulation progress.

In the above and following content, `PATH_TO_CORE_EXTENSION` varies, for **Isaac on Windows** it is something like `C:\isaacsim\extscache\isaacsim.replicator.object.core-0.x.y\isaacsim\replicator\object\core\configs\demo_kaleidoscope.yaml`, while for **Isaac on Linux** it is something like `~/isaacsim/extscache/isaacsim.replicator.object.core-0.x.y/isaacsim/replicator/object/core/configs/demo_kaleidoscope.yaml`

A guide on how to use the extension is available [here](#best-practices).

## Run from Docker

To install the Isaac Sim Docker container, visit [Container Deployment](../installation/install_container.html#isaac-sim-setup-remote-headless-container).

To run the Isaac Sim Docker container:

```python
docker run --gpus device=0 --entrypoint /bin/bash -v LOCAL_PATH:/tmp --network host -it ISAAC_SIM_DOCKER_CONTAINER_URL
```

Accordingly, update `global.yaml` to have `output_path` to be any folder under `/tmp`.

For example, to launch the simulation with `demo_kaleidoscope`:

```python
bash isaac-sim.sh --no-window --enable isaacsim.replicator.object.core --allow-root --/log/file=/tmp/isaacsim.replicator.object.log --/log/level=warn --/windowless=True --/config/file=PATH_TO_CORE_EXTENSION/isaacsim/replicator/object/core/configs/demo_kaleidoscope.yaml
```

`/tmp/isaacsim.replicator.object.log` contains the messages from execution as well as from the extension. You can search the messages from the extension by filtering the file with METROPERF.

Note

If it is not generating anything on the first run inside Docker container, run it again.

## Embedded Interface

When writing graphics content to disk is not needed, the embedded interface is a quick way to prototype a description file.

To use the embedded interface, select a description file, and then click on the **Initialize Scene Randomization** button in the **Object Detection SDG** panel to load the description file. Randomization symbols will be created and connected accordingly. From then on, the scene is randomized per click on the **Randomize Scene** button.

Note

After clicking on the **Initialize Scene Randomization** button and before clicking on the **Randomize Scene** button, it is normal that the viewport is black. To see anything of interest at this stage, press “F” to focus on the selected prim.

To preview physically, click on the triangular **Play** button on the left column of widgets.

## Expected Output

After the simulation, the output is stored in `output_path`. The output content is determined by the [output switches](ext_replicator-object/setting.html#output-switches) setting.

For example, the image output of `demo_bottle` is:

While the segmentation output is:

The 2D bounding box is:

```python
bottle_0 0 -1.0 0 1028 333 1362 2159 0 0 0 0 0 0 0
bottle_1 0 -1.0 0 1895 112 2277 1694 0 0 0 0 0 0 0
bottle_2 0 -1.0 0 1281 462 1854 2159 0 0 0 0 0 0 0
```

in which the four positive numbers indicate `x_min`, `x_max`, `y_min`, `y_max`. The number `-1` is where the occlusion rate should be, but because a bottle is transparent, it is `-1` here.

As another example, the image output of `demo_kaleidoscope` is:

While the segmentation output is:

## Concepts

Description File

The description file is a YAML file that has a main key named `isaacsim.replicator.object`.

The description file consists of key-value pairs. Each key-value pair is a [Mutable](ext_replicator-object/mutable.html#mutable), a [Harmonizer](ext_replicator-object/harmonizer.html#harmonizer), or a [Setting](ext_replicator-object/setting.html#setting).

The description file generates frames as specified. Each frame the scene is randomized, [graphics content](ext_replicator-object/setting.html#output-switches) is captured, and output to disk. [Settings](ext_replicator-object/setting.html#setting) describe how the scene is configured and how data is output. For example, you can set the number of frames to output, whether or not to output 2D bounding boxes, or set the gravity and friction of physics simulation.

The description file populates the scene with objects that are called [mutables](ext_replicator-object/mutable.html#mutable).

Mutables randomize every frame. Sometimes you might want to constrain how they randomize. For example, to know how other mutables are randomizing and randomize correspondingly. To do so, define [harmonizers](ext_replicator-object/harmonizer.html#harmonizer).

Example Minimal Description File Definition

```python
isaacsim.replicator.object:
   version: 0.x.y
   num_frames: 3
   output_path: OUTPUT_PATH
   screen_height: 1080
   screen_width: 1920
   seed: 0
```

Simulation Workflow

Every time a simulation is launched, an initialization stage happens in the beginning, and a per-frame simulation stage happens every frame.

In the initialization stage, the description file is parsed by a description parser. Symbols are created for every [mutable attribute](ext_replicator-object/mutable_attribute.html#mutable-attribute) that requires a resolution to get its actual value. These symbols will resolve to actual values when they are used to interact with the USD scene once, after they are initialized; and also in every per-frame simulation.

Each time a symbol is resolved, the dependent symbols of it are also recursively resolved. If an unresolved harmonized mutable attribute is met, the parser enters `AWAITING_HARMONIZATION` status, and then the [harmonizers](ext_replicator-object/harmonizer.html#harmonizer) harmonizes (collect information from the `pitch` attribute and randomize), and propagate output back to harmonized mutable attributes. After all harmonized mutable attributes are resolved, the parser will be out of `AWAITING_HARMONIZATION` status.

After this, the resolved values are used to update the USD scene. If gravity is turned on, physics is resolved so that objects move away from each other when they overlap or drop onto a surface (for more details, refer to [physics simulation explained](ext_replicator-object/setting.html#physics-simulation-explained)). And [graphics content](ext_replicator-object/setting.html#output-switches) is captured. Eventually, the state of the scene in this frame is recorded and saved, such that later on, it can be restored or inspected.

More details can be found in [harmonization example](ext_replicator-object/randomization_dependency.html#harmonization-example).

Scene Restoration

To support multiple-sampling for pretrained models:

In the output content, you can use the output saved from logging of a specific frame to generate the exact same graphics content as when this frame was generated. Or you can slightly modify it to have something different but everything else is the same.

## Main Simulation Workflow Walkthrough

Here is a walkthrough on how to run the main simulation workflow.

The first step is to set the description files. Turn on the extension manager, search for `isaacsim.replicator.object.core`, and click on the **Open Extension Folder** button, as shown below.

Note

If `isaacsim.replicator.object.core` and/or `isaacsim.replicator.object.ui` are not enabled, click on the capsule icons to enable them.

In the folder, go to `PATH_TO_CORE_EXTENSION/isaacsim/replicator/object/core/configs`. On Windows, the folder is opened after the **Open Extension Folder** button is clicked. On Linux, it can bring up the browser with the URL as `file://EXTENSION_PATH`, in this case, navigate to `EXTENSION_PATH` using the command line or `xdg-open`.

Edit the `global.yaml` file. Set `OUTPUT_PATH` to a folder where you want to store the output. Also, update `PATH_TO_BOXES` to a folder that contains USD files of boxes.

Select `demo_table` from the dropdown box, and click on the **Simulate** button. The simulation will run, and the output will be stored in the folder specified by `OUTPUT_PATH`.

## Compose a Description File

To compose a description file that generates a scene that has a table with randomized objects dropping onto it:

Suppose we have the following assets:

* an HDRI texture for the dome light at `PATH_TO_HDRI`
* a USD model as a table at `PATH_TO_TABLE`
* a folder that contains USD models of objects to be scattered onto the table at `PATH_TO_OBJECTS`

Plan the distribution of graphics assets before composing a description file. The assets are dragged into the viewport, to get an idea of them, refer to the image. Here a dome light is created, and its texture is set to `PATH_TO_HDRI`; then a table from `PATH_TO_TABLE`; then one of the objects from `PATH_TO_OBJECTS`.

Adjust the position of the object about to be scattered onto the table, for a reasonable range of its position.

From observation, from `(-13, 100, -70)` to `(13, 100, 70)` is a reasonable range for the position of the box. Compose a description file as follows:

```python
isaacsim.replicator.object:
  # the minimum
  version: 0.x.y
  num_frames: 3
  seed: 0
  output_path: PATH_TO_OUTPUT
  screen_height: 2160
  screen_width: 3840

  # physics parameters
  gravity: 10000
  friction: 0.3
  simulation_time: 10
  linear_damping: 4

  # light
  bright_light:
    type: light
    subtype: dome
    intensity: 1000
    transform_operators:
    - rotateX: 270
    texture_path: PATH_TO_HDRI

  # camera; transforms page has more details on how to construct a list of transform operators
  focal_length: 14.228393962367306
  horizontal_aperture: 20.955
  camera_parameters:
    screen_width: $[/screen_width]
    screen_height: $[/screen_height]
    focal_length: $[/focal_length]
    horizontal_aperture: $[/horizontal_aperture]
    near_clip: 0.001
    far_clip: 100000
  default_camera:
    type: camera
    camera_parameters: $[/camera_parameters]
    transform_operators:
    - translate:
      - 0
      - 50
      - 0
    - rotateY:
        distribution_type: range
        start: -180
        end: 180
    - rotateX: -30
    - translate_local:
      - 0
      - 0
      - 400

  # boxes
  box:
    count: 10
    type: geometry
    subtype: mesh
    physics: rigidbody # reacts to gravity, collisions, etc.
    tracked: true # if true, the bounding boxes, segmentation, etc. will be recorded in the output
    usd_path:
      distribution_type: folder
      value: PATH_TO_OBJECTS
      suffix: usd
    transform_operators:
    - translate: # as planned
        distribution_type: range
        start:
        - -13
        - 100
        - -70
        end:
        - 13
        - 100
        - 70
    - rotateXYZ:
        distribution_type: range
        start:
        - -180
        - -180
        - -180
        end:
        - 180
        - 180
        - 180
    - scale:
      - 0.2
      - 0.2
      - 0.2

  table:
    type: geometry
    subtype: mesh
    physics: collision # rigidbodies will collide with it, but it doesn't move
    usd_path: PATH_TO_TABLE
    transform_operators:
    - rotateX: -90
```

Run the simulation by clicking on the **Simulate** button to generate RGB images like:

And segmentation masks like:

Note

Check whether the YAML text is formatted correctly in the description (for example, indentation). If you meet an error `mapping values are not allowed here` it can be due to a formatting problem.

## Scene Editing

For the convenience of scene planning, a basic scene editing widget is provided to toggle the visibility of prims.

In a scene created by the [embedded interface](#embedded-interface) using [this description file](ext_replicator-object/randomization_dependency.html#iro-basic-example), you can create a cube, change its translate and size (but not its rotation), and move it around to toggle visibility of prims that has its position included within the spatial range of the cube, as shown below:

Note

Before clicking on the **Toggle Visibility of selected region** button, make sure the cube is selected.

## Catalog

Conventions in the linked catalog files:

`Type` in the tables indicates the expected data types. Where a type is expected, a macro string can be used for later evaluation of that specific type. For example, if you expect int in a value, you can either give an int or something like `$[index]`. See [Macro](ext_replicator-object/macro.html#macro) for details.

Within a mutable, aside from these options, you can also specify a [Mutable Attribute](ext_replicator-object/mutable_attribute.html#mutable-attribute) to evaluate to this type.

`numeric` means literal or evaluated `float` or `int`.

* [Setting](ext_replicator-object/setting.html)
* [Mutable](ext_replicator-object/mutable.html)
* [Camera](ext_replicator-object/camera.html)
* [Geometry](ext_replicator-object/geometry.html)
* [Force](ext_replicator-object/force.html)
* [Light](ext_replicator-object/light.html)
* [Mutable Attribute](ext_replicator-object/mutable_attribute.html)
* [Transformation](ext_replicator-object/transformation.html)
* [Harmonizer](ext_replicator-object/harmonizer.html)
* [Empty Space Detection](ext_replicator-object/empty_space_detection.html)
* [Macro](ext_replicator-object/macro.html)
* [Distribution Visualizer](ext_replicator-object/distribution_visualizer.html)
* [Randomization Dependency: Incremental Examples](ext_replicator-object/randomization_dependency.html)

## 3rd-party Libraries Used

py3dbp (modified), MIT License
PyYaml, MIT License
trimesh, MIT License
regex, Apache License

On this page

* [Motivation](#motivation)
* [Chat IRO: Natural Language Interface for IRO](#chat-iro-natural-language-interface-for-iro)
* [End-to-end Pipeline](#end-to-end-pipeline)
* [Run from the UI](#run-from-the-ui)
* [Run from Docker](#run-from-docker)
* [Embedded Interface](#embedded-interface)
* [Expected Output](#expected-output)
* [Concepts](#concepts)
* [Main Simulation Workflow Walkthrough](#main-simulation-workflow-walkthrough)
* [Compose a Description File](#compose-a-description-file)
* [Scene Editing](#scene-editing)
* [Catalog](#catalog)
* [3rd-party Libraries Used](#rd-party-libraries-used)

---

