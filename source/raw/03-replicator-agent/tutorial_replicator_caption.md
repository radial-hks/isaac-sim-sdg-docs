---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/action_and_event_data_generation/tutorial_replicator_caption.html
title: "Replicator Caption"
section: "Agent"
module: "03-replicator-agent"
checksum: "ac167210a7726bfb"
fetched: "2026-06-21T11:55:26"
---

* [Synthetic Data Generation](../synthetic_data_generation/index.html)
* [Action and Event Data Generation](index.html)
* VLM Scene Captioning

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# VLM Scene Captioning

Vision-language models (VLMs) rely on paired
image-caption datasets to learn the complex
relationships between visual content and textual
descriptions. Captions provide the semantic
grounding necessary for models to understand
objects, actions, and contexts within images.
High-quality captions are essential for training
VLMs capable of nuanced scene understanding and reasoning.

Leveraging 3D ground truth from NVIDIA
Omniverse transforms the captioning process by
enabling detailed, accurate, and scalable annotations.
These captions include overall scene descriptions,
object relationships, and spatial reasoning, such as
relative positions and interactions between elements in a camera view.
With 3D metadata, captions can describe not just what
is visible but how elements are arranged and interact,
offering richer contextual understanding.

This approach ensures more consistent and diverse
datasets, allowing VLMs to excel in complex tasks like
spatial reasoning and scene analysis, ultimately
bridging the gap between visual and linguistic comprehension.

`Isaacsim.Replicator.Caption.Core` (IRC) has the following features:

* Generate image-caption pairs for loaded scenes in Omniverse.
* Plug in to other `Isaacsim.Replicator` modules, including
  `Isaacsim.replicator.object (IRO)` and `Isaacsim.replicator.agent (IRA)` to
  generate captions for each frame at their runtime.
* Export scene graphs alongside caption outputs for customized postprocessing
  and caption preparation.

## Python API

IRC provides a Python API (`CaptionAPI`) for programmatic model configuration and caption generation:

Note

The snippet below reads the model API key from the `NVIDIA_API_KEY` environment variable. Generate your own key from the [NVIDIA NIM API key page](https://docs.nvidia.com/nim/large-language-models/latest/getting-started.html#generate-an-api-key) and export it (for example, `export NVIDIA_API_KEY=<API_KEY>`) before running the script.

Setting up the IRC model

```python
import os
from isaacsim.replicator.caption.core.api import CaptionAPI

def setup_irc_model():
    CaptionAPI.set_model_params(
        url="https://integrate.api.nvidia.com/v1",
        name="meta/llama-3.1-8b-instruct",
        key=os.environ["NVIDIA_API_KEY"],
    )
    print("IRC model params set successfully.")

setup_irc_model()
```

After setting up the model, you can generate captions programmatically:

Generating captions via the API

```python
import asyncio
from isaacsim.replicator.caption.core.api import CaptionAPI

def on_done(future):
    captions = future.result()
    print(f"Generated captions: {captions}")

task = asyncio.ensure_future(CaptionAPI.get_captions())
task.add_done_callback(on_done)
```

You can also load an IRC configuration file before generating captions:

Loading an IRC configuration file

```python
from isaacsim.replicator.caption.core.api import CaptionAPI

CaptionAPI.load_config_file("/path/to/irc_config.yaml")
```

### Workflow

`Isaacsim.Replicator.Caption.Core` uses the following workflow to generate captions:

## Scene Graph

A scene graph is an intermediate output for caption generation. It is
a structured representation of a visual scene,
where nodes represent objects and edges denote spatial relationships
between them. It captures how elements are arranged in space,
such as relative positions and orientations. For example, in
an image of a person sitting on a bench under a tree, the graph
would include nodes for âperson,â âbench,â and âtree,â with edges
like âsitting onâ and âunder.â This spatial focus makes scene graphs
valuable for tasks requiring detailed spatial reasoning and scene analysis.

You can export scene graphs alongside caption outputs to
enable flexible and customizable management of scene graph data
for your specific requirements.

### Enable Isaacsim.Replicator.Caption.Core Extension

1. Follow the [Omniverse Extension Manager guide](https://docs.omniverse.nvidia.com/extensions/latest/ext_core/ext_extension-manager.html) to enable the `isaacsim.replicator.caption.core` extension.

   > * The extension fetches sample assets from Isaac Sim Assets during start. Refer to [Isaac Sim Assets](../assets/usd_assets_overview.html) if you encounter issues for loading assets.
   > * If loading the UI appears to be hanging, try starting Isaac Sim with the flag `--/persistent/isaac/asset_root/timeout=1.0`.
2. The IRC UI panel is accessible by **Tools > Action and Event Data Generation > VLM Scene Captioning** and it opens on the right side of the screen.

IRC can be invoked using the following methods:

* [Using the UI panel](#using-ui-panel)
* [Using the IRA extension](#using-ira-extension)
* [Using the IRO extension](#using-iro-extension)

## Using the UI Panel

To launch scene caption generation with the UI panel:

1. After enabling, the extension will appear in the UI panel:
2. To load the stage USD file, open up the `Caption Settings` panel, and then click on the file selector icon.
3. Select the USD file you want to caption. There is a default USD file for demonstration.

   Note

   We include an example USD. You can find it in `[Isaac Sim Assets Path]/Samples/Replicator/Captioning/test_caption.usda`.

   `[Isaac Sim Assets Path]` is the path to [Isaac Sim Assets](../assets/usd_assets_overview.html#isaac-assets-overview)

   Refer to [Isaac Sim Assets Check](../installation/install_faq.html#isaac-sim-setup-assets-check) for how to verify the assets access and how to retrieve the asset path.
4. Click on the **Load Scene** button to load the scene.

   The stage will be loaded in the stage view. If prompted to enable script execution, click **Yes**.
5. Enter the LLM model credentials in the [API key](https://docs.nvidia.com/nim/large-language-models/latest/getting-started.html#generate-an-api-key) field of the **Model Settings** panel; click **Accept** to continue.
6. Under the **Caption Settings** panel, enter the desired caption level â **Brief Caption** for short and **Full Caption** for a more elaborate description. Enter the camera prim path in the **Input Camera Prim Path** field.
   Input the **Output Path** to specify where to save the generated captions, the associated scene graphs, and metadata. Ensure the output path is a valid directory. Click **Generate Scene Graph**.

   Note

   The default service URL and model name are provided as a convenience. The services are hosted by NVIDIA and provided free of charge on a trial basis.
   If the service associated with the default model is not reachable, a different model can be selected from the models available on
   the [NVIDIA NIM API reference page](https://docs.api.nvidia.com/nim/reference/llm-apis). Enter the model identifier in the **Model Name** field of the **Model Settings** panel.

   Itâs also possible to obtain NVIDIA NIMs and host them locally.
   Visit [NVIDIAâs NIM page](https://build.nvidia.com) for more details.
7. The scene graph, the caption, and the corresponding images are generated and saved in the output directory.

Note

Focusing on specific regions of interest (ROIs) in a complex scene can be achieved by positioning a camera appropriately.

The following steps demonstrate how to generate captions for a region of interest (ROI).

8. To generate captions for a region of interest (ROI), select the desired camera from the camera drop-down as shown below:
9. Position the camera at the desired location so that the ROI dominates the view plane, as shown below:
10. Click on the **Generate Scene Graph** button to generate the captions for the ROI, after selecting the desired caption and output parameters described in earlier steps.

## Using the IRA Extension

To launch scene caption generation with IRA, load the a YAML configuration file.
Or use the default configuration file that comes with the extension and
follow the steps below to prepare some environment variables.

The anatomy of an IRC configuration file, used to run the extension
under IRO and IRA, is explained.

1. Prepare the [NVIDIA NIM API key](https://docs.nvidia.com/nim/large-language-models/latest/getting-started.html#generate-an-api-key)
   for the extension to use.

   The extension requires NVIDIA NIM AI to generate captions.
   The credentials must be stored in the environment variables.

   **Linux/Mac:**

   Add to `~/.bashrc` or `~/.bash_profile`:

   ```python
   export NVIDIA_API_KEY=<API_KEY>
   ```

   **Windows:**

   Command Prompt:

   ```python
   set NVIDIA_API_KEY=<API_KEY>
   ```

   Note

   * The NVIDIA NIM API key has a limited lifetime. The number of free credits is limited and is accessible through the account associated with the API key. After the credits are exhausted, you can apply for more credits through the developer portal. Refer to [the developer forum](https://forums.developer.nvidia.com/t/nim-pricing/290144) for more details.
   * If you only need to generate scene graphs without captions, the AI credentials are not required.

### Example `Isaacsim.Replicator.Caption.Core` Configuration File

For example, a configuration file is similar to the following:

```python
isaacsim.replicator.caption.core:
   version: 0.6.6
   camera_prim_path: /World/Cameras/Camera
   scene_path: USD_FILE
   caption_configs:
      save_full_scene_graph: true
      save_pruned_scene_graph: true
      attach_label_to_usd: false
      use_ai_label: false
      visualize_caption: true
      max_object_capacity: 100
      export_edges: true
      global_caption: true
      qa_caption: false
      brief_caption: true
      pruning_ratio: 1.0
      verbose: true
      random_seed: 0
      caption_only: false
      export_world: true
   output_path: OUTPUT_PATH
```

## Global Properties

version

The version of IRC extension. If version does not match, the extension will not work.

camera\_prim\_path

The path to the camera prim in the scene. If not provided, the extension uses the default camera path defined in
the `default_config.yaml` file. However, if there is no camera in the scene, the extension will not work.
You must guarantee that the camera is available in the scene.

scene\_path

The path to the scene USD file. The extension can load the scene from this path. However, if the `scene_path` is
not provided, the extension uses whatever scene is loaded in the app. If no scene is loaded, the extension will not work.

output\_path

The path to the output directory where the generated captions will be saved. If not provided, the extension will use the default output path.

## Caption Configurations

save\_full\_scene\_graph

If True, it will save the full scene graph in the output directory.

The file will be saved as `<output_path>/<Camera Prim Name>/Captions/full_scene_graph.json`.

save\_pruned\_scene\_graph

If True, it will save the pruned scene graph in the output directory. The full scene graph includes
the edges between any two objects at the same level in the Support Tree.

The file will be saved as `<output_path>/<Camera Prim Name>/Captions/pruned_scene_graph.json`.

Note

**Support Tree:** A tree that represents the spatial relationships between objects in the scene.
The root of the tree is the floor (0th level). The direct children of the root are the objects on the floor, which is considered the 1st level.
The objects on the 2nd level are the objects supported by the objects on the 1st level, and so on.

pruning\_ratio

The ratio of the scene graph to be pruned. The scene graph will be pruned to a **Minimum Spanning Tree** (MST).
The pruning ratio determines the percentage of the MST edges to be kept. For example, if `pruning_ratio` is set to `0.5`,
the scene graph is pruned to 50% of the MST edges.

By default, `pruning_ratio` is set to `1.0`, which means the scene graph will not be further pruned after the MST is generated.

random\_seed

An integer for the random process. When `pruning_ratio` is less than `1.0`, the edges will be
randomly removed from the MST. The random seed is used to control the randomness of this process.

attach\_label\_to\_usd

If True, it will attach the automatically generated semantic labels to all prims with an USD address in the scene,
if the prim does not have a semantic label pre-attached.
The automatic semantic label is based on the prim path basename. For example, if the prim path is `/World/Objects/Chair`,
the semantic label will be `Chair`.

With semantic label attached, Omniverse [annotators](https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator/annotators_details.html#annotators-information)
are able to capture the prim for the annotation defined. This is critical for captioning tasks, because prims not
captured by annotators cannot be included in the scene graph and therefore will not be captioned.

use\_ai\_label

If True, it will use the AI-generated labels for the prims with semantic labels in the scene. The AI-generated labels
are preprocessed and stored in the database, and they will be pulled from the database at runtime. This function can
be combined with `attach_label_to_usd: true` to handle the case when target prims does not have semantic labels pre-stored
in the scene file.

visualize\_caption

If True, it will visualize the scene graph on the output images. The visualization will be saved as
<output\_path>/<Camera Prim Name>/Captions/vis\_camera\_scene\_graph.jpg.

max\_object\_capacity

The maximum number of objects that the scene graph can contain. The objects are selected by their 2D bounding
box sizes in the camera view in a reverse order.

export\_edges

If True, the edges of the scene graph will be exported to scene graph files. The edges represent the spatial
relationships between objects.

export\_world

If True, the extension will export 3D World locations of the prims in the scene graph, and save them in the scene
graph files. The 3D World locations are the 3D coordinates of the prims in the world space. If not mentioned, all
other locations are in the camera space.

global\_caption

If True, the extension will generate a global caption for the scene. The global caption describes the overall
scene content and context. This will be saved in the output file
`<output_path>/<Camera Prim Name>/Captions/scene_graph_caption.json`.

qa\_caption

If True, the extension will generate QA captions for the scene. The QA captions are questions and answers
that test the modelâs understanding of the scene.

This will be saved in the output file
`<output_path>/<Camera Prim Name>/Captions/scene_graph_caption.json`.

brief\_caption

If True, the extension will generate brief captions for the scene. The brief captions are the short version of
the global caption. This will be saved in the output file
`<output_path>/<Camera Prim Name>/Captions/scene_graph_caption.json`.

verbose

If True, the extension will print the detailed information of the scene graph generation process, such as the `support tree`,
and the number of nodes and edges in the scene graph.

caption\_only

If True, only the prims whose corresponding USD files have their object caption preprocessed and stored in the database
will be included in the scene graph and following caption generation process.

### Use IRC in `Isaacsim.Replicator.Agent`

[Isaacsim.replicator.agent](tutorial_replicator_agent.html#isaac-sim-app-tutorial-replicator-character) (IRA) is a module that generates
synthetic data on human characters and robots across a variety of 3D environments. With the IRC extension enabled
in IRA, you can generate captions for each frame at the same time.

To enable IRC in IRA:

1. In the IRA configuration file, use IRCâs `SceneGraphWriter` to write the captions to the output directory.

   Example:

   ```python
   isaacsim.replicator.agent:
      version: 1.6.0
      simulation_duration: 5
      environment:
         base_stage_asset_path: "Isaac/Samples/Replicator/Captioning/test_caption.usda"
      sensor:
         groups:
            ceiling_cameras:
               num: 2
               aim_at_targets:
                  distance_range: [5, 10]
                  height_range: [7, 10]
                  focal_length_range: [10, 15]
                  look_down_angle_range: [30, 45]
      character:
         groups:
            warehouse_workers:
               asset_path: "Isaac/People/Characters/"
               num: 5
               routines:
               - wander:
                    weight: 1
                    repeat: 1
                    walk:
                       speed_range: [0.8, 1.5]
                       distance_range: [5.0, 10.0]
                    idle:
                       - animation: idle
                         weight: 1
                         time_range: [2.0, 5.0]
      replicator:
         writers:
            SceneGraphWriter:
               semantic_filter_predicate: "class:*"
               rgb: true
               camera_params: true
               object_info_bounding_box_2d_tight: true
               object_info_bounding_box_2d_loose: true
               object_info_bounding_box_3d: true
               pruning_ratio: 1.0
               global_caption: true
               qa_caption: false
               brief_caption: true
               visualize_caption: true
               max_object_capacity: 100
               export_edges: true
               save_full_scene_graph: true
               save_pruned_scene_graph: true
               export_world: false
               attach_label_to_usd: false
               use_ai_label: false
               verbose: false
               random_seed: 0
               caption_only: false
               scene_graph_interval: 10
               caption_interval: 10
   ```

   The caption output will be stored in the output directory as:

   * pruned scene graph: `<output_dir>/<Camera Prim Name>/caption_pruned_json/scene_graph_pruned_<frame id>.json`
   * full scene graph: `<output_dir>/<Camera Prim Name>/caption_full_json/scene_graph_full_<frame id>.json`
   * captions: `<output_dir>/<Camera Prim Name>/caption/scene_graph_caption_<frame id>.json`

   Below are the other parameters in the `SceneGraphWriter`:

   output\_dir

   The path to the output directory where the generated captions as well as IRA outputs will be saved.
   If not provided, the extension will use the default output path.

   caption\_interval

   The interval of the caption generation process. The caption will be generated every `caption_interval` frames.
   By default, `caption_interval` is set to `1000`.

   scene\_graph\_interval

   The interval of the scene graph generation process. The scene graph will be generated every `scene_graph_interval` frames.
   By default, `scene_graph_interval` is set to `1`.

   skip\_frames

   The number of frames to skip before starting the caption generation process.
   By default, `skip_frames` is set to `0`.

   writer\_interval

   The interval of the writer process. The writer will write the IRA outputs to the output directory every `writer_interval` frames.
   By default, `writer_interval` is set to `1`.

   export\_point\_cloud

   If True, the extension will export the point cloud of the frame. The point cloud will be saved in the output directory because `<output_dir>/<Camera Prim Name>/pointcloud/pointcloud_<frame id>.npy`. By default, `export_point_cloud` is set to False.

   export\_depth

   If True, the extension will export the depth map of the frame. The depth map will be saved in the output directory as
   `<output_dir>/<Camera Prim Name>/depth/depth_<frame id>.npy`. By default, `export_depth` is set to False.
2. Follow the steps in the [Isaacsim.replicator.agent](tutorial_replicator_agent.html#isaac-sim-app-tutorial-replicator-character) tutorial to start the data generation process.

### Use IRC in `Isaacsim.Replicator.Object`

[Isaacsim.replicator.object](tutorial_replicator_object.html#isaac-sim-app-tutorial-replicator-object) (IRO) is a module that composes scenes that are
uniquely domain randomized. With the IRC extension enabled in IRC, you can generate captions for each frame at the same time.

To enable IRC in IRO:

1. In the IRO configuration file, use IRCâs `CombinedIROSceneGraphWriter` to write the IRO output together with captions
   to the output directory.

   Example:

   ```python
   isaacsim.replicator.object:
      version: 0.x.y
      camera_parameters: ...
      caption_configs:
         save_full_scene_graph: true
         save_pruned_scene_graph: true
         attach_label_to_usd: false
         use_ai_label: false
         visualize_caption: true
         max_object_capacity: 100
         export_edges: true
         caption_only: false
         global_caption: true
         qa_caption: true
         brief_caption: true
         pruning_ratio: 1.0
         verbose: true
         random_seed: 0
         caption_writer: CombinedIROSceneGraphWriter
      output_switches:
         caption: True
         ...
   ```

   In the `caption_configs` field, the configurations are the same as in the IRC configuration file, with
   one additional field `caption_writer`.

   caption\_writer

   The writer to write the captions to the output directory. The available writers are:

   * `CombinedIROSceneGraphWriter`: This writer combines the IRO outputs with the captions.
   * `IROSceneGraphWriter`: This writer only writes the captions to the output directory while suppressing other
     :   IRO outputs, such as `labels` (The 2D detection labels). However, it can generate `images`, `distance_to_image_plane` and `pointcloud`.

   The caption output will be stored in the output directory as:

   * pruned scene graph: `<output_dir>/caption/caption_pruned_json/<seed>_<camera_name>.json`
   * full scene graph: `<output_dir>/caption/caption_full_json/<seed>_<camera_name>.json`
   * visualized scene graph: `<output_dir>/caption_rgb/<seed>_<camera_name>.jpg`
   * captions: `<output_dir>/<Camera Prim Name>/caption_dict/<seed>_<camera_name>.json`
2. Follow the steps in the [Isaacsim.replicator.object](tutorial_replicator_object.html#isaac-sim-app-tutorial-replicator-object) tutorial to start the data generation process.

On this page

* [Python API](#python-api)
  + [Workflow](#workflow)
* [Scene Graph](#scene-graph)
  + [Enable Isaacsim.Replicator.Caption.Core Extension](#enable-isaacsim-replicator-caption-core-extension)
* [Using the UI Panel](#using-the-ui-panel)
* [Using the IRA Extension](#using-the-ira-extension)
  + [Example `Isaacsim.Replicator.Caption.Core` Configuration File](#example-isaacsim-replicator-caption-core-configuration-file)
* [Global Properties](#global-properties)
* [Caption Configurations](#caption-configurations)
  + [Use IRC in `Isaacsim.Replicator.Agent`](#use-irc-in-isaacsim-replicator-agent)
  + [Use IRC in `Isaacsim.Replicator.Object`](#use-irc-in-isaacsim-replicator-object)