---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/omnigraph/omnigraph_tutorial.html
title: "OmniGraph Tutorial"
section: "OmniGraph"
module: "08-omnigraph-robot-sim"
checksum: "131e6b392df29746"
fetched: "2026-06-21T13:05:38"
---

* [OmniGraph](index.html)
* Isaac Sim OmniGraph Tutorial

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Isaac Sim OmniGraph Tutorial

This tutorial introduces you to the world of visual programming via OmniGraph.
We highly recommend that you also read [OmniGraph](https://docs.omniverse.nvidia.com/extensions/latest/ext_omnigraph.html "(in Omniverse Extensions)"), because it is a key component in Omniverse Kit.

## Learning Objectives

This tutorial aims to

* walk you through building an action graph to control a robot in Isaac Sim, specifically, the Jetbot.
* show you how to use the OmniGraph shortcuts to generate a differential controller graph for the Jetbot.

## Build the Graph

Letâs build an action graph to control a robot in Isaac Sim the Jetbot.

### Setting Up the Stage

1. On a new stage, start by right clicking and selecting **create > Physics > Ground Plane**.
2. In the Content Browser, navigate to `Isaac Sim/Robots/NVIDIA/Jetbot/jetbot.usd`.
3. Click and drag `jetbot.usd` onto the stage.
4. Position the JetBot just above the ground plane.
5. When completed, verify that the JetBot is under `/World/jetbot` in the context tree and that the stage looks similar to:

Jetbot on the stage

Note

Click play! Validate that the JetBot falls and lands on the stage. Click stop before continuing.

Depending on your default render settings, the camera of the JetBot may have a placeholder mesh (it looks like a gray television camera).
To hide these meshes, click on the  icon in the viewport and select **Show By Type â> Cameras**.

### Building the Graph

1. Select **Window > Graph Editors > Action Graph** from the dropdown menu at the top of the editor.
   The Graph Editor appears in the same pane as the Content browser.
2. Click **New Action Graph** to open an empty graph.
3. Type `controller` in the search bar of the graph editor.
4. Drag an `Articulation Controller` and a `Differential Controller` onto the graph.

The `Articulation Controller` applies driver commands (in the form of force, position, or velocity) to the specified joints
of any prim with an articulation root.

To tell the controller which robot itâs going to control:

1. Select the `Articulation Controller` node in the graph and open up the property pane.
2. You can either:

   * Click **usePath** and Type in the path to the robot */World/jetbot* in **robotPath**

     **OR**
   * Click **Add Targets** near the top of the pane for `input:targetPrim` and select **JetBot** in the pop up window.

The `Differential Controller` computes drive commands for a two wheeled robot given some target linear and angular velocity. Like the
`Articulation Controller`, it also needs to be configured.

1. Select the `Differential Controller` node in the graph.
2. In the properties pane, set the `wheelDistance` to 0.1125, the `wheelRadius` to 0.03, and `maxAngularSpeed` to 0.2.

The `Articulation Controller` also needs to know which joints to articulate. It expects this information in the form of a list of tokens or index values. Each joint in a robot has a name and the JetBot has exactly two. Verify this by examining the JetBot in the stage context tree. Within `/World/jetbot/chassis`
are two revolute physics joints named `left_wheel_joint` and `right_wheel_joint`.

Stage Tree

1. Type `token` into the search bar of the graph editor.
2. Add two `Constant Token` nodes to the graph.
3. Select one and set itâs value to `left_wheel_joint` in the properties pane.
4. Repeat this for the other constant token node, but set the value to `right_wheel_joint`.
5. Type `make array` into the search bar of the graph editor.
6. Add a `Make Array` node to the graph.
7. Select the `Make Array` node and click on the `+` icon in the `inputs` section of the property pane menu to add a second input.
8. Set the `arraySize` to 2 and set the input type to `token[]` from the dropdown menu in the same pane.
9. Connect the constant token nodes to `input0` and `input1` of the `Make Array` node, and then the output of that node to the `Joint Names` input of the `Articulation Controller` node.

The last node is the event node.

1. Search for `playback` in the search bar of the graph editor.
2. Add an `On Playback Tick` node to the graph. This node emits an execution event for every frame, but only while the simulation is playing.
3. Connect the `Tick` output of the `On Playback Tick` node to the `Exec In` input of both controller nodes.
4. Connect the `Velocity Command` output of the differential controller to the `Velocity Command` input of the articulation controller.
5. Validate that the graph looks similar to:

Simple differential control for the JetBot

1. Press the play button.
2. Select the `Differential Controller` node in the graph.
3. Click and drag on either the angular or linear velocity values in the properties pane to change itâs value (or just click and type in the desired value).

Note

Explore the available OmniGraph nodes and try to setup a graph to control the JetBot with the keyboard. The graph
below is an example graph for controlling the JetBot with a keyboard.

Keyboard control Action graph for the JetBot

## OmniGraph Shortcuts

Putting the graph from scratch can be tedious, especially when you have to iterate. We made some shortcuts for frequently used graphs, so that within a couple clicks, you can generate a complex graph with multiple nodes and connections. They can be found under `Tools -> Robotics -> OmniGraph Controllers`, and the instructions for them are in [Commonly Used OmniGraph Shortcuts](omnigraph_shortcuts.html#isaac-sim-app-tutorial-advanced-omnigraph-shortcuts).

To use the Differential Controller graph from the menu shortcut:

1. Delete (or Disable if that is an option) any previous OmniGraphs that controls the Jetbot.
2. Go to the Menu bar and click on **Tools -> Robotics -> OmniGraph Controllers -> Differential Controller**.
3. You are prompted for the necessary parameters.
4. Add â/World/jetbotâ to `Articulation Root`, set the **distance between wheels** to 0.1125, and the **wheel radius** to 0.03.
5. Given JetBot only has two controllable joints, you can leave the rest of the fields empty.
6. Turn **Use Keyboard Control (WASD)** on.
7. Click **OK** to generate the graph. You can open the generated graph under `/Graph/differential_controller`.
8. Press **Play** to start simulation.
9. Verify that you can move the JetBot using the WASD keys on the keyboard.

## Summary

This tutorial covered:

* Basic concepts of OmniGraph
* Setting up a stage with a robot
* Using OmniGraph to construct interfaces to a robot
* Using the OmniGraph shortcuts to generate differential controller graph

### Further Learning

* More in-depth concepts in [OmniGraph](https://docs.omniverse.nvidia.com/extensions/latest/ext_omnigraph.html "(in Omniverse Extensions)")
* More details about all the OmniGraph shortcuts [Commonly Used OmniGraph Shortcuts](omnigraph_shortcuts.html#isaac-sim-app-tutorial-advanced-omnigraph-shortcuts)
* Examples for composing OmniGraph via Python scripting: [OmniGraph via Python Scripting Tutorial](omnigraph_scripting.html#isaac-sim-app-tutorial-advanced-omnigraph-scripting)
* Examples for writing custom Python nodes: [Custom Python Nodes](omnigraph_custom_python_nodes.html#isaac-sim-app-omnigraph-custom-python-nodes)

On this page

* [Learning Objectives](#learning-objectives)
* [Build the Graph](#build-the-graph)
  + [Setting Up the Stage](#setting-up-the-stage)
  + [Building the Graph](#building-the-graph)
* [OmniGraph Shortcuts](#omnigraph-shortcuts)
* [Summary](#summary)
  + [Further Learning](#further-learning)