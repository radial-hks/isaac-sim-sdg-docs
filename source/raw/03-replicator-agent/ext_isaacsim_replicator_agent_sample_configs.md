---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/action_and_event_data_generation/ext_replicator-agent/ext_isaacsim_replicator_agent_sample_configs.html
title: "Sample Configs"
section: "Agent配置"
module: "03-replicator-agent"
checksum: "c08754f5c61acb81"
fetched: "2026-06-21T13:40:23"
---

* [Synthetic Data Generation](../../synthetic_data_generation/index.html)
* [Action and Event Data Generation](../index.html)
* [Actor Simulation and Synthetic Data Generation](../tutorial_replicator_agent.html)
* Sample Configs

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Sample Configs

The `isaacsim.replicator.agent.core` extension ships with a small set of YAML
configurations under `[ext-path]/data/sample_configs/`. They demonstrate the
recommended ways to configure the Isaac replicator agent (IRA), from the smallest valid config to a full
data-generation pipeline.

## Layout

The directory is organized as follows:

```python
sample_configs/
  minimal.yaml         # smallest valid config (env only)
  full_pipeline.yaml   # end-to-end demo: routines + sensors + writers
  behavior_tree/       # behavior-tree samples (experimental)
    wander.yaml
    patrol_and_wander.yaml
    instance_overrides.yaml
```

Behavior-tree samples live under `behavior_tree/` because behavior-tree character
support is currently experimental (refer to [Behavior Tree Character
Group (Experimental)](ext_isaacsim_replicator_agent_configuration.html#ira-bt-character-group)). The two top-level samples
use the stable routine-trigger character API and are the recommended
starting point.

## Standard Samples

Top-level samples. They use the stable routine-trigger character API
(refer to [Configuration File](ext_isaacsim_replicator_agent_configuration.html#ira-configuration-file)).

| File | Expected behavior | Demonstrates |
| --- | --- | --- |
| `minimal.yaml` | Opens the warehouse stage. No actors, sensors, or data generation – a sanity check that IRA is enabled and the asset server is reachable. | Smallest valid IRA config. Loaded by the IRA UI on launch. |
| `full_pipeline.yaml` | 10 workers wander the warehouse for 60 seconds while six randomly placed ceiling cameras capture per-frame RGB, depth, segmentation, bounding boxes, and cosmos video annotations to the output folder. | End-to-end pipeline: routine-based character behavior, RTX sensor placement (`aim_at_targets`), and `IRABasicWriter`. |

## Behavior-Tree Samples (Experimental)

Samples under `sample_configs/behavior_tree/` that drive characters with
behavior trees instead of routines. The trees themselves live in the sibling
`sample_behavior_tree/` folder of the extension.

| File | Expected behavior | Demonstrates | Behavior Tree asset |
| --- | --- | --- | --- |
| `behavior_tree/wander.yaml` | Two warehouse workers wander randomly through the warehouse. | Single behavior-tree character group. | `sample_behavior_tree/wander.json` |
| `behavior_tree/patrol_and_wander.yaml` | Two agents follow a fixed patrol route while three others wander around them. | Two BT character groups (patrol + wander) coexisting in one config. | `sample_behavior_tree/patrol.json` + `wander.json` |
| `behavior_tree/instance_overrides.yaml` | Two warehouse workers each pick up a different cardboard box and carry it to a destination marker (`Destination_A`, `Destination_B`). | Per-group `overrides` on a shared Behavior Tree. Each group binds `SetBlackboard.slot`, `PickupObject.target`, and `PlaceObject.xform` to its own values using `instanceOverrides`. | `sample_behavior_tree/box_mover_multiple.json` |

On this page

* [Layout](#layout)
* [Standard Samples](#standard-samples)
* [Behavior-Tree Samples (Experimental)](#behavior-tree-samples-experimental)