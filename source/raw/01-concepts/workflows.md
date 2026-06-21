---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/introduction/workflows.html
title: "Workflows"
section: "概念"
module: "01-concepts"
checksum: "a27d7e9df5133e06"
fetched: "2026-06-21T13:39:50"
---

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