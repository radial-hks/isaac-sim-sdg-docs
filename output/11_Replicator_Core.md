# Replicator Core

> Replicator 引擎核心概念、入门教程、模块化脚本
> Isaac Sim 版本: 6.0
> 最后组装: 2026-06-21 14:14 UTC
> 来源页数: 10

---

## 来源链接

- [Index](https://docs.isaacsim.omniverse.nvidia.com/latest/replicator_tutorials/index.html)
- [Replicator Overview](https://docs.isaacsim.omniverse.nvidia.com/latest/replicator_tutorials/tutorial_replicator_overview.html)
- [Getting Started](https://docs.isaacsim.omniverse.nvidia.com/latest/replicator_tutorials/tutorial_replicator_getting_started.html)
- [Modular Scripting](https://docs.isaacsim.omniverse.nvidia.com/latest/replicator_tutorials/tutorial_replicator_modular_scripting.html)
- [Isaac Snippets](https://docs.isaacsim.omniverse.nvidia.com/latest/replicator_tutorials/tutorial_replicator_isaac_snippets.html)
- [Isaac Randomizers](https://docs.isaacsim.omniverse.nvidia.com/latest/replicator_tutorials/tutorial_replicator_isaac_randomizers.html)
- [Custom OG Randomizer](https://docs.isaacsim.omniverse.nvidia.com/latest/replicator_tutorials/tutorial_replicator_custom_og_randomizer.html)
- [Recorder](https://docs.isaacsim.omniverse.nvidia.com/latest/replicator_tutorials/tutorial_replicator_recorder.html)
- [Augmentation](https://docs.isaacsim.omniverse.nvidia.com/latest/replicator_tutorials/tutorial_replicator_augmentation.html)
- [Troubleshooting](https://docs.isaacsim.omniverse.nvidia.com/latest/replicator_tutorials/troubleshooting.html)

---


## 教程

### Index

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/replicator_tutorials/index.html

* [Synthetic Data Generation](../synthetic_data_generation/index.html)
* Perception Data Generation (Replicator)

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Perception Data Generation (Replicator)

Isaac Sim Replicator offers various tools and workflows for synthetic data generation (SDG), primarily using the [omni.replicator](https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator.html "(in Omniverse Extensions)") extension. The examples and tutorials in this section showcase practical applications for robotics, including domain randomization, sensor simulation, and data collection with [annotators](https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator/annotators_details.html "(in Omniverse Extensions)") and [writers](https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator/writer_examples.html "(in Omniverse Extensions)").

## Basics and Getting Started

* [Overview](tutorial_replicator_overview.html)
* [Synthetic Data Recorder](tutorial_replicator_recorder.html)
* [Getting Started Scripts](tutorial_replicator_getting_started.html)

## Tutorials

* [SDG Workflows](tutorial_replicator_sdg_workflows.html)
* [Scene Based Synthetic Dataset Generation](tutorial_replicator_scene_based_sdg.html)
* [Object Based Synthetic Dataset Generation](tutorial_replicator_object_based_sdg.html)
* [Environment Based Synthetic Dataset Generation with Infinigen](tutorial_replicator_infinigen_sdg.html)
* [Randomization in Simulation – AMR Navigation](tutorial_replicator_amr_navigation.html)
* [Randomization in Simulation – UR10 Palletizing](tutorial_replicator_ur10_palletizing.html)
* [Cosmos Synthetic Data Generation](tutorial_replicator_cosmos.html)

## Customization Tools and Techniques

* [Data Augmentation](tutorial_replicator_augmentation.html)
* [Custom Replicator Randomization Nodes](tutorial_replicator_custom_og_randomizer.html)
* [Modular Behavior Scripting](tutorial_replicator_modular_scripting.html)
* [Randomization Snippets](tutorial_replicator_isaac_randomizers.html)
* [Useful Snippets](tutorial_replicator_isaac_snippets.html)

## Troubleshooting

* [Replicator Troubleshooting](troubleshooting.html)

On this page

* [Basics and Getting Started](#basics-and-getting-started)
* [Tutorials](#tutorials)
* [Customization Tools and Techniques](#customization-tools-and-techniques)
* [Troubleshooting](#troubleshooting)

---

### Replicator Overview

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/replicator_tutorials/tutorial_replicator_overview.html

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

---

### Getting Started

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/replicator_tutorials/tutorial_replicator_getting_started.html

* [Synthetic Data Generation](../synthetic_data_generation/index.html)
* [Perception Data Generation (Replicator)](index.html)
* Getting Started Scripts

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Getting Started Scripts

This guide outlines a series of example scripts designed to facilitate typical Isaac Sim Replicator workflows. The examples include both “asynchronous” usage through the [Script Editor](../development_tools/omniverse_script_editor.html#script-editor) and “synchronous” usage through the [Standalone Application](../introduction/workflows.html#standalone-application). These scripts cover simulation-based scenarios and configurations for synthetic data generation (SDG).

## Prerequisites

Before starting with these examples, ensure you have:

* Basic understanding of Python programming
* Familiarity with USD (Universal Scene Description) concepts
* Access to NVIDIA Omniverse™ Isaac Sim
* Sufficient disk space for data capture (varies based on resolution and number of frames)
* GPU with sufficient memory for rendering (recommended: 8GB+)

## Setup and Configuration

This section introduces configurations typically used in such workflows.

## Orchestrator Step Function

In Replicator, the `orchestrator.step()` function is used to trigger the entire synthetic data generation (SDG) process, including executing randomizations and capturing data. For Isaac Sim workflows, this function is used solely to trigger data capture only, with randomization triggers assigned to custom events and manually activated.

The `step()` function has the following signature:

```python
rep.orchestrator.step(rt_subframes: int = -1, pause_timeline: bool = True, delta_time: float = None, wait_for_render: bool = True)
```

Where:

* `rt_subframes`: Specifies the number of subframes to render. A value greater than 0 enables subframe generation, reducing rendering artifacts or allowing materials to load fully.
* `pause_timeline`: Pauses the timeline (if currently playing) after the step if set to `True`.
* `delta_time`: Specifies the time to advance the timeline during a step. Defaults to the timeline’s rate if `None`.
* `wait_for_render`: If `True`, the function blocks until the renderer completes the current frame before returning. Defaults to `True`.

More details on graph-based replicator randomizers can be found in the [Randomizer Details](https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator/randomizer_details.html "(in Omniverse Extensions)"), and for custom Isaac Sim or USD API-based randomizations, refer to the [Isaac Sim Randomizers Guide](tutorial_replicator_isaac_randomizers.html#isaac-sim-app-tutorial-replicator-isaac-randomizers).

## Capture on Play Flag

By default, Replicator captures data every frame during playback. For Isaac Sim workflows, data capture is configured to occur at user-defined frames using the `step()` function. To achieve this, the capture-on-play flag is disabled:

```python
import omni.replicator.core as rep

rep.orchestrator.set_capture_on_play(False)
# OR
import carb.settings

carb.settings.get_settings().set("/omni/replicator/captureOnPlay", False)
```

## RT Subframes Parameter

In scenarios where reducing temporal rendering artifacts is needed, such as ghosting caused by quickly moving or teleporting assets, or under weak lighting conditions, RTSubframes can be used to render the same frame multiple times. This pauses the simulation and renders additional subframes, improving rendering quality.

The `rt_subframes` parameter is typically set during the capture request in the `step()` function but can also be configured globally:

```python
# Set the rt_subframes parameter for a specific capture step
rep.orchestrator.step(rt_subframes=4)

# Set the rt_subframes parameter globally
import carb.settings

carb.settings.get_settings().set("/omni/replicator/RTSubframes", 4)
```

Refer to the [documentation examples](https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator/subframes_examples.html#subframes-examples "(in Omniverse Extensions)") for additional details.

## DLSS Quality Mode for SDG

When using Replicator for synthetic data generation (SDG) workflows, it is recommended to set the DLSS model to Quality mode to avoid rendering artifacts. At lower resolutions (especially below 600x600), the default Performance mode may cause issues such as transparent or incorrectly rendered edges in the generated images.

```python
import carb.settings

# Set DLSS to Quality mode (2) for best SDG results (Options: 0 (Performance), 1 (Balanced), 2 (Quality), 3 (Auto))
carb.settings.get_settings().set("/rtx/post/dlss/execMode", 2)
```

## Wait for Render Parameter

By default, the `step()` function blocks until the renderer finishes producing the current frame before returning. Setting `wait_for_render=False` decouples the capture request from the rendering pipeline, allowing the next randomization to begin immediately while the previous frame is still being rendered. This can significantly improve throughput in workflows where the captured data does not need to exactly match the current simulation state at the time the `step()` call returns.

```python
# Default behavior: blocks until the frame is rendered
rep.orchestrator.step(wait_for_render=True)

# Non-blocking: returns immediately, allowing the next randomization to start
rep.orchestrator.step(wait_for_render=False)
```

Note

When using `wait_for_render=False`, the annotation and writer data may correspond to a previous frame rather than the frame triggered by the most recent `step()` call. Use this mode only when strict frame-to-data correspondence is not required.

## Write to Fabric Mode

Fabric is the runtime data layer that the renderer reads from directly. By default, Replicator writes attribute changes (such as positions, rotations, and colors) to the USD stage, which are then synchronized to Fabric before rendering. Enabling write-to-fabric mode bypasses the USD stage and writes changes directly to Fabric, reducing the overhead of USD-to-Fabric synchronization and improving randomization performance.

```python
import carb.settings

# Enable write-to-fabric mode
carb.settings.get_settings().set("/exts/omni.replicator.core/enableWriteToFabric", True)
```

Note

Because changes are written directly to Fabric and bypass the USD stage, they will not be reflected in the USD stage or persisted when saving the scene. This mode is intended for transient randomizations during data generation, not for permanent scene modifications.

## Custom Event Randomizations

To provide flexibility, replicator randomizers can be triggered independently using custom events. This is achieved by registering the randomizer trigger through `trigger.on_custom_event` and activating it with `utils.send_og_event`. For instance, the following example creates a randomization graph for a dome light and randomizes its color. The randomization graph is then triggered manually through its custom event name. The `step()` function does not trigger this randomization graph.

```python
# Create a randomization graph for creating a dome light and randomizing its color
with rep.trigger.on_custom_event(event_name="randomize_dome_light_color"):
    rep.create.light(light_type="Dome", color=rep.distribution.uniform((0, 0, 0), (1, 1, 1)))

# Trigger the randomization graph using its custom event name
rep.utils.send_og_event(event_name="randomize_dome_light_color")
```

An example snippet for custom events is also available [here](tutorial_replicator_isaac_snippets.html#replicator-isaac-snippets-custom-event).

## Wait Until Complete

Ensuring that all data is fully written to disk before closing the application is essential to prevent data loss. High data throughput, such as from multiple cameras or large resolutions, may introduce I/O bottlenecks; refer to the [I/O Optimization Guide](https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator/io_guidelines.html "(in Omniverse Extensions)") for strategies to mitigate such issues.

The `wait_until_complete` function ensures that all writing tasks are finalized by waiting for the writer backend to complete its operations. This process allows the application to continue updating until all writing tasks are complete, safeguarding against potential data loss.

```python
from omni.replicator.core import BackendDispatch
import omni.kit.app

async def wait_until_complete():
    while not BackendDispatch.is_done_writing():
        await omni.kit.app.get_app().next_update_async()
```

Alternatively, use the documented helper functions: `rep.orchestrator.wait_until_complete()` for synchronous contexts or `await rep.orchestrator.wait_until_complete_async()` for asynchronous contexts.

## Examples

### Data Capture: BasicWriter

This example demonstrates how to use the `BasicWriter` for data capture with RGB and bounding box annotators. It sets up a scene with a cube and a dome light, attaches semantic labels to the cube, and saves captured data to disk. The standalone example can also be run directly (on Windows use `python.bat` instead of `python.sh`):

```python
./python.sh standalone_examples/api/isaacsim.replicator.examples/sdg_getting_started_01.py
```

Script Editor

```python
import asyncio
import os

import carb.settings
import omni.replicator.core as rep
import omni.usd

async def run_example_async():
    # Create a new stage and disable capture on play
    omni.usd.get_context().new_stage()
    rep.orchestrator.set_capture_on_play(False)

    # Set DLSS to Quality mode (2) for best SDG results (Options: 0 (Performance), 1 (Balanced), 2 (Quality), 3 (Auto)
    carb.settings.get_settings().set("rtx/post/dlss/execMode", 2)

    # Setup the stage with a dome light and a cube
    rep.functional.create.xform(name="World")
    rep.functional.create.dome_light(intensity=500, parent="/World", name="DomeLight")
    cube = rep.functional.create.cube(parent="/World", name="Cube")
    rep.functional.modify.semantics(cube, {"class": "my_cube"}, mode="add")

    # Create a render product using the viewport perspective camera
    cam = rep.functional.create.camera(position=(5, 5, 5), look_at=(0, 0, 0), parent="/World", name="Camera")
    rp = rep.create.render_product(cam, (512, 512), name="MyRenderProduct")

    # Write data using the basic writer with the rgb and bounding box annotators
    backend = rep.backends.get("DiskBackend")
    out_dir = os.path.join(os.getcwd(), "_out_basic_writer")
    backend.initialize(output_dir=out_dir)
    print(f"Output directory: {out_dir}")
    writer = rep.writers.get("BasicWriter")
    writer.initialize(backend=backend, rgb=True, bounding_box_2d_tight=True)
    writer.attach(rp)

    # Trigger a data capture request (data will be written to disk by the writer)
    for i in range(3):
        print(f"Step {i}")
        await rep.orchestrator.step_async()

    # Wait for the data to be written to disk and clean up resources
    await rep.orchestrator.wait_until_complete_async()
    writer.detach()
    rp.destroy()

# Run the example
asyncio.ensure_future(run_example_async())
```

Standalone Application

```python
"""Demonstrate basic synthetic data generation with a writer and render product."""

import os

from isaacsim import SimulationApp

simulation_app = SimulationApp(launch_config={"headless": False})

import carb.settings
import omni.replicator.core as rep
import omni.usd

def run_example():
    """Run a basic SDG pipeline capturing RGB and bounding box data."""
    # Create a new stage and disable capture on play
    omni.usd.get_context().new_stage()
    rep.orchestrator.set_capture_on_play(False)

    # Set DLSS to Quality mode (2) for best SDG results , options: 0 (Performance), 1 (Balanced), 2 (Quality), 3 (Auto)
    carb.settings.get_settings().set("rtx/post/dlss/execMode", 2)

    # Setup the stage with a dome light and a cube
    rep.functional.create.xform(name="World")
    rep.functional.create.dome_light(intensity=500, parent="/World", name="DomeLight")
    cube = rep.functional.create.cube(parent="/World", name="Cube")
    rep.functional.modify.semantics(cube, {"class": "my_cube"}, mode="add")

    # Create a render product using the viewport perspective camera
    cam = rep.functional.create.camera(position=(5, 5, 5), look_at=(0, 0, 0), parent="/World", name="Camera")
    rp = rep.create.render_product(cam, (512, 512), name="MyRenderProduct")

    # Write data using the basic writer with the rgb and bounding box annotators
    backend = rep.backends.get("DiskBackend")
    out_dir = os.path.join(os.getcwd(), "_out_basic_writer")
    backend.initialize(output_dir=out_dir)
    print(f"Output directory: {out_dir}")
    writer = rep.writers.get("BasicWriter")
    writer.initialize(backend=backend, rgb=True, bounding_box_2d_tight=True)
    writer.attach(rp)

    # Trigger a data capture request (data will be written to disk by the writer)
    for i in range(3):
        print(f"Step {i}")
        rep.orchestrator.step()

    # Wait for the data to be written to disk and clean up resources
    rep.orchestrator.wait_until_complete()
    writer.detach()
    rp.destroy()

run_example()
```

The output directory will contain the captured data, including RGB images and bounding box annotations in `.npy` and `.json` formats:

### Custom Writer and Annotators with Multiple Cameras

This example demonstrates data capture by creating a custom writer to access annotator data such as camera parameters and 3D bounding boxes. It configures two cameras (custom and viewport perspective), uses annotators to access data directly, writes data to disk using `PoseWriter`. The standalone example can also be run directly (on Windows use `python.bat` instead of `python.sh`):

```python
./python.sh standalone_examples/api/isaacsim.replicator.examples/sdg_getting_started_02.py
```

Script Editor

```python
import asyncio
import os

import carb.settings
import omni.replicator.core as rep
import omni.usd
from omni.replicator.core import Writer

# Create a custom writer to access annotator data
class MyWriter(Writer):
    def __init__(self, camera_params: bool = True, bounding_box_3d: bool = True):
        # Organize data from render product perspective (legacy, annotator, renderProduct)
        self.data_structure = "renderProduct"
        self.annotators = []
        if camera_params:
            self.annotators.append(rep.annotators.get("camera_params"))
        if bounding_box_3d:
            self.annotators.append(rep.annotators.get("bounding_box_3d"))
        self._frame_id = 0

    def write(self, data: dict):
        print(f"[MyWriter][{self._frame_id}] data:")
        for key, value in data.items():
            print(f"  {key}: {value}")
        self._frame_id += 1

# Register the writer
rep.writers.register_writer(MyWriter)

async def run_example_async():
    # Create a new stage and disable capture on play
    omni.usd.get_context().new_stage()
    rep.orchestrator.set_capture_on_play(False)

    # Set DLSS to Quality mode (2) for best SDG results , options: 0 (Performance), 1 (Balanced), 2 (Quality), 3 (Auto)
    carb.settings.get_settings().set("rtx/post/dlss/execMode", 2)

    # Setup stage
    rep.functional.create.xform(name="World")
    rep.functional.create.dome_light(intensity=500, parent="/World", name="DomeLight")
    cube = rep.functional.create.cube(parent="/World", name="Cube")
    rep.functional.modify.semantics(cube, {"class": "my_cube"}, mode="add")

    # Capture from two perspectives, a custom camera and a perspective camera
    top_cam = rep.functional.create.camera(position=(0, 0, 5), look_at=(0, 0, 0), parent="/World", name="TopCamera")
    persp_cam = rep.functional.create.camera(position=(5, 5, 5), look_at=(0, 0, 0), parent="/World", name="PerspCamera")

    # Create the render products
    rp_top = rep.create.render_product(top_cam.GetPath(), (400, 400), name="top_view")
    rp_persp = rep.create.render_product(persp_cam.GetPath(), (512, 512), name="persp_view")

    # Use the annotators to access the data directly, each annotator is attached to a render product
    rgb_annotator_top = rep.annotators.get("rgb")
    rgb_annotator_top.attach(rp_top)
    rgb_annotator_persp = rep.annotators.get("rgb")
    rgb_annotator_persp.attach(rp_persp)

    # Use the custom writer to access the annotator data
    custom_writer = rep.writers.get("MyWriter")
    custom_writer.initialize(camera_params=True, bounding_box_3d=True)
    custom_writer.attach([rp_top, rp_persp])

    # Use the pose writer to write the data to disk
    pose_writer = rep.WriterRegistry.get("PoseWriter")
    out_dir = os.path.join(os.getcwd(), "_out_pose_writer")
    print(f"Output directory: {out_dir}")
    pose_writer.initialize(output_dir=out_dir, write_debug_images=True)
    pose_writer.attach([rp_top, rp_persp])

    # Trigger a data capture request (data will be written to disk by the writer)
    for i in range(3):
        print(f"Step {i}")
        await rep.orchestrator.step_async()

        # Get the data from the annotators
        rgb_data_cam = rgb_annotator_top.get_data()
        rgb_data_persp = rgb_annotator_persp.get_data()
        print(f"[Annotator][Cam][{i}] rgb_data_cam shape: {rgb_data_cam.shape}")
        print(f"[Annotator][Persp][{i}] rgb_data_persp shape: {rgb_data_persp.shape}")

    # Wait for the data to be written to disk and clean up resources
    await rep.orchestrator.wait_until_complete_async()
    pose_writer.detach()
    custom_writer.detach()
    rgb_annotator_top.detach()
    rgb_annotator_persp.detach()
    rp_top.destroy()
    rp_persp.destroy()

# Run the example
asyncio.ensure_future(run_example_async())
```

Standalone Application

```python
"""Demonstrate SDG with custom writers and multiple render products."""

import os

from isaacsim import SimulationApp

simulation_app = SimulationApp(launch_config={"headless": False})

import carb.settings
import omni.replicator.core as rep
import omni.usd
from omni.replicator.core import Writer

class MyWriter(Writer):
    """Access and print annotator data from attached render products."""

    def __init__(self, camera_params: bool = True, bounding_box_3d: bool = True):
        # Organize data from render product perspective (legacy, annotator, renderProduct)
        self.data_structure = "renderProduct"
        self.annotators = []
        if camera_params:
            self.annotators.append(rep.annotators.get("camera_params"))
        if bounding_box_3d:
            self.annotators.append(rep.annotators.get("bounding_box_3d"))
        self._frame_id = 0

    def write(self, data: dict):
        """Print captured annotator data for each frame."""
        print(f"[MyWriter][{self._frame_id}] data:")
        for key, value in data.items():
            print(f"  {key}: {value}")
        self._frame_id += 1

# Register the writer
rep.writers.register_writer(MyWriter)

def run_example():
    """Run SDG with custom writer, pose writer, and annotator data access."""
    # Create a new stage and disable capture on play
    omni.usd.get_context().new_stage()
    rep.orchestrator.set_capture_on_play(False)

    # Set DLSS to Quality mode (2) for best SDG results , options: 0 (Performance), 1 (Balanced), 2 (Quality), 3 (Auto)
    carb.settings.get_settings().set("rtx/post/dlss/execMode", 2)

    # Setup stage
    rep.functional.create.xform(name="World")
    rep.functional.create.dome_light(intensity=500, parent="/World", name="DomeLight")
    cube = rep.functional.create.cube(parent="/World", name="Cube")
    rep.functional.modify.semantics(cube, {"class": "my_cube"}, mode="add")

    # Capture from two perspectives, a custom camera and a perspective camera
    top_cam = rep.functional.create.camera(position=(0, 0, 5), look_at=(0, 0, 0), parent="/World", name="TopCamera")
    persp_cam = rep.functional.create.camera(position=(5, 5, 5), look_at=(0, 0, 0), parent="/World", name="PerspCamera")

    # Create the render products
    rp_top = rep.create.render_product(top_cam.GetPath(), (400, 400), name="top_view")
    rp_persp = rep.create.render_product(persp_cam.GetPath(), (512, 512), name="persp_view")

    # Use the annotators to access the data directly, each annotator is attached to a render product
    rgb_annotator_top = rep.annotators.get("rgb")
    rgb_annotator_top.attach(rp_top)
    rgb_annotator_persp = rep.annotators.get("rgb")
    rgb_annotator_persp.attach(rp_persp)

    # Use the custom writer to access the annotator data
    custom_writer = rep.writers.get("MyWriter")
    custom_writer.initialize(camera_params=True, bounding_box_3d=True)
    custom_writer.attach([rp_top, rp_persp])

    # Use the pose writer to write the data to disk
    pose_writer = rep.WriterRegistry.get("PoseWriter")
    out_dir = os.path.join(os.getcwd(), "_out_pose_writer")
    print(f"Output directory: {out_dir}")
    pose_writer.initialize(output_dir=out_dir, write_debug_images=True)
    pose_writer.attach([rp_top, rp_persp])

    # Trigger a data capture request (data will be written to disk by the writer)
    for i in range(3):
        print(f"Step {i}")
        rep.orchestrator.step()

        # Get the data from the annotators
        rgb_data_top = rgb_annotator_top.get_data()
        rgb_data_persp = rgb_annotator_persp.get_data()
        print(f"[Annotator][Top][{i}] rgb_data_top shape: {rgb_data_top.shape}")
        print(f"[Annotator][Persp][{i}] rgb_data_persp shape: {rgb_data_persp.shape}")

    # Wait for the data to be written to disk and clean up resources
    rep.orchestrator.wait_until_complete()
    pose_writer.detach()
    custom_writer.detach()
    rgb_annotator_top.detach()
    rgb_annotator_persp.detach()
    rp_top.destroy()
    rp_persp.destroy()

run_example()
```

The output directory will contain the captured data, including RGB with the 3D bounding box annotations as overlays together with `.json` files with the frame data. The annotator and custom writer data is printed to the terminal.

### Custom Randomizations: Replicator Graph and USD API

This example demonstrates creating a custom randomization using Replicator’s graph-based randomizers triggered by custom events and a custom USD API-based randomization. A dome light’s color is randomized through custom events, while a cube’s location is randomized through USD API. Data is captured using the `BasicWriter` with semantic segmentation. The standalone example can also be run directly (on Windows use `python.bat` instead of `python.sh`):

```python
./python.sh standalone_examples/api/isaacsim.replicator.examples/sdg_getting_started_03.py
```

Script Editor

```python
import asyncio
import os
import random

import carb.settings
import omni.replicator.core as rep
import omni.usd

# Randomize the location of a prim without the graph-based randomizer
def randomize_location(prim):
    random_pos = (random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-1, 1))
    rep.functional.modify.position(prim, random_pos)

async def run_example_async():
    # Create a new stage and disable capture on play
    omni.usd.get_context().new_stage()
    rep.orchestrator.set_capture_on_play(False)
    random.seed(42)
    rep.set_global_seed(42)

    # Set DLSS to Quality mode (2) for best SDG results , options: 0 (Performance), 1 (Balanced), 2 (Quality), 3 (Auto)
    carb.settings.get_settings().set("rtx/post/dlss/execMode", 2)

    # Setup stage
    rep.functional.create.xform(name="World")
    cube = rep.functional.create.cube(parent="/World", name="Cube")
    rep.functional.modify.semantics(cube, {"class": "my_cube"}, mode="add")

    # Create a replicator randomizer with custom event trigger
    with rep.trigger.on_custom_event(event_name="randomize_dome_light_color"):
        rep.create.light(light_type="Dome", color=rep.distribution.uniform((0, 0, 0), (1, 1, 1)))

    # Create a render product using the viewport perspective camera
    cam = rep.functional.create.camera(position=(5, 5, 5), look_at=(0, 0, 0), parent="/World", name="Camera")
    rp = rep.create.render_product(cam, (512, 512))

    # Write data using the basic writer with the rgb and bounding box annotators
    backend = rep.backends.get("DiskBackend")
    out_dir = os.path.join(os.getcwd(), "_out_basic_writer_rand")
    backend.initialize(output_dir=out_dir)
    print(f"Output directory: {out_dir}")
    writer = rep.writers.get("BasicWriter")
    writer.initialize(backend=backend, rgb=True, semantic_segmentation=True, colorize_semantic_segmentation=True)
    writer.attach(rp)

    # Trigger a data capture request (data will be written to disk by the writer)
    for i in range(3):
        print(f"Step {i}")
        # Trigger the custom graph-based event randomizer every second step
        if i % 2 == 1:
            rep.utils.send_og_event(event_name="randomize_dome_light_color")

        # Run the custom USD API location randomizer on the prims
        randomize_location(cube)

        # Since the replicator randomizer is set to trigger on custom events, step will only trigger the writer
        await rep.orchestrator.step_async(rt_subframes=32)

    # Wait for the data to be written to disk and clean up resources
    await rep.orchestrator.wait_until_complete_async()
    writer.detach()
    rp.destroy()

# Run the example
asyncio.ensure_future(run_example_async())
```

Standalone Application

```python
"""Demonstrate SDG with custom and graph-based randomizers."""

import os
import random

from isaacsim import SimulationApp

simulation_app = SimulationApp(launch_config={"headless": False})

import carb.settings
import omni.replicator.core as rep
import omni.usd

def randomize_location(prim):
    """Randomize the position of a prim using the USD functional API."""
    random_pos = (random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-1, 1))
    rep.functional.modify.position(prim, random_pos)

def run_example():
    """Run SDG with combined USD API and graph-based randomization."""
    # Create a new stage and disable capture on play
    omni.usd.get_context().new_stage()
    rep.orchestrator.set_capture_on_play(False)
    random.seed(42)
    rep.set_global_seed(42)

    # Set DLSS to Quality mode (2) for best SDG results , options: 0 (Performance), 1 (Balanced), 2 (Quality), 3 (Auto)
    carb.settings.get_settings().set("rtx/post/dlss/execMode", 2)

    # Setup stage
    rep.functional.create.xform(name="World")
    cube = rep.functional.create.cube(parent="/World", name="Cube")
    rep.functional.modify.semantics(cube, {"class": "my_cube"}, mode="add")

    # Create a replicator randomizer with custom event trigger
    with rep.trigger.on_custom_event(event_name="randomize_dome_light_color"):
        rep.create.light(light_type="Dome", color=rep.distribution.uniform((0, 0, 0), (1, 1, 1)))

    # Create a render product using the viewport perspective camera
    cam = rep.functional.create.camera(position=(5, 5, 5), look_at=(0, 0, 0), parent="/World", name="Camera")
    rp = rep.create.render_product(cam, (512, 512))

    # Write data using the basic writer with the rgb and bounding box annotators
    backend = rep.backends.get("DiskBackend")
    out_dir = os.path.join(os.getcwd(), "_out_basic_writer_rand")
    backend.initialize(output_dir=out_dir)
    print(f"Output directory: {out_dir}")
    writer = rep.writers.get("BasicWriter")
    writer.initialize(backend=backend, rgb=True, semantic_segmentation=True, colorize_semantic_segmentation=True)
    writer.attach(rp)

    # Trigger a data capture request (data will be written to disk by the writer)
    for i in range(3):
        print(f"Step {i}")
        # Trigger the custom graph-based event randomizer every second step
        if i % 2 == 1:
            rep.utils.send_og_event(event_name="randomize_dome_light_color")

        # Run the custom USD API location randomizer on the prims
        randomize_location(cube)

        # Since the replicator randomizer is set to trigger on custom events, step will only trigger the writer
        rep.orchestrator.step(rt_subframes=32)

    # Wait for the data to be written to disk and clean up resources
    rep.orchestrator.wait_until_complete()
    writer.detach()
    rp.destroy()

# Run the example
run_example()
```

The output directory will contain the RGB and semantic segmentation images with the captured data. The cube is randomized each capture, while the dome light color is randomized every second capture.

### Event-Triggered Data Capture: Timeline and Simulation

This example shows how to capture simulation data when specific conditions are met. A cube and sphere are dropped in a physics simulation, and data is captured at specific intervals based on the cube’s height. The timeline is paused during capture to ensure data consistency. The standalone example can also be run directly (on Windows use `python.bat` instead of `python.sh`):

```python
./python.sh standalone_examples/api/isaacsim.replicator.examples/sdg_getting_started_04.py
```

Script Editor

```python
import asyncio
import os

import carb.settings
import omni.kit.app
import omni.replicator.core as rep
import omni.timeline
import omni.usd
from isaacsim.core.experimental.prims import RigidPrim
from pxr import UsdGeom

async def run_example_async():
    # Create a new stage and disable capture on play
    omni.usd.get_context().new_stage()
    rep.orchestrator.set_capture_on_play(False)

    # Set DLSS to Quality mode (2) for best SDG results , options: 0 (Performance), 1 (Balanced), 2 (Quality), 3 (Auto)
    carb.settings.get_settings().set("rtx/post/dlss/execMode", 2)

    # Add a light
    rep.functional.create.xform(name="World")
    rep.functional.create.dome_light(intensity=500, parent="/World", name="DomeLight")

    # Create a cube with colliders and rigid body dynamics at a specific location
    cube = rep.functional.create.cube(name="Cube", parent="/World")
    rep.functional.modify.position(cube, (0, 0, 2))
    rep.functional.modify.semantics(cube, {"class": "my_cube"}, mode="add")
    rep.functional.physics.apply_rigid_body(cube, with_collider=True)

    # Createa a sphere with colliders and rigid body dynamics next to the cube
    sphere = rep.functional.create.sphere(name="Sphere", parent="/World")
    rep.functional.modify.position(sphere, (-1, -1, 2))
    rep.functional.modify.semantics(sphere, {"class": "my_sphere"}, mode="add")
    rep.functional.physics.apply_rigid_body(sphere, with_collider=True)

    # Create a render product using the viewport perspective camera
    cam = rep.functional.create.camera(position=(5, 5, 5), look_at=(0, 0, 0), parent="/World", name="Camera")
    rp = rep.create.render_product(cam, (512, 512))

    # Write data using the basic writer with the rgb and bounding box annotators
    backend = rep.backends.get("DiskBackend")
    out_dir = os.path.join(os.getcwd(), "_out_basic_writer_sim")
    backend.initialize(output_dir=out_dir)
    print(f"Output directory: {out_dir}")
    writer = rep.writers.get("BasicWriter")
    writer.initialize(backend=backend, rgb=True, semantic_segmentation=True, colorize_semantic_segmentation=True)
    writer.attach(rp)

    # Start the timeline (will only advance with app update)
    timeline = omni.timeline.get_timeline_interface()
    timeline.play()

    # Wrap the cube with as a RigidPrim for easy access to its world poses and velocities
    cube_rigid = RigidPrim(str(cube.GetPrimPath()))

    # Wrap the cube as an Imageable object to toggle visibility during capture
    cube_imageable = UsdGeom.Imageable(cube)

    # Define the capture interval in meters
    capture_interval_meters = 0.5
    cube_pos = cube_rigid.get_world_poses(indices=[0])[0].numpy()
    previous_capture_height = cube_pos[0, 2]

    # Update the app which will advance the timeline (and implicitly the simulation)
    for i in range(100):
        await omni.kit.app.get_app().next_update_async()
        cube_pos = cube_rigid.get_world_poses(indices=[0])[0].numpy()
        current_height = cube_pos[0, 2]
        distance_dropped = previous_capture_height - current_height
        print(f"Step {i}; cube height: {current_height:.3f}; drop since last capture: {distance_dropped:.3f}")

        # Stop the simulation if the cube falls below the ground
        if current_height < 0:
            print(f"\t Cube fell below the ground at height {current_height:.3f}, stopping simulation..")
            break

        # Capture every time the cube drops by the threshold distance
        if distance_dropped >= capture_interval_meters:
            print(f"\t Capturing at height {current_height:.3f}")
            previous_capture_height = current_height

            # Setting delta_time to 0.0 will make sure the timeline is not advanced during capture
            await rep.orchestrator.step_async(delta_time=0.0)

            # Capture again with the cube hidden
            print("\t Capturing with cube hidden")
            cube_imageable.MakeInvisible()
            await rep.orchestrator.step_async(delta_time=0.0)
            cube_imageable.MakeVisible()

            # Resume the timeline to continue the simulation
            timeline.play()

    # Pause the simulation
    timeline.pause()

    # Wait for the data to be written to disk and clean up resources
    await rep.orchestrator.wait_until_complete_async()
    writer.detach()
    rp.destroy()

# Run the example
asyncio.ensure_future(run_example_async())
```

Standalone Application

```python
"""Demonstrate simulation-driven SDG with physics-based capture triggers."""

import os

from isaacsim import SimulationApp

simulation_app = SimulationApp(launch_config={"headless": False})

import carb.settings
import omni.replicator.core as rep
import omni.timeline
import omni.usd
from isaacsim.core.experimental.prims import RigidPrim
from pxr import UsdGeom

def run_example():
    """Run physics simulation and capture data at height-based intervals."""
    # Create a new stage and disable capture on play
    omni.usd.get_context().new_stage()
    rep.orchestrator.set_capture_on_play(False)

    # Set DLSS to Quality mode (2) for best SDG results , options: 0 (Performance), 1 (Balanced), 2 (Quality), 3 (Auto)
    carb.settings.get_settings().set("rtx/post/dlss/execMode", 2)

    # Add a light
    rep.functional.create.xform(name="World")
    rep.functional.create.dome_light(intensity=500, parent="/World", name="DomeLight")

    # Create a cube with colliders and rigid body dynamics at a specific location
    cube = rep.functional.create.cube(name="Cube", parent="/World")
    rep.functional.modify.position(cube, (0, 0, 2))
    rep.functional.modify.semantics(cube, {"class": "my_cube"}, mode="add")
    rep.functional.physics.apply_rigid_body(cube, with_collider=True)

    # Createa a sphere with colliders and rigid body dynamics next to the cube
    sphere = rep.functional.create.sphere(name="Sphere", parent="/World")
    rep.functional.modify.position(sphere, (-1, -1, 2))
    rep.functional.modify.semantics(sphere, {"class": "my_sphere"}, mode="add")
    rep.functional.physics.apply_rigid_body(sphere, with_collider=True)

    # Create a render product using the viewport perspective camera
    cam = rep.functional.create.camera(position=(5, 5, 5), look_at=(0, 0, 0), parent="/World", name="Camera")
    rp = rep.create.render_product(cam, (512, 512))

    # Write data using the basic writer with the rgb and bounding box annotators
    backend = rep.backends.get("DiskBackend")
    out_dir = os.path.join(os.getcwd(), "_out_basic_writer_sim")
    backend.initialize(output_dir=out_dir)
    print(f"Output directory: {out_dir}")
    writer = rep.writers.get("BasicWriter")
    writer.initialize(backend=backend, rgb=True, semantic_segmentation=True, colorize_semantic_segmentation=True)
    writer.attach(rp)

    # Start the timeline (will only advance with app update)
    timeline = omni.timeline.get_timeline_interface()
    timeline.play()

    # Wrap the cube with as a RigidPrim for easy access to its world poses and velocities
    cube_rigid = RigidPrim(str(cube.GetPrimPath()))

    # Wrap the cube as an Imageable object to toggle visibility during capture
    cube_imageable = UsdGeom.Imageable(cube)

    # Define the capture interval in meters
    capture_interval_meters = 0.5
    cube_pos = cube_rigid.get_world_poses(indices=[0])[0].numpy()
    previous_capture_height = cube_pos[0, 2]

    # Update the app which will advance the timeline (and implicitly the simulation)
    for i in range(100):
        simulation_app.update()
        cube_pos = cube_rigid.get_world_poses(indices=[0])[0].numpy()
        current_height = cube_pos[0, 2]
        distance_dropped = previous_capture_height - current_height
        print(f"Step {i}; cube height: {current_height:.3f}; drop since last capture: {distance_dropped:.3f}")

        # Stop the simulation if the cube falls below the ground
        if current_height < 0:
            print(f"\t Cube fell below the ground at height {current_height:.3f}, stopping simulation..")
            break

        # Capture every time the cube drops by the threshold distance
        if distance_dropped >= capture_interval_meters:
            print(f"\t Capturing at height {current_height:.3f}")
            previous_capture_height = current_height

            # Setting delta_time to 0.0 will make sure the timeline is not advanced during capture
            rep.orchestrator.step(delta_time=0.0)

            # Capture again with the cube hidden
            print("\t Capturing with cube hidden")
            cube_imageable.MakeInvisible()
            rep.orchestrator.step(delta_time=0.0)
            cube_imageable.MakeVisible()

            # Resume the timeline to continue the simulation
            timeline.play()

    # Pause the simulation
    timeline.pause()

    # Wait for the data to be written to disk and clean up resources
    rep.orchestrator.wait_until_complete()
    writer.detach()
    rp.destroy()

# Run the example
run_example()
```

The output directory will contain the RGB and semantic segmentation images with the captured data at specific simulation times (cube drop height intervals) and the cube hidden during capture. During every second capture with the cube hidden, the timeline will not advance (`delta_time=0.0`) ensuring the same simulation state can be captured multiple times.

### Batch Randomization with Performance Optimization

This example demonstrates batch creation and randomization of 100 cubes using the functional API and `ReplicatorRNG`. It runs three configurations to compare performance: default (`wait_for_render=True`), non-blocking capture (`wait_for_render=False`), and non-blocking capture with [write-to-fabric](#isaac-sim-replicator-getting-started-write-to-fabric) enabled. Each run prints per-step randomization and capture timings as well as the total duration including `wait_until_complete`, illustrating the impact of [wait\_for\_render](#isaac-sim-replicator-getting-started-wait-for-render) and [write-to-fabric](#isaac-sim-replicator-getting-started-write-to-fabric) on throughput. The standalone example can also be run directly (on Windows use `python.bat` instead of `python.sh`):

```python
./python.sh standalone_examples/api/isaacsim.replicator.examples/sdg_getting_started_05.py
```

Script Editor

```python
import asyncio
import os
import time

import carb.settings
import omni.replicator.core as rep
import omni.usd

NUM_CUBES = 100
NUM_CAPTURES = 10

async def run_example_async(wait_for_render, write_to_fabric):
    print(f"\n[SDG] Running with wait_for_render={wait_for_render}, write_to_fabric={write_to_fabric}")
    omni.usd.get_context().new_stage()
    rep.orchestrator.set_capture_on_play(False)

    settings = carb.settings.get_settings()
    settings.set("rtx/post/dlss/execMode", 2)
    settings.set("/exts/omni.replicator.core/enableWriteToFabric", write_to_fabric)

    rng = rep.rng.ReplicatorRNG(seed=42)

    # Setup stage with a dome light and batch-created cubes
    rep.functional.create.xform(name="World")
    rep.functional.create.dome_light(intensity=500, parent="/World", name="DomeLight")
    cubes = rep.functional.create_batch.cube(
        count=NUM_CUBES,
        parent="/World",
        name="Cube",
        semantics={"class": "my_cube"},
    )
    rep.functional.modify.scale(cubes, (0.2, 0.2, 0.2))

    # Create the camera and render product
    cam = rep.functional.create.camera(position=(5, 5, 5), look_at=(0, 0, 0), parent="/World", name="Camera")
    rp = rep.create.render_product(cam, (512, 512))

    # Write data using BasicWriter with rgb annotator
    backend = rep.backends.get("DiskBackend")
    out_dir = os.path.join(os.getcwd(), f"_out_fabric_{write_to_fabric}_wait_{wait_for_render}")
    backend.initialize(output_dir=out_dir)
    print(f"[SDG] Output directory: {out_dir}")
    writer = rep.writers.get("BasicWriter")
    writer.initialize(backend=backend, rgb=True)
    writer.attach(rp)

    # Randomize and capture, measuring timing for each phase
    randomization_times_ms = []
    capture_times_ms = []
    total_start = time.perf_counter()

    for i in range(NUM_CAPTURES):
        random_positions = rng.generator.uniform((-3.0, -3.0, -3.0), (3.0, 3.0, 3.0), size=(NUM_CUBES, 3))
        random_rotations = rng.generator.uniform((0.0, 0.0, 0.0), (360.0, 360.0, 360.0), size=(NUM_CUBES, 3))
        random_scales = rng.generator.uniform(0.1, 0.4, size=(NUM_CUBES, 3))

        rand_start = time.perf_counter()
        rep.functional.modify.pose(
            cubes,
            position_value=random_positions,
            rotation_value=random_rotations,
            scale_value=random_scales,
        )
        rep.functional.randomizer.display_color(cubes, rng=rng)
        rand_ms = (time.perf_counter() - rand_start) * 1000.0
        randomization_times_ms.append(rand_ms)

        cap_start = time.perf_counter()
        await rep.orchestrator.step_async(wait_for_render=wait_for_render)
        cap_ms = (time.perf_counter() - cap_start) * 1000.0
        capture_times_ms.append(cap_ms)

        print(f"[SDG] Step {i}: randomization {rand_ms:.1f} ms, capture {cap_ms:.1f} ms")

    # Wait for all data to be written to disk
    print("[SDG] Waiting for all data to be written to disk..")
    await rep.orchestrator.wait_until_complete_async()
    total_ms = (time.perf_counter() - total_start) * 1000.0

    avg_rand = sum(randomization_times_ms) / len(randomization_times_ms)
    avg_cap = sum(capture_times_ms) / len(capture_times_ms)
    print(f"[SDG] Avg randomization: {avg_rand:.1f} ms, avg capture: {avg_cap:.1f} ms, total: {total_ms:.1f} ms")

    writer.detach()
    rp.destroy()

async def run_examples_async():
    # Run with different configurations to compare performance
    await run_example_async(wait_for_render=True, write_to_fabric=False)
    await run_example_async(wait_for_render=False, write_to_fabric=False)
    await run_example_async(wait_for_render=False, write_to_fabric=True)

asyncio.ensure_future(run_examples_async())
```

Standalone Application

```python
"""Demonstrate SDG performance with fabric writes and render wait options."""

import os
import time

from isaacsim import SimulationApp

simulation_app = SimulationApp(launch_config={"headless": False})

import carb.settings
import omni.replicator.core as rep
import omni.usd

NUM_CUBES = 100
NUM_CAPTURES = 10

def run_example(wait_for_render, write_to_fabric):
    """Run SDG with the given render wait and fabric write settings."""
    print(f"\n[SDG] Running with wait_for_render={wait_for_render}, write_to_fabric={write_to_fabric}")
    omni.usd.get_context().new_stage()
    rep.orchestrator.set_capture_on_play(False)

    settings = carb.settings.get_settings()
    settings.set("rtx/post/dlss/execMode", 2)
    settings.set("/exts/omni.replicator.core/enableWriteToFabric", write_to_fabric)

    rng = rep.rng.ReplicatorRNG(seed=42)

    # Setup stage with a dome light and batch-created cubes
    rep.functional.create.xform(name="World")
    rep.functional.create.dome_light(intensity=500, parent="/World", name="DomeLight")
    cubes = rep.functional.create_batch.cube(
        count=NUM_CUBES,
        parent="/World",
        name="Cube",
        semantics={"class": "my_cube"},
    )
    rep.functional.modify.scale(cubes, (0.2, 0.2, 0.2))

    # Create the camera and render product
    cam = rep.functional.create.camera(position=(5, 5, 5), look_at=(0, 0, 0), parent="/World", name="Camera")
    rp = rep.create.render_product(cam, (512, 512))

    # Write data using BasicWriter with rgb annotator
    backend = rep.backends.get("DiskBackend")
    out_dir = os.path.join(os.getcwd(), f"_out_fabric_{write_to_fabric}_wait_{wait_for_render}")
    backend.initialize(output_dir=out_dir)
    print(f"[SDG] Output directory: {out_dir}")
    writer = rep.writers.get("BasicWriter")
    writer.initialize(backend=backend, rgb=True)
    writer.attach(rp)

    # Randomize and capture, measuring timing for each phase
    randomization_times_ms = []
    capture_times_ms = []
    total_start = time.perf_counter()

    for i in range(NUM_CAPTURES):
        random_positions = rng.generator.uniform((-3.0, -3.0, -3.0), (3.0, 3.0, 3.0), size=(NUM_CUBES, 3))
        random_rotations = rng.generator.uniform((0.0, 0.0, 0.0), (360.0, 360.0, 360.0), size=(NUM_CUBES, 3))
        random_scales = rng.generator.uniform(0.1, 0.4, size=(NUM_CUBES, 3))

        rand_start = time.perf_counter()
        rep.functional.modify.pose(
            cubes,
            position_value=random_positions,
            rotation_value=random_rotations,
            scale_value=random_scales,
        )
        rep.functional.randomizer.display_color(cubes, rng=rng)
        rand_ms = (time.perf_counter() - rand_start) * 1000.0
        randomization_times_ms.append(rand_ms)

        cap_start = time.perf_counter()
        rep.orchestrator.step(wait_for_render=wait_for_render)
        cap_ms = (time.perf_counter() - cap_start) * 1000.0
        capture_times_ms.append(cap_ms)

        print(f"[SDG] Step {i}: randomization {rand_ms:.1f} ms, capture {cap_ms:.1f} ms")

    # Wait for all data to be written to disk
    print("[SDG] Waiting for all data to be written to disk..")
    rep.orchestrator.wait_until_complete()
    total_ms = (time.perf_counter() - total_start) * 1000.0

    avg_rand = sum(randomization_times_ms) / len(randomization_times_ms)
    avg_cap = sum(capture_times_ms) / len(capture_times_ms)
    print(f"[SDG] Avg randomization: {avg_rand:.1f} ms, avg capture: {avg_cap:.1f} ms, total: {total_ms:.1f} ms")

    writer.detach()
    rp.destroy()

# Run with different configurations to compare performance
run_example(wait_for_render=True, write_to_fabric=False)
run_example(wait_for_render=False, write_to_fabric=False)
run_example(wait_for_render=False, write_to_fabric=True)
```

Each configuration writes its output to a separate directory. The terminal output shows per-step randomization and capture durations (in milliseconds) and total time, allowing direct comparison of the three modes.

## Troubleshooting

For troubleshooting information related to the Getting Started Scripts, refer to the [Getting Started Scripts Issues](troubleshooting.html#isaac-sim-replicator-troubleshooting-getting-started) section in the Replicator Troubleshooting page.

## Next Steps

After completing these examples, consider exploring:

1. Advanced randomizations using the [Randomizer Details](https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator/randomizer_details.html "(in Omniverse Extensions)")
2. Custom annotators for specialized data capture
3. Distributed data generation using multiple GPUs
4. Integration with machine learning pipelines
5. Advanced physics-based simulations

For more information, refer to:
- [Replicator Documentation](https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator/basic_functionalities.html "(in Omniverse Extensions)")
- [Isaac Sim Randomizers Guide](tutorial_replicator_isaac_randomizers.html#isaac-sim-app-tutorial-replicator-isaac-randomizers)
- [I/O Optimization Guide](https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator/io_guidelines.html "(in Omniverse Extensions)")

On this page

* [Prerequisites](#prerequisites)
* [Setup and Configuration](#setup-and-configuration)
* [Orchestrator Step Function](#orchestrator-step-function)
* [Capture on Play Flag](#capture-on-play-flag)
* [RT Subframes Parameter](#rt-subframes-parameter)
* [DLSS Quality Mode for SDG](#dlss-quality-mode-for-sdg)
* [Wait for Render Parameter](#wait-for-render-parameter)
* [Write to Fabric Mode](#write-to-fabric-mode)
* [Custom Event Randomizations](#custom-event-randomizations)
* [Wait Until Complete](#wait-until-complete)
* [Examples](#examples)
  + [Data Capture: BasicWriter](#data-capture-basicwriter)
  + [Custom Writer and Annotators with Multiple Cameras](#custom-writer-and-annotators-with-multiple-cameras)
  + [Custom Randomizations: Replicator Graph and USD API](#custom-randomizations-replicator-graph-and-usd-api)
  + [Event-Triggered Data Capture: Timeline and Simulation](#event-triggered-data-capture-timeline-and-simulation)
  + [Batch Randomization with Performance Optimization](#batch-randomization-with-performance-optimization)
* [Troubleshooting](#troubleshooting)
* [Next Steps](#next-steps)

---

### Modular Scripting

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/replicator_tutorials/tutorial_replicator_modular_scripting.html

* [Synthetic Data Generation](../synthetic_data_generation/index.html)
* [Perception Data Generation (Replicator)](index.html)
* Modular Behavior Scripting

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Modular Behavior Scripting

## Overview

This tutorial introduces the `isaacsim.replicator.behavior` extension and walks through its modular behavior scripts for Isaac Sim Replicator synthetic data generation (SDG). Built on top of the [Python Scripting Component](https://docs.omniverse.nvidia.com/extensions/latest/ext_python-scripting-component/user_manual.html), these behaviors attach directly to prims in a USD stage and act as randomizers or custom smart-asset behaviors that are reusable, shareable, and easy to modify.

The behavior functionality ships as two extensions:

* `isaacsim.replicator.behavior` — the core extension containing the behavior scripts. It has no UI dependency and runs in headless mode.
* `isaacsim.replicator.behavior.ui` — the UI extension that renders exposed variables in the **Property** panel.

The two extensions communicate through a carb event, so the core can run without the UI loaded. See [Core and UI extension split](#core-and-ui-extension-split) for details.

Find the bundled behavior scripts under:

`/exts/isaacsim.replicator.behavior/isaacsim/replicator/behavior/behaviors/*`

### Learning Objectives

After completing this tutorial, you will understand how to:

* **Use pre-built behavior scripts** for common synthetic data generation tasks, including:

  + **Location Randomizer** - randomizes prim positions within specified bounds for object placement variety
  + **Rotation Randomizer** - applies random rotations to enhance orientation diversity in datasets
  + **Look At Behavior** - makes prims continuously face target locations or other prims for camera tracking
  + **Light Randomizer** - randomizes light properties like color and intensity to simulate different lighting conditions
  + **Texture Randomizer** - applies random textures to materials for increased visual variety
  + **Volume Stack Randomizer** - uses physics simulation to randomly stack objects for realistic arrangements
* **Understand behavior script architecture** - how modular Python scripts attach to prims and can be customized through exposed USD attributes, with configurable parameters like update intervals and randomization ranges
* **Control behavior execution** - configure behaviors to run on timeline events (start, update, stop) or trigger them independently using custom events for advanced workflows
* **Create custom behavior scripts** - develop your own behaviors using the provided templates and base classes for specific synthetic data generation needs
* **Build complex SDG pipelines** - combine multiple behaviors, simulations, and events to create sophisticated data generation workflows, such as physics-based object stacking followed by automated data capture

### Prerequisites

Before starting, make sure you are familiar with:

* USD and Isaac Sim APIs for creating and manipulating USD stages
* [Python Scripting Component](https://docs.omniverse.nvidia.com/extensions/latest/ext_python-scripting-component/user_manual.html) in Isaac Sim
* The [timeline](https://docs.omniverse.nvidia.com/extensions/latest/ext_animation-timeline.html "(in Omniverse Extensions)") and [custom events](https://docs.omniverse.nvidia.com/kit/docs/kit-manual/latest/guide/events.html) system
* [omni.replicator](https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator.html "(in Omniverse Extensions)") and its Isaac Sim [tutorials](tutorial_replicator_getting_started.html#isaac-sim-app-tutorial-replicator-getting-started) for synthetic data generation
* [Writers](https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator/writer_examples.html "(in Omniverse Extensions)") and [annotators](https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator/annotators_details.html "(in Omniverse Extensions)") for data capture
* Running scripts using the [Script Editor](https://docs.omniverse.nvidia.com/extensions/latest/ext_script-editor.html "(in Omniverse Extensions)") to setup and run pipelines

Note

To attach behavior scripts to prims from the UI (**Property** panel > **Add** > **Python Scripting**), enable the `omni.behavior.scripting.ui` extension from **Window** > **Extensions**. This extension ships the Python Scripting Component UI and is not enabled by default. The core behaviors in `isaacsim.replicator.behavior` run without it, which is useful for headless SDG pipelines.

### Demonstration

The [example section](#isaac-sim-app-tutorial-replicator-modular-scripting-example) provides a demonstration of how to use the behavior scripts to create a custom synthetic data generation pipeline:

### Behavior scripts

**Behavior scripts** are modular Python scripts attached to prims in a USD stage. By default, they respond to timeline events — start, pause, stop, and update — and define the randomization or custom logic applied to the prim during simulation or data generation.

Attaching scripts directly to prims embeds the behavior in the USD itself and gives you:

* **Modularity.** Attach, detach, or swap scripts on a prim without changing core logic.
* **Shareability.** Embed behaviors within assets and reuse them across projects or stages.
* **Configurability.** Expose variables as USD attributes and edit them without modifying source.
* **Persistence.** Scripts live on the prim and travel with the stage, so you can version them alongside it.
* **Reusability and encapsulation.** Write a behavior once and reuse it across prims and scenes with minimal external dependencies.

### Exposing variables through USD attributes

Each behavior script exposes its input parameters as namespaced USD attributes on the prim that carries the script. This lets you edit behavior parameters directly from the **Property** panel — or programmatically through the USD API — without modifying the script source.

Exposing variables as USD attributes provides three benefits:

* **Customization.** Tune parameters such as target locations, ranges, or seeds per prim instance.
* **Interactivity.** Edit values in the UI and observe the effect on the next update.
* **Consistency.** Every behavior presents the same editing interface regardless of its internal logic.

The scripts use the USD API to create custom attributes under a shared namespace (`exposedVar:<behaviorNamespace>:<attrName>`) and read them back during execution to drive their logic.

#### Core and UI extension split

The behavior functionality is split across two extensions:

* `isaacsim.replicator.behavior` — the **core** extension. It defines the behavior scripts, creates and removes the exposed USD attributes, and has no UI dependency. This lets you run the behaviors in headless mode (for example, during automated SDG pipelines).
* `isaacsim.replicator.behavior.ui` — the **UI** extension. It registers an `ExposedVariablesPropertyWidget` with the **Property** panel that automatically renders the exposed variables as editable fields.

The two extensions communicate through a single carb event, `isaacsim.replicator.behavior.EXPOSED_VARS_CHANGED`:

1. The core extension dispatches the event whenever it creates or removes exposed variables on a prim.
2. The UI extension subscribes to the event at startup and rebuilds the **Property** panel when it fires.

This event-based decoupling allows the core extension to run without the UI loaded, and the UI extension to refresh on demand without the core importing any UI modules.

**Example of Exposed Variables Definition:**

```python
VARIABLES_TO_EXPOSE = [
    {
        "attr_name": "targetLocation",
        "attr_type": Sdf.ValueTypeNames.Vector3d,
        "default_value": Gf.Vec3d(0.0, 0.0, 0.0),
        "doc": "The 3D vector specifying the location to look at.",
    },
    {
        "attr_name": "targetPrimPath",
        "attr_type": Sdf.ValueTypeNames.String,
        "default_value": "",
        "doc": "The path of the target prim to look at. If specified, it has priority over the target location.",
    },
    # Additional variables...
]
```

### Custom event-based behavior scripts

Timeline-driven behaviors are convenient, but some workflows need to run independently of the simulation clock — for example, pre-simulation setup, one-shot scene preparation, or sequences that must complete before data capture begins.

**Event-based scripting** lets a behavior skip the default timeline hooks and instead publish and subscribe to [custom events](https://docs.omniverse.nvidia.com/kit/docs/kit-manual/latest/guide/events.html) on the Omniverse event bus. This gives you:

* **Flexibility.** Trigger behaviors on demand, decoupled from the simulation timeline.
* **Modularity.** Orchestrate complex workflows by chaining behaviors through events.
* **Performance.** Avoid per-frame work by running behaviors only when triggered.

The `volume_stack_randomizer.py` script illustrates this pattern. It uses custom events to drop, stack, and settle assets using physics *before* the timeline starts, so the data-capture phase runs against a deterministic initial state.

## Script Examples

In this section, various behavior scripts available in the `isaacsim.replicator.behavior` extension are explored. Each script provides specific functionality that can enhance synthetic data generation workflows. The scripts are designed to be modular, reusable, and customizable through exposed variables.

The folder path for the behavior scripts is:

`/exts/isaacsim.replicator.behavior/isaacsim/replicator/behavior/behaviors/*`

### Location Randomizer

The `location_randomizer.py` script randomizes the location of prims within specified bounds during runtime, providing position variability for enhanced synthetic datasets.

Overview

**Purpose:** Randomizes prim positions within defined bounds to create variety in object placement.

**Key Features:**

* Position range randomization within minimum and maximum bounds
* Relative positioning support using target prims as reference points
* Child prim inclusion for hierarchical randomization
* Configurable update intervals for performance control

**Exposed Variables:**

Configuration Parameters

* **range:minPosition** (Vector3d): Minimum bounds of the random offset.
* **range:maxPosition** (Vector3d): Maximum bounds of the random offset.
* **frame:useRelativeFrame** (Bool): If True, preserve the prim’s initial offset (from the target prim if set, otherwise from its own starting position) and add the random offset on top. If False, the random offset is applied as an absolute position (relative to the target prim if set, otherwise to the world origin).
* **frame:targetPrimPath** (String): Optional path to a reference prim. When set, all randomization is anchored to this prim’s world location; leave empty to randomize independently of any other prim.
* **includeChildren** (Bool): Include child prims in randomization.
* **interval** (UInt): Update frequency (0 = every frame).

**Behavior Matrix:**

The combination of `frame:targetPrimPath` and `frame:useRelativeFrame` determines how the random offset is applied:

| `targetPrimPath` | `useRelativeFrame` | Resulting location |
| --- | --- | --- |
| empty | False | `random_offset` (treated as absolute world coordinates). |
| empty | True | `initial_location + random_offset` (jitter around the prim’s starting position). |
| set | False | `target_location + random_offset` (prim is placed near the target, ignoring its original position). |
| set | True | `target_location + initial_offset_from_target + random_offset` (prim follows the target while preserving its original relative offset). |

To make the prim’s randomization fully independent of any other prim, leave `frame:targetPrimPath` empty. Toggling `frame:useRelativeFrame` alone does not decouple the prim from the target.

Implementation Details

**Child Prim Inclusion:**

Child Prim Selection Logic

```python
def _setup(self):
    include_children = self._get_exposed_variable("includeChildren")
    if include_children:
        self._valid_prims = [prim for prim in Usd.PrimRange(self.prim) if prim.IsA(UsdGeom.Xformable)]
    elif self.prim.IsA(UsdGeom.Xformable):
        self._valid_prims = [self.prim]
    else:
        self._valid_prims = []
        carb.log_warn(f"[{self.prim_path}] No valid prims found.")
```

* When **includeChildren** is True: Uses Usd.PrimRange to select all transformable descendant prims
* When **includeChildren** is False: Only includes the assigned prim if it’s transformable
* Logs warning if no valid prims are found

**Randomization Logic:**

Core Randomization Implementation

```python
def _randomize_location(self, prim):
    # Generate random offset within bounds
    random_offset = Gf.Vec3d(
        random.uniform(self._min_position[0], self._max_position[0]),
        random.uniform(self._min_position[1], self._max_position[1]),
        random.uniform(self._min_position[2], self._max_position[2]),
    )

    # Calculate final location based on target prim and relative frame settings
    if self._target_prim:
        target_loc = get_world_location(self._target_prim)
        loc = (
            target_loc + self._target_offsets[prim] + random_offset
            if self._use_relative_frame
            else target_loc + random_offset
        )
    else:
        loc = self._initial_locations[prim] + random_offset if self._use_relative_frame else random_offset

    self._set_location(prim, loc)
```

* Generates a random offset within the configured `range:minPosition` / `range:maxPosition` bounds.
* If `frame:targetPrimPath` is set, anchors the result to the target prim’s current world location.
* If `frame:useRelativeFrame` is True, preserves the prim’s initial offset (from the target prim if set, otherwise from its own starting position) so the random offset acts as jitter rather than an absolute placement.
* Writes the final location to the prim using the existing translate or transform xformOp.

Usage Example

**Basic Setup:**

Step-by-Step Configuration

1. **Attach Script**: Add location\_randomizer.py to your target prim
2. **Set Bounds**: Configure range:minPosition and range:maxPosition
3. **Enable Children**: Set includeChildren to True for hierarchical randomization
4. **Set Interval**: Use interval to control update frequency

**Example Configuration:**

* **range:minPosition**: (-5.0, -5.0, 0.0)
* **range:maxPosition**: (5.0, 5.0, 2.0)
* **includeChildren**: True
* **interval**: 5 (updates every 5 frames)

**Use Cases:**

* **Background Objects**: Randomize prop positions for scene variety. Leave `frame:targetPrimPath` empty and set `frame:useRelativeFrame` to True to jitter each prop around its authored location.
* **Follow a Moving Target**: Keep an object’s relative offset to a moving prim. Set `frame:targetPrimPath` to the target and `frame:useRelativeFrame` to True.
* **Snap Near a Target**: Place an object at randomized positions around a target, ignoring its original location. Set `frame:targetPrimPath` to the target and `frame:useRelativeFrame` to False.
* **Hierarchical Randomization**: Apply randomization to object groups by enabling `includeChildren`.

### Rotation Randomizer

The `rotation_randomizer.py` script applies random rotations to prims during runtime, enhancing orientation diversity in synthetic datasets.

Overview

**Purpose:** Applies random rotations to prims within specified Euler angle bounds.

**Key Features:**

* Rotation range randomization within minimum and maximum angle bounds
* Child prim inclusion for hierarchical rotation randomization
* Configurable update intervals for performance optimization

**Exposed Variables:**

Configuration Parameters

* **range:minRotation** (Vector3d): Minimum rotation angles in degrees (X, Y, Z)
* **range:maxRotation** (Vector3d): Maximum rotation angles in degrees (X, Y, Z)
* **includeChildren** (Bool): Include child prims in rotation randomization
* **interval** (UInt): Update frequency (0 = every frame)

Implementation Details

**Child Prim Selection:**

Child Prim Selection Logic

```python
def _setup(self):
    include_children = self._get_exposed_variable("includeChildren")
    if include_children:
        self._valid_prims = [prim for prim in Usd.PrimRange(self.prim) if prim.IsA(UsdGeom.Xformable)]
    elif self.prim.IsA(UsdGeom.Xformable):
        self._valid_prims = [self.prim]
    else:
        self._valid_prims = []
        carb.log_warn(f"[{self.prim_path}] No valid prims found.")
```

* When **includeChildren** is True: All transformable descendant prims are included
* When **includeChildren** is False: Only the assigned prim is considered if transformable
* Warning logged if no valid prims found

**Rotation Randomization:**

Core Rotation Implementation

```python
def _randomize_rotation(self, prim):
    rotation = (
        Gf.Rotation(Gf.Vec3d.XAxis(), random.uniform(self._min_rotation[0], self._max_rotation[0]))
        * Gf.Rotation(Gf.Vec3d.YAxis(), random.uniform(self._min_rotation[1], self._max_rotation[1]))
        * Gf.Rotation(Gf.Vec3d.ZAxis(), random.uniform(self._min_rotation[2], self._max_rotation[2]))
    )
    set_rotation_with_ops(prim, rotation)
```

* Generates random Euler angles within specified bounds for each axis
* Creates composite rotation by multiplying X, Y, and Z axis rotations
* Applies rotation using set\_rotation\_with\_ops for proper transformation handling

Usage Example

**Basic Setup:**

Step-by-Step Configuration

1. **Attach Script**: Add rotation\_randomizer.py to your target prim
2. **Set Rotation Bounds**: Configure range:minRotation and range:maxRotation
3. **Enable Children**: Set includeChildren to True for hierarchical rotation
4. **Set Interval**: Use interval to control update frequency

**Example Configuration:**

* **range:minRotation**: (-180.0, -90.0, 0.0) degrees
* **range:maxRotation**: (180.0, 90.0, 360.0) degrees
* **includeChildren**: True
* **interval**: 10 (updates every 10 frames)

**Use Cases:**

* **Object Variety**: Randomize prop orientations for diverse scenes
* **Tumbling Effects**: Simulate falling or floating objects
* **Presentation Angles**: Vary object viewing angles for training data

### Look At Behavior

The `look_at_behavior.py` script orients prims to continuously face a specified target, ideal for camera tracking and sensor alignment.

Overview

**Purpose:** Orients prims to continuously face a target location or another prim.

**Key Features:**

* Target specification using fixed coordinates or dynamic prim tracking
* Up axis control for maintaining consistent orientation
* Child prim inclusion for hierarchical look-at behavior
* Configurable update intervals for performance control

**Exposed Variables:**

Configuration Parameters

* **targetLocation** (Vector3d): Fixed 3D coordinates to look at
* **targetPrimPath** (String): Path to target prim (overrides targetLocation)
* **upAxis** (Vector3d): Up axis for orientation (e.g., (0, 0, 1) for +Z)
* **includeChildren** (Bool): Include child prims in look-at behavior
* **interval** (UInt): Update frequency (0 = every frame)

Implementation Details

**Target Prim Handling:**

Target Prim Resolution

```python
def _setup(self):
    target_prim_path = self._get_exposed_variable("targetPrimPath")
    if target_prim_path:
        self._target_prim = self.stage.GetPrimAtPath(target_prim_path)
        if not self._target_prim or not self._target_prim.IsValid() or not self._target_prim.IsA(UsdGeom.Xformable):
            self._target_prim = None
            carb.log_warn(f"[{self.prim_path}] Invalid target prim path: {target_prim_path}")
```

* **targetPrimPath** takes precedence over **targetLocation** when specified
* Validates target prim exists and is transformable
* Logs warning if target prim is invalid

**Orientation Calculation:**

Look-At Rotation Implementation

```python
def _apply_behavior(self):
    target_location = self._get_target_location()
    for prim in self._valid_prims:
        eye = get_world_location(prim)
        if (target_location - eye).GetLength() < 1e-9:
            continue  # Already at target; skip rotation to avoid undefined look-at
        look_at_rotation = calculate_look_at_rotation(eye, target_location, self._up_axis)
        set_rotation_with_ops(prim, look_at_rotation)
```

* Retrieves current prim position using get\_world\_location
* Calculates required rotation using calculate\_look\_at\_rotation
* Applies rotation while preserving existing transformation operations

Usage Example

**Basic Setup:**

Step-by-Step Configuration

1. **Attach Script**: Add look\_at\_behavior.py to your camera or sensor prim
2. **Set Target**: Configure either targetLocation or targetPrimPath
3. **Adjust Up Axis**: Set upAxis to maintain desired orientation
4. **Set Interval**: Use interval to control update frequency

**Example Configuration:**

* **targetPrimPath**: /World/MovingObject/Prim
* **upAxis**: (0, 0, 1) (Z-up orientation)
* **includeChildren**: False (camera only)
* **interval**: 1 (update every frame)

**Use Cases:**

* **Camera Tracking**: Make cameras follow moving subjects
* **Sensor Alignment**: Point sensors at targets of interest
* **Lighting Direction**: Orient lights to follow objects

### Light Randomizer

The `light_randomizer.py` script randomizes light properties to simulate different lighting conditions for enhanced scene variability.

Overview

**Purpose:** Randomizes light color and intensity properties to create diverse lighting scenarios.

**Key Features:**

* Color randomization varying RGB values within specified ranges
* Intensity randomization adjusting brightness between minimum and maximum values
* Child light inclusion for hierarchical lighting randomization
* Configurable update intervals for performance optimization

**Exposed Variables:**

Configuration Parameters

* **includeChildren** (Bool): Include child light prims in randomization
* **interval** (UInt): Update frequency (0 = every frame)
* **range:minColor** (Color3f): Minimum RGB values for color randomization
* **range:maxColor** (Color3f): Maximum RGB values for color randomization
* **range:intensity** (Float2): Intensity range as (min, max) values

Implementation Details

**Light Property Randomization:**

Color and Intensity Randomization

```python
def _apply_behavior(self):
    for prim in self._valid_prims:
        rand_color = (
            random.uniform(self._min_color[0], self._max_color[0]),
            random.uniform(self._min_color[1], self._max_color[1]),
            random.uniform(self._min_color[2], self._max_color[2]),
        )
        prim.GetAttribute("inputs:color").Set(rand_color)

        rand_intensity = random.uniform(self._intensity_range[0], self._intensity_range[1])
        prim.GetAttribute("inputs:intensity").Set(rand_intensity)
```

* Generates random RGB values within specified color ranges
* Applies random intensity values within defined bounds
* Updates light attributes directly using USD API

**Child Light Selection:**

Light Prim Discovery

```python
def _setup(self):
    include_children = self._get_exposed_variable("includeChildren")
    if include_children:
        self._valid_prims = [prim for prim in Usd.PrimRange(self.prim) if prim.HasAPI(UsdLux.LightAPI)]
    elif self.prim.HasAPI(UsdLux.LightAPI):
        self._valid_prims = [self.prim]
    else:
        self._valid_prims = []
        carb.log_warn(f"[{self.prim_path}] No valid light prims found.")
```

* Uses UsdLux.LightAPI to identify valid light prims
* Includes child lights when **includeChildren** is enabled
* Validates that target prim or children have light API

Usage Example

**Basic Setup:**

Step-by-Step Configuration

1. **Attach Script**: Add light\_randomizer.py to a light prim or parent containing lights
2. **Set Color Range**: Configure range:minColor and range:maxColor
3. **Set Intensity Range**: Define range:intensity min/max values
4. **Enable Children**: Set includeChildren to True for multiple lights

**Example Configuration:**

* **range:minColor**: (0.8, 0.8, 0.8) (warm white minimum)
* **range:maxColor**: (1.0, 1.0, 1.0) (bright white maximum)
* **range:intensity**: (1000.0, 5000.0) (intensity range)
* **includeChildren**: True
* **interval**: 0 (update every frame)

**Use Cases:**

* **Day/Night Cycles**: Simulate changing lighting conditions
* **Dynamic Environments**: Create flickering or varying light sources
* **Color Temperature**: Randomize between warm and cool lighting

### Texture Randomizer

The `texture_randomizer.py` script randomly applies textures to materials for increased visual variety of objects.

Overview

**Purpose:** Randomly applies textures to visual prims to create diverse material appearances.

**Key Features:**

* Texture selection from provided asset arrays or CSV lists
* Material creation with randomized parameters (scale, rotation, UV projection)
* Child prim inclusion for hierarchical texture randomization
* Configurable update intervals for performance control

**Exposed Variables:**

Configuration Parameters

* **includeChildren** (Bool): Include child prims in texture randomization
* **interval** (UInt): Update frequency (0 = every frame)
* **textures:assets** (AssetArray): List of texture assets to use
* **textures:csv** (String): CSV string of texture URLs
* **projectUvwProbability** (Float): Probability of enabling project\_uvw
* **textureScaleRange** (Float2): Texture scale range as (min, max)
* **textureRotateRange** (Float2): Texture rotation range in degrees (min, max)

Implementation Details

**Texture Application:**

Material and Shader Randomization

```python
def _apply_behavior(self):
    if not self._texture_urls:
        carb.log_warn(f"[{self.prim_path}] No texture URLs provided; skipping.")
        return
    for mat in self._texture_materials:
        shader = UsdShade.Shader(omni.usd.get_shader_from_material(mat.GetPrim(), get_prim=True))
        if not shader:
            continue
        diffuse_texture = random.choice(self._texture_urls)
        if shader.GetInput("diffuse_texture"):
            shader.GetInput("diffuse_texture").Set(diffuse_texture)

        project_uvw = random.choices(
            [True, False], weights=[self._project_uvw_probability, 1 - self._project_uvw_probability]
        )[0]
        shader.GetInput("project_uvw").Set(bool(project_uvw))

        texture_scale = random.uniform(self._texture_scale_range[0], self._texture_scale_range[1])
        shader.GetInput("texture_scale").Set((texture_scale, texture_scale))

        texture_rotate = random.uniform(self._texture_rotate_range[0], self._texture_rotate_range[1])
        shader.GetInput("texture_rotate").Set(texture_rotate)
```

* Randomly selects textures from provided asset list
* Applies probabilistic UV projection settings
* Randomizes texture scale and rotation parameters
* Updates shader inputs directly via USD API

**Child Prim Selection:**

Geometric Prim Discovery

```python
def _setup(self):
    include_children = self._get_exposed_variable("includeChildren")
    if include_children:
        self._valid_prims = [prim for prim in Usd.PrimRange(self.prim) if prim.IsA(UsdGeom.Gprim)]
    elif self.prim.IsA(UsdGeom.Gprim):
        self._valid_prims = [self.prim]
    else:
        self._valid_prims = []
        carb.log_warn(f"[{self.prim_path}] No valid prims found.")
```

* Uses UsdGeom.Gprim to identify geometric prims suitable for materials
* Includes child prims when **includeChildren** is enabled
* Validates that target prims can receive material bindings

Usage Example

**Basic Setup:**

Step-by-Step Configuration

1. **Attach Script**: Add texture\_randomizer.py to a geometric prim
2. **Provide Textures**: Set textures:assets or textures:csv with texture paths
3. **Configure Parameters**: Adjust scale, rotation, and UV projection settings
4. **Enable Children**: Set includeChildren to True for multiple objects

**Example Configuration:**

* **textures:csv**: “texture1.jpg,texture2.png,texture3.exr”
* **textureScaleRange**: (0.5, 2.0) (scale variation)
* **textureRotateRange**: (0.0, 360.0) (full rotation)
* **projectUvwProbability**: 0.3 (30% chance of UV projection)
* **includeChildren**: True

**Use Cases:**

* **Material Variety**: Create diverse surface appearances for objects
* **Background Variation**: Randomize textures on environmental elements
* **Asset Augmentation**: Enhance object datasets with texture variation

### Volume Stack Randomizer

The `volume_stack_randomizer.py` script uses physics simulation to randomly stack objects for realistic object arrangements.

Overview

**Purpose:** Randomly drops and stacks assets within specified areas using physics simulation.

**Key Features:**

* Asset randomization from provided lists or CSV paths
* Physics simulation for natural stacking behavior
* Event-based execution independent of simulation timeline
* Customizable parameters for drop height, asset count, and rendering

**Exposed Variables:**

Configuration Parameters

* **includeChildren** (Bool): Include child prims in the behavior
* **event:input** (String): Event name to subscribe to for behavior control
* **event:output** (String): Event name to publish after behavior execution
* **assets:assets** (AssetArray): List of asset references to spawn
* **assets:csv** (String): CSV string of asset URLs to spawn
* **assets:numRange** (Int2): Range for number of assets to spawn (min, max)
* **dropHeight** (Float): Height from which to drop the assets
* **renderSimulation** (Bool): Whether to render simulation steps
* **removeRigidBodyDynamics** (Bool): Remove rigid body dynamics after simulation
* **preserveSimulationState** (Bool): Keep final simulation state

Implementation Details

**Core Structure:**

Class Architecture

```python
class VolumeStackRandomizer(BehaviorScript):
    BEHAVIOR_NS = "volumeStackRandomizer"
    EVENT_NAME_IN = f"{EXTENSION_NAME}.{BEHAVIOR_NS}.in"
    EVENT_NAME_OUT = f"{EXTENSION_NAME}.{BEHAVIOR_NS}.out"
    ACTION_FUNCTION_MAP = {
        "setup": "_setup_async",
        "run": "_run_behavior_async",
        "reset": "_reset_async",
    }

    async def _setup_async(self):
        # Asynchronous setup logic...
        pass

    async def _run_behavior_async(self):
        # Asynchronous behavior execution...
        pass

    async def _reset_async(self):
        # Asynchronous reset logic...
        pass
```

* Event-based behavior using custom events for lifecycle management
* Asynchronous methods for non-blocking physics simulation
* Action function mapping for external event control

**Child Prim Selection:**

Surface Area Discovery

```python
async def _setup_async(self):
    include_children = self._get_exposed_variable("includeChildren")
    if include_children:
        self._valid_prims = [prim for prim in Usd.PrimRange(self.prim) if prim.IsA(UsdGeom.Gprim)]
    elif self.prim.IsA(UsdGeom.Gprim):
        self._valid_prims = [self.prim]
    else:
        self._valid_prims = []
        carb.log_warn(f"[{self.prim_path}] No valid prims found.")
```

* Identifies geometric prims suitable for object stacking surfaces
* Includes child prims when **includeChildren** is enabled
* Validates surface prims can receive physics objects

Event-Based Control

**Custom Event System:**

Event-Based Execution Control

The Volume Stack Randomizer operates using custom events rather than timeline-based updates, allowing for precise control over when stacking operations occur.

**Event Flow:**

1. **Reset Phase**: Cleans up previous simulation state
2. **Setup Phase**: Spawns assets and prepares physics simulation
3. **Run Phase**: Executes physics simulation for object stacking
4. **Completion**: Publishes completion event with final state

**Event Control Example:**

```python
async def run_stacking_simulation_async(prim_path=None):
    actions = [("reset", "RESET", 10), ("setup", "SETUP", 500), ("run", "FINISHED", 1500)]
    for action, state, wait in actions:
        await publish_event_and_wait_for_completion_async(
            publish_payload={"prim_path": prim_path, "action": action},
            expected_payload={"prim_path": prim_path, "state_name": state},
            publish_event_name=VolumeStackRandomizer.EVENT_NAME_IN,
            subscribe_event_name=VolumeStackRandomizer.EVENT_NAME_OUT,
            max_wait_updates=wait,
        )
```

**Integration Benefits:**

* **Precise Control**: Execute stacking at specific workflow points
* **Sequential Operations**: Chain multiple stacking operations
* **State Management**: Track completion of each simulation phase
* **External Orchestration**: Control from external scripts or systems

Usage Example

**Basic Setup:**

Step-by-Step Configuration

1. **Attach Script**: Add volume\_stack\_randomizer.py to surface prims
2. **Configure Assets**: Set assets:csv or assets:assets with object paths
3. **Set Parameters**: Define assets:numRange, dropHeight, and other settings
4. **Control Events**: Use custom events to trigger stacking operations

**Example Configuration:**

* **assets:csv**: “box1.usd,box2.usd,cylinder.usd”
* **assets:numRange**: (5, 20) (spawn 5-20 objects)
* **dropHeight**: 2.0 (drop from 2 units above surface)
* **renderSimulation**: True (show simulation steps)
* **preserveSimulationState**: True (keep final arrangement)

**Use Cases:**

* **Object Arrangement**: Create realistic piles of objects
* **Physics Validation**: Test object interactions and stability
* **Scene Preparation**: Set up complex scenes before data capture
* **Simulation Workflows**: Integrate physics-based randomization into pipelines

### Templates

This section provides template scripts that serve as starting points for creating custom behaviors.

Available Templates

**Template Scripts:**

* **example\_behavior.py**: Basic template with boilerplate code for new behaviors
* **base\_behavior.py** and **example\_base\_behavior.py**: Demonstrate base behavior class inheritance for structured development
* **example\_custom\_event\_behavior.py**: Shows implementation of event-based behaviors

**Key Template Features:**

* **Variable Exposure**: Demonstrates exposing variables as USD attributes for UI customization
* **Behavior Structure**: Provides necessary methods (on\_init, on\_play, on\_update, on\_stop, on\_destroy) for timeline integration
* **Extensibility**: Base behavior classes enable easy extension and reuse in new behaviors
* **Event Integration**: Shows both timeline-based and custom event-based approaches

## Example

Below is an example demonstrating the use of behavior scripts to set up and run synthetic data generation in Isaac Sim. It showcases how to utilize behavior scripts for stacking simulations, texture randomization, light behavior, and camera tracking, ultimately capturing synthetic data with randomized scene configurations.

**Key Highlights of the Example:**

* **Volume Stacking Simulation**: Randomly stack assets using physics simulation to create realistic arrangements.
* **Texture Randomization**: Apply randomized textures to assets for scene diversity.
* **Light and Camera Behaviors**: Add randomization to light properties and make the camera track a specific target.
* **Synthetic Data Capture**: Generate and save synthetic images with the configured behaviors.

**Example Script:**

The demo script can be run directly from the [Script Editor](../development_tools/omniverse_script_editor.html#script-editor):

Behavior script-based SDG script:

```python
import asyncio
import inspect
import os

import isaacsim.core.experimental.utils.semantics as semantics_utils
import numpy as np
import omni.kit.app
import omni.replicator.core as rep
import omni.timeline
import omni.usd
from isaacsim.replicator.behavior.behaviors import (
    LightRandomizer,
    LocationRandomizer,
    LookAtBehavior,
    RotationRandomizer,
    TextureRandomizer,
    VolumeStackRandomizer,
)
from isaacsim.replicator.behavior.global_variables import EXPOSED_ATTR_NS
from isaacsim.replicator.behavior.utils.behavior_utils import (
    add_behavior_script_with_parameters_async,
    publish_event_and_wait_for_completion_async,
)
from isaacsim.storage.native import get_assets_root_path_async
from pxr import Gf, UsdGeom

async def setup_and_run_stacking_simulation_async(prim, seed: int | None = None):
    STACK_ASSETS_CSV = (
        "/Isaac/Environments/Simple_Warehouse/Props/SM_CardBoxC_01.usd,"
        "/Isaac/Environments/Simple_Warehouse/Props/SM_CardBoxD_01.usd,"
        "/Isaac/Props/KLT_Bin/small_KLT_visual.usd,"
    )

    # Add the behavior script with custom parameters
    script_path = inspect.getfile(VolumeStackRandomizer)
    parameters = {
        f"{EXPOSED_ATTR_NS}:{VolumeStackRandomizer.BEHAVIOR_NS}:assets:csv": STACK_ASSETS_CSV,
        f"{EXPOSED_ATTR_NS}:{VolumeStackRandomizer.BEHAVIOR_NS}:assets:numRange": Gf.Vec2i(2, 5),
        f"{EXPOSED_ATTR_NS}:{VolumeStackRandomizer.BEHAVIOR_NS}:renderSimulation": False,
    }
    if seed is not None:
        parameters[f"{EXPOSED_ATTR_NS}:{VolumeStackRandomizer.BEHAVIOR_NS}:seed"] = seed
    await add_behavior_script_with_parameters_async(prim, script_path, parameters)

    # Helper function to handle publishing and waiting for events
    async def handle_event(action, expected_state, max_wait):
        return await publish_event_and_wait_for_completion_async(
            publish_payload={"prim_path": prim.GetPath(), "action": action},
            expected_payload={"prim_path": prim.GetPath(), "state_name": expected_state},
            publish_event_name=VolumeStackRandomizer.EVENT_NAME_IN,
            subscribe_event_name=VolumeStackRandomizer.EVENT_NAME_OUT,
            max_wait_updates=max_wait,
        )

    # Define and execute the stacking simulation steps
    actions = [("reset", "RESET", 10), ("setup", "SETUP", 500), ("run", "FINISHED", 10000)]
    for action, state, wait in actions:
        print(f"Executing '{action}' and waiting for state '{state}'...")
        if not await handle_event(action, state, wait):
            print(f"Failed to complete '{action}' with state '{state}'.")
            if action == "run":
                print("Requesting reset before continuing.")
                await handle_event("reset", "RESET", 2000)
            return

    print("Stacking simulation finished.")

async def setup_texture_randomizer_async(prim, seed: int | None = None):
    TEXTURE_ASSETS_CSV = (
        "/Isaac/Materials/Textures/Patterns/nv_bamboo_desktop.jpg,"
        "/Isaac/Materials/Textures/Patterns/nv_wood_boards_brown.jpg,"
        "/Isaac/Materials/Textures/Patterns/nv_wooden_wall.jpg,"
    )

    script_path = inspect.getfile(TextureRandomizer)
    parameters = {
        f"{EXPOSED_ATTR_NS}:{TextureRandomizer.BEHAVIOR_NS}:interval": 5,
        f"{EXPOSED_ATTR_NS}:{TextureRandomizer.BEHAVIOR_NS}:textures:csv": TEXTURE_ASSETS_CSV,
    }
    if seed is not None:
        parameters[f"{EXPOSED_ATTR_NS}:{TextureRandomizer.BEHAVIOR_NS}:seed"] = seed
    await add_behavior_script_with_parameters_async(prim, script_path, parameters)

async def setup_light_behaviors_async(prim, light_seed: int | None = None, location_seed: int | None = None):
    # Light randomization
    light_script_path = inspect.getfile(LightRandomizer)
    light_parameters = {
        f"{EXPOSED_ATTR_NS}:{LightRandomizer.BEHAVIOR_NS}:interval": 4,
        f"{EXPOSED_ATTR_NS}:{LightRandomizer.BEHAVIOR_NS}:range:intensity": Gf.Vec2f(20000, 120000),
    }
    if light_seed is not None:
        light_parameters[f"{EXPOSED_ATTR_NS}:{LightRandomizer.BEHAVIOR_NS}:seed"] = light_seed
    await add_behavior_script_with_parameters_async(prim, light_script_path, light_parameters)

    # Location randomization
    location_script_path = inspect.getfile(LocationRandomizer)
    location_parameters = {
        f"{EXPOSED_ATTR_NS}:{LocationRandomizer.BEHAVIOR_NS}:interval": 2,
        f"{EXPOSED_ATTR_NS}:{LocationRandomizer.BEHAVIOR_NS}:range:minPosition": Gf.Vec3d(-1.25, -1.25, 0.0),
        f"{EXPOSED_ATTR_NS}:{LocationRandomizer.BEHAVIOR_NS}:range:maxPosition": Gf.Vec3d(1.25, 1.25, 0.0),
    }
    if location_seed is not None:
        location_parameters[f"{EXPOSED_ATTR_NS}:{LocationRandomizer.BEHAVIOR_NS}:seed"] = location_seed
    await add_behavior_script_with_parameters_async(prim, location_script_path, location_parameters)

async def setup_target_asset_behaviors_async(prim, rotation_seed: int | None = None, location_seed: int | None = None):
    # Rotation randomization
    rotation_script_path = inspect.getfile(RotationRandomizer)
    rotation_parameters = {}
    if rotation_seed is not None:
        rotation_parameters[f"{EXPOSED_ATTR_NS}:{RotationRandomizer.BEHAVIOR_NS}:seed"] = rotation_seed
    await add_behavior_script_with_parameters_async(prim, rotation_script_path, rotation_parameters)

    # Location randomization
    location_script_path = inspect.getfile(LocationRandomizer)
    location_parameters = {
        f"{EXPOSED_ATTR_NS}:{LocationRandomizer.BEHAVIOR_NS}:interval": 3,
        f"{EXPOSED_ATTR_NS}:{LocationRandomizer.BEHAVIOR_NS}:range:minPosition": Gf.Vec3d(-0.2, -0.2, -0.2),
        f"{EXPOSED_ATTR_NS}:{LocationRandomizer.BEHAVIOR_NS}:range:maxPosition": Gf.Vec3d(0.2, 0.2, 0.2),
    }
    if location_seed is not None:
        location_parameters[f"{EXPOSED_ATTR_NS}:{LocationRandomizer.BEHAVIOR_NS}:seed"] = location_seed
    await add_behavior_script_with_parameters_async(prim, location_script_path, location_parameters)

async def setup_camera_behaviors_async(prim, target_prim_path):
    # Look at behavior following the target asset
    script_path = inspect.getfile(LookAtBehavior)
    parameters = {
        f"{EXPOSED_ATTR_NS}:{LookAtBehavior.BEHAVIOR_NS}:targetPrimPath": target_prim_path,
    }
    await add_behavior_script_with_parameters_async(prim, script_path, parameters)

async def setup_writer_and_capture_data_async(camera_path, num_captures):
    # Create the writer and the render product
    rp = rep.create.render_product(camera_path, (512, 512))
    writer = rep.writers.get("BasicWriter")
    output_directory = os.path.join(os.getcwd(), "_out_behaviors_sdg")
    print(f"output_directory: {output_directory}")
    writer.initialize(output_dir=output_directory, rgb=True, distance_to_image_plane=True, colorize_depth=True)
    writer.attach(rp)

    # Disable capture on play, data is captured manually using the step function
    rep.orchestrator.set_capture_on_play(False)

    # Use the timeline to control the behavior scripts execution and frame captures
    timeline = omni.timeline.get_timeline_interface()

    # Start the SDG pipeline
    for i in range(num_captures):
        # Advance the timeline with one update and then pause it to avoid triggering the behavior scripts by the step_async internal updates
        timeline.play()
        await omni.kit.app.get_app().next_update_async()
        timeline.pause()
        timeline.commit()

        # Capture the frame
        print(f"Capturing frame {i} at time {timeline.get_current_time():.4f}")
        await rep.orchestrator.step_async(rt_subframes=32, delta_time=0.0)

    # Stop the timeline (and trigger the behavior scripts to stop)
    timeline.stop()
    await omni.kit.app.get_app().next_update_async()

    # Make sure all the frames are written from the backend queue and free the rendering resources
    await rep.orchestrator.wait_until_complete_async()
    writer.detach()
    rp.destroy()

async def run_example_async(num_captures, seed: int | None = None):
    STAGE_URL = "/Isaac/Samples/Replicator/Stage/warehouse_pallets_behavior_scripts.usd"
    PALLETS_ROOT_PATH = "/Root/Pallets"
    LIGHTS_ROOT_PATH = "/Root/Lights"
    CAMERA_PATH = "/Root/Camera_01"
    TARGET_ASSET_URL = "/Isaac/Props/YCB/Axis_Aligned/035_power_drill.usd"
    TARGET_ASSET_PATH = "/Root/Target"
    TARGET_ASSET_LABEL = "power_drill"
    TARGET_ASSET_LOCATION = (-1.5, 5.5, 1.5)

    # Generate unique seeds per behavior instance to ensure determinism regardless of execution order
    if seed is not None:
        seed_rng = np.random.default_rng(seed)
        stacking_seed = int(seed_rng.integers(0, 2**31))
        texture_seed = int(seed_rng.integers(0, 2**31))
        light_intensity_seed = int(seed_rng.integers(0, 2**31))
        light_location_seed = int(seed_rng.integers(0, 2**31))
        target_rotation_seed = int(seed_rng.integers(0, 2**31))
        target_location_seed = int(seed_rng.integers(0, 2**31))
    else:
        stacking_seed = texture_seed = None
        light_intensity_seed = light_location_seed = None
        target_rotation_seed = target_location_seed = None

    # Open stage
    assets_root_path = await get_assets_root_path_async()
    print(f"Opening stage from {assets_root_path + STAGE_URL}")
    await omni.usd.get_context().open_stage_async(assets_root_path + STAGE_URL)
    stage = omni.usd.get_context().get_stage()

    # Check if all required prims exist in the stage
    pallets_root_prim = stage.GetPrimAtPath(PALLETS_ROOT_PATH)
    lights_root_prim = stage.GetPrimAtPath(LIGHTS_ROOT_PATH)
    camera_prim = stage.GetPrimAtPath(CAMERA_PATH)
    if not all([pallets_root_prim.IsValid(), lights_root_prim.IsValid(), camera_prim.IsValid()]):
        print(f"Not all required prims exist in the stage.")
        return

    # Spawn the target asset at the requested location, label it with the target asset label
    target_prim = stage.DefinePrim(TARGET_ASSET_PATH, "Xform")
    target_prim.GetReferences().AddReference(assets_root_path + TARGET_ASSET_URL)
    if not target_prim.HasAttribute("xformOp:translate"):
        UsdGeom.Xformable(target_prim).AddTranslateOp()
    target_prim.GetAttribute("xformOp:translate").Set(TARGET_ASSET_LOCATION)
    semantics_utils.remove_all_labels(target_prim, include_descendants=True)
    semantics_utils.add_labels(target_prim, labels=[TARGET_ASSET_LABEL], taxonomy="class")

    # Setup and run the stacking simulation before capturing the data
    # Note: Physics simulation is non-deterministic, final positions may vary
    await setup_and_run_stacking_simulation_async(pallets_root_prim, seed=stacking_seed)

    # Setup texture randomizer
    await setup_texture_randomizer_async(pallets_root_prim, seed=texture_seed)

    # Setup the light behaviors
    await setup_light_behaviors_async(
        lights_root_prim, light_seed=light_intensity_seed, location_seed=light_location_seed
    )

    # Setup the target asset behaviors
    await setup_target_asset_behaviors_async(
        target_prim, rotation_seed=target_rotation_seed, location_seed=target_location_seed
    )

    # Setup the camera behaviors
    await setup_camera_behaviors_async(camera_prim, str(target_prim.GetPath()))

    # Setup the writer and capture the data, behavior scripts are triggered by running the timeline
    await setup_writer_and_capture_data_async(camera_path=camera_prim.GetPath(), num_captures=num_captures)

asyncio.ensure_future(run_example_async(num_captures=6))
```

On this page

* [Overview](#overview)
  + [Learning Objectives](#learning-objectives)
  + [Prerequisites](#prerequisites)
  + [Demonstration](#demonstration)
  + [Behavior scripts](#behavior-scripts)
  + [Exposing variables through USD attributes](#exposing-variables-through-usd-attributes)
    - [Core and UI extension split](#core-and-ui-extension-split)
  + [Custom event-based behavior scripts](#custom-event-based-behavior-scripts)
* [Script Examples](#script-examples)
  + [Location Randomizer](#location-randomizer)
  + [Rotation Randomizer](#rotation-randomizer)
  + [Look At Behavior](#look-at-behavior)
  + [Light Randomizer](#light-randomizer)
  + [Texture Randomizer](#texture-randomizer)
  + [Volume Stack Randomizer](#volume-stack-randomizer)
  + [Templates](#templates)
* [Example](#example)

---

### Isaac Snippets

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/replicator_tutorials/tutorial_replicator_isaac_snippets.html

* [Synthetic Data Generation](../synthetic_data_generation/index.html)
* [Perception Data Generation (Replicator)](index.html)
* Useful Snippets

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Useful Snippets

Various examples of Isaac Sim Replicator snippets that can be run as [Standalone Applications](../introduction/workflows.html#standalone-application) or from the UI using the [Script Editor](../development_tools/omniverse_script_editor.html#script-editor).

## Annotator and Custom Writer Data from Multiple Cameras

Example on how to access data from multiple cameras in a scene using annotators or custom writers. The standalone example can also be run directly (on Windows use `python.bat` instead of `python.sh`):

```python
./python.sh standalone_examples/api/isaacsim.replicator.examples/multi_camera.py
```

Script Editor

Annotator and Custom Writer Data from Multiple Cameras

```python
import asyncio
import os

import carb.settings
import omni.replicator.core as rep
import omni.usd
from omni.replicator.core import Writer
from omni.replicator.core.backends import DiskBackend
from omni.replicator.core.functional import write_image

NUM_FRAMES = 5

# Randomize cube color every frame using a graph-based replicator randomizer
def cube_color_randomizer():
    cube_prims = rep.get.prims(path_pattern="Cube")
    with cube_prims:
        rep.randomizer.color(colors=rep.distribution.uniform((0, 0, 0), (1, 1, 1)))
    return cube_prims.node

# Example of custom writer class to access the annotator data
class MyWriter(Writer):
    def __init__(self, rgb: bool = True):
        # Organize data from render product perspective (legacy, annotator, renderProduct)
        self.data_structure = "renderProduct"
        self.annotators = []
        self._frame_id = 0
        if rgb:
            # Create a new rgb annotator and add it to the writer's list of annotators
            self.annotators.append(rep.annotators.get("rgb"))
        # Create writer output directory and initialize DiskBackend
        output_dir = os.path.join(os.getcwd(), "_out_mc_writer")
        print(f"Writing writer data to {output_dir}")
        self.backend = DiskBackend(output_dir=output_dir, overwrite=True)

    def write(self, data):
        if "renderProducts" in data:
            for rp_name, rp_data in data["renderProducts"].items():
                if "rgb" in rp_data:
                    file_path = f"{rp_name}_frame_{self._frame_id}.png"
                    self.backend.schedule(write_image, data=rp_data["rgb"]["data"], path=file_path)
        self._frame_id += 1

rep.WriterRegistry.register(MyWriter)

# Create a new stage
omni.usd.get_context().new_stage()

# Set global random seed for the replicator randomizer
rep.set_global_seed(11)

# Disable capture on play to capture data manually using step
rep.orchestrator.set_capture_on_play(False)

# Set DLSS to Quality mode (2) for best SDG results , options: 0 (Performance), 1 (Balanced), 2 (Quality), 3 (Auto)
carb.settings.get_settings().set("rtx/post/dlss/execMode", 2)

# Setup stage
rep.functional.create.xform(name="World")
rep.functional.create.dome_light(intensity=900, parent="/World", name="DomeLight")
cube = rep.functional.create.cube(parent="/World", name="Cube", semantics={"class": "my_cube"})

# Register the graph-based cube color randomizer to trigger on every frame
rep.randomizer.register(cube_color_randomizer)
with rep.trigger.on_frame():
    rep.randomizer.cube_color_randomizer()

# Create cameras
cam_top = rep.functional.create.camera(position=(0, 0, 5), look_at=(0, 0, 0), parent="/World", name="CamTop")
cam_side = rep.functional.create.camera(position=(2, 2, 0), look_at=(0, 0, 0), parent="/World", name="CamSide")
cam_persp = rep.functional.create.camera(position=(5, 5, 5), look_at=(0, 0, 0), parent="/World", name="CamPersp")

# Create the render products
rp_top = rep.create.render_product(cam_top, resolution=(320, 320), name="RpTop")
rp_side = rep.create.render_product(cam_side, resolution=(640, 640), name="RpSide")
rp_persp = rep.create.render_product(cam_persp, resolution=(1024, 1024), name="RpPersp")

# Example of accessing the data through a custom writer
writer = rep.WriterRegistry.get("MyWriter")
writer.initialize(rgb=True)
writer.attach([rp_top, rp_side, rp_persp])

# Example of accessing the data directly through annotators
rgb_annotators = []
for rp in [rp_top, rp_side, rp_persp]:
    # Create a new rgb annotator for each render product
    rgb = rep.annotators.get("rgb")
    # Attach the annotator to the render product
    rgb.attach(rp)
    rgb_annotators.append(rgb)

# Create annotator output directory
output_dir_annot = os.path.join(os.getcwd(), "_out_mc_annot")
print(f"Writing annotator data to {output_dir_annot}")
os.makedirs(output_dir_annot, exist_ok=True)

async def run_example_async():
    for i in range(NUM_FRAMES):
        print(f"Step {i}")
        # The step function triggers registered graph-based randomizers, collects data from annotators,
        # and invokes the write function of attached writers with the annotator data
        await rep.orchestrator.step_async(rt_subframes=32)
        for j, rgb_annot in enumerate(rgb_annotators):
            file_path = os.path.join(output_dir_annot, f"rp{j}_step_{i}.png")
            write_image(path=file_path, data=rgb_annot.get_data())

    # Wait for the data to be written and release resources
    await rep.orchestrator.wait_until_complete_async()
    writer.detach()
    for annot in rgb_annotators:
        annot.detach()
    for rp in [rp_top, rp_side, rp_persp]:
        rp.destroy()

asyncio.ensure_future(run_example_async())
```

Standalone Application

Annotator and Custom Writer Data from Multiple Cameras

```python
"""Demonstrate multi-camera data capture with custom writers and annotators."""

from isaacsim import SimulationApp

simulation_app = SimulationApp(launch_config={"headless": False})

import os

import carb.settings
import omni.replicator.core as rep
import omni.usd
from omni.replicator.core import Writer
from omni.replicator.core.backends import DiskBackend
from omni.replicator.core.functional import write_image

NUM_FRAMES = 5

def cube_color_randomizer():
    """Randomize cube color every frame using a graph-based replicator randomizer."""
    cube_prims = rep.get.prims(path_pattern="Cube")
    with cube_prims:
        rep.randomizer.color(colors=rep.distribution.uniform((0, 0, 0), (1, 1, 1)))
    return cube_prims.node

class MyWriter(Writer):
    """Write RGB annotator data to disk from multiple render products."""

    def __init__(self, rgb: bool = True):
        # Organize data from render product perspective (legacy, annotator, renderProduct)
        self.data_structure = "renderProduct"
        self.annotators = []
        self._frame_id = 0
        if rgb:
            # Create a new rgb annotator and add it to the writer's list of annotators
            self.annotators.append(rep.annotators.get("rgb"))
        # Create writer output directory and initialize DiskBackend
        output_dir = os.path.join(os.getcwd(), "_out_mc_writer")
        print(f"Writing writer data to {output_dir}")
        self.backend = DiskBackend(output_dir=output_dir, overwrite=True)

    def write(self, data):
        """Write RGB frames from each render product to disk."""
        if "renderProducts" in data:
            for rp_name, rp_data in data["renderProducts"].items():
                if "rgb" in rp_data:
                    file_path = f"{rp_name}_frame_{self._frame_id}.png"
                    self.backend.schedule(write_image, data=rp_data["rgb"]["data"], path=file_path)
        self._frame_id += 1

rep.WriterRegistry.register(MyWriter)

# Create a new stage
omni.usd.get_context().new_stage()

# Set global random seed for the replicator randomizer
rep.set_global_seed(11)

# Disable capture on play to capture data manually using step
rep.orchestrator.set_capture_on_play(False)

# Set DLSS to Quality mode (2) for best SDG results , options: 0 (Performance), 1 (Balanced), 2 (Quality), 3 (Auto)
carb.settings.get_settings().set("rtx/post/dlss/execMode", 2)

# Setup stage
rep.functional.create.xform(name="World")
rep.functional.create.dome_light(intensity=900, parent="/World", name="DomeLight")
cube = rep.functional.create.cube(parent="/World", name="Cube", semantics={"class": "my_cube"})

# Register the graph-based cube color randomizer to trigger on every frame
rep.randomizer.register(cube_color_randomizer)
with rep.trigger.on_frame():
    rep.randomizer.cube_color_randomizer()

# Create cameras
cam_top = rep.functional.create.camera(position=(0, 0, 5), look_at=(0, 0, 0), parent="/World", name="CamTop")
cam_side = rep.functional.create.camera(position=(2, 2, 0), look_at=(0, 0, 0), parent="/World", name="CamSide")
cam_persp = rep.functional.create.camera(position=(5, 5, 5), look_at=(0, 0, 0), parent="/World", name="CamPersp")

# Create the render products
rp_top = rep.create.render_product(cam_top, resolution=(320, 320), name="RpTop")
rp_side = rep.create.render_product(cam_side, resolution=(640, 640), name="RpSide")
rp_persp = rep.create.render_product(cam_persp, resolution=(1024, 1024), name="RpPersp")

# Example of accessing the data through a custom writer
writer = rep.WriterRegistry.get("MyWriter")
writer.initialize(rgb=True)
writer.attach([rp_top, rp_side, rp_persp])

# Example of accessing the data directly through annotators
rgb_annotators = []
for rp in [rp_top, rp_side, rp_persp]:
    # Create a new rgb annotator for each render product
    rgb = rep.annotators.get("rgb")
    # Attach the annotator to the render product
    rgb.attach(rp)
    rgb_annotators.append(rgb)

# Create annotator output directory
output_dir_annot = os.path.join(os.getcwd(), "_out_mc_annot")
print(f"Writing annotator data to {output_dir_annot}")
os.makedirs(output_dir_annot, exist_ok=True)

for i in range(NUM_FRAMES):
    print(f"Step {i}")
    # The step function triggers registered graph-based randomizers, collects data from annotators,
    # and invokes the write function of attached writers with the annotator data
    rep.orchestrator.step(rt_subframes=32)
    for j, rgb_annot in enumerate(rgb_annotators):
        file_path = os.path.join(output_dir_annot, f"rp{j}_step_{i}.png")
        write_image(path=file_path, data=rgb_annot.get_data())

# Wait for the data to be written and release resources
rep.orchestrator.wait_until_complete()
writer.detach()
for annot in rgb_annotators:
    annot.detach()
for rp in [rp_top, rp_side, rp_persp]:
    rp.destroy()
```

## Synthetic Data Access at Specific Simulation Timepoints

Example on how to access synthetic data (RGB, semantic segmentation) from multiple cameras in a simulation scene at specific events using annotators or writers. The standalone example can also be run directly (on Windows use `python.bat` instead of `python.sh`):

```python
./python.sh standalone_examples/api/isaacsim.replicator.examples/simulation_get_data.py
```

Script Editor

Synthetic Data Access at Specific Simulation Timepoints

```python
import asyncio
import json
import os

import carb.settings
import numpy as np
import omni
import omni.replicator.core as rep
from isaacsim.core.experimental.objects import GroundPlane
from isaacsim.core.simulation_manager import SimulationManager
from omni.replicator.core.functional import write_image, write_json
from pxr import UsdPhysics

# Util function to save semantic segmentation annotator data
def write_sem_data(sem_data, file_path):
    id_to_labels = sem_data["info"]["idToLabels"]
    write_json(path=file_path + ".json", data=id_to_labels)
    sem_image_data = sem_data["data"]
    write_image(path=file_path + ".png", data=sem_image_data)

# Create a new stage
omni.usd.get_context().new_stage()

# Setting capture on play to False will prevent the replicator from capturing data each frame
rep.orchestrator.set_capture_on_play(False)

# Set DLSS to Quality mode (2) for best SDG results , options: 0 (Performance), 1 (Balanced), 2 (Quality), 3 (Auto)
carb.settings.get_settings().set("rtx/post/dlss/execMode", 2)

# Add a dome light and a ground plane
rep.functional.create.xform(name="World")
rep.functional.create.dome_light(intensity=500, parent="/World", name="DomeLight")
ground_plane = GroundPlane("/World/GroundPlane")
rep.functional.modify.semantics(ground_plane.prims, {"class": "ground_plane"}, mode="add")

# Create a camera and render product to collect the data from
rep.functional.create.xform(name="World")
cam = rep.functional.create.camera(position=(5, 5, 5), look_at=(0, 0, 0), parent="/World", name="Camera")
rp = rep.create.render_product(cam, resolution=(512, 512), name="MyRenderProduct")

# Set the output directory for the data
out_dir = os.path.join(os.getcwd(), "_out_sim_event")
writer_dir = os.path.join(out_dir, "writer")
annotator_dir = os.path.join(out_dir, "annotator")

os.makedirs(out_dir, exist_ok=True)
os.makedirs(writer_dir, exist_ok=True)
os.makedirs(annotator_dir, exist_ok=True)

print(f"Outputting data to {out_dir}..")
backend = rep.backends.get("DiskBackend")
backend.initialize(output_dir=writer_dir)

# Example of using a writer to save the data
writer = rep.WriterRegistry.get("BasicWriter")
writer.initialize(backend=backend, rgb=True, semantic_segmentation=True, colorize_semantic_segmentation=True)
writer.attach(rp)

# Example of accesing the data directly from annotators
rgb_annot = rep.AnnotatorRegistry.get_annotator("rgb")
rgb_annot.attach(rp)
sem_annot = rep.AnnotatorRegistry.get_annotator("semantic_segmentation", init_params={"colorize": True})
sem_annot.attach(rp)

# Initialize the simulation manager
SimulationManager.initialize_physics()

async def run_example_async():
    # Spawn and drop a few cubes, capture data when they stop moving
    for i in range(5):
        cube = rep.functional.create.cube(name=f"Cuboid_{i}", parent="/World")
        rep.functional.modify.position(cube, (0, 0, 10 + i))
        rep.functional.modify.semantics(cube, {"class": "cuboid"}, mode="add")
        rep.functional.physics.apply_rigid_body(cube, with_collider=True)
        physics_rigid_body_api = UsdPhysics.RigidBodyAPI(cube)

        for s in range(500):
            SimulationManager.step()
            linear_velocity = physics_rigid_body_api.GetVelocityAttr().Get()
            speed = np.linalg.norm(linear_velocity)

            if speed < 0.1:
                print(f"Cube_{i} stopped moving after {s} simulation steps, writing data..")
                # Tigger the writer and update the annotators with new data
                await rep.orchestrator.step_async(rt_subframes=4, delta_time=0.0, pause_timeline=False)
                rgb_path = os.path.join(annotator_dir, f"Cube_{i}_step_{s}_rgb.png")
                sem_path = os.path.join(annotator_dir, f"Cube_{i}_step_{s}_sem")
                write_image(path=rgb_path, data=rgb_annot.get_data())
                write_sem_data(sem_annot.get_data(), sem_path)
                break

    # Wait for the data to be written to disk and clean up resources
    await rep.orchestrator.wait_until_complete_async()
    rgb_annot.detach()
    sem_annot.detach()
    writer.detach()
    rp.destroy()

asyncio.ensure_future(run_example_async())
```

Standalone Application

Synthetic Data Access at Specific Simulation Timepoints

```python
"""Demonstrate simulation-event-driven data capture with writers and annotators."""

from isaacsim import SimulationApp

simulation_app = SimulationApp(launch_config={"headless": False})

import os

import carb.settings
import numpy as np
import omni
import omni.replicator.core as rep
from isaacsim.core.experimental.objects import GroundPlane
from isaacsim.core.simulation_manager import SimulationManager
from omni.replicator.core.functional import write_image, write_json
from pxr import UsdPhysics

def write_sem_data(sem_data, file_path):
    """Save semantic segmentation data as JSON labels and PNG image."""
    id_to_labels = sem_data["info"]["idToLabels"]
    write_json(path=file_path + ".json", data=id_to_labels)
    sem_image_data = sem_data["data"]
    write_image(path=file_path + ".png", data=sem_image_data)

# Create a new stage
omni.usd.get_context().new_stage()

# Setting capture on play to False will prevent the replicator from capturing data each frame
rep.orchestrator.set_capture_on_play(False)

# Set DLSS to Quality mode (2) for best SDG results , options: 0 (Performance), 1 (Balanced), 2 (Quality), 3 (Auto)
carb.settings.get_settings().set("rtx/post/dlss/execMode", 2)

# Add a dome light and a ground plane
rep.functional.create.xform(name="World")
rep.functional.create.dome_light(intensity=500, parent="/World", name="DomeLight")
ground_plane = GroundPlane("/World/GroundPlane")
rep.functional.modify.semantics(ground_plane.prims, {"class": "ground_plane"}, mode="add")

# Create a camera and render product to collect the data from
cam = rep.functional.create.camera(position=(5, 5, 5), look_at=(0, 0, 0), parent="/World", name="Camera")
rp = rep.create.render_product(cam, resolution=(512, 512), name="MyRenderProduct")

# Set the output directory for the data
out_dir = os.path.join(os.getcwd(), "_out_sim_event")
writer_dir = os.path.join(out_dir, "writer")
annotator_dir = os.path.join(out_dir, "annotator")

os.makedirs(out_dir, exist_ok=True)
os.makedirs(writer_dir, exist_ok=True)
os.makedirs(annotator_dir, exist_ok=True)

print(f"Outputting data to {out_dir}..")
backend = rep.backends.get("DiskBackend")
backend.initialize(output_dir=writer_dir)

# Example of using a writer to save the data
writer = rep.WriterRegistry.get("BasicWriter")
writer.initialize(backend=backend, rgb=True, semantic_segmentation=True, colorize_semantic_segmentation=True)
writer.attach(rp)

# Example of accesing the data directly from annotators
rgb_annot = rep.AnnotatorRegistry.get_annotator("rgb")
rgb_annot.attach(rp)
sem_annot = rep.AnnotatorRegistry.get_annotator("semantic_segmentation", init_params={"colorize": True})
sem_annot.attach(rp)

# Initialize the simulation manager
SimulationManager.initialize_physics()

# Spawn and drop a few cubes, capture data when they stop moving
for i in range(5):
    cube = rep.functional.create.cube(name=f"Cuboid_{i}", parent="/World")
    rep.functional.modify.position(cube, (0, 0, 10 + i))
    rep.functional.modify.semantics(cube, {"class": "cuboid"}, mode="add")
    rep.functional.physics.apply_rigid_body(cube, with_collider=True)
    physics_rigid_body_api = UsdPhysics.RigidBodyAPI(cube)

    for s in range(500):
        SimulationManager.step()
        linear_velocity = physics_rigid_body_api.GetVelocityAttr().Get()
        speed = np.linalg.norm(linear_velocity)

        if speed < 0.1:
            print(f"Cube_{i} stopped moving after {s} simulation steps, writing data..")
            # Tigger the writer and update the annotators with new data
            rep.orchestrator.step(rt_subframes=4, delta_time=0.0, pause_timeline=False)
            rgb_path = os.path.join(annotator_dir, f"Cube_{i}_step_{s}_rgb.png")
            write_image(path=rgb_path, data=rgb_annot.get_data())
            sem_path = os.path.join(annotator_dir, f"Cube_{i}_step_{s}_sem")
            write_sem_data(sem_annot.get_data(), sem_path)
            break

# Wait for the data to be written to disk and clean up resources
rep.orchestrator.wait_until_complete()
rgb_annot.detach()
sem_annot.detach()
writer.detach()
rp.destroy()
```

## Custom Event Randomization and Writing

The following example showcases the use of custom events to trigger randomizations and data writing at various times throughout the simulation. The standalone example can also be run directly (on Windows use `python.bat` instead of `python.sh`):

```python
./python.sh standalone_examples/api/isaacsim.replicator.examples/custom_event_and_write.py
```

Script Editor

Custom Event Randomization and Writing

```python
import asyncio
import os

import carb.settings
import omni.replicator.core as rep
import omni.usd

omni.usd.get_context().new_stage()

# Set global random seed for the replicator randomizer to ensure reproducibility
rep.set_global_seed(11)

# Setting capture on play to False will prevent the replicator from capturing data each frame
rep.orchestrator.set_capture_on_play(False)

# Set DLSS to Quality mode (2) for best SDG results , options: 0 (Performance), 1 (Balanced), 2 (Quality), 3 (Auto)
carb.settings.get_settings().set("rtx/post/dlss/execMode", 2)

rep.functional.create.xform(name="World")
rep.functional.create.distant_light(intensity=4000, rotation=(315, 0, 0), parent="/World", name="DistantLight")
small_cube = rep.functional.create.cube(scale=0.75, position=(-1.5, 1.5, 0), parent="/World", name="SmallCube")
large_cube = rep.functional.create.cube(scale=1.25, position=(1.5, -1.5, 0), parent="/World", name="LargeCube")

# Graph-based randomizations triggered on custom events
with rep.trigger.on_custom_event(event_name="randomize_small_cube"):
    small_cube_node = rep.get.prim_at_path(small_cube.GetPath())
    with small_cube_node:
        rep.randomizer.rotation()

with rep.trigger.on_custom_event(event_name="randomize_large_cube"):
    large_cube_node = rep.get.prim_at_path(large_cube.GetPath())
    with large_cube_node:
        rep.randomizer.rotation()

# Use the disk backend to write the data to disk
out_dir = os.path.join(os.getcwd(), "_out_custom_event")
print(f"Writing data to {out_dir}")
backend = rep.backends.get("DiskBackend")
backend.initialize(output_dir=out_dir)

cam = rep.functional.create.camera(position=(5, 5, 5), look_at=(0, 0, 0), parent="/World", name="Camera")
rp = rep.create.render_product(cam, (512, 512))
writer = rep.WriterRegistry.get("BasicWriter")
writer.initialize(backend=backend, rgb=True)
writer.attach(rp)

async def run_example_async():
    print(f"Capturing at original positions")
    await rep.orchestrator.step_async(rt_subframes=8)

    print("Randomizing small cube rotation (graph-based) and capturing...")
    rep.utils.send_og_event(event_name="randomize_small_cube")
    await rep.orchestrator.step_async(rt_subframes=8)

    print("Moving small cube position (USD API) and capturing...")
    small_cube.GetAttribute("xformOp:translate").Set((-1.5, 1.5, -2))
    await rep.orchestrator.step_async(rt_subframes=8)

    print("Randomizing large cube rotation (graph-based) and capturing...")
    rep.utils.send_og_event(event_name="randomize_large_cube")
    await rep.orchestrator.step_async(rt_subframes=8)

    print("Moving large cube position (USD API) and capturing...")
    large_cube.GetAttribute("xformOp:translate").Set((1.5, -1.5, 2))
    await rep.orchestrator.step_async(rt_subframes=8)

    # Wait until all the data is saved to disk and cleanup writer and render product
    await rep.orchestrator.wait_until_complete_async()
    writer.detach()
    rp.destroy()

asyncio.ensure_future(run_example_async())
```

Standalone Application

Custom Event Randomization and Writing

```python
"""Demonstrate custom event-triggered randomization and data capture."""

from isaacsim import SimulationApp

simulation_app = SimulationApp(launch_config={"headless": False})

import os

import carb.settings
import omni.replicator.core as rep
import omni.usd

omni.usd.get_context().new_stage()

# Set global random seed for the replicator randomizer to ensure reproducibility
rep.set_global_seed(11)

# Setting capture on play to False will prevent the replicator from capturing data each frame
rep.orchestrator.set_capture_on_play(False)

# Set DLSS to Quality mode (2) for best SDG results , options: 0 (Performance), 1 (Balanced), 2 (Quality), 3 (Auto)
carb.settings.get_settings().set("rtx/post/dlss/execMode", 2)

rep.functional.create.xform(name="World")
rep.functional.create.distant_light(intensity=4000, rotation=(315, 0, 0), parent="/World", name="DistantLight")
small_cube = rep.functional.create.cube(scale=0.75, position=(-1.5, 1.5, 0), parent="/World", name="SmallCube")
large_cube = rep.functional.create.cube(scale=1.25, position=(1.5, -1.5, 0), parent="/World", name="LargeCube")

# Graph-based randomizations triggered on custom events
with rep.trigger.on_custom_event(event_name="randomize_small_cube"):
    small_cube_node = rep.get.prim_at_path(small_cube.GetPath())
    with small_cube_node:
        rep.randomizer.rotation()

with rep.trigger.on_custom_event(event_name="randomize_large_cube"):
    large_cube_node = rep.get.prim_at_path(large_cube.GetPath())
    with large_cube_node:
        rep.randomizer.rotation()

# Use the disk backend to write the data to disk
out_dir = os.path.join(os.getcwd(), "_out_custom_event")
print(f"Writing data to {out_dir}")
backend = rep.backends.get("DiskBackend")
backend.initialize(output_dir=out_dir)

cam = rep.functional.create.camera(position=(5, 5, 5), look_at=(0, 0, 0), parent="/World", name="Camera")
rp = rep.create.render_product(cam, (512, 512))
writer = rep.WriterRegistry.get("BasicWriter")
writer.initialize(backend=backend, rgb=True)
writer.attach(rp)

def run_example():
    """Run custom event randomization and capture sequence."""
    print(f"Capturing at original positions")
    rep.orchestrator.step(rt_subframes=8)

    print("Randomizing small cube rotation (graph-based) and capturing...")
    rep.utils.send_og_event(event_name="randomize_small_cube")
    rep.orchestrator.step(rt_subframes=8)

    print("Moving small cube position (USD API) and capturing...")
    small_cube.GetAttribute("xformOp:translate").Set((-1.5, 1.5, -2))
    rep.orchestrator.step(rt_subframes=8)

    print("Randomizing large cube rotation (graph-based) and capturing...")
    rep.utils.send_og_event(event_name="randomize_large_cube")
    rep.orchestrator.step(rt_subframes=8)

    print("Moving large cube position (USD API) and capturing...")
    large_cube.GetAttribute("xformOp:translate").Set((1.5, -1.5, 2))
    rep.orchestrator.step(rt_subframes=8)

    # Wait until all the data is saved to disk and cleanup writer and render product
    rep.orchestrator.wait_until_complete()
    writer.detach()
    rp.destroy()

run_example()
```

## Motion Blur

This example demonstrates how to capture motion blur data using [RTX Real-Time](https://docs.omniverse.nvidia.com/materials-and-rendering/latest/rtx-renderer_rt.html) and [RTX Interactive (Path Tracing)](https://docs.omniverse.nvidia.com/materials-and-rendering/latest/rtx-renderer_pt.html) rendering modes. For the RTX - Real-Time mode, refer to [motion blur parameters](https://docs.omniverse.nvidia.com/materials-and-rendering/latest/rtx_post-processing.html#motion-blur). For the RTX – Interactive (Path Tracing) mode, motion blur is achieved by rendering multiple subframes (`/omni/replicator/pathTracedMotionBlurSubSamples`) and combining them to create the effect.

The example uses animated and physics-enabled assets with synchronized motion. Keyframe animated assets can be advanced at any custom delta time due to their interpolated motion, whereas physics-enabled assets require a custom physics FPS to ensure motion samples at any custom delta time. The example showcases how to compute the target physics FPS, change it if needed, and restore the original physics FPS after capturing the motion blur.

The standalone example can also be run directly (on Windows use `python.bat` instead of `python.sh`):

```python
./python.sh standalone_examples/api/isaacsim.replicator.examples/motion_blur.py
```

Script Editor

Motion Blur

```python
import asyncio
import os

import carb.settings
import omni.kit.app
import omni.replicator.core as rep
import omni.timeline
import omni.usd
from isaacsim.storage.native import get_assets_root_path
from pxr import PhysxSchema, Sdf, UsdPhysics

# Paths to the animated and physics-ready assets
PHYSICS_ASSET_URL = "/Isaac/Props/YCB/Axis_Aligned_Physics/003_cracker_box.usd"
ANIM_ASSET_URL = "/Isaac/Props/YCB/Axis_Aligned/003_cracker_box.usd"

# -z velocities and start locations of the animated (left side) and physics (right side) assets (stage units/s)
ASSET_VELOCITIES = [0, 5, 10]
ASSET_X_MIRRORED_LOCATIONS = [(0.5, 0, 0.3), (0.3, 0, 0.3), (0.1, 0, 0.3)]

# Used to calculate how many frames to animate the assets to maintain the same velocity as the physics assets
ANIMATION_DURATION = 10

# Number of frames to capture for each scenario
NUM_FRAMES = 3

# Configuration for motion blur examples
DELTA_TIMES = [None, 1 / 30, 1 / 60, 1 / 240]
SAMPLES_PER_PIXEL = [32, 128]
MOTION_BLUR_SUBSAMPLES = [4, 16]

def setup_stage():
    """Create a new USD stage with animated and physics-enabled assets with synchronized motion."""
    omni.usd.get_context().new_stage()
    settings = carb.settings.get_settings()
    # Set DLSS to Quality mode (2) for best SDG results , options: 0 (Performance), 1 (Balanced), 2 (Quality), 3 (Auto)
    settings.set("rtx/post/dlss/execMode", 2)

    # Capture data only on request
    rep.orchestrator.set_capture_on_play(False)

    stage = omni.usd.get_context().get_stage()
    timeline = omni.timeline.get_timeline_interface()
    timeline.set_end_time(ANIMATION_DURATION)

    # Create lights
    rep.functional.create.xform(name="World")
    rep.functional.create.dome_light(intensity=100, parent="/World", name="DomeLight")
    rep.functional.create.distant_light(intensity=2500, rotation=(315, 0, 0), parent="/World", name="DistantLight")

    # Setup the physics assets with gravity disabled and the requested velocity
    assets_root_path = get_assets_root_path()
    physics_asset_url = assets_root_path + PHYSICS_ASSET_URL
    for location, velocity in zip(ASSET_X_MIRRORED_LOCATIONS, ASSET_VELOCITIES):
        prim = rep.functional.create.reference(
            usd_path=physics_asset_url,
            parent="/World",
            name=f"physics_asset_{int(abs(velocity))}",
            position=location,
        )
        physics_rigid_body_api = UsdPhysics.RigidBodyAPI(prim)
        physics_rigid_body_api.GetVelocityAttr().Set((0, 0, -velocity))
        physx_rigid_body_api = PhysxSchema.PhysxRigidBodyAPI(prim)
        physx_rigid_body_api.GetDisableGravityAttr().Set(True)
        physx_rigid_body_api.GetAngularDampingAttr().Set(0.0)
        physx_rigid_body_api.GetLinearDampingAttr().Set(0.0)

    # Setup animated assets maintaining the same velocity as the physics assets
    anim_asset_url = assets_root_path + ANIM_ASSET_URL
    for location, velocity in zip(ASSET_X_MIRRORED_LOCATIONS, ASSET_VELOCITIES):
        start_location = (-location[0], location[1], location[2])
        prim = rep.functional.create.reference(
            usd_path=anim_asset_url,
            parent="/World",
            name=f"anim_asset_{int(abs(velocity))}",
            position=start_location,
        )
        animation_distance = velocity * ANIMATION_DURATION
        end_location = (start_location[0], start_location[1], start_location[2] - animation_distance)
        end_keyframe_time = timeline.get_time_codes_per_seconds() * ANIMATION_DURATION
        # Timesampled keyframe (animated) translation
        prim.GetAttribute("xformOp:translate").Set(start_location, time=0)
        prim.GetAttribute("xformOp:translate").Set(end_location, time=end_keyframe_time)

async def run_motion_blur_example_async(
    num_frames=NUM_FRAMES, delta_time=None, use_path_tracing=True, motion_blur_subsamples=8, samples_per_pixel=64
):
    """Capture motion blur frames with the given delta time step and render mode."""
    setup_stage()
    stage = omni.usd.get_context().get_stage()
    settings = carb.settings.get_settings()

    # Enable motion blur capture
    settings.set("/omni/replicator/captureMotionBlur", True)

    # Set motion blur settings based on the render mode
    if use_path_tracing:
        print("[MotionBlur] Setting PathTracing render mode motion blur settings")
        settings.set("/rtx/rendermode", "PathTracing")
        # (int): Total number of samples for each rendered pixel, per frame.
        settings.set("/rtx/pathtracing/spp", samples_per_pixel)
        # (int): Maximum number of samples to accumulate per pixel. When this count is reached the rendering stops until a scene or setting change is detected, restarting the rendering process. Set to 0 to remove this limit.
        settings.set("/rtx/pathtracing/totalSpp", samples_per_pixel)
        settings.set("/rtx/pathtracing/optixDenoiser/enabled", 0)
        # Number of sub samples to render if in PathTracing render mode and motion blur is enabled.
        settings.set("/omni/replicator/pathTracedMotionBlurSubSamples", motion_blur_subsamples)
    else:
        print("[MotionBlur] Setting RealTimePathTracing render mode motion blur settings")
        settings.set("/rtx/rendermode", "RealTimePathTracing")
        # 0: Disabled, 1: TAA, 2: FXAA, 3: DLSS, 4:RTXAA
        settings.set("/rtx/post/aa/op", 2)
        # (float): The fraction of the largest screen dimension to use as the maximum motion blur diameter.
        settings.set("/rtx/post/motionblur/maxBlurDiameterFraction", 0.02)
        # (float): Exposure time fraction in frames (1.0 = one frame duration) to sample.
        settings.set("/rtx/post/motionblur/exposureFraction", 1.0)
        # (int): Number of samples to use in the filter. A higher number improves quality at the cost of performance.
        settings.set("/rtx/post/motionblur/numSamples", 8)

    # Setup backend
    mode_str = f"pt_subsamples_{motion_blur_subsamples}_spp_{samples_per_pixel}" if use_path_tracing else "rt"
    delta_time_str = "None" if delta_time is None else f"{delta_time:.4f}"
    output_directory = os.path.join(os.getcwd(), f"_out_motion_blur_func_dt_{delta_time_str}_{mode_str}")
    print(f"[MotionBlur] Output directory: {output_directory}")
    backend = rep.backends.get("DiskBackend")
    backend.initialize(output_dir=output_directory)

    # Setup writer and render product
    camera = rep.functional.create.camera(
        position=(0, 1.5, 0), look_at=(0, 0, 0), parent="/World", name="MotionBlurCam"
    )
    render_product = rep.create.render_product(camera, (1280, 720))
    writer = rep.WriterRegistry.get("BasicWriter")
    writer.initialize(backend=backend, rgb=True)
    writer.attach(render_product)

    # Run a few updates to make sure all materials are fully loaded for capture
    for _ in range(5):
        await omni.kit.app.get_app().next_update_async()

    # Create or get the physics scene
    rep.functional.physics.create_physics_scene(path="/PhysicsScene")
    physx_scene = PhysxSchema.PhysxSceneAPI.Apply(stage.GetPrimAtPath(Sdf.Path("/PhysicsScene")))

    # Check the target physics depending on the delta time and the render mode
    target_physics_fps = stage.GetTimeCodesPerSecond() if delta_time is None else 1 / delta_time
    if use_path_tracing:
        target_physics_fps *= motion_blur_subsamples

    # Check if the physics FPS needs to be increased to match the delta time
    original_physics_fps = physx_scene.GetTimeStepsPerSecondAttr().Get()
    if target_physics_fps > original_physics_fps:
        print(f"[MotionBlur] Changing physics FPS from {original_physics_fps} to {target_physics_fps}")
        physx_scene.GetTimeStepsPerSecondAttr().Set(target_physics_fps)

    # Start the timeline for physics updates in the step function
    timeline = omni.timeline.get_timeline_interface()
    timeline.play()

    # Capture frames
    for i in range(num_frames):
        print(f"[MotionBlur] \tCapturing frame {i}")
        await rep.orchestrator.step_async(delta_time=delta_time)

    # Restore the original physics FPS
    if target_physics_fps > original_physics_fps:
        print(f"[MotionBlur] Restoring physics FPS from {target_physics_fps} to {original_physics_fps}")
        physx_scene.GetTimeStepsPerSecondAttr().Set(original_physics_fps)

    # Switch back to the raytracing render mode
    if use_path_tracing:
        print("[MotionBlur] Restoring render mode to RealTimePathTracing")
        settings.set("/rtx/rendermode", "RealTimePathTracing")

    # Wait until the data is fully written
    await rep.orchestrator.wait_until_complete_async()

    # Cleanup
    writer.detach()
    render_product.destroy()

async def run_motion_blur_examples_async(num_frames, delta_times, samples_per_pixel, motion_blur_subsamples):
    print(
        f"[MotionBlur] Running with delta_times={delta_times}, samples_per_pixel={samples_per_pixel}, motion_blur_subsamples={motion_blur_subsamples}"
    )

    for delta_time in delta_times:
        # RayTracing examples
        await run_motion_blur_example_async(num_frames=num_frames, delta_time=delta_time, use_path_tracing=False)
        # PathTracing examples
        for motion_blur_subsample in motion_blur_subsamples:
            for samples_per_pixel_value in samples_per_pixel:
                await run_motion_blur_example_async(
                    num_frames=num_frames,
                    delta_time=delta_time,
                    use_path_tracing=True,
                    motion_blur_subsamples=motion_blur_subsample,
                    samples_per_pixel=samples_per_pixel_value,
                )

asyncio.ensure_future(
    run_motion_blur_examples_async(
        num_frames=NUM_FRAMES,
        delta_times=DELTA_TIMES,
        samples_per_pixel=SAMPLES_PER_PIXEL,
        motion_blur_subsamples=MOTION_BLUR_SUBSAMPLES,
    )
)

async def run_motion_blur_examples_async():
    motion_blur_step_duration = [None, 1 / 30, 1 / 60, 1 / 240]
    for custom_delta_time in motion_blur_step_duration:
        # RayTracing examples
        await run_motion_blur_example_async(delta_time=custom_delta_time, use_path_tracing=False)
        # PathTracing examples
        spps = [32, 128]
        motion_blur_sub_samples = [4, 16]
        for motion_blur_sub_sample in motion_blur_sub_samples:
            for spp in spps:
                await run_motion_blur_example_async(
                    delta_time=custom_delta_time,
                    use_path_tracing=True,
                    motion_blur_subsamples=motion_blur_sub_sample,
                    samples_per_pixel=spp,
                )

asyncio.ensure_future(run_motion_blur_examples_async())
```

Standalone Application

Motion Blur

```python
"""Demonstrate motion blur capture with configurable delta times and render modes."""

from isaacsim import SimulationApp

simulation_app = SimulationApp({"headless": False})

import argparse
import os

import carb.settings
import omni.replicator.core as rep
import omni.timeline
import omni.usd
from isaacsim.storage.native import get_assets_root_path
from pxr import PhysxSchema, UsdPhysics

# Paths to the animated and physics-ready assets
PHYSICS_ASSET_URL = "/Isaac/Props/YCB/Axis_Aligned_Physics/003_cracker_box.usd"
ANIM_ASSET_URL = "/Isaac/Props/YCB/Axis_Aligned/003_cracker_box.usd"

# -z velocities and start locations of the animated (left side) and physics (right side) assets (stage units/s)
ASSET_VELOCITIES = [0, 5, 10]
ASSET_X_MIRRORED_LOCATIONS = [(0.5, 0, 0.3), (0.3, 0, 0.3), (0.1, 0, 0.3)]

# Used to calculate how many frames to animate the assets to maintain the same velocity as the physics assets
ANIMATION_DURATION = 10

# Number of frames to capture for each scenario
NUM_FRAMES = 3

def parse_delta_time(value):
    """Convert string to float or None. Accepts 'None', -1, 0, or numeric values."""
    if value.lower() == "none":
        return None
    float_value = float(value)
    return None if float_value in (-1, 0) else float_value

parser = argparse.ArgumentParser()
parser.add_argument(
    "--delta_times",
    nargs="*",
    type=parse_delta_time,
    default=[None, 1 / 30, 1 / 60, 1 / 240],
    help="List of delta times (seconds per frame) to use for motion blur captures. Use 'None' for default stage time.",
)
parser.add_argument(
    "--samples_per_pixel",
    nargs="*",
    type=int,
    default=[32, 128],
    help="List of samples per pixel (spp) values for path tracing",
)
parser.add_argument(
    "--motion_blur_subsamples",
    nargs="*",
    type=int,
    default=[4, 16],
    help="List of motion blur subsample values for path tracing",
)
args, _ = parser.parse_known_args()
delta_times = args.delta_times
samples_per_pixel = args.samples_per_pixel
motion_blur_subsamples = args.motion_blur_subsamples

def setup_stage():
    """Create a new USD stage with animated and physics-enabled assets with synchronized motion."""
    omni.usd.get_context().new_stage()
    settings = carb.settings.get_settings()
    # Set DLSS to Quality mode (2) for best SDG results , options: 0 (Performance), 1 (Balanced), 2 (Quality), 3 (Auto)
    settings.set("rtx/post/dlss/execMode", 2)

    # Capture data only on request
    rep.orchestrator.set_capture_on_play(False)

    stage = omni.usd.get_context().get_stage()
    timeline = omni.timeline.get_timeline_interface()
    timeline.set_end_time(ANIMATION_DURATION)

    # Create lights
    rep.functional.create.xform(name="World")
    rep.functional.create.dome_light(intensity=100, parent="/World", name="DomeLight")
    rep.functional.create.distant_light(intensity=2500, rotation=(315, 0, 0), parent="/World", name="DistantLight")

    # Setup the physics assets with gravity disabled and the requested velocity
    assets_root_path = get_assets_root_path()
    physics_asset_url = assets_root_path + PHYSICS_ASSET_URL
    for location, velocity in zip(ASSET_X_MIRRORED_LOCATIONS, ASSET_VELOCITIES):
        prim = rep.functional.create.reference(
            usd_path=physics_asset_url, parent="/World", name=f"physics_asset_{int(abs(velocity))}", position=location
        )
        physics_rigid_body_api = UsdPhysics.RigidBodyAPI(prim)
        physics_rigid_body_api.GetVelocityAttr().Set((0, 0, -velocity))
        physx_rigid_body_api = PhysxSchema.PhysxRigidBodyAPI(prim)
        physx_rigid_body_api.GetDisableGravityAttr().Set(True)
        physx_rigid_body_api.GetAngularDampingAttr().Set(0.0)
        physx_rigid_body_api.GetLinearDampingAttr().Set(0.0)

    # Setup animated assets maintaining the same velocity as the physics assets
    anim_asset_url = assets_root_path + ANIM_ASSET_URL
    for location, velocity in zip(ASSET_X_MIRRORED_LOCATIONS, ASSET_VELOCITIES):
        start_location = (-location[0], location[1], location[2])
        prim = rep.functional.create.reference(
            usd_path=anim_asset_url, parent="/World", name=f"anim_asset_{int(abs(velocity))}", position=start_location
        )
        animation_distance = velocity * ANIMATION_DURATION
        end_location = (start_location[0], start_location[1], start_location[2] - animation_distance)
        end_keyframe_time = timeline.get_time_codes_per_seconds() * ANIMATION_DURATION
        # Timesampled keyframe (animated) translation
        prim.GetAttribute("xformOp:translate").Set(start_location, time=0)
        prim.GetAttribute("xformOp:translate").Set(end_location, time=end_keyframe_time)

def run_motion_blur_example(
    num_frames, delta_time=None, use_path_tracing=True, motion_blur_subsamples=8, samples_per_pixel=64
):
    """Capture motion blur frames with the given delta time step and render mode."""
    setup_stage()
    stage = omni.usd.get_context().get_stage()
    settings = carb.settings.get_settings()

    # Enable motion blur capture
    settings.set("/omni/replicator/captureMotionBlur", True)

    # Set motion blur settings based on the render mode
    if use_path_tracing:
        print("[MotionBlur] Setting PathTracing render mode motion blur settings")
        settings.set("/rtx/rendermode", "PathTracing")
        # (int): Total number of samples for each rendered pixel, per frame.
        settings.set("/rtx/pathtracing/spp", samples_per_pixel)
        # (int): Maximum number of samples to accumulate per pixel. When this count is reached the rendering stops until a scene or setting change is detected, restarting the rendering process. Set to 0 to remove this limit.
        settings.set("/rtx/pathtracing/totalSpp", samples_per_pixel)
        settings.set("/rtx/pathtracing/optixDenoiser/enabled", 0)
        # Number of sub samples to render if in PathTracing render mode and motion blur is enabled.
        settings.set("/omni/replicator/pathTracedMotionBlurSubSamples", motion_blur_subsamples)
    else:
        print("[MotionBlur] Setting RealTimePathTracing render mode motion blur settings")
        settings.set("/rtx/rendermode", "RealTimePathTracing")
        # 0: Disabled, 1: TAA, 2: FXAA, 3: DLSS, 4:RTXAA
        settings.set("/rtx/post/aa/op", 2)
        # (float): The fraction of the largest screen dimension to use as the maximum motion blur diameter.
        settings.set("/rtx/post/motionblur/maxBlurDiameterFraction", 0.02)
        # (float): Exposure time fraction in frames (1.0 = one frame duration) to sample.
        settings.set("/rtx/post/motionblur/exposureFraction", 1.0)
        # (int): Number of samples to use in the filter. A higher number improves quality at the cost of performance.
        settings.set("/rtx/post/motionblur/numSamples", 8)

    # Setup backend
    mode_str = f"pt_subsamples_{motion_blur_subsamples}_spp_{samples_per_pixel}" if use_path_tracing else "rt"
    delta_time_str = "None" if delta_time is None else f"{delta_time:.4f}"
    output_directory = os.path.join(os.getcwd(), f"_out_motion_blur_func_dt_{delta_time_str}_{mode_str}")
    print(f"[MotionBlur] Output directory: {output_directory}")
    backend = rep.backends.get("DiskBackend")
    backend.initialize(output_dir=output_directory)

    # Setup writer and render product
    camera = rep.functional.create.camera(
        position=(0, 1.5, 0), look_at=(0, 0, 0), parent="/World", name="MotionBlurCam"
    )
    render_product = rep.create.render_product(camera, (1280, 720))
    writer = rep.WriterRegistry.get("BasicWriter")
    writer.initialize(backend=backend, rgb=True)
    writer.attach(render_product)

    # Run a few updates to make sure all materials are fully loaded for capture
    for _ in range(5):
        simulation_app.update()

    # Create or get the physics scene
    rep.functional.physics.create_physics_scene(path="/PhysicsScene")
    physx_scene = PhysxSchema.PhysxSceneAPI.Apply(stage.GetPrimAtPath("/PhysicsScene"))

    # Check the target physics depending on the delta time and the render mode
    target_physics_fps = stage.GetTimeCodesPerSecond() if delta_time is None else 1 / delta_time
    if use_path_tracing:
        target_physics_fps *= motion_blur_subsamples

    # Check if the physics FPS needs to be increased to match the delta time
    original_physics_fps = physx_scene.GetTimeStepsPerSecondAttr().Get()
    if target_physics_fps > original_physics_fps:
        print(f"[MotionBlur] Changing physics FPS from {original_physics_fps} to {target_physics_fps}")
        physx_scene.GetTimeStepsPerSecondAttr().Set(target_physics_fps)

    # Start the timeline for physics updates in the step function
    timeline = omni.timeline.get_timeline_interface()
    timeline.play()

    # Capture frames
    for i in range(num_frames):
        print(f"[MotionBlur] \tCapturing frame {i}")
        rep.orchestrator.step(delta_time=delta_time)

    # Restore the original physics FPS
    if target_physics_fps > original_physics_fps:
        print(f"[MotionBlur] Restoring physics FPS from {target_physics_fps} to {original_physics_fps}")
        physx_scene.GetTimeStepsPerSecondAttr().Set(original_physics_fps)

    # Switch back to the raytracing render mode
    if use_path_tracing:
        print("[MotionBlur] Restoring render mode to RealTimePathTracing")
        settings.set("/rtx/rendermode", "RealTimePathTracing")

    # Wait until the data is fully written
    rep.orchestrator.wait_until_complete()

    # Cleanup
    writer.detach()
    render_product.destroy()

def run_motion_blur_examples(num_frames, delta_times, samples_per_pixel, motion_blur_subsamples):
    """Run motion blur examples across all delta time and render mode combinations."""
    print(
        f"[MotionBlur] Running with delta_times={delta_times}, samples_per_pixel={samples_per_pixel}, motion_blur_subsamples={motion_blur_subsamples}"
    )
    for delta_time in delta_times:
        # RayTracing examples
        run_motion_blur_example(num_frames=num_frames, delta_time=delta_time, use_path_tracing=False)
        # PathTracing examples
        for motion_blur_subsample in motion_blur_subsamples:
            for samples_per_pixel_value in samples_per_pixel:
                run_motion_blur_example(
                    num_frames=num_frames,
                    delta_time=delta_time,
                    use_path_tracing=True,
                    motion_blur_subsamples=motion_blur_subsample,
                    samples_per_pixel=samples_per_pixel_value,
                )

run_motion_blur_examples(
    num_frames=NUM_FRAMES,
    delta_times=delta_times,
    samples_per_pixel=samples_per_pixel,
    motion_blur_subsamples=motion_blur_subsamples,
)
```

## Subscribers and Events at Custom FPS

Examples of subscribing to various events (such as stage, physics, and render/app), setting custom update rates, and adjusting various related settings. The standalone example can also be run directly (on Windows use `python.bat` instead of `python.sh`):

```python
./python.sh standalone_examples/api/isaacsim.replicator.examples/subscribers_and_events.py
```

Script Editor

Subscribers and Events at Custom FPS

```python
import asyncio
import time

import carb.eventdispatcher
import carb.settings
import omni.kit.app
import omni.physics.core
import omni.timeline
import omni.usd
from pxr import PhysxSchema, UsdPhysics

# TIMELINE / STAGE
USE_CUSTOM_TIMELINE_SETTINGS = True
USE_FIXED_TIME_STEPPING = True
PLAY_EVERY_FRAME = True
PLAY_DELAY_COMPENSATION = 0.0
SUBSAMPLE_RATE = 1
STAGE_FPS = 30.0

# PHYSX
USE_CUSTOM_PHYSX_FPS = False
PHYSX_FPS = 60.0
MIN_SIM_FPS = 30

# Simulations can also be enabled/disabled at runtime
DISABLE_SIMULATIONS = False

# APP / RENDER
LIMIT_APP_FPS = False
APP_FPS = 120

# Number of app updates to run while collecting events
NUM_APP_UPDATES = 100

# Print the captured events
VERBOSE = False

async def run_subscribers_and_events_async():
    def on_timeline_event(event: carb.eventdispatcher.Event):
        nonlocal timeline_events
        timeline_events.append(event)
        if VERBOSE:
            print(f"  [timeline][{len(timeline_events)}] {event}")

    def on_physics_step(dt: float, context):
        nonlocal physics_events
        physics_events.append(dt)
        if VERBOSE:
            print(f"  [physics][{len(physics_events)}] dt={dt}")

    def on_stage_render_event(event: carb.eventdispatcher.Event):
        nonlocal stage_render_events
        stage_render_events.append(event.event_name)
        if VERBOSE:
            print(f"  [stage render][{len(stage_render_events)}] {event.event_name}")

    def on_app_update(event: carb.eventdispatcher.Event):
        nonlocal app_update_events
        app_update_events.append(event.event_name)
        if VERBOSE:
            print(f"  [app update][{len(app_update_events)}] {event.event_name}")

    stage = omni.usd.get_context().get_stage()
    timeline = omni.timeline.get_timeline_interface()

    if USE_CUSTOM_TIMELINE_SETTINGS:
        # When True, the timeline forces `dt = 1 / timeCodesPerSecond` per accepted tick
        # (ignoring the run loop's measured wall-clock dt). On Play it also overrides
        # `/app/runLoops/main/rateLimitFrequency` to a value computed from
        # `targetFramerate` and `timeCodesPerSecond`.
        # Default: True in editor, False in standalone.
        # NOTE:
        # - If the app cannot sustain that rate, animation playback may slow down (see 'CompensatePlayDelayInSecs').
        # - For performance benchmarks, turn this off so the timeline advances by the loop's measured dt.
        carb.settings.get_settings().set("/app/player/useFixedTimeStepping", USE_FIXED_TIME_STEPPING)

        # This compensates for frames that require more computation time than the frame's fixed delta time, by temporarily speeding up playback.
        # The parameter represents the length of these "faster" playback periods, which means that it must be larger than the fixed frame time to take effect.
        # Default: 0.0
        # NOTE:
        # - only effective if `useFixedTimeStepping` is set to True
        # - setting a large value results in long fast playback after a huge lag spike
        carb.settings.get_settings().set("/app/player/CompensatePlayDelayInSecs", PLAY_DELAY_COMPENSATION)

        # If set to True, no frames are skipped and in every frame time advances by `1 / TimeCodesPerSecond`.
        # Default: False
        # NOTE:
        # - only effective if `useFixedTimeStepping` is set to True
        # - simulation is usually faster than real-time and processing is only limited by the frame rate of the runloop
        # - useful for recording
        # - same as `carb.settings.get_settings().set("/app/player/useFastMode", PLAY_EVERY_FRAME)`
        timeline.set_play_every_frame(PLAY_EVERY_FRAME)

        # Timeline sub-stepping, i.e. how many times updates are called (update events are dispatched) each frame.
        # Default: 1
        # NOTE: same as `carb.settings.get_settings().set("/app/player/timelineSubsampleRate", SUBSAMPLE_RATE)`
        timeline.set_ticks_per_frame(SUBSAMPLE_RATE)

        # Time codes per second for the stage
        # NOTE: same as `stage.SetTimeCodesPerSecond(STAGE_FPS)` and `carb.settings.get_settings().set("/app/stage/timeCodesPerSecond", STAGE_FPS)`
        timeline.set_time_codes_per_second(STAGE_FPS)

    # Create a PhysX scene to set the physics time step
    if USE_CUSTOM_PHYSX_FPS:
        physx_scene = None
        for prim in stage.Traverse():
            if prim.IsA(UsdPhysics.Scene):
                physx_scene = PhysxSchema.PhysxSceneAPI.Apply(prim)
                break
        if physx_scene is None:
            UsdPhysics.Scene.Define(stage, "/PhysicsScene")
            physx_scene = PhysxSchema.PhysxSceneAPI.Apply(stage.GetPrimAtPath("/PhysicsScene"))

        # Time step for the physics simulation
        # Default: 60.0
        physx_scene.GetTimeStepsPerSecondAttr().Set(PHYSX_FPS)

        # Minimum simulation frequency to prevent clamping; if the frame rate drops below this,
        # physics steps are discarded to avoid app slowdown if the overall frame rate is too low.
        # Default: 30.0
        # NOTE: Matching `minFrameRate` with `TimeStepsPerSecond` ensures a single physics step per update.
        carb.settings.get_settings().set("/persistent/simulation/minFrameRate", MIN_SIM_FPS)

    # Throttle Render/UI/Main thread update rate
    if LIMIT_APP_FPS:
        # Enable rate limiting of the main run loop (UI, rendering, etc.)
        # Default: False
        carb.settings.get_settings().set("/app/runLoops/main/rateLimitEnabled", LIMIT_APP_FPS)

        # FPS limit of the main run loop (UI, rendering, etc.)
        # Default: 120
        # NOTE: This caps the loop's tick rate (sleeps at end of frame); it does NOT set the
        # timeline's per-tick dt. On Play with `/app/player/useFixedTimeStepping=True`,
        # the timeline computes its own `rateLimitFrequency` from `targetFramerate` and
        # `timeCodesPerSecond` and overrides this value at that moment.
        carb.settings.get_settings().set("/app/runLoops/main/rateLimitFrequency", int(APP_FPS))

    # Simulations can be selectively disabled (or toggled at specific times)
    if DISABLE_SIMULATIONS:
        carb.settings.get_settings().set("/app/player/playSimulations", False)

    print("Configuration:")
    print(f"  Timeline:")
    print(f"    - Stage FPS: {STAGE_FPS}  (/app/stage/timeCodesPerSecond)")
    print(f"    - Fixed time stepping: {USE_FIXED_TIME_STEPPING}  (/app/player/useFixedTimeStepping)")
    print(f"    - Play every frame: {PLAY_EVERY_FRAME}  (/app/player/useFastMode)")
    print(f"    - Subsample rate: {SUBSAMPLE_RATE}  (/app/player/timelineSubsampleRate)")
    print(f"    - Play delay compensation: {PLAY_DELAY_COMPENSATION}s  (/app/player/CompensatePlayDelayInSecs)")
    print(f"  Physics:")
    print(f"    - PhysX FPS: {PHYSX_FPS}  (physxScene.timeStepsPerSecond)")
    print(f"    - PhysX min frame-rate clamp: {MIN_SIM_FPS}  (/persistent/simulation/minFrameRate)")
    print(f"    - Simulations enabled: {not DISABLE_SIMULATIONS}  (/app/player/playSimulations)")
    print(f"  Rendering:")
    print(f"    - App FPS limit: {APP_FPS if LIMIT_APP_FPS else 'unlimited'}  (/app/runLoops/main/rateLimitFrequency)")

    # Start the timeline
    print(f"Starting the timeline...")
    timeline.set_current_time(0)
    timeline.set_end_time(10000)
    timeline.set_looping(False)
    timeline.play()
    timeline.commit()
    wall_start_time = time.time()

    # Subscribe to events
    print(f"Subscribing to events...")
    timeline_events = []
    timeline_sub = carb.eventdispatcher.get_eventdispatcher().observe_event(
        event_name=omni.timeline.GLOBAL_EVENT_CURRENT_TIME_TICKED,
        on_event=on_timeline_event,
        observer_name="test_sdg_useful_snippets_timeline_based.on_timeline_event",
    )
    physics_events = []
    physics_sub = omni.physics.core.get_physics_simulation_interface().subscribe_physics_on_step_events(
        pre_step=False, order=0, on_update=on_physics_step
    )
    stage_render_events = []
    stage_render_sub = carb.eventdispatcher.get_eventdispatcher().observe_event(
        event_name=omni.usd.get_context().stage_rendering_event_name(omni.usd.StageRenderingEventType.NEW_FRAME, True),
        on_event=on_stage_render_event,
        observer_name="subscribers_and_events.on_stage_render_event",
    )
    app_update_events = []
    app_sub = carb.eventdispatcher.get_eventdispatcher().observe_event(
        event_name=omni.kit.app.GLOBAL_EVENT_UPDATE,
        on_event=on_app_update,
        observer_name="subscribers_and_events.on_app_update",
    )

    # Run app updates and cache events
    print(f"Starting running the application for {NUM_APP_UPDATES} updates...")
    for i in range(NUM_APP_UPDATES):
        if VERBOSE:
            print(f"[app update loop][{i+1}/{NUM_APP_UPDATES}]")
        await omni.kit.app.get_app().next_update_async()
    elapsed_wall_time = time.time() - wall_start_time
    print(f"Finished running the application for {NUM_APP_UPDATES} updates...")

    # Stop timeline and unsubscribe from all events
    print(f"Stopping timeline and unsubscribing from all events...")
    timeline.stop()
    if app_sub:
        app_sub.reset()
        app_sub = None
    if stage_render_sub:
        stage_render_sub.reset()
        stage_render_sub = None
    if physics_sub:
        physics_sub.unsubscribe()
        physics_sub = None
    if timeline_sub:
        timeline_sub.reset()
        timeline_sub = None

    # Print summary statistics
    print("\nStats:")
    print(f"- App updates: {NUM_APP_UPDATES}")
    print(f"- Wall time: {elapsed_wall_time:.4f} seconds")
    print(f"- Timeline events: {len(timeline_events)}")
    print(f"- Physics events: {len(physics_events)}")
    print(f"- Stage render events: {len(stage_render_events)}")
    print(f"- App update events: {len(app_update_events)}")

    # Calculate and display real-time performance factor
    if len(physics_events) > 0:
        sim_time = sum(physics_events)
        realtime_factor = sim_time / elapsed_wall_time if elapsed_wall_time > 0 else 0
        print(f"- Simulation time: {sim_time:.4f}s")
        print(f"- Real-time factor: {realtime_factor:.2f}x")

asyncio.ensure_future(run_subscribers_and_events_async())
```

Standalone Application

Subscribers and Events at Custom FPS

```python
"""Demonstrate timeline, physics, render, and app update event subscriptions."""

from isaacsim import SimulationApp

simulation_app = SimulationApp({"headless": False})

import time

import carb.eventdispatcher
import carb.settings
import omni.kit.app
import omni.physics.core
import omni.timeline
import omni.usd
from pxr import PhysxSchema, UsdPhysics

# TIMELINE / STAGE
USE_CUSTOM_TIMELINE_SETTINGS = True
USE_FIXED_TIME_STEPPING = True
PLAY_EVERY_FRAME = True
PLAY_DELAY_COMPENSATION = 0.0
SUBSAMPLE_RATE = 1
STAGE_FPS = 30.0

# PHYSX
USE_CUSTOM_PHYSX_FPS = False
PHYSX_FPS = 60.0
MIN_SIM_FPS = 30

# Simulations can also be enabled/disabled at runtime
DISABLE_SIMULATIONS = False

# APP / RENDER
LIMIT_APP_FPS = False
APP_FPS = 120

# Number of app updates to run while collecting events
NUM_APP_UPDATES = 100

# Print the captured events
VERBOSE = False

def on_timeline_event(event: carb.eventdispatcher.Event):
    """Handle timeline tick events."""
    global timeline_events
    timeline_events.append(event)
    if VERBOSE:
        print(f"  [timeline][{len(timeline_events)}] {event}")

def on_physics_step(dt, context):
    """Handle physics step events."""
    global physics_events
    physics_events.append(dt)
    if VERBOSE:
        print(f"  [physics][{len(physics_events)}] dt={dt}")

def on_stage_render_event(event: carb.eventdispatcher.Event):
    """Handle stage render new frame events."""
    global stage_render_events
    stage_render_events.append(event.event_name)
    if VERBOSE:
        print(f"  [stage render][{len(stage_render_events)}] {event.event_name}")

def on_app_update(event: carb.eventdispatcher.Event):
    """Handle application update events."""
    global app_update_events
    app_update_events.append(event.event_name)
    if VERBOSE:
        print(f"  [app update][{len(app_update_events)}] {event.event_name}")

stage = omni.usd.get_context().get_stage()
timeline = omni.timeline.get_timeline_interface()

if USE_CUSTOM_TIMELINE_SETTINGS:
    # When True, the timeline forces `dt = 1 / timeCodesPerSecond` per accepted tick
    # (ignoring the run loop's measured wall-clock dt). On Play it also overrides
    # `/app/runLoops/main/rateLimitFrequency` to a value computed from
    # `targetFramerate` and `timeCodesPerSecond`.
    # Default: True in editor, False in standalone.
    # NOTE:
    # - If the app cannot sustain that rate, animation playback may slow down (see 'CompensatePlayDelayInSecs').
    # - For performance benchmarks, turn this off so the timeline advances by the loop's measured dt.
    carb.settings.get_settings().set("/app/player/useFixedTimeStepping", USE_FIXED_TIME_STEPPING)

    # This compensates for frames that require more computation time than the frame's fixed delta time, by temporarily speeding up playback.
    # The parameter represents the length of these "faster" playback periods, which means that it must be larger than the fixed frame time to take effect.
    # Default: 0.0
    # NOTE:
    # - only effective if `useFixedTimeStepping` is set to True
    # - setting a large value results in long fast playback after a huge lag spike
    carb.settings.get_settings().set("/app/player/CompensatePlayDelayInSecs", PLAY_DELAY_COMPENSATION)

    # If set to True, no frames are skipped and in every frame time advances by `1 / TimeCodesPerSecond`.
    # Default: False
    # NOTE:
    # - only effective if `useFixedTimeStepping` is set to True
    # - simulation is usually faster than real-time and processing is only limited by the frame rate of the runloop
    # - useful for recording
    # - same as `carb.settings.get_settings().set("/app/player/useFastMode", PLAY_EVERY_FRAME)`
    timeline.set_play_every_frame(PLAY_EVERY_FRAME)

    # Timeline sub-stepping, i.e. how many times updates are called (update events are dispatched) each frame.
    # Default: 1
    # NOTE: same as `carb.settings.get_settings().set("/app/player/timelineSubsampleRate", SUBSAMPLE_RATE)`
    timeline.set_ticks_per_frame(SUBSAMPLE_RATE)

    # Time codes per second for the stage
    # NOTE: same as `stage.SetTimeCodesPerSecond(STAGE_FPS)` and `carb.settings.get_settings().set("/app/stage/timeCodesPerSecond", STAGE_FPS)`
    timeline.set_time_codes_per_second(STAGE_FPS)

# Create a PhysX scene to set the physics time step
if USE_CUSTOM_PHYSX_FPS:
    physx_scene = None
    for prim in stage.Traverse():
        if prim.IsA(UsdPhysics.Scene):
            physx_scene = PhysxSchema.PhysxSceneAPI.Apply(prim)
            break
    if physx_scene is None:
        UsdPhysics.Scene.Define(stage, "/PhysicsScene")
        physx_scene = PhysxSchema.PhysxSceneAPI.Apply(stage.GetPrimAtPath("/PhysicsScene"))

    # Time step for the physics simulation
    # Default: 60.0
    physx_scene.GetTimeStepsPerSecondAttr().Set(PHYSX_FPS)

    # Minimum simulation frequency to prevent clamping; if the frame rate drops below this,
    # physics steps are discarded to avoid app slowdown if the overall frame rate is too low.
    # Default: 30.0
    # NOTE: Matching `minFrameRate` with `TimeStepsPerSecond` ensures a single physics step per update.
    carb.settings.get_settings().set("/persistent/simulation/minFrameRate", MIN_SIM_FPS)

# Throttle Render/UI/Main thread update rate
if LIMIT_APP_FPS:
    # Enable rate limiting of the main run loop (UI, rendering, etc.)
    # Default: False
    carb.settings.get_settings().set("/app/runLoops/main/rateLimitEnabled", LIMIT_APP_FPS)

    # FPS limit of the main run loop (UI, rendering, etc.)
    # Default: 120
    # NOTE: This caps the loop's tick rate (sleeps at end of frame); it does NOT set the
    # timeline's per-tick dt. On Play with `/app/player/useFixedTimeStepping=True`,
    # the timeline computes its own `rateLimitFrequency` from `targetFramerate` and
    # `timeCodesPerSecond` and overrides this value at that moment.
    carb.settings.get_settings().set("/app/runLoops/main/rateLimitFrequency", int(APP_FPS))

# Simulations can be selectively disabled (or toggled at specific times)
if DISABLE_SIMULATIONS:
    carb.settings.get_settings().set("/app/player/playSimulations", False)

print("Configuration:")
print(f"  Timeline:")
print(f"    - Stage FPS: {STAGE_FPS}  (/app/stage/timeCodesPerSecond)")
print(f"    - Fixed time stepping: {USE_FIXED_TIME_STEPPING}  (/app/player/useFixedTimeStepping)")
print(f"    - Play every frame: {PLAY_EVERY_FRAME}  (/app/player/useFastMode)")
print(f"    - Subsample rate: {SUBSAMPLE_RATE}  (/app/player/timelineSubsampleRate)")
print(f"    - Play delay compensation: {PLAY_DELAY_COMPENSATION}s  (/app/player/CompensatePlayDelayInSecs)")
print(f"  Physics:")
print(f"    - PhysX FPS: {PHYSX_FPS}  (physxScene.timeStepsPerSecond)")
print(f"    - PhysX min frame-rate clamp: {MIN_SIM_FPS}  (/persistent/simulation/minFrameRate)")
print(f"    - Simulations enabled: {not DISABLE_SIMULATIONS}  (/app/player/playSimulations)")
print(f"  Rendering:")
print(f"    - App FPS limit: {APP_FPS if LIMIT_APP_FPS else 'unlimited'}  (/app/runLoops/main/rateLimitFrequency)")

# Start the timeline
print(f"Starting the timeline...")
timeline.set_current_time(0)
timeline.set_end_time(10000)
timeline.set_looping(False)
timeline.play()
timeline.commit()
wall_start_time = time.time()

# Subscribe to events
print(f"Subscribing to events...")
timeline_events = []
timeline_sub = carb.eventdispatcher.get_eventdispatcher().observe_event(
    event_name=omni.timeline.GLOBAL_EVENT_CURRENT_TIME_TICKED,
    on_event=on_timeline_event,
    observer_name="subscribers_and_events.on_timeline_event",
)
physics_events = []
physics_sub = omni.physics.core.get_physics_simulation_interface().subscribe_physics_on_step_events(
    pre_step=False, order=0, on_update=on_physics_step
)
stage_render_events = []
stage_render_sub = carb.eventdispatcher.get_eventdispatcher().observe_event(
    event_name=omni.usd.get_context().stage_rendering_event_name(omni.usd.StageRenderingEventType.NEW_FRAME, True),
    on_event=on_stage_render_event,
    observer_name="subscribers_and_events.on_stage_render_event",
)
app_update_events = []
app_sub = carb.eventdispatcher.get_eventdispatcher().observe_event(
    event_name=omni.kit.app.GLOBAL_EVENT_UPDATE,
    on_event=on_app_update,
    observer_name="subscribers_and_events.on_app_update",
)

# Run app updates and cache events
print(f"Starting running the application for {NUM_APP_UPDATES} updates.")
for i in range(NUM_APP_UPDATES):
    if VERBOSE:
        print(f"[app update loop][{i+1}/{NUM_APP_UPDATES}]")
    simulation_app.update()
elapsed_wall_time = time.time() - wall_start_time
print(f"Finished running the application for {NUM_APP_UPDATES} updates...")

# Stop timeline and unsubscribe from all events
timeline.stop()
app_sub = None
stage_render_sub = None
if physics_sub:
    physics_sub.unsubscribe()
    physics_sub = None
timeline_sub = None

# Print summary statistics
print("\nStats:")
print(f"- App updates: {NUM_APP_UPDATES}")
print(f"- Wall time: {elapsed_wall_time:.4f} seconds")
print(f"- Timeline events: {len(timeline_events)}")
print(f"- Physics events: {len(physics_events)}")
print(f"- Stage render events: {len(stage_render_events)}")
print(f"- App update events: {len(app_update_events)}")

# Calculate and display real-time performance factor
if len(physics_events) > 0:
    sim_time = sum(physics_events)
    realtime_factor = sim_time / elapsed_wall_time if elapsed_wall_time > 0 else 0
    print(f"- Simulation time: {sim_time:.4f}s")
    print(f"- Real-time factor: {realtime_factor:.2f}x")

simulation_app.close()
```

## Accessing Writer and Annotator Data at Custom FPS

Example of how to trigger a writer and access annotator data at a custom FPS, with product rendering disabled when the data is not needed. The standalone example can also be run directly (on Windows use `python.bat` instead of `python.sh`):

```python
./python.sh standalone_examples/api/isaacsim.replicator.examples/custom_fps_writer_annotator.py
```

Note

It is currently not possible to change timeline (stage) FPS after the replicator graph creation as it causes a graph reset. This issue is being addressed. As a workaround make sure you are setting the timeline (stage) parameters before creating the replicator graph.

Script Editor

Accessing Writer and Annotator Data at Custom FPS

```python
import asyncio
import os

import carb.settings
import omni.kit.app
import omni.replicator.core as rep
import omni.timeline
import omni.usd

# Configuration
NUM_CAPTURES = 6
VERBOSE = True

# NOTE: To avoid FPS delta misses make sure the sensor framerate is divisible by the timeline framerate
STAGE_FPS = 100.0
SENSOR_FPS = 10.0
SENSOR_DT = 1.0 / SENSOR_FPS

async def run_custom_fps_example_async(duration_seconds):
    # Create a new stage
    await omni.usd.get_context().new_stage_async()

    # Disable capture on play to capture data manually using step
    rep.orchestrator.set_capture_on_play(False)

    # Set DLSS to Quality mode (2) for best SDG results , options: 0 (Performance), 1 (Balanced), 2 (Quality), 3 (Auto)
    carb.settings.get_settings().set("rtx/post/dlss/execMode", 2)

    # Make sure fixed time stepping is set (the timeline will be advanced with the same delta time)
    carb.settings.get_settings().set("/app/player/useFixedTimeStepping", True)

    # Create scene with a semantically annotated cube with physics
    rep.functional.create.xform(name="World")
    rep.functional.create.dome_light(intensity=250, parent="/World", name="DomeLight")
    cube = rep.functional.create.cube(position=(0, 0, 2), parent="/World", name="Cube", semantics={"class": "cube"})
    rep.functional.physics.apply_collider(cube)
    rep.functional.physics.apply_rigid_body(cube)

    # Create render product (disabled until data capture is needed)
    cam = rep.functional.create.camera(position=(5, 5, 5), look_at=(0, 0, 0), parent="/World", name="Camera")
    rp = rep.create.render_product(cam, resolution=(512, 512), name="rp")
    rp.hydra_texture.set_updates_enabled(False)

    # Create the backend for the writer
    out_dir_rgb = os.path.join(os.getcwd(), "_out_writer_fps_rgb")
    print(f"Writer data will be written to: {out_dir_rgb}")
    backend = rep.backends.get("DiskBackend")
    backend.initialize(output_dir=out_dir_rgb)

    # Create a writer and an annotator as examples of different ways of accessing data
    writer_rgb = rep.WriterRegistry.get("BasicWriter")
    writer_rgb.initialize(backend=backend, rgb=True)
    writer_rgb.attach(rp)

    # Create an annotator to access the data directly
    annot_depth = rep.AnnotatorRegistry.get_annotator("distance_to_camera")
    annot_depth.attach(rp)

    # Run the simulation for the given number of frames and access the data at the desired framerates
    print(
        f"Starting simulation: {duration_seconds:.2f}s duration, {SENSOR_FPS:.0f} FPS sensor, {STAGE_FPS:.0f} FPS timeline"
    )

    # Set the timeline parameters
    timeline = omni.timeline.get_timeline_interface()
    timeline.set_looping(False)
    timeline.set_current_time(0.0)
    timeline.set_end_time(10)
    timeline.set_time_codes_per_second(STAGE_FPS)
    timeline.play()
    timeline.commit()

    # Run the simulation for the given number of frames and access the data at the desired framerates
    frame_count = 0
    previous_time = timeline.get_current_time()
    elapsed_time = 0.0
    iteration = 0

    while timeline.get_current_time() < duration_seconds:
        current_time = timeline.get_current_time()
        delta_time = current_time - previous_time
        elapsed_time += delta_time

        # Simulation progress
        if VERBOSE:
            print(f"Step {iteration}: timeline time={current_time:.3f}s, elapsed time={elapsed_time:.3f}s")

        # Trigger sensor at desired framerate (use small epsilon for floating point comparison)
        if elapsed_time >= SENSOR_DT - 1e-9:
            elapsed_time -= SENSOR_DT  # Reset with remainder to maintain accuracy

            rp.hydra_texture.set_updates_enabled(True)
            await rep.orchestrator.step_async(delta_time=0.0, pause_timeline=False, rt_subframes=16)
            annot_data = annot_depth.get_data()

            print(f"\n  >> Capturing frame {frame_count} at time={current_time:.3f}s | shape={annot_data.shape}\n")
            frame_count += 1

            rp.hydra_texture.set_updates_enabled(False)

        previous_time = current_time
        # Advance the app (timeline) by one frame
        await omni.kit.app.get_app().next_update_async()
        iteration += 1

    # Wait for writer to finish
    await rep.orchestrator.wait_until_complete_async()

    # Cleanup
    timeline.pause()
    writer_rgb.detach()
    annot_depth.detach()
    rp.destroy()

# Run example with duration for all captures plus a buffer of 5 frames
duration = (NUM_CAPTURES * SENSOR_DT) + (5.0 / STAGE_FPS)
asyncio.ensure_future(run_custom_fps_example_async(duration_seconds=duration))
```

Standalone Application

Accessing Writer and Annotator Data at Custom FPS

```python
"""Demonstrate custom FPS data capture using writers and annotators."""

from isaacsim import SimulationApp

simulation_app = SimulationApp({"headless": False})

import os

import carb.settings
import omni.kit.app
import omni.replicator.core as rep
import omni.timeline
import omni.usd

# Configuration
NUM_CAPTURES = 6
VERBOSE = True

# NOTE: To avoid FPS delta misses make sure the sensor framerate is divisible by the timeline framerate
STAGE_FPS = 100.0
SENSOR_FPS = 10.0
SENSOR_DT = 1.0 / SENSOR_FPS

def run_custom_fps_example(duration_seconds):
    """Run a simulation capturing data at a custom sensor framerate."""
    # Create a new stage
    omni.usd.get_context().new_stage()

    # Disable capture on play to capture data manually using step
    rep.orchestrator.set_capture_on_play(False)

    # Set DLSS to Quality mode (2) for best SDG results , options: 0 (Performance), 1 (Balanced), 2 (Quality), 3 (Auto)
    carb.settings.get_settings().set("rtx/post/dlss/execMode", 2)

    # Enable fixed time stepping: the timeline will advance by `1 / timeCodesPerSecond`
    # per accepted tick, ignoring the run loop's measured wall-clock dt.
    carb.settings.get_settings().set("/app/player/useFixedTimeStepping", True)

    # Create scene with a semantically annotated cube with physics
    rep.functional.create.xform(name="World")
    rep.functional.create.dome_light(intensity=250, parent="/World", name="DomeLight")
    cube = rep.functional.create.cube(position=(0, 0, 2), parent="/World", name="Cube", semantics={"class": "cube"})
    rep.functional.physics.apply_collider(cube)
    rep.functional.physics.apply_rigid_body(cube)

    # Create render product (disabled until data capture is needed)
    cam = rep.functional.create.camera(position=(5, 5, 5), look_at=(0, 0, 0), parent="/World", name="Camera")
    rp = rep.create.render_product(cam, resolution=(512, 512), name="rp")
    rp.hydra_texture.set_updates_enabled(False)

    # Create the backend for the writer
    out_dir_rgb = os.path.join(os.getcwd(), "_out_writer_fps_rgb")
    print(f"Writer data will be written to: {out_dir_rgb}")
    backend = rep.backends.get("DiskBackend")
    backend.initialize(output_dir=out_dir_rgb)

    # Create a writer and an annotator as examples of different ways of accessing data
    writer_rgb = rep.WriterRegistry.get("BasicWriter")
    writer_rgb.initialize(backend=backend, rgb=True)
    writer_rgb.attach(rp)

    # Create an annotator to access the data directly
    annot_depth = rep.AnnotatorRegistry.get_annotator("distance_to_camera")
    annot_depth.attach(rp)

    # Run the simulation for the given number of frames and access the data at the desired framerates
    print(
        f"Starting simulation: {duration_seconds:.2f}s duration, {SENSOR_FPS:.0f} FPS sensor, {STAGE_FPS:.0f} FPS timeline"
    )

    # Set the timeline parameters
    timeline = omni.timeline.get_timeline_interface()
    timeline.set_looping(False)
    timeline.set_current_time(0.0)
    timeline.set_end_time(10)
    timeline.set_time_codes_per_second(STAGE_FPS)
    timeline.play()
    timeline.commit()

    # Run the simulation for the given number of frames and access the data at the desired framerates
    frame_count = 0
    previous_time = timeline.get_current_time()
    elapsed_time = 0.0
    iteration = 0

    while timeline.get_current_time() < duration_seconds:
        current_time = timeline.get_current_time()
        delta_time = current_time - previous_time
        elapsed_time += delta_time

        # Simulation progress
        if VERBOSE:
            print(f"Step {iteration}: timeline time={current_time:.3f}s, elapsed time={elapsed_time:.3f}s")

        # Trigger sensor at desired framerate (use small epsilon for floating point comparison)
        if elapsed_time >= SENSOR_DT - 1e-9:
            elapsed_time -= SENSOR_DT  # Reset with remainder to maintain accuracy

            rp.hydra_texture.set_updates_enabled(True)
            rep.orchestrator.step(delta_time=0.0, pause_timeline=False, rt_subframes=16)
            annot_data = annot_depth.get_data()

            print(f"\n  >> Capturing frame {frame_count} at time={current_time:.3f}s | shape={annot_data.shape}\n")
            frame_count += 1

            rp.hydra_texture.set_updates_enabled(False)

        previous_time = current_time
        # Advance the app (timeline) by one frame
        simulation_app.update()
        iteration += 1

    # Wait for writer to finish
    rep.orchestrator.wait_until_complete()

    # Cleanup
    timeline.pause()
    writer_rgb.detach()
    annot_depth.detach()
    rp.destroy()

# Run example with duration for all captures plus a buffer of 5 frames
duration = (NUM_CAPTURES * SENSOR_DT) + (5.0 / STAGE_FPS)
run_custom_fps_example(duration_seconds=duration)
```

## Cosmos Writer Example

This example demonstrates the `CosmosWriter` for capturing multi-modal synthetic data compatible with [NVIDIA Cosmos](https://www.nvidia.com/en-us/ai/cosmos/) world foundation models. It creates a simple falling box scene and captures synchronized RGB, segmentation, depth, and edge data (images and videos) that can be used with Cosmos Transfer to generate photorealistic variations.

For a more detailed tutorial please see [Cosmos Synthetic Data Generation](tutorial_replicator_cosmos.html#isaac-sim-app-tutorial-replicator-cosmos).

The standalone example can also be run directly (on Windows use `python.bat` instead of `python.sh`):

```python
./python.sh standalone_examples/api/isaacsim.replicator.examples/cosmos_writer_simple.py
```

Script Editor

Cosmos Writer Example

```python
import asyncio
import os

import carb.settings
import omni.replicator.core as rep
import omni.timeline
import omni.usd

SEGMENTATION_MAPPING = {
    "plane": [0, 0, 255, 255],
    "cube": [255, 0, 0, 255],
    "sphere": [0, 255, 0, 255],
}
NUM_FRAMES = 60

async def run_cosmos_example_async(num_frames, segmentation_mapping=None):
    # Create a new stage
    omni.usd.get_context().new_stage()

    # CosmosWriter requires script nodes to be enabled
    carb.settings.get_settings().set_bool("/app/omni.graph.scriptnode/opt_in", True)

    # Disable capture on play, data is captured manually using the step function
    rep.orchestrator.set_capture_on_play(False)

    # Set DLSS to Quality mode (2) for best SDG results (Options: 0 (Performance), 1 (Balanced), 2 (Quality), 3 (Auto)
    carb.settings.get_settings().set("rtx/post/dlss/execMode", 2)

    # Set the stage properties
    rep.settings.set_stage_up_axis("Z")
    rep.settings.set_stage_meters_per_unit(1.0)
    rep.functional.create.dome_light(intensity=500)

    # Create the scenario with a ground plane and a falling sphere and cube.
    plane = rep.functional.create.plane(position=(0, 0, 0), scale=(10, 10, 1), semantics={"class": "plane"})
    rep.functional.physics.apply_collider(plane)

    sphere = rep.functional.create.sphere(position=(0, 0, 3), semantics={"class": "sphere"})
    rep.functional.physics.apply_collider(sphere)
    rep.functional.physics.apply_rigid_body(sphere)

    cube = rep.functional.create.cube(position=(1, 1, 2), scale=0.5, semantics={"class": "cube"})
    rep.functional.physics.apply_collider(cube)
    rep.functional.physics.apply_rigid_body(cube)

    # Set up the writer
    camera = rep.functional.create.camera(position=(5, 5, 3), look_at=(0, 0, 0))
    rp = rep.create.render_product(camera, (1280, 720))
    out_dir = os.path.join(os.getcwd(), "_out_cosmos_simple")
    print(f"Output directory: {out_dir}")
    cosmos_writer = rep.WriterRegistry.get("CosmosWriter")
    cosmos_writer.initialize(output_dir=out_dir, segmentation_mapping=segmentation_mapping)
    cosmos_writer.attach(rp)

    # Start the simulation
    timeline = omni.timeline.get_timeline_interface()
    timeline.play()

    # Capture a frame every app update
    for i in range(num_frames):
        print(f"Frame {i+1}/{num_frames}")
        await omni.kit.app.get_app().next_update_async()
        await rep.orchestrator.step_async(delta_time=0.0, pause_timeline=False)
    timeline.pause()

    # Wait for all data to be written
    await rep.orchestrator.wait_until_complete_async()
    print("Data generation complete!")
    cosmos_writer.detach()
    rp.destroy()

asyncio.ensure_future(run_cosmos_example_async(num_frames=NUM_FRAMES, segmentation_mapping=SEGMENTATION_MAPPING))
```

Standalone Application

Cosmos Writer Example

```python
"""Demonstrate synthetic data generation using the CosmosWriter."""

from isaacsim import SimulationApp

simulation_app = SimulationApp(launch_config={"headless": False})

import os

import carb.settings
import omni.replicator.core as rep
import omni.timeline
import omni.usd

SEGMENTATION_MAPPING = {
    "plane": [0, 0, 255, 255],
    "cube": [255, 0, 0, 255],
    "sphere": [0, 255, 0, 255],
}
NUM_FRAMES = 60

def run_cosmos_example(num_frames, segmentation_mapping=None):
    """Run a CosmosWriter example capturing physics simulation frames."""
    # Create a new stage
    omni.usd.get_context().new_stage()

    # Set DLSS to Quality mode (2) for best SDG results , options: 0 (Performance), 1 (Balanced), 2 (Quality), 3 (Auto)
    carb.settings.get_settings().set("rtx/post/dlss/execMode", 2)

    # CosmosWriter requires script nodes to be enabled
    carb.settings.get_settings().set_bool("/app/omni.graph.scriptnode/opt_in", True)

    # Disable capture on play, data is captured manually using the step function
    rep.orchestrator.set_capture_on_play(False)

    # Set the stage properties
    rep.settings.set_stage_up_axis("Z")
    rep.settings.set_stage_meters_per_unit(1.0)
    rep.functional.create.dome_light(intensity=500)

    # Create the scenario with a ground plane and a falling sphere and cube.
    plane = rep.functional.create.plane(position=(0, 0, 0), scale=(10, 10, 1), semantics={"class": "plane"})
    rep.functional.physics.apply_collider(plane)

    sphere = rep.functional.create.sphere(position=(0, 0, 3), semantics={"class": "sphere"})
    rep.functional.physics.apply_collider(sphere)
    rep.functional.physics.apply_rigid_body(sphere)

    cube = rep.functional.create.cube(position=(1, 1, 2), scale=0.5, semantics={"class": "cube"})
    rep.functional.physics.apply_collider(cube)
    rep.functional.physics.apply_rigid_body(cube)

    # Set up the writer
    camera = rep.functional.create.camera(position=(5, 5, 3), look_at=(0, 0, 0))
    rp = rep.create.render_product(camera, (1280, 720))
    out_dir = os.path.join(os.getcwd(), "_out_cosmos_simple")
    print(f"Output directory: {out_dir}")
    backend = rep.backends.get("DiskBackend")
    backend.initialize(output_dir=out_dir)
    cosmos_writer = rep.WriterRegistry.get("CosmosWriter")
    cosmos_writer.initialize(backend=backend, segmentation_mapping=segmentation_mapping)
    cosmos_writer.attach(rp)

    # Start the simulation
    timeline = omni.timeline.get_timeline_interface()
    timeline.play()

    # Capture a frame every app update
    for i in range(num_frames):
        print(f"Frame {i+1}/{num_frames}")
        simulation_app.update()
        rep.orchestrator.step(delta_time=0.0, pause_timeline=False)
    timeline.pause()

    # Wait for all data to be written
    rep.orchestrator.wait_until_complete()
    print("Data generation complete!")
    cosmos_writer.detach()
    rp.destroy()

run_cosmos_example(num_frames=NUM_FRAMES, segmentation_mapping=SEGMENTATION_MAPPING)
```

## Synthetic Data Generation with Deformables

This example demonstrates synthetic data generation (SDG) with deformable physics: deformable assets (e.g., bananas and markers) are dropped into a crate, and RGB plus semantic segmentation frames are captured when each asset’s lowest vertex crosses a trigger height. It uses `VolumeDeformableMaterial`, `DeformablePrim`, and the deformable tensor API (e.g., `get_nodal_positions`) for trigger detection, with optional material color randomization per capture.

The standalone example can also be run directly (on Windows use `python.bat` instead of `python.sh`):

```python
./python.sh standalone_examples/api/isaacsim.replicator.examples/sdg_deformables.py
```

Script Editor

Synthetic Data Generation with Deformables

```python
import asyncio
import os
import random

import carb.settings
import omni.kit.app
import omni.replicator.core as rep
import omni.timeline
import omni.usd
from isaacsim.core.experimental.materials import VolumeDeformableMaterial
from isaacsim.core.experimental.prims import DeformablePrim
from isaacsim.core.simulation_manager import SimulationManager
from isaacsim.storage.native import get_assets_root_path_async
from pxr import Gf, Sdf, Usd, UsdShade

TRIGGER_HEIGHT = 0.15  # Capture when lowest vertex falls below this (m)
BASE_DROP_HEIGHT = 0.2  # Starting height for first asset (m)
HEIGHT_STEP = 0.15  # Height increment between assets (m)
SPAWN_XY_JITTER = 0.07  # Random horizontal offset +/- (m)
RNG_SEED = 12  # Reproducible randomization seed
MAX_STEPS = 200  # Maximum simulation steps
CRATE_USD = "/Isaac/Props/PackingTable/props/SM_Crate_A08_Blue_01/SM_Crate_A08_Blue_01.usd"

# (label, count, usd_path, youngs_modulus_Pa [higher=stiffer], poissons_ratio [0=compressible, 0.5=incompressible])
ASSETS_CONFIG = [
    ("banana", 6, "/Isaac/Props/YCB/Axis_Aligned/011_banana.usd", 500_000, 0.45),
    ("large_marker", 5, "/Isaac/Props/YCB/Axis_Aligned/040_large_marker.usd", 9_000_000, 0.5),
]

async def run_example_async(assets_config: list[tuple[str, int, str, float, float]]):
    await omni.usd.get_context().new_stage_async()
    assets_root_path = await get_assets_root_path_async()
    rng = random.Random(RNG_SEED)

    # Disable capture on play, frames will be captured manually
    rep.orchestrator.set_capture_on_play(False)

    # Set DLSS to Quality mode (2) for best SDG results (Options: 0 (Performance), 1 (Balanced), 2 (Quality), 3 (Auto)
    carb.settings.get_settings().set("rtx/post/dlss/execMode", 2)

    rep.functional.create.xform(name="World")
    rep.functional.create.dome_light(intensity=500, parent="/World", name="DomeLight")
    ground = rep.functional.create.cube(position=(0, 0, -0.5), scale=(10, 10, 1))
    rep.functional.physics.apply_collider(ground)
    crate = rep.functional.create.reference(
        usd_path=assets_root_path + CRATE_USD,
        position=(0, 0, 0),
        scale=0.01,
        semantics={"class": "crate"},
        parent="/World",
        name="Crate",
    )
    rep.functional.physics.apply_collider(crate, approximation="none")  # Triangle mesh for concave geometry

    # Create the deformable physics materials, one per asset type
    materials = {}
    for label, _, _, youngs_modulus, poissons_ratio in assets_config:
        materials[label] = VolumeDeformableMaterial(
            f"/World/physics_materials/{label}",
            youngs_moduli=[float(youngs_modulus)],
            poissons_ratios=[float(poissons_ratio)],
        )
        print(f"[SDG]  Created deformable material for {label}: {materials[label].paths[0]}")

    # Create asset prims: cook the first of each type, clone the rest
    # Clones inherit all deformable physics, avoiding redundant cooking
    all_prims = []
    labels = []
    for label, count, usd_path, _, _ in assets_config:
        for i in range(count):
            if i == 0:
                # Create + cook deformable physics + apply material
                prim = rep.functional.create.reference(
                    usd_path=assets_root_path + usd_path,
                    semantics={"class": label},
                    parent="/World",
                    name=f"{label.capitalize()}_{i}",
                )
                first_path = prim.GetPath().pathString
                deformable = DeformablePrim(first_path, deformable_type="volume")
                deformable.apply_physics_materials(materials[label])
            else:
                # Clone inherits cooked deformable physics and material
                prim = rep.functional.create.clone(
                    first_path,
                    parent="/World",
                    name=f"{label.capitalize()}_{i}",
                )
            all_prims.append(prim)
            labels.append(label)
            print(f"[SDG]  {prim.GetPath()} ({'created' if i == 0 else 'cloned'})")
    total = len(all_prims)

    # Assign random drop heights and Z-axis rotations
    positions, rotations = [], []
    for i in range(total):
        x = rng.uniform(-SPAWN_XY_JITTER, SPAWN_XY_JITTER)
        y = rng.uniform(-SPAWN_XY_JITTER, SPAWN_XY_JITTER)
        z = BASE_DROP_HEIGHT + i * HEIGHT_STEP
        positions.append((x, y, z))
        rotations.append((0, 0, rng.uniform(0, 360)))
    rep.functional.modify.pose(all_prims, position_value=positions, rotation_value=rotations)

    # Cache asset shader prims for material randomization, each capture trigger the shader color will change once
    shaders = []
    for prim in all_prims:
        asset_shaders = []
        for child in Usd.PrimRange(prim):
            if child.IsA(UsdShade.Shader):
                asset_shaders.append(child)
        shaders.append(asset_shaders)

    # Replicator setup, render product is disabled by default and enabled only at capture time
    camera = rep.functional.create.camera(position=(1, 1, 1), look_at=(0, 0, 0), parent="/World", name="Camera")
    render_product = rep.create.render_product(camera, (720, 480))
    render_product.hydra_texture.set_updates_enabled(False)
    output_dir = os.path.join(os.getcwd(), "_out_deformable_drop")
    backend = rep.backends.get("DiskBackend")
    backend.initialize(output_dir=output_dir)
    writer = rep.writers.get("BasicWriter")
    writer.initialize(backend=backend, rgb=True, semantic_segmentation=True, colorize_semantic_segmentation=True)
    writer.attach(render_product)

    # GPU physics required for deformable tensor API
    SimulationManager.set_physics_sim_device("cuda")
    SimulationManager.initialize_physics()

    # Keep track of which assets have been triggered
    triggered = [False] * total

    # Start the simulation
    print(f"[SDG] Starting simulation")
    timeline = omni.timeline.get_timeline_interface()
    timeline.play()

    # Wrap deformables for tensor API access (requires active simulation, no re-cooking)
    deformables = []
    for i in range(total):
        deformables.append(DeformablePrim(all_prims[i].GetPath().pathString))

    for _ in range(MAX_STEPS):
        # Advance the app which will advance the timeline (and implicitly the simulation)
        await omni.kit.app.get_app().next_update_async()

        # Detect assets whose lowest vertex crossed the trigger height
        newly_triggered = []
        for i in range(total):
            # Skip if the asset has already been triggered
            if triggered[i]:
                continue

            # Use the deformable prim's get_nodal_positions to get the actual mesh vertices (not xform, which is constant for deformables)
            node_positions, _, _ = deformables[i].get_nodal_positions()
            min_z = float(node_positions[0].numpy()[:, 2].min())

            # If the lowest vertex is below the trigger height, trigger the asset
            if min_z <= TRIGGER_HEIGHT:
                triggered[i] = True
                newly_triggered.append(i)

        # If a new asset has been triggered, enable the render product, randomize the material color and capture the asset
        if newly_triggered:
            render_product.hydra_texture.set_updates_enabled(True)
        for i in newly_triggered:
            color = Gf.Vec3f(rng.random(), rng.random(), rng.random())
            for shader_prim in shaders[i]:
                attr = shader_prim.GetAttribute("inputs:diffuse_tint")
                if not attr or not attr.IsValid():
                    attr = shader_prim.CreateAttribute("inputs:diffuse_tint", Sdf.ValueTypeNames.Color3f)
                attr.Set(color)
            print(f"[SDG]  Captured {all_prims[i].GetPath()}")
            await rep.orchestrator.step_async(delta_time=0.0, pause_timeline=False, rt_subframes=16)
        if newly_triggered:
            render_product.hydra_texture.set_updates_enabled(False)

        # If all assets have been triggered, stop the simulation
        if all(triggered):
            break

    # Pause the simulation and clean up resources
    print(f"[SDG] Simulation complete. {len(triggered)} frames saved to {output_dir}")
    timeline.pause()
    await rep.orchestrator.wait_until_complete_async()
    writer.detach()
    render_product.destroy()

asyncio.ensure_future(run_example_async(ASSETS_CONFIG))
```

Standalone Application

Synthetic Data Generation with Deformables

```python
"""Demonstrate synthetic data generation with deformable physics objects."""

from isaacsim import SimulationApp

simulation_app = SimulationApp(launch_config={"headless": False})

import os
import random

import carb.settings
import omni.kit.app
import omni.replicator.core as rep
import omni.timeline
import omni.usd
from isaacsim.core.experimental.materials import VolumeDeformableMaterial
from isaacsim.core.experimental.prims import DeformablePrim
from isaacsim.core.simulation_manager import SimulationManager
from isaacsim.storage.native import get_assets_root_path
from pxr import Gf, Sdf, Usd, UsdShade

TRIGGER_HEIGHT = 0.15  # Capture when lowest vertex falls below this (m)
BASE_DROP_HEIGHT = 0.2  # Starting height for first asset (m)
HEIGHT_STEP = 0.15  # Height increment between assets (m)
SPAWN_XY_JITTER = 0.07  # Random horizontal offset +/- (m)
RNG_SEED = 12  # Reproducible randomization seed
MAX_STEPS = 200  # Maximum simulation steps
CRATE_USD = "/Isaac/Props/PackingTable/props/SM_Crate_A08_Blue_01/SM_Crate_A08_Blue_01.usd"

# (label, count, usd_path, youngs_modulus_Pa [higher=stiffer], poissons_ratio [0=compressible, 0.5=incompressible])
ASSETS_CONFIG = [
    ("banana", 6, "/Isaac/Props/YCB/Axis_Aligned/011_banana.usd", 500_000, 0.45),
    ("large_marker", 5, "/Isaac/Props/YCB/Axis_Aligned/040_large_marker.usd", 9_000_000, 0.5),
]

def run_example(assets_config: list[tuple[str, int, str, float, float]]):
    """Run deformable drop simulation and capture frames on trigger height."""
    omni.usd.get_context().new_stage()
    assets_root_path = get_assets_root_path()
    rng = random.Random(RNG_SEED)

    # Disable capture on play, frames will be captured manually
    rep.orchestrator.set_capture_on_play(False)

    # Set DLSS to Quality mode (2) for best SDG results (Options: 0 (Performance), 1 (Balanced), 2 (Quality), 3 (Auto)
    carb.settings.get_settings().set("rtx/post/dlss/execMode", 2)

    rep.functional.create.xform(name="World")
    rep.functional.create.dome_light(intensity=500, parent="/World", name="DomeLight")
    ground = rep.functional.create.cube(position=(0, 0, -0.5), scale=(10, 10, 1))  # Thick to prevent tunneling
    rep.functional.physics.apply_collider(ground)
    crate = rep.functional.create.reference(
        usd_path=assets_root_path + CRATE_USD,
        position=(0, 0, 0),
        scale=0.01,
        semantics={"class": "crate"},
        parent="/World",
        name="Crate",
    )
    rep.functional.physics.apply_collider(crate, approximation="none")  # Triangle mesh for concave geometry

    # Create the deformable physics materials, one per asset type
    materials = {}
    for label, _, _, youngs_modulus, poissons_ratio in assets_config:
        materials[label] = VolumeDeformableMaterial(
            f"/World/physics_materials/{label}",
            youngs_moduli=[float(youngs_modulus)],
            poissons_ratios=[float(poissons_ratio)],
        )
        print(f"[SDG]  Created deformable material for {label}: {materials[label].paths[0]}")

    # Create asset prims: cook the first of each type, clone the rest
    # Clones inherit all deformable physics, avoiding redundant cooking
    all_prims = []
    labels = []
    for label, count, usd_path, _, _ in assets_config:
        for i in range(count):
            if i == 0:
                # Create + cook deformable physics + apply material
                prim = rep.functional.create.reference(
                    usd_path=assets_root_path + usd_path,
                    semantics={"class": label},
                    parent="/World",
                    name=f"{label.capitalize()}_{i}",
                )
                first_path = prim.GetPath().pathString
                deformable = DeformablePrim(first_path, deformable_type="volume")
                deformable.apply_physics_materials(materials[label])
            else:
                # Clone inherits cooked deformable physics and material
                prim = rep.functional.create.clone(
                    first_path,
                    parent="/World",
                    name=f"{label.capitalize()}_{i}",
                )
            all_prims.append(prim)
            labels.append(label)
            print(f"[SDG]  {prim.GetPath()} ({'created' if i == 0 else 'cloned'})")
    total = len(all_prims)

    # Assign random drop heights and Z-axis rotations
    positions, rotations = [], []
    for i in range(total):
        x = rng.uniform(-SPAWN_XY_JITTER, SPAWN_XY_JITTER)
        y = rng.uniform(-SPAWN_XY_JITTER, SPAWN_XY_JITTER)
        z = BASE_DROP_HEIGHT + i * HEIGHT_STEP
        positions.append((x, y, z))
        rotations.append((0, 0, rng.uniform(0, 360)))
    rep.functional.modify.pose(all_prims, position_value=positions, rotation_value=rotations)

    # Cache asset shader prims for material randomization, each capture trigger the shader color will change once
    shaders = []
    for prim in all_prims:
        asset_shaders = []
        for child in Usd.PrimRange(prim):
            if child.IsA(UsdShade.Shader):
                asset_shaders.append(child)
        shaders.append(asset_shaders)

    # Replicator setup, render product is disabled by default and enabled only at capture time
    camera = rep.functional.create.camera(position=(1, 1, 1), look_at=(0, 0, 0), parent="/World", name="Camera")
    render_product = rep.create.render_product(camera, (720, 480))
    render_product.hydra_texture.set_updates_enabled(False)
    output_dir = os.path.join(os.getcwd(), "_out_deformable_drop")
    backend = rep.backends.get("DiskBackend")
    backend.initialize(output_dir=output_dir)
    writer = rep.writers.get("BasicWriter")
    writer.initialize(backend=backend, rgb=True, semantic_segmentation=True, colorize_semantic_segmentation=True)
    writer.attach(render_product)

    # GPU physics required for deformable tensor API
    SimulationManager.set_physics_sim_device("cuda")
    SimulationManager.initialize_physics()

    # Keep track of which assets have been triggered
    triggered = [False] * total

    # Start the simulation
    print(f"[SDG] Starting simulation")
    timeline = omni.timeline.get_timeline_interface()
    timeline.play()

    # Wrap deformables for tensor API access (requires active simulation, no re-cooking)
    deformables = []
    for i in range(total):
        deformables.append(DeformablePrim(all_prims[i].GetPath().pathString))

    for _ in range(MAX_STEPS):
        # Advance the app which will advance the timeline (and implicitly the simulation)
        simulation_app.update()

        # Detect assets whose lowest vertex crossed the trigger height
        newly_triggered = []
        for i in range(total):
            # Skip if the asset has already been triggered
            if triggered[i]:
                continue

            # Use the deformable prim's get_nodal_positions to get the actual mesh vertices (not xform, which is constant for deformables)
            node_positions, _, _ = deformables[i].get_nodal_positions()
            min_z = float(node_positions[0].numpy()[:, 2].min())

            # If the lowest vertex is below the trigger height, trigger the asset
            if min_z <= TRIGGER_HEIGHT:
                triggered[i] = True
                newly_triggered.append(i)

        # If a new asset has been triggered, enable the render product, randomize the material color and capture the asset
        if newly_triggered:
            render_product.hydra_texture.set_updates_enabled(True)
        for i in newly_triggered:
            color = Gf.Vec3f(rng.random(), rng.random(), rng.random())
            for shader_prim in shaders[i]:
                attr = shader_prim.GetAttribute("inputs:diffuse_tint")
                if not attr or not attr.IsValid():
                    attr = shader_prim.CreateAttribute("inputs:diffuse_tint", Sdf.ValueTypeNames.Color3f)
                attr.Set(color)
            print(f"[SDG]  Captured {all_prims[i].GetPath()}")
            rep.orchestrator.step(delta_time=0.0, pause_timeline=False, rt_subframes=16)
        if newly_triggered:
            render_product.hydra_texture.set_updates_enabled(False)

        # If all assets have been triggered, stop the simulation
        if all(triggered):
            break

    # Pause the simulation and clean up resources
    print(f"[SDG] Simulation complete. {len(triggered)} frames saved to {output_dir}")
    timeline.pause()
    rep.orchestrator.wait_until_complete()
    writer.detach()
    render_product.destroy()

run_example(ASSETS_CONFIG)
```

On this page

* [Annotator and Custom Writer Data from Multiple Cameras](#annotator-and-custom-writer-data-from-multiple-cameras)
* [Synthetic Data Access at Specific Simulation Timepoints](#synthetic-data-access-at-specific-simulation-timepoints)
* [Custom Event Randomization and Writing](#custom-event-randomization-and-writing)
* [Motion Blur](#motion-blur)
* [Subscribers and Events at Custom FPS](#subscribers-and-events-at-custom-fps)
* [Accessing Writer and Annotator Data at Custom FPS](#accessing-writer-and-annotator-data-at-custom-fps)
* [Cosmos Writer Example](#cosmos-writer-example)
* [Synthetic Data Generation with Deformables](#synthetic-data-generation-with-deformables)

---

### Isaac Randomizers

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/replicator_tutorials/tutorial_replicator_isaac_randomizers.html

* [Synthetic Data Generation](../synthetic_data_generation/index.html)
* [Perception Data Generation (Replicator)](index.html)
* Randomization Snippets

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Randomization Snippets

Examples of randomization using USD and Isaac Sim APIs. These examples demonstrate how to randomize scenes for synthetic data generation (SDG) in scenarios where default [replicator randomizers](https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator/randomizer_details.html "(in Omniverse Extensions)") are not sufficient or applicable.

The snippets are designed to align with the structure and function names used in the replicator example snippets. In comparison they also have the option to write the data to disk by stetting `write_data=True`.

Prerequisites:

* Familiarity with [USD](https://developer.nvidia.com/usd/tutorials).
* Ability to execute code from the [Script Editor](../development_tools/omniverse_script_editor.html#script-editor).
* Understanding basic replicator concepts, such as [subframes](https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator/subframes_examples.html#subframes-examples "(in Omniverse Extensions)").

## Randomizing Light Sources

This snippet sets up a new environment containing a cube and a sphere.
It then spawns a given number of lights and randomizes selected attributes for these lights over a specified number of frames.

Randomizing Light Sources

```python
import asyncio
import os

import numpy as np
import omni.kit.commands
import omni.replicator.core as rep
import omni.usd
from isaacsim.core.experimental.utils.semantics import add_labels
from pxr import Gf, Sdf, UsdGeom

omni.usd.get_context().new_stage()
stage = omni.usd.get_context().get_stage()

sphere = stage.DefinePrim("/World/Sphere", "Sphere")
UsdGeom.Xformable(sphere).AddTranslateOp().Set((0.0, 1.0, 1.0))
add_labels(sphere, labels=["sphere"], taxonomy="class")

cube = stage.DefinePrim("/World/Cube", "Cube")
UsdGeom.Xformable(cube).AddTranslateOp().Set((0.0, -2.0, 2.0))
add_labels(cube, labels=["cube"], taxonomy="class")

plane_path = "/World/Plane"
omni.kit.commands.execute("CreateMeshPrimWithDefaultXform", prim_path=plane_path, prim_type="Plane")
plane_prim = stage.GetPrimAtPath(plane_path)
plane_prim.CreateAttribute("xformOp:scale", Sdf.ValueTypeNames.Double3, False).Set(Gf.Vec3d(10, 10, 1))

def sphere_lights(num):
    lights = []
    for i in range(num):
        # "CylinderLight", "DiskLight", "DistantLight", "DomeLight", "RectLight", "SphereLight"
        prim_type = "SphereLight"
        next_free_path = omni.usd.get_stage_next_free_path(stage, f"/World/{prim_type}", False)
        light_prim = stage.DefinePrim(next_free_path, prim_type)
        UsdGeom.Xformable(light_prim).AddTranslateOp().Set((0.0, 0.0, 0.0))
        UsdGeom.Xformable(light_prim).AddRotateXYZOp().Set((0.0, 0.0, 0.0))
        UsdGeom.Xformable(light_prim).AddScaleOp().Set((1.0, 1.0, 1.0))
        light_prim.CreateAttribute("inputs:enableColorTemperature", Sdf.ValueTypeNames.Bool).Set(True)
        light_prim.CreateAttribute("inputs:colorTemperature", Sdf.ValueTypeNames.Float).Set(6500.0)
        light_prim.CreateAttribute("inputs:radius", Sdf.ValueTypeNames.Float).Set(0.5)
        light_prim.CreateAttribute("inputs:intensity", Sdf.ValueTypeNames.Float).Set(30000.0)
        light_prim.CreateAttribute("inputs:color", Sdf.ValueTypeNames.Color3f).Set((1.0, 1.0, 1.0))
        light_prim.CreateAttribute("inputs:exposure", Sdf.ValueTypeNames.Float).Set(0.0)
        light_prim.CreateAttribute("inputs:diffuse", Sdf.ValueTypeNames.Float).Set(1.0)
        light_prim.CreateAttribute("inputs:specular", Sdf.ValueTypeNames.Float).Set(1.0)
        lights.append(light_prim)
    return lights

async def run_randomizations_async(num_frames, lights, write_data, delay=None):
    if write_data:
        out_dir = os.path.join(os.getcwd(), "_out_rand_lights")
        print(f"Writing data to {out_dir}..")
        backend = rep.backends.get("DiskBackend")
        backend.initialize(output_dir=out_dir)
        writer = rep.WriterRegistry.get("BasicWriter")
        writer.initialize(backend=backend, rgb=True)
        cam = rep.functional.create.camera(position=(5, 5, 5), look_at=(0, 0, 0), name="Camera")
        rp = rep.create.render_product(cam, resolution=(512, 512))
        writer.attach(rp)

    for _ in range(num_frames):
        for light in lights:
            light.GetAttribute("xformOp:translate").Set(
                (np.random.uniform(-5, 5), np.random.uniform(-5, 5), np.random.uniform(4, 6))
            )
            scale_rand = np.random.uniform(0.5, 1.5)
            light.GetAttribute("xformOp:scale").Set((scale_rand, scale_rand, scale_rand))
            light.GetAttribute("inputs:colorTemperature").Set(np.random.normal(4500, 1500))
            light.GetAttribute("inputs:intensity").Set(np.random.normal(25000, 5000))
            light.GetAttribute("inputs:color").Set(
                (np.random.uniform(0.1, 0.9), np.random.uniform(0.1, 0.9), np.random.uniform(0.1, 0.9))
            )

        if write_data:
            await rep.orchestrator.step_async(rt_subframes=16)
        else:
            await omni.kit.app.get_app().next_update_async()
        # Optional delay between frames to better visualize the randomization in the viewport
        if delay is not None and delay > 0:
            await asyncio.sleep(delay)

    # Wait for the data to be written to disk and cleanup writer and render product
    if write_data:
        await rep.orchestrator.wait_until_complete_async()
        writer.detach()
        rp.destroy()

num_frames = 10
lights = sphere_lights(10)
asyncio.ensure_future(run_randomizations_async(num_frames=num_frames, lights=lights, write_data=True, delay=0.2))
```

## Randomizing Textures

The snippet sets up an environment, spawns a given number of cubes and spheres, and randomizes their textures for the given number of frames. After the randomizations their original materials are reassigned. The snippet also showcases how to create a new material and assign it to a prim.

Randomizing Textures

```python
import asyncio
import os

import numpy as np
import omni.replicator.core as rep
import omni.usd
from isaacsim.core.experimental.utils.semantics import add_labels, get_labels
from isaacsim.storage.native import get_assets_root_path_async
from pxr import Gf, Sdf, UsdGeom, UsdShade

omni.usd.get_context().new_stage()
stage = omni.usd.get_context().get_stage()
dome_light = stage.DefinePrim("/World/DomeLight", "DomeLight")
dome_light.CreateAttribute("inputs:intensity", Sdf.ValueTypeNames.Float).Set(1000.0)

sphere = stage.DefinePrim("/World/Sphere", "Sphere")
UsdGeom.Xformable(sphere).AddTranslateOp().Set((0.0, 0.0, 1.0))
add_labels(sphere, labels=["sphere"], taxonomy="class")

num_cubes = 10
for _ in range(num_cubes):
    prim_type = "Cube"
    next_free_path = omni.usd.get_stage_next_free_path(stage, f"/World/{prim_type}", False)
    cube = stage.DefinePrim(next_free_path, prim_type)
    UsdGeom.Xformable(cube).AddTranslateOp().Set((np.random.uniform(-3.5, 3.5), np.random.uniform(-3.5, 3.5), 1))
    scale_rand = np.random.uniform(0.25, 0.5)
    UsdGeom.Xformable(cube).AddScaleOp().Set((scale_rand, scale_rand, scale_rand))
    add_labels(cube, labels=["cube"], taxonomy="class")

plane_path = "/World/Plane"
omni.kit.commands.execute("CreateMeshPrimWithDefaultXform", prim_path=plane_path, prim_type="Plane")
plane_prim = stage.GetPrimAtPath(plane_path)
plane_prim.CreateAttribute("xformOp:scale", Sdf.ValueTypeNames.Double3, False).Set(Gf.Vec3d(10, 10, 1))

def get_shapes():
    stage = omni.usd.get_context().get_stage()
    shapes = []
    for prim in stage.Traverse():
        labels = get_labels(prim)
        if class_labels := labels.get("class"):
            if "cube" in class_labels or "sphere" in class_labels:
                shapes.append(prim)
    return shapes

shapes = get_shapes()

def create_omnipbr_material(mtl_url, mtl_name, mtl_path):
    stage = omni.usd.get_context().get_stage()
    omni.kit.commands.execute("CreateMdlMaterialPrim", mtl_url=mtl_url, mtl_name=mtl_name, mtl_path=mtl_path)
    material_prim = stage.GetPrimAtPath(mtl_path)
    shader = UsdShade.Shader(omni.usd.get_shader_from_material(material_prim, get_prim=True))

    # Add value inputs
    shader.CreateInput("diffuse_color_constant", Sdf.ValueTypeNames.Color3f)
    shader.CreateInput("reflection_roughness_constant", Sdf.ValueTypeNames.Float)
    shader.CreateInput("metallic_constant", Sdf.ValueTypeNames.Float)

    # Add texture inputs
    shader.CreateInput("diffuse_texture", Sdf.ValueTypeNames.Asset)
    shader.CreateInput("reflectionroughness_texture", Sdf.ValueTypeNames.Asset)
    shader.CreateInput("metallic_texture", Sdf.ValueTypeNames.Asset)

    # Add other attributes
    shader.CreateInput("project_uvw", Sdf.ValueTypeNames.Bool)

    # Add texture scale and rotate
    shader.CreateInput("texture_scale", Sdf.ValueTypeNames.Float2)
    shader.CreateInput("texture_rotate", Sdf.ValueTypeNames.Float)

    material = UsdShade.Material(material_prim)
    return material

def create_materials(num):
    MDL = "OmniPBR.mdl"
    mtl_name, _ = os.path.splitext(MDL)
    MAT_PATH = "/World/Looks"
    materials = []
    for _ in range(num):
        prim_path = omni.usd.get_stage_next_free_path(stage, f"{MAT_PATH}/{mtl_name}", False)
        mat = create_omnipbr_material(mtl_url=MDL, mtl_name=mtl_name, mtl_path=prim_path)
        materials.append(mat)
    return materials

materials = create_materials(len(shapes))

async def run_randomizations_async(num_frames, materials, write_data, delay=None):
    assets_root_path = await get_assets_root_path_async()
    textures = [
        assets_root_path + "/NVIDIA/Materials/vMaterials_2/Ground/textures/aggregate_exposed_diff.jpg",
        assets_root_path + "/NVIDIA/Materials/vMaterials_2/Ground/textures/gravel_track_ballast_diff.jpg",
        assets_root_path + "/NVIDIA/Materials/vMaterials_2/Ground/textures/gravel_track_ballast_multi_R_rough_G_ao.jpg",
        assets_root_path + "/NVIDIA/Materials/vMaterials_2/Ground/textures/rough_gravel_rough.jpg",
    ]

    if write_data:
        out_dir = os.path.join(os.getcwd(), "_out_rand_textures")
        print(f"Writing data to {out_dir}..")
        backend = rep.backends.get("DiskBackend")
        backend.initialize(output_dir=out_dir)
        writer = rep.WriterRegistry.get("BasicWriter")
        writer.initialize(backend=backend, rgb=True)
        cam = rep.functional.create.camera(position=(5, 5, 5), look_at=(0, 0, 0), name="Camera")
        rp = rep.create.render_product(cam, resolution=(512, 512))
        writer.attach(rp)

    # Apply the new materials and store the initial ones to reassign later
    initial_materials = {}
    for i, shape in enumerate(shapes):
        cur_mat, _ = UsdShade.MaterialBindingAPI(shape).ComputeBoundMaterial()
        initial_materials[shape] = cur_mat
        UsdShade.MaterialBindingAPI(shape).Bind(materials[i], UsdShade.Tokens.strongerThanDescendants)

    for _ in range(num_frames):
        for mat in materials:
            shader = UsdShade.Shader(omni.usd.get_shader_from_material(mat, get_prim=True))
            diffuse_texture = np.random.choice(textures)
            shader.GetInput("diffuse_texture").Set(diffuse_texture)
            project_uvw = np.random.choice([True, False], p=[0.9, 0.1])
            shader.GetInput("project_uvw").Set(bool(project_uvw))
            texture_scale = np.random.uniform(0.1, 1)
            shader.GetInput("texture_scale").Set((texture_scale, texture_scale))
            texture_rotate = np.random.uniform(0, 45)
            shader.GetInput("texture_rotate").Set(texture_rotate)

        if write_data:
            await rep.orchestrator.step_async(rt_subframes=4)
        else:
            await omni.kit.app.get_app().next_update_async()

        # Optional delay between frames to better visualize the randomization in the viewport
        if delay is not None and delay > 0:
            await asyncio.sleep(delay)

    # Wait for the data to be written to disk and cleanup writer and render product
    if write_data:
        await rep.orchestrator.wait_until_complete_async()
        writer.detach()
        rp.destroy()

    # Reassign the initial materials
    for shape, mat in initial_materials.items():
        if mat:
            UsdShade.MaterialBindingAPI(shape).Bind(mat, UsdShade.Tokens.strongerThanDescendants)
        else:
            UsdShade.MaterialBindingAPI(shape).UnbindAllBindings()

num_frames = 10
asyncio.ensure_future(run_randomizations_async(num_frames, materials, write_data=True, delay=0.2))
```

## Sequential Randomizations

The snippet provides an example of more complex randomizations, where the results of the first randomization are used to determine the next randomization. It uses a custom sampler function to set the location of the camera by iterating over (almost) equidistant points on a sphere. The snippet starts by setting up the environment, a forklift, a pallet, a bin, and a dome light. For every randomization frame, it cycles through the dome light textures, moves the pallet to a random location, and then moves the bin so that it is fully on top of the pallet. Finally, it moves the camera to a new location on the sphere, ensuring it faces the bin.

Sequential Randomizations

```python
import asyncio
import itertools
import os

import numpy as np
import omni.replicator.core as rep
import omni.usd
from isaacsim.storage.native import get_assets_root_path_async
from pxr import Gf, Usd, UsdGeom, UsdLux

# Fibonacci sphere algorithm: https://arxiv.org/pdf/0912.4540
def next_point_on_sphere(idx, num_points, radius=1, origin=(0, 0, 0)):
    offset = 2.0 / num_points
    inc = np.pi * (3.0 - np.sqrt(5.0))
    z = ((idx * offset) - 1) + (offset / 2)
    phi = ((idx + 1) % num_points) * inc
    r = np.sqrt(1 - pow(z, 2))
    y = np.cos(phi) * r
    x = np.sin(phi) * r
    return [(x * radius) + origin[0], (y * radius) + origin[1], (z * radius) + origin[2]]

async def run_randomizations_async(
    num_frames, forklift_path, pallet_path, bin_path, dome_textures, write_data, delay=None
):
    assets_root_path = await get_assets_root_path_async()

    await omni.usd.get_context().new_stage_async()
    stage = omni.usd.get_context().get_stage()

    dome_light = UsdLux.DomeLight.Define(stage, "/World/Lights/DomeLight")
    dome_light.GetIntensityAttr().Set(1000)

    forklift_prim = stage.DefinePrim("/World/Forklift", "Xform")
    forklift_prim.GetReferences().AddReference(assets_root_path + forklift_path)
    if not forklift_prim.GetAttribute("xformOp:translate"):
        UsdGeom.Xformable(forklift_prim).AddTranslateOp()
    forklift_prim.GetAttribute("xformOp:translate").Set((-4.5, -4.5, 0))

    pallet_prim = stage.DefinePrim("/World/Pallet", "Xform")
    pallet_prim.GetReferences().AddReference(assets_root_path + pallet_path)
    if not pallet_prim.GetAttribute("xformOp:translate"):
        UsdGeom.Xformable(pallet_prim).AddTranslateOp()
    if not pallet_prim.GetAttribute("xformOp:rotateXYZ"):
        UsdGeom.Xformable(pallet_prim).AddRotateXYZOp()

    bin_prim = stage.DefinePrim("/World/Bin", "Xform")
    bin_prim.GetReferences().AddReference(assets_root_path + bin_path)
    if not bin_prim.GetAttribute("xformOp:translate"):
        UsdGeom.Xformable(bin_prim).AddTranslateOp()
    if not bin_prim.GetAttribute("xformOp:rotateXYZ"):
        UsdGeom.Xformable(bin_prim).AddRotateXYZOp()

    view_cam = stage.DefinePrim("/World/Camera", "Camera")
    if not view_cam.GetAttribute("xformOp:translate"):
        UsdGeom.Xformable(view_cam).AddTranslateOp()
    if not view_cam.GetAttribute("xformOp:orient"):
        UsdGeom.Xformable(view_cam).AddOrientOp()

    dome_textures_full = [assets_root_path + tex for tex in dome_textures]
    textures_cycle = itertools.cycle(dome_textures_full)

    if write_data:
        out_dir = os.path.join(os.getcwd(), "_out_rand_sphere_scan")
        print(f"Writing data to {out_dir}..")
        backend = rep.backends.get("DiskBackend")
        backend.initialize(output_dir=out_dir)
        writer = rep.WriterRegistry.get("BasicWriter")
        writer.initialize(backend=backend, rgb=True)
        persp_cam = rep.functional.create.camera(position=(5, 5, 5), look_at=(0, 0, 0), name="PerspCamera")
        rp_persp = rep.create.render_product(persp_cam, (512, 512), name="PerspView")
        rp_view = rep.create.render_product(view_cam, (512, 512), name="SphereView")
        writer.attach([rp_view, rp_persp])

    bb_cache = UsdGeom.BBoxCache(time=Usd.TimeCode.Default(), includedPurposes=[UsdGeom.Tokens.default_])
    pallet_size = bb_cache.ComputeWorldBound(pallet_prim).GetRange().GetSize()
    pallet_length = pallet_size.GetLength()
    bin_size = bb_cache.ComputeWorldBound(bin_prim).GetRange().GetSize()

    for i in range(num_frames):
        # Set next background texture every nth frame and run an app update
        if i % 5 == 0:
            dome_light.GetTextureFileAttr().Set(next(textures_cycle))
            await omni.kit.app.get_app().next_update_async()

        # Randomize pallet pose
        pallet_prim.GetAttribute("xformOp:translate").Set(
            Gf.Vec3d(np.random.uniform(-1.5, 1.5), np.random.uniform(-1.5, 1.5), 0)
        )
        rand_z_rot = np.random.uniform(-90, 90)
        pallet_prim.GetAttribute("xformOp:rotateXYZ").Set(Gf.Vec3d(0, 0, rand_z_rot))
        pallet_tf_mat = omni.usd.get_world_transform_matrix(pallet_prim)
        pallet_rot = pallet_tf_mat.ExtractRotation()
        pallet_pos = pallet_tf_mat.ExtractTranslation()

        # Randomize bin position on top of the rotated pallet area making sure the bin is fully on the pallet
        rand_transl_x = np.random.uniform(-pallet_size[0] / 2 + bin_size[0] / 2, pallet_size[0] / 2 - bin_size[0] / 2)
        rand_transl_y = np.random.uniform(-pallet_size[1] / 2 + bin_size[1] / 2, pallet_size[1] / 2 - bin_size[1] / 2)

        # Adjust bin position to account for the random rotation of the pallet
        rand_z_rot_rad = np.deg2rad(rand_z_rot)
        rot_adjusted_transl_x = rand_transl_x * np.cos(rand_z_rot_rad) - rand_transl_y * np.sin(rand_z_rot_rad)
        rot_adjusted_transl_y = rand_transl_x * np.sin(rand_z_rot_rad) + rand_transl_y * np.cos(rand_z_rot_rad)
        bin_prim.GetAttribute("xformOp:translate").Set(
            Gf.Vec3d(
                pallet_pos[0] + rot_adjusted_transl_x,
                pallet_pos[1] + rot_adjusted_transl_y,
                pallet_pos[2] + pallet_size[2] + bin_size[2] / 2,
            )
        )
        # Keep bin rotation aligned with pallet
        bin_prim.GetAttribute("xformOp:rotateXYZ").Set(pallet_rot.GetAxis() * pallet_rot.GetAngle())

        # Get next camera position on a sphere looking at the bin with a randomized distance
        rand_radius = np.random.normal(3, 0.5) * pallet_length
        bin_pos = omni.usd.get_world_transform_matrix(bin_prim).ExtractTranslation()
        cam_pos = next_point_on_sphere(i, num_points=num_frames, radius=rand_radius, origin=bin_pos)
        view_cam.GetAttribute("xformOp:translate").Set(Gf.Vec3d(*cam_pos))

        eye = Gf.Vec3d(*cam_pos)
        target = Gf.Vec3d(*bin_pos)
        up_axis = Gf.Vec3d(0, 0, 1)
        look_at_quatd = Gf.Matrix4d().SetLookAt(eye, target, up_axis).GetInverse().ExtractRotation().GetQuat()
        view_cam.GetAttribute("xformOp:orient").Set(Gf.Quatf(look_at_quatd))

        if write_data:
            await rep.orchestrator.step_async(rt_subframes=4, delta_time=0.0)
        else:
            await omni.kit.app.get_app().next_update_async()
        # Optional delay between frames to better visualize the randomization in the viewport
        if delay is not None and delay > 0:
            await asyncio.sleep(delay)

    # Wait for the data to be written to disk and cleanup writer and render products
    if write_data:
        await rep.orchestrator.wait_until_complete_async()
        writer.detach()
        rp_persp.destroy()
        rp_view.destroy()

NUM_FRAMES = 90
FORKLIFT_PATH = "/Isaac/Props/Forklift/forklift.usd"
PALLET_PATH = "/Isaac/Props/Pallet/pallet.usd"
BIN_PATH = "/Isaac/Props/KLT_Bin/small_KLT_visual.usd"
DOME_TEXTURES = [
    "/NVIDIA/Assets/Skies/Cloudy/champagne_castle_1_4k.hdr",
    "/NVIDIA/Assets/Skies/Clear/evening_road_01_4k.hdr",
    "/NVIDIA/Assets/Skies/Clear/mealie_road_4k.hdr",
    "/NVIDIA/Assets/Skies/Clear/qwantani_4k.hdr",
]
asyncio.ensure_future(
    run_randomizations_async(
        NUM_FRAMES, FORKLIFT_PATH, PALLET_PATH, BIN_PATH, DOME_TEXTURES, write_data=True, delay=0.2
    )
)
```

## Physics-based Randomized Volume Filling

The snippet randomizes the stacking of objects on multiple surfaces. It randomly spawns a given number of pallets in the selected areas and then spawns physically simulated boxes on top of them. A temporary collision box area is created around the pallets to prevent the boxes from falling off. After all the boxes have been dropped, they are moved in various directions and finally pulled towards the center of the pallet for more stable stacking. Finally, the collision area is removed, after which the boxes can also fall to the ground. To allow easier sliding of the boxes into more stable positions, their friction is temporarily reduced during the simulation.

Physics-based Randomized Volume Filling

```python
import asyncio
import os
import random
from itertools import chain

import carb
import omni.kit.app
import omni.physx
import omni.replicator.core as rep
import omni.usd
from isaacsim.storage.native import get_assets_root_path_async
from pxr import Gf, PhysicsSchemaTools, PhysxSchema, Sdf, Usd, UsdGeom, UsdPhysics, UsdShade, UsdUtils

# Add transformation properties to the prim (if not already present)
def set_transform_attributes(prim, location=None, orientation=None, rotation=None, scale=None):
    if location is not None:
        if not prim.HasAttribute("xformOp:translate"):
            UsdGeom.Xformable(prim).AddTranslateOp()
        prim.GetAttribute("xformOp:translate").Set(location)
    if orientation is not None:
        if not prim.HasAttribute("xformOp:orient"):
            UsdGeom.Xformable(prim).AddOrientOp()
        prim.GetAttribute("xformOp:orient").Set(orientation)
    if rotation is not None:
        if not prim.HasAttribute("xformOp:rotateXYZ"):
            UsdGeom.Xformable(prim).AddRotateXYZOp()
        prim.GetAttribute("xformOp:rotateXYZ").Set(rotation)
    if scale is not None:
        if not prim.HasAttribute("xformOp:scale"):
            UsdGeom.Xformable(prim).AddScaleOp()
        prim.GetAttribute("xformOp:scale").Set(scale)

# Enables collisions with the asset (without rigid body dynamics the asset will be static)
def add_colliders(prim):
    # Iterate descendant prims (including root) and add colliders to mesh or primitive types
    for desc_prim in Usd.PrimRange(prim):
        if desc_prim.IsA(UsdGeom.Mesh) or desc_prim.IsA(UsdGeom.Gprim):
            # Physics
            if not desc_prim.HasAPI(UsdPhysics.CollisionAPI):
                collision_api = UsdPhysics.CollisionAPI.Apply(desc_prim)
            else:
                collision_api = UsdPhysics.CollisionAPI(desc_prim)
            collision_api.CreateCollisionEnabledAttr(True)

        # Add mesh specific collision properties only to mesh types
        if desc_prim.IsA(UsdGeom.Mesh):
            if not desc_prim.HasAPI(UsdPhysics.MeshCollisionAPI):
                mesh_collision_api = UsdPhysics.MeshCollisionAPI.Apply(desc_prim)
            else:
                mesh_collision_api = UsdPhysics.MeshCollisionAPI(desc_prim)
            mesh_collision_api.CreateApproximationAttr().Set("convexHull")

# Enables rigid body dynamics (physics simulation) on the prim (having valid colliders is recommended)
def add_rigid_body_dynamics(prim, disable_gravity=False, angular_damping=None):
    # Physics
    if not prim.HasAPI(UsdPhysics.RigidBodyAPI):
        rigid_body_api = UsdPhysics.RigidBodyAPI.Apply(prim)
    else:
        rigid_body_api = UsdPhysics.RigidBodyAPI(prim)
    rigid_body_api.CreateRigidBodyEnabledAttr(True)
    # PhysX
    if not prim.HasAPI(PhysxSchema.PhysxRigidBodyAPI):
        physx_rigid_body_api = PhysxSchema.PhysxRigidBodyAPI.Apply(prim)
    else:
        physx_rigid_body_api = PhysxSchema.PhysxRigidBodyAPI(prim)
    physx_rigid_body_api.GetDisableGravityAttr().Set(disable_gravity)
    if angular_damping is not None:
        physx_rigid_body_api.CreateAngularDampingAttr().Set(angular_damping)

# Create a new prim with the provided asset URL and transform properties
def create_asset(stage, asset_url, path, location=None, rotation=None, orientation=None, scale=None):
    prim_path = omni.usd.get_stage_next_free_path(stage, path, False)
    prim = stage.DefinePrim(prim_path, "Xform")
    prim.GetReferences().AddReference(asset_url)
    set_transform_attributes(prim, location=location, rotation=rotation, orientation=orientation, scale=scale)
    return prim

# Create a new prim with the provided asset URL and transform properties including colliders
def create_asset_with_colliders(stage, asset_url, path, location=None, rotation=None, orientation=None, scale=None):
    prim = create_asset(stage, asset_url, path, location, rotation, orientation, scale)
    add_colliders(prim)
    return prim

# Create collision walls around the top surface of the prim with the given height and thickness
def create_collision_walls(stage, prim, bbox_cache=None, height=2, thickness=0.3, material=None, visible=False):
    # Use the untransformed axis-aligned bounding box to calculate the prim surface size and center
    if bbox_cache is None:
        bbox_cache = UsdGeom.BBoxCache(Usd.TimeCode.Default(), includedPurposes=[UsdGeom.Tokens.default_])
    local_range = bbox_cache.ComputeWorldBound(prim).GetRange()
    width, depth, local_height = local_range.GetSize()
    # Raise the midpoint height to the prim's surface
    mid = local_range.GetMidpoint() + Gf.Vec3d(0, 0, local_height / 2)

    # Define the walls (name, location, size) with the specified thickness added externally to the surface and height
    walls = [
        ("floor", (mid[0], mid[1], mid[2] - thickness / 2), (width, depth, thickness)),
        ("ceiling", (mid[0], mid[1], mid[2] + height + thickness / 2), (width, depth, thickness)),
        (
            "left_wall",
            (mid[0] - (width + thickness) / 2, mid[1], mid[2] + height / 2),
            (thickness, depth, height),
        ),
        (
            "right_wall",
            (mid[0] + (width + thickness) / 2, mid[1], mid[2] + height / 2),
            (thickness, depth, height),
        ),
        (
            "front_wall",
            (mid[0], mid[1] + (depth + thickness) / 2, mid[2] + height / 2),
            (width, thickness, height),
        ),
        (
            "back_wall",
            (mid[0], mid[1] - (depth + thickness) / 2, mid[2] + height / 2),
            (width, thickness, height),
        ),
    ]

    # Use the parent prim path to create the walls as children (use local coordinates)
    prim_path = prim.GetPath()
    collision_walls = []
    for name, location, size in walls:
        prim = stage.DefinePrim(f"{prim_path}/{name}", "Cube")
        scale = (size[0] / 2.0, size[1] / 2.0, size[2] / 2.0)
        set_transform_attributes(prim, location=location, scale=scale)
        add_colliders(prim)
        if not visible:
            UsdGeom.Imageable(prim).MakeInvisible()
        if material is not None:
            mat_binding_api = UsdShade.MaterialBindingAPI.Apply(prim)
            mat_binding_api.Bind(material, UsdShade.Tokens.weakerThanDescendants, "physics")
        collision_walls.append(prim)
    return collision_walls

# Slide the assets independently in perpendicular directions and then pull them all together towards the given center
async def apply_forces_async(stage, boxes, pallet, strength=550, strength_center_multiplier=2):
    timeline = omni.timeline.get_timeline_interface()
    timeline.play()
    # Get the pallet center and forward vector to apply forces in the perpendicular directions and towards the center
    pallet_tf: Gf.Matrix4d = UsdGeom.Xformable(pallet).ComputeLocalToWorldTransform(Usd.TimeCode.Default())
    pallet_center = pallet_tf.ExtractTranslation()
    pallet_rot: Gf.Rotation = pallet_tf.ExtractRotation()
    force_forward = Gf.Vec3d(pallet_rot.TransformDir(Gf.Vec3d(1, 0, 0))) * strength
    force_right = Gf.Vec3d(pallet_rot.TransformDir(Gf.Vec3d(0, 1, 0))) * strength

    physx_simulation_interface = omni.physx.get_physx_simulation_interface()
    stage_id = UsdUtils.StageCache.Get().GetId(stage).ToLongInt()
    for box_prim in boxes:
        body_path = PhysicsSchemaTools.sdfPathToInt(box_prim.GetPath())
        forces = [force_forward, force_right, -force_forward, -force_right]
        for force in chain(forces, forces):
            box_tf: Gf.Matrix4d = UsdGeom.Xformable(box_prim).ComputeLocalToWorldTransform(Usd.TimeCode.Default())
            box_position = carb.Float3(*box_tf.ExtractTranslation())
            physx_simulation_interface.apply_force_at_pos(stage_id, body_path, carb.Float3(*force), box_position)
            for _ in range(10):
                await omni.kit.app.get_app().next_update_async()

    # Pull all boxes at once to the pallet center
    for box_prim in boxes:
        body_path = PhysicsSchemaTools.sdfPathToInt(box_prim.GetPath())
        box_tf: Gf.Matrix4d = UsdGeom.Xformable(box_prim).ComputeLocalToWorldTransform(Usd.TimeCode.Default())
        box_location = box_tf.ExtractTranslation()
        force_to_center = (pallet_center - box_location) * strength * strength_center_multiplier
        physx_simulation_interface.apply_force_at_pos(
            stage_id,
            body_path,
            carb.Float3(*force_to_center),
            carb.Float3(*box_location),
        )
    for _ in range(20):
        await omni.kit.app.get_app().next_update_async()
    timeline.pause()

# Create a new stage and and run the example scenario
async def stack_boxes_on_pallet_async(pallet_prim, boxes_urls_and_weights, num_boxes, drop_height=1.5, drop_margin=0.2):
    pallet_path = pallet_prim.GetPath()
    print(f"[BoxStacking] Running scenario for pallet {pallet_path} with {num_boxes} boxes..")
    stage = omni.usd.get_context().get_stage()
    bbox_cache = UsdGeom.BBoxCache(Usd.TimeCode.Default(), includedPurposes=[UsdGeom.Tokens.default_])

    # Create a custom physics material to allow the boxes to easily slide into stacking positions
    material_path = f"{pallet_path}/Looks/PhysicsMaterial"
    default_material = UsdShade.Material.Define(stage, material_path)
    physics_material = UsdPhysics.MaterialAPI.Apply(default_material.GetPrim())
    physics_material.CreateRestitutionAttr().Set(0.0)  # Inelastic collision (no bouncing)
    physics_material.CreateStaticFrictionAttr().Set(0.01)  # Small friction to allow sliding of stationary boxes
    physics_material.CreateDynamicFrictionAttr().Set(0.01)  # Small friction to allow sliding of moving boxes

    # Apply the physics material to the pallet
    mat_binding_api = UsdShade.MaterialBindingAPI.Apply(pallet_prim)
    mat_binding_api.Bind(default_material, UsdShade.Tokens.weakerThanDescendants, "physics")

    # Create collision walls around the top of the pallet and apply the physics material to them
    collision_walls = create_collision_walls(
        stage, pallet_prim, bbox_cache, height=drop_height + drop_margin, material=default_material
    )

    # Create the random boxes (without physics) with the specified weights and sort them by size (volume)
    box_urls, box_weights = zip(*boxes_urls_and_weights)
    rand_boxes_urls = random.choices(box_urls, weights=box_weights, k=num_boxes)
    boxes = [create_asset(stage, box_url, f"{pallet_path}_Boxes/Box_{i}") for i, box_url in enumerate(rand_boxes_urls)]
    boxes.sort(key=lambda box: bbox_cache.ComputeLocalBound(box).GetVolume(), reverse=True)

    # Calculate the drop area above the pallet taking into account the pallet surface, drop height and the margin
    # Note: The boxes can be spawned colliding with the surrounding collision walls as they will be pushed inwards
    pallet_range = bbox_cache.ComputeWorldBound(pallet_prim).GetRange()
    pallet_width, pallet_depth, pallet_heigth = pallet_range.GetSize()
    # Move the spawn center at the given height above the pallet surface
    spawn_center = pallet_range.GetMidpoint() + Gf.Vec3d(0, 0, pallet_heigth / 2 + drop_height)
    spawn_width, spawn_depth = pallet_width / 2 - drop_margin, pallet_depth / 2 - drop_margin

    # Use the pallet local-to-world transform to apply the local random offsets relative to the pallet
    pallet_tf: Gf.Matrix4d = UsdGeom.Xformable(pallet_prim).ComputeLocalToWorldTransform(Usd.TimeCode.Default())
    pallet_rot: Gf.Rotation = pallet_tf.ExtractRotation()

    # Simulate dropping the boxes from random poses on the pallet
    timeline = omni.timeline.get_timeline_interface()
    for box_prim in boxes:
        # Create a random location and orientation for the box within the drop area in local frame
        local_loc = spawn_center + Gf.Vec3d(
            random.uniform(-spawn_width, spawn_width), random.uniform(-spawn_depth, spawn_depth), 0
        )
        axes = [Gf.Vec3d(1, 0, 0), Gf.Vec3d(0, 1, 0), Gf.Vec3d(0, 0, 1)]
        angles = [random.choice([180, 90, 0, -90, -180]) + random.uniform(-3, 3) for _ in axes]
        local_rot = Gf.Rotation()
        for axis, angle in zip(axes, angles):
            local_rot *= Gf.Rotation(axis, angle)

        # Transform the local pose to the pallet's world coordinate system
        world_loc = pallet_tf.Transform(local_loc)
        world_quat = Gf.Quatf((pallet_rot * local_rot).GetQuat())

        # Set the spawn pose and enable collisions and rigid body dynamics with dampened angular movements
        set_transform_attributes(box_prim, location=world_loc, orientation=world_quat)
        add_colliders(box_prim)
        add_rigid_body_dynamics(box_prim, angular_damping=0.9)

        # Bind the physics material to the box (allow frictionless sliding)
        mat_binding_api = UsdShade.MaterialBindingAPI.Apply(box_prim)
        mat_binding_api.Bind(default_material, UsdShade.Tokens.weakerThanDescendants, "physics")
        # Wait for an app update to load the new attributes
        await omni.kit.app.get_app().next_update_async()

        # Play simulation for a few frames for each box
        timeline.play()
        for _ in range(20):
            await omni.kit.app.get_app().next_update_async()
        timeline.pause()

    # Iteratively apply forces to the boxes to move them around then pull them all together towards the pallet center
    await apply_forces_async(stage, boxes, pallet_prim)

    # Remove rigid body dynamics of the boxes until all other scenarios are completed
    for box in boxes:
        UsdPhysics.RigidBodyAPI(box).GetRigidBodyEnabledAttr().Set(False)

    # Increase the friction to prevent sliding of the boxes on the pallet before removing the collision walls
    physics_material.CreateStaticFrictionAttr().Set(0.9)
    physics_material.CreateDynamicFrictionAttr().Set(0.9)

    # Remove collision walls
    for wall in collision_walls:
        stage.RemovePrim(wall.GetPath())
    return boxes

# Run the example scenario
async def run_box_stacking_scenarios_async(num_pallets, env_url=None, write_data=False):
    # Get assets root path once for all asset loading operations
    assets_root_path = await get_assets_root_path_async()

    # List of pallets and boxes to randomly choose from with their respective weights
    pallets_urls_and_weights = [
        (assets_root_path + "/Isaac/Environments/Simple_Warehouse/Props/SM_PaletteA_01.usd", 0.25),
        (assets_root_path + "/Isaac/Environments/Simple_Warehouse/Props/SM_PaletteA_02.usd", 0.75),
    ]
    boxes_urls_and_weights = [
        (assets_root_path + "/Isaac/Environments/Simple_Warehouse/Props/SM_CardBoxA_01.usd", 0.02),
        (assets_root_path + "/Isaac/Environments/Simple_Warehouse/Props/SM_CardBoxB_01.usd", 0.06),
        (assets_root_path + "/Isaac/Environments/Simple_Warehouse/Props/SM_CardBoxC_01.usd", 0.12),
        (assets_root_path + "/Isaac/Environments/Simple_Warehouse/Props/SM_CardBoxD_01.usd", 0.80),
    ]

    # Load a predefined or create a new stage
    if env_url is not None:
        env_path = env_url if env_url.startswith("omniverse://") else assets_root_path + env_url
        omni.usd.get_context().open_stage(env_path)
        stage = omni.usd.get_context().get_stage()
    else:
        omni.usd.get_context().new_stage()
        stage = omni.usd.get_context().get_stage()
        distant_light = stage.DefinePrim("/World/Lights/DistantLight", "DistantLight")
        distant_light.CreateAttribute("inputs:intensity", Sdf.ValueTypeNames.Float).Set(400.0)
        if not distant_light.HasAttribute("xformOp:rotateXYZ"):
            UsdGeom.Xformable(distant_light).AddRotateXYZOp()
        distant_light.GetAttribute("xformOp:rotateXYZ").Set((0, 60, 0))
        dome_light = stage.DefinePrim("/World/Lights/DomeLight", "DomeLight")
        dome_light.CreateAttribute("inputs:intensity", Sdf.ValueTypeNames.Float).Set(500.0)

    # Spawn the pallets
    pallets = []
    pallets_urls, pallets_weights = zip(*pallets_urls_and_weights)
    rand_pallet_urls = random.choices(pallets_urls, weights=pallets_weights, k=num_pallets)
    # Custom pallet poses for the evnironment
    custom_pallet_locations = [
        (-9.3, 5.3, 1.3),
        (-9.3, 7.3, 1.3),
        (-9.3, -0.6, 1.3),
    ]
    random.shuffle(custom_pallet_locations)
    for i, pallet_url in enumerate(rand_pallet_urls):
        # Use a custom location for every other pallet
        if env_url is not None:
            if i % 2 == 0 and custom_pallet_locations:
                rand_loc = Gf.Vec3d(*custom_pallet_locations.pop())
            else:
                rand_loc = Gf.Vec3d(-6.5, i * 1.75, 0) + Gf.Vec3d(random.uniform(-0.2, 0.2), random.uniform(0, 0.2), 0)
        else:
            rand_loc = Gf.Vec3d(i * 1.5, 0, 0) + Gf.Vec3d(random.uniform(0, 0.2), random.uniform(-0.2, 0.2), 0)
        rand_rot = (0, 0, random.choice([180, 90, 0, -90, -180]) + random.uniform(-15, 15))
        pallet_prim = create_asset_with_colliders(
            stage, pallet_url, f"/World/Pallet_{i}", location=rand_loc, rotation=rand_rot
        )
        pallets.append(pallet_prim)

    # Stack the boxes on the pallets
    total_boxes = []
    for pallet in pallets:
        if env_url is not None:
            rand_num_boxes = random.randint(8, 15)
            stacked_boxes = await stack_boxes_on_pallet_async(
                pallet, boxes_urls_and_weights, num_boxes=rand_num_boxes, drop_height=1.0
            )
        else:
            rand_num_boxes = random.randint(12, 20)
            stacked_boxes = await stack_boxes_on_pallet_async(pallet, boxes_urls_and_weights, num_boxes=rand_num_boxes)
        total_boxes.extend(stacked_boxes)

    # Re-enable rigid body dynamics of the boxes and run the simulation for a while
    for box in total_boxes:
        UsdPhysics.RigidBodyAPI(box).GetRigidBodyEnabledAttr().Set(True)
    timeline = omni.timeline.get_timeline_interface()
    timeline.play()
    for _ in range(200):
        await omni.kit.app.get_app().next_update_async()
    timeline.pause()

    if write_data:
        out_dir = os.path.join(os.getcwd(), "_out_box_stacking")
        print(f"Writing data to {out_dir}..")
        backend = rep.backends.get("DiskBackend")
        backend.initialize(output_dir=out_dir)
        writer = rep.WriterRegistry.get("BasicWriter")
        writer.initialize(backend=backend, rgb=True)
        cam = rep.functional.create.camera(position=(5, -5, 2), look_at=(0, 0, 0), name="PalletCamera")
        rp = rep.create.render_product(cam, resolution=(512, 512))
        writer.attach(rp)

        # Capture the data and wait for the data to be written to disk
        await rep.orchestrator.step_async(rt_subframes=8)

        # Wait for the data to be written to disk and cleanup
        await rep.orchestrator.wait_until_complete_async()
        writer.detach()
        rp.destroy()

# asyncio.ensure_future(run_box_stacking_scenarios_async(num_pallets=1, write_data=True))
asyncio.ensure_future(
    run_box_stacking_scenarios_async(
        num_pallets=6, env_url="/Isaac/Environments/Simple_Warehouse/warehouse.usd", write_data=True
    )
)
```

## Simready Assets SDG Example

Script editor example for using [SimReady Assets](https://developer.nvidia.com/omniverse/simready-assets) to randomize the scene. SimReady Assets are physically accurate 3D objects with realistic properties, behavior, and data connections that are optimized for simulation.

Note

The example can only run in async mode and requires the [SimReady Explorer](https://docs.omniverse.nvidia.com/extensions/latest/ext_core/ext_browser-extensions/simready-explorer.html "(in Omniverse Extensions)") window to be enabled to process the search requests.

The example script will create an SDG randomization and capture pipeline scenario with a table, a plate, and a number of items on top of the plate. The scene will be simulated for a while and then the captured images will be saved to disk.

The standalone example can also be run directly (on Windows use `python.bat` instead of `python.sh`):

```python
./python.sh standalone_examples/api/isaacsim.replicator.examples/simready_assets_sdg.py
```

Script Editor

Simready Assets SDG Example

```python
import asyncio
import os
import time

import carb.settings
import numpy as np
import omni.kit.app
import omni.replicator.core as rep
import omni.usd
from isaacsim.core.experimental.utils.semantics import upgrade_prim_semantics_to_labels
from isaacsim.core.simulation_manager import SimulationManager
from pxr import Sdf, Usd, UsdGeom, UsdPhysics

# Make sure the simready explorer extension is enabled
ext_manager = omni.kit.app.get_app().get_extension_manager()
if not ext_manager.is_extension_enabled("omni.simready.explorer"):
    ext_manager.set_extension_enabled_immediate("omni.simready.explorer", True)
import omni.simready.explorer as sre

def enable_simready_explorer() -> None:
    """Enable the SimReady Explorer window if not already open."""
    if sre.get_instance().browser_model is None:
        import omni.kit.actions.core as actions

        actions.execute_action("omni.simready.explorer", "toggle_window")

def set_prim_variants(prim: Usd.Prim, variants: dict[str, str]) -> None:
    """Set variant selections on a prim from a dictionary of variant set names to values."""
    vsets = prim.GetVariantSets()
    for name, value in variants.items():
        vset = vsets.GetVariantSet(name)
        if vset:
            vset.SetVariantSelection(value)

async def search_assets_async() -> tuple[list, list, list]:
    """Search for SimReady assets (tables, dishes, items) asynchronously."""
    print(f"[SDG] Searching for SimReady assets...")
    start_time = time.time()
    tables = await sre.find_assets(["table", "furniture"])
    print(f"[SDG]   - Found {len(tables)} tables ({time.time() - start_time:.2f}s)")
    start_time = time.time()
    plates = await sre.find_assets(["plate"])
    print(f"[SDG]   - Found {len(plates)} plates ({time.time() - start_time:.2f}s)")
    start_time = time.time()
    bowls = await sre.find_assets(["bowl"])
    print(f"[SDG]   - Found {len(bowls)} bowls ({time.time() - start_time:.2f}s)")
    dishes = plates + bowls
    start_time = time.time()
    fruits = await sre.find_assets(["fruit"])
    print(f"[SDG]   - Found {len(fruits)} fruits ({time.time() - start_time:.2f}s)")
    start_time = time.time()
    vegetables = await sre.find_assets(["vegetable"])
    print(f"[SDG]   - Found {len(vegetables)} vegetables ({time.time() - start_time:.2f}s)")
    items = fruits + vegetables
    return tables, dishes, items

async def run_simready_randomization_async(
    stage: Usd.Stage,
    camera_prim: Usd.Prim,
    render_product,
    tables: list,
    dishes: list,
    items: list,
    rng: np.random.Generator = None,
) -> None:
    """Randomize a scene with SimReady assets, run physics, and capture the result."""
    if rng is None:
        rng = np.random.default_rng()

    print(f"[SDG]   Creating anonymous variation layer for the randomizations...")
    root_layer = stage.GetRootLayer()
    variation_layer = Sdf.Layer.CreateAnonymous("variation")
    root_layer.subLayerPaths.insert(0, variation_layer.identifier)
    stage.SetEditTarget(variation_layer)

    # Load the simready assets with rigid body properties
    variants = {"PhysicsVariant": "RigidBody"}
    rep.functional.create.scope(name="Assets")

    # Choose a random table and add it to the stage
    print(f"[SDG]   Loading assets...")
    table_asset = tables[rng.integers(len(tables))]
    start_time = time.time()
    table_prim = rep.functional.create.reference(usd_path=table_asset.main_url, parent="/Assets", name=table_asset.name)
    set_prim_variants(table_prim, variants)
    upgrade_prim_semantics_to_labels(table_prim)
    print(f"[SDG]     - Table: '{table_asset.name}' ({time.time() - start_time:.2f}s)")
    await omni.kit.app.get_app().next_update_async()

    # Keep only colliders on the table (disable rigid body dynamics)
    UsdPhysics.RigidBodyAPI(table_prim).GetRigidBodyEnabledAttr().Set(False)

    # Compute table dimensions from its bounding box
    bbox_cache = UsdGeom.BBoxCache(Usd.TimeCode.Default(), includedPurposes=[UsdGeom.Tokens.default_])
    table_bbox = bbox_cache.ComputeWorldBound(table_prim)
    table_extent = table_bbox.GetRange().GetSize()

    # Choose a random dish and add it to the stage
    dish_asset = dishes[rng.integers(len(dishes))]
    start_time = time.time()
    dish_prim = rep.functional.create.reference(usd_path=dish_asset.main_url, parent="/Assets", name=dish_asset.name)
    set_prim_variants(dish_prim, variants)
    upgrade_prim_semantics_to_labels(dish_prim)
    print(f"[SDG]     - Dish: '{dish_asset.name}' ({time.time() - start_time:.2f}s)")
    await omni.kit.app.get_app().next_update_async()

    # Compute dish dimensions from its bounding box
    dish_bbox = bbox_cache.ComputeWorldBound(dish_prim)
    dish_extent = dish_bbox.GetRange().GetSize()

    # Calculate random position for the dish near the center of the table
    center_region_scale = 0.75
    dish_range_x = max(0, (table_extent[0] - dish_extent[0]) / 2 * center_region_scale)
    dish_range_y = max(0, (table_extent[1] - dish_extent[1]) / 2 * center_region_scale)
    dish_position = (
        rng.uniform(-dish_range_x, dish_range_x) if dish_range_x > 0 else 0,
        rng.uniform(-dish_range_y, dish_range_y) if dish_range_y > 0 else 0,
        table_extent[2] + dish_extent[2] / 2,
    )
    dish_prim.GetAttribute("xformOp:translate").Set(dish_position)

    # Add random items above the dish
    num_items = rng.integers(2, 5)
    item_prims = []
    for _ in range(num_items):
        item_asset = items[rng.integers(len(items))]
        start_time = time.time()
        item_prim = rep.functional.create.reference(
            usd_path=item_asset.main_url, parent="/Assets", name=item_asset.name
        )
        set_prim_variants(item_prim, variants)
        upgrade_prim_semantics_to_labels(item_prim)
        print(f"[SDG]     - Item: '{item_asset.name}' ({time.time() - start_time:.2f}s)")
        item_prims.append(item_prim)
        await omni.kit.app.get_app().next_update_async()

    # Position items stacked above the dish
    print(f"[SDG]   Positioning assets on table...")
    stack_height = dish_position[2]
    item_scatter_radius = max(0, dish_extent[0] / 4)
    for item_prim in item_prims:
        item_bbox = bbox_cache.ComputeWorldBound(item_prim)
        item_extent = item_bbox.GetRange().GetSize()
        scatter_x = rng.uniform(-item_scatter_radius, item_scatter_radius) if item_scatter_radius > 0 else 0
        scatter_y = rng.uniform(-item_scatter_radius, item_scatter_radius) if item_scatter_radius > 0 else 0
        item_position = (
            dish_position[0] + scatter_x,
            dish_position[1] + scatter_y,
            stack_height + item_extent[2] / 2,
        )
        item_prim.GetAttribute("xformOp:translate").Set(item_position)
        stack_height += item_extent[2]

    # Run physics simulation for items to settle (SimulationManager handles warmup on init)
    num_sim_steps = 25
    print(f"[SDG]   Running physics simulation ({num_sim_steps} steps)...")
    SimulationManager.invalidate_physics()
    SimulationManager.initialize_physics()
    SimulationManager.step(steps=num_sim_steps)

    print(f"[SDG]   Setting edit target to root layer...")
    stage.SetEditTarget(root_layer)

    print(f"[SDG]   Positioning camera and capturing frame...")
    camera_position = (
        dish_position[0] + rng.uniform(-0.5, 0.5),
        dish_position[1] + rng.uniform(-0.5, 0.5),
        dish_position[2] + 1.5 + rng.uniform(-0.5, 0.5),
    )
    rep.functional.modify.pose(
        camera_prim, position_value=camera_position, look_at_value=dish_prim, look_at_up_axis=(0, 0, 1)
    )
    render_product.hydra_texture.set_updates_enabled(True)
    await rep.orchestrator.step_async(delta_time=0.0, rt_subframes=16)
    render_product.hydra_texture.set_updates_enabled(False)

    print(f"[SDG]   Removing temp variation layer...")
    variation_layer.Clear()
    root_layer.subLayerPaths.remove(variation_layer.identifier)

async def run_simready_randomizations_async(num_scenarios: int) -> None:
    """Run multiple SimReady randomization scenarios and capture the results."""
    print(f"[SDG] Initializing scene...")
    await omni.usd.get_context().new_stage_async()
    stage = omni.usd.get_context().get_stage()

    # Initialize randomization
    rng = np.random.default_rng(34)
    rep.set_global_seed(34)

    # Data capture will happen manually using step()
    rep.orchestrator.set_capture_on_play(False)
    SimulationManager.set_physics_dt(1.0 / 60.0)

    # Set DLSS to Quality mode (2) for best SDG results , options: 0 (Performance), 1 (Balanced), 2 (Quality), 3 (Auto)
    carb.settings.get_settings().set("rtx/post/dlss/execMode", 2)

    # Add lights to the scene
    print(f"[SDG] Setting up lighting...")
    rep.functional.create.xform(name="World")
    rep.functional.create.dome_light(intensity=500, parent="/World", name="DomeLight")
    rep.functional.create.distant_light(intensity=2500, parent="/World", name="DistantLight", rotation=(-75, 0, 0))

    # Simready explorer window needs to be created for the search to work
    enable_simready_explorer()

    # Search for the simready assets
    tables, dishes, items = await search_assets_async()

    # Create the writer and the render product for capturing the scene
    output_dir = os.path.join(os.getcwd(), "_out_simready_assets")
    backend = rep.backends.get("DiskBackend")
    backend.initialize(output_dir=output_dir)
    writer = rep.writers.get("BasicWriter")
    print(f"[SDG] Initializing writer, output directory: {output_dir}...")
    writer.initialize(backend=backend, rgb=True)

    # Create camera and render product (disabled by default, enabled only when capturing)
    print(f"[SDG] Creating camera and render product...")
    camera_prim = rep.functional.create.camera(position=(5, 5, 5), look_at=(0, 0, 0), parent="/World", name="Camera")
    rp = rep.create.render_product(camera_prim, (512, 512))
    rp.hydra_texture.set_updates_enabled(False)
    writer.attach(rp)

    # Generate randomized scenarios
    for i in range(num_scenarios):
        print(f"[SDG] Scenario {i + 1}/{num_scenarios}")
        await run_simready_randomization_async(
            stage=stage, camera_prim=camera_prim, render_product=rp, tables=tables, dishes=dishes, items=items, rng=rng
        )

    # Finalize and cleanup
    print("[SDG] Wait for the data to be written and cleanup render products...")
    await rep.orchestrator.wait_until_complete_async()
    writer.detach()
    rp.destroy()

num_scenarios = 5
print(f"[SDG] Starting SDG pipeline with {num_scenarios} scenarios...")
asyncio.ensure_future(run_simready_randomizations_async(num_scenarios))
```

Standalone Application

Simready Assets SDG Example

```python
from isaacsim import SimulationApp

simulation_app = SimulationApp(launch_config={"headless": False})

import argparse
import asyncio
import os
import time

import carb.settings
import numpy as np
import omni.kit.app
import omni.replicator.core as rep
import omni.timeline
import omni.usd
from isaacsim.core.experimental.utils.semantics import upgrade_prim_semantics_to_labels
from pxr import Gf, Sdf, Usd, UsdGeom, UsdPhysics

parser = argparse.ArgumentParser()
parser.add_argument("--num_scenarios", type=int, default=5, help="Number of randomization scenarios to create")
args, _ = parser.parse_known_args()
num_scenarios = args.num_scenarios

# Make sure the simready explorer extension is enabled
ext_manager = omni.kit.app.get_app().get_extension_manager()
if not ext_manager.is_extension_enabled("omni.simready.explorer"):
    ext_manager.set_extension_enabled_immediate("omni.simready.explorer", True)
import omni.simready.explorer as sre

def enable_simready_explorer() -> None:
    """Enable the SimReady Explorer window if not already open."""
    if sre.get_instance().browser_model is None:
        import omni.kit.actions.core as actions

        actions.execute_action("omni.simready.explorer", "toggle_window")

def set_prim_variants(prim: Usd.Prim, variants: dict[str, str]) -> None:
    """Set variant selections on a prim from a dictionary of variant set names to values."""
    vsets = prim.GetVariantSets()
    for name, value in variants.items():
        vset = vsets.GetVariantSet(name)
        if vset:
            vset.SetVariantSelection(value)

async def search_assets_async() -> tuple[list, list, list]:
    """Search for SimReady assets (tables, dishes, items) asynchronously."""
    print(f"[SDG] Searching for SimReady assets...")
    start_time = time.time()
    tables = await sre.find_assets(["table", "furniture"])
    print(f"[SDG]   - Found {len(tables)} tables ({time.time() - start_time:.2f}s)")
    start_time = time.time()
    plates = await sre.find_assets(["plate"])
    print(f"[SDG]   - Found {len(plates)} plates ({time.time() - start_time:.2f}s)")
    start_time = time.time()
    bowls = await sre.find_assets(["bowl"])
    print(f"[SDG]   - Found {len(bowls)} bowls ({time.time() - start_time:.2f}s)")
    dishes = plates + bowls
    start_time = time.time()
    fruits = await sre.find_assets(["fruit"])
    print(f"[SDG]   - Found {len(fruits)} fruits ({time.time() - start_time:.2f}s)")
    start_time = time.time()
    vegetables = await sre.find_assets(["vegetable"])
    print(f"[SDG]   - Found {len(vegetables)} vegetables ({time.time() - start_time:.2f}s)")
    items = fruits + vegetables
    return tables, dishes, items

def run_simready_randomization(
    stage: Usd.Stage,
    camera_prim: Usd.Prim,
    render_product,
    tables: list,
    dishes: list,
    items: list,
    rng: np.random.Generator = None,
) -> None:
    """Randomize a scene with SimReady assets, run physics, and capture the result."""
    if rng is None:
        rng = np.random.default_rng()

    print(f"[SDG]   Creating anonymous variation layer for the randomizations...")
    root_layer = stage.GetRootLayer()
    variation_layer = Sdf.Layer.CreateAnonymous("variation")
    root_layer.subLayerPaths.insert(0, variation_layer.identifier)
    stage.SetEditTarget(variation_layer)

    # Load the simready assets with rigid body properties
    variants = {"PhysicsVariant": "RigidBody"}
    rep.functional.create.scope(name="Assets")

    # Choose a random table and add it to the stage
    print(f"[SDG]   Loading assets...")
    table_asset = tables[rng.integers(len(tables))]
    start_time = time.time()
    table_prim = rep.functional.create.reference(usd_path=table_asset.main_url, parent="/Assets", name=table_asset.name)
    set_prim_variants(table_prim, variants)
    upgrade_prim_semantics_to_labels(table_prim)
    print(f"[SDG]     - Table: '{table_asset.name}' ({time.time() - start_time:.2f}s)")
    simulation_app.update()

    # Keep only colliders on the table (disable rigid body dynamics)
    UsdPhysics.RigidBodyAPI(table_prim).GetRigidBodyEnabledAttr().Set(False)

    # Compute table dimensions from its bounding box
    bbox_cache = UsdGeom.BBoxCache(Usd.TimeCode.Default(), includedPurposes=[UsdGeom.Tokens.default_])
    table_bbox = bbox_cache.ComputeWorldBound(table_prim)
    table_extent = table_bbox.GetRange().GetSize()

    # Choose a random dish and add it to the stage
    dish_asset = dishes[rng.integers(len(dishes))]
    start_time = time.time()
    dish_prim = rep.functional.create.reference(usd_path=dish_asset.main_url, parent="/Assets", name=dish_asset.name)
    set_prim_variants(dish_prim, variants)
    upgrade_prim_semantics_to_labels(dish_prim)
    print(f"[SDG]     - Dish: '{dish_asset.name}' ({time.time() - start_time:.2f}s)")
    simulation_app.update()

    # Compute dish dimensions from its bounding box
    dish_bbox = bbox_cache.ComputeWorldBound(dish_prim)
    dish_extent = dish_bbox.GetRange().GetSize()

    # Calculate random position for the dish near the center of the table
    center_region_scale = 0.75
    dish_range_x = max(0, (table_extent[0] - dish_extent[0]) / 2 * center_region_scale)
    dish_range_y = max(0, (table_extent[1] - dish_extent[1]) / 2 * center_region_scale)
    dish_position = (
        rng.uniform(-dish_range_x, dish_range_x) if dish_range_x > 0 else 0,
        rng.uniform(-dish_range_y, dish_range_y) if dish_range_y > 0 else 0,
        table_extent[2] + dish_extent[2] / 2,
    )
    dish_prim.GetAttribute("xformOp:translate").Set(dish_position)

    # Add random items above the dish
    num_items = rng.integers(2, 5)
    item_prims = []
    for _ in range(num_items):
        item_asset = items[rng.integers(len(items))]
        start_time = time.time()
        item_prim = rep.functional.create.reference(
            usd_path=item_asset.main_url, parent="/Assets", name=item_asset.name
        )
        set_prim_variants(item_prim, variants)
        upgrade_prim_semantics_to_labels(item_prim)
        print(f"[SDG]     - Item: '{item_asset.name}' ({time.time() - start_time:.2f}s)")
        item_prims.append(item_prim)
        simulation_app.update()

    # Position items stacked above the dish
    print(f"[SDG]   Positioning assets on table...")
    stack_height = dish_position[2]
    item_scatter_radius = max(0, dish_extent[0] / 4)
    for item_prim in item_prims:
        item_bbox = bbox_cache.ComputeWorldBound(item_prim)
        item_extent = item_bbox.GetRange().GetSize()
        scatter_x = rng.uniform(-item_scatter_radius, item_scatter_radius) if item_scatter_radius > 0 else 0
        scatter_y = rng.uniform(-item_scatter_radius, item_scatter_radius) if item_scatter_radius > 0 else 0
        item_position = (
            dish_position[0] + scatter_x,
            dish_position[1] + scatter_y,
            stack_height + item_extent[2] / 2,
        )
        item_prim.GetAttribute("xformOp:translate").Set(item_position)
        stack_height += item_extent[2]

    # Run physics simulation for items to settle
    num_sim_steps = 25
    print(f"[SDG]   Running physics simulation ({num_sim_steps} steps)...")
    timeline = omni.timeline.get_timeline_interface()
    timeline.play()
    for _ in range(num_sim_steps):
        simulation_app.update()
    timeline.pause()

    print(f"[SDG]   Setting edit target to root layer...")
    stage.SetEditTarget(root_layer)

    print(f"[SDG]   Positioning camera and capturing frame...")
    camera_position = (
        dish_position[0] + rng.uniform(-0.5, 0.5),
        dish_position[1] + rng.uniform(-0.5, 0.5),
        dish_position[2] + 1.5 + rng.uniform(-0.5, 0.5),
    )
    rep.functional.modify.pose(
        camera_prim, position_value=camera_position, look_at_value=dish_prim, look_at_up_axis=(0, 0, 1)
    )
    render_product.hydra_texture.set_updates_enabled(True)
    rep.orchestrator.step(delta_time=0.0, rt_subframes=16)
    render_product.hydra_texture.set_updates_enabled(False)

    print(f"[SDG]   Removing temp variation layer...")
    variation_layer.Clear()
    root_layer.subLayerPaths.remove(variation_layer.identifier)

def run_simready_randomizations(num_scenarios: int) -> None:
    """Run multiple SimReady randomization scenarios and capture the results."""
    print(f"[SDG] Initializing scene...")
    omni.usd.get_context().new_stage()
    stage = omni.usd.get_context().get_stage()

    # Initialize randomization
    rng = np.random.default_rng(34)
    rep.set_global_seed(34)

    # Data capture will happen manually using step()
    rep.orchestrator.set_capture_on_play(False)

    # Set DLSS to Quality mode (2) for best SDG results , options: 0 (Performance), 1 (Balanced), 2 (Quality), 3 (Auto)
    carb.settings.get_settings().set("rtx/post/dlss/execMode", 2)

    # Add lights to the scene
    print(f"[SDG] Setting up lighting...")
    rep.functional.create.xform(name="World")
    rep.functional.create.dome_light(intensity=500, parent="/World", name="DomeLight")
    rep.functional.create.distant_light(intensity=2500, parent="/World", name="DistantLight", rotation=(-75, 0, 0))

    # Simready explorer window needs to be created for the search to work
    enable_simready_explorer()

    # Search for the simready assets and wait until the task is complete
    search_task = asyncio.ensure_future(search_assets_async())
    while not search_task.done():
        simulation_app.update()
    tables, dishes, items = search_task.result()

    # Create the writer and the render product for capturing the scene
    output_dir = os.path.join(os.getcwd(), "_out_simready_assets")
    backend = rep.backends.get("DiskBackend")
    backend.initialize(output_dir=output_dir)
    writer = rep.writers.get("BasicWriter")
    print(f"[SDG] Initializing writer, output directory: {output_dir}...")
    writer.initialize(backend=backend, rgb=True)

    # Create camera and render product (disabled by default, enabled only when capturing)
    print(f"[SDG] Creating camera and render product...")
    camera_prim = rep.functional.create.camera(position=(5, 5, 5), look_at=(0, 0, 0), parent="/World", name="Camera")
    rp = rep.create.render_product(camera_prim, (512, 512))
    rp.hydra_texture.set_updates_enabled(False)
    writer.attach(rp)

    # Generate randomized scenarios
    for i in range(num_scenarios):
        print(f"[SDG] Scenario {i + 1}/{num_scenarios}")
        run_simready_randomization(
            stage=stage, camera_prim=camera_prim, render_product=rp, tables=tables, dishes=dishes, items=items, rng=rng
        )

    # Finalize and cleanup
    print("[SDG] Wait for the data to be written and cleanup render products...")
    rep.orchestrator.wait_until_complete()
    writer.detach()
    rp.destroy()

print(f"[SDG] Starting SDG pipeline with {num_scenarios} scenarios...")
run_simready_randomizations(num_scenarios)

simulation_app.close()
```

On this page

* [Randomizing Light Sources](#randomizing-light-sources)
* [Randomizing Textures](#randomizing-textures)
* [Sequential Randomizations](#sequential-randomizations)
* [Physics-based Randomized Volume Filling](#physics-based-randomized-volume-filling)
* [Simready Assets SDG Example](#simready-assets-sdg-example)

---

### Custom OG Randomizer

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/replicator_tutorials/tutorial_replicator_custom_og_randomizer.html

* [Synthetic Data Generation](../synthetic_data_generation/index.html)
* [Perception Data Generation (Replicator)](index.html)
* Custom Replicator Randomization Nodes

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Custom Replicator Randomization Nodes

This tutorial provides an example of how to create custom randomization nodes for the [omni.replicator](https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator.html "(in Omniverse Extensions)") extension.

## Learning Objectives

The goal of this tutorial is to demonstrate how to create custom [OmniGraph](https://docs.omniverse.nvidia.com/extensions/latest/ext_omnigraph.html "(in Omniverse Extensions)") randomization nodes. These nodes can then be further integrated into the Synthetic Data Generation (SDG) pipeline graph of [Replicator](https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator.html "(in Omniverse Extensions)").

This tutorial will showcase how to:

* Create custom scene randomization Python scripts.
* Wrap the scripts as OmniGraph nodes and manually add them to an existing SDG pipeline graph.
* Encapsulate the OmniGraph nodes as **ReplicatorItems** to be automatically added to the SDG pipeline graph using Replicator’s API.

## Prerequisites

* Familiarity with USD / Isaac Sim APIs for creating custom scene randomizers. See [Randomization Snippets](tutorial_replicator_isaac_randomizers.html#isaac-sim-app-tutorial-replicator-isaac-randomizers) for more details.
* Familiarity with [omni.replicator](https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator.html "(in Omniverse Extensions)") and its randomization API [replicator randomizers](https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator/randomizer_details.html "(in Omniverse Extensions)").
* Basic knowledge of [OmniGraph](https://docs.omniverse.nvidia.com/extensions/latest/ext_omnigraph.html "(in Omniverse Extensions)") and how to create [OmniGraph Nodes](https://docs.omniverse.nvidia.com/kit/docs/omni.graph.docs/latest/dev/WritingNodes.html#omnigraph-nodes).
* Experience running simulations via the [Script Editor](../development_tools/omniverse_script_editor.html#script-editor).

## Implementation

This tutorial will showcase how to create custom scene randomization Python scripts. These scripts will create prims in a new stage and randomize their rotation and locations: **in a sphere**, **on a sphere**, and **between two spheres**.

The following image shows the result after running the randomization in the Script Editor:

Code Explanation

The following functions take as input the radius (or radii) of the spheres and generate a random 3D point on the surface of a sphere, within a sphere, and between two spheres. These points will determine the prim locations.

Randomization Functions

```python
# Generate a random 3D point on the surface of a sphere of a given radius.
def random_point_on_sphere(radius):
    # Generate a random direction by spherical coordinates (phi, theta)
    phi = random.uniform(0, 2 * math.pi)
    # Sample costheta to ensure uniform distribution of points on the sphere (surface is proportional to sin(theta))
    costheta = random.uniform(-1, 1)
    theta = math.acos(costheta)

    # Convert from spherical to Cartesian coordinates
    x = radius * math.sin(theta) * math.cos(phi)
    y = radius * math.sin(theta) * math.sin(phi)
    z = radius * math.cos(theta)

    return x, y, z

# Generate a random 3D point within a sphere of a given radius, ensuring a uniform distribution throughout the volume.
def random_point_in_sphere(radius):
    # Generate a random direction by spherical coordinates (phi, theta)
    phi = random.uniform(0, 2 * math.pi)
    # Sample costheta to ensure uniform distribution of points on the sphere (surface is proportional to sin(theta))
    costheta = random.uniform(-1, 1)
    theta = math.acos(costheta)

    # Scale the radius uniformly within the sphere, applying the cube root to a random value
    # to account for volume's cubic growth with radius (r^3), ensuring spatial uniformity.
    r = radius * (random.random() ** (1 / 3))

    # Convert from spherical to Cartesian coordinates
    x = r * math.sin(theta) * math.cos(phi)
    y = r * math.sin(theta) * math.sin(phi)
    z = r * math.cos(theta)

    return x, y, z

# Generate a random 3D point between two spheres, ensuring a uniform distribution throughout the volume.
def random_point_between_spheres(radius1, radius2):
    # Ensure radius1 < radius2
    if radius1 > radius2:
        radius1, radius2 = radius2, radius1

    # Generate a random direction by spherical coordinates (phi, theta)
    phi = random.uniform(0, 2 * math.pi)
    # Sample costheta to ensure uniform distribution of points on the sphere (surface is proportional to sin(theta))
    costheta = random.uniform(-1, 1)
    theta = math.acos(costheta)

    # Uniformly distribute points between two spheres by weighting the radius to match volume growth (r^3),
    # ensuring spatial uniformity by taking the cube root of a value between the radii cubed.
    r = (random.uniform(radius1**3, radius2**3)) ** (1 / 3.0)

    # Convert from spherical to Cartesian coordinates
    x = r * math.sin(theta) * math.cos(phi)
    y = r * math.sin(theta) * math.sin(phi)
    z = r * math.cos(theta)

    return x, y, z
```

The following snippet creates prims in a new stage and randomizes their rotation and locations using the previously defined functions.

Spawning and Randomizing Prims

```python
stage = omni.usd.get_context().get_stage()
prim_count = 500
prim_scale = 0.1
rad_in = 0.5
rad_on = 1.5
rad_bet1 = 2.5
rad_bet2 = 3.5

# Create the default prims
on_sphere_prims = [stage.DefinePrim(f"/World/sphere_{i}", "Sphere") for i in range(prim_count)]
in_sphere_prims = [stage.DefinePrim(f"/World/cube_{i}", "Cube") for i in range(prim_count)]
between_spheres_prims = [stage.DefinePrim(f"/World/cylinder_{i}", "Cylinder") for i in range(prim_count)]

# Add xformOps and scale to the prims
for prim in chain(on_sphere_prims, in_sphere_prims, between_spheres_prims):
    if not prim.HasAttribute("xformOp:translate"):
        UsdGeom.Xformable(prim).AddTranslateOp()
    if not prim.HasAttribute("xformOp:scale"):
        UsdGeom.Xformable(prim).AddScaleOp()
    if not prim.HasAttribute("xformOp:rotateXYZ"):
        UsdGeom.Xformable(prim).AddRotateXYZOp()
    prim.GetAttribute("xformOp:scale").Set((prim_scale, prim_scale, prim_scale))

# Randomize the prims
for _ in range(10):
    for in_sphere_prim in in_sphere_prims:
        rand_rot = (random.uniform(0, 360), random.uniform(0, 360), random.uniform(0, 360))
        in_sphere_prim.GetAttribute("xformOp:rotateXYZ").Set(rand_rot)
        rand_loc = random_point_in_sphere(rad_in)
        in_sphere_prim.GetAttribute("xformOp:translate").Set(rand_loc)

    for on_sphere_prim in on_sphere_prims:
        rand_rot = (random.uniform(0, 360), random.uniform(0, 360), random.uniform(0, 360))
        on_sphere_prim.GetAttribute("xformOp:rotateXYZ").Set(rand_rot)
        rand_loc = random_point_on_sphere(rad_on)
        on_sphere_prim.GetAttribute("xformOp:translate").Set(rand_loc)

    for between_spheres_prim in between_spheres_prims:
        rand_rot = (random.uniform(0, 360), random.uniform(0, 360), random.uniform(0, 360))
        between_spheres_prim.GetAttribute("xformOp:rotateXYZ").Set(rand_rot)
        rand_loc = random_point_between_spheres(rad_bet1, rad_bet2)
        between_spheres_prim.GetAttribute("xformOp:translate").Set(rand_loc)
```

Script Editor

Snippet to run in the Script Editor:

Full Script Editor Script

```python
import math
import random
from itertools import chain

import omni.replicator.core as rep
import omni.usd
from pxr import UsdGeom

# Generate a random 3D point on the surface of a sphere of a given radius.
def random_point_on_sphere(radius):
    # Generate a random direction by spherical coordinates (phi, theta)
    phi = random.uniform(0, 2 * math.pi)
    # Sample costheta to ensure uniform distribution of points on the sphere (surface is proportional to sin(theta))
    costheta = random.uniform(-1, 1)
    theta = math.acos(costheta)

    # Convert from spherical to Cartesian coordinates
    x = radius * math.sin(theta) * math.cos(phi)
    y = radius * math.sin(theta) * math.sin(phi)
    z = radius * math.cos(theta)

    return x, y, z

# Generate a random 3D point within a sphere of a given radius, ensuring a uniform distribution throughout the volume.
def random_point_in_sphere(radius):
    # Generate a random direction by spherical coordinates (phi, theta)
    phi = random.uniform(0, 2 * math.pi)
    # Sample costheta to ensure uniform distribution of points on the sphere (surface is proportional to sin(theta))
    costheta = random.uniform(-1, 1)
    theta = math.acos(costheta)

    # Scale the radius uniformly within the sphere, applying the cube root to a random value
    # to account for volume's cubic growth with radius (r^3), ensuring spatial uniformity.
    r = radius * (random.random() ** (1 / 3))

    # Convert from spherical to Cartesian coordinates
    x = r * math.sin(theta) * math.cos(phi)
    y = r * math.sin(theta) * math.sin(phi)
    z = r * math.cos(theta)

    return x, y, z

# Generate a random 3D point between two spheres, ensuring a uniform distribution throughout the volume.
def random_point_between_spheres(radius1, radius2):
    # Ensure radius1 < radius2
    if radius1 > radius2:
        radius1, radius2 = radius2, radius1

    # Generate a random direction by spherical coordinates (phi, theta)
    phi = random.uniform(0, 2 * math.pi)
    # Sample costheta to ensure uniform distribution of points on the sphere (surface is proportional to sin(theta))
    costheta = random.uniform(-1, 1)
    theta = math.acos(costheta)

    # Uniformly distribute points between two spheres by weighting the radius to match volume growth (r^3),
    # ensuring spatial uniformity by taking the cube root of a value between the radii cubed.
    r = (random.uniform(radius1**3, radius2**3)) ** (1 / 3.0)

    # Convert from spherical to Cartesian coordinates
    x = r * math.sin(theta) * math.cos(phi)
    y = r * math.sin(theta) * math.sin(phi)
    z = r * math.cos(theta)

    return x, y, z

stage = omni.usd.get_context().get_stage()
prim_count = 500
prim_scale = 0.1
rad_in = 0.5
rad_on = 1.5
rad_bet1 = 2.5
rad_bet2 = 3.5

# Create the default prims
on_sphere_prims = [stage.DefinePrim(f"/World/sphere_{i}", "Sphere") for i in range(prim_count)]
in_sphere_prims = [stage.DefinePrim(f"/World/cube_{i}", "Cube") for i in range(prim_count)]
between_spheres_prims = [stage.DefinePrim(f"/World/cylinder_{i}", "Cylinder") for i in range(prim_count)]

# Add xformOps and scale to the prims
for prim in chain(on_sphere_prims, in_sphere_prims, between_spheres_prims):
    if not prim.HasAttribute("xformOp:translate"):
        UsdGeom.Xformable(prim).AddTranslateOp()
    if not prim.HasAttribute("xformOp:scale"):
        UsdGeom.Xformable(prim).AddScaleOp()
    if not prim.HasAttribute("xformOp:rotateXYZ"):
        UsdGeom.Xformable(prim).AddRotateXYZOp()
    prim.GetAttribute("xformOp:scale").Set((prim_scale, prim_scale, prim_scale))

# Randomize the prims
for _ in range(10):
    for in_sphere_prim in in_sphere_prims:
        rand_rot = (random.uniform(0, 360), random.uniform(0, 360), random.uniform(0, 360))
        in_sphere_prim.GetAttribute("xformOp:rotateXYZ").Set(rand_rot)
        rand_loc = random_point_in_sphere(rad_in)
        in_sphere_prim.GetAttribute("xformOp:translate").Set(rand_loc)

    for on_sphere_prim in on_sphere_prims:
        rand_rot = (random.uniform(0, 360), random.uniform(0, 360), random.uniform(0, 360))
        on_sphere_prim.GetAttribute("xformOp:rotateXYZ").Set(rand_rot)
        rand_loc = random_point_on_sphere(rad_on)
        on_sphere_prim.GetAttribute("xformOp:translate").Set(rand_loc)

    for between_spheres_prim in between_spheres_prims:
        rand_rot = (random.uniform(0, 360), random.uniform(0, 360), random.uniform(0, 360))
        between_spheres_prim.GetAttribute("xformOp:rotateXYZ").Set(rand_rot)
        rand_loc = random_point_between_spheres(rad_bet1, rad_bet2)
        between_spheres_prim.GetAttribute("xformOp:translate").Set(rand_loc)
```

As a next step, custom [OmniGraph Nodes](https://docs.omniverse.nvidia.com/kit/docs/omni.graph.docs/latest/dev/WritingNodes.html#omnigraph-nodes) are created for the randomization functions. The node descriptions and implementations can be found in the following code snippets:

Node Descriptions

OgnSampleInSphere.ogn

```python
{
    "OgnSampleInSphere": {
        "version": 1,
        "description": "Assigns uniformly sampled location in a sphere.",
        "language": "Python",
        "categoryDefinitions": "config/CategoryDefinition.json",
        "categories": ["isaacReplicatorExamples"],
        "icon": "icons/isaac-sim.svg",
        "metadata": {
            "uiName": "Sample In Sphere"
        },
        "inputs": {
            "prims": {
                "type": "target",
                "description": "prims to randomize",
                "default": []
            },
            "execIn": {
                "type": "execution",
                "description": "exec",
                "default": 0
            },
            "radius": {
                "type": "float",
                "description": "sphere radius",
                "default": 1.0
            }
        },
        "outputs": {
            "execOut": {
                "type": "execution",
                "description": "exec"
            }
        }
    }
}
```

OgnSampleOnSphere.ogn

```python
{
    "OgnSampleOnSphere": {
        "version": 1,
        "description": "Assigns uniformly sampled location on a sphere.",
        "language": "Python",
        "categoryDefinitions": "config/CategoryDefinition.json",
        "categories": ["isaacReplicatorExamples"],
        "icon": "icons/isaac-sim.svg",
        "metadata": {
            "uiName": "Sample On Sphere"
        },
        "inputs": {
            "prims": {
                "type": "target",
                "description": "prims to randomize",
                "default": []
            },
            "execIn": {
                "type": "execution",
                "description": "exec",
                "default": 0
            },
            "radius": {
                "type": "float",
                "description": "sphere radius",
                "default": 1.0
            }
        },
        "outputs": {
            "execOut": {
                "type": "execution",
                "description": "exec"
            }
        }
    }
}
```

OgnSampleBetweenSpheres.ogn

```python
{
    "OgnSampleBetweenSpheres": {
        "version": 1,
        "description": "Assigns uniformly sampled between two spheres",
        "language": "Python",
        "categoryDefinitions": "config/CategoryDefinition.json",
        "categories": ["isaacReplicatorExamples"],
        "icon": "icons/isaac-sim.svg",
        "metadata": {
            "uiName": "Sample Between Spheres"
        },
        "inputs": {
            "prims": {
                "type": "target",
                "description": "prims to randomize",
                "default": []
            },
            "execIn": {
                "type": "execution",
                "description": "exec",
                "default": 0
            },
            "radius1": {
                "type": "float",
                "description": "inner sphere radius",
                "default": 0.5
            },
            "radius2": {
                "type": "float",
                "description": "outer sphere radius",
                "default": 1.0
            }
        },
        "outputs": {
            "execOut": {
                "type": "execution",
                "description": "exec"
            }
        }
    }
}
```

Node Implementations

OgnSampleInSphere.py

```python
# SPDX-FileCopyrightText: Copyright (c) 2024-2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import numpy as np
import omni.graph.core as og
import omni.usd
from pxr import Sdf, UsdGeom

class OgnSampleInSphere:
    @staticmethod
    def compute(db) -> bool:
        prim_paths = db.inputs.prims
        if len(prim_paths) == 0:
            db.outputs.execOut = og.ExecutionAttributeState.DISABLED
            return False

        stage = omni.usd.get_context().get_stage()
        prims = [stage.GetPrimAtPath(str(path)) for path in prim_paths]

        radius = db.inputs.radius

        try:
            for prim in prims:
                if not UsdGeom.Xformable(prim):
                    prim_type = prim.GetTypeName()
                    raise ValueError(
                        f"Expected prim at {prim.GetPath()} to be an Xformable prim but got type {prim_type}"
                    )
                if not prim.HasAttribute("xformOp:translate"):
                    UsdGeom.Xformable(prim).AddTranslateOp()
            if radius <= 0:
                raise ValueError(f"Radius must be positive, got {radius}")

        except Exception as error:
            db.log_error(str(error))
            db.outputs.execOut = og.ExecutionAttributeState.DISABLED
            return False

        samples = []
        for _ in range(len(prims)):
            # Generate a random direction by spherical coordinates (phi, theta)
            phi = np.random.uniform(0, 2 * np.pi)
            # Sample costheta to ensure uniform distribution of points on the sphere (surface is proportional to sin(theta))
            costheta = np.random.uniform(-1, 1)
            theta = np.arccos(costheta)

            # Scale the radius uniformly within the sphere, applying the cube root to a random value
            # to account for volume's cubic growth with radius (r^3), ensuring spatial uniformity.
            r = radius * (np.random.random() ** (1 / 3))

            # Convert from spherical to Cartesian coordinates
            x = r * np.sin(theta) * np.cos(phi)
            y = r * np.sin(theta) * np.sin(phi)
            z = r * np.cos(theta)

            samples.append((x, y, z))

        with Sdf.ChangeBlock():
            for prim, sample in zip(prims, samples):
                prim.GetAttribute("xformOp:translate").Set(sample)

        db.outputs.execOut = og.ExecutionAttributeState.ENABLED
        return True
```

OgnSampleOnSphere.py

```python
# SPDX-FileCopyrightText: Copyright (c) 2024-2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import numpy as np
import omni.graph.core as og
import omni.usd
from pxr import Sdf, UsdGeom

class OgnSampleOnSphere:
    @staticmethod
    def compute(db) -> bool:
        prim_paths = db.inputs.prims
        if len(prim_paths) == 0:
            db.outputs.execOut = og.ExecutionAttributeState.DISABLED
            return False

        stage = omni.usd.get_context().get_stage()
        prims = [stage.GetPrimAtPath(str(path)) for path in prim_paths]

        radius = db.inputs.radius

        try:
            for prim in prims:
                if not UsdGeom.Xformable(prim):
                    prim_type = prim.GetTypeName()
                    raise ValueError(
                        f"Expected prim at {prim.GetPath()} to be an Xformable prim but got type {prim_type}"
                    )
                if not prim.HasAttribute("xformOp:translate"):
                    UsdGeom.Xformable(prim).AddTranslateOp()
            if radius <= 0:
                raise ValueError(f"Radius must be positive, got {radius}")

        except Exception as error:
            db.log_error(str(error))
            db.outputs.execOut = og.ExecutionAttributeState.DISABLED
            return False

        samples = []
        for _ in range(len(prims)):
            # Generate a random direction by spherical coordinates (phi, theta)
            phi = np.random.uniform(0, 2 * np.pi)
            # Sample costheta to ensure uniform distribution of points on the sphere (surface is proportional to sin(theta))
            costheta = np.random.uniform(-1, 1)
            theta = np.arccos(costheta)

            # Convert from spherical to Cartesian coordinates
            x = radius * np.sin(theta) * np.cos(phi)
            y = radius * np.sin(theta) * np.sin(phi)
            z = radius * np.cos(theta)

            samples.append((x, y, z))

        with Sdf.ChangeBlock():
            for prim, sample in zip(prims, samples):
                prim.GetAttribute("xformOp:translate").Set(sample)

        db.outputs.execOut = og.ExecutionAttributeState.ENABLED
        return True
```

OgnSampleBetweenSpheres.py

```python
# SPDX-FileCopyrightText: Copyright (c) 2024-2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import numpy as np
import omni.graph.core as og
import omni.usd
from pxr import Sdf, UsdGeom

class OgnSampleBetweenSpheres:
    @staticmethod
    def compute(db) -> bool:
        prim_paths = db.inputs.prims
        if len(prim_paths) == 0:
            db.outputs.execOut = og.ExecutionAttributeState.DISABLED
            return False

        stage = omni.usd.get_context().get_stage()
        prims = [stage.GetPrimAtPath(str(path)) for path in prim_paths]

        radius1 = db.inputs.radius1
        radius2 = db.inputs.radius2

        # Ensure radius1 < radius2
        if radius1 > radius2:
            radius1, radius2 = radius2, radius1

        try:
            for prim in prims:
                if not UsdGeom.Xformable(prim):
                    prim_type = prim.GetTypeName()
                    raise ValueError(
                        f"Expected prim at {prim.GetPath()} to be an Xformable prim but got type {prim_type}"
                    )
                if not prim.HasAttribute("xformOp:translate"):
                    UsdGeom.Xformable(prim).AddTranslateOp()
            if radius1 < 0 or radius2 <= 0:
                raise ValueError(
                    f"Radius must be positive and larger radius larger than 0, got {radius1} and {radius2}"
                )

        except Exception as error:
            db.log_error(str(error))
            db.outputs.execOut = og.ExecutionAttributeState.DISABLED
            return False

        samples = []
        for _ in range(len(prims)):
            # Generate a random direction by spherical coordinates (phi, theta)
            phi = np.random.uniform(0, 2 * np.pi)
            # Sample costheta to ensure uniform distribution of points on the sphere (surface is proportional to sin(theta))
            costheta = np.random.uniform(-1, 1)
            theta = np.arccos(costheta)

            # Uniformly distribute points between two spheres by weighting the radius to match volume growth (r^3),
            # ensuring spatial uniformity by taking the cube root of a value between the radii cubed.
            r = (np.random.uniform(radius1**3, radius2**3)) ** (1 / 3.0)

            # Convert from spherical to Cartesian coordinates
            x = r * np.sin(theta) * np.cos(phi)
            y = r * np.sin(theta) * np.sin(phi)
            z = r * np.cos(theta)

            samples.append((x, y, z))

        with Sdf.ChangeBlock():
            for prim, sample in zip(prims, samples):
                prim.GetAttribute("xformOp:translate").Set(sample)

        db.outputs.execOut = og.ExecutionAttributeState.ENABLED
        return True
```

After this step, the randomizers will be available as nodes in the graph editor. For this tutorial the nodes are already added to the built-in `isaacsim.replicator.examples` extension and are available by default. Other custom nodes created through the OmniGraph tutorial will be accessible through the `omni.new.extension` extension (if the default tutorial-provided extension name was used). An example of accessing the nodes in an action graph is depicted below:

Note

If the custom nodes are not available, the newly created extension needs to be enabled. This can be done by navigating to **Window > Extensions > THIRD PARTY > ``omni.new.extension`` > ENABLED**:

After the OmniGraph randomization nodes are created, they can be manually added to a pre-existing SDG pipeline graph. To create a basic SDG graph, the following snippet can be used in the Script Editor to randomize the rotations of the created cubes every frame.

Basic SDG Pipeline

```python
import omni.replicator.core as rep

cube = rep.create.cube(count=50, scale=0.1)
with rep.trigger.on_frame():
    with cube:
        rep.randomizer.rotation()
```

After the snippet is executed in the Script Editor, the generated graph can be opened at `/Replicator/SDGPipeline` and the custom nodes can be added to the graph. The following image shows the result after the custom nodes are added to the SDG pipeline graph together with the resulting randomization (from the UI using `Tools` > `Replicator` > `Preview` or `Step`):

To avoid manually adding the custom nodes to the SDG pipeline graph, the Replicator API can be used to automatically insert the nodes into the graph. For this purpose, the nodes need to be encapsulated as **ReplicatorItems** using the `@ReplicatorWrapper` decorator. The following code snippet demonstrates how **ReplicatorItems** can be created for the custom nodes:

ReplicatorWrapper

```python
import omni.replicator.core as rep
from omni.replicator.core.scripts.utils import (
    ReplicatorItem,
    ReplicatorWrapper,
    create_node,
    set_target_prims,
)

@ReplicatorWrapper
def on_sphere(
    radius: float = 1.0,
    input_prims: ReplicatorItem | list[str] | None = None,
) -> ReplicatorItem:

    node = create_node("isaacsim.replicator.examples.OgnSampleOnSphere", radius=radius)
    if input_prims:
        set_target_prims(node, "inputs:prims", input_prims)
    return node

@ReplicatorWrapper
def in_sphere(
    radius: float = 1.0,
    input_prims: ReplicatorItem | list[str] | None = None,
) -> ReplicatorItem:

    node = create_node("isaacsim.replicator.examples.OgnSampleInSphere", radius=radius)
    if input_prims:
        set_target_prims(node, "inputs:prims", input_prims)
    return node

@ReplicatorWrapper
def between_spheres(
    radius1: float = 0.5,
    radius2: float = 1.0,
    input_prims: ReplicatorItem | list[str] | None = None,
) -> ReplicatorItem:

    node = create_node("isaacsim.replicator.examples.OgnSampleBetweenSpheres", radius1=radius1, radius2=radius2)
    if input_prims:
        set_target_prims(node, "inputs:prims", input_prims)
    return node

prim_count = 50
prim_scale = 0.1
rad_in = 0.5
rad_on = 1.5
rad_bet1 = 2.5
rad_bet2 = 3.5

# Create the default prims
sphere = rep.create.sphere(count=prim_count, scale=prim_scale)
cube = rep.create.cube(count=prim_count, scale=prim_scale)
cylinder = rep.create.cylinder(count=prim_count, scale=prim_scale)

# Create the randomization graph
with rep.trigger.on_frame():
    with sphere:
        rep.randomizer.rotation()
        in_sphere(rad_in)

    with cube:
        rep.randomizer.rotation()
        on_sphere(rad_on)

    with cylinder:
        rep.randomizer.rotation()
        between_spheres(rad_bet1, rad_bet2)
```

Note

For this tutorial the `create_node` function uses `"isaacsim.replicator.examples.OgnSampleInSphere"` as the node path, this path needs to be replaced in case the custom nodes are not part of the built-in `isaacsim.replicator.examples` extension.

After the snippet is executed in the Script Editor, the custom nodes will be automatically added to the SDG pipeline graph. To trigger the randomization, `Tools` > `Replicator` > `Preview` (or `Step`) can be called from the UI. The following image shows the generated graph and the resulting randomization:

On this page

* [Learning Objectives](#learning-objectives)
* [Prerequisites](#prerequisites)
* [Implementation](#implementation)

---

### Recorder

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/replicator_tutorials/tutorial_replicator_recorder.html

* [Synthetic Data Generation](../synthetic_data_generation/index.html)
* [Perception Data Generation (Replicator)](index.html)
* Synthetic Data Recorder

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Synthetic Data Recorder

This tutorial introduces the Synthetic Data Recorder for Isaac Sim, which is a GUI extension for recording synthetic data with the possibility of using [custom writers](https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator/custom_writer.html "(in Omniverse Extensions)") to record the data in various formats.

The Synthetic Data Recorder requires assets to be [semantically labelled](https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator/semantics_schema_editor.html "(in Omniverse Extensions)") for all of the annotators to work correctly. The recorder uses the `BasicWriter` by default with access to most common [annotators](https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator/annotators_details.html "(in Omniverse Extensions)").

## Getting Started

The UI window can be opened from the main menu using **Tools** > **Replicator** > **Synthetic Data Recorder**.

This tutorial uses the following stage as an example:

```python
https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Isaac/6.0
/Isaac/Samples/Replicator/Stage/full_warehouse_worker_and_anim_cameras.usd
```

The stage asset can be found in the **Content Browser** under **Isaac Sim** > **Samples** > **Replicator** > **Stage** > **full\_warehouse\_worker\_and\_anim\_cameras.usd**, or can be loaded using by inserting the whole URL in the path field.

The example stage comes preloaded with semantic annotations and multiple cameras. Some of the included cameras are animated to move around the scene when running the simulation. To create custom camera movement animations, review the [Camera Animation Tutorial](https://docs.omniverse.nvidia.com/extensions/latest/ext_animation-timeline.html "(in Omniverse Extensions)").

## Basic Usage

The recorder is split into two main parts:

* the **Writer** frame - containing sensor, data, and output parameters
* the **Control** frame - containing the recording functionalities such as start, stop, pause, and parameters such as the number of frames to execute

### Writer Frame

The **Writer** frame provides access to **Render Products**, **Parameters**, **Output**, and **Config** options.

The **Render Products** frame allows the creation of a list of render product entries using the **Add New Render Product** button. By default, a new entry is added to the list using the active viewport camera as its camera path (see left figure). If cameras are selected in the stage viewer, these are added to the render products list (see right figure). The render products list can include the same camera path multiple times, with each instance having a different resolution. All entry values, such as camera path or resolution, can be manually edited in the input fields.

The **Parameters** frame offers a choice between the default built-in Replicator writer (`BasicWriter`) and a custom writer. Default writer parameters, primarily annotators, can be selected from the checkbox list. Parameters for custom writers, which are unknown beforehand, must be provided in the form of a JSON file containing all required parameters. The path to the JSON file is entered in the **Parameters Path** input field.

The **Output** frame (left figure) specifies the working directory path where the data is saved, along with the folder name for the current recording. The output folder name is incremented in case of conflicts. The recorder also supports writing to S3 buckets by enabling **Use S3**, entering the required fields, and ensuring AWS credentials are properly configured.

Note

When writing to S3, the **Increment** folder naming feature is not supported and defaults to **Timestamp**.

The **Config** frame (right figure) allows loading and saving the GUI writer state as a JSON configuration file. By default, the extension loads the most recently used configuration state.

### Control Frame

The **Control** frame contains the recording functionalities such as Start/Stop and Pause/Resume, and parameters such as the number of frames to record or the number of subframes to render for each recorded frame.

* The **Start** button creates a writer, given the selected parameters, and starts the recording.
* The **Stop** button stops the recording and clears the writer.
* The **Pause** button pauses the recording without clearing the writer.
* The **Resume** button resumes the recording.
* The **Number of Frames** input field sets the number of frames to record, after which the recorder is stopped and the writer cleared. If the value is set to `0`, the recording runs indefinitely or until the **Stop** button is pressed.
* The **RTSubframes** field sets the number of additional subframes to render for each per frame. This can be used if randomized materials are not loaded in time or if temporal rendering artifacts (such as ghosting) are present due to objects being teleported.
* The **Control Timeline** checkbox starts, stops, pauses, and resumes the timeline together with the recorder.
* The **Verbose** checkbox enables verbose logging for the recorder (events such as start, stop, pause, resume, and the number of frames recorded).

Note

To improve the rendering quality, or to avoid any rendering artifacts caused by low lighting conditions or fast-moving objects, increase the **RTSubframes** parameter. This renders multiple subframes for each frame, thereby improving the quality of recorded data at the expense of longer rendering times per frame. For more details, see the [subframes](https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator/subframes_examples.html#subframes-examples "(in Omniverse Extensions)") documentation.

## Custom Writer Example

To support custom data formats, the custom writer can be registered and loaded from the GUI. In this example, a custom writer called `MyCustomWriter` is registered using the [Script Editor](../development_tools/omniverse_script_editor.html#script-editor) for use with the recorder.

The Synthetic Data Recorder initializes the selected disk or cloud backend, then calls `writer.initialize(backend=..., **parameters)`. Starting in recent Isaac Sim / Replicator releases, those keyword arguments are applied when the writer is constructed. Custom writers must therefore accept a `backend` argument (the configured `DiskBackend` or `S3Backend` instance) or accept arbitrary keyword arguments with `**kwargs`. They should write using that backend rather than constructing a separate `BackendDispatch` from a raw output path when `backend` is supplied.

MyCustomWriter

```python
import numpy as np
import omni.replicator.core as rep
from omni.replicator.core import AnnotatorRegistry, BackendDispatch, Writer
from omni.replicator.core import functional as F
from omni.replicator.core.scripts.backends import BaseBackend

class MyCustomWriter(Writer):
    """Minimal disk writer for rgb / normals (compatible with ``DiskBackend`` from the Synthetic Data Recorder)."""

    def __init__(
        self,
        rgb: bool = True,
        normals: bool = False,
        output_dir: str | None = None,
        backend: BaseBackend | None = None,
        **kwargs,
    ):
        self.version = "0.0.1"
        self.data_structure = "renderProduct"

        if backend is not None and not isinstance(backend, BaseBackend):
            raise TypeError("`backend` must inherit from `omni.replicator.core.scripts.backends.BaseBackend`.")

        if backend is not None:
            self.backend = backend
        elif output_dir:
            self.backend = BackendDispatch(output_dir=output_dir)
        else:
            raise ValueError("Provide `backend` (for example from the recorder) or `output_dir`.")

        self.annotators = []
        if rgb:
            self.annotators.append(AnnotatorRegistry.get_annotator("rgb"))
        if normals:
            self.annotators.append(AnnotatorRegistry.get_annotator("normals"))
        self._frame_id = 0

    def write(self, data: dict):
        if "renderProducts" in data:
            for rp_name, annotators_data in data["renderProducts"].items():
                rp_prefix = f"{rp_name}/"
                if "rgb" in annotators_data:
                    rgb_entry = annotators_data["rgb"]
                    rgb_arr = rgb_entry["data"] if isinstance(rgb_entry, dict) and "data" in rgb_entry else rgb_entry
                    self.backend.schedule(F.write_image, path=f"{rp_prefix}rgb/rgb_{self._frame_id}.png", data=rgb_arr)
                if "normals" in annotators_data:
                    n_entry = annotators_data["normals"]
                    n_arr = n_entry["data"] if isinstance(n_entry, dict) and "data" in n_entry else n_entry
                    colored = ((n_arr * 0.5 + 0.5) * 255).astype(np.uint8)
                    self.backend.schedule(
                        F.write_image, path=f"{rp_prefix}normals/normals_{self._frame_id}.png", data=colored
                    )
            self._frame_id += 1
            return

        for annotator in list(data.keys()):
            annotator_split = annotator.split("-")
            render_product_path = ""
            multi_render_prod = 0
            if len(annotator_split) > 1:
                multi_render_prod = 1
                render_product_name = annotator_split[-1]
                render_product_path = f"{render_product_name}/"

            if annotator.startswith("rgb"):
                if multi_render_prod:
                    render_product_path += "rgb/"
                filename = f"{render_product_path}rgb_{self._frame_id}.png"
                print(f"[{self._frame_id}] Writing {filename} ..")
                self.backend.schedule(F.write_image, path=filename, data=data[annotator])

            if annotator.startswith("normals"):
                if multi_render_prod:
                    render_product_path += "normals/"
                filename = f"{render_product_path}normals_{self._frame_id}.png"
                print(f"[{self._frame_id}] Writing {filename} ..")
                colored_data = ((data[annotator] * 0.5 + 0.5) * 255).astype(np.uint8)
                self.backend.schedule(F.write_image, path=filename, data=colored_data)

        self._frame_id += 1

    def on_final_frame(self):
        self._frame_id = 0

rep.writers.register_writer(MyCustomWriter)
```

my\_params.json

```python
1{
2    "rgb": true,
3    "normals": true
4}
```

### Data Visualization Writer

The **Data Visualization** writer is a custom writer that can be used to visualize the annotation data on top of rendered images. The writer and its implementation details can be found in `/isaacsim.replicator.writers/python/scripts/writers/data_visualization_writer.py`, and can be imported using `from isaacsim.replicator.writers import DataVisualizationWriter`. The custom writer can be selected from the **Parameters** frame and its parameters can be loaded from a JSON file using the **Parameters Path** input field. Here is an example JSON file that can be used to parameterize the writer:

my\_data\_visualization\_params.json

```python
 1{
 2    "bounding_box_2d_tight": true,
 3    "bounding_box_2d_tight_params": {
 4        "background": "rgb",
 5        "outline": "green",
 6        "fill": null
 7    },
 8    "bounding_box_2d_loose": true,
 9    "bounding_box_2d_loose_params": {
10        "background": "normals",
11        "outline": "red",
12        "fill": null
13    },
14    "bounding_box_3d": true,
15    "bounding_box_3d_params": {
16        "background": "rgb",
17        "fill": "blue",
18        "width": 2
19    }
20}
```

And the resulting data:

For more information on the supported parameters, see the class docstring:

DataVisualizationWriter class docstring

```python
"""Data Visualization Writer

This writer can be used to visualize various annotator data.

Supported annotators:
- bounding_box_2d_tight
- bounding_box_2d_loose
- bounding_box_3d

Supported backgrounds:
- rgb
- normals

Args:
    output_dir (str):
        Output directory for the data visualization files forwarded to the backend writer.
    bounding_box_2d_tight (bool, optional):
        If True, 2D tight bounding boxes will be drawn on the selected background (transparent by default).
        Defaults to False.
    bounding_box_2d_tight_params (dict, optional):
        Parameters for the 2D tight bounding box annotator. Defaults to None.
    bounding_box_2d_loose (bool, optional):
        If True, 2D loose bounding boxes will be drawn on the selected background (transparent by default).
        Defaults to False.
    bounding_box_2d_loose_params (dict, optional):
        Parameters for the 2D loose bounding box annotator. Defaults to None.
    bounding_box_3d (bool, optional):
        If True, 3D bounding boxes will be drawn on the selected background (transparent by default). Defaults to False.
    bounding_box_3d_params (dict, optional):
        Parameters for the 3D bounding box annotator. Defaults to None.
    frame_padding (int, optional):
        Number of digits used for the frame number in the file name. Defaults to 4.

"""
```

## Replicator Randomized Cameras

To take advantage of Replicator randomization techniques, randomized cameras can be loaded using the [Script Editor](../development_tools/omniverse_script_editor.html#script-editor) before starting the recorder to run scene randomizations during recording. In this example a randomized camera is created using the Replicator API. This can be attached as a render product to the recorder and for each frame the camera is randomized with the given parameters.

```python
import omni.replicator.core as rep

camera = rep.create.camera()
with rep.trigger.on_frame():
    with camera:
        rep.modify.pose(
            position=rep.distribution.uniform((-5, 5, 1), (-1, 15, 5)),
            look_at="/Root/Warehouse/SM_CardBoxA_3",
        )
```

## Recording Loop Overview

The **Synthetic Data Recorder** is a GUI extension for Isaac Sim that uses the `BasicWriter` or custom Replicator writers for capturing data. Its implementation is located in `/isaacsim.replicator.synthetic_recorder/isaacsim/replicator/synthetic_recorder/synthetic_recorder.py` and utilizes the `orchestrator.step(rt_subframes, pause_timeline, delta_time)` function to manage the recording process. This function ensures that recorded frames remain synchronized with the stage by waiting for any “frames in flight” from the renderer. For integration with the UI, the recorder uses the asynchronous version of this function: `step_async`.

```python
while self._current_frame < num_frames:
    timeline = omni.timeline.get_timeline_interface()

    if self.control_timeline and not timeline.is_playing():
        timeline.play()
        timeline.commit()

    await rep.orchestrator.step_async(rt_subframes=self.rt_subframes, delta_time=None, pause_timeline=False)

    self._current_frame += 1
```

The recording loop offers flexibility for different use cases. It can advance the timeline for dynamic scenes, such as simulations or animations, or operate without advancing the timeline for static captures. This approach enables recording scenarios like randomizing views, adjusting lighting conditions, or repositioning objects.

On this page

* [Getting Started](#getting-started)
* [Basic Usage](#basic-usage)
  + [Writer Frame](#writer-frame)
  + [Control Frame](#control-frame)
* [Custom Writer Example](#custom-writer-example)
  + [Data Visualization Writer](#data-visualization-writer)
* [Replicator Randomized Cameras](#replicator-randomized-cameras)
* [Recording Loop Overview](#recording-loop-overview)

---

### Augmentation

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/replicator_tutorials/tutorial_replicator_augmentation.html

* [Synthetic Data Generation](../synthetic_data_generation/index.html)
* [Perception Data Generation (Replicator)](index.html)
* Data Augmentation

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Data Augmentation

Example of using Isaac Sim and Replicator to capture augmented synthetic data.

## Learning Objectives

This tutorial provides examples on how to use omni.replicator [augmentations](https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator/augmentation_examples.html "(in Omniverse Extensions)") on annotators or writers. The provided examples will showcase how to augment **rgb** and **depth** annotator data using warp (GPU) or NumPy (CPU) kernel/filters. The use of warp is particularly advantageous for executing parallelizable tasks, especially if the data already resides in the GPUs memory, thus avoiding memory copies from GPU to CPU.

* For a better understanding of the tutorial, familiarity with [omni.replicator](https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator.html "(in Omniverse Extensions)"), [annotators](https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator/annotators_details.html "(in Omniverse Extensions)"), [writers](https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator/writer_examples.html "(in Omniverse Extensions)") and [warp](https://docs.omniverse.nvidia.com/extensions/latest/ext_warp.html "(in Omniverse Extensions)") is recommended.

## Scenario

The depicted figure showcases the example augmentations used throughout the examples. The first image is an illustrative example switching the red and blue channels of the image. The second image is a composed augmentation of converting the rgb data to hsv, adding gaussian noise, and converting back to rgb. The third and forth image are results of applying gaussian noise filters with various sigma values to the depth data.

For the example scenario a red cube is spawned with a camera looking at it from a top view. For the cube a replicator randomization graph is created which is triggered by a custom event sent before each capture step, producing a random rotation for every frame capture.

## Implementation

The tutorial is split into two parts, the first example will showcase how to augment annotators directly, and secondly how to augment writers. Both examples can be run as [Standalone Applications](../introduction/workflows.html#standalone-application) or from the UI using the [Script Editor](../development_tools/omniverse_script_editor.html#script-editor).

### Annotator Augmentation

The annotator example will output rgb images with the red and blue channels switched, and two depth images with different gaussian noise levels (saved as grayscale PNGs). The example can switch between using warp or NumPy augmentations.

Standalone Application

The example can be run as a standalone application using the following commands in the terminal (on Windows use `python.bat` instead of `python.sh`):

```python
./python.sh standalone_examples/replicator/augmentation/annotator_augmentation.py --env_url /Isaac/Environments/Grid/default_environment.usd
```

Optionally the following arguments can be used to change the default behavior:

* `--env_url` – USD environment path relative to the assets root (default: empty scene with dome light and ground plane)
* `--use_warp` – flag to use warp (GPU) instead of numpy (CPU) for the augmentation functions (default: False)
* `--num_frames` – the number of frames to be captured (default: 25)

```python
./python.sh standalone_examples/replicator/augmentation/annotator_augmentation.py --use_warp --num_frames 25 --env_url /Isaac/Environments/Grid/default_environment.usd
```

Full Standalone Script

```python
"""Generate augmented synthetic data from annotators."""

from isaacsim import SimulationApp

simulation_app = SimulationApp(launch_config={"headless": False})

import argparse
import os
import time

import carb.settings
import numpy as np
import omni.replicator.core as rep
import omni.usd
import warp as wp
from isaacsim.core.utils.stage import open_stage
from isaacsim.storage.native import get_assets_root_path
from omni.replicator.core.functional import write_image

parser = argparse.ArgumentParser()
parser.add_argument("--num_frames", type=int, default=5, help="The number of frames to capture")
parser.add_argument(
    "--use_warp",
    action="store_true",
    help="Use warp augmentations instead of numpy",
)
parser.add_argument("--resolution", nargs=2, type=int, default=[512, 512], help="Camera resolution")
parser.add_argument("--env_url", type=str, default="", help="USD environment URL (empty for basic scene)")
args, unknown = parser.parse_known_args()

num_frames = args.num_frames
use_warp = args.use_warp
resolution = args.resolution
env_url = args.env_url or None
SEED = 42

# Enable warp scripts
carb.settings.get_settings().set_bool("/app/omni.graph.scriptnode/opt_in", True)

def rgb_to_bgr_np(data_in):
    """Swap RGBA red and blue channels using NumPy (CPU)."""
    data_in[:, :, [0, 2]] = data_in[:, :, [2, 0]]
    return data_in

@wp.kernel
def rgb_to_bgr_wp(data_in: wp.array3d(dtype=wp.uint8), data_out: wp.array3d(dtype=wp.uint8)):
    """Swap RGBA red and blue channels using Warp (GPU)."""
    i, j = wp.tid()
    data_out[i, j, 0] = data_in[i, j, 2]
    data_out[i, j, 1] = data_in[i, j, 1]
    data_out[i, j, 2] = data_in[i, j, 0]
    data_out[i, j, 3] = data_in[i, j, 3]

def gaussian_noise_depth_np(data_in, sigma: float, seed: int):
    """Add Gaussian noise to depth values using NumPy (CPU)."""
    np.random.seed(seed)
    result = data_in.astype(np.float32) + np.random.randn(*data_in.shape) * sigma
    return np.clip(result, 0, None).astype(data_in.dtype)

rep.annotators.register_augmentation(
    "gn_depth_np", rep.annotators.Augmentation.from_function(gaussian_noise_depth_np, sigma=0.1, seed=SEED)
)

@wp.kernel
def gaussian_noise_depth_wp(
    data_in: wp.array2d(dtype=wp.float32), data_out: wp.array2d(dtype=wp.float32), sigma: float, seed: int
):
    """Add Gaussian noise to depth values using Warp (GPU)."""
    i, j = wp.tid()
    # Unique ID for random seed per pixel
    scalar_pixel_id = i * data_in.shape[1] + j
    state = wp.rand_init(seed, scalar_pixel_id)
    data_out[i, j] = data_in[i, j] + sigma * wp.randn(state)

rep.annotators.register_augmentation(
    "gn_depth_wp", rep.annotators.Augmentation.from_function(gaussian_noise_depth_wp, sigma=0.1, seed=SEED)
)

def convert_depth_to_uint8(data):
    """Normalize depth data and convert it to uint8 grayscale."""
    if isinstance(data, wp.array):
        data = data.numpy()
    depth = data.astype(np.float32, copy=False)
    depth[np.isinf(depth)] = np.nan
    mean_val = np.nanmean(depth)
    if np.isnan(mean_val):
        mean_val = 0.0
    depth = np.nan_to_num(depth, nan=mean_val, copy=False)
    min_val = depth.min()
    max_val = depth.max()
    if max_val <= min_val:
        return np.zeros(depth.shape, dtype=np.uint8)
    normalized = (depth - min_val) / (max_val - min_val)
    return (normalized * 255.0).astype(np.uint8)

def run_example(num_frames: int, resolution: tuple[int, int], use_warp: bool, env_url: str | None = None) -> float:
    """Run the capture pipeline using step() to trigger a randomization and data capture."""
    print(f"Running example with num_frames: {num_frames}, resolution: {resolution}, use_warp: {use_warp}")

    if env_url is not None and env_url != "":
        assets_root_path = get_assets_root_path()
        stage_path = assets_root_path + env_url
        print(f"Opening stage: {stage_path}")
        open_stage(stage_path)
    else:
        omni.usd.get_context().new_stage()
        rep.functional.create.dome_light(intensity=1000, rotation=(270, 0, 0))
        ground_plane = rep.functional.create.plane(scale=(10, 10, 1), position=(0, 0, 0))
        rep.functional.physics.apply_collider(ground_plane)

    # Use a fixed global seed for reproducibility
    rep.set_global_seed(SEED)

    # Disable capture on play, data is captured manually using the step function
    rep.orchestrator.set_capture_on_play(False)

    # Set DLSS to Quality mode (2) for best SDG results (Options: 0 (Performance), 1 (Balanced), 2 (Quality), 3 (Auto)
    carb.settings.get_settings().set("rtx/post/dlss/execMode", 2)

    # Augment the RGB and depth annotators
    rgb_to_bgr_augm = rep.annotators.Augmentation.from_function(rgb_to_bgr_wp if use_warp else rgb_to_bgr_np)
    depth_aug = rep.annotators.get_augmentation("gn_depth_wp" if use_warp else "gn_depth_np")
    rgb_to_bgr_annot = rep.annotators.augment(
        source_annotator=rep.annotators.get("rgb"),
        augmentation=rgb_to_bgr_augm,
    )
    depth_annot_1 = rep.annotators.get("distance_to_camera")
    depth_annot_1.augment(depth_aug)
    depth_annot_2 = rep.annotators.get("distance_to_camera")
    depth_annot_2.augment(depth_aug, sigma=0.5)

    # Create the render product and attach the annotators to it
    cam = rep.functional.create.camera(position=(0, 0, 5), look_at=(0, 0, 0))
    rp = rep.create.render_product(cam, resolution)
    rgb_to_bgr_annot.attach(rp)
    depth_annot_1.attach(rp)
    depth_annot_2.attach(rp)

    # Create a red cube and randomize its rotation on a custom event sent before each capture step
    red_cube = rep.functional.create.cube(position=(0, 0, 0.71))
    rep.functional.create.material(mdl="OmniPBR.mdl", bind_prims=[red_cube], diffuse_color_constant=(1, 0, 0))

    with rep.trigger.on_custom_event(event_name="randomize_red_cube"):
        red_cube_node = rep.get.prim_at_path(red_cube.GetPath())
        with red_cube_node:
            rep.randomizer.rotation()

    # Output directory
    out_dir = os.path.join(os.getcwd(), f"_out_augm_annot_{'warp' if use_warp else 'numpy'}")
    print(f"Writing data to: {out_dir}")
    os.makedirs(out_dir, exist_ok=True)

    capture_start = time.time()
    for frame_idx in range(num_frames):
        print(f"  Capturing frame {frame_idx + 1}/{num_frames}")
        rep.utils.send_og_event(event_name="randomize_red_cube")
        rep.orchestrator.step(rt_subframes=32)

        # Get the data from the annotators
        rgb_data = rgb_to_bgr_annot.get_data()
        depth_data_1 = depth_annot_1.get_data()
        depth_data_2 = depth_annot_2.get_data()

        # Schedule the write of the data to disk
        write_image(path=os.path.join(out_dir, f"annot_rgb_{frame_idx}.png"), data=rgb_data)
        write_image(
            path=os.path.join(out_dir, f"annot_depth_1_{frame_idx}.png"),
            data=convert_depth_to_uint8(depth_data_1),
        )
        write_image(
            path=os.path.join(out_dir, f"annot_depth_2_{frame_idx}.png"),
            data=convert_depth_to_uint8(depth_data_2),
        )

    # Wait for the data to be written to disk and release resources
    rep.orchestrator.wait_until_complete()
    rgb_to_bgr_annot.detach()
    depth_annot_1.detach()
    depth_annot_2.detach()
    rp.destroy()

    return time.time() - capture_start

duration = run_example(num_frames, resolution, use_warp, env_url)
average = duration / num_frames if num_frames else 0.0
mode_label = "warp" if use_warp else "numpy"
print(
    f"The duration for capturing {num_frames} frames using '{mode_label}' was: {duration:.4f} seconds, "
    f"with an average of {average:.4f} seconds per frame."
)

simulation_app.close()
```

Script Editor

Full Script Editor Script

```python
import asyncio
import os
import time

import carb.settings
import numpy as np
import omni.replicator.core as rep
import warp as wp
from isaacsim.core.experimental.utils.stage import open_stage
from isaacsim.storage.native import get_assets_root_path_async
from omni.replicator.core.functional import write_image

NUM_FRAMES = 5
RESOLUTION = (512, 512)
USE_WARP = False
ENV_URL = "/Isaac/Environments/Grid/default_environment.usd"
SEED = 42

# Enable warp scripts
carb.settings.get_settings().set_bool("/app/omni.graph.scriptnode/opt_in", True)

def rgb_to_bgr_np(data_in):
    """Swap RGBA red and blue channels using NumPy (CPU)."""
    data_in[:, :, [0, 2]] = data_in[:, :, [2, 0]]
    return data_in

@wp.kernel
def rgb_to_bgr_wp(data_in: wp.array3d(dtype=wp.uint8), data_out: wp.array3d(dtype=wp.uint8)):
    """Swap RGBA red and blue channels using Warp (GPU)."""
    i, j = wp.tid()
    data_out[i, j, 0] = data_in[i, j, 2]
    data_out[i, j, 1] = data_in[i, j, 1]
    data_out[i, j, 2] = data_in[i, j, 0]
    data_out[i, j, 3] = data_in[i, j, 3]

def gaussian_noise_depth_np(data_in, sigma: float, seed: int):
    """Add Gaussian noise to depth values using NumPy (CPU)."""
    np.random.seed(seed)
    result = data_in.astype(np.float32) + np.random.randn(*data_in.shape) * sigma
    return np.clip(result, 0, None).astype(data_in.dtype)

rep.annotators.register_augmentation(
    "gn_depth_np", rep.annotators.Augmentation.from_function(gaussian_noise_depth_np, sigma=0.1, seed=SEED)
)

@wp.kernel
def gaussian_noise_depth_wp(
    data_in: wp.array2d(dtype=wp.float32), data_out: wp.array2d(dtype=wp.float32), sigma: float, seed: int
):
    """Add Gaussian noise to depth values using Warp (GPU)."""
    i, j = wp.tid()
    # Unique ID for random seed per pixel
    scalar_pixel_id = i * data_in.shape[1] + j
    state = wp.rand_init(seed, scalar_pixel_id)
    data_out[i, j] = data_in[i, j] + sigma * wp.randn(state)

rep.annotators.register_augmentation(
    "gn_depth_wp", rep.annotators.Augmentation.from_function(gaussian_noise_depth_wp, sigma=0.1, seed=SEED)
)

def convert_depth_to_uint8(data):
    """Normalize depth data and convert it to uint8 grayscale."""
    if isinstance(data, wp.array):
        data = data.numpy()
    depth = data.astype(np.float32, copy=False)
    depth[np.isinf(depth)] = np.nan
    mean_val = np.nanmean(depth)
    if np.isnan(mean_val):
        mean_val = 0.0
    depth = np.nan_to_num(depth, nan=mean_val, copy=False)
    min_val = depth.min()
    max_val = depth.max()
    if max_val <= min_val:
        return np.zeros(depth.shape, dtype=np.uint8)
    normalized = (depth - min_val) / (max_val - min_val)
    return (normalized * 255.0).astype(np.uint8)

# Run the capture pipeline using step() to trigger a randomization and data capture
async def run_example_async(num_frames: int, resolution: tuple[int, int], use_warp: bool) -> float:
    print(f"Running example with num_frames: {num_frames}, resolution: {resolution}, use_warp: {use_warp}")

    # Open a new stage
    assets_root_path = await get_assets_root_path_async()
    stage_path = assets_root_path + ENV_URL
    print(f"Opening stage: {stage_path}")
    open_stage(stage_path)

    # Use a fixed global seed for reproducibility
    rep.set_global_seed(SEED)

    # Disable capture on play, data is captured manually using the step function
    rep.orchestrator.set_capture_on_play(False)

    # Set DLSS to Quality mode (2) for best SDG results (Options: 0 (Performance), 1 (Balanced), 2 (Quality), 3 (Auto)
    carb.settings.get_settings().set("rtx/post/dlss/execMode", 2)

    # Augment the RGB and depth annotators
    rgb_to_bgr_augm = rep.annotators.Augmentation.from_function(rgb_to_bgr_wp if use_warp else rgb_to_bgr_np)
    depth_aug = rep.annotators.get_augmentation("gn_depth_wp" if use_warp else "gn_depth_np")
    rgb_to_bgr_annot = rep.annotators.augment(
        source_annotator=rep.annotators.get("rgb"),
        augmentation=rgb_to_bgr_augm,
    )
    depth_annot_1 = rep.annotators.get("distance_to_camera")
    depth_annot_1.augment(depth_aug)
    depth_annot_2 = rep.annotators.get("distance_to_camera")
    depth_annot_2.augment(depth_aug, sigma=0.5)

    # Create the render product and attach the annotators to it
    cam = rep.functional.create.camera(position=(0, 0, 5), look_at=(0, 0, 0))
    rp = rep.create.render_product(cam, resolution)
    rgb_to_bgr_annot.attach(rp)
    depth_annot_1.attach(rp)
    depth_annot_2.attach(rp)

    # Create a red cube and randomize its rotation on a custom event sent before each capture step
    red_cube = rep.functional.create.cube(position=(0, 0, 0.71))
    rep.functional.create.material(mdl="OmniPBR.mdl", bind_prims=[red_cube], diffuse_color_constant=(1, 0, 0))

    with rep.trigger.on_custom_event(event_name="randomize_red_cube"):
        red_cube_node = rep.get.prim_at_path(red_cube.GetPath())
        with red_cube_node:
            rep.randomizer.rotation()

    # Output directory
    out_dir = os.path.join(os.getcwd(), "_out_augm_annot")
    print(f"Writing data to: {out_dir}")
    os.makedirs(out_dir, exist_ok=True)

    capture_start = time.time()
    for frame_idx in range(num_frames):
        print(f"  Capturing frame {frame_idx + 1}/{num_frames}")
        rep.utils.send_og_event(event_name="randomize_red_cube")
        await rep.orchestrator.step_async(rt_subframes=32)

        # Get the data from the annotators
        rgb_data = rgb_to_bgr_annot.get_data()
        depth_data_1 = depth_annot_1.get_data()
        depth_data_2 = depth_annot_2.get_data()

        # Schedule the write of the data to disk
        write_image(path=os.path.join(out_dir, f"annot_rgb_{frame_idx}.png"), data=rgb_data)
        write_image(
            path=os.path.join(out_dir, f"annot_depth_1_{frame_idx}.png"),
            data=convert_depth_to_uint8(depth_data_1),
        )
        write_image(
            path=os.path.join(out_dir, f"annot_depth_2_{frame_idx}.png"),
            data=convert_depth_to_uint8(depth_data_2),
        )

    # Wait for the data to be written to disk and release resources
    await rep.orchestrator.wait_until_complete_async()
    rgb_to_bgr_annot.detach()
    depth_annot_1.detach()
    depth_annot_2.detach()
    rp.destroy()

    return time.time() - capture_start

def on_task_done(task: asyncio.Task):
    """Report timing information when capture completes."""
    duration = task.result()
    average = duration / NUM_FRAMES if NUM_FRAMES else 0.0
    mode_label = "warp" if USE_WARP else "numpy"
    print(
        f"The duration for capturing {NUM_FRAMES} frames using '{mode_label}' was: {duration:.4f} seconds, "
        f"with an average of {average:.4f} seconds per frame."
    )

task = asyncio.ensure_future(run_example_async(NUM_FRAMES, RESOLUTION, USE_WARP))
task.add_done_callback(on_task_done)
```

Code Explanation

To be able to run the augmentation functions, enable scripting in the settings:

Enable Scripting

```python
# Enable warp scripts
carb.settings.get_settings().set_bool("/app/omni.graph.scriptnode/opt_in", True)
```

To augment the **rgb** data we provide for illustrative purposes a function that switches the red and blue channels in the rgb data using NumPy (CPU) and warp (GPU) kernels:

RGB to BGR using Warp and Numpy

```python
def rgb_to_bgr_np(data_in):
    """Swap RGBA red and blue channels using NumPy (CPU)."""
    data_in[:, :, [0, 2]] = data_in[:, :, [2, 0]]
    return data_in

@wp.kernel
def rgb_to_bgr_wp(data_in: wp.array3d(dtype=wp.uint8), data_out: wp.array3d(dtype=wp.uint8)):
    """Swap RGBA red and blue channels using Warp (GPU)."""
    i, j = wp.tid()
    data_out[i, j, 0] = data_in[i, j, 2]
    data_out[i, j, 1] = data_in[i, j, 1]
    data_out[i, j, 2] = data_in[i, j, 0]
    data_out[i, j, 3] = data_in[i, j, 3]
```

For the **depth** data we use gaussian noise filters. Note that the functions are registered in the annotator registry for later access:

Depth Gaussian Noise using Warp and Numpy

```python
def gaussian_noise_depth_np(data_in, sigma: float, seed: int):
    """Add Gaussian noise to depth values using NumPy (CPU)."""
    np.random.seed(seed)
    result = data_in.astype(np.float32) + np.random.randn(*data_in.shape) * sigma
    return np.clip(result, 0, None).astype(data_in.dtype)

rep.annotators.register_augmentation(
    "gn_depth_np", rep.annotators.Augmentation.from_function(gaussian_noise_depth_np, sigma=0.1, seed=SEED)
)

@wp.kernel
def gaussian_noise_depth_wp(
    data_in: wp.array2d(dtype=wp.float32), data_out: wp.array2d(dtype=wp.float32), sigma: float, seed: int
):
    """Add Gaussian noise to depth values using Warp (GPU)."""
    i, j = wp.tid()
    # Unique ID for random seed per pixel
    scalar_pixel_id = i * data_in.shape[1] + j
    state = wp.rand_init(seed, scalar_pixel_id)
    data_out[i, j] = data_in[i, j] + sigma * wp.randn(state)

rep.annotators.register_augmentation(
    "gn_depth_wp", rep.annotators.Augmentation.from_function(gaussian_noise_depth_wp, sigma=0.1, seed=SEED)
)
```

Create the augmentations (warp or NumPy) once using the function directly and once from the registry:

Augmentations using Warp or Numpy

```python
# Augment the RGB and depth annotators
rgb_to_bgr_augm = rep.annotators.Augmentation.from_function(rgb_to_bgr_wp if use_warp else rgb_to_bgr_np)
depth_aug = rep.annotators.get_augmentation("gn_depth_wp" if use_warp else "gn_depth_np")
rgb_to_bgr_annot = rep.annotators.augment(
    source_annotator=rep.annotators.get("rgb"),
    augmentation=rgb_to_bgr_augm,
)
depth_annot_1 = rep.annotators.get("distance_to_camera")
depth_annot_1.augment(depth_aug)
depth_annot_2 = rep.annotators.get("distance_to_camera")
depth_annot_2.augment(depth_aug, sigma=0.5)
```

You can also register a new annotator together with its augmentation:

Register Augmentated Annotator

```python
rgb_to_bgr_annot = rep.annotators.augment(
    source_annotator=rep.annotators.get("rgb"),
    augmentation=rgb_to_bgr_augm,
)
depth_annot_1 = rep.annotators.get("distance_to_camera")
depth_annot_1.augment(depth_aug)
depth_annot_2 = rep.annotators.get("distance_to_camera")
depth_annot_2.augment(depth_aug, sigma=0.5)
```

Finally create the augmented annotators (1x **rgb**, 2x **depth**) and attach them to a render product to generate data:

Annotator Augmentation

```python
# Create the render product and attach the annotators to it
cam = rep.functional.create.camera(position=(0, 0, 5), look_at=(0, 0, 0))
rp = rep.create.render_product(cam, resolution)
rgb_to_bgr_annot.attach(rp)
depth_annot_1.attach(rp)
depth_annot_2.attach(rp)
```

### Writer Augmentation

The **writer** example will output gaussian noise augmented RGB and depth annotator data from a writer.

Standalone Application

The example can be run as a standalone application using the following commands in the terminal (on Windows use `python.bat` instead of `python.sh`):

> ```python
> ./python.sh standalone_examples/replicator/augmentation/writer_augmentation.py --env_url /Isaac/Environments/Grid/default_environment.usd
> ```
>
> Optionally the following arguments can be used to change the default behavior:
>
> * `--env_url` – USD environment path relative to the assets root (default: empty scene with dome light and ground plane)
> * `--use_warp` – flag to use warp (GPU) instead of NumPy (CPU) for the augmentation functions (default: False)
> * `--num_frames` – the number of frames to be captured (default: 25)
>
> ```python
> ./python.sh standalone_examples/replicator/augmentation/writer_augmentation.py --use_warp --num_frames 25 --env_url /Isaac/Environments/Grid/default_environment.usd
> ```
>
> Full Standalone Script
>
> ```python
> """Generate augmented synthetic data from a writer."""
>
> from isaacsim import SimulationApp
>
> simulation_app = SimulationApp(launch_config={"headless": False})
>
> import argparse
> import os
> import time
>
> import carb.settings
> import numpy as np
> import omni.replicator.core as rep
> import omni.usd
> import warp as wp
> from isaacsim.core.utils.stage import open_stage
> from isaacsim.storage.native import get_assets_root_path
>
> parser = argparse.ArgumentParser()
> parser.add_argument("--num_frames", type=int, default=5, help="The number of frames to capture")
> parser.add_argument(
>     "--use_warp",
>     action="store_true",
>     help="Use warp augmentations instead of numpy",
> )
> parser.add_argument("--resolution", nargs=2, type=int, default=[512, 512], help="Camera resolution")
> parser.add_argument("--env_url", type=str, default="", help="USD environment URL (empty for basic scene)")
> args, unknown = parser.parse_known_args()
>
> num_frames = args.num_frames
> use_warp = args.use_warp
> resolution = args.resolution
> env_url = args.env_url or None
> SEED = 42
>
> # Enable warp scripts
> carb.settings.get_settings().set_bool("/app/omni.graph.scriptnode/opt_in", True)
>
>
> def gaussian_noise_rgb_np(data_in, sigma: float, seed: int):
>     """Add Gaussian noise to RGB data using NumPy (CPU)."""
>     np.random.seed(seed)
>     # Convert to float32 space
>     data_in = data_in.astype(np.float32)
>     # Add Gaussian noise to each channel
>     data_in[:, :, 0] = data_in[:, :, 0] + np.random.randn(*data_in.shape[:-1]) * sigma
>     data_in[:, :, 1] = data_in[:, :, 1] + np.random.randn(*data_in.shape[:-1]) * sigma
>     data_in[:, :, 2] = data_in[:, :, 2] + np.random.randn(*data_in.shape[:-1]) * sigma
>     # Clip to [0, 255] and convert to uint8
>     data_in = np.clip(data_in, 0, 255).astype(np.uint8)
>     return data_in
>
>
> @wp.kernel
> def gaussian_noise_rgb_wp(
>     data_in: wp.array3d(dtype=wp.uint8), data_out: wp.array3d(dtype=wp.uint8), sigma: float, seed: int
> ):
>     """Add Gaussian noise to RGB data using Warp (GPU)."""
>     # Get thread coordinates and image dimensions to calculate unique pixel ID for random generation
>     i, j = wp.tid()
>     dim_i = data_in.shape[0]
>     dim_j = data_in.shape[1]
>     pixel_id = i * dim_i + j
>
>     # Use pixel_id as offset to create unique seeds for each pixel and channel (ensure independent noise patterns across R,G,B channels)
>     state_r = wp.rand_init(seed, pixel_id + (dim_i * dim_j * 0))
>     state_g = wp.rand_init(seed, pixel_id + (dim_i * dim_j * 1))
>     state_b = wp.rand_init(seed, pixel_id + (dim_i * dim_j * 2))
>
>     # Apply noise to each channel independently using unique seeds; work in float32 space, then clip and convert to uint8
>     val_r = wp.float32(data_in[i, j, 0]) + sigma * wp.randn(state_r)
>     val_g = wp.float32(data_in[i, j, 1]) + sigma * wp.randn(state_g)
>     val_b = wp.float32(data_in[i, j, 2]) + sigma * wp.randn(state_b)
>
>     # Clip to [0, 255] and convert to uint8
>     data_out[i, j, 0] = wp.uint8(wp.clamp(val_r, 0.0, 255.0))
>     data_out[i, j, 1] = wp.uint8(wp.clamp(val_g, 0.0, 255.0))
>     data_out[i, j, 2] = wp.uint8(wp.clamp(val_b, 0.0, 255.0))
>     data_out[i, j, 3] = data_in[i, j, 3]
>
>
> def gaussian_noise_depth_np(data_in, sigma: float, seed: int):
>     """Add Gaussian noise to depth values using NumPy (CPU)."""
>     np.random.seed(seed)
>     result = data_in.astype(np.float32) + np.random.randn(*data_in.shape) * sigma
>     return np.clip(result, 0, None).astype(data_in.dtype)
>
>
> rep.AnnotatorRegistry.register_augmentation(
>     "gn_depth_np", rep.annotators.Augmentation.from_function(gaussian_noise_depth_np, sigma=0.1, seed=None)
> )
>
>
> @wp.kernel
> def gaussian_noise_depth_wp(
>     data_in: wp.array2d(dtype=wp.float32), data_out: wp.array2d(dtype=wp.float32), sigma: float, seed: int
> ):
>     """Add Gaussian noise to depth values using Warp (GPU)."""
>     i, j = wp.tid()
>     # Unique ID for random seed per pixel
>     scalar_pixel_id = i * data_in.shape[1] + j
>     state = wp.rand_init(seed, scalar_pixel_id)
>     data_out[i, j] = data_in[i, j] + sigma * wp.randn(state)
>
>
> rep.AnnotatorRegistry.register_augmentation(
>     "gn_depth_wp", rep.annotators.Augmentation.from_function(gaussian_noise_depth_wp, sigma=0.1, seed=None)
> )
>
>
> def run_example(num_frames: int, resolution: tuple[int, int], use_warp: bool, env_url: str | None = None) -> float:
>     """Run the capture pipeline using step() to trigger a randomization and data capture."""
>     print(f"Running example with num_frames: {num_frames}, resolution: {resolution}, use_warp: {use_warp}")
>
>     if env_url is not None and env_url != "":
>         assets_root_path = get_assets_root_path()
>         stage_path = assets_root_path + env_url
>         print(f"Opening stage: {stage_path}")
>         open_stage(stage_path)
>     else:
>         omni.usd.get_context().new_stage()
>         rep.functional.create.dome_light(intensity=1000, rotation=(270, 0, 0))
>         ground_plane = rep.functional.create.plane(scale=(10, 10, 1), position=(0, 0, 0))
>         rep.functional.physics.apply_collider(ground_plane)
>
>     # Use a fixed global seed for reproducibility
>     rep.set_global_seed(SEED)
>
>     # Disable capture on play, data is captured manually using the step function
>     rep.orchestrator.set_capture_on_play(False)
>
>     # Set DLSS to Quality mode (2) for best SDG results (Options: 0 (Performance), 1 (Balanced), 2 (Quality), 3 (Auto)
>     carb.settings.get_settings().set("rtx/post/dlss/execMode", 2)
>
>     # Augment the annotators
>     rgb_to_hsv_augm = rep.annotators.Augmentation.from_function(rep.augmentations_default.aug_rgb_to_hsv)
>     hsv_to_rgb_augm = rep.annotators.Augmentation.from_function(rep.augmentations_default.aug_hsv_to_rgb)
>
>     # Augment the RGB and depth annotators
>     gn_rgb_augm = rep.annotators.Augmentation.from_function(
>         gaussian_noise_rgb_wp if use_warp else gaussian_noise_rgb_np, sigma=15.0, seed=SEED
>     )
>     gn_depth_augm = rep.annotators.get_augmentation("gn_depth_wp" if use_warp else "gn_depth_np")
>
>     # Create a writer and apply the augmentations to its corresponding annotators
>     out_dir = os.path.join(os.getcwd(), f"_out_augm_writer_{'warp' if use_warp else 'numpy'}")
>     backend = rep.backends.get("DiskBackend")
>     backend.initialize(output_dir=out_dir)
>     print(f"Writing data to: {out_dir}")
>     writer = rep.writers.get("BasicWriter")
>     writer.initialize(backend=backend, rgb=True, distance_to_camera=True, colorize_depth=True)
>
>     # Apply the augmentations to the RGB and depth annotators
>     augmented_rgb_annot = rep.annotators.get("rgb").augment_compose(
>         [rgb_to_hsv_augm, gn_rgb_augm, hsv_to_rgb_augm], name="rgb"
>     )
>     writer.add_annotator(augmented_rgb_annot)
>     writer.augment_annotator("distance_to_camera", gn_depth_augm)
>
>     # Create a camera and a render product and attach them to the writer
>     cam = rep.functional.create.camera(position=(0, 0, 5), look_at=(0, 0, 0))
>     rp = rep.create.render_product(cam, resolution)
>     writer.attach(rp)
>
>     # Create a red cube and randomize its rotation on a custom event sent before each capture step
>     red_cube = rep.functional.create.cube(position=(0, 0, 0.71))
>     rep.functional.create.material(mdl="OmniPBR.mdl", bind_prims=[red_cube], diffuse_color_constant=(1, 0, 0))
>     with rep.trigger.on_custom_event(event_name="randomize_red_cube"):
>         red_cube_node = rep.get.prim_at_path(red_cube.GetPath())
>         with red_cube_node:
>             rep.randomizer.rotation()
>
>     capture_start = time.time()
>     for frame_idx in range(num_frames):
>         print(f"  Capturing frame {frame_idx + 1}/{num_frames}")
>         rep.utils.send_og_event(event_name="randomize_red_cube")
>         rep.orchestrator.step(rt_subframes=32)
>
>     # Wait for the data to be written to disk and release resources
>     rep.orchestrator.wait_until_complete()
>     writer.detach()
>     rp.destroy()
>
>     return time.time() - capture_start
>
>
> duration = run_example(num_frames, resolution, use_warp, env_url)
> average = duration / num_frames if num_frames else 0.0
> mode_label = "warp" if use_warp else "numpy"
> print(
>     f"The duration for capturing {num_frames} frames using '{mode_label}' was: {duration:.4f} seconds, "
>     f"with an average of {average:.4f} seconds per frame."
> )
>
> simulation_app.close()
> ```

Script Editor

Full Script Editor Script

```python
import asyncio
import os
import time

import carb.settings
import numpy as np
import omni.replicator.core as rep
import warp as wp
from isaacsim.core.experimental.utils.stage import open_stage
from isaacsim.storage.native import get_assets_root_path_async

NUM_FRAMES = 5
RESOLUTION = (512, 512)
USE_WARP = False
ENV_URL = "/Isaac/Environments/Grid/default_environment.usd"
SEED = 42

# Enable warp scripts
carb.settings.get_settings().set_bool("/app/omni.graph.scriptnode/opt_in", True)

def gaussian_noise_rgb_np(data_in, sigma: float, seed: int):
    """Add Gaussian noise to RGB data using NumPy (CPU)."""
    np.random.seed(seed)
    # Convert to float32 space
    data_in = data_in.astype(np.float32)
    # Add Gaussian noise to each channel
    data_in[:, :, 0] = data_in[:, :, 0] + np.random.randn(*data_in.shape[:-1]) * sigma
    data_in[:, :, 1] = data_in[:, :, 1] + np.random.randn(*data_in.shape[:-1]) * sigma
    data_in[:, :, 2] = data_in[:, :, 2] + np.random.randn(*data_in.shape[:-1]) * sigma
    # Clip to [0, 255] and convert to uint8
    data_in = np.clip(data_in, 0, 255).astype(np.uint8)
    return data_in

@wp.kernel
def gaussian_noise_rgb_wp(
    data_in: wp.array3d(dtype=wp.uint8), data_out: wp.array3d(dtype=wp.uint8), sigma: float, seed: int
):
    """Add Gaussian noise to RGB data using Warp (GPU)."""
    # Get thread coordinates and image dimensions to calculate unique pixel ID for random generation
    i, j = wp.tid()
    dim_i = data_in.shape[0]
    dim_j = data_in.shape[1]
    pixel_id = i * dim_i + j

    # Use pixel_id as offset to create unique seeds for each pixel and channel (ensure independent noise patterns across R,G,B channels)
    state_r = wp.rand_init(seed, pixel_id + (dim_i * dim_j * 0))
    state_g = wp.rand_init(seed, pixel_id + (dim_i * dim_j * 1))
    state_b = wp.rand_init(seed, pixel_id + (dim_i * dim_j * 2))

    # Apply noise to each channel independently using unique seeds; work in float32 space, then clip and convert to uint8
    val_r = wp.float32(data_in[i, j, 0]) + sigma * wp.randn(state_r)
    val_g = wp.float32(data_in[i, j, 1]) + sigma * wp.randn(state_g)
    val_b = wp.float32(data_in[i, j, 2]) + sigma * wp.randn(state_b)

    # Clip to [0, 255] and convert to uint8
    data_out[i, j, 0] = wp.uint8(wp.clamp(val_r, 0.0, 255.0))
    data_out[i, j, 1] = wp.uint8(wp.clamp(val_g, 0.0, 255.0))
    data_out[i, j, 2] = wp.uint8(wp.clamp(val_b, 0.0, 255.0))
    data_out[i, j, 3] = data_in[i, j, 3]

def gaussian_noise_depth_np(data_in, sigma: float, seed: int):
    """Add Gaussian noise to depth values using NumPy (CPU)."""
    np.random.seed(seed)
    result = data_in.astype(np.float32) + np.random.randn(*data_in.shape) * sigma
    return np.clip(result, 0, None).astype(data_in.dtype)

rep.annotators.register_augmentation(
    "gn_depth_np", rep.annotators.Augmentation.from_function(gaussian_noise_depth_np, sigma=0.1, seed=SEED)
)

@wp.kernel
def gaussian_noise_depth_wp(
    data_in: wp.array2d(dtype=wp.float32), data_out: wp.array2d(dtype=wp.float32), sigma: float, seed: int
):
    """Add Gaussian noise to depth values using Warp (GPU)."""
    i, j = wp.tid()
    # Unique ID for random seed per pixel
    scalar_pixel_id = i * data_in.shape[1] + j
    state = wp.rand_init(seed, scalar_pixel_id)
    data_out[i, j] = data_in[i, j] + sigma * wp.randn(state)

rep.annotators.register_augmentation(
    "gn_depth_wp", rep.annotators.Augmentation.from_function(gaussian_noise_depth_wp, sigma=0.1, seed=SEED)
)

# Run the capture pipeline using step() to trigger a randomization and data capture
async def run_example_async(num_frames: int, resolution: tuple[int, int], use_warp: bool) -> float:
    print(f"Running example with num_frames: {num_frames}, resolution: {resolution}, use_warp: {use_warp}")

    # Open a new stage
    assets_root_path = await get_assets_root_path_async()
    stage_path = assets_root_path + ENV_URL
    print(f"Opening stage: {stage_path}")
    open_stage(stage_path)

    # Use a fixed global seed for reproducibility
    rep.set_global_seed(SEED)

    # Disable capture on play, data is captured manually using the step function
    rep.orchestrator.set_capture_on_play(False)

    # Set DLSS to Quality mode (2) for best SDG results (Options: 0 (Performance), 1 (Balanced), 2 (Quality), 3 (Auto)
    carb.settings.get_settings().set("rtx/post/dlss/execMode", 2)

    # Augment the annotators
    rgb_to_hsv_augm = rep.annotators.Augmentation.from_function(rep.augmentations_default.aug_rgb_to_hsv)
    hsv_to_rgb_augm = rep.annotators.Augmentation.from_function(rep.augmentations_default.aug_hsv_to_rgb)

    # Augment the RGB and depth annotators
    gn_rgb_augm = rep.annotators.Augmentation.from_function(
        gaussian_noise_rgb_wp if use_warp else gaussian_noise_rgb_np, sigma=15.0, seed=SEED
    )
    gn_depth_augm = rep.annotators.get_augmentation("gn_depth_wp" if use_warp else "gn_depth_np")

    # Create a writer and apply the augmentations to its corresponding annotators
    out_dir = os.path.join(os.getcwd(), "_out_augm_writer")
    backend = rep.backends.get("DiskBackend")
    backend.initialize(output_dir=out_dir)
    print(f"Writing data to: {out_dir}")
    writer = rep.writers.get("BasicWriter")
    writer.initialize(backend=backend, rgb=True, distance_to_camera=True, colorize_depth=True)

    # Apply the augmentations to the RGB and depth annotators
    augmented_rgb_annot = rep.annotators.get("rgb").augment_compose(
        [rgb_to_hsv_augm, gn_rgb_augm, hsv_to_rgb_augm], name="rgb"
    )
    writer.add_annotator(augmented_rgb_annot)
    writer.augment_annotator("distance_to_camera", gn_depth_augm)

    # Create a camera and a render product and attach them to the writer
    cam = rep.functional.create.camera(position=(0, 0, 5), look_at=(0, 0, 0))
    rp = rep.create.render_product(cam, resolution)
    writer.attach(rp)

    # Create a red cube and randomize its rotation on a custom event sent before each capture step
    red_cube = rep.functional.create.cube(position=(0, 0, 0.71))
    rep.functional.create.material(mdl="OmniPBR.mdl", bind_prims=[red_cube], diffuse_color_constant=(1, 0, 0))
    with rep.trigger.on_custom_event(event_name="randomize_red_cube"):
        red_cube_node = rep.get.prim_at_path(red_cube.GetPath())
        with red_cube_node:
            rep.randomizer.rotation()

    capture_start = time.time()
    for frame_idx in range(num_frames):
        print(f"  Capturing frame {frame_idx + 1}/{num_frames}")
        rep.utils.send_og_event(event_name="randomize_red_cube")
        await rep.orchestrator.step_async(rt_subframes=32)

    # Wait for the data to be written to disk and release resources
    await rep.orchestrator.wait_until_complete_async()
    writer.detach()
    rp.destroy()

    return time.time() - capture_start

def on_task_done(task: asyncio.Task):
    """Report timing information when capture completes."""
    duration = task.result()
    average = duration / NUM_FRAMES if NUM_FRAMES else 0.0
    mode_label = "warp" if USE_WARP else "numpy"
    print(
        f"The duration for capturing {NUM_FRAMES} frames using '{mode_label}' was: {duration:.4f} seconds, "
        f"with an average of {average:.4f} seconds per frame."
    )

task = asyncio.ensure_future(run_example_async(NUM_FRAMES, RESOLUTION, USE_WARP))
task.add_done_callback(on_task_done)
```

Code Explanation

To be able to run the augmentation functions one needs to enable scripting in the settings:

Enable Scripting

```python
# Enable warp scripts
carb.settings.get_settings().set_bool("/app/omni.graph.scriptnode/opt_in", True)
```

For the **rgb** (**LdrColor**) annotator of the writer, we provide gaussian noise functions using NumPy (CPU) and warp (GPU) kernels, applied on the RGB channels of the RGBA provided data format.

RGB Gaussian Noise using Warp and Numpy

```python
def gaussian_noise_rgb_np(data_in, sigma: float, seed: int):
    """Add Gaussian noise to RGB data using NumPy (CPU)."""
    np.random.seed(seed)
    # Convert to float32 space
    data_in = data_in.astype(np.float32)
    # Add Gaussian noise to each channel
    data_in[:, :, 0] = data_in[:, :, 0] + np.random.randn(*data_in.shape[:-1]) * sigma
    data_in[:, :, 1] = data_in[:, :, 1] + np.random.randn(*data_in.shape[:-1]) * sigma
    data_in[:, :, 2] = data_in[:, :, 2] + np.random.randn(*data_in.shape[:-1]) * sigma
    # Clip to [0, 255] and convert to uint8
    data_in = np.clip(data_in, 0, 255).astype(np.uint8)
    return data_in

@wp.kernel
def gaussian_noise_rgb_wp(
    data_in: wp.array3d(dtype=wp.uint8), data_out: wp.array3d(dtype=wp.uint8), sigma: float, seed: int
):
    """Add Gaussian noise to RGB data using Warp (GPU)."""
    # Get thread coordinates and image dimensions to calculate unique pixel ID for random generation
    i, j = wp.tid()
    dim_i = data_in.shape[0]
    dim_j = data_in.shape[1]
    pixel_id = i * dim_i + j

    # Use pixel_id as offset to create unique seeds for each pixel and channel
    state_r = wp.rand_init(seed, pixel_id + (dim_i * dim_j * 0))
    state_g = wp.rand_init(seed, pixel_id + (dim_i * dim_j * 1))
    state_b = wp.rand_init(seed, pixel_id + (dim_i * dim_j * 2))

    # Apply noise to each channel independently using unique seeds
    val_r = wp.float32(data_in[i, j, 0]) + sigma * wp.randn(state_r)
    val_g = wp.float32(data_in[i, j, 1]) + sigma * wp.randn(state_g)
    val_b = wp.float32(data_in[i, j, 2]) + sigma * wp.randn(state_b)

    # Clip to [0, 255] and convert to uint8
    data_out[i, j, 0] = wp.uint8(wp.clamp(val_r, 0.0, 255.0))
    data_out[i, j, 1] = wp.uint8(wp.clamp(val_g, 0.0, 255.0))
    data_out[i, j, 2] = wp.uint8(wp.clamp(val_b, 0.0, 255.0))
    data_out[i, j, 3] = data_in[i, j, 3]
```

For the **depth** annotator of the writer, there are gaussian noise functions using NumPy (CPU) and warp (GPU) kernels, applied on the 2D array of float32 values. The functions are registered in the annotator registry for later access:

Depth Gaussian Noise using Warp and Numpy

```python
def gaussian_noise_depth_np(data_in, sigma: float, seed: int):
    """Add Gaussian noise to depth values using NumPy (CPU)."""
    np.random.seed(seed)
    result = data_in.astype(np.float32) + np.random.randn(*data_in.shape) * sigma
    return np.clip(result, 0, None).astype(data_in.dtype)

rep.AnnotatorRegistry.register_augmentation(
    "gn_depth_np", rep.annotators.Augmentation.from_function(gaussian_noise_depth_np, sigma=0.1, seed=None)
)

@wp.kernel
def gaussian_noise_depth_wp(
    data_in: wp.array2d(dtype=wp.float32), data_out: wp.array2d(dtype=wp.float32), sigma: float, seed: int
):
    """Add Gaussian noise to depth values using Warp (GPU)."""
    i, j = wp.tid()
    # Unique ID for random seed per pixel
    scalar_pixel_id = i * data_in.shape[1] + j
    state = wp.rand_init(seed, scalar_pixel_id)
    data_out[i, j] = data_in[i, j] + sigma * wp.randn(state)

rep.AnnotatorRegistry.register_augmentation(
    "gn_depth_wp", rep.annotators.Augmentation.from_function(gaussian_noise_depth_wp, sigma=0.1, seed=None)
)
```

Access the default (**rgb**) augmentations from replicator:

Built-in Replicator Augmentations

```python
# Augment the annotators
rgb_to_hsv_augm = rep.annotators.Augmentation.from_function(rep.augmentations_default.aug_rgb_to_hsv)
hsv_to_rgb_augm = rep.annotators.Augmentation.from_function(rep.augmentations_default.aug_hsv_to_rgb)
```

Furthermore the custom augmentations are created (warp or NumPy), after using the function directly and once from the registry:

Augmentations using Warp or Numpy

```python
# Augment the RGB and depth annotators
gn_rgb_augm = rep.annotators.Augmentation.from_function(
    gaussian_noise_rgb_wp if use_warp else gaussian_noise_rgb_np, sigma=15.0, seed=SEED
)
gn_depth_augm = rep.annotators.get_augmentation("gn_depth_wp" if use_warp else "gn_depth_np")
```

Finally the writer is created and initialized to use the **rgb** and **depth** (**distance\_to\_camera**) annotators. The built-in `rgb` annotator is replaced by a new augmented one by using the same `name="rgb"` name and adding it to the writer (`add_annotator`). The augmented RGB annotator uses a composition by switching the data to hsv, adding gaussian noise, and switching back to RGB. The `distance_to_camera` annotator is augmented by using the built-in `augment_annotator` function:

Writer Augmentation

```python
# Create a writer and apply the augmentations to its corresponding annotators
out_dir = os.path.join(os.getcwd(), f"_out_augm_writer_{'warp' if use_warp else 'numpy'}")
backend = rep.backends.get("DiskBackend")
backend.initialize(output_dir=out_dir)
print(f"Writing data to: {out_dir}")
writer = rep.writers.get("BasicWriter")
writer.initialize(backend=backend, rgb=True, distance_to_camera=True, colorize_depth=True)

# Apply the augmentations to the RGB and depth annotators
augmented_rgb_annot = rep.annotators.get("rgb").augment_compose(
    [rgb_to_hsv_augm, gn_rgb_augm, hsv_to_rgb_augm], name="rgb"
)
writer.add_annotator(augmented_rgb_annot)
writer.augment_annotator("distance_to_camera", gn_depth_augm)

# Create a camera and a render product and attach them to the writer
cam = rep.functional.create.camera(position=(0, 0, 5), look_at=(0, 0, 0))
rp = rep.create.render_product(cam, resolution)
writer.attach(rp)
```

On this page

* [Learning Objectives](#learning-objectives)
* [Scenario](#scenario)
* [Implementation](#implementation)
  + [Annotator Augmentation](#annotator-augmentation)
  + [Writer Augmentation](#writer-augmentation)

---

### Troubleshooting

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/replicator_tutorials/troubleshooting.html

* [Help & FAQ](../overview/help.html)
* [Troubleshooting](../overview/troubleshooting.html)
* Replicator Troubleshooting

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Replicator Troubleshooting

This page consolidates troubleshooting information for Replicator components in Isaac Sim.

## Replicator Rendering Issues

If there is unwanted noise in simulated depth images, disable anti-aliasing under the **Render Settings > Ray Tracing > Anti-Aliasing** tab by setting the `Algorithm` to `None`.

If randomized materials are not loaded on time for synthetic data generation, the [rt\_subframes](https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator/subframes_examples.html#subframes-examples "(in Omniverse Extensions)") must be set to be at least `2`.

The replicator Scatter3D OmniGraph node breaks physics when called on a stage using world. Avoid using these together or use alternative methods for object placement.

If ghosting artifacts are observed in the captured data, especially for scenes with moving objects or significant changes in lighting conditions, increase the `rt_subframes` value when capturing the data to a value until the renderer is able to remove the artifacts. For more information see [RT Subframes Parameter](tutorial_replicator_getting_started.html#isaac-sim-replicator-getting-started-subframes) and [subframes examples](https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator/subframes_examples.html#subframes-examples "(in Omniverse Extensions)").

If the captured images are written as black, try starting Isaac Sim once with the `--reset-user` to clear any previous user settings.

## Async Rendering and Frame Skipping

When using Replicator, frames may be skipped due to the `isaacsim.core.throttling` extension toggling `/app/asyncRendering=True` by default when the timeline is stopped. Since Replicator remains in STARTED mode, it does not re-initialize and toggle the setting back to False, leading to frames being skipped during capture.

**Solution:** Launch Isaac Sim with the following flag to disable async rendering toggling from the throttling extension:

```python
--/exts/isaacsim.core.throttling/enable_async=false
```

This occurs because when the timeline is stopped, the throttling extension enables async rendering for performance. However, when Replicator schedules frames for capture before the timeline starts playing again, those frames may be skipped due to async rendering being enabled. The flag above prevents the throttling extension from toggling async rendering, ensuring all scheduled frames are captured properly.

## Replicator Data Storage Issues

Using Replicator to write to S3 buckets with the built-in backend in Windows may require setting the credentials in the environment variables instead of the AWS config files. This is because of a possible path parsing error in Boto3 on Windows.

When working with large datasets or high-resolution images, you may experience storage bottlenecks. Consider:
1. Using a faster storage device
2. Reducing the image resolution or compression level
3. Using batch processing with smaller batches

## Replicator Layers and Randomization

Using [replicator](https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator/basic_functionalities.html "(in Omniverse Extensions)")’s `rep.new_layer()` functionality, which creates a new layer in which to place and randomize assets, may lead to issues in simulation scenarios where these assets are used. In such cases the use of `rep.new_layer()` can be omitted.

When using multiple randomizers, be aware that they may conflict with each other. Test your randomization settings carefully to ensure they produce the expected results.

## Replicator Performance Issues

For complex scenes with many objects and randomizers, you may experience performance issues. Consider:
1. Reducing the number of objects in the scene
2. Simplifying the randomization parameters
3. Using fewer sensors or lower resolution sensors
4. Running with headless mode for improved performance during data generation

## Replicator API Changes

If you are encountering any issues regarding the dependencies on `omni.replicator.character` or `omni.replicator.agent`, the extension is now renamed to `isaacsim.replicator.agent`. Revise your code accordingly.

## Getting Started Scripts Issues

Common issues and solutions for the Getting Started Scripts:

1. **Data not being captured**
   - Ensure the capture-on-play flag is properly set
   - Check if the render products are correctly attached to writers
   - Verify the output directory has write permissions
2. **Rendering artifacts**
   - Try increasing RTSubframes value
   - Check if materials are fully loaded before capture
   - Ensure proper lighting setup
3. **Performance issues**
   - Reduce resolution or number of cameras
   - Use headless mode for faster processing
   - Optimize scene complexity
4. **Memory issues**
   - Reduce batch size
   - Clear unused resources with `destroy()`
   - Monitor GPU memory usage

## First Frame Missing in Windows Standalone Mode

On Windows, when running SDG pipelines with Replicator in standalone mode, the first frame may be skipped by writers or data may be missing from annotators.

### Workaround

Call a few “warmup” steps to advance the simulation before the first capture to avoid missing the initial frame. For example:

```python
# Warmup the simulation
timeline = omni.timeline.get_timeline_interface()
timeline.play()
for _ in range(2):
    standalone_app.update()
```

Alternative (depending on your Replicator control flow):

```python
import omni.replicator.core as rep
# [..] initialize writer [..]
rep.orchestrator.step()
# [..] start SDG pipeline [..]
```

On this page

* [Replicator Rendering Issues](#replicator-rendering-issues)
* [Async Rendering and Frame Skipping](#async-rendering-and-frame-skipping)
* [Replicator Data Storage Issues](#replicator-data-storage-issues)
* [Replicator Layers and Randomization](#replicator-layers-and-randomization)
* [Replicator Performance Issues](#replicator-performance-issues)
* [Replicator API Changes](#replicator-api-changes)
* [Getting Started Scripts Issues](#getting-started-scripts-issues)
* [First Frame Missing in Windows Standalone Mode](#first-frame-missing-in-windows-standalone-mode)
  + [Workaround](#workaround)

---

