---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/development_tools/vscode.html
title: "VS Code"
section: "开发工具"
module: "02-fundamentals-dev"
checksum: "d2c6927fa757d3f2"
fetched: "2026-06-21T12:48:07"
---

* [Development Tools](index.html)
* Visual Studio Code (VS Code)

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Visual Studio Code (VS Code)

## Isaac Sim VS Code Edition

[Isaac Sim VS Code Edition](https://marketplace.visualstudio.com/items?itemName=NVIDIA.isaacsim-vscode-edition) is an extension for Visual Studio Code that provides development support for NVIDIA Omniverse in general and Isaac Sim in particular.

Key Features:

* Execute Python code, in the Python environment of a running application, locally or remotely from VS Code and show the output in the *Isaac Sim VS Code Edition* panel.
* Browse and insert snippets of code related to Isaac Sim, Omniverse Kit and Universal Scene Description (USD).
* Create templates for Omniverse/Isaac Sim extensions and other development approaches.
* Quick access to the most relevant Omniverse/Isaac Sim documentation sources and resources without leaving the editor.

**Install it now to get started**: [Isaac Sim VS Code Edition](https://marketplace.visualstudio.com/items?itemName=NVIDIA.isaacsim-vscode-edition)

---

## Interactive Scripting

The `isaacsim.code_editor.vscode` extension adds VS Code launcher and menu integration to Isaac Sim.
It depends on the `isaacsim.code_editor.python_server` extension which provides the TCP server for remote Python code execution (see [Python Server (Remote Code Execution)](python_server.html#isaac-sim-app-python-server) for full protocol details and usage examples).

Both extensions can be enabled or disabled using the [Extension Manager](https://docs.omniverse.nvidia.com/extensions/latest/ext_core/ext_extension-manager.html "(in Omniverse Extensions)") by searching for `isaacsim.code_editor.vscode`.
Enabling the VS Code extension automatically enables the Python server.

> Note
>
> This extension requires its Visual Studio Code pair extension: [Isaac Sim VS Code Edition](https://marketplace.visualstudio.com/items?itemName=NVIDIA.isaacsim-vscode-edition) to be installed and enabled, in the VS Code editor, in order to execute Python scripts on a running Isaac Sim instance.

1. To begin, enable this extension using the [Extension Manager](https://docs.omniverse.nvidia.com/extensions/latest/ext_core/ext_extension-manager.html "(in Omniverse Extensions)") by searching for `isaacsim.code_editor.vscode`.
2. Once the extension is enabled, go to the top menu bar and click on Window > VS Code to open the Isaac Sim folder in a VS Code application.
3. Open a stored file or write the code you want to run in a VS Code editor tab.
4. From the VS Code editor, click on the *Isaac Sim VS Code Edition* container in the Activity Bar (the one with the Isaac Sim logo) to open it.
   Then, click on *Run* (or *Run selected text* if you have selected code statements), in the *Commands* tree view, to execute it.
5. Inspect the execution output, if any, in the *Isaac Sim VS Code Edition* output panel.

Tip

The Python server can also be used independently of VS Code, for example by LLM agents or custom scripts.
See [Python Server (Remote Code Execution)](python_server.html#isaac-sim-app-python-server) for details on the wire protocol and programmatic usage.

---

## VS Code Configuration Files

The Isaac Sim installation provides a `.vscode` workspace with a pre-configured environment under the following three files:

```python
.vscode/launch.json
.vscode/settings.json
.vscode/tasks.json
```

### launch.json

This file provides three different configurations that can be executed using the `Run & Debug` section in VSCode.

* **Python: Current File**: Debug the currently open standalone Python file, should not be used with extension examples/code.
* **Python: Attach**: Attach to a running Isaac Sim application for debugging purposes, most useful when running an interactive GUI application. See [Attaching the Debugger to a Running App](../utilities/debugging/tutorial_advanced_python_debugging.html#isaac-sim-app-tutorial-advanced-attach-debugger) for usage information.
* **(Linux) isaac-sim** Run the main Isaac Sim application with an attached debugger.

### settings.json

This file sets the default Python executable that comes with Isaac Sim:

```python
# "python.pythonPath": "${workspaceFolder}/kit/python/bin/python3",
```

As well as a configuration for `"python.analysis.extraPaths"` which by default includes all of the extensions that are provided by default. You can add additional paths here if needed.

### tasks.json

This is a helper file that contains a task used to automatically setup the Python environment when using the `Python: Current File` option in `Run & Debug`.

```python
# "tasks": [
#     {
#         "label": "setup_python_env",
#         "type": "shell",
#         "linux": {
#             "command": "source ${workspaceFolder}/setup_python_env.sh && printenv >${workspaceFolder}/.vscode/.standalone_examples.env"
#         }
#     }
# ]
```

Once executed, the task generates the `.standalone_examples.env` file used by VS Code to launch the Python debug process.
Refer to [Debugging With Visual Studio Code](../utilities/debugging/tutorial_advanced_python_debugging.html#isaac-sim-app-tutorial-advanced-debug-vscode) for more details.

On this page

* [Isaac Sim VS Code Edition](#id1)
* [Interactive Scripting](#interactive-scripting)
* [VS Code Configuration Files](#vs-code-configuration-files)
  + [launch.json](#launch-json)
  + [settings.json](#settings-json)
  + [tasks.json](#tasks-json)