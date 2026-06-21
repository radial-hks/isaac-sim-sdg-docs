# SDG 实战Pipeline

> Cosmos 增强 + InfiniGen SDG + Metropolis Pipeline + Telemetry + Headless
> Isaac Sim 版本: 6.0
> 最后组装: 2026-06-21 12:48 UTC
> 来源页数: 8

---

## 来源链接

- [Cosmos](https://docs.isaacsim.omniverse.nvidia.com/latest/replicator_tutorials/tutorial_replicator_cosmos.html)
- [InfiniGen SDG](https://docs.isaacsim.omniverse.nvidia.com/latest/replicator_tutorials/tutorial_replicator_infinigen_sdg.html)
- [Metropolis Pipeline](https://docs.isaacsim.omniverse.nvidia.com/latest/action_and_event_data_generation/tutorial_omni_metropolis_pipeline.html)
- [Telemetry](https://docs.isaacsim.omniverse.nvidia.com/latest/action_and_event_data_generation/tutorial_telemetry.html)
- [Event Reactive Actors](https://docs.isaacsim.omniverse.nvidia.com/latest/action_and_event_data_generation/example_event_reactive_actors.html)
- [Performance Optimization](https://docs.isaacsim.omniverse.nvidia.com/latest/reference_material/sim_performance_optimization_handbook.html)
- [Rendering Modes](https://docs.isaacsim.omniverse.nvidia.com/latest/reference_material/rendering_modes.html)
- [Glossary](https://docs.isaacsim.omniverse.nvidia.com/latest/reference_material/reference_glossary.html)

---


## 增强

### Cosmos

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/replicator_tutorials/tutorial_replicator_cosmos.html

* [Synthetic Data Generation](../synthetic_data_generation/index.html)
* [Perception Data Generation (Replicator)](index.html)
* Cosmos Synthetic Data Generation

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Cosmos Synthetic Data Generation

This tutorial demonstrates generating multi-modal synthetic data for [NVIDIA Cosmos](https://www.nvidia.com/en-us/ai/cosmos/) using the `CosmosWriter` in Isaac Sim. The writer captures synchronized RGB, depth, segmentation, and edge data from a robot navigating a warehouse environment.

The generated data serves as ground truth input for [Cosmos Transfer](https://docs.nvidia.com/cosmos/latest/), which transforms low-resolution control signals into high-quality visual simulations through its Multi-ControlNet architecture.

## Why Use the CosmosWriter?

The CosmosWriter bridges the gap between simulation and real-world robotics applications by generating rich, multi-modal datasets from synthetic environments. Key use cases include:

* **Sim-to-Real Transfer**: Transform synthetic simulation videos into photorealistic scenes with varied materials, lighting, and environmental conditions using Cosmos Transfer
* **Domain Adaptation**: Generate diverse training data from a single simulation, creating variations in scene styles, materials, and lighting without re-running expensive simulations or capturing real-world data
* **Data Augmentation**: Expand limited datasets by generating multiple visual variations while preserving robot motions, object positions, and scene structure

For examples of sim-to-real transformations in robotics, see the [Cosmos Cookbook Robotics Gallery](https://nvidia-cosmos.github.io/cosmos-cookbook/gallery/robotics_inference.html), which showcases how synthetic kitchen scenes can be transformed into photorealistic environments with different cabinet styles, robot materials, and lighting conditions.

## Prerequisites

* Familiarity with the [omni.replicator](https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator.html "(in Omniverse Extensions)") extension and its [writers](https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator/writer_examples.html "(in Omniverse Extensions)")
* Basic understanding of Isaac Simâs SDG [Getting Started Scripts](tutorial_replicator_getting_started.html#isaac-sim-app-tutorial-replicator-getting-started)
* Running simulations as [Standalone Applications](../introduction/workflows.html#standalone-application) or via the [Script Editor](../development_tools/omniverse_script_editor.html#script-editor).

## What the CosmosWriter Generates

The writer outputs five synchronized modalities from the robotâs camera:

* **RGB** - Color imagery (vis control)
* **Depth** - Distance-to-camera for spatial understanding
* **Segmentation** - Instance masks for object tracking
* **Shaded Segmentation** - Instance masks with realistic shading
* **Edges** - Canny edge detection for boundaries

These modalities correspond to [Cosmos Transferâs](https://docs.nvidia.com/cosmos/latest/#controlnet-specification) control branches:

* **vis**: Uses RGB imagery with bilateral blurring
* **edge**: Applies Canny edge detection (tunable thresholds)
* **depth**: Depth maps for 3D structure understanding
* **seg**: Segmentation masks for object identification

Each control branch can be weighted (0.0-1.0) to balance adherence vs. creative freedom in the generated output.

## Implementation

This example demonstrates a Carter Nova robot autonomously navigating through a warehouse environment. As the robot moves from its starting position to a target location, the `CosmosWriter` captures synchronized multi-modal data (RGB, depth, segmentation, shaded segmentation, and edges) from the robotâs front camera. The captured data is organized into clips, with each clip containing a sequence of frames that can be used as input for Cosmos Transfer.

Standalone Application

The example can be run as a standalone application using the following commands in the terminal (on Windows use `python.bat` instead of `python.sh`):

```python
./python.sh standalone_examples/replicator/cosmos_writer_warehouse.py
```

Full Standalone Script

```python
"""Generate synthetic video clips in a warehouse using the CosmosWriter."""

from isaacsim import SimulationApp

simulation_app = SimulationApp(launch_config={"headless": False})

import os

import carb
import omni.replicator.core as rep
import omni.timeline
import omni.usd
from isaacsim.core.utils.stage import add_reference_to_stage
from isaacsim.storage.native import get_assets_root_path
from pxr import UsdGeom

# Capture parameters
START_DELAY = 0.1  # Timeline duration delay before capturing the first clip
NUM_CLIPS = 2  # Number of video clips to capture with the CosmosWriter
NUM_FRAMES_PER_CLIP = 10  # Number of frames for each clip
CAPTURE_INTERVAL = 2  # Capture interval between frames (capture every N simulation steps)

# Stage and asset paths
STAGE_URL = "/Isaac/Samples/Replicator/Stage/full_warehouse_worker_and_anim_cameras.usd"
CARTER_NAV_ASSET_URL = "/Isaac/Samples/Replicator/OmniGraph/nova_carter_nav_only.usd"
CARTER_NAV_PATH = "/NavWorld/CarterNav"
CARTER_NAV_TARGET_PATH = f"{CARTER_NAV_PATH}/targetXform"
CARTER_CAMERA_PATH = f"{CARTER_NAV_PATH}/chassis_link/sensors/front_hawk/left/camera_left"
CARTER_NAV_POSITION = (-6, 4, 0)
CARTER_NAV_TARGET_POSITION = (3, 3, 0)

def advance_timeline_by_duration(duration: float, max_updates: int = 1000):
    """Advance the simulation timeline by the specified duration in seconds."""
    timeline = omni.timeline.get_timeline_interface()
    current_time = timeline.get_current_time()
    target_time = current_time + duration

    if timeline.get_end_time() < target_time:
        timeline.set_end_time(1000000)

    if not timeline.is_playing():
        timeline.play()

    print(f"Advancing timeline from {current_time:.4f}s to {target_time:.4f}s")
    step_count = 0
    while current_time < target_time:
        if step_count >= max_updates:
            print(f"Max updates reached: {step_count}, finishing timeline advance.")
            break

        prev_time = current_time
        simulation_app.update()
        current_time = timeline.get_current_time()
        step_count += 1

        if step_count % 10 == 0:
            print(f"\tStep {step_count}, {current_time:.4f}s/{target_time:.4f}s")

        if current_time <= prev_time:
            print(f"Warning: Timeline did not advance at update {step_count} (time: {current_time:.4f}s).")
    print(f"Finished advancing timeline to {current_time:.4f}s (target {target_time:.4f}s) in {step_count} steps")

def run_sdg_pipeline(
    camera_path, num_clips, num_frames_per_clip, capture_interval, use_instance_id=True, segmentation_mapping=None
):
    """Run the synthetic data generation pipeline and capture video clips."""
    rp = rep.create.render_product(camera_path, (1280, 720))
    cosmos_writer = rep.WriterRegistry.get("CosmosWriter")
    backend = rep.backends.get("DiskBackend")
    out_dir = os.path.join(os.getcwd(), f"_out_cosmos_warehouse")
    print(f"output_directory: {out_dir}")
    backend.initialize(output_dir=out_dir)
    cosmos_writer.initialize(
        backend=backend, use_instance_id=use_instance_id, segmentation_mapping=segmentation_mapping
    )
    cosmos_writer.attach(rp)

    # Make sure the timeline is playing
    timeline = omni.timeline.get_timeline_interface()
    if not timeline.is_playing():
        timeline.play()

    print(
        f"Starting SDG pipeline. Capturing {num_clips} clips with {num_frames_per_clip} frames each, every {capture_interval} simulation step(s)."
    )

    for clip_index in range(num_clips):
        print(f"Starting clip {clip_index + 1}/{num_clips}")

        frames_captured_count = 0
        simulation_step_index = 0
        while frames_captured_count < num_frames_per_clip:
            print(f"Simulation step {simulation_step_index}")
            if simulation_step_index % capture_interval == 0:
                print(f"\t Capturing frame {frames_captured_count + 1}/{num_frames_per_clip} for clip {clip_index + 1}")
                rep.orchestrator.step(pause_timeline=False)
                frames_captured_count += 1
            else:
                simulation_app.update()
            simulation_step_index += 1

        print(f"Finished clip {clip_index + 1}/{num_clips}. Captured {frames_captured_count} frames")

        # Move to next clip if not the last clip
        if clip_index < num_clips - 1:
            print(f"Moving to next clip...")
            cosmos_writer.next_clip()

    print("Waiting to finish processing and writing the data")
    rep.orchestrator.wait_until_complete()
    print(f"Finished SDG pipeline. Captured {num_clips} clips with {num_frames_per_clip} frames each")
    cosmos_writer.detach()
    rp.destroy()
    timeline.pause()

def run_example(
    num_clips,
    num_frames_per_clip,
    capture_interval,
    start_delay=0.0,
    use_instance_id=True,
    segmentation_mapping=None,
):
    """Set up the warehouse scene and run the SDG pipeline."""
    assets_root_path = get_assets_root_path()
    stage_path = assets_root_path + STAGE_URL
    print(f"Opening stage: '{stage_path}'")
    omni.usd.get_context().open_stage(stage_path)
    stage = omni.usd.get_context().get_stage()

    # Enable script nodes
    carb.settings.get_settings().set_bool("/app/omni.graph.scriptnode/opt_in", True)

    # Disable capture on play on the new stage, data is captured manually using the step function
    rep.orchestrator.set_capture_on_play(False)

    # Set DLSS to Quality mode (2) for best SDG results , options: 0 (Performance), 1 (Balanced), 2 (Quality), 3 (Auto)
    carb.settings.get_settings().set("rtx/post/dlss/execMode", 2)

    # Load carter nova asset with its navigation graph
    carter_url_path = assets_root_path + CARTER_NAV_ASSET_URL
    print(f"Loading carter nova asset: '{carter_url_path}' at prim path: '{CARTER_NAV_PATH}'")
    carter_nav_prim = add_reference_to_stage(usd_path=carter_url_path, prim_path=CARTER_NAV_PATH)

    if not carter_nav_prim.GetAttribute("xformOp:translate"):
        UsdGeom.Xformable(carter_nav_prim).AddTranslateOp()
    carter_nav_prim.GetAttribute("xformOp:translate").Set(CARTER_NAV_POSITION)

    # Set the navigation target position
    carter_navigation_target_prim = stage.GetPrimAtPath(CARTER_NAV_TARGET_PATH)
    if not carter_navigation_target_prim.IsValid():
        print(f"Carter navigation target prim not found at path: {CARTER_NAV_TARGET_PATH}, exiting")
        return
    if not carter_navigation_target_prim.GetAttribute("xformOp:translate"):
        UsdGeom.Xformable(carter_navigation_target_prim).AddTranslateOp()
    carter_navigation_target_prim.GetAttribute("xformOp:translate").Set(CARTER_NAV_TARGET_POSITION)

    # Use the carter nova front hawk camera for capturing data
    camera_prim = stage.GetPrimAtPath(CARTER_CAMERA_PATH)
    if not camera_prim.IsValid():
        print(f"Camera prim not found at path: {CARTER_CAMERA_PATH}, exiting")
        return

    # tickRate=0 forces autotrigger so the sensor cameras stay in sync with rep.orchestrator.step
    # under multi-tick rendering.
    if camera_prim.HasAttribute("omni:sensor:tickRate"):
        camera_prim.GetAttribute("omni:sensor:tickRate").Set(0.0)

    # Advance the timeline with the start delay if provided
    if start_delay is not None and start_delay > 0:
        advance_timeline_by_duration(start_delay)

    # Run the SDG pipeline
    run_sdg_pipeline(
        camera_prim.GetPath(), num_clips, num_frames_per_clip, capture_interval, use_instance_id, segmentation_mapping
    )

# Setup the environment and run the example
run_example(
    num_clips=NUM_CLIPS,
    num_frames_per_clip=NUM_FRAMES_PER_CLIP,
    capture_interval=CAPTURE_INTERVAL,
    start_delay=START_DELAY,
    use_instance_id=True,
)

simulation_app.close()
```

Script Editor

Full Script Editor Script

```python
import asyncio
import os

import carb
import omni.replicator.core as rep
import omni.timeline
import omni.usd
from isaacsim.core.experimental.utils.stage import add_reference_to_stage
from isaacsim.storage.native import get_assets_root_path_async
from pxr import UsdGeom

# Capture parameters
START_DELAY = 0.1  # Timeline duration delay before capturing the first clip
NUM_CLIPS = 3  # Number of video clips to capture with the CosmosWriter
NUM_FRAMES_PER_CLIP = 120  # Number of frames for each clip
CAPTURE_INTERVAL = 2  # Capture interval between frames (capture every N simulation steps)

# Stage and asset paths
STAGE_URL = "/Isaac/Samples/Replicator/Stage/full_warehouse_worker_and_anim_cameras.usd"
CARTER_NAV_ASSET_URL = "/Isaac/Samples/Replicator/OmniGraph/nova_carter_nav_only.usd"
CARTER_NAV_PATH = "/NavWorld/CarterNav"
CARTER_NAV_TARGET_PATH = f"{CARTER_NAV_PATH}/targetXform"
CARTER_CAMERA_PATH = f"{CARTER_NAV_PATH}/chassis_link/sensors/front_hawk/left/camera_left"
CARTER_NAV_POSITION = (-6, 4, 0)
CARTER_NAV_TARGET_POSITION = (3, 3, 0)

async def advance_timeline_by_duration_async(duration: float, max_updates: int = 1000):
    timeline = omni.timeline.get_timeline_interface()
    current_time = timeline.get_current_time()
    target_time = current_time + duration

    if timeline.get_end_time() < target_time:
        timeline.set_end_time(1000000)

    if not timeline.is_playing():
        timeline.play()

    print(f"Advancing timeline from {current_time:.4f}s to {target_time:.4f}s")
    step_count = 0
    while current_time < target_time:
        if step_count >= max_updates:
            print(f"Max updates reached: {step_count}, finishing timeline advance.")
            break

        prev_time = current_time
        await omni.kit.app.get_app().next_update_async()
        current_time = timeline.get_current_time()
        step_count += 1

        if step_count % 10 == 0:
            print(f"\tStep {step_count}, {current_time:.4f}s/{target_time:.4f}s")

        if current_time <= prev_time:
            print(f"Warning: Timeline did not advance at update {step_count} (time: {current_time:.4f}s).")
    print(f"Finished advancing timeline to {current_time:.4f}s (target {target_time:.4f}s) in {step_count} steps")

async def run_sdg_pipeline_async(
    camera_path,
    num_clips,
    num_frames_per_clip,
    capture_interval,
    use_instance_id=True,
    segmentation_mapping=None,
):
    rp = rep.create.render_product(camera_path, (1280, 720))
    cosmos_writer = rep.WriterRegistry.get("CosmosWriter")
    backend = rep.backends.get("DiskBackend")
    out_dir = os.path.join(os.getcwd(), f"_out_cosmos_warehouse")
    print(f"output_directory: {out_dir}")
    backend.initialize(output_dir=out_dir)
    cosmos_writer.initialize(
        backend=backend, use_instance_id=use_instance_id, segmentation_mapping=segmentation_mapping
    )
    cosmos_writer.attach(rp)

    # Make sure the timeline is playing
    timeline = omni.timeline.get_timeline_interface()
    if not timeline.is_playing():
        timeline.play()

    print(
        f"Starting SDG pipeline. Capturing {num_clips} clips with {num_frames_per_clip} frames each, every {capture_interval} simulation step(s)."
    )

    for clip_index in range(num_clips):
        print(f"Starting clip {clip_index + 1}/{num_clips}")

        frames_captured_count = 0
        simulation_step_index = 0
        while frames_captured_count < num_frames_per_clip:
            print(f"Simulation step {simulation_step_index}")
            if simulation_step_index % capture_interval == 0:
                print(f"\t Capturing frame {frames_captured_count + 1}/{num_frames_per_clip} for clip {clip_index + 1}")
                await rep.orchestrator.step_async(pause_timeline=False)
                frames_captured_count += 1
            else:
                await omni.kit.app.get_app().next_update_async()
            simulation_step_index += 1

        print(f"Finished clip {clip_index + 1}/{num_clips}. Captured {frames_captured_count} frames")

        # Move to next clip if not the last clip
        if clip_index < num_clips - 1:
            print(f"Moving to next clip...")
            cosmos_writer.next_clip()

    print("Waiting to finish processing and writing the data")
    await rep.orchestrator.wait_until_complete_async()
    print(f"Finished SDG pipeline. Captured {num_clips} clips with {num_frames_per_clip} frames each")
    cosmos_writer.detach()
    rp.destroy()
    timeline.pause()

async def run_example_async(
    num_clips,
    num_frames_per_clip,
    capture_interval,
    start_delay=0.0,
    use_instance_id=True,
    segmentation_mapping=None,
):
    assets_root_path = await get_assets_root_path_async()
    stage_path = assets_root_path + STAGE_URL
    print(f"Opening stage: '{stage_path}'")
    omni.usd.get_context().open_stage(stage_path)
    stage = omni.usd.get_context().get_stage()

    # Enable script nodes
    carb.settings.get_settings().set_bool("/app/omni.graph.scriptnode/opt_in", True)

    # Disable capture on play on the new stage, data is captured manually using the step function
    rep.orchestrator.set_capture_on_play(False)

    # Set DLSS to Quality mode (2) for best SDG results (Options: 0 (Performance), 1 (Balanced), 2 (Quality), 3 (Auto)
    carb.settings.get_settings().set("rtx/post/dlss/execMode", 2)

    # Load carter nova asset with its navigation graph
    carter_url_path = assets_root_path + CARTER_NAV_ASSET_URL
    print(f"Loading carter nova asset: '{carter_url_path}' at prim path: '{CARTER_NAV_PATH}'")
    carter_nav_prim = add_reference_to_stage(usd_path=carter_url_path, path=CARTER_NAV_PATH)

    if not carter_nav_prim.GetAttribute("xformOp:translate"):
        UsdGeom.Xformable(carter_nav_prim).AddTranslateOp()
    carter_nav_prim.GetAttribute("xformOp:translate").Set(CARTER_NAV_POSITION)

    # Set the navigation target position
    carter_navigation_target_prim = stage.GetPrimAtPath(CARTER_NAV_TARGET_PATH)
    if not carter_navigation_target_prim.IsValid():
        print(f"Carter navigation target prim not found at path: {CARTER_NAV_TARGET_PATH}, exiting")
        return
    if not carter_navigation_target_prim.GetAttribute("xformOp:translate"):
        UsdGeom.Xformable(carter_navigation_target_prim).AddTranslateOp()
    carter_navigation_target_prim.GetAttribute("xformOp:translate").Set(CARTER_NAV_TARGET_POSITION)

    # Use the carter nova front hawk camera for capturing data
    camera_prim = stage.GetPrimAtPath(CARTER_CAMERA_PATH)
    if not camera_prim.IsValid():
        print(f"Camera prim not found at path: {CARTER_CAMERA_PATH}, exiting")
        return

    # tickRate=0 forces autotrigger so the sensor cameras stay in sync with rep.orchestrator.step_async
    # under multi-tick rendering.
    if camera_prim.HasAttribute("omni:sensor:tickRate"):
        camera_prim.GetAttribute("omni:sensor:tickRate").Set(0.0)

    # Advance the timeline with the start delay if provided
    if start_delay is not None and start_delay > 0:
        await advance_timeline_by_duration_async(start_delay)

    # Run the SDG pipeline
    await run_sdg_pipeline_async(
        camera_prim.GetPath(),
        num_clips,
        num_frames_per_clip,
        capture_interval,
        use_instance_id,
        segmentation_mapping,
    )

# Setup the environment and run the example
asyncio.ensure_future(
    run_example_async(
        num_clips=NUM_CLIPS,
        num_frames_per_clip=NUM_FRAMES_PER_CLIP,
        capture_interval=CAPTURE_INTERVAL,
        start_delay=START_DELAY,
        use_instance_id=True,
    )
)
```

Code Explanation

This tab explains how the warehouse navigation example works and how the CosmosWriter captures multi-modal data during robot movement.

**Script Overview**

The script simulates a Carter Nova robot navigating through a warehouse while capturing synchronized multi-modal data from its front camera. The robot moves from a starting position to a target location, and the CosmosWriter generates ground truth data for Cosmos Transfer.

Main Execution Flow

```python
# Setup the environment and run the example
run_example(
    num_clips=NUM_CLIPS,
    num_frames_per_clip=NUM_FRAMES_PER_CLIP,
    capture_interval=CAPTURE_INTERVAL,
    start_delay=START_DELAY,
    use_instance_id=True,
)

simulation_app.close()
```

**Key Configuration Parameters**

Capture Parameters

* `NUM_CLIPS = 2`: Generate 2 separate video clips
* `NUM_FRAMES_PER_CLIP = 10`: Each clip contains 10 frames
* `CAPTURE_INTERVAL = 2`: Capture every 2nd simulation step
* `START_DELAY = 0.1`: Custom delay to start capturing at a specific time

**Data Capture Pipeline**

The `run_sdg_pipeline` function orchestrates the entire capture process:

SDG Pipeline Implementation

```python
def run_sdg_pipeline(
    camera_path, num_clips, num_frames_per_clip, capture_interval, use_instance_id=True, segmentation_mapping=None
):
    rp = rep.create.render_product(camera_path, (1280, 720))
    cosmos_writer = rep.WriterRegistry.get("CosmosWriter")
    backend = rep.backends.get("DiskBackend")
    out_dir = os.path.join(os.getcwd(), f"_out_cosmos_warehouse")
    print(f"output_directory: {out_dir}")
    backend.initialize(output_dir=out_dir)
    cosmos_writer.initialize(
        backend=backend, use_instance_id=use_instance_id, segmentation_mapping=segmentation_mapping
    )
    cosmos_writer.attach(rp)

    # Make sure the timeline is playing
    timeline = omni.timeline.get_timeline_interface()
    if not timeline.is_playing():
        timeline.play()

    print(
        f"Starting SDG pipeline. Capturing {num_clips} clips with {num_frames_per_clip} frames each, every {capture_interval} simulation step(s)."
    )

    for clip_index in range(num_clips):
        print(f"Starting clip {clip_index + 1}/{num_clips}")

        frames_captured_count = 0
        simulation_step_index = 0
        while frames_captured_count < num_frames_per_clip:
            print(f"Simulation step {simulation_step_index}")
            if simulation_step_index % capture_interval == 0:
                print(f"\t Capturing frame {frames_captured_count + 1}/{num_frames_per_clip} for clip {clip_index + 1}")
                rep.orchestrator.step(pause_timeline=False)
                frames_captured_count += 1
            else:
                simulation_app.update()
            simulation_step_index += 1

        print(f"Finished clip {clip_index + 1}/{num_clips}. Captured {frames_captured_count} frames")

        # Move to next clip if not the last clip
        if clip_index < num_clips - 1:
            print(f"Moving to next clip...")
            cosmos_writer.next_clip()

    print("Waiting to finish processing and writing the data")
    rep.orchestrator.wait_until_complete()
    print(f"Finished SDG pipeline. Captured {num_clips} clips with {num_frames_per_clip} frames each")
    cosmos_writer.detach()
    rp.destroy()
    timeline.pause()
```

**Key aspects:**
- The render product is created from the robotâs front camera at 1280x720 resolution
- `pause_timeline=False` allows the robot to continue moving during capture
- The simulation advances between captures to show navigation progress

**CosmosWriter Configuration**

Writer Modes and Parameters

The CosmosWriter supports two segmentation modes:

1. **Instance ID Mode** (default):

   ```python
   cosmos_writer.initialize(
       backend=backend, use_instance_id=use_instance_id, segmentation_mapping=segmentation_mapping
   )
   ```
2. **Semantic Segmentation Mode**:

   ```python
   segmentation_mapping = {
       "floor": [255, 0, 0, 255],  # Red
       "wall": [0, 255, 0, 255],  # Green
       "rack": [0, 0, 255, 255],  # Blue
   }

   # Note: This overrides instance ID mode and requires semantic annotations
   cosmos_writer.initialize(backend=backend, segmentation_mapping=segmentation_mapping)
   ```

**Timeline Management**

The script uses a helper function to advance the timeline before starting capture:

> Timeline Advancement
>
> ```python
> def advance_timeline_by_duration(duration: float, max_updates: int = 1000):
>     timeline = omni.timeline.get_timeline_interface()
>     current_time = timeline.get_current_time()
>     target_time = current_time + duration
>
>     if timeline.get_end_time() < target_time:
>         timeline.set_end_time(1000000)
>
>     if not timeline.is_playing():
>         timeline.play()
>
>     print(f"Advancing timeline from {current_time:.4f}s to {target_time:.4f}s")
>     step_count = 0
>     while current_time < target_time:
>         if step_count >= max_updates:
>             print(f"Max updates reached: {step_count}, finishing timeline advance.")
>             break
>
>         prev_time = current_time
>         simulation_app.update()
>         current_time = timeline.get_current_time()
>         step_count += 1
>
>         if step_count % 10 == 0:
>             print(f"\tStep {step_count}, {current_time:.4f}s/{target_time:.4f}s")
>
>         if current_time <= prev_time:
>             print(f"Warning: Timeline did not advance at update {step_count} (time: {current_time:.4f}s).")
>     print(f"Finished advancing timeline to {current_time:.4f}s (target {target_time:.4f}s) in {step_count} steps")
> ```

## Output Structure

After running the script, an output folder (e.g., `_out_cosmos_warehouse`) is created containing organized multi-modal data optimized for Cosmos Transfer and other foundation model training pipelines. Each clip represents a continuous sequence of frames captured during robot navigation:

```python
_out_cosmos_warehouse/
  clip_0000/                    # First clip sequence
    rgb/                        # Standard color images
      rgb_0000.png, rgb_0001.png, ...
    depth/                      # Colorized depth visualization
      depth_0000.png, depth_0001.png, ...
    segmentation/              # Instance/semantic masks
      segmentation_0000.png, segmentation_0001.png, ...
    shaded_seg/                # Segmentation with realistic shading
      shaded_seg_0000.png, shaded_seg_0001.png, ...
    edges/                      # Canny edge detection results
      edges_0000.png, edges_0001.png, ...
    rgb.mp4                     # Combined RGB video
    depth.mp4                   # Combined depth video
    segmentation.mp4            # Combined segmentation video
    shaded_seg.mp4              # Combined shaded segmentation video
    edges.mp4                   # Combined edges video
  clip_0001/                    # Next clip sequence
```

**What Each Modality Provides:**

* **RGB (rgb.mp4)**: The visual input video used with Cosmos Transferâs `vis` control branch for preserving lighting and camera properties
* **Depth (depth.mp4)**: 3D spatial information used with the `depth` control branch to maintain perspective and spatial relationships
* **Segmentation (segmentation.mp4)**: Instance or semantic masks used with the `seg` control branch for object-level transformations
* **Shaded Segmentation (shaded\_seg.mp4)**: Combines segmentation with realistic shading for enhanced visual coherence
* **Edges (edges.mp4)**: Structural boundaries used with the `edge` control branch to preserve object shapes while allowing material and lighting changes

These MP4 files can be directly passed to Cosmos Transfer as control inputs. The PNG sequences are provided for frame-level inspection or custom processing pipelines.

## Advanced Usage

**Custom Segmentation Colors:**

Map specific semantic labels to custom colors when you need consistent class identification across datasets. Use this when training models that require specific object classes to maintain the same color/ID across all training data, ensuring Cosmos Transfer preserves class relationships.

```python
segmentation_mapping = {
    "floor": [255, 0, 0, 255],  # Red
    "wall": [0, 255, 0, 255],  # Green
    "rack": [0, 0, 255, 255],  # Blue
}

# Note: This overrides instance ID mode and requires semantic annotations
cosmos_writer.initialize(backend=backend, segmentation_mapping=segmentation_mapping)
```

**Edge Detection Tuning:**

Adjust Canny edge detection parameters for the hysteresis procedure when generating edge maps. The Canny algorithm uses two thresholds:

* **Low threshold**: Edges with gradient magnitude above this value are considered as potential edges
* **High threshold**: Edges with gradient magnitude above this value are definitely edges

Lower threshold values detect more edges (including noise), while higher values produce cleaner output with only strong edges. Values typically range from 10-200.

```python
cosmos_writer.initialize(
    backend=backend,
    use_instance_id=True,
    canny_threshold_low=10,  # Low threshold for hysteresis
    canny_threshold_high=100,  # High threshold for hysteresis
)
```

## Using Data with Cosmos Transfer

The generated data can be used with [Cosmos Transfer](https://docs.nvidia.com/cosmos/latest/) to create high-quality visual simulations. This enables sim-to-real transfer where synthetic scenes are transformed into photorealistic environments while preserving robot motions and scene structure.

For real-world examples of this workflow, see the [Cosmos Cookbook Robotics Gallery](https://nvidia-cosmos.github.io/cosmos-cookbook/gallery/robotics_inference.html), which demonstrates:

* **Edge-only control**: Transform simulation videos into diverse kitchen styles (white cabinets, red cabinets, wood tones) and robot materials (plastic, metal, gold) while preserving exact robot motions
* **Multi-control**: Combine depth, edge, and segmentation controls for precise scene manipulation

Hereâs how the modalities map to Transferâs control branches:

**Basic Single Control Example:**

```python
{
    "prompt": "A modern warehouse with autonomous robots...",
    "input_video_path": "_out_cosmos_warehouse/clip_0000/rgb.mp4",
    "edge": {
        "control_weight": 1.0
    }
}
```

**Multi-Modal Control Example:**

```python
{
    "prompt": "High-quality warehouse simulation...",
    "input_video_path": "_out_cosmos_warehouse/clip_0000/rgb.mp4",
    "vis": {"control_weight": 0.25},
    "edge": {"control_weight": 0.25},
    "depth": {
        "input_control": "_out_cosmos_warehouse/clip_0000/depth.mp4",
        "control_weight": 0.25
    },
    "seg": {
        "input_control": "_out_cosmos_warehouse/clip_0000/segmentation.mp4",
        "control_weight": 0.25
    }
}
```

**Key Considerations:**

* **Control Weights**: Values 0.0-1.0 control adherence (higher = stricter following, lower = more creative freedom)
* **Automatic Normalization**: If total weights > 1.0, theyâre normalized automatically
* **Prompting**: Focus on single scenes with rich descriptions; avoid camera control instructions
* **Safety**: Human faces are automatically blurred by Cosmos Guardrail

For advanced features like spatiotemporal control maps and prompt upsampling, refer to the [Cosmos Transfer documentation](https://docs.nvidia.com/cosmos/latest/).

## Summary

This tutorial demonstrated using the CosmosWriter to generate synchronized multi-modal data from a robot navigating a warehouse. The output provides ground truth for Cosmos Transfer to create high-quality visual simulations for physical AI applications.

**Next Steps:**

1. **Explore your output**: Navigate to the generated output folder (e.g., `_out_cosmos_warehouse`) to inspect the RGB, depth, segmentation, and edge data
2. **Use with Cosmos Transfer**: Pass the generated MP4 files to Cosmos [Transfer1](https://docs.nvidia.com/cosmos/latest/transfer1/index.html) or [Transfer2.5](https://docs.nvidia.com/cosmos/latest/transfer2.5/index.html) using the JSON configuration examples above
3. **See real examples**: Visit the [Cosmos Cookbook Robotics Gallery](https://nvidia-cosmos.github.io/cosmos-cookbook/gallery/robotics_inference.html) for examples of sim-to-real transformations using similar data
4. **Customize for your use case**: Adjust capture parameters, segmentation mappings, and edge detection thresholds to optimize for your specific training pipeline

On this page

* [Why Use the CosmosWriter?](#why-use-the-cosmoswriter)
* [Prerequisites](#prerequisites)
* [What the CosmosWriter Generates](#what-the-cosmoswriter-generates)
* [Implementation](#implementation)
* [Output Structure](#output-structure)
* [Advanced Usage](#advanced-usage)
* [Using Data with Cosmos Transfer](#using-data-with-cosmos-transfer)
* [Summary](#summary)

---

### InfiniGen SDG

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/replicator_tutorials/tutorial_replicator_infinigen_sdg.html

* [Synthetic Data Generation](../synthetic_data_generation/index.html)
* [Perception Data Generation (Replicator)](index.html)
* Environment Based Synthetic Dataset Generation with Infinigen

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Environment Based Synthetic Dataset Generation with Infinigen

This tutorial explains how to set up a synthetic data generation (SDG) pipeline in Isaac Sim using the [omni.replicator](https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator.html "(in Omniverse Extensions)") extension and procedurally generated environments from [Infinigen](https://infinigen.org/). The example uses the [standalone](../introduction/workflows.html#standalone-application) workflow.

Example of Infinigen generated rooms.

Example data collected from the synthetic dataset generation pipeline.

## Learning Objectives

In this tutorial, you will learn how to:

* Load procedurally generated environments from Infinigen as background scenes.
* Prepare the environments for SDG and physics simulations.
* Load physics-enabled target assets (labeled) for data collection and distractor assets (unlabeled) for scene diversity.
* Use built-in Replicator randomizer graphs manually triggered at custom intervals, detached from the writing process.
* Use custom USD / Isaac Sim API functions for custom randomizers.
* Use multiple Replicator Writers and cameras (render products) to save different types of data from different viewpoints.
* Use config files to easily customize the simulation and data collection process.
* Understand and customize configuration parameters for flexibility.

## Prerequisites

Before starting this tutorial, you should be familiar with:

* USD / Isaac Sim APIs for creating and manipulating USD stages.
* [Rigid-body dynamics](https://docs.omniverse.nvidia.com/kit/docs/omni_physics/latest/dev_guide/rigid_bodies_articulations/rigid_bodies.html "(in Omni Physics)") and physics simulation in Isaac Sim.
* Replicator [randomizers](https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator/randomizer_details.html "(in Omniverse Extensions)") and [OmniGraph](https://docs.omniverse.nvidia.com/extensions/latest/ext_omnigraph.html "(in Omniverse Extensions)") for a better understanding of the Replicator randomization graphs pipeline.
* Running simulations as [Standalone Applications](../introduction/workflows.html#standalone-application).
* Procedurally generating environments using [Infinigen](https://infinigen.org/).

## Generating Infinigen Environments

1. **Install Infinigen**: Follow the installation instructions on the [Infinigen GitHub Repository](https://github.com/princeton-vl/infinigen/blob/main/docs/Installation.md).

   Note

   The Infinigen scene generation step is only tested on Linux. Refer to the [Infinigen platform support matrix](https://github.com/princeton-vl/infinigen/blob/main/docs/Installation.md#installation-options--supported-platforms) for the current platform status, as Infinigen is an external library maintained outside of Isaac Sim.
2. **Generate Environments**: Use the [Hello Room](https://github.com/princeton-vl/infinigen/blob/main/docs/HelloRoom.md) instructions to generate indoor scenes using various settings and parameters.
3. **Example Script**: Use the following example script (Linux) to generate multiple dining room environments with different seeds. The script can be run directly from the terminal.

   ```python
   # Loop from 1 to 10 to generate 10 scenes
   for i in {1..10}
   do
     # Create the output folders for both the Infinigen generation and the Omniverse export
     mkdir -p outputs/indoors/dining_room_$i
     mkdir -p outputs/omniverse/dining_room_$i

     # Step 1: Run Infinigen scene generation for a DiningRoom scene with a specific seed
     python -m infinigen_examples.generate_indoors \
       --seed $i \
       --task coarse \
       --output_folder outputs/indoors/dining_room_$i \
       -g fast_solve.gin singleroom.gin \
       -p compose_indoors.terrain_enabled=False restrict_solving.restrict_parent_rooms=\[\"DiningRoom\"\] &&

     # Step 2: Export the generated scene to Omniverse-compatible format
     python -m infinigen.tools.export \
       --input_folder outputs/indoors/dining_room_$i \
       --output_folder outputs/omniverse/dining_room_$i \
       -f usdc \
       -r 1024 \
       --omniverse
   done
   ```

   * This script generates 10 unique dining room environments by varying the seed value.
   * The `infinigen_examples.generate_indoors` command generates the environments and stores them in `outputs/indoors/dining_room_$i`.
   * The `infinigen.tools.export` command exports the generated environments to the selected format, saving them to `outputs/omniverse/dining_room_$i`.
   * The `-f usdc` flag specifies the format of the exported file to USD.
   * The `--omniverse` flag ensures compatibility with Omniverse applications.

## Scenario Overview

In this tutorial, we will use procedurally generated environments as backdrops for synthetic data generation. These environments are then configured with colliders and physics properties, enabling physics-based simulations. Within each indoor environment, we define a âworking areaââin this case, the dining tableâwhere we will place both labeled target assets and unlabeled distractor assets.

The assets are divided into two categories:

* **Falling assets**: Physics-enabled objects that interact with the environment and settle onto surfaces, such as the ground or table.
* **Floating assets**: Objects equipped only with colliders that remain floating in the air.

For each background environment, we will capture frames in two scenarios:

1. Assets floating around the working area.
2. Physics-enabled assets that have settled on surfaces like the ground or table.

To capture these frames, we use multiple cameras (render products) configured with one or multiple writers. The cameras will be randomized for each frame, changing their positions around the working area and orienting toward randomly selected target assets.

Once the captures for one environment are complete, a new environment will be loaded, configured with colliders and physics properties, and the process will repeat until the desired number of captures is achieved.

During the capture process, we will apply randomizers at various frames to introduce variability into the scene. These randomizations include:

* Object poses.
* Lighting configurations, including dome light settings.
* Colors of shape distractors.

By incorporating these randomizations, we increase the diversity of the dataset, making it more robust for training machine learning models.

## Getting Started

The main script for this tutorial is located at:

`<install_path>/standalone_examples/replicator/infinigen/infinigen_sdg.py`

This script is designed to run as a **Standalone Application**. The default configurations are stored within the script itself in the form of a Python dictionary. You can override these defaults by providing custom configuration files in JSON or YAML format.

Helper functions are located in the `infinigen_sdg_utils.py` file. These functions help with loading environments, spawning assets, randomizing object poses, and running physics simulations.

To generate a synthetic dataset using the default configuration, run the following command (on Windows use `python.bat` instead of `python.sh`):

```python
./python.sh standalone_examples/replicator/infinigen/infinigen_sdg.py
```

To use a custom configuration file that supports multiple writers and other custom settings, use the âconfig argument:

```python
./python.sh standalone_examples/replicator/infinigen/infinigen_sdg.py \
    --config standalone_examples/replicator/infinigen/config/infinigen_multi_writers_pt.yaml
```

## Implementation

The following sections provide an overview of the key steps involved in setting up and running the synthetic data generation pipeline.
The complete implementation consists of two files: the main script and a utilities module.

Main script

```python
"""Generate synthetic datasets using infinigen (https://infinigen.org/) generated environments."""

import argparse
import json
import os

import yaml
from isaacsim import SimulationApp

# Default config dict, can be updated/replaced using json/yaml config files ('--config' cli argument)
config = {
    "environments": {
        # List of background environments (list of folders or files)
        "folders": ["/Isaac/Samples/Replicator/Infinigen/dining_rooms/"],
        "files": [],
    },
    "capture": {
        # Number of captures (frames = total_captures * num_cameras)
        "total_captures": 9,
        # Number of captures per environment before running the simulation (objects in the air)
        "num_floating_captures_per_env": 2,
        # Number of captures per environment after running the simulation (objects fallen)
        "num_dropped_captures_per_env": 2,
        # Number of cameras to capture from (each camera will have a render product attached)
        "num_cameras": 2,
        # Resolution of the captured frames
        "resolution": (720, 480),
        # Disable render products throughout the piepline, enable them only when capturing the frames
        "disable_render_products": False,
        # Number of subframes to render (RealTimePathTracing) to avoid temporal rendering artifacts (e.g. ghosting)
        "rt_subframes": 8,
        # Use PathTracing renderer or RealTimePathTracing when capturing the frames
        "path_tracing": False,
        # Offset to avoid the images always being in the image center
        "camera_look_at_target_offset": 0.1,
        # Distance between the camera and the target object
        "camera_distance_to_target_range": (1.15, 1.45),
        # Number of scene lights to create in the working area
        "num_scene_lights": 3,
    },
    "writers": [
        {
            # Type of the writer to use (e.g. PoseWriter, BasicWriter, etc.) and the kwargs to pass to the writer init
            "type": "PoseWriter",
            "kwargs": {
                "output_dir": "_out_infinigen_posewriter",
                "format": None,
                "use_subfolders": True,
                "write_debug_images": True,
                "skip_empty_frames": False,
            },
        }
    ],
    "labeled_assets": {
        # Labeled assets with auto-labeling (e.g. 002_banana -> banana) using regex pattern replacement on the asset name
        "auto_label": {
            # Number of labeled assets to create from the given files/folders list
            "num": 6,
            # Chance to disable gravity for the labeled assets (0.0 - all the assets will fall, 1.0 - all the assets will float)
            "gravity_disabled_chance": 0.25,
            # List of folders and files to search for the labeled assets
            "folders": ["/Isaac/Props/YCB/Axis_Aligned/"],
            "files": ["/Isaac/Props/YCB/Axis_Aligned/036_wood_block.usd"],
            # Regex pattern to replace in the asset name (e.g. "002_banana" -> "banana")
            "regex_replace_pattern": r"^\d+_",
            "regex_replace_repl": "",
        },
        # Manually labeled assets with specific labels and properties
        "manual_label": [
            {
                "url": "/Isaac/Props/YCB/Axis_Aligned/008_pudding_box.usd",
                "label": "pudding_box",
                "num": 2,
                "gravity_disabled_chance": 0.25,
            },
            {
                "url": "/Isaac/Props/YCB/Axis_Aligned_Physics/006_mustard_bottle.usd",
                "label": "mustard_bottle",
                "num": 2,
                "gravity_disabled_chance": 0.25,
            },
        ],
    },
    "distractors": {
        # Shape distractors (unlabeled background assets) to drop in the scene (e.g. capsules, cones, cylinders)
        "shape_distractors": {
            # Amount of shape distractors to create
            "num": 20,
            # Chance to disable gravity for the shape distractors
            "gravity_disabled_chance": 0.25,
            # List of shape types to randomly choose from
            "types": ["capsule", "cone", "cylinder", "sphere", "cube"],
        },
        # Mesh distractors (unlabeled background assets) to drop in the scene
        "mesh_distractors": {
            # Amount of mesh distractors to create
            "num": 8,
            # Chance to disable gravity for the mesh distractors
            "gravity_disabled_chance": 0.25,
            # List of folders and files to search to randomly choose from
            "folders": [
                "/Isaac/Environments/Simple_Warehouse/Props/",
                "/Isaac/Environments/Office/Props/",
            ],
            "files": [
                "/Isaac/Environments/Hospital/Props/SM_MedicalBag_01a.usd",
                "/Isaac/Environments/Hospital/Props/SM_MedicalBox_01g.usd",
            ],
        },
    },
    # Physics GPU memory settings for the simulation (override defaults if scenes are complex)
    "physics": {
        # GPU collision stack size in bytes (default: 300 MB, PhysX default is only 64 MB which is
        # insufficient for infinigen scenes with many colliders)
        "gpu_collision_stack_size": 314572800,
    },
    # Hide ceilling to get a top-down view of the scene, move viewport camera to the top-down view
    "debug_mode": True,
}

# Check if there are any config files (yaml or json) are passed as arguments
parser = argparse.ArgumentParser()
parser.add_argument("--config", required=False, help="Include specific config parameters (json or yaml))")
parser.add_argument(
    "--close-on-completion", action="store_true", help="Ensure the app closes on completion even in debug mode"
)
args, unknown = parser.parse_known_args()
args_config = {}
if args.config and os.path.isfile(args.config):
    with open(args.config) as f:
        if args.config.endswith(".json"):
            args_config = json.load(f)
        elif args.config.endswith(".yaml"):
            args_config = yaml.safe_load(f)
        else:
            print(f"[SDG] Warning: Config file {args.config} is not json or yaml, using default config")
else:
    print(f"[SDG] Warning: Config file {args.config} does not exist, using default config")

# Update the default config dict with the external one
config.update(args_config)

simulation_app = SimulationApp(launch_config={"headless": False})

from itertools import cycle

import carb.settings
import infinigen_sdg_utils as infinigen_utils
import numpy as np
import omni.kit.app
import omni.replicator.core as rep
import omni.usd
from isaacsim.core.utils.viewports import set_camera_view

# Run the SDG pipeline on the scenarios
def run_sdg(config):
    """Run the synthetic data generation pipeline on the configured scenarios."""
    # Load the config parameters
    env_config = config.get("environments", {})
    env_urls = infinigen_utils.get_usd_paths(
        files=env_config.get("files", []), folders=env_config.get("folders", []), skip_folder_keywords=[".thumbs"]
    )
    if not env_urls:
        print("[SDG] Error: No environment USD files found. Please check the 'environments' config.")
        return
    print(f"[SDG] Found {len(env_urls)} environment(s)")
    capture_config = config.get("capture", {})
    writers_config = config.get("writers", {})
    labeled_assets_config = config.get("labeled_assets", {})
    distractors_config = config.get("distractors", {})

    # Create a new stage
    print("[SDG] Creating a new stage")
    omni.usd.get_context().new_stage()
    stage = omni.usd.get_context().get_stage()

    # Disable capture on play
    rep.orchestrator.set_capture_on_play(False)

    # Disable UJITSO cooking ([Warning] [omni.ujitso] UJITSO : Build storage validation failed)
    carb.settings.get_settings().set("/physics/cooking/ujitsoCollisionCooking", False)

    # Set DLSS to Quality mode (2) for best SDG results , options: 0 (Performance), 1 (Balanced), 2 (Quality), 3 (Auto)
    carb.settings.get_settings().set("rtx/post/dlss/execMode", 2)

    # Initialize randomization
    rep.set_global_seed(12)
    rng = np.random.default_rng(12)

    # Debug mode (hide ceiling, move viewport camera to the top-down view)
    debug_mode = config.get("debug_mode", False)

    # Create the cameras
    cameras = []
    num_cameras = capture_config.get("num_cameras", 0)
    rep.functional.create.scope(name="Cameras")
    for i in range(num_cameras):
        cam_prim = rep.functional.create.camera(parent="/Cameras", name=f"cam_{i}", clipping_range=(0.25, 1000))
        cameras.append(cam_prim)
    print(f"[SDG] Created {len(cameras)} cameras")

    # Create the render products for the cameras
    render_products = []
    resolution = capture_config.get("resolution", (1280, 720))
    disable_render_products = capture_config.get("disable_render_products", False)
    for cam in cameras:
        rp = rep.create.render_product(cam.GetPath(), resolution, name=f"rp_{cam.GetName()}")
        if disable_render_products:
            rp.hydra_texture.set_updates_enabled(False)
        render_products.append(rp)
    print(f"[SDG] Created {len(render_products)} render products")

    # Only create the writers if there are render products to attach to
    writers = []
    if render_products:
        for writer_config in writers_config:
            writer = infinigen_utils.setup_writer(writer_config)
            if writer:
                writer.attach(render_products)
                writers.append(writer)
                print(
                    f"[SDG] {writer_config['type']}'s out dir: {writer_config.get('kwargs', {}).get('output_dir', '')}"
                )
    print(f"[SDG] Created {len(writers)} writers")

    # Load target assets with auto-labeling (e.g. 002_banana -> banana)
    auto_label_config = labeled_assets_config.get("auto_label", {})
    auto_floating_assets, auto_falling_assets = infinigen_utils.load_auto_labeled_assets(auto_label_config, rng)
    print(f"[SDG] Loaded {len(auto_floating_assets)} floating auto-labeled assets")
    print(f"[SDG] Loaded {len(auto_falling_assets)} falling auto-labeled assets")

    # Load target assets with manual labels
    manual_label_config = labeled_assets_config.get("manual_label", [])
    manual_floating_assets, manual_falling_assets = infinigen_utils.load_manual_labeled_assets(manual_label_config, rng)
    print(f"[SDG] Loaded {len(manual_floating_assets)} floating manual-labeled assets")
    print(f"[SDG] Loaded {len(manual_falling_assets)} falling manual-labeled assets")
    target_assets = auto_floating_assets + auto_falling_assets + manual_floating_assets + manual_falling_assets

    # Load the shape distractors
    shape_distractors_config = distractors_config.get("shape_distractors", {})
    floating_shapes, falling_shapes = infinigen_utils.load_shape_distractors(shape_distractors_config, rng)
    print(f"[SDG] Loaded {len(floating_shapes)} floating shape distractors")
    print(f"[SDG] Loaded {len(falling_shapes)} falling shape distractors")
    shape_distractors = floating_shapes + falling_shapes

    # Load the mesh distractors
    mesh_distractors_config = distractors_config.get("mesh_distractors", {})
    floating_meshes, falling_meshes = infinigen_utils.load_mesh_distractors(mesh_distractors_config, rng)
    print(f"[SDG] Loaded {len(floating_meshes)} floating mesh distractors")
    print(f"[SDG] Loaded {len(falling_meshes)} falling mesh distractors")
    mesh_distractors = floating_meshes + falling_meshes

    # Resolve any centimeter-meter scale issues of the assets
    infinigen_utils.resolve_scale_issues_with_metrics_assembler()

    # Create lights to randomize in the working area
    scene_lights = []
    num_scene_lights = capture_config.get("num_scene_lights", 0)
    for i in range(num_scene_lights):
        light_prim = stage.DefinePrim(f"/Lights/SphereLight_scene_{i}", "SphereLight")
        scene_lights.append(light_prim)
    print(f"[SDG] Created {len(scene_lights)} scene lights")

    # Register replicator randomizers and trigger them once
    print("[SDG] Registering replicator graph randomizers")
    infinigen_utils.register_dome_light_randomizer()
    infinigen_utils.register_shape_distractors_color_randomizer(shape_distractors)

    # Configure the PhysX scene GPU memory settings before running any simulation.
    # This prevents PxGpuDynamicsMemoryConfig::collisionStackSize buffer overflow errors
    # when simulating complex scenes with many colliders (distractors, assets, environment meshes).
    physics_config = config.get("physics", {})
    print("[SDG] Configuring physics scene GPU memory settings")
    infinigen_utils.configure_physics_scene(physics_config)

    # Check if the render mode needs to be switched to path tracing for the capture (by default: RealTimePathTracing)
    use_path_tracing = capture_config.get("path_tracing", False)

    # Capture detail using subframes (https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator/subframes_examples.html)
    rt_subframes = capture_config.get("rt_subframes", 3)

    # Min and max distance between the camera and the target object
    camera_distance_to_target_range = capture_config.get("camera_distance_to_target_range", (0.5, 1.5))

    # Number of captures (frames = total_captures * num_cameras)
    # NOTE: if captured frames have no labeled data, they can be skipped (e.g. PoseWriter with skip_empty_frames=True)
    total_captures = capture_config.get("total_captures", 0)

    # Number of captures per environment with the objects in the air or dropped
    num_floating_captures_per_env = capture_config.get("num_floating_captures_per_env", 0)
    num_dropped_captures_per_env = capture_config.get("num_dropped_captures_per_env", 0)

    # Start the SDG loop
    env_cycle = cycle(env_urls)
    capture_counter = 0
    while capture_counter < total_captures:
        # Load the next environment
        env_url = next(env_cycle)

        # Load the new environment
        print(f"[SDG] Loading environment: {env_url}")
        infinigen_utils.load_env(env_url, prim_path="/Environment")

        # Setup the environment (add collision, fix lights, etc.) and update the app once to apply the changes
        print(f"[SDG] Setting up the environment")
        infinigen_utils.setup_env(root_path="/Environment", hide_top_walls=debug_mode)
        simulation_app.update()

        # Get the location of the prim above which the assets will be randomized
        working_area_loc = infinigen_utils.get_matching_prim_location(
            match_string="TableDining", root_path="/Environment"
        )

        # Move viewport above the working area to get a top-down view of the scene
        if debug_mode:
            camera_loc = (working_area_loc[0], working_area_loc[1], working_area_loc[2] + 10)
            set_camera_view(eye=np.array(camera_loc), target=np.array(working_area_loc))

        # Get the spawn areas as offseted location ranges from the working area (min_x, min_y, min_z, max_x, max_y, max_z)
        print(f"[SDG] Randomizing {len(target_assets)} target assets around the working area")
        target_loc_range = infinigen_utils.offset_range((-0.5, -0.5, 1, 0.5, 0.5, 1.5), working_area_loc)
        infinigen_utils.randomize_poses(
            target_assets,
            location_range=target_loc_range,
            rotation_range=(0, 360),
            scale_range=(0.95, 1.15),
            rng=rng,
        )

        # Mesh distractors
        print(f"[SDG] Randomizing {len(mesh_distractors)} mesh distractors around the working area")
        mesh_loc_range = infinigen_utils.offset_range((-1, -1, 1, 1, 1, 2), working_area_loc)
        infinigen_utils.randomize_poses(
            mesh_distractors,
            location_range=mesh_loc_range,
            rotation_range=(0, 360),
            scale_range=(0.3, 1.0),
            rng=rng,
        )

        # Shape distractors
        print(f"[SDG] Randomizing {len(shape_distractors)} shape distractors around the working area")
        shape_loc_range = infinigen_utils.offset_range((-1.5, -1.5, 1, 1.5, 1.5, 2), working_area_loc)
        infinigen_utils.randomize_poses(
            shape_distractors,
            location_range=shape_loc_range,
            rotation_range=(0, 360),
            scale_range=(0.01, 0.1),
            rng=rng,
        )

        print(f"[SDG] Randomizing {len(scene_lights)} scene lights properties and locations around the working area")
        lights_loc_range = infinigen_utils.offset_range((-2, -2, 1, 2, 2, 3), working_area_loc)
        infinigen_utils.randomize_lights(
            scene_lights,
            location_range=lights_loc_range,
            intensity_range=(500, 2500),
            color_range=(0.1, 0.1, 0.1, 0.9, 0.9, 0.9),
            rng=rng,
        )

        print("[SDG] Randomizing dome lights")
        rep.utils.send_og_event(event_name="randomize_dome_lights")

        print("[SDG] Randomizing shape distractor colors")
        rep.utils.send_og_event(event_name="randomize_shape_distractor_colors")

        # Run the physics simulation for a few frames to solve any collisions
        print("[SDG] Fixing collisions through physics simulation")
        simulation_app.update()
        infinigen_utils.run_simulation(num_frames=4, render=True)

        # Check if the render products need to be enabled for the capture
        if disable_render_products:
            for rp in render_products:
                rp.hydra_texture.set_updates_enabled(True)

        # Check if the render mode needs to be switched to path tracing for the capture
        if use_path_tracing:
            print("[SDG] Switching to PathTracing render mode")
            carb.settings.get_settings().set("/rtx/rendermode", "PathTracing")

        # Capture frames with the objects in the air
        for i in range(num_floating_captures_per_env):
            # Check if the total captures have been reached
            if capture_counter >= total_captures:
                break
            # Randomize the camera poses
            print(f"[SDG] Randomizing camera poses ({len(cameras)} cameras)")
            infinigen_utils.randomize_camera_poses(
                cameras, target_assets, camera_distance_to_target_range, polar_angle_range=(0, 75), rng=rng
            )
            print(
                f"[SDG] Capturing floating assets {i+1}/{num_floating_captures_per_env} (total: {capture_counter+1}/{total_captures})"
            )
            rep.orchestrator.step(rt_subframes=rt_subframes, delta_time=0.0)
            capture_counter += 1

        # Check if the render products need to be disabled until the next capture
        if disable_render_products:
            for rp in render_products:
                rp.hydra_texture.set_updates_enabled(False)

        # Check if the render mode needs to be switched back to raytracing until the next capture
        if use_path_tracing:
            carb.settings.get_settings().set("/rtx/rendermode", "RealTimePathTracing")

        print("[SDG] Running the simulation")
        infinigen_utils.run_simulation(num_frames=200, render=False)

        # Check if the render products need to be enabled for the capture
        if disable_render_products:
            for rp in render_products:
                rp.hydra_texture.set_updates_enabled(True)

        # Check if the render mode needs to be switched to path tracing for the capture
        if use_path_tracing:
            carb.settings.get_settings().set("/rtx/rendermode", "PathTracing")

        for i in range(num_dropped_captures_per_env):
            # Check if the total captures have been reached
            if capture_counter >= total_captures:
                break
            # Spawn the cameras with a smaller polar angle to have mostly a top-down view of the objects
            print("[SDG] Randomizing camera poses")
            infinigen_utils.randomize_camera_poses(
                cameras,
                target_assets,
                distance_range=camera_distance_to_target_range,
                polar_angle_range=(0, 45),
                rng=rng,
            )
            print(
                f"[SDG] Capturing dropped assets {i+1}/{num_dropped_captures_per_env} (total: {capture_counter+1}/{total_captures})"
            )
            rep.orchestrator.step(rt_subframes=rt_subframes, delta_time=0.0)
            capture_counter += 1

        # Check if the render products need to be disabled until the next capture
        if disable_render_products:
            for rp in render_products:
                rp.hydra_texture.set_updates_enabled(False)

        # Check if the render mode needs to be switched back to raytracing until the next capture
        if use_path_tracing:
            carb.settings.get_settings().set("/rtx/rendermode", "RealTimePathTracing")

    # Wait until the data is written to the disk
    rep.orchestrator.wait_until_complete()

    # Detach the writers
    print("[SDG] Detaching writers")
    for writer in writers:
        writer.detach()

    # Destroy render products
    print("[SDG] Destroying render products")
    for rp in render_products:
        rp.destroy()

    print(f"[SDG] Finished, captured {capture_counter * num_cameras} frames")

# Check if debug mode is enabled
debug_mode = config.get("debug_mode", False)

# Start the SDG pipeline
print("[SDG] Starting the SDG pipeline")
run_sdg(config)
print("[SDG] Pipeline finished")

# Make sure the app closes on completion even if in debug mode
if args.close_on_completion:
    simulation_app.close()

# In debug mode, keep the app running until manually closed
if debug_mode:
    while simulation_app.is_running():
        simulation_app.update()

simulation_app.close()
```

Utils module

```python
"""Provide utility functions for Infinigen synthetic data generation."""

import math
import os
import re
from itertools import chain

import numpy as np
import omni.client
import omni.kit.app
import omni.kit.commands
import omni.physics.core
import omni.replicator.core as rep
import omni.timeline
import omni.usd
from isaacsim.core.utils.semantics import add_labels, remove_labels
from isaacsim.core.utils.stage import add_reference_to_stage
from isaacsim.storage.native import get_assets_root_path
from pxr import Gf, PhysxSchema, Usd, UsdGeom, UsdPhysics

def add_colliders(root_prim: Usd.Prim, approximation_type: str = "convexHull") -> None:
    """Add collision attributes to mesh and geometry primitives under the root prim."""
    for desc_prim in Usd.PrimRange(root_prim):
        if desc_prim.IsA(UsdGeom.Gprim):
            if not desc_prim.HasAPI(UsdPhysics.CollisionAPI):
                collision_api = UsdPhysics.CollisionAPI.Apply(desc_prim)
            else:
                collision_api = UsdPhysics.CollisionAPI(desc_prim)
            collision_api.CreateCollisionEnabledAttr(True)

        if desc_prim.IsA(UsdGeom.Mesh):
            if not desc_prim.HasAPI(UsdPhysics.MeshCollisionAPI):
                mesh_collision_api = UsdPhysics.MeshCollisionAPI.Apply(desc_prim)
            else:
                mesh_collision_api = UsdPhysics.MeshCollisionAPI(desc_prim)
            mesh_collision_api.CreateApproximationAttr().Set(approximation_type)

def add_rigid_body(prim: Usd.Prim, disable_gravity: bool = False, ensure_mass: bool = False) -> None:
    """Apply rigid body physics, optionally ensuring a valid mass property exists (defaults to 1.0 kg)."""
    rep.functional.physics.apply_rigid_body(prim, disableGravity=disable_gravity)
    if not ensure_mass:
        return
    if not prim.HasAPI(UsdPhysics.MassAPI):
        UsdPhysics.MassAPI.Apply(prim)
    mass_api = UsdPhysics.MassAPI(prim)
    mass_attr = mass_api.GetMassAttr()
    if not mass_attr or mass_attr.Get() is None or mass_attr.Get() <= 0:
        mass_api.CreateMassAttr(1.0)

def get_random_pose_on_sphere(
    origin: tuple[float, float, float],
    radius_range: tuple[float, float],
    polar_angle_range: tuple[float, float],
    camera_forward_axis: tuple[float, float, float] = (0, 0, -1),
    rng: np.random.Generator = None,
) -> tuple[Gf.Vec3d, Gf.Quatf]:
    """Generate a random pose on a sphere looking at the origin, with specified radius and polar angle ranges."""
    if rng is None:
        rng = np.random.default_rng()

    # https://docs.isaacsim.omniverse.nvidia.com/latest/reference_material/reference_conventions.html
    # Convert degrees to radians for polar angles (theta)
    polar_angle_min_rad = math.radians(polar_angle_range[0])
    polar_angle_max_rad = math.radians(polar_angle_range[1])

    # Generate random spherical coordinates
    radius = rng.uniform(radius_range[0], radius_range[1])
    polar_angle = rng.uniform(polar_angle_min_rad, polar_angle_max_rad)
    azimuthal_angle = rng.uniform(0, 2 * math.pi)

    # Convert spherical coordinates to Cartesian coordinates
    x = radius * math.sin(polar_angle) * math.cos(azimuthal_angle)
    y = radius * math.sin(polar_angle) * math.sin(azimuthal_angle)
    z = radius * math.cos(polar_angle)

    # Calculate the location in 3D space
    location = Gf.Vec3d(origin[0] + x, origin[1] + y, origin[2] + z)

    # Calculate direction vector from camera to look_at point
    direction = Gf.Vec3d(origin) - location
    direction_normalized = direction.GetNormalized()

    # Calculate rotation from forward direction (rotateFrom) to direction vector (rotateTo)
    rotation = Gf.Rotation(Gf.Vec3d(camera_forward_axis), direction_normalized)
    orientation = Gf.Quatf(rotation.GetQuat())

    return location, orientation

def randomize_camera_poses(
    cameras: list[Usd.Prim],
    targets: list[Usd.Prim],
    distance_range: tuple[float, float],
    polar_angle_range: tuple[float, float] = (0, 180),
    look_at_offset: tuple[float, float] = (-0.1, 0.1),
    rng: np.random.Generator = None,
) -> None:
    """Randomize the poses of cameras to look at random targets with adjustable distance and offset."""
    for cam in cameras:
        # Get a random target asset to look at
        target_asset = targets[rng.integers(len(targets))]

        # Add a look_at offset so the target is not always in the center of the camera view
        target_loc = target_asset.GetAttribute("xformOp:translate").Get()
        target_loc = (
            target_loc[0] + rng.uniform(look_at_offset[0], look_at_offset[1]),
            target_loc[1] + rng.uniform(look_at_offset[0], look_at_offset[1]),
            target_loc[2] + rng.uniform(look_at_offset[0], look_at_offset[1]),
        )

        # Generate random camera pose
        loc, quat = get_random_pose_on_sphere(target_loc, distance_range, polar_angle_range, rng=rng)

        # Set the camera's transform attributes to the generated location and orientation
        rep.functional.modify.pose(cam, position_value=loc, rotation_value=quat)

def get_usd_paths_from_folder(
    folder_path: str, recursive: bool = True, usd_paths: list[str] = None, skip_keywords: list[str] = None
) -> list[str]:
    """Retrieve USD file paths from a folder, optionally searching recursively and filtering by keywords."""
    if usd_paths is None:
        usd_paths = []
    skip_keywords = skip_keywords or []

    ext_manager = omni.kit.app.get_app().get_extension_manager()
    if not ext_manager.is_extension_enabled("omni.client"):
        ext_manager.set_extension_enabled_immediate("omni.client", True)

    result, entries = omni.client.list(folder_path)
    if result != omni.client.Result.OK:
        print(f"[SDG] Error: Could not list assets in path: {folder_path}")
        return usd_paths

    for entry in entries:
        if any(keyword.lower() in entry.relative_path.lower() for keyword in skip_keywords):
            continue
        _, ext = os.path.splitext(entry.relative_path)
        if ext in [".usd", ".usda", ".usdc"]:
            path_posix = os.path.join(folder_path, entry.relative_path).replace("\\", "/")
            usd_paths.append(path_posix)
        elif recursive and entry.flags & omni.client.ItemFlags.CAN_HAVE_CHILDREN:
            sub_folder = os.path.join(folder_path, entry.relative_path).replace("\\", "/")
            get_usd_paths_from_folder(sub_folder, recursive=recursive, usd_paths=usd_paths, skip_keywords=skip_keywords)

    return usd_paths

def get_usd_paths(
    files: list[str] = None, folders: list[str] = None, skip_folder_keywords: list[str] = None
) -> list[str]:
    """Retrieve USD paths from specified files and folders, optionally filtering out specific folder keywords."""

    def resolve_path(path: str, assets_root: str, is_folder: bool = False) -> str:
        """Resolve path to full URL: remote URLs and existing local paths used as-is, otherwise prefixed with assets_root."""
        # Remote URLs - use as-is
        if path.startswith(("omniverse://", "http://", "https://", "file://")):
            return path
        # Windows absolute path (e.g., C:\path or C:/path) - use as-is
        if len(path) > 2 and path[1] == ":" and path[2] in ("/", "\\"):
            return path
        # Local absolute path that exists - use as-is
        if path.startswith("/") and (os.path.isfile(path) or (is_folder and os.path.isdir(path))):
            return path
        # Nucleus relative path - prepend assets root
        return assets_root + path

    files = files or []
    folders = folders or []
    skip_folder_keywords = skip_folder_keywords or []

    assets_root_path = get_assets_root_path()
    env_paths = []

    for file_path in files:
        env_paths.append(resolve_path(file_path, assets_root_path, is_folder=False))

    for folder_path in folders:
        resolved_folder = resolve_path(folder_path, assets_root_path, is_folder=True)
        env_paths.extend(get_usd_paths_from_folder(resolved_folder, recursive=True, skip_keywords=skip_folder_keywords))

    return env_paths

def load_env(usd_path: str, prim_path: str, remove_existing: bool = True) -> Usd.Prim:
    """Load an environment from a USD file into the stage at the specified prim path, optionally removing any existing prim."""
    stage = omni.usd.get_context().get_stage()

    # Remove existing prim if specified
    if remove_existing and stage.GetPrimAtPath(prim_path):
        omni.kit.commands.execute("DeletePrimsCommand", paths=[prim_path])

    root_prim = add_reference_to_stage(usd_path=usd_path, prim_path=prim_path)
    return root_prim

def add_colliders_to_env(root_path: str | None = None, approximation_type: str = "none") -> None:
    """Add colliders to all mesh prims within the specified root path in the stage."""
    stage = omni.usd.get_context().get_stage()
    prim = stage.GetPseudoRoot() if root_path is None else stage.GetPrimAtPath(root_path)

    for prim in Usd.PrimRange(prim):
        if prim.IsA(UsdGeom.Mesh):
            add_colliders(prim, approximation_type)

def find_matching_prims(
    match_strings: list[str], root_path: str | None = None, prim_type: str | None = None, first_match_only: bool = False
) -> Usd.Prim | list[Usd.Prim] | None:
    """Find prims matching specified strings, with optional type filtering and single match return."""
    stage = omni.usd.get_context().get_stage()
    root_prim = stage.GetPseudoRoot() if root_path is None else stage.GetPrimAtPath(root_path)

    matching_prims = []
    for prim in Usd.PrimRange(root_prim):
        if any(match in str(prim.GetPath()) for match in match_strings):
            if prim_type is None or prim.GetTypeName() == prim_type:
                if first_match_only:
                    return prim
                matching_prims.append(prim)

    return matching_prims if not first_match_only else None

def hide_matching_prims(match_strings: list[str], root_path: str | None = None, prim_type: str | None = None) -> None:
    """Set visibility of prims matching specified strings to 'invisible' within the root path."""
    stage = omni.usd.get_context().get_stage()
    root_prim = stage.GetPseudoRoot() if root_path is None else stage.GetPrimAtPath(root_path)

    for prim in Usd.PrimRange(root_prim):
        if prim_type is None or prim.GetTypeName() == prim_type:
            if any(match in str(prim.GetPath()) for match in match_strings):
                prim.GetAttribute("visibility").Set("invisible")

def setup_env(root_path: str | None = None, approximation_type: str = "none", hide_top_walls: bool = False) -> None:
    """Set up the environment with colliders, ceiling light adjustments, and optional top wall hiding."""
    # Fix ceiling lights: meshes are blocking the light and need to be set to invisible
    ceiling_light_meshes = find_matching_prims(["001_SPLIT_GLA"], root_path, "Xform")
    for light_mesh in ceiling_light_meshes:
        light_mesh.GetAttribute("visibility").Set("invisible")

    # Hide ceiling light meshes for lighting fix
    hide_matching_prims(["001_SPLIT_GLA"], root_path, "Xform")

    # Hide top walls for better debug view, if specified
    if hide_top_walls:
        hide_matching_prims(["_exterior", "_ceiling"], root_path)

    # Add colliders to the environment
    add_colliders_to_env(root_path, approximation_type)

    # Fix dining table collision by setting it to a bounding cube approximation
    table_prim = find_matching_prims(
        match_strings=["TableDining"], root_path=root_path, prim_type="Xform", first_match_only=True
    )
    if table_prim is not None:
        add_colliders(table_prim, approximation_type="boundingCube")
    else:
        print("[SDG] Warning: Could not find dining table prim in the environment")

def create_shape_distractors(
    num_distractors: int,
    shape_types: list[str],
    root_path: str,
    gravity_disabled_chance: float,
    rng: np.random.Generator = None,
) -> tuple[list[Usd.Prim], list[Usd.Prim]]:
    """Create shape distractors with optional gravity settings, returning lists of floating and falling shapes."""
    if rng is None:
        rng = np.random.default_rng()
    stage = omni.usd.get_context().get_stage()
    floating_shapes = []
    falling_shapes = []
    for _ in range(num_distractors):
        rand_shape = shape_types[rng.integers(len(shape_types))]
        disable_gravity = rng.random() < gravity_disabled_chance
        name_prefix = "floating_" if disable_gravity else "falling_"
        prim_path = omni.usd.get_stage_next_free_path(stage, f"{root_path}/{name_prefix}{rand_shape}", False)
        prim = stage.DefinePrim(prim_path, rand_shape.capitalize())
        add_colliders(prim)
        add_rigid_body(prim, disable_gravity=disable_gravity, ensure_mass=True)
        (floating_shapes if disable_gravity else falling_shapes).append(prim)
    return floating_shapes, falling_shapes

def load_shape_distractors(
    shape_distractors_config: dict, rng: np.random.Generator = None
) -> tuple[list[Usd.Prim], list[Usd.Prim]]:
    """Load shape distractors based on configuration, returning lists of floating and falling shapes."""
    num_shapes = shape_distractors_config.get("num", 0)
    shape_types = shape_distractors_config.get("shape_types", ["capsule", "cone", "cylinder", "sphere", "cube"])
    shape_gravity_disabled_chance = shape_distractors_config.get("gravity_disabled_chance", 0.0)
    return create_shape_distractors(num_shapes, shape_types, "/Distractors", shape_gravity_disabled_chance, rng)

def create_mesh_distractors(
    num_distractors: int,
    mesh_urls: list[str],
    root_path: str,
    gravity_disabled_chance: float,
    rng: np.random.Generator = None,
) -> tuple[list[Usd.Prim], list[Usd.Prim]]:
    """Create mesh distractors from specified URLs with optional gravity settings."""
    if rng is None:
        rng = np.random.default_rng()
    stage = omni.usd.get_context().get_stage()
    floating_meshes = []
    falling_meshes = []
    for _ in range(num_distractors):
        rand_mesh_url = mesh_urls[rng.integers(len(mesh_urls))]
        disable_gravity = rng.random() < gravity_disabled_chance
        name_prefix = "floating_" if disable_gravity else "falling_"
        prim_name = os.path.basename(rand_mesh_url).split(".")[0]
        prim_path = omni.usd.get_stage_next_free_path(stage, f"{root_path}/{name_prefix}{prim_name}", False)
        try:
            prim = add_reference_to_stage(usd_path=rand_mesh_url, prim_path=prim_path)
        except Exception as e:
            print(f"[SDG] Error: Failed to load mesh distractor '{rand_mesh_url}': {e}")
            continue
        add_colliders(prim)
        add_rigid_body(prim, disable_gravity=disable_gravity, ensure_mass=True)
        (floating_meshes if disable_gravity else falling_meshes).append(prim)
    return floating_meshes, falling_meshes

def load_mesh_distractors(
    mesh_distractors_config: dict, rng: np.random.Generator = None
) -> tuple[list[Usd.Prim], list[Usd.Prim]]:
    """Load mesh distractors based on configuration, returning lists of floating and falling meshes."""
    num_meshes = mesh_distractors_config.get("num", 0)
    mesh_gravity_disabled_chance = mesh_distractors_config.get("gravity_disabled_chance", 0.0)
    mesh_folders = mesh_distractors_config.get("folders", [])
    mesh_files = mesh_distractors_config.get("files", [])
    mesh_urls = get_usd_paths(
        files=mesh_files, folders=mesh_folders, skip_folder_keywords=["material", "texture", ".thumbs"]
    )
    floating_meshes, falling_meshes = create_mesh_distractors(
        num_meshes, mesh_urls, "/Distractors", mesh_gravity_disabled_chance, rng
    )
    for prim in chain(floating_meshes, falling_meshes):
        remove_labels(prim, include_descendants=True)
    return floating_meshes, falling_meshes

def create_auto_labeled_assets(
    num_assets: int,
    asset_urls: list[str],
    root_path: str,
    regex_replace_pattern: str,
    regex_replace_repl: str,
    gravity_disabled_chance: float,
    rng: np.random.Generator = None,
) -> tuple[list[Usd.Prim], list[Usd.Prim]]:
    """Create assets with automatic labels, applying optional gravity settings."""
    if rng is None:
        rng = np.random.default_rng()
    stage = omni.usd.get_context().get_stage()
    floating_assets = []
    falling_assets = []
    for _ in range(num_assets):
        asset_url = asset_urls[rng.integers(len(asset_urls))]
        disable_gravity = rng.random() < gravity_disabled_chance
        name_prefix = "floating_" if disable_gravity else "falling_"
        basename = os.path.basename(asset_url)
        name_without_ext = os.path.splitext(basename)[0]
        label = re.sub(regex_replace_pattern, regex_replace_repl, name_without_ext)
        prim_path = omni.usd.get_stage_next_free_path(stage, f"{root_path}/{name_prefix}{label}", False)
        try:
            prim = add_reference_to_stage(usd_path=asset_url, prim_path=prim_path)
        except Exception as e:
            print(f"[SDG] Error: Failed to load asset '{asset_url}': {e}")
            continue
        add_colliders(prim)
        add_rigid_body(prim, disable_gravity=disable_gravity, ensure_mass=True)
        remove_labels(prim, include_descendants=True)
        add_labels(prim, labels=[label], instance_name="class")
        (floating_assets if disable_gravity else falling_assets).append(prim)
    return floating_assets, falling_assets

def load_auto_labeled_assets(
    auto_label_config: dict, rng: np.random.Generator = None
) -> tuple[list[Usd.Prim], list[Usd.Prim]]:
    """Load auto-labeled assets based on configuration, returning lists of floating and falling assets."""
    num_assets = auto_label_config.get("num", 0)
    gravity_disabled_chance = auto_label_config.get("gravity_disabled_chance", 0.0)
    assets_files = auto_label_config.get("files", [])
    assets_folders = auto_label_config.get("folders", [])
    assets_urls = get_usd_paths(
        files=assets_files, folders=assets_folders, skip_folder_keywords=["material", "texture", ".thumbs"]
    )
    regex_replace_pattern = auto_label_config.get("regex_replace_pattern", "")
    regex_replace_repl = auto_label_config.get("regex_replace_repl", "")
    return create_auto_labeled_assets(
        num_assets,
        assets_urls,
        "/Assets",
        regex_replace_pattern,
        regex_replace_repl,
        gravity_disabled_chance,
        rng,
    )

def create_labeled_assets(
    num_assets: int,
    asset_url: str,
    label: str,
    root_path: str,
    gravity_disabled_chance: float,
    rng: np.random.Generator = None,
) -> tuple[list[Usd.Prim], list[Usd.Prim]]:
    """Create labeled assets with optional gravity settings, returning lists of floating and falling assets."""
    if rng is None:
        rng = np.random.default_rng()
    stage = omni.usd.get_context().get_stage()
    assets_root_path = get_assets_root_path()
    asset_url = (
        asset_url
        if asset_url.startswith(("omniverse://", "http://", "https://", "file://"))
        else assets_root_path + asset_url
    )
    floating_assets = []
    falling_assets = []
    for _ in range(num_assets):
        disable_gravity = rng.random() < gravity_disabled_chance
        name_prefix = "floating_" if disable_gravity else "falling_"
        prim_path = omni.usd.get_stage_next_free_path(stage, f"{root_path}/{name_prefix}{label}", False)

        prim = add_reference_to_stage(usd_path=asset_url, prim_path=prim_path)
        add_colliders(prim)
        add_rigid_body(prim, disable_gravity=disable_gravity, ensure_mass=True)
        remove_labels(prim, include_descendants=True)
        add_labels(prim, labels=[label], instance_name="class")
        (floating_assets if disable_gravity else falling_assets).append(prim)
    return floating_assets, falling_assets

def load_manual_labeled_assets(
    manual_labeled_assets_config: list[dict], rng: np.random.Generator = None
) -> tuple[list[Usd.Prim], list[Usd.Prim]]:
    """Load manually labeled assets based on configuration, returning lists of floating and falling assets."""
    labeled_floating_assets = []
    labeled_falling_assets = []
    for labeled_asset_config in manual_labeled_assets_config:
        asset_url = labeled_asset_config.get("url", "")
        asset_label = labeled_asset_config.get("label", "")
        num_assets = labeled_asset_config.get("num", 0)
        gravity_disabled_chance = labeled_asset_config.get("gravity_disabled_chance", 0.0)
        floating_assets, falling_assets = create_labeled_assets(
            num_assets,
            asset_url,
            asset_label,
            "/Assets",
            gravity_disabled_chance,
            rng,
        )
        labeled_floating_assets.extend(floating_assets)
        labeled_falling_assets.extend(falling_assets)
    return labeled_floating_assets, labeled_falling_assets

def resolve_scale_issues_with_metrics_assembler() -> None:
    """Enable and execute metrics assembler to resolve scale issues in the stage."""
    import omni.kit.app

    ext_manager = omni.kit.app.get_app().get_extension_manager()
    if not ext_manager.is_extension_enabled("omni.usd.metrics.assembler"):
        ext_manager.set_extension_enabled_immediate("omni.usd.metrics.assembler", True)
    from omni.metrics.assembler.core import get_metrics_assembler_interface

    stage_id = omni.usd.get_context().get_stage_id()
    get_metrics_assembler_interface().resolve_stage(stage_id)

def get_matching_prim_location(match_string, root_path=None):
    """Return the translation of the first prim matching the given string."""
    prim = find_matching_prims(
        match_strings=[match_string], root_path=root_path, prim_type="Xform", first_match_only=True
    )
    if prim is None:
        print("[SDG] Warning: Could not find matching prim, returning (0, 0, 0)")
        return (0, 0, 0)
    if prim.HasAttribute("xformOp:translate"):
        return prim.GetAttribute("xformOp:translate").Get()
    elif prim.HasAttribute("xformOp:transform"):
        return prim.GetAttribute("xformOp:transform").Get().ExtractTranslation()
    else:
        print(f"[SDG] Warning: Could not find location attribute for '{prim.GetPath()}', returning (0, 0, 0)")
        return (0, 0, 0)

def offset_range(
    range_coords: tuple[float, float, float, float, float, float], offset: tuple[float, float, float]
) -> tuple[float, float, float, float, float, float]:
    """Offset the min and max coordinates of a range by the specified offset."""
    return (
        range_coords[0] + offset[0],  # min_x
        range_coords[1] + offset[1],  # min_y
        range_coords[2] + offset[2],  # min_z
        range_coords[3] + offset[0],  # max_x
        range_coords[4] + offset[1],  # max_y
        range_coords[5] + offset[2],  # max_z
    )

def randomize_poses(
    prims: list[Usd.Prim],
    location_range: tuple[float, float, float, float, float, float],
    rotation_range: tuple[float, float],
    scale_range: tuple[float, float],
    rng: np.random.Generator = None,
) -> None:
    """Randomize the location, rotation, and scale of a list of prims within specified ranges."""
    if rng is None:
        rng = np.random.default_rng()
    for prim in prims:
        rand_loc = (
            rng.uniform(location_range[0], location_range[3]),
            rng.uniform(location_range[1], location_range[4]),
            rng.uniform(location_range[2], location_range[5]),
        )
        rand_rot = (
            rng.uniform(rotation_range[0], rotation_range[1]),
            rng.uniform(rotation_range[0], rotation_range[1]),
            rng.uniform(rotation_range[0], rotation_range[1]),
        )
        rand_scale = rng.uniform(scale_range[0], scale_range[1])
        rep.functional.modify.pose(prim, position_value=rand_loc, rotation_value=rand_rot, scale_value=rand_scale)

def get_or_create_physx_scene(prim_path: str = "/PhysicsScene") -> PhysxSchema.PhysxSceneAPI:
    """Get the existing PhysX scene or create a new one at the given prim path.

    Searches the current stage for an existing UsdPhysics.Scene prim. If found, applies
    and returns the PhysxSceneAPI on it. If not found, creates a new physics scene at the
    given prim path and returns the PhysxSceneAPI.

    Args:
        prim_path: The prim path to create a new physics scene at if none exists.

    Returns:
        The PhysxSceneAPI applied to the physics scene prim.
    """
    stage = omni.usd.get_context().get_stage()
    for prim in stage.Traverse():
        if prim.IsA(UsdPhysics.Scene):
            return PhysxSchema.PhysxSceneAPI.Apply(prim)

    UsdPhysics.Scene.Define(stage, prim_path)
    return PhysxSchema.PhysxSceneAPI.Apply(stage.GetPrimAtPath(prim_path))

# Default GPU collision stack size for the infinigen SDG pipeline (300 MB).
# The PhysX default (64 MB) is insufficient for scenes with many colliders (e.g. 30+ shape
# distractors, 10+ mesh distractors, labeled assets, and environment collision meshes).
# The error message from PhysX recommends at least ~272 MB for a typical infinigen scene,
# so 300 MB provides a comfortable margin.
INFINIGEN_DEFAULT_GPU_COLLISION_STACK_SIZE = 314572800

def configure_physics_scene(physics_config: dict | None = None) -> None:
    """Configure the PhysX scene GPU memory settings for the infinigen SDG pipeline.

    This must be called before running any physics simulation. It sets the GPU collision
    stack size and other GPU memory parameters on the PhysX scene to prevent buffer overflow
    errors when simulating complex scenes with many colliders.

    Args:
        physics_config: Optional dictionary with physics configuration overrides.
            Supported keys (all optional):
            - gpu_collision_stack_size (int): GPU collision stack size in bytes.
              Defaults to INFINIGEN_DEFAULT_GPU_COLLISION_STACK_SIZE (300 MB).
            - gpu_found_lost_pairs_capacity (int): GPU found/lost pairs capacity.
            - gpu_found_lost_aggregate_pairs_capacity (int): GPU found/lost aggregate pairs capacity.
            - gpu_total_aggregate_pairs_capacity (int): GPU total aggregate pairs capacity.
            - gpu_max_rigid_contact_count (int): Maximum rigid body contact count on GPU.
            - gpu_max_rigid_patch_count (int): Maximum rigid body contact patches on GPU.
            - gpu_heap_capacity (int): GPU heap capacity in bytes.
            - gpu_temp_buffer_capacity (int): GPU temporary buffer capacity in bytes.
    """
    physics_config = physics_config or {}
    physx_scene = get_or_create_physx_scene()

    gpu_collision_stack_size = physics_config.get(
        "gpu_collision_stack_size", INFINIGEN_DEFAULT_GPU_COLLISION_STACK_SIZE
    )
    physx_scene.GetGpuCollisionStackSizeAttr().Set(gpu_collision_stack_size)

    # Apply other GPU memory settings if provided
    gpu_settings_map = {
        "gpu_found_lost_pairs_capacity": physx_scene.GetGpuFoundLostPairsCapacityAttr,
        "gpu_found_lost_aggregate_pairs_capacity": physx_scene.GetGpuFoundLostAggregatePairsCapacityAttr,
        "gpu_total_aggregate_pairs_capacity": physx_scene.GetGpuTotalAggregatePairsCapacityAttr,
        "gpu_max_rigid_contact_count": physx_scene.GetGpuMaxRigidContactCountAttr,
        "gpu_max_rigid_patch_count": physx_scene.GetGpuMaxRigidPatchCountAttr,
        "gpu_heap_capacity": physx_scene.GetGpuHeapCapacityAttr,
        "gpu_temp_buffer_capacity": physx_scene.GetGpuTempBufferCapacityAttr,
    }
    for key, attr_getter in gpu_settings_map.items():
        if key in physics_config:
            attr_getter().Set(physics_config[key])

    print(f"[SDG] Configured PhysX scene GPU collision stack size: {gpu_collision_stack_size} bytes")

def run_simulation(num_frames: int, render: bool = True) -> None:
    """Run a simulation for a specified number of frames, optionally without rendering."""
    if render:
        # Start the timeline and advance the app, this will render the physics simulation results every frame
        timeline = omni.timeline.get_timeline_interface()
        timeline.set_start_time(0)
        timeline.set_end_time(1000000)
        timeline.set_looping(False)
        timeline.play()
        for _ in range(num_frames):
            omni.kit.app.get_app().update()
        timeline.pause()
    else:
        # Run the physics simulation steps without advancing the app
        physx_scene = get_or_create_physx_scene()

        # Get simulation parameters
        physx_dt = 1 / physx_scene.GetTimeStepsPerSecondAttr().Get()
        physics_sim_interface = omni.physics.core.get_physics_simulation_interface()

        # Run physics simulation for each frame
        for _ in range(num_frames):
            physics_sim_interface.simulate(physx_dt, 0)

def register_dome_light_randomizer() -> None:
    """Register a replicator graph randomizer for dome lights using various sky textures."""
    assets_root_path = get_assets_root_path()
    dome_textures = [
        assets_root_path + "/NVIDIA/Assets/Skies/Cloudy/champagne_castle_1_4k.hdr",
        assets_root_path + "/NVIDIA/Assets/Skies/Cloudy/kloofendal_48d_partly_cloudy_4k.hdr",
        assets_root_path + "/NVIDIA/Assets/Skies/Clear/evening_road_01_4k.hdr",
        assets_root_path + "/NVIDIA/Assets/Skies/Clear/mealie_road_4k.hdr",
        assets_root_path + "/NVIDIA/Assets/Skies/Clear/qwantani_4k.hdr",
        assets_root_path + "/NVIDIA/Assets/Skies/Clear/noon_grass_4k.hdr",
        assets_root_path + "/NVIDIA/Assets/Skies/Evening/evening_road_01_4k.hdr",
        assets_root_path + "/NVIDIA/Assets/Skies/Night/kloppenheim_02_4k.hdr",
        assets_root_path + "/NVIDIA/Assets/Skies/Night/moonlit_golf_4k.hdr",
    ]
    with rep.trigger.on_custom_event(event_name="randomize_dome_lights"):
        rep.create.light(light_type="Dome", texture=rep.distribution.choice(dome_textures))

def register_shape_distractors_color_randomizer(shape_distractors: list[Usd.Prim]) -> None:
    """Register a replicator graph randomizer to change colors of shape distractors."""
    with rep.trigger.on_custom_event(event_name="randomize_shape_distractor_colors"):
        shape_distractors_paths = [prim.GetPath() for prim in shape_distractors]
        shape_distractors_group = rep.create.group(shape_distractors_paths)
        with shape_distractors_group:
            rep.randomizer.color(colors=rep.distribution.uniform((0, 0, 0), (1, 1, 1)))

def randomize_lights(
    lights: list[Usd.Prim],
    location_range: tuple[float, float, float, float, float, float] | None = None,
    color_range: tuple[float, float, float, float, float, float] | None = None,
    intensity_range: tuple[float, float] | None = None,
    rng: np.random.Generator = None,
) -> None:
    """Randomize location, color, and intensity of specified lights within given ranges."""
    if rng is None:
        rng = np.random.default_rng()
    for light in lights:
        # Randomize the location of the light
        if location_range is not None:
            rand_loc = (
                rng.uniform(location_range[0], location_range[3]),
                rng.uniform(location_range[1], location_range[4]),
                rng.uniform(location_range[2], location_range[5]),
            )
            rep.functional.modify.pose(light, position_value=rand_loc)

        # Randomize the color of the light
        if color_range is not None:
            rand_color = (
                rng.uniform(color_range[0], color_range[3]),
                rng.uniform(color_range[1], color_range[4]),
                rng.uniform(color_range[2], color_range[5]),
            )
            light.GetAttribute("inputs:color").Set(rand_color)

        # Randomize the intensity of the light
        if intensity_range is not None:
            rand_intensity = rng.uniform(intensity_range[0], intensity_range[1])
            light.GetAttribute("inputs:intensity").Set(rand_intensity)

def setup_writer(config: dict) -> None:
    """Setup a writer based on configuration settings, initializing with specified arguments."""
    writer_type = config.get("type", None)
    if writer_type is None:
        print("[SDG] Warning: No writer type specified, skipping writer setup")
        return None

    try:
        writer = rep.writers.get(writer_type)
    except Exception as e:
        print(f"[SDG] Error: Writer type '{writer_type}' not found: {e}")
        return None

    writer_kwargs = config.get("kwargs", {})
    if out_dir := writer_kwargs.get("output_dir"):
        # If not an absolute path, make path relative to the current working directory
        if not os.path.isabs(out_dir):
            out_dir = os.path.join(os.getcwd(), out_dir)
            writer_kwargs["output_dir"] = out_dir

    writer.initialize(**writer_kwargs)
    return writer
```

### Configuration Files

Example configuration files are provided in the `infinigen/config` directory. These files allow you to customize various aspects of the simulation, such as the number of captures, assets to include, randomization parameters, and writers to use.

Hereâs an example of a custom YAML configuration file that demonstrates the use of multiple writers:

Custom YAML Configuration File

```python
environments:
  # List of background environments (list of folders or files)
  folders:
    - /Isaac/Samples/Replicator/Infinigen/dining_rooms/
  files: []

capture:
  # Number of captures (frames = total_captures * num_cameras)
  total_captures: 12
  # Number of captures per environment before running the simulation (objects in the air)
  num_floating_captures_per_env: 2
  # Number of captures per environment after running the simulation (objects dropped)
  num_dropped_captures_per_env: 3
  # Number of cameras to capture from (each camera will have a render product attached)
  num_cameras: 2
  # Resolution of the captured frames
  resolution: [640, 480]
  # Disable render products throughout the pipeline, enable them only when capturing the frames
  disable_render_products: true
  # Number of subframes to render (RealTimePathTracing) to avoid temporal rendering artifacts (e.g. ghosting)
  rt_subframes: 8
  # Use PathTracing renderer instead of RealTimePathTracing when capturing the frames
  path_tracing: true
  # Offset to avoid the images always being in the image center
  camera_look_at_target_offset: 0.1
  # Distance between the camera and the target object
  camera_distance_to_target_range: [1.05, 1.25]
  # Number of scene lights to create in the working area
  num_scene_lights: 4

writers:
  # Type of the writer to use (e.g. PoseWriter, BasicWriter, etc.) and the kwargs to pass to the writer init
  - type: BasicWriter
    kwargs:
      output_dir: "_out_infinigen_basicwriter_pt"
      rgb: true
      semantic_segmentation: true
      colorize_semantic_segmentation: true
      use_common_output_dir: false
  - type: DataVisualizationWriter
    kwargs:
      output_dir: "_out_infinigen_dataviswriter_pt"
      bounding_box_2d_tight: true
      bounding_box_2d_tight_params:
        background: rgb
      bounding_box_3d: true
      bounding_box_3d_params:
        background: normals

labeled_assets:
  # Labeled assets with auto-labeling (e.g. 002_banana -> banana) using regex pattern replacement on the asset name
  auto_label:
    # Number of labeled assets to create from the given files/folders list
    num: 5
    # Chance to disable gravity for the labeled assets (0.0 - all the assets will fall, 1.0 - all the assets will float)
    gravity_disabled_chance: 0.25
    # List of folders and files to search for the labeled assets
    folders:
      - /Isaac/Props/YCB/Axis_Aligned/
    files:
      - /Isaac/Props/YCB/Axis_Aligned/036_wood_block.usd
    # Regex pattern to replace in the asset name (e.g. "002_banana" -> "banana")
    regex_replace_pattern: "^\\d+_"
    regex_replace_repl: ""

  # Manually labeled assets with specific labels and properties
  manual_label:
    - url: /Isaac/Props/YCB/Axis_Aligned/008_pudding_box.usd
      label: pudding_box
      num: 2
      gravity_disabled_chance: 0.25
    - url: /Isaac/Props/YCB/Axis_Aligned_Physics/006_mustard_bottle.usd
      label: mustard_bottle
      num: 2
      gravity_disabled_chance: 0.25

distractors:
  # Shape distractors (unlabeled background assets) to drop in the scene (e.g. capsules, cones, cylinders)
  shape_distractors:
    # Amount of shape distractors to create
    num: 30
    # Chance to disable gravity for the shape distractors
    gravity_disabled_chance: 0.25
    # List of shape types to randomly choose from
    types: ["capsule", "cone", "cylinder", "sphere", "cube"]

  # Mesh distractors (unlabeled background assets) to drop in the scene
  mesh_distractors:
    # Amount of mesh distractors to create
    num: 10
    # Chance to disable gravity for the mesh distractors
    gravity_disabled_chance: 0.25
    # List of folders and files to search to randomly choose from
    folders:
      - /Isaac/Environments/Office/Props/
    files:
      - /Isaac/Environments/Simple_Warehouse/Props/SM_CardBoxD_04_1847.usd
      - /Isaac/Environments/Simple_Warehouse/Props/SM_CardBoxA_01_414.usd
      - /Isaac/Environments/Simple_Warehouse/Props/S_TrafficCone.usd
      - /Isaac/Environments/Simple_Warehouse/Props/S_WetFloorSign.usd
      - /Isaac/Environments/Hospital/Props/SM_MedicalBag_01a.usd
      - /Isaac/Environments/Hospital/Props/SM_MedicalBox_01g.usd

# Physics GPU memory settings for the simulation
physics:
  # GPU collision stack size in bytes (300 MB, PhysX default of 64 MB overflows with many colliders)
  gpu_collision_stack_size: 314572800

# Hide ceiling, move viewport camera to top-down view above the working area
debug_mode: true
```

### Configuration Parameters

Here is an explanation of the configuration parameters:

* **environments**:

  + **folders**: List of directories containing the Infinigen environments to be used.
  + **files**: Specific USD files of environments to be loaded.
* **capture**:

  + **total\_captures**: Total number of captures to generate.
  + **num\_floating\_captures\_per\_env**: Number of captures to take before running the physics simulation (assets are floating).
  + **num\_dropped\_captures\_per\_env**: Number of captures to take after the physics simulation (assets have settled).
  + **num\_cameras**: Number of cameras to use for capturing images.
  + **resolution**: Resolution of the rendered images (width, height).
  + **disable\_render\_products**: If true, render products are disabled between captures to improve performance.
  + **rt\_subframes**: Number of subframes to render for each capture.
  + **path\_tracing**: If true, uses path tracing for rendering (higher quality, slower).
  + **camera\_look\_at\_target\_offset**: Random offset applied when cameras look at target assets.
  + **camera\_distance\_to\_target\_range**: Range of distances for cameras from the target assets.
  + **num\_scene\_lights**: Number of additional lights to add to the scene.
* **writers**: List of writers to use for data output.

  + **type**: Type of writer (e.g., BasicWriter, DataVisualizationWriter).
  + **kwargs**: Arguments specific to each writer type.
* **labeled\_assets**:

  + **auto\_label**: Configuration for automatically labeled assets.

    - **num**: Number of assets to spawn.
    - **gravity\_disabled\_chance**: Probability that an asset will have gravity disabled (will float).
    - **folders** and **files**: Sources for the asset USD files.
    - **regex\_replace\_pattern** and **regex\_replace\_repl**: Used to generate labels from file names.
  + **manual\_label**: List of assets with manually specified labels.

    - **url**: USD file path of the asset.
    - **label**: Semantic label to assign.
    - **num**: Number of instances to spawn.
    - **gravity\_disabled\_chance**: Probability of gravity being disabled.
* **distractors**:

  + **shape\_distractors**: Configuration for primitive shape distractors.

    - **num**: Number of distractors to spawn.
    - **gravity\_disabled\_chance**: Probability of gravity being disabled.
    - **types**: List of primitive shapes to use.
  + **mesh\_distractors**: Configuration for mesh distractors.

    - **num**: Number of distractors to spawn.
    - **gravity\_disabled\_chance**: Probability of gravity being disabled.
    - **folders** and **files**: Sources for the distractor USD files.
* **physics**:

  + **gpu\_collision\_stack\_size**: GPU collision stack size in bytes. The PhysX default of 64 MB is insufficient for complex Infinigen scenes with many colliders (environment meshes, distractors, labeled assets). Defaults to 300 MB (`314572800`). If PhysX reports a `collisionStackSize buffer overflow` error, increase this value to at least the size recommended in the error message.
  + Additional GPU memory settings can be configured if needed: `gpu_found_lost_pairs_capacity`, `gpu_found_lost_aggregate_pairs_capacity`, `gpu_total_aggregate_pairs_capacity`, `gpu_max_rigid_contact_count`, `gpu_max_rigid_patch_count`, `gpu_heap_capacity`, `gpu_temp_buffer_capacity`.
* **debug\_mode**: When set to true, certain elements like ceilings are hidden to provide a better view of the scene during development and debugging.

### Loading Infinigen Environments

We will load environments generated by Infinigen into the Isaac Sim stage. The environments are specified in the configuration file, either through folders or individual files.

Loading Infinigen Environments

```python
def run_sdg(config):
    # Load the config parameters
    env_config = config.get("environments", {})
    env_urls = infinigen_utils.get_usd_paths(
        files=env_config.get("files", []), folders=env_config.get("folders", []), skip_folder_keywords=[".thumbs"]
    )
    if not env_urls:
        print("[SDG] Error: No environment USD files found. Please check the 'environments' config.")
        return
    print(f"[SDG] Found {len(env_urls)} environment(s)")
```

```python
# Start the SDG loop
env_cycle = cycle(env_urls)
capture_counter = 0
while capture_counter < total_captures:
    # Load the next environment
    env_url = next(env_cycle)

    # Load the new environment
    print(f"[SDG] Loading environment: {env_url}")
    infinigen_utils.load_env(env_url, prim_path="/Environment")
```

In the above code, we use the `get_usd_paths` utility function to collect all USD files from the specified folders and files in the configuration. The `skip_folder_keywords` parameter filters out directories containing specified keywords (e.g., `.thumbs` thumbnail folders). We then cycle through these environments to load them one by one.

### Setting Up the Scene

After loading the environment, we set up the scene by:

* Hiding unnecessary elements (e.g., ceiling) for better visibility if the debugging mode is selected.
* Adding colliders to the environment for physics simulation.
* Loading labeled assets and distractors with physics properties.
* Randomizing asset poses within the working area.

Loading Assets

```python
# Load target assets with auto-labeling (e.g. 002_banana -> banana)
auto_label_config = labeled_assets_config.get("auto_label", {})
auto_floating_assets, auto_falling_assets = infinigen_utils.load_auto_labeled_assets(auto_label_config, rng)
print(f"[SDG] Loaded {len(auto_floating_assets)} floating auto-labeled assets")
print(f"[SDG] Loaded {len(auto_falling_assets)} falling auto-labeled assets")

# Load target assets with manual labels
manual_label_config = labeled_assets_config.get("manual_label", [])
manual_floating_assets, manual_falling_assets = infinigen_utils.load_manual_labeled_assets(manual_label_config, rng)
print(f"[SDG] Loaded {len(manual_floating_assets)} floating manual-labeled assets")
print(f"[SDG] Loaded {len(manual_falling_assets)} falling manual-labeled assets")
target_assets = auto_floating_assets + auto_falling_assets + manual_floating_assets + manual_falling_assets

# Load the shape distractors
shape_distractors_config = distractors_config.get("shape_distractors", {})
floating_shapes, falling_shapes = infinigen_utils.load_shape_distractors(shape_distractors_config, rng)
print(f"[SDG] Loaded {len(floating_shapes)} floating shape distractors")
print(f"[SDG] Loaded {len(falling_shapes)} falling shape distractors")
shape_distractors = floating_shapes + falling_shapes

# Load the mesh distractors
mesh_distractors_config = distractors_config.get("mesh_distractors", {})
floating_meshes, falling_meshes = infinigen_utils.load_mesh_distractors(mesh_distractors_config, rng)
print(f"[SDG] Loaded {len(floating_meshes)} floating mesh distractors")
print(f"[SDG] Loaded {len(falling_meshes)} falling mesh distractors")
mesh_distractors = floating_meshes + falling_meshes
```

Setting Up the Environment and Randomizing Poses

```python
# Setup the environment (add collision, fix lights, etc.) and update the app once to apply the changes
print(f"[SDG] Setting up the environment")
infinigen_utils.setup_env(root_path="/Environment", hide_top_walls=debug_mode)
simulation_app.update()

# Get the location of the prim above which the assets will be randomized
working_area_loc = infinigen_utils.get_matching_prim_location(
    match_string="TableDining", root_path="/Environment"
)

# Move viewport above the working area to get a top-down view of the scene
if debug_mode:
    camera_loc = (working_area_loc[0], working_area_loc[1], working_area_loc[2] + 10)
    set_camera_view(eye=np.array(camera_loc), target=np.array(working_area_loc))

# Get the spawn areas as offseted location ranges from the working area (min_x, min_y, min_z, max_x, max_y, max_z)
print(f"[SDG] Randomizing {len(target_assets)} target assets around the working area")
target_loc_range = infinigen_utils.offset_range((-0.5, -0.5, 1, 0.5, 0.5, 1.5), working_area_loc)
infinigen_utils.randomize_poses(
    target_assets,
    location_range=target_loc_range,
    rotation_range=(0, 360),
    scale_range=(0.95, 1.15),
    rng=rng,
)

# Mesh distractors
print(f"[SDG] Randomizing {len(mesh_distractors)} mesh distractors around the working area")
mesh_loc_range = infinigen_utils.offset_range((-1, -1, 1, 1, 1, 2), working_area_loc)
infinigen_utils.randomize_poses(
    mesh_distractors,
    location_range=mesh_loc_range,
    rotation_range=(0, 360),
    scale_range=(0.3, 1.0),
    rng=rng,
)

# Shape distractors
print(f"[SDG] Randomizing {len(shape_distractors)} shape distractors around the working area")
shape_loc_range = infinigen_utils.offset_range((-1.5, -1.5, 1, 1.5, 1.5, 2), working_area_loc)
infinigen_utils.randomize_poses(
    shape_distractors,
    location_range=shape_loc_range,
    rotation_range=(0, 360),
    scale_range=(0.01, 0.1),
    rng=rng,
)
```

**Explanation:**

* **Loading Assets**: Assets are loaded once at the beginning of the pipeline. The `load_auto_labeled_assets` function automatically generates labels from file names using regex patterns (e.g., `002_banana` becomes `banana`). The `load_manual_labeled_assets` function uses explicitly defined labels. Both functions return separate lists of floating (gravity disabled) and falling (gravity enabled) assets.
* **Environment Setup**: The `setup_env` utility function adds colliders to the environment and hides top walls if `debug_mode` is `true`. Hiding the top walls provides a clear view of the scene during debugging.
* **Working Area Location**: We use `get_matching_prim_location` to find the location of the dining table, which serves as our working area.
* **Randomizing Poses**: The `randomize_poses` function takes explicit `location_range`, `rotation_range`, and `scale_range` parameters. The `offset_range` helper function creates location ranges relative to the working area location.

### Creating Cameras and Render Products

We create multiple cameras to capture images from different viewpoints. Each camera is assigned a render product, which is used by Replicator writers to save data.

Creating Cameras and Render Products

```python
# Create the cameras
cameras = []
num_cameras = capture_config.get("num_cameras", 0)
rep.functional.create.scope(name="Cameras")
for i in range(num_cameras):
    cam_prim = rep.functional.create.camera(parent="/Cameras", name=f"cam_{i}", clipping_range=(0.25, 1000))
    cameras.append(cam_prim)
print(f"[SDG] Created {len(cameras)} cameras")

# Create the render products for the cameras
render_products = []
resolution = capture_config.get("resolution", (1280, 720))
disable_render_products = capture_config.get("disable_render_products", False)
for cam in cameras:
    rp = rep.create.render_product(cam.GetPath(), resolution, name=f"rp_{cam.GetName()}")
    if disable_render_products:
        rp.hydra_texture.set_updates_enabled(False)
    render_products.append(rp)
print(f"[SDG] Created {len(render_products)} render products")
```

**Explanation:**

* We use Replicatorâs `rep.functional.create.scope` to create an organizational scope for cameras.
* Cameras are created using `rep.functional.create.camera` which provides a cleaner API for camera creation with configurable clipping range.
* Render products are created using Replicatorâs `create.render_product` function.
* If `disable_render_products` is set to `true` in the configuration, we disable the render products during creation. They will be enabled only during capture to save computational resources.

### Setting Up Replicator Writers

We use multiple Replicator writers to collect and store different types of data generated during the simulation. Writers are specified in the configuration file and can include various types such as `BasicWriter`, `DataVisualizationWriter`, `PoseWriter`, and custom writers.

Setting Up Replicator Writers

```python
# Only create the writers if there are render products to attach to
writers = []
if render_products:
    for writer_config in writers_config:
        writer = infinigen_utils.setup_writer(writer_config)
        if writer:
            writer.attach(render_products)
            writers.append(writer)
            print(
                f"[SDG] {writer_config['type']}'s out dir: {writer_config.get('kwargs', {}).get('output_dir', '')}"
            )
print(f"[SDG] Created {len(writers)} writers")
```

**Explanation:**

* Writers are only created if there are render products available to attach to.
* The `setup_writer` utility function initializes writers based on the configuration, handling output directory paths and writer-specific arguments.
* Writers are attached to the render products (cameras) to capture data from the specified viewpoints.
* Multiple writers can be used simultaneously to generate different dataset types.

### Domain Randomization

To enhance the diversity of the dataset, we apply domain randomization to various elements in the scene:

* **Randomizing Object Poses**: Positions, orientations, and scales of assets are randomized within specified ranges.
* **Randomizing Lights**: Scene lights are randomized in terms of position, intensity, and color.
* **Randomizing Dome Light**: The environment dome light is randomized to simulate different lighting conditions.
* **Randomizing Shape Distractor Colors**: Colors of shape distractors are randomized to increase visual diversity.

Creating and Registering Randomizers

```python
# Create lights to randomize in the working area
scene_lights = []
num_scene_lights = capture_config.get("num_scene_lights", 0)
for i in range(num_scene_lights):
    light_prim = stage.DefinePrim(f"/Lights/SphereLight_scene_{i}", "SphereLight")
    scene_lights.append(light_prim)
print(f"[SDG] Created {len(scene_lights)} scene lights")

# Register replicator randomizers and trigger them once
print("[SDG] Registering replicator graph randomizers")
infinigen_utils.register_dome_light_randomizer()
infinigen_utils.register_shape_distractors_color_randomizer(shape_distractors)
```

Triggering Randomizations

```python
print(f"[SDG] Randomizing {len(scene_lights)} scene lights properties and locations around the working area")
lights_loc_range = infinigen_utils.offset_range((-2, -2, 1, 2, 2, 3), working_area_loc)
infinigen_utils.randomize_lights(
    scene_lights,
    location_range=lights_loc_range,
    intensity_range=(500, 2500),
    color_range=(0.1, 0.1, 0.1, 0.9, 0.9, 0.9),
    rng=rng,
)

print("[SDG] Randomizing dome lights")
rep.utils.send_og_event(event_name="randomize_dome_lights")

print("[SDG] Randomizing shape distractor colors")
rep.utils.send_og_event(event_name="randomize_shape_distractor_colors")
```

**Explanation:**

* **Scene Lights**: Additional sphere lights are created using the USD API (`stage.DefinePrim`) and stored for later randomization.
* **Randomizers Registration**: Custom Replicator graph randomizers for dome lights and shape distractor colors are registered once during setup.
* **Light Randomization**: The `randomize_lights` utility function randomizes light properties (location, intensity, color) within specified ranges.
* **Event-Based Triggering**: Randomizations are triggered using `rep.utils.send_og_event` which sends OmniGraph events to the registered randomizer graphs.

### Configuring Physics GPU Memory

Complex Infinigen scenes with many colliders (environment meshes, distractors, labeled assets) can exceed the default PhysX GPU collision stack size (64 MB), causing `PxGpuDynamicsMemoryConfig::collisionStackSize buffer overflow` errors and dropped contacts. To prevent this, we configure the PhysX scene GPU memory settings before running any simulation.

Configuring Physics Scene GPU Memory

```python
# Configure the PhysX scene GPU memory settings before running any simulation.
# This prevents PxGpuDynamicsMemoryConfig::collisionStackSize buffer overflow errors
# when simulating complex scenes with many colliders (distractors, assets, environment meshes).
physics_config = config.get("physics", {})
print("[SDG] Configuring physics scene GPU memory settings")
infinigen_utils.configure_physics_scene(physics_config)
```

**Explanation:**

* The `configure_physics_scene` utility function retrieves or creates a PhysX scene prim and sets the `gpuCollisionStackSize` attribute (and optionally other GPU memory attributes) based on values from the configuration.
* The default collision stack size is set to 300 MB (`314572800` bytes), which provides a comfortable margin above the ~272 MB typically required by Infinigen scenes. This value can be overridden via the `physics.gpu_collision_stack_size` configuration parameter.

### Running Physics Simulation

We run physics simulations to allow objects to interact naturally within the environment. This involves:

* Running a short simulation to resolve any initial overlaps.
* Capturing images before objects have settled (floating captures).
* Running a longer simulation to let objects fall and settle.
* Capturing images after objects have settled (dropped captures).

Running Physics Simulation

```python
# Run the physics simulation for a few frames to solve any collisions
print("[SDG] Fixing collisions through physics simulation")
simulation_app.update()
infinigen_utils.run_simulation(num_frames=4, render=True)

# Check if the render products need to be enabled for the capture
if disable_render_products:
    for rp in render_products:
        rp.hydra_texture.set_updates_enabled(True)

# Check if the render mode needs to be switched to path tracing for the capture
if use_path_tracing:
    print("[SDG] Switching to PathTracing render mode")
    carb.settings.get_settings().set("/rtx/rendermode", "PathTracing")

# Capture frames with the objects in the air
for i in range(num_floating_captures_per_env):
    # Check if the total captures have been reached
    if capture_counter >= total_captures:
        break
    # Randomize the camera poses
    print(f"[SDG] Randomizing camera poses ({len(cameras)} cameras)")
    infinigen_utils.randomize_camera_poses(
        cameras, target_assets, camera_distance_to_target_range, polar_angle_range=(0, 75), rng=rng
    )
    print(
        f"[SDG] Capturing floating assets {i+1}/{num_floating_captures_per_env} (total: {capture_counter+1}/{total_captures})"
    )
    rep.orchestrator.step(rt_subframes=rt_subframes, delta_time=0.0)
    capture_counter += 1

# Check if the render products need to be disabled until the next capture
if disable_render_products:
    for rp in render_products:
        rp.hydra_texture.set_updates_enabled(False)

# Check if the render mode needs to be switched back to raytracing until the next capture
if use_path_tracing:
    carb.settings.get_settings().set("/rtx/rendermode", "RealTimePathTracing")

print("[SDG] Running the simulation")
infinigen_utils.run_simulation(num_frames=200, render=False)

# Check if the render products need to be enabled for the capture
if disable_render_products:
    for rp in render_products:
        rp.hydra_texture.set_updates_enabled(True)

# Check if the render mode needs to be switched to path tracing for the capture
if use_path_tracing:
    carb.settings.get_settings().set("/rtx/rendermode", "PathTracing")

for i in range(num_dropped_captures_per_env):
    # Check if the total captures have been reached
    if capture_counter >= total_captures:
        break
    # Spawn the cameras with a smaller polar angle to have mostly a top-down view of the objects
    print("[SDG] Randomizing camera poses")
    infinigen_utils.randomize_camera_poses(
        cameras,
        target_assets,
        distance_range=camera_distance_to_target_range,
        polar_angle_range=(0, 45),
        rng=rng,
    )
    print(
        f"[SDG] Capturing dropped assets {i+1}/{num_dropped_captures_per_env} (total: {capture_counter+1}/{total_captures})"
    )
    rep.orchestrator.step(rt_subframes=rt_subframes, delta_time=0.0)
    capture_counter += 1

# Check if the render products need to be disabled until the next capture
if disable_render_products:
    for rp in render_products:
        rp.hydra_texture.set_updates_enabled(False)

# Check if the render mode needs to be switched back to raytracing until the next capture
if use_path_tracing:
    carb.settings.get_settings().set("/rtx/rendermode", "RealTimePathTracing")
```

**Explanation:**

* **Initial Simulation**: A short simulation resolves any initial overlaps among assets.
* **Render Product Management**: Render products are enabled only during capture and disabled during simulation to save computational resources.
* **Path Tracing**: When enabled, the render mode switches to PathTracing for higher quality captures and back to RealTimePathTracing during simulation.
* **Floating Captures**: We capture images while assets are still floating, with cameras positioned using larger polar angles (0-75Â°) for varied viewpoints.
* **Physics Simulation**: A longer simulation (200 frames) allows assets to fall and settle according to physics, without rendering for efficiency.
* **Dropped Captures**: We capture images after assets have settled, using smaller polar angles (0-45Â°) for mostly top-down views.
* **Capture Counter**: Each capture increments the counter, with early exit checks to respect the total capture limit.

### Capturing Data

We capture data at specified intervals, ensuring that we have a diverse set of images covering various object states and viewpoints.

* **Randomizing Camera Poses**: Cameras are positioned randomly around target assets to capture images from different angles.
* **Triggering Randomizations**: Randomizations are applied at each environment to ensure diversity.

Capturing Data Loop

```python
# Configure PhysX GPU memory once before the loop (the /PhysicsScene prim persists across environments)
physics_config = config.get("physics", {})
infinigen_utils.configure_physics_scene(physics_config)

# Start the SDG loop
env_cycle = cycle(env_urls)
capture_counter = 0
while capture_counter < total_captures:
    # Load the next environment
    env_url = next(env_cycle)

    # Load the new environment
    print(f"[SDG] Loading environment: {env_url}")
    infinigen_utils.load_env(env_url, prim_path="/Environment")

    # Setup the environment (add collision, fix lights, etc.)
    infinigen_utils.setup_env(root_path="/Environment", hide_top_walls=debug_mode)
    simulation_app.update()

    # Get the location of the working area (e.g., dining table)
    working_area_loc = infinigen_utils.get_matching_prim_location(
        match_string="TableDining", root_path="/Environment"
    )

    # Randomize poses for target assets, mesh distractors, shape distractors
    # ... (randomization code as shown in previous snippets)

    # Trigger graph-based randomizers
    rep.utils.send_og_event(event_name="randomize_dome_lights")
    rep.utils.send_og_event(event_name="randomize_shape_distractor_colors")

    # Run physics simulation and capture floating assets
    infinigen_utils.run_simulation(num_frames=4, render=True)
    for i in range(num_floating_captures_per_env):
        if capture_counter >= total_captures:
            break
        infinigen_utils.randomize_camera_poses(cameras, target_assets, ...)
        rep.orchestrator.step(rt_subframes=rt_subframes, delta_time=0.0)
        capture_counter += 1

    # Run longer simulation for dropped assets
    infinigen_utils.run_simulation(num_frames=200, render=False)
    for i in range(num_dropped_captures_per_env):
        if capture_counter >= total_captures:
            break
        infinigen_utils.randomize_camera_poses(cameras, target_assets, ...)
        rep.orchestrator.step(rt_subframes=rt_subframes, delta_time=0.0)
        capture_counter += 1

# Cleanup: wait for data, detach writers, destroy render products
rep.orchestrator.wait_until_complete()
for writer in writers:
    writer.detach()
for rp in render_products:
    rp.destroy()
print(f"[SDG] Finished, captured {capture_counter * num_cameras} frames")
```

**Explanation:**

* We loop through the environments using `cycle` to repeat environments if needed.
* The `capture_counter` is incremented inside each capture loop (floating and dropped), not at the end of the environment iteration.
* After loading each environment, we call `simulation_app.update()` to apply changes before proceeding.
* Randomizations are triggered using OmniGraph events for each environment.
* After all captures are complete, we wait for the data to be written, then properly cleanup by detaching writers and destroying render products.

## Summary

In this tutorial, you learned how to generate synthetic datasets using Infinigen environments in NVIDIA Omniverse Isaac Sim. The key steps included:

1. **Generating Infinigen Environments**: Using Infinigen to create photorealistic indoor environments.
2. **Understanding Configuration Parameters**: Customizing the simulation and data generation process through configuration files.
3. **Setting Up the Simulation**: Running Isaac Sim as a standalone application and loading Infinigen environments.
4. **Spawning Assets**: Using the Isaac Sim API to place labeled assets and distractors in the environment.
5. **Configuring the SDG Pipeline**: Creating cameras, render products, and using multiple Replicator writers to generate different datasets.
6. **Applying Domain Randomization**: Enhancing dataset diversity through randomizations.
7. **Running Physics Simulations**: Simulating object interactions for realistic scenes.
8. **Capturing and Saving Data**: Collecting images and annotations using multiple Replicator writers.

By following this tutorial, you now have the foundation to create rich, diverse synthetic datasets using procedurally generated environments and advanced randomization techniques.

## Next Steps

With the generated datasets, you can proceed to train machine learning models for tasks like object detection, segmentation, and pose estimation. Consider exploring the [TAO Toolkit](https://docs.nvidia.com/tao/) for training workflows and pre-trained models.

On this page

* [Learning Objectives](#learning-objectives)
* [Prerequisites](#prerequisites)
* [Generating Infinigen Environments](#generating-infinigen-environments)
* [Scenario Overview](#scenario-overview)
* [Getting Started](#getting-started)
* [Implementation](#implementation)
  + [Configuration Files](#configuration-files)
  + [Configuration Parameters](#configuration-parameters)
  + [Loading Infinigen Environments](#loading-infinigen-environments)
  + [Setting Up the Scene](#setting-up-the-scene)
  + [Creating Cameras and Render Products](#creating-cameras-and-render-products)
  + [Setting Up Replicator Writers](#setting-up-replicator-writers)
  + [Domain Randomization](#domain-randomization)
  + [Configuring Physics GPU Memory](#configuring-physics-gpu-memory)
  + [Running Physics Simulation](#running-physics-simulation)
  + [Capturing Data](#capturing-data)
* [Summary](#summary)
* [Next Steps](#next-steps)

---


## Pipeline

### Metropolis Pipeline

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/action_and_event_data_generation/tutorial_omni_metropolis_pipeline.html

* [Synthetic Data Generation](../synthetic_data_generation/index.html)
* [Action and Event Data Generation](index.html)
* Omni Metropolis Pipeline

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Omni Metropolis Pipeline

The `omni.metropolis.pipeline` extension provides a shared configuration, trigger, and agent layer used by Action and Event Data Generation extensions.

It supplies the **ConfigurationManager**, a singleton that loads YAML configuration files, parses sections per extension, and runs async setup so extensions can configure the application from a single config file.
It also supplies the **TriggersManager** and built-in trigger types so that events (such as those from [Physical Space Event Generation](tutorial_replicator_incident.html#isaac-sim-app-tutorial-replicator-incident)) can be started at a specific time, on a carb event, or on a physics collision.
It also supplies the **AgentManager** and base agent interface so that agents (such as those from [Actor Simulation and Synthetic Data Generation](tutorial_replicator_agent.html#isaac-sim-app-tutorial-replicator-character)) can be created and managed.

## Overview

* **Configuration** â YAML-driven application setup

  + **ConfigurationManager** â Singleton that loads a config file and dispatches sections to registered extensions. Extensions register a section parser and async setup function that are used when the config file is loaded and the simulation is set up.
* **Triggers** â event objects that run callbacks when they fire

  + **TriggersManager** â Singleton that creates and manages trigger instances from a dictionary description. Use it to create triggers in script and pass them into incident (fire, topple, spill) and other event APIs.
  + **Trigger types** â Time-based, carb-event-based, and collision-based triggers are registered by the extension at startup. Each trigger can have callbacks added using `add_callback`; when the trigger fires, all callbacks are invoked.
* **Agents** â runtime representations of entities that can perform routines and respond to triggers

  + **AgentManager** â Singleton that creates and manages agent instances from a dictionary description. Use it to create agents in script and pass them into agent APIs.
  + **Base agent interface** â The base agent interface is a USD Prim that defines the agentâs behavior and trigger. It is used to create and manage agents.

## Configuration

The **ConfigurationManager** loads a YAML config file and routes sections to extensions that have registered a parser and setup function. The config file currently supports the `isaacsim.replicator.agent` extension. Refer to the [Configuration File Guide](ext_replicator-agent/ext_isaacsim_replicator_agent_configuration.html#ira-configuration-file) for more formatting information.

### Using ConfigurationManager in Script

Access the singleton using `ConfigurationManager.get_instance()` or use the module-level functions from `omni.metropolis.pipeline.configuration`. Register your extensionâs section before loading a config file; then call `load_config_file(path)` and `await setup_simulation()`.

**Registration**

* **register\_config\_section(extension\_name, section\_header, section\_name, section\_parser, section\_setup)** â Register a config section. `section_header` is the YAML top-level key (for example, `"omni.metropolis.pipeline"` or `"isaacsim.replicator.agent.core"`). `section_name` is the key under the orchestrator header (for example, `"agent"`). `section_parser` is a callable that accepts the raw dict for that section and returns parsed data. `section_setup` is an async callable that receives the parsed payload and runs when `setup_simulation()` is called.
* **is\_section\_registered(extension\_name)** â Return whether that extension has registered a section.
* **unregister\_config\_section(extension\_name)** â Remove the registration.

**Loading and access**

* **load\_config\_file(file\_path)** â Load and parse the YAML file. Returns `True` on success. Use `get_load_error_message()` if it returns `False`.
* **get\_config(extension\_name)** â Return the parsed configuration for that extension, or `None` if not present or not loaded.
* **get\_config\_file\_path()** â Return the path of the currently loaded config file, or `None`.

**Setup**

* **setup\_simulation()** â Async. Run each registered extensionâs setup function with its parsed config. Returns `True` if all succeeded. Use `get_setup_error_message()` on failure.

### Example Usage

```python
import asyncio
from pathlib import Path
from omni.metropolis.pipeline.configuration import (
    get_config,
    get_load_error_message,
    get_setup_error_message,
    load_config_file,
    register_config_section,
    setup_simulation,
)

def parse_my_section(raw: dict):
    # Parser receives {section_header: section_data}. Return any structure your setup needs.
    return next(iter(raw.values()), {})

async def setup_my_section(parsed):
    # Run async setup using parsed config (for example, create prims, load assets).
    pass

# Register before loading. Use section_header and section_name that match your YAML.
register_config_section(
    extension_name="my.extension.name",
    section_header="my.extension.name.core",
    section_name="my_section",
    section_parser=parse_my_section,
    section_setup=setup_my_section,
)

if load_config_file(Path("/path/to/config.yaml")):
    if asyncio.run(setup_simulation()):
        config = get_config("my.extension.name")
        # Use config as needed.
    else:
        print(get_setup_error_message())
else:
    print(get_load_error_message())
```

## Triggers

### Using TriggersManager in Script

Get the manager singleton and create triggers from a dictionary. For a complete script example that creates a time trigger, adds a callback, and passes the trigger into IRI event managers (fire, topple, spill), refer to [Physical Space Event Generation](tutorial_replicator_incident.html#isaac-sim-app-tutorial-replicator-incident) and the [Event Configuration in IRI Script](tutorial_replicator_incident.html#iri-conifg-script) and [Triggers](tutorial_replicator_incident.html#iri-trigger-section) sections there.

**Prerequisites**

* Enable `isaacsim.replicator.incident.core` when using triggers with IRI events.
* The `omni.metropolis.pipeline` extension is loaded automatically when using the Action and Event Data Generation application.

### Trigger Types

The extension registers these trigger types. Use the `type` field in the trigger dictionary and the corresponding parameters. For YAML and script examples of each trigger type with IRI events, refer to [Triggers](tutorial_replicator_incident.html#iri-trigger-section) in the Physical Space Event Generation tutorial.

**time**

Fires when the simulation timeline reaches the given time (in seconds). Dictionary shape: `{"trigger": {"type": "time", "time": <seconds>}}`.

**carb\_event**

Fires when the named carb event is dispatched. Optional payload is available on the trigger after firing. Dictionary shape: `{"trigger": {"type": "carb_event", "event_name": "<event_name>"}}`.

**collision**

Fires on physics trigger enter/exit for a collider prim. The collider must have CollisionAPI, TriggerAPI, and RigidbodyAPI. Optionally filter by other collider names using the `metro:collider:name` attribute. Parameters: `collider_prim_path`, `trigger_enter`, `trigger_exit`, `other_collider_names`.

### Trigger API Summary

* **TriggersManager.get\_instance()** â Return the singleton TriggersManager.
* **create\_trigger\_by\_dict(dict\_data)** â Build a trigger from `{"trigger": {"type": "...", ...}}`. Returns a trigger instance or `None` if no registered type matches.
* **TriggerBase.add\_callback(callback\_fn)** â Add a callable that takes the trigger instance as an argument; it is invoked when the trigger fires.
* **TriggerBase.destroy()** â Unsubscribe from timeline/events and clear callbacks. Call when the trigger is no longer needed.

### Example Usage

```python
import carb
from omni.metropolis.pipeline.triggers import TriggersManager

def callback(trigger):
    carb.log_info("Trigger fired!")

# Register a callback on a time trigger that fires at 1 second
trigger_manager = TriggersManager.get_instance()
trigger = trigger_manager.create_trigger_by_dict({"trigger": {"type": "time", "time": 1.0}})
trigger.add_callback(callback)
```

## Agents

### Using AgentManager in Script

For creating and configuring agents in the Action and Event Data Generation application (YAML, UI), refer to [Actor Simulation and Synthetic Data Generation](tutorial_replicator_agent.html#isaac-sim-app-tutorial-replicator-character).

### Example Usage

The following pattern registers a custom agent class and creates a prim with the agentâs API. When the timeline plays, AgentsManager discovers the prim and instantiates the agent; when the timeline stops, runtime instances are cleared.

```python
from typing import ClassVar
from pxr import Usd, UsdPhysics
import carb
import omni.usd
import omni.timeline
from omni.metropolis.pipeline.agent import Agent, AgentsManager

class MyAgent(Agent):
    AGENT_API: ClassVar[Usd.APISchemaBase] = UsdPhysics.RigidBodyAPI

    def get_world_position(self):
        return carb.Float3(0, 0, 0)

    def get_world_rotation(self):
        return carb.Float4(0, 0, 0, 1)

    def get_speed(self):
        return 0.0

    def get_facing_direction(self):
        return carb.Float3(1, 0, 0)

    def get_current_task_name(self):
        return None

    def on_update(self, delta_time: float):
        pass  # Custom behavior each frame

# Create a prim with the agent API so the manager can discover it
stage = omni.usd.get_context().get_stage()
stage.DefinePrim("/World", "Xform")
prim = stage.DefinePrim("/World/MyAgent", "Xform")
UsdPhysics.RigidBodyAPI.Apply(prim)

# Register the agent class and play to collect runtime instances
manager = AgentsManager.get_instance()
manager.register_agent_class(MyAgent)

timeline = omni.timeline.get_timeline_interface()
timeline.play()
# After play, manager.get_runtime_agent_instances() will contain MyAgent instances
# for each prim that has RigidBodyAPI. Call timeline.stop() to clear them.
```

On this page

* [Overview](#overview)
* [Configuration](#configuration)
  + [Using ConfigurationManager in Script](#using-configurationmanager-in-script)
  + [Example Usage](#example-usage)
* [Triggers](#triggers)
  + [Using TriggersManager in Script](#using-triggersmanager-in-script)
  + [Trigger Types](#trigger-types)
  + [Trigger API Summary](#trigger-api-summary)
  + [Example Usage](#id1)
* [Agents](#agents)
  + [Using AgentManager in Script](#using-agentmanager-in-script)
  + [Example Usage](#id2)

---

### Telemetry

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/action_and_event_data_generation/tutorial_telemetry.html

* [Synthetic Data Generation](../synthetic_data_generation/index.html)
* [Action and Event Data Generation](index.html)
* Telemetry and Performance Tracking

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Telemetry and Performance Tracking

The Action and Event Data Generation extensions include built-in telemetry capabilities to track performance metrics and usage patterns. The telemetry system captures various metrics across extensions, providing valuable insights into system behavior, performance characteristics, and usage patterns.

## Overview

Telemetry in the Action and Event Data Generation ecosystem helps developers and users:

* **Monitor Performance**: Track execution times, resource usage, and system performance
* **Understand Usage Patterns**: Gain insights into how features are being used
* **Identify Issues**: Detect bottlenecks and performance problems early
* **Improve User Experience**: Use data-driven insights to optimize workflows

The telemetry system is implemented across multiple extensions and provides a standardized approach to metric collection and reporting.

Local telemetry logs can be found in the `~/.nvidia-omniverse/logs/` directory.

## Telemetry Architecture

The telemetry system is built on NVIDIA Omniverseâs structured logging framework and consists of:

* **Schema Definition**: Structured schemas defining telemetry events and their attributes
* **Event Generation**: Automated Python bindings generated from schema definitions
* **Data Collection**: Instrumented code that emits telemetry events
* **Storage and Analysis**: Events logged locally and transmitted to analysis platforms

For more details, refer to the [Omniverse Telemetry Walkthrough](https://docs.omniverse.nvidia.com/kit/docs/carbonite/latest/docs/structuredlog/Walkthrough.html).

## Telemetry Modes

The telemetry system supports different operational modes:

* **Production Mode**: `--/telemetry/mode=prod` - Default mode for production deployments.
* **Test Mode**: `--/telemetry/mode=test` - Internal mode for QA, validation, and testing.
* **Dev Mode**: `--/telemetry/mode=dev` - Internal mode for development.

Note that different modes have different data collection and transmission policies. To disable transmission or structured logging, refer to [Configuring Telemetry](#configuring-telemetry) below.

If you are running in headless mode, telemetry is disabled by default. To enable telemetry, pass `--/telemetry/mode=dev` using the application config:

```python
import os
from isaacsim import SimulationApp

base_exp_path = os.path.join(
    os.environ["EXP_PATH"],
    "isaacsim.exp.action_and_event_data_generation.base.kit"
)
app_config = {
    "headless": True,
    "width": 1920,
    "height": 1080,
    "extra_args": ["--/telemetry/mode=dev"], # Enables telemetry in dev mode
}
sim_app = SimulationApp(launch_config=app_config, experience=base_exp_path)
```

Regardless of the mode, data is saved locally to the userâs home directory in the `~/.nvidia-omniverse/logs/` directory.

## Configuring Telemetry

To disable telemetry transmission (data collection), set `--/telemetry/enableAnonymousData=false` (or 0) on the command line or in the application config. Telemetry events will still be logged locally. Alternatively, in the appâs `.kit` file, set `enableAnonymousData = false` under `[settings.telemetry]` (refer to [Data Collection & Usage](../common/data-collection.html)).

To disable all telemetry (transmission and local logging), set `--/structuredLog/enable=false` (or 0) on the command line or in the application config.

Telemetry can also be enabled or disabled at the extension level through individual `extension.toml` files.

The following extensions contain specific telemetry settings:

* `isaacsim.replicator.agent` â config at `EXTS_PATH/isaacsim.replicator.agent.core/config/extension.toml`
* `omni.metropolis.utils` â config at `EXTS_PATH/omni.metropolis.utils/config/extension.toml`

Note

`isaacsim.replicator.agent` has two parts (`isaacsim.replicator.agent.core` and `isaacsim.replicator.agent.ui`). Updating the setting in the **core** extension affects both.

`EXTS_PATH` varies by platform. For example, on **Windows** it might look like `C:\isaacsim\extscache\isaacsim.replicator.agent.core-1.x.y\config\extension.toml`; on **Linux**, like `~/isaacsim/extscache/isaacsim.replicator.agent.core-1.x.y/config/extension.toml` (version `1.x.y` might differ).

```python
[settings]
exts."isaacsim.replicator.agent".telemetry_enabled = true
```

To modify telemetry settings at runtime:

```python
import carb.settings

settings = carb.settings.get_settings()

# Enable telemetry for specific extensions
settings.set("/exts/isaacsim.replicator.agent/telemetry_enabled", True)
settings.set("/exts/omni.metropolis.utils/telemetry_enabled", True)

# Disable telemetry for specific extensions
settings.set("/exts/isaacsim.replicator.agent/telemetry_enabled", False)
settings.set("/exts/omni.metropolis.utils/telemetry_enabled", False)
```

### Available Telemetry Events

The following telemetry events are available across the Action and Event Data Generation extensions:

**omni.metropolis.utils**

* `file_read` - Tracks file read operations
* `file_write` - Tracks file write operations

**isaacsim.replicator.agent.core**

* `data_generation` - Tracks data generation operations
* `load_asset_to_scene` - Tracks asset loading events
* `stage_setup_event` - Tracks stage setup operations
* `writer_initialized_event` - Tracks writer initialization events

## Related Documentation

* [Action and Event Data Generation Overview](index.html)
* [Actor Simulation and Synthetic Data Generation](tutorial_replicator_agent.html)
* [Object Simulation and Synthetic Data Generation](tutorial_replicator_object.html)

## Additional Resources

* [Omniverse Telemetry Walkthrough](https://docs.omniverse.nvidia.com/kit/docs/carbonite/latest/docs/structuredlog/Walkthrough.html)

On this page

* [Overview](#overview)
* [Telemetry Architecture](#telemetry-architecture)
* [Telemetry Modes](#telemetry-modes)
* [Configuring Telemetry](#configuring-telemetry)
  + [Available Telemetry Events](#available-telemetry-events)
* [Related Documentation](#related-documentation)
* [Additional Resources](#additional-resources)

---

### Event Reactive Actors

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/action_and_event_data_generation/example_event_reactive_actors.html

* [Synthetic Data Generation](../synthetic_data_generation/index.html)
* [Action and Event Data Generation](index.html)
* Reacting to Events with Actor Triggers

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Reacting to Events with Actor Triggers

This example shows how Event Generation (`isaacsim.replicator.incident`) and Actor Synthetic Data Generation (SDG) (`isaacsim.replicator.agent`) can be wired together end-to-end **without writing a single line of Python**. You edit two YAML config files and drive the two extensions from their Omniverse windows.

At runtime, Event Generation fires a fire event in the warehouse, which dispatches a [carb event](https://docs.omniverse.nvidia.com/dev-guide/latest/programmer_ref/events.html); Actor SDG characters subscribe to that carb event through `event_trigger` and swap their behavior: pause briefly, walk to a safe point, stand still, and finally resume their wander routine.

## Prerequisites

* Both extensions are enabled. Refer to [Enable Extensions](tutorial_replicator_agent.html#actor-sim-enable-extensions) for the Actor SDG side; the Event Generation extension is enabled automatically by the same Action and Event Data Generation app launch.
* Familiarity with the standalone tutorials is helpful, but not required:

  + [Actor Simulation and Synthetic Data Generation](tutorial_replicator_agent.html#isaac-sim-app-tutorial-replicator-character)
  + [Physical Space Event Generation](tutorial_replicator_incident.html#isaac-sim-app-tutorial-replicator-incident)

## How the Two Extensions Connect

The two extensions have no direct API coupling. They connect through the **carb event bus** that every extension in a Kit app instance shares. Event Generation dispatches a named carb event when an incident fires, and Actor SDGâs `event_trigger` listens for that same name. A matching string is the only contract between them.

The dispatched event name is always:

```python
isaacsim.replicator.incident.core.events/<event_name>
```

Replace `<event_name>` with whatever you put under `FireEvent.name` (or `SpillEvent.name`) in the Event Generation YAML. The extension interpolates the event name into the dispatched string exactly as written. Use underscores instead of spaces; a space in `name` causes the actorâs `event_trigger` lookup to silently fail.

Only `FireEvent` and `SpillEvent` dispatch carb events. `ToppleEvent` currently signals only within Event Generation and cannot drive an actor trigger. For the complete list of trigger types incidents support (including chaining one incident from another), refer to [Triggers](tutorial_replicator_incident.html#iri-trigger-section).

## Step 1 - Author the Event Generation YAML

Save the following as `incident_config.yaml` anywhere on disk:

```python
isaacsim.replicator.incident:
  version: 0.1.0
  global:
    report_dir: ~/EventsResult
    seed: 42
  event:
    event_list:
      - FireEvent:
          name: warehouse_fire
          flammable_item:
            item: $random_flammable_item$
            flammable_nearby_radius: 1.5
          trigger:
            type: time
            time: 4
```

The `time: 4` is seconds counted from when the timeline starts playing. The extension resolves `$random_flammable_item$` at setup time by scanning the stage for prims tagged `IsaacSim_Replicator_Incident_Attr:FlammableItem`.

## Step 2 - Author the Actor SDG YAML

Save as `agent_config.yaml`. The triggerâs `event:` string must match what Step 1 dispatches exactly.

```python
isaacsim.replicator.agent:
  version: 1.6.0
  seed: 42
  simulation_duration: 25.0
  environment:
    base_stage_asset_path: Isaac/Environments/Simple_Warehouse/full_warehouse.usd
  sensor:
    groups:
      sensor_group_00:
        num: 1
        aim_at_targets: {}
  character:
    groups:
      warehouse_workers:
        num: 2
        routines:
          - wander:
              weight: 1.0
              repeat: 1
              walk:
                speed_range: [1.0, 1.0]
                distance_range: [5.0, 10.0]
                navigation_areas: []
              idle:
                - animation: idle
                  weight: 1.0
                  time_range: [3.0, 5.0]
        triggers:
          - event_trigger:
              event: isaacsim.replicator.incident.core.events/warehouse_fire
              priority: 10
              behavior:
                - stop:
                    weight: 1.0
                    repeat: 1
                    time_range: [1.0, 2.0]
                - patrol:
                    weight: 1.0
                    repeat: 1
                    speed_range: [3.0, 4.0]
                    path_points:
                      - [0.0, 0.0, 0.0]
                - stop:
                    weight: 1.0
                    repeat: 1
                    time_range: [10.0, 15.0]
  replicator:
    writers:
      IRABasicWriter:
        output_dir: ~/out_event_reactive_actors
        rgb: true
        camera_params: true
```

A few notes on this config:

* The `sensor` block creates a single placeholder camera. The trigger does not require it, but the Configuration Editor populates it by default; leaving it in place keeps the YAML round-trippable through the editor UI.
* `weight`, `repeat`, and `navigation_areas: []` are shown explicitly even though each is a default. This example surfaces them so that you can see what the Configuration Editor writes out and modify the values in place.
* The triggerâs `behavior` list runs **in order**: a brief 1-2 second stop, then a patrol to `(0, 0, 0)`, then a 10-15 second stop. After the list completes, the actor resumes its routine.

Important

Both extensions operate on whichever stage Actor SDG loads, because they share a single Kit stage. If you point Actor SDG at an untagged warehouse, Event Generation logs `'$random_flammable_item$' is not a tagged prim` and no event fires. Either tag a prim manually (Step 5) or load a pre-tagged stage such as `Isaac/Samples/Replicator/Incidents/full_warehouse_with_incident_tags.usd`.

## Step 3 - Launch the App

From the Isaac Sim install directory:

```python
./isaac-sim.action_and_event_data_generation.sh --/rtx/hydra/supportMultiTickRate=false
```

This opens `isaacsim.exp.action_and_event_data_generation.full.kit`, which enables both Actor SDG and Event Generation UIs. Two menu entries appear under **Tools > Action and Event Data Generation**:

* **Actor SDG** â Actor SDGâs config window.
* **Event Config File** â Event Generationâs config window.

Open both from the **Tools** menu and they dock side by side.

Note

The `--/rtx/hydra/supportMultiTickRate=false` override is required for fire effects
to render correctly during the `FireEvent`. Refer to
[the multi-tick rendering warning](tutorial_replicator_incident.html#iri-fire-multitick-warning)
for background and alternative ways to apply the setting.

## Step 4 - Set Up Actor SDG

In the **Actor SDG** window:

1. Click the **Select A Configuration File** field (or paste the path to `agent_config.yaml`).
2. Once the path is set, click **Set Up Simulation**.

Internally this opens the warehouse stage, instantiates two `warehouse_workers` characters with their wander routine, and attaches a carb-event listener to each character already subscribed to `isaacsim.replicator.incident.core.events/warehouse_fire`. The subscription is live before you touch anything else.

Do **not** start the timeline yet. Avoid both **Start Data Generation** and the **Play** button, because Event Generationâs time countdown begins as soon as the timeline plays. Complete Step 5 first.

## Step 5 - Set Up Event Generation

Open the **Event Config File** window from **Tools > Action and Event Data Generation > Event Config File** if it is not already open. The menu entry only appears when the `isaacsim.replicator.incident.ui` extension is enabled, which the `action_and_event_data_generation` app launched in Step 3 does automatically. Then:

1. Use the **Config File Path** picker to select `incident_config.yaml`.
2. In the **Stage** window, select any box prim on a shelf (for example, `/Root/Box_21069` from the Simple Warehouse stage).
3. In the **Property** panel for the selected prim, click **+ Add > IncidentTagging > FlammableItem > Box**.
4. Click **Set Up Incident**.

If you adapt this example to use `SpillEvent` or `ToppleEvent`, choose **LeakableItem** or **LooseItem** under **+ Add > IncidentTagging** instead, before clicking **Set Up Incident**.

Internally, Event Generation reads the YAML, waits for navmesh baking, picks the tagged prim as the flammable target, and arms a time trigger that will fire at `t = 4 s` after the timeline plays. Nothing has fired yet.

The Global sectionâs Seed field should populate to `42`, and the event list should show `warehouse_fire`.

## Step 6 - Play and Watch

You have two ways to start the simulation:

* **Play** button â in the Toolbar on the left side of the viewport. It plays the timeline only and writes no data. Useful for previewing the event and behavior sequence.
* **Start Data Generation** (**Actor SDG** window) â plays the timeline *and* runs the Replicator writers configured in the `replicator` section to capture synthetic data. `simulation_duration: 25.0` stops playback automatically when the run completes; `IRABasicWriter` output appears under `~/out_event_reactive_actors/` in your home directory.

Either way, verify that you receive:

On this page

* [Prerequisites](#prerequisites)
* [How the Two Extensions Connect](#how-the-two-extensions-connect)
* [Step 1 - Author the Event Generation YAML](#step-1-author-the-event-generation-yaml)
* [Step 2 - Author the Actor SDG YAML](#step-2-author-the-actor-sdg-yaml)
* [Step 3 - Launch the App](#step-3-launch-the-app)
* [Step 4 - Set Up Actor SDG](#step-4-set-up-actor-sdg)
* [Step 5 - Set Up Event Generation](#step-5-set-up-event-generation)
* [Step 6 - Play and Watch](#step-6-play-and-watch)

---


## 性能

### Performance Optimization

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/reference_material/sim_performance_optimization_handbook.html

* Isaac Sim Performance Optimization Handbook

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Isaac Sim Performance Optimization Handbook

## Understanding Isaac Sim Performance

The speed of the simulation can be influenced by a variety of factors. The physics step size, complexity of the scene, number of physics objects, and quantity/resolution of cameras and sensors all play a role in simulation performance. The below tips address common performance optimizations for each of these factors.

Note

The [Isaac Sim Benchmarks](benchmarks.html#isaac-sim-benchmarks-measuring-kpis) page contains common workflows to evaluate performance as well as specific optimization recommendations based on the workflow.

Note

To identify performance bottlenecks, profiling the simulation can be helpful. See [Profiling Performance Using Tracy](../utilities/debugging/profiling_performance.html#isaac-sim-app-profiling-performance) for details on using the Tracy profiler to profile the simulation.

## Physics Simulation Optimizations

1. **Physics Step Size**: The physics step size determines the time interval for each physics simulation step.

* A smaller step size will result in a more accurate simulation but will also require more computational resources and thus slow down the simulation.
* A larger step size will speed up the simulation but may result in less accurate physics.

Note

Adjust the physics step size in your script using the `SimulationManager.set_physics_dt(dt)` function, where dt is the desired step size in seconds.

2. **PhysX Minimum Frame Rate Clamp** (`--/persistent/simulation/minFrameRate`): caps how many `physics_dt` substeps PhysX will run per app update to catch up after a slow frame. The value represents the target minimum app frame rate; PhysX will not run so many catch-up substeps in one update that the effective frame rate would drop below it. This is a direct performance-vs-accuracy knob:

* **Raising the clamp** (for example to `60`) keeps the app frame rate up under load at the cost of physics-time accuracy: when an app update is slow, PhysX truncates the substep budget, so simulated time falls behind wall-clock and the simulation appears to run in slow motion (or, equivalently, some physics work is effectively dropped). Use this when responsiveness / rendering throughput matters more than 1:1 sim-time-to-wall-time playback.
* **Lowering the clamp** (for example to `15`) lets PhysX run more catch-up substeps after a slow frame, keeping simulated time closer to wall-clock at the cost of further reducing the visible frame rate. Use this when sim-time accuracy or determinism matters more than smoothness.

This setting is **not** the same as the timelineâs `targetFrameRate` (set via `isaacsim.core.rendering_manager.RenderingManager.set_dt()`) or the loop runnerâs `/app/runLoops/main/rateLimitFrequency`. See [Architecture: Timeline, Physics, and the Renderer](../sensors/isaacsim_sensors_multitick_rendering.html#isaac-sim-sensors-multitick-clock-relationships) for the three-clock architecture.

Note

Adjust the PhysX minimum frame rate clamp by modifying the `--/persistent/simulation/minFrameRate=<value>` setting, where `<value>` is the target minimum app frame rate in FPS.

3. **GPU Dynamics**: Enabling GPU dynamics can potentially speed up the simulation by offloading the physics calculations to the GPU.

Note

This will only be beneficial if your GPU is powerful enough and not already fully utilized by other tasks.
Enable or disable GPU dynamics in your script using the `SimulationManager.set_physics_sim_device(device)` function, where device is a string value of either `cuda` or `cpu`. In multi-GPU setups, a specific device can be specified by passing the device index as part of the string such as `cuda:0`.

4. **Physics Scene Complexity**: The complexity of the physics objects in the scene will heavily impact the performance of the simulation.

* Simple colliders are typically the most performant. The performance scaling is as follows:

  > + Primitive colliders (box, sphere, capsule, plane) are most performant.
  > + Convex meshes are the next most performant (Convex Hull or Convex Decomposition approximation)
  > + Cylinders are a good choice for smooth, precise rolling behavior but are more expensive than a low-vertex convex mesh approximation.
* Disable or simplify colliders that are not essential for the workflow being simulated. For example, if a robot is not expected to interact with the walls of a room, the wall colliders could be disabled while keeping the floor collider enabled.

  > + Similarly, avoid unnecessary collisions. Where possible, reduce the number of object overlaps to reduce the overhead in the collision phase of the simulation.

Note

This applies to both the scene as a whole and individual physics objects. Complex colliders on highly-articulated robots as well as many complex collision meshes on walls, tables, etc. all add to the computational cost.

5. **Adjusting PhysX Thread Count**: The number of threads used by PhysX can be adjusted to improve performance depending on the workload.

Note

This is specifically applicable for CPU-based physics simulation. Dropping thread count to 0 will run synchronously on the main thread which in some simple scenes can enable speedups. The default thread count is 8. Set the thread count using `--/persistent/physics/numThreads=<value>`.

Checkout the [Physics Simulation Performance](https://docs.omniverse.nvidia.com/kit/docs/omni_physics/latest/dev_guide/guides/physics-performance.html) guide for more optimization tricks!

## Robot Asset Optimizations

A step-by-step tutorial to optimize a sample asset is provided in [Tutorial 12: Asset Optimization](../robot_setup_tutorials/optimizing_asset.html#isaac-asset-optimization).

1. **Merge Mesh Tool**: Using the Merge Mesh tool at **Tools** > **Robotics** > **Asset Editors** > **Mesh Merge Tool** can allow for a more streamlined asset structure and reduction in total mesh count.
2. **Scenegraph Instancing**: Instancing enables shareable, referenceable prim subgraphs. Using pointers to shared reference assets can reduce total memory usage for assets with repeated, identical meshes (e.g. wheels).

   * An example of instancing is described in [Tutorial 12: Asset Optimization](../robot_setup_tutorials/optimizing_asset.html#isaac-asset-optimization). A general guide to instanceable assets can be found at [Instanceable Assets](../isaac_lab_tutorials/tutorial_instanceable_assets.html#isaac-sim-app-tutorial-instanceable-assets).

Note

Instancing inherently carries some limitations related to attributes as children cannot have modified attributes from the parent reference object.

3. **Simplify Colliders**: Colliders have high computational costs. The simpler, the collision shape, the more performant the simulation behaves.

   * A reduction in contact points brings substantial performance improvements. For wheel colliders, itâs recommended to use a simple cylinder or sphere collider instead of a mesh collider. This greatly simplifies contact with the ground plane, increasing performance and allows the robot to drive smoothly over terrain.
   * For a robot, use the simplest approximations possible that provide the needed level of precision. For example, for a mobile robot, a cube approximation is often sufficient for the body.
   * Reducing the total number of colliders is also beneficial. Consider whether every collider added to the asset needs to be enabled. Selectively disabling/enabling colliders can greatly reduce computational cost.

Note

Higher precision applications require using mesh colliders rather than simplified shapes. There are different approximations available and the choice of each one is a tradeoff between performance and precision.

4. **Disable Self Collisions**: Disabling self collisions from an Articulation Root could reduce computational load and create substantial speedups at runtime if not needed.

Note

This is highly usecase-dependent. With a complex articulated hand, self collisions are necessary to avoid interpenetrations and provide realistic collisions. For a wheeled mobile robot with some internal geometries, it is likely an unnecessary load to compute any collisions other than those with the external environment.

## Scene and Rendering Optimizations

For an overview of available renderer modes and when to use each one, see [Rendering modes](rendering_modes.html#isaac-sim-rendering-modes).

1. **Simplify the Scene**: Reducing the complexity of the scene, implementing level of detail (LOD), culling invisible objects, and optimizing the physics settings.

Note

Isaac Sim provides several tools for simplifying your scene

* [Scene Optimizer](https://docs.omniverse.nvidia.com/extensions/latest/ext_scene-optimizer.html): kit extension that performs scene optimization on the USD level
* [Mesh Merge Tool](../robot_setup/ext_isaacsim_util_merge_mesh.html#isaac-merge-mesh): Isaac Sim utility to merge multiple meshes to a single mesh

Note

During realtime simulation, the gizmos (including floor grids) automatically disappear to optimize performance. They reappear when the simulation is paused or stopped.

2. **Using RTX Real-Time 2.0**: (see [RTX - Real-Time 2.0 mode](https://docs.omniverse.nvidia.com/materials-and-rendering/latest/rtx-renderer_rt.html))

   > * RT2 is the new default rendering mode in Isaac Sim. It offers both accuracy and performance improvements over the previous RTX Real-Time mode.
   > * For training-in-the-loop or other workflows that prioritize throughput over full light transport, consider RTX - Minimal for faster performance. In standalone Python, set `renderer` to `MinimalRendering` in the `SimulationApp` launch configuration and use `minimal_shading_mode` to choose the simplified shading behavior. See [Rendering modes](rendering_modes.html#isaac-sim-rendering-modes) for mode selection guidance.
   > * The retrace threshold can be decreased to improve performance at the cost of a slightly more biased result. This will still be comparable in accuracy to the legacy RTX Real-Time mode.
   >
   >   > ```python
   >   > "--/rtx/pathtracing/cached/retrace=0.1"
   >   > ```
   > * Disabling Fractional Cutout Opacity may also improve performance at the cost of losing accuracy of translucency effects.
   >
   >   > ```python
   >   > "--/rtx/pathtracing/fractionalCutoutOpacity=false"
   >   > ```

Note

On some older hardware, specifically in the Ampere generation, performance of RT2 may fall lower than RTX Real-Time mode. Using the Retrace Threshold setting above shoud improve performance of RT2 above that of the legacy mode with comparable accuracy.

3. **Disable Materials and Lights**: (see [RT2 Mode](https://docs.omniverse.nvidia.com/materials-and-rendering/latest/rtx-renderer_rt.html) for specific RT2 and Path Tracing settings)

   > * Loading time can be drastically slowed down by a large quantity of materials in the scene. Loading materials can be disabled by setting:
   >
   >   > ```python
   >   > "--/app/renderer/skipMaterialLoading=true"
   >   > ```
   > * Disabling lights can simplify the rendering workload and improve performance.
   > * Turn off rendering features in the render settings panel (these will also have equivalent carb settings that can be set in python). There is no non-rtx rendering mode in the Isaac Sim GUI application, but you can disable almost everything (reflections, transparency, etc) to increase execution speed. To disable rendering completely unless explicitly needed by a sensor, you can use the headless application workflow.
4. **Adjust DLSS Performance Mode**: DLSS performance mode is toggled by the `--/rtx/post/dlss/execMode=<value>` setting. Values are as follows:

   > * Performance (`0`) - the most performant setting, reducing VRAM consumption and rendering time but decreasing render quality. This is the default value in Isaac Sim.
   > * Balanced (`1`) - offers both optimized performance and image quality.
   > * Quality (`2`) - offers higher image quality than balanced mode, at the cost of increased render time and VRAM consumption.
   > * Auto (`3`) - Selects the best DLSS Mode for the current output resolution. When rendering 720p cameras, Auto mode tends to select Quality, so you may see performance impacts by running in Auto mode while rendering cameras at lower resolution.

Note

The DLSS mode is currently set to `Performance` by default. `Performance` mode will yield the best performance, but may result in artifacts such as smearing when rendering cameras at lower resolutions (720p or lower).

5. **Disabling viewport updates in headless mode**: Running in headless mode with `./python.sh` still renders the default viewport. This adds the overhead of rendering a view that may not be needed.

   > * To improve performance, viewport updates can be disabled by setting the `SimulationApp` configuration parameter `disable_viewport_updates=True`.
   >
   >   > ```python
   >   > from isaacsim import SimulationApp
   >   >
   >   > simulation_app = SimulationApp({"headless": True, "disable_viewport_updates": True})
   >   > ```
   > * When not using SimulationApp, users can also disable viewport updates with the following code snippet:
   >
   >   > ```python
   >   > from omni.kit.viewport.utility import get_active_viewport
   >   >
   >   > viewport = get_active_viewport()
   >   > viewport.updates_enabled = False
   >   > ```

Note

Setting `disable_viewport_updates` in SimulationApp is only supported if running in headless mode. For streaming usecases, this option should not be used.

6. **Disabling texture streaming**: Texture streaming is a feature that helps minimize GPU memory consumption, particularly in large scenes.

   > * Disabling texture streaming can have positive performance benefits but will result in increased GPU memory consumption. Thereâs also possible negative UX impacts if memory is running low - leading to crashes or missing some textures.
   > * To disable texture streaming, modify the value of the `/rtx-transient/resourcemanager/texturestreaming/enabled` setting.
   >
   >   > ```python
   >   > "--/rtx-transient/resourcemanager/texturestreaming/enabled=false"
   >   > ```

Note

This is not recommended for all use cases. It should be used on a case-by-case basis and evaluated for each workflow to determine its suitability. This may lead to unintended rendering behavior.

## CPU Thread Count Optimizations

Three settings control the number of CPU threads used by Isaac Sim. When left unset (the default behavior), Isaac Sim will use all available threads on the system. Standalone Python workflows are limited to 32 threads by default and can be modified by changing the `limit_cpu_threads` argument in the `SimulationApp` constructor.

1. `--/plugins/carb.tasking.plugin/threadCount`: Sets Carboniteâs maximum worker thread count.
2. `--/persistent/physics/numThreads`: Sets how many Carbonite worker threads to use for physics simulation.
3. `--/plugins/omni.tbb.globalcontrol/maxThreadCount`: Sets Omniverse TBB schedulerâs maximmum worker thread count.

Spawning too many worker threads may lead to CPU bottlenecking. Consider limiting the number of CPU threads used by Isaac Sim to fewer than the number of virtual cores on the system. Current testing indicates that 32 threads is optimal for most use cases.

For example, on Ubuntu:

```python
./isaac-sim.sh --/plugins/carb.tasking.plugin/threadCount=16 --/plugins/omni.tbb.globalcontrol/maxThreadCount=16
```

Standalone Python:

```python
from isaacsim import SimulationApp

simulation_app = SimulationApp({"headless": False, "limit_cpu_threads": 16})
```

## CPU Governor Settings on Linux

CPU governors dictate the operating clock frequency range and scaling of the CPU. This can be a limiting factor for Isaac Sim performance. For maximum performance, the CPU governor should be set to `performance`. To modify the CPU governor, run the following commands:

```python
sudo apt-get install linux-tools-common
cpupower frequency-info # Check available governors
sudo cpupower frequency-set -g performance # Set governor with root permissions
```

Note

Not all governors are available on all systems. Governors enabling higher clock speed are typically more performance-centric and can yield substantially better performance for Isaac Sim.

## Asynchronous Rendering

Asynchronous rendering is a feature that allows the rendering to run in a separate thread from the simulation thread. In Isaac Sim, asynchronous rendering is enabled by default whenever Isaac Sim is in a stoppped or paused state. This greatly improves UI responsiveness and viewport FPS, particularly for complex scenes.

### Asynchronous Rendering Toggle (Default)

This is set in the isaacsim.core.throttling extension. To disable this feature in the event of unexpected behavior, set the `exts."isaacsim.core.throttling".enable_async` setting to `false` when starting the application.

```python
./isaac-sim.sh --exts."isaacsim.core.throttling".enable_async=false
```

Note

This setting is only set true when running with `isaacsim.exp.full.kit`, not when running via a Python-based workflow. It could be enabled manually using the above setting for other workflows if desired.
In certain use cases, particularly with Replicator-based SDG workflows, it may be necessary to disable asynchronous rendering to ensure proper behavior.

### Runtime Asynchronous Rendering (Experimental)

Asynchronous rendering is experimentally supported during runtime. To enable asynchronous rendering for Python-based workflows, add the below arguments to the run command. For full Isaac Sim workflows, additionally disable the toggle in the *isaacsim.core.throttling* extension so that the application will always run asynchronously.

```python
./isaac-sim.sh --exts."isaacsim.core.throttling".enable_async=false --/app/asyncRendering=true --/app/omni.usd/asyncHandshake=true --/omni/replicator/asyncRendering=true

./python.sh script.py --/app/asyncRendering=true --/app/omni.usd/asyncHandshake=true --/omni/replicator/asyncRendering=true
```

Note

This feature is experimental and may lead to unexpected behavior. Enabling this feature will not necessarily lead to performance improvements. Possible speedups will heavily vary based on the use case and hardware, but are more likely given heavily CPU-bound workflows.

## Multi-GPU Support

The following rules of thumb may help improve multi-GPU performance, based on our multi-GPU benchmarks.

Note

Exact Isaac Sim performance metrics when using multiple data-center-grade GPUs can be found [here](benchmarks.html#isaac-sim-benchmarks-gpu-dependent).

1. **Add as many GPUs as cameras being rendered - but no more.** When rendering 2 720p cameras with 2 GPUs, we saw a speed up of 72% to 89% compared to single GPU performance, but using 4 GPUs yielded only 61 - 81% improvement.
2. **Performance scales better the more cameras youâre rendering.** Our 4 camera with 4x GPUs test scaled well with an overall speed up of about 213% - 233%, but our 8 camera with 4 GPUs test scaled even better with an overall speedup of 271% - 281%.
3. **Single high-resolution cameras render faster on multiple GPUs.** An exception to our earlier rules - if you are rendering a single high-resolution (4K or higher) camera, multiple GPUs can help accelerate rendering.
4. **Increasing GPU count does not improve scene load time.** GPU count does not influence the amount of time it takes to load a USD, or the maximum USD scene size that can be loaded.
5. **GPU Physics simulation only utilizes 1 GPU.** Increasing GPU count will not improve GPU physics simulation performance.

### Disabling IOMMU On Linux

Per the [CUDA C++ Programming Guide](https://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html#iommu-on-linux), users on bare-metal Linux should disable the IOMMU to improve multi-GPU performance.

IOMMU may be disabled from system BIOS (exact instructions vary based on motherboard specification), or from the command line via:

```python
sudo bash -c 'echo GRUB_CMDLINE_LINUX="amd_iommu=off" >> /etc/default/grub'
sudo update-grub
sudo reboot
```

After rebooting, the IOMMU should be disabled.

Note

If IOMMU is enabled, you will receive a warning like `IOMMU is enabled.` below the `nvidia-smi` output in the logs when running Isaac Sim.

## Reducing GPU Memory Utilization

These are suggestions to help reduce Isaac Sim GPU memory utilization:

1. Reduce the Texture Streaming Budget. Select the `Render Settings` tab, then select the `Common` settings. Under `Debug` > `Streaming Settings`, reduce `"Texture Streaming Budget (% of GPU memory)"`. By default this value is set to **0.6**, 60% of GPU memory capacity. To reduce GPU memory consumption, the number can be reduced further. For standalone Python workflows, you can modify the value of the `/rtx-transient/resourcemanager/texturestreaming/memoryBudget` setting.
2. Reduce total rendered pixel count by turning off unnecessary viewports or reducing rendered camera resolution, if possible.

## Experimental: Reducing Potential Memory Leaks

Experimental suggestion to help reduce Isaac Sim RAM consumption in the event of memory leaks in long-running workflows:

1. Adjusting the memory allocator to reduce memory leaks in long running workflows, particularly where stages are loaded and unloaded repeatedly.
   :   * To change the allocator configuration, set the following environment variable:

         > ```python
         > export GLIBC_TUNABLES=glibc.malloc.arena_max=1:glibc.malloc.mmap_max=0:glibc.malloc.mmap_threshold=2147483647
         > ```

## Useful Tools

### Windows

Task Manager is a great resource for giving nice clean graphs and can show peak usage on a variety of system information regarding performance.

1. Click on the Start icon
2. Type âTask Managerâ
3. In Task Manager, Select the âPerformanceâ Tab

On the left side of this pane you will see various graphs like CPU, Memory and GPU. Select any of these to get a more detailed view of the data. Generally speaking if any of these are spiking and peaking out, you should look into its cause and begin to troubleshoot.

### Linux

`nvidia-smi` is a great resource for giving useful data on Linux.

See these documents for further information:

* [NVIDIA-SMI](https://developer.nvidia.com/nvidia-system-management-interface)
* [NVIDIA-SMI Documentation (PDF)](http://developer.download.nvidia.com/compute/DCGM/docs/nvidia-smi-367.38.pdf)

On this page

* [Understanding Isaac Sim Performance](#understanding-isaac-sim-short-performance)
* [Physics Simulation Optimizations](#physics-simulation-optimizations)
* [Robot Asset Optimizations](#robot-asset-optimizations)
* [Scene and Rendering Optimizations](#scene-and-rendering-optimizations)
* [CPU Thread Count Optimizations](#cpu-thread-count-optimizations)
* [CPU Governor Settings on Linux](#cpu-governor-settings-on-linux)
* [Asynchronous Rendering](#asynchronous-rendering)
  + [Asynchronous Rendering Toggle (Default)](#asynchronous-rendering-toggle-default)
  + [Runtime Asynchronous Rendering (Experimental)](#runtime-asynchronous-rendering-experimental)
* [Multi-GPU Support](#multi-gpu-support)
  + [Disabling IOMMU On Linux](#disabling-iommu-on-linux)
* [Reducing GPU Memory Utilization](#reducing-gpu-memory-utilization)
* [Experimental: Reducing Potential Memory Leaks](#experimental-reducing-potential-memory-leaks)
* [Useful Tools](#useful-tools)
  + [Windows](#windows)
  + [Linux](#linux)

---

### Rendering Modes

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/reference_material/rendering_modes.html

* Rendering modes

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Rendering modes

Isaac Sim uses the NVIDIA Omniverse RTX Renderer for viewport rendering, camera sensors, and synthetic data generation workflows. Select the render mode based on the balance you need between visual fidelity, physical accuracy, latency, and throughput.

For the complete renderer setting reference, see the [Omniverse RTX Renderer documentation](https://docs.omniverse.nvidia.com/materials-and-rendering/latest/rtx-renderer.html).

## Rendering mode overview

| Mode | Best used for | Notes | Omniverse docs |
| --- | --- | --- | --- |
| RTX - Real-Time 2.0 | Interactive simulation, robotics workflows, and synthetic data generation where real-time performance is important. | This is the default rendering mode in Isaac Sim. It uses path tracing with NVIDIA DLSS neural rendering technologies to provide a balance of fidelity and real-time performance. | [RTX - Real-Time 2.0 mode](https://docs.omniverse.nvidia.com/materials-and-rendering/latest/rtx-renderer_rt.html) |
| RTX - Interactive (Path Tracing) | High-quality still captures, validation images, and workflows that can trade performance for higher physical accuracy. | This mode accumulates samples for higher-fidelity lighting and material results. It is slower than RTX - Real-Time 2.0 and commonly requires more samples per pixel for low-noise output. | [RTX - Interactive (Path Tracing) mode](https://docs.omniverse.nvidia.com/materials-and-rendering/latest/rtx-renderer_pt.html) |
| RTX - Minimal | Training-in-the-loop and high-throughput workflows where low latency is more important than full light transport. | This mode provides simplified rendering. It disables indirect light transport and uses only the first distant light in the scene, with hard shadows. Ambient lighting can improve visibility. | [RTX - Minimal](https://docs.omniverse.nvidia.com/materials-and-rendering/latest/rtx-renderer_minimal.html) |

Common RTX renderer features, such as multi-GPU rendering, materials, light types, cameras, post-processing, volume rendering, texture streaming, and debug views, are documented in [RTX - Common](https://docs.omniverse.nvidia.com/materials-and-rendering/latest/rtx-renderer_common.html).

## Select a rendering mode

For standalone Python workflows, configure the renderer when you create `SimulationApp`:

```python
from isaacsim import SimulationApp

simulation_app = SimulationApp({"renderer": "RealTimePathTracing"})
```

Common `renderer` values include:

* `RealTimePathTracing` for RTX - Real-Time 2.0.
* `PathTracing` for RTX - Interactive (Path Tracing).
* `RaytracedLighting` for RTX Real-Time (Legacy).
* `MinimalRendering` for RTX - Minimal (`Minimal` is also accepted).

For RTX - Minimal, set `minimal_shading_mode` in the `SimulationApp` launch configuration to select the shading behavior. This option maps to `/rtx/minimal/mode`. The default is `0`. Accepted values are:

* `0` â Real-Time 2.0 (reference).
* `1` â Diffuse/Glossy/Emission.
* `2` â Textured Diffuse.
* `3` â Constant Diffuse.
* `4` â No Rendering (black color output; use when only non-color AOVs such as depth or segmentation are needed).

In the Isaac Sim GUI, you can also select RTX - Minimal from the viewport render mode menu and modify shading behavior and other settings in the Rendering Settings panel.

Call `reset_render_settings()` after opening a new stage to re-apply the launch configuration, including the renderer and minimal shading mode.

You can also change the active render mode while Isaac Sim is running by setting `/rtx/rendermode`:

```python
import carb.settings

carb.settings.get_settings().set("/rtx/rendermode", "PathTracing")
```

For RTX - Minimal at runtime, set `/rtx/rendermode` to `MinimalRendering` and adjust `/rtx/minimal/mode` as needed. Other RTX - Minimal carb settings, such as `/rtx/minimal/constantColor` and ambient light options under `/rtx/sceneDb/`, are described in [RTX - Minimal limitations](#isaac-sim-rendering-modes-minimal) and in [RTX - Minimal](https://docs.omniverse.nvidia.com/materials-and-rendering/latest/rtx-renderer_minimal.html).

## Material translucency and cutout opacity

Some vMaterials use fractional cutout opacity to render fine translucent or cutout details, such as layered composites, fabrics, glass, liquids, plastics, and stones. If this feature is disabled, these materials can render with incorrect opacity, missing cutout detail, or other translucency artifacts.

Set `/rtx/pathtracing/fractionalCutoutOpacity` to `true` when correct vMaterial appearance matters in RTX - Real-Time 2.0 or RTX - Interactive (Path Tracing):

```python
import carb.settings

settings = carb.settings.get_settings()
settings.set("/rtx/pathtracing/fractionalCutoutOpacity", True)
```

This setting can increase render cost. If the workflow does not depend on translucent or cutout material detail, disabling it can improve performance. See [Scene and Rendering Optimizations](sim_performance_optimization_handbook.html#isaac-sim-performance-optimization-handbook-scene-and-rendering) for related performance settings.

## RTX - Minimal limitations

RTX - Minimal is optimized for throughput and latency, not full lighting fidelity. Use it when simplified visual output is acceptable for the workflow.

RTX - Minimal has the following limitations:

* It disables indirect light transport.
* It uses only the first distant light source found in the scene.
* It supports hard shadows only.
* It does not reproduce all material and lighting effects available in RTX - Real-Time 2.0 or RTX - Interactive (Path Tracing).
* The `No Rendering` minimal shading mode outputs black color images and is intended for workflows that only need non-color outputs such as depth, normals, or instance segmentation.

The primary RTX - Minimal settings are `/rtx/minimal/mode`, `/rtx/minimal/constantColor`, `/rtx/sceneDb/ambientLightColor`, and `/rtx/sceneDb/ambientLightIntensity`. In standalone Python workflows, `SimulationApp` applies `/rtx/minimal/mode` from `minimal_shading_mode` when `renderer` is set to `MinimalRendering`. Use `SimulationApp.set_setting()` or carb settings directly for the other values. See [RTX - Minimal](https://docs.omniverse.nvidia.com/materials-and-rendering/latest/rtx-renderer_minimal.html) for the full setting descriptions.

## Mode selection guidance

Use RTX - Real-Time 2.0 for most interactive robotics and simulation workflows. It provides the best default balance between quality and performance.

Use RTX - Interactive (Path Tracing) when image quality and physically accurate lighting matter more than frame time. This is commonly useful for final captures, quality comparisons, and validation images.

Use RTX - Minimal when throughput or latency is the primary requirement and the workflow does not depend on full light transport, multiple light sources, or high-fidelity material appearance.

On this page

* [Rendering mode overview](#rendering-mode-overview)
* [Select a rendering mode](#select-a-rendering-mode)
* [Material translucency and cutout opacity](#material-translucency-and-cutout-opacity)
* [RTX - Minimal limitations](#rtx-minimal-limitations)
* [Mode selection guidance](#mode-selection-guidance)

---


## 参考

### Glossary

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/reference_material/reference_glossary.html

* Glossary

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Glossary

This section provides an explanation of the terms used throughout NVIDIA Isaac Sim and replicates several of the terms defined in the Omniverse Glossary.

* [Omniverse](#omniverse)

  + [Application](#application)
  + [Apps](#apps)
  + [Connectors](#connectors)
  + [Omniverse Nucleus](#omniverse-nucleus)
  + [Hub Workstation Cache](#hub-workstation-cache)
  + [Live Sync](#live-sync)
  + [Omniverse Kit](#omniverse-kit)
  + [Omniverse Launcher](#omniverse-launcher)
  + [Omniverse USD Composer](#omniverse-usd-composer)
  + [Carbonite (carb)](#carbonite-carb)
  + [RTX - Real-Time mode](#real-time-render-mode)
  + [RTX â Interactive (Path Tracing) mode](#interactive-render-mode)
  + [Extensions](#extensions)
  + [Omniverse Connect](#omniverse-connect)
* [USD](#usd)

  + [USD](#id1)
  + [MDL](#mdl)
  + [Stage](#stage)
  + [Prim](#prim)
  + [Mesh](#mesh)
  + [Shape](#shape)
  + [Reference vs Payload vs Instance](#reference-vs-payload-vs-instance)
  + [Y-Up / Z-Up](#y-up-z-up)
  + [Layer](#layer)
  + [Instance](#instance)
  + [Checkpoint](#checkpoint)
* [PhysX](#physx)
* [Isaac Sim](#isaac-sim)

  + [ROS / ROS 2](#ros-ros-2)
  + [Dynamic Control](#dynamic-control)
  + [Core API](#core-api)
  + [Riemannian Motion Policy (RMP)](#riemannian-motion-policy-rmp)
  + [World](#world)
  + [Scene](#scene)
  + [Task](#task)
  + [Articulation](#articulation)
  + [Replicator](#replicator)
  + [Synthetic Data Generation](#synthetic-data-generation)
  + [Ground Truth](#ground-truth)

## [Omniverse](#id3)

### [Application](#id4)

An Omniverse App is built upon a specific set of Extensions to provide a desired functionality. An App gives the user a customized experience by implementing the UIâs of its Extensions with a custom layout. You can quickly and easily create customized Apps comprised of any number of Extensions developed by you, the Omniverse Community or NVIDIA. An App can be as simple as a 3D viewer or as complex as an AI suite. This modular approach to building Apps makes it easy to create a customized workflow or a global scale cloud application

### [Apps](#id5)

An Omniverse App is built upon a specific set of Extensions to provide a desired functionality. An App gives the user a customized experience by implementing the UIâs of its Extensions with a custom layout. You can quickly and easily create customized Apps comprised of any number of Extensions developed by you, the Omniverse Community or NVIDIA. An App can be as simple as a 3D viewer or as complex as an AI suite. This modular approach to building Apps makes it easy to create a customized workflow or a global scale cloud application

### [Connectors](#id6)

An Omniverse Connector is middleware with which Omniverse and other software applications communicate with each other. They enable the import/export 3D assets, data, and models between different tools and workflows. Itâs important to note that this means using USD as the âgo betweenâ format to convert 3D data.

### [Omniverse Nucleus](#id7)

Omniverse Nucleus offers a set of fundamental services that allow a variety of client applications, renderers, and microservices to share and modify representations of virtual worlds.

Nucleus operates under a publish/subscribe model. Subject to access controls, Omniverse clients can publish modifications to digital assets and virtual worlds to the Nucleus Database (DB) or subscribe to their changes. Changes are transmitted in real-time between connected applications. Digital assets can include geometry, lights, materials, textures and other data that describe virtual worlds and their evolution through time.

This allows a variety of Omniverse-enabled client applications ( Apps, Connectors, and others) to share and modify authoritative representations of virtual worlds.

* See [Nucleus overview](https://docs.omniverse.nvidia.com/nucleus/latest/overview/overview.html "(in Omniverse Nucleus)") for a more in-depth look at Nucleusâs data model, architecture, and distribution platforms.

### [Hub Workstation Cache](#id8)

Hub Workstation Cache is a service that helps speed up USD workflows on your local workstation. This is a stand-alone service that runs on your local workstation and benefits Kit-based applications or Client Library tools.

Hub Workstation Cache has been performance optimized and supports storage-derived data from newer versions of Kit-based applications.

* See [Hub Workstation Cache overview](https://docs.omniverse.nvidia.com/utilities/latest/cache/hub-workstation.html "(in Omniverse Utilities)") for more details.
* See the [Workstation Installation](../installation/install_workstation.html#isaac-sim-app-install-workstation) for how to install

### [Live Sync](#id9)

Live Sync mode enables real-time âliveâ editing of shared files on a Nucleus Server. The Live Sync button is on the top-right corner of the Workspace.

### [Omniverse Kit](#id10)

NVIDIA Omniverseâ¢ Kit is a toolkit for building native Omniverse applications and microservices. It is built on a base framework known as Carbonite that provides a wide variety of functionality through a set of light-weight plugins. Carbonite plugins are all authored with C interfaces for persistent ABI compatibility. A Python interpreter is provided for scripting and customization.

NVIDIA Omniverseâ¢ Kit exposes much of its functionality through Python bindings. This provides an API that can be used to write new extensions to Omniverse Kit or new experiences for Omniverse.

* For a more in-depth look at developing in Kit, see the [Kit Programming Manual](https://docs.omniverse.nvidia.com/kit/docs/kit-manual/latest/guide/kit_overview.html "(in Omniverse Kit)").

### [Omniverse Launcher](#id11)

The NVIDIA Omniverse Launcher is your first step into the Omniverse. It provides immediate access to all the apps, connectors and other downloads within the Omniverse.

* See the [Launcher overview](https://docs.omniverse.nvidia.com/launcher/latest/index.html "(in Omniverse Launcher)") for more details.

### [Omniverse USD Composer](#id12)

NVIDIA Omniverseâ¢ USD Composer was an Omniverse app for world-building that allows users to assemble, light, simulate and render large scale scenes. It is built using NVIDIA Omniverseâ¢ Kit. The Scene Description and in-memory model is based on Pixarâs USD. USD Composer takes advantage of the advanced workflows of USD like Layers, Variants, Instancing and much more.

### [Carbonite (carb)](#id13)

The Carbonite SDK provides the core functionality of all Omniverse apps. This is a C++ based SDK with Python bindings that provides features such as plugin management, input handling, file access, asset loading and management, thread and task management, and much more.

### [RTX - Real-Time mode](#id14)

High quality real-time rendering mode.

### [RTX â Interactive (Path Tracing) mode](#id15)

The highest quality, physically accurate rendering mode.

### [Extensions](#id16)

Extensions are plug-ins to Omniverse Kit that extend its capabilities. They are offered with complete source code to help developers easily create, add, and modify the tools and workflows they need to be productive. Extensions are the core building blocks of Omniverse Kit based applications.

* See [Extension Manager](https://docs.omniverse.nvidia.com/extensions/latest/ext_core/ext_extension-manager.html "(in Omniverse Extensions)") for more details.

### [Omniverse Connect](#id17)

Connectors are extensions and additional software layers on top of the open-source USD distribution that allow DCC tools and compute services to communicate easily with each other through the Omniverse Nucleus DB. Those extensions and additions are collectively known as NVIDIA Omniverseâ¢ Connect.

## [USD](#id18)

### [USD](#id19)

Universal Scene Description (USD) is an easily extensible, open-source 3D scene description file format developed by Pixar for content creation and interchange among different tools. As a result of its power and versatility, itâs being widely adopted, not only in the visual effects community, but also in architecture, design, robotics, manufacturing, and other disciplines.

* For a more in-depth look at USD in Omniverse, see NVIDIAâs USD primer [What is USD?](https://developer.nvidia.com/usd/).
* See the [USD API](https://graphics.pixar.com/usd/release/index.html) docs for more details.
* See the [USD Glossary of Terms & Concepts](https://graphics.pixar.com/usd/release/glossary.html) for more details.
* See [NVIDIAâs USD tutorials](https://developer.nvidia.com/usd/tutorials)

### [MDL](#id20)

Material Definition Language (MDL) is a NVIDIA-developed USD schema that represents material assignments and specifies material parameters.

### [Stage](#id21)

The Omniverse Stage window allows you to see all the assets in your current USD Scene. The [USD Stage](https://graphics.pixar.com/usd/release/glossary.html#usdglossary-stage) is the USD abstraction for a scenegraph derived from a root USD file, and all of the referenced/layered files it composes. Listed in a hierarchical (parent/child) order the Stage offers convenient access and is typically used to navigate large scenes.

* See the [Stage](https://docs.omniverse.nvidia.com/extensions/latest/ext_core/ext_stage.html "(in Omniverse Extensions)") docs for more details.
* See the [USD Glossary of Terms & Concepts](https://graphics.pixar.com/usd/release/glossary.html) for more details.

### [Prim](#id22)

A [Prim](https://graphics.pixar.com/usd/release/glossary.html#usdglossary-prim) is the primary container object in USD: prims can contain (and order) other prims, creating a ânamespace hierarchyâ on a Stage,
and prims can also contain (and order) properties that hold meaningful data. Prims, along with their associated, computed indices, are
the only persistent scenegraph objects that a Stage retains in memory, and the API for interacting with prims is provided by the UsdPrim class.

* See the [USD Glossary of Terms & Concepts](https://graphics.pixar.com/usd/release/glossary.html) for more details.

### [Mesh](#id23)

A mesh is a subdividable primitive that consists of points, edges, and faces that define its shape. In USD, a mesh is encoded in a [UseGeomMesh](https://graphics.pixar.com/usd/release/api/class_usd_geom_mesh.html) class.

### [Shape](#id24)

A Shape is a geometric primitive that maps to one of USDâs five âintrinsicâ `UsdGeomGprim` classes:

> * [UsdGeomCapsule](https://graphics.pixar.com/usd/release/api/class_usd_geom_capsule.html)
> * [UsdGeomCone](https://graphics.pixar.com/usd/release/api/class_usd_geom_cone.html)
> * [UsdGeomCube](https://graphics.pixar.com/usd/release/api/class_usd_geom_cube.html)
> * [UsdGeomCylinder](https://graphics.pixar.com/usd/release/api/class_usd_geom_cylinder.html)
> * [UsdGeomSphere](https://graphics.pixar.com/usd/release/api/class_usd_geom_sphere.html)

Shapes are not [meshes](https://docs.omniverse.nvidia.com/utilities/latest/common/glossary-of-terms.html#term-Mesh "(in Omniverse Utilities)"), in that they are not defined by a collection of points, edges, and faces. Instead, they are defined by their shape and volume.

Pixar describes their use cases for these prims in their [UsdGeomGprim schema documentation](https://graphics.pixar.com/usd/release/api/usd_geom_page_front.html).

### [Reference vs Payload vs Instance](#id25)

Everything in USD is a primitive (prim) with attributes. Some of these primitives are defined in your current layer (the active stage), while others are defined in other layers (other USD files).

A primitive that is included from some other layer is a **Reference** to that prim, and are indicated by the **orange arrow** on the associated Xform icon in the context tree of Isaac Sim. References are designed to be lightweight, and carry with them an implicit assumption that the child prims of a reference will not be modified.

If the contents of a reference need to be modified during simulation, then it must be converted into a **Payload**. A payload is indicated by the **blue arrow** on the associated Xform in the context tree of Isaac Sim. Payloads are references that have all of their data actively loaded by the sim so that it can be modified at runtime.

**Instances** are indicated by a **blue âIâ**, and can be either references or payloads. They carry additional assumptions about the structure of the asset for more efficient vectorization (scaled up).

For example, suppose you want to collect synthetic data with a robot. If you arenât going to modify the structure of the robot, it can exist as a reference on the stage (the asset is defined in some other file). If, during data collection, you want to be able to swap the robot out for a different one, those meshes need to be held in active memory. This means that the asset first needs to be converted from a reference to a payload. If you wanted to collect data with a 1000 robots at once, and they are all the same, you might use instantiable references. Whereas, if you wanted to collect data with a 1000 randomly sampled robots (different arms with the same number of joints for example), you would use instance payloads.

### [Y-Up / Z-Up](#id26)

The axis of orientation of a given scene/prim. Y-Up refers to the Positive Y Axis is pointing up. Z-Up refers to the Positive Z Axis is pointing up. This orientation setting is generally set by the application of the scene/prims origination.

### [Layer](#id27)

A component of the collaborative nature of USD. Each layer in USD signifies a userâs âopinionâ on assets inside a stage. Layers can override other layers.

### [Instance](#id28)

A light-weight and less manipulable copy of a prim.

### [Checkpoint](#id29)

Immutable historical file versions. Checkpoints are used for version control and allow you to look at and restore the stage to a previous state.

## [PhysX](#id30)

NVIDIA PhysX is a scalable multi-platform physics simulation solution.
The NVIDIA Omniverseâ¢ Physics simulation extension is powered by the NVIDIA PhysX SDK, and includes
Rigid Body Simulation, Articulations, Deformable-Body Simulation, and Character Controller.

* See [Physics Core](https://docs.omniverse.nvidia.com/kit/docs/omni_physics/latest/index.html "(in Omni Physics)") for more details.

## [Isaac Sim](#id31)

### [ROS / ROS 2](#id32)

The [Robot Operating System (ROS)](https://www.ros.org/) is a set of software libraries and tools that help you build robot applications.
NVIDIA Isaac Sim provides many extensions, examples, and APIs for connecting to ROS and ROS 2 workflows.

### [Dynamic Control](#id33)

The Dynamic Control extension a set of utilities to control physics objects. It provides opaque handles for different physics objects that remain valid between PhysX scene resets, which occur whenever play or stop is pressed.

* See the [API Documentation](../py/source/deprecated/omni.isaac.dynamic_control/docs/index.html) documentation for full usage examples and API details.

Note

omni.isaac.dynamic\_control is deprecated.

### [Core API](#id34)

Important

Isaac Sim 5.0.0 has introduced the [Core Experimental API](../py/docs/overview/experimental.html): a rewritten implementation of the current Core API
designed to be more robust, flexible, and powerful, yet still maintain the core utilities and wrapper concepts.

Going forward, it will become the base API used in all Isaac Sim source code.
The current Core API will be deprecated and removed in future releases.

Therefore, **we strongly encourage early adoption and use of the Core Experimental API**.

The Isaac Core Extension in Isaac Sim provides high-level interfaces to PhysX and raw USD APIs. It abstracts away default parameters to simplify creation and manipulation of a simulated world
and scenarios encountered in robotics simulators. Specifically, the extension allows for

> 1. easy creation, manipulation, and management of the world, all its time-related events, and related physical and numerical parameters
> 2. creation of various robotic tasks and controllers
> 3. vectorized manipulation of reinforcement learning environments through various view classes such as `ArticulationView`, `RigidPrimView`, `XFormPrimView`, which provide high-level functionalities to manipulate in parallel sets of articulations, rigid prims, and xforms, respectively.

* See the [API Documentation](../py/source/extensions/isaacsim.core.api/docs/index.html) documentation for full usage examples and API details.

### [Riemannian Motion Policy (RMP)](#id35)

Riemannian Motion Policy (RMP) is a set of motion generation tools that underlies most of our manipulator controls inside Omniverse Isaac Sim. It creates smooth trajectories for the robots with intelligent collision avoidance.

* See the [Motion Generation](../manipulators/concepts/index.html#isaac-sim-motion-generation) documentation for more details and examples.

### [World](#id36)

World is the core class that enables you to interact with the simulator in an easy and modular way. It takes care of many time-related events such as adding callbacks, stepping physics, resetting the scene, adding tasks, etc. The World class is a Singleton which means only one World can exist while running Omniverse Isaac Sim. Query the World for information about the simulation from different extensions.

### [Scene](#id37)

A world contains an instance of a Scene, think about it as a scene management class that manages the assets of interest in the USD stage. It provides an easy API to add, manipulate and inspect different USD assets in the stage as well as setting its default reset states. Many of the object classes available which could be added to a Scene usually takes an already existing USD prim in stage or creates a new USD prim, thus providing an easy way to set/ get its common properties.

### [Task](#id38)

The Task class in `isaacsim.core.api` provides a way to modularize the scene creation, information retrieval, calculating metrics and creating more complex scenes with more involved logic.

### [Articulation](#id39)

An articulated robot is a robot with rotary joints (e.g: a legged robot, a manipulator or a wheeled robot). In `isaacsim.core.api` extension in NVIDIA Isaac Sim there exists an Articulation class which enables the interaction with articulations that exists in a USD stage in an easy way.

### [Replicator](#id40)

Replicator is a Synthetic Data Generation tool for creating parameterizable offline datasets in NVIDIA Isaac Sim.

* See the [omni.replicator extension documentation](https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator.html "(in Omniverse Extensions)") for additional usage information.

### [Synthetic Data Generation](#id41)

NVIDIA Isaac Sim supports Synthetic Data Generations workflows. See [Replicator](#isaac-sim-glossary-replicator) for more details.

### [Ground Truth](#id42)

NVIDIA Isaac Sim can be used to generate ground truth data that is very similar to real-life analogs. See [Replicator](#isaac-sim-glossary-replicator) for more details.

On this page

* [Omniverse](#omniverse)
  + [Application](#application)
  + [Apps](#apps)
  + [Connectors](#connectors)
  + [Omniverse Nucleus](#omniverse-nucleus)
  + [Hub Workstation Cache](#hub-workstation-cache)
  + [Live Sync](#live-sync)
  + [Omniverse Kit](#omniverse-kit)
  + [Omniverse Launcher](#omniverse-launcher)
  + [Omniverse USD Composer](#omniverse-usd-composer)
  + [Carbonite (carb)](#carbonite-carb)
  + [RTX - Real-Time mode](#real-time-render-mode)
  + [RTX â Interactive (Path Tracing) mode](#interactive-render-mode)
  + [Extensions](#extensions)
  + [Omniverse Connect](#omniverse-connect)
* [USD](#usd)
  + [USD](#id1)
  + [MDL](#mdl)
  + [Stage](#stage)
  + [Prim](#prim)
  + [Mesh](#mesh)
  + [Shape](#shape)
  + [Reference vs Payload vs Instance](#reference-vs-payload-vs-instance)
  + [Y-Up / Z-Up](#y-up-z-up)
  + [Layer](#layer)
  + [Instance](#instance)
  + [Checkpoint](#checkpoint)
* [PhysX](#physx)
* [Isaac Sim](#isaac-sim)
  + [ROS / ROS 2](#ros-ros-2)
  + [Dynamic Control](#dynamic-control)
  + [Core API](#core-api)
  + [Riemannian Motion Policy (RMP)](#riemannian-motion-policy-rmp)
  + [World](#world)
  + [Scene](#scene)
  + [Task](#task)
  + [Articulation](#articulation)
  + [Replicator](#replicator)
  + [Synthetic Data Generation](#synthetic-data-generation)
  + [Ground Truth](#ground-truth)

---

