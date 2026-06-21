# SDG Workflows

> 合成数据生成工作流：Object-Based / Scene-Based / Grab / Mobility / Teleop
> Isaac Sim 版本: 6.0
> 最后组装: 2026-06-21 13:05 UTC
> 来源页数: 9

---

## 来源链接

- [SDG Index](https://docs.isaacsim.omniverse.nvidia.com/latest/synthetic_data_generation/index.html)
- [SDG Workflows](https://docs.isaacsim.omniverse.nvidia.com/latest/replicator_tutorials/tutorial_replicator_sdg_workflows.html)
- [Object-Based SDG](https://docs.isaacsim.omniverse.nvidia.com/latest/replicator_tutorials/tutorial_replicator_object_based_sdg.html)
- [Scene-Based SDG](https://docs.isaacsim.omniverse.nvidia.com/latest/replicator_tutorials/tutorial_replicator_scene_based_sdg.html)
- [Grasping SDG](https://docs.isaacsim.omniverse.nvidia.com/latest/synthetic_data_generation/tutorial_replicator_grasping_sdg.html)
- [Mobility Gen](https://docs.isaacsim.omniverse.nvidia.com/latest/synthetic_data_generation/tutorial_replicator_mobility_gen.html)
- [Teleop SDG](https://docs.isaacsim.omniverse.nvidia.com/latest/synthetic_data_generation/tutorial_replicator_teleop_sdg.html)
- [AMR Navigation](https://docs.isaacsim.omniverse.nvidia.com/latest/replicator_tutorials/tutorial_replicator_amr_navigation.html)
- [UR10 Palletizing](https://docs.isaacsim.omniverse.nvidia.com/latest/replicator_tutorials/tutorial_replicator_ur10_palletizing.html)

---


## SDG

### SDG Index

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/synthetic_data_generation/index.html

* Synthetic Data Generation

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Synthetic Data Generation

Synthetic Data Generation (SDG) is a collection of tools and workflows for generating synthetic data in Isaac Sim.

* [Perception Data Generation (Replicator)](../replicator_tutorials/index.html)
* [Action and Event Data Generation](../action_and_event_data_generation/index.html)
* [Grasping Synthetic Data Generation](tutorial_replicator_grasping_sdg.html)
* [Data Generation with MobilityGen](tutorial_replicator_mobility_gen.html)
* [Teleoperation Synthetic Data Generation](tutorial_replicator_teleop_sdg.html)

---

### SDG Workflows

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/replicator_tutorials/tutorial_replicator_sdg_workflows.html

* [Synthetic Data Generation](../synthetic_data_generation/index.html)
* [Perception Data Generation (Replicator)](index.html)
* SDG Workflows

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# SDG Workflows

This tutorial walks through two complete synthetic data generation (SDG) scripts. Each script authors a USD scene, randomizes it, runs the simulation, and writes annotated images to disk through a `BasicWriter`. The two scripts share the same setup code but solve different problems: the first reuses one persistent scene and settles physics between captures, the second rebuilds the scene on a cadence and places assets with collision checks.

This tutorial is for developers who are comfortable with rigid-body simulation and USD scene graphs and want to see the Replicator API used end to end. By the end you will recognize the settings every SDG script configures at startup, the capture loop pattern both workflows follow, and the gotchas that produce corrupt or low-quality datasets.

## Prerequisites

Before starting, make sure you have:

* Read [Getting Started Scripts](tutorial_replicator_getting_started.html#isaac-sim-app-tutorial-replicator-getting-started). It introduces the orchestrator step, the capture-on-play flag, `rt_subframes`, `wait_for_render`, `wait_until_complete`, and DLSS quality mode one concept at a time. This tutorial assumes you know what each one does.
* Familiarity with USD (Universal Scene Description) concepts: prims, scopes, references, and transforms.
* A working Isaac Sim install you can run as a [Standalone Application](../introduction/workflows.html#standalone-application) or through the [Script Editor](../development_tools/omniverse_script_editor.html#script-editor).
* Enough disk space for the captured dataset (scales with resolution and frame count).

## Setup and Configuration

Both scripts run the same startup sequence before the capture loop. Each setting below shows the API call, why the workflows use it, and the effect of omitting it. The excerpts come from the example scripts shown later.

## Writers and Backends

A *writer* formats annotator output (RGB, depth, segmentation, bounding boxes, and so on) and hands it to a *backend* that performs the I/O. Both workflows attach the built-in `BasicWriter` to a `DiskBackend` and request RGB and colorized semantic segmentation:

```python
backend = rep.backends.get("DiskBackend")
backend.initialize(output_dir=out_dir)
writer = rep.writers.get("BasicWriter")
writer.initialize(
    backend=backend,
    rgb=True,
    semantic_segmentation=True,
    colorize_semantic_segmentation=True,
)
writer.attach(rp)
```

`attach` connects the writer to one or more render products. After this call, every orchestrator step routes that render productâs annotator data through the writer. Each annotator you enable (`rgb`, `semantic_segmentation`, and so on) adds GPU and I/O cost, so enable only what your dataset needs.

Replicator ships other built-in writers, for example `PoseWriter` (6-DoF object pose data) and `CosmosWriter` (multi-modal training data for [NVIDIA Cosmos](https://www.nvidia.com/en-us/ai/cosmos/)). To emit any other format, register a [custom writer](https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator/custom_writer.html "(in Omniverse Extensions)"). See [writer examples](https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator/writer_examples.html "(in Omniverse Extensions)") for the full list and [annotators](https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator/annotators_details.html "(in Omniverse Extensions)") for the data sources writers can consume.

## Capture on Play Flag

By default Replicator captures a frame every time the timeline ticks. Both workflows capture data at specific timepoints rather than continuously, so they disable this flag once at startup and trigger each capture explicitly:

```python
rep.orchestrator.set_capture_on_play(False)
```

After this call the writer receives only frames produced by an explicit `step()` (or `step_async`). This lets Workflow 1 advance several physics frames between captures without recording any of them.

## Orchestrator Step

`rep.orchestrator.step()` (`step_async()` in the Script Editor) captures and processes one frame for the attached writers and annotators. Each workflow calls it once per capture. Its parameters are:

```python
rep.orchestrator.step(rt_subframes=-1, pause_timeline=True, delta_time=None, wait_for_render=True)
```

* `rt_subframes` - number of subframes rendered before the frame is captured, covered in [RT Subframes](#isaac-sim-app-tutorial-replicator-sdg-workflows-rt-subframes) below.
* `pause_timeline` - pause the timeline after the step. Defaults to `True`
* `delta_time` - how far the timeline advances during the step. `None` (default) advances by the timelineâs rate, `0.0` does not advance the timeline, and a positive value advances by that amount.
* `wait_for_render` - block until the frame finishes rendering. Defaults to `True`. Set it to `False` to let the next randomization start while the previous frame is still rendering, when exact frame-to-state correspondence is not required.

## RT Subframes

`rt_subframes` is the number of times the renderer produces the *same* logical frame before the writer reads its annotators. The simulation is paused during subframe generation. The default is `-1` (use the global `/omni/replicator/RTSubframes` carb setting); per-step values must be greater than `0`. Both workflows pass `rt_subframes=8` because they teleport the camera and randomize materials between captures.

Increase it when:

* The camera or props moved a lot between two captures (DLSS ghosting; faint trails or blurred silhouettes from the previous frame).
* Lights, textures, or MDL materials changed between captures (newly assigned materials need a few frames to fully load and resolve in the render graph).
* Path tracing is enabled or the scene is dimly lit.

Use `rt_subframes=1` only when nothing is changing between captures.

## DLSS Quality Mode

Isaac Sim ships with the DLSS denoiser in Performance mode (`execMode=0`). At common SDG resolutions the performance modes can produce visible ghosting around moving edges and incorrect transparency on thin geometry. Both workflows switch DLSS to Quality mode once at startup:

```python
import carb.settings

carb.settings.get_settings().set("rtx/post/dlss/execMode", 2)
```

Available values: `0` Performance, `1` Balanced, `2` Quality, `3` Auto.

## Render Product Updates

A render product ties a camera to the rendering and annotation graph (ray tracing, denoising, segmentation, bounding boxes, etc.). Once created, it keeps rendering on every application tick even when `step()` is not called. This wastes GPU time during physics, scene construction, and randomization.

The pattern both scripts use is to disable updates immediately after the render product is created and re-enable them only around the orchestrator step:

```python
rp = rep.create.render_product(cam, RESOLUTION, name="rp_workflow_01")
rp.hydra_texture.set_updates_enabled(False)

# ... scene updates, physics, randomization (no rendering cost) ...

rp.hydra_texture.set_updates_enabled(True)
rep.orchestrator.step(delta_time=0.0, rt_subframes=RT_SUBFRAMES)
rp.hydra_texture.set_updates_enabled(False)
```

The cost difference is most visible in Workflow 1, which advances PhysX many ticks between captures, and in any pipeline with multiple high-resolution cameras.

## Seeded Randomization

The scripts use a single `ReplicatorRNG` instance for all sampling. Helpers such as `randomize_camera`, `scatter_2d`, and `rng.generator.uniform` all take that instance as their `rng=` argument. Seed it once at startup so the script is fully reproducible:

```python
rng = rep.rng.ReplicatorRNG(seed=42)
```

The same seed always produces the same dataset, which is useful when regenerating a specific outlier image.

## Wait Until Complete

Replicator writers do their I/O on background threads. If the script closes the application immediately after the last orchestrator step, the writer can still have several frames queued and the dataset will be missing PNGs or have half-written JSON files. Always wait before tearing down:

```python
rep.orchestrator.wait_until_complete()                  # standalone
await rep.orchestrator.wait_until_complete_async()      # script editor
```

After `wait_until_complete` returns it is safe to detach the writer, destroy the render product, and close the application.

## Async vs Sync

Each workflow ships with two entry-point scripts that share scene-authoring code but differ in how they drive the application loop:

* **Script Editor** (`*_script_editor.py`) - executes inside the Isaac Sim [Script Editor](../development_tools/omniverse_script_editor.html#script-editor) window. The entry function is a coroutine that awaits the `_async` Replicator helpers (for example `rep.orchestrator.step_async`) and yields back to the application loop with `await omni.kit.app.get_app().next_update_async()`.
* **Standalone Application** (`sdg_workflow_*.py`) - launches its own [Standalone Application](../introduction/workflows.html#standalone-application) (`python.sh` on Linux, `python.bat` on Windows). It uses the synchronous Replicator helpers and drives the application loop directly with `simulation_app.update()`.

## Examples

The following sections present two complete example scripts that apply the settings from the previous section. Each section describes its scene, its capture loop, and its output on its own. Every script is shown in both the Script Editor and Standalone Application forms described above.

### Workflow 1: Physics-Based Object Settling

This workflow builds one scene (dome light, pallet, distractors, cardboxes, and camera) and keeps it for the whole run. Before each capture it re-drops one box and lets PhysX settle it, so every frame shows a slightly different physical arrangement of the same objects. The render product and writer are created once and reused, which avoids per-capture setup cost when the scene structure does not change.

The script defines helper functions that each randomize one part of the existing scene:

* `randomize_dome_light` - chooses an HDR texture and intensity for the dome light.
* `randomize_distractors` - samples positions, rotations, scales, and display colors for the distractor prims.
* `randomize_pallet` - picks one of the pre-created materials and binds it to the pallet.
* `randomize_camera` - samples an orbit position around the pallet and points the camera back at it.
* `randomize_boxes` - writes per-box poses just before the timeline plays so PhysX settles the boxes over `NUM_SIMULATION_FRAMES` ticks.

The capture loop runs `NUM_CAPTURES` times:

1. Randomize the lighting, distractors, and pallet material with the helpers above.
2. Pick one box at random, give it a fresh pose, and advance the timeline `NUM_SIMULATION_FRAMES` ticks so PhysX settles the new pose.
3. Move the camera, enable the render product, call the orchestrator step, then disable the render product again.

Physics runs *between* captures (step 2), and only the orchestrator step (step 3) produces a frame.

The standalone example can also be run directly (on Windows use `python.bat` instead of `python.sh`):

```python
./python.sh standalone_examples/api/isaacsim.replicator.examples/sdg_workflow_01.py
```

Script Editor

```python
"""
Basic SDG workflow with scene creation, asset placement, randomization, and data capture.
Boxes are randomized and simulated with physics before each capture.
"""

import asyncio
import math
import os

import carb
import carb.settings
import omni.kit.app
import omni.replicator.core as rep
import omni.timeline
import omni.usd
from isaacsim.storage.native import get_assets_root_path
from pxr import Usd, UsdGeom, UsdPhysics

NUM_CAPTURES = 5
RESOLUTION = (1280, 720)
RT_SUBFRAMES = 8
NUM_DROP_BOXES = 10
NUM_SIMULATION_FRAMES = 75
NUM_PRIM_DISTRACTORS = 5
ENV_URL = "/Isaac/Environments/Grid/default_environment.usd"

def randomize_distractors(prims, rng):
    # Sample small distractors on a loose ring around the pallet.
    count = len(prims)
    angles = rng.generator.uniform(0.0, 2.0 * math.pi, count)
    radii = rng.generator.uniform(0.9, 1.4, count)
    heights = rng.generator.uniform(0.15, 0.45, count)
    positions = [
        (float(radius * math.cos(angle)), float(radius * math.sin(angle)), float(height))
        for angle, radius, height in zip(angles, radii, heights)
    ]
    rotations = rng.generator.uniform((0.0, 0.0, 0.0), (45.0, 45.0, 360.0), size=(count, 3)).tolist()
    scales = rng.generator.uniform(0.1, 0.2, count).tolist()
    rep.functional.modify.pose(
        prims,
        position_value=positions,
        rotation_value=rotations,
        scale_value=scales,
    )
    rep.functional.randomizer.display_color(prims, rng=rng)

def randomize_dome_light(dome_light, texture_urls, rng):
    texture_url = texture_urls[int(rng.generator.integers(0, len(texture_urls)))]
    intensity = float(rng.generator.uniform(500.0, 900.0))
    rep.functional.modify.attribute(dome_light, "inputs:texture:file", texture_url)
    rep.functional.modify.attribute(dome_light, "inputs:intensity", intensity)

def randomize_pallet(pallet, materials, rng):
    material = materials[int(rng.generator.integers(0, len(materials)))]
    rep.functional.modify.material(pallet, material)

def randomize_camera(camera, look_at, rng):
    theta = float(rng.generator.uniform(0.0, 2.0 * math.pi))
    radius = float(rng.generator.uniform(2.6, 3.4))
    position = (
        radius * math.cos(theta),
        radius * math.sin(theta),
        float(rng.generator.uniform(1.4, 2.2)),
    )
    rep.functional.modify.pose(
        camera,
        position_value=position,
        look_at_value=look_at,
        look_at_up_axis=(0, 0, 1),
        write_to_usd=True,
    )

def randomize_boxes(boxes, start_height, rng):
    for i, box in enumerate(boxes):
        lateral_range = 0.4
        height = start_height + 0.2 * i
        tilt_range = 15.0
        rep.functional.modify.pose(
            box,
            position_value=(
                float(rng.generator.uniform(-lateral_range, lateral_range)),
                float(rng.generator.uniform(-lateral_range, lateral_range)),
                height,
            ),
            rotation_value=(
                float(rng.generator.uniform(0.0, tilt_range)),
                float(rng.generator.uniform(0.0, tilt_range)),
                float(rng.generator.uniform(0.0, 360.0)),
            ),
            write_to_usd=True,
        )

async def run_workflow_async():
    assets_root_path = get_assets_root_path()
    if assets_root_path is None:
        carb.log_error("[SDG] Could not resolve assets root path; aborting.")
        return

    # Load stage.
    env_path = assets_root_path + ENV_URL
    stage, error = await omni.usd.get_context().open_stage_async(env_path)
    if error or stage is None:
        carb.log_error(f"[SDG] Failed to open stage: '{env_path}', exiting.")
        return

    # Disable automatic capture so only explicit `step_async()` calls write frames.
    rep.orchestrator.set_capture_on_play(False)

    # Set DLSS to Quality mode to reduce low-resolution SDG rendering artifacts.
    carb.settings.get_settings().set("rtx/post/dlss/execMode", 2)

    # Seed the functional randomizer so re-running the script is reproducible.
    rng = rep.rng.ReplicatorRNG(seed=42)

    # Create a dome light which will be randomized by texture and brightness.
    rep.functional.create.xform(name="SDG")
    rep.functional.create.scope(name="Lights", parent="/SDG")
    dome_texture_urls = [
        assets_root_path + "/NVIDIA/Assets/Skies/Indoor/autoshop_01_4k.hdr",
        assets_root_path + "/NVIDIA/Assets/Skies/Indoor/carpentry_shop_01_4k.hdr",
        assets_root_path + "/NVIDIA/Assets/Skies/Indoor/wooden_lounge_4k.hdr",
    ]
    dome_light = rep.functional.create.dome_light(
        texture=dome_texture_urls[0],
        intensity=700,
        parent="/SDG/Lights",
        name="DomeLight",
    )
    randomize_dome_light(dome_light, dome_texture_urls, rng=rng)

    # Create a pallet with collision to drop boxes onto, its materials will be randomized.
    rep.functional.create.scope(name="Assets", parent="/SDG")
    rep.functional.create.scope(name="Materials", parent="/SDG")
    pallet_url = assets_root_path + "/Isaac/Environments/Simple_Warehouse/Props/SM_PaletteA_01.usd"
    pallet = rep.functional.create.reference(
        usd_path=pallet_url,
        parent="/SDG/Assets",
        name="Pallet",
        semantics={"class": "pallet"},
    )
    rep.functional.physics.apply_rigid_body(pallet, with_collider=True, kinematicEnabled=True)
    pallet_materials = []
    for i in range(5):
        color = rng.generator.uniform((0.45, 0.3, 0.15), (0.95, 0.85, 0.55), size=3)
        pallet_materials.append(
            rep.functional.create.material(
                mdl="OmniPBR.mdl",
                diffuse_color_constant=tuple(float(channel) for channel in color),
                reflection_roughness_constant=float(rng.generator.uniform(0.45, 0.95)),
                metallic_constant=float(rng.generator.uniform(0.0, 0.05)),
                name=f"PalletMaterial_{i}",
                parent="/SDG/Materials",
            )
        )
    randomize_pallet(pallet, pallet_materials, rng=rng)

    # Create primitive distractors to randomly place around the scene.
    rep.functional.create.scope(name="Distractors", parent="/SDG/Assets")
    cube_distractors = rep.functional.create_batch.cube(
        count=NUM_PRIM_DISTRACTORS,
        parent="/SDG/Assets/Distractors",
        name="DistractorCube",
        semantics={"class": "distractor"},
    )
    sphere_distractors = rep.functional.create_batch.sphere(
        count=NUM_PRIM_DISTRACTORS,
        parent="/SDG/Assets/Distractors",
        name="DistractorSphere",
        semantics={"class": "distractor"},
    )
    cylinder_distractors = rep.functional.create_batch.cylinder(
        count=NUM_PRIM_DISTRACTORS,
        parent="/SDG/Assets/Distractors",
        name="DistractorCylinder",
        semantics={"class": "distractor"},
    )
    cone_distractors = rep.functional.create_batch.cone(
        count=NUM_PRIM_DISTRACTORS,
        parent="/SDG/Assets/Distractors",
        name="DistractorCone",
        semantics={"class": "distractor"},
    )
    distractors = cube_distractors + sphere_distractors + cylinder_distractors + cone_distractors
    randomize_distractors(distractors, rng=rng)

    # Create boxes with rigid body dynamics to randomly drop onto the pallet.
    cardbox_url = assets_root_path + "/Isaac/Environments/Simple_Warehouse/Props/SM_CardBoxD_04.usd"
    boxes = []
    for i in range(NUM_DROP_BOXES):
        box = rep.functional.create.reference(
            usd_path=cardbox_url,
            parent="/SDG/Assets",
            name=f"Box_{i}",
            semantics={"class": "cardbox"},
        )
        # The referenced box has mesh children, so set a simple box collider on each mesh.
        for child_prim in Usd.PrimRange(box):
            if child_prim.IsA(UsdGeom.Mesh):
                mesh_collision_api = UsdPhysics.MeshCollisionAPI.Apply(child_prim)
                mesh_collision_api.CreateApproximationAttr().Set("boundingCube")
                rep.functional.physics.apply_rigid_body(child_prim, with_collider=True, approximation="boundingCube")
        rep.functional.physics.apply_rigid_body(box)
        boxes.append(box)
    randomize_boxes(boxes, start_height=0.3, rng=rng)

    # Drop the boxes.
    timeline = omni.timeline.get_timeline_interface()
    timeline.play()
    for _ in range(NUM_SIMULATION_FRAMES):
        await omni.kit.app.get_app().next_update_async()
    timeline.pause()

    # Setup SDG.
    rep.functional.create.scope(name="Cameras", parent="/SDG")
    cam = rep.functional.create.camera(
        position=(3.0, 3.0, 2.0), look_at=(0, 0, 0.4), parent="/SDG/Cameras", name="Camera"
    )
    rp = rep.create.render_product(cam, RESOLUTION, name="rp_workflow_01")
    # Disable render products by default and only enable them at capture time.
    rp.hydra_texture.set_updates_enabled(False)

    # Create a `BasicWriter` to save common annotations from the same camera view.
    backend = rep.backends.get("DiskBackend")
    out_dir = os.path.join(os.getcwd(), "_out_workflow_01")
    backend.initialize(output_dir=out_dir)
    print(f"[SDG] Output directory: {out_dir}")
    writer = rep.writers.get("BasicWriter")
    writer.initialize(
        backend=backend,
        rgb=True,
        semantic_segmentation=True,
        colorize_semantic_segmentation=True,
    )
    writer.attach(rp)

    for i in range(NUM_CAPTURES):
        print(f"[SDG] Capture {i + 1}/{NUM_CAPTURES}")

        # Run the randomizers on the scene.
        randomize_dome_light(dome_light, dome_texture_urls, rng=rng)
        randomize_distractors(distractors, rng=rng)
        randomize_pallet(pallet, pallet_materials, rng=rng)

        # Re-drop one box so each capture has a slightly different physical arrangement.
        box = boxes[int(rng.generator.integers(0, len(boxes)))]
        randomize_boxes([box], start_height=1.2, rng=rng)
        timeline.play()
        for _ in range(NUM_SIMULATION_FRAMES):
            await omni.kit.app.get_app().next_update_async()
        timeline.pause()

        # Sample a new camera position on a small orbit while looking at the pallet.
        randomize_camera(cam, pallet, rng=rng)

        # Enable rendering only for the capture step to avoid extra GPU work.
        rp.hydra_texture.set_updates_enabled(True)
        await rep.orchestrator.step_async(delta_time=0.0, rt_subframes=RT_SUBFRAMES)
        rp.hydra_texture.set_updates_enabled(False)

    # Cleanup.
    await rep.orchestrator.wait_until_complete_async()
    writer.detach()
    rp.destroy()

asyncio.ensure_future(run_workflow_async())
```

Standalone Application

```python
"""Basic SDG workflow with scene creation, asset placement, randomization, and data capture.
Boxes are randomized and simulated with physics before each capture.
"""

import math
import os

from isaacsim import SimulationApp

simulation_app = SimulationApp(launch_config={"headless": False})

import carb
import carb.settings
import omni.replicator.core as rep
import omni.timeline
import omni.usd
from isaacsim.storage.native import get_assets_root_path
from pxr import Usd, UsdGeom, UsdPhysics

NUM_CAPTURES = 5
RESOLUTION = (1280, 720)
RT_SUBFRAMES = 8
NUM_DROP_BOXES = 10
NUM_SIMULATION_FRAMES = 75
NUM_PRIM_DISTRACTORS = 5
ENV_URL = "/Isaac/Environments/Grid/default_environment.usd"

def randomize_distractors(prims, rng):
    # Sample small distractors on a loose ring around the pallet.
    count = len(prims)
    angles = rng.generator.uniform(0.0, 2.0 * math.pi, count)
    radii = rng.generator.uniform(0.9, 1.4, count)
    heights = rng.generator.uniform(0.15, 0.45, count)
    positions = [
        (float(radius * math.cos(angle)), float(radius * math.sin(angle)), float(height))
        for angle, radius, height in zip(angles, radii, heights)
    ]
    rotations = rng.generator.uniform((0.0, 0.0, 0.0), (45.0, 45.0, 360.0), size=(count, 3)).tolist()
    scales = rng.generator.uniform(0.1, 0.2, count).tolist()
    rep.functional.modify.pose(
        prims,
        position_value=positions,
        rotation_value=rotations,
        scale_value=scales,
    )
    rep.functional.randomizer.display_color(prims, rng=rng)

def randomize_dome_light(dome_light, texture_urls, rng):
    texture_url = texture_urls[int(rng.generator.integers(0, len(texture_urls)))]
    intensity = float(rng.generator.uniform(500.0, 900.0))
    rep.functional.modify.attribute(dome_light, "inputs:texture:file", texture_url)
    rep.functional.modify.attribute(dome_light, "inputs:intensity", intensity)

def randomize_pallet(pallet, materials, rng):
    material = materials[int(rng.generator.integers(0, len(materials)))]
    rep.functional.modify.material(pallet, material)

def randomize_camera(camera, look_at, rng):
    theta = float(rng.generator.uniform(0.0, 2.0 * math.pi))
    radius = float(rng.generator.uniform(2.6, 3.4))
    position = (
        radius * math.cos(theta),
        radius * math.sin(theta),
        float(rng.generator.uniform(1.4, 2.2)),
    )
    rep.functional.modify.pose(
        camera,
        position_value=position,
        look_at_value=look_at,
        look_at_up_axis=(0, 0, 1),
        write_to_usd=True,
    )

def randomize_boxes(boxes, start_height, rng):
    for i, box in enumerate(boxes):
        lateral_range = 0.4
        height = start_height + 0.2 * i
        tilt_range = 15.0
        rep.functional.modify.pose(
            box,
            position_value=(
                float(rng.generator.uniform(-lateral_range, lateral_range)),
                float(rng.generator.uniform(-lateral_range, lateral_range)),
                height,
            ),
            rotation_value=(
                float(rng.generator.uniform(0.0, tilt_range)),
                float(rng.generator.uniform(0.0, tilt_range)),
                float(rng.generator.uniform(0.0, 360.0)),
            ),
            write_to_usd=True,
        )

def run_workflow():
    assets_root_path = get_assets_root_path()
    if assets_root_path is None:
        carb.log_error("[SDG] Could not resolve assets root path; aborting.")
        return

    # Load stage.
    env_path = assets_root_path + ENV_URL
    omni.usd.get_context().open_stage(env_path)
    stage = omni.usd.get_context().get_stage()
    if stage is None:
        carb.log_error(f"[SDG] Failed to open stage: '{env_path}', exiting.")
        return

    # Disable automatic capture so only explicit `step()` calls write frames.
    rep.orchestrator.set_capture_on_play(False)

    # Set DLSS to Quality mode to reduce low-resolution SDG rendering artifacts.
    carb.settings.get_settings().set("rtx/post/dlss/execMode", 2)

    # Seed the functional randomizer so re-running the script is reproducible.
    rng = rep.rng.ReplicatorRNG(seed=42)
    timeline = omni.timeline.get_timeline_interface()

    # Create a dome light which will be randomized by texture and brightness.
    rep.functional.create.xform(name="SDG")
    rep.functional.create.scope(name="Lights", parent="/SDG")
    dome_texture_urls = [
        assets_root_path + "/NVIDIA/Assets/Skies/Indoor/autoshop_01_4k.hdr",
        assets_root_path + "/NVIDIA/Assets/Skies/Indoor/carpentry_shop_01_4k.hdr",
        assets_root_path + "/NVIDIA/Assets/Skies/Indoor/wooden_lounge_4k.hdr",
    ]
    dome_light = rep.functional.create.dome_light(
        texture=dome_texture_urls[0],
        intensity=700,
        parent="/SDG/Lights",
        name="DomeLight",
    )
    randomize_dome_light(dome_light, dome_texture_urls, rng=rng)

    # Create a pallet with collision to drop boxes onto, its materials will be randomized.
    rep.functional.create.scope(name="Assets", parent="/SDG")
    rep.functional.create.scope(name="Materials", parent="/SDG")
    pallet_url = assets_root_path + "/Isaac/Environments/Simple_Warehouse/Props/SM_PaletteA_01.usd"
    pallet = rep.functional.create.reference(
        usd_path=pallet_url,
        parent="/SDG/Assets",
        name="Pallet",
        semantics={"class": "pallet"},
    )
    rep.functional.physics.apply_rigid_body(pallet, with_collider=True, kinematicEnabled=True)
    pallet_materials = []
    for i in range(5):
        color = rng.generator.uniform((0.45, 0.3, 0.15), (0.95, 0.85, 0.55), size=3)
        pallet_materials.append(
            rep.functional.create.material(
                mdl="OmniPBR.mdl",
                diffuse_color_constant=tuple(float(channel) for channel in color),
                reflection_roughness_constant=float(rng.generator.uniform(0.45, 0.95)),
                metallic_constant=float(rng.generator.uniform(0.0, 0.05)),
                name=f"PalletMaterial_{i}",
                parent="/SDG/Materials",
            )
        )
    randomize_pallet(pallet, pallet_materials, rng=rng)

    # Create primitive distractors to randomly place around the scene.
    rep.functional.create.scope(name="Distractors", parent="/SDG/Assets")
    cube_distractors = rep.functional.create_batch.cube(
        count=NUM_PRIM_DISTRACTORS,
        parent="/SDG/Assets/Distractors",
        name="DistractorCube",
        semantics={"class": "distractor"},
    )
    sphere_distractors = rep.functional.create_batch.sphere(
        count=NUM_PRIM_DISTRACTORS,
        parent="/SDG/Assets/Distractors",
        name="DistractorSphere",
        semantics={"class": "distractor"},
    )
    cylinder_distractors = rep.functional.create_batch.cylinder(
        count=NUM_PRIM_DISTRACTORS,
        parent="/SDG/Assets/Distractors",
        name="DistractorCylinder",
        semantics={"class": "distractor"},
    )
    cone_distractors = rep.functional.create_batch.cone(
        count=NUM_PRIM_DISTRACTORS,
        parent="/SDG/Assets/Distractors",
        name="DistractorCone",
        semantics={"class": "distractor"},
    )
    distractors = cube_distractors + sphere_distractors + cylinder_distractors + cone_distractors
    randomize_distractors(distractors, rng=rng)

    # Create boxes with rigid body dynamics to randomly drop onto the pallet.
    cardbox_url = assets_root_path + "/Isaac/Environments/Simple_Warehouse/Props/SM_CardBoxD_04.usd"
    boxes = []
    for i in range(NUM_DROP_BOXES):
        box = rep.functional.create.reference(
            usd_path=cardbox_url,
            parent="/SDG/Assets",
            name=f"Box_{i}",
            semantics={"class": "cardbox"},
        )
        # The referenced box has mesh children, so set a simple box collider on each mesh.
        for child_prim in Usd.PrimRange(box):
            if child_prim.IsA(UsdGeom.Mesh):
                mesh_collision_api = UsdPhysics.MeshCollisionAPI.Apply(child_prim)
                mesh_collision_api.CreateApproximationAttr().Set("boundingCube")
                rep.functional.physics.apply_rigid_body(child_prim, with_collider=True, approximation="boundingCube")
        rep.functional.physics.apply_rigid_body(box)
        boxes.append(box)
    randomize_boxes(boxes, start_height=0.3, rng=rng)

    # Drop the boxes.
    timeline.play()
    for _ in range(NUM_SIMULATION_FRAMES):
        simulation_app.update()
    timeline.pause()

    # Setup SDG.
    rep.functional.create.scope(name="Cameras", parent="/SDG")
    cam = rep.functional.create.camera(
        position=(3.0, 3.0, 2.0), look_at=(0, 0, 0.4), parent="/SDG/Cameras", name="Camera"
    )
    rp = rep.create.render_product(cam, RESOLUTION, name="rp_workflow_01")
    # Disable render products by default and only enable them at capture time.
    rp.hydra_texture.set_updates_enabled(False)

    # Attach a `BasicWriter` to save common annotations from the same camera view.
    backend = rep.backends.get("DiskBackend")
    out_dir = os.path.join(os.getcwd(), "_out_workflow_01")
    backend.initialize(output_dir=out_dir)
    print(f"[SDG] Output directory: {out_dir}")
    writer = rep.writers.get("BasicWriter")
    writer.initialize(
        backend=backend,
        rgb=True,
        semantic_segmentation=True,
        colorize_semantic_segmentation=True,
    )
    writer.attach(rp)

    for i in range(NUM_CAPTURES):
        print(f"[SDG] Capture {i + 1}/{NUM_CAPTURES}")

        # Run the randomizers on the scene.
        randomize_dome_light(dome_light, dome_texture_urls, rng=rng)
        randomize_distractors(distractors, rng=rng)
        randomize_pallet(pallet, pallet_materials, rng=rng)

        # Re-drop one box so each capture has a slightly different physical arrangement.
        box = boxes[int(rng.generator.integers(0, len(boxes)))]
        randomize_boxes([box], start_height=1.2, rng=rng)
        timeline.play()
        for _ in range(NUM_SIMULATION_FRAMES):
            simulation_app.update()
        timeline.pause()

        # Sample a new camera position on a small orbit while looking at the pallet.
        randomize_camera(cam, pallet, rng=rng)

        # Enable rendering only for the capture step to avoid extra GPU work.
        rp.hydra_texture.set_updates_enabled(True)
        rep.orchestrator.step(delta_time=0.0, rt_subframes=RT_SUBFRAMES)
        rp.hydra_texture.set_updates_enabled(False)

    # Cleanup.
    rep.orchestrator.wait_until_complete()
    writer.detach()
    rp.destroy()

run_workflow()
```

Output directory `_out_workflow_01`: per captured frame, an `rgb_*.png`, a colorized `semantic_segmentation_*.png`, and a matching `*.json` label map written by the `BasicWriter`.

### Workflow 2: Collision-Checked Asset Placement

This workflow rebuilds its SDG content on a configurable cadence (`CAPTURES_PER_SCENE`). Each rebuild picks an environment, scatters pallets on the floor, builds vertical box stacks on each pallet, and orbits one camera around each pallet. It places assets with sample-time collision checks rather than rigid-body simulation, so there is no physics settling step.

The persistent objects (a dome light, one camera, one render product, and one `BasicWriter`) are created once. The per-rebuild content lives under a unique scope `/World/SDG/Scene_<n>`. The script removes the previous scope before authoring the next one. If the old scope remains on the stage, Replicatorâs scatter-mesh cache reuses stale planes and asset placement fails.

Each scene rebuild does the following:

1. Pick an environment URL from `DEFAULT_ENV_URLS`. If the entry is `None`, build a large ground plane with a collider instead.
2. `create_pallets_on_floor` - sample a count from `PALLET_COUNT_RANGE`, scatter that many pallets on a hidden floor plane with `rep.functional.randomizer.scatter_2d` and `check_for_collisions=True`, then snap each pallet so its measured bottom rests at `z=0`.
3. `create_stacks_on_pallet` for each pallet - sample a stack count, scatter base boxes on a hidden plane fitted to the pallet top with collision checks (retry with one fewer base if scattering cannot find a collision-free layout), then build each stack vertically by referencing the same box asset at increasing heights.
4. For each capture in this scene, `randomize_camera` orbits the camera around the next pallet and the orchestrator step writes one frame.

The outer loop continues until `TOTAL_CAPTURES` frames have been written. The hidden scatter planes and the bounding-box queries (`compute_aabb`) place assets on surfaces without running physics.

The standalone example can also be run directly (on Windows use `python.bat` instead of `python.sh`):

```python
./python.sh standalone_examples/api/isaacsim.replicator.examples/sdg_workflow_02.py
```

Script Editor

```python
"""
Generate palletized box stacks across randomized scenes.
Each scene chooses an environment, scatters pallets, builds box stacks, and captures camera views.
"""

import asyncio
import math
import os

import carb
import carb.settings
import isaacsim.core.experimental.utils.bounds as bounds_utils
import omni.kit.app
import omni.replicator.core as rep
import omni.usd
from isaacsim.storage.native import get_assets_root_path
from omni.replicator.core.scripts.functional import utils as rep_utils

DEFAULT_ENV_URLS = [
    "/Isaac/Environments/Simple_Warehouse/warehouse.usd",
    None,
]
PALLET_URL = "/Isaac/Environments/Simple_Warehouse/Props/SM_PaletteA_01.usd"
BOX_URLS = [
    "/Isaac/Environments/Simple_Warehouse/Props/SM_CardBoxC_01.usd",
    "/Isaac/Environments/Simple_Warehouse/Props/SM_CardBoxD_01.usd",
]

TOTAL_CAPTURES = 5
CAPTURES_PER_SCENE = 3
RESOLUTION = (1280, 720)
RT_SUBFRAMES = 8
PALLET_COUNT_RANGE = range(2, 6)
STACK_COUNT_RANGE = range(1, 4)
BOXES_PER_STACK_RANGE = range(1, 6)
STACK_SCATTER_AREA_SCALE = 0.9

async def create_pallets_on_floor(scene_scope_path, assets_root_path, rng):
    pallet_count = int(rng.generator.choice(PALLET_COUNT_RANGE))
    # Use a hidden floor plane as a sampling surface so scattered pallets avoid each other.
    floor_plane = rep.functional.create.plane(
        parent=scene_scope_path,
        name="PalletScatterPlane",
        position=(0.0, 0.0, 0.0),
        scale=(5.0, 5.0, 1.0),
        visible=False,
    )

    pallets = []
    for i in range(pallet_count):
        pallets.append(
            rep.functional.create.reference(
                usd_path=assets_root_path + PALLET_URL,
                parent=scene_scope_path,
                name=f"Pallet_{i}",
                position=(i * 2.0, 0.0, 1.0),
                rotation=(0.0, 0.0, float(rng.generator.choice([0.0, 90.0, 180.0, 270.0]))),
                semantics={"class": "pallet"},
            )
        )

    await omni.kit.app.get_app().next_update_async()
    rep.functional.randomizer.scatter_2d(pallets, floor_plane, check_for_collisions=True, rng=rng)
    await omni.kit.app.get_app().next_update_async()

    bbox_cache = bounds_utils.create_bbox_cache()
    for pallet in pallets:
        aabb = bounds_utils.compute_aabb(pallet, bbox_cache=bbox_cache, include_children=True)
        origin = rep_utils.get_world_position(pallet)
        origin_to_bottom = float(origin[2] - aabb[2])
        # Move the pallet origin so the measured bottom sits on the floor.
        rep.functional.modify.pose(
            pallet,
            position_value=(float(origin[0]), float(origin[1]), origin_to_bottom),
            write_to_usd=True,
        )

    await omni.kit.app.get_app().next_update_async()
    return pallets

async def create_stacks_on_pallet(scene_scope_path, pallet_index, pallet, assets_root_path, rng):
    bbox_cache = bounds_utils.create_bbox_cache()
    pallet_bounds = bounds_utils.compute_aabb(pallet, bbox_cache=bbox_cache, include_children=True)
    pallet_origin = rep_utils.get_world_position(pallet)
    stack_count = int(rng.generator.choice(STACK_COUNT_RANGE))
    pallet_top_z = float(pallet_bounds[5])
    pallet_center_x = float(pallet_origin[0])
    pallet_center_y = float(pallet_origin[1])
    pallet_size_x = float(pallet_bounds[3] - pallet_bounds[0])
    pallet_size_y = float(pallet_bounds[4] - pallet_bounds[1])

    base_boxes = []
    stack_data = []
    for i in range(stack_count):
        box_url = BOX_URLS[int(rng.generator.integers(0, len(BOX_URLS)))]
        box = rep.functional.create.reference(
            usd_path=assets_root_path + box_url,
            parent=scene_scope_path,
            name=f"Pallet_{pallet_index}_BoxStack_{i}_Base",
            position=(i * 2.0, 0.0, pallet_top_z + 1.0),
            semantics={"class": "cardbox"},
        )
        base_boxes.append(box)
        stack_data.append(
            {
                "box": box,
                "url": assets_root_path + box_url,
                "height_count": int(rng.generator.choice(BOXES_PER_STACK_RANGE)),
            }
        )

    await omni.kit.app.get_app().next_update_async()
    bbox_cache = bounds_utils.create_bbox_cache()
    max_box_height = 0.0
    for stack in stack_data:
        aabb = bounds_utils.compute_aabb(stack["box"], bbox_cache=bbox_cache, include_children=True)
        origin = rep_utils.get_world_position(stack["box"])
        stack["size"] = (
            float(aabb[3] - aabb[0]),
            float(aabb[4] - aabb[1]),
            float(aabb[5] - aabb[2]),
        )
        # Referenced box assets use an origin near the bottom, so keep this offset when stacking.
        stack["origin_to_bottom"] = float(origin[2] - aabb[2])
        max_box_height = max(max_box_height, stack["size"][2])

    # Scatter stack bases on a hidden plane smaller than the pallet top.
    scatter_plane = rep.functional.create.plane(
        parent=scene_scope_path,
        name=f"Pallet_{pallet_index}_StackScatterPlane",
        position=(pallet_center_x, pallet_center_y, pallet_top_z),
        scale=(pallet_size_x * STACK_SCATTER_AREA_SCALE, pallet_size_y * STACK_SCATTER_AREA_SCALE, 1.0),
        visible=False,
    )

    while True:
        try:
            rep.functional.randomizer.scatter_2d(
                base_boxes,
                scatter_plane,
                offset=max_box_height * 0.5,
                check_for_collisions=True,
                rng=rng,
            )
            break
        except ValueError:
            if len(base_boxes) <= 1:
                raise
            stack_data.pop()
            removed_box = base_boxes.pop()
            omni.usd.get_context().get_stage().RemovePrim(removed_box.GetPath())
            print(
                f"[SDG] Warning: could not scatter {len(base_boxes) + 1} stacks on pallet {pallet_index}; "
                f"retrying with {len(base_boxes)}."
            )
            await omni.kit.app.get_app().next_update_async()
    await omni.kit.app.get_app().next_update_async()

    all_boxes = list(base_boxes)
    for stack_idx, stack in enumerate(stack_data):
        _, _, box_height = stack["size"]
        origin_to_bottom = stack["origin_to_bottom"]
        origin = rep_utils.get_world_position(stack["box"])
        origin_x = float(origin[0])
        origin_y = float(origin[1])

        rep.functional.modify.pose(
            stack["box"],
            position_value=(origin_x, origin_y, pallet_top_z + origin_to_bottom),
            write_to_usd=True,
        )

        for level in range(1, stack["height_count"]):
            all_boxes.append(
                rep.functional.create.reference(
                    usd_path=stack["url"],
                    parent=scene_scope_path,
                    name=f"Pallet_{pallet_index}_BoxStack_{stack_idx}_{level}",
                    position=(origin_x, origin_y, pallet_top_z + origin_to_bottom + box_height * level),
                    semantics={"class": "cardbox"},
                )
            )

    return all_boxes

def randomize_camera(camera, pallet, rng):
    bbox_cache = bounds_utils.create_bbox_cache()
    pallet_bounds = bounds_utils.compute_aabb(pallet, bbox_cache=bbox_cache, include_children=True)
    pallet_origin = rep_utils.get_world_position(pallet)
    target = (
        float(pallet_origin[0]),
        float(pallet_origin[1]),
        float(pallet_bounds[5] + 0.5),
    )
    theta = float(rng.generator.uniform(0.0, 2.0 * math.pi))
    radius = float(rng.generator.uniform(2.4, 3.2))
    height = float(rng.generator.uniform(1.4, 2.2))
    rep.functional.modify.pose(
        camera,
        position_value=(
            target[0] + radius * math.cos(theta),
            target[1] + radius * math.sin(theta),
            target[2] + height,
        ),
        look_at_value=target,
        look_at_up_axis=(0, 0, 1),
        write_to_usd=True,
    )

async def run_workflow_async():
    # Create a clean stage for this tutorial workflow.
    assets_root_path = get_assets_root_path()
    if assets_root_path is None:
        carb.log_error("[SDG] Could not resolve assets root path; aborting.")
        return

    await omni.usd.get_context().new_stage_async()
    stage = omni.usd.get_context().get_stage()
    if stage is None:
        carb.log_error("[SDG] Could not create a new stage; aborting.")
        return

    # Disable automatic capture so only explicit `step_async()` calls write frames.
    rep.orchestrator.set_capture_on_play(False)

    # Set DLSS to Quality mode to reduce low-resolution SDG rendering artifacts.
    carb.settings.get_settings().set("rtx/post/dlss/execMode", 2)

    # Seed the randomizer so re-running the script produces the same scene.
    rng = rep.rng.ReplicatorRNG(seed=42)

    rep.functional.create.xform(name="World")
    rep.functional.create.xform(parent="/World", name="SDG")

    # Keep generated SDG content separate from the randomized environment.
    rep.functional.create.dome_light(intensity=500, parent="/World/SDG", name="DomeLight")

    # Use one camera and move it to each pallet before capturing.
    cam = rep.functional.create.camera(position=(3, 3, 3), look_at=(0, 0, 0), parent="/World/SDG", name="Camera")
    rp = rep.create.render_product(cam, RESOLUTION, name="rp_workflow_02")
    # Disable render products by default and only enable them at capture time.
    rp.hydra_texture.set_updates_enabled(False)

    # Create a `BasicWriter` to save RGB and colorized semantic labels.
    backend = rep.backends.get("DiskBackend")
    out_dir = os.path.join(os.getcwd(), "_out_workflow_02")
    backend.initialize(output_dir=out_dir)
    print(f"[SDG] Output directory: {out_dir}")
    writer = rep.writers.get("BasicWriter")
    writer.initialize(
        backend=backend,
        rgb=True,
        semantic_segmentation=True,
        colorize_semantic_segmentation=True,
    )
    writer.attach(rp)

    environment_scope_path = "/World/Environment"
    capture_count = 0
    randomization_count = 0
    prev_scene_scope_path = None

    while capture_count < TOTAL_CAPTURES:
        randomization_count += 1
        print(f"[SDG] Randomization {randomization_count}")

        # Use a unique scene scope per randomization so Replicator's scatter mesh cache stays fresh.
        scene_scope_name = f"Scene_{randomization_count}"
        scene_scope_path = f"/World/SDG/{scene_scope_name}"

        if stage.GetPrimAtPath(environment_scope_path).IsValid():
            stage.RemovePrim(environment_scope_path)
        if prev_scene_scope_path is not None and stage.GetPrimAtPath(prev_scene_scope_path).IsValid():
            stage.RemovePrim(prev_scene_scope_path)
        await omni.kit.app.get_app().next_update_async()

        rep.functional.create.scope(name="Environment", parent="/World")
        # Pick an environment; None means use a generated ground plane.
        env_url = DEFAULT_ENV_URLS[int(rng.generator.integers(0, len(DEFAULT_ENV_URLS)))]
        if env_url is None:
            ground = rep.functional.create.plane(
                parent=environment_scope_path,
                name="GroundPlane",
                scale=(100, 100, 1),
            )
            rep.functional.physics.apply_collider(ground)
        else:
            rep.functional.create.reference(
                usd_path=assets_root_path + env_url,
                parent=environment_scope_path,
                name="Scene",
            )

        rep.functional.create.scope(name=scene_scope_name, parent="/World/SDG")
        prev_scene_scope_path = scene_scope_path

        # Choose the pallet count, scatter them, shuffle the order, then build stacks.
        pallets = await create_pallets_on_floor(scene_scope_path, assets_root_path, rng)
        pallet_order = list(range(len(pallets)))
        rng.generator.shuffle(pallet_order)
        pallets = [pallets[i] for i in pallet_order]
        for pallet_idx, pallet in enumerate(pallets):
            await create_stacks_on_pallet(scene_scope_path, pallet_idx, pallet, assets_root_path, rng)

        captures_this_scene = min(CAPTURES_PER_SCENE, TOTAL_CAPTURES - capture_count)
        for capture_idx in range(captures_this_scene):
            pallet = pallets[capture_idx % len(pallets)]
            randomize_camera(cam, pallet, rng)

            capture_count += 1
            print(f"[SDG] Capture {capture_count}/{TOTAL_CAPTURES}")
            rp.hydra_texture.set_updates_enabled(True)
            await rep.orchestrator.step_async(rt_subframes=RT_SUBFRAMES)
            rp.hydra_texture.set_updates_enabled(False)

    # Cleanup.
    await rep.orchestrator.wait_until_complete_async()
    writer.detach()
    rp.destroy()

asyncio.ensure_future(run_workflow_async())
```

Standalone Application

```python
"""Generate palletized box stacks across randomized scenes.
Each scene chooses an environment, scatters pallets, builds box stacks, and captures camera views.
"""

import math
import os

from isaacsim import SimulationApp

simulation_app = SimulationApp(launch_config={"headless": False})

import carb
import carb.settings
import isaacsim.core.experimental.utils.bounds as bounds_utils
import omni.replicator.core as rep
import omni.usd
from isaacsim.storage.native import get_assets_root_path
from omni.replicator.core.scripts.functional import utils as rep_utils

DEFAULT_ENV_URLS = [
    "/Isaac/Environments/Simple_Warehouse/warehouse.usd",
    None,
]
PALLET_URL = "/Isaac/Environments/Simple_Warehouse/Props/SM_PaletteA_01.usd"
BOX_URLS = [
    "/Isaac/Environments/Simple_Warehouse/Props/SM_CardBoxC_01.usd",
    "/Isaac/Environments/Simple_Warehouse/Props/SM_CardBoxD_01.usd",
]

TOTAL_CAPTURES = 5
CAPTURES_PER_SCENE = 3
RESOLUTION = (1280, 720)
RT_SUBFRAMES = 8
PALLET_COUNT_RANGE = range(2, 6)
STACK_COUNT_RANGE = range(1, 4)
BOXES_PER_STACK_RANGE = range(1, 6)
STACK_SCATTER_AREA_SCALE = 0.9

def create_pallets_on_floor(scene_scope_path, assets_root_path, rng):
    pallet_count = int(rng.generator.choice(PALLET_COUNT_RANGE))
    # Use a hidden floor plane as a sampling surface so scattered pallets avoid each other.
    floor_plane = rep.functional.create.plane(
        parent=scene_scope_path,
        name="PalletScatterPlane",
        position=(0.0, 0.0, 0.0),
        scale=(5.0, 5.0, 1.0),
        visible=False,
    )

    pallets = []
    for i in range(pallet_count):
        pallets.append(
            rep.functional.create.reference(
                usd_path=assets_root_path + PALLET_URL,
                parent=scene_scope_path,
                name=f"Pallet_{i}",
                position=(i * 2.0, 0.0, 1.0),
                rotation=(0.0, 0.0, float(rng.generator.choice([0.0, 90.0, 180.0, 270.0]))),
                semantics={"class": "pallet"},
            )
        )

    simulation_app.update()
    rep.functional.randomizer.scatter_2d(pallets, floor_plane, check_for_collisions=True, rng=rng)
    simulation_app.update()

    bbox_cache = bounds_utils.create_bbox_cache()
    for pallet in pallets:
        aabb = bounds_utils.compute_aabb(pallet, bbox_cache=bbox_cache, include_children=True)
        origin = rep_utils.get_world_position(pallet)
        origin_to_bottom = float(origin[2] - aabb[2])
        # Move the pallet origin so the measured bottom sits on the floor.
        rep.functional.modify.pose(
            pallet,
            position_value=(float(origin[0]), float(origin[1]), origin_to_bottom),
            write_to_usd=True,
        )

    simulation_app.update()
    return pallets

def create_stacks_on_pallet(scene_scope_path, pallet_index, pallet, assets_root_path, rng):
    bbox_cache = bounds_utils.create_bbox_cache()
    pallet_bounds = bounds_utils.compute_aabb(pallet, bbox_cache=bbox_cache, include_children=True)
    pallet_origin = rep_utils.get_world_position(pallet)
    stack_count = int(rng.generator.choice(STACK_COUNT_RANGE))
    pallet_top_z = float(pallet_bounds[5])
    pallet_center_x = float(pallet_origin[0])
    pallet_center_y = float(pallet_origin[1])
    pallet_size_x = float(pallet_bounds[3] - pallet_bounds[0])
    pallet_size_y = float(pallet_bounds[4] - pallet_bounds[1])

    base_boxes = []
    stack_data = []
    for i in range(stack_count):
        box_url = BOX_URLS[int(rng.generator.integers(0, len(BOX_URLS)))]
        box = rep.functional.create.reference(
            usd_path=assets_root_path + box_url,
            parent=scene_scope_path,
            name=f"Pallet_{pallet_index}_BoxStack_{i}_Base",
            position=(i * 2.0, 0.0, pallet_top_z + 1.0),
            semantics={"class": "cardbox"},
        )
        base_boxes.append(box)
        stack_data.append(
            {
                "box": box,
                "url": assets_root_path + box_url,
                "height_count": int(rng.generator.choice(BOXES_PER_STACK_RANGE)),
            }
        )

    simulation_app.update()
    bbox_cache = bounds_utils.create_bbox_cache()
    max_box_height = 0.0
    for stack in stack_data:
        aabb = bounds_utils.compute_aabb(stack["box"], bbox_cache=bbox_cache, include_children=True)
        origin = rep_utils.get_world_position(stack["box"])
        stack["size"] = (
            float(aabb[3] - aabb[0]),
            float(aabb[4] - aabb[1]),
            float(aabb[5] - aabb[2]),
        )
        # Referenced box assets use an origin near the bottom, so keep this offset when stacking.
        stack["origin_to_bottom"] = float(origin[2] - aabb[2])
        max_box_height = max(max_box_height, stack["size"][2])

    # Scatter stack bases on a hidden plane smaller than the pallet top.
    scatter_plane = rep.functional.create.plane(
        parent=scene_scope_path,
        name=f"Pallet_{pallet_index}_StackScatterPlane",
        position=(pallet_center_x, pallet_center_y, pallet_top_z),
        scale=(pallet_size_x * STACK_SCATTER_AREA_SCALE, pallet_size_y * STACK_SCATTER_AREA_SCALE, 1.0),
        visible=False,
    )

    while True:
        try:
            rep.functional.randomizer.scatter_2d(
                base_boxes,
                scatter_plane,
                offset=max_box_height * 0.5,
                check_for_collisions=True,
                rng=rng,
            )
            break
        except ValueError:
            if len(base_boxes) <= 1:
                raise
            stack_data.pop()
            removed_box = base_boxes.pop()
            omni.usd.get_context().get_stage().RemovePrim(removed_box.GetPath())
            print(
                f"[SDG] Warning: could not scatter {len(base_boxes) + 1} stacks on pallet {pallet_index}; "
                f"retrying with {len(base_boxes)}."
            )
            simulation_app.update()
    simulation_app.update()

    all_boxes = list(base_boxes)
    for stack_idx, stack in enumerate(stack_data):
        _, _, box_height = stack["size"]
        origin_to_bottom = stack["origin_to_bottom"]
        origin = rep_utils.get_world_position(stack["box"])
        origin_x = float(origin[0])
        origin_y = float(origin[1])

        rep.functional.modify.pose(
            stack["box"],
            position_value=(origin_x, origin_y, pallet_top_z + origin_to_bottom),
            write_to_usd=True,
        )

        for level in range(1, stack["height_count"]):
            all_boxes.append(
                rep.functional.create.reference(
                    usd_path=stack["url"],
                    parent=scene_scope_path,
                    name=f"Pallet_{pallet_index}_BoxStack_{stack_idx}_{level}",
                    position=(origin_x, origin_y, pallet_top_z + origin_to_bottom + box_height * level),
                    semantics={"class": "cardbox"},
                )
            )

    return all_boxes

def randomize_camera(camera, pallet, rng):
    bbox_cache = bounds_utils.create_bbox_cache()
    pallet_bounds = bounds_utils.compute_aabb(pallet, bbox_cache=bbox_cache, include_children=True)
    pallet_origin = rep_utils.get_world_position(pallet)
    target = (
        float(pallet_origin[0]),
        float(pallet_origin[1]),
        float(pallet_bounds[5] + 0.5),
    )
    theta = float(rng.generator.uniform(0.0, 2.0 * math.pi))
    radius = float(rng.generator.uniform(2.4, 3.2))
    height = float(rng.generator.uniform(1.4, 2.2))
    rep.functional.modify.pose(
        camera,
        position_value=(
            target[0] + radius * math.cos(theta),
            target[1] + radius * math.sin(theta),
            target[2] + height,
        ),
        look_at_value=target,
        look_at_up_axis=(0, 0, 1),
        write_to_usd=True,
    )

def run_workflow():
    assets_root_path = get_assets_root_path()
    if assets_root_path is None:
        carb.log_error("[SDG] Could not resolve assets root path; aborting.")
        return

    # Create a clean stage for this tutorial workflow.
    omni.usd.get_context().new_stage()
    stage = omni.usd.get_context().get_stage()
    if stage is None:
        carb.log_error("[SDG] Could not create a new stage; aborting.")
        return

    # Disable automatic capture so only explicit `step()` calls write frames.
    rep.orchestrator.set_capture_on_play(False)

    # Set DLSS to Quality mode to reduce low-resolution SDG rendering artifacts.
    carb.settings.get_settings().set("rtx/post/dlss/execMode", 2)

    # Seed the randomizer so re-running the script produces the same scene.
    rng = rep.rng.ReplicatorRNG(seed=42)

    rep.functional.create.xform(name="World")
    rep.functional.create.xform(parent="/World", name="SDG")

    # Keep generated SDG content separate from the randomized environment.
    rep.functional.create.dome_light(intensity=500, parent="/World/SDG", name="DomeLight")

    # Use one camera and move it to each pallet before capturing.
    cam = rep.functional.create.camera(position=(3, 3, 3), look_at=(0, 0, 0), parent="/World/SDG", name="Camera")
    rp = rep.create.render_product(cam, RESOLUTION, name="rp_workflow_02")
    rp.hydra_texture.set_updates_enabled(False)

    # Attach a `BasicWriter` to save RGB and colorized semantic labels.
    backend = rep.backends.get("DiskBackend")
    out_dir = os.path.join(os.getcwd(), "_out_workflow_02")
    backend.initialize(output_dir=out_dir)
    print(f"[SDG] Output directory: {out_dir}")
    writer = rep.writers.get("BasicWriter")
    writer.initialize(
        backend=backend,
        rgb=True,
        semantic_segmentation=True,
        colorize_semantic_segmentation=True,
    )
    writer.attach(rp)

    environment_scope_path = "/World/Environment"
    capture_count = 0
    randomization_count = 0
    prev_scene_scope_path = None

    while capture_count < TOTAL_CAPTURES:
        randomization_count += 1
        print(f"[SDG] Randomization {randomization_count}")

        # Use a unique scene scope per randomization so Replicator's scatter mesh cache stays fresh.
        scene_scope_name = f"Scene_{randomization_count}"
        scene_scope_path = f"/World/SDG/{scene_scope_name}"

        if stage.GetPrimAtPath(environment_scope_path).IsValid():
            stage.RemovePrim(environment_scope_path)
        if prev_scene_scope_path is not None and stage.GetPrimAtPath(prev_scene_scope_path).IsValid():
            stage.RemovePrim(prev_scene_scope_path)
        simulation_app.update()

        rep.functional.create.scope(name="Environment", parent="/World")
        # Pick an environment; None means use a generated ground plane.
        env_url = DEFAULT_ENV_URLS[int(rng.generator.integers(0, len(DEFAULT_ENV_URLS)))]
        if env_url is None:
            ground = rep.functional.create.plane(
                parent=environment_scope_path,
                name="GroundPlane",
                scale=(100, 100, 1),
            )
            rep.functional.physics.apply_collider(ground)
        else:
            rep.functional.create.reference(
                usd_path=assets_root_path + env_url,
                parent=environment_scope_path,
                name="Scene",
            )

        rep.functional.create.scope(name=scene_scope_name, parent="/World/SDG")
        prev_scene_scope_path = scene_scope_path

        # Choose the pallet count, scatter them, shuffle the order, then build stacks.
        pallets = create_pallets_on_floor(scene_scope_path, assets_root_path, rng)
        pallet_order = list(range(len(pallets)))
        rng.generator.shuffle(pallet_order)
        pallets = [pallets[i] for i in pallet_order]
        for pallet_idx, pallet in enumerate(pallets):
            create_stacks_on_pallet(scene_scope_path, pallet_idx, pallet, assets_root_path, rng)

        captures_this_scene = min(CAPTURES_PER_SCENE, TOTAL_CAPTURES - capture_count)
        for capture_idx in range(captures_this_scene):
            pallet = pallets[capture_idx % len(pallets)]
            randomize_camera(cam, pallet, rng)

            capture_count += 1
            print(f"[SDG] Capture {capture_count}/{TOTAL_CAPTURES}")
            rp.hydra_texture.set_updates_enabled(True)
            rep.orchestrator.step(rt_subframes=RT_SUBFRAMES)
            rp.hydra_texture.set_updates_enabled(False)

    # Cleanup.
    rep.orchestrator.wait_until_complete()
    writer.detach()
    rp.destroy()

run_workflow()
```

Output directory `_out_workflow_02`: per captured frame, an `rgb_*.png`, a colorized `semantic_segmentation_*.png`, and a matching `*.json` label map.

## Troubleshooting

See [Replicator Troubleshooting](troubleshooting.html#isaac-sim-replicator-troubleshooting) for the full list.

* **Ghosting or artifacts in early captures.** Increase `rt_subframes` (see [above](#isaac-sim-app-tutorial-replicator-sdg-workflows-rt-subframes)).
* **Frames missing from the writer.** `wait_until_complete` was not called before exit.
* **Scattered assets overlap or land in the wrong place after a rebuild (Workflow 2).** The previous scene scope was not removed before authoring the new one, so Replicatorâs scatter-mesh cache reused stale planes.
* **Slow runs even though few frames are written.** The render product was left enabled during physics, scene construction, or randomization. Disable it and re-enable only around the orchestrator step.

## See Also

* [Getting Started Scripts](tutorial_replicator_getting_started.html#isaac-sim-app-tutorial-replicator-getting-started) - smaller, single-concept scripts that introduce the same settings in isolation.
* [Scene Based SDG](tutorial_replicator_scene_based_sdg.html#isaac-sim-app-tutorial-replicator-scene-based-sdg) - large-scale configurable dataset generation.
* [Object Based SDG](tutorial_replicator_object_based_sdg.html#isaac-sim-app-tutorial-replicator-object-based-sdg) - physics-heavy object drops with multiple cameras.
* [Writer examples](https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator/writer_examples.html "(in Omniverse Extensions)") and [custom writer guide](https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator/custom_writer.html "(in Omniverse Extensions)") - write a different output format.
* [Annotators](https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator/annotators_details.html "(in Omniverse Extensions)") - the full set of data sources available to writers.
* [I/O Optimization Guide](https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator/io_guidelines.html "(in Omniverse Extensions)") - scaling to large datasets.
* [Performance Optimization Handbook](../reference_material/sim_performance_optimization_handbook.html#isaac-sim-performance-optimization-handbook) - full set of `rtx/post/dlss/execMode` values and other render settings.
* [Replicator Troubleshooting](troubleshooting.html#isaac-sim-replicator-troubleshooting).

On this page

* [Prerequisites](#prerequisites)
* [Setup and Configuration](#setup-and-configuration)
* [Writers and Backends](#writers-and-backends)
* [Capture on Play Flag](#capture-on-play-flag)
* [Orchestrator Step](#orchestrator-step)
* [RT Subframes](#rt-subframes)
* [DLSS Quality Mode](#dlss-quality-mode)
* [Render Product Updates](#render-product-updates)
* [Seeded Randomization](#seeded-randomization)
* [Wait Until Complete](#wait-until-complete)
* [Async vs Sync](#async-vs-sync)
* [Examples](#examples)
  + [Workflow 1: Physics-Based Object Settling](#workflow-1-physics-based-object-settling)
  + [Workflow 2: Collision-Checked Asset Placement](#workflow-2-collision-checked-asset-placement)
* [Troubleshooting](#troubleshooting)
* [See Also](#see-also)

---

### Object-Based SDG

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/replicator_tutorials/tutorial_replicator_object_based_sdg.html

* [Synthetic Data Generation](../synthetic_data_generation/index.html)
* [Perception Data Generation (Replicator)](index.html)
* Object Based Synthetic Dataset Generation

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Object Based Synthetic Dataset Generation

This document is an example of using Isaac Sim and [Replicator](https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator.html "(in Omniverse Extensions)") to generate object-centric synthetic datasets. The script spawns labeled and distractor assets in a predefined area (closed off with invisible collision walls) and captures scenes from multiple camera viewpoints. The script also demonstrates how to randomize the camera poses, apply random velocities to the objects, and trigger custom events to randomize the scene. The randomizers can be Replicator-based or custom Isaac Sim/USD API based and can be triggered at specific times.

## Learning Objectives

The goal of this tutorial is to demonstrate how to use Isaac Sim and [replicator randomizers](https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator/randomizer_details.html "(in Omniverse Extensions)") in a hybrid way in simulated environments. The tutorial covers the following topics:

* How to create a custom USD stage and add [rigid-body](https://docs.omniverse.nvidia.com/kit/docs/omni_physics/latest/dev_guide/rigid_bodies_articulations/rigid_bodies.html "(in Omni Physics)") enabled assets with colliders.

  > + How to spawn and add colliders and rigid body dynamics to assets.
  > + How to create a collision box area around the assets to prevent them from drifting away.
  > + How to add a physics scene and set custom physics settings.
* How to create custom randomizers and trigger them at specific times.

  > + How to randomize the camera poses to look at a random target asset.
  > + How to randomize the shape distractor colors and apply random velocities to the floating shape distractors.
  > + How to randomize the lights in the working area and the dome background.
* How to capture motion blur by combining the number of pathtraced subframes samples simulated for the given duration.

  > + How to enable motion blur and set the number of sub samples to render for motion blur in PathTracing mode.
  > + How to set the render mode to PathTracing.
* How to create a custom synthetic dataset generation pipeline.
* Performance optimization by enabling rendering and data processing only for the frames to be captured.
* Use custom writers to export the data.

## Prerequisites

* Familiarity with USD / Isaac Sim APIs for creating and manipulating USD stages.
* Familiarity with [omni.replicator](https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator.html "(in Omniverse Extensions)"), its [writers](https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator/writer_examples.html "(in Omniverse Extensions)"), and [randomizers](https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator/randomizer_details.html "(in Omniverse Extensions)").
* Basic understanding of [OmniGraph](https://docs.omniverse.nvidia.com/extensions/latest/ext_omnigraph.html "(in Omniverse Extensions)") for the Replicator randomization and trigger pipeline.
* Familiarity with [rigid-body](https://docs.omniverse.nvidia.com/kit/docs/omni_physics/latest/dev_guide/rigid_bodies_articulations/rigid_bodies.html "(in Omni Physics)") dynamics and physics simulation in Isaac Sim.
* Running simulations as [Standalone Applications](../introduction/workflows.html#standalone-application) or via the [Script Editor](../development_tools/omniverse_script_editor.html#script-editor).

## Getting Started

The main script of the tutorial is located at `<install_path>/standalone_examples/replicator/object_based_sdg/object_based_sdg.py` with its util functions at `<install_path>/standalone_examples/replicator/object_based_sdg/object_based_sdg_utils.py`.

* The script can be run as a standalone application (on Windows use `python.bat` instead of `python.sh`):

```python
./python.sh standalone_examples/replicator/object_based_sdg/object_based_sdg.py
```

To overwrite the default configuration parameters, you can provide custom config files as a command-line argument for the script by using `--config <path/to/file.json/yaml>`. Example config files are stored in `<install_path>/standalone_examples/replicator/object_based_sdg/config/*`.

* Example of running the script with a custom config file:

```python
./python.sh standalone_examples/replicator/object_based_sdg/object_based_sdg.py \
    --config standalone_examples/replicator/object_based_sdg/config/<example_config>.yaml
```

## Implementation

The following section provides an implementation overview of the script. It includes details regarding the configuration parameters, scene generation helper functions, randomizations (Isaac Sim and Replicator), and data capture loop.

The complete implementation consists of two files: the main script and a utilities module.

Script Editor

Utils module and main script

```python
import asyncio
import os
import random
import time
from itertools import chain

import carb.settings
import numpy as np
import omni.kit.app
import omni.replicator.core as rep
import omni.timeline
import omni.usd
from isaacsim.core.experimental.utils.semantics import add_labels, remove_all_labels, upgrade_prim_semantics_to_labels
from isaacsim.storage.native import get_assets_root_path
from omni.kit.viewport.utility import get_active_viewport
from omni.physx import get_physx_interface, get_physx_scene_query_interface
from pxr import Gf, PhysxSchema, Sdf, Usd, UsdGeom, UsdPhysics

def add_colliders(root_prim: Usd.Prim) -> None:
    """Enable collisions on the asset (without rigid body dynamics the asset will be static)."""
    for desc_prim in Usd.PrimRange(root_prim):
        if desc_prim.IsA(UsdGeom.Mesh) or desc_prim.IsA(UsdGeom.Gprim):
            if not desc_prim.HasAPI(UsdPhysics.CollisionAPI):
                collision_api = UsdPhysics.CollisionAPI.Apply(desc_prim)
            else:
                collision_api = UsdPhysics.CollisionAPI(desc_prim)
            collision_api.CreateCollisionEnabledAttr(True)
            if not desc_prim.HasAPI(PhysxSchema.PhysxCollisionAPI):
                physx_collision_api = PhysxSchema.PhysxCollisionAPI.Apply(desc_prim)
            else:
                physx_collision_api = PhysxSchema.PhysxCollisionAPI(desc_prim)
            physx_collision_api.CreateContactOffsetAttr(0.001)
            physx_collision_api.CreateRestOffsetAttr(0.0)
        if desc_prim.IsA(UsdGeom.Mesh):
            if not desc_prim.HasAPI(UsdPhysics.MeshCollisionAPI):
                mesh_collision_api = UsdPhysics.MeshCollisionAPI.Apply(desc_prim)
            else:
                mesh_collision_api = UsdPhysics.MeshCollisionAPI(desc_prim)
            mesh_collision_api.CreateApproximationAttr().Set("convexHull")

def create_collision_box_walls(
    stage: Usd.Stage,
    path: str,
    width: float,
    depth: float,
    height: float,
    thickness: float = 0.5,
    visible: bool = False,
) -> None:
    """Create a collision box area wrapping the given working area with origin at (0, 0, 0)."""
    walls = [
        ("floor", (0, 0, (height + thickness) / -2.0), (width, depth, thickness)),
        ("ceiling", (0, 0, (height + thickness) / 2.0), (width, depth, thickness)),
        ("left_wall", ((width + thickness) / -2.0, 0, 0), (thickness, depth, height)),
        ("right_wall", ((width + thickness) / 2.0, 0, 0), (thickness, depth, height)),
        ("front_wall", (0, (depth + thickness) / 2.0, 0), (width, thickness, height)),
        ("back_wall", (0, (depth + thickness) / -2.0, 0), (width, thickness, height)),
    ]
    for name, location, size in walls:
        prim = stage.DefinePrim(f"{path}/{name}", "Cube")
        scale = (size[0] / 2.0, size[1] / 2.0, size[2] / 2.0)
        rep.functional.modify.pose(prim, position_value=location, scale_value=scale)
        add_colliders(prim)
        if not visible:
            UsdGeom.Imageable(prim).MakeInvisible()

def get_random_transform_values(
    loc_min=(0, 0, 0), loc_max=(1, 1, 1), rot_min=(0, 0, 0), rot_max=(360, 360, 360), scale_min_max=(0.1, 1.0)
):
    """Create random transformation values for location, rotation, and scale."""
    location = (
        random.uniform(loc_min[0], loc_max[0]),
        random.uniform(loc_min[1], loc_max[1]),
        random.uniform(loc_min[2], loc_max[2]),
    )
    rotation = (
        random.uniform(rot_min[0], rot_max[0]),
        random.uniform(rot_min[1], rot_max[1]),
        random.uniform(rot_min[2], rot_max[2]),
    )
    scale = tuple([random.uniform(scale_min_max[0], scale_min_max[1])] * 3)
    return location, rotation, scale

def get_random_pose_on_sphere(origin, radius, camera_forward_axis=(0, 0, -1)):
    """Generate a random pose on a sphere looking at the origin."""
    origin = Gf.Vec3f(origin)
    camera_forward_axis = Gf.Vec3f(camera_forward_axis)
    theta = np.random.uniform(0, 2 * np.pi)
    phi = np.arcsin(np.random.uniform(-1, 1))
    x = radius * np.cos(theta) * np.cos(phi)
    y = radius * np.sin(phi)
    z = radius * np.sin(theta) * np.cos(phi)
    location = origin + Gf.Vec3f(x, y, z)
    direction = origin - location
    direction_normalized = direction.GetNormalized()
    rotation = Gf.Rotation(Gf.Vec3d(camera_forward_axis), Gf.Vec3d(direction_normalized))
    orientation = Gf.Quatf(rotation.GetQuat())
    return location, orientation

def set_render_products_updates(render_products, enabled, include_viewport=False):
    """Enable or disable the render products and viewport rendering."""
    for rp in render_products:
        rp.hydra_texture.set_updates_enabled(enabled)
    if include_viewport:
        get_active_viewport().updates_enabled = enabled

def apply_velocities_towards_target(prims, target=(0, 0, 0), strength_range=(0.1, 1.0)):
    """Apply velocities to prims directing them towards a target point."""
    for prim in prims:
        loc = prim.GetAttribute("xformOp:translate").Get()
        strength = random.uniform(strength_range[0], strength_range[1])
        velocity = (
            (target[0] - loc[0]) * strength,
            (target[1] - loc[1]) * strength,
            (target[2] - loc[2]) * strength,
        )
        prim.GetAttribute("physics:velocity").Set(velocity)

def apply_random_velocities(prims, linear_range=(-2.5, 2.5), angular_range=(-45, 45)):
    """Apply random linear and angular velocities to prims."""
    for prim in prims:
        lin_vel = (
            random.uniform(linear_range[0], linear_range[1]),
            random.uniform(linear_range[0], linear_range[1]),
            random.uniform(linear_range[0], linear_range[1]),
        )
        ang_vel = (
            random.uniform(angular_range[0], angular_range[1]),
            random.uniform(angular_range[0], angular_range[1]),
            random.uniform(angular_range[0], angular_range[1]),
        )
        prim.GetAttribute("physics:velocity").Set(lin_vel)
        prim.GetAttribute("physics:angularVelocity").Set(ang_vel)

async def run_example_async(config: dict) -> None:
    """Run the object-based SDG example asynchronously."""
    assets_root_path = get_assets_root_path()
    stage = None

    # ENVIRONMENT
    env_url = config.get("env_url", "")
    if env_url:
        env_path = env_url if env_url.startswith("omniverse://") else assets_root_path + env_url
        omni.usd.get_context().open_stage(env_path)
        stage = omni.usd.get_context().get_stage()
        for prim in stage.Traverse():
            upgrade_prim_semantics_to_labels(prim, include_descendants=True)
            remove_all_labels(prim, include_descendants=True)
    else:
        omni.usd.get_context().new_stage()
        stage = omni.usd.get_context().get_stage()
        rep.functional.create.xform(name="World")
        rep.functional.create.distant_light(intensity=400.0, rotation=(0, 60, 0), name="DistantLight")

    working_area_size = config.get("working_area_size", (3, 3, 3))
    working_area_min = (working_area_size[0] / -2, working_area_size[1] / -2, working_area_size[2] / -2)
    working_area_max = (working_area_size[0] / 2, working_area_size[1] / 2, working_area_size[2] / 2)

    create_collision_box_walls(
        stage, "/World/CollisionWalls", working_area_size[0], working_area_size[1], working_area_size[2]
    )

    rep.functional.physics.create_physics_scene("/PhysicsScene", timeStepsPerSecond=60)
    physx_scene = PhysxSchema.PhysxSceneAPI.Apply(stage.GetPrimAtPath("/PhysicsScene"))

    # TRAINING ASSETS
    labeled_assets_and_properties = config.get("labeled_assets_and_properties", [])
    floating_labeled_prims = []
    falling_labeled_prims = []
    labeled_prims = []
    rep.functional.create.scope(name="Labeled", parent="/World")
    for obj in labeled_assets_and_properties:
        obj_url = obj.get("url", "")
        label = obj.get("label", "unknown")
        count = obj.get("count", 1)
        floating = obj.get("floating", False)
        scale_min_max = obj.get("randomize_scale", (1, 1))
        for i in range(count):
            rand_loc, rand_rot, rand_scale = get_random_transform_values(
                loc_min=working_area_min, loc_max=working_area_max, scale_min_max=scale_min_max
            )
            asset_path = obj_url if obj_url.startswith("omniverse://") else assets_root_path + obj_url
            prim = rep.functional.create.reference(
                usd_path=asset_path,
                parent="/World/Labeled",
                name=label,
                position=rand_loc,
                rotation=rand_rot,
                scale=rand_scale,
            )
            add_colliders(prim)
            rep.functional.physics.apply_rigid_body(prim, disableGravity=floating)
            add_labels(prim, labels=[label], taxonomy="class")
            if floating:
                floating_labeled_prims.append(prim)
            else:
                falling_labeled_prims.append(prim)
    labeled_prims = floating_labeled_prims + falling_labeled_prims

    # DISTRACTORS
    shape_distractors_types = config.get("shape_distractors_types", ["capsule", "cone", "cylinder", "sphere", "cube"])
    shape_distractors_scale_min_max = config.get("shape_distractors_scale_min_max", (0.02, 0.2))
    shape_distractors_num = config.get("shape_distractors_num", 350)
    shape_distractors = []
    floating_shape_distractors = []
    falling_shape_distractors = []
    for i in range(shape_distractors_num):
        rand_loc, rand_rot, rand_scale = get_random_transform_values(
            loc_min=working_area_min, loc_max=working_area_max, scale_min_max=shape_distractors_scale_min_max
        )
        rand_shape = random.choice(shape_distractors_types)
        prim_path = omni.usd.get_stage_next_free_path(stage, f"/World/Distractors/{rand_shape}", False)
        prim = stage.DefinePrim(prim_path, rand_shape.capitalize())
        rep.functional.modify.pose(prim, position_value=rand_loc, rotation_value=rand_rot, scale_value=rand_scale)
        disable_gravity = random.choice([True, False])
        add_colliders(prim)
        rep.functional.physics.apply_rigid_body(prim, disableGravity=disable_gravity)
        if disable_gravity:
            floating_shape_distractors.append(prim)
        else:
            falling_shape_distractors.append(prim)
        shape_distractors.append(prim)

    mesh_distactors_urls = config.get("mesh_distractors_urls", [])
    mesh_distactors_scale_min_max = config.get("mesh_distractors_scale_min_max", (0.1, 2.0))
    mesh_distactors_num = config.get("mesh_distractors_num", 10)
    mesh_distractors = []
    floating_mesh_distractors = []
    falling_mesh_distractors = []
    for i in range(mesh_distactors_num):
        rand_loc, rand_rot, rand_scale = get_random_transform_values(
            loc_min=working_area_min, loc_max=working_area_max, scale_min_max=mesh_distactors_scale_min_max
        )
        mesh_url = random.choice(mesh_distactors_urls)
        prim_name = os.path.basename(mesh_url).split(".")[0]
        asset_path = mesh_url if mesh_url.startswith("omniverse://") else assets_root_path + mesh_url
        prim = rep.functional.create.reference(
            usd_path=asset_path,
            parent="/World/Distractors",
            name=prim_name,
            position=rand_loc,
            rotation=rand_rot,
            scale=rand_scale,
        )
        disable_gravity = random.choice([True, False])
        add_colliders(prim)
        rep.functional.physics.apply_rigid_body(prim, disableGravity=disable_gravity)
        if disable_gravity:
            floating_mesh_distractors.append(prim)
        else:
            falling_mesh_distractors.append(prim)
        mesh_distractors.append(prim)
        upgrade_prim_semantics_to_labels(prim, include_descendants=True)
        remove_all_labels(prim, include_descendants=True)

    # REPLICATOR
    rep.set_global_seed(42)
    random.seed(42)
    rep.orchestrator.set_capture_on_play(False)
    carb.settings.get_settings().set("rtx/post/dlss/execMode", 2)

    cameras = []
    num_cameras = config.get("num_cameras", 1)
    camera_properties_kwargs = config.get("camera_properties_kwargs", {})
    rep.functional.create.scope(name="Cameras", parent="/World")
    for i in range(num_cameras):
        cam_prim = rep.functional.create.camera(parent="/World/Cameras", name="cam", **camera_properties_kwargs)
        cameras.append(cam_prim)

    camera_colliders = []
    camera_collider_radius = config.get("camera_collider_radius", 0)
    if camera_collider_radius > 0:
        for cam in cameras:
            cam_path = cam.GetPath()
            cam_collider = stage.DefinePrim(f"{cam_path}/CollisionSphere", "Sphere")
            cam_collider.GetAttribute("radius").Set(camera_collider_radius)
            rep.functional.physics.apply_collider(cam_collider)
            collision_api = UsdPhysics.CollisionAPI(cam_collider)
            collision_api.GetCollisionEnabledAttr().Set(False)
            UsdGeom.Imageable(cam_collider).MakeInvisible()
            camera_colliders.append(cam_collider)

    await omni.kit.app.get_app().next_update_async()

    render_products = []
    resolution = config.get("resolution", (640, 480))
    for cam in cameras:
        rp = rep.create.render_product(cam.GetPath(), resolution)
        render_products.append(rp)

    disable_render_products_between_captures = config.get("disable_render_products_between_captures", True)
    if disable_render_products_between_captures:
        set_render_products_updates(render_products, False, include_viewport=False)

    writer_type = config.get("writer_type", None)
    writer_kwargs = config.get("writer_kwargs", {})
    if out_dir := writer_kwargs.get("output_dir"):
        if not os.path.isabs(out_dir):
            out_dir = os.path.join(os.getcwd(), out_dir)
            writer_kwargs["output_dir"] = out_dir
        print(f"[SDG] Writing data to: {out_dir}")
    if writer_type is not None and len(render_products) > 0:
        writer = rep.writers.get(writer_type)
        writer.initialize(**writer_kwargs)
        writer.attach(render_products)

    # RANDOMIZERS
    def on_overlap_hit(hit) -> bool:
        prim = omni.usd.get_context().get_stage().GetPrimAtPath(str(hit.rigid_body))
        if prim not in camera_colliders:
            rand_vel = (random.uniform(-2, 2), random.uniform(-2, 2), random.uniform(4, 8))
            prim.GetAttribute("physics:velocity").Set(rand_vel)
        return True

    overlap_area_thickness = 0.1
    overlap_area_origin = (0, 0, (-working_area_size[2] / 2) + (overlap_area_thickness / 2))
    overlap_area_extent = (
        working_area_size[0] / 2 * 0.99,
        working_area_size[1] / 2 * 0.99,
        overlap_area_thickness / 2 * 0.99,
    )

    def on_physics_step(dt: float) -> None:
        get_physx_scene_query_interface().overlap_box(
            carb.Float3(overlap_area_extent),
            carb.Float3(overlap_area_origin),
            carb.Float4(0, 0, 0, 1),
            on_overlap_hit,
            False,
        )

    physx_sub = get_physx_interface().subscribe_physics_step_events(on_physics_step)

    camera_distance_to_target_min_max = config.get("camera_distance_to_target_min_max", (0.1, 0.5))
    camera_look_at_target_offset = config.get("camera_look_at_target_offset", 0.2)

    def randomize_camera_poses() -> None:
        for cam in cameras:
            target_asset = random.choice(labeled_prims)
            loc_offset = (
                random.uniform(-camera_look_at_target_offset, camera_look_at_target_offset),
                random.uniform(-camera_look_at_target_offset, camera_look_at_target_offset),
                random.uniform(-camera_look_at_target_offset, camera_look_at_target_offset),
            )
            target_loc = target_asset.GetAttribute("xformOp:translate").Get() + loc_offset
            distance = random.uniform(camera_distance_to_target_min_max[0], camera_distance_to_target_min_max[1])
            cam_loc, quat = get_random_pose_on_sphere(origin=target_loc, radius=distance)
            rep.functional.modify.pose(cam, position_value=cam_loc, rotation_value=quat)

    async def simulate_camera_collision_async(num_frames: int = 1) -> None:
        for cam_collider in camera_colliders:
            collision_api = UsdPhysics.CollisionAPI(cam_collider)
            collision_api.GetCollisionEnabledAttr().Set(True)
        if not timeline.is_playing():
            timeline.play()
        for _ in range(num_frames):
            await omni.kit.app.get_app().next_update_async()
        for cam_collider in camera_colliders:
            collision_api = UsdPhysics.CollisionAPI(cam_collider)
            collision_api.GetCollisionEnabledAttr().Set(False)

    with rep.trigger.on_custom_event(event_name="randomize_shape_distractor_colors"):
        shape_distractors_paths = [
            prim.GetPath() for prim in chain(floating_shape_distractors, falling_shape_distractors)
        ]
        shape_distractors_group = rep.create.group(shape_distractors_paths)
        with shape_distractors_group:
            rep.randomizer.color(colors=rep.distribution.uniform((0, 0, 0), (1, 1, 1)))

    with rep.trigger.on_custom_event(event_name="randomize_lights"):
        lights = rep.create.light(
            light_type="Sphere",
            color=rep.distribution.uniform((0, 0, 0), (1, 1, 1)),
            temperature=rep.distribution.normal(6500, 500),
            intensity=rep.distribution.normal(35000, 5000),
            position=rep.distribution.uniform(working_area_min, working_area_max),
            scale=rep.distribution.uniform(0.1, 1),
            count=3,
        )

    with rep.trigger.on_custom_event(event_name="randomize_dome_background"):
        dome_textures = [
            assets_root_path + "/NVIDIA/Assets/Skies/Indoor/autoshop_01_4k.hdr",
            assets_root_path + "/NVIDIA/Assets/Skies/Indoor/carpentry_shop_01_4k.hdr",
            assets_root_path + "/NVIDIA/Assets/Skies/Indoor/hotel_room_4k.hdr",
            assets_root_path + "/NVIDIA/Assets/Skies/Indoor/wooden_lounge_4k.hdr",
        ]
        dome_light = rep.create.light(light_type="Dome")
        with dome_light:
            rep.modify.attribute("inputs:texture:file", rep.distribution.choice(dome_textures))
            rep.randomizer.rotation()

    async def capture_with_motion_blur_and_pathtracing_async(
        duration: float = 0.05, num_samples: int = 8, spp: int = 64
    ) -> None:
        orig_physics_fps = physx_scene.GetTimeStepsPerSecondAttr().Get()
        target_physics_fps = 1 / duration * num_samples
        if target_physics_fps > orig_physics_fps:
            physx_scene.GetTimeStepsPerSecondAttr().Set(target_physics_fps)
        is_motion_blur_enabled = carb.settings.get_settings().get("/omni/replicator/captureMotionBlur")
        if not is_motion_blur_enabled:
            carb.settings.get_settings().set("/omni/replicator/captureMotionBlur", True)
        carb.settings.get_settings().set("/omni/replicator/pathTracedMotionBlurSubSamples", num_samples)
        prev_render_mode = carb.settings.get_settings().get("/rtx/rendermode")
        carb.settings.get_settings().set("/rtx/rendermode", "PathTracing")
        carb.settings.get_settings().set("/rtx/pathtracing/spp", spp)
        carb.settings.get_settings().set("/rtx/pathtracing/totalSpp", spp)
        carb.settings.get_settings().set("/rtx/pathtracing/optixDenoiser/enabled", 0)
        if not timeline.is_playing():
            timeline.play()
        await rep.orchestrator.step_async(delta_time=duration, pause_timeline=False)
        if target_physics_fps > orig_physics_fps:
            physx_scene.GetTimeStepsPerSecondAttr().Set(orig_physics_fps)
        carb.settings.get_settings().set("/omni/replicator/captureMotionBlur", is_motion_blur_enabled)
        carb.settings.get_settings().set("/rtx/rendermode", prev_render_mode)

    async def run_simulation_loop_async(duration: float) -> None:
        timeline = omni.timeline.get_timeline_interface()
        if not timeline.is_playing():
            timeline.play()
        elapsed_time = 0.0
        previous_time = timeline.get_current_time()
        while elapsed_time <= duration:
            await omni.kit.app.get_app().next_update_async()
            elapsed_time += timeline.get_current_time() - previous_time
            previous_time = timeline.get_current_time()

    # SDG
    num_frames = config.get("num_frames", 10)
    rt_subframes = config.get("rt_subframes", -1)
    sim_duration_between_captures = config.get("simulation_duration_between_captures", 0.025)

    rep.utils.send_og_event(event_name="randomize_shape_distractor_colors")
    rep.utils.send_og_event(event_name="randomize_dome_background")
    for _ in range(5):
        await omni.kit.app.get_app().next_update_async()

    timeline = omni.timeline.get_timeline_interface()
    timeline.set_start_time(0)
    timeline.set_end_time(1000000)
    timeline.set_looping(False)
    timeline.play()
    timeline.commit()
    await omni.kit.app.get_app().next_update_async()

    wall_time_start = time.perf_counter()

    for i in range(num_frames):
        if i % 3 == 0:
            randomize_camera_poses()
            if camera_colliders:
                await simulate_camera_collision_async(num_frames=4)
        if i % 10 == 0:
            apply_velocities_towards_target(list(chain(labeled_prims, shape_distractors, mesh_distractors)))
        if i % 5 == 0:
            rep.utils.send_og_event(event_name="randomize_lights")
        if i % 15 == 0:
            rep.utils.send_og_event(event_name="randomize_shape_distractor_colors")
        if i % 25 == 0:
            rep.utils.send_og_event(event_name="randomize_dome_background")
        if i % 17 == 0:
            apply_random_velocities(list(chain(floating_shape_distractors, floating_mesh_distractors)))

        if disable_render_products_between_captures:
            set_render_products_updates(render_products, True, include_viewport=False)

        print(f"[SDG] Capturing frame {i}/{num_frames}, at simulation time: {timeline.get_current_time():.2f}")
        if i % 5 == 0:
            await capture_with_motion_blur_and_pathtracing_async(duration=0.025, num_samples=8, spp=128)
        else:
            await rep.orchestrator.step_async(delta_time=0.0, rt_subframes=rt_subframes, pause_timeline=False)

        if disable_render_products_between_captures:
            set_render_products_updates(render_products, False, include_viewport=False)

        if sim_duration_between_captures > 0:
            await run_simulation_loop_async(sim_duration_between_captures)
        else:
            await omni.kit.app.get_app().next_update_async()

    await rep.orchestrator.wait_until_complete_async()

    wall_duration = time.perf_counter() - wall_time_start
    sim_duration = timeline.get_current_time()
    num_captures = num_frames * num_cameras
    print(
        f"[SDG] Captured {num_frames} frames, {num_captures} entries in {wall_duration:.2f} seconds.\n"
        f"\t Simulation duration: {sim_duration:.2f}\n"
    )

    physx_sub.unsubscribe()
    physx_sub = None
    await omni.kit.app.get_app().next_update_async()
    timeline.stop()

config = {
    "env_url": "",
    "working_area_size": (5, 5, 3),
    "rt_subframes": 4,
    "num_frames": 10,
    "num_cameras": 2,
    "camera_collider_radius": 1.25,
    "disable_render_products_between_captures": False,
    "simulation_duration_between_captures": 0.05,
    "resolution": (640, 480),
    "camera_properties_kwargs": {
        "focal_length": 24.0,
        "focus_distance": 400,
        "f_stop": 0.0,
        "clipping_range": (0.01, 10000),
    },
    "camera_look_at_target_offset": 0.15,
    "camera_distance_to_target_min_max": (0.25, 0.75),
    "writer_type": "PoseWriter",
    "writer_kwargs": {
        "output_dir": "_out_obj_based_sdg_pose_writer",
        "format": None,
        "use_subfolders": False,
        "write_debug_images": True,
        "skip_empty_frames": False,
    },
    "labeled_assets_and_properties": [
        {
            "url": "/Isaac/Props/YCB/Axis_Aligned/008_pudding_box.usd",
            "label": "pudding_box",
            "count": 5,
            "floating": True,
            "scale_min_max": (0.85, 1.25),
        },
        {
            "url": "/Isaac/Props/YCB/Axis_Aligned_Physics/006_mustard_bottle.usd",
            "label": "mustard_bottle",
            "count": 7,
            "floating": False,
            "scale_min_max": (0.85, 3.25),
        },
    ],
    "shape_distractors_types": ["capsule", "cone", "cylinder", "sphere", "cube"],
    "shape_distractors_scale_min_max": (0.015, 0.15),
    "shape_distractors_num": 150,
    "mesh_distractors_urls": [
        "/Isaac/Environments/Simple_Warehouse/Props/SM_CardBoxD_04_1847.usd",
        "/Isaac/Environments/Simple_Warehouse/Props/SM_CardBoxA_01_414.usd",
        "/Isaac/Environments/Simple_Warehouse/Props/S_TrafficCone.usd",
    ],
    "mesh_distractors_scale_min_max": (0.35, 1.35),
    "mesh_distractors_num": 75,
}

asyncio.ensure_future(run_example_async(config))
```

Standalone Application

Main script

```python
"""Generate synthetic data using object-based scene randomization."""

import argparse
import json
import os

import yaml
from isaacsim import SimulationApp

# Default config dict, can be updated/replaced using json/yaml config files ('--config' cli argument)
config = {
    "launch_config": {
        "renderer": "RealTimePathTracing",
        "headless": False,
    },
    "env_url": "",
    "working_area_size": (4, 4, 3),
    "rt_subframes": 4,
    "num_frames": 4,
    "num_cameras": 2,
    "camera_collider_radius": 0.5,
    "disable_render_products_between_captures": False,
    "simulation_duration_between_captures": 0.05,
    "resolution": (640, 480),
    "camera_properties_kwargs": {
        "focal_length": 24.0,
        "focus_distance": 400,
        "f_stop": 0.0,
        "clipping_range": (0.01, 10000),
    },
    "camera_look_at_target_offset": 0.15,
    "camera_distance_to_target_min_max": (0.25, 0.75),
    "writer_type": "PoseWriter",
    "writer_kwargs": {
        "output_dir": "_out_obj_based_sdg_pose_writer",
        "format": None,
        "use_subfolders": False,
        "write_debug_images": True,
        "skip_empty_frames": False,
    },
    "labeled_assets_and_properties": [
        {
            "url": "/Isaac/Props/YCB/Axis_Aligned/008_pudding_box.usd",
            "label": "pudding_box",
            "count": 5,
            "floating": True,
            "scale_min_max": (0.85, 1.25),
        },
        {
            "url": "/Isaac/Props/YCB/Axis_Aligned_Physics/006_mustard_bottle.usd",
            "label": "mustard_bottle",
            "count": 7,
            "floating": True,
            "scale_min_max": (0.85, 1.25),
        },
    ],
    "shape_distractors_types": ["capsule", "cone", "cylinder", "sphere", "cube"],
    "shape_distractors_scale_min_max": (0.015, 0.15),
    "shape_distractors_num": 350,
    "mesh_distractors_urls": [
        "/Isaac/Environments/Simple_Warehouse/Props/SM_CardBoxD_04_1847.usd",
        "/Isaac/Environments/Simple_Warehouse/Props/SM_CardBoxA_01_414.usd",
        "/Isaac/Environments/Simple_Warehouse/Props/S_TrafficCone.usd",
    ],
    "mesh_distractors_scale_min_max": (0.35, 1.35),
    "mesh_distractors_num": 75,
}

import carb

# Check if there are any config files (yaml or json) are passed as arguments
parser = argparse.ArgumentParser()
parser.add_argument("--config", required=False, help="Include specific config parameters (json or yaml))")
args, unknown = parser.parse_known_args()
args_config = {}
if args.config and os.path.isfile(args.config):
    with open(args.config) as f:
        if args.config.endswith(".json"):
            args_config = json.load(f)
        elif args.config.endswith(".yaml"):
            args_config = yaml.safe_load(f)
        else:
            carb.log_warn(f"File {args.config} is not json or yaml, will use default config")
else:
    carb.log_warn(f"File {args.config} does not exist, will use default config")

# Update the default config dict with the external one
config.update(args_config)

print(f"[SDG] Using config:\n{config}")

launch_config = config.get("launch_config", {})
simulation_app = SimulationApp(launch_config=launch_config)

import random
import time
from itertools import chain

import carb.settings

# Custom util functions for the example
import object_based_sdg_utils
import omni.physics.core
import omni.replicator.core as rep
import omni.timeline
import omni.usd
from isaacsim.core.utils.semantics import add_labels, remove_labels, upgrade_prim_semantics_to_labels
from isaacsim.storage.native import get_assets_root_path
from omni.physics.core import get_physics_scene_query_interface
from pxr import PhysicsSchemaTools, PhysxSchema, UsdGeom, UsdPhysics

# Isaac nucleus assets root path
assets_root_path = get_assets_root_path()
stage = None

# ENVIRONMENT
# Create an empty or load a custom stage (clearing any previous semantics)
env_url = config.get("env_url", "")
if env_url:
    env_path = env_url if env_url.startswith("omniverse://") else assets_root_path + env_url
    omni.usd.get_context().open_stage(env_path)
    stage = omni.usd.get_context().get_stage()
    # Remove any previous semantics in the loaded stage
    for prim in stage.Traverse():
        # Make sure old semantics api are upgraded to the new labels api
        upgrade_prim_semantics_to_labels(prim, include_descendants=True)
        remove_labels(prim, include_descendants=True)
else:
    omni.usd.get_context().new_stage()
    stage = omni.usd.get_context().get_stage()
    rep.functional.create.xform(name="World")
    rep.functional.create.distant_light(intensity=400.0, rotation=(0, 60, 0), name="DistantLight")

# Get the working area size and bounds (width=x, depth=y, height=z)
working_area_size = config.get("working_area_size", (3, 3, 3))
working_area_min = (working_area_size[0] / -2, working_area_size[1] / -2, working_area_size[2] / -2)
working_area_max = (working_area_size[0] / 2, working_area_size[1] / 2, working_area_size[2] / 2)

# Create a collision box area around the assets to prevent them from drifting away
object_based_sdg_utils.create_collision_box_walls(
    stage, "/World/CollisionWalls", working_area_size[0], working_area_size[1], working_area_size[2]
)

rep.functional.physics.create_physics_scene("/PhysicsScene", timeStepsPerSecond=60)
physx_scene = PhysxSchema.PhysxSceneAPI.Apply(stage.GetPrimAtPath("/PhysicsScene"))

# TRAINING ASSETS
# Add the objects to be trained in the environment with their labels and properties
labeled_assets_and_properties = config.get("labeled_assets_and_properties", [])
floating_labeled_prims = []
falling_labeled_prims = []
labeled_prims = []
rep.functional.create.scope(name="Labeled", parent="/World")
for obj in labeled_assets_and_properties:
    obj_url = obj.get("url", "")
    label = obj.get("label", "unknown")
    count = obj.get("count", 1)
    floating = obj.get("floating", False)
    scale_min_max = obj.get("randomize_scale", (1, 1))
    for i in range(count):
        # Create a prim and add the asset reference
        rand_loc, rand_rot, rand_scale = object_based_sdg_utils.get_random_transform_values(
            loc_min=working_area_min, loc_max=working_area_max, scale_min_max=scale_min_max
        )
        asset_path = obj_url if obj_url.startswith("omniverse://") else assets_root_path + obj_url
        prim = rep.functional.create.reference(
            usd_path=asset_path,
            parent="/World/Labeled",
            name=label,
            position=rand_loc,
            rotation=rand_rot,
            scale=rand_scale,
        )
        # Apply colliders and rigid body dynamics
        object_based_sdg_utils.add_colliders(prim)
        rep.functional.physics.apply_rigid_body(prim, disableGravity=False)
        #  Label the asset (any previous 'class' label will be overwritten)
        add_labels(prim, labels=[label], instance_name="class")
        if floating:
            floating_labeled_prims.append(prim)
        else:
            falling_labeled_prims.append(prim)
labeled_prims = floating_labeled_prims + falling_labeled_prims

# DISTRACTORS
# Add shape distractors to the environment as floating or falling objects
shape_distractors_types = config.get("shape_distractors_types", ["capsule", "cone", "cylinder", "sphere", "cube"])
shape_distractors_scale_min_max = config.get("shape_distractors_scale_min_max", (0.02, 0.2))
shape_distractors_num = config.get("shape_distractors_num", 350)
shape_distractors = []
floating_shape_distractors = []
falling_shape_distractors = []
for i in range(shape_distractors_num):
    rand_loc, rand_rot, rand_scale = object_based_sdg_utils.get_random_transform_values(
        loc_min=working_area_min, loc_max=working_area_max, scale_min_max=shape_distractors_scale_min_max
    )
    rand_shape = random.choice(shape_distractors_types)
    prim_path = omni.usd.get_stage_next_free_path(stage, f"/World/Distractors/{rand_shape}", False)
    prim = stage.DefinePrim(prim_path, rand_shape.capitalize())
    rep.functional.modify.pose(prim, position_value=rand_loc, rotation_value=rand_rot, scale_value=rand_scale)
    disable_gravity = random.choice([True, False])
    object_based_sdg_utils.add_colliders(prim)
    rep.functional.physics.apply_rigid_body(prim, disableGravity=disable_gravity)
    if disable_gravity:
        floating_shape_distractors.append(prim)
    else:
        falling_shape_distractors.append(prim)
    shape_distractors.append(prim)

# Add mesh distractors to the environment as floating of falling objects
mesh_distactors_urls = config.get("mesh_distractors_urls", [])
mesh_distactors_scale_min_max = config.get("mesh_distractors_scale_min_max", (0.1, 2.0))
mesh_distactors_num = config.get("mesh_distractors_num", 10)
mesh_distractors = []
floating_mesh_distractors = []
falling_mesh_distractors = []
for i in range(mesh_distactors_num):
    rand_loc, rand_rot, rand_scale = object_based_sdg_utils.get_random_transform_values(
        loc_min=working_area_min, loc_max=working_area_max, scale_min_max=mesh_distactors_scale_min_max
    )
    mesh_url = random.choice(mesh_distactors_urls)
    prim_name = os.path.basename(mesh_url).split(".")[0]
    asset_path = mesh_url if mesh_url.startswith("omniverse://") else assets_root_path + mesh_url
    prim = rep.functional.create.reference(
        usd_path=asset_path,
        parent="/World/Distractors",
        name=prim_name,
        position=rand_loc,
        rotation=rand_rot,
        scale=rand_scale,
    )
    disable_gravity = random.choice([True, False])
    object_based_sdg_utils.add_colliders(prim)
    rep.functional.physics.apply_rigid_body(prim, disableGravity=disable_gravity)
    if disable_gravity:
        floating_mesh_distractors.append(prim)
    else:
        falling_mesh_distractors.append(prim)
    mesh_distractors.append(prim)
    # Remove any previous semantics on the mesh distractor
    upgrade_prim_semantics_to_labels(prim, include_descendants=True)
    remove_labels(prim, include_descendants=True)

# REPLICATOR
# Initialize randomization
rep.set_global_seed(42)
random.seed(42)

# Disable capturing every frame (capture will be triggered manually using the step function)
rep.orchestrator.set_capture_on_play(False)

# Set DLSS to Quality mode (2) for best SDG results , options: 0 (Performance), 1 (Balanced), 2 (Quality), 3 (Auto)
carb.settings.get_settings().set("rtx/post/dlss/execMode", 2)

# Create the camera prims and their properties
cameras = []
num_cameras = config.get("num_cameras", 1)
camera_properties_kwargs = config.get("camera_properties_kwargs", {})
rep.functional.create.scope(name="Cameras", parent="/World")
for i in range(num_cameras):
    cam_prim = rep.functional.create.camera(parent="/World/Cameras", name="cam", **camera_properties_kwargs)
    cameras.append(cam_prim)

# Add collision spheres (disabled by default) to cameras to avoid objects overlaping with the camera view
camera_colliders = []
camera_collider_radius = config.get("camera_collider_radius", 0)
if camera_collider_radius > 0:
    for cam in cameras:
        cam_path = cam.GetPath()
        cam_collider = stage.DefinePrim(f"{cam_path}/CollisionSphere", "Sphere")
        cam_collider.GetAttribute("radius").Set(camera_collider_radius)
        rep.functional.physics.apply_collider(cam_collider)
        collision_api = UsdPhysics.CollisionAPI(cam_collider)
        collision_api.GetCollisionEnabledAttr().Set(False)
        UsdGeom.Imageable(cam_collider).MakeInvisible()
        camera_colliders.append(cam_collider)

# Wait an app update to ensure the prim changes are applied
simulation_app.update()

# Create render products using the cameras
render_products = []
resolution = config.get("resolution", (640, 480))
for cam in cameras:
    rp = rep.create.render_product(cam.GetPath(), resolution)
    render_products.append(rp)

# Enable rendering only at capture time
disable_render_products_between_captures = config.get("disable_render_products_between_captures", True)
if disable_render_products_between_captures:
    object_based_sdg_utils.set_render_products_updates(render_products, False, include_viewport=False)

# Create the writer and attach the render products
writer_type = config.get("writer_type", "PoseWriter")
writer_kwargs = config.get("writer_kwargs", {})
# If not an absolute path, set it relative to the current working directory
if out_dir := writer_kwargs.get("output_dir"):
    if not os.path.isabs(out_dir):
        out_dir = os.path.join(os.getcwd(), out_dir)
        writer_kwargs["output_dir"] = out_dir
    print(f"[SDG] Writing data to: {out_dir}")
if writer_type is not None and len(render_products) > 0:
    writer = rep.writers.get(writer_type)
    writer.initialize(**writer_kwargs)
    writer.attach(render_products)

# RANDOMIZERS
def on_overlap_hit(hit) -> bool:
    """Apply a random upwards velocity to objects overlapping the bounce area."""
    prim_path = str(PhysicsSchemaTools.intToSdfPath(hit.rigid_body))
    prim = stage.GetPrimAtPath(prim_path)
    # Skip the camera collision spheres
    if prim not in camera_colliders:
        rand_vel = (random.uniform(-2, 2), random.uniform(-2, 2), random.uniform(4, 8))
        prim.GetAttribute("physics:velocity").Set(rand_vel)
    return True  # return True to continue the query

# Area to check for overlapping objects (above the bottom collision box)
overlap_area_thickness = 0.1
overlap_area_origin = (0, 0, (-working_area_size[2] / 2) + (overlap_area_thickness / 2))
overlap_area_extent = (
    working_area_size[0] / 2 * 0.99,
    working_area_size[1] / 2 * 0.99,
    overlap_area_thickness / 2 * 0.99,
)

def on_physics_step(dt: float, context) -> None:
    """Check for overlapping objects on every physics update step."""
    get_physics_scene_query_interface().overlap_box(
        carb.Float3(overlap_area_extent),
        carb.Float3(overlap_area_origin),
        carb.Float4(0, 0, 0, 1),
        on_overlap_hit,
    )

# Subscribe to the physics step events to check for objects overlapping the 'bounce' area
physics_sub = omni.physics.core.get_physics_simulation_interface().subscribe_physics_on_step_events(
    pre_step=False, order=0, on_update=on_physics_step
)

camera_distance_to_target_min_max = config.get("camera_distance_to_target_min_max", (0.1, 0.5))
camera_look_at_target_offset = config.get("camera_look_at_target_offset", 0.2)

def randomize_camera_poses() -> None:
    """Randomize camera poses to look at a random target asset with random distance and offset."""
    for cam in cameras:
        target_asset = random.choice(labeled_prims)
        # Add a look_at offset so the target is not always in the center of the camera view
        loc_offset = (
            random.uniform(-camera_look_at_target_offset, camera_look_at_target_offset),
            random.uniform(-camera_look_at_target_offset, camera_look_at_target_offset),
            random.uniform(-camera_look_at_target_offset, camera_look_at_target_offset),
        )
        target_loc = target_asset.GetAttribute("xformOp:translate").Get() + loc_offset
        distance = random.uniform(camera_distance_to_target_min_max[0], camera_distance_to_target_min_max[1])
        cam_loc, quat = object_based_sdg_utils.get_random_pose_on_sphere(origin=target_loc, radius=distance)
        rep.functional.modify.pose(cam, position_value=cam_loc, rotation_value=quat)

def simulate_camera_collision(num_frames: int = 1) -> None:
    """Enable camera colliders temporarily and simulate to push out overlapping objects."""
    for cam_collider in camera_colliders:
        collision_api = UsdPhysics.CollisionAPI(cam_collider)
        collision_api.GetCollisionEnabledAttr().Set(True)
    if not timeline.is_playing():
        timeline.play()
    for _ in range(num_frames):
        simulation_app.update()
    for cam_collider in camera_colliders:
        collision_api = UsdPhysics.CollisionAPI(cam_collider)
        collision_api.GetCollisionEnabledAttr().Set(False)

# Create a randomizer for the shape distractors colors, manually triggered at custom events
with rep.trigger.on_custom_event(event_name="randomize_shape_distractor_colors"):
    shape_distractors_paths = [prim.GetPath() for prim in chain(floating_shape_distractors, falling_shape_distractors)]
    shape_distractors_group = rep.create.group(shape_distractors_paths)
    with shape_distractors_group:
        rep.randomizer.color(colors=rep.distribution.uniform((0, 0, 0), (1, 1, 1)))

# Create a randomizer for lights in the working area, manually triggered at custom events
with rep.trigger.on_custom_event(event_name="randomize_lights"):
    lights = rep.create.light(
        light_type="Sphere",
        color=rep.distribution.uniform((0, 0, 0), (1, 1, 1)),
        temperature=rep.distribution.normal(6500, 500),
        intensity=rep.distribution.normal(35000, 5000),
        position=rep.distribution.uniform(working_area_min, working_area_max),
        scale=rep.distribution.uniform(0.1, 1),
        count=3,
    )

# Create a randomizer for the dome background, manually triggered at custom events
with rep.trigger.on_custom_event(event_name="randomize_dome_background"):
    dome_textures = [
        assets_root_path + "/NVIDIA/Assets/Skies/Indoor/autoshop_01_4k.hdr",
        assets_root_path + "/NVIDIA/Assets/Skies/Indoor/carpentry_shop_01_4k.hdr",
        assets_root_path + "/NVIDIA/Assets/Skies/Indoor/hotel_room_4k.hdr",
        assets_root_path + "/NVIDIA/Assets/Skies/Indoor/wooden_lounge_4k.hdr",
    ]
    dome_light = rep.create.light(light_type="Dome")
    with dome_light:
        rep.modify.attribute("inputs:texture:file", rep.distribution.choice(dome_textures))
        rep.randomizer.rotation()

def capture_with_motion_blur_and_pathtracing(
    physx_scene: PhysxSchema.PhysxSceneAPI, duration: float = 0.05, num_samples: int = 8, spp: int = 64
) -> None:
    """Capture motion blur by combining pathtraced subframe samples simulated for the given duration."""
    # For small step sizes the physics FPS needs to be temporarily increased to provide movements every sub sample
    orig_physics_fps = physx_scene.GetTimeStepsPerSecondAttr().Get()
    target_physics_fps = 1 / duration * num_samples
    if target_physics_fps > orig_physics_fps:
        print(f"[SDG] Changing physics FPS from {orig_physics_fps} to {target_physics_fps}")
        physx_scene.GetTimeStepsPerSecondAttr().Set(target_physics_fps)

    # Enable motion blur (if not enabled)
    is_motion_blur_enabled = carb.settings.get_settings().get("/omni/replicator/captureMotionBlur")
    if not is_motion_blur_enabled:
        carb.settings.get_settings().set("/omni/replicator/captureMotionBlur", True)
    # Number of sub samples to render for motion blur in PathTracing mode
    carb.settings.get_settings().set("/omni/replicator/pathTracedMotionBlurSubSamples", num_samples)

    # Set the render mode to PathTracing
    prev_render_mode = carb.settings.get_settings().get("/rtx/rendermode")
    carb.settings.get_settings().set("/rtx/rendermode", "PathTracing")
    carb.settings.get_settings().set("/rtx/pathtracing/spp", spp)
    carb.settings.get_settings().set("/rtx/pathtracing/totalSpp", spp)
    carb.settings.get_settings().set("/rtx/pathtracing/optixDenoiser/enabled", 0)

    # Make sure the timeline is playing
    if not timeline.is_playing():
        timeline.play()

    # Capture the frame by advancing the simulation for the given duration and combining the sub samples
    rep.orchestrator.step(delta_time=duration, pause_timeline=False)

    # Restore the original physics FPS
    if target_physics_fps > orig_physics_fps:
        print(f"[SDG] Restoring physics FPS from {target_physics_fps} to {orig_physics_fps}")
        physx_scene.GetTimeStepsPerSecondAttr().Set(orig_physics_fps)

    # Restore the previous render and motion blur  settings
    carb.settings.get_settings().set("/omni/replicator/captureMotionBlur", is_motion_blur_enabled)
    print(f"[SDG] Restoring render mode from 'PathTracing' to '{prev_render_mode}'")
    carb.settings.get_settings().set("/rtx/rendermode", prev_render_mode)

def run_simulation_loop(duration: float) -> None:
    """Update the app until a given simulation duration has passed."""
    timeline = omni.timeline.get_timeline_interface()
    elapsed_time = 0.0
    previous_time = timeline.get_current_time()
    if not timeline.is_playing():
        timeline.play()
    app_updates_counter = 0
    while elapsed_time <= duration:
        simulation_app.update()
        elapsed_time += timeline.get_current_time() - previous_time
        previous_time = timeline.get_current_time()
        app_updates_counter += 1
        print(
            f"\t Simulation loop at {timeline.get_current_time():.2f}, current elapsed time: {elapsed_time:.2f}, counter: {app_updates_counter}"
        )
    print(
        f"[SDG] Simulation loop finished in {elapsed_time:.2f} seconds at {timeline.get_current_time():.2f} with {app_updates_counter} app updates."
    )

# SDG
# Number of frames to capture
num_frames = config.get("num_frames", 10)

# Increase subframes if materials are not loaded on time, or ghosting artifacts appear on moving objects,
# see: https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator/subframes_examples.html
rt_subframes = config.get("rt_subframes", -1)

# Amount of simulation time to wait between captures
sim_duration_between_captures = config.get("simulation_duration_between_captures", 0.025)

# Initial trigger for randomizers before the SDG loop with several app updates (ensures materials/textures are loaded)
rep.utils.send_og_event(event_name="randomize_shape_distractor_colors")
rep.utils.send_og_event(event_name="randomize_dome_background")
for _ in range(5):
    simulation_app.update()

# Set the timeline parameters (start, end, no looping) and start the timeline
timeline = omni.timeline.get_timeline_interface()
timeline.set_start_time(0)
timeline.set_end_time(1000000)
timeline.set_looping(False)
# If no custom physx scene is created, a default one will be created by the physics engine once the timeline starts
timeline.play()
timeline.commit()
simulation_app.update()

# Store the wall start time for stats
wall_time_start = time.perf_counter()

# Run the simulation and capture data triggering randomizations and actions at custom frame intervals
for i in range(num_frames):
    # Cameras will be moved to a random position and look at a randomly selected labeled asset
    if i % 3 == 0:
        print(f"\t Randomizing camera poses")
        randomize_camera_poses()
        # Temporarily enable camera colliders and simulate for a few frames to push out any overlapping objects
        if camera_colliders:
            simulate_camera_collision(num_frames=4)

    # Apply a random velocity towards the origin to the working area to pull the assets closer to the center
    if i % 10 == 0:
        print(f"\t Applying velocity towards the origin")
        object_based_sdg_utils.apply_velocities_towards_target(
            list(chain(labeled_prims, shape_distractors, mesh_distractors))
        )

    # Randomize lights locations and colors
    if i % 5 == 0:
        print(f"\t Randomizing lights")
        rep.utils.send_og_event(event_name="randomize_lights")

    # Randomize the colors of the primitive shape distractors
    if i % 15 == 0:
        print(f"\t Randomizing shape distractors colors")
        rep.utils.send_og_event(event_name="randomize_shape_distractor_colors")

    # Randomize the texture of the dome background
    if i % 25 == 0:
        print(f"\t Randomizing dome background")
        rep.utils.send_og_event(event_name="randomize_dome_background")

    # Apply a random velocity on the floating distractors (shapes and meshes)
    if i % 17 == 0:
        print(f"\t Randomizing shape distractors velocities")
        object_based_sdg_utils.apply_random_velocities(
            list(chain(floating_shape_distractors, floating_mesh_distractors))
        )

    # Enable render products only at capture time
    if disable_render_products_between_captures:
        object_based_sdg_utils.set_render_products_updates(render_products, True, include_viewport=False)

    # Capture the current frame
    print(f"[SDG] Capturing frame {i}/{num_frames}, at simulation time: {timeline.get_current_time():.2f}")
    if i % 5 == 0:
        capture_with_motion_blur_and_pathtracing(physx_scene, duration=0.025, num_samples=8, spp=128)
    else:
        rep.orchestrator.step(delta_time=0.0, rt_subframes=rt_subframes, pause_timeline=False)

    # Disable render products between captures
    if disable_render_products_between_captures:
        object_based_sdg_utils.set_render_products_updates(render_products, False, include_viewport=False)

    # Run the simulation for a given duration between frame captures
    if sim_duration_between_captures > 0:
        run_simulation_loop(duration=sim_duration_between_captures)
    else:
        simulation_app.update()

# Wait for the data to be written (default writer backends are asynchronous)
rep.orchestrator.wait_until_complete()

# Get the stats
wall_duration = time.perf_counter() - wall_time_start
sim_duration = timeline.get_current_time()
avg_frame_fps = num_frames / wall_duration
num_captures = num_frames * num_cameras
avg_capture_fps = num_captures / wall_duration
print(
    f"[SDG] Captured {num_frames} frames, {num_captures} entries (frames * cameras) in {wall_duration:.2f} seconds.\n"
    f"\t Simulation duration: {sim_duration:.2f}\n"
    f"\t Simulation duration between captures: {sim_duration_between_captures:.2f}\n"
    f"\t Average frame FPS: {avg_frame_fps:.2f}\n"
    f"\t Average capture entries (frames * cameras) FPS: {avg_capture_fps:.2f}\n"
)

# Unsubscribe the physics overlap checks and stop the timeline
physics_sub = None
simulation_app.update()
timeline.stop()

simulation_app.close()
```

Utils module

```python
"""Provide utility functions for object-based synthetic data generation."""

import random

import numpy as np
import omni.replicator.core as rep
from omni.kit.viewport.utility import get_active_viewport
from pxr import Gf, PhysxSchema, Usd, UsdGeom, UsdPhysics

def add_colliders(root_prim: Usd.Prim) -> None:
    """Enable collisions on the asset (without rigid body dynamics the asset will be static)."""
    # Iterate descendant prims (including root) and add colliders to mesh or primitive types
    for desc_prim in Usd.PrimRange(root_prim):
        if desc_prim.IsA(UsdGeom.Mesh) or desc_prim.IsA(UsdGeom.Gprim):
            # Physics
            if not desc_prim.HasAPI(UsdPhysics.CollisionAPI):
                collision_api = UsdPhysics.CollisionAPI.Apply(desc_prim)
            else:
                collision_api = UsdPhysics.CollisionAPI(desc_prim)
            collision_api.CreateCollisionEnabledAttr(True)
            # PhysX
            if not desc_prim.HasAPI(PhysxSchema.PhysxCollisionAPI):
                physx_collision_api = PhysxSchema.PhysxCollisionAPI.Apply(desc_prim)
            else:
                physx_collision_api = PhysxSchema.PhysxCollisionAPI(desc_prim)
            # Set PhysX specific properties
            physx_collision_api.CreateContactOffsetAttr(0.001)
            physx_collision_api.CreateRestOffsetAttr(0.0)

        # Add mesh specific collision properties only to mesh types
        if desc_prim.IsA(UsdGeom.Mesh):
            # Add mesh collision properties to the mesh (e.g. collider aproximation type)
            if not desc_prim.HasAPI(UsdPhysics.MeshCollisionAPI):
                mesh_collision_api = UsdPhysics.MeshCollisionAPI.Apply(desc_prim)
            else:
                mesh_collision_api = UsdPhysics.MeshCollisionAPI(desc_prim)
            mesh_collision_api.CreateApproximationAttr().Set("convexHull")

def create_collision_box_walls(
    stage: Usd.Stage,
    path: str,
    width: float,
    depth: float,
    height: float,
    thickness: float = 0.5,
    visible: bool = False,
) -> None:
    """Create a collision box area wrapping the given working area with origin at (0, 0, 0)."""
    # Define the walls (name, location, size) with thickness towards outside of the working area
    walls = [
        ("floor", (0, 0, (height + thickness) / -2.0), (width, depth, thickness)),
        ("ceiling", (0, 0, (height + thickness) / 2.0), (width, depth, thickness)),
        ("left_wall", ((width + thickness) / -2.0, 0, 0), (thickness, depth, height)),
        ("right_wall", ((width + thickness) / 2.0, 0, 0), (thickness, depth, height)),
        ("front_wall", (0, (depth + thickness) / 2.0, 0), (width, thickness, height)),
        ("back_wall", (0, (depth + thickness) / -2.0, 0), (width, thickness, height)),
    ]
    for name, location, size in walls:
        prim = stage.DefinePrim(f"{path}/{name}", "Cube")
        scale = (size[0] / 2.0, size[1] / 2.0, size[2] / 2.0)
        rep.functional.modify.pose(prim, position_value=location, scale_value=scale)
        add_colliders(prim)
        if not visible:
            UsdGeom.Imageable(prim).MakeInvisible()

def get_random_transform_values(
    loc_min: tuple[float, float, float] = (0, 0, 0),
    loc_max: tuple[float, float, float] = (1, 1, 1),
    rot_min: tuple[float, float, float] = (0, 0, 0),
    rot_max: tuple[float, float, float] = (360, 360, 360),
    scale_min_max: tuple[float, float] = (0.1, 1.0),
) -> tuple[tuple[float, float, float], tuple[float, float, float], tuple[float, float, float]]:
    """Create random transformation values for location, rotation, and scale."""
    location = (
        random.uniform(loc_min[0], loc_max[0]),
        random.uniform(loc_min[1], loc_max[1]),
        random.uniform(loc_min[2], loc_max[2]),
    )
    rotation = (
        random.uniform(rot_min[0], rot_max[0]),
        random.uniform(rot_min[1], rot_max[1]),
        random.uniform(rot_min[2], rot_max[2]),
    )
    scale = tuple([random.uniform(scale_min_max[0], scale_min_max[1])] * 3)
    return location, rotation, scale

def get_random_pose_on_sphere(
    origin: tuple[float, float, float],
    radius: float,
    camera_forward_axis: tuple[float, float, float] = (0, 0, -1),
) -> tuple[Gf.Vec3f, Gf.Quatf]:
    """Generate a random pose on a sphere looking at the origin."""
    origin = Gf.Vec3f(origin)
    camera_forward_axis = Gf.Vec3f(camera_forward_axis)

    # Generate random angles for spherical coordinates
    theta = np.random.uniform(0, 2 * np.pi)
    phi = np.arcsin(np.random.uniform(-1, 1))

    # Spherical to Cartesian conversion
    x = radius * np.cos(theta) * np.cos(phi)
    y = radius * np.sin(phi)
    z = radius * np.sin(theta) * np.cos(phi)

    location = origin + Gf.Vec3f(x, y, z)

    # Calculate direction vector from camera to look_at point
    direction = origin - location
    direction_normalized = direction.GetNormalized()

    # Calculate rotation from forward direction (rotateFrom) to direction vector (rotateTo)
    rotation = Gf.Rotation(Gf.Vec3d(camera_forward_axis), Gf.Vec3d(direction_normalized))
    orientation = Gf.Quatf(rotation.GetQuat())

    return location, orientation

def set_render_products_updates(render_products: list, enabled: bool, include_viewport: bool = False) -> None:
    """Enable or disable the render products and viewport rendering."""
    for rp in render_products:
        rp.hydra_texture.set_updates_enabled(enabled)
    if include_viewport:
        get_active_viewport().updates_enabled = enabled

def apply_velocities_towards_target(
    prims: list[Usd.Prim],
    target: tuple[float, float, float] = (0, 0, 0),
    strength_range: tuple[float, float] = (0.1, 1.0),
) -> None:
    """Apply velocities to prims directing them towards a target point."""
    for prim in prims:
        loc = prim.GetAttribute("xformOp:translate").Get()
        strength = random.uniform(strength_range[0], strength_range[1])
        velocity = ((target[0] - loc[0]) * strength, (target[1] - loc[1]) * strength, (target[2] - loc[2]) * strength)
        prim.GetAttribute("physics:velocity").Set(velocity)

def apply_random_velocities(
    prims: list[Usd.Prim],
    linear_range: tuple[float, float] = (-2.5, 2.5),
    angular_range: tuple[float, float] = (-45, 45),
) -> None:
    """Apply random linear and angular velocities to prims."""
    for prim in prims:
        lin_vel = (
            random.uniform(linear_range[0], linear_range[1]),
            random.uniform(linear_range[0], linear_range[1]),
            random.uniform(linear_range[0], linear_range[1]),
        )
        ang_vel = (
            random.uniform(angular_range[0], angular_range[1]),
            random.uniform(angular_range[0], angular_range[1]),
            random.uniform(angular_range[0], angular_range[1]),
        )
        prim.GetAttribute("physics:velocity").Set(lin_vel)
        prim.GetAttribute("physics:angularVelocity").Set(ang_vel)
```

## Config Scenarios

The script has the following main configuration parameters:

* **launch\_config** (dict): Configuration for the launch settings, such as the renderer and headless mode.
* **env\_url** (str): The URL of the environment to load, if empty a new empty stage is created.
* **working\_area\_size** (tuple): The size of the area (width, depth, height) in which the objects will be placed, this area will be surrounded by invisible collision walls to prevent objects from drifting away.
* **num\_frames** (int): The number of frames to capture (the total number of entries will be num\_frames \* num\_cameras).
* **num\_cameras** (int): The number of cameras to use for capturing the frames, these will be randomized and moved to look at different targets.
* **disable\_render\_products\_between\_captures** (bool): If True, the render products will be disabled between captures to save resources.
* **simulation\_duration\_between\_captures** (float): The amount of simulation time to run between data captures.
* **camera\_properties\_kwargs** (dict): The camera properties to set for the cameras (focal length, focus distance, f-stop, clipping range).
* **writer\_type** (str): The writer type to use to write the data to disk. For example, PoseWriter or BasicWriter.
* **writer\_kwargs** (dict): The writer parameters to use when initializing the writer. For example, output\_dir, format, use\_subfolders.
* **labeled\_assets\_and\_properties** (list): A list of dictionaries with the labeled assets to add to the environment with their properties.
* **shape\_distractors\_types** (list): A list of shape types to use for the distractors (capsule, cone, cylinder, sphere, cube).
* **shape\_distractors\_num** (int): The number of shape distractors to add to the environment.
* **mesh\_distractors\_urls** (list): A list of mesh URLs to use for the distractors. For example, `/Isaac/Environments/Simple_Warehouse/Props/SM_CardBoxD_04_1847.usd` or `omniverse://...`.
* **mesh\_distractors\_num** (int): The number of mesh distractors to add to the environment.

The following provides details about the various config scenarios:

Built-in

Without an explicit config file, the script uses the default parameters stored in the script itself. The default parameters are the following:

Built-in (default) Config

```python
config = {
    "launch_config": {
        "renderer": "RealTimePathTracing",
        "headless": False,
    },
    "env_url": "",
    "working_area_size": (4, 4, 3),
    "rt_subframes": 4,
    "num_frames": 4,
    "num_cameras": 2,
    "camera_collider_radius": 0.5,
    "disable_render_products_between_captures": False,
    "simulation_duration_between_captures": 0.05,
    "resolution": (640, 480),
    "camera_properties_kwargs": {
        "focal_length": 24.0,
        "focus_distance": 400,
        "f_stop": 0.0,
        "clipping_range": (0.01, 10000),
    },
    "camera_look_at_target_offset": 0.15,
    "camera_distance_to_target_min_max": (0.25, 0.75),
    "writer_type": "PoseWriter",
    "writer_kwargs": {
        "output_dir": "_out_obj_based_sdg_pose_writer",
        "format": None,
        "use_subfolders": False,
        "write_debug_images": True,
        "skip_empty_frames": False,
    },
    "labeled_assets_and_properties": [
        {
            "url": "/Isaac/Props/YCB/Axis_Aligned/008_pudding_box.usd",
            "label": "pudding_box",
            "count": 5,
            "floating": True,
            "scale_min_max": (0.85, 1.25),
        },
        {
            "url": "/Isaac/Props/YCB/Axis_Aligned_Physics/006_mustard_bottle.usd",
            "label": "mustard_bottle",
            "count": 7,
            "floating": True,
            "scale_min_max": (0.85, 1.25),
        },
    ],
    "shape_distractors_types": ["capsule", "cone", "cylinder", "sphere", "cube"],
    "shape_distractors_scale_min_max": (0.015, 0.15),
    "shape_distractors_num": 350,
    "mesh_distractors_urls": [
        "/Isaac/Environments/Simple_Warehouse/Props/SM_CardBoxD_04_1847.usd",
        "/Isaac/Environments/Simple_Warehouse/Props/SM_CardBoxA_01_414.usd",
        "/Isaac/Environments/Simple_Warehouse/Props/S_TrafficCone.usd",
    ],
    "mesh_distractors_scale_min_max": (0.35, 1.35),
    "mesh_distractors_num": 75,
}
```

The following command runs the script with the default parameters:

```python
./python.sh standalone_examples/replicator/object_based_sdg/object_based_sdg.py
```

Basic Writer

The `object_based_sdg_config.yaml` config file uses `BasicWriter` with extended labeled assets and mesh distractors configurations.

Custom YAML Config using BasicWriter

```python
launch_config:
  renderer: RealTimePathTracing
  headless: false
env_url: ''
working_area_size:
- 4
- 4
- 3
rt_subframes: 4
num_frames: 10
num_cameras: 2
disable_render_products_between_captures: false
simulation_duration_between_captures: 0.0
resolution:
- 640
- 480
camera_look_at_target_offset: 0.15
camera_distance_to_target_min_max:
  - 0.25
  - 0.75
writer_type: BasicWriter
writer_kwargs:
  output_dir: _out_obj_based_sdg_basic_writer
  rgb: true
  semantic_segmentation: true
  use_common_output_dir: true
labeled_assets_and_properties:
- url: /Isaac/Props/YCB/Axis_Aligned/008_pudding_box.usd
  label: pudding_box
  count: 5
  floating: true
  scale_min_max:
    - 0.85
    - 1.25
- url: /Isaac/Props/YCB/Axis_Aligned/011_banana.usd
  label: banana
  count: 10
  floating: false
  scale_min_max:
    - 0.85
    - 1.25
- url: /Isaac/Props/YCB/Axis_Aligned_Physics/006_mustard_bottle.usd
  label: mustard_bottle
  count: 7
  floating: true
  scale_min_max:
    - 0.85
    - 1.25
shape_distractors_types:
- capsule
- cone
- cylinder
- sphere
- cube
shape_distractors_scale_min_max:
  - 0.015
  - 0.15
shape_distractors_num: 350
mesh_distractors_urls:
- /Isaac/Environments/Simple_Warehouse/Props/SM_CardBoxD_04_1847.usd
- /Isaac/Environments/Simple_Warehouse/Props/SM_CardBoxA_01_414.usd
- /Isaac/Environments/Simple_Warehouse/Props/S_TrafficCone.usd
- /Isaac/Environments/Simple_Warehouse/Props/S_WetFloorSign.usd
- /Isaac/Environments/Simple_Warehouse/Props/SM_BarelPlastic_B_03.usd
- /Isaac/Environments/Office/Props/SM_Board.usd
- /Isaac/Environments/Office/Props/SM_Book_03.usd
- /Isaac/Environments/Office/Props/SM_Book_34.usd
- /Isaac/Environments/Office/Props/SM_BookOpen_01.usd
- /Isaac/Environments/Office/Props/SM_Briefcase.usd
- /Isaac/Environments/Office/Props/SM_Extinguisher.usd
- /Isaac/Environments/Hospital/Props/SM_GasCart_01b.usd
- /Isaac/Environments/Hospital/Props/SM_MedicalBag_01a.usd
- /Isaac/Environments/Hospital/Props/SM_MedicalBox_01g.usd
- /Isaac/Environments/Hospital/Props/SM_Toweldispenser_01a.usd
mesh_distractors_scale_min_max:
  - 0.35
  - 1.35
mesh_distractors_num: 75
```

The following command runs the script with the custom parameters:

```python
./python.sh standalone_examples/replicator/object_based_sdg/object_based_sdg.py \
    --config standalone_examples/replicator/object_based_sdg/config/object_based_sdg_config.yaml
```

PoseWriter (DOPE)

The `object_based_sdg_dope_config.yaml` config file uses `PoseWriter` with DOPE format output for training DOPE networks.

Custom YAML Config using PoseWriter with DOPE format

```python
writer_type: PoseWriter
writer_kwargs:
  output_dir: _out_obj_based_sdg_pose_writer_dope
  format: dope
  write_debug_images: true
  skip_empty_frames: false
```

The following command runs the script with the custom parameters:

```python
./python.sh standalone_examples/replicator/object_based_sdg/object_based_sdg.py \
    --config standalone_examples/replicator/object_based_sdg/config/object_based_sdg_dope_config.yaml
```

PoseWriter (CenterPose)

The `object_based_sdg_centerpose_config.yaml` config file uses `PoseWriter` with CenterPose format output for training CenterPose networks.

Custom YAML Config using PoseWriter with CenterPose format

```python
writer_type: PoseWriter
writer_kwargs:
  output_dir: _out_obj_based_sdg_pose_writer_centerpose
  format: centerpose
  write_debug_images: true
  skip_empty_frames: false
```

The following command runs the script with the custom parameters:

```python
./python.sh standalone_examples/replicator/object_based_sdg/object_based_sdg.py \
    --config standalone_examples/replicator/object_based_sdg/config/object_based_sdg_centerpose_config.yaml
```

### Util Functions

The script uses the `rep.functional` API directly for common operations such as setting transforms (`rep.functional.modify.pose`), creating assets (`rep.functional.create.reference`, `rep.functional.create.camera`), and applying physics properties (`rep.functional.physics.apply_rigid_body`, `rep.functional.physics.apply_collider`). Additional helper functions are provided in a separate utils module for custom operations.

Replicator Functional API for Transforms

The `rep.functional.modify.pose` function is used to set position, rotation, and scale on prims. This replaces the need for custom transform helper functions.

```python
def get_random_transform_values(
    loc_min: tuple[float, float, float] = (0, 0, 0),
    loc_max: tuple[float, float, float] = (1, 1, 1),
    rot_min: tuple[float, float, float] = (0, 0, 0),
    rot_max: tuple[float, float, float] = (360, 360, 360),
    scale_min_max: tuple[float, float] = (0.1, 1.0),
) -> tuple[tuple[float, float, float], tuple[float, float, float], tuple[float, float, float]]:
    """Create random transformation values for location, rotation, and scale."""
    location = (
        random.uniform(loc_min[0], loc_max[0]),
        random.uniform(loc_min[1], loc_max[1]),
        random.uniform(loc_min[2], loc_max[2]),
    )
    rotation = (
        random.uniform(rot_min[0], rot_max[0]),
        random.uniform(rot_min[1], rot_max[1]),
        random.uniform(rot_min[2], rot_max[2]),
    )
    scale = tuple([random.uniform(scale_min_max[0], scale_min_max[1])] * 3)
    return location, rotation, scale
```

Example usage for creating and positioning shape distractors:

```python
falling_shape_distractors = []
for i in range(shape_distractors_num):
    rand_loc, rand_rot, rand_scale = object_based_sdg_utils.get_random_transform_values(
        loc_min=working_area_min, loc_max=working_area_max, scale_min_max=shape_distractors_scale_min_max
    )
    rand_shape = random.choice(shape_distractors_types)
    prim_path = omni.usd.get_stage_next_free_path(stage, f"/World/Distractors/{rand_shape}", False)
    prim = stage.DefinePrim(prim_path, rand_shape.capitalize())
    rep.functional.modify.pose(prim, position_value=rand_loc, rotation_value=rand_rot, scale_value=rand_scale)
    disable_gravity = random.choice([True, False])
    object_based_sdg_utils.add_colliders(prim)
    rep.functional.physics.apply_rigid_body(prim, disableGravity=disable_gravity)
    if disable_gravity:
        floating_shape_distractors.append(prim)
    else:
        falling_shape_distractors.append(prim)
    shape_distractors.append(prim)
```

Generate 3D Transform Values

The following functions are used to generate random 3D transform values for various scenarios.

```python
def get_random_transform_values(
    loc_min: tuple[float, float, float] = (0, 0, 0),
    loc_max: tuple[float, float, float] = (1, 1, 1),
    rot_min: tuple[float, float, float] = (0, 0, 0),
    rot_max: tuple[float, float, float] = (360, 360, 360),
    scale_min_max: tuple[float, float] = (0.1, 1.0),
) -> tuple[tuple[float, float, float], tuple[float, float, float], tuple[float, float, float]]:
    """Create random transformation values for location, rotation, and scale."""
    location = (
        random.uniform(loc_min[0], loc_max[0]),
        random.uniform(loc_min[1], loc_max[1]),
        random.uniform(loc_min[2], loc_max[2]),
    )
    rotation = (
        random.uniform(rot_min[0], rot_max[0]),
        random.uniform(rot_min[1], rot_max[1]),
        random.uniform(rot_min[2], rot_max[2]),
    )
    scale = tuple([random.uniform(scale_min_max[0], scale_min_max[1])] * 3)
    return location, rotation, scale
```

Example of generating a random pose on a sphere looking at the origin:

```python
def get_random_pose_on_sphere(
    origin: tuple[float, float, float],
    radius: float,
    camera_forward_axis: tuple[float, float, float] = (0, 0, -1),
) -> tuple[Gf.Vec3f, Gf.Quatf]:
    """Generate a random pose on a sphere looking at the origin."""
    origin = Gf.Vec3f(origin)
    camera_forward_axis = Gf.Vec3f(camera_forward_axis)

    # Generate random angles for spherical coordinates
    theta = np.random.uniform(0, 2 * np.pi)
    phi = np.arcsin(np.random.uniform(-1, 1))

    # Spherical to Cartesian conversion
    x = radius * np.cos(theta) * np.cos(phi)
    y = radius * np.sin(phi)
    z = radius * np.sin(theta) * np.cos(phi)

    location = origin + Gf.Vec3f(x, y, z)

    # Calculate direction vector from camera to look_at point
    direction = origin - location
    direction_normalized = direction.GetNormalized()

    # Calculate rotation from forward direction (rotateFrom) to direction vector (rotateTo)
    rotation = Gf.Rotation(Gf.Vec3d(camera_forward_axis), Gf.Vec3d(direction_normalized))
    orientation = Gf.Quatf(rotation.GetQuat())

    return location, orientation
```

Rigid-body Dynamics

Physics properties are applied using the `rep.functional.physics` API. The `apply_rigid_body` function adds rigid body dynamics, while `apply_collider` adds collision properties to prims. For custom collision settings (such as mesh approximation types), a helper function is still used.

```python
def add_colliders(root_prim: Usd.Prim) -> None:
    """Enable collisions on the asset (without rigid body dynamics the asset will be static)."""
    # Iterate descendant prims (including root) and add colliders to mesh or primitive types
    for desc_prim in Usd.PrimRange(root_prim):
        if desc_prim.IsA(UsdGeom.Mesh) or desc_prim.IsA(UsdGeom.Gprim):
            # Physics
            if not desc_prim.HasAPI(UsdPhysics.CollisionAPI):
                collision_api = UsdPhysics.CollisionAPI.Apply(desc_prim)
            else:
                collision_api = UsdPhysics.CollisionAPI(desc_prim)
            collision_api.CreateCollisionEnabledAttr(True)
            # PhysX
            if not desc_prim.HasAPI(PhysxSchema.PhysxCollisionAPI):
                physx_collision_api = PhysxSchema.PhysxCollisionAPI.Apply(desc_prim)
            else:
                physx_collision_api = PhysxSchema.PhysxCollisionAPI(desc_prim)
            # Set PhysX specific properties
            physx_collision_api.CreateContactOffsetAttr(0.001)
            physx_collision_api.CreateRestOffsetAttr(0.0)

        # Add mesh specific collision properties only to mesh types
        if desc_prim.IsA(UsdGeom.Mesh):
            # Add mesh collision properties to the mesh (e.g. collider aproximation type)
            if not desc_prim.HasAPI(UsdPhysics.MeshCollisionAPI):
                mesh_collision_api = UsdPhysics.MeshCollisionAPI.Apply(desc_prim)
            else:
                mesh_collision_api = UsdPhysics.MeshCollisionAPI(desc_prim)
            mesh_collision_api.CreateApproximationAttr().Set("convexHull")
```

Example usage for creating labeled assets with colliders and rigid body:

```python
scale_min_max = obj.get("randomize_scale", (1, 1))
for i in range(count):
    # Create a prim and add the asset reference
    rand_loc, rand_rot, rand_scale = object_based_sdg_utils.get_random_transform_values(
        loc_min=working_area_min, loc_max=working_area_max, scale_min_max=scale_min_max
    )
    asset_path = obj_url if obj_url.startswith("omniverse://") else assets_root_path + obj_url
    prim = rep.functional.create.reference(
        usd_path=asset_path,
        parent="/World/Labeled",
        name=label,
        position=rand_loc,
        rotation=rand_rot,
        scale=rand_scale,
    )
    # Apply colliders and rigid body dynamics
    object_based_sdg_utils.add_colliders(prim)
    rep.functional.physics.apply_rigid_body(prim, disableGravity=False)
    #  Label the asset (any previous 'class' label will be overwritten)
    add_labels(prim, labels=[label], instance_name="class")
    if floating:
        floating_labeled_prims.append(prim)
    else:
        falling_labeled_prims.append(prim)
```

### Randomizers

The following snippets show the various randomizations used throughout the script.

* **|isaac-sim\_short|/USD based:** bounce randomizer, randomizing camera poses, applying custom velocities to assets
* **Replicator based:** randomizing lights, shape distractors colors, dome background, and floating distractors velocities

Overlap Triggered Velocity Randomizer

The following snippet simulates a bouncing area above the bottom collision box. The function checks for overlapping objects in the area and applies a random velocity to the objects. The function is triggered every physics update step to check for objects overlapping the âbounceâ area.

```python
# RANDOMIZERS
def on_overlap_hit(hit) -> bool:
    """Apply a random upwards velocity to objects overlapping the bounce area."""
    prim_path = str(PhysicsSchemaTools.intToSdfPath(hit.rigid_body))
    prim = stage.GetPrimAtPath(prim_path)
    # Skip the camera collision spheres
    if prim not in camera_colliders:
        rand_vel = (random.uniform(-2, 2), random.uniform(-2, 2), random.uniform(4, 8))
        prim.GetAttribute("physics:velocity").Set(rand_vel)
    return True  # return True to continue the query

# Area to check for overlapping objects (above the bottom collision box)
overlap_area_thickness = 0.1
overlap_area_origin = (0, 0, (-working_area_size[2] / 2) + (overlap_area_thickness / 2))
overlap_area_extent = (
    working_area_size[0] / 2 * 0.99,
    working_area_size[1] / 2 * 0.99,
    overlap_area_thickness / 2 * 0.99,
)

def on_physics_step(dt: float, context) -> None:
    """Check for overlapping objects on every physics update step."""
    get_physics_scene_query_interface().overlap_box(
        carb.Float3(overlap_area_extent),
        carb.Float3(overlap_area_origin),
        carb.Float4(0, 0, 0, 1),
        on_overlap_hit,
    )

# Subscribe to the physics step events to check for objects overlapping the 'bounce' area
physics_sub = omni.physics.core.get_physics_simulation_interface().subscribe_physics_on_step_events(
    pre_step=False, order=0, on_update=on_physics_step
)
```

Camera Randomization

The camera randomization function uses the `rep.functional` API along with Isaac Sim/USD API to look at a randomly chosen labeled asset from a randomized distance together with an offset to avoid always looking at the center of the asset. Cameras are created using `rep.functional.create.camera` and positioned using `rep.functional.modify.pose`. If camera colliders are enabled, the function will temporarily enable them and simulate for a few frames to push out any overlapping objects.

```python
def randomize_camera_poses() -> None:
    """Randomize camera poses to look at a random target asset with random distance and offset."""
    for cam in cameras:
        target_asset = random.choice(labeled_prims)
        # Add a look_at offset so the target is not always in the center of the camera view
        loc_offset = (
            random.uniform(-camera_look_at_target_offset, camera_look_at_target_offset),
            random.uniform(-camera_look_at_target_offset, camera_look_at_target_offset),
            random.uniform(-camera_look_at_target_offset, camera_look_at_target_offset),
        )
        target_loc = target_asset.GetAttribute("xformOp:translate").Get() + loc_offset
        distance = random.uniform(camera_distance_to_target_min_max[0], camera_distance_to_target_min_max[1])
        cam_loc, quat = object_based_sdg_utils.get_random_pose_on_sphere(origin=target_loc, radius=distance)
        rep.functional.modify.pose(cam, position_value=cam_loc, rotation_value=quat)

def simulate_camera_collision(num_frames: int = 1) -> None:
    """Enable camera colliders temporarily and simulate to push out overlapping objects."""
    for cam_collider in camera_colliders:
        collision_api = UsdPhysics.CollisionAPI(cam_collider)
        collision_api.GetCollisionEnabledAttr().Set(True)
    if not timeline.is_playing():
        timeline.play()
    for _ in range(num_frames):
        simulation_app.update()
    for cam_collider in camera_colliders:
        collision_api = UsdPhysics.CollisionAPI(cam_collider)
        collision_api.GetCollisionEnabledAttr().Set(False)
```

Apply Velocities Towards a Target

The following function applies velocities to the prims with a random magnitude towards the given target (center of the working area). This is making sure in the example scenario that the objects donât drift away and are occasionally pulled towards the center to clutter the scene.

```python
def apply_velocities_towards_target(
    prims: list[Usd.Prim],
    target: tuple[float, float, float] = (0, 0, 0),
    strength_range: tuple[float, float] = (0.1, 1.0),
) -> None:
    """Apply velocities to prims directing them towards a target point."""
    for prim in prims:
        loc = prim.GetAttribute("xformOp:translate").Get()
        strength = random.uniform(strength_range[0], strength_range[1])
        velocity = ((target[0] - loc[0]) * strength, (target[1] - loc[1]) * strength, (target[2] - loc[2]) * strength)
        prim.GetAttribute("physics:velocity").Set(velocity)
```

Randomize Sphere Lights

The following snippet creates the given number of lights that will be added to a replicator randomization graph that will randomize the lights attributes (color, temperature, intensity, position, scale) when manually triggered (`rep.utils.send_og_event(event_name="randomize_lights")`).

```python
# Create a randomizer for lights in the working area, manually triggered at custom events
with rep.trigger.on_custom_event(event_name="randomize_lights"):
    lights = rep.create.light(
        light_type="Sphere",
        color=rep.distribution.uniform((0, 0, 0), (1, 1, 1)),
        temperature=rep.distribution.normal(6500, 500),
        intensity=rep.distribution.normal(35000, 5000),
        position=rep.distribution.uniform(working_area_min, working_area_max),
        scale=rep.distribution.uniform(0.1, 1),
        count=3,
    )
```

Randomize Shape Distractors Colors

The following snippet creates a randomizer graph for the shape distractors colors, manually triggered at custom events (`rep.utils.send_og_event(event_name="randomize_shape_distractor_colors")`. The paths of the shape distractors prims are used to create a graph node representing the distractor prims, which are then used in the built-in Replicator color randomizer (`rep.randomizer.color`).

```python
# Create a randomizer for the shape distractors colors, manually triggered at custom events
with rep.trigger.on_custom_event(event_name="randomize_shape_distractor_colors"):
    shape_distractors_paths = [prim.GetPath() for prim in chain(floating_shape_distractors, falling_shape_distractors)]
    shape_distractors_group = rep.create.group(shape_distractors_paths)
    with shape_distractors_group:
        rep.randomizer.color(colors=rep.distribution.uniform((0, 0, 0), (1, 1, 1)))
```

### SDG Loop

The following snippet shows the main data capture loop that runs the simulation for a given number of frames and captures the data at custom intervals. The loop triggers the randomizations and actions at custom frame intervals. For example, randomizing camera poses, applying velocities towards the origin, randomizing lights, shape distractors colors, dome background, and floating distractors velocities.

SDG Loop

```python
# Run the simulation and capture data triggering randomizations and actions at custom frame intervals
for i in range(num_frames):
    # Cameras will be moved to a random position and look at a randomly selected labeled asset
    if i % 3 == 0:
        print(f"\t Randomizing camera poses")
        randomize_camera_poses()
        # Temporarily enable camera colliders and simulate for a few frames to push out any overlapping objects
        if camera_colliders:
            simulate_camera_collision(num_frames=4)

    # Apply a random velocity towards the origin to the working area to pull the assets closer to the center
    if i % 10 == 0:
        print(f"\t Applying velocity towards the origin")
        object_based_sdg_utils.apply_velocities_towards_target(
            list(chain(labeled_prims, shape_distractors, mesh_distractors))
        )

    # Randomize lights locations and colors
    if i % 5 == 0:
        print(f"\t Randomizing lights")
        rep.utils.send_og_event(event_name="randomize_lights")

    # Randomize the colors of the primitive shape distractors
    if i % 15 == 0:
        print(f"\t Randomizing shape distractors colors")
        rep.utils.send_og_event(event_name="randomize_shape_distractor_colors")

    # Randomize the texture of the dome background
    if i % 25 == 0:
        print(f"\t Randomizing dome background")
        rep.utils.send_og_event(event_name="randomize_dome_background")

    # Apply a random velocity on the floating distractors (shapes and meshes)
    if i % 17 == 0:
        print(f"\t Randomizing shape distractors velocities")
        object_based_sdg_utils.apply_random_velocities(
            list(chain(floating_shape_distractors, floating_mesh_distractors))
        )

    # Enable render products only at capture time
    if disable_render_products_between_captures:
        object_based_sdg_utils.set_render_products_updates(render_products, True, include_viewport=False)

    # Capture the current frame
    print(f"[SDG] Capturing frame {i}/{num_frames}, at simulation time: {timeline.get_current_time():.2f}")
    if i % 5 == 0:
        capture_with_motion_blur_and_pathtracing(physx_scene, duration=0.025, num_samples=8, spp=128)
    else:
        rep.orchestrator.step(delta_time=0.0, rt_subframes=rt_subframes, pause_timeline=False)

    # Disable render products between captures
    if disable_render_products_between_captures:
        object_based_sdg_utils.set_render_products_updates(render_products, False, include_viewport=False)

    # Run the simulation for a given duration between frame captures
    if sim_duration_between_captures > 0:
        run_simulation_loop(duration=sim_duration_between_captures)
    else:
        simulation_app.update()

# Wait for the data to be written (default writer backends are asynchronous)
rep.orchestrator.wait_until_complete()
```

### Motion Blur

The following snippet captures the frames using path tracing and motion blur, it selects the duration of the movement to capture and the number of frames to combine.

Example of a captured frame using motion blur and path tracing:

Motion Blur

```python
def capture_with_motion_blur_and_pathtracing(
    physx_scene: PhysxSchema.PhysxSceneAPI, duration: float = 0.05, num_samples: int = 8, spp: int = 64
) -> None:
    """Capture motion blur by combining pathtraced subframe samples simulated for the given duration."""
    # For small step sizes the physics FPS needs to be temporarily increased to provide movements every sub sample
    orig_physics_fps = physx_scene.GetTimeStepsPerSecondAttr().Get()
    target_physics_fps = 1 / duration * num_samples
    if target_physics_fps > orig_physics_fps:
        print(f"[SDG] Changing physics FPS from {orig_physics_fps} to {target_physics_fps}")
        physx_scene.GetTimeStepsPerSecondAttr().Set(target_physics_fps)

    # Enable motion blur (if not enabled)
    is_motion_blur_enabled = carb.settings.get_settings().get("/omni/replicator/captureMotionBlur")
    if not is_motion_blur_enabled:
        carb.settings.get_settings().set("/omni/replicator/captureMotionBlur", True)
    # Number of sub samples to render for motion blur in PathTracing mode
    carb.settings.get_settings().set("/omni/replicator/pathTracedMotionBlurSubSamples", num_samples)

    # Set the render mode to PathTracing
    prev_render_mode = carb.settings.get_settings().get("/rtx/rendermode")
    carb.settings.get_settings().set("/rtx/rendermode", "PathTracing")
    carb.settings.get_settings().set("/rtx/pathtracing/spp", spp)
    carb.settings.get_settings().set("/rtx/pathtracing/totalSpp", spp)
    carb.settings.get_settings().set("/rtx/pathtracing/optixDenoiser/enabled", 0)

    # Make sure the timeline is playing
    if not timeline.is_playing():
        timeline.play()

    # Capture the frame by advancing the simulation for the given duration and combining the sub samples
    rep.orchestrator.step(delta_time=duration, pause_timeline=False)

    # Restore the original physics FPS
    if target_physics_fps > orig_physics_fps:
        print(f"[SDG] Restoring physics FPS from {target_physics_fps} to {orig_physics_fps}")
        physx_scene.GetTimeStepsPerSecondAttr().Set(orig_physics_fps)

    # Restore the previous render and motion blur  settings
    carb.settings.get_settings().set("/omni/replicator/captureMotionBlur", is_motion_blur_enabled)
    print(f"[SDG] Restoring render mode from 'PathTracing' to '{prev_render_mode}'")
    carb.settings.get_settings().set("/rtx/rendermode", prev_render_mode)
```

### Performance Optimization

To optimize the performance of the SDG pipeline, especially if there are many frames computed between captures, the render products (rendering and processing) can be disabled by default and only enabled during the capture time. This can be achieved by setting the `disable_render_products_between_captures` parameter to **True** in the configuration. Setting the `include_viewport` argument to **True** in the `set_render_products_updates` function will also disable the viewport (UI) rendering, this will disable any live feedback in the viewport during the simulation, this can be especially useful if the pipeline is running on a headless server.

Toggle Render Products

```python
def set_render_products_updates(render_products: list, enabled: bool, include_viewport: bool = False) -> None:
    """Enable or disable the render products and viewport rendering."""
    for rp in render_products:
        rp.hydra_texture.set_updates_enabled(enabled)
    if include_viewport:
        get_active_viewport().updates_enabled = enabled
```

### Writer

By default the script uses the `PoseWriter` writer to write the data to disk. The writer parameters are as follows:

* **output\_dir** (str): The output directory to write the data to
* **format** (str): The format to use for the output files (for example, CenterPose, DOPE), if None a default format will be used writing all the available data.
* **use\_subfolders** (bool): If True, the data will be written to subfolders based on the camera name.
* **write\_debug\_images** (bool): If True, debug images will also be written (for example, bounding box overlays).
* **skip\_empty\_frames** (bool): If True, empty frames will be skipped when writing the data.

The `PoseWriter` implementation can be found in the `pose_writer.py` file in the `isaacsim.replicator.writers` extension. Examples of using various output formats can be found in the `/config/object_based_sdg_dope_config.yaml` and `/config/object_based_sdg_centerpose_config.yaml` configuration files. Where the `format` parameter is set to **dope** and **centerpose** respectively.

To use a custom writer, the `writer_type` and `writer_kwargs` parameters can be set in the config files or in the script to load a custom writer implementation.

```python
"writer_type": "MyCustomWriter",
"writer_kwargs": {
    "arg1": "val1",
    "arg2": "val2",
    "argn": "valn",
}
```

## SyntheticaDETR

SyntheticaDETR is a 2D object detection network aimed to detect indoor objects in RGB images. It is built on top of RT-DETR, a state of the art 2D object detection network on COCO dataset, with training done on data collected entirely in simulation using the Isaac Sim Replicator. As of today SyntheticaDETR is the top performing object detection network on the BOP leaderboard for YCBV dataset.

Leaderboard link: <https://bop.felk.cvut.cz/leaderboards/detection-bop22/ycb-v/>

### Data Generation

Generate data using Isaac Sim and Replicator with procedurally generated scenes. Objects are dropped from ceilings and simulation is run with physics enabled to avoid interpenetrations to allow for objects to settle into stable configurations on the floor. The RGB renderings are captured during the process along with the ground truth segmentation, depth and bounding boxes of visible objects in the view frustum. The image and ground truth pair are used to train networks using supervised learning.

### Data Generation with Real World Asset Capture

While the above data generation process is suited for objects with known 3D assets already available in digital form, including USD and OBJ format, there are scenarios where such assets are not available apriori.

Therefore, use the AR Code app for iPad/iPhone to capture the assets. The app uses LiDAR and multiple images captured from various diverse viewpoints to obtain the 3D asset model directly in USD format suited for rendering with the Isaac Sim and Replicator.

Below are the asset models captured using the app and visualized from different viewpoints.

These assets were used in the Synthetica rendering framework to obtain rendered images:

The results of the detector trained on this synthetic data and tested directly on the real world images are shown below:

The numbers next to the labels on the bounding boxes represent the confidence values with which the detector is certain about the identity of the object.

### SyntheticaDETR Model and Isaac ROS RT-DETR

The SyntheticaDETR model is available in the NGC Catalog at the following link:
[SyntheticaDETR in NGC](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/isaac/models/synthetica_detr)

Furthermore, to run the model in ROS, refer to this thorough tutorial:
[Isaac ROS RT-DETR Tutorial](https://nvidia-isaac-ros.github.io/repositories_and_packages/isaac_ros_object_detection/isaac_ros_rtdetr/index.html)

On this page

* [Learning Objectives](#learning-objectives)
* [Prerequisites](#prerequisites)
* [Getting Started](#getting-started)
* [Implementation](#implementation)
* [Config Scenarios](#config-scenarios)
  + [Util Functions](#util-functions)
  + [Randomizers](#randomizers)
  + [SDG Loop](#sdg-loop)
  + [Motion Blur](#motion-blur)
  + [Performance Optimization](#performance-optimization)
  + [Writer](#writer)
* [SyntheticaDETR](#syntheticadetr)
  + [Data Generation](#data-generation)
  + [Data Generation with Real World Asset Capture](#data-generation-with-real-world-asset-capture)
  + [SyntheticaDETR Model and Isaac ROS RT-DETR](#syntheticadetr-model-and-isaac-ros-rt-detr)

---

### Scene-Based SDG

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/replicator_tutorials/tutorial_replicator_scene_based_sdg.html

* [Synthetic Data Generation](../synthetic_data_generation/index.html)
* [Perception Data Generation (Replicator)](index.html)
* Scene Based Synthetic Dataset Generation

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Scene Based Synthetic Dataset Generation

This tutorial illustrates the process of generating synthetic datasets using the [omni.replicator](https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator.html "(in Omniverse Extensions)") extension. The resulting data is stored offline (on disk), making it readily available for training deep neural networks. The examples can be executed within the Isaac Sim Python [standalone](../introduction/workflows.html#standalone-application) environment. The example uses Isaac Sim and Replicator to create synthetic datasets offline (on disk) for the training of machine learning models.

In this tutorial you:

* Utilize and set up external customizable config files (YAML/JSON) to adjust simulation and scenario parameters
* Load custom environments
* Spawn assets using the Isaac Sim API
* Run randomized physics simulations
* Register various Replicator randomization [graphs](https://docs.omniverse.nvidia.com/extensions/latest/ext_omnigraph.html "(in Omniverse Extensions)")
* Create cameras and render products with the Replicator API
* Use Replicator writers to save data to disk

## Prerequisites

* Familiarity with the [omni.replicator](https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator.html "(in Omniverse Extensions)") extension, including its [annotators](https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator/annotators_details.html "(in Omniverse Extensions)") and [writers](https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator/writer_examples.html "(in Omniverse Extensions)").
* Basic understanding of Isaac Simâs [Stage](../reference_material/reference_glossary.html#isaac-sim-glossary-stage) and [World](../reference_material/reference_glossary.html#isaac-sim-glossary-world) concepts, further explained in the [Hello World](../core_api_tutorials/tutorial_core_hello_world.html#isaac-sim-app-tutorial-core-hello-world) tutorial.
* Running simulations as [Standalone Applications](../introduction/workflows.html#standalone-application) or via the [Script Editor](../development_tools/omniverse_script_editor.html#script-editor).
* Familiarity with Replicator [randomizers](https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator/randomizer_details.html "(in Omniverse Extensions)") and [OmniGraph](https://docs.omniverse.nvidia.com/extensions/latest/ext_omnigraph.html "(in Omniverse Extensions)") for a better understanding of the randomization pipeline.

## Scenario

By default, the scenario is executed in a warehouse environment. Within this setting, a forklift is randomly placed in a designated area. Based on the forkliftâs position, a pallet is placed in front of it at a randomized distance. Using Replicatorâs `scatter_2d` randomization function with the collision check argument `check_for_collisions` set to `True`, the pallet is scattered with boxes, ensuring the boxes do not self-collide. The scatter graph node randomly scatters the boxes in each capture frame. Additionally, a traffic cone is randomly positioned at one of the bottom corners of the forkliftâs oriented bounding box (OBB). Before the synthetic data generation (SDG) pipeline starts, a short physics simulation is executed, during which several boxes are dropped onto a pallet situated behind the forklift.

Three camera views are used for the synthetic data generation (SDG). The first (`top_view_cam`) offers a top-down view of the scenario (left), the second (`pallet_cam`) captures a randomized view of the boxes scattered on the pallet (center), and the third is overlooking the pallet from the driverâs place in the forklift using various heights (right).
The data is collected using Replicator writers with configurable backends. The default setup uses `BasicWriter` with a `DiskBackend`. The writerâs config parameters are loaded from the `writer_config` entry and used to initialize the writer with annotators including rgb, semantic\_segmentation, and bounding\_box\_3d. The output directory is specified in `backend_params`, which by default is `<working_dir>/_out_scene_based_sdg`.

## Getting Started

The main script of the tutorial is located at `<install_path>/standalone_examples/replicator/scene_based_sdg/scene_based_sdg.py` and it is set to run as a standalone application. The default configurations are stored in the script itself in the form of a Python dictionary, there is no need to provide a config file.

To overwrite the default configuration parameters, you can provided custom config files as a command-line argument for the script by using `--config <path/to/file.json/yaml>`. Example config files are stored in `scene_based_sdg/config/*`. In the provided examples, the configuration files serve as templates to illustrate and showcase the configurability of the script.

Helper functions are located in the `scene_based_sdg_utils.py` file.

To generate a synthetic dataset, run the following command for the Standalone Application (on Windows use `python.bat` instead of `python.sh`):

```python
./python.sh standalone_examples/replicator/scene_based_sdg/scene_based_sdg.py
```

## Implementation

The following section provides an implementation overview of the script. It includes details regarding the configuration parameters, scene generation helper functions, randomizations (Isaac Sim and Replicator), and data capture loop. As standalone example the script is split into two files: the main script and a utilities module.

Script Editor

Utils module and main script

```python
import asyncio
import math
import os

import carb.settings
import numpy as np
import omni.kit.app
import omni.replicator.core as rep
import omni.usd
from isaacsim.core.experimental.prims import GeomPrim, RigidPrim, XformPrim
from isaacsim.core.experimental.utils.bounds import (
    compute_combined_aabb,
    compute_obb,
    create_bbox_cache,
    get_obb_corners,
)
from isaacsim.core.experimental.utils.semantics import add_labels, remove_all_labels
from isaacsim.core.experimental.utils.stage import add_reference_to_stage, define_prim
from isaacsim.core.experimental.utils.transform import euler_angles_to_quaternion, quaternion_to_euler_angles
from isaacsim.core.simulation_manager import SimulationManager
from isaacsim.storage.native import get_assets_root_path_async
from pxr import Gf, Usd, UsdGeom

def setup_writer(config: dict) -> rep.Writer | None:
    """Setup and initialize writer with optional backend support."""

    def normalize_output_dir(params):
        if "output_dir" in params and not os.path.isabs(params["output_dir"]):
            params["output_dir"] = os.path.join(os.getcwd(), params["output_dir"])

    writer_type = config.get("writer", "BasicWriter")
    if writer_type not in rep.WriterRegistry.get_writers():
        print(f"[SDG] Writer type '{writer_type}' not found in registry.")
        return None

    writer = rep.WriterRegistry.get(writer_type)
    writer_kwargs = dict(config.get("writer_config", {}))
    normalize_output_dir(writer_kwargs)

    backend_type = config.get("backend_type")
    backend = None
    if backend_type:
        try:
            backend = rep.backends.get(backend_type)
        except Exception as e:
            print(f"[SDG] Backend '{backend_type}' not found: {e}")
            return None

        backend_params = dict(config.get("backend_params", {}))
        normalize_output_dir(backend_params)

        try:
            print(f"[SDG] Backend: {backend_type} | Params: {backend_params}")
            backend.initialize(**backend_params)
        except TypeError as e:
            print(f"[SDG] Invalid backend params: {e}")
            return None

    if "output_dir" in writer_kwargs:
        print(f"[SDG] Output: {writer_kwargs['output_dir']}")

    backend_info = f" + {backend_type}" if backend else ""
    print(f"[SDG] Writer: {writer_type}{backend_info} | Config: {writer_kwargs}")

    try:
        if backend:
            writer.initialize(backend=backend, **writer_kwargs)
        else:
            writer.initialize(**writer_kwargs)
    except TypeError as e:
        print(f"[SDG] Invalid writer params: {e}")
        return None

    return writer

async def simulate_falling_objects_async(
    forklift_prim: Usd.Prim,
    assets_root_path: str,
    config: dict,
    max_sim_steps: int = 250,
    num_boxes: int = 8,
    rng: np.random.Generator | None = None,
) -> None:
    """Run physics simulation to drop boxes on pallet near forklift."""
    if rng is None:
        rng = np.random.default_rng()

    forklift_transform = omni.usd.get_world_transform_matrix(forklift_prim)
    sim_pallet_offset = Gf.Matrix4d().SetTranslate(Gf.Vec3d(rng.uniform(-1, 1), rng.uniform(-4, -3.6), 0))
    sim_pallet_position = (sim_pallet_offset * forklift_transform).ExtractTranslation()
    sim_pallet_rotation = euler_angles_to_quaternion([0, 0, rng.uniform(0, math.pi)]).numpy()

    sim_pallet_path = "/World/SimulatedPallet"
    sim_pallet = define_prim(sim_pallet_path)
    add_reference_to_stage(assets_root_path + config["pallet"]["url"], sim_pallet_path)
    add_labels(sim_pallet, labels=[config["pallet"]["class"]], taxonomy="class")
    XformPrim(
        sim_pallet_path,
        positions=tuple(sim_pallet_position),
        orientations=sim_pallet_rotation,
        reset_xform_op_properties=True,
    )
    sim_pallet_geom = GeomPrim(f"{str(sim_pallet.GetPrimPath())}/.*", apply_collision_apis=True)
    sim_pallet_geom.set_collision_approximations("boundingCube")

    bbox_cache = create_bbox_cache()
    current_height = bbox_cache.ComputeLocalBound(sim_pallet).GetRange().GetSize()[2] * 1.1

    sim_box_rigid_prims = []
    for box_index in range(num_boxes):
        box_xy_offset = Gf.Vec3d(rng.uniform(-0.2, 0.2), rng.uniform(-0.2, 0.2), current_height)
        sim_box_path = f"/World/SimulatedCardbox_{box_index}"
        sim_box = define_prim(sim_box_path)
        add_reference_to_stage(assets_root_path + config["cardbox"]["url"], sim_box_path)
        add_labels(sim_box, labels=[config["cardbox"]["class"]], taxonomy="class")
        XformPrim(
            sim_box_path,
            positions=tuple(sim_pallet_position + box_xy_offset),
            orientations=sim_pallet_rotation,
            reset_xform_op_properties=True,
        )
        current_height += bbox_cache.ComputeLocalBound(sim_box).GetRange().GetSize()[2] * 1.1

        sim_box_geom = GeomPrim(f"{str(sim_box.GetPrimPath())}/.*", apply_collision_apis=True)
        sim_box_geom.set_collision_approximations("convexHull")
        sim_box_rigid_prims.append(RigidPrim(str(sim_box.GetPrimPath())))

    SimulationManager.set_physics_dt(1.0 / 90.0)
    SimulationManager.initialize_physics()

    velocity_threshold = 0.01
    for step in range(max_sim_steps):
        SimulationManager.step()
        if sim_box_rigid_prims:
            top_box_velocity = sim_box_rigid_prims[-1].get_velocities(indices=[0])[0].numpy()
            if np.linalg.norm(top_box_velocity) < velocity_threshold:
                print(f"[SDG] Simulation settled at step {step}")
                break
        await omni.kit.app.get_app().next_update_async()

def setup_camera_bounds(
    pallet_prim: Usd.Prim, forklift_prim: Usd.Prim, pallet_tf: Gf.Matrix4d, forklift_tf: Gf.Matrix4d
) -> dict[str, dict[str, tuple[float, float, float]]]:
    """Calculate camera randomization bounds for pallet, top view, and driver cameras."""
    pallet_pos = pallet_tf.ExtractTranslation()
    pallet_cam_bounds = {
        "min": (pallet_pos[0] - 2, pallet_pos[1] - 2, 2),
        "max": (pallet_pos[0] + 2, pallet_pos[1] + 2, 4),
    }

    forklift_pos = forklift_tf.ExtractTranslation()
    top_cam_bounds = {
        "min": (forklift_pos[0], forklift_pos[1], 9),
        "max": (forklift_pos[0], forklift_pos[1], 11),
    }

    driver_cam_pos = forklift_pos + Gf.Vec3d(0.0, 0.0, 1.9)
    driver_cam_bounds = {
        "min": (driver_cam_pos[0], driver_cam_pos[1], driver_cam_pos[2] - 0.25),
        "max": (driver_cam_pos[0], driver_cam_pos[1], driver_cam_pos[2] + 0.25),
    }

    return {
        "pallet_cam": pallet_cam_bounds,
        "top_cam": top_cam_bounds,
        "driver_cam": driver_cam_bounds,
    }

def create_scatter_plane_for_prim(
    prim: Usd.Prim, prim_tf: Gf.Matrix4d, parent_path: str, scale_factor: float = 0.8, visible: bool = False
) -> Usd.Prim:
    """Create scatter plane sized and aligned to prim surface."""
    bb_cache = create_bbox_cache()
    prim_bbox = bb_cache.ComputeLocalBound(prim)
    prim_bbox.Transform(prim_tf)
    prim_size = prim_bbox.GetRange().GetSize()

    prim_quat = prim_tf.ExtractRotation().GetQuaternion()
    prim_quat_xyzw = (prim_quat.GetReal(), *prim_quat.GetImaginary())
    prim_rotation_deg = quaternion_to_euler_angles(np.array(prim_quat_xyzw), degrees=True).numpy()

    prim_pos = prim_tf.ExtractTranslation()
    scatter_plane_scale = (prim_size[0] * scale_factor, prim_size[1] * scale_factor, 1)
    scatter_plane_pos = prim_pos + Gf.Vec3d(0, 0, prim_size[2])

    scatter_plane = rep.functional.create.plane(
        scale=scatter_plane_scale,
        position=tuple(scatter_plane_pos),
        rotation=tuple(prim_rotation_deg),
        visible=visible,
        parent=parent_path,
    )

    return scatter_plane

def setup_cone_placement_corners(
    forklift_prim: Usd.Prim, bb_cache=None, scale_factor: float = 1.3
) -> tuple[list[list[float]], tuple[float, float, float]]:
    """Calculate forklift OBB corners for cone placement."""
    if bb_cache is None:
        bb_cache = create_bbox_cache()

    forklift_obb_center, forklift_obb_axes, forklift_obb_extent = compute_obb(forklift_prim, bbox_cache=bb_cache)
    enlarged_extent = (
        forklift_obb_extent[0] * scale_factor,
        forklift_obb_extent[1] * scale_factor,
        forklift_obb_extent[2],
    )
    forklift_obb_corners = get_obb_corners(forklift_obb_center, forklift_obb_axes, enlarged_extent)

    cone_placement_corners = [
        forklift_obb_corners[0].tolist(),
        forklift_obb_corners[2].tolist(),
        forklift_obb_corners[4].tolist(),
        forklift_obb_corners[6].tolist(),
    ]

    forklift_obb_quat = Gf.Matrix3d(forklift_obb_axes).ExtractRotation().GetQuaternion()
    forklift_obb_quat_xyzw = (forklift_obb_quat.GetReal(), *forklift_obb_quat.GetImaginary())
    forklift_rotation_deg = quaternion_to_euler_angles(np.array(forklift_obb_quat_xyzw), degrees=True).numpy()

    return cone_placement_corners, forklift_rotation_deg

def register_lights_graph_randomizer(forklift_prim: Usd.Prim, pallet_prim: Usd.Prim, event_name: str) -> None:
    """Register graph randomizer for sphere lights."""
    bb_cache = create_bbox_cache()
    combined_bounds = compute_combined_aabb([forklift_prim, pallet_prim], bbox_cache=bb_cache)
    light_pos_min = (combined_bounds[0], combined_bounds[1], 6)
    light_pos_max = (combined_bounds[3], combined_bounds[4], 7)

    with rep.trigger.on_custom_event(event_name):
        rep.create.light(
            light_type="Sphere",
            color=rep.distribution.uniform((0.2, 0.1, 0.1), (0.9, 0.8, 0.8)),
            intensity=rep.distribution.uniform(2000, 4000),
            position=rep.distribution.uniform(light_pos_min, light_pos_max),
            scale=rep.distribution.uniform(1, 4),
            count=3,
        )

def register_cardboxes_materials_graph_randomizer(
    cardboxes: list[Usd.Prim], cardbox_material_urls: list[str], event_name: str
) -> None:
    """Register graph randomizer for cardbox materials."""
    cardbox_mesh_paths = []
    for cardbox in cardboxes:
        meshes = [child for child in cardbox.GetChildren() if child.IsA(UsdGeom.Mesh)]
        cardbox_mesh_paths.extend([mesh.GetPrimPath() for mesh in meshes])

    with rep.trigger.on_custom_event(event_name):
        cardbox_mesh_group_node = rep.create.group(cardbox_mesh_paths)
        with cardbox_mesh_group_node:
            rep.randomizer.materials(cardbox_material_urls)

async def run_example_async(config):
    assets_root_path = await get_assets_root_path_async()
    if assets_root_path is None:
        print("[SDG] Could not get nucleus server path")
        return

    # Load environment stage
    env_url = config.get("env_url", "/Isaac/Environments/Grid/default_environment.usd")
    env_path = env_url if env_url.startswith("omniverse://") else assets_root_path + env_url
    print(f"[SDG] Loading Stage {env_url}")
    omni.usd.get_context().open_stage(env_path)
    stage = omni.usd.get_context().get_stage()

    await omni.kit.app.get_app().next_update_async()

    # Initialize randomization
    rep.set_global_seed(42)
    rng = np.random.default_rng(42)

    # Configure replicator for manual triggering
    rep.orchestrator.set_capture_on_play(False)

    # Set DLSS to Quality mode for best SDG results
    carb.settings.get_settings().set("rtx/post/dlss/execMode", 2)

    # Clear previous semantic labels
    if config.get("clear_previous_semantics", True):
        for prim in stage.Traverse():
            remove_all_labels(prim, include_descendants=True)

    # Create SDG scope for organizing all generated objects
    define_prim("/SDG", "Scope")

    # Spawn forklift at random pose
    forklift_path = "/SDG/Forklift"
    forklift_prim = define_prim(forklift_path)
    add_reference_to_stage(assets_root_path + config["forklift"]["url"], forklift_path)
    add_labels(forklift_prim, labels=[config["forklift"]["class"]], taxonomy="class")
    XformPrim(
        forklift_path,
        positions=(rng.uniform(-20, -2), rng.uniform(-1, 3), 0),
        orientations=euler_angles_to_quaternion([0, 0, rng.uniform(0, math.pi)]).numpy(),
        reset_xform_op_properties=True,
    )

    # Spawn pallet in front of forklift with random offset
    forklift_tf = omni.usd.get_world_transform_matrix(forklift_prim)
    pallet_offset_tf = Gf.Matrix4d().SetTranslate(Gf.Vec3d(0, rng.uniform(-1.8, -1.2), 0))
    pallet_pos = tuple((pallet_offset_tf * forklift_tf).ExtractTranslation())
    forklift_quat = forklift_tf.ExtractRotationQuat()
    forklift_quat_xyzw = (forklift_quat.GetReal(), *forklift_quat.GetImaginary())

    pallet_path = "/SDG/Pallet"
    pallet_prim = define_prim(pallet_path)
    add_reference_to_stage(assets_root_path + config["pallet"]["url"], pallet_path)
    add_labels(pallet_prim, labels=[config["pallet"]["class"]], taxonomy="class")
    XformPrim(
        pallet_path,
        positions=pallet_pos,
        orientations=forklift_quat_xyzw,
        reset_xform_op_properties=True,
    )

    # Create cardboxes for pallet scattering
    cardboxes = []
    for i in range(5):
        cardbox_path = f"/SDG/CardBox_{i}"
        cardbox = define_prim(cardbox_path)
        add_reference_to_stage(assets_root_path + config["cardbox"]["url"], cardbox_path)
        add_labels(cardbox, labels=[config["cardbox"]["class"]], taxonomy="class")
        cardboxes.append(cardbox)

    # Create traffic cone for corner placement
    cone_path = "/SDG/Cone"
    cone = define_prim(cone_path)
    add_reference_to_stage(assets_root_path + config["cone"]["url"], cone_path)
    add_labels(cone, labels=[config["cone"]["class"]], taxonomy="class")

    # Create cameras
    rep.functional.create.scope(name="Cameras", parent="/SDG")
    driver_cam = rep.functional.create.camera(
        focus_distance=400.0,
        focal_length=24.0,
        clipping_range=(0.1, 10000000.0),
        name="DriverCam",
        parent="/SDG/Cameras",
    )
    pallet_cam = rep.functional.create.camera(name="PalletCam", parent="/SDG/Cameras")
    top_view_cam = rep.functional.create.camera(clipping_range=(6.0, 1000000.0), name="TopCam", parent="/SDG/Cameras")

    await omni.kit.app.get_app().next_update_async()

    # Setup render products
    resolution = config.get("resolution", (512, 512))
    forklift_rp = rep.create.render_product(top_view_cam, resolution, name="TopView")
    driver_rp = rep.create.render_product(driver_cam, resolution, name="DriverView")
    pallet_rp = rep.create.render_product(pallet_cam, resolution, name="PalletView")

    render_products = [forklift_rp, driver_rp, pallet_rp]
    for render_product in render_products:
        render_product.hydra_texture.set_updates_enabled(False)

    # Initialize writer and attach to render products
    writer = setup_writer(config)
    if not writer:
        print("[SDG] Failed to setup writer")
        return

    writer.attach(render_products)

    for render_product in render_products:
        render_product.hydra_texture.set_updates_enabled(True)

    rt_subframes = config.get("rt_subframes", -1)

    # Calculate camera randomization bounds
    pallet_tf = omni.usd.get_world_transform_matrix(pallet_prim)
    camera_bounds = setup_camera_bounds(pallet_prim, forklift_prim, pallet_tf, forklift_tf)
    pallet_cam_bounds_min = camera_bounds["pallet_cam"]["min"]
    pallet_cam_bounds_max = camera_bounds["pallet_cam"]["max"]
    top_cam_bounds_min = camera_bounds["top_cam"]["min"]
    top_cam_bounds_max = camera_bounds["top_cam"]["max"]
    driver_cam_bounds_min = camera_bounds["driver_cam"]["min"]
    driver_cam_bounds_max = camera_bounds["driver_cam"]["max"]

    # Setup scatter plane and cone placement
    scatter_plane = create_scatter_plane_for_prim(pallet_prim, pallet_tf, parent_path="/SDG", scale_factor=0.8)
    cone_placement_corners, forklift_rotation_deg = setup_cone_placement_corners(forklift_prim)

    # Register graph-based randomizers for lights and materials
    register_lights_graph_randomizer(forklift_prim, pallet_prim, event_name="randomize_lights")

    cardbox_material_urls = [
        f"{assets_root_path}/Isaac/Environments/Simple_Warehouse/Materials/MI_PaperNotes_01.mdl",
        f"{assets_root_path}/Isaac/Environments/Simple_Warehouse/Materials/MI_CardBoxB_05.mdl",
    ]
    register_cardboxes_materials_graph_randomizer(
        cardboxes, cardbox_material_urls, event_name="randomize_cardboxes_materials"
    )

    # Run physics simulation to settle boxes on pallet
    await simulate_falling_objects_async(forklift_prim, assets_root_path, config, rng=rng)

    # SDG loop - generate frames with randomizations
    num_frames = config.get("num_frames", 10)
    print(f"[SDG] Running SDG for {num_frames} frames")
    for i in range(num_frames):
        print(f"[SDG] Frame {i}/{num_frames}")

        print(f"[SDG]  Randomizing boxes on pallet.")
        rep.functional.randomizer.scatter_2d(
            prims=cardboxes, surface_prims=scatter_plane, check_for_collisions=True, rng=rng
        )

        print(f"[SDG]  Randomizing boxes materials.")
        rep.utils.send_og_event(event_name="randomize_cardboxes_materials")
        print(f"[SDG]  Randomizing lights.")
        rep.utils.send_og_event(event_name="randomize_lights")

        print(f"[SDG]  Randomizing pallet camera.")
        rep.functional.modify.pose(
            pallet_cam,
            position_value=rng.uniform(pallet_cam_bounds_min, pallet_cam_bounds_max),
            look_at_value=pallet_prim,
            look_at_up_axis=(0, 0, 1),
        )

        print(f"[SDG]  Randomizing driver camera.")
        rep.functional.modify.pose(
            driver_cam,
            position_value=rng.uniform(driver_cam_bounds_min, driver_cam_bounds_max),
            look_at_value=pallet_prim,
            look_at_up_axis=(0, 0, 1),
        )

        if i % 2 == 0:
            print(f"[SDG]  Randomizing cone position.")
            selected_corner = cone_placement_corners[rng.integers(0, len(cone_placement_corners))]
            rep.functional.modify.pose(
                cone,
                position_value=selected_corner,
            )

        if i % 4 == 0:
            print(f"[SDG]  Randomizing top view camera.")
            roll_angle = rng.uniform(0, 2 * np.pi)
            rep.functional.modify.pose(
                top_view_cam,
                position_value=rng.uniform(top_cam_bounds_min, top_cam_bounds_max),
                look_at_value=forklift_prim,
                look_at_up_axis=(np.cos(roll_angle), np.sin(roll_angle), 0.0),
            )

        print(f"[SDG]  Capturing frame with rt_subframes={rt_subframes}")
        await rep.orchestrator.step_async(delta_time=0.0, rt_subframes=rt_subframes)

    # Cleanup
    await rep.orchestrator.wait_until_complete_async()
    writer.detach()
    for render_product in render_products:
        render_product.destroy()

    print("[SDG] Complete")

config = {
    "resolution": [512, 512],
    "rt_subframes": 32,
    "num_frames": 10,
    "env_url": "/Isaac/Environments/Simple_Warehouse/full_warehouse.usd",
    "writer": "BasicWriter",
    "backend_type": "DiskBackend",
    "backend_params": {
        "output_dir": "_out_scene_based_sdg",
    },
    "writer_config": {
        "rgb": True,
        "bounding_box_2d_tight": True,
        "semantic_segmentation": True,
        "distance_to_image_plane": True,
        "bounding_box_3d": True,
        "occlusion": True,
    },
    "clear_previous_semantics": True,
    "forklift": {
        "url": "/Isaac/Props/Forklift/forklift.usd",
        "class": "forklift",
    },
    "cone": {
        "url": "/Isaac/Environments/Simple_Warehouse/Props/S_TrafficCone.usd",
        "class": "traffic_cone",
    },
    "pallet": {
        "url": "/Isaac/Environments/Simple_Warehouse/Props/SM_PaletteA_01.usd",
        "class": "pallet",
    },
    "cardbox": {
        "url": "/Isaac/Environments/Simple_Warehouse/Props/SM_CardBoxD_04.usd",
        "class": "cardbox",
    },
}

asyncio.ensure_future(run_example_async(config))
```

Standalone Application

Main script

```python
"""Generate offline synthetic dataset."""

import argparse
import json
import math
import os

import numpy as np
import yaml
from isaacsim import SimulationApp

# Default configuration
config = {
    "launch_config": {
        "renderer": "RealTimePathTracing",
        "headless": False,
    },
    "resolution": [512, 512],
    "rt_subframes": 32,
    "num_frames": 10,
    "env_url": "/Isaac/Environments/Simple_Warehouse/full_warehouse.usd",
    "writer": "BasicWriter",
    "backend_type": "DiskBackend",
    "backend_params": {
        "output_dir": "_out_scene_based_sdg",
    },
    "writer_config": {
        "rgb": True,
        "bounding_box_2d_tight": True,
        "semantic_segmentation": True,
        "distance_to_image_plane": True,
        "bounding_box_3d": True,
        "occlusion": True,
    },
    "clear_previous_semantics": True,
    "forklift": {
        "url": "/Isaac/Props/Forklift/forklift.usd",
        "class": "forklift",
    },
    "cone": {
        "url": "/Isaac/Environments/Simple_Warehouse/Props/S_TrafficCone.usd",
        "class": "traffic_cone",
    },
    "pallet": {
        "url": "/Isaac/Environments/Simple_Warehouse/Props/SM_PaletteA_01.usd",
        "class": "pallet",
    },
    "cardbox": {
        "url": "/Isaac/Environments/Simple_Warehouse/Props/SM_CardBoxD_04.usd",
        "class": "cardbox",
    },
    "close_app_after_run": True,
}

import carb

# Parse command line arguments for optional config file
parser = argparse.ArgumentParser()
parser.add_argument("--config", required=False, help="Include specific config parameters (json or yaml))")
args, unknown = parser.parse_known_args()

# Load config file if provided
args_config = {}
if args.config and os.path.isfile(args.config):
    print("File exist")
    with open(args.config) as f:
        if args.config.endswith(".json"):
            args_config = json.load(f)
        elif args.config.endswith(".yaml"):
            args_config = yaml.safe_load(f)
        else:
            carb.log_warn(f"File {args.config} is not json or yaml, will use default config")
else:
    carb.log_warn(f"File {args.config} does not exist, will use default config")

# Clear default writer_config if overridden in args
if "writer_config" in args_config:
    config["writer_config"].clear()

# Merge args config into default config
config.update(args_config)

# Initialize simulation app
simulation_app = SimulationApp(launch_config=config["launch_config"])

import carb.settings

# Runtime modules (must import after SimulationApp creation)
import omni.replicator.core as rep
import omni.usd
import scene_based_sdg_utils
from isaacsim.core.experimental.prims import XformPrim
from isaacsim.core.experimental.utils.semantics import add_labels, remove_all_labels
from isaacsim.core.experimental.utils.stage import add_reference_to_stage, define_prim, get_current_stage, open_stage
from isaacsim.core.experimental.utils.transform import euler_angles_to_quaternion
from isaacsim.storage.native import get_assets_root_path
from pxr import Gf

# Get assets root path from nucleus server
assets_root_path = get_assets_root_path()
if assets_root_path is None:
    carb.log_error("Could not get nucleus server path, closing application..")
    simulation_app.close()

# Load environment stage
print(f"[SDG] Loading Stage {config['env_url']}")
stage_opened, _ = open_stage(assets_root_path + config["env_url"])
if not stage_opened:
    carb.log_error(f"Could not open stage{config['env_url']}, closing application..")
    simulation_app.close()

# Initialize randomization
rep.set_global_seed(42)
rng = np.random.default_rng(42)

# Configure replicator for manual triggering
rep.orchestrator.set_capture_on_play(False)

# Set DLSS to Quality mode for best SDG results
carb.settings.get_settings().set("rtx/post/dlss/execMode", 2)

# Clear previous semantic labels
if config["clear_previous_semantics"]:
    for prim in get_current_stage().Traverse():
        remove_all_labels(prim, include_descendants=True)

# Create SDG scope for organizing all generated objects
define_prim("/SDG", "Scope")

# Spawn forklift at random pose
forklift_path = "/SDG/Forklift"
forklift_prim = define_prim(forklift_path)
add_reference_to_stage(assets_root_path + config["forklift"]["url"], forklift_path)
add_labels(forklift_prim, labels=[config["forklift"]["class"]], taxonomy="class")
XformPrim(
    forklift_path,
    positions=(rng.uniform(-20, -2), rng.uniform(-1, 3), 0),
    orientations=euler_angles_to_quaternion([0, 0, rng.uniform(0, math.pi)]).numpy(),
    reset_xform_op_properties=True,
)

# Spawn pallet in front of forklift with random offset
forklift_tf = omni.usd.get_world_transform_matrix(forklift_prim)
pallet_offset_tf = Gf.Matrix4d().SetTranslate(Gf.Vec3d(0, rng.uniform(-1.8, -1.2), 0))
pallet_pos = tuple((pallet_offset_tf * forklift_tf).ExtractTranslation())
forklift_quat = forklift_tf.ExtractRotationQuat()
forklift_quat_xyzw = (forklift_quat.GetReal(), *forklift_quat.GetImaginary())

pallet_path = "/SDG/Pallet"
pallet_prim = define_prim(pallet_path)
add_reference_to_stage(assets_root_path + config["pallet"]["url"], pallet_path)
add_labels(pallet_prim, labels=[config["pallet"]["class"]], taxonomy="class")
XformPrim(
    pallet_path,
    positions=pallet_pos,
    orientations=forklift_quat_xyzw,
    reset_xform_op_properties=True,
)

# Create cardboxes for pallet scattering
cardboxes = []
for i in range(5):
    cardbox_path = f"/SDG/CardBox_{i}"
    cardbox = define_prim(cardbox_path)
    add_reference_to_stage(assets_root_path + config["cardbox"]["url"], cardbox_path)
    add_labels(cardbox, labels=[config["cardbox"]["class"]], taxonomy="class")
    cardboxes.append(cardbox)

# Create traffic cone for corner placement
cone_path = "/SDG/Cone"
cone = define_prim(cone_path)
add_reference_to_stage(assets_root_path + config["cone"]["url"], cone_path)
add_labels(cone, labels=[config["cone"]["class"]], taxonomy="class")

# Create cameras
rep.functional.create.scope(name="Cameras", parent="/SDG")
driver_cam = rep.functional.create.camera(
    focus_distance=400.0, focal_length=24.0, clipping_range=(0.1, 10000000.0), name="DriverCam", parent="/SDG/Cameras"
)
pallet_cam = rep.functional.create.camera(name="PalletCam", parent="/SDG/Cameras")
top_view_cam = rep.functional.create.camera(clipping_range=(6.0, 1000000.0), name="TopCam", parent="/SDG/Cameras")

# Setup render products
resolution = config.get("resolution", (512, 512))
forklift_rp = rep.create.render_product(top_view_cam, resolution, name="TopView")
driver_rp = rep.create.render_product(driver_cam, resolution, name="DriverView")
pallet_rp = rep.create.render_product(pallet_cam, resolution, name="PalletView")

render_products = [forklift_rp, driver_rp, pallet_rp]
for render_product in render_products:
    render_product.hydra_texture.set_updates_enabled(False)

# Initialize writer and attach to render products
writer = scene_based_sdg_utils.setup_writer(config)
if not writer:
    carb.log_error("[SDG] Failed to setup writer, closing application.")
    simulation_app.close()

writer.attach(render_products)

for render_product in render_products:
    render_product.hydra_texture.set_updates_enabled(True)

# Configure raytracing subframes for material loading and motion artifacts
rt_subframes = config.get("rt_subframes", -1)

# Calculate camera randomization bounds
pallet_tf = omni.usd.get_world_transform_matrix(pallet_prim)
camera_bounds = scene_based_sdg_utils.setup_camera_bounds(pallet_prim, forklift_prim, pallet_tf, forklift_tf)
pallet_cam_bounds_min = camera_bounds["pallet_cam"]["min"]
pallet_cam_bounds_max = camera_bounds["pallet_cam"]["max"]
top_cam_bounds_min = camera_bounds["top_cam"]["min"]
top_cam_bounds_max = camera_bounds["top_cam"]["max"]
driver_cam_bounds_min = camera_bounds["driver_cam"]["min"]
driver_cam_bounds_max = camera_bounds["driver_cam"]["max"]

# Setup scatter plane and cone placement
scatter_plane = scene_based_sdg_utils.create_scatter_plane_for_prim(
    pallet_prim, pallet_tf, parent_path="/SDG", scale_factor=0.8
)
cone_placement_corners, forklift_rotation_deg = scene_based_sdg_utils.setup_cone_placement_corners(forklift_prim)

# Register graph-based randomizers for lights and materials
scene_based_sdg_utils.register_lights_graph_randomizer(forklift_prim, pallet_prim, event_name="randomize_lights")

cardbox_material_urls = [
    f"{assets_root_path}/Isaac/Environments/Simple_Warehouse/Materials/MI_PaperNotes_01.mdl",
    f"{assets_root_path}/Isaac/Environments/Simple_Warehouse/Materials/MI_CardBoxB_05.mdl",
]
scene_based_sdg_utils.register_cardboxes_materials_graph_randomizer(
    cardboxes, cardbox_material_urls, event_name="randomize_cardboxes_materials"
)

# Run physics simulation to settle boxes on pallet
scene_based_sdg_utils.simulate_falling_objects(forklift_prim, assets_root_path, config, rng=rng)

# SDG loop - generate frames with randomizations
num_frames = config.get("num_frames", 0)
print(f"[SDG] Running SDG for {num_frames} frames")
for i in range(num_frames):
    print(f"[SDG] Frame {i}/{num_frames}")

    print(f"[SDG]  Randomizing boxes on pallet.")
    rep.functional.randomizer.scatter_2d(
        prims=cardboxes, surface_prims=scatter_plane, check_for_collisions=True, rng=rng
    )

    print(f"[SDG]  Randomizing boxes materials.")
    rep.utils.send_og_event(event_name="randomize_cardboxes_materials")
    print(f"[SDG]  Randomizing lights.")
    rep.utils.send_og_event(event_name="randomize_lights")

    print(f"[SDG]  Randomizing pallet camera.")
    rep.functional.modify.pose(
        pallet_cam,
        position_value=rng.uniform(pallet_cam_bounds_min, pallet_cam_bounds_max),
        look_at_value=pallet_prim,
        look_at_up_axis=(0, 0, 1),
    )

    print(f"[SDG]  Randomizing driver camera.")
    rep.functional.modify.pose(
        driver_cam,
        position_value=rng.uniform(driver_cam_bounds_min, driver_cam_bounds_max),
        look_at_value=pallet_prim,
        look_at_up_axis=(0, 0, 1),
    )

    if i % 2 == 0:
        print(f"[SDG]  Randomizing cone position.")
        selected_corner = cone_placement_corners[rng.integers(0, len(cone_placement_corners))]
        rep.functional.modify.pose(
            cone,
            position_value=selected_corner,
        )

    if i % 4 == 0:
        print(f"[SDG]  Randomizing top view camera.")
        roll_angle = rng.uniform(0, 2 * np.pi)
        rep.functional.modify.pose(
            top_view_cam,
            position_value=rng.uniform(top_cam_bounds_min, top_cam_bounds_max),
            look_at_value=forklift_prim,
            look_at_up_axis=(np.cos(roll_angle), np.sin(roll_angle), 0.0),
        )

    print(f"[SDG]  Capturing frame with rt_subframes={rt_subframes}")
    rep.orchestrator.step(delta_time=0.0, rt_subframes=rt_subframes)

# Cleanup
rep.orchestrator.wait_until_complete()
writer.detach()
for render_product in render_products:
    render_product.destroy()

# Check if the application should keep running after data generation
close_app_after_run = config.get("close_app_after_run", True)
if config["launch_config"]["headless"]:
    if not close_app_after_run:
        print("[SDG] 'close_app_after_run' is ignored when running headless. The application will be closed.")
elif not close_app_after_run:
    print("[SDG] The application will not be closed after the run. Make sure to close it manually.")
    while simulation_app.is_running():
        simulation_app.update()
simulation_app.close()
```

Utils module

```python
"""Provide utility functions for scene-based synthetic data generation."""

import math
import os

import carb
import numpy as np
import omni.replicator.core as rep
import omni.usd
from isaacsim.core.experimental.prims import GeomPrim, RigidPrim, XformPrim
from isaacsim.core.experimental.utils.bounds import (
    compute_combined_aabb,
    compute_obb,
    create_bbox_cache,
    get_obb_corners,
)
from isaacsim.core.experimental.utils.semantics import add_labels
from isaacsim.core.experimental.utils.stage import add_reference_to_stage, define_prim
from isaacsim.core.experimental.utils.transform import euler_angles_to_quaternion, quaternion_to_euler_angles
from isaacsim.core.simulation_manager import SimulationManager
from pxr import Gf, Usd, UsdGeom

def setup_writer(config: dict) -> rep.Writer | None:
    """Setup and initialize writer with optional backend support and error handling."""

    def normalize_output_dir(params):
        """Convert relative output_dir to absolute path."""
        if "output_dir" in params and not os.path.isabs(params["output_dir"]):
            params["output_dir"] = os.path.join(os.getcwd(), params["output_dir"])

    # Get writer from registry
    writer_type = config.get("writer", "BasicWriter")
    if writer_type not in rep.WriterRegistry.get_writers():
        carb.log_error(f"[SDG] Writer type '{writer_type}' not found in registry.")
        return None

    writer = rep.WriterRegistry.get(writer_type)
    writer_kwargs = dict(config.get("writer_config", {}))
    normalize_output_dir(writer_kwargs)

    # Initialize backend if specified
    backend_type = config.get("backend_type")
    backend = None
    if backend_type:
        try:
            backend = rep.backends.get(backend_type)
        except Exception as e:
            carb.log_error(f"[SDG] Backend '{backend_type}' not found: {e}")
            return None

        backend_params = dict(config.get("backend_params", {}))
        normalize_output_dir(backend_params)

        try:
            print(f"[SDG] Backend: {backend_type} | Params: {backend_params}")
            backend.initialize(**backend_params)
        except TypeError as e:
            carb.log_error(f"[SDG] Invalid backend params: {e}")
            return None

    # Initialize writer
    if "output_dir" in writer_kwargs:
        print(f"[SDG] Output: {writer_kwargs['output_dir']}")

    backend_info = f" + {backend_type}" if backend else ""
    print(f"[SDG] Writer: {writer_type}{backend_info} | Config: {writer_kwargs}")

    try:
        if backend:
            writer.initialize(backend=backend, **writer_kwargs)
        else:
            writer.initialize(**writer_kwargs)
    except TypeError as e:
        carb.log_error(f"[SDG] Invalid writer params: {e}")
        return None

    return writer

def simulate_falling_objects(
    forklift_prim: Usd.Prim,
    assets_root_path: str,
    config: dict,
    max_sim_steps: int = 250,
    num_boxes: int = 8,
    rng: np.random.Generator | None = None,
) -> None:
    """Run physics simulation to drop boxes on pallet near forklift."""
    if rng is None:
        rng = np.random.default_rng()

    forklift_transform = omni.usd.get_world_transform_matrix(forklift_prim)
    sim_pallet_offset = Gf.Matrix4d().SetTranslate(Gf.Vec3d(rng.uniform(-1, 1), rng.uniform(-4, -3.6), 0))
    sim_pallet_position = (sim_pallet_offset * forklift_transform).ExtractTranslation()
    sim_pallet_rotation = euler_angles_to_quaternion([0, 0, rng.uniform(0, math.pi)]).numpy()

    sim_pallet_path = "/World/SimulatedPallet"
    sim_pallet = define_prim(sim_pallet_path)
    add_reference_to_stage(assets_root_path + config["pallet"]["url"], sim_pallet_path)
    add_labels(sim_pallet, labels=[config["pallet"]["class"]], taxonomy="class")
    XformPrim(
        sim_pallet_path,
        positions=tuple(sim_pallet_position),
        orientations=sim_pallet_rotation,
        reset_xform_op_properties=True,
    )
    sim_pallet_geom = GeomPrim(f"{str(sim_pallet.GetPrimPath())}/.*", apply_collision_apis=True)
    sim_pallet_geom.set_collision_approximations("boundingCube")

    bbox_cache = create_bbox_cache()
    current_height = bbox_cache.ComputeLocalBound(sim_pallet).GetRange().GetSize()[2] * 1.1

    sim_box_rigid_prims = []
    for box_index in range(num_boxes):
        box_xy_offset = Gf.Vec3d(rng.uniform(-0.2, 0.2), rng.uniform(-0.2, 0.2), current_height)
        sim_box_path = f"/World/SimulatedCardbox_{box_index}"
        sim_box = define_prim(sim_box_path)
        add_reference_to_stage(assets_root_path + config["cardbox"]["url"], sim_box_path)
        add_labels(sim_box, labels=[config["cardbox"]["class"]], taxonomy="class")
        XformPrim(
            sim_box_path,
            positions=tuple(sim_pallet_position + box_xy_offset),
            orientations=sim_pallet_rotation,
            reset_xform_op_properties=True,
        )
        current_height += bbox_cache.ComputeLocalBound(sim_box).GetRange().GetSize()[2] * 1.1

        sim_box_geom = GeomPrim(f"{str(sim_box.GetPrimPath())}/.*", apply_collision_apis=True)
        sim_box_geom.set_collision_approximations("convexHull")
        sim_box_rigid_prims.append(RigidPrim(str(sim_box.GetPrimPath())))

    SimulationManager.set_physics_dt(1.0 / 90.0)
    SimulationManager.initialize_physics()

    velocity_threshold = 0.01
    for step in range(max_sim_steps):
        SimulationManager.step()
        if sim_box_rigid_prims:
            top_box_velocity = sim_box_rigid_prims[-1].get_velocities(indices=[0])[0].numpy()
            if np.linalg.norm(top_box_velocity) < velocity_threshold:
                print(f"[SDG] Simulation settled at step {step}")
                break

def setup_camera_bounds(
    pallet_prim: Usd.Prim, forklift_prim: Usd.Prim, pallet_tf: Gf.Matrix4d, forklift_tf: Gf.Matrix4d
) -> dict[str, dict[str, tuple[float, float, float]]]:
    """Calculate camera randomization bounds for pallet, top view, and driver cameras."""
    pallet_pos = pallet_tf.ExtractTranslation()
    pallet_cam_bounds = {
        "min": (pallet_pos[0] - 2, pallet_pos[1] - 2, 2),
        "max": (pallet_pos[0] + 2, pallet_pos[1] + 2, 4),
    }

    forklift_pos = forklift_tf.ExtractTranslation()
    top_cam_bounds = {
        "min": (forklift_pos[0], forklift_pos[1], 9),
        "max": (forklift_pos[0], forklift_pos[1], 11),
    }

    driver_cam_pos = forklift_pos + Gf.Vec3d(0.0, 0.0, 1.9)
    driver_cam_bounds = {
        "min": (driver_cam_pos[0], driver_cam_pos[1], driver_cam_pos[2] - 0.25),
        "max": (driver_cam_pos[0], driver_cam_pos[1], driver_cam_pos[2] + 0.25),
    }

    return {
        "pallet_cam": pallet_cam_bounds,
        "top_cam": top_cam_bounds,
        "driver_cam": driver_cam_bounds,
    }

def create_scatter_plane_for_prim(
    prim: Usd.Prim, prim_tf: Gf.Matrix4d, parent_path: str, scale_factor: float = 0.8, visible: bool = False
) -> Usd.Prim:
    """Create scatter plane sized and aligned to prim surface."""
    bb_cache = create_bbox_cache()
    prim_bbox = bb_cache.ComputeLocalBound(prim)
    prim_bbox.Transform(prim_tf)
    prim_size = prim_bbox.GetRange().GetSize()

    prim_quat = prim_tf.ExtractRotation().GetQuaternion()
    prim_quat_xyzw = (prim_quat.GetReal(), *prim_quat.GetImaginary())
    prim_rotation_deg = quaternion_to_euler_angles(np.array(prim_quat_xyzw), degrees=True).numpy()

    prim_pos = prim_tf.ExtractTranslation()
    scatter_plane_scale = (prim_size[0] * scale_factor, prim_size[1] * scale_factor, 1)
    scatter_plane_pos = prim_pos + Gf.Vec3d(0, 0, prim_size[2])

    scatter_plane = rep.functional.create.plane(
        scale=scatter_plane_scale,
        position=tuple(scatter_plane_pos),
        rotation=tuple(prim_rotation_deg),
        visible=visible,
        parent=parent_path,
    )

    return scatter_plane

def setup_cone_placement_corners(
    forklift_prim: Usd.Prim, bb_cache=None, scale_factor: float = 1.3
) -> tuple[list[list[float]], tuple[float, float, float]]:
    """Calculate forklift OBB corners for cone placement."""
    if bb_cache is None:
        bb_cache = create_bbox_cache()

    forklift_obb_center, forklift_obb_axes, forklift_obb_extent = compute_obb(forklift_prim, bbox_cache=bb_cache)
    enlarged_extent = (
        forklift_obb_extent[0] * scale_factor,
        forklift_obb_extent[1] * scale_factor,
        forklift_obb_extent[2],
    )
    forklift_obb_corners = get_obb_corners(forklift_obb_center, forklift_obb_axes, enlarged_extent)

    cone_placement_corners = [
        forklift_obb_corners[0].tolist(),
        forklift_obb_corners[2].tolist(),
        forklift_obb_corners[4].tolist(),
        forklift_obb_corners[6].tolist(),
    ]

    forklift_obb_quat = Gf.Matrix3d(forklift_obb_axes).ExtractRotation().GetQuaternion()
    forklift_obb_quat_xyzw = (forklift_obb_quat.GetReal(), *forklift_obb_quat.GetImaginary())
    forklift_rotation_deg = quaternion_to_euler_angles(np.array(forklift_obb_quat_xyzw), degrees=True).numpy()

    return cone_placement_corners, forklift_rotation_deg

def register_lights_graph_randomizer(forklift_prim: Usd.Prim, pallet_prim: Usd.Prim, event_name: str) -> None:
    """Register graph randomizer for sphere lights."""
    bb_cache = create_bbox_cache()
    combined_bounds = compute_combined_aabb([forklift_prim, pallet_prim], bbox_cache=bb_cache)
    light_pos_min = (combined_bounds[0], combined_bounds[1], 6)
    light_pos_max = (combined_bounds[3], combined_bounds[4], 7)

    with rep.trigger.on_custom_event(event_name):
        rep.create.light(
            light_type="Sphere",
            color=rep.distribution.uniform((0.2, 0.1, 0.1), (0.9, 0.8, 0.8)),
            intensity=rep.distribution.uniform(2000, 4000),
            position=rep.distribution.uniform(light_pos_min, light_pos_max),
            scale=rep.distribution.uniform(1, 4),
            count=3,
        )

def register_cardboxes_materials_graph_randomizer(
    cardboxes: list[Usd.Prim], cardbox_material_urls: list[str], event_name: str
) -> None:
    """Register graph randomizer for cardbox materials."""
    cardbox_mesh_paths = []
    for cardbox in cardboxes:
        meshes = [child for child in cardbox.GetChildren() if child.IsA(UsdGeom.Mesh)]
        cardbox_mesh_paths.extend([mesh.GetPrimPath() for mesh in meshes])

    with rep.trigger.on_custom_event(event_name):
        cardbox_mesh_group_node = rep.create.group(cardbox_mesh_paths)
        with cardbox_mesh_group_node:
            rep.randomizer.materials(cardbox_material_urls)
```

## Config Scenarios

The following provides details about the various config scenarios:

Built-in

Without an explicit config file, the script uses the default parameters stored in the script itself. The default parameters are the following:

Built-in (default) Config

```python
config = {
    "launch_config": {
        "renderer": "RealTimePathTracing",
        "headless": False,
    },
    "resolution": [512, 512],
    "rt_subframes": 32,
    "num_frames": 10,
    "env_url": "/Isaac/Environments/Simple_Warehouse/full_warehouse.usd",
    "writer": "BasicWriter",
    "backend_type": "DiskBackend",
    "backend_params": {
        "output_dir": "_out_scene_based_sdg",
    },
    "writer_config": {
        "rgb": True,
        "bounding_box_2d_tight": True,
        "semantic_segmentation": True,
        "distance_to_image_plane": True,
        "bounding_box_3d": True,
        "occlusion": True,
    },
    "clear_previous_semantics": True,
    "forklift": {
        "url": "/Isaac/Props/Forklift/forklift.usd",
        "class": "forklift",
    },
    "cone": {
        "url": "/Isaac/Environments/Simple_Warehouse/Props/S_TrafficCone.usd",
        "class": "traffic_cone",
    },
    "pallet": {
        "url": "/Isaac/Environments/Simple_Warehouse/Props/SM_PaletteA_01.usd",
        "class": "pallet",
    },
    "cardbox": {
        "url": "/Isaac/Environments/Simple_Warehouse/Props/SM_CardBoxD_04.usd",
        "class": "cardbox",
    },
    "close_app_after_run": True,
}
```

The following command runs the script with the default parameters:

```python
./python.sh standalone_examples/replicator/scene_based_sdg/scene_based_sdg.py
```

Basic Writer

Using the `config_basic_writer.yaml` config file explictly chooses `BasicWriter` with the given `writer_config` configurations. It also changes the environment to `/Isaac/Environments/Grid/default_environment.usd`.

Custom YAML Config

```python
launch_config:
  renderer: RealTimePathTracing
  headless: false
resolution: [512, 512]
env_url: "/Isaac/Environments/Grid/default_environment.usd"
rt_subframes: 32
writer: BasicWriter
backend_type: DiskBackend
backend_params:
  output_dir: _out_basicwriter
writer_config:
  rgb: true
```

The following command runs the script with the custom parameters:

```python
./python.sh standalone_examples/replicator/scene_based_sdg/scene_based_sdg.py \
    --config standalone_examples/replicator/scene_based_sdg/config/config_basic_writer.yaml
```

Default Writer

The `config_default_writer.json` uses the default writer (which is still the `BasicWriter`) and changes the `writer_config` values to **rgb** and **instance\_segmentation** annotators.

Custom JSON Config

```python
{
    "launch_config": {
        "renderer": "RealTimePathTracing",
        "headless": false
    },
    "resolution": [512, 512],
    "backend_type": "DiskBackend",
    "backend_params": {
        "output_dir": "_out_defaultwriter"
    },
    "writer_config": {
        "rgb": true,
        "instance_segmentation": true
    }
}
```

The following command runs the script with the custom parameters:

```python
./python.sh standalone_examples/replicator/scene_based_sdg/scene_based_sdg.py \
    --config standalone_examples/replicator/scene_based_sdg/config/config_default_writer.json
```

Kitti Writer

The `config_kitti_writer.yaml` config file uses `KittiWriter` with the given `writer_config` configurations.

Custom YAML Config using KittiWriter

```python
launch_config:
  renderer: RealTimePathTracing
  headless: true
resolution: [512, 512]
num_frames: 5
clear_previous_semantics: false
writer: KittiWriter
backend_type: null
writer_config:
  output_dir: _out_kitti
  colorize_instance_segmentation: true
  mapping_dict:
    forklift: [11, 110, 223, 255]
    pallet: [211, 210, 223, 255]
```

The following command runs the script with the custom parameters:

```python
./python.sh standalone_examples/replicator/scene_based_sdg/scene_based_sdg.py \
    --config standalone_examples/replicator/scene_based_sdg/config/config_kitti_writer.yaml
```

Coco Writer

The `config_coco_writer.yaml` config file uses `CocoWriter` with the given `writer_config` configurations.

Custom YAML Config using CocoWriter

```python
launch_config:
  renderer: RealTimePathTracing
  headless: true
resolution: [512, 512]
num_frames: 5
clear_previous_semantics: true
backend_type: null
writer: CocoWriter
writer_config:
  output_dir: _out_coco
  coco_categories:
    forklift:
      name: forklift
      id: 333
      supercategory: warehouse
      color: [211, 111, 211]
      isthing: 1
    pallet:
      name: pallet
      id: 313
      supercategory: warehouse
      color: [141, 111, 131]
      isthing: 1
```

The following command runs the script with the custom parameters:

```python
./python.sh standalone_examples/replicator/scene_based_sdg/scene_based_sdg.py \
    --config standalone_examples/replicator/scene_based_sdg/config/config_coco_writer.yaml
```

## Loading the Environment

The environment is a USD stage. Use `get_assets_root_path` to get the path to the nucleus server and then load the environment with `open_stage`.

Load the Environment

```python
# Get assets root path from nucleus server
assets_root_path = get_assets_root_path()
if assets_root_path is None:
    carb.log_error("Could not get nucleus server path, closing application..")
    simulation_app.close()

# Load environment stage
print(f"[SDG] Loading Stage {config['env_url']}")
stage_opened, _ = open_stage(assets_root_path + config["env_url"])
if not stage_opened:
    carb.log_error(f"Could not open stage{config['env_url']}, closing application..")
    simulation_app.close()

# Initialize randomization
rep.set_global_seed(42)
rng = np.random.default_rng(42)

# Configure replicator for manual triggering
rep.orchestrator.set_capture_on_play(False)

# Set DLSS to Quality mode for best SDG results
carb.settings.get_settings().set("rtx/post/dlss/execMode", 2)

# Clear previous semantic labels
if config["clear_previous_semantics"]:
    for prim in get_current_stage().Traverse():
        remove_all_labels(prim, include_descendants=True)
```

## Creating the Cameras and the Writer

The example creates cameras with `rep.functional.create.camera` and creates referenced assets with the Isaac Sim API. The asset prims are defined with `define_prim`, populated with `add_reference_to_stage`, labeled with `add_labels`, and transformed with `XformPrim`. The created render products are attached to the built-in `BasicWriter` to collect the data from the selected annotators (rgb, semantic\_segmentation, bounding\_box\_3d) and to write it to the given output path.

The examples use `rep.functional.create.camera` to create camera prims for render products.

Cameras

```python
# Create cameras
rep.functional.create.scope(name="Cameras", parent="/SDG")
driver_cam = rep.functional.create.camera(
    focus_distance=400.0, focal_length=24.0, clipping_range=(0.1, 10000000.0), name="DriverCam", parent="/SDG/Cameras"
)
pallet_cam = rep.functional.create.camera(name="PalletCam", parent="/SDG/Cameras")
top_view_cam = rep.functional.create.camera(clipping_range=(6.0, 1000000.0), name="TopCam", parent="/SDG/Cameras")
```

From the cameras, render products are created and disabled until the SDG pipeline starts to improve performance by avoiding unnecessary rendering. The writer setup is handled by a helper function that supports optional backend configuration for flexible output handling.

Writer and Render Products

```python
# Setup render products
resolution = config.get("resolution", (512, 512))
forklift_rp = rep.create.render_product(top_view_cam, resolution, name="TopView")
driver_rp = rep.create.render_product(driver_cam, resolution, name="DriverView")
pallet_rp = rep.create.render_product(pallet_cam, resolution, name="PalletView")

render_products = [forklift_rp, driver_rp, pallet_rp]
for render_product in render_products:
    render_product.hydra_texture.set_updates_enabled(False)

# Initialize writer and attach to render products
writer = scene_based_sdg_utils.setup_writer(config)
if not writer:
    carb.log_error("[SDG] Failed to setup writer, closing application.")
    simulation_app.close()

writer.attach(render_products)

for render_product in render_products:
    render_product.hydra_texture.set_updates_enabled(True)
```

The `setup_writer` helper function handles writer initialization with optional backend support:

```python
def setup_writer(config: dict) -> rep.Writer | None:
    """Setup and initialize writer with optional backend support and error handling."""

    def normalize_output_dir(params):
        """Convert relative output_dir to absolute path."""
        if "output_dir" in params and not os.path.isabs(params["output_dir"]):
            params["output_dir"] = os.path.join(os.getcwd(), params["output_dir"])

    # Get writer from registry
    writer_type = config.get("writer", "BasicWriter")
    if writer_type not in rep.WriterRegistry.get_writers():
        carb.log_error(f"[SDG] Writer type '{writer_type}' not found in registry.")
        return None

    writer = rep.WriterRegistry.get(writer_type)
    writer_kwargs = dict(config.get("writer_config", {}))
    normalize_output_dir(writer_kwargs)

    # Initialize backend if specified
    backend_type = config.get("backend_type")
    backend = None
    if backend_type:
        try:
            backend = rep.backends.get(backend_type)
        except Exception as e:
            carb.log_error(f"[SDG] Backend '{backend_type}' not found: {e}")
            return None

        backend_params = dict(config.get("backend_params", {}))
        normalize_output_dir(backend_params)

        try:
            print(f"[SDG] Backend: {backend_type} | Params: {backend_params}")
            backend.initialize(**backend_params)
        except TypeError as e:
            carb.log_error(f"[SDG] Invalid backend params: {e}")
            return None

    # Initialize writer
    if "output_dir" in writer_kwargs:
        print(f"[SDG] Output: {writer_kwargs['output_dir']}")

    backend_info = f" + {backend_type}" if backend else ""
    print(f"[SDG] Writer: {writer_type}{backend_info} | Config: {writer_kwargs}")

    try:
        if backend:
            writer.initialize(backend=backend, **writer_kwargs)
        else:
            writer.initialize(**writer_kwargs)
    except TypeError as e:
        carb.log_error(f"[SDG] Invalid writer params: {e}")
        return None

    return writer
```

## Domain Randomization

The following snippet provides examples of various randomization possibilities using Isaac Sim and Replicator API. The example uses a seeded random number generator (`numpy.random.Generator`) for reproducible randomization. It starts by spawning a forklift using the Isaac Sim API to a randomly generated pose. It then uses the forklift pose to place a pallet in front of it within the bounds of a random distance. Cardboxes and a traffic cone are also created upfront for later randomization.

Isaac Sim API Asset Spawning

```python
# Spawn forklift at random pose
forklift_path = "/SDG/Forklift"
forklift_prim = define_prim(forklift_path)
add_reference_to_stage(assets_root_path + config["forklift"]["url"], forklift_path)
add_labels(forklift_prim, labels=[config["forklift"]["class"]], taxonomy="class")
XformPrim(
    forklift_path,
    positions=(rng.uniform(-20, -2), rng.uniform(-1, 3), 0),
    orientations=euler_angles_to_quaternion([0, 0, rng.uniform(0, math.pi)]).numpy(),
    reset_xform_op_properties=True,
)

# Spawn pallet in front of forklift with random offset
forklift_tf = omni.usd.get_world_transform_matrix(forklift_prim)
pallet_offset_tf = Gf.Matrix4d().SetTranslate(Gf.Vec3d(0, rng.uniform(-1.8, -1.2), 0))
pallet_pos = (pallet_offset_tf * forklift_tf).ExtractTranslation()
forklift_quat = forklift_tf.ExtractRotationQuat()
forklift_quat_xyzw = (forklift_quat.GetReal(), *forklift_quat.GetImaginary())

pallet_path = "/SDG/Pallet"
pallet_prim = define_prim(pallet_path)
add_reference_to_stage(assets_root_path + config["pallet"]["url"], pallet_path)
add_labels(pallet_prim, labels=[config["pallet"]["class"]], taxonomy="class")
XformPrim(
    pallet_path,
    positions=tuple(pallet_pos),
    orientations=forklift_quat_xyzw,
    reset_xform_op_properties=True,
)

# Create cardboxes for pallet scattering
cardboxes = []
for i in range(5):
    cardbox_path = f"/SDG/CardBox_{i}"
    cardbox = define_prim(cardbox_path)
    add_reference_to_stage(assets_root_path + config["cardbox"]["url"], cardbox_path)
    add_labels(cardbox, labels=[config["cardbox"]["class"]], taxonomy="class")
    cardboxes.append(cardbox)

# Create traffic cone for corner placement
cone_path = "/SDG/Cone"
cone = define_prim(cone_path)
add_reference_to_stage(assets_root_path + config["cone"]["url"], cone_path)
add_labels(cone, labels=[config["cone"]["class"]], taxonomy="class")
```

The Replicator API uses `rep.functional` for direct randomization without graph registration. A scatter plane is created using a helper function, and boxes are scattered directly using `rep.functional.randomizer.scatter_2d` in the SDG loop. Material randomization is handled through a separate graph-based randomizer.

Scatter Plane Setup

```python
def create_scatter_plane_for_prim(
    prim: Usd.Prim, prim_tf: Gf.Matrix4d, parent_path: str, scale_factor: float = 0.8, visible: bool = False
) -> Usd.Prim:
    """Create scatter plane sized and aligned to prim surface."""
    bb_cache = create_bbox_cache()
    prim_bbox = bb_cache.ComputeLocalBound(prim)
    prim_bbox.Transform(prim_tf)
    prim_size = prim_bbox.GetRange().GetSize()

    prim_quat = prim_tf.ExtractRotation().GetQuaternion()
    prim_quat_xyzw = (prim_quat.GetReal(), *prim_quat.GetImaginary())
    prim_rotation_deg = quaternion_to_euler_angles(np.array(prim_quat_xyzw), degrees=True).numpy()

    prim_pos = prim_tf.ExtractTranslation()
    scatter_plane_scale = (prim_size[0] * scale_factor, prim_size[1] * scale_factor, 1)
    scatter_plane_pos = prim_pos + Gf.Vec3d(0, 0, prim_size[2])

    scatter_plane = rep.functional.create.plane(
        scale=scatter_plane_scale,
        position=tuple(scatter_plane_pos),
        rotation=tuple(prim_rotation_deg),
        visible=visible,
        parent=parent_path,
    )

    return scatter_plane
```

Material randomization for cardboxes is registered as a graph-based randomizer triggered by custom events:

Material Randomization Graph

```python
def register_cardboxes_materials_graph_randomizer(
    cardboxes: list[Usd.Prim], cardbox_material_urls: list[str], event_name: str
) -> None:
    """Register graph randomizer to apply random materials to cardbox meshes."""
    cardbox_mesh_paths = []
    for cardbox in cardboxes:
        meshes = [child for child in cardbox.GetChildren() if child.IsA(UsdGeom.Mesh)]
        cardbox_mesh_paths.extend([mesh.GetPrimPath() for mesh in meshes])

    with rep.trigger.on_custom_event(event_name):
        cardbox_mesh_group_node = rep.create.group(cardbox_mesh_paths)
        with cardbox_mesh_group_node:
            rep.randomizer.materials(cardbox_material_urls)
```

The traffic cone is positioned at one of the forkliftâs bounding box corners. A helper function calculates the corner positions:

Cone Placement Setup

```python
def setup_cone_placement_corners(
    forklift_prim: Usd.Prim, bb_cache=None, scale_factor: float = 1.3
) -> tuple[list[list[float]], tuple[float, float, float]]:
    """Calculate forklift OBB corners for cone placement."""
    if bb_cache is None:
        bb_cache = create_bbox_cache()

    forklift_obb_center, forklift_obb_axes, forklift_obb_extent = compute_obb(forklift_prim, bbox_cache=bb_cache)
    enlarged_extent = (
        forklift_obb_extent[0] * scale_factor,
        forklift_obb_extent[1] * scale_factor,
        forklift_obb_extent[2],
    )
    forklift_obb_corners = get_obb_corners(forklift_obb_center, forklift_obb_axes, enlarged_extent)

    cone_placement_corners = [
        forklift_obb_corners[0].tolist(),
        forklift_obb_corners[2].tolist(),
        forklift_obb_corners[4].tolist(),
        forklift_obb_corners[6].tolist(),
    ]

    forklift_obb_quat = Gf.Matrix3d(forklift_obb_axes).ExtractRotation().GetQuaternion()
    forklift_obb_quat_xyzw = (forklift_obb_quat.GetReal(), *forklift_obb_quat.GetImaginary())
    forklift_rotation_deg = quaternion_to_euler_angles(np.array(forklift_obb_quat_xyzw), degrees=True).numpy()

    return cone_placement_corners, forklift_rotation_deg
```

Light randomization is registered as a graph-based randomizer triggered by custom events:

Light Randomization Graph

```python
def register_lights_graph_randomizer(forklift_prim: Usd.Prim, pallet_prim: Usd.Prim, event_name: str) -> None:
    """Register graph randomizer for sphere lights."""
    bb_cache = create_bbox_cache()
    combined_bounds = compute_combined_aabb([forklift_prim, pallet_prim], bbox_cache=bb_cache)
    light_pos_min = (combined_bounds[0], combined_bounds[1], 6)
    light_pos_max = (combined_bounds[3], combined_bounds[4], 7)

    with rep.trigger.on_custom_event(event_name):
        rep.create.light(
            light_type="Sphere",
            color=rep.distribution.uniform((0.2, 0.1, 0.1), (0.9, 0.8, 0.8)),
            intensity=rep.distribution.uniform(2000, 4000),
            position=rep.distribution.uniform(light_pos_min, light_pos_max),
            scale=rep.distribution.uniform(1, 4),
            count=3,
        )
```

Similar to the above examples, Replicator has support for many other randomizations. For more information, see Replicatorâs [randomizer examples tutorials](https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator/randomizer_details.html "(in Omniverse Extensions)").

Camera bounds are calculated using a helper function to determine the randomization ranges:

Camera Bounds Setup

```python
def setup_camera_bounds(
    pallet_prim: Usd.Prim, forklift_prim: Usd.Prim, pallet_tf: Gf.Matrix4d, forklift_tf: Gf.Matrix4d
) -> dict[str, dict[str, tuple[float, float, float]]]:
    """Calculate camera randomization bounds for pallet, top view, and driver cameras."""
    pallet_pos = pallet_tf.ExtractTranslation()
    pallet_cam_bounds = {
        "min": (pallet_pos[0] - 2, pallet_pos[1] - 2, 2),
        "max": (pallet_pos[0] + 2, pallet_pos[1] + 2, 4),
    }

    forklift_pos = forklift_tf.ExtractTranslation()
    top_cam_bounds = {
        "min": (forklift_pos[0], forklift_pos[1], 9),
        "max": (forklift_pos[0], forklift_pos[1], 11),
    }

    driver_cam_pos = forklift_pos + Gf.Vec3d(0.0, 0.0, 1.9)
    driver_cam_bounds = {
        "min": (driver_cam_pos[0], driver_cam_pos[1], driver_cam_pos[2] - 0.25),
        "max": (driver_cam_pos[0], driver_cam_pos[1], driver_cam_pos[2] + 0.25),
    }

    return {
        "pallet_cam": pallet_cam_bounds,
        "top_cam": top_cam_bounds,
        "driver_cam": driver_cam_bounds,
    }
```

After setting up the randomizers and before running the data collection, a short physics simulation is run. The example drops several stacked boxes on a pallet behind the forklift using `SimulationManager` and the experimental `GeomPrim` and `RigidPrim` classes. The simulation uses `boundingCube` collision approximations to avoid high-detail mesh cooking for these generated objects.

Isaac Sim Simulation

```python
def simulate_falling_objects(
    forklift_prim: Usd.Prim,
    assets_root_path: str,
    config: dict,
    max_sim_steps: int = 250,
    num_boxes: int = 8,
    rng: np.random.Generator | None = None,
) -> None:
    """Run physics simulation to drop boxes on pallet near forklift."""
    if rng is None:
        rng = np.random.default_rng()

    forklift_transform = omni.usd.get_world_transform_matrix(forklift_prim)
    sim_pallet_offset = Gf.Matrix4d().SetTranslate(Gf.Vec3d(rng.uniform(-1, 1), rng.uniform(-4, -3.6), 0))
    sim_pallet_position = (sim_pallet_offset * forklift_transform).ExtractTranslation()
    sim_pallet_rotation = euler_angles_to_quaternion([0, 0, rng.uniform(0, math.pi)]).numpy()

    sim_pallet_path = "/World/SimulatedPallet"
    sim_pallet = define_prim(sim_pallet_path)
    add_reference_to_stage(assets_root_path + config["pallet"]["url"], sim_pallet_path)
    add_labels(sim_pallet, labels=[config["pallet"]["class"]], taxonomy="class")
    XformPrim(
        sim_pallet_path,
        positions=tuple(sim_pallet_position),
        orientations=sim_pallet_rotation,
        reset_xform_op_properties=True,
    )
    sim_pallet_geom = GeomPrim(f"{str(sim_pallet.GetPrimPath())}/.*", apply_collision_apis=True)
    sim_pallet_geom.set_collision_approximations("boundingCube")

    bbox_cache = create_bbox_cache()
    current_height = bbox_cache.ComputeLocalBound(sim_pallet).GetRange().GetSize()[2] * 1.1

    sim_box_rigid_prims = []
    for box_index in range(num_boxes):
        box_xy_offset = Gf.Vec3d(rng.uniform(-0.2, 0.2), rng.uniform(-0.2, 0.2), current_height)
        sim_box_path = f"/World/SimulatedCardbox_{box_index}"
        sim_box = define_prim(sim_box_path)
        add_reference_to_stage(assets_root_path + config["cardbox"]["url"], sim_box_path)
        add_labels(sim_box, labels=[config["cardbox"]["class"]], taxonomy="class")
        XformPrim(
            sim_box_path,
            positions=tuple(sim_pallet_position + box_xy_offset),
            orientations=sim_pallet_rotation,
            reset_xform_op_properties=True,
        )
        current_height += bbox_cache.ComputeLocalBound(sim_box).GetRange().GetSize()[2] * 1.1

        sim_box_geom = GeomPrim(f"{str(sim_box.GetPrimPath())}/.*", apply_collision_apis=True)
        sim_box_geom.set_collision_approximations("boundingCube")
        sim_box_rigid_prims.append(RigidPrim(str(sim_box.GetPrimPath())))

    # Run physics simulation
    SimulationManager.set_physics_dt(1.0 / 90.0)
    SimulationManager.initialize_physics()

    # Simulate until boxes settle or max steps reached
    velocity_threshold = 0.01
    for step in range(max_sim_steps):
        SimulationManager.step()
        if sim_box_rigid_prims:
            top_box_velocity = sim_box_rigid_prims[-1].get_velocities(indices=[0])[0].numpy()
            if np.linalg.norm(top_box_velocity) < velocity_threshold:
                print(f"[SDG] Simulation settled at step {step}")
                break
```

## Running the Script

The SDG loop runs randomizations directly using `rep.functional` APIs, triggers graph-based randomizers via custom events, and captures frames. The loop uses the seeded random number generator for reproducible results.

SDG Loop Execution

```python
# SDG loop - generate frames with randomizations
num_frames = config.get("num_frames", 0)
print(f"[SDG] Running SDG for {num_frames} frames")
for i in range(num_frames):
    print(f"[SDG] Frame {i}/{num_frames}")

    print(f"[SDG]  Randomizing boxes on pallet.")
    rep.functional.randomizer.scatter_2d(
        prims=cardboxes, surface_prims=scatter_plane, check_for_collisions=True, rng=rng
    )

    print(f"[SDG]  Randomizing boxes materials.")
    rep.utils.send_og_event(event_name="randomize_cardboxes_materials")
    print(f"[SDG]  Randomizing lights.")
    rep.utils.send_og_event(event_name="randomize_lights")

    print(f"[SDG]  Randomizing pallet camera.")
    rep.functional.modify.pose(
        pallet_cam,
        position_value=rng.uniform(pallet_cam_bounds_min, pallet_cam_bounds_max),
        look_at_value=pallet_prim,
        look_at_up_axis=(0, 0, 1),
    )

    print(f"[SDG]  Randomizing driver camera.")
    rep.functional.modify.pose(
        driver_cam,
        position_value=rng.uniform(driver_cam_bounds_min, driver_cam_bounds_max),
        look_at_value=pallet_prim,
        look_at_up_axis=(0, 0, 1),
    )

    if i % 2 == 0:
        print(f"[SDG]  Randomizing cone position.")
        selected_corner = cone_placement_corners[rng.integers(0, len(cone_placement_corners))]
        rep.functional.modify.pose(
            cone,
            position_value=selected_corner,
        )

    if i % 4 == 0:
        print(f"[SDG]  Randomizing top view camera.")
        roll_angle = rng.uniform(0, 2 * np.pi)
        rep.functional.modify.pose(
            top_view_cam,
            position_value=rng.uniform(top_cam_bounds_min, top_cam_bounds_max),
            look_at_value=forklift_prim,
            look_at_up_axis=(np.cos(roll_angle), np.sin(roll_angle), 0.0),
        )

    print(f"[SDG]  Capturing frame with rt_subframes={rt_subframes}")
    rep.orchestrator.step(delta_time=0.0, rt_subframes=rt_subframes)
```

After the SDG loop completes, proper cleanup ensures all data is written and resources are released:

Cleanup

```python
# Cleanup
rep.orchestrator.wait_until_complete()
writer.detach()
for render_product in render_products:
    render_product.destroy()

# Check if the application should keep running after data generation
close_app_after_run = config.get("close_app_after_run", True)
if config["launch_config"]["headless"]:
    if not close_app_after_run:
        print("[SDG] 'close_app_after_run' is ignored when running headless. The application will be closed.")
elif not close_app_after_run:
    print("[SDG] The application will not be closed after the run. Make sure to close it manually.")
    while simulation_app.is_running():
        simulation_app.update()
simulation_app.close()
```

## Summary

This tutorial covered the following topics:

1. Starting a `SimulationApp` instance of Isaac Sim to work with Replicator
2. Loading a stage and custom assets at random locations using Isaac Sim API with seeded randomization
3. Setting up cameras using `rep.functional.create.camera` with organized stage structure
4. Configuring writers with optional backend support for flexible output handling
5. Using `rep.functional` APIs for direct randomization (scatter, pose modification)
6. Creating graph-based randomizers for lights and materials triggered by custom events
7. Running physics simulations with `SimulationManager` and experimental `GeomPrim`/`RigidPrim` classes
8. Proper cleanup of writers and render products

## Next Steps

One possible use for the created data is with the TAO Toolkit. After the generated synthetic data is in Kitti format, you can use the TAO Toolkit to
train a model. TAO provides [segmentation, classification and object detection models](https://docs.nvidia.com/tao/tao-toolkit/text/overview.html#pre-trained-models).
This example uses object detection with the [Detectnet V2 model](https://docs.nvidia.com/tao/tao-toolkit-archive/5.2.0/text/object_detection/detectnet_v2.html)
as a use case.

To get started with TAO, follow the [set-up instruction video](https://docs.nvidia.com/tao/tao-toolkit/text/quick_start_guide/index.html).

TAO uses Jupyter notebooks to guide you through the training process.
In the folder cv\_samples\_v1.3.0, you can find notebooks for multiple models.
You can use any of the object detection networks for this use case, but this example uses Detectnet\_V2.

In the detectnet\_v2 folder, you can find the Jupyter notebook and the specs folder.
The [TAO Detectnet V2 documentation](https://docs.nvidia.com/tao/tao-toolkit-archive/5.2.0/text/object_detection/detectnet_v2.html)
goes into more detail about this sample. TAO works with configuration files that can be found in the
specs folder. Here, you must modify the specs to refer to the generated synthetic data as the
input.

To prepare the data, you must run the following command.

```python
tao detectnet_v2 dataset-convert [-h] -d DATASET_EXPORT_SPEC -o OUTPUT_FILENAME [-f VALIDATION_FOLD]
```

This is in the Jupyter notebook with a sample configuration. Modify the spec file to match the folder
structure of your synthetic data. The data is in TFrecord format and is ready for training.
Again, you need to change the spec file for training to represent the path to the synthetic data and
the classes being detected.

```python
tao detectnet_v2 train [-h] -k <key>
                        -r <result directory>
                        -e <spec_file>
                        [-n <name_string_for_the_model>]
                        [--gpus <num GPUs>]
                        [--gpu_index <comma separate gpu indices>]
                        [--use_amp]
                        [--log_file <log_file>]
```

For any questions regarding the TAO Toolkit, refer to the [TAO documentation](https://docs.nvidia.com/tao/tao-toolkit/text/overview.html).

## Further Learning

To learn how to use NVIDIA Isaac Sim to create data sets in an interactive manner, see the
[Synthetic Data Recorder](tutorial_replicator_recorder.html#isaac-sim-app-tutorial-replicator-recorder) and then visualize them with the [Synthetic Data Visualizer](tutorial_replicator_overview.html#the-synthetic-data-visualizer).

On this page

* [Prerequisites](#prerequisites)
* [Scenario](#scenario)
* [Getting Started](#getting-started)
* [Implementation](#implementation)
* [Config Scenarios](#config-scenarios)
* [Loading the Environment](#loading-the-environment)
* [Creating the Cameras and the Writer](#creating-the-cameras-and-the-writer)
* [Domain Randomization](#domain-randomization)
* [Running the Script](#running-the-script)
* [Summary](#summary)
* [Next Steps](#next-steps)
* [Further Learning](#further-learning)

---

### Grasping SDG

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/synthetic_data_generation/tutorial_replicator_grasping_sdg.html

* [Synthetic Data Generation](index.html)
* Grasping Synthetic Data Generation

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Grasping Synthetic Data Generation

This tutorial introduces the `isaacsim.replicator.grasping` extension and its associated UI, `isaacsim.replicator.grasping.ui`. These tools provide a comprehensive workflow for generating synthetic grasping datasets in Isaac Sim.

## Learning Objectives

After completing this tutorial, you will be able to:

* Understand the core components and data flow of the Grasping SDG extension.
* Navigate and utilize the Grasping SDG UI to configure and run grasp generation workflows.
* Define gripper properties, joint states, and multi-step grasp phases.
* Configure object properties and grasp pose sampling parameters.
* Execute and interpret the results of physics-based grasp evaluations.
* Manage grasping configurations using YAML files for saving, loading, and sharing setups.

The extensions are automatically loaded in Isaac Sim, and the UI window can be opened from the main menu using **Tools** > **Replicator** > **Grasping**.

## Getting Started

Before proceeding, it is recommended that you familiarize yourself with:

* [Simulation Fundamentals](../physics/simulation_fundamentals.html#simulation-fundamentals): For understanding physics simulation concepts and gripper rigging (for example, drive joints).
* [Grasp Editor](../robot_simulation/grasp_editor.html#isaac-sim-app-tutorial-grasp-editor-import): This tutorial covers related concepts and provides a foundation for grasp definition.

Note

The grasp sampler requires the `libspatialindex` library. If you see related warnings, install it (for example, on Ubuntu: `sudo apt-get install libspatialindex-dev`).

This tutorial utilizes an example stage that includes a pre-configured gripper and objects suitable for grasping exercises. You can find this stage at:

```python
https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Isaac/6.0
/Isaac/Samples/Replicator/Stage/sdg_grasping_xarm.usd
```

The stage asset can be found in the **Content Browser** under **Isaac Sim** > **Samples** > **Replicator** > **Stage** > **sdg\_grasping\_xarm.usd**, or can be loaded using by inserting the whole URL in the path field.

The example stage features a gripper with drive joints and three objects equipped with rigid body physics and colliders. Gravity is disabled for these objects to simplify initial interactions. The Grasping UI window typically docks in the **Property** panel upon opening.

## Overview

The extension is designed to automate the process of finding and evaluating potential grasp poses for a given gripper-object pair. At its core, the workflow revolves around several key components and stages:

1. **Configuration**: Defining the specific gripper, the target object, and the parameters that govern how grasps are found and tested.
2. **Grasp Pose Sampling**: Algorithms (for example, antipodal samplers) generate a set of candidate grasp poses around the target object. These poses represent potential ways the gripper might hold the object.
3. **Grasp Execution Phases**: For each candidate grasp, a sequence of actions, termed âGrasp Phasesâ (for example, move to pre-grasp, close fingers, lift), is simulated. This allows for defining complex, multi-step grasping behaviors analogous to real-world robot actions.
4. **Physics-Based Evaluation**: Each phase of the grasp is simulated in the physics engine. The success or failure of the grasp attempt, along with other metrics (like contact forces, object displacement), can be recorded. In its current state the extension saves the gripper state as result from which the grasps can be evaluated.
5. **Data Logging and Management**: Successful grasps and their associated parameters are logged. The entire setup can be saved to and loaded from configuration files (YAML format), ensuring reproducibility and facilitating batch processing.

The `GraspingManager` class is the central Python API orchestrating these steps, while the UI provides an intuitive way to configure and run this pipeline.

## UI Window Overview

The Grasping UI window provides the interface for setting up and running the grasping simulations workflows. It is organized into several sections, each addressing a specific part of the process. The general workflow involves configuring these sections, typically starting with the gripper and object, then defining the evaluation workflow and simulation parameters, and finally managing the overall configuration.

### Gripper Section

This section is dedicated to defining the properties and behavior of the gripper, which is fundamental for any grasp attempt.

* **Path**: Specify the USD path to the root prim of your gripper (for example, `/World/Robot/gripper_base`).
* **Joints**: After a gripper is selected, its articulated joints are listed. Here you can:

  + **Include/Exclude**: Select the joints that are actively controlled during the grasp phases. These joints have to be drive joints.
  + Set **pre-grasp positions**: Define the initial state for each joint, typically an open configuration, before the grasp sequence begins.
  + Toggle visibility between all joints or of type drive (non-mimic) joints.
* **Grasp Phases**: This powerful feature allows you to define a sequence of discrete actions that constitute a complete grasp attempt. This is analogous to defining a state machine or a sequence of motion primitives for the gripper.

  For each phase (for example, âOpenâ, âCloseâ), you specify:

  + Target joint positions for the active gripper joints.
  + Simulation step delta time (`dt`) for the physics steps within this phase.
  + Number of simulation steps to execute for this phase.

  Phases can be reordered, deleted, or simulated individually for debugging. If pre-grasp joint positions adequately prepare the gripper (for example, fully open), an explicit âOpenâ phase might be unnecessary.

### Object Section

This section focuses on specifying the target object and configuring how potential grasp poses are generated for it.

* **Path**: The USD path to the target object prim (for example, `/World/MyObject`).
* **Grasp Pose Sampler**: This configures the algorithm used to find potential grasp poses. This tutorial primarily uses an **antipodal grasp sampler** (implemented in `sampler_utils.py`). An antipodal grasp is typically stable for parallel-jaw grippers, involving two contact points on opposite sides of the object. Key parameters include:

  + **Number of orientations per grasp axis**: How many rotational variations around the primary grasp axis to sample.
  + **Gripper standoff distance**: The distance from the gripperâs Tool Center Point (TCP) or fingertips to the object surface during the approach phase, crucial for avoiding premature collision.
  + **Maximum gripper aperture**: The widest opening of the gripper jaws, filtering out grasps that are too wide for the object.
  + **Alignment axes for the grasp**: Defines local gripper axes to align with object features or the grasp line.
  + **Gripper approach direction**: The vector along which the gripper moves towards the object.
  + **Lateral perturbation (sigma)**: Adds randomness to the grasp point location along the grasp axis, allowing for exploration around nominal contact points.
  + **Random seed**: For ensuring reproducible sampling results.
* **Grasp Poses**: Manages the set of candidate grasp poses generated by the sampler.

  + Specify the desired number of candidate poses.
  + Clear previously generated poses.
  + Visualize the poses in the viewport (either in world or object-local frames) and cycle through them to inspect their placement.

  The following image shows example grasp poses generated by the antipodal sampler on various objects:
* **Trimesh**: Provides options for debug visualization of the objectâs triangle mesh, which is used internally by the sampler for geometric calculations and collision checks.

Note

The [Measure Tool](https://docs.omniverse.nvidia.com/extensions/latest/ext_measure-tool.html) can be useful for determining values like gripper aperture or standoff distance.

### Workflow Section

The Workflow section is where you orchestrate the actual grasp evaluation process using the configurations defined in the Gripper and Object sections.

The system first saves the gripperâs initial pose. Then, for each generated grasp pose selected for evaluation, it sequentially executes the defined grasp phases within the physics simulation. After all phases for a given pose are completed, the outcome (for example, success based on object stability, contact with target) and other relevant metrics are recorded.

* **Number of Grasps Samples**: Specify how many of the generated grasp poses should be evaluated. Use -1 to evaluate all available poses.
* **Output Path**: Define the directory and base file name for saving the evaluation results. The results are typically saved in a structured format like YAML, detailing each evaluated grasp and its outcome.
* **Overwrite Results**: If enabled, existing result files at the output path will be overwritten. Otherwise, new files will be created (for example, with incremental numbering) to avoid data loss.
* **Start Workflow**: Initiates the grasp evaluation process. The UI will often provide feedback on the progress.

### Simulation Section

This section allows you to fine-tune global parameters that affect how the physics simulation is run during the grasp evaluation.

* **Render each simulation step**: Control whether the viewport updates after each individual physics step within a grasp phase. Disabling this can speed up the evaluation process significantly for large datasets, with rendering potentially only occurring after each full grasp attempt or phase.
* **Simulate using timeline**: Choose between advancing the simulation by stepping the main Isaac Sim timeline or by directly stepping the physics scene. Direct physics steps can offer more precise control for rapid evaluations, while timeline-based simulation might be closer to how a full robot application would run.
* **Isolated physics scene**: Optionally specify a path to a **Physics Scene** prim. If provided, the grasping simulation can be run within this dedicated physics scene, preventing interference from other dynamic objects or physics settings in the main stage. This is useful for ensuring consistent and repeatable grasp evaluations.

### Config Section

The Config section provides the crucial functionality for saving your entire grasping setup to a YAML file and loading it back later. This is essential for reproducibility, sharing configurations, and running batch experiments.

* **File Path**: Specify the path to the YAML configuration file for saving or loading.
* **Config Includes**: Selectively choose which components of the setup are included in the save/load operation. This allows for modular configurations. Options typically include:

  + Gripper Path
  + Joint Pregrasp States
  + Grasp Phases
  + Object Path
  + Sampler Parameters
  + Generated Grasp Poses (if you wish to save a specific set of poses)
* **Overwrite Existing File**: When saving, this option determines if an existing file at the specified path should be overwritten.
* **Load/Save Buttons**: Execute the respective file operations.

This structured UI and configuration system offers detailed control and flexibility for generating diverse grasping datasets.

### Configuration File Example

Below is a snippet illustrating the structure of a YAML configuration file. It can store settings for the gripper, object, sampler, and defined grasp phases. The specific content will depend on which components were selected for inclusion through the âConfig Includesâ UI options.

xarm\_antipodal.yaml

```python
grasp_phases:
- joint_drive_targets:
    /World/Grippers/xarm_gripper/joints/drive_joint: 48.0
  name: Close
  simulation_step_dt: 0.016666666666666666
  simulation_steps: 32
gripper_path: /World/Grippers/xarm_gripper
joint_pregrasp_states:
  /World/Grippers/xarm_gripper/joints/drive_joint: 0.0
  /World/Grippers/xarm_gripper/joints/left_finger_joint: 0.0
  /World/Grippers/xarm_gripper/joints/left_inner_knuckle_joint: 0.0
  /World/Grippers/xarm_gripper/joints/right_finger_joint: 0.0
  /World/Grippers/xarm_gripper/joints/right_inner_knuckle_joint: 0.0
  /World/Grippers/xarm_gripper/joints/right_outer_knuckle_joint: 0.0
  /World/Grippers/xarm_gripper/root_joint: 0.0
sampler_config:
  grasp_align_axis:
  - 0
  - 1
  - 0
  gripper_approach_direction:
  - 0
  - 0
  - 1
  gripper_maximum_aperture: 0.08
  gripper_standoff_fingertips: 0.17000000178813934
  lateral_sigma: 0.0
  num_candidates: 100
  num_orientations: 1
  orientation_sample_axis:
  - 0
  - 1
  - 0
  random_seed: -1
  sampler_type: antipodal
  verbose: false
```

## Code Example

The following scripts demonstrates a complete workflow for generating a grasping dataset using the `GraspingManager` API. This script programmatically performs the steps configurable through the UI:

* opening a stage
* setting up the `GraspingManager` (potentially by loading a configuration file)
* generating grasp Poses
* evaluating these poses using physics simulation
* saving the results

This approach is highly suitable for batch processing or integration into larger robotics workflows. The script can be run directly from the [Script Editor](../development_tools/omniverse_script_editor.html#script-editor) or as a [Standalone Application](../introduction/workflows.html#standalone-application).

To run the standalone example from the terminal (on Windows, use `python.bat` instead of `python.sh`):

```python
./python.sh standalone_examples/api/isaacsim.replicator.grasping/grasping_workflow_sdg.py
```

Script Editor

Grasping Synthetic Data Generation Workflow

```python
import asyncio
import os

import omni.kit.app
import omni.usd
from isaacsim.core.utils.extensions import get_extension_path_from_name
from isaacsim.replicator.grasping.grasping_manager import GraspingManager
from isaacsim.storage.native import get_assets_root_path_async

async def run_example_async(
    stage_path,
    config_path=None,
    sampler_config=None,
    physics_scene_path=None,
    output_dir=None,
    gripper_path=None,
    object_prim_path=None,
):
    assets_root_path = await get_assets_root_path_async()
    print(f"Assets root path: {assets_root_path}")
    stage_url = assets_root_path + stage_path
    print(f"Opening stage: {stage_url}")
    await omni.usd.get_context().open_stage_async(stage_url)
    stage = omni.usd.get_context().get_stage()

    grasping_manager = GraspingManager()

    if config_path is not None:
        load_status = grasping_manager.load_config(config_path)
        print(f"Config load status: {load_status}")

    # Make sure the object to grasp is set (either from the config file or from the argument)
    if not grasping_manager.get_object_prim_path() and object_prim_path:
        grasping_manager.object_path = object_prim_path

    if not grasping_manager.get_object_prim_path():
        print("Warning: Object to grasp is not set (missing in config and argument). Aborting.")
        return

    # Make sure the gripper is set (either from the config file or from the argument)
    if not grasping_manager.gripper_path and gripper_path:
        grasping_manager.gripper_path = gripper_path

    if not grasping_manager.gripper_path:
        print("Warning: Gripper path is not set (missing in config and argument). Aborting.")
        return

    # If there are already grasp poses in the configuration, don't generate new ones
    if grasping_manager.grasp_locations:
        print(
            f"Found {len(grasping_manager.grasp_locations)} grasp poses in the configuration file. No new poses will be generated."
        )
    else:
        print("No grasp poses found in configuration, generating new ones...")

        # Determine Sampler Configuration
        if not (grasping_manager.sampler_config and grasping_manager.sampler_config.get("sampler_type")):
            if sampler_config:
                grasping_manager.sampler_config = sampler_config.copy()
            else:
                print(
                    "Warning: Sampler configuration is missing or invalid (not in config file and not provided as argument). Aborting pose generation."
                )
                return

        # Generate the grasp poses
        success_generation = grasping_manager.generate_grasp_poses()
        if not success_generation or not grasping_manager.grasp_locations:
            print("Failed to generate grasp poses or no poses were generated.")
            return
        print(f"Generated {len(grasping_manager.grasp_locations)} new grasp poses.")

    # Store the initial gripper pose to be able to restore it after the evaluation
    grasping_manager.store_initial_gripper_pose()

    print("Evaluating grasp poses...")
    poses_to_evaluate = grasping_manager.get_grasp_poses(in_world_frame=True)
    if not poses_to_evaluate:
        print("No poses available to evaluate..")
        return

    # Determine Output Path
    if not output_dir:
        print("Warning: Output path is not defined data will not be saved.")

    # Set the output path and overwrite flag
    grasping_manager.set_results_output_dir(output_dir)
    grasping_manager.set_overwrite_results_output(True)

    # Determine Physics Scene Path
    physics_scene_path_for_eval = None
    if physics_scene_path and stage.GetPrimAtPath(physics_scene_path):
        physics_scene_path_for_eval = physics_scene_path
    print(f"Physics scene path for evaluation: {physics_scene_path_for_eval}")

    await grasping_manager.evaluate_grasp_poses(
        grasp_poses=poses_to_evaluate,
        render=True,
        physics_scene_path=physics_scene_path_for_eval,
        simulate_using_timeline=False,
    )

    print("Grasping workflow example finished.")
    grasping_manager.clear()

stage_path = "/Isaac/Samples/Replicator/Stage/sdg_grasping_xarm.usd"
ext_path = get_extension_path_from_name("isaacsim.replicator.grasping")
config_path = os.path.join(ext_path, "data/gripper_configs/xarm_antipodal_soup_can.yaml")
output_dir = os.path.join(os.getcwd(), "xarm_antipodal")

asyncio.ensure_future(run_example_async(stage_path=stage_path, config_path=config_path, output_dir=output_dir))
```

Standalone Application

Grasping Synthetic Data Generation Workflow

```python
"""Demonstrate grasp pose generation and evaluation using the grasping manager."""

from isaacsim import SimulationApp

simulation_app = SimulationApp(launch_config={"headless": False})

import asyncio
import os

import omni.kit.app
import omni.usd
from isaacsim.core.experimental.utils.app import get_extension_path as get_extension_path_from_name
from isaacsim.storage.native import get_assets_root_path

# Make sure the grasping extension is loaded and enabled
ext_manager = omni.kit.app.get_app().get_extension_manager()
if not ext_manager.is_extension_enabled("isaacsim.replicator.grasping"):
    ext_manager.set_extension_enabled_immediate("isaacsim.replicator.grasping", True)
from isaacsim.replicator.grasping.grasping_manager import GraspingManager

def run_example(
    stage_path,
    config_path=None,
    sampler_config=None,
    physics_scene_path=None,
    output_dir=None,
    gripper_path=None,
    object_prim_path=None,
):
    """Run grasp pose generation and physics-based evaluation workflow."""
    assets_root_path = get_assets_root_path()
    print(f"Assets root path: {assets_root_path}")
    stage_url = assets_root_path + stage_path
    print(f"Opening stage: {stage_url}")
    omni.usd.get_context().open_stage(stage_url)
    stage = omni.usd.get_context().get_stage()

    grasping_manager = GraspingManager()

    if config_path is not None:
        load_status = grasping_manager.load_config(config_path)
        print(f"Config load status: {load_status}")

    # Make sure the object to grasp is set (either from the config file or from the argument)
    if not grasping_manager.get_object_prim_path() and object_prim_path:
        grasping_manager.object_path = object_prim_path

    if not grasping_manager.get_object_prim_path():
        print("Warning: Object to grasp is not set (missing in config and argument). Aborting.")
        return

    # Make sure the gripper is set (either from the config file or from the argument)
    if not grasping_manager.gripper_path and gripper_path:
        grasping_manager.gripper_path = gripper_path

    if not grasping_manager.gripper_path:
        print("Warning: Gripper path is not set (missing in config and argument). Aborting.")
        return

    # If there are already grasp poses in the configuration, don't generate new ones
    if grasping_manager.grasp_locations:
        print(
            f"Found {len(grasping_manager.grasp_locations)} grasp poses in the configuration file. No new poses will be generated."
        )
    else:
        print("No grasp poses found in configuration, generating new ones...")

        # Determine Sampler Configuration
        if not (grasping_manager.sampler_config and grasping_manager.sampler_config.get("sampler_type")):
            if sampler_config:
                grasping_manager.sampler_config = sampler_config.copy()
            else:
                print(
                    "Warning: Sampler configuration is missing or invalid (not in config file and not provided as argument). Aborting pose generation."
                )
                return

        # Generate the grasp poses
        success_generation = grasping_manager.generate_grasp_poses()
        if not success_generation or not grasping_manager.grasp_locations:
            print("Failed to generate grasp poses or no poses were generated.")
            return
        print(f"Generated {len(grasping_manager.grasp_locations)} new grasp poses.")

    # Store the initial gripper pose to be able to restore it after the evaluation
    grasping_manager.store_initial_gripper_pose()

    print("Evaluating grasp poses...")
    poses_to_evaluate = grasping_manager.get_grasp_poses(in_world_frame=True)
    if not poses_to_evaluate:
        print("No poses available to evaluate..")
        return

    # Determine Output Path
    if not output_dir:
        print("Warning: Output path is not defined data will not be saved.")

    # Set the output path and overwrite flag
    grasping_manager.set_results_output_dir(output_dir)
    grasping_manager.set_overwrite_results_output(True)

    # Determine Physics Scene Path
    physics_scene_path_for_eval = None
    if physics_scene_path and stage.GetPrimAtPath(physics_scene_path):
        physics_scene_path_for_eval = physics_scene_path
    print(f"Physics scene path for evaluation: {physics_scene_path_for_eval}")

    grasping_workflow_task = asyncio.ensure_future(
        grasping_manager.evaluate_grasp_poses(
            grasp_poses=poses_to_evaluate,
            render=True,
            physics_scene_path=physics_scene_path_for_eval,
            simulate_using_timeline=False,
        )
    )

    while not grasping_workflow_task.done():
        simulation_app.update()

    print("Grasping workflow example finished.")
    grasping_manager.clear()

stage_path = "/Isaac/Samples/Replicator/Stage/sdg_grasping_xarm.usd"
ext_path = get_extension_path_from_name("isaacsim.replicator.grasping")
config_path = os.path.join(ext_path, "data/gripper_configs/xarm_antipodal_soup_can.yaml")
output_dir = os.path.join(os.getcwd(), "xarm_antipodal")

run_example(stage_path=stage_path, config_path=config_path, output_dir=output_dir)
```

On this page

* [Learning Objectives](#learning-objectives)
* [Getting Started](#getting-started)
* [Overview](#overview)
* [UI Window Overview](#ui-window-overview)
  + [Gripper Section](#gripper-section)
  + [Object Section](#object-section)
  + [Workflow Section](#workflow-section)
  + [Simulation Section](#simulation-section)
  + [Config Section](#config-section)
  + [Configuration File Example](#configuration-file-example)
* [Code Example](#code-example)

---

### Mobility Gen

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/synthetic_data_generation/tutorial_replicator_mobility_gen.html

* [Synthetic Data Generation](index.html)
* Data Generation with MobilityGen

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Data Generation with MobilityGen

MobilityGen is a toolset built on NVIDIA Isaac Sim
that enables you to generate and collect data for mobile robots.

MobilityGen supports:

* Many robot types
  :   + Differential drive - Jetbot, Carter
      + Quadruped - Spot
      + Humanoid - H1
* Many sensor configurations
  :   + Single front-camera configurations
        :   - JetbotRobot, CarterRobot, H1Robot, SpotRobot
      + USD-based multi-sensor rigs (current version supports multi-camera only)
        :   - JetbotMultiSensorRobot, CarterMultiSensorRobot, H1MultiSensorRobot, SpotMultiSensorRobot
* Many data collection methods
  :   + Manual - Keyboard Teleoperation, Gamepad Teleoperation
      + Automated - Random Accelerations, Random Path Following

## Generate Data with MobilityGen

### Launch Isaac Sim

Open Isaac Sim from the terminal with multi-GPU rendering disabled:

```python
./isaac-sim.sh --/renderer/multiGpu/enabled=false
```

Note

Always launch Isaac Sim with `--/renderer/multiGpu/enabled=false` when using
MobilityGen. On machines with multiple GPUs, leaving multi-GPU rendering enabled
can cause CUDA errors or crashes during MobilityGen startup.

### Build an Occupancy Map

You must create an occupancy map of your environment.

This tutorial uses an example warehouse scene.

1. Load the warehouse stage:

   1. Open Content Browser if itâs not already open (**Window > Browsers > Content**).
   2. Load the warehouse USD file in Isaac Sim/Environments/Simple\_Warehouse/warehouse\_multiple\_shelves.usd.
2. Create the occupancy map:

   1. Select **Tools > Robotics > Occupancy Map** to open the Occupancy Map extension.
   2. In the **Occupancy Map** window set **Origin** to:

      * `X`: `2.0`
      * `Y`: `0.0`
      * `Z`: `0.0`

      To input a value in the text box, `ctrl + left click` to activate the input mode.
   3. In the **Occupancy Map** window set **Upper Bound** to:

      * `X`: `10.0`
      * `Y`: `20.0`
      * `Z`: `2.0` (Assumes the robot can move under two meter overpasses)
   4. In the **Occupancy Map** window set **Lower Bound** to:

      * `X`: `-14.0`
      * `Y`: `-18.0`
      * `Z`: `0.1` (Assume the robot can move over `5cm` bumps)

      Please note, the coordinates specified for the occupancy upper and lower bound define a bounding box within the warehouse\_multiple\_shelves.usd scene that we want the robot to be able to navigate. Weâve pre-selected values that cover the main floor area.
      When using a different scene, you may adjust these bounds to cover the area suitable for your USD scene.
   5. Click **Calculate** to generate the occupancy map.
   6. Click **Visualize Image** to view the occupancy map.
   7. Enter âmapâ in the **Image File Name** field and click **Update YAML**.
   8. Click **Save YAML**.
   9. In the tree explorer, open the folder `~/MobilityGenData/maps/warehouse_multiple_shelves`.

      On Windows replace ~ with the directory of your choice.
   10. Under the file name enter `map.yaml` and click save.
   11. Back in the **Visualization** window, click **Save Image**.
   12. In the tree explorer, open the folder `~/MobilityGenData/maps/warehouse_multiple_shelves`.
   13. Under the file name enter `map.png` and click save.

Verify that you now have a folder named `~/MobilityGenData/maps/warehouse_multiple_shelves/` with
a file named `map.yaml` and `map.png` inside.

### Record a Trajectory

After creating a map of the environment, you can generate data with MobilityGen:

1. Enable the MobilityGen UI extension.

   1. Navigate to **Window** > **Extensions** and search for **MobilityGen UI**.
   2. Click the toggle switch for the **MobilityGen UI** extension.
   3. Verify that two windows open. One window is the MobilityGen UI, the other is to display the Occupancy Map and visualizations. One window might be hiding behind the other when they first appear, so we recommend dragging them into a window pane to view both at the same time.

1. Build the scenario:

   1. In the **MobilityGen** window under **Stage** paste the following USD:

      <http://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Isaac/5.1/Isaac/Environments/Simple_Warehouse/warehouse_multiple_shelves.usd>
   2. In the **MobilityGen** window under **Occupancy Map** enter the path to the `map.yaml` file created previously.

      ~/MobilityGenData/maps/warehouse\_multiple\_shelves/map.yaml
   3. Under the **Robot** dropdown select **H1Robot**.
   4. Under the **Scenario** dropdown select **KeyboardTeleoperationScenario**.
   5. Click **Build**.

      After a few seconds, verify that the scene and occupancy map appear.

1. Test drive the robot using the following keys:

   * `W` - Move forward
   * `A` - Turn left
   * `S` - Move backwards
   * `D` - Turn right
2. Start recording:

   1. Click **Start recording** to start recording a log.
   2. Move the robot around.
   3. Click **Stop recording** to stop recording.

The data is now recorded to `~/MobilityGenData/recordings` by default.

### Sensor calibration overrides

If you change sensors on the robot in Isaac Simâfor example camera intrinsics, distortion
coefficients, projection type, or sensor transformsâMobilityGen persists those edits as a **small
USD diff**, not a full copy of the robot asset.

The comparison below contrasts replay **without** the persisted override file against replay **with**
`sensor_overrides.usda` applied, so rendered cameras match the calibration from capture time.

The following screen capture walks through applying sensor calibration in the UI and how that ties
into recording and replay with `sensor_overrides.usda`.

The MobilityGen extension uses the helpers in
`source/extensions/isaacsim.replicator.experimental.mobility_gen/python/impl/sensor_overrides.py`
to:

1. **Save** calibration overrides from the live stage into a file named `sensor_overrides.usda`
   inside each recording directory. Only attributes you changed (relative to the referenced robot
   USD) are written; the result is a lightweight override layer.
2. **Apply** that same file when you replay or render: the extension loads `sensor_overrides.usda`
   and merges those opinions onto the robot prim **subtree** so nested cameras and rigs match the
   calibration from capture time.

`sensor_overrides.usda` is optional: if a recording does not contain one (for example,
recordings predating this feature), no overrides are applied during replay.

### Replay and Render

After recording a trajectory (robot poses and joint state), you can *replay* it headlessly
to render sensor images (RGB, depth, segmentation, normals) without re-running the physics
simulation.

Note

Recordings made with Isaac Sim 5.x use a different on-disk format than 6.0 and must be
converted before replay. See [MobilityGen Recordings](../migration_guides/isaac_sim_6_0/mobility_gen_recordings_migration.html#mobility-gen-recordings-migration) for the conversion
script.

Isaac Sim ships a standalone replay script for this. Run it from the Isaac Sim root directory
(replace `~/omni_isaac_sim` with your actual Isaac Sim installation path):

```python
./python.sh \
    standalone_examples/replicator/mobility_gen/replay_directory.py \
    --input  ~/MobilityGenData/recordings \
    --output ~/MobilityGenData/replays \
    --render_interval 40
```

* `--input` â directory containing one or more recordings (each in its own subdirectory).
* `--output` â directory where replays with rendered sensor data will be written.
* `--render_interval` â render every Nth physics step. `40` renders roughly once per second and is a good starting point; set to `1` for full-frame-rate output.

Additional optional flags:

* `--rgb_enabled` â enable RGB image rendering (default: `True`).
* `--depth_enabled` â enable depth image rendering (default: `True`).
* `--segmentation_enabled` â enable semantic segmentation rendering (default: `True`).
* `--normals_enabled` â enable surface normal rendering (default: `False`).
* `--instance_id_segmentation_enabled` â enable instance segmentation rendering (default: `False`).
* `--render_rt_subframes` â number of RT subframes per step; increase for higher rendering quality at the cost of speed (default: `1`).

After the script finishes, verify that you have a folder `~/MobilityGenData/replays`, which contains
the rendered sensor data.

You can open this folder to explore the data. Some data (like segmentation masks) can be difficult to visualize using the file browser alone.

Fortunately, there are many examples on how to load and work with the recorded data in the open source [MobilityGen GitHub Repository](https://github.com/NVlabs/MobilityGen/tree/dev-external-occupancy-map-generation/examples). We recommend visualizing your recorded data by running the [Gradio Visualization Script](https://github.com/NVlabs/MobilityGen/blob/main/examples/04_visualize_gradio.py).

To run this example you would clone the above repository and run the following command from a Python interpreter with Gradio installed

```python
python examples/04_visualize_gradio.py --input_dir ~/MobilityGenData/replays
```

You can also check the [reader.py](https://github.com/NVlabs/MobilityGen/blob/main/examples/reader.py) file for a helper class for reading the data in Python.

## Tips

### Generate Procedural Data

Generating procedural mobility data with MobilityGen is done very similar to the basic teleoperation workflow above.

To generate procedural data:

1. Follow `Build an Occupancy Map` above to create an occupancy map of the environment.
2. Follow `Record a Trajectory` above, but select `RandomPathFollowingScenario` instead of `KeyboardTeleoperationScenario`.
   - You no longer need to manually teleoperate the robot. When the scenario is built, it will run and reset automatically.
   - You do need to hit âstart recordingâ to enable recording to disk. However, when the scenario resets, a new recording will be created automatically.
   - Verify that you have recordings collected in the `~/MobilityGenData` folder the same as above.
3. Follow `Replay and render` above to render the sensor data from the recorded trajectories.

The process for other procedural scenarios (like `RandomAccelerationScenario`) is similar.

### Add a Custom Robot

You can implement a new robot for use with MobilityGen. This involves editing the `robots.py` file in the MobilityGen Examples extension.

The general workflow is as follows:

1. Open the `robots.py` file in an editor of choice. This is located at `<isaac sim path>/exts/isaacsim.replicator.mobility_gen.examples/isaacsim/replicator/mobility_gen/examples/robots.py`.
2. Create a new class that subclasses the `MobilityGenRobot` class. Alternatively, if your robot fits one of the existing implementations (like `WheeledMobilityGenRobot`), you can subclass that.

   * We recommend starting by reviewing an existing robot implementation in `robots.py`, to get started. A good way to start is by customizing an existing robot.
3. If you are starting from scratch, implement the required abstract methods of `MobilityGenRobot` class:

   * Implement the `build()` method. This method is responsible for adding the robot to the USD stage.
   * Implement the `write_action()` method. This method takes as input a linear and angular velocity command and performs any control logic.
   * Overwrite common class parameters (like physics\_dt).
4. Register the robot class by using the `ROBOTS.register()` decorator. This makes the custom robot discoverable by MobilityGen.

After implementing this in the file above, save the file.

When you restart Isaac Sim, verify that the new robot is registered, in the MobilityGen UI, and ready for data collection.

Because the registration of a new robot requires editing the Isaac Sim build file, make a copy of your `robot.py` externally so you do not lose it.

When defining your robot, you may find the following list of common parameters and their descriptions helpful

Common Robot Parameters

| Parameter | Description |
| --- | --- |
| `physics_dt` | The physics timestep to use for simulating the robot. |
| `z_offset` | The Z-axis offset height to spawn the robot. |
| `chase_camera_base_path` | The relative USD path which will be used to spawn the third person view camera. This is typically set to the robot base frame. |
| `chase_camera_x_offset` | The relative X-axis offset to spawn the third person view camera. |
| `chase_camera_z_offset` | The relative Z-axis offset to spawn the third person view camera. |
| `chase_camera_tilt_angle` | The tilt angle to apply to the third person view camera. |
| `occupancy_map_radius` | The robot footprint radius to use for spawning and path planning. |
| `occupancy_map_collision_radius` | The robot footprint radius to use for collision based episode termination. |
| `front_camera_type` | The static class representing the front camera. |
| `front_camera_base_path` | The relative USD path to spawn the front camera. |
| `front_camera_rotation` | The relative XYZ rotation used when spawning the front camera. |
| `front_camera_translation` | The relative XYZ translation used when spawning the front camera. |
| `keyboard_linear_velocity_gain` | The gain used to map keyboard button presses to the robotâs linear velocity. A larger gain results in faster movement. |
| `keyboard_angular_velocity_gain` | The gain used to map keyboard button presses to the robotâs angular velocity. A larger gain results in faster movement. |
| `gamepad_linear_velocity_gain` | The gain used to map gamepad axis movement to the robotâs linear velocity. A larger gain results in faster movement. |
| `gamepad_angular_velocity_gain` | The gain used to map gamepad axis movement to the robotâs angular velocity. A larger gain results in faster movement. |
| `random_action_linear_velocity_range` | The robot linear velocity limits for the random acceleration scenario. |
| `random_action_angular_velocity_range` | The robot angular velocity limits for the random acceleration scenario. |
| `random_action_linear_acceleration_std` | The standard deviation used for sampling the robot linear acceleration each timestep during the random acceleration scenario. |
| `random_action_angular_acceleration_std` | The standard deviation used for sampling the robot angular acceleration each timestep during the random acceleration scenario. |
| `random_action_grid_pose_sampler_grid_size` | The grid size to use for spawning the robot during the random acceleration scenario. |
| `path_following_speed` | The constant linear speed to use for the path following scenario. |
| `path_following_angular_gain` | The gain used for the proportional steering control in the path following scenario. A larger gain results in quicker turning, but potential overshoot and wobbling. |
| `path_following_stop_distance_threshold` | The distance threshold at which point the robot will stop. Applies to the path following scenario. |
| `path_following_forward_angle_threshold` | The angle threshold at which point the robot will move forward. Applies to the path following scenario. |
| `path_following_target_point_offset_meters` | The offset distance used to generate the âtarget pointâ that the robot will follow in the path following scenario. A larger offset results in smoother motion, but too large may cause the robot to cut corners during turns. |

### Use NuRec Assets in MobilityGen

MobilityGen operates on USD environments, including 3D reconstructed scenes produced with the NVIDIA NuRec pipeline.
The [NVIDIA PhysicalAI-Robotics NuRec dataset](https://huggingface.co/datasets/nvidia/PhysicalAI-Robotics-NuRec)
provides ready-to-use indoor scenes that can be used directly as MobilityGen stages.

#### Overview

NuRec scenes are published in two USD formats: **Particle USD**, a particle-based representation, and **Volume USD**,
a volumetric representation. Either format can be used as the MobilityGen stage, and many scenes also include a
pre-computed occupancy map that can replace manual map generation.

This workflow follows the same core MobilityGen pipeline described above: select or generate an occupancy map,
record a trajectory, and replay that trajectory to render sensor data. Only the source of the stage and occupancy
map changes when working with NuRec assets.

#### Use a NuRec Scene

1. Download a scene USD file in either particle or volume format from the
   [NVIDIA PhysicalAI-Robotics NuRec dataset](https://huggingface.co/datasets/nvidia/PhysicalAI-Robotics-NuRec).
2. If the dataset provides an occupancy map for the selected scene, use that file directly and skip
   occupancy-map generation.
3. If no occupancy map is available, load the reconstructed USD in Isaac Sim and follow the same
   occupancy-map procedure used for other MobilityGen environments.
4. In the MobilityGen window, set **Stage** to the path of the NuRec scene USD, for example:

   ```python
   /path/to/nurec_scene.usd
   ```
5. Set **Occupancy Map** to the corresponding `map.yaml` file, either from the dataset or from
   the generated output.
6. Continue with the standard MobilityGen flow: record a trajectory, then run `replay_directory.py`
   to replay and render sensor data.

Note

RGB rendering is fully supported for trajectories recorded in reconstructed environments.
Depth rendering can be enabled, but accuracy is not guaranteed because reconstructed geometry
may be incomplete or noisy. Semantic segmentation is not supported for reconstructed scenes
in this workflow.

To skip depth and semantic segmentation during replay (recommended for NuRec-only workflows),
pass the negated flags supported by `replay_directory.py`:

```python
./python.sh \
    standalone_examples/replicator/mobility_gen/replay_directory.py \
    --input  ~/MobilityGenData/recordings \
    --output ~/MobilityGenData/replays \
    --render_interval 6 \
    --no-depth_enabled \
    --no-segmentation_enabled
```

`--no-depth_enabled` turns off depth image rendering; `--no-segmentation_enabled` turns off
semantic segmentation. RGB remains on by default (use `--no-rgb_enabled` only if you want to
disable RGB as well).

Occupancy-map quality depends on the collision geometry available in the USD stage. When
generating a map for a reconstructed scene, review the occupancy-map visualization and adjust
bounds as needed before recording trajectories.

## Next Steps

In this tutorial, you:

1. Built an occupancy map for use with MobilityGen.
2. Recorded a MobilityGen trajectory using the H1 robot with keyboard Teleoperation.
3. Rendered sensor data based on the recorded trajectory.

As next steps, try recording data:

* for a different robot (for example: Spot)
* using a different scenario (for example: Random Path Following)

On this page

* [Generate Data with MobilityGen](#generate-data-with-mobilitygen)
  + [Launch Isaac Sim](#launch-isaac-sim)
  + [Build an Occupancy Map](#build-an-occupancy-map)
  + [Record a Trajectory](#record-a-trajectory)
  + [Sensor calibration overrides](#sensor-calibration-overrides)
  + [Replay and Render](#replay-and-render)
* [Tips](#tips)
  + [Generate Procedural Data](#generate-procedural-data)
  + [Add a Custom Robot](#add-a-custom-robot)
  + [Use NuRec Assets in MobilityGen](#use-nurec-assets-in-mobilitygen)
    - [Overview](#overview)
    - [Use a NuRec Scene](#use-a-nurec-scene)
* [Next Steps](#next-steps)

---

### Teleop SDG

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/synthetic_data_generation/tutorial_replicator_teleop_sdg.html

* [Synthetic Data Generation](index.html)
* Teleoperation Synthetic Data Generation

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Teleoperation Synthetic Data Generation

Teleoperation in Isaac Sim lets you control robots with a VR headset and controllers, capture the resulting motion as demonstration data, and replay it to generate synthetic datasets for robot learning.

|  |  |
| --- | --- |
|  |  |

This tutorial covers the `isaacsim.replicator.teleop` and `isaacsim.replicator.teleop.ui` extensions. The runtime drives robot arms, grippers, floating end effectors, and mobile bases from VR controllers. The UI exposes that runtime as a Teleop window with six collapsible panels. The `isaacsim.replicator.episode_recorder` extension handles recording, replay, and offline synthetic data generation.

## Learning objectives

After completing this tutorial, you will be able to:

* Connect Isaac Sim to a CloudXR-capable VR headset through the Isaac Teleop runtime.
* Configure the Floating, IK, Grasp, and Locomotion controllers from the Teleop window.
* Operate a robot from VR controllers, or from on-screen markers and sliders in debug mode.
* Save and reload complete teleop setups as YAML profiles.
* Record teleop episodes to HDF5 with the Episode Recorder.
* Replay recorded episodes through Replicator writers to generate synthetic datasets.

## Getting started

### Prerequisites

* Isaac Sim built and launchable.
* [Isaac Teleop](https://github.com/NVIDIA/IsaacTeleop) installed from PyPI:

  ```python
  python -m pip install "isaacteleop[cloudxr,retargeters]~=1.0.0"
  ```
* A CloudXR-compatible VR headset on the same network as the host machine. Controller button mappings in this tutorial target the Meta Quest 3; other headsets may surface different button semantics through the same OpenXR actions.
* A stage with a robot. Use one of the [built-in scenario stages](#isaac-sim-app-tutorial-replicator-teleop-test-stages) (for example `teleop_scenario_floating_xarm_dex3.usd`) while learning the workflow.

Note

Debug mode replaces VR input with draggable USD markers and on-screen sliders. It does not require a headset, CloudXR, or the Isaac Teleop package. Skip the CloudXR steps below if you only plan to use debug mode. See [Operate without VR (debug mode)](#isaac-sim-app-tutorial-replicator-teleop-sdg-debug).

### Start CloudXR and connect the headset

Start the Isaac Teleop CloudXR runtime in a separate terminal and keep it running for the whole teleop session:

```python
python -m isaacteleop.cloudxr
```

Open the [Isaac Teleop Web Client](https://nvidia.github.io/IsaacTeleop/client/) from the headset browser and follow the displayed connection steps to pair the headset. With CloudXR running and the headset connected, you complete the rest of the workflow in Isaac Sim â launching the app, opening the Teleop window, and clicking **Connect** â without returning to the web client.

### Running modes

The teleop runtime works in two Isaac Sim launch configurations. Both load the Teleop UI and support every controller described in this tutorial.

* **2D monitor (controller tracking only)** â The desktop viewport renders the scene on a flat screen. The headset and controllers feed pose tracking to the runtime over CloudXR but do not stereo-render the scene. This is the default mode and requires no special app:

  ```python
  ./isaac-sim.sh
  ```
* **VR headset (stereo rendering)** â Launches the XR VR experience app (`isaacsim.exp.base.xr.vr.kit`). The headset receives a stereo-rendered viewport for a first-person 3D view and exposes an in-headset **Play** / **Stop** UI equivalent to the desktop timeline buttons. The desktop window stays available for UI interaction:

  ```python
  ./isaac-sim.xr.vr.sh
  ```

### Open the Teleop window

The extensions are loaded automatically. Open the Teleop window from **Tools** > **Replicator** > **Teleop**:

With the CloudXR runtime running and the headset connected, click **Connect** in the **Session** panel to start the teleop session.

## Quick start

Pair one of the built-in scenario stages with its matching profile, connect, and press **Play**. The profile resolves every controller against the stage, so no manual setup is needed.

1. Open one of the [built-in scenario stages](#isaac-sim-app-tutorial-replicator-teleop-test-stages), for example `teleop_scenario_floating_xarm_dex3.usd`.
2. In the Teleop windowâs **Profiles** panel, select the matching profile (`floating_xarm_dex3.yaml`) and click **Load**. Every controller resolves against the stage and its **Enable** button activates.
3. Expand **Session** and click **Connect**. Without a headset, expand **Session > Debug** and check **Debug Tracking** instead.
4. Press **Play** on the timeline.
5. Move the VR controllers (or drag the on-screen markers in debug mode) to operate the robot.

A profile enables only the controllers its scenario needs:

* [Floating Controller](#isaac-sim-app-tutorial-replicator-teleop-ui-floating) â tracks a free rigid-body gripper or end effector to the VR controller pose.
* [IK Controller](#isaac-sim-app-tutorial-replicator-teleop-ui-ik) â drives an articulated arm through inverse kinematics so its end effector tracks the VR controller.
* [Grasp Controller](#isaac-sim-app-tutorial-replicator-teleop-ui-grasp) â maps the VR trigger to gripper open and close.
* [Locomotion](#isaac-sim-app-tutorial-replicator-teleop-ui-locomotion) â moves the robot base or the VR origin from the thumbsticks.

For example, `floating_xarm_dex3.yaml` enables the Floating, Grasp, and Locomotion controllers; the IK profiles enable IK instead of Floating. See the [workflow walkthrough](#isaac-sim-app-tutorial-replicator-teleop-walkthrough) for the detailed, step-by-step version, including recording and replay.

## Overview

The extension is split into two layers:

* `isaacsim.replicator.teleop` â runtime that handles VR input, frame markers, and the four controllers (Floating, IK, Grasp, Locomotion), all managed by `TeleopManager`.
* `isaacsim.replicator.teleop.ui` â the Teleop window with six collapsible panels: **Profiles**, **Session**, **Floating Controller**, **IK Controller**, **Grasp Controller**, and **Locomotion**.

Every controller follows the same three-step lifecycle:

1. **Apply** validates the prim path and prepares the controller resources.
2. **Enable** arms the controller for the next **Play**.
3. **Clear** tears down the resources but keeps the prim path for quick reconfiguration.

Controllers are only active while the timeline is playing and deactivate automatically on **Stop**. Gains, rotation offsets, and speed sliders are live-editable during **Play** and persist across sessions. The complete state of every panel can be saved to a YAML profile from the **Profiles** panel.

The Episode Recorder window handles recording and replay. While a `TeleopManager` is alive, sessions opened from that window automatically capture teleop controller, aim-pose, and head-pose channels in addition to the articulation, rigid-body, and Xform channels selected in the UI. The recorded HDF5 files feed the offline [synthetic-data pipeline](#isaac-sim-app-tutorial-replicator-teleop-sdg-replay). For scripted workflows, `build_teleop_recorder` returns an equivalent recorder preconfigured with both teleop and scene recordables.

## UI window overview

The Teleop window contains six collapsible panels, described below from top to bottom. The separate Episode Recorder window handles recording and replay; see [Record and replay](#isaac-sim-app-tutorial-replicator-teleop-episode-recorder).

### Profiles

The **Profiles** panel saves and restores the complete state of every other panel as a single YAML file.

* **Dir** â working directory for teleop profile files. Defaults to the built-in profiles shipped with the extension. Click the folder icon to browse for a custom directory.
* **Profile dropdown** â lists all `.yaml` files found in the working directory.
* **Load** â reads the selected profile and applies it to all panels. If the stage contains the referenced prims, controllers are resolved immediately; otherwise the UI fields are populated and unresolved paths are reported.
* **Save** â opens an inline **Name** field and **Confirm** button. Enter a filename (without `.yaml`) and click **Confirm** to write the current panel state to disk. If a file with that name already exists, an **Overwrite profile** dialog asks for confirmation; click **Overwrite** to replace it or **Cancel** to keep the existing file.
* **Validate** â checks all panel settings against the current stage and reports error and warning counts in the status line. Detailed issues are printed to the console.
* **Delete** (trash icon) â permanently removes the selected profile file from disk.

### Session

The **Session** panel manages the VR connection, frame markers, the **XR Anchor** (custom-anchor prim plus headset offset and rotation), and the debug controls.

#### Connection

* **Connect** / **Disconnect** â establishes or tears down the OpenXR connection to the Isaac Teleop CloudXR session.
* **Status** â displays the current connection state: red (**Disconnected**), green (**Connected - markers active**), or yellow (intermediate states such as **No data**).

#### Frame Markers

The **Frame Markers** sub-section shows the live VR poses as four frame-axis prims under `/Teleop/Markers/TrackingOrigin` â the origin, **Left**, **Right**, and **Head**. Markers are created automatically on **Connect** and on enabling **Debug Tracking**; you can also create or remove them manually here.

* **Show** â creates the four frame-axis markers and begins streaming VR poses to them.
* **Remove** â deletes the markers and stops tracking.
* **Scale** â adjusts the visual axis length of every marker.

#### XR Anchor

The **XR Anchor** sub-panel groups every control that determines where the VR headset and controllers appear in the scene: the prim the anchor follows (**Custom Anchor**), the per-pose **Coordinate Frame** conversion, and the headset offset, rotation, and fixed-height controls applied on top of that anchor. The naming mirrors Kitâs VR Profile menu, where the same concept is exposed under **Navigation Settings > Physical World USD Anchor > Custom USD Anchor**.

* **Coordinate Frame** â selects how incoming VR poses are converted:

  + **Isaac Sim (Z-up)** â applies a Y-up to Z-up rotation so poses match the Isaac Sim stage convention (default).
  + **Raw (no conversion)** â passes poses through unchanged.
* **Custom Anchor** â scene prim that the VR headset and controllers are anchored to. Click **Set** to validate the path and start live every-frame following of the primâs world transform. After a custom path is active, the same row button changes to **Clear**. **Clear** reverts the active anchor to the built-in origin marker under `/Teleop/Markers/` and resets the marker to world (0, 0, 0); the typed path is preserved in the field. To retarget the active anchor, click **Clear**, edit the path if needed, and click **Set** again. Use the bin glyph in the row to clear the field text. Paths under the reserved `/Teleop/Markers/` namespace fall back to the built-in origin on **Set**.
* **Offset** â position offset in metres for the VR headset camera (one row with **X**, **Y**, and **Z** fields). Without a Custom Anchor this is an absolute world position; with one, it is relative to that prim.
* **Rotation** â how the headset camera yaw tracks the Custom Anchor prim:

  + **Fixed** â ignore prim rotation entirely.
  + **Follow Prim** â yaw tracks the prim (roll and pitch are stripped).
  + **Follow (Smoothed)** â same as Follow Prim with slerp damping.
* **Smooth** â slerp time constant in seconds, used only in **Smoothed** mode. Lower values give snappier tracking; higher values are smoother.
* **Fixed Height** â locks the headset camera Z to its initial value, preventing vertical bobbing when the Custom Anchor prim moves up or down.

Note

The teleop extension owns Kitâs XR profile anchor (set under **VR Profile > Navigation Settings > Physical World USD Anchor**) for the duration of a session. On **Connect** it switches Kit to `custom anchor` mode pointing at `/World/XRAnchor` and drives that prim every frame from the **Custom Anchor** prim plus the offset, rotation, smoothing, and coordinate-frame controls above. To retarget an active custom anchor, clear it first and then set the new path. Kitâs profile-level **Adjust for User Height** setting (under **Navigation Settings**) is unrelated â it shifts the camera at scene-entry time, while **Fixed Height** here locks Z to its first-frame value during the teleop session.

#### Debug

Debug mode replaces VR controller input with draggable USD markers and on-screen sliders, so every controller can be exercised without VR hardware. See [debug mode](#isaac-sim-app-tutorial-replicator-teleop-sdg-debug) for the step-by-step walkthrough.

|  |  |
| --- | --- |
|  |  |

* **Write Backend** â overrides the global `XformPrim` backend used for all teleop writes. Options: **USD** (plain attribute writes), **USD-RT** (Fabric hierarchy), **Fabric** (fastest path, requires Fabric Scene Delegate).
* **Debug Tracking** checkbox â enables synthetic pose input. Mutually exclusive with a live VR connection: disconnect first, or disable debug tracking before connecting.
* **L Grasp** / **R Grasp** â sliders (0â1) that simulate the VR trigger squeeze. Feed directly into the Grasp Controller as `trigger_value`.
* **Slide X** / **Slide Y** â sliders (-1 to 1) that simulate the left thumbstick for Locomotion lateral and forward/backward slide.
* **Turn** â slider (-1 to 1) that simulates the right thumbstick for Locomotion yaw.
* **Up** / **Down** â hold-buttons that simulate the right-side face buttons for vertical motion.
* **Carry Origin** â hold-button that simulates the left primary face button. Press and hold to assert the input; release to clear it. The Locomotion controller toggles **Carry Tracking Space** on the rising edge.

### Floating Controller

The **Floating Controller** drives a free rigid body so that it tracks the VR controller pose using velocity-based PD control. Use it for end effectors or grippers that are not part of an articulation chain. Each side (**Left** / **Right**) has its own collapsible sub-panel.

The target prim must be a rigid body. To control an articulated gripper with the Floating Controller, attach the articulation root joint to a rigid body and point the Floating Controller at that rigid body. The gripper articulation is then carried along as a child, while the Grasp Controller independently drives its finger joints.

* **Prim Path** â the rigid body prim to drive. Click the **+** button to pick the prim from the viewport, or paste the path. Click **Apply** to validate. The path field, **+** button, and trash button are locked once configured; click **Clear** to reconfigure.
* **Target Rot** (one row with **X**, **Y**, and **Z** combos) â per-axis local rotation offset in 90-degree increments (-180, -90, 0, +90, +180). Different grippers and end effectors have different local-frame conventions; these offsets align the controlled body so that its forward axis matches the VR controller pointing direction. For example, a gripper whose local Z points sideways instead of forward can be corrected with a 90-degree Y offset. Adjustable during **Play** and saved in teleop profiles.
* **Pos Kp / Kd** â position proportional and derivative gains. Higher **Kp** makes the body snap to the target faster; **Kd** damps oscillations.
* **Rot Kp / Kd** â orientation proportional and derivative gains. Same principle as position gains, applied to rotational tracking.
* **Enable** / **Disable** â arms or disarms the controller for the next **Play**. Status transitions: *Configured* â *Standby* â *Active* (on Play).
* **Clear** â destroys the controller resources while keeping the prim path.

### IK Controller

The **IK Controller** drives an articulated robot arm through inverse kinematics so that its end effector tracks the VR controller pose. Each side (**Left** / **Right**) has its own collapsible sub-panel.

The target prim must be an articulation. The IK solver operates on the joint chain from the articulation root down to the selected end-effector link. For a typical setup â for example a UR3e arm with a gripper attached â select the wrist link as the end effector so that IK solves only for the arm joints. The gripper joints are then driven separately by the Grasp Controller.

#### Articulation and end effector

* **Prim Path** â the articulation root prim. Click **Apply** to validate. On success the **EE Link** dropdown is populated with all body links in the kinematic chain.
* **EE Link** â selects which link in the chain is the IK target. Choose the last arm link (for example the wrist) to exclude gripper joints from the IK solve. The last link in the chain is selected by default.
* **Clear** â destroys the solver and articulation resources; the prim path is preserved for quick reconfiguration.

#### Solver selection

* **Solver** dropdown â chooses the IK backend. Each solver can be hot-swapped during **Play** without stopping the timeline:

  | Solver | Description |
  | --- | --- |
  | **Position-based** | Single-step Jacobian differential IK. Supports a configurable **Method** dropdown. |
  | **Velocity-based** | Velocity-space IK with a proportional **Gain** slider that controls tracking aggressiveness. Also supports a **Method** dropdown. |
  | **Levenberg-Marquardt** | Multi-iteration damped least-squares per frame. No method or gain controls. |
  | **PINK** | Task-based QP IK using a Pinocchio backend with joint-limit enforcement and posture regularisation. Exposes additional tuning described below. |
* **Method** dropdown â visible only for **Position-based** and **Velocity-based** solvers. Selects the Jacobian inversion strategy:

  + **Damped LS** â most stable default; handles singularities well.
  + **Pseudoinverse** â direct tracking when well-conditioned; less stable near singularities.
  + **Transpose** â cheapest update; can be gain-sensitive.
  + **SVD** â robust singular-value filtering; typically the heaviest compute.

#### Rotation offset and tuning

* **EE Rot** (one row with **X**, **Y**, and **Z** combos) â per-axis local rotation offset in 90-degree increments (-180, -90, 0, +90, +180). Same purpose as **Target Rot** for the Floating Controller: align the IK target so the robotâs tool tip or gripper faces the same direction as the VR controller. Adjustable at runtime and saved in profiles.
* **VR Target Filter** â exponential moving average (EMA) low-pass filter on the incoming VR target pose. Range 0.0â0.95. Higher values reduce jitter but add delay. Default 0.0 (no filtering).
* **Max Joint Step** â safety clamp on the maximum joint-angle change per simulation step (radians). Prevents sudden joint jumps without acting as a true velocity limit. Default 0.0 (disabled).
* **Gain** â (Velocity-based solver only) proportional gain controlling how aggressively the end effector tracks the VR target. Values of 1â5 give smooth conservative tracking; 10â20 are fast; above 30 may oscillate.

#### PINK-specific tuning

These controls appear only when the **PINK** solver is selected:

* **Task Gain** â PINK `FrameTask` response gain. Higher values make tracking more aggressive; lower values soften it.
* **Posture** â posture regularisation cost. Higher values keep the arm closer to its current pose; lower values give the end-effector task more freedom.
* **QP** dropdown â quadratic-program solver backend. Use to compare solve quality and performance across backends.
* **LM Damp** â `FrameTask` Levenberg-Marquardt damping. Higher values improve stability in difficult configurations but slow response.

#### Enable and status

* **Enable** / **Disable** â arms or disarms the IK controller for the next **Play**. During Play the status shows **Active** when the target is reachable and **Out of reach** when the VR target leaves the armâs workspace. Tracking resumes automatically when the target returns to a reachable pose.

### Grasp Controller

The **Grasp Controller** maps the VR triggerâs analog value (0 = open, 1 = fully closed) to gripper joint drive targets. Grippers vary widely â a parallel-jaw gripper has a single drive joint, while a multi-finger hand can have a dozen joints across several fingers â so the controller relies on a YAML config file that defines the mapping from the linear 0â1 trigger value to each jointâs target position. Each side (**Left** / **Right**) has its own collapsible sub-panel with independent configuration.

* **Prim Path** â the gripper articulation prim. Click **Apply** to validate the path and load the currently selected config in one step. The field is locked after configuration; click **Clear** to reconfigure.
* **Config** dropdown â selects a built-in grasp configuration shipped with the extension. Selecting an entry immediately updates the path field next to it and resets the side to `Config changed - click Apply`, so **Apply** must be clicked again before **Enable** becomes available.
* **Config path field** (the editable text field next to **Config**) â full path or `builtin://` URI to a grasp config YAML. Type a custom path here to use your own config file for a custom gripper or grasp style. Editing this field also requires another **Apply** click.
* **Enable** / **Disable** â arms or disarms trigger tracking for this side.
* **Clear** â destroys grasp resources while keeping the paths for quick reconfiguration.

During **Play**, trigger pressure is read from the VR controller or from the **L Grasp** / **R Grasp** debug sliders. For each joint listed in the config, the controller interpolates linearly between the open and closed target values based on the current trigger value.

#### Config file format

Each config file lists the joints to drive, the input range, and the corresponding target range in degrees. Author custom config files to support your own grippers or to define alternative grasp styles on the same hand â for example, a pinch grasp vs. a full-palm grasp on a five-finger hand.

**Simple gripper** â `xarm_grasp.yaml` maps a single drive joint:

```python
joints:
  - name: "drive_joint"
    input_range: [0.0, 1.0]
    target_range: [0.0, 48.0]
```

**Multi-finger hand** â `dex3_grasp.yaml` maps seven joints across three fingers, each with its own target range:

```python
joints:
  - name: "right_hand_index_0_joint"
    input_range: [0.0, 1.0]
    target_range: [0.0, 90.0]
  - name: "right_hand_index_1_joint"
    input_range: [0.0, 1.0]
    target_range: [0.0, 80.0]
  - name: "right_hand_middle_0_joint"
    input_range: [0.0, 1.0]
    target_range: [0.0, 90.0]
  - name: "right_hand_middle_1_joint"
    input_range: [0.0, 1.0]
    target_range: [0.0, 80.0]
  - name: "right_hand_thumb_0_joint"
    input_range: [0.0, 1.0]
    target_range: [0.0, 0.0]
  - name: "right_hand_thumb_1_joint"
    input_range: [0.0, 1.0]
    target_range: [0.0, -60.0]
  - name: "right_hand_thumb_2_joint"
    input_range: [0.0, 1.0]
    target_range: [0.0, -60.0]
```

### Locomotion

The **Locomotion** controller moves a prim kinematically using VR thumbstick and face-button input. Horizontal movement is projected onto the world ground plane using the primâs heading, so axes remain correct regardless of the target primâs local-frame orientation.

Two workflows are supported:

* **Robot base** â set the prim path to a robot base link. Thumbstick input moves the robot, and attached arms and grippers follow. Toggle **Carry Tracking Space** (left primary button) to co-move the VR origin with the robot.
* **VR origin** â set the prim path to the built-in tracking-space origin marker (`/Teleop/Markers/TrackingOrigin`). Carry is implicit because the locomotion prim *is* the VR origin. Use this for floating grippers that have no physical base.

Controls:

* **Prim Path** â the prim to move. Click **Apply** to validate.
* **Slide Step** â slide distance per app update at full input. Drives left-thumbstick translation (forward, backward, lateral) and the right face-button vertical motion.
* **Turn Step** â turn angle per app update at full right-thumbstick yaw input.
* **Enable** / **Disable** â arms or disarms locomotion for the next **Play**.
* **Clear** â destroys the configured state while keeping the prim path.

During **Play** the controller reads the following VR inputs:

* **Left thumbstick** â forward/backward (Y) and left/right (X) slide in the world ground plane.
* **Right thumbstick** â left/right yaw turn.
* **Right face buttons** â `A` (primary) moves down, `B` (secondary) moves up along world Z (Meta-style controller layout).
* **Left primary face button** (`X` on Meta-style controllers) â toggles **Carry Tracking Space** mode. When active, locomotion also moves the Tracking Space prim with the base, including turn rotation around the base pivot. When the locomotion prim *is* the tracking-space origin, carry is implicit and the toggle has no additional effect.

## Record and replay (Episode Recorder)

The Episode Recorder window (`isaacsim.replicator.episode_recorder.ui`, opened from **Tools** > **Replicator** > **Episode Recorder**) records per-physics-step simulation state to multi-episode HDF5 files and replays them through the Kit timeline. It works on any stage. When a `TeleopManager` is alive, teleop controller, aim-pose, and head-pose channels are appended to every session opened from the window via `install_teleop_session_injector`.

A recording *session* is one HDF5 file that contains many *episodes*. Episodes auto-start on timeline **Play** and auto-end on timeline **Stop**. The window buttons, the VR recording button, and any scripted caller add a manual start, end, or toggle edge on top of that, all driving the same underlying session.

### Targets and output

* **USD Root** â prim path scanned by the discovery helpers. `/World` is a sensible default.
* **Discover** â lists every articulation (via `ArticulationRootAPI`), rigid body (via `RigidBodyAPI`), and plain Xform prim under the root. Plain Xforms are always included, so a locomotion-driven robot-base cube, a hand-placed tracker, or a visual tool tip under an articulation show up without extra opt-in.
* **Discovered Targets** (collapsible, scrollable) â the articulations and prims found under the root. Tick the boxes for every target you want recorded; each tick maps to a group or dataset inside the HDF5 file.
* **Output Dir** â directory where the HDF5 file is written. Defaults to `<cwd>/_episode_recorder`; created if missing.
* **Export Scene** (next to the Output Dir field) â writes a flattened USD of the current stage as `<output_dir>/stage_snapshot.usd` together with `stage_snapshot.sidecar.json`. The snapshot is scene-level, so one click per scene is enough: subsequent **Open Session** calls detect the file and stamp its basename into the HDF5 `stage_snapshot` attribute automatically.
* **File Prefix** â filename prefix. The final path is `{prefix}_{timestamp}.hdf5`.
* **Auto-start recording on timeline Play** â when checked (default), pressing **Play** automatically starts a new episode. Uncheck it to record only when **Start** / **End** (or the VR button) is pressed; the timeline can play without any episode being captured.
* **Pose Backend** (record side) â selects the backend used by the recorderâs per-tick batch `XformPrim.get_world_poses()` read. Options: **usd** (default; pure USD reads), **usdrt** (Fabric Scene Delegate via `IFabricHierarchy`), **fabric** (Fabric Scene Delegate direct). The Fabric-backed options are safe speedups when Fabric Scene Delegate is enabled and fall back to `usd` with a carb warning when it is disabled. Distinct from the **Write Backend** in the Teleop **Session > Debug** panel, which controls the teleop *write* path.

### Session and episode control

* **Open Session** / **Close Session** â single toggle button. On open, the recorder creates the HDF5 file, subscribes to simulation events, and the filename appears below. All configuration options are locked while a session is open.
* **Start** / **End** â single toggle button that manually starts or ends an episode inside the open session. Only enabled while a session is open. Also driven by the VR left-Y button (see below) and, when **Auto-start recording on timeline Play** is enabled, by the timeline PLAY / STOP hooks.
* **Binding badge** â small dotted label rendered next to **Start / End**. Lights up green and lists every external input (for example a `VRRecordingButton` attached by `TeleopManager`) currently wired to this recorder. The tooltip enumerates each bindingâs label and the command it dispatches (`start` / `end` / `toggle`). Empty when no external bindings are active.
* **Status label** â colour-coded feedback below the buttons:

  + *Idle* (dim).
  + *Session open - N articulation(s), M prim(s)* (yellow).
  + *Recording episode #K* (green).
  + *Standby - K episode(s) captured* (yellow).
  + *Session closed (K episode(s))* (green).

  Errors and warnings are shown in red and yellow.

### VR recording button

`TeleopManager` auto-attaches the Meta Quest left-Y button (`VRButton.LEFT_SECONDARY`) to the `toggle` command via `VRRecordingButton` on construction and keeps the binding alive for its lifetime. One press starts a new episode; a second press ends it. The binding is rising-edge triggered, so holding the button does not retrigger. When no session is open the dispatch is a no-op.

The binding has only been tested with the Meta Quest 3; other headsets may surface different button semantics through the same OpenXR action.

### Replay

The **Replay** sub-section (collapsible, collapsed by default) plays any previously recorded HDF5 back through the Kit timeline. Replay is mutually exclusive with recording: while a session is open the Replay controls are locked, and while replay is attached the recording controls are locked.

The transport row uses Kit timeline-style glyph buttons rather than text labels: play / stop, pause, step-backward, and step-forward.

* **File** â full path to an HDF5 session file. Use **Latest** to fill in the newest `{prefix}_*.hdf5` in the current **Output Dir**.
* **Load** â opens the HDF5 and populates the **Episode** dropdown with every episode name and its frame count. The info label next to the dropdown shows `success=True/False` for the selected episode, so abandoned takes are visible at a glance. After load, a red warning row appears below the status if any prim paths referenced by the HDF5 do not resolve on the current stage â open the matching scene (or the exported `stage_snapshot.usd`) before starting the replay.
* **Pose Backend** (replay side) â selects the backend used by the replayerâs per-tier batch pose write. Options match the record-side selector (**usd** / **usdrt** / **fabric**). `usd` is the recommended default â the ancestry-ordered tier split plus USD writes is what avoids parent-lag stutter on articulations nested under moving xforms. `usdrt` and `fabric` are reserved for benchmarking flat scenes and may exhibit a one-frame parent-lag on nested hierarchies. Applied on **Load**.
* **Play / Stop** glyph â drives `EpisodeReplayer.start_replay`. Each Kit app update applies one recorded frame and seeks (never plays) the Kit timeline to the recorded `sim_time`, so any stage-authored USD animations play back in lockstep without stepping physics. Pose writes land in an anonymous USD sublayer so the root stage is never mutated. Stopping (or reaching the last frame in non-loop mode) pops that sublayer, returning every prim to its pre-replay pose; the HDF5 session stays loaded so a fresh replay can be started immediately.
* **Pause** glyph â pauses the replay on the current frame; the last applied frame stays on the stage. Pressing it again resumes from where it left off. The Stop glyph still pops the anonymous sublayer.
* **Step Backward / Step Forward** glyphs â apply the previous or next recorded frame and auto-pause the replay. Use them to inspect the recording one frame at a time or to seek to a specific moment before resuming.
* **Seek timeline** â when checked (default), each applied frame also seeks the Kit timeline to that frameâs recorded `sim_time` so stage-authored USD animations stay in sync with the recording. Uncheck it to replay only the recorded prim poses and leave the timeline untouched.
* **Progress label** â below the replay status, shows the currently applied frame as `Frame X / N`. The same counter is emitted to the terminal at one-second intervals and on the first and last frame.

Replay is pure-USD and timeline-seeking only â the replayer never plays the timeline and never calls into the physics engine. Teleop controllers (Floating, IK, Grasp, Locomotion) stay dormant during replay, which avoids the `Simulation view object is invalidated` errors that playing the timeline against a stopped simulation would otherwise trigger. The start / stop lifecycle emits `[EpisodeRecorder][UI] Replay: starting (episode ..., N frames, file=...)` and `Replay: stopped (reason=user | finished | stage_closed)` on the terminal, plus a periodic `Replay: frame X/N` progress line.

For replay to work, every prim path recorded in the HDF5 must exist on the loaded stage. The Replay panel uses a lenient replayer (`ReplayPolicy(strictness="best_effort")`) that skips missing paths with a warning rather than erroring. To guarantee a reproducible setup, click **Export Scene** once before recording; the resulting `stage_snapshot.usd` can be opened on any machine to reproduce the authored stage before replaying.

### HDF5 file layout

Each session produces one HDF5 file with one group per episode. Datasets are preallocated per episode and trimmed to their true length on `end_episode`.

```python
<file>.hdf5                             # one file per open_session()
âââ @schema_version, @created_at, manifest/, ...  # file-level attrs + manifest
âââ @stage_snapshot                     # optional, set by Export Scene
âââ episodes/
    âââ episode_00000/                  # @episode_index, @started_at, @ended_at,
    â   â                               # @num_frames, @success (optional),
    â   â                               # @user_metadata (optional, JSON)
    â   âââ meta/time/
    â   â   âââ sim_time            (N,)     float64
    â   â   âââ physics_step        (N,)     int64
    â   â   âââ wall_time           (N,)     float64
    â   âââ state/<name>/                  # articulation, xform, or rigid body (UI naming)
    â   â   âââ positions           (N, L, 3)  float32   # articulation: per-link world position
    â   â   âââ orientations        (N, L, 4)  float32   # articulation: per-link wxyz
    â   â   âââ position            (N, 3)     float32   # xform / rigid body
    â   â   âââ orientation         (N, 4)     float32   # wxyz
    â   âââ teleop/                        # present when a live TeleopManager is active
    â       âââ <side>/{trigger, squeeze, thumbstick_x, thumbstick_y}     (N,)    float32
    â       âââ <side>/{primary_click, secondary_click, thumbstick_click} (N,)    uint8
    â       âââ <side>/aim_position          (N, 3)  float32   # record_aim_pose=True
    â       âââ <side>/aim_orientation       (N, 4)  float32   # wxyz
    â       âââ head/{position, orientation} (N, 3 | 4)  float32   # record_head_pose=True
    âââ episode_00001/ ...
    âââ episode_00002/ ...
```

For articulations, `L` is the number of recorded links (the articulation root plus every `UsdGeom.Xformable` descendant). The link list is frozen on **Open Session** and stored in the manifest so the replayer binds to the same prim set. There are no DOF, velocity, or drive-target channels: every gripper-drive joint is reproduced through its child linkâs recorded world pose, so replaying open / closed grippers works without running any teleop logic.

`EpisodeReplayer.list_episodes` iterates the `episodes/episode_NNNNN` groups for per-episode playback.

### Recorded data vs. replayed data

The recorder captures two kinds of data per frame:

* **World state** (under `state/<name>/`, one HDF5 group per recorded articulation, Xform, or rigid body) â the world pose of every recorded prim. For articulations, this is the per-link pose array; for rigid bodies and Xforms, the single root pose. This is the *only* data the replayer applies.
* **Teleop input channels** (under `teleop/<side>/...`, present only when a live `TeleopManager` is active at record time) â trigger, squeeze, thumbstick, button clicks, and optional OpenXR aim-pose and head-pose channels. Recorded for offline analysis, policy learning, and re-simulation; the replayer *ignores* them entirely.

Aim-pose and head-pose capture is controlled by the carb settings `/persistent/exts/isaacsim.replicator.teleop/record/record_aim_pose` and `.../record_head_pose` (both default `True`). Toggle them from the Script Editor (`carb.settings.get_settings().set_bool(...)`) before opening a session if you want to skip them.

On replay, `EpisodeReplayer.apply_frame` writes the recorded world pose of every prim (and every articulation link) into an anonymous USD sublayer through `XformPrim.set_world_poses`. No physics is stepped, no DOFs are written, no IK is solved, no trigger command is re-dispatched, no OpenXR input is consumed. The teleop controllers (**Floating**, **IK**, **Grasp**, **Locomotion**) stay dormant. Replay is strictly a USD-pose playback.

### Programmatic recordables (cameras, attributes)

The Episode Recorder window only auto-discovers articulations, rigid bodies, and plain Xforms under the **USD Root**. To capture additional channels â typically camera trajectories for the [synthetic-data pipeline](#isaac-sim-app-tutorial-replicator-teleop-sdg-replay) or arbitrary USD attributes for offline analysis â build the recorder programmatically and `add` the extra recordables before opening the session:

```python
from isaacsim.replicator.episode_recorder import (
    CameraRecordable,
    AttributeRecordable,
)
from isaacsim.replicator.teleop import build_teleop_recorder

recorder = build_teleop_recorder(
    output_dir="/tmp/demos",
    teleop_manager=teleop_manager,
    articulations={"robot": "/World/teleop/robot"},
)
recorder.add(CameraRecordable(
    group="cameras/wrist",
    prim_path="/World/teleop/robot/.../wrist_cam",
))
recorder.add(AttributeRecordable(
    group="env/light_intensity",
    prim_path="/World/Lights/key_light",
    attribute_name="intensity",
))
recorder.open_session()
```

`CameraRecordable` captures the cameraâs world pose plus its USD intrinsics (focal length, horizontal and vertical aperture, clipping range) every frame; resolution is stored once in the session manifest. On replay the same channel re-authors the recorded camera trajectory into the anonymous sublayer, so any Replicator render product attached to the camera prim picks it up without extra wiring.

`AttributeRecordable` captures a single USD attribute on a prim per frame. Use it for environment state that is not a pose (light intensity, material parameter, custom authored attributes, and so on).

Third-party extensions can also add channels to every session opened from the UI window by registering a session injector with `register_session_injector` â this is the same mechanism `install_teleop_session_injector` uses to contribute teleop controller, aim-pose, and head-pose channels.

## Teleop profiles

A teleop profile is a single YAML file that captures the complete state of every panel in the Teleop window. Use the **Profiles** panel at the top of the Teleop window to save, load, and delete profiles. Built-in profiles ship with the extension under `source/extensions/isaacsim.replicator.teleop/data/teleop_profiles/`; point the **Dir** field at a custom folder to manage your own profiles alongside the built-in ones.

When loaded, a profile applies every section in order: session globals first, then each controller panel. If the referenced prims exist on the current stage, the controllers resolve and are ready to **Enable** immediately. If the stage does not match (different robot or missing prims), the UI fields are still populated and the unresolved paths are reported in the status line.

### Built-in profiles

The extension ships four built-in profiles that pair each locomotion workflow (VR-origin or robot-base) with a solo and a bimanual robot configuration:

| Profile | Matching stage | Configuration |
| --- | --- | --- |
| `floating_xarm.yaml` | `teleop_scenario_floating_xarm.usd` | Solo floating xArm gripper (right side); VR-origin locomotion. |
| `floating_xarm_dex3.yaml` | `teleop_scenario_floating_xarm_dex3.usd` | Bimanual floating grippers (xArm left + Dex3 right); VR-origin locomotion. |
| `ik_solo_ur3_xarm.yaml` | `teleop_scenario_solo_ur3_xarm.usd` | Single UR3e arm with xArm gripper (right side); robot-base locomotion. |
| `ik_dual_ur3_xarm_dex3.yaml` | `teleop_scenario_dual_ur3_xarm_dex3.usd` | Bimanual UR3e arms (xArm gripper left + Dex3 right); robot-base locomotion. |

The two bimanual profiles are described in detail below; the solo variants share the same structure with one side disabled and the locomotion target adjusted for the simpler robot.

#### Bimanual floating grippers (VR origin locomotion)

`floating_xarm_dex3.yaml` configures a dual floating-gripper setup. The **Floating Controller** drives each gripper as a free rigid body, and **Locomotion** targets the VR origin marker so that thumbstick input repositions the entire VR workspace.

**Session** â global settings that apply before any controller is configured:

```python
session:
  coordinate_system: isaac_sim       # Z-up coordinate conversion
  tracking_space_enabled: false
  tracking_space_path: ''            # empty = built-in origin marker
  marker_scale: 0.05
  anchor_x: 0.0
  anchor_y: 0.0
  anchor_z: 0.0
  anchor_rotation_mode: fixed
  anchor_smoothing: 1.0
  anchor_fixed_height: true
```

**Floating** â per-side rigid-body controller with PD gains and rotation offsets. Both sides are enabled, each pointing at a different gripper root prim:

```python
floating:
  left:
    enabled: true
    settings:
      prim_path: /World/teleop_xarm_dex3/.../xarm_gripper_rigid_root
      pos_kp: 20.0
      pos_kd: 0.5
      orient_kp: 20.0
      orient_kd: 0.2
      target_rot_x_deg: 180
      target_rot_y_deg: 0
      target_rot_z_deg: 90
  right:
    enabled: true
    settings:
      prim_path: /World/teleop_xarm_dex3/.../dex3_1_r_rigid_root
      pos_kp: 20.0
      pos_kd: 0.5
      orient_kp: 20.0
      orient_kd: 0.2
      target_rot_x_deg: -90
      target_rot_y_deg: 0
      target_rot_z_deg: 90
```

**IK** â neither side is enabled because the grippers are floating rigid bodies rather than articulations. The section is still present with defaults so that loading the profile resets any prior IK configuration.

**Grasp** â maps each side to a gripper articulation prim and a built-in grasp config. `builtin://` paths resolve to YAML files shipped with the extension:

```python
grasp:
  left:
    enabled: true
    prim_path: /World/teleop_xarm_dex3/.../xarm_gripper
    config_path: builtin://xarm_grasp
  right:
    enabled: true
    prim_path: /World/teleop_xarm_dex3/.../dex3_1_r
    config_path: builtin://dex3_grasp
```

**Locomotion** â drives the built-in tracking-space origin so that thumbstick input moves the entire teleop workspace (VR-origin workflow):

```python
locomotion:
  enabled: true
  settings:
    prim_path: /Teleop/Markers/TrackingOrigin
    linear_step: 0.003333333333333333
    angular_step: 0.003333333333333333
```

#### Dual-arm IK (robot-base locomotion)

`ik_dual_ur3_xarm_dex3.yaml` configures a dual UR3e arm setup where each arm is driven by the **PINK** IK solver. **Locomotion** targets the robotâs root prim so that thumbstick input moves the entire robot base.

**IK** â both sides are enabled with the PINK solver. Each side points at a different UR3e arm within the dual-arm assembly. The `ee_rot_*` offsets align each end effectorâs local frame with the VR controller pointing direction. The PINK solver does not use a Jacobian-inversion method; for the Position-based and Velocity-based solvers, add `method: damped-least-squares | pseudoinverse | transpose | singular-value-decomposition` to the sideâs settings.

```python
ik:
  left:
    enabled: true
    settings:
      robot_path: /World/teleop_dual_ur3_xarm_dex3/dual_arm/left_arm_ur3e_xarm/ur3e
      ee_link: wrist_3_link
      solver: pink
      gain: 5.0
      vr_target_filter: 0.0
      max_joint_step: 0.0
      pink_qp_solver: osqp
      pink_task_gain: 0.5
      pink_posture_cost: 0.001
      pink_lm_damping: 1.0
      ee_rot_x_deg: 180
      ee_rot_y_deg: 0
      ee_rot_z_deg: 90
  right:
    enabled: true
    settings:
      robot_path: /World/teleop_dual_ur3_xarm_dex3/dual_arm/right_arm_ur3e_dex3/ur3e
      ee_link: wrist_3_link
      solver: pink
      gain: 5.0
      vr_target_filter: 0.0
      max_joint_step: 0.0
      pink_qp_solver: daqp
      pink_task_gain: 0.5
      pink_posture_cost: 0.001
      pink_lm_damping: 1.0
      ee_rot_x_deg: 180
      ee_rot_y_deg: 0
      ee_rot_z_deg: -180
```

**Floating** â disabled because the arms are articulations controlled by IK.

**Grasp** â same gripper mapping as the floating profile, with each side pointing at the corresponding gripper articulation.

**Locomotion** â drives the robot root prim so that thumbstick input moves the dual-arm assembly as a whole (robot-base workflow). **Carry Tracking Space** can be toggled to co-move the VR origin with the robot:

```python
locomotion:
  enabled: true
  settings:
    prim_path: /World/teleop_dual_ur3_xarm_dex3
    linear_step: 0.003333333333333333
    angular_step: 0.003333333333333333
```

## Built-in scenario stages

Each [built-in profile](#isaac-sim-app-tutorial-replicator-teleop-profiles) pairs with a matching stage on the Isaac Sim assets server. Open the stage on the Kit timeline, load the profile from the **Profiles** panel, and every controller resolves immediately and is ready to **Enable**.

All four scenario stages live under the same path on the assets server:

```python
http://omniverse-content-production.s3-us-west-2.amazonaws.com
/Assets/Isaac/6.0/Isaac/Samples/Replicator/Teleop/
```

| Scenario | Stage filename |
| --- | --- |
| Floating, solo (right xArm) | `teleop_scenario_floating_xarm.usd` |
| Floating, bimanual (xArm left + Dex3 right) | `teleop_scenario_floating_xarm_dex3.usd` |
| IK, solo (xArm on UR3e, right side) | `teleop_scenario_solo_ur3_xarm.usd` |
| IK, bimanual (xArm left + Dex3 right on dual UR3e) | `teleop_scenario_dual_ur3_xarm_dex3.usd` |

## Workflow walkthrough

This section expands the [quick start](#isaac-sim-app-tutorial-replicator-teleop-quickstart) into the full workflow: configuring from a profile, connecting in VR or debug mode, operating each controller, and recording and replaying an episode. To capture data, open an Episode Recorder session before pressing **Play**.

### Configure with a built-in profile

1. Open **Tools** > **Replicator** > **Teleop**.
2. Open one of the [built-in scenario stages](#isaac-sim-app-tutorial-replicator-teleop-test-stages) above.
3. In the **Profiles** panel, the **Dir** field defaults to the built-in profile directory. Pick the profile that matches the stage from the dropdown and click **Load**. The **Floating Controller**, **IK Controller**, **Grasp Controller**, and **Locomotion** panels are configured against the loaded stage and their **Enable** buttons become available.
4. Click **Validate** to confirm the status line reports `0 error(s), 0 warning(s)`. Unresolved prim paths are listed in the console.

To configure controllers manually for a custom robot, work through each panel as described in the [UI window overview](#isaac-sim-app-tutorial-replicator-teleop-ui). The lifecycle is the same for every controller: enter the prim path, click **Apply**, tune as needed, and click **Enable**.

### Connect to VR

1. Confirm the CloudXR runtime is running (`python -m isaacteleop.cloudxr`) and the headset web client is connected.
2. Expand **Session** and click **Connect**. The status turns green (**Connected - markers active**) and four frame markers appear under `/Teleop/Markers/TrackingOrigin`.
3. Move the VR controllers. The **Left** and **Right** markers track in real time.

If **Connect** fails the status stays red. The most common cause is that the CloudXR process has stopped or the headset has disconnected; restart both and click **Connect** again.

### Operate without VR (debug mode)

Use debug mode when no headset is available, when iterating on tuning, or when running headless. Debug mode and VR mode are mutually exclusive â disconnect VR before enabling debug, and uncheck **Debug Tracking** before clicking **Connect**.

1. Expand **Session** > **Debug** and check **Debug Tracking**. Frame markers appear in the viewport, the **Connect** button is disabled, and the **L Grasp**, **R Grasp**, **Slide X**, **Slide Y**, **Turn**, **Up**, **Down**, and **Carry Origin** controls become live.
2. Drag the **Left**, **Right**, or **Head** marker in the viewport to set its pose; drag the **TrackingOrigin** parent to move all four markers together. The marker hierarchy mirrors a real VR tracking space.

### Operate the robot

Press **Play** on the Kit timeline. Each enabled controller transitions to **Active**. The mapping between input and controller is:

| Controller | VR input | Debug input |
| --- | --- | --- |
| **Floating** / **IK** | Move the controller; the rigid body or end effector tracks the pose. | Drag the **Left** or **Right** frame marker. |
| **Grasp** | Squeeze the trigger (0 = open, 1 = closed). | Move the **L Grasp** or **R Grasp** slider. |
| **Locomotion** (slide) | Push the left thumbstick (forward, back, lateral); right face buttons **A** / **B** drive Z down / up. | Move the **Slide X** / **Slide Y** sliders; hold **Up** / **Down**. |
| **Locomotion** (turn) | Push the right thumbstick left or right. | Move the **Turn** slider. |
| **Locomotion** (carry tracking space) | Press the left primary face button (**X** on Meta) to toggle. | Click the **Carry Origin** toggle. |

Gains, rotation offsets, and step sliders are live-editable during **Play**. Save the tuned state to a profile via **Profiles > Save** when finished. Press **Stop** to deactivate every controller.

To run only one side, configure the side you want and click **Clear** on the other; the cleared side ignores its VR controller / marker.

### Record an episode

The Episode Recorder window captures simulation state and (when a `TeleopManager` is alive) teleop input channels. See [Record and replay](#isaac-sim-app-tutorial-replicator-teleop-episode-recorder) for the full UI reference.

1. Open **Tools** > **Replicator** > **Episode Recorder**. Keep the Teleop window open so the session injector remains active.
2. Set **USD Root** to `/World`, click **Discover**, and tick the targets to record (the robot, any tracked Xforms).
3. Optional â click **Export Scene** once to write `stage_snapshot.usd` next to the HDF5 output. Replays on a different machine can use this snapshot as a portable stage.
4. Click **Open Session**. The configuration controls lock and the filename appears below the buttons.
5. Press **Play** on the timeline. With **Auto-start recording on timeline Play** checked (the default), the status turns green with `Recording episode #1`. Operate the robot. Press **Stop** to end the episode. Repeat for additional episodes.
6. To toggle recording manually from VR, press the left-**Y** button on the Meta Quest controller. Each rising edge starts or ends an episode.
7. Click **Close Session** when done.

### Replay an episode

1. Expand the **Replay** sub-section in the Episode Recorder window.
2. Click **Latest** to fill in the most recent HDF5 file in the **Output Dir**, then click **Load**. The **Episode** dropdown lists every episode with its frame count and `success` flag.
3. Select an episode and click the play glyph in the transport row. The Kit timeline seeks to each frameâs recorded `sim_time`. Every prim moves through its recorded trajectory; teleop controllers stay dormant.
4. Use the pause and step-backward / step-forward glyphs to scrub. Uncheck **Seek timeline** to leave the Kit timeline alone (useful when the stage has no authored animation).
5. Click the stop glyph to revert the stage to its pre-replay pose. The HDF5 stays loaded so a fresh replay can start immediately.

For replay to work, every prim path recorded in the HDF5 must exist on the loaded stage. If the original stage is unavailable, open the `stage_snapshot.usd` written by **Export Scene**.

## Synthetic data generation from recorded episodes

The UI replay covered in [Record and replay](#isaac-sim-app-tutorial-replicator-teleop-episode-recorder) is a quick visual preview driven by the Kit timeline. For offline synthetic data generation, drive `EpisodeReplayer` frame by frame and call `rep.orchestrator.step_async` after each `apply_frame`. This detaches recording time from rendering time, so an expensive writer or DLSS mode can run per frame without slowing teleop and without time drift.

### Prerequisites

* An HDF5 session produced by the [Episode Recorder window](#isaac-sim-app-tutorial-replicator-teleop-episode-recorder) (or any `EpisodeRecorder` subclass).
* A USD stage to replay against. Every prim path in the HDF5 must resolve on this stage. Point `STAGE_URL` at the assets-server path of the original scene, or at an exported snapshot â click **Export Scene** in the Episode Recorder window or call `export_stage_snapshot` from a script to produce `stage_snapshot.usd` next to the HDF5.
* Isaac Sim running. A VR or CloudXR connection is not required for replay.

### What the script does

The script opens `STAGE_URL` (resolved through `get_assets_root_path`), resolves the cameras listed in `CAMERA_PATHS` (falling back to a default camera if none resolve), attaches a `BasicWriter` (RGB PNGs) to the camera render products, and iterates every recorded frame â calling `rep.orchestrator.step` (or `step_async` in the Script Editor variant) after each `step_frame`. Outputs land under `_out_teleop_replay/basic/` next to the current working directory.

Before running either variant below, edit `HDF5_PATH` and `STAGE_URL` at the top of the script to point at your recorded session and its matching USD stage.

Standalone Application

The example can be run as a standalone application using the following commands in the terminal (on Windows use `python.bat` instead of `python.sh`):

```python
./python.sh standalone_examples/api/isaacsim.replicator.teleop/sdg_teleop_replay.py
```

Full Standalone Script

```python
import os

from isaacsim import SimulationApp

simulation_app = SimulationApp(launch_config={"headless": False})

import carb.settings
import omni.kit.app
import omni.replicator.core as rep
import omni.usd
from isaacsim.core.utils.extensions import enable_extension

# Enable the teleop extension before importing modules it owns and before resolving its data path.
# It also transitively pulls in `isaacsim.replicator.episode_recorder`, which is not part of the base kit.
enable_extension("isaacsim.replicator.teleop")

from isaacsim.replicator.episode_recorder import EpisodeReplayer
from isaacsim.storage.native import get_assets_root_path
from pxr import UsdGeom

# Resolve the bundled golden HDF5 episode shipped with the isaacsim.replicator.teleop extension tests.
_TELEOP_EXT_PATH = (
    omni.kit.app.get_app().get_extension_manager().get_extension_path_by_module("isaacsim.replicator.teleop")
)

# Path to the USD stage to replay against; every prim path in the HDF5 must resolve on this stage.
STAGE_URL = "/Isaac/Samples/Replicator/Teleop/teleop_scenario_floating_xarm_dex3.usd"
HDF5_PATH = os.path.join(
    _TELEOP_EXT_PATH,
    "isaacsim",
    "replicator",
    "teleop",
    "tests",
    "data",
    "_episode_recorder",
    "episode_floating_xarm_dex3.hdf5",
)
CAMERA_PATHS = [
    "/World/teleop_xarm_dex3/gripper_origin_xform/xarm_gripper_root_xform/xarm_gripper/xarm_gripper_base_link/xarm_view_cam",
    "/World/teleop_xarm_dex3/gripper_origin_xform/dex3_1_r_root_xform/dex3_1_r/right_hand_palm_link/dex3_view_cam",
]
EPISODE_INDEX = 0
RESOLUTION = (512, 512)
NUM_CAPTURES = 10  # Number of frames to capture, evenly distributed across the episode

def run_example():
    print("[TeleopReplay] Starting replay example")
    if not HDF5_PATH:
        print("[TeleopReplay] HDF5 path not provided, exiting")
        return
    if not os.path.isfile(HDF5_PATH):
        print(f"[TeleopReplay] HDF5 session file does not exist: '{HDF5_PATH}', exiting")
        return
    print(f"[TeleopReplay] HDF5 session: {HDF5_PATH}")

    # Load the authored USD stage so every prim path in the HDF5 resolves.
    assets_root_path = get_assets_root_path()
    if assets_root_path is None:
        print("[TeleopReplay] Could not find Isaac Sim assets folder, exiting")
        return
    stage_path = assets_root_path + STAGE_URL
    print(f"[TeleopReplay] Opening stage: {stage_path}")
    omni.usd.get_context().open_stage(stage_path)
    print("[TeleopReplay] Stage opened")

    # Drive writers manually via rep.orchestrator.step, not via timeline play.
    rep.orchestrator.set_capture_on_play(False)

    # Set DLSS to Quality mode (2) for best SDG results (Options: 0 (Performance), 1 (Balanced), 2 (Quality), 3 (Auto)
    carb.settings.get_settings().set("rtx/post/dlss/execMode", 2)

    # Resolve CAMERA_PATHS to UsdGeom.Camera prims; fall back to a default (5,5,5)
    # camera looking at the origin when CAMERA_PATHS is empty or none resolve.
    stage = omni.usd.get_context().get_stage()
    valid_camera_paths: list[str] = []
    for path in CAMERA_PATHS:
        prim = stage.GetPrimAtPath(path) if path else None
        if prim is None or not prim.IsValid():
            print(f"[TeleopReplay] Camera path '{path}' not found in stage, skipping")
            continue
        if not prim.IsA(UsdGeom.Camera):
            print(f"[TeleopReplay] Prim at '{path}' is not a UsdGeom.Camera (type={prim.GetTypeName()}), skipping")
            continue
        valid_camera_paths.append(path)

    render_products = []
    if valid_camera_paths:
        print(f"[TeleopReplay] Using {len(valid_camera_paths)} scene camera(s): {valid_camera_paths}")
        for i, cam_path in enumerate(valid_camera_paths):
            render_products.append(rep.create.render_product(cam_path, RESOLUTION, name=f"ReplayRP_{i}"))
    else:
        if CAMERA_PATHS:
            print(
                "[TeleopReplay] No valid scene cameras found in CAMERA_PATHS, falling back to default (5,5,5) camera."
            )
        cam = rep.functional.create.camera(position=(5, 5, 5), look_at=(0, 0, 0), name="ReplayCamera")
        render_products.append(rep.create.render_product(cam, RESOLUTION, name="ReplayRP"))
    print(f"[TeleopReplay] Created {len(render_products)} render product(s) at resolution {RESOLUTION}")

    # BasicWriter for RGB PNGs writing straight into the output directory.
    out_dir = os.path.join(os.getcwd(), "_out_sdg_teleop_replay")
    print(f"[TeleopReplay] Output directory: {out_dir}")

    basic_backend = rep.backends.get("DiskBackend")
    basic_backend.initialize(output_dir=out_dir)
    basic_writer = rep.writers.get("BasicWriter")
    basic_writer.initialize(backend=basic_backend, rgb=True)
    basic_writer.attach(render_products)
    print(f"[TeleopReplay] BasicWriter attached -> {out_dir}")

    # Prepare the episode and capture one RGB frame per recorded frame.
    print(f"[TeleopReplay] Preparing episode {EPISODE_INDEX}")
    try:
        replayer = EpisodeReplayer(HDF5_PATH)
        # Start replay with seek_timeline=True to match recorded sim_time, then pause to manually step and capture.
        replayer.start_replay(episode=EPISODE_INDEX, seek_timeline=True)
        replayer.pause_replay()
    except Exception as exc:
        print(f"[TeleopReplay] Could not start replay for episode {EPISODE_INDEX} from '{HDF5_PATH}': {exc}, exiting")
        return
    num_frames = replayer.num_frames(EPISODE_INDEX)
    if num_frames <= 0:
        print(f"[TeleopReplay] Episode {EPISODE_INDEX} has no frames in '{HDF5_PATH}', exiting")
        replayer.close()
        return
    # Replay every frame so the user can watch the full episode, but only trigger a writer capture
    # on NUM_CAPTURES indices evenly distributed across the episode (e.g. every 10% for NUM_CAPTURES=10).
    num_captures = min(NUM_CAPTURES, num_frames)
    capture_set = {(i * num_frames) // num_captures for i in range(num_captures)}
    print(f"[TeleopReplay] Replaying episode {EPISODE_INDEX}: capturing {len(capture_set)} of {num_frames} frames")

    capture_count = 0
    for f in range(num_frames):
        if f > 0:
            replayer.step_frame(1)
        if f in capture_set:
            rep.orchestrator.step(delta_time=0.0, pause_timeline=False)
            capture_count += 1
            print(f"[TeleopReplay] Captured {capture_count}/{len(capture_set)} (frame {f + 1}/{num_frames})")
        else:
            simulation_app.update()

    # Wait for the data to be written to disk and clean up resources.
    print("[TeleopReplay] Waiting for writers to flush...")
    rep.orchestrator.wait_until_complete()
    basic_writer.detach()
    for rp in render_products:
        rp.destroy()
    replayer.close()
    print(f"[TeleopReplay] Done. Output: {out_dir}")

# Run the example
run_example()
```

Script Editor

Paste the snippet below into the **Script Editor** (`Window > Script Editor`).

Full Script Editor Script

```python
import asyncio
import os

import carb.settings
import omni.kit.app
import omni.replicator.core as rep
import omni.usd
from isaacsim.core.utils.extensions import enable_extension

# Enable the teleop extension before importing modules it owns and before resolving its data path.
# It also transitively pulls in `isaacsim.replicator.episode_recorder`, which is not part of the base kit.
enable_extension("isaacsim.replicator.teleop")

from isaacsim.replicator.episode_recorder import EpisodeReplayer
from isaacsim.storage.native import get_assets_root_path_async
from pxr import UsdGeom

# Resolve the bundled golden HDF5 episode shipped with the isaacsim.replicator.teleop extension tests.
_TELEOP_EXT_PATH = (
    omni.kit.app.get_app().get_extension_manager().get_extension_path_by_module("isaacsim.replicator.teleop")
)

# Path to the USD stage to replay against; every prim path in the HDF5 must resolve on this stage.
STAGE_URL = "/Isaac/Samples/Replicator/Teleop/teleop_scenario_floating_xarm_dex3.usd"
HDF5_PATH = os.path.join(
    _TELEOP_EXT_PATH,
    "isaacsim",
    "replicator",
    "teleop",
    "tests",
    "data",
    "_episode_recorder",
    "episode_floating_xarm_dex3.hdf5",
)
CAMERA_PATHS = [
    "/World/teleop_xarm_dex3/gripper_origin_xform/xarm_gripper_root_xform/xarm_gripper/xarm_gripper_base_link/xarm_view_cam",
    "/World/teleop_xarm_dex3/gripper_origin_xform/dex3_1_r_root_xform/dex3_1_r/right_hand_palm_link/dex3_view_cam",
]
EPISODE_INDEX = 0
RESOLUTION = (512, 512)
NUM_CAPTURES = 10  # Number of frames to capture, evenly distributed across the episode

async def run_example_async():
    print("[TeleopReplay] Starting replay example")
    if not HDF5_PATH:
        print("[TeleopReplay] HDF5 path not provided, exiting")
        return
    if not os.path.isfile(HDF5_PATH):
        print(f"[TeleopReplay] HDF5 session file does not exist: '{HDF5_PATH}', exiting")
        return
    print(f"[TeleopReplay] HDF5 session: {HDF5_PATH}")

    # Load the authored USD stage so every prim path in the HDF5 resolves.
    assets_root_path = await get_assets_root_path_async()
    if assets_root_path is None:
        print("[TeleopReplay] Could not find Isaac Sim assets folder, exiting")
        return
    stage_path = assets_root_path + STAGE_URL
    print(f"[TeleopReplay] Opening stage: {stage_path}")
    await omni.usd.get_context().open_stage_async(stage_path)
    print("[TeleopReplay] Stage opened")

    # Drive writers manually via rep.orchestrator.step, not via timeline play.
    rep.orchestrator.set_capture_on_play(False)

    # Set DLSS to Quality mode (2) for best SDG results (Options: 0 (Performance), 1 (Balanced), 2 (Quality), 3 (Auto)
    carb.settings.get_settings().set("rtx/post/dlss/execMode", 2)

    # Create a default camera if no valid cameras are found in CAMERA_PATHS
    stage = omni.usd.get_context().get_stage()
    valid_camera_paths: list[str] = []
    for path in CAMERA_PATHS:
        prim = stage.GetPrimAtPath(path) if path else None
        if prim is None or not prim.IsValid():
            print(f"[TeleopReplay] Camera path '{path}' not found in stage, skipping")
            continue
        if not prim.IsA(UsdGeom.Camera):
            print(f"[TeleopReplay] Prim at '{path}' is not a UsdGeom.Camera (type={prim.GetTypeName()}), skipping")
            continue
        valid_camera_paths.append(path)

    render_products = []
    if valid_camera_paths:
        print(f"[TeleopReplay] Using {len(valid_camera_paths)} scene camera(s): {valid_camera_paths}")
        for i, cam_path in enumerate(valid_camera_paths):
            render_products.append(rep.create.render_product(cam_path, RESOLUTION, name=f"ReplayRP_{i}"))
    else:
        if CAMERA_PATHS:
            print(
                "[TeleopReplay] No valid scene cameras found in CAMERA_PATHS, falling back to default (5,5,5) camera."
            )
        cam = rep.functional.create.camera(position=(5, 5, 5), look_at=(0, 0, 0), name="ReplayCamera")
        render_products.append(rep.create.render_product(cam, RESOLUTION, name="ReplayRP"))
    print(f"[TeleopReplay] Created {len(render_products)} render product(s) at resolution {RESOLUTION}")

    # BasicWriter for RGB PNGs writing straight into the output directory.
    out_dir = os.path.join(os.getcwd(), "_out_sdg_teleop_replay")
    print(f"[TeleopReplay] Output directory: {out_dir}")

    basic_backend = rep.backends.get("DiskBackend")
    basic_backend.initialize(output_dir=out_dir)
    basic_writer = rep.writers.get("BasicWriter")
    basic_writer.initialize(backend=basic_backend, rgb=True)
    basic_writer.attach(render_products)
    print(f"[TeleopReplay] BasicWriter attached -> {out_dir}")

    # Prepare the episode and capture one RGB frame per recorded frame.
    print(f"[TeleopReplay] Preparing episode {EPISODE_INDEX}")
    try:
        replayer = EpisodeReplayer(HDF5_PATH)
        # Start replay with seek_timeline=True to match recorded sim_time, then pause to manually step and capture.
        replayer.start_replay(episode=EPISODE_INDEX, seek_timeline=True)
        replayer.pause_replay()
    except Exception as exc:
        print(f"[TeleopReplay] Could not start replay for episode {EPISODE_INDEX} from '{HDF5_PATH}': {exc}, exiting")
        return
    num_frames = replayer.num_frames(EPISODE_INDEX)
    if num_frames <= 0:
        print(f"[TeleopReplay] Episode {EPISODE_INDEX} has no frames in '{HDF5_PATH}', exiting")
        replayer.close()
        return
    # Replay every frame so the user can watch the full episode, but only trigger a writer capture
    # on NUM_CAPTURES indices evenly distributed across the episode (e.g. every 10% for NUM_CAPTURES=10).
    num_captures = min(NUM_CAPTURES, num_frames)
    capture_set = {(i * num_frames) // num_captures for i in range(num_captures)}
    print(f"[TeleopReplay] Replaying episode {EPISODE_INDEX}: capturing {len(capture_set)} of {num_frames} frames")

    app = omni.kit.app.get_app()
    capture_count = 0
    for f in range(num_frames):
        if f > 0:
            replayer.step_frame(1)
        if f in capture_set:
            await rep.orchestrator.step_async(delta_time=0.0, pause_timeline=False)
            capture_count += 1
            print(f"[TeleopReplay] Captured {capture_count}/{len(capture_set)} (frame {f + 1}/{num_frames})")
        else:
            await app.next_update_async()

    # Wait for the data to be written to disk and clean up resources.
    print("[TeleopReplay] Waiting for writers to flush...")
    await rep.orchestrator.wait_until_complete_async()
    basic_writer.detach()
    for rp in render_products:
        rp.destroy()
    replayer.close()
    print(f"[TeleopReplay] Done. Output: {out_dir}")

# Run the example
asyncio.ensure_future(run_example_async())
```

Adapt the script to your pipeline by swapping or adding Replicator writers (depth, semantic segmentation, instance segmentation, normals, motion vectors, Cosmos video, and so on) or by inserting randomizers between `step_frame` and `rep.orchestrator.step` to produce scene variants per recorded trajectory.

On this page

* [Learning objectives](#learning-objectives)
* [Getting started](#getting-started)
  + [Prerequisites](#prerequisites)
  + [Start CloudXR and connect the headset](#start-cloudxr-and-connect-the-headset)
  + [Running modes](#running-modes)
  + [Open the Teleop window](#open-the-teleop-window)
* [Quick start](#quick-start)
* [Overview](#overview)
* [UI window overview](#ui-window-overview)
  + [Profiles](#profiles)
  + [Session](#session)
    - [Connection](#connection)
    - [Frame Markers](#frame-markers)
    - [XR Anchor](#xr-anchor)
    - [Debug](#debug)
  + [Floating Controller](#floating-controller)
  + [IK Controller](#ik-controller)
    - [Articulation and end effector](#articulation-and-end-effector)
    - [Solver selection](#solver-selection)
    - [Rotation offset and tuning](#rotation-offset-and-tuning)
    - [PINK-specific tuning](#pink-specific-tuning)
    - [Enable and status](#enable-and-status)
  + [Grasp Controller](#grasp-controller)
    - [Config file format](#config-file-format)
  + [Locomotion](#locomotion)
* [Record and replay (Episode Recorder)](#record-and-replay-episode-recorder)
  + [Targets and output](#targets-and-output)
  + [Session and episode control](#session-and-episode-control)
  + [VR recording button](#vr-recording-button)
  + [Replay](#replay)
  + [HDF5 file layout](#hdf5-file-layout)
  + [Recorded data vs. replayed data](#recorded-data-vs-replayed-data)
  + [Programmatic recordables (cameras, attributes)](#programmatic-recordables-cameras-attributes)
* [Teleop profiles](#teleop-profiles)
  + [Built-in profiles](#built-in-profiles)
    - [Bimanual floating grippers (VR origin locomotion)](#bimanual-floating-grippers-vr-origin-locomotion)
    - [Dual-arm IK (robot-base locomotion)](#dual-arm-ik-robot-base-locomotion)
* [Built-in scenario stages](#built-in-scenario-stages)
* [Workflow walkthrough](#workflow-walkthrough)
  + [Configure with a built-in profile](#configure-with-a-built-in-profile)
  + [Connect to VR](#connect-to-vr)
  + [Operate without VR (debug mode)](#operate-without-vr-debug-mode)
  + [Operate the robot](#operate-the-robot)
  + [Record an episode](#record-an-episode)
  + [Replay an episode](#replay-an-episode)
* [Synthetic data generation from recorded episodes](#synthetic-data-generation-from-recorded-episodes)
  + [Prerequisites](#id1)
  + [What the script does](#what-the-script-does)

---

### AMR Navigation

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/replicator_tutorials/tutorial_replicator_amr_navigation.html

* [Synthetic Data Generation](../synthetic_data_generation/index.html)
* [Perception Data Generation (Replicator)](index.html)
* Randomization in Simulation â AMR Navigation

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Randomization in Simulation â AMR Navigation

Example of using Isaac Sim and Replicator to capture synthetic data from simulated environments (AMR Navigation).

## Learning Objectives

The goal of this tutorial is to demonstrate how to setup an Isaac Sim simulation scenario together with the [omni.replicator](https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator.html "(in Omniverse Extensions)") extension to capture synthetic data using diverse randomization techniques.

In this tutorial you:

* Implement scene randomizations using USD / Isaac Sim APIs:

  > + Randomize poses of assets in the scene
  > + Switch between different background environments
* Collect synthetic data at specific simulation events with Replicator
* Create and destroy render products on the fly to improve runtime performance
* Create and destroy Replicator capture graphs within the same simulation instance

### Prerequisites

* Familiarity with USD / Isaac Sim APIs for scene creation and manipulation.
* Familiarity with [omni.replicator](https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator.html "(in Omniverse Extensions)") and its [writers](https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator/writer_examples.html "(in Omniverse Extensions)").
* Basic understanding of [OmniGraph](https://docs.omniverse.nvidia.com/extensions/latest/ext_omnigraph.html "(in Omniverse Extensions)") for the navigation implementation.
* Running simulations as [Standalone Applications](../introduction/workflows.html#standalone-application) or via the [Script Editor](../development_tools/omniverse_script_editor.html#script-editor).

## Scenario

This tutorial uses the Nova Carter robot equipped with an [OmniGraph](https://docs.omniverse.nvidia.com/extensions/latest/ext_omnigraph.html "(in Omniverse Extensions)") navigation stack, notably without collision avoidance features. The navigation stack constantly drives the robot towards a designated Xform target (`<..>/targetXform`), positioned at the location of the randomized objects of interest. As the robot comes in the proximity of the object of interest, a synthetic data generation (SDG) pipeline is triggered to capture data from its two main camera sensors. After the data is captured the objects of interest are re-randomized and the simulation continues. After a certain number of frames (`env_interval`) the background environment is changed as well. After `num_frames` the application terminates.

The `use_temp_rp` flag is used to provide an option to use temporary render products to improve the runtime performance. This speeds up the simulation by only using the render products when capturing the data, thus avoiding the overhead of rendering the sensor views when not capturing data.

The scenario uses the left and right camera sensors of Nova Carter (`<..>/stereo_cam_<left/right>_sensor_frame/camera_sensor_<left/right>`) to collect **LdrColor** (rgb) [annotator](https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator/annotators_details.html "(in Omniverse Extensions)") data using Replicator. By default, the data is written to `<working_dir>/_out_nav_sdg_demo` and runs for `num_frames=9` iterations.

Furthermore, it changes the background environment every `env_interval=3` captured frames. By default the tutorial cycles through `DEFAULT_ENV_URLS`; an entry of `None` creates a generic environment under `/Environment` using a Replicator dome light and a collider-enabled plane instead of loading a USD environment. The `use_temp_rp` flag can be used to optimize performance by disabling the sensor render products during simulation and temporarily enabling them during data capture.

The following image provides an illustration of the resulting data from the various environments.

## Implementation

The following section provides an overview and explanation of the implementation and examples on how to run the demo.

Standalone Application

To run the example as a standalone application, use the following command to execute the provided script. The script also accepts several optional arguments to customize its behavior (on Windows use `python.bat` instead of `python.sh`):

```python
./python.sh standalone_examples/replicator/amr_navigation.py
```

Arguments include:

* `--use_temp_rp` flag to use temporary render products (default: False)
* `--num_frames` the number of frames to be captured (default: 9)
* `--env_interval` the capture interval at which the background environment is changed (default: 3)
* `--env_urls` replaces `DEFAULT_ENV_URLS` entirely. Use `None` for the generic environment

For example, to run the application with all the arguments:

```python
./python.sh standalone_examples/replicator/amr_navigation.py --use_temp_rp --num_frames 9 --env_interval 3
```

Standalone Script

```python
"""Generate synthetic data from an AMR navigating to random locations."""

from isaacsim import SimulationApp

simulation_app = SimulationApp(launch_config={"headless": False})

import argparse
import builtins
import os
import random
from itertools import cycle

import carb.eventdispatcher
import carb.settings
import omni.client
import omni.replicator.core as rep
import omni.timeline
import omni.usd
import omni.usd.commands
from isaacsim.core.utils.stage import create_new_stage
from isaacsim.storage.native import get_assets_root_path
from pxr import Gf, UsdGeom

DEFAULT_ENV_URLS = [
    "/Isaac/Environments/Grid/default_environment.usd",
    "/Isaac/Environments/Simple_Warehouse/warehouse.usd",
    "/Isaac/Environments/Grid/gridroom_black.usd",
    None,
]

def _parse_env_url_arg(env_url: str) -> str | None:
    """Parse CLI environment arguments, where None/null selects the generic environment."""
    return None if env_url.lower() in {"none", "null"} else env_url

parser = argparse.ArgumentParser()
parser.add_argument("--num_frames", type=int, default=9, help="The number of frames to capture")
parser.add_argument("--env_interval", type=int, default=3, help="Interval at which to change the environments")
parser.add_argument(
    "--env_urls",
    nargs="+",
    type=_parse_env_url_arg,
    default=None,
    help="Replace DEFAULT_ENV_URLS entirely. Use None for the generic environment.",
)
parser.add_argument("--use_temp_rp", action="store_true", help="Create and destroy render products for each SDG frame")
args, unknown = parser.parse_known_args()

class NavSDGDemo:
    """Demonstration of synthetic data generation using an AMR navigating towards a target."""

    CARTER_URL = "/Isaac/Samples/Replicator/OmniGraph/nova_carter_nav_only.usd"
    DOLLY_URL = "/Isaac/Props/Dolly/dolly.usd"
    PROPS_URL = "/Isaac/Props/YCB/Axis_Aligned_Physics"
    LEFT_CAMERA_REL_PATH = "sensors/front_hawk/left/camera_left"
    RIGHT_CAMERA_REL_PATH = "sensors/front_hawk/right/camera_right"
    ENVIRONMENT_SCOPE_PATH = "/Environment"

    def __init__(self) -> None:
        """Initialize the navigation SDG demo with default values."""
        self._carter_chassis = None
        self._carter_nav_target = None
        self._dolly = None
        self._dolly_light = None
        self._props = []
        self._cycled_env_urls = None
        self._env_interval = 1
        self._timeline = None
        self._timeline_sub = None
        self._stage_event_sub = None
        self._stage = None
        self._trigger_distance = 2.0
        self._num_frames = 0
        self._frame_counter = 0
        self._writer = None
        self._out_dir = None
        self._render_products = []
        self._use_temp_rp = False
        self._in_running_state = False

    def start(
        self,
        num_frames: int = 10,
        out_dir: str | None = None,
        env_urls: list[str | None] | None = None,
        env_interval: int = 3,
        use_temp_rp: bool = False,
        seed: int | None = None,
    ) -> None:
        """Start the SDG demo with the given configuration."""
        print(f"[SDG] Starting")
        if seed is not None:
            rep.set_global_seed(seed)
            random.seed(seed)
        selected_env_urls = env_urls if env_urls is not None else DEFAULT_ENV_URLS
        self._num_frames = num_frames
        self._out_dir = out_dir if out_dir is not None else os.path.join(os.getcwd(), "_out_nav_sdg_demo")
        self._cycled_env_urls = cycle(selected_env_urls)
        self._env_interval = env_interval
        self._use_temp_rp = use_temp_rp
        self._frame_counter = 0
        self._trigger_distance = 2.0
        self._load_env()
        self._randomize_dolly_pose()
        self._randomize_dolly_light()
        self._randomize_prop_poses()
        self._setup_sdg()
        self._timeline = omni.timeline.get_timeline_interface()
        self._timeline.play()
        self._timeline_sub = carb.eventdispatcher.get_eventdispatcher().observe_event(
            event_name=omni.timeline.GLOBAL_EVENT_CURRENT_TIME_TICKED,
            on_event=self._on_timeline_event,
            observer_name="amr_navigation.NavSDGDemo._on_timeline_event",
        )
        self._stage_event_sub = carb.eventdispatcher.get_eventdispatcher().observe_event(
            event_name=omni.usd.get_context().stage_event_name(omni.usd.StageEventType.CLOSING),
            on_event=self._on_stage_closing_event,
            observer_name="amr_navigation.NavSDGDemo._on_stage_closing_event",
        )
        self._in_running_state = True

    def clear(self) -> None:
        """Reset all state variables and unsubscribe from events."""
        self._cycled_env_urls = None
        self._carter_chassis = None
        self._carter_nav_target = None
        self._dolly = None
        self._dolly_light = None
        self._timeline = None
        self._frame_counter = 0
        self._stage_event_sub = None
        self._timeline_sub = None
        self._clear_sdg_render_products()
        self._stage = None
        self._in_running_state = False

    def is_running(self) -> bool:
        """Return whether the SDG demo is currently running."""
        return self._in_running_state

    def _is_running_in_script_editor(self) -> bool:
        """Return whether the script is running in the Isaac Sim script editor."""
        return builtins.ISAAC_LAUNCHED_FROM_TERMINAL is True

    def _on_stage_closing_event(self, e: carb.eventdispatcher.Event):
        """Handle stage closing event by clearing state."""
        self.clear()

    def _load_env(self) -> None:
        """Create a new stage and load environment, robot, dolly, light, and props."""
        create_new_stage()
        self._stage = omni.usd.get_context().get_stage()
        assets_root_path = get_assets_root_path()
        rep.functional.physics.create_physics_scene(
            "/PhysicsScene", enableCCD=True, broadphaseType="MBP", enableGPUDynamics=False
        )

        # Environment
        self._load_environment(next(self._cycled_env_urls))

        # Nova Carter
        rep.functional.create.scope(name="NavWorld")
        carter = rep.functional.create.reference(
            position=(0, 0, 0),
            rotation=(0, 0, 0),
            usd_path=assets_root_path + self.CARTER_URL,
            parent="/NavWorld",
            name="CarterNav",
        )

        # Iterate children until targetXform (for navigation target) and chassis_link (for current location) are found
        for child in carter.GetChildren():
            if child.GetName() == "targetXform":
                self._carter_nav_target = child
                break
        for child in carter.GetChildren():
            if child.GetName() == "chassis_link":
                self._carter_chassis = child
                break

        # Dolly
        self._dolly = rep.functional.create.reference(
            position=(0, 0, 0),
            rotation=(0, 0, 0),
            usd_path=assets_root_path + self.DOLLY_URL,
            parent="/NavWorld",
            name="Dolly",
        )

        # # Add colliders to the dolly and its geometry primitives
        for desc_prim in self._dolly.GetChildren():
            if desc_prim.IsA(UsdGeom.Gprim):
                rep.functional.physics.apply_rigid_body(desc_prim)

        # Light
        self._dolly_light = rep.functional.create.sphere_light(
            position=(0, 0, 0),
            intensity=250000,
            radius=0.3,
            color=(1.0, 1.0, 1.0),
            parent="/NavWorld",
            name="DollyLight",
        )

        # Props
        props_urls = []
        props_folder_path = assets_root_path + self.PROPS_URL
        result, entries = omni.client.list(props_folder_path)
        if result != omni.client.Result.OK:
            carb.log_error(f"Could not list assets in path: {props_folder_path}")
            return
        for entry in entries:
            _, ext = os.path.splitext(entry.relative_path)
            if ext == ".usd":
                props_urls.append(f"{props_folder_path}/{entry.relative_path}")

        cycled_props_url = cycle(props_urls)
        for i in range(15):
            prop_url = next(cycled_props_url)
            prop_name = os.path.splitext(os.path.basename(prop_url))[0]
            path = f"/NavWorld/Props/Prop_{prop_name}_{i}"
            prim = self._stage.DefinePrim(path, "Xform")
            prim.GetReferences().AddReference(prop_url)
            self._props.append(prim)

    def _randomize_dolly_pose(self) -> None:
        """Set random dolly position ensuring minimum distance from Carter."""
        min_dist_from_carter = 4
        carter_loc = self._carter_chassis.GetAttribute("xformOp:translate").Get()
        for _ in range(100):
            x, y = random.uniform(-6, 6), random.uniform(-6, 6)
            dist = (Gf.Vec2f(x, y) - Gf.Vec2f(carter_loc[0], carter_loc[1])).GetLength()
            if dist > min_dist_from_carter:
                self._dolly.GetAttribute("xformOp:translate").Set((x, y, 0))
                self._carter_nav_target.GetAttribute("xformOp:translate").Set((x, y, 0))
                break
        self._dolly.GetAttribute("xformOp:rotateXYZ").Set((0, 0, random.uniform(-180, 180)))

    def _randomize_dolly_light(self) -> None:
        """Position light above dolly with random color."""
        dolly_loc = self._dolly.GetAttribute("xformOp:translate").Get()
        self._dolly_light.GetAttribute("xformOp:translate").Set(dolly_loc + (0, 0, 3))
        self._dolly_light.GetAttribute("inputs:color").Set(
            (random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1))
        )

    def _randomize_prop_poses(self) -> None:
        """Stack props above the dolly with random horizontal offsets."""
        spawn_loc = self._dolly.GetAttribute("xformOp:translate").Get()
        spawn_loc[2] = spawn_loc[2] + 0.5
        for prop in self._props:
            prop.GetAttribute("xformOp:translate").Set(spawn_loc + (random.uniform(-1, 1), random.uniform(-1, 1), 0))
            spawn_loc[2] = spawn_loc[2] + 0.2

    def _setup_sdg(self) -> None:
        """Configure SDG settings, camera parameters, writer, and render products."""
        rep.orchestrator.set_capture_on_play(False)

        # Set DLSS to Quality mode (2) for best SDG results , options: 0 (Performance), 1 (Balanced), 2 (Quality), 3 (Auto)
        carb.settings.get_settings().set("rtx/post/dlss/execMode", 2)

        # fStop=0 for well-lit sharp images; tickRate=0 forces autotrigger so the sensor
        # cameras stay in sync with rep.orchestrator.step_async under multi-tick rendering.
        for rel_path in (self.LEFT_CAMERA_REL_PATH, self.RIGHT_CAMERA_REL_PATH):
            camera_prim = self._stage.GetPrimAtPath(self._carter_chassis.GetPath().AppendPath(rel_path))
            camera_prim.GetAttribute("fStop").Set(0.0)
            if camera_prim.HasAttribute("omni:sensor:tickRate"):
                camera_prim.GetAttribute("omni:sensor:tickRate").Set(0.0)

        backend = rep.backends.get("DiskBackend")
        backend.initialize(output_dir=self._out_dir)
        print(f"[SDG] Writing data to: {self._out_dir}")
        self._writer = rep.writers.get("BasicWriter")
        self._writer.initialize(backend=backend, rgb=True)
        self._setup_sdg_render_products()

    def _setup_sdg_render_products(self) -> None:
        """Create and attach render products for left and right cameras."""
        print(f"[SDG] Creating SDG render products")
        left_camera_path = self._carter_chassis.GetPath().AppendPath(self.LEFT_CAMERA_REL_PATH)
        rp_left = rep.create.render_product(
            str(left_camera_path),
            (1024, 1024),
            name="left_sensor",
            force_new=True,
        )
        right_camera_path = self._carter_chassis.GetPath().AppendPath(self.RIGHT_CAMERA_REL_PATH)
        rp_right = rep.create.render_product(
            str(right_camera_path),
            (1024, 1024),
            name="right_sensor",
            force_new=True,
        )
        self._render_products = [rp_left, rp_right]
        # For better performance the render products can be disabled when not in use, and re-enabled only during SDG
        if self._use_temp_rp:
            self._disable_render_products()
        self._writer.attach(self._render_products)

    def _clear_sdg_render_products(self) -> None:
        """Detach writer and destroy all render products."""
        print(f"[SDG] Clearing SDG render products")
        if self._writer:
            self._writer.detach()
        for rp in self._render_products:
            rp.destroy()
        self._render_products.clear()
        if self._stage.GetPrimAtPath("/Replicator"):
            omni.kit.commands.execute("DeletePrimsCommand", paths=["/Replicator"])

    def _enable_render_products(self) -> None:
        """Enable texture updates on all render products."""
        print(f"[SDG] Enabling render products for SDG..")
        for rp in self._render_products:
            rp.hydra_texture.set_updates_enabled(True)

    def _disable_render_products(self) -> None:
        """Disable texture updates on all render products."""
        print(f"[SDG] Disabling render products (enabled only during SDG)..")
        for rp in self._render_products:
            rp.hydra_texture.set_updates_enabled(False)

    def _run_sdg(self) -> None:
        """Execute one SDG capture step synchronously."""
        if self._use_temp_rp:
            self._enable_render_products()
        rep.orchestrator.step(rt_subframes=16)
        if self._use_temp_rp:
            self._disable_render_products()

    async def _run_sdg_async(self) -> None:
        """Execute one SDG capture step asynchronously."""
        if self._use_temp_rp:
            self._enable_render_products()
        await rep.orchestrator.step_async(rt_subframes=16)
        if self._use_temp_rp:
            self._disable_render_products()

    def _load_next_env(self) -> None:
        """Replace current environment with the next one from the cycle."""
        self._load_environment(next(self._cycled_env_urls))

    def _load_environment(self, env_url: str | None) -> None:
        """Load the next environment under a shared scope."""
        if self._stage.GetPrimAtPath(self.ENVIRONMENT_SCOPE_PATH):
            omni.kit.commands.execute("DeletePrimsCommand", paths=[self.ENVIRONMENT_SCOPE_PATH])

        rep.functional.create.scope(name="Environment")
        if env_url:
            assets_root_path = get_assets_root_path()
            rep.functional.create.reference(
                usd_path=assets_root_path + env_url, parent=self.ENVIRONMENT_SCOPE_PATH, name="Scene"
            )
            return

        rep.functional.create.dome_light(intensity=500, parent=self.ENVIRONMENT_SCOPE_PATH, name="DomeLight")
        ground = rep.functional.create.plane(
            parent=self.ENVIRONMENT_SCOPE_PATH, name="GroundPlane", scale=(100, 100, 1)
        )
        rep.functional.physics.apply_collider(ground)

    def _on_sdg_done(self, task) -> None:
        """Callback invoked when async SDG step completes."""
        self._setup_next_frame()

    def _setup_next_frame(self) -> None:
        """Prepare scene for next frame or finish if all frames captured."""
        self._frame_counter += 1
        if self._frame_counter >= self._num_frames:
            print(f"[SDG] Finished")
            # Make sure the data has been written to disk before clearing the state
            if self._is_running_in_script_editor():
                import asyncio

                task = asyncio.ensure_future(rep.orchestrator.wait_until_complete_async())
                task.add_done_callback(lambda t: self.clear())
            else:
                rep.orchestrator.wait_until_complete()
                self.clear()
            return

        self._randomize_dolly_pose()
        self._randomize_dolly_light()
        self._randomize_prop_poses()
        if self._frame_counter % self._env_interval == 0:
            self._load_next_env()
        # Set a new random distance from which to take capture the next frame
        self._trigger_distance = random.uniform(1.75, 2.5)
        self._timeline.play()
        self._timeline_sub = carb.eventdispatcher.get_eventdispatcher().observe_event(
            event_name=omni.timeline.GLOBAL_EVENT_CURRENT_TIME_TICKED,
            on_event=self._on_timeline_event,
            observer_name="amr_navigation.NavSDGDemo._on_timeline_event",
        )

    def _on_timeline_event(self, e: carb.eventdispatcher.Event):
        """Check distance to dolly and trigger SDG capture when close enough."""
        carter_loc = self._carter_chassis.GetAttribute("xformOp:translate").Get()
        dolly_loc = self._dolly.GetAttribute("xformOp:translate").Get()
        dist = (Gf.Vec2f(dolly_loc[0], dolly_loc[1]) - Gf.Vec2f(carter_loc[0], carter_loc[1])).GetLength()
        if dist < self._trigger_distance:
            print(f"[SDG] Starting SDG for frame no. {self._frame_counter}")
            self._timeline.pause()
            if self._is_running_in_script_editor():
                import asyncio

                task = asyncio.ensure_future(self._run_sdg_async())
                task.add_done_callback(self._on_sdg_done)
            else:
                self._run_sdg()
                self._setup_next_frame()

out_dir = os.path.join(os.getcwd(), "_out_nav_sdg_demo", "")
selected_env_urls = args.env_urls if args.env_urls is not None else DEFAULT_ENV_URLS
nav_demo = NavSDGDemo()
nav_demo.start(
    num_frames=args.num_frames,
    out_dir=out_dir,
    env_urls=selected_env_urls,
    env_interval=args.env_interval,
    use_temp_rp=args.use_temp_rp,
    seed=22,
)

while simulation_app.is_running() and nav_demo.is_running():
    simulation_app.update()

simulation_app.close()
```

Script Editor

To run the example from the script editor, the following code must be executed:

Script Editor Script

```python
import asyncio
import builtins
import os
import random
from itertools import cycle

import carb.settings
import omni.client
import omni.kit.app
import omni.replicator.core as rep
import omni.timeline
import omni.usd
import omni.usd.commands
from isaacsim.core.experimental.utils.stage import create_new_stage
from isaacsim.storage.native import get_assets_root_path
from pxr import Gf, UsdGeom

DEFAULT_ENV_URLS = [
    "/Isaac/Environments/Grid/default_environment.usd",
    "/Isaac/Environments/Simple_Warehouse/warehouse.usd",
    "/Isaac/Environments/Grid/gridroom_black.usd",
    None,
]
NUM_FRAMES = 9
ENV_INTERVAL = 3
USE_TEMP_RP = True

class NavSDGDemo:
    """Demonstration of synthetic data generation using an AMR navigating towards a target."""

    CARTER_URL = "/Isaac/Samples/Replicator/OmniGraph/nova_carter_nav_only.usd"
    DOLLY_URL = "/Isaac/Props/Dolly/dolly.usd"
    PROPS_URL = "/Isaac/Props/YCB/Axis_Aligned_Physics"
    LEFT_CAMERA_REL_PATH = "sensors/front_hawk/left/camera_left"
    RIGHT_CAMERA_REL_PATH = "sensors/front_hawk/right/camera_right"
    ENVIRONMENT_SCOPE_PATH = "/Environment"

    def __init__(self) -> None:
        """Initialize the navigation SDG demo with default values."""
        self._carter_chassis = None
        self._carter_nav_target = None
        self._dolly = None
        self._dolly_light = None
        self._props = []
        self._cycled_env_urls = None
        self._env_interval = 1
        self._timeline = None
        self._timeline_sub = None
        self._stage_event_sub = None
        self._stage = None
        self._trigger_distance = 2.0
        self._num_frames = 0
        self._frame_counter = 0
        self._writer = None
        self._out_dir = None
        self._render_products = []
        self._use_temp_rp = False
        self._in_running_state = False
        self._completion_event = None

    async def run_async(
        self,
        num_frames: int = 10,
        out_dir: str | None = None,
        env_urls: list[str | None] | None = None,
        env_interval: int = 3,
        use_temp_rp: bool = False,
        seed: int | None = None,
    ) -> None:
        """Run the SDG demo asynchronously and wait for completion."""
        self._completion_event = asyncio.Event()
        self.start(
            num_frames=num_frames,
            out_dir=out_dir,
            env_urls=env_urls,
            env_interval=env_interval,
            use_temp_rp=use_temp_rp,
            seed=seed,
        )
        await self._completion_event.wait()

    def start(
        self,
        num_frames: int = 10,
        out_dir: str | None = None,
        env_urls: list[str | None] | None = None,
        env_interval: int = 3,
        use_temp_rp: bool = False,
        seed: int | None = None,
    ) -> None:
        """Start the SDG demo with the given configuration."""
        print(f"[SDG] Starting")
        if seed is not None:
            rep.set_global_seed(seed)
            random.seed(seed)
        selected_env_urls = env_urls if env_urls is not None else DEFAULT_ENV_URLS
        self._num_frames = num_frames
        self._out_dir = out_dir if out_dir is not None else os.path.join(os.getcwd(), "_out_nav_sdg_demo")
        self._cycled_env_urls = cycle(selected_env_urls)
        self._env_interval = env_interval
        self._use_temp_rp = use_temp_rp
        self._frame_counter = 0
        self._trigger_distance = 2.0
        self._load_env()
        self._randomize_dolly_pose()
        self._randomize_dolly_light()
        self._randomize_prop_poses()
        self._setup_sdg()
        self._timeline = omni.timeline.get_timeline_interface()
        self._timeline.play()
        self._timeline_sub = self._timeline.get_timeline_event_stream().create_subscription_to_pop_by_type(
            int(omni.timeline.TimelineEventType.CURRENT_TIME_TICKED), self._on_timeline_event
        )
        self._stage_event_sub = (
            omni.usd.get_context()
            .get_stage_event_stream()
            .create_subscription_to_pop_by_type(int(omni.usd.StageEventType.CLOSING), self._on_stage_closing_event)
        )
        self._in_running_state = True

    def clear(self) -> None:
        """Reset all state variables and unsubscribe from events."""
        self._cycled_env_urls = None
        self._carter_chassis = None
        self._carter_nav_target = None
        self._dolly = None
        self._dolly_light = None
        self._timeline = None
        self._frame_counter = 0
        if self._stage_event_sub:
            self._stage_event_sub.unsubscribe()
        self._stage_event_sub = None
        if self._timeline_sub:
            self._timeline_sub.unsubscribe()
        self._timeline_sub = None
        self._clear_sdg_render_products()
        self._stage = None
        self._in_running_state = False
        # Signal completion for async waiters
        if self._completion_event:
            self._completion_event.set()
            self._completion_event = None

    def is_running(self) -> bool:
        """Return whether the SDG demo is currently running."""
        return self._in_running_state

    def _is_running_in_script_editor(self) -> bool:
        """Return whether the script is running in the Isaac Sim script editor."""
        return builtins.ISAAC_LAUNCHED_FROM_TERMINAL is True

    def _on_stage_closing_event(self, e: carb.events.IEvent) -> None:
        """Handle stage closing event by clearing state."""
        self.clear()

    def _load_env(self) -> None:
        """Create a new stage and load environment, robot, dolly, light, and props."""
        create_new_stage()
        self._stage = omni.usd.get_context().get_stage()
        rep.functional.physics.create_physics_scene(
            "/PhysicsScene", enableCCD=True, broadphaseType="MBP", enableGPUDynamics=False
        )

        # Environment
        assets_root_path = get_assets_root_path()
        self._load_environment(next(self._cycled_env_urls))

        # Nova Carter
        rep.functional.create.scope(name="NavWorld")
        carter = rep.functional.create.reference(
            position=(0, 0, 0),
            rotation=(0, 0, 0),
            usd_path=assets_root_path + self.CARTER_URL,
            parent="/NavWorld",
            name="CarterNav",
        )

        # Iterate children until targetXform (for navigation target) and chassis_link (for current location) are found
        for child in carter.GetChildren():
            if child.GetName() == "targetXform":
                self._carter_nav_target = child
                break
        for child in carter.GetChildren():
            if child.GetName() == "chassis_link":
                self._carter_chassis = child
                break

        # Dolly
        self._dolly = rep.functional.create.reference(
            position=(0, 0, 0),
            rotation=(0, 0, 0),
            usd_path=assets_root_path + self.DOLLY_URL,
            parent="/NavWorld",
            name="Dolly",
        )

        # Add colliders to the dolly and its geometry primitives
        for desc_prim in self._dolly.GetChildren():
            if desc_prim.IsA(UsdGeom.Gprim):
                rep.functional.physics.apply_rigid_body(desc_prim)

        # Light
        self._dolly_light = rep.functional.create.sphere_light(
            position=(0, 0, 0),
            intensity=250000,
            radius=0.3,
            color=(1.0, 1.0, 1.0),
            parent="/NavWorld",
            name="DollyLight",
        )

        # Props
        props_urls = []
        props_folder_path = assets_root_path + self.PROPS_URL
        result, entries = omni.client.list(props_folder_path)
        if result != omni.client.Result.OK:
            carb.log_error(f"Could not list assets in path: {props_folder_path}")
            return
        for entry in entries:
            _, ext = os.path.splitext(entry.relative_path)
            if ext == ".usd":
                props_urls.append(f"{props_folder_path}/{entry.relative_path}")

        cycled_props_url = cycle(props_urls)
        for i in range(15):
            prop_url = next(cycled_props_url)
            prop_name = os.path.splitext(os.path.basename(prop_url))[0]
            path = f"/NavWorld/Props/Prop_{prop_name}_{i}"
            prim = self._stage.DefinePrim(path, "Xform")
            prim.GetReferences().AddReference(prop_url)
            self._props.append(prim)

    def _randomize_dolly_pose(self) -> None:
        """Set random dolly position ensuring minimum distance from Carter."""
        min_dist_from_carter = 4
        carter_loc = self._carter_chassis.GetAttribute("xformOp:translate").Get()
        for _ in range(100):
            x, y = random.uniform(-6, 6), random.uniform(-6, 6)
            dist = (Gf.Vec2f(x, y) - Gf.Vec2f(carter_loc[0], carter_loc[1])).GetLength()
            if dist > min_dist_from_carter:
                self._dolly.GetAttribute("xformOp:translate").Set((x, y, 0))
                self._carter_nav_target.GetAttribute("xformOp:translate").Set((x, y, 0))
                break
        self._dolly.GetAttribute("xformOp:rotateXYZ").Set((0, 0, random.uniform(-180, 180)))

    def _randomize_dolly_light(self) -> None:
        """Position light above dolly with random color."""
        dolly_loc = self._dolly.GetAttribute("xformOp:translate").Get()
        self._dolly_light.GetAttribute("xformOp:translate").Set(dolly_loc + (0, 0, 3))
        self._dolly_light.GetAttribute("inputs:color").Set(
            (random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1))
        )

    def _randomize_prop_poses(self) -> None:
        """Stack props above the dolly with random horizontal offsets."""
        spawn_loc = self._dolly.GetAttribute("xformOp:translate").Get()
        spawn_loc[2] = spawn_loc[2] + 0.5
        for prop in self._props:
            prop.GetAttribute("xformOp:translate").Set(spawn_loc + (random.uniform(-1, 1), random.uniform(-1, 1), 0))
            spawn_loc[2] = spawn_loc[2] + 0.2

    def _setup_sdg(self) -> None:
        """Configure SDG settings, camera parameters, writer, and render products."""
        rep.orchestrator.set_capture_on_play(False)

        # Set DLSS to Quality mode (2) for best SDG results , options: 0 (Performance), 1 (Balanced), 2 (Quality), 3 (Auto)
        carb.settings.get_settings().set("rtx/post/dlss/execMode", 2)

        # fStop=0 for well-lit sharp images; tickRate=0 forces autotrigger so the sensor
        # cameras stay in sync with rep.orchestrator.step_async under multi-tick rendering.
        for rel_path in (self.LEFT_CAMERA_REL_PATH, self.RIGHT_CAMERA_REL_PATH):
            camera_prim = self._stage.GetPrimAtPath(self._carter_chassis.GetPath().AppendPath(rel_path))
            camera_prim.GetAttribute("fStop").Set(0.0)
            if camera_prim.HasAttribute("omni:sensor:tickRate"):
                camera_prim.GetAttribute("omni:sensor:tickRate").Set(0.0)

        backend = rep.backends.get("DiskBackend")
        backend.initialize(output_dir=self._out_dir)
        print(f"[SDG] Writing data to: {self._out_dir}")
        self._writer = rep.writers.get("BasicWriter")
        self._writer.initialize(backend=backend, rgb=True)
        self._setup_sdg_render_products()

    def _setup_sdg_render_products(self) -> None:
        """Create and attach render products for left and right cameras."""
        print(f"[SDG] Creating SDG render products")
        left_camera_path = self._carter_chassis.GetPath().AppendPath(self.LEFT_CAMERA_REL_PATH)
        rp_left = rep.create.render_product(
            str(left_camera_path),
            (1024, 1024),
            name="left_sensor",
            force_new=True,
        )
        right_camera_path = self._carter_chassis.GetPath().AppendPath(self.RIGHT_CAMERA_REL_PATH)
        rp_right = rep.create.render_product(
            str(right_camera_path),
            (1024, 1024),
            name="right_sensor",
            force_new=True,
        )
        self._render_products = [rp_left, rp_right]
        # For better performance the render products can be disabled when not in use, and re-enabled only during SDG
        if self._use_temp_rp:
            self._disable_render_products()
        self._writer.attach(self._render_products)

    def _clear_sdg_render_products(self) -> None:
        """Detach writer and destroy all render products."""
        print(f"[SDG] Clearing SDG render products")
        if self._writer:
            self._writer.detach()
        for rp in self._render_products:
            rp.destroy()
        self._render_products.clear()
        if self._stage.GetPrimAtPath("/Replicator"):
            omni.kit.commands.execute("DeletePrimsCommand", paths=["/Replicator"])

    def _enable_render_products(self) -> None:
        """Enable texture updates on all render products."""
        print(f"[SDG] Enabling render products for SDG..")
        for rp in self._render_products:
            rp.hydra_texture.set_updates_enabled(True)

    def _disable_render_products(self) -> None:
        """Disable texture updates on all render products."""
        print(f"[SDG] Disabling render products (enabled only during SDG)..")
        for rp in self._render_products:
            rp.hydra_texture.set_updates_enabled(False)

    def _run_sdg(self) -> None:
        """Execute one SDG capture step synchronously."""
        if self._use_temp_rp:
            self._enable_render_products()
        rep.orchestrator.step(rt_subframes=16)
        if self._use_temp_rp:
            self._disable_render_products()

    async def _run_sdg_async(self) -> None:
        """Execute one SDG capture step asynchronously."""
        if self._use_temp_rp:
            self._enable_render_products()
        await rep.orchestrator.step_async(rt_subframes=16)
        if self._use_temp_rp:
            self._disable_render_products()

    def _load_next_env(self) -> None:
        """Replace current environment with the next one from the cycle."""
        self._load_environment(next(self._cycled_env_urls))

    def _load_environment(self, env_url: str | None) -> None:
        """Load the next environment under a shared scope."""
        if self._stage.GetPrimAtPath(self.ENVIRONMENT_SCOPE_PATH):
            omni.kit.commands.execute("DeletePrimsCommand", paths=[self.ENVIRONMENT_SCOPE_PATH])

        rep.functional.create.scope(name="Environment")
        if env_url:
            assets_root_path = get_assets_root_path()
            rep.functional.create.reference(
                usd_path=assets_root_path + env_url, parent=self.ENVIRONMENT_SCOPE_PATH, name="Scene"
            )
            return

        rep.functional.create.dome_light(intensity=500, parent=self.ENVIRONMENT_SCOPE_PATH, name="DomeLight")
        ground = rep.functional.create.plane(
            parent=self.ENVIRONMENT_SCOPE_PATH, name="GroundPlane", scale=(100, 100, 1)
        )
        rep.functional.physics.apply_collider(ground)

    def _on_sdg_done(self, task) -> None:
        """Callback invoked when async SDG step completes."""
        self._setup_next_frame()

    def _setup_next_frame(self) -> None:
        """Prepare scene for next frame or finish if all frames captured."""
        self._frame_counter += 1
        if self._frame_counter >= self._num_frames:
            print(f"[SDG] Finished")
            if self._is_running_in_script_editor():
                task = asyncio.ensure_future(rep.orchestrator.wait_until_complete_async())
                task.add_done_callback(lambda t: self.clear())
            else:
                rep.orchestrator.wait_until_complete()
                self.clear()
            return

        self._randomize_dolly_pose()
        self._randomize_dolly_light()
        self._randomize_prop_poses()
        if self._frame_counter % self._env_interval == 0:
            self._load_next_env()
        # Set a new random distance from which to capture the next frame
        self._trigger_distance = random.uniform(1.75, 2.5)
        self._timeline.play()
        self._timeline_sub = self._timeline.get_timeline_event_stream().create_subscription_to_pop_by_type(
            int(omni.timeline.TimelineEventType.CURRENT_TIME_TICKED), self._on_timeline_event
        )

    def _on_timeline_event(self, e: carb.events.IEvent) -> None:
        """Check distance to dolly and trigger SDG capture when close enough."""
        carter_loc = self._carter_chassis.GetAttribute("xformOp:translate").Get()
        dolly_loc = self._dolly.GetAttribute("xformOp:translate").Get()
        dist = (Gf.Vec2f(dolly_loc[0], dolly_loc[1]) - Gf.Vec2f(carter_loc[0], carter_loc[1])).GetLength()
        if dist < self._trigger_distance:
            print(f"[SDG] Starting SDG for frame no. {self._frame_counter}")
            self._timeline.pause()
            self._timeline_sub.unsubscribe()
            if self._is_running_in_script_editor():
                task = asyncio.ensure_future(self._run_sdg_async())
                task.add_done_callback(self._on_sdg_done)
            else:
                self._run_sdg()
                self._setup_next_frame()

out_dir = os.path.join(os.getcwd(), "_out_nav_sdg_demo", "")
nav_demo = NavSDGDemo()
asyncio.ensure_future(
    nav_demo.run_async(
        num_frames=NUM_FRAMES,
        out_dir=out_dir,
        env_urls=DEFAULT_ENV_URLS,
        env_interval=ENV_INTERVAL,
        use_temp_rp=USE_TEMP_RP,
        seed=22,
    )
)
```

Code Explanation

This tab describes each section of the larger sample script that is used for this tutorial. By reviewing the descriptions and code snippets you can understand how the script is working and how you might customize it for your use.

The following snippets can be used to load and start the demo scene. Each of the snippets has an explanation that can be expanded. The snippets and explanations are collapsed so that you can control opening them as you read and work through the tutorial for yourself.

**Running the AMR Navigation SDG Demo**

The following snippet is from the end of the code sample, it runs for the given `num_frames` and changes the background environment every `env_interval`. The output is written to the given `out_dir path`. The `use_temp_rp` parameter can be used to optimize performance by creating render products only for the frames when the data is captured. When `--env_urls` is provided it replaces `DEFAULT_ENV_URLS` entirely; otherwise the demo uses the default environment cycle.

The start method loads and runs the demo with the specified parameters, while clear halts the demo and clears any active subscribers and render products. You can use `is_running` to verify whether the demo is still running.

Running the NavSDGDemo Python Script Example

```python
out_dir = os.path.join(os.getcwd(), "_out_nav_sdg_demo", "")
selected_env_urls = args.env_urls if args.env_urls is not None else DEFAULT_ENV_URLS
nav_demo = NavSDGDemo()
nav_demo.start(
    num_frames=args.num_frames,
    out_dir=out_dir,
    env_urls=selected_env_urls,
    env_interval=args.env_interval,
    use_temp_rp=args.use_temp_rp,
    seed=22,
)

while simulation_app.is_running() and nav_demo.is_running():
    simulation_app.update()

simulation_app.close()
```

**NavSDGDemo Class and Attributes**

The demo script is wrapped in its own class called `NavSDGDemo`.

NavSDGDemo Class Snippet

```python
class NavSDGDemo:
    """Demonstration of synthetic data generation using an AMR navigating towards a target."""

    CARTER_URL = "/Isaac/Samples/Replicator/OmniGraph/nova_carter_nav_only.usd"
    DOLLY_URL = "/Isaac/Props/Dolly/dolly.usd"
    PROPS_URL = "/Isaac/Props/YCB/Axis_Aligned_Physics"
    LEFT_CAMERA_REL_PATH = "sensors/front_hawk/left/camera_left"
    RIGHT_CAMERA_REL_PATH = "sensors/front_hawk/right/camera_right"
    ENVIRONMENT_SCOPE_PATH = "/Environment"

    def __init__(self) -> None:
        """Initialize the navigation SDG demo with default values."""
        self._carter_chassis = None
        self._carter_nav_target = None
        self._dolly = None
        self._dolly_light = None
        self._props = []
        self._cycled_env_urls = None
        self._env_interval = 1
        self._timeline = None
        self._timeline_sub = None
        self._stage_event_sub = None
        self._stage = None
        self._trigger_distance = 2.0
        self._num_frames = 0
        self._frame_counter = 0
        self._writer = None
        self._out_dir = None
        self._render_products = []
        self._use_temp_rp = False
        self._in_running_state = False
```

The attributes of this class include:

* `self._carter_chassis` and `self._carter_nav_target` prims are used to track Nova Carter and its target Xform in the navigation graph
* `self._dolly` is used as the target for the navigation target of Nova Carter and to track the distance to Nova Carter
* `self._dolly_light` randomized light placed above the dolly each captured frame
* `self._props` list of prop prims to place and simulate above the dolly each captured frame
* `self._cycled_env_urls` the paths for the background environments to cycle through, including `None` for the generic Replicator-built environment
* `self._env_interval` is used to determine after how many frames to change the background environment
* `self._timeline` is used to control (play/pause) the simulation timeline between frame captures
* `self._timeline_sub` is the subscriber to the timeline ticks. It is used as the feedback loop to trigger the synthetic data generation
* `self._stage_event_sub` is a subscriber to stage closing events used to clear the demo in case a new stage is opened
* `self._stage` is used to access the active stage in order to create, access, and delete prims of interest
* `self._trigger_distance` is used to determine the distance between Nova Carter and the dolly at which the synthetic data generation should trigger, the value is randomized after each capture
* `self._num_frames` and `self._frame_counter` are used to track and stop the demo after the given number of frames
* `self._writer` is the writer used to write the synthetic data to disk
* `self._render_products` are the two render products attached to the left and right camera sensors of Nova Carter, the writer is attached to these to access data from the annotators
* `self._use_temp_rp` is a flag, which when set to `True`, causes the demo to disable render products when not capturing. Otherwise the render products are always enabled
* `self._in_running_state` indicates the running state of the demo used to track whether the demo has finished or not
* The class constant `ENVIRONMENT_SCOPE_PATH` keeps both referenced USD environments and the generic fallback environment under the same `/Environment` scope, which makes switching between them consistent.

**Workflow and Start Function**

The workflowâs main functions are `start` and the `_on_timeline_event` callback functions. `start` resolves the selected environment list, creates a new environment with:

* navigation specific physics scene
* Nova Carter
* navigation graph with the target Xform
* dolly
* randomization light
* props to drop around the dolly

If `env_urls` is `None`, `start` uses `DEFAULT_ENV_URLS`. Environment changes are routed through `_load_environment`, which always rebuilds the shared `/Environment` scope. When the selected environment entry is `None`, the demo creates a generic environment with `rep.functional.create.dome_light`, `rep.functional.create.plane`, and `rep.functional.physics.apply_collider`.

It also creates the timeline subscriber with `_on_timeline_event` as the callback function triggered with each timeline tick. The `_on_timeline_event` function checks if Nova Carter is close enough to the dolly, if so it pauses the simulation, unsubscribes the timeline callback, and triggers the synthetic data generation (SDG). Depending on whether the demo is running in the script editor or as a standalone application it runs the SDG synchronously or asynchronously.

Workflow Snippet

```python
def start(
    self,
    num_frames: int = 10,
    out_dir: str | None = None,
    env_urls: list[str | None] | None = None,
    env_interval: int = 3,
    use_temp_rp: bool = False,
    seed: int | None = None,
) -> None:
    """Start the SDG demo with the given configuration."""
    print(f"[SDG] Starting")
    if seed is not None:
        rep.set_global_seed(seed)
        random.seed(seed)
    selected_env_urls = env_urls if env_urls is not None else DEFAULT_ENV_URLS
    self._num_frames = num_frames
    self._out_dir = out_dir if out_dir is not None else os.path.join(os.getcwd(), "_out_nav_sdg_demo")
    self._cycled_env_urls = cycle(selected_env_urls)
    self._env_interval = env_interval
    self._use_temp_rp = use_temp_rp
    self._frame_counter = 0
    self._trigger_distance = 2.0
    self._load_env()
    self._randomize_dolly_pose()
    self._randomize_dolly_light()
    self._randomize_prop_poses()
    self._setup_sdg()
    self._timeline = omni.timeline.get_timeline_interface()
    self._timeline.play()
    self._timeline_sub = carb.eventdispatcher.get_eventdispatcher().observe_event(
        event_name=omni.timeline.GLOBAL_EVENT_CURRENT_TIME_TICKED,
        on_event=self._on_timeline_event,
        observer_name="amr_navigation.NavSDGDemo._on_timeline_event",
    )
    self._stage_event_sub = carb.eventdispatcher.get_eventdispatcher().observe_event(
        event_name=omni.usd.get_context().stage_event_name(omni.usd.StageEventType.CLOSING),
        on_event=self._on_stage_closing_event,
        observer_name="amr_navigation.NavSDGDemo._on_stage_closing_event",
    )
    self._in_running_state = True
```

```python
def _on_timeline_event(self, e: carb.eventdispatcher.Event):
    """Check distance to dolly and trigger SDG capture when close enough."""
    carter_loc = self._carter_chassis.GetAttribute("xformOp:translate").Get()
    dolly_loc = self._dolly.GetAttribute("xformOp:translate").Get()
    dist = (Gf.Vec2f(dolly_loc[0], dolly_loc[1]) - Gf.Vec2f(carter_loc[0], carter_loc[1])).GetLength()
    if dist < self._trigger_distance:
        print(f"[SDG] Starting SDG for frame no. {self._frame_counter}")
        self._timeline.pause()
        if self._is_running_in_script_editor():
            import asyncio

            task = asyncio.ensure_future(self._run_sdg_async())
            task.add_done_callback(self._on_sdg_done)
        else:
            self._run_sdg()
            self._setup_next_frame()
```

**Randomizations Explanation**

To randomize the environment before the synthetic data capture, the following functions are used:

* `_randomize_dolly_pose`: places the dolly at a random pose with a given minimum distance from Nova Carter. After such a pose is found, the navigation target is placed at the dollyâs position.
* `_randomize_dolly_light`: places the dolly light above the dolly with a new random color.
* `_randomize_prop_poses`: places the props above the dolly at random locations, which eventually starts to fall after the simulation starts.

Randomizations Snippet

```python
def _randomize_dolly_pose(self) -> None:
    """Set random dolly position ensuring minimum distance from Carter."""
    min_dist_from_carter = 4
    carter_loc = self._carter_chassis.GetAttribute("xformOp:translate").Get()
    for _ in range(100):
        x, y = random.uniform(-6, 6), random.uniform(-6, 6)
        dist = (Gf.Vec2f(x, y) - Gf.Vec2f(carter_loc[0], carter_loc[1])).GetLength()
        if dist > min_dist_from_carter:
            self._dolly.GetAttribute("xformOp:translate").Set((x, y, 0))
            self._carter_nav_target.GetAttribute("xformOp:translate").Set((x, y, 0))
            break
    self._dolly.GetAttribute("xformOp:rotateXYZ").Set((0, 0, random.uniform(-180, 180)))

def _randomize_dolly_light(self) -> None:
    """Position light above dolly with random color."""
    dolly_loc = self._dolly.GetAttribute("xformOp:translate").Get()
    self._dolly_light.GetAttribute("xformOp:translate").Set(dolly_loc + (0, 0, 3))
    self._dolly_light.GetAttribute("inputs:color").Set(
        (random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1))
    )

def _randomize_prop_poses(self) -> None:
    """Stack props above the dolly with random horizontal offsets."""
    spawn_loc = self._dolly.GetAttribute("xformOp:translate").Get()
    spawn_loc[2] = spawn_loc[2] + 0.5
    for prop in self._props:
        prop.GetAttribute("xformOp:translate").Set(spawn_loc + (random.uniform(-1, 1), random.uniform(-1, 1), 0))
        spawn_loc[2] = spawn_loc[2] + 0.2
```

**Synthetic Data Generation (SDG) Explanation**

When executing the synthetic data generation (SDG) pipeline the `rep.orchestrator.step` function is called to initiate the data capture and the execution of the writerâs write function.

Depending on the value of the `use_temp_rp` flag, the sensorâs render products are handled differently:

* If set to `True`, the render products are only enabled during data capture.
* `False` is the default. It renders the render products and processes every frame.

Note

`_setup_sdg` sets `omni:sensor:tickRate = 0` (autotrigger) on the Nova Carter
`front_hawk` left and right cameras. Under multi-tick rendering, the per-sensor
tick scheduler can fall out of sync with `rep.orchestrator.step_async` and the
writer may receive no frames; forcing autotrigger keeps these sensor cameras in
step with the orchestrator. This workaround is expected to be removed in a future
release. See [Multi-Tick Rendering](../sensors/isaacsim_sensors_multitick_rendering.html#isaac-sim-sensors-multitick-rendering) for details on the
`omni:sensor:tickRate` attribute.

Synthetic Data Generation (SDG) Snippet

```python
def _run_sdg(self) -> None:
    """Execute one SDG capture step synchronously."""
    if self._use_temp_rp:
        self._enable_render_products()
    rep.orchestrator.step(rt_subframes=16)
    if self._use_temp_rp:
        self._disable_render_products()
```

**Next Frame Explanation**

After the synthetic data generation (SDG) completes, the `_setup_next_frame` function prepares the simulation for the next frame. This involves incrementing the frame counter (`self._frame_counter`), randomizing the dolly, dolly light, and props. Then changing the background environment, if the `env_interval` is reached. Because environment loading now goes through the shared `/Environment` scope, switching between referenced USD environments and the generic `None` environment uses the same update path. Additionally the timeline and its subscriber are re-started.

If the `_num_frames` is reached the demo makes sure the the writer backend is finished with writing the data to disk (`rep.orchestrator.wait_until_complete`) and clears the demo.

Next Frame Snippet

```python
def _setup_next_frame(self) -> None:
    """Prepare scene for next frame or finish if all frames captured."""
    self._frame_counter += 1
    if self._frame_counter >= self._num_frames:
        print(f"[SDG] Finished")
        # Make sure the data has been written to disk before clearing the state
        if self._is_running_in_script_editor():
            import asyncio

            task = asyncio.ensure_future(rep.orchestrator.wait_until_complete_async())
            task.add_done_callback(lambda t: self.clear())
        else:
            rep.orchestrator.wait_until_complete()
            self.clear()
        return

    self._randomize_dolly_pose()
    self._randomize_dolly_light()
    self._randomize_prop_poses()
    if self._frame_counter % self._env_interval == 0:
        self._load_next_env()
    # Set a new random distance from which to take capture the next frame
    self._trigger_distance = random.uniform(1.75, 2.5)
    self._timeline.play()
    self._timeline_sub = carb.eventdispatcher.get_eventdispatcher().observe_event(
        event_name=omni.timeline.GLOBAL_EVENT_CURRENT_TIME_TICKED,
        on_event=self._on_timeline_event,
        observer_name="amr_navigation.NavSDGDemo._on_timeline_event",
    )
```

On this page

* [Learning Objectives](#learning-objectives)
  + [Prerequisites](#prerequisites)
* [Scenario](#scenario)
* [Implementation](#implementation)

---

### UR10 Palletizing

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/replicator_tutorials/tutorial_replicator_ur10_palletizing.html

* [Synthetic Data Generation](../synthetic_data_generation/index.html)
* [Perception Data Generation (Replicator)](index.html)
* Randomization in Simulation â UR10 Palletizing

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Randomization in Simulation â UR10 Palletizing

Example of using Isaac Sim and Replicator to capture synthetic data from simulated environments (UR10 palletizing).

## Learning Objectives

The goal of this tutorial is to provide an example on how to extend an existing Isaac Sim simulation to trigger a synthetic data generation (SDG) pipeline to randomize the environment and collect synthetic data at specific simulation events using the [omni.replicator](https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator.html "(in Omniverse Extensions)") extension.

Note

The tutorial makes sure that the SDG pipeline does not change the outcome of the running simulation and cleans up its changes after each capture.

This tutorial teaches you to:

* Collect synthetic data at specific simulation events with Replicator:

  > + Using annotators to collect the data and manually write it to disk
  > + Using writers to implicitly write the data to disk
* Setup various Replicator randomization graphs to:

  > + Randomize lights around the object of interest
  > + Randomize materials and textures of objects of interest running at different rates
* Create and destroy Replicator randomization and capture graphs within the same simulation instance
* Switch between different rendering modes on the fly
* Create and destroy render products on the fly to improve runtime performance

## Prerequisites

* Familiarity with the [omni.replicator](https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator.html "(in Omniverse Extensions)") extension and its [annotators](https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator/annotators_details.html "(in Omniverse Extensions)") and [writers](https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator/writer_examples.html "(in Omniverse Extensions)").
* Familiarity with Replicator [randomizers](https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator/randomizer_details.html "(in Omniverse Extensions)") and [OmniGraph](https://docs.omniverse.nvidia.com/extensions/latest/ext_omnigraph.html "(in Omniverse Extensions)") for a better understanding of the randomization pipeline.
* Executing code from the [Script Editor](../development_tools/omniverse_script_editor.html#script-editor).

## Scenario

For this tutorial, you build on top of the UR10 palletizing demo scene, which is programmatically loaded and started by the provided script.

The demo scene depicts a simple palletizing scenario where the UR10 robot picks up bins from a conveyor belt and places them on a pallet.

For bins that are flipped, the robot flips them right side up with a helper object before placing them on the pallet.

In the above images, data collected from the actions in the left side image belong to the **bin flip scenario**.

In the above images, data collected from the right side image belongs to the **bin on pallet scenario**.

For each frame in this scenario, the camera pose is iterated through in a predefined sequence, while the custom lightsâ parameters are randomized. Data is generated for each manipulated bin in the palletizing demo scene.

The events for which synthetic data are collected are:

* When the bin is placed on the flipping helper object
* When the bin is placed on the pallet (or on another bin that is already on the pallet)

Below, in each captured frame the bin colors are randomized. At a lower randomization rate, the camera poses and pallet textures are also randomized.

The [annotator](https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator/annotators_details.html "(in Omniverse Extensions)") data collected by the scenario includes the **LdrColor** (rgb) and **instance segmentation**.

The data is directly accessed from the annotators and saved to disk using custom helper functions.

The data is written to disk using a built-in Replicator [writer](https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator/writer_examples.html "(in Omniverse Extensions)") (`BasicWriter`).

## Implementation

Script Editor

The example can be run from UI using the [Script Editor](../development_tools/omniverse_script_editor.html#script-editor):

Full Script Editor Script

```python
import asyncio
import json
import os

import carb.settings
import omni
import omni.kit.app
import omni.kit.commands
import omni.replicator.core as rep
import omni.timeline
import omni.usd
from isaacsim.storage.native import get_assets_root_path
from omni.physx import get_physx_scene_query_interface
from omni.replicator.core.functional import write_image
from pxr import Usd, UsdGeom, UsdShade

DEFAULT_NUM_CAPTURES = 4  # Number bins to capture
DEFAULT_BIN_FLIP_FRAMES = 2  # Number of frames to capture for the bin flip scenario
DEFAULT_PALLET_FRAMES = 2  # Number of frames to capture for the pallet scenario
MAX_BINS = 36  # Maximum number of bins available in the scene

class PalletizingSDGDemo:
    BINS_FOLDER_PATH = "/World/Ur10Table/bins"
    FLIP_HELPER_PATH = "/World/Ur10Table/pallet_holder"
    PALLET_PRIM_MESH_PATH = "/World/Ur10Table/pallet/Xform/Mesh_015"

    def __init__(self):
        # There are 36 bins in total
        self._bin_counter = 0
        self._num_captures = MAX_BINS
        self._bin_flip_frames = DEFAULT_BIN_FLIP_FRAMES
        self._pallet_frames = DEFAULT_PALLET_FRAMES
        self._stage = None
        self._active_bin = None

        # Cleanup in case the user closes the stage
        self._stage_event_sub = None

        # Simulation state flags
        self._in_running_state = False
        self._bin_flip_scenario_done = False

        # Used to pause/resume the simulation
        self._timeline = None

        # Used to actively track the active bins surroundings (e.g., in contact with pallet)
        self._timeline_sub = None
        self._overlap_extent = None

        # SDG
        self._rep_camera = None
        self._output_dir = os.path.join(os.getcwd(), "_out_palletizing_sdg_demo")
        print(f"[PalletizingSDGDemo] Output directory: {self._output_dir}")

    def start(self, num_captures, bin_flip_frames, pallet_frames):
        self._num_captures = num_captures if 1 <= num_captures <= 36 else 36
        self._bin_flip_frames = bin_flip_frames
        self._pallet_frames = pallet_frames
        if self._init():
            self._start()

    def is_running(self):
        return self._in_running_state

    def _init(self):
        self._stage = omni.usd.get_context().get_stage()
        self._active_bin = self._stage.GetPrimAtPath(f"{self.BINS_FOLDER_PATH}/bin_{self._bin_counter}")

        if not self._active_bin:
            print("[PalletizingSDGDemo] Could not find bin, make sure the palletizing demo is loaded..")
            return False

        bb_cache = UsdGeom.BBoxCache(Usd.TimeCode.Default(), includedPurposes=[UsdGeom.Tokens.default_])
        half_ext = bb_cache.ComputeLocalBound(self._active_bin).GetRange().GetSize() * 0.5
        self._overlap_extent = carb.Float3(half_ext[0], half_ext[1], half_ext[2] * 1.1)

        self._timeline = omni.timeline.get_timeline_interface()
        if not self._timeline.is_playing():
            print("[PalletizingSDGDemo] Please start the palletizing demo first..")
            return False

        # Disable capture on play for replicator, data capture will be triggered manually
        rep.orchestrator.set_capture_on_play(False)

        # Set DLSS to Quality mode (2) for best SDG results (Options: 0 (Performance), 1 (Balanced), 2 (Quality), 3 (Auto)
        carb.settings.get_settings().set("rtx/post/dlss/execMode", 2)

        # Clear any previously generated SDG graphs
        if self._stage.GetPrimAtPath("/Replicator"):
            omni.kit.commands.execute("DeletePrimsCommand", paths=["/Replicator"])

        return True

    def _start(self):
        self._timeline_sub = carb.eventdispatcher.get_eventdispatcher().observe_event(
            event_name=omni.timeline.GLOBAL_EVENT_CURRENT_TIME_TICKED,
            on_event=self._on_timeline_event,
            observer_name="test_sdg_ur10_palletizing.PalletizingSDGDemo._on_timeline_event",
        )
        self._stage_event_sub = carb.eventdispatcher.get_eventdispatcher().observe_event(
            event_name=omni.usd.get_context().stage_event_name(omni.usd.StageEventType.CLOSING),
            on_event=self._on_stage_closing_event,
            observer_name="test_sdg_ur10_palletizing.PalletizingSDGDemo._on_stage_closing_event",
        )
        self._in_running_state = True
        print("[PalletizingSDGDemo] Starting the palletizing SDG demo..")

    def clear(self):
        if self._timeline_sub:
            self._timeline_sub.reset()
            self._timeline_sub = None
        if self._stage_event_sub:
            self._stage_event_sub.reset()
            self._stage_event_sub = None
        self._in_running_state = False
        self._bin_counter = 0
        self._active_bin = None
        if self._stage.GetPrimAtPath("/Replicator"):
            omni.kit.commands.execute("DeletePrimsCommand", paths=["/Replicator"])

    def _on_stage_closing_event(self, e: carb.eventdispatcher.Event):
        # Make sure the subscribers are unsubscribed for new stages
        self.clear()

    def _on_timeline_event(self, e: carb.eventdispatcher.Event):
        self._check_bin_overlaps()

    def _check_bin_overlaps(self):
        bin_pose = omni.usd.get_world_transform_matrix(self._active_bin)
        origin = bin_pose.ExtractTranslation()
        quat_gf = bin_pose.ExtractRotation().GetQuaternion()

        any_hit_flag = False
        hit_info = get_physx_scene_query_interface().overlap_box(
            carb.Float3(self._overlap_extent),
            carb.Float3(origin[0], origin[1], origin[2]),
            carb.Float4(
                quat_gf.GetImaginary()[0],
                quat_gf.GetImaginary()[1],
                quat_gf.GetImaginary()[2],
                quat_gf.GetReal(),
            ),
            self._on_overlap_hit,
            any_hit_flag,
        )

    def _on_overlap_hit(self, hit):
        # Skip self-hits
        if hit.rigid_body == str(self._active_bin.GetPrimPath()):
            return True

        # Handle flip scenario (only once per bin)
        if not self._bin_flip_scenario_done and hit.rigid_body.startswith(self.FLIP_HELPER_PATH):
            self._timeline.pause()
            if self._timeline_sub:
                self._timeline_sub.reset()
                self._timeline_sub = None
            asyncio.ensure_future(self._run_bin_flip_scenario())
            return False

        # Handle pallet landing scenario
        is_pallet_hit = hit.rigid_body.startswith(self.PALLET_PRIM_MESH_PATH)
        is_other_bin_hit = hit.rigid_body.startswith(f"{self.BINS_FOLDER_PATH}/bin_")
        if is_pallet_hit or is_other_bin_hit:
            self._timeline.pause()
            if self._timeline_sub:
                self._timeline_sub.reset()
                self._timeline_sub = None
            asyncio.ensure_future(self._run_pallet_scenario())

        return True  # No relevant hit, return True to continue the query

    def _switch_to_pathtracing(self, spp=32, total_spp=32):
        carb.settings.get_settings().set("/rtx/rendermode", "PathTracing")
        carb.settings.get_settings().set("/rtx/pathtracing/spp", spp)
        carb.settings.get_settings().set("/rtx/pathtracing/totalSpp", total_spp)

    def _switch_to_realtime_pathtracing(self):
        carb.settings.get_settings().set("/rtx/rendermode", "RealTimePathTracing")

    async def _run_bin_flip_scenario(self):
        await omni.kit.app.get_app().next_update_async()
        print(f"[PalletizingSDGDemo] Running bin flip scenario for bin {self._bin_counter}..")

        self._switch_to_pathtracing(spp=16, total_spp=32)
        await omni.kit.app.get_app().next_update_async()
        self._create_bin_flip_graph()

        rgb_annot = rep.annotators.get("rgb")
        instance_segmentation_annot = rep.annotators.get("instance_segmentation", init_params={"colorize": True})
        rp = rep.create.render_product(self._rep_camera, (512, 512))
        rgb_annot.attach(rp)
        instance_segmentation_annot.attach(rp)
        out_dir = os.path.join(self._output_dir, f"annot_bin_{self._bin_counter}")
        os.makedirs(out_dir, exist_ok=True)

        print(f"[PalletizingSDGDemo] Starting capturing data for bin flip scenario for bin {self._bin_counter}..")
        for i in range(self._bin_flip_frames):
            print(f"  [PalletizingSDGDemo] Capturing frame {i + 1}/{self._bin_flip_frames}")
            await rep.orchestrator.step_async(rt_subframes=16, delta_time=0.0)

            rgb_data = rgb_annot.get_data()
            rgb_file_path = os.path.join(out_dir, f"rgb_{i}.png")
            write_image(path=rgb_file_path, data=rgb_data)

            instance_segmentation_data = instance_segmentation_annot.get_data()
            instance_segmentation_file_path = os.path.join(out_dir, f"instance_segmentation_{i}.png")
            write_image(path=instance_segmentation_file_path, data=instance_segmentation_data["data"])
            with open(os.path.join(out_dir, f"instance_segmentation_info_{i}.json"), "w") as f:
                json.dump(instance_segmentation_data["info"], f, indent=4)

        # Wait for the data to be written to disk and free up resources after the capture
        await rep.orchestrator.wait_until_complete_async()
        rgb_annot.detach()
        instance_segmentation_annot.detach()
        rp.destroy()

        # Cleanup the generated SDG graph
        if self._stage.GetPrimAtPath("/Replicator"):
            omni.kit.commands.execute("DeletePrimsCommand", paths=["/Replicator"])

        self._switch_to_realtime_pathtracing()

        # Set the flag to indicate that the bin flip scenario is done and the simulation can continue to the next bin
        self._bin_flip_scenario_done = True
        self._timeline_sub = carb.eventdispatcher.get_eventdispatcher().observe_event(
            event_name=omni.timeline.GLOBAL_EVENT_CURRENT_TIME_TICKED,
            on_event=self._on_timeline_event,
            observer_name="test_sdg_ur10_palletizing.PalletizingSDGDemo._on_timeline_event",
        )
        self._timeline.play()

    def _create_bin_flip_graph(self):
        # Create new random lights using the color palette for the color attribute
        color_palette = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]

        def randomize_bin_flip_lights():
            lights = rep.create.light(
                light_type="Sphere",
                temperature=rep.distribution.normal(6500, 2000),
                intensity=rep.distribution.normal(45000, 15000),
                position=rep.distribution.uniform((0.25, 0.25, 0.5), (1, 1, 0.75)),
                scale=rep.distribution.uniform(0.5, 0.8),
                color=rep.distribution.choice(color_palette),
                count=3,
            )
            return lights.node

        rep.randomizer.register(randomize_bin_flip_lights)

        # Move the camera to the given location sequences and look at the predefined location
        camera_positions = [
            (1.96, 0.72, -0.34),
            (1.48, 0.70, 0.90),
            (0.79, -0.86, 0.12),
            (-0.49, 1.47, 0.58),
        ]
        self._rep_camera = rep.create.camera()
        with rep.trigger.on_frame():
            rep.randomizer.randomize_bin_flip_lights()
            with self._rep_camera:
                rep.modify.pose(
                    position=rep.distribution.sequence(camera_positions),
                    look_at=(0.78, 0.72, -0.1),
                )

    async def _run_pallet_scenario(self):
        await omni.kit.app.get_app().next_update_async()
        print(f"[PalletizingSDGDemo] Running pallet scenario for bin {self._bin_counter}..")
        mesh_to_orig_mats = {}
        pallet_mesh = self._stage.GetPrimAtPath(self.PALLET_PRIM_MESH_PATH)
        pallet_orig_mat, _ = UsdShade.MaterialBindingAPI(pallet_mesh).ComputeBoundMaterial()
        mesh_to_orig_mats[pallet_mesh] = pallet_orig_mat
        for i in range(self._bin_counter + 1):
            bin_mesh = self._stage.GetPrimAtPath(f"{self.BINS_FOLDER_PATH}/bin_{i}/Visuals/FOF_Mesh_Magenta_Box")
            bin_orig_mat, _ = UsdShade.MaterialBindingAPI(bin_mesh).ComputeBoundMaterial()
            mesh_to_orig_mats[bin_mesh] = bin_orig_mat

        self._create_bin_and_pallet_graph()

        out_dir = os.path.join(self._output_dir, f"writer_bin_{self._bin_counter}", "")
        backend = rep.backends.get("DiskBackend")
        backend.initialize(output_dir=out_dir)
        writer = rep.WriterRegistry.get("BasicWriter")
        writer.initialize(
            backend=backend,
            rgb=True,
            instance_segmentation=True,
            colorize_instance_segmentation=True,
        )
        rp = rep.create.render_product(self._rep_camera, (512, 512))
        writer.attach(rp)

        print(f"[PalletizingSDGDemo] Starting capturing data for pallet scenario for bin {self._bin_counter}..")
        for i in range(self._pallet_frames):
            print(f"  [PalletizingSDGDemo] Capturing frame {i + 1}/{self._pallet_frames}")
            await rep.orchestrator.step_async(rt_subframes=16, delta_time=0.0)

        # Make sure the backend finishes writing the data before clearing the generated SDG graph
        await rep.orchestrator.wait_until_complete_async()

        # Free up resources after the capture
        writer.detach()
        rp.destroy()

        # Cleanup the generated SDG graph
        print(f"[PalletizingSDGDemo] Restoring {len(mesh_to_orig_mats)} original materials")
        for mesh, mat in mesh_to_orig_mats.items():
            UsdShade.MaterialBindingAPI(mesh).Bind(mat, UsdShade.Tokens.strongerThanDescendants)

        # Cleanup the generated SDG graph
        if self._stage.GetPrimAtPath("/Replicator"):
            omni.kit.commands.execute("DeletePrimsCommand", paths=["/Replicator"])

        # Return in paused state if there are no more bins to capture
        if not self._next_bin():
            return

        # Resume the simulation and continue with the next bin
        self._timeline_sub = carb.eventdispatcher.get_eventdispatcher().observe_event(
            event_name=omni.timeline.GLOBAL_EVENT_CURRENT_TIME_TICKED,
            on_event=self._on_timeline_event,
            observer_name="test_sdg_ur10_palletizing.PalletizingSDGDemo._on_timeline_event",
        )
        self._timeline.play()

    def _create_bin_and_pallet_graph(self):
        # Bin material randomization
        bin_paths = [
            f"{self.BINS_FOLDER_PATH}/bin_{i}/Visuals/FOF_Mesh_Magenta_Box" for i in range(self._bin_counter + 1)
        ]
        bins_node = rep.get.prim_at_path(bin_paths)

        with rep.trigger.on_frame():
            mats = rep.create.material_omnipbr(
                diffuse=rep.distribution.uniform((0.2, 0.1, 0.3), (0.6, 0.6, 0.7)),
                roughness=rep.distribution.choice([0.1, 0.9]),
                count=10,
            )
            with bins_node:
                rep.randomizer.materials(mats)

        # Camera and pallet texture randomization at a slower rate
        assets_root_path = get_assets_root_path()
        texture_paths = [
            assets_root_path + "/NVIDIA/Materials/Base/Wood/Oak/Oak_BaseColor.png",
            assets_root_path + "/NVIDIA/Materials/Base/Wood/Ash/Ash_BaseColor.png",
            assets_root_path + "/NVIDIA/Materials/Base/Wood/Plywood/Plywood_BaseColor.png",
            assets_root_path + "/NVIDIA/Materials/Base/Wood/Timber/Timber_BaseColor.png",
        ]
        pallet_node = rep.get.prim_at_path(self.PALLET_PRIM_MESH_PATH)
        pallet_prim = pallet_node.get_output_prims()["prims"][0]
        pallet_loc = omni.usd.get_world_transform_matrix(pallet_prim).ExtractTranslation()
        self._rep_camera = rep.create.camera()
        with rep.trigger.on_frame(interval=4):
            with pallet_node:
                rep.randomizer.texture(texture_paths, texture_rotate=rep.distribution.uniform(80, 95))
            with self._rep_camera:
                rep.modify.pose(
                    position=rep.distribution.uniform((0, -2, 1), (2, 1, 2)),
                    look_at=(pallet_loc[0], pallet_loc[1], pallet_loc[2]),
                )

    def _next_bin(self):
        self._bin_counter += 1
        if self._bin_counter >= self._num_captures:
            self.clear()
            print("[PalletizingSDGDemo] Palletizing SDG demo finished..")
            return False
        self._active_bin = self._stage.GetPrimAtPath(f"{self.BINS_FOLDER_PATH}/bin_{self._bin_counter}")
        print(f"[PalletizingSDGDemo] Moving to bin {self._bin_counter}..")
        self._bin_flip_scenario_done = False
        return True

async def run_example_async(num_captures, bin_flip_frames, pallet_frames):
    import random

    from isaacsim.cortex.examples.ur10_palletizing.ur10_palletizing import (
        BinStacking,
    )

    # Createa new stage
    await omni.usd.get_context().new_stage_async()

    # Seed for the bin drop stage(if it needs to be flipped or not)
    random.seed(42)

    # Seed for the replicator randomization
    rep.set_global_seed(42)

    # Load the bin stacking stage and start the demo
    bin_staking_sample = BinStacking()
    print(f"[PalletizingSDGDemo] Loading the bin stacking stage..")
    await bin_staking_sample.load_world_async()
    print(f"[PalletizingSDGDemo] Starting bin stacking..")
    await bin_staking_sample.on_event_async()

    # Wait a few frames for the stage to fully load then start the SDG pipeline
    for _ in range(5):
        await omni.kit.app.get_app().next_update_async()

    print(f"[PalletizingSDGDemo] Starting SDG pipeline with {num_captures} bins to capture")
    sdg_demo = PalletizingSDGDemo()
    sdg_demo.start(num_captures, bin_flip_frames, pallet_frames)

    # Wait until the SDG pipeline demo is finished
    while sdg_demo.is_running():
        await omni.kit.app.get_app().next_update_async()
    print("[PalletizingSDGDemo] SDG pipeline finished, pausing the simulation..")
    timeline = omni.timeline.get_timeline_interface()
    timeline.pause()

asyncio.ensure_future(
    run_example_async(
        num_captures=DEFAULT_NUM_CAPTURES, bin_flip_frames=DEFAULT_BIN_FLIP_FRAMES, pallet_frames=DEFAULT_PALLET_FRAMES
    )
)
```

Code Explanation

This tab describes each section of the larger sample script that is used for this tutorial. By reviewing the descriptions and code snippets you can understand how the script is working and how you might customize it for your use.

**Running the UR10 Palletizing Demo Scene**

The following snippet is from the end of the code sample, it loads and starts the default UR10 Palletizing demo scene, followed by the synthetic data generation (SDG) that runs and captures the requested number of iterations (`num_captures`). You can modify NUM\_CAPTURES to run for a different number of frame captures.

Running the Example Snippet

```python
async def run_example_async(num_captures, bin_flip_frames, pallet_frames):
    import random

    from isaacsim.cortex.examples.ur10_palletizing.ur10_palletizing import (
        BinStacking,
    )

    # Create a new stage
    await omni.usd.get_context().new_stage_async()

    # Seed for the bin drop stage (if it needs to be flipped or not)
    random.seed(42)

    # Seed for the replicator randomization
    rep.set_global_seed(42)

    # Load the bin stacking stage and start the demo
    bin_staking_sample = BinStacking()
    print(f"[PalletizingSDGDemo] Loading the bin stacking stage..")
    await bin_staking_sample.load_world_async()
    print(f"[PalletizingSDGDemo] Starting bin stacking..")
    await bin_staking_sample.on_event_async()

    # Wait a few frames for the stage to fully load then start the SDG pipeline
    for _ in range(5):
        await omni.kit.app.get_app().next_update_async()

    print(f"[PalletizingSDGDemo] Starting SDG pipeline with {num_captures} bins to capture")
    sdg_demo = PalletizingSDGDemo()
    sdg_demo.start(num_captures, bin_flip_frames, pallet_frames)

    # Wait until the SDG pipeline demo is finished
    while sdg_demo.is_running():
        await omni.kit.app.get_app().next_update_async()
    print("[PalletizingSDGDemo] SDG pipeline finished, pausing the simulation..")
    timeline = omni.timeline.get_timeline_interface()
    timeline.pause()

asyncio.ensure_future(
    run_example_async(
        num_captures=DEFAULT_NUM_CAPTURES,
        bin_flip_frames=DEFAULT_BIN_FLIP_FRAMES,
        pallet_frames=DEFAULT_PALLET_FRAMES
    )
)
```

**PalletizingSDGDemo Class**

The demo script is wrapped in the `PalletizingSDGDemo` class. It oversees the simulation environment and manages the synthetic data generation.

PalletizingSDGDemo Class Snippet

```python
class PalletizingSDGDemo:
    BINS_FOLDER_PATH = "/World/Ur10Table/bins"
    FLIP_HELPER_PATH = "/World/Ur10Table/pallet_holder"
    PALLET_PRIM_MESH_PATH = "/World/Ur10Table/pallet/Xform/Mesh_015"

    def __init__(self):
        # There are 36 bins in total
        self._bin_counter = 0
        self._num_captures = MAX_BINS
        self._bin_flip_frames = DEFAULT_BIN_FLIP_FRAMES
        self._pallet_frames = DEFAULT_PALLET_FRAMES
        self._stage = None
        self._active_bin = None

        # Cleanup in case the user closes the stage
        self._stage_event_sub = None

        # Simulation state flags
        self._in_running_state = False
        self._bin_flip_scenario_done = False

        # Used to pause/resume the simulation
        self._timeline = None

        # Used to actively track the active bins surroundings (e.g., in contact with pallet)
        self._timeline_sub = None
        self._overlap_extent = None

        # SDG
        self._rep_camera = None
        self._output_dir = os.path.join(os.getcwd(), "_out_palletizing_sdg_demo")
        print(f"[PalletizingSDGDemo] Output directory: {self._output_dir}")
```

The attributes of this class include:

* `self._bin_counter` and `self._num_captures` are used to track the current bin index and the requested number of frames to capture
* `self._stage` is used to access objects of interest in the environment during the simulation
* `self._active_bin` is tracking the current active bin
* `self._stage_event_sub` is a subscriber to stage closing events, it is used to cleanup the demo if the stage is closed
* `self._in_running_state` indicates whether the demo is currently running
* `self._bin_flip_scenario_done` is a flag to mark if the bin flip scenario has been completed, to avoid triggering it again
* `self._timeline` is used to pause and resume the simulation in response to Synthetic Data Generation (SDG) events
* `self._timeline_sub` is a subscriber to timeline events, allowing the monitoring of the simulation state (tracking the active binâs surroundings)
* `self._overlap_extent` represents an extent cache of the bin size, which is used to query for overlaps around the active bin
* `self._rep_camera` points the temporary replicator camera to capture SDG data
* `self._output_dir` is the output directory where the SDG data gets stored

**Start Function**

The `start` function initializes and starts the SDG demo. During initialization (using `self._init()`), it checks whether the UR10 palletizing demo is loaded and running. Additionally, it sets up the `self._stage` and `self._active_bin` attributes. The demo is then started with the `self._start()` function. This function subscribes to timeline events through `self._timeline_sub`, which uses the `self._on_timeline_event` callback function to monitor the simulation state.

Start Function Workflow Snippet

```python
def start(self, num_captures, bin_flip_frames, pallet_frames):
    self._num_captures = num_captures if 1 <= num_captures <= 36 else 36
    self._bin_flip_frames = bin_flip_frames
    self._pallet_frames = pallet_frames
    if self._init():
        self._start()

def is_running(self):
    return self._in_running_state

def _init(self):
    self._stage = omni.usd.get_context().get_stage()
    self._active_bin = self._stage.GetPrimAtPath(f"{self.BINS_FOLDER_PATH}/bin_{self._bin_counter}")

    if not self._active_bin:
        print("[PalletizingSDGDemo] Could not find bin, make sure the palletizing demo is loaded..")
        return False

    bb_cache = create_bbox_cache()
    half_ext = bb_cache.ComputeLocalBound(self._active_bin).GetRange().GetSize() * 0.5
    self._overlap_extent = carb.Float3(half_ext[0], half_ext[1], half_ext[2] * 1.1)

    self._timeline = omni.timeline.get_timeline_interface()
    if not self._timeline.is_playing():
        print("[PalletizingSDGDemo] Please start the palletizing demo first..")
        return False

    # Disable capture on play for replicator, data capture will be triggered manually
    rep.orchestrator.set_capture_on_play(False)

    # Set DLSS to Quality mode (2) for best SDG results
    carb.settings.get_settings().set("rtx/post/dlss/execMode", 2)

    # Clear any previously generated SDG graphs
    if self._stage.GetPrimAtPath("/Replicator"):
        omni.kit.commands.execute("DeletePrimsCommand", paths=["/Replicator"])

    return True

def _start(self):
    self._timeline_sub = carb.eventdispatcher.get_eventdispatcher().observe_event(
        event_name=omni.timeline.GLOBAL_EVENT_CURRENT_TIME_TICKED,
        on_event=self._on_timeline_event,
        observer_name="test_sdg_ur10_palletizing.PalletizingSDGDemo._on_timeline_event",
    )
    self._stage_event_sub = carb.eventdispatcher.get_eventdispatcher().observe_event(
        event_name=omni.usd.get_context().stage_event_name(omni.usd.StageEventType.CLOSING),
        on_event=self._on_stage_closing_event,
        observer_name="test_sdg_ur10_palletizing.PalletizingSDGDemo._on_stage_closing_event",
    )
    self._in_running_state = True
    print("[PalletizingSDGDemo] Starting the palletizing SDG demo..")
```

**Timeline Advance and Bin Overlaps**

On every timeline advance update, the `self._check_bin_overlaps` function is called to monitor the surroundings of the active bin. If an overlap is detected, the `self._on_overlap_hit` callback function is invoked. This function determines if the overlap is relevant to one of two scenarios:

> * bin flip
> * bin on pallet

If relevant, the simulation is paused, the timeline event subscription is removed, and the Synthetic Data Generation (SDG) starts for the current active bin. Depending on the current simulation state, the SDG is initiated by the `self._run_bin_flip_scenario` or the `self._run_pallet_scenario` function.

Bin Tracking Snippet

```python
def _on_timeline_event(self, e: carb.eventdispatcher.Event):
    self._check_bin_overlaps()

def _check_bin_overlaps(self):
    bin_pose = omni.usd.get_world_transform_matrix(self._active_bin)
    origin = bin_pose.ExtractTranslation()
    quat_gf = bin_pose.ExtractRotation().GetQuaternion()

    any_hit_flag = False
    hit_info = get_physx_scene_query_interface().overlap_box(
        carb.Float3(self._overlap_extent),
        carb.Float3(origin[0], origin[1], origin[2]),
        carb.Float4(
            quat_gf.GetImaginary()[0],
            quat_gf.GetImaginary()[1],
            quat_gf.GetImaginary()[2],
            quat_gf.GetReal(),
        ),
        self._on_overlap_hit,
        any_hit_flag,
    )

def _on_overlap_hit(self, hit):
    # Skip self-hits
    if hit.rigid_body == self._active_bin.GetPrimPath():
        return True

    # Handle flip scenario (only once per bin)
    if not self._bin_flip_scenario_done and hit.rigid_body.startswith(self.FLIP_HELPER_PATH):
        self._timeline.pause()
        if self._timeline_sub:
            self._timeline_sub.reset()
            self._timeline_sub = None
        asyncio.ensure_future(self._run_bin_flip_scenario())
        return False

    # Handle pallet landing scenario
    is_pallet_hit = hit.rigid_body.startswith(self.PALLET_PRIM_MESH_PATH)
    is_other_bin_hit = hit.rigid_body.startswith(f"{self.BINS_FOLDER_PATH}/bin_")
    if is_pallet_hit or is_other_bin_hit:
        self._timeline.pause()
        if self._timeline_sub:
            self._timeline_sub.reset()
            self._timeline_sub = None
        asyncio.ensure_future(self._run_pallet_scenario())

    return True  # No relevant hit, return True to continue the query
```

When the active bin is positioned on the flip helper object, it triggers the **bin flip scenario**. In this scenario, path tracing is chosen as the rendering mode. To collect the data, Replicator annotators are used directly to access the data and the `write_image` function from `omni.replicator.core.functional` writes the data to disk.

The `_create_bin_flip_graph` function is used to create the Replicator randomization graphs for the **bin flip scenario**. This includes the creation of a camera and randomized lights. After setting up the graph, a delayed preview command is dispatched, ensuring the graph is fully created prior to launching the Synthetic Data Generation (SDG).

The `rep.orchestrator.step_async` function is called for the requested number of frames (`self._bin_flip_frames`) to advance the randomization graph by one frame and provide the annotators with the new data. The data is then retrieved using the `get_data()` function and saved to disk using `write_image`. To optimize simulation performance, render products are discarded after each SDG pipeline and the constructed Replicator graphs are removed.

After the SDG scenario is completed, the render mode is set back to realtime path tracing. The timeline then resumes the simulation and the timeline subscriber is reactivated to continue monitoring the simulation environment. To ensure that the **bin flip scenario** doesnât re-trigger, given that the bin remains in contact with the flip helper object, the `self._bin_flip_scenario_done` flag is set to `True`.

Bin Flip Scenario Snippet

```python
async def _run_bin_flip_scenario(self):
    await omni.kit.app.get_app().next_update_async()
    print(f"[PalletizingSDGDemo] Running bin flip scenario for bin {self._bin_counter}..")

    self._switch_to_pathtracing(spp=16, total_spp=32)
    await omni.kit.app.get_app().next_update_async()
    self._create_bin_flip_graph()

    rgb_annot = rep.annotators.get("rgb")
    instance_segmentation_annot = rep.annotators.get("instance_segmentation", init_params={"colorize": True})
    rp = rep.create.render_product(self._rep_camera, (512, 512))
    rgb_annot.attach(rp)
    instance_segmentation_annot.attach(rp)
    out_dir = os.path.join(self._output_dir, f"annot_bin_{self._bin_counter}")
    os.makedirs(out_dir, exist_ok=True)

    print(f"[PalletizingSDGDemo] Starting capturing data for bin flip scenario for bin {self._bin_counter}..")
    for i in range(self._bin_flip_frames):
        print(f"  [PalletizingSDGDemo] Capturing frame {i + 1}/{self._bin_flip_frames}")
        await rep.orchestrator.step_async(rt_subframes=16, delta_time=0.0)

        rgb_data = rgb_annot.get_data()
        rgb_file_path = os.path.join(out_dir, f"rgb_{i}.png")
        write_image(path=rgb_file_path, data=rgb_data)

        instance_segmentation_data = instance_segmentation_annot.get_data()
        instance_segmentation_file_path = os.path.join(out_dir, f"instance_segmentation_{i}.png")
        write_image(path=instance_segmentation_file_path, data=instance_segmentation_data["data"])
        with open(os.path.join(out_dir, f"instance_segmentation_info_{i}.json"), "w") as f:
            json.dump(instance_segmentation_data["info"], f, indent=4)

    # Wait for the data to be written to disk and free up resources after the capture
    await rep.orchestrator.wait_until_complete_async()
    rgb_annot.detach()
    instance_segmentation_annot.detach()
    rp.destroy()

    # Cleanup the generated SDG graph
    if self._stage.GetPrimAtPath("/Replicator"):
        omni.kit.commands.execute("DeletePrimsCommand", paths=["/Replicator"])

    self._switch_to_realtime_pathtracing()

    # Set the flag to indicate that the bin flip scenario is done
    self._bin_flip_scenario_done = True
    self._timeline_sub = carb.eventdispatcher.get_eventdispatcher().observe_event(
        event_name=omni.timeline.GLOBAL_EVENT_CURRENT_TIME_TICKED,
        on_event=self._on_timeline_event,
        observer_name="test_sdg_ur10_palletizing.PalletizingSDGDemo._on_timeline_event",
    )
    self._timeline.play()
```

For the **bin flip scenario**, the Replicator randomization graph uses a predefined color palette list. This list provides options for the system to randomly select colors when varying the lights using `rep.distribution.choice(color_palette)`. Meanwhile, the camera operates from a set of predefined locations. Instead of random selections, the camera sequentially transitions between these locations using `rep.distribution.sequence(camera_positions)`. Both the randomization of lights and the systematic camera movement are programmed to execute with every frame capture, as indicated by `rep.trigger.on_frame()`.

Bin Flip Randomization Graph Snippet

```python
def _create_bin_flip_graph(self):
    # Create new random lights using the color palette for the color attribute
    color_palette = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]

    def randomize_bin_flip_lights():
        lights = rep.create.light(
            light_type="Sphere",
            temperature=rep.distribution.normal(6500, 2000),
            intensity=rep.distribution.normal(45000, 15000),
            position=rep.distribution.uniform((0.25, 0.25, 0.5), (1, 1, 0.75)),
            scale=rep.distribution.uniform(0.5, 0.8),
            color=rep.distribution.choice(color_palette),
            count=3,
        )
        return lights.node

    rep.randomizer.register(randomize_bin_flip_lights)

    # Move the camera to the given location sequences and look at the predefined location
    camera_positions = [
        (1.96, 0.72, -0.34),
        (1.48, 0.70, 0.90),
        (0.79, -0.86, 0.12),
        (-0.49, 1.47, 0.58),
    ]
    self._rep_camera = rep.create.camera()
    with rep.trigger.on_frame():
        rep.randomizer.randomize_bin_flip_lights()
        with self._rep_camera:
            rep.modify.pose(
                position=rep.distribution.sequence(camera_positions),
                look_at=(0.78, 0.72, -0.1),
            )
```

When the active bin is placed on the pallet, or on top of another bin on the pallet, it triggers the **bin on pallet scenario**. Because the randomization graph is modifying the materials and textures of the bins and the pallet, these original materials are cached. This ensures that they can be reapplied after the simulation resumes.

The `_create_bin_and_pallet_graph` function sets up the Replicator randomization graphs for this scenario. These graphs include the camera, which randomizes its position around the pallet, the varying materials for the bins placed on the pallet, and the alternating textures for the pallet itself. After the graph is created, a delayed preview command is dispatched to ensure that it is fully generated before the Synthetic Data Generation (SDG) begins.

For data writing, the **bin on pallet scenario** uses a `DiskBackend` with the built-in Replicator `BasicWriter`. For each frame defined by `self._pallet_frames`, the `rep.orchestrator.step_async` function advances the randomization graph by a single frame. This action also triggers the writer to save the data to disk. To improve performance during the simulation, the created render products are discarded after each scenario and the generated graphs are removed.

After the scenario completes, the cached materials are re-applied. The system then checks to see if it has processed the last bin. If not, the simulation is resumed, designating the next bin as active and reactivating the timeline subscriber to continue monitoring the simulation environment.

Bin on Pallet Scenario Snippet

```python
async def _run_pallet_scenario(self):
    await omni.kit.app.get_app().next_update_async()
    print(f"[PalletizingSDGDemo] Running pallet scenario for bin {self._bin_counter}..")
    mesh_to_orig_mats = {}
    pallet_mesh = self._stage.GetPrimAtPath(self.PALLET_PRIM_MESH_PATH)
    pallet_orig_mat, _ = UsdShade.MaterialBindingAPI(pallet_mesh).ComputeBoundMaterial()
    mesh_to_orig_mats[pallet_mesh] = pallet_orig_mat
    for i in range(self._bin_counter + 1):
        bin_mesh = self._stage.GetPrimAtPath(f"{self.BINS_FOLDER_PATH}/bin_{i}/Visuals/FOF_Mesh_Magenta_Box")
        bin_orig_mat, _ = UsdShade.MaterialBindingAPI(bin_mesh).ComputeBoundMaterial()
        mesh_to_orig_mats[bin_mesh] = bin_orig_mat

    self._create_bin_and_pallet_graph()

    out_dir = os.path.join(self._output_dir, f"writer_bin_{self._bin_counter}", "")
    backend = rep.backends.get("DiskBackend")
    backend.initialize(output_dir=out_dir)
    writer = rep.WriterRegistry.get("BasicWriter")
    writer.initialize(
        backend=backend,
        rgb=True,
        instance_segmentation=True,
        colorize_instance_segmentation=True,
    )
    rp = rep.create.render_product(self._rep_camera, (512, 512))
    writer.attach(rp)

    print(f"[PalletizingSDGDemo] Starting capturing data for pallet scenario for bin {self._bin_counter}..")
    for i in range(self._pallet_frames):
        print(f"  [PalletizingSDGDemo] Capturing frame {i + 1}/{self._pallet_frames}")
        await rep.orchestrator.step_async(rt_subframes=16, delta_time=0.0)

    # Make sure the backend finishes writing the data before clearing the generated SDG graph
    await rep.orchestrator.wait_until_complete_async()

    # Free up resources after the capture
    writer.detach()
    rp.destroy()

    # Cleanup the generated SDG graph
    print(f"[PalletizingSDGDemo] Restoring {len(mesh_to_orig_mats)} original materials")
    for mesh, mat in mesh_to_orig_mats.items():
        UsdShade.MaterialBindingAPI(mesh).Bind(mat, UsdShade.Tokens.strongerThanDescendants)

    # Cleanup the generated SDG graph
    if self._stage.GetPrimAtPath("/Replicator"):
        omni.kit.commands.execute("DeletePrimsCommand", paths=["/Replicator"])

    # Return in paused state if there are no more bins to capture
    if not self._next_bin():
        return

    # Resume the simulation and continue with the next bin
    self._timeline_sub = carb.eventdispatcher.get_eventdispatcher().observe_event(
        event_name=omni.timeline.GLOBAL_EVENT_CURRENT_TIME_TICKED,
        on_event=self._on_timeline_event,
        observer_name="test_sdg_ur10_palletizing.PalletizingSDGDemo._on_timeline_event",
    )
    self._timeline.play()
```

For the **bin on pallet scenario**, the Replicator randomization graph randomizes the colors of the bin materials. A predefined list of textures is used, from which the graph randomly selects and applies th pallet textures, this is done by `rep.randomizer.texture(texture_paths,..)`. The cameraâs position varies around the pallet using `rep.distribution.uniform(..)` and is oriented towards the palletâs location. The trigger is split into two parts:

* the bin materials are changed **every frame** as shown by `rep.trigger.on_frame()`
* while the pallet textures and the camera positions are executed every **four frames**, represented by `rep.trigger.on_frame(interval=4)`

Bin on Pallet Randomization Graph Snippet

```python
def _create_bin_and_pallet_graph(self):
    # Bin material randomization
    bin_paths = [
        f"{self.BINS_FOLDER_PATH}/bin_{i}/Visuals/FOF_Mesh_Magenta_Box" for i in range(self._bin_counter + 1)
    ]
    bins_node = rep.get.prim_at_path(bin_paths)

    with rep.trigger.on_frame():
        mats = rep.create.material_omnipbr(
            diffuse=rep.distribution.uniform((0.2, 0.1, 0.3), (0.6, 0.6, 0.7)),
            roughness=rep.distribution.choice([0.1, 0.9]),
            count=10,
        )
        with bins_node:
            rep.randomizer.materials(mats)

    # Camera and pallet texture randomization at a slower rate
    assets_root_path = get_assets_root_path()
    texture_paths = [
        assets_root_path + "/NVIDIA/Materials/Base/Wood/Oak/Oak_BaseColor.png",
        assets_root_path + "/NVIDIA/Materials/Base/Wood/Ash/Ash_BaseColor.png",
        assets_root_path + "/NVIDIA/Materials/Base/Wood/Plywood/Plywood_BaseColor.png",
        assets_root_path + "/NVIDIA/Materials/Base/Wood/Timber/Timber_BaseColor.png",
    ]
    pallet_node = rep.get.prim_at_path(self.PALLET_PRIM_MESH_PATH)
    pallet_prim = pallet_node.get_output_prims()["prims"][0]
    pallet_loc = omni.usd.get_world_transform_matrix(pallet_prim).ExtractTranslation()
    self._rep_camera = rep.create.camera()
    with rep.trigger.on_frame(interval=4):
        with pallet_node:
            rep.randomizer.texture(texture_paths, texture_rotate=rep.distribution.uniform(80, 95))
        with self._rep_camera:
            rep.modify.pose(
                position=rep.distribution.uniform((0, -2, 1), (2, 1, 2)),
                look_at=(pallet_loc[0], pallet_loc[1], pallet_loc[2]),
            )
```

On this page

* [Learning Objectives](#learning-objectives)
* [Prerequisites](#prerequisites)
* [Scenario](#scenario)
* [Implementation](#implementation)

---

