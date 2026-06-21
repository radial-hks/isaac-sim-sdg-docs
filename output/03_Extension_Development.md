# Extension 开发

> Omniverse Kit Extension 从零搭建：模板、搜索、更新、调试
> Isaac Sim 版本: 6.0
> 最后组装: 2026-06-21 14:14 UTC
> 来源页数: 10

---

## 来源链接

- [Templates Index](https://docs.isaacsim.omniverse.nvidia.com/latest/utilities/templates_index.html)
- [Extension Templates Tutorial](https://docs.isaacsim.omniverse.nvidia.com/latest/utilities/extension_templates_tutorial.html)
- [CLI Extension Templates](https://docs.isaacsim.omniverse.nvidia.com/latest/utilities/cli_extension_templates.html)
- [VSCode Extension Template Generator](https://docs.isaacsim.omniverse.nvidia.com/latest/utilities/vscode_extension_template_generator.html)
- [Search Extension Tutorial](https://docs.isaacsim.omniverse.nvidia.com/latest/utilities/tutorial_search_extension.html)
- [Updating Extensions](https://docs.isaacsim.omniverse.nvidia.com/latest/utilities/updating_extensions.html)
- [Content Browser](https://docs.isaacsim.omniverse.nvidia.com/latest/utilities/content_browser.html)
- [Browsers](https://docs.isaacsim.omniverse.nvidia.com/latest/utilities/browsers.html)
- [Building C++ USD Plugins](https://docs.isaacsim.omniverse.nvidia.com/latest/omniverse_usd/building_cpp_usd_plugins.html)
- [Application Template](https://docs.isaacsim.omniverse.nvidia.com/latest/app_template/index.html)

---


## Extension 模板

### Templates Index

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/utilities/templates_index.html

* Templates

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Templates

We have many templates and template generator tools to help you get started with your projects.

* To scaffold a new extension from the terminal, use the [CLI Extension Templates](cli_extension_templates.html#isaac-sim-cli-extension-templates). These cover Python, UI (with scene management and Examples Browser), C++, and OmniGraph extensions.
* You can use the Extension Template Generator to create a new extension projects: [Extension Template Generator](extension_template_generator.html#isaac-sim-app-extension-template-generator). These templates are structured to utilize Isaac Sim libraries and built with robotics applications in mind.
* For extension using any combinations of C++, Python, OmniGraph, GUI elements, and more, refer to the [Advanced Extension Template Generator from VS Code](vscode_extension_template_generator.html#isaac-sim-app-vscode-extension-template-generator).

These are all for Extension-based projects. For standalone projects, simply browse through our Standalone Examples folder (`PATH_TO_ISAAC_SIM/standalone_examples`), and use them as a starting point.

---

### Extension Templates Tutorial

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/utilities/extension_templates_tutorial.html

* [Templates](templates_index.html)
* [Extension Template Generator](extension_template_generator.html)
* Extension Template Generator Explained

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Extension Template Generator Explained

Deprecated since version 6.0.0: The UI-based Extension Template Generator (`isaacsim.examples.extension`) is deprecated.
Use the [CLI Extension Templates](cli_extension_templates.html#isaac-sim-cli-extension-templates) instead.

## General Concepts

Each template provided by the *Extension Template Generator* has a common underlying structure with a thin layer of implementation on top.
In each template root directory, there is a folder called `./scripts` where all Python code supporting the extension is stored. Inside
`./scripts`, there are three common Python files:

* global\_variables.py
  :   A script that stores the global variables that the user specified when creating their extension in the *Extension Template Generator*
      such as the Title and Description.
* extension.py
  :   A class containing the standard boilerplate necessary to have the user extension show up on the Toolbar. This
      class is meant to fulfill most use-cases without modification.
      In extension.py, useful standard callback functions are created that the user may complete in ui\_builder.py.
* ui\_builder.py
  :   This file is the user’s main entrypoint into the template. Here, the user can see useful callback functions that have been
      set up for them, and they may also create UI elements that are hooked up to user-defined callback functions. This file is
      the most thoroughly documented, and the user should read through it before making serious modification.

A typical user will only need to modify `./scripts/ui_builder.py` to get their extension working the way they want. Inside `./scripts/ui_builder.py`, the user
will find a set of standard callback functions that connect them to the simulator:

* on\_menu\_callback(): Called when extension is opened
* on\_timeline\_event(): Called when timeline is stopped, paused, or played
* on\_physics\_step(): Called on every physics step. Physics steps only happen while the timeline is playing.
* on\_stage\_event(): Called when stage is opened or closed
* cleanup(): Called when resources such as physics subscriptions should be cleaned up because the extension is being closed
* build\_ui(): User function that creates the UI they want.

In the provided extension templates, most of the implementation is in the `build_ui()` function. The extension templates utilize a set of wrapper classes around
`omni.ui` elements that allow the user to easily create and manage a variety of UI elements. These are referred to in this tutorial as `UIElementWrappers`. Each wrapper is meant to provide the
user with the most common-sense way of interacting with a UI element. For example, the user can create a `FloatField` UI element; any time the user modifies the `FloatField` in the UI,
a user callback function will be called with the new `float` value passed in.

Each extension template builds a UI with a set of governing callback functions in `build_ui()`. These callback functions contain all of the logic to make the UI run smoothly and
make it easy to connect user code for a custom application.

## Loaded Scenario Template

The *Loaded Scenario Template* starts the user off with a simple UI that contains three buttons: *Load*, *Reset*, and *Run*. This is meant to provide
as clear a pathway as possible for the user to start writing code to directly affect the USD stage without having to understand much about the
internal workings of the underlying simulator. There user only needs to know the following simple concepts.

### Important Concepts

In Omniverse Kit Applications, there is a simulation timeline that can be directly stopped, paused, and played on the left-hand side toolbar. Physics
is only running while the timeline is active (not stopped). As such, the user cannot control a robot `Articulation` while the timeline is stopped,
and initialization needs to be performed on certain assets such as an `Articulation` when the timeline goes from stopped to playing. The purpose of the
*Loaded Scenario Template* is to make it easier for the user to interact with the simulator without having to handle things like initialization.

In `isaacsim.core.api.world` there is a singleton class `World` that is designed to set up and properly manage the simulation with simple and clear
user-interaction. In this template, the `World` is managed by the *Load* and *Reset* buttons, leaving the user with clear guarantees about the
state of the simulator at the time that their callback functions are called. The user interaction with the `World` is minimized to the point that
they their only interaction with the `World` takes the form `world.scene.add(user_object)` where `user_object` is any object from `isaacsim.core.api`.

To ensure proper functionality, all manipulation of the timeline should be done by the *Load* and *Reset* buttons. I.e. the user is able to cause trouble
by pressing the *Stop* and *Play* buttons on the left-hand toolbar outside of this UI. For this reason, the template directly handles the cases where
the user messes with the timeline outside of the template UI by resetting the UI when necessary to maintain assumptions on user callback functions.

### Implementation Details

The *Load* button has two callback functions:

* def setup\_scene\_fn():
  :   On pressing the *Load* button, a new instance of `World` is created and then this function is called.
      The user should now load their assets onto the stage and add them to the `World` with `world.scene.add()`.
* def setup\_post\_load\_fn():
  :   The user may assume that their assets have been loaded by their setup\_scene\_fn callback, that
      their objects are properly initialized, and that the timeline is paused on timestep 0.

The *Reset* button has two callback functions:

* pre\_reset\_fn():
  :   This function is called before the `World` is reset, so there are no guarantees on the state of the simulator.
* post\_reset\_fn():
  :   The user may assume that their objects are properly initialized, and that the timeline is paused on timestep 0.

      They may also assume that objects that were added to the `World` have been moved to their default positions.
      I.e. a cube prim will move back to the position it was in when it was created in setup\_scene\_fn().

The *Run* button is not connected to the `World`. It is a `StateButton`, which means that it will switch between two states: *Run* and *Stop*.
A `StateButton` can have three callback functions:

* on\_a\_click():
  :   Function called when the `StateButton` is showing its a\_text
* on\_b\_click():
  :   Function called when the `StateButton` is showing its b\_text
* physics\_callback\_fn():
  :   If specified, the `StateButton` will call this function on every physics step while the state button is in its B state, and
      it will cancel the physics subscription whenever the state button is in its A state.

Note

You can see how these functions are called in the `UIBuilder` class (`template_source_files/loaded_scenario_workflow/ui_builder.py` file in the `isaacsim.examples.extension` extension).

To try it, open the Template Generator (*Utilities > Generate Extension Templates* menu) and create a new extension under the *Loaded Scenario Template* section.
Then, enable the extension (*Window > Extensions* menu, search for the given extension name) and click on the toolbar entry with the same name.

## Scripting Template

The *Scripting Template* is a natural extension of the *Loaded Scenario Template* that demonstrates the
implementation of a more advanced framework for programming script-like behavior from a UI-based
extension in NVIDIA Isaac Sim. This template uses the same mechanics for loading and resetting the robot
position, but it implements the *Run* button as a script.

Using the pattern demonstrated in this template, the user can program script-like behavior by implementing
long-running functions that check in on every physics step to send a new command or determine that it is
time to return. The *Scripting Template* contains an implementation of the functions `goto_position()`,
`open_gripper_franka()` and `close_gripper_franka()`. These functions are used in series in order to
script the simple pick-and-place task shown below.

### Implementation Details

The implementation details of the UI match the *Loaded Scenario Template*, and so this section focuses
on the implementation of script-like behavior. Long-running functions that check in on every frame
can be written using Python’s yield/generator framework. A function `my_script()` is implemented in
the file `scenario.py` that contains the sequence of `goto_position()`, `open_gripper_franka()`, and
`close_gripper_franka()` function calls. The `my_script()` function makes use of `yield` and `yield from` statements.
This allows `my_script()` to be wrapped in a generator with `self._script_generator = self.my_script()`.
Then, on every physics step, `next(self._script_generator)` is called to step the generator and
execute code until the next `yield` statement is encountered (in either `my_script()` or a nested function).

Take the function `open_gripper_franka()` as an example:

```python
def open_gripper_franka(self, articulation):
    open_gripper_action = ArticulationAction(np.array([0.04, 0.04]), joint_indices=np.array([7, 8]))
    articulation.apply_action(open_gripper_action)

    # Check in once a frame until the gripper has been successfully opened.
    while not np.allclose(articulation.get_joint_positions()[7:], np.array([0.04, 0.04]), atol=0.001):
        yield ()

    return True
```

`my_script()` calls `yield from open_gripper_franka()`. The function `open_gripper_franka()` sends
a single command to the Franka `Articulation` that the grippers should open, and then on every subsequent
physics step, it checks if the gripper has made it to the target position. Once the gripper has reached
the target position, the function stops calling `yield` and instead calls `return True` to signal a success.
The control flow goes back to `my_script()` and the next function in the sequence gets called.

To try it, open the Template Generator (*Utilities > Generate Extension Templates* menu) and create a new extension under the *Scripting Template* section.
Then, enable the extension (*Window > Extensions* menu, search for the given extension name) and click on the toolbar entry with the same name.

## Configuration Tooling Template

The *Configuration Tooling Template* provides a simple template that serves as a solid foundation for building tools for asset configuration.
The provided implementation creates a drop-down menu that finds any `Articulation` on the stage and dynamically creates a UI frame through
which the user may control each joint in the selected `Articulation`.

Unlike the *Loaded Scenario Template* this extension assumes no control over the timeline or the stage. Instead, it allows the user to select
whatever is there and start reading and writing its state. Building asset configuration tools is a more advanced use-case, and as such,
it requires a better internal model of the Simulation timeline. For example, because an `Articulation` is only accessible while the timeline
is playing, the provided template only allows the user to attempt to modify their selected `Articulation` while the timeline is playing.

### Implementation Details

The `DropDown` is populated by a function that searches the USD stage for all objects of the specified type. This is provided as a convenience function
directly in the `DropDown` UI wrapper, but a version of the function it is using is left at the bottom of the template to allow the user further
customization.

Whenever a new item is selected from the `DropDown`, the *Robot Control Frame* is rebuilt using a builder function. This is a powerful paradigm for creating robust dynamic UI tools.
In this template, the frame can either report to the user that no robot could be selected, or it can list every joint in the selected robot if everything went well.

To try it, open the Template Generator (*Utilities > Generate Extension Templates* menu) and create a new extension under the *Configuration Tooling Template* section.
Then, enable the extension (*Window > Extensions* menu, search for the given extension name) and click on the toolbar entry with the same name.
Finally, in a new stage (*File > New* menu), add the Franka robot (*Create > Robots > Franka Emika Panda Arm* menu) and play with it.

## UI Component Library

The *UI Component Library* template demonstrates the usage of each `UIElementWrapper` that has been created. This should be used as a reference when
setting up a custom UI tool. Most importantly, this template shows the specific type of arguments and return values required for each callback function that can be
attached to each `UIElementWrapper`. This template omits the *Load* and *Reset* buttons, as these are special case buttons that are demonstrated in
the *Loaded Scenario Template*. None of the UI components shown in this template directly impact the simulation; they only call user callback functions.

The components in the *UI Component Library* template wrap a subset of the elements in `omni.ui`, and each wrapper is opinionated about how the UI component should be placed and labeled so that
it will look good next to other wrapped components. An advanced user may start adding `omni.ui` components next to wrapped components without issue.

To see the UI elements demonstrated by the template, open the Template Generator (*Utilities > Generate Extension Templates* menu) and create a new extension under the *UI Component Library* section.
Then, enable the extension (*Window > Extensions* menu, search for the given extension name) and click on the toolbar entry with the same name. The full set of UI elements is demonstrated in the newly opened window.

## Summary

This tutorial covered the templates provided in the NVIDIA Isaac Sim *Extension Template Generator*. Each template has a common underlying structure with a thin layer of implementation to show a different
use-case. The user will be able to reference one or more of these templates to get started building a highly customized UI-based extension in NVIDIA Isaac Sim without having to build a detailed knowledge
of the internal simulator mechanics.

### Further Learning

In conjunction with these templates, the user will want to reference the [API documentation](../py/source/extensions/isaacsim.gui.components/docs/index.html#ui-element-wrappers) for the `UIElementWrapper` objects.

On this page

* [General Concepts](#general-concepts)
* [Loaded Scenario Template](#loaded-scenario-template)
  + [Important Concepts](#important-concepts)
  + [Implementation Details](#implementation-details)
* [Scripting Template](#scripting-template)
  + [Implementation Details](#id1)
* [Configuration Tooling Template](#configuration-tooling-template)
  + [Implementation Details](#id2)
* [UI Component Library](#ui-component-library)
* [Summary](#summary)
  + [Further Learning](#further-learning)

---

### CLI Extension Templates

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/utilities/cli_extension_templates.html

* [Templates](templates_index.html)
* CLI extension templates

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# CLI extension templates

The command-line interface (CLI) extension templates allow you to scaffold new Isaac Sim extensions from the terminal using `./repo.sh template new`. Four templates cover the most common extension patterns:

* **Python extension** — Minimal Python-only extension with `extension.py`, docs, and test scaffolding.
* **UI extension** — Python extension with **Examples Browser** integration, **Load World**/**Reset** controls, physics callbacks, and custom UI using the experimental `BaseSample` and `BaseSampleUITemplate` classes.
* **C++ extension** — Extension with a Carbonite C++ plugin, pybind11 Python bindings, and a Python wrapper.
* **OmniGraph extension** — Extension with C++ and Python OmniGraph Node (OGN) definitions, a Carbonite plugin, pybind11 bindings, and OGN build integration.

The generator places all extensions in `source/extensions/`, and the build system discovers them automatically — no manual registration required.

## Prerequisites

The template generator runs from the Isaac Sim source tree. If you have not already cloned the
open-source repository, do so first:

```python
git clone -b main https://github.com/isaac-sim/IsaacSim.git isaacsim
cd isaacsim
```

All commands shown in this guide are run from the repository root (the directory that contains
`repo.sh`, `build.sh`, and `templates/`). On Windows, substitute `./repo.sh` with `.\repo.bat`
and `./build.sh` with `.\build.bat`.

The first invocation of `./build.sh` prompts you to accept the **NVIDIA Software License Agreement**.
After acceptance, a marker file `.eula_accepted` is written to the repository root and the prompt does
not appear again. Similarly, `./repo.sh template new` has its own EULA prompt that writes
`.omniverse_eula_accepted.txt`. Both files must exist for a fully non-interactive workflow.
See [Non-interactive usage (CI)](#cli-ext-templates-ci) below for how to pre-accept the EULA in non-interactive
(CI) environments.

For the full list of platform requirements (OS, GPU, driver, build tools), see the project
[README](https://github.com/isaac-sim/IsaacSim#prerequisites-and-environment-setup).

## Getting started

To create a new extension:

```python
./repo.sh template new
```

Follow the interactive prompts to select a template and configure your extension name, title, and other variables.

## Available templates

### Python extension

A minimal Python-only extension. Use this when you need a lightweight extension without UI, scene management, or C++ code.

Generated structure:

```python
source/extensions/isaacsim.my.extension/
├── config/extension.toml
├── data/icon.png, preview.png
├── docs/Overview.md, CHANGELOG.md
├── isaacsim/my/extension/
│   ├── __init__.py
│   ├── extension.py
│   └── tests/__init__.py, test_extension.py
└── premake5.lua
```

**Key files to modify:**

* `extension.py` — Add your startup/shutdown logic in `on_startup()` and `on_shutdown()`.

### UI extension

A Python extension with full UI and scene management. This template provides:

* **Examples Browser integration** — Your extension appears under your chosen category in **Window > Examples Browser**.
* **Load/Reset world controls** — Pre-built **Load World** and **Reset** buttons that manage the simulation lifecycle.
* **Physics callbacks** — A `scenario.py` with `on_physics_step()` called every simulation step via `SimulationManager`.
* **Custom UI** — A `ui.py` with an **Actions** frame where you add your own buttons and controls using `btn_builder` and other `UIElementWrapper` utilities.

The template uses the experimental APIs:

* `isaacsim.examples.base.base_sample_experimental.BaseSample` for scene lifecycle
* `isaacsim.examples.base.base_sample_extension_experimental.BaseSampleUITemplate` for UI
* `isaacsim.core.simulation_manager.SimulationManager` for physics callbacks
* `isaacsim.core.experimental.utils` for stage and app utilities

Generated structure:

```python
source/extensions/isaacsim.my.example/
├── config/extension.toml
├── data/icon.png, preview.png
├── docs/Overview.md, CHANGELOG.md
├── isaacsim/my/example/
│   ├── __init__.py
│   ├── extension.py   ← Examples Browser registration
│   ├── scenario.py    ← BaseSample with physics callbacks
│   ├── ui.py          ← BaseSampleUITemplate with custom controls
│   └── tests/__init__.py, test_extension.py
└── premake5.lua
```

**Key files to modify:**

* `scenario.py` — Add your simulation assets in `setup_scene()` and logic in `on_physics_step()`.
* `ui.py` — Add custom buttons and controls in `build_extra_frames()`.

### C++ extension

An extension with a Carbonite C++ plugin and pybind11 Python bindings. The plugin implements a Carbonite interface
(`IExample`) and the bindings expose `acquire_example_interface()` / `release_example_interface()` to Python.
The Python `extension.py` acquires the interface on startup, which triggers the Carbonite plugin to load.

Generated structure:

```python
source/extensions/isaacsim.my.extension/
├── config/extension.toml
├── data/icon.png, preview.png
├── docs/api.rst, Overview.md, CHANGELOG.md
├── include/isaacsim/my/extension/IExample.h       ← Carbonite interface
├── plugins/isaacsim.my.extension/ExamplePlugin.cpp ← Plugin implementation
├── bindings/isaacsim.my.extension/Bindings.cpp     ← pybind11 bindings
├── python/
│   ├── __init__.py
│   ├── impl/__init__.py, extension.py
│   └── tests/__init__.py, test_extension.py
└── premake5.lua
```

The `binding_module` variable controls the pybind11 module name (e.g., `my_extension` produces `_my_extension.so`).

**Key files to modify:**

* `IExample.h` — Define your Carbonite interface methods.
* `ExamplePlugin.cpp` — Implement the interface.
* `Bindings.cpp` — Expose additional methods to Python via pybind11.
* `extension.py` — The interface is already acquired on startup; add your Python-side logic.

### OmniGraph extension

An extension with both C++ and Python OmniGraph node definitions, a Carbonite plugin for C++ node registration,
pybind11 bindings, and full OGN build integration.

The C++ nodes are defined by `.ogn` + `.cpp` pairs in `nodes/`. The Python nodes are defined by `.ogn` + `.py`
pairs in `python/nodes/`. The OGN build system auto-generates database classes and test scaffolding for both.

The Carbonite plugin implements `INITIALIZE_OGN_NODES()` / `RELEASE_OGN_NODES()` in `carbOnPluginStartup()` /
`carbOnPluginShutdown()`. The pybind11 bindings expose `acquire_example_nodes_interface()` which `extension.py`
calls on startup — this triggers the plugin to load and register the C++ OGN nodes.

Generated structure:

```python
source/extensions/isaacsim.my.nodes/
├── config/extension.toml
├── data/icon.png, preview.png
├── docs/api.rst, Overview.md, CHANGELOG.md
├── include/isaacsim/my/nodes/IExampleNodes.h          ← Carbonite interface
├── nodes/
│   ├── OgnExampleCpp.ogn, OgnExampleCpp.cpp           ← C++ OGN node
│   ├── config/CategoryDefinition.json
│   └── icons/isaac-sim.svg
├── plugins/isaacsim.my.nodes/PluginInterface.cpp       ← Plugin with OGN macros
├── bindings/isaacsim.my.nodes/Bindings.cpp             ← pybind11 bindings
├── python/
│   ├── __init__.py
│   ├── impl/__init__.py, extension.py
│   ├── nodes/
│   │   ├── OgnExamplePython.ogn, OgnExamplePython.py   ← Python OGN node
│   │   ├── config/CategoryDefinition.json
│   │   └── icons/isaac-sim.svg
│   └── tests/__init__.py, test_extension.py
└── premake5.lua
```

Unlike the C++ template, the OGN template does not use a separate `binding_module` variable. The OGN build system
automatically derives the bindings module name from the extension name (e.g., `isaacsim.my.nodes` →
`_isaacsim_my_nodes`).

**Key files to modify:**

* `.ogn` files — Define node inputs, outputs, and metadata (JSON format).
* `OgnExampleCpp.cpp` — Implement the `compute()` method for the C++ node.
* `OgnExamplePython.py` — Implement the `compute()` method for the Python node.
* To add more nodes, create new `.ogn` + `.cpp`/`.py` pairs in the appropriate `nodes/` directory.

## Tutorial: Creating and testing an extension

This tutorial walks through creating a Python extension, building it, and verifying it works.

### Step 1: Generate the extension

Run the template generator:

```python
./repo.sh template new
```

Select the **Python extension** template and enter values when prompted:

* Extension name: `isaacsim.my.hello`
* Title: `Hello World`
* Version: `0.1.0`
* Description: `A hello world extension.`
* Category: `Examples`

You should see:

```python
Extension 'isaacsim.my.hello' created successfully in
source/extensions/isaacsim.my.hello
```

### Step 2: Build

Rebuild the project so the new extension is included:

```python
./build.sh
```

The build system discovers the extension automatically — no manual registration required.
A successful build ends with a summary similar to:

```python
BUILD (release) SUCCEEDED (Took NN.NN seconds)
```

After the build, the extension is staged at:

```python
_build/linux-x86_64/release/exts/isaacsim.my.hello/
```

If the build fails, re-run with `./build.sh -v` for verbose output and inspect the first error
message — subsequent errors are usually cascading consequences of the first.

### Step 3: Run the startup test

Every generated extension includes a startup test. Run it from the build directory:

```python
cd _build/linux-x86_64/release
./tests/tests-isaacsim.my.hello.sh
```

This runs two test suites:

* A **startup test** that loads Kit with the extension enabled and verifies it starts and shuts down cleanly.
* The **unit tests** in `isaacsim/my/hello/tests/test_extension.py`.

A successful run ends with the standard `unittest` summary lines:

```python
Ran N tests in N.NNs

OK
```

If a test fails, the failing test name and traceback are printed above the summary. Kit log files
written during the run can be found under `~/.nvidia-omniverse/logs/` for deeper inspection.

### Step 4: Verify in Isaac Sim

Launch Isaac Sim with your extension enabled:

```python
./_build/linux-x86_64/release/isaac-sim.sh --enable isaacsim.my.hello
```

**Extension Manager check**

Open the **Extensions Manager** (**Window > Extensions**) and search for `isaacsim.my.hello`.
The extension should appear in the list with its status toggle set to **enabled** (green) and the
title and description from your `extension.toml`.

**Script Editor check**

From **Window > Script Editor**, run:

```python
import omni.kit.app
ext_mgr = omni.kit.app.get_app().get_extension_manager()
print(ext_mgr.is_extension_enabled("isaacsim.my.hello"))
# Expected: True
```

### Step 5: Customize

Open `source/extensions/isaacsim.my.hello/isaacsim/my/hello/extension.py` and modify the
`on_startup` and `on_shutdown` methods to add your custom logic. Rebuild and re-test.

### Verifying UI, C++, and OmniGraph extensions

The verification flow is the same for every template (build → run startup test → launch and check
in the **Extensions Manager**); the additional checks below confirm the template-specific surfaces.

**UI extension**

After enabling the extension, open **Window > Examples Browser**. Your extension should appear under
the category you selected at generation time (e.g., `Examples`). Selecting it opens a panel with
**Load World** and **Reset** buttons:

* Click **Load World** — the simulation should load the default scene defined in
  `scenario.py::setup_scene()` (a grid ground plane referenced from
  `Isaac/Environments/Grid/default_environment.usd`) and physics callbacks become active.
* Click **Reset** — the world should return to its initial state and physics callbacks stop.

Replace the body of `setup_scene()` and `on_physics_step()` to drive your own simulation.

**C++ extension**

Verify the bindings work after building:

```python
cd _build/linux-x86_64/release
./tests/tests-isaacsim.my.extension.sh
```

The unit tests import the bindings module and call the `greet()` method on the Carbonite interface.
You can repeat the check interactively from the **Script Editor** (substituting your own
`extension_name` and `binding_module`):

```python
from isaacsim.my.extension.bindings._my_extension import acquire_example_interface
iface = acquire_example_interface()
print(iface.greet())
# Expected: a non-empty greeting string
```

**OmniGraph extension**

Verify both C++ and Python nodes are registered:

```python
cd _build/linux-x86_64/release
./tests/tests-isaacsim.my.nodes.sh
```

The unit tests check that both node types appear in `og.get_registered_nodes()` and that their
`compute()` methods produce correct results.

You can also verify OGN nodes interactively via the **Script Editor**:

```python
import omni.graph.core as og
nodes = og.get_registered_nodes()
print([n for n in nodes if "my.nodes" in n])
# Expected: ['isaacsim.my.nodes.ExampleCpp', 'isaacsim.my.nodes.ExamplePython']
```

To exercise the nodes graphically, open **Window > Graph Editors > Action Graph**, create a new
graph, and search the node palette for `ExampleCpp` / `ExamplePython`. Both should appear under
the category named after the first segment of your extension name (e.g., `isaacsim`), as defined
in the generated `CategoryDefinition.json` files.

## Non-interactive usage (CI)

For Continuous Integration (CI) automation, the full pipeline is:

1. **Pre-accept the EULA.** Both `./build.sh` and `./repo.sh template` prompt on first use;
   in a non-interactive job the prompt blocks execution. Create **both** marker files in your CI
   setup step:

   ```python
   touch .eula_accepted
   touch .omniverse_eula_accepted.txt
   ```

   * `.eula_accepted` is checked by `tools/eula_check.sh` (used by `./build.sh`).
   * `.omniverse_eula_accepted.txt` is checked by the template generator (used by
     `./repo.sh template new` and `./repo.sh template replay`).

   Both are empty files that persist across builds, so creating them once at the start of the job
   is sufficient.

   Note

   If only `.eula_accepted` is present, `./build.sh` will work but
   `./repo.sh template replay` will fail with an unhandled exception in the EULA prompt
   because the playback frontend cannot answer interactive prompts.
2. **Generate a playback file once, interactively.** This step records the template selection and
   variable values into a TOML file:

   ```python
   ./repo.sh template new --generate-playback my_extension.toml
   ```
3. **Replay non-interactively in CI.** The replay command consumes the playback file and produces the
   extension without prompting:

   ```python
   ./repo.sh template replay my_extension.toml
   ```
4. **Build and run the startup tests** as in the tutorial above:

   ```python
   ./build.sh
   cd _build/linux-x86_64/release
   ./tests/tests-<extension_name>.sh
   ```

Playback files use TOML (Tom’s Obvious, Minimal Language) format to specify the template and variable
values. The section header names the template (one of `isaacsim-python-extension`,
`isaacsim-ui-extension`, `isaacsim-cpp-extension`, `isaacsim-omnigraph-extension`):

```python
[isaacsim-python-extension]
extension_name = "isaacsim.sensors.lidar"
title = "Lidar Sensor"
version = "0.1.0"
description = "Provides lidar sensor simulation."
category = "Sensors"
```

The `templates/tests/` directory contains pre-defined playback files
(`test_python_extension.toml`, `test_ui_extension.toml`, `test_cpp_extension.toml`,
`test_omnigraph_extension.toml`) used for CI build verification — copy one as a starting point
when wiring up your own pipeline.

## Template variables

All templates share a common set of variables:

| Variable | Source | Description |
| --- | --- | --- |
| `extension_name` | User input | Dotted extension name (e.g., `isaacsim.sensors.lidar`) |
| `title` | User input | Human-readable title |
| `version` | User input | Semantic version (e.g., `0.1.0`) |
| `description` | User input | Short description of the extension |
| `category` | User input | Extension category (e.g., `Simulation`, `Sensors`) |
| `binding_module` | User input (C++ only) | pybind11 module name (e.g., `my_extension` → `_my_extension.so`) |
| `python_module` | Auto-derived | Same as `extension_name` |
| `python_module_path` | Auto-derived | Dots replaced with slashes (e.g., `isaacsim/sensors/lidar`) |
| `python_module_toplevel` | Auto-derived | First segment of `extension_name` (e.g., `isaacsim`) |
| `current_date` | Auto-generated | Today’s date |

Note

The OmniGraph template does not use `binding_module`. The OGN build system automatically
derives the pybind11 module name from `extension_name`.

## Build and verification checklist

After generating an extension, always:

1. **Build** — `./build.sh`
2. **Test** — `cd _build/linux-x86_64/release && ./tests/tests-<extension_name>.sh`

For C++ and OmniGraph templates, the build compiles the Carbonite plugin and pybind11 bindings.
If the build fails, check that the `premake5.lua` include paths match your extension’s directory layout.

## Troubleshooting

**Extension not loading at runtime**
:   Check that the extension name in `config/extension.toml` matches the directory name under `source/extensions/`.
    Verify the extension is enabled with `--enable <extension_name>` on the command line or through the **Extensions Manager**.

**C++ plugin not loading**
:   Ensure the `[[native.plugin]]` section in `extension.toml` includes `path = "bin/*.plugin"`.
    Without this, Kit cannot find the `.so` plugin file in the extension’s `bin/` directory.

**C++ OGN nodes not registering**
:   The Carbonite plugin must be started for `INITIALIZE_OGN_NODES()` to run. This happens when
    `acquire_example_nodes_interface()` is called from the pybind11 bindings in `extension.py`.
    If the C++ nodes don’t appear in `og.get_registered_nodes()`, verify that:

    * `Bindings.cpp` has a `defineInterfaceClass<IExampleNodes>` call
    * `extension.py` imports and calls `acquire_example_nodes_interface()` in `on_startup()`
    * `PluginInterface.cpp` does **not** have `CARB_PLUGIN_IMPL_DEPS` (this can prevent the plugin from loading)

**Build errors with OmniGraph nodes**
:   Verify that `.ogn` files are valid JSON and that each C++ `.ogn` has a matching `.cpp` file
    with the `REGISTER_OGN_NODE()` macro. Python `.ogn` files need `"language": "Python"` and a
    matching `.py` file with a `compute()` method.

**Stubgen failure during build**
:   The stubgen step may fail with `generic_type: type "X" is already registered` errors.
    This is a known issue with the pybind11 stub generator when multiple extensions share type names.
    The build itself succeeds — only the `.pyi` stub generation fails, which does not affect runtime.

**Template replay fails with “This should not be encountered”**
:   This means `.omniverse_eula_accepted.txt` is missing from the repository root. The template
    generator’s playback frontend cannot answer the EULA prompt interactively, so it raises an
    exception in its `select()` method. Fix by creating the file:

    ```python
    touch .omniverse_eula_accepted.txt
    ```

    This is a separate file from `.eula_accepted` (which is used by `./build.sh`). Both must
    exist for fully non-interactive CI pipelines.

On this page

* [Prerequisites](#prerequisites)
* [Getting started](#getting-started)
* [Available templates](#available-templates)
  + [Python extension](#python-extension)
  + [UI extension](#ui-extension)
  + [C++ extension](#c-extension)
  + [OmniGraph extension](#omnigraph-extension)
* [Tutorial: Creating and testing an extension](#tutorial-creating-and-testing-an-extension)
  + [Step 1: Generate the extension](#step-1-generate-the-extension)
  + [Step 2: Build](#step-2-build)
  + [Step 3: Run the startup test](#step-3-run-the-startup-test)
  + [Step 4: Verify in Isaac Sim](#step-4-verify-in-isaac-sim)
  + [Step 5: Customize](#step-5-customize)
  + [Verifying UI, C++, and OmniGraph extensions](#verifying-ui-c-and-omnigraph-extensions)
* [Non-interactive usage (CI)](#non-interactive-usage-ci)
* [Template variables](#template-variables)
* [Build and verification checklist](#build-and-verification-checklist)
* [Troubleshooting](#troubleshooting)

---

### VSCode Extension Template Generator

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/utilities/vscode_extension_template_generator.html

* [Templates](templates_index.html)
* Advanced Extension Template Generator from VS Code

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Advanced Extension Template Generator from VS Code

The [Isaac Sim VS Code Edition](https://marketplace.visualstudio.com/items?itemName=NVIDIA.isaacsim-vscode-edition) is a Visual Studio Code extension that provides development support for NVIDIA Omniverse in general and Isaac Sim in particular.
One of its features is the generation of advanced extension templates.

Isaac Sim VS Code Edition’s Extension template generator wizard

Extension templates can be generated in the following forms:

* Ready-to-use extensions (**Python**)
* Extensions requiring a Kit-based build system (**C++** and/or **Python**)

The following table list the extension components that can be generated by the template as well as their availability according to the programming language to be used.

Extension components that can be generated by the template

| Component | Python | C++ | Description |
| --- | --- | --- | --- |
| Extension | yes | yes | Define an extension class that derives from `omni.ext.IExt` |
| API | yes | yes | Define/expose codebase Application Programming Interface (API) |
| OmniGraph | yes | yes | Create nodes using the OmniGraph framework for visual scripting |
| Pybind | no | yes | Reflect C++ code using `pybind11` so that it can be called from Python |
| UI | yes | no | Create Graphical User Interfaces (GUI) using Omniverse UI framework |
| Tests | yes | yes | Create test cases for the extension |

---

## Ready-To-Use Extensions

A ready-to-use extension (**Python**), as the name suggests, is an extension that can be used as-is once created without the need for any extra configuration or build system.

The subsequent subsections describe how to generate and run this type of extensions.

### Creating the Extension

Note

The folder containing the extension to be created had to be listed in the Isaac Sim extension search path in order to be discoverable.

If this is not the case, you can use the Isaac Sim’s Extensions Manager (*Window > Extensions* menu) to add it.
Click on the hamburger icon in the Extensions Manager, and then *Settings* in the sub-menu, to add the path to the folder containing your extensions.

Hint

For convenience, the `extsUser` folder at the root of the Isaac Sim installation is listed in the extension search path, so it is recommended to create the extension in that folder.

Open, in the VS Code Editor, the *Isaac Sim VS Code Edition*’s extension template generator wizard (*Templates > Extension*) and fill/check, at least, the following fields:

* **Ext. name**: Given extension name. E.g. `my.custom.extension`.
* **Ext. path**: Folder path that will contain the extension. E.g.: `PATH_TO_ISAAC_SIM/extsUser`.
* Enable the **Ready-to-use extension** checkbox.
* Enable the specific component(s) to generate.

Then, press *Create* to generate the extension. Check that the generated extension exists in the specified path. At this point, the extension is ready to be modified with your own code.

### Running the Extension

Launch Isaac Sim, then search and enable the created extension in the Extension Manager (using the given extension name).
Depending on the component(s) created, the following can be expected (without additional modification):

* Extension/API: Simply, the extension is enabled.
* OmniGraph: The node `OgnMyCustomExtensionPy` can be instantiated in an Action Graph (e.g.: through *Create > Visual Scripting > Action Graph*).
* UI: A sample window can be opened when clicking on the *Window > My Custom Extension* menu.
* Tests: The tests can be run from an opened terminal in the root directory of Isaac Sim as follows:

  > Linux
  >
  > ```python
  > ./kit/kit --empty --enable omni.kit.test --/exts/omni.kit.test/runTestsAndQuit=true --/exts/omni.kit.test/testExts/0='my.custom.extension' --ext-folder "extsUser" --no-window --allow-root
  > ```
  >
  >
  > Windows
  >
  > ```python
  > .\kit\kit --empty --enable omni.kit.test --/exts/omni.kit.test/runTestsAndQuit=true --/exts/omni.kit.test/testExts/0='my.custom.extension' --ext-folder "extsUser" --no-window --allow-root
  > ```

---

## Extensions Requiring a Kit-based Build System

Extensions (**C++** and/or **Python**) requiring Kit-based build system, as the name suggests, need to be configured as part of a Kit SDK-based application (such as the [Isaac Sim Open-Source Application](https://github.com/isaac-sim/IsaacSim) or the [Omniverse Kit App Template](https://github.com/NVIDIA-Omniverse/kit-app-template)) in order to be compiled.

The subsequent subsections describe how to generate and run this type of extensions.

### Building the Open-Source Application

Get the [Isaac Sim Open-Source Application](https://github.com/isaac-sim/IsaacSim), and setup and build it according to its documentation.

### Creating the Extension

Hint

For convenience, the `source/extensions` folder at the root of the Isaac Sim Open-Source Application is configured, in the build system, as a place to search for the extensions’ source code.
Therefore, it is recommended to create the extension there. **Create it if the folder doesn’t exist**.

Open, in the VS Code Editor, the *Isaac Sim VS Code Edition*’s extension template generator wizard (*Templates > Extension*) and fill/check, at least, the following fields:

* **Ext. name**: Given extension name. E.g. `my.custom.extension`.
* **Ext. path**: Folder path that will contain the extension source code. E.g.: `PATH_TO_ISAAC_SIM_APPLICATION/source/extensions`.
* Disable the *Ready-to-use extension* checkbox (if it is already enabled).
* Enable the specific component(s) to generate.

Then, press *Create* to generate the extension. Check that the generated extension exists in the specified path.

### Configuring the Build System

Depending on the component(s) created, the following configuration is necessary:

* OmniGraph: Edit the `kit-sdk-deps.packman.xml` file (in the `deps/` or `tools/deps/` folder, according to the application) to include the USD dependency, if it is not already present:

  > ```python
  > <import path="...all-deps.packman.xml">
  >     <!-- JUST ADD THE NEXT LINE -->
  >     <filter include="usd-${config}"/>
  > </import>
  >
  > <!-- JUST ADD THE NEXT LINE -->
  > <!-- use ../ for deps/ folder, or ../../ for tools/deps/ folder -->
  > <dependency name="usd-${config}" linkPath="../_build/target-deps/usd/${config}"/>
  > ```
* Tests: Edit the `kit-sdk-deps.packman.xml` file (in the `deps/` or `tools/deps/` folder, according to the application) to include the `doctest` dependency, if it is not already present:

  > ```python
  > <import path="...all-deps.packman.xml">
  >     <!-- JUST ADD THE NEXT LINE -->
  >     <filter include="doctest"/>
  > </import>
  >
  > <!-- JUST ADD THE NEXT LINE -->
  > <!-- use ../ for deps/ folder, or ../../ for tools/deps/ folder -->
  > <dependency name="doctest" linkPath="../_build/target-deps/doctest">
  >     <package name="doctest" version="2.4.5+nv1-3" />
  > </dependency>
  > ```

### Building the Extension

To build the extension, simply run the following command from an opened terminal in the root directory of the Isaac Sim Open-Source Application:

Linux

```python
./build.sh  # or ./repo.sh build
```

Windows

```python
build.bat  :: or .\repo.bat build
```

### Running the Extension

Launch Isaac Sim, then search and enable the created extension in the Extension Manager (using the given extension name).
Depending on the component(s) created, the following can be expected (without additional modification):

* Extension/API: Simply, the extension is enabled.
* OmniGraph: The node `OgnMyCustomExtensionPy` (Python) and/or `OgnMyCustomExtensionCpp` (C++) can be instantiated in an Action Graph (e.g.: through *Create > Visual Scripting > Action Graph*).
* Pybind (C++ only): The exposed C++ API via `pybind11` can be called from Python.

  > For example, execute the following code in the *Script Editor* (*Window > Script Editor* menu):
  >
  > ```python
  > import my.custom.extension
  >
  > interface = my.custom.extension.acquire_extension_interface()
  > my.custom.extension.set_default_status("custom status")
  > interface.register_object(10)
  > my.custom.extension.release_extension_interface()
  > ```
* UI (Python only): A sample window can be opened when clicking on the *Window > My Custom Extension* menu.
* Tests: The tests can be run from an opened terminal in the root directory of the Isaac Sim Open-Source Application as follows:

  > Linux
  >
  > ```python
  > ./_build/linux-x86_64/release/tests-my.custom.extension.sh
  > ```
  >
  >
  > Windows
  >
  > ```python
  > .\_build\windows-x86_64\release\tests-my.custom.extension.bat
  > ```

On this page

* [Ready-To-Use Extensions](#ready-to-use-extensions)
  + [Creating the Extension](#creating-the-extension)
  + [Running the Extension](#running-the-extension)
* [Extensions Requiring a Kit-based Build System](#extensions-requiring-a-kit-based-build-system)
  + [Building the Open-Source Application](#building-the-open-source-application)
  + [Creating the Extension](#id2)
  + [Configuring the Build System](#configuring-the-build-system)
  + [Building the Extension](#building-the-extension)
  + [Running the Extension](#id3)

---


## Extension 管理

### Search Extension Tutorial

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/utilities/tutorial_search_extension.html

* SimReady Content Browser Search Extension Tutorial

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# SimReady Content Browser Search Extension Tutorial

The **SimReady Asset Search** feature helps you find digital assets that match your criteria by combining a directory tree with an AI-assisted search control panel. This tutorial explains how to use these features to search your local file system and AWS S3 buckets for assets.

This tutorial assumes you are familiar with [SimReady concepts](https://github.com/NVIDIA/simready-foundation) and the [Content Browser](content_browser.html#isaac-sim-app-gui-content-browser) and workflow. It addresses the following topics:

* [Prerequisites](#prerequisites)
* [Overview](#overview)
* [How to Open and Use the SimReady Asset Search Control Panel](#how-to-open-and-use-the-simready-asset-search-control-panel)
* [How to Limit the Scope of Your Searches](#how-to-limit-the-scope-of-your-searches)
* [How to Display and Filter on Relevance Scores](#how-to-display-and-filter-on-relevance-scores)

## [Prerequisites](#id2)

* You have installed the latest versions of the Omniverse Kit and the `omni.simready.content.browser` UI extension.
* You have access to assets in local folders and AWS S3 buckets.

## [Overview](#id3)

To find assets, optionally select a folder in the directory tree to scope your search, then select a search mode and enter filters in the **SimReady Asset Search** control panel. The control panel initiates the search and displays results in the SimReady Content Browser, where you can view asset data, filter the results, and open assets.

The following sections explain how to use these features.

## [How to Open and Use the SimReady Asset Search Control Panel](#id4)

There are two ways to open the **SimReady Asset Search** control panel:

1. Click the Search icon in the SimReady Content Browser and select **Assets Search** in the context menu.
2. Right-click a folder in the directory tree, and select **AssetSearch here** in the context menu.

Both ways open the **SimReady Asset Search** control panel.

## [How to Limit the Scope of Your Searches](#id5)

Use the directory tree to limit the scope of your searches. The directory tree contains all folders that can contain assets. Selecting a folder limits your searches to the contents of that folder and its subfolders. Selecting a folder in the tree is optional; if you do not select one, **SimReady Asset Search** searches the entire directory tree by default.

The directory tree spans both your local file system and AWS S3 buckets, which gives you flexibility in how broadly or narrowly you scope your searches. You can, for example, search across all registered AWS S3 buckets or limit a search to a specific folder in your local file system. When you select a folder, it becomes the *anchor path* that the search API bases its search on. Until you change it, all searches are scoped to the contents of the selected folder and its subfolders.

As noted in the previous section, the contents of the **SimReady Asset Search** control panel are sensitive to your directory tree selection. Changing your selection initializes the control panel for a new search. (You do not need to close and reopen the control panel to initiate a new search.)

When you select a folder, the SimReady Content Browser displays its contents in a panel to the right of the directory tree. If you select a folder in that panel, the effect is the same as selecting the same folder in the directory tree.

### How to Enter Search Parameters

The **SimReady Asset Search** control panel displays the *anchor path*, **Search Mode** options, and context-sensitive filters.

* The *anchor path* reflects which folder you select in the directory tree. This is the base path for searches; all searches are restricted to the contents of this folder and its subfolders. Select a different folder in the tree to change it. For example, selecting the `Assets/Isaac/SimReady` folder changes the *anchor path* to `Assets/Isaac/SimReady`.
* The *anchor path* determines which **Search Mode** options are available. For example, if the *anchor path* is a folder in your local file system, only the **File Index** search mode is available.
* The **Search Mode** determines which filters are available. For example, if **Search Mode** is **File Index**, only the **Name** filter is available.
* The filters specify which assets the search API returns. If you do not select any filters, the search API returns all assets it finds. If you select one or more filters, the search API returns only assets that pass those filters.

There are three **Search Mode** options: **File Index**, **AI**, and **WSCache**.

* **File Index** is only available if the *anchor path* is a folder in your local file system or an `Assets/Isaac/*` S3 folder. This option enables the following filter:

  + **Name** filter - Enter text in the **Name** field to return only assets whose pathnames match the text. For example, enter “robot” to have the search API return all assets whose pathname contains “robot”.
  + **Index Files** button - Click this to index files in the selected folder. This is needed if there are files in a local folder that have been added since the last index, or if you exited and restarted Isaac Sim since the last index. (You do not need to click this button if you select an `Assets/Isaac/*` S3 folder.)
* **AI** is only available for folders in AWS S3 buckets. This option enables the following filters:

  + **Relevance cutoff** filter - Enter a value between 0 and 1 to set the minimum relevance score for assets to be returned. Assets with a relevance score lower than the specified cutoff are not returned. (*Relevance* is a measure of how well the asset matches the search query. A value of 1.0 is the highest confidence match possible, a value of 0.0 is no match, and values in between are partial matches. *Relevance* is discussed in more detail in [How to Display and Filter on Relevance Scores](#how-to-display-and-filter-on-relevance-scores).)
  + **Phrase** filter - Enter a natural language phrase to search for assets that match the phrase. For example, enter “a robot with a camera” to have the search API return only assets whose properties match that description.
  + These filters are cumulative. The search API returns all assets that match ALL of the filters you specify, and excludes all others.
* **WSCache** (SimReady Workspace Cache) is only available for folders in the `/SimReady` S3 bucket. This option enables the following filters:

  + **Name** filter - Enter text for **Name** to return assets whose pathnames match the text. For example, enter “robot” to have the search API return assets whose pathnames match “robot”.
  + **Profile** filter - Click the entry field and select a SimReady profile from the dropdown menu to return assets that match the selected profile.
  + **Feature** filter - Click the entry field and select a SimReady feature from the dropdown menu to return assets that match the selected feature.
  + **Tag** filter - Click the entry field and select a SimReady tag from the dropdown menu to return assets with the associated tag.
  + These filters are cumulative. Select the **Match Any** checkbox to have the search API return all assets that match ANY of the filters you specify. Select the **Match All** checkbox to have the search API return only assets that match ALL of the filters you specify.

### How to Index Local Files

For the search API to find assets in a folder, its contents must be indexed. The indexes for local files are stored in memory, and are updated only when you manually index the folder. Assets added to a local folder are not automatically indexed and, if you exit from Isaac Sim and restart it, local indexes are lost. In either case, you must index the folder to make the assets searchable.

To index a local folder and its subfolders, select the folder in the directory tree and click **Index Files**. (This option is only available when **Search Mode** is **File Index**.)

### How to Initiate a Search

When you have scoped your search, selected a search mode, entered relevant search filters, and optionally indexed local files, click **Search** in the **SimReady Asset Search** control panel to initiate the search. The search API runs the search and returns matching assets in the SimReady Content Browser, where you can see asset data, filter the results, and open an asset.

### Examples

The following examples assume you have already opened the **SimReady Asset Search** control panel.

#### Search for assets in the `Assets/Isaac/Robots` folder whose pathnames contain “Fanuc”.

1. Select the `Assets/Isaac/Robots` folder in the directory tree.
2. Select **File Index** for **Search Mode**.
3. Enter *Fanuc* for **Name**.
4. Click **Search**.

Note

Unless you select a local folder, there is no need to click **Index Files**.

#### Search for assets in the `Assets/Isaac` S3 folder or its subfolders that are robots.

1. Select the `Assets/Isaac` S3 folder in the directory tree.
2. Select **AI** for **Search Mode**.
3. Enter or accept the default **Relevance cutoff** value, such as 0.5, to exclude results for which the search API has low confidence.
4. Enter *robots* for **Phrase**.
5. Click **Search**.

#### Search for assets in the `Assets/Isaac/SimReady` S3 folder whose **Profile** is “Prop-Robotics-Isaac” and **Feature** is “FET003\_BASE\_NEUTRAL”.

1. Select the `Assets/Isaac/SimReady` S3 folder in the directory tree.
2. Select **WSCache** for **Search Mode**.
3. Select “Prop-Robotics-Isaac” for **Profile**.
4. Select “FET003\_BASE\_NEUTRAL” for **Feature**.
5. Select the **Match All** checkbox.
6. Click **Search**.

In this example, the SimReady Content Browser lists only those assets that satisfy both of these conditions.

## [How to Display and Filter on Relevance Scores](#id6)

When you set **Search Mode** to **AI**, the SimReady Content Browser displays a relevance score for each asset it lists. The search API calculates this score; it is a measure of how well the asset matched the search query. A value of 1.0 is the highest confidence match possible, a value of 0.0 is no match, and values in between are partial matches. Use these scores to help you identify which assets are good matches for your search criteria.

Setting **Search Mode** to **AI** exposes a **Relevance cutoff** filter. Use this filter to limit the results to matches for which the search API has higher confidence. Enter your minimum acceptable relevance score in the control panel’s **Relevance cutoff** field. This restricts the search results to assets whose relevance scores are equal to or greater than the value you specify.

On this page

* [Prerequisites](#prerequisites)
* [Overview](#overview)
* [How to Open and Use the SimReady Asset Search Control Panel](#how-to-open-and-use-the-simready-asset-search-control-panel)
* [How to Limit the Scope of Your Searches](#how-to-limit-the-scope-of-your-searches)
  + [How to Enter Search Parameters](#how-to-enter-search-parameters)
  + [How to Index Local Files](#how-to-index-local-files)
  + [How to Initiate a Search](#how-to-initiate-a-search)
  + [Examples](#examples)
    - [Search for assets in the `Assets/Isaac/Robots` folder whose pathnames contain “Fanuc”.](#search-for-assets-in-the-assets-isaac-robots-folder-whose-pathnames-contain-fanuc)
    - [Search for assets in the `Assets/Isaac` S3 folder or its subfolders that are robots.](#search-for-assets-in-the-assets-isaac-s3-folder-or-its-subfolders-that-are-robots)
    - [Search for assets in the `Assets/Isaac/SimReady` S3 folder whose **Profile** is “Prop-Robotics-Isaac” and **Feature** is “FET003\_BASE\_NEUTRAL”.](#search-for-assets-in-the-assets-isaac-simready-s3-folder-whose-profile-is-prop-robotics-isaac-and-feature-is-fet003-base-neutral)
* [How to Display and Filter on Relevance Scores](#how-to-display-and-filter-on-relevance-scores)

---

### Updating Extensions

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/utilities/updating_extensions.html

* Adding and Updating Extensions Guide

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Adding and Updating Extensions Guide

This guide explains how to add or update an extension in Omniverse.

## Steps to Add an Extension

Follow these steps to add an extension from a local folder path or a new extension registry.

1. **Open the Extensions Menu**

   Open the menu by navigating to **Window > Extensions**:
2. **Add the Path to the Extension (optional)**

   This step is optional if you have already added the path to the extension in the settings panel. Or if the extension you want to add is already in an existing extension registry.

   Click the dropdown in the top right and select the settings option.

   * If you have the extension in a local folder, you can add the path to the extension by clicking the green **+** button in the **Extension Search Paths** section at the top and then typing the full path to the parent folder containing the extension’s folder. This path can contain multiple extensions.
   * If you want to add a new extension registry, click the green **+** button in the **Extension Registries** section at the bottom and type in the full URL of the extension registry.
3. **Search for the Extension**

   In the search bar, type the name of the desired extension. For example, type:

   ```python
   omni.kit.window.tests
   ```

   you can then select it from the results and click **INSTALL**.

   Note

   Custom or non NVIDIA extensions may show up under the **THIRD PARTY** tab

   After installing, click the toggle next to the extension name to enable the extension.

## Steps to Update an Extension

1. **Open the Extensions Menu**

   Open the menu by navigating to **Window > Extensions**:
2. **Search for the Extension**

   In the search bar, type the name of the desired extension. For example, to update the MJCF importer, type:

   ```python
   isaacsim.asset.importer.mjcf
   ```
3. **Click the Update Button**

   Once you find the extension, click the **UPDATE** button.

Note

For some extensions, it may be required to reload Isaac Sim to properly load the newest version.

On this page

* [Steps to Add an Extension](#steps-to-add-an-extension)
* [Steps to Update an Extension](#steps-to-update-an-extension)

---


## 工具

### Content Browser

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/utilities/content_browser.html

* [Browsers](browsers.html)
* Content Browser

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Content Browser

The Content Browser is the main browser for Isaac Sim content. It is accessible from the **Window > Browsers > Content** tab.

## User Interface

You can browse and load the Isaac Sim Asset Cards under the **Isaac Sim** folder in the Directory Navigator.

Refer to the [Content Browser](https://docs.omniverse.nvidia.com/extensions/latest/ext_core/ext_content-browser.html "(in Omniverse Extensions)") Omniverse documentation for more details.

On this page

* [User Interface](#user-interface)

---

### Browsers

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/utilities/browsers.html

* Browsers

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Browsers

Isaac Sim provides several browsers to help you manage your assets and scenes.
These include the [Content Browser](content_browser.html#isaac-sim-app-gui-content-browser),
the [NVIDIA Asset Browser](https://docs.omniverse.nvidia.com/extensions/latest/ext_core/ext_browser-extensions/asset-browser.html "(in Omniverse Extensions)"),
the [Material Browser](https://docs.omniverse.nvidia.com/extensions/latest/ext_core/ext_browser-extensions/material-browser.html "(in Omniverse Extensions)"),
and the [SimReady Explorer](https://docs.omniverse.nvidia.com/extensions/latest/ext_core/ext_browser-extensions/simready-explorer.html "(in Omniverse Extensions)").

* [Content Browser](content_browser.html)
* [Material Browser](https://docs.omniverse.nvidia.com/extensions/latest/ext_core/ext_browser-extensions/material-browser.html "(in Omniverse Extensions)")
* [NVIDIA Asset Browser](https://docs.omniverse.nvidia.com/extensions/latest/ext_core/ext_browser-extensions/asset-browser.html "(in Omniverse Extensions)")
* [SimReady Explorer](https://docs.omniverse.nvidia.com/extensions/latest/ext_core/ext_browser-extensions/simready-explorer.html "(in Omniverse Extensions)")

---


## 高级

### Building C++ USD Plugins

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/omniverse_usd/building_cpp_usd_plugins.html

* [Omniverse and USD](index.html)
* Building C++ USD Plugins Against the Standalone Installer

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Building C++ USD Plugins Against the Standalone Installer

The standalone Isaac Sim installer ships the USD runtime shared
libraries (under `extscache/omni.usd.libs-*/bin/`) and the matching Python
bindings, but it does not ship the C++ headers or the `pxrConfig.cmake`
package-config files needed to compile your own native USD plugins. This
page describes a supported workflow for obtaining matching headers and
linking native plugins against the USD libraries that Isaac Sim
loads at runtime.

If you are developing in-tree against a Kit C++ extension template, use the
workflow described in [CLI extension templates](../utilities/cli_extension_templates.html#isaac-sim-cli-extension-templates) instead. The
page below is specifically for building standalone native USD plugins
(those discovered and loaded via `Plug::Load()` at runtime) against an
installed Isaac Sim package.

## When You Need This

You need this workflow when you are building a C++ USD plugin that must be
loaded into a Isaac Sim process, and you are starting from the
standalone installer rather than the source repository.

USD discovers your plugin at runtime by walking `PXR_PLUGINPATH_NAME`,
parsing its `plugInfo.json`, and then calling `Plug::Load()`.
`Plug::Load()` performs a normal `dlopen()` on your shared library,
which means your plugin must be ABI-compatible with the USD runtime
libraries already loaded in the Isaac Sim process.

## Prerequisites

Inside the standalone installer, locate the bundled packman launcher and
the manifest that pins all of Isaac Sim’s external dependencies:

```python
<isaac-sim-install>/kit/dev/tools/packman/packman
<isaac-sim-install>/kit/dev/all-deps.packman.xml
```

Open `all-deps.packman.xml` and find the `usd-release` dependency
entry. It contains an inner `<package>` element whose `name` and
`version` attributes identify the exact OpenUSD build that
Isaac Sim was compiled against — for example:

```python
<dependency name="usd-release">
    <package name="usd.py312.manylinux_2_35_x86_64.stock.release"
             version="0.25.11.kit.2-gl.19811"/>
</dependency>
```

The `name` is platform- and Python-version-encoded; copy both
attributes verbatim into your own packman project file (see below).

You also need the Python development headers that ship inside the
installer:

```python
<isaac-sim-install>/kit/python/include/python3.XX/
```

The USD `Ar` and `Tf` headers transitively include Boost.Python via
`TfPyObjWrapper`, so even a plugin that does not directly call Python
must be able to `#include <Python.h>`.

## Pull Matching USD Dev Artifacts With Packman

Create a small packman project file next to your plugin source — for
example, `usd-dev.packman.xml`:

```python
<project toolsVersion="6.0">
  <!--
    Replace PACKAGE_NAME_FROM_ALL_DEPS and VERSION_FROM_ALL_DEPS with
    the inner <package> element's name and version copied verbatim
    from the usd-release entry in
    <isaac-sim-install>/kit/dev/all-deps.packman.xml.
  -->
  <dependency name="usd-release" linkPath="_deps/usd-release">
    <package name="PACKAGE_NAME_FROM_ALL_DEPS" version="VERSION_FROM_ALL_DEPS"/>
  </dependency>
</project>
```

Then pull the matching dev artifacts using the packman bundled with the
installer:

```python
<isaac-sim-install>/kit/dev/tools/packman/packman pull \
    usd-dev.packman.xml --platform linux-x86_64
```

After `packman pull` finishes, `_deps/usd-release/` will contain the
USD development tree:

```python
_deps/usd-release/
  include/
    pxr/        # OpenUSD C++ headers; in OpenUSD 25.x and later,
                # Boost.Python is vendored under pxr/external/boost/
    tbb/        # TBB headers used by USD
  lib/          # Packman-built USD libraries (do NOT link against these)
  pxrConfig.cmake
  cmake/
```

Use `include/` for compilation. `pxrConfig.cmake` is shipped in the
drop, but it transitively `find_dependency()`-loads the
`*Config.cmake` files for TBB, MaterialX, Imath, and OpenSubdiv, and
the `usd-release` packman drop does not include them. A plain
`find_package(pxr REQUIRED)` therefore fails to resolve. The recipe in
the next section sidesteps this by pointing CMake at `include/`
directly. **Do not** link your plugin against the libraries under
`_deps/usd-release/lib/` — see the next section.

## Compile and Link

The build needs:

* Headers from `_deps/usd-release/include/` and from
  `<isaac-sim-install>/kit/python/include/python3.XX/`.
* Link directory `<isaac-sim-install>/extscache/omni.usd.libs-*/bin/`
  (the libraries Isaac Sim loads at runtime), **not**
  `_deps/usd-release/lib/`.
* Link libraries `usd_ar`, `usd_sdf`, `usd_tf`, `usd_plug`,
  `usd_vt` (add more as your plugin requires).
* Linker flag `-Wl,--no-as-needed` around those libraries.

The same paths and flags apply to any build system, but how each tool
expresses them differs — some accept absolute filesystem paths
directly, others encourage wrapping pre-built libraries as targets or
referencing them through workspace-local paths. Use whatever mechanism
is idiomatic for your build system. As an example, in CMake:

```python
cmake_minimum_required(VERSION 3.20)
project(my_usd_plugin LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Python development headers shipped inside Isaac Sim.
set(ISAAC_SIM_INSTALL "/path/to/isaac-sim" CACHE PATH "Isaac Sim install root")
set(ISAAC_SIM_USD_LIBS "${ISAAC_SIM_INSTALL}/extscache/omni.usd.libs-<version>/bin"
    CACHE PATH "Directory containing libusd_*.so shipped with Isaac Sim")
set(ISAAC_SIM_PYTHON_INCLUDE "${ISAAC_SIM_INSTALL}/kit/python/include/python3.XX"
    CACHE PATH "Python development headers shipped inside Isaac Sim")

add_library(my_usd_plugin SHARED my_usd_plugin.cpp)

# Use the packman-pulled headers directly; do not call find_package(pxr).
# See the prose above for why pxrConfig.cmake is intentionally bypassed.
target_include_directories(my_usd_plugin PRIVATE
    "${CMAKE_SOURCE_DIR}/_deps/usd-release/include"
    "${ISAAC_SIM_PYTHON_INCLUDE}"
)

# Link against the USD libraries Isaac Sim actually loads at runtime,
# not the libraries packman pulled. Linking against packman's libs
# produces a binary that resolves to one set of pxrInternal_v0_* symbols
# at link time and a (potentially different) set at runtime, which
# manifests as undefined-symbol errors inside Plug::Load().
target_link_directories(my_usd_plugin PRIVATE "${ISAAC_SIM_USD_LIBS}")
target_link_libraries(my_usd_plugin PRIVATE
    -Wl,--no-as-needed
    usd_ar
    usd_sdf
    usd_tf
    usd_plug
    usd_vt
    -Wl,--as-needed
)
```

Two link-line details matter:

1. `-Wl,--no-as-needed` is required around the `usd_*` libraries.
   Without it, the linker drops any USD library whose symbols are only
   referenced through the C++ vtable and RTTI of your plugin class — and
   for any class discovered by `Plug` that is essentially every USD
   library you depend on. The result is a plugin that links cleanly but
   fails inside `Plug::Load()` at runtime with undefined-symbol errors
   against `pxrInternal_v0_*::...`.
2. The library search path passed to the linker must be
   `<isaac-sim-install>/extscache/omni.usd.libs-*/bin/`, **not**
   `_deps/usd-release/lib/`. The packman-pulled libraries are built
   with the same OpenUSD version but are not necessarily the exact same
   binaries Isaac Sim ships, and any mismatch (including build
   flags or symbol versioning) produces silent ABI breakage.

At runtime, set `PXR_PLUGINPATH_NAME` (or place your `plugInfo.json`
under a directory USD already scans) so that Isaac Sim discovers
your plugin during stage open.

## Plugin Source Requirements

USD’s plugin registration macros (`TF_REGISTRY_FUNCTION`,
`TF_REGISTRY_FUNCTION_WITH_TAG`) expand at global namespace scope and
reference unqualified `Tf_RegistryInit` and the per-library tag
`MFB_ALT_PACKAGE_NAME`. Two source-level requirements are not
optional:

1. Define three preprocessor macros at compile time, one per plugin
   target. They identify the plugin to USD’s registry; the values are
   conventionally the same short name in three case variants. In CMake,
   this looks like:

   ```python
   target_compile_definitions(my_usd_plugin PRIVATE
       MFB_PACKAGE_NAME=myUsdPlugin
       MFB_ALT_PACKAGE_NAME=myUsdPlugin
       MFB_PACKAGE_MODULE=MyUsdPlugin
   )
   ```
2. Place `PXR_NAMESPACE_USING_DIRECTIVE` near the top of any
   translation unit that uses `TF_REGISTRY_FUNCTION`, so that the
   unqualified `Tf_RegistryInit` inside the macro expansion resolves
   to the OpenUSD inline namespace:

   ```python
   #include <pxr/pxr.h>
   #include <pxr/base/tf/type.h>
   #include <pxr/usd/ar/resolver.h>

   PXR_NAMESPACE_USING_DIRECTIVE

   class MyResolver : public ArResolver { /* ... */ };

   TF_REGISTRY_FUNCTION(TfType) {
       TfType::Define<MyResolver, TfType::Bases<ArResolver>>();
   }
   ```

Without either, the plugin will not compile.

## Keeping Headers and Runtime In Sync

OpenUSD encodes its release version in the `pxrInternal_v0_*` inline
namespace. A plugin compiled against one OpenUSD release cannot be loaded
into a process that links a different OpenUSD release — the mangled
symbol names will not match, and you will see undefined-symbol errors
inside `Plug::Load()`.

The OpenUSD version shipped inside Isaac Sim can change across
releases. The table below records known mappings; always confirm the
exact version by inspecting the `usd-release` entry inside the
`all-deps.packman.xml` of the installer you are targeting.

| Isaac Sim version | OpenUSD version | Inline namespace (`pxrInternal_v0_*`) |
| --- | --- | --- |
| 5.1.0 | 24.05 | `pxrInternal_v0_24_5__pxrReserved__` |
| 6.0.0 | 25.11 | `pxrInternal_v0_25_11__pxrReserved__` |

Caution

The packman approach in this page automatically pulls the matching
OpenUSD headers for the installer you target, so you should not need
to read the inline-namespace strings yourself. They are listed here
only as a diagnostic aid: if you see an undefined symbol that
contains `pxrInternal_v0_24_5` but your plugin was compiled against
`pxrInternal_v0_25_11`, the headers and runtime are out of sync and
the link step is pointing at the wrong USD libraries. Confirm the
exact namespace string for your installer with `nm -D --defined-only
extscache/omni.usd.libs-*/bin/libusd_tf.so | head` before
relying on this table.

## Related

* [CLI extension templates](../utilities/cli_extension_templates.html#isaac-sim-cli-extension-templates) — in-tree C++ Kit extension
  development against the Isaac Sim source repository. Use this
  workflow when you can build inside the repo; use the page above when
  you can only build against the standalone installer.
* [USD Tools](usd_tools.html#isaac-sim-app-usd-tools) — GUI-side USD tooling shipped with
  Isaac Sim.

On this page

* [When You Need This](#when-you-need-this)
* [Prerequisites](#prerequisites)
* [Pull Matching USD Dev Artifacts With Packman](#pull-matching-usd-dev-artifacts-with-packman)
* [Compile and Link](#compile-and-link)
* [Plugin Source Requirements](#plugin-source-requirements)
* [Keeping Headers and Runtime In Sync](#keeping-headers-and-runtime-in-sync)
* [Related](#related)

---

### Application Template

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/app_template/index.html

* Application Template

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Application Template

Deprecated since version 6.0.0: Isaac Sim 5.1.0 was the final release of the standalone Application Template (`isaacsim-app-template`). Starting with Isaac Sim 6.0.0, its functionality is integrated into the open-source [Isaac Sim repository](https://github.com/isaac-sim/IsaacSim).

Isaac Sim can also be installed and customized via the [application template repo](https://github.com/isaac-sim/isaacsim-app-template).
This repository allows you to build lightweight apps that pull extensions from the registry directly.
We provide a set of default applications that mirror the main Isaac Sim binary application configs as well as a set of templates that can be customized and extended for your own applications.

For more details and a quick start guide see [here](https://github.com/isaac-sim/isaacsim-app-template).

---

