---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/python_scripting/manual_standalone_python.html
title: "Standalone Python"
section: "Python 脚本"
module: "02-fundamentals-dev"
checksum: "74eb06359f98fe33"
fetched: "2026-06-21T14:14:20"
---

* [Python Scripting and Tutorials](index.html)
* Python Environment

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Python Environment

This document will cover:

* Details about how running standalone Python scripts works.
* A short list of interesting/useful standalone Python scripts to try.
* Resources to develop Python scripts for NVIDIA Isaac Sim, such as VSCode and Jupyter Notebook support.

## Details: How `python.sh` works

Note

* On Windows use python.bat instead of python.sh
* The details of how python.sh works below are similar to how python.bat works

This script first defines the location of the apps folder so the contained .kit files can be located at runtime.

```python
# Get path to the script
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
# The apps directory is relative to where the script lives
export EXP_PATH=$SCRIPT_DIR/apps
```

Then we source the NVIDIA Isaac Sim Python environment so all extension interfaces can be loaded correctly.

```python
source ${SCRIPT_DIR}/setup_python_env.sh
```

The setup\_python\_env.sh script update/defined the following environment variables:

* ISAAC\_PATH: Path to the main isaac folder
* PYTHONPATH: Paths to each extensions Python interfaces
* LD\_LIBRARY\_PATH: Paths to binary interfaces required to find symbols at runtime
* CARB\_APP\_PATH: path to the core Omniverse kit executable

Finally, we execute the Python interpreter that is packaged with Omniverse:

```python
python_exe=${PYTHONEXE:-"${SCRIPT_DIR}/kit/python/bin/python3"}
...
$python_exe $@
```

## SimulationApp

The [SimulationApp Class](../py/source/extensions/isaacsim.simulation_app/docs/index.html) provides convenience functions to manage the lifetime of a NVIDIA Isaac Sim application.

### Usage Example:

The following code provides a usage example for how SimulationApp can be used to create an app, step forward in time and then exit.

Note

Any Omniverse level imports **must** occur after the class is instantiated.
Because APIs are provided by the extension/runtime plugin system, it must be loaded before they will be available to import.

Important

When running headless:

* Set `"headless": True` in the config when initializing `SimulationApp`
* Any calls that create/open a matplotlib window need to be commented out

```python
from isaacsim import SimulationApp

# Simple example showing how to start and stop the helper
simulation_app = SimulationApp({"headless": True})

### Perform any omniverse imports here after the helper loads ###

simulation_app.update()  # Render a single frame
simulation_app.close()  # Cleanup application
```

### Details: How `SimulationApp` works

Although `SimulationApp` further configures the application and exposes APIs, there are some fundamental steps in any Omniverse Kit-based implementation that must be executed.

The first is to get the carbonite framework.
Here the environment variables (e.g.: `CARB_APP_PATH`, `ISAAC_PATH` and `EXP_PATH`) were defined when running the python.sh script.

```python
import carb
import omni.kit.app

framework = carb.get_framework()
framework.load_plugins(
    loaded_file_wildcards=["omni.kit.app.plugin"],
    search_paths=[os.path.abspath(f'{os.environ["CARB_APP_PATH"]}/kernel/plugins')],
)
```

After loading the framework, it is possible to configure the start arguments before loading the application. For example:

```python
# Inject a experience config
sys.argv.insert(1, f'{os.environ["EXP_PATH"]}/isaacsim.exp.base.python.kit')

# Add paths to extensions
sys.argv.append(f"--ext-folder")
sys.argv.append(f'{os.path.abspath(os.environ["ISAAC_PATH"])}/exts')

# Run headless
sys.argv.append("--no-window")
```

And then start the application.

```python
app = omni.kit.app.get_app()
app.startup("Isaac-Sim", os.environ["CARB_APP_PATH"], sys.argv)
```

Shutting down a running application is done by calling `shutdown` and then unloading the framework:

```python
app.shutdown()
framework.unload_all_plugins()
```

### Enabling additional extensions

There are two methods for adding additional extensions:

1. Under `[dependencies]` section in an experience file (e.g.: `apps/isaacsim.exp.base.python.kit`):

   > ```python
   > # [dependencies]
   > # # Enable the layers and stage windows in the UI
   > # "omni.kit.window.stage" = {}
   > # "omni.kit.widget.layers" = {}
   > ```
2. From Python code:

   ```python
   from isaacsim import SimulationApp

   # Start the application
   simulation_app = SimulationApp({"headless": False})

   # Get the utility to enable extensions
   from isaacsim.core.utils.extensions import enable_extension

   # Enable the layers and stage windows in the UI
   enable_extension("omni.kit.widget.stage")
   enable_extension("omni.kit.widget.layers")

   simulation_app.update()
   ```

## Standalone Example Scripts

### Time Stepping

This sample shows how to start an Omniverse Kit Python app and then create callbacks which get called each rendering frame and each physics timestep. It also shows the different ways to step physics and rendering.

The sample can be executed by running the following:

```python
./python.sh standalone_examples/deprecated/api/isaacsim.core.api/time_stepping.py
```

### Load USD Stage

This sample demonstrates how to load a USD stage and start simulating it.

The sample can be executed by running the following, specify `usd_path` to a location on your nucleus server:

```python
./python.sh standalone_examples/api/isaacsim.simulation_app/load_stage.py --usd_path /Isaac/Environments/Simple_Room/simple_room.usd
```

### URDF Import

This sample demonstrates how to use the URDF Python API, configure its physics and then simulate it for a fixed number of frames.

The sample can be executed by running the following:

```python
./python.sh standalone_examples/api/isaacsim.asset.importer.urdf/urdf_import.py
```

### Change Resolution

This sample demonstrates how to change the resolution of the viewport at runtime.

The sample can be executed by running the following:

```python
./python.sh standalone_examples/api/isaacsim.simulation_app/change_resolution.py
```

### Convert Assets to USD

This sample demonstrates how to batch convert OBJ/STL/FBX assets to USD.

To execute it with sample data, run the following:

```python
./python.sh standalone_examples/api/omni.kit.asset_converter/asset_usd_converter.py --folders standalone_examples/data/cube standalone_examples/data/torus
```

The input folders containing OBJ/STL/FBX assets are specified as argument
and it will output in terminal the path to converted USD files.

```python
Converting folder standalone_examples/data/cube...
---Added standalone_examples/data/cube_converted/cube_fbx.usd

Converting folder standalone_examples/data/torus...
---Added standalone_examples/data/torus_converted/torus_stl.usd
```

This sample leverages Python APIs from the [Asset Importer](https://docs.omniverse.nvidia.com/extensions/latest/ext_asset-converter.html "(in Omniverse Extensions)") extension.

The details about the import options can be found [here](https://docs.omniverse.nvidia.com/extensions/latest/ext_asset-importer.html "(in Omniverse Extensions)").

### Livestream

This sample demonstrates how to enable livestreaming when running in native Python.

See [Isaac Sim WebRTC Streaming Client](../installation/manual_livestream_clients.html#isaac-sim-setup-livestream-webrtc) for more information on running the client.

```python
./python.sh standalone_examples/api/isaacsim.simulation_app/livestream.py
```

Note

* Running livestream.py will not have all of the default Isaac Sim extensions enabled. See [enabling additional extensions](#isaac-sim-python-additional-extensions) for more information.

On this page

* [Details: How `python.sh` works](#details-how-python-sh-works)
* [SimulationApp](#simulationapp)
  + [Usage Example:](#usage-example)
  + [Details: How `SimulationApp` works](#details-how-simulationapp-works)
  + [Enabling additional extensions](#enabling-additional-extensions)
* [Standalone Example Scripts](#standalone-example-scripts)
  + [Time Stepping](#time-stepping)
  + [Load USD Stage](#load-usd-stage)
  + [URDF Import](#urdf-import)
  + [Change Resolution](#change-resolution)
  + [Convert Assets to USD](#convert-assets-to-usd)
  + [Livestream](#livestream)