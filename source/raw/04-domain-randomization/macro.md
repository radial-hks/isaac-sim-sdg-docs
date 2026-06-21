---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/action_and_event_data_generation/ext_replicator-object/macro.html
title: "Macro"
section: "Replicator Object"
module: "04-domain-randomization"
checksum: "bc9a102208a5c4d5"
fetched: "2026-06-21T11:55:29"
---

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

`$[seed]` resolves to the current frameâs seed number, and `$[frame]` resolves to the frame index.

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