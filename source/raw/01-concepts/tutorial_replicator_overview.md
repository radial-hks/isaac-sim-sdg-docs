---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/replicator_tutorials/tutorial_replicator_overview.html
title: "Replicator Overview"
section: "SDG概念"
module: "01-concepts"
checksum: "1a64f6b67404b9f1"
fetched: "2026-06-21T13:39:51"
---

* [Synthetic Data Generation](../synthetic_data_generation/index.html)
* [Perception Data Generation (Replicator)](index.html)
* Overview

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Overview

Isaac Sim Replicator offers various tools and workflows for synthetic data generation (SDG), with its core functionalities mostly provided by, but not limited to, the [omni.replicator](https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator.html "(in Omniverse Extensions)") extension. This page provides an overview of these tools and extensions, including semantic labeling, sensor visualization, GUI-based data recording, config file-based SDG workflows, and getting started scripts (examples). To enable SDG relevant UI panels you can use the [Synthetic Data Generation Layout](../gui/layouts.html#isaac-sim-app-gui-layouts).

## The Semantics Schema Editor

The [Semantics Schema Editor](https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator/semantics_schema_editor.html "(in Omniverse Extensions)") is a GUI-based extension that enables you to view, add, edit, or remove semantic labels on prims in a stage. Semantically labeling prims is necessary for annotators like semantic segmentation or bounding boxes to include semantic information in the synthetic data. You can access the editor through **Tools > Replicator > Semantics Schema Editor**. To programmatically label prims in a stage, see the following [example snippet](../python_scripting/environment_setup.html#apply-semantic-data-on-entire-stage).

## The Synthetic Data Visualizer

The [Synthetic Data Visualizer](https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator/visualization.html "(in Omniverse Extensions)") tool enables sensor output visualization directly in the Viewport window, it can be accessed using the  icon and selecting the desired output formats.

Note

* Cross Correspondence visualization requires a specific two-camera setup explained in the Cross Correspondence section of the [annotator details](https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator/annotators_details.html "(in Omniverse Extensions)") page.

## The Synthetic Data Recorder

The [Synthetic Data Recorder](tutorial_replicator_recorder.html#isaac-sim-app-tutorial-replicator-recorder) is a GUI-based tool that allows you to record synthetic data directly from the editor. It is built on top of `omni.replicator` using `BasicWriter` as its default writer, it is useful for rapid iterations of synthetic data recordings for testing purposes. You can access the recorder via **Tools > Replicator > Synthetic Data Recorder**.

## Replicator YAML

[Replicator YAML](https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator/yaml_workflow.html "(in Omniverse Extensions)") is a configuration file-based workflow built on top of the Replicator API. It allows you to define randomizations and data capture pipelines as configuration files. These configurations are transformed through the Replicator API into an [OmniGraph](https://docs.omniverse.nvidia.com/extensions/latest/ext_omnigraph.html "(in Omniverse Extensions)") workflow for synthetic data generation. You can access the YAML workflow using **Tools > Replicator > Replicator YAML**.

## Getting Started Scripts

The [Getting Started Scripts](tutorial_replicator_getting_started.html#isaac-sim-app-tutorial-replicator-getting-started) provides a starting point for typical Isaac Sim Replicator workflows. These tutorials cover basic topics such as accessing data from [annotators](https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator/annotators_details.html "(in Omniverse Extensions)") or [writers](https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator/writer_examples.html "(in Omniverse Extensions)"), and using Replicator randomizers together with custom USD/Isaac Sim API randomizers triggered independently from the data capture.

On this page

* [The Semantics Schema Editor](#the-semantics-schema-editor)
* [The Synthetic Data Visualizer](#the-synthetic-data-visualizer)
* [The Synthetic Data Recorder](#the-synthetic-data-recorder)
* [Replicator YAML](#replicator-yaml)
* [Getting Started Scripts](#getting-started-scripts)