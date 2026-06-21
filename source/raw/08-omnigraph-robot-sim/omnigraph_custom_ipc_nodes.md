---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/omnigraph/omnigraph_custom_ipc_nodes.html
title: "Custom IPC Nodes"
section: "OmniGraph"
module: "08-omnigraph-robot-sim"
checksum: "6f58adf7a6528737"
fetched: "2026-06-21T13:40:09"
---

* [OmniGraph](index.html)
* Building Custom IPC OmniGraph Nodes

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Building Custom IPC OmniGraph Nodes

This guide explains how to build OmniGraph nodes for inter-process communication (IPC) in Isaac Sim. It covers the node schema, transport lifecycle with `BaseResetNode`, non-blocking I/O inside `compute`, and how to add your transport library as a dependency. The OmniGraph patterns apply regardless of the IPC stack that you use. The working example is `isaacsim.examples.ipc`, a clock-send and step-receive node pair over BSD sockets in C++ and Python. The tutorial starts by scaffolding a new extension with the CLI template so you have a working build skeleton before writing any IPC code.

Note

This workflow requires a **source checkout** of the [Isaac Sim](https://github.com/isaac-sim/IsaacSim) repository. It is not supported with the pip packages or the binary release. Clone the GitHub repository before you begin.

Note

All commands in this tutorial are run from the **Isaac Sim repository root** (the directory that contains `build.sh`/`build.bat` and `repo.sh`/`repo.bat`).

## Before You Start

**Prerequisites**:

* **Custom C++ extensions** — [Kit C++ Extension Template](https://docs.omniverse.nvidia.com/kit/docs/kit-extension-template-cpp/latest/index.html).
* **OmniGraph** — [OmniGraph Core Concepts](https://docs.omniverse.nvidia.com/extensions/latest/ext_omnigraph/getting-started/core_concepts.html "(in Omniverse Extensions)") and [Basic OmniGraph Tutorial](https://docs.omniverse.nvidia.com/extensions/latest/ext_omnigraph/tutorials/gentle_intro.html "(in Omniverse Extensions)").
* **Custom nodes** — [Custom Python Nodes](omnigraph_custom_python_nodes.html#isaac-sim-app-omnigraph-custom-python-nodes) and [Custom C++ Nodes](omnigraph_custom_cpp_nodes.html#isaac-sim-app-tutorial-advanced-omnigraph-custom-cpp-nodes).

Optional: [Isaac Sim OmniGraph Tutorial](omnigraph_tutorial.html#isaac-sim-app-tutorial-gui-omnigraph), if you are new to the Action Graph editor.

See also

[ROS 2 Python Custom OmniGraph Node](../ros2_tutorials/tutorial_ros2_custom_omnigraph_node_python.html#isaac-sim-app-ros2-custom-omnigraph-node-python) for a complete Python node
example. ROS 2 context, but the `internal_state()` factory,
`BaseResetNode`, `db.per_instance_state`, and
`og.ExecutionAttributeState.ENABLED` patterns are identical for any IPC
node.

## Scaffold Your Extension

Before writing IPC code, create the extension skeleton with the CLI template:

Linux

```python
./repo.sh template new
```

Windows

```python
.\repo.bat template new
```

When prompted, select **Isaac Sim OmniGraph Node Extension**. You will be asked for:

* `extension_name` Dotted identifier, for example `isaacsim.my.ipc.nodes`.
* `title` Human-readable name shown in the Extensions window.
* `description` Short summary.
* `category` Used to group your nodes in the Action Graph node library (for example `Simulation`).

The template creates the full extension skeleton under `source/extensions/<extension_name>/`:

```python
source/extensions/<extension_name>/
├── config/extension.toml          ← metadata, dependencies, test entries
├── nodes/
│   ├── OgnExampleCpp.ogn          ← rename/replace with your IPC node schema
│   └── OgnExampleCpp.cpp          ← rename/replace with your IPC node implementation
├── plugins/<extension_name>/
│   └── PluginInterface.cpp        ← Carbonite plugin + OGN registration (keep as-is)
├── bindings/<extension_name>/
│   └── Bindings.cpp               ← pybind11 bindings; acquires the Carbonite interface (keep as-is)
├── include/<extension_name>/
│   └── IExampleNodes.h            ← Carbonite interface (keep as-is)
├── python/nodes/
│   ├── OgnExamplePython.ogn       ← rename/replace with your Python node schema
│   └── OgnExamplePython.py        ← rename/replace with your Python Node Implementation
├── python/impl/extension.py       ← calls acquire_example_ipc_interface() on startup to load the plugin
├── python/tests/                  ← test modules go here
└── premake5.lua                   ← build configuration
```

The build step is required before the extension loads in Isaac Sim — it compiles the C++ plugin and generates the OmniGraph database files that register your nodes. Run it now:

Linux

```python
./build.sh
```

Windows

```python
.\build.bat
```

The generated nodes — **Example C++ Node** (`OgnExampleCpp`) and **Example Python Node** (`OgnExamplePython`) — are placeholder stubs that double an input value. The display names in the Action Graph library come from the `uiName` field in each `.ogn` file, not the file name. Rename or replace them with your actual IPC node(s) as you work through the sections below.

Try it: verify your scaffold

After the build completes above, confirm the scaffold registers its placeholder nodes:

1. Launch the repo-built Isaac Sim — not a separately installed Isaac Sim:

   Linux

   ```python
   ./_build/linux-x86_64/release/isaac-sim.sh
   ```

   Windows

   ```python
   .\_build\windows-x86_64\release\isaac-sim.bat
   ```
2. Open **Window → Extensions**, search for your extension name (for example `isaacsim.my.ipc.nodes`), and enable it.
3. Open **Window → Graph Editors → Action Graph** and search for `Example C++ Node` and `Example Python Node` in the node library. These names match the `uiName` fields in the scaffold’s `.ogn` files.

If both nodes appear, the scaffold is wired correctly. Proceed to [Design and Implement Your Nodes](#design-and-implement-your-nodes) to replace the placeholders.

If the nodes do not appear, check the following:

* The build (`./build.sh` on Linux, `.\build.bat` on Windows) completed without errors. Nodes are not registered until the C++ plugin is compiled and the OmniGraph database files are generated by the build.
* You launched the repo-built Isaac Sim (`./_build/linux-x86_64/release/isaac-sim.sh` or `.\_build\windows-x86_64\release\isaac-sim.bat`). A separately installed Isaac Sim does not search the repository `exts/` directory and will not find your extension.
* The extension is enabled (green toggle) in **Window → Extensions**. If it was enabled before the build ran, disable and re-enable it.
* After any `.ogn` schema or code change, the build must be re-run and Isaac Sim restarted before updated nodes appear.

## Add Your Transport Library

Before writing node code, wire in the library that provides your IPC and serialization. The generated `config/extension.toml` and `premake5.lua` are already in place. The sections below show where to add entries.

### Python

Isaac Sim ships a pip archive (`omni.isaac.core_archive` and related extensions) that pre-bundles many common packages, including NumPy and SciPy. If your library is already in that archive you can import it directly with no extra configuration.

If the package is not yet bundled, declare it in `config/extension.toml`, for example:

```python
[python.pipapi]
requirements = ["pyzmq>=25", "grpcio"]  # replace with your actual packages
use_online_index = true
```

Isaac Sim resolves these at extension startup. `use_online_index = true` must be set. If it is omitted or set to `false`, `omni.kit.pipapi` logs a warning and skips the `requirements` list entirely.

### C++

Prebuilt native libraries go through packman. These steps follow the same pattern described in the [Kit Extension C++ template documentation](https://docs.omniverse.nvidia.com/kit/docs/kit-extension-template-cpp/latest/index.html):

1. **Declare the dependency.** Add your library to `deps/ext-deps.packman.xml`. It is the designated file for extension-specific dependencies (separate from the Kit SDK deps). The unpacked tree typically lands under `_build/target-deps/<libname>/`:

   ```python
   <project toolsVersion="5.0">
     <dependency name="mylib" linkPath="../_build/target-deps/mylib">
       <package name="mylib" version="1.2.3" />
     </dependency>
   </project>
   ```
2. **Update ``premake5.lua``.** Point to the include and library directories and add the link:

   ```python
   includedirs { "%{target_deps}/mylib/include" }
   libdirs     { "%{target_deps}/mylib/lib/%{platform}" }
   links       { "mylib" }
   ```
3. **Shared libraries at runtime.** If the library ships as a `.so` / `.dll`, either bundle it beside the extension plugin or list it under `[native.library]` in `extension.toml` so Kit’s loader finds it.

The sample extension uses only standard BSD socket APIs and has no additional native library entries beyond the plugin itself.

## Design and Implement Your Nodes

### Design Principle

Keep IPC nodes thin. They should only handle **serialization and transport**. Simulation data reads (joint positions, sensor data, simulation time) belong in upstream built-in nodes wired into the graph before your IPC node. Downstream processing or command writes belong in other nodes after it. This keeps `compute` fast and makes the graph layout self-documenting.

### What Every IPC Node Requires

Every custom IPC node requires the same six things, regardless of transport:

* **Node schema** (`.ogn` file) — declare inputs (URI, config), outputs (data, `execOut`), and state. Refer to the sample `.ogn` files under `nodes/` in `isaacsim.examples.ipc` as a reference.
* `BaseResetNode` subclass — holds per-instance state (sockets, buffers, handles). Implement `reset()` (C++) or `custom_reset()` (Python) to tear down the transport when the timeline stops or inputs change.
* `compute(db)` with a lifecycle split:

  > + Detect input changes (URI, config) → call reset and teardown
  > + Try to open the transport if not ready → return early on failure (retry next evaluation)
  > + Do non-blocking I/O (send or try-receive)
  > + Write `db.outputs` and fire `execOut`
* **Non-blocking I/O** — never block indefinitely in `compute`. Use try-receive, timeouts, or offload slow paths to a worker thread (refer to [Performance Considerations](#performance-considerations)).
* **Fire** `execOut` at the end of `compute` to signal downstream nodes that the transport operation is complete and/or new data is ready. You control when to fire it. For example, fire on every evaluation, only on successful send, or only when a full message has been received.
* **Your transport library** — add it as a dependency (refer to [Add Your Transport Library](#add-your-transport-library) above) and replace the TCP helpers with your stack’s API.

### OGN Schema Quick Reference

Each `.ogn` file is a single JSON object keyed by the node’s registered type
name. The minimum schema for a Python IPC node looks like this:

```python
{
    "MyNodeName": {
        "version": 1,
        "language": "Python",
        "description": "One-line description shown in the node library.",
        "metadata": { "uiName": "My Node Display Name" },
        "categoryDefinitions": "config/CategoryDefinition.json",
        "categories": "myCategory",
        "inputs": {
            "execIn":  { "type": "execution", "description": "Trigger." },
            "uri":     { "type": "string",    "description": "...", "default": "tcp://127.0.0.1:5550" },
            "myValue": { "type": "double",    "description": "...", "default": 0.0 }
        },
        "outputs": {
            "execOut":  { "type": "execution", "description": "Output execution port." },
            "myTokens": { "type": "token[]",   "description": "Array of token outputs." }
        }
    }
}
```

Common scalar types: `"string"`, `"double"`, `"float"`, `"int"`,
`"uint"`, `"bool"`, `"execution"`. Array variants append `[]`:
`"double[]"`, `"float[]"`, `"token[]"`, etc. The `"default"` key is
required for non-execution scalar inputs; use `[]` for array inputs.

`categoryDefinitions` is a path relative to the `nodes/` directory that
points to a JSON file mapping category keys to human-readable display strings:

```python
{
    "categoryDefinitions": {
        "myCategory": "My node group label in the Action Graph library"
    }
}
```

### C++ Node Implementation

`BaseResetNode` is declared in `isaacsim.core.includes`. This extension is a compile-time only dependency, do **not** add it to `[dependencies]` in `extension.toml`. Instead, add the header path in `premake5.lua`:

```python
includedirs { "%{root}/source/extensions/isaacsim.core.includes/include" }
```

Then include the header in your `.cpp` file:

```python
#include <isaacsim/core/includes/BaseResetNode.h>
```

Derive your per-instance node class from `isaacsim::core::includes::BaseResetNode`. That base subscribes to the timeline stop event and calls your `reset()` so transport handles are not left open after simulation stops.

Replace the generated `OgnExampleCpp` stub with a class like this (refer to `OgnSimpleSendSimulationClockCpp.cpp` in `isaacsim.examples.ipc` for TCP implementation):

```python
#include <isaacsim/core/includes/BaseResetNode.h>

#include <OgnMyIpcNodeCppDatabase.h>
#include <memory>
#include <string>

using isaacsim::core::includes::BaseResetNode;

class OgnMyIpcNodeCpp : public BaseResetNode
{
public:
    static bool compute(OgnMyIpcNodeCppDatabase& db)
    {
        auto& state = db.perInstanceState<OgnMyIpcNodeCpp>();

        // Detect input changes (e.g. URI) and reset transport.
        const std::string uriIn(db.inputs.uri());
        if (state.m_handle && state.m_handle->getUri() != uriIn)
        {
            state.reset();
        }

        const bool success = state.ensureOpenAndTransfer(db);
        // Fire execOut unconditionally (send nodes). For receive nodes, fire only when
        // a complete message arrives (i.e. only when success == true).
        db.outputs.execOut() = omni::graph::core::kExecutionAttributeStateEnabled;
        return success;
    }

    static void releaseInstance(NodeObj const& nodeObj, GraphInstanceID instanceId)
    {
        auto& state = OgnMyIpcNodeCppDatabase::sPerInstanceState<OgnMyIpcNodeCpp>(nodeObj, instanceId);
        state.reset();
    }

    void reset() override
    {
        if (m_handle)
        {
            m_handle->close();
            m_handle.reset();
        }
    }

private:
    bool isOpen() const
    {
        return m_handle && m_handle->isOpen();
    }

    void tryOpen(OgnMyIpcNodeCppDatabase& db)
    {
        // Open transport from db.inputs (e.g. URI, config).
        // m_handle = std::make_unique<MyTransportHandle>(std::string(db.inputs.uri()));
    }

    bool transfer(OgnMyIpcNodeCppDatabase& db)
    {
        // Non-blocking send or try-receive; write db.outputs on success.
        // See Performance Considerations for time-budget guidance.
        return false; // replace with actual transfer
    }

    bool ensureOpenAndTransfer(OgnMyIpcNodeCppDatabase& db)
    {
        if (!isOpen())
        {
            tryOpen(db);
            if (!isOpen())
                return false;
        }
        return transfer(db);
    }

    std::unique_ptr<MyTransportHandle> m_handle; // replace with your transport type
};

REGISTER_OGN_NODE()
```

Note

The generated `python/impl/extension.py` calls `acquire_example_ipc_interface()` in
`on_startup()`. This is what triggers the Carbonite plugin to load and run
`INITIALIZE_OGN_NODES()`, registering your C++ nodes. If your nodes do not appear in the
Action Graph library, verify that `extension.py` is calling the acquire function and that
`PluginInterface.cpp` does **not** contain a `CARB_PLUGIN_IMPL_DEPS` line, because that macro
can prevent the plugin from loading.

### Python Node Implementation

`BaseResetNode` is provided by the `isaacsim.core.nodes` extension. Add it as a dependency in `config/extension.toml` and import it in your node file:

```python
[dependencies]
"isaacsim.core.nodes" = {}
```

```python
import omni.graph.core as og
from isaacsim.core.nodes import BaseResetNode
```

Put per-instance data in a small class that subclasses `BaseResetNode`. Pass `initialize=False` to `super().__init__`, if you lazy-open sockets in `compute`, as the samples do. Without it, `BaseResetNode.__init__` calls `custom_reset()` immediately during construction, before your instance attributes (such as, `self.sock = None`) are set, raising `AttributeError`. Implement `custom_reset()` to close sockets and clear buffers. `custom_reset()` runs on timeline stop and mirrors the C++ `reset()`.

Replace the generated `OgnExamplePython` stub with a class like this (refer to `OgnSimpleSendSimulationClockPy.py` in `isaacsim.examples.ipc` for a full TCP implementation):

```python
import omni.graph.core as og
from isaacsim.core.nodes import BaseResetNode

class OgnMyIpcNodePyState(BaseResetNode):
    """Per-instance state for the template IPC node."""

    def __init__(self) -> None:
        # Declare all attributes BEFORE calling super().__init__,
        # because BaseResetNode.__init__ calls custom_reset() immediately.
        self.handle = None  # replace with your transport handle
        self.uri = ""
        super().__init__(initialize=False)

    def custom_reset(self) -> None:
        """Reset transport state when timeline or inputs change."""
        # Called on timeline stop and when inputs change.
        if self.handle is not None:
            self.handle.close()
            self.handle = None
        self.uri = ""

class OgnMyIpcNodePy:
    """Template OmniGraph node for custom IPC transports."""

    @staticmethod
    def internal_state() -> OgnMyIpcNodePyState:
        """Create per-instance state for the node."""
        return OgnMyIpcNodePyState()

    @staticmethod
    def compute(db: object) -> bool:
        """Evaluate one non-blocking IPC transfer step."""
        state = db.per_instance_state

        uri = db.inputs.uri
        if state.handle is not None and state.uri != uri:
            state.custom_reset()

        if state.handle is None:
            # Open transport from inputs (e.g. URI, config).
            # state.handle = open_my_transport(uri)
            # state.uri = uri
            # Fire execOut even on failure so downstream nodes keep running.
            db.outputs.execOut = og.ExecutionAttributeState.ENABLED
            return False

        # Non-blocking send or try-receive; write db.outputs on success.
        # See Performance Considerations for time-budget guidance.
        success = False  # replace with actual transfer

        # For send nodes: fire execOut every tick.
        # For receive nodes: fire execOut only when a full message arrives.
        if success:
            db.outputs.execOut = og.ExecutionAttributeState.ENABLED
        return success
```

Try it: implement and build your node

Adapt your scaffolded extension to a minimal IPC sender:

1. **Update the OGN schema.** In `nodes/OgnExampleCpp.ogn` (or `OgnExamplePython.ogn`), rename the node and add a `uri` string input (default `"127.0.0.1:9000"`) and `execIn`/`execOut` execution ports.
2. **Replace the implementation.** Copy the template above into `OgnExampleCpp.cpp` (or `OgnExamplePython.py`), rename classes to match, and fill in a no-op `transfer()` that always returns `true`.
3. **Rebuild:** `./build.sh` (Linux) or `.\build.bat` (Windows).
4. **Restart Isaac Sim** by closing and relaunching `./_build/linux-x86_64/release/isaac-sim.sh` (Linux) or `.\_build\windows-x86_64\release\isaac-sim.bat` (Windows).
5. **Verify:** enable your extension in Isaac Sim and confirm the renamed node appears in the Action Graph library under its new `uiName`.

For a complete TCP implementation of the same pattern, study `OgnSimpleSendSimulationClockCpp.cpp` (or the Python equivalent) in `source/extensions/isaacsim.examples.ipc/`.

For Python-only extensions (no C++ plugin), omit `project_ext_plugin`, `project_ext_bindings`, and all `includedirs` / `links` entries from `premake5.lua`. Keep `add_ogn_dependencies` (processes `.ogn` files and generates `*Database.py` modules) and the `repo_build.prebuild_link` block:

```python
local ext = get_current_extension_info()
local ogn = get_ogn_project_information(ext, "myorg/my/ipc/nodes")
project_ext(ext)

add_ogn_dependencies(ogn, { "python/nodes" })

repo_build.prebuild_copy {
    { "python/__init__.py",  ogn.python_target_path },
    { "python/extension.py", ogn.python_target_path },
}

repo_build.prebuild_link {
    { "python/nodes",  ogn.python_target_path .. "/nodes" },
    { "python/tests",  ogn.python_target_path .. "/tests" },
}
```

### Sample Extension Reference

Source: `source/extensions/isaacsim.examples.ipc/`.

| Registered type name | Implementation | Role |
| --- | --- | --- |
| `SimpleSendSimulationClockCpp` / `SimpleSendSimulationClockPy` | C++ / Python | Forwards the simulation clock to an external process on each evaluation. Connects as a TCP client to `uri` (`host:port`). Input: `simulationTime` (`double`, seconds; connect from `IsaacReadSimulationTime`). Encodes the value as nanoseconds in an 8-byte signed int64 (little-endian) and sends it. Fires `execOut` on every evaluation. |
| `SimpleReceiveExternalStepCpp` / `SimpleReceiveExternalStepPy` | C++ / Python | Receives a step counter from an external process and exposes it to downstream nodes. Binds as a TCP server on `uri` and accepts one client. Outputs a `step` (uint32). Fires `execOut` only when a complete 4-byte message arrives. Partial reads are buffered across evaluations. |

In graphs, the full path is typically `isaacsim.examples.ipc.<TypeName>` (refer to the extension’s `config/extension.toml`).

C++ and Python follow the same sequence in `compute`. They only differ by name and state wiring. For example, `reset()` compared to `custom_reset()`, and C++ `state` from the OGN database compared to Python `internal_state()`.

```python
compute(db)
     │
     ├─► uri (or relevant inputs) changed? ──yes──► teardown transport
     │                    C++: state.reset()    Python: custom_reset()
     ▼
try open: connect or listen / accept
     │         (retry next eval if not ready)
     ▼
transport ready? ──no──► return false
     │    (recv: often "no full message yet")
     yes
     ▼
framed try-send / try-recv  (see Performance Considerations for time budget)
     │
     ▼
write db.outputs and set execOut
     │
     ▼
return true/false  (per node type / sample rules)
```

## Use Your Nodes in Isaac Sim

### Enable Your Extension and Find Your Nodes

Note

If you have not yet replaced the scaffold placeholders, you can follow the steps below using `isaacsim.examples.ipc` as a stand-in — it ships with Isaac Sim and has fully working nodes ready to enable and find. Repeat the steps with your own extension name once you have implemented and built your nodes.

The build (`./build.sh` on Linux, `.\build.bat` on Windows) compiles your extension and places the output under `_build/<platform>/release/exts/<extension_name>/` (`linux-x86_64` or `windows-x86_64` depending on host). Isaac Sim launched from the same repo automatically searches that directory, so no additional path configuration is needed.

Note

Always launch Isaac Sim from the repo build. A separately installed Isaac Sim does not search the repository `exts/` directory and will not find your extension. After each build run, restart Isaac Sim — a loaded C++ plugin cannot be hot-swapped.

Launch (or restart) Isaac Sim from the repo build:

Linux

```python
./_build/linux-x86_64/release/isaac-sim.sh
```

Windows

```python
.\_build\windows-x86_64\release\isaac-sim.bat
```

Then enable your extension:

1. Open **Window > Extensions**.
2. Search for your extension name (for example `isaacsim.my.ipc.nodes`) and enable it.

Your nodes then appear in the Action Graph node library under the category you chose during scaffolding. Search by the `uiName` value defined in your `.ogn` file (for the scaffold defaults: `Example C++ Node` and `Example Python Node`).

### Building an Example Graph

The steps below build the sample graph for `tcp_tutorial_playback_bridge.py` using the reference nodes from `isaacsim.examples.ipc`. Use it to verify the end-to-end IPC pattern before wiring in your own nodes.

1. Enable the sample extension. **Open Window > Extensions**, search for `isaacsim.examples.ipc`, and enable IPC OmniGraph Node Examples.
2. Open the Action Graph editor. **Window > Graph Editors > Action Graph**.
3. Place the tutorial nodes. Under Isaac Examples in the node library, add Receive External Step and Send Simulation Clock. Use the search box to add On Playback Tick and Isaac Read Simulation Time from `isaacsim.core.nodes`. Either C++ or Python node pair works with the bridge script.
4. Wire the graph.

   Execution chain:

   * On Playback Tick `execOut` → Receive External Step `execIn`
   * Receive External Step `execOut` → Send Simulation Clock `execIn`

   Data:

   * Isaac Read Simulation Time `simulationTime` → Send Simulation Clock `simulationTime`

   The default `uri` values are `127.0.0.1:9001` on the receive node and `127.0.0.1:9000` on the send node.
5. **Start playback.** Click the **Play** button in the toolbar (or press **Space**) to begin the simulation.

General Action Graph UI is covered in [Isaac Sim OmniGraph Tutorial](omnigraph_tutorial.html#isaac-sim-app-tutorial-gui-omnigraph) and in the OmniGraph documentation linked in [Before You Start](#before-you-start).

After the graph is wired and playback is running, Receive External Step listens on its URI, the bridge script connects and sends the first step token, and Send Simulation Clock reports the current simulation time back to the script after each tick. The script drives the timing loop and Isaac Sim advances one tick per received step.

Try it: run the bridge with your own node

Once the reference graph works end-to-end with `isaacsim.examples.ipc` nodes, substitute your custom node:

1. In the graph, delete the `SimpleSendSimulationClock` node.
2. Add your renamed node from the exercise above.
3. Wire it the same way: Receive External Step `execOut` → your node `execIn`, and Isaac Read Simulation Time `simulationTime` → your node `simulationTime`.
4. Run the bridge script. Because `transfer()` is still a stub that returns `true` without sending data, the script will connect but receive no clock output — that is expected. This confirms that your extension loads, enables, and participates in the graph.
5. To complete the implementation, add the actual send logic to `transfer()`. Use `OgnSimpleSendSimulationClockCpp.cpp` (or the Python equivalent) in `source/extensions/isaacsim.examples.ipc/` as a reference.

### External Python Playback Bridge

The `tcp_tutorial_playback_bridge.py` script demonstrates a complete roundtrip. It listens for the eight-byte clock that the Send node emits, connects to the Receive node’s listen port, primes one step, then for each frame reads the clock and sends back the next step so the next `OnPlaybackTick` can fire.

The script only uses the Python standard library (`socket`, `struct`, `argparse`) and has no Isaac Sim or third-party dependencies. Run it from the repo root with any system `python3`:

```python
python3 source/extensions/isaacsim.examples.ipc/python/scripts/tcp_tutorial_playback_bridge.py
```

Pass `--help` to see `--clock-host`, `--clock-port`, `--step-host`, `--step-port`, and `--max-frames` options.

Warning

The script binds a TCP listener on `127.0.0.1`. For real deployments, bind only to loopback unless you intentionally expose a port. Open interfaces can increase attack surface. Treat any IPC bridge like a network service, where authentication, TLS or equivalent, and firewall rules are your responsibility.

## Performance Considerations

**Stay within your frame budget.**

> OmniGraph evaluates `compute` on paths that must stay responsive relative to simulation, UI, and other graphs. The usual failure mode is unpredictably long work and is not “synchronous” I/O by itself. Waiting on a slow peer, large copies, contended locks, or RPC that can stall for many milliseconds may cause performance issues.

**Small, fast paths are often fine.**

> A tiny, fixed-size, fire-and-forget operation in `compute` (the tutorial’s eight byte clock send once the socket is connected) can stay on the graph thread if it consistently completes within your per-node budget at the target frame rate. The same applies to other stacks when you have measured the path and it does not wait on back-pressure from the remote side.

**When to use workers, queues, or async APIs.**

> * If a call can block for an unknown duration (request/response, readiness waits, large payloads, or anything that can exceed your per-node budget), run that IPC on a worker thread. Use callbacks that enqueue results, and keep `compute` to non-blocking dequeue and writing `db.outputs`.
> * For inbound data, try-receive (as in the tutorial’s step node) avoids waiting indefinitely when the external process does not send on your schedule.
> * **Async or callback-based I/O:** Drive network or IPC on a worker thread, push decoded messages into a thread-safe queue, and let `compute` only dequeue (non-blocking) and write `db.outputs`.
> * **Deferred completion:** Post work from `compute` without waiting for the reply. A background thread enqueues results for a later evaluation.

**Structured messages vs fixed bytes.**

> The fixed-size framing in the tutorial is for clarity. A production bridge typically uses your library’s message format (IDL-generated types, JSON, or another schema). You still decide when to send, how to parse inbound data, and how to keep each `compute` within budget.

**Large messages (camera frames, point clouds).**

> Single-shot calls that move multi-megabyte payloads can stress memory and scheduling. Use streaming APIs, explicit back-pressure (drop or skip frames on a slow consumer), or shared-memory and zero-copy paths outside OmniGraph, with the node passing only handles or small metadata.

## Built-In Nodes for Data in and Out

Besides `isaacsim.examples.ipc`, several extensions register OmniGraph nodes that read simulation state or drive simulation inside Isaac Sim, without acting as a general-purpose bridge to another process. The table highlights types that often sit next to custom IPC nodes in a bridge graph.

Before designing your custom node’s inputs and outputs, check the `.ogn` of the built-in nodes you plan to connect to—their output attribute names and types determine what your node needs to consume or produce.

Common built-in OmniGraph nodes for bridge-style graphs

| Goal | Node (registered type) | Extension | Key inputs / outputs (abbrev.) |
| --- | --- | --- | --- |
| Read joint positions / velocities (and efforts) for publishing | `IsaacArticulationState` | `isaacsim.core.nodes` | In: `robotPath` or `targetPrim`, optional `jointNames` / `jointIndices`. Out: `jointPositions`, `jointVelocities` (`double[]`), `jointNames` (`token[]`), plus measured effort arrays. |
| Alternative joint state (physics sensor path) | `isaacsim.sensors.physics.IsaacReadJointState` | `isaacsim.sensors.physics.nodes` | In: `prim` (articulation root). Out: `jointPositions`, `jointVelocities`, `jointEfforts`, `jointNames`, `execOut`, etc. |
| Apply joint position / velocity / effort commands | `IsaacArticulationController` | `isaacsim.core.nodes` | In: same robot targeting as above; `positionCommand`, `velocityCommand`, `effortCommand` (`double[]`). Angular units are radians at the controller API. |
| Simulation tick / gating | `OnPhysicsStep`, `IsaacSimulationGate`, `IsaacReadSimulationTime`, … | `isaacsim.core.nodes` | Use to pace state reads and command writes consistently (exact attributes vary by node). |
| Camera / viewport render product path (setup only) | `IsaacGetViewportRenderProduct`, `IsaacCreateRenderProduct`, `IsaacAttachHydraTexture`, `IsaacSetCameraOnRenderProduct` | `isaacsim.core.nodes` | Mostly paths and targets (`renderProductPath`, `renderProductPrim`). Pixels require a separate readback step. Refer to [Camera and Render Products](#camera-and-render-products). |

Other read extensions you can chain before a custom sender:

* `isaacsim.sensors.physics.nodes` — IMU, contact, effort, etc., backed by `isaacsim.sensors.experimental.physics`.
* `isaacsim.sensors.physx` — for example Isaac Read Lidar Beams, Isaac Read Lidar Point Cloud, Isaac Read Light Beam Sensor.
* `isaacsim.sensors.rtx.nodes` — for example Isaac Extract RTX Sensor Point Cloud.

For IPC with external applications (topics, services, or other runtimes), use dedicated bridge extensions rather than treating the nodes in the table above as a transport layer. Examples include `isaacsim.ros2.nodes` (ROS 2) or `isaacsim.ucx.nodes` (UCX). Those extensions play the same role as the TCP tutorial nodes, not the sensor-read nodes in the table.

**Reference implementations in this repository.**

> The `source/extensions/` directory contains full IPC bridge implementations
> you can study when you outgrow the TCP tutorial. Two stacks are available:
>
> > * **ROS 2**: `isaacsim.ros2.nodes`, `isaacsim.ros2.bridge`, and related
> >   packages.
> > * **UCX**: `isaacsim.ucx.nodes`, `isaacsim.ucx.core`,
> >   `isaacsim.ucx.bridge`.
>
> Each stack shows how a complete bridge is laid out: `extension.toml`
> dependencies, native plugins, C++ and Python OmniGraph nodes, and transport
> backends.

Use the OmniGraph node library in the Kit docs to search by name: [OmniGraph](https://docs.omniverse.nvidia.com/extensions/latest/ext_omnigraph.html "(in Omniverse Extensions)").

## Camera and Render Products

Getting raw RGB pixels into a custom IPC node requires more than a plain `uchar[]` OGN input. Imagery typically flows through a Replicator pipeline or a render product chain before reaching any IPC encoder, not a single wire in the graph editor. The key steps are:

> 1. Set up a render product (`IsaacCreateRenderProduct` or `IsaacGetViewportRenderProduct`) and attach a camera.
> 2. Feed the render product into a readback mechanism either a:
>
>    * Replicator annotator (host-friendly NumPy arrays)
>    * Hydra texture chain (GPU handles through `IsaacAttachHydraTexture`)
> 3. Pass the resulting CPU-addressable bytes or arrays into your IPC encoder node.

The `isaacsim.ros2.bridge` extension’s camera helper node is a concrete reference for how this pipeline is assembled. The ROS 2 camera publisher wires a render product to host readback and then to IPC. Browsing that source is the fastest way to understand the pattern before building your own.

Refer to [Performance Considerations](#performance-considerations) before passing large buffers through `compute`. Camera frames are a common source of frame-budget overruns.

## Testing Your OmniGraph Node Implementation

Python integration tests for OmniGraph nodes can build Action Graphs at runtime
using `og.Controller.edit`, wire nodes together programmatically, drive the
timeline, and assert on output attribute values. Useful areas to cover:

* **Correct outputs**: Given known inputs, the node produces the expected
  `db.outputs` values.
* **execOut timing**: The node fires `execOut` only under the intended
  conditions. For send nodes, this means every evaluation. For receive nodes,
  this means only on data receipt.
* **Reset behavior**: Changing a URI input or stopping the timeline closes the
  transport, and a subsequent evaluation reopens it cleanly.
* **Edge cases**: Partial messages, peer disconnect, and malformed data from the
  external process.

For C++ helpers (parsing, encoding, and endianness), unit tests can run outside
Isaac Sim through a native test library such as doctest, wired in
`premake5.lua` and referenced from `extension.toml`.

Point `[[test]]` entries in your `extension.toml` at your test modules. The
generated test driver is typically
`_build/<platform>/<config>/tests/tests-<your.extension.id>.sh`. For a
scaffolded extension, tests go in `python/tests/` (already created by the
template).

For examples of the patterns above (async tests, `OnImpulseEvent`, free-port
helpers, and timeline control), refer to
`source/extensions/isaacsim.examples.ipc/python/tests/`.

On this page

* [Before You Start](#before-you-start)
* [Scaffold Your Extension](#scaffold-your-extension)
* [Add Your Transport Library](#add-your-transport-library)
  + [Python](#python)
  + [C++](#c)
* [Design and Implement Your Nodes](#design-and-implement-your-nodes)
  + [Design Principle](#design-principle)
  + [What Every IPC Node Requires](#what-every-ipc-node-requires)
  + [OGN Schema Quick Reference](#ogn-schema-quick-reference)
  + [C++ Node Implementation](#c-node-implementation)
  + [Python Node Implementation](#python-node-implementation)
  + [Sample Extension Reference](#sample-extension-reference)
* [Use Your Nodes in Isaac Sim](#use-your-nodes-in-isaac-sim-short)
  + [Enable Your Extension and Find Your Nodes](#enable-your-extension-and-find-your-nodes)
  + [Building an Example Graph](#building-an-example-graph)
  + [External Python Playback Bridge](#external-python-playback-bridge)
* [Performance Considerations](#performance-considerations)
* [Built-In Nodes for Data in and Out](#built-in-nodes-for-data-in-and-out)
* [Camera and Render Products](#camera-and-render-products)
* [Testing Your OmniGraph Node Implementation](#testing-your-omnigraph-node-implementation)