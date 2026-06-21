---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/action_and_event_data_generation/tutorial_omni_metropolis_pipeline.html
title: "Metropolis Pipeline"
section: "Pipeline"
module: "07-sdg-pipeline"
checksum: "e8f1ba9dead6b4da"
fetched: "2026-06-21T11:55:37"
---

* [Synthetic Data Generation](../synthetic_data_generation/index.html)
* [Action and Event Data Generation](index.html)
* Omni Metropolis Pipeline

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Omni Metropolis Pipeline

The `omni.metropolis.pipeline` extension provides a shared configuration, trigger, and agent layer used by Action and Event Data Generation extensions.

It supplies the **ConfigurationManager**, a singleton that loads YAML configuration files, parses sections per extension, and runs async setup so extensions can configure the application from a single config file.
It also supplies the **TriggersManager** and built-in trigger types so that events (such as those from [Physical Space Event Generation](tutorial_replicator_incident.html#isaac-sim-app-tutorial-replicator-incident)) can be started at a specific time, on a carb event, or on a physics collision.
It also supplies the **AgentManager** and base agent interface so that agents (such as those from [Actor Simulation and Synthetic Data Generation](tutorial_replicator_agent.html#isaac-sim-app-tutorial-replicator-character)) can be created and managed.

## Overview

* **Configuration** â YAML-driven application setup

  + **ConfigurationManager** â Singleton that loads a config file and dispatches sections to registered extensions. Extensions register a section parser and async setup function that are used when the config file is loaded and the simulation is set up.
* **Triggers** â event objects that run callbacks when they fire

  + **TriggersManager** â Singleton that creates and manages trigger instances from a dictionary description. Use it to create triggers in script and pass them into incident (fire, topple, spill) and other event APIs.
  + **Trigger types** â Time-based, carb-event-based, and collision-based triggers are registered by the extension at startup. Each trigger can have callbacks added using `add_callback`; when the trigger fires, all callbacks are invoked.
* **Agents** â runtime representations of entities that can perform routines and respond to triggers

  + **AgentManager** â Singleton that creates and manages agent instances from a dictionary description. Use it to create agents in script and pass them into agent APIs.
  + **Base agent interface** â The base agent interface is a USD Prim that defines the agentâs behavior and trigger. It is used to create and manage agents.

## Configuration

The **ConfigurationManager** loads a YAML config file and routes sections to extensions that have registered a parser and setup function. The config file currently supports the `isaacsim.replicator.agent` extension. Refer to the [Configuration File Guide](ext_replicator-agent/ext_isaacsim_replicator_agent_configuration.html#ira-configuration-file) for more formatting information.

### Using ConfigurationManager in Script

Access the singleton using `ConfigurationManager.get_instance()` or use the module-level functions from `omni.metropolis.pipeline.configuration`. Register your extensionâs section before loading a config file; then call `load_config_file(path)` and `await setup_simulation()`.

**Registration**

* **register\_config\_section(extension\_name, section\_header, section\_name, section\_parser, section\_setup)** â Register a config section. `section_header` is the YAML top-level key (for example, `"omni.metropolis.pipeline"` or `"isaacsim.replicator.agent.core"`). `section_name` is the key under the orchestrator header (for example, `"agent"`). `section_parser` is a callable that accepts the raw dict for that section and returns parsed data. `section_setup` is an async callable that receives the parsed payload and runs when `setup_simulation()` is called.
* **is\_section\_registered(extension\_name)** â Return whether that extension has registered a section.
* **unregister\_config\_section(extension\_name)** â Remove the registration.

**Loading and access**

* **load\_config\_file(file\_path)** â Load and parse the YAML file. Returns `True` on success. Use `get_load_error_message()` if it returns `False`.
* **get\_config(extension\_name)** â Return the parsed configuration for that extension, or `None` if not present or not loaded.
* **get\_config\_file\_path()** â Return the path of the currently loaded config file, or `None`.

**Setup**

* **setup\_simulation()** â Async. Run each registered extensionâs setup function with its parsed config. Returns `True` if all succeeded. Use `get_setup_error_message()` on failure.

### Example Usage

```python
import asyncio
from pathlib import Path
from omni.metropolis.pipeline.configuration import (
    get_config,
    get_load_error_message,
    get_setup_error_message,
    load_config_file,
    register_config_section,
    setup_simulation,
)

def parse_my_section(raw: dict):
    # Parser receives {section_header: section_data}. Return any structure your setup needs.
    return next(iter(raw.values()), {})

async def setup_my_section(parsed):
    # Run async setup using parsed config (for example, create prims, load assets).
    pass

# Register before loading. Use section_header and section_name that match your YAML.
register_config_section(
    extension_name="my.extension.name",
    section_header="my.extension.name.core",
    section_name="my_section",
    section_parser=parse_my_section,
    section_setup=setup_my_section,
)

if load_config_file(Path("/path/to/config.yaml")):
    if asyncio.run(setup_simulation()):
        config = get_config("my.extension.name")
        # Use config as needed.
    else:
        print(get_setup_error_message())
else:
    print(get_load_error_message())
```

## Triggers

### Using TriggersManager in Script

Get the manager singleton and create triggers from a dictionary. For a complete script example that creates a time trigger, adds a callback, and passes the trigger into IRI event managers (fire, topple, spill), refer to [Physical Space Event Generation](tutorial_replicator_incident.html#isaac-sim-app-tutorial-replicator-incident) and the [Event Configuration in IRI Script](tutorial_replicator_incident.html#iri-conifg-script) and [Triggers](tutorial_replicator_incident.html#iri-trigger-section) sections there.

**Prerequisites**

* Enable `isaacsim.replicator.incident.core` when using triggers with IRI events.
* The `omni.metropolis.pipeline` extension is loaded automatically when using the Action and Event Data Generation application.

### Trigger Types

The extension registers these trigger types. Use the `type` field in the trigger dictionary and the corresponding parameters. For YAML and script examples of each trigger type with IRI events, refer to [Triggers](tutorial_replicator_incident.html#iri-trigger-section) in the Physical Space Event Generation tutorial.

**time**

Fires when the simulation timeline reaches the given time (in seconds). Dictionary shape: `{"trigger": {"type": "time", "time": <seconds>}}`.

**carb\_event**

Fires when the named carb event is dispatched. Optional payload is available on the trigger after firing. Dictionary shape: `{"trigger": {"type": "carb_event", "event_name": "<event_name>"}}`.

**collision**

Fires on physics trigger enter/exit for a collider prim. The collider must have CollisionAPI, TriggerAPI, and RigidbodyAPI. Optionally filter by other collider names using the `metro:collider:name` attribute. Parameters: `collider_prim_path`, `trigger_enter`, `trigger_exit`, `other_collider_names`.

### Trigger API Summary

* **TriggersManager.get\_instance()** â Return the singleton TriggersManager.
* **create\_trigger\_by\_dict(dict\_data)** â Build a trigger from `{"trigger": {"type": "...", ...}}`. Returns a trigger instance or `None` if no registered type matches.
* **TriggerBase.add\_callback(callback\_fn)** â Add a callable that takes the trigger instance as an argument; it is invoked when the trigger fires.
* **TriggerBase.destroy()** â Unsubscribe from timeline/events and clear callbacks. Call when the trigger is no longer needed.

### Example Usage

```python
import carb
from omni.metropolis.pipeline.triggers import TriggersManager

def callback(trigger):
    carb.log_info("Trigger fired!")

# Register a callback on a time trigger that fires at 1 second
trigger_manager = TriggersManager.get_instance()
trigger = trigger_manager.create_trigger_by_dict({"trigger": {"type": "time", "time": 1.0}})
trigger.add_callback(callback)
```

## Agents

### Using AgentManager in Script

For creating and configuring agents in the Action and Event Data Generation application (YAML, UI), refer to [Actor Simulation and Synthetic Data Generation](tutorial_replicator_agent.html#isaac-sim-app-tutorial-replicator-character).

### Example Usage

The following pattern registers a custom agent class and creates a prim with the agentâs API. When the timeline plays, AgentsManager discovers the prim and instantiates the agent; when the timeline stops, runtime instances are cleared.

```python
from typing import ClassVar
from pxr import Usd, UsdPhysics
import carb
import omni.usd
import omni.timeline
from omni.metropolis.pipeline.agent import Agent, AgentsManager

class MyAgent(Agent):
    AGENT_API: ClassVar[Usd.APISchemaBase] = UsdPhysics.RigidBodyAPI

    def get_world_position(self):
        return carb.Float3(0, 0, 0)

    def get_world_rotation(self):
        return carb.Float4(0, 0, 0, 1)

    def get_speed(self):
        return 0.0

    def get_facing_direction(self):
        return carb.Float3(1, 0, 0)

    def get_current_task_name(self):
        return None

    def on_update(self, delta_time: float):
        pass  # Custom behavior each frame

# Create a prim with the agent API so the manager can discover it
stage = omni.usd.get_context().get_stage()
stage.DefinePrim("/World", "Xform")
prim = stage.DefinePrim("/World/MyAgent", "Xform")
UsdPhysics.RigidBodyAPI.Apply(prim)

# Register the agent class and play to collect runtime instances
manager = AgentsManager.get_instance()
manager.register_agent_class(MyAgent)

timeline = omni.timeline.get_timeline_interface()
timeline.play()
# After play, manager.get_runtime_agent_instances() will contain MyAgent instances
# for each prim that has RigidBodyAPI. Call timeline.stop() to clear them.
```

On this page

* [Overview](#overview)
* [Configuration](#configuration)
  + [Using ConfigurationManager in Script](#using-configurationmanager-in-script)
  + [Example Usage](#example-usage)
* [Triggers](#triggers)
  + [Using TriggersManager in Script](#using-triggersmanager-in-script)
  + [Trigger Types](#trigger-types)
  + [Trigger API Summary](#trigger-api-summary)
  + [Example Usage](#id1)
* [Agents](#agents)
  + [Using AgentManager in Script](#using-agentmanager-in-script)
  + [Example Usage](#id2)