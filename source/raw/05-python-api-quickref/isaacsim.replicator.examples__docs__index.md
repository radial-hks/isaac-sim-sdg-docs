---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/py/source/extensions/isaacsim.replicator.examples/docs/index.html
title: "replicator.examples Docs"
section: "Replicator"
module: "05-python-api-quickref"
checksum: "104a6a5ef60a9def"
fetched: "2026-06-21T14:14:27"
---

* [isaacsim.replicator.examples] Isaac Sim Replicator Examples

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# [isaacsim.replicator.examples] Isaac Sim Replicator Examples

**Version**: 1.11.4

## Overview

The isaacsim.replicator.examples extension provides example implementations and demonstrations of Replicator functionality within Isaac Sim for synthetic data generation workflows in robotics simulation and machine learning.

### Functionality

The extension demonstrates key Replicator concepts through practical spatial sampling operations commonly used in robotics and machine learning data generation:

* **Spatial Randomization**: Shows how to implement different spatial distribution patterns for objects in 3D scenes
* **Graph-Based Workflows**: Demonstrates integration with OmniGraph for building complex data generation pipelines
* **Execution Flow Control**: Provides examples of managing execution order in graph-based synthetic data workflows

### Integration

The extension integrates with Isaac Sim’s synthetic data generation ecosystem through its dependencies on **omni.replicator.core** and isaacsim.replicator.writers. The OmniGraph nodes can be combined with other Replicator components to create sophisticated randomization workflows for training data generation in robotics applications.

## Enable Extension

The extension can be enabled (if not already) in one of the following ways:

Command-line interface

Define the next entry as an application argument from a terminal.

```python
APP_SCRIPT.(sh|bat) --enable isaacsim.replicator.examples
```

Experience/extension configuration

Define the next entry under `[dependencies]` in an experience (`.kit`) file or an extension configuration (`extension.toml`) file.

```python
[dependencies]
"isaacsim.replicator.examples" = {}
```

Extension Manager UI

Open the *Window > Extensions* menu in a running application instance and search for `isaacsim.replicator.examples`.
Then, toggle the enable control button if it is not already active.

## Omnigraph Nodes

The extension exposes the following Omnigraph nodes:

* [Sample Between Spheres](ogn/OgnSampleBetweenSpheres.html)
* [Sample In Sphere](ogn/OgnSampleInSphere.html)
* [Sample On Sphere](ogn/OgnSampleOnSphere.html)

On this page

* [Overview](#overview)
  + [Functionality](#functionality)
  + [Integration](#integration)
* [Enable Extension](#enable-extension)
* [Omnigraph Nodes](#omnigraph-nodes)