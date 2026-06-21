---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/robot_setup/ext_isaacsim_robot_setup_collision_detector.html
title: "Collision Detector"
section: "Setup 工具"
module: "07-robot-setup"
checksum: "1f233d55169f2294"
fetched: "2026-06-21T14:14:33"
---

* [Robot Setup](index.html)
* [Editor Tools](editing_tools.html)
* Robot Self-Collision Detector

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Robot Self-Collision Detector

## About

The [Robot Self-Collision Detector](#isaac-collision-detector) extension detects and manages self-collision pairs between the rigid body links of a robot articulation.
During physics simulation, pairs of colliders that overlap in their initial configuration generate unwanted contact forces that destabilize the robot.
This tool enumerates those pairs and lets you mark them as **Filtered Pairs** using the `UsdPhysics.FilteredPairsAPI`, so the physics engine ignores contact between them.

To access this extension, go to the top menu bar and click **Tools > Robotics > Asset Editors > Robot Self-Collision Detector**.
This extension is enabled by default. If it is ever disabled, it can be re-enabled from the [Extension Manager](https://docs.omniverse.nvidia.com/extensions/latest/ext_core/ext_extension-manager.html "(in Omniverse Extensions)")
by searching for `isaacsim.robot_setup.collision_detector`.

### When to Use

Use this tool after importing or authoring a robot asset whose collision meshes overlap at rest.
Common scenarios include:

* Newly imported URDF/MJCF robots that have adjacent-link colliders intersecting at joint boundaries.
* Robots with dense collision geometry (e.g. dexterous hands) where many links are in close proximity.
* Adding collision filtering as a physics feature layer on an existing asset following the [asset structure guidelines](asset_structure.html#isaac-sim-app-reference-asset-structure).

## User Interface

### Robot Selection

* **Robot dropdown**: Lists all prims on the stage that have the Robot Schema applied. Select the robot you want to inspect.
* **Check Collisions button**: Runs collision detection on the selected robot and populates the results table.

### Options

* **Include environment collisions**: When enabled, the results also include collision pairs between robot links and non-robot bodies in the scene (e.g. a table or ground plane).

### Collision Pairs Table

The table has three columns:

| Column | Content | Description |
| --- | --- | --- |
| **Rigid Body A** | Color swatch + link name | First body in the collision pair. Click the focal icon to select its collision prims in the Stage window. |
| **Rigid Body B** | Color swatch + link name | Second body in the collision pair. Same focal-icon behavior. |
| **Filtered Pair** | Checkbox | Toggle on to add a `FilteredPairsAPI` relationship so the physics engine ignores this contact. Toggle off to remove it. |

Additional table interactions:

* **Search bar**: Filter rows by body name (case-insensitive).
* **Column sorting**: Click the header sort icon to toggle alphabetical ordering.
* **Row selection**: Click a row to highlight both bodies in the viewport with distinct colors, making it easy to visually locate the pair. Clicking elsewhere in the viewport clears the table selection.
* **Keyboard navigation**: Press `Ctrl+Up` / `Ctrl+Down` to move the row selection up or down. When multiple rows are selected the entire block shifts together.
* **Batch toggle**: Select multiple rows and toggle one checkbox to apply the same filtered state to all selected pairs.
* **No collisions**: When no self-collisions are detected an overlay message is shown in place of the table.

### Viewport Highlighting

When a collision pair row is selected, the two rigid bodies are highlighted in the viewport using distinct colors from a 64-color palette. Each body receives a colored selection-group outline so you can distinguish them at a glance. If the viewport selection outline setting is disabled, the panel temporarily enables it for the duration of the selection and restores the original setting when the selection is cleared, the panel is hidden, or the extension shuts down.

## Example Usage: Unitree Dex5 Hand

This walkthrough uses the **Isaac/Robots/Unitree/Dex5/Dex5-URDF-R.usda** asset from the Isaac Sim asset library.

### 1. Open the Robot Asset

Open or reference the Dex5 hand asset onto your stage:

**File > Open** or drag it from the Content Browser at `Isaac/Robots/Unitree/Dex5/Dex5-URDF-R.usda`.

### 2. Open the Self-Collision Detector

Navigate to **Tools > Robotics > Asset Editors > Robot Self-Collision Detector**.

The panel opens docked at the bottom-left of the editor, adjacent to the Content window.

### 3. Select the Robot and Detect Collisions

The robot dropdown auto-populates with every prim on the stage that has the Robot Schema applied. It automatically selects the first robot on the stage, and checks collisions. If you made modifications to the robot, click **Check Collisions** to update the results.

The tool queries the physics engine for all collider pairs that overlap in the robot’s current configuration, maps each collider to its owning rigid body link, and populates the table.

### 4. Inspect a Collision Pair

Click a row to highlight both bodies in the viewport. Each body is drawn with a unique color so you can visually confirm whether the overlap is expected (e.g. adjacent finger segments) or unintended.

Click the **focal icon** (crosshair) next to a body name to select only that body in the viewport and the Stage window. The table row is selected (or kept selected if it already was), but only the clicked body receives the colored outline, making it easy to isolate one side of the pair. Clicking the focal icon on the other body in the same row switches the viewport highlight without changing the selected row.

### 5. Filter Collision Pairs

For each pair that should be ignored by the physics engine, check the **Filtered Pair** checkbox. This writes a `UsdPhysics.FilteredPairsAPI` relationship to the stage.

To filter multiple pairs at once, select the desired rows (hold `Ctrl` or `Shift` while clicking), then toggle one checkbox. All selected rows are updated together.

Note

Other ways to resolve for the collision pairs are to adjust the collision geometry, or modify the robot starting pose using the [Robot Poser](robot_poser.html#isaac-sim-robot-poser) extension. Filtered pairs are displayed in the self-collision detector, so you can easily see which pairs are being ignored, but whenever a pair is not filtered nor is detected by the collision engine, it will not be displayed in the self-collision detector. When the robot has the self-collision disabled in the articulation root, no collision pairs will be detected by the collision engine, and a message will be displayed on the table.

### 6. Inspect Multiple Collision Pairs

You can select multiple rows to highlight multiple pairs in the viewport. Hold `Ctrl` or `Shift` while clicking to select multiple rows.
To quickly move the selection up or down, press `Ctrl+Up` or `Ctrl+Down`.

## Further Learning

* [Asset Structure](asset_structure.html#isaac-sim-app-reference-asset-structure) for the recommended robot asset layering structure.
* [UsdPhysics.FilteredPairsAPI](https://openusd.org/release/api/class_usd_physics_filtered_pairs_a_p_i.html) reference in the OpenUSD documentation.
* [Robot Schema](../omniverse_usd/robot_schema.html#isaac-sim-robot-schema) for details on the Robot Schema used to identify robots on stage.

On this page

* [About](#about)
  + [When to Use](#when-to-use)
* [User Interface](#user-interface)
  + [Robot Selection](#robot-selection)
  + [Options](#options)
  + [Collision Pairs Table](#collision-pairs-table)
  + [Viewport Highlighting](#viewport-highlighting)
* [Example Usage: Unitree Dex5 Hand](#example-usage-unitree-dex5-hand)
  + [1. Open the Robot Asset](#open-the-robot-asset)
  + [2. Open the Self-Collision Detector](#open-the-self-collision-detector)
  + [3. Select the Robot and Detect Collisions](#select-the-robot-and-detect-collisions)
  + [4. Inspect a Collision Pair](#inspect-a-collision-pair)
  + [5. Filter Collision Pairs](#filter-collision-pairs)
  + [6. Inspect Multiple Collision Pairs](#inspect-multiple-collision-pairs)
* [Further Learning](#further-learning)