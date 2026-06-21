---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/omnigraph/omnigraph_custom_python_nodes.html
title: "Custom Python Nodes"
section: "OmniGraph"
module: "08-omnigraph-robot-sim"
checksum: "b9172bdcd79da502"
fetched: "2026-06-21T13:40:09"
---

* [OmniGraph](index.html)
* Custom Python Nodes

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Custom Python Nodes

There already exist a large number of default nodes that comes with Isaac Sim. You can find the definitions and descriptions for them in either the [OmniGraph Node Library](https://docs.omniverse.nvidia.com/extensions/latest/ext_omnigraph/node-library/node-library.html "(in Omniverse Extensions)") or [API Documentation](../reference_python_api.html#isaac-sim-python-manual). If those prove to be insufficient, you can write your own and integrate them into Isaac Sim.

A node is defined by two files, an .ogn file, which is a JSON file that defines the structure of the node, including its inputs, outputs, and parameters. Either a Python file or a C++ file can be used to define its function. Here we will focus on Python nodes.

## Node Files

All OmniGraph Node files starts with “Ogn” as a prefix. This is expected by the parser.

### Node Definition (.ogn)

The .ogn file is a JSON file that defines the structure of the node, including its inputs, outputs, and parameters. Here is an example of a simple node definition:

```python
 1{
 2 "NodeName": {
 3     "version": 1,
 4     "categories": "examples",
 5     "description": ["Minimum Example"],
 6     "language": "python",
 7     "metadata": {
 8         "uiName": "minimum example"
 9     },
10     "inputs": {
11                        "execIn": {
12             "description": "the trigger input that starts the node",
13             "type": "execution",
14         },
15                        "value_input": {
16             "type": "double",
17             "description": "a number",
18             "default": 0.0,
19          },
20     },
21     "outputs": {
22         "output_bool": {
23             "type": "bool",
24             "description": "let output be a boolean",
25          }
26      }
27   }
28}
```

A note about the input “execIn”. This is a special input that is used to trigger the node. This trigger is only relevant in an Action Graph, where you must explicitly trigger the node to run, such as on a physics tick, or a stage event, like opening and closing a stage. In a Push Graph, the node will run automatically at every frame and the ‘execIn’ input is not necessary.

### Function Definition

Here’s a minimum example of a Python node that takes an input number and outputs a boolean value based on whether the input is greater than 0:

```python
class OgnNodeName:
    @staticmethod
    def compute(db):
        db.outputs.out = bool(db.inputs.value_input > 0.0)
        return True
```

Notes:

* the class name must match the name of the node in the .ogn file, and the file name must match the class name.
* the “compute” function is what the ‘execIn’ input triggers. It takes a single argument, the database, which contains the inputs and outputs of the node. The function should return True if the node ran successfully, and False if it failed.
* this node has no internal state, which means all data that passes through it is gone the next tick. If you need to store data between ticks, you can use the “internal state” to store it.

## Using the Custom Node

You can simply insert your custom node’s `.py` and `.ogn` files into any of extensions that already have a directory that contains the `.py` and `.ogn` files for existing nodes and thereby avoid creating your own extension that way.

You can also create your own extension and insert the files there. (link to the new template generator)

## Isaac Sim Nodes as Examples

You are welcome to dig into the code behind some of our existing OmniGraph nodes to find examples of how to structure a node, or even modify them to suite your own need. To find the backend `.py` and `.ogn` files for a particular node. Hover your mouse over the node in the editor window, a tooltip window will appear and the name of the extension will be written in the parentheses. You can then navigate to the extensions’s folder that contains the backend scripts for the nodes by going to `exts/isaacsim.<ext_name>/isaacsim/<ext_name>/ogn/python/nodes/`.

Not all of the nodes are written in Python, some have C++ backends, so if you won’t necessarily see a corresponding `.py` and `.ogn` files for all the nodes on the list. Note that if you found a folder with a list of `Ogn<node_name>Database.py`, this is NOT the directory that contains the Python description of the node.

On this page

* [Node Files](#node-files)
  + [Node Definition (.ogn)](#node-definition-ogn)
  + [Function Definition](#function-definition)
* [Using the Custom Node](#using-the-custom-node)
* [Isaac Sim Nodes as Examples](#isaac-sim-nodes-as-examples)