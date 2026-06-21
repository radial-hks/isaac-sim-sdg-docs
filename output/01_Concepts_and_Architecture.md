# Concepts & Architecture

> Isaac Sim 架构总览、核心概念、工作流、UI、资产结构、OpenUSD 基础
> Isaac Sim 版本: 6.0
> 最后组装: 2026-06-21 13:58 UTC
> 来源页数: 20

---

## 来源链接

- [Reference Architecture](https://docs.isaacsim.omniverse.nvidia.com/latest/introduction/reference_architecture.html)
- [Workflows](https://docs.isaacsim.omniverse.nvidia.com/latest/introduction/workflows.html)
- [User Interface Reference](https://docs.isaacsim.omniverse.nvidia.com/latest/gui/reference_user_interface.html)
- [Keyboard Shortcuts Reference](https://docs.isaacsim.omniverse.nvidia.com/latest/gui/reference_keyboard_shortcuts.html)
- [Asset Structure](https://docs.isaacsim.omniverse.nvidia.com/latest/robot_setup/asset_structure.html)
- [What Is Isaac Sim?](https://docs.isaacsim.omniverse.nvidia.com/latest/index.html)
- [Quick Start Isaac Sim](https://docs.isaacsim.omniverse.nvidia.com/latest/introduction/quickstart_isaacsim.html)
- [Quick Start with Robot](https://docs.isaacsim.omniverse.nvidia.com/latest/introduction/quickstart_isaacsim_robot.html)
- [Quick Start Index](https://docs.isaacsim.omniverse.nvidia.com/latest/introduction/quickstart_index.html)
- [Robot Simulation Core Concepts](https://docs.isaacsim.omniverse.nvidia.com/latest/robot_simulation/robot_simulation_core_concepts.html)
- [Robot Simulation Tips](https://docs.isaacsim.omniverse.nvidia.com/latest/robot_simulation/robot_simulation_tips.html)
- [Intro to USD](https://docs.isaacsim.omniverse.nvidia.com/latest/omniverse_usd/intro_to_usd.html)
- [OpenUSD](https://docs.isaacsim.omniverse.nvidia.com/latest/omniverse_usd/open_usd.html)
- [Robot Schema](https://docs.isaacsim.omniverse.nvidia.com/latest/omniverse_usd/robot_schema.html)
- [Sensor Schema](https://docs.isaacsim.omniverse.nvidia.com/latest/omniverse_usd/sensor_schema.html)
- [Synthetic Data Generation Index](https://docs.isaacsim.omniverse.nvidia.com/latest/synthetic_data_generation/index.html)
- [Replicator Overview](https://docs.isaacsim.omniverse.nvidia.com/latest/replicator_tutorials/tutorial_replicator_overview.html)
- [Isaac Sim Conventions](https://docs.isaacsim.omniverse.nvidia.com/latest/reference_material/reference_conventions.html)
- [Glossary](https://docs.isaacsim.omniverse.nvidia.com/latest/reference_material/reference_glossary.html)
- [Benchmarks](https://docs.isaacsim.omniverse.nvidia.com/latest/reference_material/benchmarks.html)

---


## 概念

### Reference Architecture

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/introduction/reference_architecture.html

* Reference Architecture and Task Groupings

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Reference Architecture and Task Groupings

Isaac Sim is typically installed and used as one part of a larger solution. Depending on your use case and requirements, this document provides a reference architecture. Almost all use-cases involve some commonalities, which are highlighted as task groupings in the diagrams below. Within each task grouping your product architecture could include one or more of the products or components that are listed.

Regardless of your product components, most Isaac Sim use cases involve the following high level task groupings that occur in roughly the same order:

1. Geometry Authoring

* [SimReady Assets](https://developer.nvidia.com/omniverse/simready-assets)
* [Isaac Sim Assets](../assets/usd_assets_overview.html#isaac-assets-overview)

2. Importing Assets

* [Importers and Exporters](../importer_exporter/importers_exporters.html#isaac-sim-importers-and-exporters)
* [USD Tools](../omniverse_usd/index.html#isaac-sim-app-omniverse-usd-tools)

3. Scene Setup

* [Robot Setup Tools and Standards](../robot_setup/index.html#isaac-sim-robot-setup)
* [Robot Setup Tutorials](../robot_setup_tutorials/index.html#isaac-sim-robot-setup-tutorials)
* [Synthetic Sensors](../sensors/index.html#isaac-sim-sensor-simulation)

4. Interaction with the Digital Twin

* [Robot Simulation and Controllers](../robot_simulation/index.html#isaac-sim-robot-simulation)
* [Robot Articulation and Physics Tools](../physics/index.html#isaac-sim-physics)
* [Motion Generation](../manipulators/concepts/index.html#isaac-sim-motion-generation)
* [OmniGraph](../omnigraph/index.html#isaac-sim-omnigraph-overview-page)

5. Use Cases

* [Isaac Lab](../isaac_lab_tutorials/index.html#isaac-lab-tutorials-page)
* [Synthetic Data Generation](../synthetic_data_generation/index.html#isaac-synthetic-data-generation-page)
* [ROS 2 Bridge](../ros2_tutorials/index.html#isaac-ros2-tutorials-page)
* [Isaac ROS](../nvidia_isaac_ros/isaac_ros_tutorials.html#isaac-sim-app-isaac-ros-tutorials)

Typical use-cases are summarized in [Use Cases](#isaac-sim-ra-consumption).

## Geometry Authoring

The simulation environment (scene) is composed of various components including robots,
static, and dynamic objects. The mechanical and geometrical design for these components
is usually done with CAD software like Solidworks, Pro-E, Catia, AutoCad, or Creo. Parts and
components of varying complexity can be designed and assembled.

Developers can also leverage existing 3D asset libraries, which provide a vast collection of
existing 3D assets. Omniverse and Isaac Sim leverage a file format called [Universal Scene
Description (OpenUSD)](https://www.nvidia.com/en-us/omniverse/usd/).

All assets need to be converted to OpenUSD before they can be used with Isaac Sim, and the default unit for Isaac Sim is meters.

NVIDIA provides a vast collection of OpenUSD ‘SimReady’ assets. [SimReady](https://developer.nvidia.com/omniverse/simready-assets), or
simulation-ready, assets are physically accurate 3D objects that have accurate
physical properties, behavior, and connected data streams that are used to represent the real world in
simulated digital worlds. Developers can use these building blocks to construct scenes and
generate data per their requirements. The Warehouse asset collection includes over
800 3D assets of commonly available tools, equipment, and items in a warehouse including
forklifts, pallets, racks, and shelves.

## Importing Assets

There are extensions that enable importing CAD (Computer Aided Design) files into Isaac Sim
that handle conversion to OpenUSD. Extensions are core building blocks that
interact with and add or extend the functionality of Isaac Sim.

### Importing and Creating Environments

The [asset importer](https://docs.omniverse.nvidia.com/extensions/latest/ext_asset-importer.html#asset-importer)
can be leveraged for importing OBJ, FBX, and glTF formats. The [CAD converter](https://docs.omniverse.nvidia.com/extensions/latest/ext_cad-converter.html#cad-converter)
extension supports a variety of popular CAD files from applications including
Catia, Solidworks, AutoCad, and Creo. This enables you to quickly convert and
import your environment into Isaac Sim.

OpenUSD Connections and Data Exchange, formerly Omniverse Connect, is a collection of
[importers](https://docs.omniverse.nvidia.com/connect/latest/catalog.html#importers-exporters),
[exporters](https://docs.omniverse.nvidia.com/connect/latest/catalog.html#exporters),
[converters](https://docs.omniverse.nvidia.com/connect/latest/catalog.html#converters), and
[USD file format](https://docs.omniverse.nvidia.com/connect/latest/catalog.html#file-format-plugins) plug-ins. They enable various 3D applications, products, and file formats to exchange data using OpenUSD.

Some CAD applications have connectors with Omniverse, which allows them to bring over more relevant
and contextual information when converting to USD. For example, PTC Creo, Autodesk Revit, or Autodesk Alias have corresponding connectors. The files generated
from their CAD converters will have all the visual meshes represented in OpenUSD.

### Importing Robots

Isaac Sim comes with a variety of robots already imported. The pre-imported robots can be found on the [Robot Assets](../assets/usd_assets_robots.html#isaac-assets-robots) page. Isaac Sim also provides advanced options for importing other robots.

If your robot is in [URDF](https://wiki.ros.org/urdf), you can use the [URDF Importer Extension](../importer_exporter/ext_isaacsim_asset_importer_urdf.html#isaac-sim-urdf-importer) extension from the GUI or from Python. This extension will import the visual meshes and the prim hierarchies (child-parent relationships), along with extra information about how the collision meshes, joints, and sensors are encoded.

You could also use the [Onshape Importer](https://docs.omniverse.nvidia.com/extensions/latest/ext_onshape.html) and [MJCF Importer Extension](../importer_exporter/ext_isaacsim_asset_importer_mjcf.html#isaac-sim-mjcf-importer). With these importers, you will have to add the joint drives in
and may have to tune them. The [Gain Tuner Extension](../robot_setup/ext_isaacsim_robot_setup_gain_tuner.html#isaac-gain-tuner) allows you to visualize and tune the joints.

## Scene Setup

You can set up the scene after all the necessary assets are converted to OpenUSD and
imported into Isaac Sim.

To properly simulate real world situations, you must have physics characteristics defined. For example, physics characteristics define if an object is subject to gravity or how solid it is.

### Adding Physics

After importing the required assets into Isaac Sim, make sure they have appropriate
Physics for accurate simulations. Some asset importers like the URDF and Onshape Importer carry over
most Physics parameters and configurations, for the rest of the imported assets adding
physics before proceeding would be necessary. The [NVIDIA Omniverse™ Physics simulation
extension](https://docs.omniverse.nvidia.com/extensions/latest/ext_physics.html#physics-core)
is powered by the NVIDIA PhysX SDK. It supports Rigid Body Simulation,
Character Control, Deformable Body Simulation, Particle Simulation, and Articulations. The
important steps for adding Physics to your scene are:

> 1. Creating the physics scene
> 2. Assigning collision settings
> 3. Adding joints and drives.

#### Creating the Physics Scene

The first step is to create a Physics Scene and ensure that the default parameters
for it are acceptable. For example, verify the direction and magnitude of gravity in
the scene. If the imported scene does not contain a ground plane, make sure to add
one before proceeding. It will prevent any physics-enabled objects from falling
below it. Unless you are simulating hundreds of rigid bodies and robots, it is more
efficient to use the CPU solver instead of the GPU solver.
Refer to the [Tutorial 1: Stage Setup](../robot_setup_tutorials/tutorial_intro_environment_setup.html#isaac-sim-app-tutorial-intro-environment-setup) tutorial

#### Assigning Collision Settings

[Collision](https://docs.omniverse.nvidia.com/kit/docs/omni_physics/latest/dev_guide/rigid_bodies_articulations/rigid_bodies.html#create-a-rigid-body-with-a-collider)
enables rigid bodies to interact with each other in an environment. The
geometry of the object can be approximated by convex hull, convex decomposition,
bounding sphere, bounding box, and SDF collision meshes. Each of them
approximates the geometry using different methods and may be better suited for
specific use cases. PhysX supports exact representations for Cube, Capsule, and
Sphere shapes. Cones and Cylinders are supported through the custom geometry
flag and are particularly useful when setting collision approximations for wheels of
robots. [Rigid-body physics materials](https://docs.omniverse.nvidia.com/kit/docs/omni_physics/latest/dev_guide/rigid_bodies_articulations/rigid_bodies.html#configure-rigid-body-s-material-properties)
provide friction, restitution (a.k.a. ‘bounciness’), and material density properties

#### Adding Joints and Drives

After adding the appropriate collision meshes to prims in the scene, we need to
ensure that they interact correctly with one another. We can do this by defining
appropriate joints between prims connected to each other. Joints give you the
ability to connect physics objects by defining how the objects may move relative to
each other. There are various [joints types](https://docs.omniverse.nvidia.com/kit/docs/omni_physics/latest/dev_guide/rigid_bodies_articulations/joints.html)
to select from including revolute, prismatic, spherical, fixed, etc.

### Adding Sensors

Isaac Sim sensor simulation extensions can simulate ground truth perception and
physics-based sensors, and has a library of realistic sensor models. You can simulate
camera, lidar, radar, and physics-based sensors. It is possible to use camera calibration
parameters obtained from OpenCV or ROS by converting them to Isaac Sim units, refer to the [Camera Sensors](../sensors/isaacsim_sensors_camera.html#isaacsim-sensors-camera) page.
RTX Lidar and Radar sensors are simulated at render time on the GPU with RTX hardware. A variety of physics-based sensors
like contact sensors, IMUs sensor, force sensor, effort sensor, and proximity sensor are also included. These sensors can be added
at the appropriate locations in the stage hierarchy (for example, a camera or lidar might be
added near the front/top of the robot). The [Camera and Depth Sensors](../assets/usd_assets_camera_depth_sensors.html#isaac-assets-camera-depth-sensors) and [Non-Visual Sensors](../assets/usd_assets_nonvisual_sensors.html#isaac-assets-nonvisual-sensors) pages
highlight all the available physical sensor assets available with Isaac Sim

### Import and Create Materials

[Materials](https://docs.omniverse.nvidia.com/materials-and-rendering/latest/materials.html#omniverse-materials) in Isaac Sim
are supported using [NVIDIA Material Definition Language (MDL)](https://www.nvidia.com/en-us/design-visualization/technologies/material-definition-language/) ,
a shading language designed for defining and describing the appearance
of materials in computer graphics. It allows artists and developers to create highly realistic
materials by specifying their physical properties, surface characteristics, and how they
interact with light. Omniverse comes with several template materials, including a physically
based glass; several general purpose multi-lobed materials useful for dielectric and
non-dielectric materials, skin, hair, liquids and other materials requiring subsurface
scattering or transmissive effects; and USD’s UsdPreviewSurface.

## Interaction with Digital Twin

Once the assets have been imported and the scene has been set up, there are various ways
to interact with the simulated environment, which are summarized below.

### GUI

The GUI provides intuitive controls for scene management, object manipulation, and
real-time monitoring, providing a streamlined interface for developing and testing robotic
systems. Pre-packaged examples, robots and environments can easily be accessed and
added to the scene via the GUI. Create tools make it easy to assemble, illuminate, simulate,
and render scenes large and small, therefore making it the ideal place to build your virtual
worlds, assemble robots, and examine physics. Refer to the [GUI Reference](../gui/index.html#isaac-sim-gui-tutorials-page) for
getting started with the GUI tutorials.

### Standalone Python

Isaac Sim provides a built-in [Python Environment](../python_scripting/manual_standalone_python.html#isaac-sim-python-environment) that packages can use, like a
system-level Python install. This is the recommended environment for running Python
Scripts with Isaac Sim. All Isaac Sim libraries and dependencies can be imported and
accessed through this Python environment. It also allows users to script and run their
entire worflkow headlessly. For using libraries and tools which are not a part of Isaac Sim,
ensure that they work with Python 3.11 first. A collection of standalone python examples is
provided with Isaac Sim and serves as a good starting point to understand the overall
steps involved. Jupyter notebook and Visual Studio Code support is also available. Workflows from the GUI
can be completely scripted in Python and can be run in headless mode too.

### Extensions

Extensions enable developers to add functionality and integrate other tools for Isaac Sim.
They are individually built application modules. All the tools used in Isaac Sim are built as
extensions. Various extensions enable easier interaction with sensors, robots and prims in
the scene. The ROS 2 Bridge extension can be used to connect your ROS packages and
code to Isaac Sim. Developers can write their own extensions in C++, Python or a
combination of both.

### OmniGraph

[OmniGraph](https://docs.omniverse.nvidia.com/extensions/latest/ext_omnigraph.html) is the visual scripting language
for Omniverse. It is not a single type of graph, but a composition of many different graph systems
under a single framework. Many Isaac Sim extensions provide nodes for building graphs for common
use cases. Core, sensor, and ROS extensions are a few examples that contain such OmniGraph Nodes.

## Use Cases

### Synthetic Data Generation (SDG)

Developers can generate physically accurate synthetic data that can enhance the training
and performance of AI perception networks used for robotics using
[Omniverse Replicator](https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator.html).
Replicator is a collection of extensions, Python APIs, workflows, and tools that enable
synthetic data generation tasks.

Once the scene has been set up, Replicator can be used to modify and randomize various
features like position, rotation, lighting, size, and textures of assets in the scene. A wide
range of annotations are supported including 2D bounding boxes, 3D bounding boxes,
semantic and instance segmentation masks, normals, depth, pointclouds, and more, with
data being written in common formats like COCO and KITTI formats. Custom annotators
and writers can also be implemented for advanced use cases like pose estimation. This
enables developers to seamlessly integrate the generated data with their training pipelines

To get started, developers can leverage the Python API provided by Omniverse Replicator
for generating synthetic data. The same scripts can be used to generate data headlessly in
the cloud through the Isaac Sim docker container (instructions [Container Installation](../installation/install_container.html#isaac-sim-app-install-container))
on a developer’s preferred CSP (AWS, Alibaba, Azure, GCP) with the [Cloud Deployment](../installation/install_cloud.html#isaac-sim-app-install-cloud) guide.
[Replicator YAML](https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator/yaml_workflow.html#replicator-yaml)
can be used for low-code situations where scripts can easily be edited by non-technical experts.
They offer a high level of portability and care suitable for cloud use cases.

### Software in the Loop (SIL)

Once the simulation scenario has been set up, developers can tune and test various
aspects of their robotics software stack. The insights gained after varying parameters and
configurations of the software stack and the simulated robot enable an easier and
accurate transition to the physical real-world robot. A few common use cases are
highlighted below:

#### Single and Multi-Robot Navigation

The navigation stack for a robot can be easily tested in various scenarios. The assets in the
environment can be randomized to come up with these scenarios. For running navigation
with multiple robots, a multi-GPU setup can be leveraged. Isaac Sim supports the ROS 2
Nav2 stack via the ROS 2 Bridge.

#### AI Model Evaluation

Evaluating models is easy in simulation because of direct access to ground truth which
could be through Physics, the state of a robot, or reading of a sensor. These can then be
compared with the model predictions to obtain the evaluation metrics.

For example, in computer vision tasks, the rendered image from the simulated camera can
be passed through the model for obtaining predictions. This can then be compared with
the ground truth (available directly from simulation or via Replicator) to obtain evaluation
metrics. This can also be done for other sensors like Lidars and can be easily extended to
multimodal applications

#### Perception

[Isaac Perceptor](https://developer.nvidia.com/isaac/perceptor) is a reference workflow of
NVIDIA-accelerated libraries and AI models that helps you quickly build robust autonomous
mobile robots (AMRs) to perceive, localize, and operate in unstructured environments like
warehouses or factories. It works with inputs from simulated environments in Isaac Sim

#### Manipulation

[Isaac Manipulator](https://nvidia-isaac-ros.github.io/reference_workflows/isaac_manipulator/index.html)
can be leveraged for manipulation tasks and verified in simulation. It is a
collection of GPU-accelerated packages for perception driven manipulation, providing
capabilities such as object detection and pose estimation. Time optimal collision-free
motion can be generated with cuMotion. Nvblox can be used for local 3D reconstruction
and obstacle detection. MoveIt is also supported via the ROS Bridge in Isaac Sim.

#### Reinforcement Learning

[Isaac Lab](../isaac_lab_tutorials/index.html#isaac-lab-tutorials-page) is a united and modular framework for robot learning that aims to simplify
common workflows in robotics research (such as RL, learning from demonstrations, and
motion planning). It is built upon NVIDIA Isaac Sim.

### Hardware in the Loop (HIL)

Hardware in the loop testing and evaluation can be done with Isaac Sim. The target
deployment device will receive all the data from the simulated robot and sensors which can
be fed to the needed software stacks/algorithms. ROS 2 can be leveraged as the
middleware which handles sending and receiving all the data from the simulation computer
to the target device. For example, a simulated camera from Isaac Sim will stream over all
the image data via the ROS 2 bridge from Isaac Sim to an
[NVIDIA Jetson Orin](https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-orin/), the
embedded device on the robot which will run the computer vision application. This is
particularly useful when selecting the target deployment device to verify it can run the
software stack needed before physically setting up the robot.

### CI/CD

#### OSMO

[OSMO](https://developer.nvidia.com/osmo)
is a cloud-native workow orchestration platform that lets you easily scale your
workloads across distributed environments — from on-premises to private and public
cloud. You can now apply for early access.

#### Sizing Calculator

Please refer to the [Isaac Sim Benchmarks](../reference_material/benchmarks.html#isaac-sim-benchmarks) page for Isaac Sim performance benchmarks
across multiple consumer and enterprise hardware configurations.

## Further Reading

Follow the relevant tutorials for a deeper dive into a corresponding section.

On this page

* [Geometry Authoring](#geometry-authoring)
* [Importing Assets](#importing-assets)
  + [Importing and Creating Environments](#importing-and-creating-environments)
  + [Importing Robots](#importing-robots)
* [Scene Setup](#scene-setup)
  + [Adding Physics](#adding-physics)
    - [Creating the Physics Scene](#creating-the-physics-scene)
    - [Assigning Collision Settings](#assigning-collision-settings)
    - [Adding Joints and Drives](#adding-joints-and-drives)
  + [Adding Sensors](#adding-sensors)
  + [Import and Create Materials](#import-and-create-materials)
* [Interaction with Digital Twin](#interaction-with-digital-twin)
  + [GUI](#gui)
  + [Standalone Python](#standalone-python)
  + [Extensions](#extensions)
  + [OmniGraph](#omnigraph)
* [Use Cases](#use-cases)
  + [Synthetic Data Generation (SDG)](#synthetic-data-generation-sdg)
  + [Software in the Loop (SIL)](#software-in-the-loop-sil)
    - [Single and Multi-Robot Navigation](#single-and-multi-robot-navigation)
    - [AI Model Evaluation](#ai-model-evaluation)
    - [Perception](#perception)
    - [Manipulation](#manipulation)
    - [Reinforcement Learning](#reinforcement-learning)
  + [Hardware in the Loop (HIL)](#hardware-in-the-loop-hil)
  + [CI/CD](#ci-cd)
    - [OSMO](#osmo)
    - [Sizing Calculator](#sizing-calculator)
* [Further Reading](#further-reading)

---

### Workflows

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/introduction/workflows.html

* Workflows

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Workflows

Isaac Sim is a component of larger solutions and can be used on its own. It consequently has multiple ways that you can use it to achieve the same thing. We refer to those different ways to do things as workflows. There are three main workflows when developing in Isaac Sim:

* GUI
* Extensions
* Standalone Python

We recommend that you go through the [Quick Start Tutorials](quickstart_index.html) to have a basic understanding of all of them and how they are interconnected.

## Workflows

Here is a summary of the key features and their recommended usages:

**GUI**

* **Key features**: Visual, intuitive, specialized tools for populating and simulating a virtual world.
* **Recommended usage**: World building, assemble robots, attach sensors, visual programming using OmniGraphs, and initializing ROS bridges.

**Extension**

* **Key features**: Runs asynchronously to allow interactions with the stage, *hot reloading* to reflect changes immediately, adaptive physics steps for real-time simulation.
* **Recommended usage**: Testing Python snippets, building interactive GUIs, custom application modules, and real-time sensitive applications.

**Standalone Python**

* **Key features**: Control over timing of physics and rendering steps, can be run in headless mode.
* **Recommended usage**: Large scale training for reinforcement learning, systematic world generation, and modification.

## Combining Workflows

Most of the actions that can be performed in the GUI, can be performed using Python. You can switch between performing actions in the GUI and in Python. Anything you make inside the GUI can be saved as part the USD file.

For example, you can create the world, include the actions needed for your robots using the GUI. Then pull the entire USD file into a standalone Python script and systematically modify properties there as needed.

### Extensions and the GUI

[Extensions](../reference_material/reference_glossary.html#isaac-sim-glossary-extensions) are the core building blocks of Omniverse Kit based applications. They are individually built application modules and can be used across different Omniverse applications. Most of the tools in Isaac Sim are built as extensions. You can enable and disable any set of extensions according to your project needs.

The **GUI workflow** uses a collection of extensions that are loaded by default at the start of Isaac Sim. These are general tools that are frequently used when building virtual worlds, robots, examining physics, rendering, material properties, profiling performance, and include tools for visual programming, for managing USD stage and assets, and for Robotics applications.

**Next steps**: Learn how to build your own extension with our [Templates](../utilities/templates_index.html#isaac-sim-templates), and explore our interactive examples in the [Examples Browser](examples.html#isaac-sim-app-intro-examples), all of which are extension-based.

### Python Standalone and in an Extension

The Extension and Standalone Python workflows use the same APIs for all the functions. However, they diverge for printing or commanding the robot joint states continuously.

**Python in an Extension** – The [Script Editor](https://docs.omniverse.nvidia.com/extensions/latest/ext_script-editor.html "(in Omniverse Extensions)") allows you to interact with the Stage asynchronously using Python. This means that the Python APIs are interacting with the USD stage.

The Python in extension runs without blocking rendering and physics stepping. If you want to interact with the physics and rendering steps or perform an action that is likely to be blocking, you would have to explicitly insert relevant callbacks and async functions for those functions to work. In the extension applications, rendering is stepping the moment viewport opens and physics is stepping when you press the **Play** button.

**Standalone Python** – To use the standalone Python version of Isaac Sim, you launch it using a Python script. Inside the script, you can control whether you open the GUI interface or run in headless mode.

In standalone Python, you can do step rendering and physics manually, which gives you the ability to guarantee that stepping only happens after the completion of a set of commands. These functions make the standalone workflow ideal for use cases, such as training behaviors where there might be randomization actions that all need to complete before the next step, or if you need to control message publishing rates in ROS, as well as running headless to increase performance.

**Next steps**: Learn how to run your first standalone application with [Hello World](../core_api_tutorials/tutorial_core_hello_world.html#isaac-sim-app-tutorial-core-hello-world), and how to use development tools such as [Jupyter Notebook](../development_tools/jupyter_notebook.html#isaac-sim-app-jupyter-notebook) or [Visual Studio Code (VS Code)](../development_tools/vscode.html#isaac-sim-app-vscode) for Python development.

## Hot Reloading for Extensions

Python-based Extensions also have the ability to “hot reload”. This means that you can change the underlying code while Isaac Sim is running, and then see the reflected changes in your application after saving the file, without shutting down or restarting Isaac Sim. This is a powerful feature that allows you to iterate quickly on your application.

## Review Examples

Review the:

* **Extension Examples** available in the [Examples Browser](examples.html#isaac-sim-app-intro-examples).
* **Standalone Examples** available in the `<isaac-sim-root-dir>/standalone_examples` folder.

On this page

* [Workflows](#id1)
* [Combining Workflows](#combining-workflows)
  + [Extensions and the GUI](#extensions-and-the-gui)
  + [Python Standalone and in an Extension](#python-standalone-and-in-an-extension)
* [Hot Reloading for Extensions](#hot-reloading-for-extensions)
* [Review Examples](#review-examples)

---

### User Interface Reference

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/gui/reference_user_interface.html

* User Interface Reference

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# User Interface Reference

[NVIDIA Omniverse™ Isaac Sim](../index.html#isaac-sim-app-overview) is built on [NVIDIA Omniverse](https://docs.omniverse.nvidia.com/) platform, so it shares the same UI elements as many Omniverse apps.

## Opening Page

Here’s a summary of the Isaac Sim frequently mentioned elements on the opening page. For more detailed view of all the elements on the page, go to [Omniverse User Interface](https://docs.omniverse.nvidia.com/composer/latest/interface.html "(in Omniverse USD Composer)").

| Ref # | Option | Result |
| --- | --- | --- |
| 1 | Menu Bar | Isaac Sim [Menu Bar](#isaac-sim-menu-bar) |
| 2 | Viewport | The primary way of viewing assets. See [Viewport](https://docs.omniverse.nvidia.com/extensions/latest/ext_core/ext_viewport.html "(in Omniverse Extensions)") for more details. |
| 3 | Main Toolbar | [Tool Bar](#toolbar) for manipulating the assets and start/stop simulation buttons are located. |
| 4 | Browsers | The default location for asset and example browsers. |
| 5 | Stage | The Stage window allows you to see all the assets in your current USD Scene. See the [Stage](https://docs.omniverse.nvidia.com/extensions/latest/ext_core/ext_stage.html "(in Omniverse Extensions)") docs for more details. |
| 6 | Property Panel | The window that displays the details of selected prim. See [Property Window](https://docs.omniverse.nvidia.com/extensions/latest/ext_core/ext_property-panel.html "(in Omniverse Extensions)") for more details. |

## Menu Bar

The Isaac Sim menu layout may be different from the layout of other Omniverse applications. Here are the ones unique to Isaac Sim.

| Ref # | Option | Result |
| --- | --- | --- |
| 1 | Create | The menu for creating various primitives and other simulation objects |
| 2 | Window | Opens various windows of loaded extensions, in this case, the ones composing the GUI and other extensions |
| 3 | Tools | The menu of available simulation tools for animation, physics, replicator, robotics, and USD |
| 4 | Utilities | Access various diagnostic and developer utilities such as debugging and extension templates |
| 5 | Layout | Opens menu for selecting preferred gui layouts |

## Tool Bar

| Icon | Menu Item | Action |
| --- | --- | --- |
| / | [Selection Modes](selection-modes.html) | Allows user to pick select and object in the viewport.  This is also the default viewport mouse behavior. |
| / | Move (Global / Local) | Instantiates a user widget that allows user to move a  selected object or group of objects |
|  | Rotate (Global / Local) | Instantiates a user widget that allows user to rotate  a selected object or group of objects |
|  | Scale | Instantiates a user widget that allows user to scale a  selected object or group of objects |
|  | Snap (enable/disable) | Sets snapping to specified increments or surface snap. |
|  | Select Mode | Toggles transform widgets between local and global  translation modes |
|  | * Play | Start an animation |
|  | * Stop | Stop an animation |

Note

Tools with a small triangle below their icon denotes additional options are available by right clicking the icon.

## Tabs

The Layout of the windows can be rearranged by moving the tabbed windows around, and docking them to different locations.

1. Panel Being Dragged (See Note below).
2. Panels Original location.
3. Acceptable Docking Locations.

Note

A tab can be “torn-off” and moved to another panel or window by click-hold-drag on the tabs title-bar and dragging it to another location or UI pane.

### OS Tabs

Certain tabs in the interface can be detached from the main window, which can be useful on multiple monitors and wide aspect ratio monitors.

To Detach a Tabbed panel use the following procedure.

1. `Right Click` on a `Tab` to invoke the `Move to New OS Window` option.
2. `Left Click` Select `Move to OS Window` action.
3. Position the window wherever you wish by using `Left-Click` + Dragging.

## Grab Handles

Grab handles are found in all Omniverse Apps and allow you to resize panels.

1. Grab Handle.

They are “invisible” UI element dividers that, when rolled over, will illuminate and can be click-dragged. This allows for UI customization, which is especially helpful in managing window content.

Note

Sliding is restricted to horizontal or vertical only.

### See Also

* [Omniverse User Interface](https://docs.omniverse.nvidia.com/composer/latest/interface.html "(in Omniverse USD Composer)") - Detailed overview of Omniverse UI elements
* [Viewport](https://docs.omniverse.nvidia.com/extensions/latest/ext_core/ext_viewport.html "(in Omniverse Extensions)") - In-depth guide to the viewport functionality
* [Stage](https://docs.omniverse.nvidia.com/extensions/latest/ext_core/ext_stage.html "(in Omniverse Extensions)") - Comprehensive documentation of the Stage window
* [Property Window](https://docs.omniverse.nvidia.com/extensions/latest/ext_core/ext_property-panel.html "(in Omniverse Extensions)") - Detailed guide to the Property Panel

On this page

* [Opening Page](#opening-page)
* [Menu Bar](#menu-bar)
* [Tool Bar](#tool-bar)
* [Tabs](#tabs)
  + [OS Tabs](#os-tabs)
* [Grab Handles](#grab-handles)
  + [See Also](#see-also)

---

### Keyboard Shortcuts Reference

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/gui/reference_keyboard_shortcuts.html

* Keyboard Shortcuts Reference

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Keyboard Shortcuts Reference

Keyboard shortcuts can reduce the amount of clicking one must do by providing “hot keys” that allow for “one touch” operation.

## Most Commonly Used Shortcuts

The gizmos for manipulating an object are on the left hand side toolbar.

> * Press “W” or click on the Move Gizmo to drag and move, for example, a Cube. You can move it in only one axis by clicking on the arrows and drag, in two axes by clicking on the colored squares and drag, or in all three axes by clicking on the dot in the center of the gizmo and drag.
> * Press “E” or click on the Rotate Gizmo to rotate.
> * Press “R” or click on the Scale Gizmo to scale. You can scale in one dimension by clicking on the the arrows and drag, two dimensions by clicking on the colored squares and drag, or in all three dimensions by clicking on the circle in the center of the gizmo and drag.
> * Press “ESCAPE” to deselect an object.

## Viewport Controls

| Input | Alternate Input | Result |
| --- | --- | --- |
| RMB + W | RMB + Up Arrow | Move Forward |
| RMB + S | RMB + Down Arrow | Move Backward |
| RMB + A | RMB + Left Arrow | Move Left |
| RMB + D | RMB + Right Arrow | Move Right |
| RMB + Q | RMB + Page Up | Move Up |
| RMB + E | RMB + Page Down | Move Down |
| Scroll Wheel | Opt + RMB | Zoom |
| LMB |  | Select |
| ESCAPE |  | Deselect |
| Select + ‘F’ |  | Zoom Camera to Selected Objects |
| Deselect + ‘F’ |  | Zoom Camera to All |
| Opt + LMB |  | Orbit about the Viewport Center |
| MMB (Hold) |  | Pan |
| RMB (Hold) |  | Pivot Camera |
| RMB (Click) |  | Invoke Contextual Menus |
| Shift + H |  | Show / Hide Grid and HUD information |
| F7 |  | Enables and disables the visibility of the UI |
| F11 |  | Toggles full screen mode |
| F10 |  | Capture Screen Shot |

Note

While using any move command, Shift can be held to double the movement speed. Control can be used to halve the movement speed.

## Selection

| Input | Alternate Input | Result |
| --- | --- | --- |
| Ctrl + A |  | Selects all assets in the current scene |
| Ctrl + I |  | Selects all assets not selected and deselects all selected assets |
| Esc |  | Deselects all assets in the current scene |

## File Operations

| Input | Alternate Input | Result |
| --- | --- | --- |
| Ctrl + S |  | Save File |
| Ctrl + O |  | Open File |

## Asset Control

| Input | Alternate Input | Result |
| --- | --- | --- |
| Del |  | Deletes selected asset |
| Ctrl + Shift + I |  | Create an instance of the current asset |
| Ctrl + D |  | Duplicates current asset |
| Ctrl + G |  | Groups selected assets into a container |
| H |  | Toggles selected asset visibility |

## Animation Controls

| Input | Alternate Input | Result |
| --- | --- | --- |
| Space |  | Plays/Pauses animations |

## Custom Hotkeys

You can create your own custom hotkey combinations to work faster and more effectively by using the [Hotkeys Extension](https://docs.omniverse.nvidia.com/extensions/latest/ext_core/ext_hotkeys.html "(in Omniverse Extensions)").

On this page

* [Most Commonly Used Shortcuts](#most-commonly-used-shortcuts)
* [Viewport Controls](#viewport-controls)
* [Selection](#selection)
* [File Operations](#file-operations)
* [Asset Control](#asset-control)
* [Animation Controls](#animation-controls)
* [Custom Hotkeys](#custom-hotkeys)

---

### Asset Structure

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/robot_setup/asset_structure.html

* Asset Structure

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Asset Structure

The Isaac Sim Imported assets are organized in a specific structure to make it easier to manage, reuse, and simulate them.
Each asset is broken down into multiple components, such as geometries, materials, instances, physics, and robot.

## The benefits of this structure are:

* Separation of USD components into multiple files for reviewing
* Isolate attributes for different physics engines to prevent clashing
* Use of layers, payloads, and variants for different robot use cases.
* Store different physics tuning parameters for different physics engines
* Ascii based structure is easy to read and edit by hand, as well as track changes with version control systems.

### Asset Source

Assets in this stage represent their raw form as imported from their original file format. They are typically organized into:

1. **Base Asset (** `base.usda` **):** Contains the full structural hierarchy of the asset, such as robot assemblies.
2. **Geometries (** `geometries.usd` **):** Includes individual meshes.
3. **Instances (** `instances.usda` **)**: Composes geometries, materials, and colliders into visual and collision meshes.
4. **Materials (** `materials.usda` **)**: A collection of materials used by the asset.
5. **Physics (** `physics.usd` **)**: Includes the USD / Newton physics setup for the asset.
6. **MuJoCo (** `mujoco.usda` **)**: Includes the MuJoCo physics setup for the asset.
7. **PhysX (** `physx.usda` **)**: Includes the PhysX physics setup for the asset.
8. **Robot (** `robot.usda` **)**: Includes the robot schema for the asset.

### Expanding the asset structure

Through payloads and variants, the asset structure can be expanded to include more features.
Examples of such features are:

1. **End Effectors Stacks (** `gripper.usda` **)**: Adds end effector such as grippers or suction cups for simulations.
2. **Control Stack (** `control.usd` **)**: Adds specific control parameters for connecting controllers to the robot.
3. **ROS Integration Stack (** `ros.usd` **)**: Configures ROS OmniGraph for the robot for publishing and subscribing to ROS topics.

## Guidelines

* The source assets must remain unchanged to ensure that they can be re-imported seamlessly without losing downstream modifications.
* Consistency is critical. The structural hierarchy, naming conventions, and part assemblies must remain intact.

## Transformation

This stage prepares the asset for simulation by reorganizing and optimizing it. This transformation is necessary when the
source asset contains nested rigid bodies or a complex structure that doesn’t meet the requirements of simulation.
The structure must be flattened with rigid bodies organized into a basic list, and meshes must be simplified to minimize their total count.
The transformation process includes:

* **Reorganizing Structure**:

  > + Create the simulation structure (for example, separating visuals and colliders as needed).
  > + Adjust the hierarchy to fit simulation requirements.
* **Optimizing Meshes**:

  > + Merge meshes that will function as a single rigid body.
  > + Simplify the material count into a single visual material list.
  > + Clean and format meshes as instantiable references to enhance performance.

Note

If the **asset source** is already in a format suitable for simulation, this step or parts of it can be skipped.

### Features

Simulation features are added in this stage and each feature is defined as a separate lightweight layer that builds on
top of the transformed asset.
These features include, but are not limited to, physics setups, sensor configurations, and control graphs.

## Workflow for Adding and Modifying Features

1. Create a new empty stage or open the existing feature stage.
2. Add the **optimized asset** (`asset_sim_optimized.usd`) as a sub-layer.
3. Modify the root layer to add/modify the feature.
4. Remove or disable the sub-layer (optimized asset) from the stage composition before saving.
5. Add the feature to the final asset as a **payload**. Optionally, a Variant set can be configured to enable quick switching between different feature sets by selecting them on a list.

## Example Features

* **Physics (** `physics.usd` **)**: Adds rigid bodies, joints, and articulations.
* **MuJoCo (** `mujoco.usda` **)**: Adds MuJoCo physics specific setup.
* **Control Graphs (** `asset_control.usd` **)**: Adds control features for simulations.
* **ROS Integration (** `asset_ros.usd` **)**: Configures ROS OmniGraph functionalities.
* **Gripper (** `robotiq_2f_140.usda` **)**: Adds gripper features for simulations.

### Composition of Final Asset

The final composed asset is represented in the `asset.usd` file, which integrates all the necessary components for simulation. This is achieved through the following composition process:

* **Sublayers**:
  :   + The neutral physics asset (`physics.usda`) is included as a sublayer for `physx.usda` and `mujoco.usda` to provide the core physics setup.
* **Payloads**:
  :   + Features such as end effectors (`gripper.usda`) and control graphs (`asset_control.usda`) are dynamically added as payloads. This allows for flexible and efficient loading of components.
* **References**:
  :   + The physics setup (`base.usda`) is added as a reference to the default prim, ensuring a consistent simulation-ready configuration.
* **Variants**:
  :   + Variants can be configured in the `physx.usda` or `mujoco.usda` file to enable different physics setups, without duplicating the asset.

This modular approach ensures that the final asset file is both lightweight and highly flexible, making it easy to adapt to
different simulation scenarios.

To keep assets organized and maintainable, it is recommended that you follow the structure and guidelines outlined above.
This will help streamline the asset creation process and improve overall simulation performance.

It is also suggested that you keep the assets organized in folders, with the source assets in their own folder, and
all features in a features folder, while the final asset is saved in the root folder. By default Isaac Sim importers for
robots follow this structure.

## Robot Schema

The [Robot Schema](../omniverse_usd/robot_schema.html#isaac-sim-robot-schema) provides a way to describe the robot structure agnostic of the simulation asset structure.
The robot schema must be included as a sublayer on the robot asset.

### Key Definitions and Notes

* **Add-ons**:
  - Features that have the simulation asset as a temporary sublayer used during feature creation. It is called the Add-on. The sublayer connection is broken before saving the feature asset.
* **Payloads**: Dynamically loadable components that reduce memory overhead and improve modularity.

### File-by-file explanation for the Inspire Hand asset

The following walkthrough explains the role of each source file and where to author changes.
This mirrors USD Asset Structure 3.0 guidance used in Isaac Sim 6.0 and helps keep assets
modular across physics runtimes.

1. `geometries.usd` - Mesh data only

   * Stores mesh topology and vertex data in binary USD for performance.
   * Should not contain physics tuning, robot metadata, or runtime-specific attributes.
   * Edit this layer when geometry itself changes (for example, after CAD updates).

   Example:

   ```python
   def Mesh "right_thumb_1"
   {
       int[] faceVertexCounts = [4, 4, 4]
       int[] faceVertexIndices = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
       point3f[] points = [(0, 0, 0), (0.01, 0, 0), (0.01, 0.02, 0), (0, 0.02, 0)]
   }
   ```
2. `materials.usda` - Material definitions

   * Contains material prims and shader bindings (for example MDL shader attributes).
   * Keeps look-development separate from geometry and simulation logic.
   * Edit this file when changing visual appearance without touching structure or physics.

   Example:

   ```python
   def Material "Plastic_ABS"
   {
       prepend token outputs:mdl:surface.connect = </Materials/Plastic_ABS/Shader.outputs:out>

       def Shader "Shader"
       {
           token info:implementationSource = "sourceAsset"
           asset info:mdl:sourceAsset = @../Materials/Plastic_ABS.mdl@
           token info:mdl:sourceAsset:subIdentifier = "Plastic_ABS"
           color3f inputs:diffuse_tint = (1, 1, 1)
       }
   }
   ```
3. `instances.usda` - Mesh, material, and collider assembly

   * References mesh prims from `geometries.usd` and applies materials.
   * Common place to define visual vs. collision mesh composition and collision approximation.
   * Edit this file for collider representation choices (for example convex hull vs. mesh).

   Example:

   ```python
   def Xform "right_thumb_1" (
       prepend references = @geometries.usd@</Geometries/right_thumb_1>
   )
   {
       over "right_thumb_1" (
           apiSchemas = ["PhysicsCollisionAPI", "PhysicsMeshCollisionAPI"]
       )
       {
           token physics:approximation = "convexHull"
           token purpose = "guide"
       }
   }
   ```
4. `robot.usda` - Robot schema and metadata

   * Applies Isaac robot schema and robot-level metadata (description, namespace, joint rels).
   * Keeps robot identity and metadata separate from visual and physics composition.
   * Edit this file for robot metadata and schema relationships, not for mesh or dynamics.

   Example:

   ```python
   over "inspire_hand" (
       prepend apiSchemas = ["IsaacRobotAPI"]
   )
   {
       string isaac:description = "Inspire RH56DFX hand"
       string isaac:namespace = "inspire_hand"
       rel isaac:physics:robotJoints = [</inspire_hand/Physics/right_thumb_1_joint>]
   }
   ```
5. `base.usda` - Simulation-ready structure

   * Organizes the transformed kinematic hierarchy and references reusable instances.
   * Defines transforms and structure used by downstream simulation feature layers.
   * Edit this layer when restructuring hierarchy for simulation compatibility.

   Example:

   ```python
   def Xform "right_thumb_1"
   {
       quatf xformOp:orient = (1, 0, 0, 0)
       float3 xformOp:scale = (1, 1, 1)
       double3 xformOp:translate = (0.01696, 0.02045, 0.0667)
       uniform token[] xformOpOrder = ["xformOp:translate", "xformOp:orient", "xformOp:scale"]

       def Xform "instance" (
           instanceable = true
           prepend references = @instances.usda@</Instances/right_thumb_1>
       )
       {
       }
   }
   ```
6. `physics.usda` - USD / Newton physics setup

   * Defines common physics setup: rigid bodies, masses, joints, and articulation structure.
   * Serves as a neutral physics layer that specialized runtimes build on.
   * Edit this file for core physical behavior that should apply across runtimes.

   Example:

   ```python
   def PhysicsRevoluteJoint "right_thumb_1_joint" (
       prepend apiSchemas = ["PhysicsDriveAPI:angular", "PhysicsJointStateAPI:angular"]
   )
   {
       uniform token physics:axis = "Z"
       prepend rel physics:body0 = </inspire_hand/r_base_link>
       prepend rel physics:body1 = </inspire_hand/right_thumb_1>
       float physics:lowerLimit = 0
       float physics:upperLimit = 75
   }
   ```
7. `mujoco.usda` - MuJoCo physics setup

   * Holds MuJoCo-specific attributes and tuning values.
   * Isolates MuJoCo behavior so it does not clash with PhysX or neutral physics.
   * Edit this file only for MuJoCo runtime tuning.

   Example:

   ```python
   over "right_thumb_1_joint"
   {
       custom string mujoco:actuatorType = "position"
       custom float mujoco:damping = 0.2
       custom float mujoco:frictionloss = 0.01
   }
   ```
8. `physx.usda` - PhysX physics setup

   * Holds PhysX-specific APIs and tuning (for example mimic setup or solver-related attributes).
   * Typically composes the neutral physics layer and adds PhysX-only details.
   * Edit this file for PhysX runtime behavior, not shared cross-engine behavior.

   Example:

   ```python
   over "right_thumb_4_joint" (
       prepend apiSchemas = ["PhysxJointAPI", "PhysxMimicJointAPI:rotX"]
   )
   {
       float physxMimicJoint:rotX:gearing = -0.7508
       float physxMimicJoint:rotX:naturalFrequency = 25
       rel physxMimicJoint:rotX:referenceJoint = </inspire_hand/Physics/right_thumb_3_joint>
   }
   ```
9. `interface.usda` - Final composed interface asset

   * Exposes the final robot prim that consumers load in simulation scenes.
   * Composes base structure by reference and adds optional features through payloads/variants.
   * Edit this file to control composition entry points and variant-driven feature selection.

   Example:

   ```python
   def Xform "inspire_hand" (
       prepend references = @payloads/base.usda@
       append variantSets = "Physics"
   )
   {
       variantSet "Physics" = {
           "none" {
           }
           "physics" (
               prepend payload = @payloads/Physics/physics.usda@
           ) {
           }
           "physx" (
               prepend payload = @payloads/Physics/physx.usda@
           ) {
           }
       }
   }
   ```

**Practical rule of thumb:**

* **Need to change shape or colliders?** Start in `geometries.usd` or `instances.usda`.
* **Need to change robot description/schema links?** Use `robot.usda`.
* **Need to change dynamics for all engines?** Use `physics.usd`.
* **Need engine-specific tuning?** Use `mujoco.usda` or `physx.usda`.
* **Need optional features or runtime switching?** Configure `asset.usd` payloads and variants.

On this page

* [The benefits of this structure are:](#the-benefits-of-this-structure-are)
  + [Asset Source](#asset-source)
  + [Expanding the asset structure](#expanding-the-asset-structure)
* [Guidelines](#guidelines)
* [Transformation](#transformation)
  + [Features](#features)
* [Workflow for Adding and Modifying Features](#workflow-for-adding-and-modifying-features)
* [Example Features](#example-features)
  + [Composition of Final Asset](#composition-of-final-asset)
* [Robot Schema](#robot-schema)
  + [Key Definitions and Notes](#key-definitions-and-notes)
  + [File-by-file explanation for the Inspire Hand asset](#file-by-file-explanation-for-the-inspire-hand-asset)

---


## SDG概念

### Synthetic Data Generation Index

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/index.html

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

### Synthetic Data Generation Index

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


## 入门

### Quick Start Isaac Sim

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/introduction/quickstart_isaacsim.html

* [Quick Tutorials](quickstart_index.html)
* Isaac Sim Basic Usage Tutorial

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Isaac Sim Basic Usage Tutorial

This tutorial covers the basics of Isaac Sim, including navigating the GUI, adding objects to the stage, looking up basic properties of objects, and running simulations.

In this tutorial, you will go from a blank stage to a moving robot using your choice of three different workflows. The purpose of including the three different workflows is to illustrate that Isaac Sim can be used in different ways depending on your needs.

You can review the scripts in both workflows to see how they differ. Comparing and contrasting can help you understand how to perform the exact same tasks:

* The **extension script** can be found in **Window > Examples > Robotics Examples**, then click on **Open Script** on the right upper corner of the browser.
* The **standalone script** can be found in the `<isaac-sim-root-dir>/standalone_examples/tutorials/` folder.

You can try the “hot-reloading” feature out by editing any of the scripts in the Extension examples. Save the file and see the changes reflected immediately without shutting down the simulator.

For a description of workflow concepts, see [Workflows](workflows.html#isaac-sim-app-tutorial-intro-workflows).

## Tutorial

There are three tabs for this tutorial, all three perform the same actions and reach the same outcome. Go through the full page under the same tab to learn about each workflow. Toggle between tabs to compare the different workflows or to perform the tutorial steps for your environment.

* GUI
* Extensions
* Standalone Python

GUI

Launch

1. Launch Isaac Sim from installation root folder.

   Linux

   ```python
   cd ~/isaacsim
   ./isaac-sim.sh
   ```

   Windows

   ```python
   cd C:\isaacsim
   isaac-sim.bat
   ```

   After the simulator is fully loaded, create a new scene:
2. From the top Menu Bar, click **File > New**. The first time you launch Isaac Sim, it may take a five - ten minutes to complete.

Add a Ground Plane

Add a ground plane to the scene:

1. From the top Menu Bar, click **Create > Physics > Ground Plane**.

Add a Light Source

You can add a light source to the scene to illuminate the objects in the scene. If you have a light source in the scene, but no object to reflect the light, the scene will still be dark.

Add a Distant Light source to the scene:

1. From the top Menu Bar, click **Create > Lights > Distant Light**.

Add a Visual Cube

A “visual” cube is a cube with no physics properties attached, for example, no mass, no collision. This cube will not fall under gravity or collide with other objects.

Add a cube to the scene:

1. From the top Menu Bar, click **Create > Shape > Cube**.
2. From the far left side of the UI locate the arrow icon and press **Play**. The cube does not do anything when simulation is running.

Move, Rotate, and Scale the Cube

Use the various gizmos on the left hand side toolbar to manipulate the cube.

1. Press “W” or click on the Move Gizmo to drag and move the cube. You can move it in only one axis by clicking on the arrows and drag, in two axes by clicking on the colored squares and drag, or in all three axes by clicking on the dot in the center of the gizmo and drag.
2. Press “E” or click on the Rotate Gizmo to rotate the cube.
3. Press “R” or click on the Scale Gizmo to scale the cube. You can scale it in one dimension by clicking on the the arrows and drag, two dimensions by clicking on the colored squares and drag, or in all three dimensions by clicking on the circle in the center of the gizmo and drag.
4. Press “esc” to deselect the cube.

For “Move” and “Rotate”, you can indicate if you are maneuvering in local or world coordinates. Click and hold on the gizmos to see the options.

You can make more precise modifications to the cube through its **Property** panel by typing in the exact numbers in the corresponding boxes. Click on the blue square next to the boxes to reset the values to default.

Add Physics and Collision Properties

Common physics properties are mass and inertia matrix, which are the properties that allow the object to fall under gravity. Collision Properties are the properties that allow the object to collide with other objects.

Physics and collision properties can be added separately, so you can have an object that collides with other objects but does not fall under gravity, or falls under gravity but does not collide with other objects. But in many cases, they are added together.

To add physics and collision properties to the cube:

1. Find the object (“/World/Cube”) on the stage tree and highlight it.
2. From the **Property** panel on the bottom right of the Workspace, click on the **Add** button and select **Physics** on the dropdown menu. This will show a list of properties that can be added to the object.
3. Select **Rigid Body with Colliders Preset** to add both physics and collision meshes to the object.
4. Press the **Play** button to see the cube fall under gravity and collide with the ground plane.

Extension

Launch

We will demonstrate the property of an Extension workflow using an existing Extension module called the “Script Editor”. The Script Editor allows the users to interact with the stage using Python. You will see that we will be mostly using the same Python APIs as in the Standalone Python workflow. The difference between the two workflows will become clear when we start to interact with the simulation timeline, especially in the [next tutorial](quickstart_isaacsim_robot.html#isaac-sim-app-intro-quickstart-robot).

Launch a fresh instance of Isaac Sim, go the top Menu Bar and click **Window > Script Editor**.
The code snippets in this tab are sections from one runnable script and should be executed in order.

Add a Ground Plane

To add a ground plane using the interactive Python, copy paste the following snippet in the Script Editor and run it by clicking the **Run** button on the bottom.

```python
import isaacsim.core.experimental.utils.stage as stage_utils
from isaacsim.core.experimental.objects import GroundPlane

stage_utils.create_new_stage()
GroundPlane("/World/GroundPlane", positions=[0, 0, 0])
```

Add a Light Source

You can add a light source to the scene to illuminate the objects in the scene. If you have a light source in the scene, but no object to reflect the light, the scene will still be dark.

1. Open a new tab in the Script Editor (**Tab > Add Tab**).
2. Add a light source by copy-pasting the following snippet in the Script Editor and running it.

```python
from isaacsim.core.experimental.objects import DistantLight

distant_light = DistantLight("/DistantLight")
distant_light.set_intensities(300)
```

Add a Visual Cube

A “visual” cube is a cube with no physics properties attached. No mass, no collision. This cube will not fall under gravity or collide with other objects. You can press **Play** to see that the cube does not do anything when the simulation is running.

1. Open a new tab in the Script Editor (**Tab > Add Tab**).
2. Add two cubes by copy-pasting the following snippet in the Script Editor and run it. We’ll keep one as visual-only, and add physics and collision properties to the other for comparison.

```python
from isaacsim.core.experimental.materials import PreviewSurfaceMaterial
from isaacsim.core.experimental.objects import Cube

yellow_material = PreviewSurfaceMaterial("/Materials/yellow")
yellow_material.set_input_values("diffuseColor", [1.0, 1.0, 0.0])

cyan_material = PreviewSurfaceMaterial("/Materials/cyan")
cyan_material.set_input_values("diffuseColor", [0.0, 1.0, 1.0])

visual_cube = Cube(
    paths="/visual_cube",
    positions=[0, 0.5, 0.5],
    sizes=0.3,
)
visual_cube.apply_visual_materials(yellow_material)

test_cube = Cube(
    paths="/test_cube",
    positions=[0, -0.5, 0.5],
    sizes=0.3,
)
test_cube.apply_visual_materials(cyan_material)
```

Isaac Sim Core API are wrappers for raw USD and physics engine APIs. You can add a visual cube (without physics and color properties) using raw USD API. Notice that the raw USD API is more verbose, but gives you more control over each property.

```python
import omni.usd
from pxr import Gf, UsdGeom

stage = omni.usd.get_context().get_stage()

path = "/visual_cube_usd"
cube_geom = UsdGeom.Cube.Define(stage, path)
cube_prim = stage.GetPrimAtPath(path)
size = 0.5
offset = Gf.Vec3f(1.5, -0.2, 1.0)
cube_geom.CreateSizeAttr(size)
if not cube_prim.HasAttribute("xformOp:translate"):
    UsdGeom.Xformable(cube_prim).AddTranslateOp().Set(offset)
else:
    cube_prim.GetAttribute("xformOp:translate").Set(offset)
```

Add Physics and Collision Properties

Common physics properties are mass and inertia matrix, which are the properties that allow the object to fall under gravity. Collision Properties are the properties that allow the object to collide with other objects.

Physics and collision properties can be added separately, so that you can have an object that collides with other objects but does not fall under gravity, or falls under gravity but does not collide with other objects. But in many cases, they are added together.

With the core APIs, you can add a new cube with physics and collision by creating a cube and then applying rigid body and collision APIs.

```python
from isaacsim.core.experimental.materials import PreviewSurfaceMaterial
from isaacsim.core.experimental.objects import Cube
from isaacsim.core.experimental.prims import GeomPrim, RigidPrim

red_material = PreviewSurfaceMaterial("/Materials/red")
red_material.set_input_values("diffuseColor", [1.0, 0.0, 0.0])

dynamic_cube = Cube(
    paths="/dynamic_cube",
    positions=[0, -1.0, 1.0],
    sizes=0.3,
    scales=[0.6, 0.5, 0.2],
)
dynamic_cube.apply_visual_materials(red_material)
RigidPrim(paths="/dynamic_cube")
GeomPrim(paths="/dynamic_cube", apply_collision_apis=True)
```

Alternatively, if you want to modify an existing object to have physics and collision properties, you can use the following snippet.

```python
from isaacsim.core.experimental.prims import GeomPrim, RigidPrim

RigidPrim(paths="/test_cube")
GeomPrim(paths="/test_cube", apply_collision_apis=True)
```

Click the **Play** button to see the cubes fall under gravity and collide with the ground plane.

Move, Rotate, and Scale the Cube

Moving an object using core API:

```python
from isaacsim.core.experimental.prims import XformPrim

translate_offset = [1.5, 1.2, 1.0]
orientation_offset = [0.7, 0.7, 0, 1]
scale = [1, 1.5, 0.2]

cube_prim = XformPrim(paths="/test_cube")
cube_prim.set_world_poses(translate_offset, orientation_offset)
cube_prim.set_local_scales(scale)
```

Moving an object using raw USD API:

```python
import omni.usd
from pxr import Gf, UsdGeom

stage = omni.usd.get_context().get_stage()
cube_prim = stage.GetPrimAtPath("/visual_cube_usd")
translate_offset = Gf.Vec3f(1.5, -0.2, 1.0)
rotate_offset = Gf.Vec3f(90, -90, 180)  # Note this is in degrees.
scale = Gf.Vec3f(1, 1.5, 0.2)

if not cube_prim.HasAttribute("xformOp:translate"):
    UsdGeom.Xformable(cube_prim).AddTranslateOp().Set(translate_offset)
else:
    cube_prim.GetAttribute("xformOp:translate").Set(translate_offset)

if not cube_prim.HasAttribute("xformOp:rotateXYZ"):
    UsdGeom.Xformable(cube_prim).AddRotateXYZOp().Set(rotate_offset)
else:
    cube_prim.GetAttribute("xformOp:rotateXYZ").Set(rotate_offset)

if not cube_prim.HasAttribute("xformOp:scale"):
    UsdGeom.Xformable(cube_prim).AddScaleOp().Set(scale)
else:
    cube_prim.GetAttribute("xformOp:scale").Set(scale)
```

Standalone Python

Launch

The script that runs Part I, [Isaac Sim Basic Usage Tutorial](#isaac-sim-app-intro-quickstart), is located in `standalone_examples/tutorials/getting_started/getting_started.py`.

To run the script, open a terminal, navigate to the root of the Isaac Sim installation, and run the following command:

Linux

```python
./python.sh standalone_examples/tutorials/getting_started/getting_started.py
```

Windows

```python
python.bat standalone_examples\tutorials\getting_started\getting_started.py
```

Code Explained

**Add a Ground Plane**

The lines inside `getting_started.py` that are relevant to adding a ground plane to the scene are below.

```python
from isaacsim.core.experimental.objects import GroundPlane

GroundPlane("/World/GroundPlane", positions=[0, 0, 0])
```

**Add a Light Source**

You can add a light source to the scene to illuminate the objects in the scene. If you have a light source in the scene, but no object to reflect the light, the scene will still be dark.

The lines inside `getting_started.py` that add a Distant Light are:

```python
from isaacsim.core.experimental.objects import DistantLight

distantLight = DistantLight("/DistantLight")
distantLight.set_intensities(300)
```

**Add a Visual Cube**

A “visual” cube is a cube with no physics properties attached. No mass, no collision. This cube will not fall under gravity or collide with other objects. You can press **Play** to see that the cube does not do anything when the simulation is running.

The lines inside `getting_started.py` that add a visual cube to the scene are:

```python
from isaacsim.core.experimental.materials import PreviewSurfaceMaterial
from isaacsim.core.experimental.objects import Cube

yellow_material = PreviewSurfaceMaterial("/Materials/yellow")
yellow_material.set_input_values("diffuseColor", [1.0, 1.0, 0.0])

visual_cube = Cube(
    paths="/visual_cube",
    positions=[0, 0.5, 1.0],
    sizes=0.3,
)
visual_cube.apply_visual_materials(yellow_material)
```

**Add Physics and Collision Properties**

Common physics properties are mass and inertia matrix, which are the properties that allow the object to fall under gravity. Collision properties are the properties that allow the object to collide with other objects.

Physics and collision properties can be added separately, so you can have an object that collides with other objects but does not fall under gravity, or falls under gravity but does not collide with other objects. But in many cases, they are added together.

With the experimental APIs, you spawn a cube with `Cube`, then apply rigid body and collision by wrapping the prim with `RigidPrim` and `GeomPrim`. The script creates a cube at `/dynamic_cube` and then applies physics and collision to it:

```python
from isaacsim.core.experimental.materials import PreviewSurfaceMaterial
from isaacsim.core.experimental.objects import Cube
from isaacsim.core.experimental.prims import GeomPrim, RigidPrim

cyan_material = PreviewSurfaceMaterial("/Materials/cyan")
cyan_material.set_input_values("diffuseColor", [0.0, 1.0, 1.0])

cube = Cube(
    paths="/dynamic_cube",
    positions=[0, -0.5, 1.5],
    sizes=0.3,
)
cube.apply_visual_materials(cyan_material)
RigidPrim(paths="/dynamic_cube")
GeomPrim(paths="/dynamic_cube", apply_collision_apis=True)
```

Move, Rotate, and Scale the Cube

The snippet below shows the lines that moved the objects in the scene using the core API.

```python
translate_offset = [1.5, 1.2, 1.0]
orientation_offset = [0.7, 0.7, 0, 1]  # quaternion wxyz
scale = [1, 1.5, 0.2]

cube_prim = XformPrim(paths="/visual_cube")
cube_prim.set_world_poses(translate_offset, orientation_offset)
cube_prim.set_local_scales(scale)
```

Save your work.

You can now proceed to [the next tutorial](quickstart_isaacsim_robot.html#isaac-sim-app-intro-quickstart-robot).

On this page

* [Tutorial](#tutorial)

---

### Quick Start with Robot

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/introduction/quickstart_isaacsim_robot.html

* [Quick Tutorials](quickstart_index.html)
* Basic Robot Tutorial

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Basic Robot Tutorial

This tutorial describes how to add a robot to the stage, move the robot, and examine the robot.

You must complete the previous [Isaac Sim Basic Usage Tutorial](quickstart_isaacsim.html#isaac-sim-app-intro-quickstart) before starting this one.

## Tutorial

GUI

Add a robot to Stage

1. Start with a new stage, **File > New Stage**.
2. Add robot to the scene, from the top Menu Bar, click **Create > Robots > Franka Emika Panda Arm**.

Examine the robot

Use the Physics Inspector to examine the robot’s joint properties.

1. Go to **Tools > Physics > Physics Inspector**. A window opens on the right.
2. Select Franka to inspect. The window will populate the joint information, such as the upper and lower limits as well as its default position by default.
3. Click on the hamburger icon on the top right to see more options, such as the joint stiffness and damping.
4. Optionally, make any changes to these values to see the robot move on the Stage corresponding to the change. A green check mark will appear.
5. To commit the changes to be the new default values for the robot, click the green check mark.

Control the Robot

The GUI-based robot controllers are inside the Omniverse visual programming tool, OmniGraphs. There are more involved tutorials about OmniGraph in the [OmniGraph](../omnigraph/index.html#isaac-sim-omnigraph-overview-page) section. For the purpose of this tutorial, we will generate the graph using a shortcut tool, and then examine the graph in the OmniGraph editor.

1. Open the graph generator by going to **Tools > Robotics > OmniGraph Controllers > Joint Position**.
2. In the newly appeared **Articulation Position Controller Inputs** popup window, click **Add** for the **Robot Prim** field.
3. Select **Franka** as the Target.
4. Click **OK** to generate the graph.

To move the robot:

1. In the Stage tab to the upper right, select **Graph > Position\_Controller**.
2. Select the **JointCommandArray** node. You can do this by either selecting the node on the Stage tree, or selecting the node in the graph editor.
3. In the **Property** tab to the lower right, you can see the joint command values. The **Inputs** under the **Construct Array Node** correspond to joints on the robot, starting with the base joint.
4. Press **Play** to start the simulation.
5. Click+hold+drag various value fields or type different values to see the robot arm change position.

To visualize the generated graph:

1. Open an graph editor window, **Window > Graph Editors > Action Graph**. The editor window opens in the tab below the Viewport tab that contains the robot.
2. Pull up the newly opened browser tab.
3. Click **Edit Action Graph** that is in the middle of the graph editor window.
4. Select the only existing graph on the list.
5. Select an array and review the **Stage** and **Property** tabs to see the values associated with each array node.
6. Select the **Articulation Controller** object in the graph to review its properties.

Extension

Add a robot to Stage

Start with a new Stage (File > New). To add a robot to the scene, copy-paste the following code snippet into the Script Editor and run it.

```python
import isaacsim.core.experimental.utils.stage as stage_utils
from isaacsim.core.experimental.prims import Articulation, XformPrim
from isaacsim.storage.native import get_assets_root_path

assets_root_path = get_assets_root_path()
asset_path = assets_root_path + "/Isaac/Robots/FrankaRobotics/FrankaPanda/franka.usd"
stage_utils.add_reference_to_stage(usd_path=asset_path, path="/World/Arm")

arm_transform = XformPrim("/World/Arm")
arm_transform.set_world_poses(positions=[0.0, 1.0, 0.0])

arm_handle = Articulation("/World/Arm")
```

Examine the robot

Isaac Sim Core API has many function calls to retrieve information about the robot. Here are some examples for finding the number of joints and the joint names, various joint properties, and joint states.

Open a new tab in the Script Editor, copy-paste the following code snippet. This can only be run after the previous adding robot step, where `arm_handle` has already been established. Press **Play** before running the snippet. Physics must be running for these commands to work.

```python
# Requires physics running (Press Play first). arm_handle from add_franka_to_stage snippet.
print("Number of joints:", arm_handle.num_dofs)
print("Joint names:", arm_handle.dof_names)
positions = arm_handle.get_dof_positions()
print("Joint positions:", positions)
```

Notice when you pressed “Run”, it only prints the state once, even if the simulation is running. You would have to keep pressing “Run” if you want to see more recent states. If you want to see the information printed at every physics step, you would need to insert these commands into a physics callback that runs at each physics step. We will go more in depth on how time stepping works in the next section [Workflows](workflows.html#isaac-sim-app-tutorial-intro-workflows).

To insert the commands into a physics callback, run the following snippet in a separate tab in the Script Editor.

```python
from isaacsim.core.simulation_manager import IsaacEvents, SimulationManager

def print_joint_positions_callback(dt, context):
    positions = arm_handle.get_dof_positions()
    print("Joint positions:", positions)

# Store callback_id to remove later if needed
callback_id = SimulationManager.register_callback(print_joint_positions_callback, IsaacEvents.POST_PHYSICS_STEP)
```

Start the simulation by pressing **Play**, then run the snippet. You should see the information printed at every physics step in the terminal.

If printing at every physics step is no longer necessary, you can remove the physics callback by running the following snippet. Use the `callback_id` that was returned when you registered the callback.

```python
from isaacsim.core.simulation_manager import SimulationManager

# callback_id was returned when registering the callback
SimulationManager.deregister_callback(callback_id)
```

Control the Robot

There are many ways to control the robot in Isaac Sim. The lowest level is sending direct joint commands to set position, velocity, and efforts. Here is an example of how to control the robot using the Articulation API at the joint level.

Open a new tab in the Script Editor, copy-paste the following code snippet. This can only be run after the previous “Add a robot to Stage” step, where `arm_handle` has already been established. Press **Play** before running the snippet. Physics must be running for these commands to work. The snippet sets the Franka arm to a target pose. If you have added the print-state callback above, you should see the printed joint values change as the robot moves.

```python
# Move arm to a target pose. arm_handle from add_franka_to_stage snippet.
# Franka has 9 DOFs: 7 arm joints + 2 finger joints
arm_handle.set_dof_positions([-1.5, 0.0, 0.0, -1.5, 0.0, 1.5, 0.5, 0.04, 0.04])

# To reset to default pose:
# arm_handle.set_dof_positions([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.04, 0.04])
```

Similar to the examine snippet above, `set_dof_positions` here is executed once when you press “Run”. If you wish to send commands at every physics step, you would need to insert these commands into a physics callback that runs at each physics step.

Standalone Python

The script that runs this tutorial is located in `standalone_examples/tutorials/getting_started/getting_started_robot.py`. To run the script, open a terminal, navigate to the root of the Isaac Sim installation, and run the following command:

Linux

```python
./python.sh standalone_examples/tutorials/getting_started/getting_started_robot.py
```

Windows

```python
python.bat standalone_examples\tutorials\getting_started\getting_started_robot.py
```

Code Explained

The `getting_started_robot.py` script sets up the scene and adds robots to the stage using the same core API as the Extension workflow. It imports the necessary modules, adds the ground plane and a distant light, sets the camera view, then adds two robots (a Franka arm and a Nova Carter) to the scene.

The notable differences between the Extension workflow and Standalone Python are:

**Starting the Simulator at the top**

The standalone script starts the simulation app and sets up the stage (create new stage, ground plane, add Franka and Carter). The following snippet illustrates the pattern: starting the app, then using the experimental API to create the stage and add the robot.

```python
from isaacsim import SimulationApp

simulation_app = SimulationApp({"headless": False})

import isaacsim.core.experimental.utils.stage as stage_utils
from isaacsim.core.experimental.objects import GroundPlane
from isaacsim.core.experimental.prims import Articulation, XformPrim
from isaacsim.storage.native import get_assets_root_path

assets_root_path = get_assets_root_path()
stage_utils.create_new_stage()
GroundPlane("/World/GroundPlane", positions=[0, 0, 0])

asset_path = assets_root_path + "/Isaac/Robots/FrankaRobotics/FrankaPanda/franka.usd"
stage_utils.add_reference_to_stage(usd_path=asset_path, path="/World/Arm")
arm_transform = XformPrim("/World/Arm")
arm_transform.set_world_poses(positions=[0.0, 1.0, 0.0])
arm = Articulation("/World/Arm")
```

**Stepping the simulation explicitly**

At the bottom of the script, a loop calls `SimulationManager.step()` and `RenderingManager.render()` every iteration to advance physics and rendering. The script runs for 4 cycles; in each cycle the arm and the car move or stop, and the car’s joint positions are printed at every physics step in the last cycle.

```python
from isaacsim.core.rendering_manager import RenderingManager
from isaacsim.core.simulation_manager import SimulationManager

# Move the arm
arm.set_dof_positions([-1.5, 0.0, 0.0, -1.5, 0.0, 1.5, 0.5, 0.04, 0.04])

for _ in range(100):
    SimulationManager.step()
    RenderingManager.render()
    simulation_app.update()
    # Print joint positions at every physics step
    joint_positions = arm.get_dof_positions()
    print("Joint positions:", joint_positions)
```

The `get_dof_positions` and `set_dof_positions` functions are the same as those used in the Extension workflow. Because stepping is explicit in standalone, these commands sit inside the loop and run every physics step by default. This is the main difference between the Extension and Standalone Python workflows. See the next section [Workflows](workflows.html#isaac-sim-app-tutorial-intro-workflows) for more details.

Save your work.

The next set of recommend tutorials are the GUI reference [Robot Setup Tutorials Series](../robot_setup_tutorials/index.html#isaac-sim-robot-setup-tutorials).

Or, you can continue to the next section to explore use-cases and capabilities of NVIDIA Isaac Sim by accessing a library of examples and demos in [Examples](examples.html#isaac-sim-app-intro-examples).

On this page

* [Tutorial](#tutorial)

---

### Quick Start Index

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/introduction/quickstart_index.html

* Quick Tutorials

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Quick Tutorials

If you are new to NVIDIA Isaac Sim, we recommend that you review the GUI references and complete the two tutorials listed below.

* [Isaac Sim Basic Usage Tutorial](quickstart_isaacsim.html)
* [Basic Robot Tutorial](quickstart_isaacsim_robot.html)
* [Tutorial Reference Table](tutorial_list.html)

In the *Quick Tutorials*, all the actions that can be performed in the GUI, can be performed using Python. You can switch between performing actions in the GUI and in Python. Anything you make inside the GUI can be saved as part the USD file.

For example, you can create the world, include the actions needed for your robots using the GUI. Then pull the entire USD file into a standalone Python script and systematically modify properties there as needed.

## For Beginners: Robot Setup Tutorials

If you are new to NVIDIA Isaac Sim and want to learn how to set up and rig robots, we **strongly recommend** exploring our comprehensive [Robot Setup Tutorials](../robot_setup_tutorials/index.html#isaac-sim-robot-setup-tutorials). These tutorials will teach you:

* How to set up environments and stages
* How to assemble and rig robots from basic shapes
* How to add joints, articulations, and sensors
* How to import and configure manipulators
* Advanced techniques for complex robot structures

The Robot Setup Tutorials are designed as a complete learning path that takes you from basic concepts to advanced robot rigging techniques. They are perfect for beginners who want to understand how to work with robots in Isaac Sim.

**Start here:** [Tutorial 1: Stage Setup](../robot_setup_tutorials/tutorial_intro_environment_setup.html#isaac-sim-app-tutorial-intro-environment-setup)

## What’s Next

After completing either the Robot Setup Tutorials or Quick Tutorials, explore these additional resources:

* **Examples and Demos:** Access a library of examples and demos in [Examples](examples.html#isaac-sim-app-intro-examples) to explore use-cases and capabilities of NVIDIA Isaac Sim
* **Available Assets:** Browse the [Assets](../assets/usd_assets_overview.html#isaac-assets-overview) section to see what assets are available to you
* **Advanced Python API:** See [Build a Robot using Core Python API](../core_api_tutorials/index.html#isaac-sim-core-api-tutorials-page) for more complex tutorials

On this page

* [For Beginners: Robot Setup Tutorials](#for-beginners-robot-setup-tutorials)
* [What’s Next](#what-s-next)

---


## 仿真概念

### Robot Simulation Core Concepts

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/robot_simulation/robot_simulation_core_concepts.html

* [Robot Simulation](index.html)
* Useful Links

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Useful Links

Some important concepts that are useful to understand when working with robot simulation in Isaac Sim are located in the following sections:

* [Physics Simulation Fundamentals](../physics/simulation_fundamentals.html#simulation-fundamentals): Provides basic summary about rigid bodies, colliders, joints, articulation, as well as simulation timelines and steps.
* [Core API Overview](../python_scripting/core_api_overview.html#isaac-sim-app-python-core-api-overview): Provides an overview of how the core API in Isaac Sim interfaces with the physics backend.

---

### Robot Simulation Tips

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/robot_simulation/robot_simulation_tips.html

* [Robot Simulation](index.html)
* Robot Simulation Tips

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Robot Simulation Tips

## Improve Simulation Performance

* You can speed up the simulation by reducing the number of objects in the scene, reducing the complexity of the objects in the scene, or reducing the number of simulation steps. For more information, see [Isaac Sim Performance Optimization Handbook](../reference_material/sim_performance_optimization_handbook.html#isaac-sim-performance-optimization-handbook) for more details.
* Alternatively, you can reduce the number of sensors, or reduce the resolution of sensors in the scene. See [Isaac Sim Benchmarks](../reference_material/benchmarks.html#isaac-sim-benchmarks) for more performance benchmarks.

## Simulation Time Stepping and Rendering Rate

* Adjust the physics step rate and the application’s loop / timeline rate. The physics step rate is set independently on the Physics Scene (or via `isaacsim.core.simulation_manager.SimulationManager.setup_simulation()`); lowering the application’s render rate via `isaacsim.core.rendering_manager.RenderingManager.set_dt()` does **not** automatically increase the number of physics substeps per frame. If you want more physics resolution, raise the Physics Scene’s `timeStepsPerSecond` (equivalently `SimulationManager.setup_simulation(dt=...)`); if you want fewer, lower it.
* For an end-to-end coherent rate change, call `SimulationManager.setup_simulation(dt=...)` and `RenderingManager.set_dt(...)` with the same `dt` so the three rate clocks stay aligned. See [Architecture: Timeline, Physics, and the Renderer](../sensors/isaacsim_sensors_multitick_rendering.html#isaac-sim-sensors-multitick-clock-relationships) for the relationship between the clocks.

### Alternatives to Animated USD with a Fixed Manual Step Size

The full Isaac Sim experience (`isaacsim.exp.full.kit`) enables Fixed Time Stepping by default so that `SimulationApp` and other scripted workflows step the timeline deterministically. Under Fixed Time Stepping, the timeline advances by a fixed `dt` per loop tick rather than by wall-clock time, so USD scenes that drive motion through time-sampled (`timeSample`) keyframes will appear to play back slower than real time whenever the renderer cannot sustain the target rate. The same content plays smoothly in USD Composer or in the Isaac Sim Base experience (`isaacsim.exp.base.kit`), both of which default to Variable stepping.

If you are authoring or simulating a scene where moving parts are driven by USD keyframes, prefer one of the following over leaving the content as an animated USD that relies on the default fixed manual step:

* **Drive the transforms procedurally each simulation tick.** Replace the time-sampled attributes on the moving prims with a per-step callback. The current API is `SimulationManager.register_callback(fn, event=SimulationEvent.PHYSICS_POST_STEP)` from `isaacsim.core.simulation_manager`; `add_physics_callback` on `SimulationContext` / `World` from the deprecated `isaacsim.core.api` namespace works equivalently for existing code. An OmniGraph triggered by the `OnPhysicsStep` node is the visual-scripting equivalent. Compute the pose from your own time variable — wall-clock `dt` for smooth GUI playback, simulation `dt` for determinism. This is the recommended pattern for scripted scenarios: it keeps determinism for `SimulationApp` and stays correct under any time-stepping mode.
* **Author the motion as articulated joints or rigid-body kinematics** rather than as keyframed transforms. Joint targets and kinematic bodies are advanced by the physics step, so the motion stays synchronized with simulation time regardless of render rate. This is also the right choice when other simulated objects need to interact with the moving parts.
* **Tune the loop rate to match the authored animation’s sample rate.** If you must keep the content as a keyframed USD and you are running interactively, set the main loop rate so that one fixed `dt` corresponds to one keyframe interval (for example, `--/app/runLoops/main/rateLimitFrequency=60` for a 60 FPS authored animation), and reduce scene cost (LODs, lighting, viewport resolution) until the renderer can hit that rate. While the renderer falls behind, timeline time will continue to lag wall-clock.
* **Switch the GUI to Variable stepping for review and authoring.** For animation review or content-authoring sessions where determinism is not required, launch with the flags listed in [Choppy or Slow Animation Playback (Fixed Time Stepping)](../overview/troubleshooting.html#isaac-sim-troubleshooting-animation-playback-slow) to opt the experience into Variable stepping. Do not use these flags for `SimulationApp` jobs that depend on a fixed per-step `dt`.

## Adjusting friction for wheeled robots

* add and adjust friction parameters to both the wheels and the ground. See [Adding Contact and Friction Parameters](../robot_setup_tutorials/tutorial_intro_assemble_robot.html#isaacsim-gui-add-physics-material) for instructions.
* Coefficient of friction is the ratio between between the normal force and the friction force. Increasing the Coefficient of static or dynamic friciton to a higher value will increase the friction force for the same normal force. Coefficient of friction should not exceed 1.0 in most cases.
* modify the frictiion combine mode to adjust how friction is computed between two objects.

## Gripper not picking up objects

* You can increase the friction parameters on both the fingers and object. See [Adding Contact and Friction Parameters](../robot_setup_tutorials/tutorial_intro_assemble_robot.html#isaacsim-gui-add-physics-material) for instructions.
* Use the Physics Authoring Toolbar (Tools > Physics Toolbar), especially the [Mass Distribution Tool](https://docs.omniverse.nvidia.com/kit/docs/omni_physics/latest/extensions/ux/source/omni.physx.supportui/docs/dev_guide/authoring_tools.html#mass-distribution-manipulator) to make sure the weight of the object and weight of the arms are reasonable.
* The gripper is not following your commands accurately, consider increase the stiffness and damping gains in the controller.

## Colliders

* Colliders should only be applied to the parts of the robot that need to interact with the environment.
* Use simple shape colliders (box, sphere, capsule, convex hull) or convex hull whenever possible for better performance.
* Only use convex decomposition colliders when necessary, such as tips of end effectors, as they are more computationally expensive. Adjust the Error Percentage, Shrink Wrap, and ofset parameters in the advanced tab for better accuracy.
* Apply collision filters to avoid unnecessary collision checks between parts of the robot that should not collide with each other, such as the rubber pads on the finger and the finger itself. Overlapping colliders can cause instability in the simulation and cause the robot to “explode”. Collision filters can be set via *Physics Collision Group*
* For dynamic collisions, use convex hull, convex decomposition, box, sphere, or SDF approximations only. Triangle mesh, and Mesh simplification only works for static objects.

## Masses

* For accurate simulation, the mass, center of mass, diagonal inertia, principal axes of the rigid body should be set using the MassAPI, and match the real world masses as closely as possible.
* If it’s not specified, the mass will be estimated based on the volume of the mesh, with dentisty set to 1000 kg/m^3 by default.

On this page

* [Improve Simulation Performance](#improve-simulation-performance)
* [Simulation Time Stepping and Rendering Rate](#simulation-time-stepping-and-rendering-rate)
  + [Alternatives to Animated USD with a Fixed Manual Step Size](#alternatives-to-animated-usd-with-a-fixed-manual-step-size)
* [Adjusting friction for wheeled robots](#adjusting-friction-for-wheeled-robots)
* [Gripper not picking up objects](#gripper-not-picking-up-objects)
* [Colliders](#colliders)
* [Masses](#masses)

---


## OpenUSD

### Intro to USD

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/omniverse_usd/intro_to_usd.html

* [Omniverse and USD](index.html)
* Working with USD

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Working with USD

## Learning Objectives

This tutorial covers how to:

* save USD stages
* load and reference existing USD stages
* Organize stage tree hierarchy

## Saving Options

* **Save**: To save the current USD stage, go to the Menu Bar and click *Files > Save* or *Files > Save As ..* to save as a new file.
* **Save Flattened As**: Saves the current USD file while merging all components to one mesh.
* **as .usda files**: You have the option to save as `.usda` file instead of `.usd` file. `.usda` file is a human-readable text file format for the given USD stage.
* **Collect Assets**: If your current stage used many reference USD stages, materials, and textures from other folders and servers, you must *Collect Assets* to make sure all the external references that are used in your stage get collected in one folder. To do so, save the current USD locally, then find it in the *Content* tab, right-click on it, and select *Collect Asset*.

try {
var kalturaPlayer = KalturaPlayer.setup({
targetId: "kaltura\_player\_1",
provider:
{ partnerId: 2935771, uiConfId: 46302491 }
});
kalturaPlayer.loadMedia(
{entryId: '1\_rhc2d1dw'}
);
} catch (e)
{ console.error(e.message) }

## Loading Options

* **Open**: To load a USD stage, go to Menu Bar and click *Files > Open*. This opens the USD stage for direct editing.
* **Add Reference**: *Files > Add Reference* adds a USD file as a reference. Or find the file in the *Content* Tab and drag it into the viewport. You can not edit the referenced USD.

### Set the Stage for a Reference

To demonstrate adding a file as reference, save the current stage with the cube and cylinders as a mock robot.
First, you must rearrange the rigid bodies on the stage into a hierarchical structure with meaningful names.
Put all the rigid body parts of the robot under a single [Prim](../reference_material/reference_glossary.html#isaac-sim-glossary-prim).

1. Right click inside the *Stage* tab, select *Create > Xform*.
2. Rename the newly added [Xform](https://docs.omniverse.nvidia.com/utilities/latest/common/glossary-of-terms.html#term-XForm "(in Omniverse Utilities)") to *mock\_robot*. The Prim appears under the *World* prim.
3. Drag and drop the Cube, both Cylinders, Physics Material, and Looks folder under *mock\_robot*.
4. Rename the Cube and Cylinders to the body, wheel\_left, and wheel\_right.
5. Save the stage as an USD file.

   > try {
   > var kalturaPlayer = KalturaPlayer.setup({
   > targetId: "kaltura\_player\_2",
   > provider:
   > { partnerId: 2935771, uiConfId: 46302491 }
   > });
   > kalturaPlayer.loadMedia(
   > {entryId: '1\_szx9q5qp'}
   > );
   > } catch (e)
   > { console.error(e.message) }
6. Open a new stage.
7. Load the USD file as a reference, either *Files > Add Reference* or drag the file from *Content* on to the stage. It loads the referenced USD under a Prim withe the same name as the USD filename.
8. Validate that it loaded everything under the original `World(defaultPrim)`, including `PhysicsScene`, `defaultLight`, and `GroundPlane`. This may not be optimal if you are loading multiple USD references that all have their own version of PhysicsScenes and defaultLights. You cannot delete them on the new stage because they are loaded by reference, but deleting them in the original USD would make it difficult to work within those USD stages.

To have the necessary environment set up in the USD stages but not export them when they are being referenced, you need to move non-referenced items out of the default Prim:

* Select the robot’s parent prim on stage, in this tutorial /mock\_robot.
* Open the menu *Edit* while the prim is selected, and click on *unparent*.
* Validate that instead of being under World, mock\_robot is parallel to World.
* Right-click on the robot prim again on stage, and *Set as a Default Prim*. Save.
* Open a new stage and load the same file again as a reference, verify that only the robot is imported.

try {
var kalturaPlayer = KalturaPlayer.setup({
targetId: "OVK1624\_Isaac-tutorial-gui-set-default-prim",
provider: {
partnerId: 2935771,
uiConfId: 53712482
}
});
kalturaPlayer.loadMedia({entryId: '1\_01lzd38n'});
} catch (e) {
console.error(e.message)
}

## Summary

In this tutorial, you learned how to save and open USD files.

### Further Readings

More on [File Menu](https://docs.omniverse.nvidia.com/composer/latest/menu_file.html "(in Omniverse USD Composer)"), [Collect Assets](https://docs.omniverse.nvidia.com/extensions/latest/ext_collect.html "(in Omniverse Extensions)"), and others in [Composer](https://docs.omniverse.nvidia.com/composer/latest/index.html "(in Omniverse USD Composer)").

On this page

* [Learning Objectives](#learning-objectives)
* [Saving Options](#saving-options)
* [Loading Options](#loading-options)
  + [Set the Stage for a Reference](#set-the-stage-for-a-reference)
* [Summary](#summary)
  + [Further Readings](#further-readings)

---

### OpenUSD

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/omniverse_usd/open_usd.html

* [Omniverse and USD](index.html)
* OpenUSD Fundamentals

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# OpenUSD Fundamentals

The language used in Isaac Sim to describe the robot and its environment is the [Universal Scene Description (USD)](https://openusd.org/release/index.html).

## Why USD?

USD enables seamless interchange of 3D content among diverse content creation apps with its rich, extensible language. With concepts of layering and variants, it’s a powerful tool that enables live collaboration on the same asset and scene. And when properly used, it permits working on assets without overwriting and erasing someone else’s work.

USD provides a text-based format for direct editing (*.usda). For higher performance and space optimization, there is a binary-encoded format (*.usd). All aspects of USD can be accessed through coding in C++ or Python.

APIs are available for you to set up a scene or tune a robot directly in USD, but, typically it is not necessary to use them.

## Hello World

Let’s start by creating a basic USD file from code:

```python
xformPrim = UsdGeom.Xform.Define(stage, "/hello")
spherePrim = UsdGeom.Sphere.Define(stage, "/hello/world")
# stage.GetRootLayer().SaveAs('/path/to/hello_world.usda')
print(stage.GetRootLayer().ExportToString())
```

Uncomment the line `stage.GetRootLayer().SaveAs('/path/to/hello_world.usda')` and replace `/path/to/` with the desired save folder, you can execute this code in the script editor (**Window > Script Editor**) in Isaac Sim, and it yields the following USD file:

```python
#usda 1.0

def Xform "hello"
{
    def Sphere "world"
    {
    }
}
```

This example contains a couple of powerful things we can take away from it:

* **Type**: Elements in USD (called *Prims*) have a defined type. In the case of `hello`, it is of type `Xform`, a type used everywhere, and it defines elements that contain a transform in the world. `World` is of type *Sphere*, which represents a primitive geometry.
* **Composition**: Prims can have *nested prims*. These nested prims are, for all effects, fully defined elements, with their own attributes.
* **Introspection**: If uncommented, the line `generic_spherePrim = stage.DefinePrim('/hello/world_generic', 'Sphere')` would yield a sphere just like the `/hello/world`. Prim types can be defined directly through their schema name.
* **Namespaces**: Both *Xform* and *Sphere* are part of the standard pxr namespace *UsdGeom*, a set of types that represent geometry elements in the scene.

You can open this USD file in Isaac Sim in the script editor window with:

```python
import omni

omni.usd.get_context().open_stage("/path/to/hello_world.usda")
```

### Inspecting and Authoring Properties

With a basic scene, you can start making modifications to the elements. Start by opening and getting the elements from the scene:

```python
xform = stage.GetPrimAtPath("/hello")
sphere = stage.GetPrimAtPath("/hello/world")
print(xform.GetPropertyNames())
print(sphere.GetPropertyNames())
```

The output for the code above is:

```python
['proxyPrim', 'purpose', 'visibility', 'xformOpOrder']
['doubleSided', 'extent', 'orientation', 'primvars:displayColor' 'primvars:displayOpacity', 'proxyPrim', 'purpose', 'radius', 'visibility', 'xformOpOrder']
```

USD offers polymorphism. If you review both lists you can see the common attributes. By having a common `XFormable` ancestor, Xforms and Spheres share a subset of properties, while sphere contains some unique elements that only make sense for its specialization (for example, *radius*).

To update these attributes, you can append the following to the code above:

```python
radiusAttr = sphere.GetAttribute("radius")
print(radiusAttr.Get())
radiusAttr.Set(0.50)
print(radiusAttr.Get())
```

Because the stage was still open from the previous sample, you’ll see the sphere reducing from radius 1.0 to 0.5, but it also prints these values in the console.

To move the sphere to a new position use `xformOpOrder`, which is common to `Xform` and `Sphere`. Many different transforms can be applied to a prim, each from potentially different layers. The `xformOpOrder` tracks and manages the different transforms, it is like a list of `Xform` operations, applied in the order specified from first to last.

Our sphere doesn’t have its own, so to create a new one:

```python
translation = Gf.Vec3d(1, 0, 0)
sphere_xformable = UsdGeom.Xformable(sphere)
move_sphere_op = sphere_xformable.AddTranslateOp(opSuffix="moveSphereOp")
move_sphere_op.Set(translation)
```

Notice that the sphere has jumped to a new position along the X-axis. Alternatively, you could apply the translation to the parent `xform` instead.

```python
translation = Gf.Vec3d(0, 0, 1)
xform_xformable = UsdGeom.Xformable(xform)
move_parent_op = xform_xformable.AddTranslateOp(opSuffix="moveParentOp")
move_parent_op.Set(translation)
```

Verify that you see the sphere jump to a new location, which is the composition of both the parent and child transforms.

A consequence of the universal nature of USD is that when you fetch a prim by path, it is always of type `prim` and needs to be cast appropriately before performing operations with or on it.

To create and bind a material to the prim to change its color, first create it:

```python
# create the material and shader
material_path = "/hello/material"
mat_prim = stage.DefinePrim(Sdf.Path(material_path), "Material")
material_prim = UsdShade.Material.Get(stage, mat_prim.GetPath())

shader_path = stage.DefinePrim(Sdf.Path("{}/Shader".format(material_path)), "Shader")
shader_prim = UsdShade.Shader.Get(stage, shader_path.GetPath())

with Sdf.ChangeBlock():
    # connect up the shader graph
    shader_out = shader_prim.CreateOutput("out", Sdf.ValueTypeNames.Token)
    material_prim.CreateSurfaceOutput("mdl").ConnectToSource(shader_out)
    material_prim.CreateVolumeOutput("mdl").ConnectToSource(shader_out)
    material_prim.CreateDisplacementOutput("mdl").ConnectToSource(shader_out)
    shader_prim.GetImplementationSourceAttr().Set(UsdShade.Tokens.sourceAsset)
    shader_prim.SetSourceAsset(Sdf.AssetPath("OmniPBR.mdl"), "mdl")
    shader_prim.SetSourceAssetSubIdentifier("OmniPBR", "mdl")

    omni.usd.create_material_input(
        mat_prim,
        "diffuse_color_constant",
        Gf.Vec3f(1, 0, 0),
        Sdf.ValueTypeNames.Color3f,
    )
    omni.usd.create_material_input(
        mat_prim,
        "emissive_color",
        Gf.Vec3f(1, 0, 0),
        Sdf.ValueTypeNames.Color3f,
    )
```

Material color shading is complicated. After creating the prim and appropriate attributes, you must link those attributes and properties together to form a `shader graph` that is processed to produce the desired material effect. After it’s created, the material can then be bound to the prim, thus changing its apparent color in the viewport.

```python
# bind the material
material = UsdShade.Material(material_prim)
binding_api = UsdShade.MaterialBindingAPI.Apply(sphere)
binding_api.Bind(material)
```

If you save the stage and examine the USDA file, you can see the material.

```python
#usda 1.0

def Material "material"
{
    token outputs:mdl:displacement.connect = </hello/material/Shader.outputs:out>
    token outputs:mdl:surface.connect = </hello/material/Shader.outputs:out>
    token outputs:mdl:volume.connect = </hello/material/Shader.outputs:out>

    def Shader "Shader"
    {
        uniform token info:implementationSource = "sourceAsset"
        uniform asset info:mdl:sourceAsset = @OmniPBR.mdl@
        uniform token info:mdl:sourceAsset:subIdentifier = "OmniPBR"
        color3f inputs:diffuse_color_constant = (1, 0, 0) (
            customData = {
                float3 default = (0.2, 0.2, 0.2)
            }
            displayGroup = "Albedo"
            displayName = "Albedo Color"
            doc = "This is the albedo base color"
            hidden = false
            renderType = "color"
        )
        color3f inputs:emissive_color = (1, 0, 0) (
            customData = {
                float3 default = (1, 0.1, 0.1)
            }
            displayGroup = "Emissive"
            displayName = "Emissive Color"
            doc = "The emission color"
            hidden = false
            renderType = "color"
        )
        token outputs:out
    }
}
```

and specifically, the `diffuse_color_constant` attribute type. To directly modify this attribute to change the color of our sphere:

```python
new_shader = UsdShade.Shader.Get(stage, "/hello/material/Shader")
new_shader.GetInput("diffuse_color_constant").Set(Gf.Vec3f(0, 0, 1))
```

Of course, this level of direct manipulation of USD can become tedious. For situations like this, there are a set of predefined commands through the kit API, which dramatically simplifies working with USD in code. For example, you could have done the following instead:

```python
omni.kit.commands.execute(
    "CreateAndBindMdlMaterialFromLibrary",
    mdl_name="OmniSurface.mdl",
    mtl_name="OmniSurface",
    mtl_created_list=["/Looks/OmniSurface"],
)

new_material = UsdShade.Material.Get(stage, "/Looks/OmniSurface")

binding_api = UsdShade.MaterialBindingAPI.Apply(sphere)
binding_api.Bind(new_material)
```

## Further Reading

For a complete tutorial on USD, see the [openUSD tutorials](https://openusd.org/release/tut_usd_tutorials.html). With a few tweaks, as shown on the basic examples above, these tutorials can be run from the Script editor or in the [Isaac Python shell](../python_scripting/manual_standalone_python.html#isaac-sim-python-environment).

For more in-depth content, see [guided learning](https://docs.omniverse.nvidia.com/usd/latest/learn-openusd/guided-learning.html#openusd-guided-learning) content or the [independent learning](https://docs.omniverse.nvidia.com/usd/latest/learn-openusd/independent-learning.html).

## Units in USD

By default, Isaac Sim USD uses the following default units:

| Unit | Default |
| --- | --- |
| Distance | meters (m) |
| Time | seconds (s) |
| Mass | Kilogram (kg) |
| Angle | Degrees |

For more Isaac Sim conventions, see [Isaac Sim Conventions](../reference_material/reference_conventions.html#isaac-sim-conventions).

There are cases when assets coming from different apps follow a different standard. By default, Isaac Sim has enabled the [Metrics Assembler](https://docs.omniverse.nvidia.com/extensions/latest/ext_metrics_assembler.html "(in Omniverse Extensions)"), which automatically converts the asset scale for the distance unit, mass unit, and Up Axis.

For more details about how USD handles units, see [Units in USD](https://docs.omniverse.nvidia.com/usd/latest/learn-openusd/independent/units.html).

## Useful USD Snippets

Here are some useful snippets that can be useful when dealing with USD in code. These snippets assume that `stage` and `prim`: are respectively pxr.UsdStage and pxr.UsdPrim types, and if any additional type is used, the necessary imports are included in the snippet.

### Traversing Stage or Prim

```python
# For stage traversal there's a built-in method:
for a in stage.Traverse():
    do_something(a)

# For prim, it's not the same method though
from pxr import Usd

prim = stage.GetDefaultPrim()
for a in Usd.PrimRange(prim):
    do_something(a)
```

### Working with Multiple Layers

```python
from pxr import Sdf

# Get References to all layers
root_layer = stage.GetRootLayer()
session_layer = stage.GetSessionLayer()

# Add a SubLayer to the Root Layer
additional_layer = layer = Sdf.Layer.FindOrOpen("my_layer.usd")
root_layer.subLayerPaths.append(additional_layer.identifier)

# Set Edit Layer
# Method 1
with Usd.EditContext(stage, root_layer):
    do_something()

# Method 2
stage.SetEditTarget(additional_layer)

# Make non-persistent changes to the stage (won't be saved regardless if you call stage.Save)

with Usd.EditContext(stage, session_layer):
    do_something()
```

### Converting Transform Pose in Position, Orient, Scale

Note

You can use this to create a set\_pose method that receives a transform and applies to the prim.

```python
import omni.usd
from pxr import Gf, Usd, UsdGeom

def convert_ops_from_transform(prim: Usd.Prim):

    # Get the Xformable from prim
    xform = UsdGeom.Xformable(prim)

    # Gets local transform matrix - used to convert the Xform Ops.
    pose = omni.usd.get_local_transform_matrix(prim)

    # Compute Scale
    x_scale = Gf.Vec3d(pose[0][0], pose[0][1], pose[0][2]).GetLength()
    y_scale = Gf.Vec3d(pose[1][0], pose[1][1], pose[1][2]).GetLength()
    z_scale = Gf.Vec3d(pose[2][0], pose[2][1], pose[2][2]).GetLength()

    # Clear Transforms from xform.
    xform.ClearXformOpOrder()

    # Add the Transform, orient, scale set
    xform_op_t = xform.AddXformOp(UsdGeom.XformOp.TypeTranslate, UsdGeom.XformOp.PrecisionDouble, "")
    xform_op_r = xform.AddXformOp(UsdGeom.XformOp.TypeOrient, UsdGeom.XformOp.PrecisionDouble, "")
    xform_op_s = xform.AddXformOp(UsdGeom.XformOp.TypeScale, UsdGeom.XformOp.PrecisionDouble, "")

    xform_op_t.Set(pose.ExtractTranslation())
    xform_op_r.Set(pose.ExtractRotationQuat().GetNormalized())
    xform_op_s.Set(Gf.Vec3d(x_scale, y_scale, z_scale))
```

On this page

* [Why USD?](#why-usd)
* [Hello World](#hello-world)
  + [Inspecting and Authoring Properties](#inspecting-and-authoring-properties)
* [Further Reading](#further-reading)
* [Units in USD](#units-in-usd)
* [Useful USD Snippets](#useful-usd-snippets)
  + [Traversing Stage or Prim](#traversing-stage-or-prim)
  + [Working with Multiple Layers](#working-with-multiple-layers)
  + [Converting Transform Pose in Position, Orient, Scale](#converting-transform-pose-in-position-orient-scale)

---

### Robot Schema

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/omniverse_usd/robot_schema.html

* [Omniverse and USD](index.html)
* Robot Schema

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Robot Schema

The Robot Schema extends OpenUSD with a set of applied API schemas that describe robotic structures in a standardized, composable way. It builds on USD Common definitions and the Physics Schema for kinematic tree definitions, providing the canonical representation for robots in Isaac Sim.

The schema is implemented across two extensions:

* `isaacsim.robot.schema` – Schema definitions, application helpers, and programmatic utilities for traversing and maintaining robot structures.
* `isaacsim.robot.schema.ui` – Interactive [Robot Inspector Window](../robot_setup/robot_inspector.html#isaac-sim-robot-inspector-window) for viewing robot kinematic trees in multiple display modes, selectively masking and bypassing components, anchoring links to the world, and visualizing joint connections in the viewport.

# Schema Overview

The Robot Schema defines five applied API schemas and two typed schema:

| Schema | Purpose |
| --- | --- |
| **IsaacRobotAPI** | Root definition applied to the robot’s top-level prim. Holds metadata and ordered lists of links and joints. |
| **IsaacLinkAPI** | Flags a rigid body (or other simulated body) as a link in the robot composition. |
| **IsaacJointAPI** | Flags a physics joint as part of the robot composition and carries DOF ordering information. |
| **IsaacSiteAPI** | Marks a point of interest on the robot (tool mount, sensor location, end-effector frame). |
| **IsaacAttachmentPointAPI** | Defines attachment points used by surface grippers. |
| **IsaacNamedPose** | Typed prim schema storing a named joint configuration with an IK target transform, used by the [Robot Poser](../robot_setup/robot_poser.html#isaac-sim-robot-poser). |
| **IsaacSurfaceGripper** | Typed prim schema for surface-gripper mechanics (grip forces, distances, retry behavior). |

## Robot API

`IsaacRobotAPI` is applied to the robot’s root prim and serves as the single source of truth for the robot’s composition and metadata.

**Relationships**

| Relationship | Description |
| --- | --- |
| `isaac:physics:robotLinks` | Ordered list of links that compose the robot, starting with the base link. May include sites interleaved after their parent links. |
| `isaac:physics:robotJoints` | Ordered list of joints connecting the links. |
| `isaac:robot:namedPoses` | List of [IsaacNamedPose](#isaac-sim-robot-schema-named-pose) prims defining stored joint configurations for the robot. |

**Attributes**

| Attribute | Type | Description |
| --- | --- | --- |
| `isaac:description` | String | Free-form text describing the robot’s purpose and capabilities. |
| `isaac:namespace` | String | Unique namespace identifier used for component messaging. |
| `isaac:robotType` | Token | Category of robot, such as `Manipulator`, `Humanoid`, or `Mobile Base`. |
| `isaac:license` | Token | License under which the robot asset is distributed. |
| `isaac:source` | String | URL or reference to the original asset source. |
| `isaac:version` | String | Semantic version number of the robot asset. |
| `isaac:changelog` | String[] | Ordered list of change descriptions across asset revisions. |

Note

The Links and Joints lists need only contain elements relevant for reporting. The full kinematic tree may contain additional elements not present in these lists.

## Link API

`IsaacLinkAPI` is applied to each body that participates in the robot composition. It acts as a flag indicating that the prim should appear in robot state reporting.

| Attribute | Type | Description |
| --- | --- | --- |
| `isaac:nameOverride` | String | Optional custom name used instead of the prim name when reporting robot state. |

Links are not restricted to rigid bodies. The API can be applied to deformable bodies or other simulation types, though computing robot state from non-rigid links requires custom handling.

All links that belong to the robot must have `IsaacLinkAPI` applied, regardless of whether they appear in the `IsaacRobotAPI` links list.

## Joint API

`IsaacJointAPI` is applied to physics joints that participate in the robot composition. It flags the joint for inclusion and carries DOF ordering information.

| Attribute | Type | Description |
| --- | --- | --- |
| `isaac:nameOverride` | String | Optional custom name used instead of the prim name when reporting robot state. |
| `isaac:physics:DofOffsetOpOrder` | Token[] | Ordered list of degree-of-freedom tokens (`TransX`, `TransY`, `TransZ`, `RotX`, `RotY`, `RotZ`) defining the flattened DOF index ordering. Single-DOF joints (revolute, prismatic) and zero-DOF joints (fixed) do not require this attribute. |

All joints that belong to the robot must have `IsaacJointAPI` applied, regardless of whether they appear in the `IsaacRobotAPI` joints list.

Note

In prior revisions, per-axis DOF offset attributes (`isaac:physics:Tr_X:DoFOffset`, etc.) were used instead of the token array. These are deprecated. Use `UpdateDeprecatedJointDofOrder` or `UpdateDeprecatedSchemas` to migrate existing assets.

## Site API

`IsaacSiteAPI` describes points of interest on the robot – tool attachment frames, sensor mount locations, end-effector reference frames, and similar.

| Attribute | Type | Description |
| --- | --- | --- |
| `isaac:Description` | String | Description of the site, such as `"Tool Attachment Point"`. |
| `isaac:forwardAxis` | Token | Axis considered the forward direction of the site (`X`, `Y`, or `Z`). |

Sites are included in the `robotLinks` relationship. They can be placed immediately after their parent link or grouped at the end of the list, controlled by the `sites_last` parameter during population.

Note

`IsaacSiteAPI` replaces the deprecated `IsaacReferencePointAPI`. Robots still carrying the old schema will function but emit deprecation warnings. Use `UpdateDeprecatedSchemas` to migrate.

## Named Pose

`IsaacNamedPose` is a typed prim schema (inheriting from `Xform`) that stores a reusable joint configuration for a segment of the robot’s kinematic chain. Each named pose captures the joints between a start link and an end link/site, the corresponding joint values, and the target end-effector transform encoded in the prim’s Xform ops.

Named poses are collected under a `Named_Poses` scope beneath the robot root prim and registered via the `isaac:robot:namedPoses` relationship on `IsaacRobotAPI`. They are created and managed through the [Robot Poser](../robot_setup/robot_poser.html#isaac-sim-robot-poser) UI or programmatically via the `isaacsim.robot.poser` API.

**Relationships**

| Relationship | Description |
| --- | --- |
| `isaac:robot:pose:startLink` | The start link of the kinematic chain covered by this pose. |
| `isaac:robot:pose:endLink` | The end link or site of the kinematic chain. |
| `isaac:robot:pose:joints` | Ordered list of joint prims in the chain between the start and end links. |

**Attributes**

| Attribute | Type | Description |
| --- | --- | --- |
| `isaac:robot:pose:valid` | Bool | Whether the stored pose represents a valid IK solution. |
| `isaac:robot:pose:jointValues` | Float[] | Joint values in USD native units (degrees for revolute, meters for prismatic), ordered to match the `joints` relationship. |
| `isaac:robot:pose:jointFixed` | Bool[] | Per-joint fixed flags. When `True`, the corresponding joint is held constant during IK solving. |

Because `IsaacNamedPose` inherits from `Xform`, its translate and orient ops store the target end-effector pose in the robot’s coordinate frame. Moving the prim in the viewport updates this target, and the [Robot Poser](../robot_setup/robot_poser.html#isaac-sim-robot-poser) can track the prim’s transform in real time to solve IK continuously.

# Composing Robots

Robot compositions are built by applying `IsaacRobotAPI` to each sub-robot’s root prim. The final assembly is achieved by either:

* Adding a sub-robot’s root prim to the parent robot’s links and joints lists, which causes the parent to recursively include the sub-robot’s full kinematic tree.
* Selecting specific links and joints from sub-robots and adding them directly to the parent robot’s lists.

# Applying the Robot Schema

All robots in Isaac Sim’s asset library and those imported through [URDF Importer Extension](../importer_exporter/ext_isaacsim_asset_importer_urdf.html#isaac-sim-urdf-importer) or [MJCF Importer Extension](../importer_exporter/ext_isaacsim_asset_importer_mjcf.html#isaac-sim-mjcf-importer) have the Robot Schema pre-applied. For robots imported in prior versions or from external sources, the schema must be applied manually.

## Through the GUI

1. Select the root prim of the robot in the Stage panel.
2. In the Properties panel, click the **+ Add** button.
3. Select **Isaac > Robot Schema > Robot API**.

This applies `IsaacRobotAPI` to the root prim and automatically traverses the physics articulation to apply `IsaacLinkAPI` and `IsaacJointAPI` to all discovered bodies and joints.

Properties for each schema appear in the Properties panel under their respective API sections (displayed in purple).

If the robot structure changes over time (for instance, new links or joints are added), either manually apply the individual APIs to new prims, or reapply the Robot API to the root prim to re-run automatic population.

Note

When applying the schema, if your asset follows the [Asset Structure](../robot_setup/asset_structure.html#isaac-sim-app-reference-asset-structure) guidelines, apply it either in the base layer or in a dedicated robot schema layer – not directly in the interface layer. Auto-population requires authored physics, so temporarily add the physics layer as a sublayer during schema application, then remove it before saving.

## Through Code

The following snippet applies the Robot Schema programmatically. Following the [Asset Structure](../robot_setup/asset_structure.html#isaac-sim-app-reference-asset-structure) guidelines, the schema is authored in a separate layer so it remains independent of other payloads and is easy to update as the schema evolves.

```python
import omni.usd
import pxr
import usd.schema.isaac.robot_schema as rs
from pxr import Sdf, Usd, UsdGeom

stage = omni.usd.get_context().get_stage()
robot_asset_path = "/".join(stage.GetRootLayer().identifier.split("/")[:-1])  # Get the asset path from the stage
robot_asset = ".".join(
    stage.GetRootLayer().identifier.split("/")[-1].split(".")[:-1]
)  # Get the asset name from the stage
schema_asset = f"configuration/{robot_asset}_robot_schema.usda"
edit_layer = Sdf.Layer.FindOrOpen(f"{robot_asset_path}/{schema_asset}")
if not edit_layer:
    edit_layer = Sdf.Layer.CreateNew(f"{robot_asset_path}/{schema_asset}")
# Add sublayer to the stage, but as a relative path, only if not already present
if schema_asset not in stage.GetRootLayer().subLayerPaths:
    stage.GetRootLayer().subLayerPaths.append(schema_asset)
# Make all edits in the edit layer
with pxr.Usd.EditContext(stage, edit_layer):

    default_prim = stage.GetDefaultPrim()

    # Apply the Robot API to the default prim, and auto-populate the Links and Joints lists
    rs.ApplyRobotAPI(default_prim)

edit_layer.Save()
stage.Save()
```

# Editing in the Properties Panel

When a prim with `IsaacRobotAPI` is selected, the Properties panel shows a dedicated **Robot Schema** widget that consolidates the robot metadata, the link/joint relationship lists, and a maintenance toolbar in a single Figma-style layout. The widget is provided by `isaacsim.gui.property` and replaces the generic relationship/attribute editors that previously surfaced these properties.

The widget is split into three collapsible sections.

## Robot Schema (Metadata)

The first collapsible section binds each scalar [Robot API](#isaac-sim-robot-schema-robot-api) attribute to an inline editor.

| Field | Editor | Notes |
| --- | --- | --- |
| **Description** | Text field | Free-form text. Updated on field commit (Enter / focus loss). |
| **License** | Drop-down | Populated from the schema’s `allowedTokens` so only recognized SPDX-style identifiers can be selected. |
| **Namespace** | Text field | Used for component messaging. |
| **Robot Type** | Drop-down with **(Other)** entry | Selecting **(Other)** appends a side text field for typing a custom token; selecting any predefined value clears the override. |
| **Source** | Text field | URL or reference to the original asset. |
| **Version** | Text field | Semantic version string. |
| **Changelog** | Inline editable list with **+** and **−** buttons | New entries are prepended; each entry exposes a remove button. The full list is written back as a USD string array. |

## Robot Joints and Robot Links

The next two sections expose the `isaac:physics:robotJoints` and `isaac:physics:robotLinks` relationships as scrollable, drag-reorderable lists.

Each row shows:

* A numeric index (only for direct children, not for sub-robot rows).
* A grab handle for drag-and-drop reordering. Dragging a row reveals a horizontal drop indicator at the insertion point.
* The target prim’s display name. Hovering shows a tooltip with the full prim path. Double-clicking selects the prim on the stage.
* A trailing remove button that drops the entry from the relationship.

### Adding entries

The **Add Joint** and **Add Link** buttons open a stage prim picker pre-filtered to compatible prims:

* **Add Joint** – shows prims with `IsaacJointAPI` or `IsaacRobotAPI`.
* **Add Link** – shows prims with `IsaacLinkAPI`, `IsaacSiteAPI`, or `IsaacRobotAPI`.

### Sub-robot rows

When a row targets a prim that itself has `IsaacRobotAPI`, a disclosure triangle appears next to the label. Expanding the row displays a read-only, indented preview of that sub-robot’s matching relationship – joints in the joints list, links in the links list. The preview recurses up to four levels deep so deeply nested compositions stay legible.

.
Maintenance Toolbar
——————-

Two buttons at the bottom of the widget keep the relationships consistent with the underlying physics articulation and the asset’s layer stack:

| Control | Behavior |
| --- | --- |
| **Re-Calculate Robot Tree** | Calls `RecalculateRobotSchema`: rescans the articulation, appends newly discovered links and joints, and removes invalid targets. Existing valid items keep their order. |
| **Force Update** (checkbox) | When ticked, the next **Re-Calculate Robot Tree** discards the current `robotLinks`/`robotJoints` order and rewrites both relationships from scratch. |
| **Save to Robot Layer** | Calls `SaveRobotSchemaToRobotLayer` to flush the current order to the layer that authors `IsaacRobotAPI`. Other layers (references, attachments, sublayers) are left untouched. A warning is logged if no authoring layer can be located. |

## Other Robot Schema Widgets

Selecting a prim with one of the other Robot Schema APIs surfaces a focused widget for that schema:

* **Robot Link** (`IsaacLinkAPI`) – exposes the optional `isaac:nameOverride` attribute.
* **Robot Joint** (`IsaacJointAPI`) – exposes `isaac:nameOverride`, `isaac:physics:DofOffsetOpOrder`, and the `isaac:actuator` flag.
* **Robot Site** (`IsaacSiteAPI`) – exposes the site description and forward-axis token; available on any `Xformable` prim.

Each widget has a remove button in its header that drops the schema and clears its authored properties. Use the **+ Add** menu’s `Isaac/Robot Schema/...` entries to apply any of these schemas to a new prim.

# Parsing Robot Structure

The robot kinematic tree is derived from the Physics Schema augmented with Robot Schema relationships. Parsing proceeds as follows:

1. Collect links from the `robotLinks` relationship on the `IsaacRobotAPI` prim.
2. Collect joints from the `robotJoints` relationship.
3. Starting from the first link (the base link), perform a breadth-first traversal through joints to connected links, building a tree.

The tree must be acyclic. Joints that would form loops must have their **Exclude from Articulation** attribute set; otherwise, loops are broken arbitrarily during parsing based on visit order.

## Example

1. In the Content Browser, drag a UR10e robot (`Robots/UniversalRobots/ur10e/ur10e.usd`) onto the stage.
2. In the Variant selection menu in the Properties panel, select the Robotiq 2f-140 gripper variant.

1. Open the Script Editor via **Window > Script Editor** and run:

   ```python
   import omni.usd
   from pxr import Usd, UsdGeom

   # For legacy reasons, we need to import the schema from the usd.schema.isaac package
   from usd.schema.isaac import robot_schema

   stage = omni.usd.get_context().get_stage()
   prim = stage.GetPrimAtPath("/World/ur10e")

   robot_tree = robot_schema.utils.GenerateRobotLinkTree(stage, prim)

   robot_schema.utils.PrintRobotTree(robot_tree)
   ```

   The console output:

   ```python
   base_link
     shoulder_link
       upper_arm_link
         forearm_link
           wrist_1_link
             wrist_2_link
               wrist_3_link
                 robotiq_base_link
                   left_outer_knuckle
                     left_outer_finger
                     left_inner_finger
                       left_inner_knuckle
                   right_outer_knuckle
                     right_outer_finger
                     right_inner_finger
                       right_inner_knuckle
   ```

Note how the gripper appears in the robot structure even though it is a separate sub-robot composed into the UR10e. Select the UR10e prim on the stage to see how the Robot Lists include `ee_link`.

# Utility Functions

The `isaacsim.robot.schema` extension provides a comprehensive set of utility functions in the `utils` module, accessible via:

```python
from usd.schema.isaac.robot_schema import utils
```

## Traversal and Tree Generation

| Function | Description |
| --- | --- |
| `GenerateRobotLinkTree(stage, robot_link_prim)` | Builds and returns a `RobotLinkNode` tree representing the robot’s kinematic structure. Returns the root node. |
| `GetAllRobotLinks(stage, robot_link_prim, include_reference_points)` | Returns all links of the robot. Retrieves from schema relationships and supplements with any missing links discovered through articulation traversal. |
| `GetAllRobotJoints(stage, robot_link_prim, parse_nested_robots)` | Returns all joints of the robot. Retrieves from schema relationships and supplements with any missing joints from articulation traversal. |
| `GetJointBodyRelationship(joint_prim, bodyIndex)` | Returns the target path for a joint’s body connection (index 0 or 1). Returns `None` if the joint is excluded from articulation. |
| `GetJointPose(robot_prim, joint_prim)` | Returns the joint’s pose as a 4x4 matrix in the robot’s coordinate frame. |
| `GetLinksFromJoint(root, joint_prim)` | Given a tree root and a joint, returns two lists: links before the joint (toward the base) and links after the joint (toward the leaves). |
| `PrintRobotTree(root, indent)` | Prints an indented text representation of the link tree to the console. |

The `RobotLinkNode` class (from `isaacsim.robot.schema.utils`) represents a node in the kinematic tree:

| Attribute | Description |
| --- | --- |
| `prim` | The USD prim for this link. |
| `name` | Prim name (or `None`). |
| `path` | Prim path (or `None`). |
| `parent` | Parent `RobotLinkNode` (`None` for root). |
| `children` | List of child `RobotLinkNode` instances. |

## Schema Population

| Function | Description |
| --- | --- |
| `PopulateRobotSchemaFromArticulation(stage, robot_prim, articulation_prim, *, detect_sites, sites_last)` | Traverses the physics articulation graph via DFS, applies `IsaacLinkAPI` and `IsaacJointAPI` to discovered prims, and writes the ordered `robotLinks` and `robotJoints` relationships. Optionally detects and applies `IsaacSiteAPI` to leaf Xforms under links. |
| `RecalculateRobotSchema(stage, robot_prim, articulation_prim, *, detect_sites, sites_last)` | Similar to `PopulateRobotSchemaFromArticulation` but preserves the existing order of valid items. New links and joints are appended; invalid targets are removed. Use this for incremental updates. |

Both functions accept:

* `detect_sites` (bool): When `True`, child Xforms with no children under each link are detected and have `IsaacSiteAPI` applied automatically.
* `sites_last` (bool): When `False`, detected sites are inserted immediately after their parent link. When `True`, all sites are appended at the end of the links list.

## Site Detection and Management

| Function | Description |
| --- | --- |
| `DetectAndApplySites(stage, robot_prim, *, sites_last)` | Scans all links under a robot for child Xforms that qualify as sites (leaf Xforms with no children, no existing APIs). Applies `IsaacSiteAPI` to each. Returns `(all_sites, sites_by_parent_path)`. |
| `AddSitesToRobotLinks(robot_prim, sites, sites_by_parent, *, sites_last)` | Adds detected sites to the `robotLinks` relationship, either interleaved after their parent link or appended at the end. |

## Validation and Maintenance

| Function | Description |
| --- | --- |
| `ValidateRobotSchemaRelationships(robot_prim)` | Checks all targets in `robotLinks` and `robotJoints`. Returns `(valid_links, invalid_links, valid_joints, invalid_joints)`. |
| `EnsurePrependListForRobotRelationships(robot_prim)` | Rebuilds `robotLinks` and `robotJoints` using USD prepend list operations for correct layering behavior. |
| `RebuildRelationshipAsPrepend(prim, rel_name, targets)` | Low-level helper that rebuilds a single relationship using prepend list operations. |
| `UpdateDeprecatedSchemas(robot_prim)` | Traverses the robot subtree and replaces `IsaacReferencePointAPI` with `IsaacSiteAPI`. Also migrates deprecated per-axis DOF offset attributes on joints. |
| `UpdateDeprecatedJointDofOrder(joint_prim)` | Migrates a single joint’s deprecated per-axis `DoFOffset` attributes to the `DofOffsetOpOrder` token array. Removes the deprecated attributes from the edit layer. |

## Named Pose Query

| Function | Description |
| --- | --- |
| `GetAllNamedPoses(stage, robot_prim)` | Returns all [IsaacNamedPose](#isaac-sim-robot-schema-named-pose) prims registered in the robot’s `namedPoses` relationship. |
| `GetNamedPoseStartLink(named_pose_prim)` | Returns the start link path from the named pose. |
| `GetNamedPoseEndLink(named_pose_prim)` | Returns the end link / site path from the named pose. |
| `GetNamedPoseJoints(named_pose_prim)` | Returns the ordered list of joint paths in the pose’s kinematic chain. |
| `GetNamedPoseJointValues(named_pose_prim)` | Returns the stored joint values array (native USD units). |
| `GetNamedPoseJointFixed(named_pose_prim)` | Returns the per-joint fixed flags array. |
| `GetNamedPoseValid(named_pose_prim)` | Returns whether the stored pose is valid. |

# Kinematics

The `isaacsim.robot.schema` extension includes a pure-Python kinematics stack for forward kinematics, Jacobian computation, and inverse kinematics. These modules are used internally by the [Robot Poser](../robot_setup/robot_poser.html#isaac-sim-robot-poser) and are available for direct use.

```python
from usd.schema.isaac.robot_schema.ik_solver import IKSolver, IKSolverRegistry
from usd.schema.isaac.robot_schema.kinematic_chain import KinematicChain
from usd.schema.isaac.robot_schema.math import Joint, Transform
```

## Math Primitives

The `math` module (`usd.schema.isaac.robot_schema.math`) provides foundational data structures and pure math utilities with no USD stage or simulation dependencies.

**Data structures**

| Class | Description |
| --- | --- |
| `Transform` | Rigid SE(3) transform (translation `t` + quaternion `q` in `[w, x, y, z]` order). Supports composition via `@`, inversion via `inv()`. |
| `Joint` | Single joint in a kinematic chain. Stores the screw axis (`w` for revolute, `v` for prismatic), home pose, joint limits (`lower`, `upper`), an optional trailing tip offset, and the USD `prim_path`. The `exp(q)` method returns the relative transform for a given joint value. |

**Quaternion utilities**

| Function | Description |
| --- | --- |
| `quat_mul(q1, q2)` | Hamilton product of two quaternions. |
| `quat_conj(q)` | Quaternion conjugate. |
| `quat_rotate(q, v)` | Rotate a 3D vector by a unit quaternion. |
| `axis_angle_to_quat(axis, angle)` | Build a unit quaternion from axis-angle representation. |
| `quat_to_matrix(q)` | Convert a unit quaternion to a 3x3 rotation matrix. |

**Linear algebra**

| Function | Description |
| --- | --- |
| `skew(v)` | 3x3 skew-symmetric matrix for cross-product with `v`. |
| `adjoint(T)` | 6x6 adjoint matrix for a rigid transform `T`. |

## Kinematic Chain

The `kinematic_chain` module (`usd.schema.isaac.robot_schema.kinematic_chain`) provides the `KinematicChain` class that caches the robot’s kinematic tree and builds an ordered joint chain between a start and end prim for FK and IK computation.

| Method / Property | Description |
| --- | --- |
| `KinematicChain(stage, robot_prim, start_prim, end_prim)` | Constructor. Builds the kinematic tree once and extracts the joint chain between the two prims. `start_prim` and `end_prim` are optional; when omitted the cached tree is available for teleport operations without IK. |
| `compute_fk(q)` | Compute end-effector FK for joint configuration `q`. Returns `(Transform, per_joint_transforms)`. |
| `compute_fk_and_jacobian(q)` | Fused single-pass FK and spatial Jacobian computation. Returns `(Transform, 6xN Jacobian)`. |
| `read_joint_states()` | Read current USD joint state for the chain joints. Returns a dict of prim-path to value (radians or meters). |
| `teleport(joint_dict)` | Apply joint values by propagating FK body transforms through the kinematic tree. For use when simulation is stopped. |
| `teleport_anchored(joint_dict)` | Apply joint values while keeping a fixed prim’s world position unchanged. Handles backward (child-to-parent) joints by rigidly correcting the robot after FK propagation. |
| `joints` | Ordered list of `Joint` objects in the chain. |
| `tree_root` | Cached kinematic tree root node. |

## IK Solver Interface

The `ik_solver` module (`usd.schema.isaac.robot_schema.ik_solver`) defines an abstract solver interface and a global registry.

| Class / Function | Description |
| --- | --- |
| `IKSolver` | Abstract base class. Subclasses implement `solve(chain, target, q0, **kwargs)` returning joint values that achieve the target pose. |
| `IKSolverRegistry.register(name, solver_cls, *, default)` | Register an IK solver class under the given name. Set `default=True` to make it the default solver. |
| `IKSolverRegistry.get(name)` | Return a new instance of the solver registered under the given name. `None` returns the default solver. |
| `IKSolverRegistry.available()` | List all registered solver names. |
| `pose_error(Td, T)` | Compute 6-DOF pose error between desired and actual transforms. Returns a 6-vector `[rot_x, rot_y, rot_z, pos_x, pos_y, pos_z]`. |

Custom IK solvers can be registered at import time and used by the Robot Poser by passing their name to the `solver_name` parameter.

## Levenberg-Marquardt Solver

The `lm_ik` module (`usd.schema.isaac.robot_schema.lm_ik`) provides the default IK solver registered as `"lm"`. It implements Levenberg-Marquardt optimization with adaptive damping, joint-limit clamping, null-space bias toward joint mid-range, and per-joint fixed masks.

| Parameter | Default | Description |
| --- | --- | --- |
| `lam` | `1e-3` | Initial LM damping factor. Adapts automatically: shrinks on progress, grows on overshoot. |
| `iters` | `30` | Maximum iterations. |
| `tol` | `1e-6` | Convergence tolerance on the weighted cost. |
| `w_rot` | `1.0` | Weight on rotational error components. |
| `w_pos` | `1.0` | Weight on positional error components. |
| `max_step` | `0.5` | Maximum joint-space step per iteration (prevents wild jumps). |
| `null_space_bias` | `0.05` | Strength of null-space bias toward joint mid-range. Helps escape singular configurations. |
| `joint_fixed` | `None` | Boolean mask of chain length. `True` locks that DOF (Jacobian column zeroed). |

# Named Pose CRUD

The `isaacsim.robot.poser` extension provides higher-level CRUD and I/O operations for [IsaacNamedPose](#isaac-sim-robot-schema-named-pose) prims. These functions build on the [Kinematic Chain](#isaac-sim-robot-schema-kinematics) and IK solver to create, retrieve, apply, and export named poses.

```python
from isaacsim.robot.poser import (
    apply_pose_by_name,
    delete_named_pose,
    export_poses,
    get_named_pose,
    import_poses,
    list_named_poses,
    store_named_pose,
)
```

| Function | Description |
| --- | --- |
| `store_named_pose(stage, robot_prim, pose_name, pose_result)` | Creates an `IsaacNamedPose` prim, writes joint values, relationships, and the target Xform, and registers it in the robot’s `namedPoses` relationship. |
| `get_named_pose(stage, robot_prim, pose_name)` | Retrieves a stored pose as a `PoseResult` dataclass. |
| `list_named_poses(stage, robot_prim)` | Returns the names of all named poses on the robot. |
| `delete_named_pose(stage, robot_prim, pose_name)` | Removes the pose prim and its entry from the `namedPoses` relationship. |
| `apply_pose_by_name(stage, robot_prim, pose_name)` | Applies a stored pose to the robot. Teleports when simulation is stopped; drives via joint targets when running. |
| `export_poses(stage, robot_prim, filepath)` | Exports all named poses to a JSON file. |
| `import_poses(stage, robot_prim, filepath)` | Imports named poses from a JSON file and stores them on the robot. |

Note

`pose_name` is sanitized via `pxr.Tf.MakeValidIdentifier()` before being used as a prim name. Characters outside ASCII `[A-Za-z0-9_]` are replaced with `_`, and a leading `_` is prepended when the input would otherwise start with a digit. Distinct inputs that sanitize to the same identifier (for example `"home:v2"` and `"home/v2"`) refer to the same stored pose; `store_named_pose` logs a warning when this overwrites an existing pose.

For interactive authoring of named poses, see the [Robot Poser](../robot_setup/robot_poser.html#isaac-sim-robot-poser) documentation.

The `isaacsim.robot.schema` extension provides a comprehensive set of utility functions in the `utils` module, accessible via:

```python
from usd.schema.isaac.robot_schema import utils
```

## Traversal and Tree Generation

| Function | Description |
| --- | --- |
| `GenerateRobotLinkTree(stage, robot_link_prim)` | Builds and returns a `RobotLinkNode` tree representing the robot’s kinematic structure. Returns the root node. |
| `GetAllRobotLinks(stage, robot_link_prim, include_reference_points)` | Returns all links of the robot. Retrieves from schema relationships and supplements with any missing links discovered through articulation traversal. |
| `GetAllRobotJoints(stage, robot_link_prim, parse_nested_robots)` | Returns all joints of the robot. Retrieves from schema relationships and supplements with any missing joints from articulation traversal. |
| `GetJointBodyRelationship(joint_prim, bodyIndex)` | Returns the target path for a joint’s body connection (index 0 or 1). Returns `None` if the joint is excluded from articulation. |
| `GetJointPose(robot_prim, joint_prim)` | Returns the joint’s pose as a 4x4 matrix in the robot’s coordinate frame. |
| `GetLinksFromJoint(root, joint_prim)` | Given a tree root and a joint, returns two lists: links before the joint (toward the base) and links after the joint (toward the leaves). |
| `PrintRobotTree(root, indent)` | Prints an indented text representation of the link tree to the console. |

The `RobotLinkNode` class (from `isaacsim.robot.schema.utils`) represents a node in the kinematic tree:

| Attribute | Description |
| --- | --- |
| `prim` | The USD prim for this link. |
| `name` | Prim name (or `None`). |
| `path` | Prim path (or `None`). |
| `parent` | Parent `RobotLinkNode` (`None` for root). |
| `children` | List of child `RobotLinkNode` instances. |

## Schema Population

| Function | Description |
| --- | --- |
| `PopulateRobotSchemaFromArticulation(stage, robot_prim, articulation_prim, *, detect_sites, sites_last)` | Traverses the physics articulation graph via BFS, applies `IsaacLinkAPI` and `IsaacJointAPI` to discovered prims, and writes the ordered `robotLinks` and `robotJoints` relationships. Optionally detects and applies `IsaacSiteAPI` to leaf Xforms under links. |
| `RecalculateRobotSchema(stage, robot_prim, articulation_prim, *, detect_sites, sites_last)` | Similar to `PopulateRobotSchemaFromArticulation` but preserves the existing order of valid items. New links and joints are appended; invalid targets are removed. Use this for incremental updates. |

Both functions accept:

* `detect_sites` (bool): When `True`, child Xforms with no children under each link are detected and have `IsaacSiteAPI` applied automatically.
* `sites_last` (bool): When `False`, detected sites are inserted immediately after their parent link. When `True`, all sites are appended at the end of the links list.

## Site Detection and Management

| Function | Description |
| --- | --- |
| `DetectAndApplySites(stage, robot_prim, *, sites_last)` | Scans all links under a robot for child Xforms that qualify as sites (leaf Xforms with no children, no existing APIs). Applies `IsaacSiteAPI` to each. Returns `(all_sites, sites_by_parent_path)`. |
| `AddSitesToRobotLinks(robot_prim, sites, sites_by_parent, *, sites_last)` | Adds detected sites to the `robotLinks` relationship, either interleaved after their parent link or appended at the end. |

## Validation and Maintenance

| Function | Description |
| --- | --- |
| `ValidateRobotSchemaRelationships(robot_prim)` | Checks all targets in `robotLinks` and `robotJoints`. Returns `(valid_links, invalid_links, valid_joints, invalid_joints)`. |
| `EnsurePrependListForRobotRelationships(robot_prim)` | Rebuilds `robotLinks` and `robotJoints` using USD prepend list operations for correct layering behavior. |
| `RebuildRelationshipAsPrepend(prim, rel_name, targets)` | Low-level helper that rebuilds a single relationship using prepend list operations. |
| `UpdateDeprecatedSchemas(robot_prim)` | Traverses the robot subtree and replaces `IsaacReferencePointAPI` with `IsaacSiteAPI`. Also migrates deprecated per-axis DOF offset attributes on joints. |
| `UpdateDeprecatedJointDofOrder(joint_prim)` | Migrates a single joint’s deprecated per-axis `DoFOffset` attributes to the `DofOffsetOpOrder` token array. Removes the deprecated attributes from the edit layer. |

# Asset Structure

Following the guidelines for [Asset Structure](../robot_setup/asset_structure.html#isaac-sim-app-reference-asset-structure), apply the Robot Schema on a separate layer and load it as a sublayer on the robot asset. This keeps the schema isolated from physics and geometry payloads, making it straightforward to update as the schema evolves across releases.

On this page

* [Robot Schema](#)
* [Schema Overview](#schema-overview)
  + [Robot API](#robot-api)
  + [Link API](#link-api)
  + [Joint API](#joint-api)
  + [Site API](#site-api)
  + [Named Pose](#named-pose)
* [Composing Robots](#composing-robots)
* [Applying the Robot Schema](#applying-the-robot-schema)
  + [Through the GUI](#through-the-gui)
  + [Through Code](#through-code)
* [Editing in the Properties Panel](#editing-in-the-properties-panel)
  + [Robot Schema (Metadata)](#robot-schema-metadata)
  + [Robot Joints and Robot Links](#robot-joints-and-robot-links)
    - [Adding entries](#adding-entries)
    - [Sub-robot rows](#sub-robot-rows)
  + [Other Robot Schema Widgets](#other-robot-schema-widgets)
* [Parsing Robot Structure](#parsing-robot-structure)
  + [Example](#example)
* [Utility Functions](#utility-functions)
  + [Traversal and Tree Generation](#traversal-and-tree-generation)
  + [Schema Population](#schema-population)
  + [Site Detection and Management](#site-detection-and-management)
  + [Validation and Maintenance](#validation-and-maintenance)
  + [Named Pose Query](#named-pose-query)
* [Kinematics](#kinematics)
  + [Math Primitives](#math-primitives)
  + [Kinematic Chain](#kinematic-chain)
  + [IK Solver Interface](#ik-solver-interface)
  + [Levenberg-Marquardt Solver](#levenberg-marquardt-solver)
* [Named Pose CRUD](#named-pose-crud)
  + [Traversal and Tree Generation](#id1)
  + [Schema Population](#id2)
  + [Site Detection and Management](#id3)
  + [Validation and Maintenance](#id4)
* [Asset Structure](#asset-structure)

---

### Sensor Schema

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/omniverse_usd/sensor_schema.html

* [Omniverse and USD](index.html)
* Sensor Schema

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Sensor Schema

The Sensor Schema extends OpenUSD with typed prim schemas for the physics-based sensors in Isaac Sim. All sensor schemas inherit from a common `IsaacBaseSensor` base class and are defined in the `isaacsim.robot.schema` extension alongside the [Robot Schema](robot_schema.html#isaac-sim-robot-schema).

The schema source lives in `source/extensions/isaacsim.robot.schema/sensor_schema/SensorSchema.usda`.

## Base Sensor

`IsaacBaseSensor` is the abstract base class for all typed sensor prims. It inherits from `Xformable`, so every sensor has a position and orientation on the stage.

| Attribute | Type | Description |
| --- | --- | --- |
| `enabled` | Bool | Set to `True` to enable this sensor, `False` to disable. |

## Contact Sensor (`IsaacContactSensor`)

`IsaacContactSensor` measures contact forces between the prim it is attached to and other prims in the scene. It inherits from `IsaacBaseSensor`.

See [Contact sensor](../sensors/isaacsim_sensors_physics_contact.html#isaacsim-sensors-physics-contact) for usage documentation.

| Attribute | Type | Description |
| --- | --- | --- |
| `threshold` | Float2 | Min and max force detected by this sensor, in (kg) \* (stage length unit) / (second)^2. |
| `radius` | Float | Radius of the contact sensor sphere, in stage length units. A value of `-1` uses the prim’s collision geometry. |
| `color` | Float4 | Color of the contact sensor visualization sphere (R, G, B, A). |
| `sensorPeriod` | Float | **Deprecated** since `isaacsim.robot.schema` 6.2.0. Only used by the deprecated `isaacsim.sensors.physx` extension. Time between measurements in simulator seconds. |

## IMU Sensor (`IsaacImuSensor`)

`IsaacImuSensor` measures linear acceleration, angular velocity, and orientation of the prim it is attached to. It inherits from `IsaacBaseSensor`.

See [IMU sensor](../sensors/isaacsim_sensors_physics_imu.html#isaacsim-sensors-physics-imu) for usage documentation.

| Attribute | Type | Description |
| --- | --- | --- |
| `sensorPeriod` | Float | **Deprecated** since `isaacsim.robot.schema` 6.2.0. Only used by the deprecated `isaacsim.sensors.physx` extension. Time between measurements in simulator seconds. |
| `linearAccelerationFilterWidth` | Int | Number of linear acceleration measurements used in the rolling average filter. |
| `angularVelocityFilterWidth` | Int | Number of angular velocity measurements used in the rolling average filter. |
| `orientationFilterWidth` | Int | Number of orientation measurements used in the rolling average filter. |

## Raycast Sensor (`IsaacRaycastSensor`)

`IsaacRaycastSensor` is a physics-raycast-based sensor with explicit per-ray origin offsets, direction vectors, and optional time offsets. It inherits from `IsaacBaseSensor` and is used by the `isaacsim.sensors.experimental.physics` extension.

See [Physics raycast sensor](../sensors/isaacsim_sensors_physics_raycast.html#isaacsim-sensors-physics-raycast) for usage documentation.

Origins and directions are specified in the sensor prim’s local coordinate frame. At each physics step the sensor’s world transform is computed from the current rigid-body pose, optionally extrapolated forward using linear/angular velocity when a non-zero `rayTimeOffset` is specified. Each ray’s local origin and direction are then transformed into world space for the raycast.

All attributes are read once when the sensor is first evaluated after simulation starts. Changing attribute values while the simulation is playing has no effect; stop and restart the simulation to pick up changes.

| Attribute | Type | Description |
| --- | --- | --- |
| `numRays` | UInt | Number of rays cast by this sensor. `rayOrigins` and `rayDirections` must each have exactly this many elements. |
| `minRange` | Float | Minimum detection range in stage length units. Rays start at `origin + direction * minRange`. |
| `maxRange` | Float | Maximum detection range in stage length units. |
| `rayOrigins` | Float3[] | Per-ray origin translations in the sensor’s local coordinate frame. |
| `rayDirections` | Float3[] | Per-ray cast direction vectors in the sensor’s local coordinate frame. Vectors are normalized before use. |
| `rayTimeOffsets` | Float[] | Per-ray time offsets in seconds. When provided, only rays whose time offsets fall within the current physics step’s time window are fired. The sweep period equals `max(rayTimeOffsets)`. If empty, all rays fire every step. |
| `outputFrameOfReference` | Token | Coordinate frame for hit positions and normals: `SENSOR` (default) or `WORLD`. |
| `reportHitPrimPaths` | Bool | When `True`, the sensor reading includes the USD prim path of each hit surface. |

## Deprecated Sensor Schemas

The following sensor schemas are defined in `SensorSchema.usda` but are deprecated:

* **IsaacLightBeamSensor** – Deprecated since `isaacsim.robot.schema` 6.2.0. Use `IsaacRaycastSensor` with `isaacsim.sensors.experimental.physics` instead. See [Migrating to the physics raycast sensor](../sensors/isaacsim_sensors_physx_lightbeam.html#isaacsim-sensors-physx-lightbeam-migration).

The `IsaacRtxLidarSensorAPI` and `IsaacRtxRadarSensorAPI` are applied API schemas for the RTX sensor pipeline and are not physics-based sensors. See [RTX Sensors](../sensors/isaacsim_sensors_rtx.html#isaacsim-sensors-rtx) for RTX sensor documentation.

On this page

* [Base Sensor](#base-sensor)
* [Contact Sensor (`IsaacContactSensor`)](#contact-sensor-isaaccontactsensor)
* [IMU Sensor (`IsaacImuSensor`)](#imu-sensor-isaacimusensor)
* [Raycast Sensor (`IsaacRaycastSensor`)](#raycast-sensor-isaacraycastsensor)
* [Deprecated Sensor Schemas](#deprecated-sensor-schemas)

---


## 参考

### Isaac Sim Conventions

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/reference_material/reference_conventions.html

* Isaac Sim Conventions

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Isaac Sim Conventions

This section provides a reference for the units, representations, and coordinate conventions used within NVIDIA Isaac Sim.

## Default Units

| Measurement | Units | Notes |
| --- | --- | --- |
| Length | Meter |  |
| Mass | Kilogram |  |
| Time | Seconds |  |
| Physics Time-Step | Seconds | Configurable by User. Default is 1/60. |
| Force | Newton |  |
| Frequency | Hertz |  |
| Linear Drive Stiffness | \(kg/s^2\) |  |
| Angular Drive Stiffness | \((kg\*m^2)/(s^2\*angle)\) |  |
| Linear Drive Damping | \(kg/s\) |  |
| Angular Drive Damping | \((kg\*m^2)/(s\*angle)\) |  |
| Diagonal of Inertia | \((kg\*m^2)\) |  |

## Default Rotation Representations

### Quaternions

| API | Representation |
| --- | --- |
| Isaac Sim Core | (QW, QX, QY, QZ) |
| USD | (QW, QX, QY, QZ) |
| PhysX | (QX, QY, QZ, QW) |
| Dynamic Control | (QX, QY, QZ, QW) |

### Angles

| API | Representation |
| --- | --- |
| Isaac Sim Core | Radians |
| USD | Degrees |
| PhysX | Radians |
| Dynamic Control | Radians |

Note

UI elements that show attributes from USD should always display angles in Degrees, even if the value comes from Physics.

### Matrix Order

| API | Representation |
| --- | --- |
| Isaac Sim Core | Row Major |
| USD | Row Major |

### World Axes

NVIDIA Isaac Sim follows the right-handed coordinate conventions.

| Direction | Axis | Notes |
| --- | --- | --- |
| Up | +Z |  |
| Forward | +X |  |

### Default Camera Axes

| Direction | Axis | Notes |
| --- | --- | --- |
| Up | +Y |  |
| Forward | -Z |  |

Note

**Isaac Sim to ROS Conversion**: To convert from Isaac Sim Camera Coordinates to ROS Camera Coordinates, rotate 180 degrees about the X-Axis.

### Image Frames (Synthetic Data)

| Coordinate | Corner |
| --- | --- |
| (0,0) | Top Left |

## Sensor Axes Representation (LiDAR, Cameras)

Cameras in Isaac Sim are subject to three different types of axes definition, depending on the context of use. Here, we introduce the three conventions and how it’s used in different contexts.

### World Axes

The world axes uses the +X forward, +Z up convention. The origin of the world prim is always represented in the World axes.
The camera prim, represented in the world axes, is shown in the figure below.

### USD Axes

In the computer graphics community, the USD convention is used. The USD axes uses the [+Y up, -Z forward convention](https://openusd.org/dev/api/class_usd_geom_camera.html). In an Isaac Sim application, the Property panel displays the poses of objects in the USD stage. The poses of all objects in the stage are displayed in the world axes, with the exception of camera prims, which is displayed in the +Y up, -Z forward convention. Therefore, this convention is referred to as USD Axes in the context of camera prims.
The camera prim, represented in the USD axes convention, is shown in the figure below.

### ROS Axes

The ROS axes uses the [-Y up, +Z forward convention](https://www.ros.org/reps/rep-0103.html#suffix-frames). Therefore, any camera data including transforms published to ROS 2( [ROS 2 Cameras](../ros2_tutorials/tutorial_ros2_camera.html#isaac-sim-app-tutorial-ros2-camera) ) will be represented in this convention.
The camera prim, represented in the ROS axes convention, is shown in the figure below.

### Transforms Between These Frames

For observing poses of camera prims in the proper axes convention, see the Camera Inspector tutorial.

On this page

* [Default Units](#default-units)
* [Default Rotation Representations](#default-rotation-representations)
  + [Quaternions](#quaternions)
  + [Angles](#angles)
  + [Matrix Order](#matrix-order)
  + [World Axes](#world-axes)
  + [Default Camera Axes](#default-camera-axes)
  + [Image Frames (Synthetic Data)](#image-frames-synthetic-data)
* [Sensor Axes Representation (LiDAR, Cameras)](#sensor-axes-representation-lidar-cameras)
  + [World Axes](#id2)
  + [USD Axes](#usd-axes)
  + [ROS Axes](#ros-axes)
  + [Transforms Between These Frames](#transforms-between-these-frames)

---

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
  + [RTX – Interactive (Path Tracing) mode](#interactive-render-mode)
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

An Omniverse App is built upon a specific set of Extensions to provide a desired functionality. An App gives the user a customized experience by implementing the UI’s of its Extensions with a custom layout. You can quickly and easily create customized Apps comprised of any number of Extensions developed by you, the Omniverse Community or NVIDIA. An App can be as simple as a 3D viewer or as complex as an AI suite. This modular approach to building Apps makes it easy to create a customized workflow or a global scale cloud application

### [Apps](#id5)

An Omniverse App is built upon a specific set of Extensions to provide a desired functionality. An App gives the user a customized experience by implementing the UI’s of its Extensions with a custom layout. You can quickly and easily create customized Apps comprised of any number of Extensions developed by you, the Omniverse Community or NVIDIA. An App can be as simple as a 3D viewer or as complex as an AI suite. This modular approach to building Apps makes it easy to create a customized workflow or a global scale cloud application

### [Connectors](#id6)

An Omniverse Connector is middleware with which Omniverse and other software applications communicate with each other. They enable the import/export 3D assets, data, and models between different tools and workflows. It’s important to note that this means using USD as the “go between” format to convert 3D data.

### [Omniverse Nucleus](#id7)

Omniverse Nucleus offers a set of fundamental services that allow a variety of client applications, renderers, and microservices to share and modify representations of virtual worlds.

Nucleus operates under a publish/subscribe model. Subject to access controls, Omniverse clients can publish modifications to digital assets and virtual worlds to the Nucleus Database (DB) or subscribe to their changes. Changes are transmitted in real-time between connected applications. Digital assets can include geometry, lights, materials, textures and other data that describe virtual worlds and their evolution through time.

This allows a variety of Omniverse-enabled client applications ( Apps, Connectors, and others) to share and modify authoritative representations of virtual worlds.

* See [Nucleus overview](https://docs.omniverse.nvidia.com/nucleus/latest/overview/overview.html "(in Omniverse Nucleus)") for a more in-depth look at Nucleus’s data model, architecture, and distribution platforms.

### [Hub Workstation Cache](#id8)

Hub Workstation Cache is a service that helps speed up USD workflows on your local workstation. This is a stand-alone service that runs on your local workstation and benefits Kit-based applications or Client Library tools.

Hub Workstation Cache has been performance optimized and supports storage-derived data from newer versions of Kit-based applications.

* See [Hub Workstation Cache overview](https://docs.omniverse.nvidia.com/utilities/latest/cache/hub-workstation.html "(in Omniverse Utilities)") for more details.
* See the [Workstation Installation](../installation/install_workstation.html#isaac-sim-app-install-workstation) for how to install

### [Live Sync](#id9)

Live Sync mode enables real-time “live” editing of shared files on a Nucleus Server. The Live Sync button is on the top-right corner of the Workspace.

### [Omniverse Kit](#id10)

NVIDIA Omniverse™ Kit is a toolkit for building native Omniverse applications and microservices. It is built on a base framework known as Carbonite that provides a wide variety of functionality through a set of light-weight plugins. Carbonite plugins are all authored with C interfaces for persistent ABI compatibility. A Python interpreter is provided for scripting and customization.

NVIDIA Omniverse™ Kit exposes much of its functionality through Python bindings. This provides an API that can be used to write new extensions to Omniverse Kit or new experiences for Omniverse.

* For a more in-depth look at developing in Kit, see the [Kit Programming Manual](https://docs.omniverse.nvidia.com/kit/docs/kit-manual/latest/guide/kit_overview.html "(in Omniverse Kit)").

### [Omniverse Launcher](#id11)

The NVIDIA Omniverse Launcher is your first step into the Omniverse. It provides immediate access to all the apps, connectors and other downloads within the Omniverse.

* See the [Launcher overview](https://docs.omniverse.nvidia.com/launcher/latest/index.html "(in Omniverse Launcher)") for more details.

### [Omniverse USD Composer](#id12)

NVIDIA Omniverse™ USD Composer was an Omniverse app for world-building that allows users to assemble, light, simulate and render large scale scenes. It is built using NVIDIA Omniverse™ Kit. The Scene Description and in-memory model is based on Pixar’s USD. USD Composer takes advantage of the advanced workflows of USD like Layers, Variants, Instancing and much more.

### [Carbonite (carb)](#id13)

The Carbonite SDK provides the core functionality of all Omniverse apps. This is a C++ based SDK with Python bindings that provides features such as plugin management, input handling, file access, asset loading and management, thread and task management, and much more.

### [RTX - Real-Time mode](#id14)

High quality real-time rendering mode.

### [RTX – Interactive (Path Tracing) mode](#id15)

The highest quality, physically accurate rendering mode.

### [Extensions](#id16)

Extensions are plug-ins to Omniverse Kit that extend its capabilities. They are offered with complete source code to help developers easily create, add, and modify the tools and workflows they need to be productive. Extensions are the core building blocks of Omniverse Kit based applications.

* See [Extension Manager](https://docs.omniverse.nvidia.com/extensions/latest/ext_core/ext_extension-manager.html "(in Omniverse Extensions)") for more details.

### [Omniverse Connect](#id17)

Connectors are extensions and additional software layers on top of the open-source USD distribution that allow DCC tools and compute services to communicate easily with each other through the Omniverse Nucleus DB. Those extensions and additions are collectively known as NVIDIA Omniverse™ Connect.

## [USD](#id18)

### [USD](#id19)

Universal Scene Description (USD) is an easily extensible, open-source 3D scene description file format developed by Pixar for content creation and interchange among different tools. As a result of its power and versatility, it’s being widely adopted, not only in the visual effects community, but also in architecture, design, robotics, manufacturing, and other disciplines.

* For a more in-depth look at USD in Omniverse, see NVIDIA’s USD primer [What is USD?](https://developer.nvidia.com/usd/).
* See the [USD API](https://graphics.pixar.com/usd/release/index.html) docs for more details.
* See the [USD Glossary of Terms & Concepts](https://graphics.pixar.com/usd/release/glossary.html) for more details.
* See [NVIDIA’s USD tutorials](https://developer.nvidia.com/usd/tutorials)

### [MDL](#id20)

Material Definition Language (MDL) is a NVIDIA-developed USD schema that represents material assignments and specifies material parameters.

### [Stage](#id21)

The Omniverse Stage window allows you to see all the assets in your current USD Scene. The [USD Stage](https://graphics.pixar.com/usd/release/glossary.html#usdglossary-stage) is the USD abstraction for a scenegraph derived from a root USD file, and all of the referenced/layered files it composes. Listed in a hierarchical (parent/child) order the Stage offers convenient access and is typically used to navigate large scenes.

* See the [Stage](https://docs.omniverse.nvidia.com/extensions/latest/ext_core/ext_stage.html "(in Omniverse Extensions)") docs for more details.
* See the [USD Glossary of Terms & Concepts](https://graphics.pixar.com/usd/release/glossary.html) for more details.

### [Prim](#id22)

A [Prim](https://graphics.pixar.com/usd/release/glossary.html#usdglossary-prim) is the primary container object in USD: prims can contain (and order) other prims, creating a “namespace hierarchy” on a Stage,
and prims can also contain (and order) properties that hold meaningful data. Prims, along with their associated, computed indices, are
the only persistent scenegraph objects that a Stage retains in memory, and the API for interacting with prims is provided by the UsdPrim class.

* See the [USD Glossary of Terms & Concepts](https://graphics.pixar.com/usd/release/glossary.html) for more details.

### [Mesh](#id23)

A mesh is a subdividable primitive that consists of points, edges, and faces that define its shape. In USD, a mesh is encoded in a [UseGeomMesh](https://graphics.pixar.com/usd/release/api/class_usd_geom_mesh.html) class.

### [Shape](#id24)

A Shape is a geometric primitive that maps to one of USD’s five “intrinsic” `UsdGeomGprim` classes:

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

**Instances** are indicated by a **blue “I”**, and can be either references or payloads. They carry additional assumptions about the structure of the asset for more efficient vectorization (scaled up).

For example, suppose you want to collect synthetic data with a robot. If you aren’t going to modify the structure of the robot, it can exist as a reference on the stage (the asset is defined in some other file). If, during data collection, you want to be able to swap the robot out for a different one, those meshes need to be held in active memory. This means that the asset first needs to be converted from a reference to a payload. If you wanted to collect data with a 1000 robots at once, and they are all the same, you might use instantiable references. Whereas, if you wanted to collect data with a 1000 randomly sampled robots (different arms with the same number of joints for example), you would use instance payloads.

### [Y-Up / Z-Up](#id26)

The axis of orientation of a given scene/prim. Y-Up refers to the Positive Y Axis is pointing up. Z-Up refers to the Positive Z Axis is pointing up. This orientation setting is generally set by the application of the scene/prims origination.

### [Layer](#id27)

A component of the collaborative nature of USD. Each layer in USD signifies a user’s “opinion” on assets inside a stage. Layers can override other layers.

### [Instance](#id28)

A light-weight and less manipulable copy of a prim.

### [Checkpoint](#id29)

Immutable historical file versions. Checkpoints are used for version control and allow you to look at and restore the stage to a previous state.

## [PhysX](#id30)

NVIDIA PhysX is a scalable multi-platform physics simulation solution.
The NVIDIA Omniverse™ Physics simulation extension is powered by the NVIDIA PhysX SDK, and includes
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
  + [RTX – Interactive (Path Tracing) mode](#interactive-render-mode)
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

### Benchmarks

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/reference_material/benchmarks.html

* Isaac Sim Benchmarks

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Isaac Sim Benchmarks

This page contains key performance indicators (KPIs) for Isaac Sim, captured across
different reference hardware and measured using the `isaacsim.benchmark.services` extension. It also
contains a guide on how to collect the same KPIs on your hardware, to compare to our published
performance specs.

## GPU-Independent KPIs

These KPIs measure Isaac Sim performance independent of the GPU on which Isaac Sim is running.

Note

These KPIs were measured on a standardized reference machine using an Intel i9-14900k CPU and 32GB of DDR5 RAM.

GPU-Independent KPIs

| Name | Definition | Units | Value |
| --- | --- | --- | --- |
| Binary package size (Windows) | Size of Windows binary package | GB | 9.90 |
| Binary package size (Linux) | Size of Linux binary package | GB | 12.2 |
| Docker container size | Size of Docker container before extraction on [NGC](https://ngc.nvidia.com/catalog/containers/nvidia:isaac-sim) | GB | 9.97 |
| `pip` package size | Size of `pip` package as downloaded | GB |  |
| Startup time (async) | Time from launching Isaac Sim executable to `app ready` appearing in logs | seconds | 31.472 [[1]](#id5)   6.31 [[2]](#id6) |
| Startup time (non-async) | Time from initializing `SimulationApp` in standalone Python to `app ready` appearing in logs | seconds | 263 [[3]](#id7)   4.43 [[4]](#id8) |

[[1](#id1)]

Includes shader installation, which is typically one-time when shaders are cached.

[[2](#id2)]

Startup time (async) using cached shaders.

[[3](#id3)]

Includes shader installation, which is typically one-time when shaders are cached.

[[4](#id4)]

Startup time (non-async) using cached shaders.

## GPU-Dependent KPIs

These KPIs measure Isaac Sim performance on reference hardware, including
frame rate for benchmark scenes and render rate for specific sensor combinations.
KPIs are reported as the average KPI value across 600 frames.

Note

For detailed explanations of each KPI, refer to [Measuring KPIs on Local Hardware](#isaac-sim-benchmarks-measuring-kpis). Instructions on how to measure the KPIs on local hardware as well as relevant optimization tips for similar workflows are provided.

### Workstation GPUs

GeForce RTX 5080

Note

These KPIs were measured on a standardized reference machine using an Intel i9-14900k CPU and 32GB of DDR5 RAM.

Hardware-Dependent KPIs

| Name | Definition | Units | Windows | Ubuntu |
| --- | --- | --- | --- | --- |
| Full Warehouse Sample Scene Load Time | Wall-clock time to load Full Warehouse Sample Scene | Seconds | 27.15 | 27.45 |
| Full Warehouse Sample Scene FPS | Frame rate of Full Warehouse Sample Scene | Frames per second | 155.52 | 161.55 |
| Physics steps per second | Number of physics steps executed per wall-clock second with 10 O3dyn robots | Hz | 32.95 | 31.43 |
| Isaac ROS Sample Scene FPS | Frame rate of Isaac ROS Sample Scene | Frames per second | 28.34 | 46.56 |
| ROS2 render & publishing speed | Frame rate rendered and published using [ROS2 bridge](../ros2_tutorials/tutorial_ros2_navigation.html#isaac-sim-app-tutorial-ros2-navigation) from Nova Carter ROS asset, per wall-clock second | Frames per second | 13.54 | 18.34 |
| SDG images per second (simple) | Images rendered by SDG per second, with only RGBD annotators enabled, per wall-clock second | Images per second | 24.54 | 40.83 |
| SDG images per second (complex) | Images rendered by SDG per second, with all annotators enabled, per wall-clock second | Images per second | 8.86 | 13.77 |

RTX PRO 6000 Blackwell

Note

These KPIs were measured on a standardized reference machine using an Intel i9-14900k CPU and 32GB of DDR5 RAM.

Hardware-Dependent KPIs

| Name | Definition | Units | Windows | Ubuntu |
| --- | --- | --- | --- | --- |
| Full Warehouse Sample Scene Load Time | Wall-clock time to load Full Warehouse Sample Scene | Seconds | 32.86 | 29.14 |
| Full Warehouse Sample Scene FPS | Frame rate of Full Warehouse Sample Scene | Frames per second | 159.72 | 153.33 |
| Physics steps per second | Number of physics steps executed per wall-clock second with 10 O3dyn robots | Hz | 32.51 | 35.40 |
| Isaac ROS Sample Scene FPS | Frame rate of Isaac ROS Sample Scene | Frames per second | 47.55 | 51.94 |
| ROS2 render & publishing speed | Frame rate rendered and published using [ROS2 bridge](../ros2_tutorials/tutorial_ros2_navigation.html#isaac-sim-app-tutorial-ros2-navigation) from Nova Carter ROS asset, per wall-clock second | Frames per second | 26.78 | 28.38 |
| SDG images per second (simple) | Images rendered by SDG per second, with only RGBD annotators enabled, per wall-clock second | Images per second | 29.27 | 41.37 |
| SDG images per second (complex) | Images rendered by SDG per second, with all annotators enabled, per wall-clock second | Images per second | 9.57 | 14.24 |

### Server GPUs

L40

Note

These KPIs were measured on a standardized OVX machine using 2x Intel 8362 CPU and 1024GB of DDR4 RAM, on Ubuntu 24.04.
Some KPIs are measured on multi-GPU configurations, typically for 1, 4, or 8 GPUs.

Hardware-Dependent KPIs by GPU Count

| Name | Definition | Units | x1 | x4 | x8 |
| --- | --- | --- | --- | --- | --- |
| Full Warehouse Sample Scene Load Time | Wall-clock time to load Full Warehouse Sample Scene | Seconds | 101.23 | 102.43 | 100.28 |
| Full Warehouse Sample Scene FPS | Frame rate of Full Warehouse Sample Scene | Frames per second | 182.48 | 151.75 | 120.34 |
| Physics steps per second | Number of physics steps executed per wall-clock second with 10 O3dyn robots | Hz | 30.6 | 31.53 | 33.05 |
| Isaac ROS Sample Scene FPS | Frame rate of Isaac ROS Sample Scene | Frames per second | 44.62 | 40.00 | 36.40 |
| ROS2 render & publishing speed | Frame rate rendered and published using [ROS2 bridge](../ros2_tutorials/tutorial_ros2_navigation.html#isaac-sim-app-tutorial-ros2-navigation) from Nova Carter ROS asset, per wall-clock second | Frames per second | 33.12 | 38.92 | 39.41 |
| SDG images per second (simple) | Images rendered by SDG per second, with only RGBD annotators enabled, per wall-clock second | Images per second |  |  |  |
| SDG images per second (complex) | Images rendered by SDG per second, with all annotators enabled, per wall-clock second | Images per second |  |  |  |

RTX PRO 6000 Blackwell Server Edition

Hardware-Dependent KPIs by GPU Count

| Name | Definition | Units | x1 | x4 | x8 |
| --- | --- | --- | --- | --- | --- |
| Full Warehouse Sample Scene Load Time | Wall-clock time to load Full Warehouse Sample Scene | Seconds | 102.34 | 101.75 | 101.45 |
| Full Warehouse Sample Scene FPS | Frame rate of Full Warehouse Sample Scene | Frames per second | 193.05 | 173.01 | 168.92 |
| Physics steps per second | Number of physics steps executed per wall-clock second with 10 O3dyn robots | Hz | 35.13 | 34.88 | 34.46 |
| Isaac ROS Sample Scene FPS | Frame rate of Isaac ROS Sample Scene | Frames per second | 109.77 | 105.82 | 97.47 |
| ROS2 render & publishing speed | Frame rate rendered and published using [ROS2 bridge](../ros2_tutorials/tutorial_ros2_navigation.html#isaac-sim-app-tutorial-ros2-navigation) from Nova Carter ROS asset, per wall-clock second | Frames per second | 38.61 | 40.97 | 39.15 |
| SDG images per second (simple) | Images rendered by SDG per second, with only RGBD annotators enabled, per wall-clock second | Images per second |  |  |  |
| SDG images per second (complex) | Images rendered by SDG per second, with all annotators enabled, per wall-clock second | Images per second |  |  |  |

## Measuring KPIs on Local Hardware

Isaac Sim KPIs can be measured using the Python scripts provided in `standalone_examples/benchmarks`. Select a category below to review benchmark details, commands, and configuration options as well as optimization tips for similar workflows.

More specific optimization guidance can be found in the [Isaac Sim Performance Optimization Handbook](sim_performance_optimization_handbook.html#isaac-sim-performance-optimization-handbook).

Note

Commands are provided in `bash` syntax (for Ubuntu). For Windows, replace `.sh` with `.bat` and `\` for multiline commands to `` ` ``.

Startup & Loading

Benchmarks for measuring application initialization and scene loading performance.

Startup Time (Async)

**Purpose:** Measure Isaac Sim initialization time in headless mode without blocking operations.

**What it measures:** Time from application launch to ready state, measured as `Runtime` for `phase: startup` in the logs.

**Command:**

```python
./isaac-sim.sh --no-window --/app/quitAfter=200 --/app/file/ignoreUnsavedOnExit=1 \
  --enable isaacsim.benchmark.services
```

**Interpreting Results:** Look for the following in the console output:

```python
[INFO] Runtime for phase: startup = 15234 ms
```

**Typical Values:** 10-30 seconds depending on hardware and system configuration.

Startup Time (Non-Async)

**Purpose:** Measure Isaac Sim initialization time with synchronous loading using the Python API.

**What it measures:** Time for complete application initialization through the Python API.

**Command:**

```python
./python.sh standalone_examples/api/isaacsim.simulation_app/hello_world.py \
  --enable isaacsim.benchmark.services
```

**Interpreting Results:** Look for `Runtime` for `phase: startup` in the logs.

**Comparison:** Non-async startup is typically slower than async due to synchronous loading.

Full Warehouse Load Time + FPS

**Purpose:** Measure scene loading performance and rendering FPS for complex warehouse environment.

**What it measures:** Duration of stage loading phase and FPS at runtime for the given stage.

**Command:**

```python
./python.sh standalone_examples/benchmarks/benchmark_scene_loading.py \
  --env-url /Isaac/Environments/Simple_Warehouse/full_warehouse.usd
```

**Configuration:**

* Environment: full warehouse sample scene

**Interpreting Results:**

```python
[INFO] Runtime for phase: loading = 8123 ms
[INFO] Mean FPS for phase: benchmark = 45.2
```

**Performance Notes:** Loading time depends on asset complexity and storage speed. FPS varies with CPU and GPU capability.

**Optimization Tips:**

1. Use a simpler scene with fewer materials and textures.
2. Disable material loading to reduce initial loading time (`--/app/renderer/skipMaterialLoading=1`).
3. Reduce rendering quality to increase runtime FPS.

Isaac ROS Sample Scene Load Time + FPS

**Purpose:** Measure load time and runtime performance in stages with the ROS2 bridge enabled.

**What it measures:** Duration of stage loading phase and FPS at runtime for the given stage with the ROS2 bridge enabled. The stage uses the Nova Carter robot in a warehouse environment with animated human workers.

**Measurement:** Loading time is measure by `Runtime` for `phase: loading`. Runtime FPS is measured as `Mean FPS` for `phase: benchmark`.

**Command:**

```python
./python.sh standalone_examples/benchmarks/benchmark_scene_loading.py \
  --env-url /Isaac/Samples/ROS2/Scenario/carter_warehouse_apriltags_worker.usd
```

**Interpreting Results:**

```python
[INFO] Runtime for phase: loading = 8556 ms
[INFO] Mean FPS for phase: benchmark = 38.7
```

**Optimization Tips:**

1. Disable material loading to reduce initial loading time (`--/app/renderer/skipMaterialLoading=1`).
2. Reduce rendering quality to increase runtime FPS.
3. Use a simpler scene with fewer materials, textures, and lighting. This will simplify the rendering work done by each render product.

**Multi-GPU:** Loading time is not impacted by the number of GPUs. Runtime FPS for this benchmark scales with GPU count - optimal GPU count is hardware dependent but typically 4 or 8 GPUs.

Workflow Performance

Benchmarks for measuring physics computation, rendering speed, and overall simulation performance.

Physics Steps per Second

**Purpose:** Measure physics simulation performance and compare CPU vs GPU physics backends for a complex robot.

**What it measures:** How many physics steps are executed per wall-clock second given a fixed step size, robot count, and Physics backend for the O3dyn robot in the full warehouse sample scene.

**Measurement:** Measured as `Mean FPS` for `phase: benchmark` given a physics dt of 1/60s.

**Command:**

```python
./python.sh standalone_examples/benchmarks/benchmark_robots_o3dyn.py \
  --num-robots 10 --num-gpus 1
```

**Configurations:**

* Robot Count
* Physics Backend (CPU: numpy, GPU: torch, warp)

```python
# CPU Physics
./python.sh standalone_examples/benchmarks/benchmark_robots_o3dyn.py \
  --num-robots 2 --physics numpy

# GPU Physics (default: torch)
./python.sh standalone_examples/benchmarks/benchmark_robots_o3dyn.py \
  --num-robots 10 --physics warp
```

**Interpreting Results:**

```python
Mean FPS: 51.706 FPS
```

Given a physics dt of `1/60`, the physics steps per second is equivalent to the FPS. A smaller physics dt will result in multiple physics steps per frame, changing the computation to be `FPS * physics steps per frame`.

**Performance Notes:** The O3dyn robot is very complex, particularly due to the simulation of the highly articulated wheels. Simpler robots will achieve faster framerates due to reduced physics computation work. Higher-spec GPUs will enable higher throughput as robot count or physics object count increases.

**Optimization Tips:**

1. Select the appropriate physics backend for the workload. It’s recommended to test with both backends to determine the optimal choice.

> * CPU Physics: Low robot count and/or low complexity robots + scenes
> * GPU Physics: Higher robot counts and/or higher complexity robots + scenes

2. Reduce the complexity of the robot by disabling unnecessary colliders, joints, and other components. Similarly decrease the complexity of the scene.

**Performance Scaling:** The O3dyn robot is a good example to review how CPU and GPU physics performance scales with the number of robots and the complexity of the robots.

* 1-4 robots: CPU physics is faster
* ~5 robots: CPU and GPU physics are comparable (hardware-dependent)
* 6+ robots: GPU physics is faster

**Multi-GPU:** GPU physics performance does not scale with GPU count as PhysX runs on a single GPU.

Rendering Speed

**Purpose:** Measure pure rendering performance with no additional physics computation.

**What it measures:** The framerate of the simulation when rendering the full warehouse sample scene with a variable number of cameras.

**Measurement:** Measured as `Mean FPS` for `phase: benchmark`

**Command:**

```python
./python.sh standalone_examples/benchmarks/benchmark_camera.py \
  --num-cameras 2 --resolution 1280 720 --num-gpus 1
```

**Configurations:**

* Camera count
* Camera resolution (default: 1280x720)
* GPU count (default: all available GPUs)

**Interpreting Results:**

```python
Mean FPS: 45.36 FPS
```

**Performance Notes:** Faster GPUs will achieve better performance as camera count and/or resolution increases. GPUs with lower VRAM may struggle to render multiple high resolution cameras or high counts of lower resolution cameras.

**Optimization Tips:**

1. Use minimum number of cameras and resolution to reduce rendering work.
2. Use as many GPUs as cameras to maximize throughput. Very high resolution cameras will also benefit from multiple GPUs due to tiling.
3. If visual quality is not critical, modify render settings to reduce realism of rendered images.
4. Use a simpler scene with fewer materials, textures, and lighting. This will simplify the rendering work done by each render product.

**Multi-GPU:** Camera rendering performance most effectively scales with the number of GPUs. The more GPUs, the more cameras can be rendered in parallel, improving throughput.

ROS 2 Render & Publishing Speed (Rendering + Physics + ROS2 Workflow)

**Purpose:** Measure full SIL workflow performance - combining rendering, physics, ROS2 message publishing, and robot control.

**What it measures:** Simulation framerate when publishing using ROS2 bridge using Nova Carter ROS asset, per wall-clock second. A total of 11 sensors are enabled: 3 lidars + 4 stereo camera pairs

**Measurement:** Overall speed is measured as `Mean FPS` for `phase: benchmark`.

**Command:**

```python
./python.sh standalone_examples/benchmarks/benchmark_robots_nova_carter_ros2.py \
  --num-robots 1 --enable-3d-lidar 1 --enable-2d-lidar 2 --enable-hawks 4
```

**Configuration:**

* 1x Nova Carter Robot

  + 1x 3D LiDAR sensor
  + 2x 2D LiDAR sensors
  + 4x Hawk stereo cameras (8x render products at 1920x1200p each)

**Interpreting Results:**

```python
[INFO] Mean FPS for phase: benchmark = 25.3
```

**Performance Notes:** This benchmarks uses a heavy sensor suite by default, reducing the number or resolution of sensors will improve performance. Lower VRAM GPUs (under 12GB) may not be able to render all sensors. Performance with fast CPUs will be limited by rendering speed, performance benefits will be observed with higher-spec GPUs or multi-GPU configurations.

**Optimization Tips:**

1. Reduce the camera count (`--enable-hawks 2`). This command runs 8 render products at 1920x1200p each. Reducing the camera count will reduce the number of render products and improve performance.
2. If visual quality is not critical, modify render settings to reduce accuracy of rendered images.
3. Use a simpler scene with fewer materials, textures, and lighting. This will simplify the rendering work done by each render product.

**Multi-GPU:** Performance scales with the sensor count. The more sensors, the more GPUs will help improve throughput. For server-grade hardware, simulating 4 Nova Carters with full sensor suites is feasible with 4x or 8x GPUs.

RTX Lidar ROS2 PointCloud2 Metadata Publishing

**Purpose:** Measure RTX Lidar performance when publishing PointCloud2 messages with configurable metadata fields using ROS2.

**What it measures:** Simulation framerate when creating multiple RTX Lidar sensors, each with their own ROS2 OmniGraph that publishes PointCloud2 messages with configurable metadata fields, in the full warehouse sample scene.

**Measurement:** Overall speed is measured as `Mean FPS` for `phase: benchmark`.

**Command:**

```python
./python.sh standalone_examples/benchmarks/benchmark_rtx_lidar_ros2_pcl_metadata.py \
  --num-frames 10 --num-sensors 2 --metadata \
  Intensity \
  Timestamp \
  EmitterId \
  ChannelId \
  MaterialId \
  TickId \
  HitNormal \
  Velocity \
  ObjectId \
  EchoId \
  TickState
```

**Configuration:**

* 2x RTX Lidar sensors (Example\_Rotary)
* All metadata fields enabled (Intensity, Timestamp, EmitterId, ChannelId, MaterialId, TickId, HitNormal, Velocity, ObjectId, EchoId, TickState)
* Full warehouse sample scene
* ROS2 bridge publishing PointCloud2 messages per sensor

**Configuration Options:**

```python
# Fewer sensors
./python.sh standalone_examples/benchmarks/benchmark_rtx_lidar_ros2_pcl_metadata.py \
  --num-sensors 1 --metadata Intensity ObjectId

# Solid state lidar
./python.sh standalone_examples/benchmarks/benchmark_rtx_lidar_ros2_pcl_metadata.py \
  --num-sensors 2 --lidar-type Solid_State --metadata Intensity ObjectId

# Fewer metadata fields
./python.sh standalone_examples/benchmarks/benchmark_rtx_lidar_ros2_pcl_metadata.py \
  --num-sensors 2 --metadata Intensity ObjectId
```

**Interpreting Results:**

```python
[INFO] Mean FPS for phase: benchmark = 25.3
```

**Performance Notes:** Enabling more metadata fields increases the amount of data published per PointCloud2 message, which may reduce throughput. Performance depends on sensor count, metadata field count, and GPU capability.

**Optimization Tips:**

1. Reduce the number of metadata fields to only those required for your use case.
2. Reduce the number of sensors to minimize parallel publishing overhead.
3. Use a simpler scene with fewer materials, textures, and lighting to reduce rendering work.

Synthetic Data Generation

Benchmarks for measuring synthetic data generation performance and throughput.

SDG Images per Second (Simple)

**Purpose:** Measure synthetic data generation performance with basic annotations

**What it measures:** Image generation rate with RGB and depth annotations for 500 prims, randomizing pose/orientation/scale/color per frame.

**Measurement:** Overall speed is measured as `Mean FPS` for `phase: benchmark`. Images generated per second is measured as `Mean FPS * number of cameras`.

**Command:**

```python
./python.sh standalone_examples/benchmarks/benchmark_sdg.py \
  --num-cameras 2 --resolution 1280 720 --asset-count 100 \
  --annotators rgb distance_to_image_plane --skip-write
```

**Configuration:**

* 2 cameras at 1280x720 resolution
* 100 count per asset type (5 types for total of 500 prims)
* RGB + depth annotations only
* Skip disk write for pure generation speed

**Interpreting Results:**

```python
[INFO] Mean FPS for phase: benchmark = 15.8
```

The throughput can be calculated as `Mean FPS * number of cameras` to yield the total number of images generated per second.

**Performance Notes:** The usage of the –skip-write flag improves performance by skipping the disk write step, which can cause a bottleneck due to IO operations. Randomization of pose/orientation/material are CPU-intensive operations currently.

**Optimization Tips:**

1. If saving to disk, review the I/O Optimization Guide in the Replicator documentation to optimize throughput.
2. Decrease total number of assets in the scene.
3. Minimize randomization operations, review are CPU-intensive.

**Multi-GPU:** Performance scales most effectively based on camera count and resolution. The more cameras, or higher the resolution, in the scene, the more GPUs will help improve throughput. This default benchmark with two 720p cameras does not scale well with more GPUs because it is limited by randomization operations.

SDG Images per Second (Complex)

**Purpose:** Measure synthetic data generation performance with full suite of annotators enabled.

**What it measures:** Image generation rate with all annotators enabled for 500 prims, randomizing pose/orientation/scale/color per frame.

**Measurement:** Overall speed is measured as `Mean FPS` for `phase: benchmark`. Images generated per second is measured as `Mean FPS * number of cameras`.

**Command:**

```python
./python.sh standalone_examples/benchmarks/benchmark_sdg.py \
  --num-cameras 2 --resolution 1280 720 --asset-count 100 \
  --annotators all --skip-write
```

**Configuration:**

* 2 cameras at 1280x720 resolution
* 100 count per asset type (5 types for total of 500 prims)
* All available annotators enabled
* Skip disk write for pure generation speed

**Annotators Available:**

* RGB
* Distance to Image Plane
* Distance to Camera
* Bounding Box 2D Tight
* Bounding Box 2D Loose
* Bounding Box 3D
* Semantic Segmentation
* Instance Segmentation
* Occlusion
* Normals
* Motion vectors
* Camera Parameters
* Point Cloud
* Skeleton Data

**Interpreting Results:**

```python
[INFO] Mean FPS for phase: benchmark = 4.2
```

The throughput can be calculated as `Mean FPS * number of cameras` to yield the total number of images generated per second.

**Performance Notes:** The usage of the `--skip-write` flag improves performance by skipping the disk write step review can cause a bottleneck due to IO operations. Randomization of pose/orientation/material are CPU-intensive operations, limiting GPU scaling.

**Optimization Tips:**

1. Disable unneeded annotators to improve performance for specific use cases.
2. If saving to disk, review the I/O Optimization Guide in the Replicator documentation to optimize throughput.
3. Decrease total number of assets in the scene.
4. Minimize randomization operations, review are CPU-intensive.

**Multi-GPU:** Performance scales most effectively based on camera count and resolution. The more cameras, or higher the resolution, in the scene, the more GPUs will help improve throughput. This default benchmark with two 720p cameras does not scale with more GPUs because it is limited by randomization operations rather than rendering.

## Understanding Benchmark Outputs

This section walks through the outputs of the benchmark script to explain the different metrics and how to interpret them.

The benchmark script outputs a summary report and a raw metric file. The summary report is a concise summary of the benchmark results. The metrics file contains the raw metrics that are parsed into the summary report. The log indicates where the metrics file is stored.

### Summary Report

The summary report is output to the console for every benchmark script. It provides a concise summary of the benchmark results.

**Example Output:**

```python
|----------------------------------------------------|
|                   Summary Report                   |
|----------------------------------------------------|
| workflow_name: benchmark_robots_nova_carter_ros2   |
| num_robots: 2                                      |
| num_gpus: 1                                        |
| num_3d_lidar: 1                                    |
| num_2d_lidar: 2                                    |
| num_hawks: 4                                       |
| num_cpus: 32                                       |
| gpu_device_name: NVIDIA GeForce RTX 4090           |
|----------------------------------------------------|
| Phase: loading                                     |
| System Memory RSS: 17.021 GB                       |
| System Memory VMS: 145.177 GB                      |
| System Memory USS: 16.997 GB                       |
| GPU Memory Tracked: 1.124 GB                       |
| Runtime: 5549.776 ms                               |
|----------------------------------------------------|
| Phase: benchmark                                   |
| System Memory RSS: 17.021 GB                       |
| System Memory VMS: 145.177 GB                      |
| System Memory USS: 16.997 GB                       |
| GPU Memory Tracked: 1.124 GB                       |
| Mean FPS: 51.706 FPS                               |
| Real Time Factor: 0.849                            |
| Runtime: 11772.105 ms                              |
| Frametimes (ms):    mean |  stdev |   min |   max  |
| App_Update         19.34 |   0.39 | 18.92 | 20.42  |
| Physics            17.61 |   0.08 | 17.52 | 17.99  |
|----------------------------------------------------|
```

#### Configuration Section

The first section shows the benchmark configuration and system information.

```python
|----------------------------------------------------|
| workflow_name: benchmark_robots_nova_carter_ros2   |
| num_robots: 2                                      |
| num_gpus: 1                                        |
| num_3d_lidar: 1                                    |
| num_2d_lidar: 2                                    |
| num_hawks: 4                                       |
| num_cpus: 32                                       |
| gpu_device_name: NVIDIA GeForce RTX 4090           |
|----------------------------------------------------|
```

It’s populated with the `workflow_metadata` dictionary passed into the `BaseIsaacBenchmark` object defined in each benchmark script.

#### Loading Phase Metrics

The loading phase measures resource usage during scene loading and other setup steps:

* **System Memory RSS:** Resident Set Size of the process in GB
* **System Memory VMS:** Virtual Memory Size of the process in GB
* **System Memory USS:** Unique Set Size of the process in GB
* **GPU Memory Tracked:** VRAM utilized by the GPU in GB
* **Runtime:** Wall-clock time in milliseconds

#### Benchmark Phase Metrics

The benchmark phase measures performance during active simulation:

**Performance Metrics:**

* **Mean FPS:** Computed as `1000/mean_app_update_frametime` where `mean_app_update_frametime` is the average frametime of the app update phase in milliseconds.
* **Real Time Factor:** A ratio of how close simulation time is to wall-clock time. Computed as `simulation_time / wall_clock_time` where `simulation_time` is the total time simulated and `wall_clock_time` is the real-world time elapsed.
* **Runtime:** The wall-clock duration in milliseconds of the benchmark phase.

**Frametime Breakdown:**

The frametimes section shows detailed timing for different simulation components:

* **App\_Update:** One app update represents one frame of the simulation. In default configurations, this typically involves one physics step and one render step.
* **Physics:** The duration of the physics step. This is a component of the total `app_update` frametime, representing the duration of physics computation work.
* **GPU:** The duration of GPU work. This is a component of the total `app_update` frametime, representing the duration of rendering work. This is only collected when the `--gpu-frametime` flag is enabled.

For further insight into how the frametime breaks down for a specific workflow, refer to [Profiling Performance Using Tracy](../utilities/debugging/profiling_performance.html#isaac-sim-app-profiling-performance) for details on using the Tracy profiler to profile the simulation.

Note

One app update is characterized by some amount of physics compute and some amount of rendering work for the given frame. The sum of these two components are not expected to equal the app\_update frametime due to parallelization, other overhead, and any dedicated per frame compute.

### Interpreting Results

This section details how to interpret some of the key results explained in the previous sections, specifically as they relate to hardware selection.

**Mean FPS:**

The Mean FPS is the key metric to consider when selecting hardware. It is the average frame rate of the simulation over the course of the benchmark. It is a good indicator of the overall performance of the hardware for a given workflow.

**GPU Memory Tracked:**

The GPU Memory Tracked metric indicates the amount of VRAM needed by the workflow. Workflows that involve large scenes, high resolution cameras, or large amounts of sensors will require more VRAM.

**Physics Frametime:**

A Physics Frametime very close to the App Update frametime indicates that the physics computation may be bottlenecking the performance. With GPU Physics, higher-spec GPUs will scale better with more physics objects and/or higher complexity robots.

**GPU Frametime:**

With a GPU frametime very close to the App Update frametime, it indicates that the GPU rendering might be bottlenecking the performance. Adding additional GPUs or using a higher-spec GPU will help improve performance. Otherwise, if the GPU frametime is much lower than the App\_Update frametime, it indicates that CPU performance might be the bottleneck.

## Benchmark Methodology Changes

This section tracks changes to benchmark methodologies, measurement scripts, and hardware configurations across Isaac Sim versions to enable accurate version-to-version comparisons.

Note

When comparing benchmark results between versions, ensure you account for any methodology or hardware changes listed below.

### Version 6.0.0

**Measurement Changes:**

* Updated reference hardware CPU for workstation hardware from Intel i9-14900k to Intel Core Ultra 9 285K for workstation GPU KPIs

**Script Changes:**

* No changes to benchmark scripts in this version

### Version 5.1.0

**Measurement Changes:**

* Motion BVH disabled by default (previously enabled) - decreases rendering accuracy for motion-related sensor effects but improves rendering performance

**Script Changes:**

* Disabled default collection of GPU frametime due to slight performance impact on overall benchmark performance. Can be enabled with `--gpu-frametime` flag.

### Version 5.0.0

**Measurement Changes:**

* KPIs measured with Motion BVH (enabled by default in Isaac Sim 5.0.0) - increases rendering accuracy for motion-related sensor effects but decreases overall rendering performance

**Script Changes:**

* Disabled viewport updates by default in headless mode to improve performance (can be enabled with `--viewport-updates`)
* Physics Steps per Second (`benchmark_robots_o3dyn.py`): Added support for both CPU and GPU physics backends (previously CPU only).

  + Backend default changed from CPU to GPU (torch) physics backend
  + Robot count default changed from 2 to 10

### Version 4.5.0

**Measurement Changes:**

* Initial baseline measurements

**Script Changes:**

* Benchmark scripts introduced in `standalone_examples/benchmarks/`

On this page

* [GPU-Independent KPIs](#gpu-independent-kpis)
* [GPU-Dependent KPIs](#gpu-dependent-kpis)
  + [Workstation GPUs](#workstation-gpus)
  + [Server GPUs](#server-gpus)
* [Measuring KPIs on Local Hardware](#measuring-kpis-on-local-hardware)
* [Understanding Benchmark Outputs](#understanding-benchmark-outputs)
  + [Summary Report](#summary-report)
    - [Configuration Section](#configuration-section)
    - [Loading Phase Metrics](#loading-phase-metrics)
    - [Benchmark Phase Metrics](#benchmark-phase-metrics)
  + [Interpreting Results](#interpreting-results)
* [Benchmark Methodology Changes](#benchmark-methodology-changes)
  + [Version 6.0.0](#version-6-0-0)
  + [Version 5.1.0](#version-5-1-0)
  + [Version 5.0.0](#version-5-0-0)
  + [Version 4.5.0](#version-4-5-0)

---

