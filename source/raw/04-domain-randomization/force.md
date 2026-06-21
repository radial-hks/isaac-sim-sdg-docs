---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/action_and_event_data_generation/ext_replicator-object/force.html
title: "Force"
section: "Replicator Object"
module: "04-domain-randomization"
checksum: "ec8db37c939c34ef"
fetched: "2026-06-21T11:55:29"
---

* [Synthetic Data Generation](../../synthetic_data_generation/index.html)
* [Action and Event Data Generation](../index.html)
* [Object Simulation and Synthetic Data Generation](../tutorial_replicator_object.html)
* Force

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Force

If a mutable has attribute `type` of `force`, itâs a force mutable that applies PhysX forces to rigid bodies. Forces can be used to create dynamic simulations with objects being pushed, pulled, or animated through physics.

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