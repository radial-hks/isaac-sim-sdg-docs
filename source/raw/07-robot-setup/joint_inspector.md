---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/robot_setup/joint_inspector.html
title: "Joint Inspector"
section: "Setup 工具"
module: "07-robot-setup"
checksum: "2bdc9507a5d5029d"
fetched: "2026-06-21T13:05:34"
---

* [Robot Setup](index.html)
* [Inspector Tools](inspector_tools.html)
* Joint Inspector

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Joint Inspector

The `isaacsim.gui.property` extension provides a standalone **Joint Inspector** window for Adjusting per-joint values across the robots present on the stage.

## Opening the Window

Open the inspector through **Tools > Robotics > Joint Inspector**.

The window docks to the left of the viewport.

## Selecting a Robot

The header exposes a robot picker, a refresh button, and a **+ New Inspector** button.

* **Robot drop-down** â lists every prim on the stage that has `IsaacRobotAPI` applied. Click the drop-down to open a searchable popup; type any substring of the prim path to narrow the list. Selecting a robot rebinds the table to that robotâs joints.
* **Refresh** â rescans the stage for prims with `IsaacRobotAPI`. Use this after authoring a new robot in a script editor or after switching layers.
* **+ New Inspector** â spawns an additional Joint Inspector window. Each window keeps an independent robot selection and column set, which is useful for side-by-side comparison of two robots or two views of the same robot.

The window listens to stage open/close and asset-load events so the robot list refreshes automatically when assets finish loading.

## Filtering Joints

A search field above the table filters the joint rows by name. Two matching modes are supported:

* **Substring (default)** â a case-insensitive substring match against the joint short name and the full prim path. `arm` matches `shoulder_arm_joint` as well as `/World/UR10/shoulder/arm`.
* **Glob (``\*`` or ``?`` in the query)** â `fnmatch`-style wildcards. The query is also matched in a substring-fenced form (`*pattern*`) so `hand*` finds anything that contains `hand`, mirroring the typical search-bar mental model.

A clear button on the right of the field removes the query and restores the full list.

## Choosing Columns

The hamburger button on the right of the toolbar opens a categorized columns popup.

The popup contains:

* **Backend pills** at the top â `PhysX` and `MuJoCo` toggle the visibility of every column belonging to that simulation backend. The pill state does not flip the per-column checkboxes, so re-enabling a backend restores the previously checked columns.
* **Categorized checkbox rows** for the available column groups.

The available column groups are summarized below.

| Group | Backend | Columns |
| --- | --- | --- |
| **Joint Limits** | USD / PhysX | `Position Min`, `Position Max`, `Velocity Max`. |
| **Drives** | USD | `Max Force`, `Target Position`, `Target Velocity`, `Stiffness`, `Damping`. |
| **Performance Envelope** | PhysX | `Max Actuator Velocity`, `Speed-Effort Gradient`, `Velocity-Dependent Resistance`. |
| **Joint State** | PhysX | `State Position`, `State Velocity`. |
| **MuJoCo Joint** | MuJoCo | `Armature`, `Damping`, `Stiffness`, `Friction Loss`, `Spring Ref`, `SolRef Limit (timeconst)`, `SolImp Limit (dmin)`. |

Column behavior:

* Items whose backing API is not applied on any joint of the current robot stay clickable but render dimmed; their tooltip explains why the column is currently empty.
* The userâs column selection persists across robot switches. A column reappears as soon as a robot whose joints back the column is selected.
* `Joint Limits` columns belong to USD core schemas and are not affected by the backend pills.

### Per-axis fan-out

When every joint authoring a multi-apply schema has at most one axis applied (the common case for revolute and prismatic chains), the per-axis dimension is collapsed and the column appears once. The cell automatically picks the jointâs authored axis or its natural axis (`angular` for revolute, `linear` for prismatic).

Multi-DOF (for example, `D6Joint`) joints make the column fan out: one column per distinct axis (`transX`, `transY`, `transZ`, `rotX`, `rotY`, `rotZ`) is rendered, with the axis token appended to the header label.

## Editing Values

Each cell is a free-form `ui.FloatDrag` bound directly to the underlying USD attribute. Drag horizontally to scrub the value or click to type a number. double-click or Ctrl-click to type a number.

Behavior of empty cells, multi-row edits, and array-typed attributes:

* Cells whose backing API is not applied on the joint render empty rather than as a disabled `0.0` field. This avoids implying a meaningful zero where no value is authored.
* Click rows to select them. `Ctrl` / `Cmd` and `Shift` allow multi-row selection. Editing one cell of a selected row mirrors the new value to the same column on every other selected row whose attribute exists.
* The MuJoCo `solreflimit` and `solimplimit` columns surface only the dominant element of the underlying array (`timeconst` and `dmin`); the rest of the array is preserved on write.

The status line above the table shows the number of joints currently displayed.

## Default Visible Columns

The first time the inspector is opened, the following columns are visible:

* `Position Min` and `Position Max` (Joint Limits)
* `Target Position`, `Stiffness`, `Damping` (Drives)
* `State Position` (Joint State)
* `Armature`, `Damping`, `Stiffness`, `Friction Loss` (MuJoCo Joint)

Use the columns menu to add or remove columns from this set.

On this page

* [Opening the Window](#opening-the-window)
* [Selecting a Robot](#selecting-a-robot)
* [Filtering Joints](#filtering-joints)
* [Choosing Columns](#choosing-columns)
  + [Per-axis fan-out](#per-axis-fan-out)
* [Editing Values](#editing-values)
* [Default Visible Columns](#default-visible-columns)