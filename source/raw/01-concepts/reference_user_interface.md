---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/gui/reference_user_interface.html
title: "User Interface Reference"
section: "概念"
module: "01-concepts"
checksum: "f602d579595b6fef"
fetched: "2026-06-21T13:39:50"
---

* User Interface Reference

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# User Interface Reference

[NVIDIA Omniverse™ Isaac Sim](../index.html#isaac-sim-app-overview) is built on [NVIDIA Omniverse](https://docs.omniverse.nvidia.com/) platform, so it shares the same UI elements as many Omniverse apps.

## Opening Page

Here’s a summary of the Isaac Sim frequently mentioned elements on the opening page. For more detailed view of all the elements on the page, go to [Omniverse User Interface](https://docs.omniverse.nvidia.com/composer/latest/interface.html "(in Omniverse USD Composer)").

| Ref # | Option | Result |
| --- | --- | --- |
| 1 | Menu Bar | Isaac Sim [Menu Bar](#isaac-sim-menu-bar) |
| 2 | Viewport | The primary way of viewing assets. See [Viewport](https://docs.omniverse.nvidia.com/extensions/latest/ext_core/ext_viewport.html "(in Omniverse Extensions)") for more details. |
| 3 | Main Toolbar | [Tool Bar](#toolbar) for manipulating the assets and start/stop simulation buttons are located. |
| 4 | Browsers | The default location for asset and example browsers. |
| 5 | Stage | The Stage window allows you to see all the assets in your current USD Scene. See the [Stage](https://docs.omniverse.nvidia.com/extensions/latest/ext_core/ext_stage.html "(in Omniverse Extensions)") docs for more details. |
| 6 | Property Panel | The window that displays the details of selected prim. See [Property Window](https://docs.omniverse.nvidia.com/extensions/latest/ext_core/ext_property-panel.html "(in Omniverse Extensions)") for more details. |

## Menu Bar

The Isaac Sim menu layout may be different from the layout of other Omniverse applications. Here are the ones unique to Isaac Sim.

| Ref # | Option | Result |
| --- | --- | --- |
| 1 | Create | The menu for creating various primitives and other simulation objects |
| 2 | Window | Opens various windows of loaded extensions, in this case, the ones composing the GUI and other extensions |
| 3 | Tools | The menu of available simulation tools for animation, physics, replicator, robotics, and USD |
| 4 | Utilities | Access various diagnostic and developer utilities such as debugging and extension templates |
| 5 | Layout | Opens menu for selecting preferred gui layouts |

## Tool Bar

| Icon | Menu Item | Action |
| --- | --- | --- |
| / | [Selection Modes](selection-modes.html) | Allows user to pick select and object in the viewport.  This is also the default viewport mouse behavior. |
| / | Move (Global / Local) | Instantiates a user widget that allows user to move a  selected object or group of objects |
|  | Rotate (Global / Local) | Instantiates a user widget that allows user to rotate  a selected object or group of objects |
|  | Scale | Instantiates a user widget that allows user to scale a  selected object or group of objects |
|  | Snap (enable/disable) | Sets snapping to specified increments or surface snap. |
|  | Select Mode | Toggles transform widgets between local and global  translation modes |
|  | * Play | Start an animation |
|  | * Stop | Stop an animation |

Note

Tools with a small triangle below their icon denotes additional options are available by right clicking the icon.

## Tabs

The Layout of the windows can be rearranged by moving the tabbed windows around, and docking them to different locations.

1. Panel Being Dragged (See Note below).
2. Panels Original location.
3. Acceptable Docking Locations.

Note

A tab can be “torn-off” and moved to another panel or window by click-hold-drag on the tabs title-bar and dragging it to another location or UI pane.

### OS Tabs

Certain tabs in the interface can be detached from the main window, which can be useful on multiple monitors and wide aspect ratio monitors.

To Detach a Tabbed panel use the following procedure.

1. `Right Click` on a `Tab` to invoke the `Move to New OS Window` option.
2. `Left Click` Select `Move to OS Window` action.
3. Position the window wherever you wish by using `Left-Click` + Dragging.

## Grab Handles

Grab handles are found in all Omniverse Apps and allow you to resize panels.

1. Grab Handle.

They are “invisible” UI element dividers that, when rolled over, will illuminate and can be click-dragged. This allows for UI customization, which is especially helpful in managing window content.

Note

Sliding is restricted to horizontal or vertical only.

### See Also

* [Omniverse User Interface](https://docs.omniverse.nvidia.com/composer/latest/interface.html "(in Omniverse USD Composer)") - Detailed overview of Omniverse UI elements
* [Viewport](https://docs.omniverse.nvidia.com/extensions/latest/ext_core/ext_viewport.html "(in Omniverse Extensions)") - In-depth guide to the viewport functionality
* [Stage](https://docs.omniverse.nvidia.com/extensions/latest/ext_core/ext_stage.html "(in Omniverse Extensions)") - Comprehensive documentation of the Stage window
* [Property Window](https://docs.omniverse.nvidia.com/extensions/latest/ext_core/ext_property-panel.html "(in Omniverse Extensions)") - Detailed guide to the Property Panel

On this page

* [Opening Page](#opening-page)
* [Menu Bar](#menu-bar)
* [Tool Bar](#tool-bar)
* [Tabs](#tabs)
  + [OS Tabs](#os-tabs)
* [Grab Handles](#grab-handles)
  + [See Also](#see-also)