---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/py/source/extensions/isaacsim.core.experimental.utils/docs/index.html
title: "core.experimental.utils Docs"
section: "Core"
module: "05-python-api-quickref"
checksum: "09fc7fed699b604b"
fetched: "2026-06-21T14:14:27"
---

* [isaacsim.core.experimental.utils] Isaac Sim Core (Utils)

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# [isaacsim.core.experimental.utils] Isaac Sim Core (Utils)

**Version**: 0.17.1

## Overview

The isaacsim.core.experimental.utils extension provides a comprehensive set of utility functions for Isaac Sim applications. These utilities streamline common operations across application lifecycle management, USD stage manipulation, prim operations, geometric transformations, and backend switching, offering developers essential tools for building Isaac Sim applications efficiently.

### Functionality

#### Application Management

The extension provides comprehensive application lifecycle control through timeline operations, extension management, and update stepping. Users can programmatically control the timeline state with `play()`, `pause()`, and `stop()` functions, while also managing extension loading and querying extension information.

```python
import isaacsim.core.experimental.utils.app as app_utils

# Control timeline playback
app_utils.play()
app_utils.pause()
app_utils.stop()

# Step through application updates
app_utils.update_app(steps=10)

# Manage extensions
app_utils.enable_extension("omni.pip.cloud")
app_utils.is_extension_enabled("omni.pip.cloud")
```

#### Stage Operations

Stage management utilities handle USD file operations, prim creation and manipulation, and stage configuration. The extension supports creating new stages from templates, opening and saving USD files, and managing stage properties like units and coordinate systems.

```python
import isaacsim.core.experimental.utils.stage as stage_utils

# Create and manage stages
stage_utils.create_new_stage(template="sunlight")
stage_utils.open_stage("/path/to/file.usd")
stage_utils.save_stage("/path/to/output.usd")

# Define and manipulate prims
stage_utils.define_prim("/World/Cube", "Cube")
stage_utils.add_reference_to_stage("/path/to/asset.usd", "/World/Asset")
```

#### Prim Utilities

Comprehensive prim manipulation tools enable attribute management, API schema operations, and hierarchical searches. These utilities simplify working with USD prims by providing convenient functions for common operations.

```python
import isaacsim.core.experimental.utils.prim as prim_utils

# Work with prim attributes
value = prim_utils.get_prim_attribute_value("/World/Cube", "size")
attributes = prim_utils.get_prim_attribute_names("/World/Cube")

# Find prims with predicates
matching_prims = prim_utils.get_all_matching_child_prims(
    "/World",
    predicate=lambda prim, path: prim.GetTypeName() == "Cube"
)
```

#### Transform Operations

Mathematical transformation utilities support conversion between rotation representations, quaternion operations, and coordinate system transformations. These functions work with various input formats including lists, NumPy arrays, and Warp arrays.

```python
import isaacsim.core.experimental.utils.transform as transform_utils

# Convert between rotation representations
rotation_matrix = transform_utils.euler_angles_to_rotation_matrix([0, np.pi/2, 0])
quaternion = transform_utils.euler_angles_to_quaternion([0, np.pi/2, 0])

# Perform quaternion operations
result = transform_utils.quaternion_multiplication(quat1, quat2)
conjugate = transform_utils.quaternion_conjugate(quaternion)

# Compute relative transform between two world matrices
relative = transform_utils.compute_relative_transform(source_to_world, target_to_world)

# Compute camera look-at transform
matrix = transform_utils.look_at_matrix(eye=[5.0, 5.0, 5.0], target=[0.0, 0.0, 0.0])
```

The `look_at_matrix` function computes the `Gf.Matrix4d` camera transform (position + orientation) that places a camera at a given eye position oriented toward a target. It accepts lists, NumPy arrays, or `Gf.Vec3d` and automatically selects a fallback up vector when the forward direction is collinear with the specified up axis. The batched `look_at_quaternion` variant returns a Warp array quaternion and supports batched inputs for multi-camera workflows.

#### Pose Manipulation

Spatial transformation utilities provide local and world pose operations for prims. These functions support getting and setting both local and world coordinates with automatic coordinate system handling.

```python
import isaacsim.core.experimental.utils.xform as xform_utils

# Get and set poses
translation, orientation = xform_utils.get_local_pose("/World/Cube")
world_translation, world_orientation = xform_utils.get_world_pose("/World/Cube")

# Set poses (USDRT/Fabric backends)
xform_utils.set_local_pose("/World/Cube", translation=[1, 2, 3])
xform_utils.set_world_pose("/World/Cube", position=[5, 6, 7])

# Compute relative transform between two prims
relative_tf = xform_utils.get_relative_transform("/World/Source", "/World/Target")
```

### Key Components

#### Backend System

The backend system enables switching between USD, USDRT, and Fabric processing backends through context managers. This allows applications to choose the optimal backend for specific operations.

```python
import isaacsim.core.experimental.utils.backend as backend_utils

# Switch processing backends
with backend_utils.use_backend("usdrt"):
    # Operations use USDRT backend
    pass
```

#### Data Operations

Array and data manipulation utilities provide consistent interfaces for working with Python primitives, NumPy arrays, and Warp arrays. These utilities handle device placement, type conversion, and broadcasting operations.

```python
import isaacsim.core.experimental.utils.ops as ops_utils

# Convert and place data
array = ops_utils.place([1, 2, 3], device="cuda", dtype=wp.float32)
indices = ops_utils.resolve_indices([0, 1, 2], device="cpu")
broadcasted = ops_utils.broadcast_to(5.0, shape=(3, 3))
```

#### Semantic Labeling

Semantic utilities manage taxonomies and labels on USD prims, supporting multiple classification schemes for organizing and querying scene content.

```python
import isaacsim.core.experimental.utils.semantics as semantics_utils

# Manage semantic labels
semantics_utils.add_labels("/World/Cube", labels=["furniture", "wooden"])
labels = semantics_utils.get_labels("/World/Cube")
semantics_utils.remove_labels("/World/Cube", labels=["wooden"])
```

### Integration

The extension integrates with the broader Isaac Sim ecosystem through its dependencies. It uses **omni.usd** for USD operations, **omni.warp.core** for array processing, and **omni.kit.stage\_templates** for stage creation templates. The utilities serve as building blocks for higher-level Isaac Sim functionality while maintaining compatibility across different processing backends.

## Enable Extension

The extension can be enabled (if not already) in one of the following ways:

Command-line interface

Define the next entry as an application argument from a terminal.

```python
APP_SCRIPT.(sh|bat) --enable isaacsim.core.experimental.utils
```

Experience/extension configuration

Define the next entry under `[dependencies]` in an experience (`.kit`) file or an extension configuration (`extension.toml`) file.

```python
[dependencies]
"isaacsim.core.experimental.utils" = {}
```

Extension Manager UI

Open the *Window > Extensions* menu in a running application instance and search for `isaacsim.core.experimental.utils`.
Then, toggle the enable control button if it is not already active.

## Python API

Warning

**The API featured in this extension is experimental and subject to change without deprecation cycles.**
Although we will try to maintain backward compatibility in the event of a change, it may not always be possible.

The following table summarizes the available modules.

|  |  |
| --- | --- |
| [`app`](#module-isaacsim.core.experimental.utils.impl.app "isaacsim.core.experimental.utils.impl.app") | Functions for interacting with the application and its available extensions. |
| [`backend`](#module-isaacsim.core.experimental.utils.impl.backend "isaacsim.core.experimental.utils.impl.backend") | Functions for selecting and managing the supported simulation backends. |
| [`foundation`](#module-isaacsim.core.experimental.utils.impl.foundation "isaacsim.core.experimental.utils.impl.foundation") | Functions for working with USD/USDRT foundations, e.g.: Scene Description Foundations (Sdf), Graphics Foundations (Gf). |
| [`ops`](#module-isaacsim.core.experimental.utils.impl.ops "isaacsim.core.experimental.utils.impl.ops") | Functions for manipulating and performing operations on Warp arrays and other types. |
| [`prim`](#module-isaacsim.core.experimental.utils.impl.prim "isaacsim.core.experimental.utils.impl.prim") | Functions for working with USD/USDRT prims. |
| [`semantics`](#module-isaacsim.core.experimental.utils.impl.semantics "isaacsim.core.experimental.utils.impl.semantics") | Functions for creating, accessing and deleting semantic labels. |
| [`stage`](#module-isaacsim.core.experimental.utils.impl.stage "isaacsim.core.experimental.utils.impl.stage") | Functions for working with USD/USDRT stages. |
| [`transform`](#module-isaacsim.core.experimental.utils.impl.transform "isaacsim.core.experimental.utils.impl.transform") | Functions for performing transform operations. |
| [`xform`](#module-isaacsim.core.experimental.utils.impl.xform "isaacsim.core.experimental.utils.impl.xform") | Functions for performing transform operations on Xformable USD/USDRT prims. |

### App Utils

Functions for interacting with the application and its available extensions.

enable\_extension(*name: str*, *\**, *enabled: bool = True*) → bool
:   Enable/disable an extension from the extension manager.

    Parameters:
    :   * **name** – Name of the extension.
        * **enabled** – Whether the extension should be enabled.

    Returns:
    :   Whether the extension was enabled/disabled successfully.

    Example:

    ```python
    >>> import isaacsim.core.experimental.utils.app as app_utils
    >>>
    >>> # enable the 'omni.pip.cloud' extension
    >>> app_utils.enable_extension("omni.pip.cloud")
    True
    >>>
    >>> # disable the 'omni.pip.cloud' extension
    >>> app_utils.enable_extension("omni.pip.cloud", enabled=False)
    True
    ```

get\_extension\_dict(*name: str*) → dict | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None")
:   Get the extension configuration (`extension.toml` file) as a Python dictionary.

    Parameters:
    :   **name** – Name/ID of the extension.

    Returns:
    :   Configuration dictionary, or `None` if the extension is not enabled/found.

    Example:

    ```python
    >>> import isaacsim.core.experimental.utils.app as app_utils
    >>>
    >>> # get the configuration dictionary of the 'omni.pip.cloud' extension
    >>> app_utils.enable_extension("omni.pip.cloud")  
    >>> app_utils.get_extension_dict("omni.pip.cloud")  
    {
        'name': 'omni.pip.cloud',
        'package': {
            'version': '4.2.0',
            'description': "...",
        },
        ...
    }
    ```

get\_extension\_id(*name: str*) → str | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None")
:   Get the ID of an extension.

    Parameters:
    :   **name** – Name/ID of the extension.

    Returns:
    :   Extension ID (name-version) or `None` if the extension is not enabled/found.

    Example:

    ```python
    >>> import isaacsim.core.experimental.utils.app as app_utils
    >>>
    >>> # get the id of the 'omni.pip.cloud' extension
    >>> app_utils.enable_extension("omni.pip.cloud")  
    >>> app_utils.get_extension_id("omni.pip.cloud")  
    'omni.pip.cloud-4.2.0'
    ```

get\_extension\_path(*name: str*) → str
:   Get the path of an extension.

    Parameters:
    :   **name** – Name/ID of the extension.

    Returns:
    :   Path of the extension root directory.

    Example:

    ```python
    >>> import isaacsim.core.experimental.utils.app as app_utils
    >>>
    >>> # get the path of the 'omni.pip.cloud' extension
    >>> app_utils.enable_extension("omni.pip.cloud")  
    >>> app_utils.get_extension_path("omni.pip.cloud")  
    '.../exts/omni.pip.cloud'
    ```

is\_extension\_enabled(*name: str*) → bool
:   Check if an extension is enabled.

    Parameters:
    :   **name** – Name of the extension.

    Returns:
    :   Whether the extension is enabled.

    Example:

    ```python
    >>> import isaacsim.core.experimental.utils.app as app_utils
    >>>
    >>> # check if the 'omni.pip.cloud' extension is enabled
    >>> app_utils.enable_extension("omni.pip.cloud", enabled=False)  
    >>> app_utils.is_extension_enabled("omni.pip.cloud")
    False
    ```

is\_paused() → bool
:   Check if the application timeline is paused.

    Returns:
    :   Whether the application timeline is paused.

    Example:

    ```python
    >>> import isaacsim.core.experimental.utils.app as app_utils
    >>>
    >>> app_utils.is_paused()
    False
    ```

is\_playing() → bool
:   Check if the application timeline is playing.

    Returns:
    :   Whether the application timeline is playing.

    Example:

    ```python
    >>> import isaacsim.core.experimental.utils.app as app_utils
    >>>
    >>> app_utils.is_playing()
    False
    ```

is\_stopped() → bool
:   Check if the application timeline is stopped.

    Returns:
    :   Whether the application timeline is stopped.

    Example:

    ```python
    >>> import isaacsim.core.experimental.utils.app as app_utils
    >>>
    >>> app_utils.is_stopped()
    True
    ```

pause(*\**, *commit: bool | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = True*) → [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None")
:   Pause the application timeline.

    Note

    After committing the timeline state (silently or not), the new value will be available immediately
    when querying it (e.g.: via [`is_paused()`](#isaacsim.core.experimental.utils.impl.app.is_paused "isaacsim.core.experimental.utils.impl.app.is_paused")). Otherwise, one app update step is required to reflect
    the new state and trigger any registered callback.

    Parameters:
    :   **commit** –

        Whether to commit the “pause” state. The following values are supported:

        * `True`: Commit the state and trigger callbacks.
        * `False`: Do not commit the state.
        * `None`: Commit the state silently (without triggering callbacks).

    Example:

    ```python
    >>> import isaacsim.core.experimental.utils.app as app_utils
    >>>
    >>> app_utils.pause()
    ```

play(*\**, *commit: bool | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = True*) → [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None")
:   Play the application timeline.

    Note

    After committing the timeline state (silently or not), the new value will be available immediately
    when querying it (e.g.: via [`is_playing()`](#isaacsim.core.experimental.utils.impl.app.is_playing "isaacsim.core.experimental.utils.impl.app.is_playing")). Otherwise, one app update step is required to reflect
    the new state and trigger any registered callback.

    Parameters:
    :   **commit** –

        Whether to commit the “play” state. The following values are supported:

        * `True`: Commit the state and trigger callbacks.
        * `False`: Do not commit the state.
        * `None`: Commit the state silently (without triggering callbacks).

    Example:

    ```python
    >>> import isaacsim.core.experimental.utils.app as app_utils
    >>>
    >>> app_utils.play()
    ```

stop(*\**, *commit: bool | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = True*) → [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None")
:   Stop the application timeline.

    Note

    After committing the timeline state (silently or not), the new value will be available immediately
    when querying it (e.g.: via [`is_stopped()`](#isaacsim.core.experimental.utils.impl.app.is_stopped "isaacsim.core.experimental.utils.impl.app.is_stopped")). Otherwise, one app update step is required to reflect
    the new state and trigger any registered callback.

    Parameters:
    :   **commit** –

        Whether to commit the “stop” state. The following values are supported:

        * `True`: Commit the state and trigger callbacks.
        * `False`: Do not commit the state.
        * `None`: Commit the state silently (without triggering callbacks).

    Example:

    ```python
    >>> import isaacsim.core.experimental.utils.app as app_utils
    >>>
    >>> app_utils.stop()
    ```

update\_app( : *\**, : *steps: int = 1*, : *callback: Callable[[int, int], bool | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None")] | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, ) → [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None")
:   Perform one or more update steps of the application.

    Parameters:
    :   * **steps** – Number of update steps to perform.
        * **callback** – Optional callback function to call after each update step.
          The function should take two arguments: the current step number and the total number of steps.
          If no return value is provided, the update loop will run for the specified number of steps.
          However, if the function returns `False`, no more update steps will be performed.

    Example:

    ```python
    >>> import isaacsim.core.experimental.utils.app as app_utils
    >>>
    >>> # perform one update step
    >>> app_utils.update_app()  
    >>>
    >>> # perform 10 update steps
    >>> app_utils.update_app(steps=10)  
    >>>
    >>> # perform 10 update steps with a callback
    >>> def callback(step, steps):
    ...     print(f"update step {step}/{steps}")
    ...     return step < 3  # stop after 3 steps (return False to break the loop)
    ...
    >>> app_utils.update_app(steps=10, callback=callback)  
    update step 1/10
    update step 2/10
    update step 3/10
    ```

*async* update\_app\_async( : *\**, : *steps: int = 1*, : *callback: Callable[[int, int], bool | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None")] | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, ) → [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None")
:   Perform one or more update steps of the application.

    This function is the asynchronous version of [`update_app()`](#isaacsim.core.experimental.utils.impl.app.update_app "isaacsim.core.experimental.utils.impl.app.update_app").

    Parameters:
    :   * **steps** – Number of update steps to perform.
        * **callback** – Optional callback function to call after each update step.
          The function should take two arguments: the current step number and the total number of steps.
          If no return value is provided, the update loop will run for the specified number of steps.
          However, if the function returns `False`, no more update steps will be performed.

    Example:

    ```python
    >>> import asyncio
    >>> import isaacsim.core.experimental.utils.app as app_utils
    >>> from omni.kit.async_engine import run_coroutine
    >>>
    >>> async def task():
    ...     await app_utils.update_app_async()
    ...
    >>> run_coroutine(task())
    ```

### Backend Utils

Functions for selecting and managing the supported simulation backends.

*class* SimStateMode( : *value*, : *names=<not given>*, : *\*values*, : *module=None*, : *qualname=None*, : *type=None*, : *start=1*, : *boundary=None*, )
:   Mode for SimState backend integration with articulation data.

    DISABLED *= 'disabled'*
    :   SimState is not used; existing backend selection applies (default).

    EXCLUSIVE *= 'exclusive'*
    :   SimState replaces the normal backend; data only goes to SimStateStorage.

    MIRROR *= 'mirror'*
    :   SimState runs in parallel; data goes to both SimStateStorage AND the normal backend.

get\_current\_backend( : *supported\_backends: list[str]*, : *\**, : *raise\_on\_unsupported: bool | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, ) → str
:   Get the current backend value if it exists.

    Parameters:
    :   * **supported\_backends** – The list of supported backends.
        * **raise\_on\_unsupported** – Whether to raise an error if the backend is not supported when requested.
          If set to a value other than `None`, this parameter has precedence over the context value.

    Returns:
    :   The current backend value or the default value (first supported backend) if no backend is active.

get\_simstate\_mode() → [SimStateMode](#isaacsim.core.experimental.utils.impl.backend.SimStateMode "isaacsim.core.experimental.utils.impl.backend.SimStateMode")
:   Get the current SimState mode from context manager or application settings.

    The mode is determined using the following priority:

    1. **Context manager override**: If `use_backend("simstate")` is active,
       EXCLUSIVE mode is used regardless of the application setting.
       This allows programmatic control for specific code blocks.
    2. **Application setting**: Otherwise, the `/isaacsim/articulation/simStateMode`
       setting is used. Valid values are `"disabled"`, `"exclusive"`, and `"mirror"`.
    3. **Default**: If the setting is not configured or invalid, DISABLED is used,
       which preserves the original tensor/usd backend behavior.

    Returns:
    :   The current SimState mode.

    Example:

    ```python
    >>> import isaacsim.core.experimental.utils.backend as backend_utils
    >>>
    >>> # Check the current mode (from setting)
    >>> mode = backend_utils.get_simstate_mode()
    >>> if mode == backend_utils.SimStateMode.MIRROR:
    ...     print("SimState is running in mirror mode")
    >>>
    >>> # Override with context manager for a specific block
    >>> with backend_utils.use_backend("simstate"):
    ...     # Forces EXCLUSIVE mode, regardless of the setting
    ...     pass
    ```

is\_backend\_set() → bool
:   Check if a backend is set in the context.

    Returns:
    :   Whether a backend is set in the context.

should\_raise\_on\_fallback() → bool
:   Check whether an exception should be raised, depending on the context’s raise on fallback state.

    Returns:
    :   Whether an exception should be raised on fallback backend.

should\_raise\_on\_unsupported() → bool
:   Check whether an exception should be raised, depending on the context’s raise on unsupported state.

    Returns:
    :   Whether an exception should be raised on unsupported backend.

use\_backend( : *backend: Literal['usd', 'usdrt', 'fabric', 'tensor', 'simstate']*, : *\**, : *raise\_on\_unsupported: bool = False*, : *raise\_on\_fallback: bool = False*, ) → Generator[[None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None"), [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None"), [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None")]
:   Context manager that sets a thread-local backend value.

    Warning

    The usdrt and fabric backends require Fabric Scene Delegate (FSD) to be enabled.
    FSD can be enabled in *apps/.kit* experience files by setting `app.useFabricSceneDelegate = true`.

    Parameters:
    :   * **backend** – The value to set in the context.
        * **raise\_on\_unsupported** – Whether to raise an exception if the backend is not supported when requested.
        * **raise\_on\_fallback** – Whether to raise an exception if the backend is supported,
          but a fallback is being used at a particular point in time when requested.

    Raises:
    :   **RuntimeError** – If the `usdrt` or `fabric` backend is specified but Fabric Scene Delegate (FSD) is disabled.

    Example:

    ```python
    >>> import isaacsim.core.experimental.utils.backend as backend_utils
    >>>
    >>> with backend_utils.use_backend("usdrt"):
    ...    # operate on the specified backend
    ...    pass
    >>> # operate on the default backend
    ```

### Foundation Utils

Functions for working with USD/USDRT foundations, e.g.: Scene Description Foundations (Sdf), Graphics Foundations (Gf).

get\_value\_type\_names( : *\**, : *format: Literal[str*, : *Sdf.ValueTypeNames*, : *usdrt.Sdf.ValueTypeNames] = <class 'str'>*, ) → list[str | Sdf.ValueTypeName | usdrt.Sdf.ValueTypeName]
:   Get all supported (from Isaac Sim’s Core API perspective) value type names.

    Parameters:
    :   **format** – Format to get the value type names in.

    Returns:
    :   List of value type names.

    Raises:
    :   **ValueError** – If the format is invalid.

    Example:

    ```python
    >>> import isaacsim.core.experimental.utils.foundation as foundation_utils
    >>> import usdrt
    >>> from pxr import Sdf
    >>>
    >>> foundation_utils.get_value_type_names(format=str)
    ['asset', 'asset[]', 'bool', 'bool[]', 'color3d', ...]
    >>> foundation_utils.get_value_type_names(format=Sdf.ValueTypeNames)
    [<pxr.Sdf.ValueTypeName object at 0x...>, <pxr.Sdf.ValueTypeName object at 0x...>, ...]
    >>> foundation_utils.get_value_type_names(format=usdrt.Sdf.ValueTypeNames)
    [Sdf.ValueTypeName('asset'), Sdf.ValueTypeName('asset[]'), Sdf.ValueTypeName('bool'), ...]
    ```

resolve\_value\_type\_name( : *type\_name: str | Sdf.ValueTypeName | usdrt.Sdf.ValueTypeName*, : *\**, : *backend: str | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, ) → Sdf.ValueTypeName | usdrt.Sdf.ValueTypeName
:   Resolve the value type name for a given (value) type name according to the USD/USDRT specifications.

    Backends: usd, usdrt, fabric.

    Parameters:
    :   * **type\_name** – Type name.
        * **backend** – Backend to use to get the value type name. If not `None`, it has precedence over the current backend
          set via the [`use_backend()`](#isaacsim.core.experimental.utils.impl.backend.use_backend "isaacsim.core.experimental.utils.impl.backend.use_backend") context manager.

    Returns:
    :   Value type name instance.

    Raises:
    :   * **ValueError** – If the backend is not supported.
        * **ValueError** – If the type name is invalid.

    Example:

    ```python
    >>> import isaacsim.core.experimental.utils.foundation as foundation_utils
    >>>
    >>> foundation_utils.resolve_value_type_name("color3f", backend="usd")
    <pxr.Sdf.ValueTypeName object at 0x...>
    >>> foundation_utils.resolve_value_type_name("color3f", backend="usdrt")
    Sdf.ValueTypeName('float3 (color)')
    ```

value\_type\_name\_to\_str( : *type\_name: str | Sdf.ValueTypeName | usdrt.Sdf.ValueTypeName*, ) → str
:   Get the string representation of a given value type name.

    Parameters:
    :   **type\_name** – Value type name.

    Returns:
    :   String representation of the value type name.

    Raises:
    :   **ValueError** – If the type name is invalid.

    Example:

    ```python
    >>> import isaacsim.core.experimental.utils.foundation as foundation_utils
    >>> import usdrt
    >>> from pxr import Sdf
    >>>
    >>> foundation_utils.value_type_name_to_str("color3f[]")
    'color3f[]'
    >>> foundation_utils.value_type_name_to_str(Sdf.ValueTypeNames.Color3fArray)
    'color3f[]'
    >>> foundation_utils.value_type_name_to_str(usdrt.Sdf.ValueTypeNames.Color3fArray)
    'color3f[]'
    ```

### Ops Utils

Functions for manipulating and performing operations on Warp arrays and other types.

broadcast\_to( : *x: bool | int | float | list | np.ndarray | wp.array*, : *\**, : *shape: list[int]*, : *dtype: type | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *device: str | wp.Device | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, ) → wp.array
:   Broadcast a Python primitive or list, a NumPy array, or a Warp array to a Warp array with a new shape.

    Note

    Broadcasting follows NumPy’s rules: Two shapes are compatible if by comparing their dimensions element-wise,
    starting with the trailing dimension (i.e., rightmost) and moving leftward

    * they are equal, or
    * one of them is 1.

    Parameters:
    :   * **x** – Python primitive or list, NumPy array, or Warp array.
        * **shape** – Shape of the desired array.
        * **dtype** – Data type of the output array. If `None`, the data type of the input is used.
        * **device** – Device to place the output array on. If `None`, the default device is used,
          unless the input is a Warp array (in which case the input device is used).

    Returns:
    :   Warp array with the given shape.

    Raises:
    :   * **ValueError** – If the input list or array is not compatible with the new shape according to the broadcasting rules.
        * **TypeError** – If the input argument `x` is not a supported data container.

    Example:

    ```python
    >>> import isaacsim.core.experimental.utils.ops as ops_utils
    >>> import numpy as np
    >>> import warp as wp
    >>>
    >>> # Python primitive
    >>> # - bool
    >>> array = ops_utils.broadcast_to(True, shape=(1, 3))  
    >>> print(array)
    [[ True  True  True]]
    >>> # - int
    >>> array = ops_utils.broadcast_to(2, shape=(1, 3))  
    >>> print(array)
    [[2 2 2]]
    >>> # - float
    >>> array = ops_utils.broadcast_to(3.0, shape=(1, 3))  
    >>> print(array)
    [[3. 3. 3.]]
    >>>
    >>> # Python list
    >>> array = ops_utils.broadcast_to([1, 2, 3], shape=(1, 3))  
    >>> print(array)
    [[1 2 3]]
    >>>
    >>> # NumPy array (with shape (1, 3))
    >>> array = ops_utils.broadcast_to(np.array([[1, 2, 3]]), shape=(2, 3))  
    >>> print(array)
    [[1 2 3]
     [1 2 3]]
    >>>
    >>> # Warp array (with different device)
    >>> array = ops_utils.broadcast_to(wp.array([1, 2, 3], device="cpu"), shape=(3, 3), device="cuda")  
    >>> print(array)
    [[1 2 3]
     [1 2 3]
     [1 2 3]]
    ```

parse\_device( : *device: str | wp.Device | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None")*, : *\**, : *raise\_on\_invalid: bool = False*, ) → wp.Device
:   Parse the input device and return a Warp `Device` instance.

    Parameters:
    :   * **device** – Device specification. If the specified device is `None` or it cannot be resolved,
          the default available device will be returned instead.
        * **raise\_on\_invalid** – Whether to raise an exception if the device is invalid.
          If `False`, a warning is logged and the default available device is returned instead.

    Returns:
    :   Warp Device.

    Raises:
    :   **ValueError** – If the input device is invalid and `raise_on_invalid` is `True`.

    Example:

    ```python
    >>> import isaacsim.core.experimental.utils.ops as ops_utils
    >>>
    >>> device = ops_utils.parse_device("cpu")
    >>> print(type(device), device)
    <class 'warp._src.context.Device'> cpu
    >>> device = ops_utils.parse_device("cuda")
    >>> print(type(device), device)
    <class 'warp._src.context.Device'> cuda:0
    >>> device = ops_utils.parse_device("cuda:0")
    >>> print(type(device), device)
    <class 'warp._src.context.Device'> cuda:0
    ```

place( : *x: bool | int | float | list | np.ndarray | wp.array*, : *\**, : *dtype: type | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *device: str | wp.Device | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, ) → wp.array
:   Create a Warp array from a Python primitive or list, a NumPy array, or a Warp array.

    Parameters:
    :   * **x** – Python primitive or list, NumPy array, or Warp array.
          If the input is a Warp array with the same device and dtype, it is returned as is.
        * **dtype** – Data type of the output array. If not provided, the data type of the input is used.
        * **device** – Device to place the output array on. If `None`, the default device is used,
          unless the input is a Warp array (in which case the input device is used).

    Returns:
    :   Warp array instance.

    Raises:
    :   **TypeError** – If the input argument `x` is not a supported data container.

    Example:

    ```python
    >>> import isaacsim.core.experimental.utils.ops as ops_utils
    >>> import numpy as np
    >>> import warp as wp
    >>>
    >>> # Python primitive
    >>> # - bool
    >>> array = ops_utils.place(True, device="cpu")  
    >>> print(array, array.dtype, array.device, array.shape)
    [ True] <class 'warp._src.types.bool'> cpu (1,)
    >>> # - int
    >>> array = ops_utils.place(1, device="cpu")  
    >>> print(array, array.dtype, array.device, array.shape)
    [1] <class 'warp._src.types.int64'> cpu (1,)
    >>> # - float
    >>> array = ops_utils.place(1.0, device="cpu")  
    >>> print(array, array.dtype, array.device, array.shape)
    [1.] <class 'warp._src.types.float64'> cpu (1,)
    >>>
    >>> # Python list
    >>> array = ops_utils.place([1.0, 2.0, 3.0], device="cpu")  
    >>> print(array, array.dtype, array.device, array.shape)
    [1. 2. 3.] <class 'warp._src.types.float64'> cpu (3,)
    >>>
    >>> # NumPy array (with shape (3, 1))
    >>> array = ops_utils.place(np.array([[1], [2], [3]], dtype=np.uint8), dtype=wp.float32)  
    >>> print(array, array.dtype, array.device, array.shape)
    [[1.] [2.] [3.]] <class 'warp._src.types.float32'> cuda:0 (3, 1)
    >>>
    >>> # Warp array (with different device)
    >>> array = ops_utils.place(wp.array([1.0, 2.0, 3.0], device="cpu"), device="cuda")  
    >>> print(array, array.dtype, array.device, array.shape)
    [1. 2. 3.] <class 'warp._src.types.float64'> cuda:0 (3,)
    ```

resolve\_indices( : *x: bool | int | float | list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None")*, : *\**, : *count: int | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *dtype: type | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = warp.int32*, : *device: str | wp.Device | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, ) → wp.array
:   Create a flattened (1D) Warp array to be used as indices from a Python primitive or list, a NumPy array, or a Warp array.

    Parameters:
    :   * **x** – Python primitive or list, NumPy array, or Warp array.
        * **count** – Number of indices to resolve.
          If input argument `x` is `None`, the indices are generated from 0 to `count - 1`.
          If input argument `x` is not `None`, this value is ignored.
        * **dtype** – Data type of the output array. If `None`, `wp.int32` is used.
        * **device** – Device to place the output array on. If `None`, the default device is used,
          unless the input is a Warp array (in which case the input device is used).

    Returns:
    :   Flattened (1D) Warp array instance.

    Raises:
    :   * **ValueError** – If input argument `x` is `None` and `count` is not provided.
        * **TypeError** – If the input argument `x` is not a supported data container.

    Example:

    ```python
    >>> import isaacsim.core.experimental.utils.ops as ops_utils
    >>> import numpy as np
    >>> import warp as wp
    >>>
    >>> # Python primitive
    >>> # - bool
    >>> indices = ops_utils.resolve_indices(True, device="cpu")  
    >>> print(indices, indices.dtype, indices.device, indices.shape)
    [1] <class 'warp._src.types.int32'> cpu (1,)
    >>> # - int
    >>> indices = ops_utils.resolve_indices(2, device="cpu")  
    >>> print(indices, indices.dtype, indices.device, indices.shape)
    [2] <class 'warp._src.types.int32'> cpu (1,)
    >>> # - float
    >>> indices = ops_utils.resolve_indices(3.0, device="cpu")  
    >>> print(indices, indices.dtype, indices.device, indices.shape)
    [3] <class 'warp._src.types.int32'> cpu (1,)
    >>>
    >>> # Python list
    >>> indices = ops_utils.resolve_indices([1, 2, 3], device="cpu")  
    >>> print(indices, indices.dtype, indices.device, indices.shape)
    [1 2 3] <class 'warp._src.types.int32'> cpu (3,)
    >>>
    >>> # NumPy array (with shape (3, 1))
    >>> indices = ops_utils.resolve_indices(np.array([[1], [2], [3]], dtype=np.uint8))  
    >>> print(indices, indices.dtype, indices.device, indices.shape)
    [1 2 3] <class 'warp._src.types.int32'> cuda:0 (3,)
    >>>
    >>> # Warp array (with different device)
    >>> indices = ops_utils.resolve_indices(wp.array([1, 2, 3], device="cpu"), device="cuda")  
    >>> print(indices, indices.dtype, indices.device, indices.shape)
    [1 2 3] <class 'warp._src.types.int32'> cuda:0 (3,)
    ```

### Prim Utils

Functions for working with USD/USDRT prims.

create\_prim\_attribute( : *prim: str | Usd.Prim | usdrt.Usd.Prim*, : *\**, : *name: str*, : *type\_name: Sdf.ValueTypeName | usdrt.Sdf.ValueTypeName*, : *exist\_ok: bool = True*, ) → Usd.Attribute | usdrt.Usd.Attribute
:   Create a new attribute on a USD prim.

    Backends: usd, usdrt, fabric.

    Parameters:
    :   * **prim** – Prim path or prim instance.
        * **name** – Name of the attribute to create.
        * **type\_name** – Type of the attribute to create.
        * **exist\_ok** – Whether to do not raise an error if the attribute already exists.

    Returns:
    :   Created attribute, or the existing attribute if it already exists (and `exist_ok` is `True`).

    Raises:
    :   * **RuntimeError** – If the attribute already exists and `exist_ok` is `False`.
        * **ValueError** – If the attribute already exists with a different type name (and `exist_ok` is `True`).

ensure\_api( : *prim: str | Usd.Prim*, : *api: type*, : *\*args: Any*, : *\*\*kwargs: Any*, ) → Any
:   Ensure that a prim has the specified API schema applied.

    Backends: usd.

    If a prim doesn’t have the API schema, it will be applied.
    If it already has it, the existing API schema will be returned.

    Parameters:
    :   * **prim** – Prim path or prim instance.
        * **api** – The API schema type to ensure.
        * **\*args** – Additional positional arguments passed to API schema when applying it.
        * **\*\*kwargs** – Additional keyword arguments passed to API schema when applying it.

    Returns:
    :   API schema object.

    Example:

    ```python
    >>> import isaacsim.core.experimental.utils.prim as prim_utils
    >>> import isaacsim.core.experimental.utils.stage as stage_utils
    >>> from pxr import UsdLux
    >>>
    >>> prim = stage_utils.define_prim("/World/Light", "Xform")
    >>> prim_utils.ensure_api(prim, UsdLux.LightAPI)
    UsdLux.LightAPI(Usd.Prim(</World/Light>))
    ```

find\_matching\_prim\_paths( : *path: str*, : *\**, : *traverse: bool = False*, ) → list[str]
:   Find all the prim paths in the stage that match the given (regex) path.

    Backends: usd, usdrt, fabric.

    Parameters:
    :   * **path** – Path to match against the stage. It can be a regex expression or a valid prim path.
        * **traverse** – Whether to traverse the stage hierarchy to find all matching prims. If `True`, the function will
          return all the prim paths in the stage that match the given (regex) path, including its descendants, if any.
          Otherwise, only the paths of the first matching prim (performing a segment-wise search) will be returned.

    Returns:
    :   List of matching prim paths.

    Example:

    ```python
    >>> import isaacsim.core.experimental.utils.prim as prim_utils
    >>> import isaacsim.core.experimental.utils.stage as stage_utils
    >>>
    >>> # / (root prim)
    >>> #  |-- World
    >>> #  |    |-- prim_0
    >>> #  |    |    |-- prim_a
    >>> #  |    |    |-- prim_b
    >>> stage_utils.define_prim("/World/prim_0/prim_a")  
    >>> stage_utils.define_prim("/World/prim_0/prim_b")  
    >>>
    >>> prim_utils.find_matching_prim_paths("/World/prim_.*")
    ['/World/prim_0']
    >>> prim_utils.find_matching_prim_paths("/World/prim_.*", traverse=True)
    ['/World/prim_0', '/World/prim_0/prim_a', '/World/prim_0/prim_b']
    >>>
    >>> prim_utils.find_matching_prim_paths(".*_[ab]")
    []
    >>> prim_utils.find_matching_prim_paths(".*_[ab]", traverse=True)
    ['/World/prim_0/prim_a', '/World/prim_0/prim_b']
    ```

get\_all\_matching\_child\_prims( : *prim: str | Usd.Prim | usdrt.Usd.Prim*, : *\**, : *predicate: Callable[[Usd.Prim | usdrt.Usd.Prim, str], bool]*, : *include\_self: bool = False*, : *max\_depth: int | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, ) → list[Usd.Prim | usdrt.Usd.Prim]
:   Get all prim children of the given prim (excluding itself by default) that pass the predicate.

    Backends: usd, usdrt, fabric.

    Parameters:
    :   * **prim** – Prim path or prim instance.
        * **predicate** – Function to test the prims against.
          The function should take two positional arguments: a prim instance and its path.
          The function should return a boolean value indicating whether a prim passes the predicate.
        * **include\_self** – Whether to include the given prim in the search.
        * **max\_depth** – Maximum depth to search (current prim is at depth 0). If `None`, search till the end of the tree.

    Returns:
    :   List of matching prim children.

    Raises:
    :   **ValueError** – If `max_depth` is defined and is less than 0.

    Example:

    ```python
    >>> import isaacsim.core.experimental.utils.prim as prim_utils
    >>> import isaacsim.core.experimental.utils.stage as stage_utils
    >>>
    >>> # define some prims
    >>> stage_utils.define_prim("/World/Cube_0", "Cube")  
    >>> stage_utils.define_prim("/World/Cube_0/Cube_1", "Cube")  
    >>>
    >>> # get all `/World`'s child prims of type Cube
    >>> predicate = lambda prim, path: prim.GetTypeName() == "Cube"
    >>> prim_utils.get_all_matching_child_prims("/World", predicate=predicate)
    [Usd.Prim(</World/Cube_0>), Usd.Prim(</World/Cube_0/Cube_1>)]
    >>>
    >>> # get all `/World`'s child prims of type Cube with max depth 1
    >>> prim_utils.get_all_matching_child_prims("/World", predicate=predicate, max_depth=1)
    [Usd.Prim(</World/Cube_0>)]
    ```

get\_first\_matching\_child\_prim( : *prim: str | Usd.Prim | usdrt.Usd.Prim*, : *\**, : *predicate: Callable[[Usd.Prim | usdrt.Usd.Prim, str], bool]*, : *include\_self: bool = False*, ) → Usd.Prim | usdrt.Usd.Prim | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None")
:   Get the first prim child of the given prim (excluding itself by default) that passes the predicate.

    Backends: usd, usdrt, fabric.

    Parameters:
    :   * **prim** – Prim path or prim instance.
        * **predicate** – Function to test the prims against.
          The function should take two positional arguments: a prim instance and its path.
          The function should return a boolean value indicating whether a prim passes the predicate.
        * **include\_self** – Whether to include the given prim in the search.

    Returns:
    :   First prim child or `None` if no prim child passes the predicate.

    Example:

    ```python
    >>> import isaacsim.core.experimental.utils.prim as prim_utils
    >>> import isaacsim.core.experimental.utils.stage as stage_utils
    >>>
    >>> # define some prims
    >>> stage_utils.define_prim("/World/Cube", "Cube")  
    >>> stage_utils.define_prim("/World/Cylinder", "Cylinder")  
    >>> stage_utils.define_prim("/World/Sphere", "Sphere")  
    >>>
    >>> # get the first `/World`'s child prim of type Sphere
    >>> predicate = lambda prim, path: prim.GetTypeName() == "Sphere"
    >>> prim_utils.get_first_matching_child_prim("/World", predicate=predicate)
    Usd.Prim(</World/Sphere>)
    ```

get\_first\_matching\_parent\_prim( : *prim: str | Usd.Prim | usdrt.Usd.Prim*, : *\**, : *predicate: Callable[[Usd.Prim | usdrt.Usd.Prim, str], bool]*, : *include\_self: bool = False*, ) → Usd.Prim | usdrt.Usd.Prim | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None")
:   Get the first prim parent of the given prim (excluding itself by default) that passes the predicate.

    Backends: usd, usdrt, fabric.

    Warning

    The root prim (`/`) is not considered a valid parent prim but a pseudo-root prim.
    Therefore, it is not taken into account by this function, and any match for this prim will return `None`.

    Parameters:
    :   * **prim** – Prim path or prim instance.
        * **predicate** – Function to test the prims against.
          The function should take two positional arguments: a prim instance and its path.
          The function should return a boolean value indicating whether a prim passes the predicate.
        * **include\_self** – Whether to include the given prim in the search.

    Returns:
    :   First prim parent or `None` if no prim parent passes the predicate.

    Example:

    ```python
    >>> import isaacsim.core.experimental.utils.prim as prim_utils
    >>> import isaacsim.core.experimental.utils.stage as stage_utils
    >>>
    >>> # define some nested prims
    >>> stage_utils.define_prim("/World/Cube", "Cube")  
    >>> stage_utils.define_prim("/World/Cube/Cylinder", "Cylinder")  
    >>> stage_utils.define_prim("/World/Cube/Cylinder/Sphere", "Sphere")  
    >>>
    >>> # get the first `Sphere`'s parent prim of type Cube
    >>> predicate = lambda prim, path: prim.GetTypeName() == "Cube"
    >>> prim_utils.get_first_matching_parent_prim("/World/Cube/Cylinder/Sphere", predicate=predicate)
    Usd.Prim(</World/Cube>)
    ```

get\_prim\_at\_path( : *path: str | Sdf.Path | Usd.Prim | usdrt.Usd.Prim | Usd.SchemaBase | usdrt.Usd.SchemaBase*, ) → Usd.Prim | usdrt.Usd.Prim
:   Get the prim at a given path.

    Backends: usd, usdrt, fabric.

    Hint

    To maximize robustness and versatility, this method supports either a USD/USDRT prim or schema
    instance as input. In such a case, the held prim is returned.

    Parameters:
    :   **path** – Prim path. It also accepts a prim/schema instance as input.

    Returns:
    :   Prim.

    Example:

    ```python
    >>> import isaacsim.core.experimental.utils.prim as prim_utils
    >>> import isaacsim.core.experimental.utils.stage as stage_utils
    >>>
    >>> stage_utils.define_prim(f"/World/Cube", "Cube")  
    >>>
    >>> prim_utils.get_prim_at_path("/World/Cube")
    Usd.Prim(</World/Cube>)
    ```

get\_prim\_attribute\_names( : *prim: str | Usd.Prim | usdrt.Usd.Prim*, ) → list[str]
:   Get all valid attribute names for a prim.

    Backends: usd, usdrt, fabric.

    Parameters:
    :   **prim** – Prim path or prim instance.

    Returns:
    :   Attribute names authored on the prim.

    Example:

    ```python
    >>> import isaacsim.core.experimental.utils.prim as prim_utils
    >>> import isaacsim.core.experimental.utils.stage as stage_utils
    >>>
    >>> stage_utils.define_prim("/World/Cube", "Cube")  
    >>>
    >>> prim_utils.get_prim_attribute_names("/World/Cube")
    ['doubleSided', 'extent', 'orientation', 'primvars:displayColor', 'primvars:displayOpacity', 'purpose', 'size', 'visibility', 'xformOpOrder']
    ```

get\_prim\_attribute\_value( : *prim: str | Usd.Prim | usdrt.Usd.Prim*, : *attribute\_name: str*, ) → Any
:   Get the value of a prim attribute.

    Backends: usd, usdrt, fabric.

    For vector and matrix types (e.g., float3, matrix4d, quatf), the value is returned as a Python list.
    For scalar and other types, the raw attribute value is returned.

    Parameters:
    :   * **prim** – Prim path or prim instance.
        * **attribute\_name** – Name of the attribute to get.

    Returns:
    :   The attribute value. Vector and matrix types are returned as lists.

    Raises:
    :   **ValueError** – If the prim does not have the specified attribute.

    Example:

    ```python
    >>> import isaacsim.core.experimental.utils.prim as prim_utils
    >>> import isaacsim.core.experimental.utils.stage as stage_utils
    >>>
    >>> stage_utils.define_prim("/World/Cube", "Cube")  
    >>>
    >>> prim_utils.get_prim_attribute_value("/World/Cube", "size")
    2.0
    ```

get\_prim\_path( : *prim: Usd.Prim | usdrt.Usd.Prim | Usd.SchemaBase | usdrt.Usd.SchemaBase | str | Sdf.Path*, ) → str
:   Get the path of a given prim.

    Backends: usd, usdrt, fabric.

    Hint

    To maximize robustness and versatility, this method supports either a USD/USDRT schema
    instance or a path as input. In such a case, the held prim path is returned.

    Parameters:
    :   **prim** – Prim instance. It also accepts a schema instance or a path as input.

    Returns:
    :   Prim path.

    Example:

    ```python
    >>> import isaacsim.core.experimental.utils.prim as prim_utils
    >>> import isaacsim.core.experimental.utils.stage as stage_utils
    >>>
    >>> prim = stage_utils.define_prim(f"/World/Cube", "Cube")
    >>> prim_utils.get_prim_path(prim)
    '/World/Cube'
    ```

get\_prim\_variant\_collection( : *prim: str | Usd.Prim*, ) → dict[str, list[str]]
:   Get variant collection (all variant sets and selections) for a USD prim.

    Backends: usd.

    Parameters:
    :   **prim** – Prim path or prim instance.

    Returns:
    :   Variant collection (variant sets and selections).

    Example:

    ```python
    >>> import isaacsim.core.experimental.utils.prim as prim_utils
    >>> import isaacsim.core.experimental.utils.stage as stage_utils
    >>> from isaacsim.storage.native import get_assets_root_path
    >>>
    >>> stage_utils.open_stage(
    ...     get_assets_root_path() + "/Isaac/Robots/FrankaRobotics/FrankaPanda/franka.usd"
    ... )  
    >>>
    >>> prim_utils.get_prim_variant_collection("/panda")
    {'Mesh': ['Performance', 'Quality'], 'Gripper': ['AlternateFinger', 'Default', 'None', 'Robotiq_2F_85']}
    ```

get\_prim\_variants(*prim: str | Usd.Prim*) → list[tuple[str, str]]
:   Get variants (variant sets and selections) authored on a USD prim.

    Backends: usd.

    Parameters:
    :   **prim** – Prim path or prim instance.

    Returns:
    :   Authored variants (variant sets and selections).

    Example:

    ```python
    >>> import isaacsim.core.experimental.utils.prim as prim_utils
    >>> import isaacsim.core.experimental.utils.stage as stage_utils
    >>> from isaacsim.storage.native import get_assets_root_path
    >>>
    >>> stage_utils.open_stage(
    ...     get_assets_root_path() + "/Isaac/Robots/FrankaRobotics/FrankaPanda/franka.usd"
    ... )  
    >>>
    >>> prim_utils.get_prim_variants("/panda")
    [('Gripper', 'Default'), ('Mesh', 'Performance')]
    ```

has\_api( : *prim: str | Usd.Prim*, : *api: str | type | list[str | type]*, : *\**, : *test: Literal['all', 'any', 'none'] = 'all'*, ) → bool
:   Check if a prim has or not the given API schema(s) applied.

    Backends: usd.

    Parameters:
    :   * **prim** – Prim path or prim instance.
        * **api** – API schema name or type, or a list of them.
        * **test** –

          Checking operation to test for. Supported values are:

          + `"all"`: All APIs must be present.
          + `"any"`: Any API must be present.
          + `"none"`: No APIs must be present.

    Returns:
    :   Whether the prim has or not (depending on the test) the given API schema applied.

    Raises:
    :   **ValueError** – If the test operation is invalid.

    Example:

    ```python
    >>> import isaacsim.core.experimental.utils.prim as prim_utils
    >>> import isaacsim.core.experimental.utils.stage as stage_utils
    >>> from pxr import UsdLux
    >>>
    >>> prim = stage_utils.define_prim("/World/Light", "SphereLight")
    >>> prim_utils.has_api(prim, UsdLux.LightAPI)
    True
    ```

is\_prim\_non\_root\_articulation\_link( : *prim: str | Usd.Prim | usdrt.Usd.Prim*, ) → bool
:   Check whether a prim corresponds to a non-root link in an articulation.

    Backends: usd, usdrt, fabric.

    This function returns `True` only if all the following conditions are met:

    * The prim belongs to an articulation.
    * The prim is a link (has the `RigidBodyAPI` applied).
    * The prim is related to a joint.

    Warning

    While a `True` return value guarantees that the prim is a non-root link in an articulation,
    a `False` return value does not guarantee that the prim is an articulation root link.

    Parameters:
    :   **prim** – Prim path or prim instance.

    Returns:
    :   Whether the prim corresponds to a non-root link in an articulation.

    Example:

    ```python
    >>> import isaacsim.core.experimental.utils.prim as prim_utils
    >>> import isaacsim.core.experimental.utils.stage as stage_utils
    >>> from isaacsim.storage.native import get_assets_root_path
    >>>
    >>> stage_utils.open_stage(
    ...     get_assets_root_path() + "/Isaac/Robots/FrankaRobotics/FrankaPanda/franka.usd"
    ... )  
    >>>
    >>> prim_utils.is_prim_non_root_articulation_link("/panda")
    False
    >>> prim_utils.is_prim_non_root_articulation_link("/panda/panda_link0")
    True
    ```

set\_prim\_variants( : *prim: str | Usd.Prim*, : *\**, : *variants: list[tuple[str, str]]*, ) → [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None")
:   Set/author variants (variant sets and selections) on a USD prim.

    Backends: usd.

    Parameters:
    :   * **prim** – Prim path or prim instance.
        * **variants** – Variants (variant sets and selections) to author on the USD prim.

    Raises:
    :   **ValueError** – If a variant set or selection is invalid.

    Example:

    ```python
    >>> import isaacsim.core.experimental.utils.prim as prim_utils
    >>> import isaacsim.core.experimental.utils.stage as stage_utils
    >>> from isaacsim.storage.native import get_assets_root_path
    >>>
    >>> stage_utils.open_stage(
    ...     get_assets_root_path() + "/Isaac/Robots/FrankaRobotics/FrankaPanda/franka.usd"
    ... )  
    >>>
    >>> prim_utils.set_prim_variants("/panda", variants=[("Mesh", "Quality"), ("Gripper", "AlternateFinger")])
    ```

### Semantics Utils

Functions for creating, accessing and deleting semantic labels.

add\_labels( : *prim: str | Usd.Prim*, : *\**, : *labels: str | list[str]*, : *taxonomy: str = 'class'*, ) → [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None")
:   Add semantic labels, given a taxonomy (instance name), to a prim.

    Backends: usd.

    Parameters:
    :   * **prim** – Prim path or prim instance.
        * **labels** – Label(s) to add to existing ones (if any).
        * **taxonomy** – Name of the taxonomy (instance name).

    Examples:

    ```python
    >>> import isaacsim.core.experimental.utils.semantics as semantics_utils
    >>> import isaacsim.core.experimental.utils.stage as stage_utils
    >>>
    >>> stage_utils.define_prim("/World/Cube", "Cube")  
    >>>
    >>> # add some labels to the default 'class' and 'custom' taxonomies
    >>> semantics_utils.add_labels("/World/Cube", labels=["label_a", "label_b"])
    >>> semantics_utils.add_labels("/World/Cube", labels=["label_c"], taxonomy="custom")
    >>>
    >>> # get the labels
    >>> semantics_utils.get_labels("/World/Cube")
    {'class': ['label_a', 'label_b'], 'custom': ['label_c']}
    ```

get\_labels( : *prim: str | Usd.Prim*, : *\**, : *include\_descendants: bool = False*, ) → dict[str, list[str]]
:   Get all the semantic labels applied to a prim.

    Backends: usd.

    Parameters:
    :   * **prim** – Prim path or prim instance.
        * **include\_descendants** – Whether to include labels from all descendants of the prim.

    Returns:
    :   Dictionary mapping taxonomies (instance names) to a list of semantic labels applied to the prim.

    Examples:

    ```python
    >>> import isaacsim.core.experimental.utils.semantics as semantics_utils
    >>> import isaacsim.core.experimental.utils.stage as stage_utils
    >>>
    >>> stage_utils.define_prim("/World/Cube", "Cube")  
    >>>
    >>> # add some labels to the default 'class' and 'custom' taxonomies
    >>> semantics_utils.add_labels("/World/Cube", labels=["label_a", "label_b"])
    >>> semantics_utils.add_labels("/World/Cube", labels=["label_c"], taxonomy="custom")
    >>>
    >>> # get the labels
    >>> semantics_utils.get_labels("/World/Cube")
    {'class': ['label_a', 'label_b'], 'custom': ['label_c']}
    ```

remove\_all\_labels( : *prim: str | Usd.Prim*, : *\**, : *remove\_taxonomies: bool = False*, : *include\_descendants: bool = False*, ) → [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None")
:   Remove all semantic labels from a prim.

    Backends: usd.

    This function removes all labels from a prim (and optionally all its descendants).
    To remove specific labels, use the [`remove_labels()`](#isaacsim.core.experimental.utils.impl.semantics.remove_labels "isaacsim.core.experimental.utils.impl.semantics.remove_labels") function instead.

    Parameters:
    :   * **prim** – Prim path or prim instance.
        * **remove\_taxonomies** – Whether to remove the taxonomies (instance names) along with the labels.
        * **include\_descendants** – Whether to remove labels from all descendants of the prim.

    Examples:

    ```python
    >>> import isaacsim.core.experimental.utils.semantics as semantics_utils
    >>> import isaacsim.core.experimental.utils.stage as stage_utils
    >>>
    >>> stage_utils.define_prim("/World/Cube", "Cube")  
    >>>
    >>> # add some labels to the default 'class' and 'custom' taxonomies
    >>> semantics_utils.add_labels("/World/Cube", labels=["label_a", "label_b"])
    >>> semantics_utils.add_labels("/World/Cube", labels=["label_c"], taxonomy="custom")
    >>>
    >>> # remove all labels
    >>> semantics_utils.remove_all_labels("/World/Cube")
    >>> semantics_utils.get_labels("/World/Cube")
    {'class': [], 'custom': []}
    >>>
    >>> # remove all labels and taxonomies
    >>> semantics_utils.remove_all_labels("/World/Cube", remove_taxonomies=True)
    >>> semantics_utils.get_labels("/World/Cube")
    {}
    ```

remove\_labels( : *prim: str | Usd.Prim*, : *\**, : *labels: str | list[str]*, : *taxonomy: str | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *include\_descendants: bool = False*, ) → [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None")
:   Remove semantic labels from a prim.

    Backends: usd.

    This function removes specific labels from a prim (and optionally all its descendants).
    To remove all labels, use the [`remove_all_labels()`](#isaacsim.core.experimental.utils.impl.semantics.remove_all_labels "isaacsim.core.experimental.utils.impl.semantics.remove_all_labels") function instead.

    Parameters:
    :   * **prim** – Prim path or prim instance.
        * **labels** – Label(s) to remove (if any).
        * **taxonomy** – Name of the taxonomy (instance name) to remove labels from.
          If not specified, matching labels from all taxonomies will be removed.
        * **include\_descendants** – Whether to remove labels from all descendants of the prim.

    Examples:

    ```python
    >>> import isaacsim.core.experimental.utils.semantics as semantics_utils
    >>> import isaacsim.core.experimental.utils.stage as stage_utils
    >>>
    >>> stage_utils.define_prim("/World/Cube", "Cube")  
    >>>
    >>> # add some labels to the default 'class' and 'custom' taxonomies
    >>> semantics_utils.add_labels("/World/Cube", labels=["label_a", "label_b"])
    >>> semantics_utils.add_labels("/World/Cube", labels=["label_c"], taxonomy="custom")
    >>>
    >>> # remove one of the labels and get the remaining ones
    >>> semantics_utils.remove_labels("/World/Cube", labels="label_a")
    >>> semantics_utils.get_labels("/World/Cube")
    {'class': ['label_b'], 'custom': ['label_c']}
    ```

upgrade\_prim\_semantics\_to\_labels( : *prim: str | Usd.Prim*, : *\**, : *include\_descendants: bool = False*, ) → list[str]
:   Upgrade a prim from the deprecated `Semantics.SemanticsAPI` to `UsdSemantics.LabelsAPI`.

    Backends: usd.

    Converts each `SemanticsAPI` instance found on the prim (and optionally its
    descendants) to a `LabelsAPI` instance. The old `semanticType` becomes
    the new taxonomy (instance name), and the old `semanticData` becomes the
    label. The old `SemanticsAPI` is removed after upgrading.

    Parameters:
    :   * **prim** – Prim path or prim instance.
        * **include\_descendants** – If `True`, upgrades the prim and all its descendants.
          If `False`, upgrades only the specified prim.

    Returns:
    :   Paths of prims that had at least one `SemanticsAPI` instance upgraded.

    Examples:

    ```python
    >>> import isaacsim.core.experimental.utils.semantics as semantics_utils
    >>>
    >>> # upgrade old-style semantics on a prim and its descendants
    >>> upgraded_paths = semantics_utils.upgrade_prim_semantics_to_labels("/World/Asset", include_descendants=True)
    ```

### Stage Utils

Functions for working with USD/USDRT stages.

add\_reference\_to\_stage( : *usd\_path: str*, : *path: str*, : *\**, : *prim\_type: str = 'Xform'*, : *variants: list[tuple[str, str]] | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, ) → pxr.Usd.Prim
:   Add a USD file reference to the stage at the specified prim path.

    Backends: usd.

    Note

    This function handles stage units verification to ensure compatibility.

    Parameters:
    :   * **usd\_path** – USD file path to reference.
        * **path** – Prim path where the reference will be attached.
        * **prim\_type** – Prim type to create if the given `path` doesn’t exist.
        * **variants** – Variants (variant sets and selections) to author on the USD prim.

    Returns:
    :   USD prim.

    Raises:
    :   * **Exception** – The USD file might not exist or might not be a valid USD file.
        * **ValueError** – If a variant set or selection is invalid.

    Example:

    ```python
    >>> import isaacsim.core.experimental.utils.stage as stage_utils
    >>> from isaacsim.storage.native import get_assets_root_path
    >>>
    >>> prim = stage_utils.add_reference_to_stage(
    ...     usd_path=get_assets_root_path() + "/Isaac/Robots/FrankaRobotics/FrankaPanda/franka.usd",
    ...     path="/panda",
    ...     variants=[("Gripper", "AlternateFinger"), ("Mesh", "Performance")],
    ... )
    ```

close\_stage() → bool
:   Close the stage attached to the USD context.

    Backends: usd.

    Returns:
    :   Whether the stage was closed successfully.

create\_new\_stage(*\**, *template: str | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*) → pxr.Usd.Stage
:   Create a new USD stage attached to the USD context.

    Backends: usd.

    Note

    At least the following templates should be available.
    Other templates might be available depending on app customizations.

    Isaac Sim templates

    | Template | Description |
    | --- | --- |
    | `"gridroom"` | Stage with a blue gridroom scene. |

    Kit templates

    | Template | Description |
    | --- | --- |
    | `"default stage"` | Stage with a gray gridded plane, dome and distant lights, and the `/World` Xform prim. |
    | `"empty"` | Empty stage with the `/World` Xform prim. |
    | `"sunlight"` | Stage with a distant light and the `/World` Xform prim. |

    Parameters:
    :   **template** – The template to use to create the stage. If `None`, a new stage is created with nothing.

    Returns:
    :   New USD stage instance.

    Raises:
    :   **ValueError** – When the template is not found.

    Example:

    ```python
    >>> import isaacsim.core.experimental.utils.stage as stage_utils
    >>>
    >>> # create a new stage from the 'gridroom' template
    >>> stage_utils.create_new_stage(template="gridroom")
    Usd.Stage.Open(rootLayer=Sdf.Find('anon:...usd'), ...)

    >>> # get the list of available Kit templates
    >>> import omni.kit.stage_templates
    >>>
    >>> [name for item in omni.kit.stage_templates.get_stage_template_list() for name in item]
    ['empty', 'sunlight', 'default stage']
    ```

*async* create\_new\_stage\_async( : *\**, : *template: str | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, ) → pxr.Usd.Stage
:   Create a new USD stage attached to the USD context.

    Backends: usd.

    This function is the asynchronous version of [`create_new_stage()`](#isaacsim.core.experimental.utils.impl.stage.create_new_stage "isaacsim.core.experimental.utils.impl.stage.create_new_stage").

    Parameters:
    :   **template** – The template to use to create the stage. If `None`, a new stage is created with nothing.

    Returns:
    :   New USD stage instance.

    Raises:
    :   **ValueError** – When the template is not found.

define\_prim( : *path: str*, : *type\_name: str = 'Xform'*, ) → Usd.Prim | usdrt.Usd.Prim
:   Attempt to define a prim of the specified type at the given path.

    Backends: usd, usdrt, fabric.

    Common token values for `type_name` are:

    * `"Camera"`, `"Mesh"`, `"PhysicsScene"`, `"Scope"`, `"Xform"`
    * Shapes (`"Capsule"`, `"Cone"`, `"Cube"`, `"Cylinder"`, `"Plane"`, `"Sphere"`)
    * Lights (`"CylinderLight"`, `"DiskLight"`, `"DistantLight"`, `"DomeLight"`, `"RectLight"`, `"SphereLight"`)

    Parameters:
    :   * **path** – Absolute prim path.
        * **type\_name** – Token identifying the prim type.

    Raises:
    :   * **ValueError** – If the path is not a valid or absolute path string.
        * **RuntimeError** – If there is already a prim at the given path with a different type.

    Returns:
    :   Defined prim.

    Example:

    ```python
    >>> import isaacsim.core.experimental.utils.stage as stage_utils
    >>>
    >>> stage_utils.define_prim("/World/Sphere", type_name="Sphere")
    Usd.Prim(</World/Sphere>)
    ```

delete\_prim(*prim: str | Usd.Prim*) → bool
:   Delete a prim from the stage.

    Backends: usd.

    Parameters:
    :   **prim** – Prim path or prim instance to delete.

    Returns:
    :   Whether the prim was deleted successfully.

    Raises:
    :   **ValueError** – If the target prim is not a valid prim.

    Example:

    ```python
    >>> import isaacsim.core.experimental.utils.stage as stage_utils
    >>>
    >>> stage_utils.define_prim("/World/Sphere", type_name="Sphere")  
    >>> stage_utils.delete_prim("/World/Sphere")
    True
    ```

generate\_next\_free\_path( : *path: str | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *\**, : *prepend\_default\_prim: bool = True*, ) → str
:   Generate the next free usd path for the current stage.

    Backends: usd.

    Parameters:
    :   * **path** – Base path to generate the next free path from.
          If empty, pseudo-root or not defined, `"Prim"` will be used as the default name.
        * **prepend\_default\_prim** – Whether to prepend the default prim path to the base path.

    Returns:
    :   Next free path.

    Example:

    ```python
    >>> import isaacsim.core.experimental.utils.stage as stage_utils
    >>>
    >>> # given the stage: /World/Cube, /World/Cube_01
    >>> stage_utils.define_prim("/World/Cube", type_name="Cube")  
    >>> stage_utils.define_prim("/World/Cube_01", type_name="Cube")  
    >>>
    >>> # generate the next available path for /World/Cube
    >>> stage_utils.generate_next_free_path("/World/Cube")
    '/World/Cube_02'
    ```

generate\_stage\_representation( : *mode: Literal['list', 'tree'] = 'tree'*, ) → str
:   Generate a string representation of the stage.

    Parameters:
    :   **mode** –

        The mode to use to generate the representation. Available modes are:

        * `"list"`: List all prims in the stage.
        * `"tree"`: Tree representation of the stage.

    Returns:
    :   String representation of the stage.

    Example:

    ```python
    >>> import isaacsim.core.experimental.utils.stage as stage_utils
    >>>
    >>> stage_utils.create_new_stage()  
    >>> stage_utils.define_prim("/World/PrimA", type_name="Sphere")  
    >>> stage_utils.define_prim("/World/PrimB", type_name="Cube")  
    >>> stage_utils.define_prim("/PrimC", type_name="Camera")  
    >>>
    >>> print(stage_utils.generate_stage_representation(mode="list"))
    /World ()
    /World/PrimA (Sphere)
    /World/PrimB (Cube)
    /PrimC (Camera)
    >>>
    >>> print(stage_utils.generate_stage_representation(mode="tree"))
    / ()
    ├─ World ()
    │  ├─ PrimA (Sphere)
    │  ├─ PrimB (Cube)
    ├─ PrimC (Camera)
    ```

get\_current\_stage( : *\**, : *backend: str | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, ) → Usd.Stage | usdrt.Usd.Stage
:   Get the stage set in the context manager or the default stage attached to the USD context.

    Backends: usd, usdrt, fabric.

    Parameters:
    :   **backend** – Backend to use to get the stage. If not `None`, it has precedence over the current backend
        set via the [`use_backend()`](#isaacsim.core.experimental.utils.impl.backend.use_backend "isaacsim.core.experimental.utils.impl.backend.use_backend") context manager.

    Returns:
    :   The current stage instance or the default stage attached to the USD context if no stage is set.

    Raises:
    :   * **ValueError** – If the backend is not supported.
        * **ValueError** – If there is no stage (set via context manager or attached to the USD context).

    Example:

    ```python
    >>> import isaacsim.core.experimental.utils.stage as stage_utils
    >>>
    >>> stage_utils.get_current_stage()
    Usd.Stage.Open(rootLayer=Sdf.Find('anon:...usd'), ...)
    ```

get\_stage\_id(*stage: pxr.Usd.Stage*) → int
:   Get the stage ID of a USD stage.

    Backends: usd.

    Parameters:
    :   **stage** – The stage to get the ID of.

    Returns:
    :   The stage ID.

    Example:

    ```python
    >>> import isaacsim.core.experimental.utils.stage as stage_utils
    >>>
    >>> stage = stage_utils.get_current_stage()
    >>> stage_utils.get_stage_id(stage)  
    9223006
    ```

get\_stage\_time\_code() → tuple[float, float, float]
:   Get the stage time code (start, end, and time codes per second).

    Backends: usd.

    Returns:
    :   The stage time code (start, end, and time codes per second).

    Example:

    ```python
    >>> import isaacsim.core.experimental.utils.stage as stage_utils
    >>>
    >>> stage_utils.get_stage_time_code()
    (0.0, 100.0, 60.0)
    ```

get\_stage\_units() → tuple[float, float]
:   Get the stage meters per unit and kilograms per unit currently set.

    Backends: usd.

    The most common distance units and their values are listed in the following table:

    | Unit | Value |
    | --- | --- |
    | kilometer (km) | 1000.0 |
    | meters (m) | 1.0 |
    | inch (in) | 0.0254 |
    | centimeters (cm) | 0.01 |
    | millimeter (mm) | 0.001 |

    The most common mass units and their values are listed in the following table:

    | Unit | Value |
    | --- | --- |
    | metric ton (t) | 1000.0 |
    | kilogram (kg) | 1.0 |
    | gram (g) | 0.001 |
    | pound (lb) | 0.4536 |
    | ounce (oz) | 0.0283 |

    Returns:
    :   Current stage meters per unit and kilograms per unit.

    Example:

    ```python
    >>> import isaacsim.core.experimental.utils.stage as stage_utils
    >>>
    >>> stage_utils.get_stage_units()
    (1.0, 1.0)
    ```

get\_stage\_up\_axis() → Literal['Y', 'Z']
:   Get the stage up axis.

    Backends: usd.

    Note

    According to the USD specification, only `"Y"` and `"Z"` axes are supported.

    Returns:
    :   The stage up axis.

    Example:

    ```python
    >>> import isaacsim.core.experimental.utils.stage as stage_utils
    >>>
    >>> stage_utils.get_stage_up_axis()
    'Z'
    ```

is\_stage\_loading() → bool
:   Check whether the stage is loading.

    Backends: usd.

    Returns:
    :   Whether the stage is loading.

is\_stage\_set() → bool
:   Check if a stage is set in the context manager.

    Returns:
    :   Whether a stage is set in the context manager.

move\_prim( : *target: str | Usd.Prim*, : *destination: str | Usd.Prim*, ) → tuple[bool, str]
:   Move a prim to a different location on the stage hierarchy.

    Backends: usd.

    The move operation follows the next rules:

    * If the destination exists, the target prim is moved (as a child) into the destination prim.
      Moved prim keeps its name.
    * If the destination does not exist, the target prim is moved to the specified destination path,
      provided that the parent exists (if not, an error is raised). Moved prim is renamed.

    Parameters:
    :   * **target** – Prim path or prim instance to move.
        * **destination** – Destination path or prim instance to move the prim to.

    Returns:
    :   Whether the prim was moved successfully and the new path.

    Raises:
    :   * **ValueError** – If the target prim is not a valid prim.
        * **ValueError** – If the destination path has unexisting parents.
        * **ValueError** – If the destination path is not a valid path string.

    Example:

    ```python
    >>> import isaacsim.core.experimental.utils.stage as stage_utils
    >>>
    >>> prim_A = stage_utils.define_prim("/World/A")
    >>> prim_B = stage_utils.define_prim("/World/B")
    >>>
    >>> # move prim A to (into) prim B
    >>> stage_utils.move_prim(prim_A, prim_B)
    (True, '/World/B/A')
    >>> # move prim A next to /World (with name C)
    >>> stage_utils.move_prim("/World/B/A", "/World/C")
    (True, '/World/C')
    ```

open\_stage(*usd\_path: str*) → tuple[bool, Usd.Stage | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None")]
:   Open a USD file attached to the USD context.

    Backends: usd.

    Parameters:
    :   **usd\_path** – USD file path to open.

    Returns:
    :   Two-elements tuple. 1) Whether the USD file was opened successfully.
        2) Opened USD stage instance or None if the USD file was not opened.

    Raises:
    :   **ValueError** – If the USD file does not exist or is not a valid (shallow check).

    Example:

    ```python
    >>> import isaacsim.core.experimental.utils.stage as stage_utils
    >>> from isaacsim.storage.native import get_assets_root_path
    >>>
    >>> # open a USD file
    >>> result, stage = stage_utils.open_stage(
    ...     get_assets_root_path() + "/Isaac/Robots/FrankaRobotics/FrankaPanda/franka.usd"
    ... )
    >>> result
    True
    >>> stage
    Usd.Stage.Open(rootLayer=Sdf.Find('...'), ...)
    ```

*async* open\_stage\_async(*usd\_path: str*) → tuple[bool, Usd.Stage | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None")]
:   Open a USD file attached to the USD context.

    Backends: usd.

    This function is the asynchronous version of [`open_stage()`](#isaacsim.core.experimental.utils.impl.stage.open_stage "isaacsim.core.experimental.utils.impl.stage.open_stage").

    Parameters:
    :   **usd\_path** – USD file path to open.

    Returns:
    :   Two-elements tuple. 1) Whether the USD file was opened successfully.
        2) Opened USD stage instance or None if the USD file was not opened.

    Raises:
    :   **ValueError** – If the USD file does not exist or is not a valid (shallow check).

save\_stage(*usd\_path: str*) → bool
:   Save the current stage to a USD file.

    Backends: usd.

    Parameters:
    :   **usd\_path** – USD file path to save the current stage to.

    Returns:
    :   Whether the stage was saved successfully.

    Example:

    ```python
    >>> import os
    >>> import tempfile
    >>> import isaacsim.core.experimental.utils.stage as stage_utils
    >>>
    >>> # save the current stage to a USD file
    >>> usd_path = os.path.join(tempfile.gettempdir(), "test.usd")
    >>> stage_utils.save_stage(usd_path)
    True
    ```

set\_stage\_time\_code( : *\**, : *start\_time\_code: float | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *end\_time\_code: float | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *time\_codes\_per\_second: float | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, ) → [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None")
:   Set the stage time code (start, end, and time codes per second).

    Backends: usd.

    Parameters:
    :   * **start\_time\_code** – The start time code.
        * **end\_time\_code** – The end time code.
        * **time\_codes\_per\_second** – The time codes per second.

    Example:

    ```python
    >>> import isaacsim.core.experimental.utils.stage as stage_utils
    >>>
    >>> stage_utils.set_stage_time_code(start_time_code=0.0, end_time_code=100.0, time_codes_per_second=10.0)
    ```

set\_stage\_units( : *\**, : *meters\_per\_unit: float | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *kilograms\_per\_unit: float | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, ) → [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None")
:   Set the stage meters per unit and kilograms per unit.

    Backends: usd.

    The most common distance units and their values are listed in the following table:

    | Unit | Value |
    | --- | --- |
    | kilometer (km) | 1000.0 |
    | meters (m) | 1.0 |
    | inch (in) | 0.0254 |
    | centimeters (cm) | 0.01 |
    | millimeter (mm) | 0.001 |

    The most common mass units and their values are listed in the following table:

    | Unit | Value |
    | --- | --- |
    | metric ton (t) | 1000.0 |
    | kilogram (kg) | 1.0 |
    | gram (g) | 0.001 |
    | pound (lb) | 0.4536 |
    | ounce (oz) | 0.0283 |

    Parameters:
    :   * **meters\_per\_unit** – Meters per unit.
        * **kilograms\_per\_unit** – Kilograms per unit.

    Example:

    ```python
    >>> import isaacsim.core.experimental.utils.stage as stage_utils
    >>>
    >>> # set stage units to inch and pound respectively
    >>> stage_utils.set_stage_units(meters_per_unit=0.0254, kilograms_per_unit=0.4536)
    ```

set\_stage\_up\_axis(*up\_axis: Literal['Y', 'Z']*) → [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None")
:   Set the stage up axis.

    Backends: usd.

    Note

    According to the USD specification, only `"Y"` and `"Z"` axes are supported.

    Parameters:
    :   **up\_axis** – The stage up axis.

    Raises:
    :   **ValueError** – If the up axis is not a valid token.

    Example:

    ```python
    >>> import isaacsim.core.experimental.utils.stage as stage_utils
    >>>
    >>> stage_utils.set_stage_up_axis("Y")
    ```

use\_stage( : *stage: pxr.Usd.Stage*, ) → Generator[[None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None"), [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None"), [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None")]
:   Context manager that sets a thread-local stage instance.

    Parameters:
    :   **stage** – The stage to set in the context.

    Raises:
    :   **AssertionError** – If the stage is not a USD stage instance.

    Example:

    ```python
    >>> from pxr import Usd
    >>> import isaacsim.core.experimental.utils.stage as stage_utils
    >>>
    >>> stage_in_memory = Usd.Stage.CreateInMemory()
    >>> with stage_utils.use_stage(stage_in_memory):
    ...    # operate on the specified stage
    ...    pass
    >>> # operate on the default stage attached to the USD context
    ```

### Transform Utils

Functions for performing transform operations.

compute\_relative\_transform( : *source\_to\_world: list | np.ndarray | wp.array*, : *target\_to\_world: list | np.ndarray | wp.array*, ) → np.ndarray
:   Compute the relative 4x4 transform from a source frame to a target frame given their world transforms.

    Both inputs are expected in USD row-major convention (as returned by
    `UsdGeom.Xformable.ComputeLocalToWorldTransform`). The result is a column-major
    4x4 matrix that transforms points from the source local frame into the target local frame.

    Parameters:
    :   * **source\_to\_world** – Row-major 4x4 world transform of the source frame.
        * **target\_to\_world** – Row-major 4x4 world transform of the target frame.

    Returns:
    :   Column-major 4x4 relative transformation matrix.

    Example:

    ```python
    >>> import isaacsim.core.experimental.utils.transform as transform_utils
    >>> import numpy as np
    >>>
    >>> identity = np.eye(4)
    >>> translated = np.eye(4)
    >>> translated[3, :3] = [1.0, 2.0, 3.0]  # USD row-major: translation in last row
    >>> result = transform_utils.compute_relative_transform(identity, translated)
    >>> result[:3, 3]  # column-major: translation in last column
    array([-1., -2., -3.])
    ```

euler\_angles\_to\_quaternion( : *euler\_angles: list | np.ndarray | wp.array*, : *\**, : *degrees: bool = False*, : *extrinsic: bool = True*, : *dtype: type | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *device: str | wp.Device | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, ) → wp.array
:   Convert Euler angles to quaternion.

    Parameters:
    :   * **euler\_angles** – Euler angles or batch of Euler angles with shape (…, 3).
          Input order is always [X, Y, Z] = [roll, pitch, yaw] for both conventions.
        * **degrees** – Whether input angles are in degrees.
        * **extrinsic** – True if the euler angles follows the extrinsic angles
          convention (rotation applied as Rz \* Ry \* Rx about fixed world axes) and False if it
          follows the intrinsic angles conventions (rotation applied as Rx \* Ry \* Rz about
          body-fixed axes).
        * **dtype** – Data type of the output array. If `None`, the data type of the input is used.
        * **device** – Device to place the output array on. If `None`, the default device is used,
          unless the input is a Warp array (in which case the input device is used).

    Returns:
    :   Quaternion (w, x, y, z) or batch of quaternions with shape (…, 4).

    Example:

    ```python
    >>> import isaacsim.core.experimental.utils.transform as transform_utils
    >>> import numpy as np
    >>>
    >>> # Convert 90 degree rotation around Y axis
    >>> euler = np.array([0, np.pi/2, 0])
    >>> quaternion = transform_utils.euler_angles_to_quaternion(euler)  
    >>> quaternion.numpy()
    array([0.70710678, 0.        , 0.70710678, 0.        ])
    ```

euler\_angles\_to\_rotation\_matrix( : *euler\_angles: list | np.ndarray | wp.array*, : *\**, : *degrees: bool = False*, : *extrinsic: bool = True*, : *dtype: type | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *device: str | wp.Device | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, ) → wp.array
:   Convert Euler angles to rotation matrix.

    Parameters:
    :   * **euler\_angles** – Euler angles or batch of Euler angles with shape (…, 3).
          Input order is always [X, Y, Z] = [roll, pitch, yaw] for both conventions.
        * **degrees** – Whether passed angles are in degrees.
        * **extrinsic** – True if the euler angles follows the extrinsic angles
          convention (rotation applied as Rz \* Ry \* Rx about fixed world axes) and False if it
          follows the intrinsic angles conventions (rotation applied as Rx \* Ry \* Rz about
          body-fixed axes).
        * **dtype** – Data type of the output array. If `None`, the data type of the input is used.
        * **device** – Device to place the output array on. If `None`, the default device is used,
          unless the input is a Warp array (in which case the input device is used).

    Returns:
    :   A 3x3 rotation matrix or batch of 3x3 rotation matrices with shape (…, 3, 3).

    Example:

    ```python
    >>> import isaacsim.core.experimental.utils.transform as transform_utils
    >>> import numpy as np
    >>>
    >>> # Zero rotation
    >>> euler = np.array([0, 0, 0])
    >>> rotation_matrix = transform_utils.euler_angles_to_rotation_matrix(euler)  
    >>> rotation_matrix.numpy()
    array([[1., 0., 0.],
           [0., 1., 0.],
           [0., 0., 1.]], dtype=float32)
    ```

look\_at\_matrix( : *eye: list | ndarray | Any*, : *target: list | ndarray | Any*, : *up: list | ndarray | Any | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *\**, : *epsilon: float = 1e-05*, ) → Any
:   Compute the camera transform matrix (position + orientation) for a look-at.

    Returns the `Gf.Matrix4d` that places a camera at *eye* oriented so its
    negative-Z axis points toward *target* (USD / OpenGL camera convention).
    This is the inverse of the standard view (LookAt) matrix and can be used
    directly as a prim’s local transform.

    When the forward direction (*target* − *eye*) is nearly parallel to *up*,
    a perpendicular fallback up vector is chosen automatically.

    Parameters:
    :   * **eye** – Camera position with shape (3,). Accepts list, numpy array, or `Gf.Vec3d`.
        * **target** – Target position with shape (3,). Accepts list, numpy array, or `Gf.Vec3d`.
        * **up** – World up vector with shape (3,). Defaults to Z-up `[0, 0, 1]`.
          Accepts list, numpy array, or `Gf.Vec3d`.
        * **epsilon** – Collinearity threshold. When the cross-product of the forward
          direction and *up* has length below this value, a fallback up vector
          is used.

    Returns:
    :   `Gf.Matrix4d` camera transform (position + orientation). This is **not**
        the view matrix — it is the prim world/local transform.

    Example:

    ```python
    >>> import isaacsim.core.experimental.utils.transform as transform_utils
    >>> import numpy as np
    >>>
    >>> # Camera at (5, 5, 5) looking at the origin
    >>> mat = transform_utils.look_at_matrix(
    ...     eye=np.array([5.0, 5.0, 5.0]),
    ...     target=np.array([0.0, 0.0, 0.0]),
    ... )  
    >>> from pxr import Gf
    >>> isinstance(mat, Gf.Matrix4d)
    True
    ```

look\_at\_quaternion( : *eye: list | np.ndarray | wp.array*, : *target: list | np.ndarray | wp.array*, : *up: list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *\**, : *dtype: type | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *device: str | wp.Device | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, ) → wp.array
:   Compute the orientation quaternion for a look-at transform.

    Compute the quaternion that orients a frame at `eye` so that its
    negative-Z axis points toward `target` (OpenGL / USD camera convention).

    When the forward direction is nearly parallel to the given up vector,
    a perpendicular fallback is chosen automatically.

    The function supports batched inputs. When batch dimensions are present
    the shapes of `eye` and `target` must match. The `up` vector is
    broadcast if necessary.

    Parameters:
    :   * **eye** – Observer position or batch of positions with shape (…, 3).
        * **target** – Target position or batch of positions with shape (…, 3).
        * **up** – World up vector with shape (3,) or matching batch shape (…, 3).
          Defaults to Z-up `[0, 0, 1]`.
        * **dtype** – Data type of the output array. If `None`, the data type of the
          `eye` input is used.
        * **device** – Device to place the output array on. If `None`, the default
          device is used, unless the input is a Warp array (in which case the
          input device is used).

    Returns:
    :   Quaternion (w, x, y, z) or batch of quaternions with shape (…, 4).

    Example:

    ```python
    >>> import isaacsim.core.experimental.utils.transform as transform_utils
    >>> import numpy as np
    >>>
    >>> # Camera at (5,5,5) looking at origin
    >>> quat = transform_utils.look_at_quaternion(
    ...     eye=np.array([5.0, 5.0, 5.0]),
    ...     target=np.array([0.0, 0.0, 0.0]),
    ... )  
    >>> quat.numpy()  
    array([0.33985114, 0.1759199 , 0.42470822, 0.82047325])
    ```

quaternion\_conjugate( : *quaternion: list | np.ndarray | wp.array*, : *\**, : *dtype: type | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *device: str | wp.Device | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, ) → wp.array
:   Compute quaternion conjugate by negating the vector part.

    Quaternion conjugate is used to compute the inverse rotation.
    For unit quaternions, conjugate equals inverse.

    Parameters:
    :   * **quaternion** – Quaternion or batch of quaternions with shape (…, 4) in [w, x, y, z] format.
        * **dtype** – Data type of the output array. If `None`, the data type of the input is used.
        * **device** – Device to place the output array on. If `None`, the default device is used,
          unless the input is a Warp array (in which case the input device is used).

    Returns:
    :   Conjugate quaternion with shape (…, 4).

    Example:

    ```python
    >>> import isaacsim.core.experimental.utils.transform as transform_utils
    >>> import numpy as np
    >>>
    >>> # Conjugate of a simple rotation quaternion
    >>> quaternion = np.array([0.7071, 0.7071, 0.0, 0.0])  # 90 deg around X
    >>> conjugate = transform_utils.quaternion_conjugate(quaternion)  
    >>> conjugate.numpy()
    array([ 0.7071, -0.7071,  0.    ,  0.    ])
    ```

quaternion\_multiplication( : *first\_quaternion: list | np.ndarray | wp.array*, : *second\_quaternion: list | np.ndarray | wp.array*, : *\**, : *dtype: type | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *device: str | wp.Device | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, ) → wp.array
:   Multiply two quaternions using Hamilton product.

    Quaternion multiplication is used for combining rotations.
    Input quaternions are in [w, x, y, z] format.

    Parameters:
    :   * **first\_quaternion** – First quaternion or batch of quaternions with shape (…, 4) in [w, x, y, z] format.
        * **second\_quaternion** – Second quaternion or batch of quaternions with shape (…, 4) in [w, x, y, z] format.
        * **dtype** – Data type of the output array. If `None`, the data type of the first input is used.
        * **device** – Device to place the output array on. If `None`, the default device is used,
          unless the input is a Warp array (in which case the input device is used).

    Returns:
    :   Result of quaternion multiplication with shape (…, 4).

    Example:

    ```python
    >>> import isaacsim.core.experimental.utils.transform as transform_utils
    >>> import numpy as np
    >>>
    >>> # Identity quaternion multiplied with itself
    >>> identity = np.array([1.0, 0.0, 0.0, 0.0])
    >>> result = transform_utils.quaternion_multiplication(identity, identity)  
    >>> result.numpy()
    array([1., 0., 0., 0.])
    ```

quaternion\_to\_euler\_angles( : *quaternion: list | np.ndarray | wp.array*, : *\**, : *degrees: bool = False*, : *extrinsic: bool = True*, : *dtype: type | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *device: str | wp.Device | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, ) → wp.array
:   Convert quaternion to Euler angles.

    Converts quaternions in [w, x, y, z] format to Euler angles. The output order matches
    `isaacsim.core.utils.numpy.rotations.quat_to_euler_angles()` for consistency.

    Parameters:
    :   * **quaternion** – Quaternion or batch of quaternions with shape (…, 4) in [w, x, y, z] format.
        * **degrees** – Whether to return angles in degrees.
        * **extrinsic** – True if the euler angles follows the extrinsic angles
          convention (equivalent to ZYX ordering but returned in the reverse) and False if it follows
          the intrinsic angles conventions (equivalent to XYZ ordering).
        * **dtype** – Data type of the output array. If `None`, the data type of the input is used.
        * **device** – Device to place the output array on. If `None`, the default device is used,
          unless the input is a Warp array (in which case the input device is used).

    Returns:
    :   Euler angles with shape (…, 3). For extrinsic convention, order is [X, Y, Z] (roll, pitch, yaw).
        For intrinsic convention, order is [X, Y, Z] (roll, pitch, yaw).

    Example:

    ```python
    >>> import isaacsim.core.experimental.utils.transform as transform_utils
    >>> import numpy as np
    >>>
    >>> # Identity quaternion to euler angles
    >>> identity = np.array([1.0, 0.0, 0.0, 0.0])
    >>> euler = transform_utils.quaternion_to_euler_angles(identity)  
    >>> euler.numpy()
    array([0., 0., 0.])
    ```

quaternion\_to\_rotation\_matrix( : *quaternion: list | np.ndarray | wp.array*, : *\**, : *dtype: type | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *device: str | wp.Device | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, ) → wp.array
:   Convert quaternion to rotation matrix.

    Converts quaternions in [w, x, y, z] format to 3x3 rotation matrices
    using the standard quaternion-to-matrix formula.

    Parameters:
    :   * **quaternion** – Quaternion or batch of quaternions with shape (…, 4) in [w, x, y, z] format.
        * **dtype** – Data type of the output array. If `None`, the data type of the input is used.
        * **device** – Device to place the output array on. If `None`, the default device is used,
          unless the input is a Warp array (in which case the input device is used).

    Returns:
    :   A 3x3 rotation matrix or batch of 3x3 rotation matrices with shape (…, 3, 3).

    Example:

    ```python
    >>> import isaacsim.core.experimental.utils.transform as transform_utils
    >>> import numpy as np
    >>>
    >>> # Identity quaternion to rotation matrix
    >>> identity = np.array([1.0, 0.0, 0.0, 0.0])
    >>> rotation_matrix = transform_utils.quaternion_to_rotation_matrix(identity)  
    >>> rotation_matrix.numpy()
    array([[1., 0., 0.],
           [0., 1., 0.],
           [0., 0., 1.]])
    ```

rotation\_matrix\_to\_quaternion( : *rotation\_matrix: list | np.ndarray | wp.array*, : *\**, : *dtype: type | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *device: str | wp.Device | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, ) → wp.array
:   Convert rotation matrix to quaternion.

    Parameters:
    :   * **rotation\_matrix** – A 3x3 rotation matrix or batch of 3x3 rotation matrices with shape (…, 3, 3).
        * **dtype** – Data type of the output array. If `None`, the data type of the input is used.
        * **device** – Device to place the output array on. If `None`, the default device is used,
          unless the input is a Warp array (in which case the input device is used).

    Returns:
    :   Quaternion (w, x, y, z) or batch of quaternions with shape (…, 4).

    Example:

    ```python
    >>> import isaacsim.core.experimental.utils.transform as transform_utils
    >>> import numpy as np
    >>>
    >>> # Identity matrix to quaternion
    >>> identity = np.eye(3)
    >>> quaternion = transform_utils.rotation_matrix_to_quaternion(identity)  
    >>> quaternion.numpy()
    array([1., 0., 0., 0.])
    ```

### Xform Utils

Functions for performing transform operations on Xformable USD/USDRT prims.

get\_local\_pose( : *prim: str | Usd.Prim | usdrt.Usd.Prim*, : *\**, : *device: str | wp.Device | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, ) → tuple[wp.array, wp.array]
:   Get the local pose of a prim.

    Backends: usd, usdrt, fabric.

    Parameters:
    :   * **prim** – Prim path or prim instance.
        * **device** – Device to place the output arrays on. If `None`, the default device is used.

    Returns:
    :   Two-elements tuple. 1) The translation in the local frame (shape `(3,)`).
        2) The orientation in the local frame (shape `(4,)`, quaternion `wxyz`).

    Example:

    ```python
    >>> import isaacsim.core.experimental.utils.xform as xform_utils
    >>>
    >>> # given the stage with the following hierarchy:
    >>> # / ()
    >>> # ├─ A (Xform)    --> with local position: (1.0, 2.0, 3.0)
    >>> # │  ├─ B (Xform) --> with local position: (4.0, 5.0, 6.0)
    >>> translation, orientation = xform_utils.get_local_pose("/A/B")
    >>> print(translation)  
    [4. 5. 6.]
    >>> print(orientation)
    [1. 0. 0. 0.]
    ```

get\_relative\_transform( : *source\_prim: str | Usd.Prim*, : *target\_prim: str | Usd.Prim*, ) → np.ndarray
:   Compute the relative transformation matrix from a source prim to a target prim.

    Computes the column-major 4x4 matrix that transforms points from the source prim’s
    local frame into the target prim’s local frame.

    Backends: usd.

    Parameters:
    :   * **source\_prim** – Source prim path or prim instance.
        * **target\_prim** – Target prim path or prim instance.

    Returns:
    :   Column-major transformation matrix with shape (4, 4).

    Example:

    ```python
    >>> import isaacsim.core.experimental.utils.xform as xform_utils
    >>> import omni.usd
    >>>
    >>> stage = omni.usd.get_context().get_stage()
    >>> source = stage.GetPrimAtPath("/World/Source")
    >>> target = stage.GetPrimAtPath("/World/Target")
    >>> relative_tf = xform_utils.get_relative_transform(source, target)  
    >>> relative_tf.shape  
    (4, 4)
    ```

get\_world\_pose( : *prim: str | Usd.Prim | usdrt.Usd.Prim*, : *\**, : *device: str | wp.Device | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, ) → tuple[wp.array, wp.array]
:   Get the world pose of a prim.

    Backends: usd, usdrt, fabric.

    Parameters:
    :   * **prim** – Prim path or prim instance.
        * **device** – Device to place the output arrays on. If `None`, the default device is used.

    Returns:
    :   Two-elements tuple. 1) The translation in the world frame (shape `(3,)`).
        2) The orientation in the world frame (shape `(4,)`, quaternion `wxyz`).

    Example:

    ```python
    >>> import isaacsim.core.experimental.utils.xform as xform_utils
    >>>
    >>> # given the stage with the following hierarchy:
    >>> # / ()
    >>> # ├─ A (Xform)    --> with local position: (1.0, 2.0, 3.0)
    >>> # │  ├─ B (Xform) --> with local position: (4.0, 5.0, 6.0)
    >>> translation, orientation = xform_utils.get_world_pose("/A/B")
    >>> print(translation)  
    [5. 7. 9.]
    >>> print(orientation)
    [1. 0. 0. 0.]
    ```

set\_local\_pose( : *prim: str | Usd.Prim | usdrt.Usd.Prim*, : *\**, : *translation: list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *orientation: list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, ) → [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None")
:   Set the local pose of a prim.

    Backends: usd, usdrt, fabric.

    Warning

    This function is not implemented for the usd backend.
    Use [`set_local_poses()`](../../isaacsim.core.experimental.prims/docs/index.html#isaacsim.core.experimental.prims.XformPrim.set_local_poses "isaacsim.core.experimental.prims.XformPrim.set_local_poses") instead of what is being implemented.

    Parameters:
    :   * **prim** – Prim path or prim instance.
        * **translation** – Translation in the local frame (shape `(3,)`).
        * **orientation** – Orientation in the local frame (shape `(4,)`, quaternion `wxyz`).

    Raises:
    :   **NotImplementedError** – If the backend is USD.

    Example:

    ```python
    >>> import isaacsim.core.experimental.utils.xform as xform_utils
    >>>
    >>> # given the stage with the following hierarchy:
    >>> # / ()
    >>> # ├─ A (Xform)    --> with local position: (1.0, 2.0, 3.0)
    >>> # │  ├─ B (Xform) --> with local position: (4.0, 5.0, 6.0)
    >>> xform_utils.set_local_pose("/A/B", translation=[-4.0, -5.0, -6.0])
    ```

set\_world\_pose( : *prim: str | Usd.Prim | usdrt.Usd.Prim*, : *\**, : *position: list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, : *orientation: list | np.ndarray | wp.array | [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None") = None*, ) → [None](../../isaacsim.asset.gen.omap/docs/index.html#isaacsim.asset.gen.omap.bindings._omap.Generator.None "isaacsim.asset.gen.omap.bindings._omap.Generator.None")
:   Set the world pose of a prim.

    Backends: usd, usdrt, fabric.

    Warning

    This function is not implemented for the usd backend.
    Use [`set_world_poses()`](../../isaacsim.core.experimental.prims/docs/index.html#isaacsim.core.experimental.prims.XformPrim.set_world_poses "isaacsim.core.experimental.prims.XformPrim.set_world_poses") instead of what is being implemented.

    Parameters:
    :   * **prim** – Prim path or prim instance.
        * **position** – Position in the world frame (shape `(3,)`).
        * **orientation** – Orientation in the world frame (shape `(4,)`, quaternion `wxyz`).

    Raises:
    :   **NotImplementedError** – If the backend is USD.

    Example:

    ```python
    >>> import isaacsim.core.experimental.utils.xform as xform_utils
    >>>
    >>> # given the stage with the following hierarchy:
    >>> # / ()
    >>> # ├─ A (Xform)    --> with local position: (1.0, 2.0, 3.0)
    >>> # │  ├─ B (Xform) --> with local position: (4.0, 5.0, 6.0)
    >>> xform_utils.set_world_pose("/A/B", position=[-4.0, -5.0, -6.0])
    ```

On this page

* [Overview](#overview)
  + [Functionality](#functionality)
    - [Application Management](#application-management)
    - [Stage Operations](#stage-operations)
    - [Prim Utilities](#prim-utilities)
    - [Transform Operations](#transform-operations)
    - [Pose Manipulation](#pose-manipulation)
  + [Key Components](#key-components)
    - [Backend System](#backend-system)
    - [Data Operations](#data-operations)
    - [Semantic Labeling](#semantic-labeling)
  + [Integration](#integration)
* [Enable Extension](#enable-extension)
* [Python API](#python-api)
  + [App Utils](#module-isaacsim.core.experimental.utils.impl.app)
    - [`enable_extension()`](#isaacsim.core.experimental.utils.impl.app.enable_extension)
    - [`get_extension_dict()`](#isaacsim.core.experimental.utils.impl.app.get_extension_dict)
    - [`get_extension_id()`](#isaacsim.core.experimental.utils.impl.app.get_extension_id)
    - [`get_extension_path()`](#isaacsim.core.experimental.utils.impl.app.get_extension_path)
    - [`is_extension_enabled()`](#isaacsim.core.experimental.utils.impl.app.is_extension_enabled)
    - [`is_paused()`](#isaacsim.core.experimental.utils.impl.app.is_paused)
    - [`is_playing()`](#isaacsim.core.experimental.utils.impl.app.is_playing)
    - [`is_stopped()`](#isaacsim.core.experimental.utils.impl.app.is_stopped)
    - [`pause()`](#isaacsim.core.experimental.utils.impl.app.pause)
    - [`play()`](#isaacsim.core.experimental.utils.impl.app.play)
    - [`stop()`](#isaacsim.core.experimental.utils.impl.app.stop)
    - [`update_app()`](#isaacsim.core.experimental.utils.impl.app.update_app)
    - [`update_app_async()`](#isaacsim.core.experimental.utils.impl.app.update_app_async)
  + [Backend Utils](#module-isaacsim.core.experimental.utils.impl.backend)
    - [`SimStateMode`](#isaacsim.core.experimental.utils.impl.backend.SimStateMode)
      * [`DISABLED`](#isaacsim.core.experimental.utils.impl.backend.SimStateMode.DISABLED)
      * [`EXCLUSIVE`](#isaacsim.core.experimental.utils.impl.backend.SimStateMode.EXCLUSIVE)
      * [`MIRROR`](#isaacsim.core.experimental.utils.impl.backend.SimStateMode.MIRROR)
    - [`get_current_backend()`](#isaacsim.core.experimental.utils.impl.backend.get_current_backend)
    - [`get_simstate_mode()`](#isaacsim.core.experimental.utils.impl.backend.get_simstate_mode)
    - [`is_backend_set()`](#isaacsim.core.experimental.utils.impl.backend.is_backend_set)
    - [`should_raise_on_fallback()`](#isaacsim.core.experimental.utils.impl.backend.should_raise_on_fallback)
    - [`should_raise_on_unsupported()`](#isaacsim.core.experimental.utils.impl.backend.should_raise_on_unsupported)
    - [`use_backend()`](#isaacsim.core.experimental.utils.impl.backend.use_backend)
  + [Foundation Utils](#module-isaacsim.core.experimental.utils.impl.foundation)
    - [`get_value_type_names()`](#isaacsim.core.experimental.utils.impl.foundation.get_value_type_names)
    - [`resolve_value_type_name()`](#isaacsim.core.experimental.utils.impl.foundation.resolve_value_type_name)
    - [`value_type_name_to_str()`](#isaacsim.core.experimental.utils.impl.foundation.value_type_name_to_str)
  + [Ops Utils](#module-isaacsim.core.experimental.utils.impl.ops)
    - [`broadcast_to()`](#isaacsim.core.experimental.utils.impl.ops.broadcast_to)
    - [`parse_device()`](#isaacsim.core.experimental.utils.impl.ops.parse_device)
    - [`place()`](#isaacsim.core.experimental.utils.impl.ops.place)
    - [`resolve_indices()`](#isaacsim.core.experimental.utils.impl.ops.resolve_indices)
  + [Prim Utils](#module-isaacsim.core.experimental.utils.impl.prim)
    - [`create_prim_attribute()`](#isaacsim.core.experimental.utils.impl.prim.create_prim_attribute)
    - [`ensure_api()`](#isaacsim.core.experimental.utils.impl.prim.ensure_api)
    - [`find_matching_prim_paths()`](#isaacsim.core.experimental.utils.impl.prim.find_matching_prim_paths)
    - [`get_all_matching_child_prims()`](#isaacsim.core.experimental.utils.impl.prim.get_all_matching_child_prims)
    - [`get_first_matching_child_prim()`](#isaacsim.core.experimental.utils.impl.prim.get_first_matching_child_prim)
    - [`get_first_matching_parent_prim()`](#isaacsim.core.experimental.utils.impl.prim.get_first_matching_parent_prim)
    - [`get_prim_at_path()`](#isaacsim.core.experimental.utils.impl.prim.get_prim_at_path)
    - [`get_prim_attribute_names()`](#isaacsim.core.experimental.utils.impl.prim.get_prim_attribute_names)
    - [`get_prim_attribute_value()`](#isaacsim.core.experimental.utils.impl.prim.get_prim_attribute_value)
    - [`get_prim_path()`](#isaacsim.core.experimental.utils.impl.prim.get_prim_path)
    - [`get_prim_variant_collection()`](#isaacsim.core.experimental.utils.impl.prim.get_prim_variant_collection)
    - [`get_prim_variants()`](#isaacsim.core.experimental.utils.impl.prim.get_prim_variants)
    - [`has_api()`](#isaacsim.core.experimental.utils.impl.prim.has_api)
    - [`is_prim_non_root_articulation_link()`](#isaacsim.core.experimental.utils.impl.prim.is_prim_non_root_articulation_link)
    - [`set_prim_variants()`](#isaacsim.core.experimental.utils.impl.prim.set_prim_variants)
  + [Semantics Utils](#module-isaacsim.core.experimental.utils.impl.semantics)
    - [`add_labels()`](#isaacsim.core.experimental.utils.impl.semantics.add_labels)
    - [`get_labels()`](#isaacsim.core.experimental.utils.impl.semantics.get_labels)
    - [`remove_all_labels()`](#isaacsim.core.experimental.utils.impl.semantics.remove_all_labels)
    - [`remove_labels()`](#isaacsim.core.experimental.utils.impl.semantics.remove_labels)
    - [`upgrade_prim_semantics_to_labels()`](#isaacsim.core.experimental.utils.impl.semantics.upgrade_prim_semantics_to_labels)
  + [Stage Utils](#module-isaacsim.core.experimental.utils.impl.stage)
    - [`add_reference_to_stage()`](#isaacsim.core.experimental.utils.impl.stage.add_reference_to_stage)
    - [`close_stage()`](#isaacsim.core.experimental.utils.impl.stage.close_stage)
    - [`create_new_stage()`](#isaacsim.core.experimental.utils.impl.stage.create_new_stage)
    - [`create_new_stage_async()`](#isaacsim.core.experimental.utils.impl.stage.create_new_stage_async)
    - [`define_prim()`](#isaacsim.core.experimental.utils.impl.stage.define_prim)
    - [`delete_prim()`](#isaacsim.core.experimental.utils.impl.stage.delete_prim)
    - [`generate_next_free_path()`](#isaacsim.core.experimental.utils.impl.stage.generate_next_free_path)
    - [`generate_stage_representation()`](#isaacsim.core.experimental.utils.impl.stage.generate_stage_representation)
    - [`get_current_stage()`](#isaacsim.core.experimental.utils.impl.stage.get_current_stage)
    - [`get_stage_id()`](#isaacsim.core.experimental.utils.impl.stage.get_stage_id)
    - [`get_stage_time_code()`](#isaacsim.core.experimental.utils.impl.stage.get_stage_time_code)
    - [`get_stage_units()`](#isaacsim.core.experimental.utils.impl.stage.get_stage_units)
    - [`get_stage_up_axis()`](#isaacsim.core.experimental.utils.impl.stage.get_stage_up_axis)
    - [`is_stage_loading()`](#isaacsim.core.experimental.utils.impl.stage.is_stage_loading)
    - [`is_stage_set()`](#isaacsim.core.experimental.utils.impl.stage.is_stage_set)
    - [`move_prim()`](#isaacsim.core.experimental.utils.impl.stage.move_prim)
    - [`open_stage()`](#isaacsim.core.experimental.utils.impl.stage.open_stage)
    - [`open_stage_async()`](#isaacsim.core.experimental.utils.impl.stage.open_stage_async)
    - [`save_stage()`](#isaacsim.core.experimental.utils.impl.stage.save_stage)
    - [`set_stage_time_code()`](#isaacsim.core.experimental.utils.impl.stage.set_stage_time_code)
    - [`set_stage_units()`](#isaacsim.core.experimental.utils.impl.stage.set_stage_units)
    - [`set_stage_up_axis()`](#isaacsim.core.experimental.utils.impl.stage.set_stage_up_axis)
    - [`use_stage()`](#isaacsim.core.experimental.utils.impl.stage.use_stage)
  + [Transform Utils](#module-isaacsim.core.experimental.utils.impl.transform)
    - [`compute_relative_transform()`](#isaacsim.core.experimental.utils.impl.transform.compute_relative_transform)
    - [`euler_angles_to_quaternion()`](#isaacsim.core.experimental.utils.impl.transform.euler_angles_to_quaternion)
    - [`euler_angles_to_rotation_matrix()`](#isaacsim.core.experimental.utils.impl.transform.euler_angles_to_rotation_matrix)
    - [`look_at_matrix()`](#isaacsim.core.experimental.utils.impl.transform.look_at_matrix)
    - [`look_at_quaternion()`](#isaacsim.core.experimental.utils.impl.transform.look_at_quaternion)
    - [`quaternion_conjugate()`](#isaacsim.core.experimental.utils.impl.transform.quaternion_conjugate)
    - [`quaternion_multiplication()`](#isaacsim.core.experimental.utils.impl.transform.quaternion_multiplication)
    - [`quaternion_to_euler_angles()`](#isaacsim.core.experimental.utils.impl.transform.quaternion_to_euler_angles)
    - [`quaternion_to_rotation_matrix()`](#isaacsim.core.experimental.utils.impl.transform.quaternion_to_rotation_matrix)
    - [`rotation_matrix_to_quaternion()`](#isaacsim.core.experimental.utils.impl.transform.rotation_matrix_to_quaternion)
  + [Xform Utils](#module-isaacsim.core.experimental.utils.impl.xform)
    - [`get_local_pose()`](#isaacsim.core.experimental.utils.impl.xform.get_local_pose)
    - [`get_relative_transform()`](#isaacsim.core.experimental.utils.impl.xform.get_relative_transform)
    - [`get_world_pose()`](#isaacsim.core.experimental.utils.impl.xform.get_world_pose)
    - [`set_local_pose()`](#isaacsim.core.experimental.utils.impl.xform.set_local_pose)
    - [`set_world_pose()`](#isaacsim.core.experimental.utils.impl.xform.set_world_pose)