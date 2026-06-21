---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/py/source/extensions/isaacsim.replicator.experimental.domain_randomization/docs/index.html
title: "replicator.experimental.domain_randomization Docs"
section: "Replicator"
module: "05-python-api-quickref"
checksum: "95dd3770425661cf"
fetched: "2026-06-21T14:14:27"
---

* [isaacsim.replicator.experimental.domain\_randomization] Isaac Sim Replicator Domain Randomization

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# [isaacsim.replicator.experimental.domain\_randomization] Isaac Sim Replicator Domain Randomization

**Version**: 1.2.4

## Overview

The isaacsim.replicator.experimental.domain\_randomization extension provides domain randomization capabilities for reinforcement learning and simulation-to-real transfer applications in Isaac Sim. This extension offers specialized OmniGraph nodes that enable dynamic randomization of physics simulation parameters across multiple environments, supporting both individual environment resets and interval-based randomization patterns.

### Key Components

#### Physics View Integration

The extension integrates with Isaac Sim’s physics view system to enable efficient batch randomization operations. Users register RigidPrim and Articulation views by name, then reference these registered views in randomization functions.

The physics view integration supports three operation modes:

* **Direct**: Replace existing values with randomized samples
* **Additive**: Add randomized values to current properties
* **Scaling**: Multiply current values by randomized factors

#### Context Management

The ReplicatorIsaacContext class manages randomization state across multiple environments. It tracks reset indices, coordinates trigger events, and maintains execution context for complex randomization workflows involving tendon properties and multi-environment scenarios.

### Functionality

#### Trigger Gates

The extension provides gate functions that determine when randomization should occur. The `on_interval()` function creates interval-based triggers that activate randomization at specified frequencies. The `on_env_reset()` function triggers randomization whenever environments are reset, ensuring consistent initial conditions.

#### Distribution Support

All randomization functions accept ReplicatorItem distributions from the **omni.replicator.core** system. This enables sophisticated sampling strategies including uniform, normal, and custom distributions with configurable parameters.

#### Attribute Randomization

The extension supports randomization of numerous physics attributes organized into categories:

**Simulation Context**: Global parameters like gravity that affect the entire simulation environment.

**Rigid Body Properties**: Individual object characteristics including transforms, dynamics, and material properties.

**Articulation Properties**: Joint-specific parameters, body properties, and tendon configurations for complex mechanisms.

### Relationships

This extension builds upon **omni.replicator.core** for distribution sampling and **omni.graph.core** for OmniGraph node infrastructure. It integrates with isaacsim.core.experimental.prims for physics view management and isaacsim.core.simulation\_manager for simulation context control. The extension coordinates with these systems to provide domain randomization capabilities that work seamlessly within Isaac Sim’s physics simulation pipeline.

## Enable Extension

The extension can be enabled (if not already) in one of the following ways:

Command-line interface

Define the next entry as an application argument from a terminal.

```python
APP_SCRIPT.(sh|bat) --enable isaacsim.replicator.experimental.domain_randomization
```

Experience/extension configuration

Define the next entry under `[dependencies]` in an experience (`.kit`) file or an extension configuration (`extension.toml`) file.

```python
[dependencies]
"isaacsim.replicator.experimental.domain_randomization" = {}
```

Extension Manager UI

Open the *Window > Extensions* menu in a running application instance and search for `isaacsim.replicator.experimental.domain_randomization`.
Then, toggle the enable control button if it is not already active.

## Omnigraph Nodes

The extension exposes the following Omnigraph nodes:

* [Count](ogn/OgnCountIndices.html)
* [Interval Filter](ogn/OgnIntervalFiltering.html)
* [On Frame](ogn/OgnOnRLFrame.html)
* [Random 3f](ogn/OgnRandom3f.html)
* [Write Physics Attribute using Tensor API](ogn/OgnWritePhysicsArticulationView.html)
* [Write Physics Attribute using Tensor API](ogn/OgnWritePhysicsRigidPrimView.html)
* [Write Physics Attribute using Tensor API](ogn/OgnWritePhysicsSimulationContext.html)

On this page

* [Overview](#overview)
  + [Key Components](#key-components)
    - [Physics View Integration](#physics-view-integration)
    - [Context Management](#context-management)
  + [Functionality](#functionality)
    - [Trigger Gates](#trigger-gates)
    - [Distribution Support](#distribution-support)
    - [Attribute Randomization](#attribute-randomization)
  + [Relationships](#relationships)
* [Enable Extension](#enable-extension)
* [Omnigraph Nodes](#omnigraph-nodes)