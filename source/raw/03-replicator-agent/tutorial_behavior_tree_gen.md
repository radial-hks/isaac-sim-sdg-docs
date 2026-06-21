---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/action_and_event_data_generation/tutorial_behavior_tree_gen.html
title: "BT Gen Tutorial"
section: "BehaviorTree"
module: "03-replicator-agent"
checksum: "6ad73fe90b07d4d3"
fetched: "2026-06-21T13:40:23"
---

* [Synthetic Data Generation](../synthetic_data_generation/index.html)
* [Action and Event Data Generation](index.html)
* Behavior Tree Generation

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Behavior Tree Generation

The behavior tree generation workflow is packaged under the `omni.ai.behavior_tree_gen` namespace.
`omni.ai.behavior_tree_gen.bridge` provides the Kit UI, and
`omni.ai.behavior_tree_gen.core` provides the reusable scripted API that turns natural-language
scenarios into behavior tree outputs.

Before using this workflow, read [What Is Isaac Sim?](../index.html#isaac-sim-app-overview) to learn about
Isaac Sim and follow [Installation](../installation/index.html) to install Isaac Sim.

## Enable Extensions

1. Follow the [Omniverse Extension Manager guide](https://docs.omniverse.nvidia.com/extensions/latest/ext_core/ext_extension-manager.html)
   to enable `omni.ai.behavior_tree_gen.bridge`. The bridge loads
   `omni.ai.behavior_tree_gen.core` as a dependency.
2. Open **Behavior Tree Gen** from **Tools > Behavior Tree Gen**.
3. Optional: open the examples window from **Window > Examples > Behavior Tree Gen Examples** to
   load the bundled `simple` or `warehouse` scenes and prefill the main workflow window.

Note

The workflow expects scene context files, node catalogs, model configuration files, a writable
output directory, and a valid NVIDIA API key before a generation run can succeed.

## What the Bridge Does

`omni.ai.behavior_tree_gen.bridge` integrates the core pipeline with the Kit user experience.

* The **Behavior Tree Gen** window lets you review input files, set output and runtime options,
  enter a natural-language scenario, and run the pipeline.

* The examples window helps you load bundled demo stages, such as `simple` and `warehouse`.

* The bridge connects scene and cache data to the runtime so actor and object context, node
  catalogs, blackboard data, and model configuration files are available to the pipeline.
* The bridge tracks file snapshots so unchanged runs can reuse the loaded workspace and prepared
  runtime instead of rebuilding everything from scratch.

## Supported Workflows

Behavior tree generation supports both of the following workflows:

* **Interactive testing and demos** inside Kit, where you want a UI-driven workflow.
* **Scripted usage**, where the same flow is called directly from Python APIs.

## Workflow Overview

A typical UI session starts from the examples window or from manually selected input files. The
examples flow is the fastest way to begin because it loads a sample stage and pre-fills the
workflow panels, while manual usage lets you point the pipeline at your own context, catalog,
schema, and model configuration files.

After the inputs are available, use the **Behavior Tree Gen** window to review the loaded files,
choose the output location, provide a valid NVIDIA API key, and enter the natural-language scenario
that should be converted into behavior tree output.

For the full step-by-step UI flow, expected outputs, and example scenario, review
[Example Walkthrough](ext_behavior_tree_gen/example_walkthrough.html).

## Core API

`omni.ai.behavior_tree_gen.core` provides the reusable pipeline used by both the UI and Python
callers. Its public API intentionally exposes `setup_workspace(...)`,
`prepare_runtime(...)`, and `generate_behavior_tree(...)` for the same workflow used by the
bridge UI.

For a tutorial on authoring context files and metadata schemas, refer to
[Context Files and Metadata Schemas](ext_behavior_tree_gen/context_files_and_schemas.html).
For the full API sequence and script example, refer to
[Using the API Functions](ext_behavior_tree_gen/three_api_functions.html).

## Detailed Guides

For more detailed guidance on the workflow, schema-based context authoring, required inputs,
example usage, and API sequence, refer to the following pages:

* [Context Files and Metadata Schemas](ext_behavior_tree_gen/context_files_and_schemas.html)
* [Required inputs](ext_behavior_tree_gen/required_inputs.html)
* [Example Walkthrough](ext_behavior_tree_gen/example_walkthrough.html)
* [Using the API Functions](ext_behavior_tree_gen/three_api_functions.html)

## Terminology

omni.ai.behavior\_tree\_gen.bridge

The bridge extension provides the Kit and Omniverse user experience for behavior tree
generation. It exposes the UI windows, example loaders, and pipeline execution entry points
used by interactive workflows.

omni.ai.behavior\_tree\_gen.core

The core extension provides the reusable pipeline and public API used to prepare runtime state
and generate behavior tree output from natural-language scenarios.

PlannerSession

`PlannerSession` is the reusable workspace state returned by `setup_workspace(...)`. The
same session can be reused across runs when the tracked workflow inputs do not change.

On this page

* [Enable Extensions](#enable-extensions)
* [What the Bridge Does](#what-the-bridge-does)
* [Supported Workflows](#supported-workflows)
* [Workflow Overview](#workflow-overview)
* [Core API](#core-api)
* [Detailed Guides](#detailed-guides)
* [Terminology](#terminology)