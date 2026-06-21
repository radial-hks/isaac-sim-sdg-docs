---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/omnigraph/omnigraph_scripting.html
title: "OmniGraph Scripting"
section: "OmniGraph"
module: "08-omnigraph-robot-sim"
checksum: "d54c6cd7c04fc1fb"
fetched: "2026-06-21T13:40:09"
---

* [OmniGraph](index.html)
* OmniGraph via Python Scripting Tutorial

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# OmniGraph via Python Scripting Tutorial

While OmniGraph is intended to be a visual scripting tool, it does have Python scripting interfaces. This tutorial will give some examples of how to script an action graph using Python.

## Learning Objectives

This tutorial will

* walk you through examples of scripting an OmniGraph using purely Python APIs
* introduce the basic concepts and frequently used parameters in OmniGraphs and showcase them using scripted examples

## Getting Started

**Prerequisites**

* Review the GUI Tutorial series, especially [Isaac Sim OmniGraph Tutorial](omnigraph_tutorial.html#isaac-sim-app-tutorial-gui-omnigraph) and [Omniverse Script Editor](../development_tools/omniverse_script_editor.html#isaac-sim-app-omniverse-script-editor) prior to beginning this tutorial.
* Review the Core API Tutorial series, especially [Hello World](../core_api_tutorials/tutorial_core_hello_world.html#isaac-sim-app-tutorial-core-hello-world) to become familiar with the extension workflow via Python, as well as the Python Standalone workflow.

## Code Snippets

### Creating a Graph

First let’s build a simple action graph that prints “Hello World” to the console on every simulation frame.

1. Open ‘Window > Script Editor’ and paste the following code:

   > ```python
   > import omni.graph.core as og
   >
   > keys = og.Controller.Keys
   > graph_handle, list_of_nodes, _, _ = og.Controller.edit(
   >     {"graph_path": "/action_graph", "evaluator_name": "execution"},
   >     {
   >         keys.CREATE_NODES: [("tick", "omni.graph.action.OnTick"), ("print", "omni.graph.ui_nodes.PrintText")],
   >         keys.SET_VALUES: [
   >             ("print.inputs:text", "Hello World"),
   >             (
   >                 "print.inputs:logLevel",
   >                 "Warning",
   >             ),  # setting the log level to warning so we can see the printout in terminal
   >         ],
   >         keys.CONNECT: [("tick.outputs:tick", "print.inputs:execIn")],
   >     },
   > )
   > ```
2. Press ‘Run’ to execute the script. You should see a new prim `/action_graph` created on the Stage tree.
3. Expand the prim on stage, the nodes “tick” and “print” should be listed under the graph. These nodes can be accessed just like any other prim on the stage.
4. Press “play” to start the simulation. You should see “Hello World” printed to the console on every frame.
5. Open graph editor by going to Window > Graph Editors > Action Graph.
6. With the newly created graph highlighted on the Stage tree on the right, open the graph by clicking on the icon for ‘Edit Action Graph’ in the graph editor window. You should see two nodes connected with each other by a line.

### Editing a Graph

Once a graph has been created, there are specific APIs to manipulate the graph’s terms.

**Getting and Setting Attribute Values**

Open another tab in the Script Editor, paste the snippet below, and run.

```python
import omni.graph.core as og

# get existing value from an attribute
existing_text = og.Controller.attribute("/action_graph/print.inputs:text").get()
print("Existing Text: ", existing_text)

# set new value
og.Controller.attribute("/action_graph/print.inputs:text").set("New Texts to print")
```

This will change the value in the “Print Text” node from “Hello World” to “New Texts to print”. But this affect won’t take place until the first tick through the graph. So when you press ‘Run’ in the script editor, the graph has yet to be ticked, so it should fetch the current value from the node, and print out a single string of “Existing Text: Hello World” in the Script Editor’s console (as well as the terminal if you are using that, or the main Omniverse’s console if you include “Info” to be printed).

Now press ‘Play’ and start the simulation. It should now print, at the rate of one string per tick, the updated text “New Texts to print”, in the terminal or the main Omniverse console (though not the Script Editor’s console).

**Adding Nodes and Connections**

Open a third tab in the Script Editor to add nodes and make more connections to an existing graph.

```python
import omni.graph.core as og

og.Controller.create_node("/action_graph/new_node_name", "omni.graph.nodes.ConstantString")
og.Controller.attribute("/action_graph/new_node_name.inputs:value").set("This is a new node")
og.Controller.connect("/action_graph/new_node_name.inputs:value", "/action_graph/print.inputs:text")
```

A new node named “new\_node\_name” will be created and connected to the “Print Text” node. If you have the graph editor (Window > Graph Editors > Action Graph) open, you can see that there are now three nodes connected to each other instead of two.

### Graph Execution

By default, the graph is evaluated on every frame. You can change this behavior by setting the graph to evaluate only when you call it.

You can also trigger each graph explicitly by making execute only when you call it. To do this, there is a special parameter called “pipeline\_stage” where you can set the graph to execute “On Demand”. Most of the times we want to set this variable during the creation of the graph:

1. Delete the previous graph by selecting it on the stage tree and pressing ‘Delete’ key.
2. Open a new tab in the Script Editor and paste the following code

   > ```python
   > import omni.graph.core as og
   >
   > keys = og.Controller.Keys
   > demand_graph_handle, _, _, _ = og.Controller.edit(
   >     {
   >         "graph_path": "/ondemand_graph",
   >         "evaluator_name": "execution",
   >         "pipeline_stage": og.GraphPipelineStage.GRAPH_PIPELINE_STAGE_ONDEMAND,
   >     },
   >     {
   >         keys.CREATE_NODES: [("tick", "omni.graph.action.OnTick"), ("print", "omni.graph.ui_nodes.PrintText")],
   >         keys.SET_VALUES: [("print.inputs:text", "On Demand Graph"), ("print.inputs:logLevel", "Warning")],
   >         keys.CONNECT: [("tick.outputs:tick", "print.inputs:execIn")],
   >     },
   > )
   > ```
3. Press ‘Run’ in the Script Editor. A new graph `/ondemand_graph` will be created.
4. Start simulation by press “play”, nothing should be printed from this graph because we did not explicitly call to evaluate it.
5. To manually trigger a graph, open another tab, and paste in `demand_graph_handle.evaluate()`
6. Make sure simulation is still running. Click ‘Run’ in the Script Editor. You should see “On Demand Graph” printed to the console once.

Alternatively, you can also set it for an existing graph by `demand_graph_handle.change_pipeline_stage(og.GraphPipelineStage.GRAPH_PIPELINE_STAGE_ONDEMAND)`

A more in-depth example of attaching graphs to physics callbacks and/or rendering callbacks can be found in standalone\_examples/api/isaacsim.core.experimental.api/omnigraph\_triggers.py

## Summary

In this tutorial, we introduced scripting OmniGraph via Python.

### Further Reading

For more Python Scripting API in [OmniGraph APIs](https://docs.omniverse.nvidia.com/kit/docs/omni.graph/latest/omni.graph.core.html)

On this page

* [Learning Objectives](#learning-objectives)
* [Getting Started](#getting-started)
* [Code Snippets](#code-snippets)
  + [Creating a Graph](#creating-a-graph)
  + [Editing a Graph](#editing-a-graph)
  + [Graph Execution](#graph-execution)
* [Summary](#summary)
  + [Further Reading](#further-reading)