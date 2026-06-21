---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/digital_twin/warehouse_logistics/ext_omni_warehouse_creator.html
title: "Warehouse Creator"
section: "数字孪生"
module: "06-sim2real-ue5"
checksum: "de57989f0df41d3f"
fetched: "2026-06-21T13:40:03"
---

* [Digital Twin](../index.html)
* Warehouse Creator Extension

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Warehouse Creator Extension

The Warehouse Creator is an interactive plan builder that converts a 2D grid layout into a USD warehouse
built from the Modular Warehouse asset pack. Sketch the floor plan in a top-down editor, place tiles from a
block library, and generate the corresponding USD prims on the active stage.

The feature ships as two extensions:

* `omni.warehouse.creator.api` — headless logic (grid engine, auto-tiling, plan-to-stage sync, and the
  column editing controller). Use it from scripts and tests with no UI dependency.
* `omni.warehouse.creator.ui` — the **Warehouse Builder** window, toolbar, block library palette,
  variant property widget, and column placement workflow.

## Installing and enabling the extension

1. Open **Window > Extensions** from the top menu.
2. Search for `omni.warehouse.creator.ui` in the **Extension Manager** window.
3. Click **Install** or **Update** if needed.
4. Toggle the extension on. Enable **Autoload** to start it on every launch.

The UI extension pulls in `omni.warehouse.creator.api` automatically. Enabling the API extension on its
own is supported for headless / scripted workflows.

## Opening the editor

Open **Window > Warehouse Creator** to show the **Warehouse Builder** window. The window contains:

* An **overhead 2D viewport** centered on the grid origin.
* A **floating toolbar** along the bottom of the viewport with all editing tools.
* A **block library palette** docked to the side of the window.
* A **Warehouse Creator** panel with the **Generate Warehouse** button and the collapsible **Column
  Editor** section.

The window builds on first open and stays in memory after you close it, so reopening is instantaneous.

## Configuring the dataset source

Configure asset paths from **Edit > Preferences > Warehouse Creator**. The page exposes:

| Setting | Purpose |
| --- | --- |
| **Cell Size (world units)** | World-space size of a single grid cell. Controls both the editor grid and the generated tile spacing. |
| **Wall Height (world units)** | Height applied to the wall asset preset. |
| **Center (floor) Asset** | File name of the center/floor USD asset relative to the asset root. |
| **Wall Asset** | File name of the wall USD asset relative to the asset root. |
| **Asset Root Path** | Local or Nucleus root folder containing the warehouse assets. Point this at your downloaded Isaac Sim assets folder for the fastest editor and generation experience. |
| **Cloud Assets URL** | HTTPS fallback used when **Asset Root Path** is unset or unreachable. |

Note

The **Cell Size**, **Wall Height**, and asset name settings depend on the asset pack you use. The
default values match the Isaac Sim assets pack; for a custom pack, set the values manually. An asset
pack is a collection of Center/Floor and Wall assets that share a variant system exposing every
available option of each asset type as a reference. See the Modular Warehouse pack for an example of
how to structure one.

For local performance, download the Isaac Sim assets pack (see [Latest Release](../../installation/download.html#isaac-sim-latest-release)) and point
**Asset Root Path** at `[Isaac Sim Assets Path]/Isaac/Environments/Modular_Warehouse_New/`. The block
library palette and the warehouse generator both read from this location.

## Editor workflow

The editor operates on a logical grid. At generation time, each occupied cell becomes a center/floor
prim and each exposed cell edge becomes a wall prim. The generator omits walls between two adjacent
occupied cells.

The toolbar uses three categories of buttons:

* **Modal tools** — mutually exclusive. Activating one deactivates the previously active modal tool.

  + **Select**
  + **Move**
  + **Rotate**
  + **Draw**
  + **Line**
  + **Box**
  + **Erase**
* **Toggles** — coexist with any modal tool. Activating symmetry mirrors every drawing or erasing
  action across the chosen axis.

  + **Symmetry Horizontal**
  + **Symmetry Vertical**
* **Immediate actions** — one-shot operations. They execute on click without becoming the active tool.

  + **Flip Horizontal**
  + **Flip Vertical**
  + **Group**
  + **Ungroup**
  + **Merge**
  + **Subtract**
  + **Zoom In**
  + **Zoom Out**

Selection-dependent actions ( **Flip**,  **Group**,  **Ungroup**,
 **Merge**, and  **Subtract**) are disabled in the toolbar when the current
selection does not meet their requirements.

### Drawing tiles

1. Pick an asset in the **Block Library Palette**. The next drawing operation places this asset as the
   manual tile.
2. Activate  **Draw** for free-form painting,  **Line** for a straight-line drag, or
    **Box** for filled rectangles.
3. Click and drag inside the viewport to add cells.  **Erase** removes cells with the same
   gestures.

To drop a single tile at the cursor without changing the active tool, drag a palette card directly onto
the viewport.

**Symmetry Horizontal** and  **Symmetry Vertical** mirror every drawing or erasing
action across the world origin on the selected axis. Toggle them at any time without leaving the active
drawing tool.

### Selecting and editing

* **Select** — click a cell to select it. Click and drag to draw a selection box.
  Selecting a grouped cell selects the entire group.
* **Move** — drag selected cells or groups to a new grid location.
* **Rotate** — click to rotate the selection 90 degrees clockwise. Use the keyboard
  shortcuts below for finer control.
* **Flip Horizontal** /  **Flip Vertical** — mirror the selection across the
  corresponding axis in place.

### Hotkeys

The window owns its hotkey scope, so the shortcuts only fire while the cursor is over the
**Warehouse Builder** window.

| Shortcut | Action |
| --- | --- |
| `Delete` / `Backspace` | Delete the current selection (cells and groups). |
| `Esc` | Clear the current selection. |
| `Ctrl+Z` / `Ctrl+Y` | Undo / redo the last grid command. |
| `Left` / `Right` | Rotate the selected cells 90 degrees counter-clockwise / clockwise. Hold `Shift` to rotate in place. |
| `Space` | Cycle to the next tool (when `enable_hotkeys` is enabled in the extension settings). |

### Grouping cells

A group treats a set of cells as a single floating object. You can move, rotate, and flip a group as a
unit, and the generator emits each group as a separate warehouse root prim.

* **Group** — combine the selection into a new group. Requires at least two ungrouped cells
  or existing groups.
* **Ungroup** — stamp a selected group’s cells back onto the grid as ungrouped cells.
* **Merge** — combine two or more selected groups into one.
* **Subtract** — remove the cells of later-selected groups from the first-selected
  group.

At generation time, each group becomes its own `/Warehouse_group_<id>` root prim with walls derived
from its boundary. Adjacent groups can sit next to ungrouped cells without sharing walls.

### Variant property widget

The generator emits two tile types — **Wall** and **Center** — and each tile ships with a set of
visual variants such as a loading dock, an access panel, or a window. After generation, select one or
more tile prims in the stage and use the **Warehouse Tiles** section of the **Property** panel to switch
the variant on every selected tile of that type.

Tip

In the viewport, set **Select Mode** to **Component** (right-click the toolbar) so individual tiles
are selectable instead of the whole warehouse hierarchy.

## Generating the warehouse

The **Generate Warehouse** button in the **Warehouse Creator** panel converts the current plan into USD
prims on the active stage:

* All ungrouped cells go under `/Warehouse`.
* Each group goes under its own `/Warehouse_group_<id>`.
* A center/floor prim is placed at every occupied cell, and a wall prim is added on every exposed edge,
  rotated to face outward.

A modal **Generating Warehouse** popup blocks input until the USD layers settle. This keeps the editor
responsive while large layouts stream in.

Re-running **Generate Warehouse** replaces the existing root prims with a fresh layout, so you can
iterate on the plan and regenerate without manual cleanup.

## Editing column placement

Each warehouse block carries a quarter-column at every corner. Adjacent blocks combine their
quarter-columns into a single full column. The **Column Editor** toggles individual full columns on or
off after the warehouse is generated, without manually authoring per-block variants.

1. Generate the warehouse, then select any prim under one of the warehouse roots. The **Edit Column
   Placement** button becomes available when the selection sits under a generated warehouse.
2. Click **Edit Column Placement** to enter edit mode. The editor hides the ceiling and non-column
   geometry, highlights each column (green for kept, red for pending removal), and forces the viewport
   outline overlay on so the highlights remain visible.
3. Click columns in the viewport to toggle each between **Enabled** (green) and **Disabled** (red). Drag
   a marquee to toggle multiple at once. Use the **Enable All**, **Disable All**, and **Flip All**
   buttons for bulk operations.
4. Click **Confirm** to author the variant selections on the root layer, or **Cancel** to discard the
   pending changes. Both actions exit edit mode and clear the temporary visibility overrides.

## Headless API

For scripts, batch jobs, and tests, `omni.warehouse.creator.api` exposes the same generation pipeline
without any UI:

```python
import omni.usd
from omni.warehouse.creator.api import CellData, GridConfig, GridEngine, StageSyncer

cells = {
    (0, 0): CellData(),
    (1, 0): CellData(),
    (1, 1): CellData(),
}

engine = GridEngine(GridConfig(cell_size=10.0))
stage = omni.usd.get_context().get_stage()

placed = StageSyncer().sync(cells, engine, stage)
```

The `ColumnEditorController` mirrors the **Column Editor** workflow for headless use. Call
`enter()` to begin a session, mutate the pending-disabled set with `set_all()`,
`flip_all()`, or `toggle_keys()`, then call `leave()` with `commit=True` to author the
selections.

On this page

* [Installing and enabling the extension](#installing-and-enabling-the-extension)
* [Opening the editor](#opening-the-editor)
* [Configuring the dataset source](#configuring-the-dataset-source)
* [Editor workflow](#editor-workflow)
  + [Drawing tiles](#drawing-tiles)
  + [Selecting and editing](#selecting-and-editing)
  + [Hotkeys](#hotkeys)
  + [Grouping cells](#grouping-cells)
  + [Variant property widget](#variant-property-widget)
* [Generating the warehouse](#generating-the-warehouse)
* [Editing column placement](#editing-column-placement)
* [Headless API](#headless-api)