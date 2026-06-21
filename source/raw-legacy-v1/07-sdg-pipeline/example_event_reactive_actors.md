---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/action_and_event_data_generation/example_event_reactive_actors.html
title: "Event Reactive Actors"
section: "Pipeline"
module: "07-sdg-pipeline"
checksum: "c1a553f8bde75df7"
fetched: "2026-06-21T13:58:17"
---

* [Synthetic Data Generation](../synthetic_data_generation/index.html)
* [Action and Event Data Generation](index.html)
* Reacting to Events with Actor Triggers

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Reacting to Events with Actor Triggers

This example shows how Event Generation (`isaacsim.replicator.incident`) and Actor Synthetic Data Generation (SDG) (`isaacsim.replicator.agent`) can be wired together end-to-end **without writing a single line of Python**. You edit two YAML config files and drive the two extensions from their Omniverse windows.

At runtime, Event Generation fires a fire event in the warehouse, which dispatches a [carb event](https://docs.omniverse.nvidia.com/dev-guide/latest/programmer_ref/events.html); Actor SDG characters subscribe to that carb event through `event_trigger` and swap their behavior: pause briefly, walk to a safe point, stand still, and finally resume their wander routine.

## Prerequisites

* Both extensions are enabled. Refer to [Enable Extensions](tutorial_replicator_agent.html#actor-sim-enable-extensions) for the Actor SDG side; the Event Generation extension is enabled automatically by the same Action and Event Data Generation app launch.
* Familiarity with the standalone tutorials is helpful, but not required:

  + [Actor Simulation and Synthetic Data Generation](tutorial_replicator_agent.html#isaac-sim-app-tutorial-replicator-character)
  + [Physical Space Event Generation](tutorial_replicator_incident.html#isaac-sim-app-tutorial-replicator-incident)

## How the Two Extensions Connect

The two extensions have no direct API coupling. They connect through the **carb event bus** that every extension in a Kit app instance shares. Event Generation dispatches a named carb event when an incident fires, and Actor SDG’s `event_trigger` listens for that same name. A matching string is the only contract between them.

The dispatched event name is always:

```python
isaacsim.replicator.incident.core.events/<event_name>
```

Replace `<event_name>` with whatever you put under `FireEvent.name` (or `SpillEvent.name`) in the Event Generation YAML. The extension interpolates the event name into the dispatched string exactly as written. Use underscores instead of spaces; a space in `name` causes the actor’s `event_trigger` lookup to silently fail.

Only `FireEvent` and `SpillEvent` dispatch carb events. `ToppleEvent` currently signals only within Event Generation and cannot drive an actor trigger. For the complete list of trigger types incidents support (including chaining one incident from another), refer to [Triggers](tutorial_replicator_incident.html#iri-trigger-section).

## Step 1 - Author the Event Generation YAML

Save the following as `incident_config.yaml` anywhere on disk:

```python
isaacsim.replicator.incident:
  version: 0.1.0
  global:
    report_dir: ~/EventsResult
    seed: 42
  event:
    event_list:
      - FireEvent:
          name: warehouse_fire
          flammable_item:
            item: $random_flammable_item$
            flammable_nearby_radius: 1.5
          trigger:
            type: time
            time: 4
```

The `time: 4` is seconds counted from when the timeline starts playing. The extension resolves `$random_flammable_item$` at setup time by scanning the stage for prims tagged `IsaacSim_Replicator_Incident_Attr:FlammableItem`.

## Step 2 - Author the Actor SDG YAML

Save as `agent_config.yaml`. The trigger’s `event:` string must match what Step 1 dispatches exactly.

```python
isaacsim.replicator.agent:
  version: 1.6.0
  seed: 42
  simulation_duration: 25.0
  environment:
    base_stage_asset_path: Isaac/Environments/Simple_Warehouse/full_warehouse.usd
  sensor:
    groups:
      sensor_group_00:
        num: 1
        aim_at_targets: {}
  character:
    groups:
      warehouse_workers:
        num: 2
        routines:
          - wander:
              weight: 1.0
              repeat: 1
              walk:
                speed_range: [1.0, 1.0]
                distance_range: [5.0, 10.0]
                navigation_areas: []
              idle:
                - animation: idle
                  weight: 1.0
                  time_range: [3.0, 5.0]
        triggers:
          - event_trigger:
              event: isaacsim.replicator.incident.core.events/warehouse_fire
              priority: 10
              behavior:
                - stop:
                    weight: 1.0
                    repeat: 1
                    time_range: [1.0, 2.0]
                - patrol:
                    weight: 1.0
                    repeat: 1
                    speed_range: [3.0, 4.0]
                    path_points:
                      - [0.0, 0.0, 0.0]
                - stop:
                    weight: 1.0
                    repeat: 1
                    time_range: [10.0, 15.0]
  replicator:
    writers:
      IRABasicWriter:
        output_dir: ~/out_event_reactive_actors
        rgb: true
        camera_params: true
```

A few notes on this config:

* The `sensor` block creates a single placeholder camera. The trigger does not require it, but the Configuration Editor populates it by default; leaving it in place keeps the YAML round-trippable through the editor UI.
* `weight`, `repeat`, and `navigation_areas: []` are shown explicitly even though each is a default. This example surfaces them so that you can see what the Configuration Editor writes out and modify the values in place.
* The trigger’s `behavior` list runs **in order**: a brief 1-2 second stop, then a patrol to `(0, 0, 0)`, then a 10-15 second stop. After the list completes, the actor resumes its routine.

Important

Both extensions operate on whichever stage Actor SDG loads, because they share a single Kit stage. If you point Actor SDG at an untagged warehouse, Event Generation logs `'$random_flammable_item$' is not a tagged prim` and no event fires. Either tag a prim manually (Step 5) or load a pre-tagged stage such as `Isaac/Samples/Replicator/Incidents/full_warehouse_with_incident_tags.usd`.

## Step 3 - Launch the App

From the Isaac Sim install directory:

```python
./isaac-sim.action_and_event_data_generation.sh --/rtx/hydra/supportMultiTickRate=false
```

This opens `isaacsim.exp.action_and_event_data_generation.full.kit`, which enables both Actor SDG and Event Generation UIs. Two menu entries appear under **Tools > Action and Event Data Generation**:

* **Actor SDG** – Actor SDG’s config window.
* **Event Config File** – Event Generation’s config window.

Open both from the **Tools** menu and they dock side by side.

Note

The `--/rtx/hydra/supportMultiTickRate=false` override is required for fire effects
to render correctly during the `FireEvent`. Refer to
[the multi-tick rendering warning](tutorial_replicator_incident.html#iri-fire-multitick-warning)
for background and alternative ways to apply the setting.

## Step 4 - Set Up Actor SDG

In the **Actor SDG** window:

1. Click the **Select A Configuration File** field (or paste the path to `agent_config.yaml`).
2. Once the path is set, click **Set Up Simulation**.

Internally this opens the warehouse stage, instantiates two `warehouse_workers` characters with their wander routine, and attaches a carb-event listener to each character already subscribed to `isaacsim.replicator.incident.core.events/warehouse_fire`. The subscription is live before you touch anything else.

Do **not** start the timeline yet. Avoid both **Start Data Generation** and the **Play** button, because Event Generation’s time countdown begins as soon as the timeline plays. Complete Step 5 first.

## Step 5 - Set Up Event Generation

Open the **Event Config File** window from **Tools > Action and Event Data Generation > Event Config File** if it is not already open. The menu entry only appears when the `isaacsim.replicator.incident.ui` extension is enabled, which the `action_and_event_data_generation` app launched in Step 3 does automatically. Then:

1. Use the **Config File Path** picker to select `incident_config.yaml`.
2. In the **Stage** window, select any box prim on a shelf (for example, `/Root/Box_21069` from the Simple Warehouse stage).
3. In the **Property** panel for the selected prim, click **+ Add > IncidentTagging > FlammableItem > Box**.
4. Click **Set Up Incident**.

If you adapt this example to use `SpillEvent` or `ToppleEvent`, choose **LeakableItem** or **LooseItem** under **+ Add > IncidentTagging** instead, before clicking **Set Up Incident**.

Internally, Event Generation reads the YAML, waits for navmesh baking, picks the tagged prim as the flammable target, and arms a time trigger that will fire at `t = 4 s` after the timeline plays. Nothing has fired yet.

The Global section’s Seed field should populate to `42`, and the event list should show `warehouse_fire`.

## Step 6 - Play and Watch

You have two ways to start the simulation:

* **Play** button – in the Toolbar on the left side of the viewport. It plays the timeline only and writes no data. Useful for previewing the event and behavior sequence.
* **Start Data Generation** (**Actor SDG** window) – plays the timeline *and* runs the Replicator writers configured in the `replicator` section to capture synthetic data. `simulation_duration: 25.0` stops playback automatically when the run completes; `IRABasicWriter` output appears under `~/out_event_reactive_actors/` in your home directory.

Either way, verify that you receive:

On this page

* [Prerequisites](#prerequisites)
* [How the Two Extensions Connect](#how-the-two-extensions-connect)
* [Step 1 - Author the Event Generation YAML](#step-1-author-the-event-generation-yaml)
* [Step 2 - Author the Actor SDG YAML](#step-2-author-the-actor-sdg-yaml)
* [Step 3 - Launch the App](#step-3-launch-the-app)
* [Step 4 - Set Up Actor SDG](#step-4-set-up-actor-sdg)
* [Step 5 - Set Up Event Generation](#step-5-set-up-event-generation)
* [Step 6 - Play and Watch](#step-6-play-and-watch)