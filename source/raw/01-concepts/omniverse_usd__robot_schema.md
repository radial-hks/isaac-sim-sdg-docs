---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/omniverse_usd/robot_schema.html
title: "Robot Schema"
section: "OpenUSD"
module: "01-concepts"
checksum: "71fe2e5e967f2488"
fetched: "2026-06-21T14:14:17"
---

* [Omniverse and USD](index.html)
* Robot Schema

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Robot Schema

The Robot Schema extends OpenUSD with a set of applied API schemas that describe robotic structures in a standardized, composable way. It builds on USD Common definitions and the Physics Schema for kinematic tree definitions, providing the canonical representation for robots in Isaac Sim.

The schema is implemented across two extensions:

* `isaacsim.robot.schema` – Schema definitions, application helpers, and programmatic utilities for traversing and maintaining robot structures.
* `isaacsim.robot.schema.ui` – Interactive [Robot Inspector Window](../robot_setup/robot_inspector.html#isaac-sim-robot-inspector-window) for viewing robot kinematic trees in multiple display modes, selectively masking and bypassing components, anchoring links to the world, and visualizing joint connections in the viewport.

# Schema Overview

The Robot Schema defines five applied API schemas and two typed schema:

| Schema | Purpose |
| --- | --- |
| **IsaacRobotAPI** | Root definition applied to the robot’s top-level prim. Holds metadata and ordered lists of links and joints. |
| **IsaacLinkAPI** | Flags a rigid body (or other simulated body) as a link in the robot composition. |
| **IsaacJointAPI** | Flags a physics joint as part of the robot composition and carries DOF ordering information. |
| **IsaacSiteAPI** | Marks a point of interest on the robot (tool mount, sensor location, end-effector frame). |
| **IsaacAttachmentPointAPI** | Defines attachment points used by surface grippers. |
| **IsaacNamedPose** | Typed prim schema storing a named joint configuration with an IK target transform, used by the [Robot Poser](../robot_setup/robot_poser.html#isaac-sim-robot-poser). |
| **IsaacSurfaceGripper** | Typed prim schema for surface-gripper mechanics (grip forces, distances, retry behavior). |

## Robot API

`IsaacRobotAPI` is applied to the robot’s root prim and serves as the single source of truth for the robot’s composition and metadata.

**Relationships**

| Relationship | Description |
| --- | --- |
| `isaac:physics:robotLinks` | Ordered list of links that compose the robot, starting with the base link. May include sites interleaved after their parent links. |
| `isaac:physics:robotJoints` | Ordered list of joints connecting the links. |
| `isaac:robot:namedPoses` | List of [IsaacNamedPose](#isaac-sim-robot-schema-named-pose) prims defining stored joint configurations for the robot. |

**Attributes**

| Attribute | Type | Description |
| --- | --- | --- |
| `isaac:description` | String | Free-form text describing the robot’s purpose and capabilities. |
| `isaac:namespace` | String | Unique namespace identifier used for component messaging. |
| `isaac:robotType` | Token | Category of robot, such as `Manipulator`, `Humanoid`, or `Mobile Base`. |
| `isaac:license` | Token | License under which the robot asset is distributed. |
| `isaac:source` | String | URL or reference to the original asset source. |
| `isaac:version` | String | Semantic version number of the robot asset. |
| `isaac:changelog` | String[] | Ordered list of change descriptions across asset revisions. |

Note

The Links and Joints lists need only contain elements relevant for reporting. The full kinematic tree may contain additional elements not present in these lists.

## Link API

`IsaacLinkAPI` is applied to each body that participates in the robot composition. It acts as a flag indicating that the prim should appear in robot state reporting.

| Attribute | Type | Description |
| --- | --- | --- |
| `isaac:nameOverride` | String | Optional custom name used instead of the prim name when reporting robot state. |

Links are not restricted to rigid bodies. The API can be applied to deformable bodies or other simulation types, though computing robot state from non-rigid links requires custom handling.

All links that belong to the robot must have `IsaacLinkAPI` applied, regardless of whether they appear in the `IsaacRobotAPI` links list.

## Joint API

`IsaacJointAPI` is applied to physics joints that participate in the robot composition. It flags the joint for inclusion and carries DOF ordering information.

| Attribute | Type | Description |
| --- | --- | --- |
| `isaac:nameOverride` | String | Optional custom name used instead of the prim name when reporting robot state. |
| `isaac:physics:DofOffsetOpOrder` | Token[] | Ordered list of degree-of-freedom tokens (`TransX`, `TransY`, `TransZ`, `RotX`, `RotY`, `RotZ`) defining the flattened DOF index ordering. Single-DOF joints (revolute, prismatic) and zero-DOF joints (fixed) do not require this attribute. |

All joints that belong to the robot must have `IsaacJointAPI` applied, regardless of whether they appear in the `IsaacRobotAPI` joints list.

Note

In prior revisions, per-axis DOF offset attributes (`isaac:physics:Tr_X:DoFOffset`, etc.) were used instead of the token array. These are deprecated. Use `UpdateDeprecatedJointDofOrder` or `UpdateDeprecatedSchemas` to migrate existing assets.

## Site API

`IsaacSiteAPI` describes points of interest on the robot – tool attachment frames, sensor mount locations, end-effector reference frames, and similar.

| Attribute | Type | Description |
| --- | --- | --- |
| `isaac:Description` | String | Description of the site, such as `"Tool Attachment Point"`. |
| `isaac:forwardAxis` | Token | Axis considered the forward direction of the site (`X`, `Y`, or `Z`). |

Sites are included in the `robotLinks` relationship. They can be placed immediately after their parent link or grouped at the end of the list, controlled by the `sites_last` parameter during population.

Note

`IsaacSiteAPI` replaces the deprecated `IsaacReferencePointAPI`. Robots still carrying the old schema will function but emit deprecation warnings. Use `UpdateDeprecatedSchemas` to migrate.

## Named Pose

`IsaacNamedPose` is a typed prim schema (inheriting from `Xform`) that stores a reusable joint configuration for a segment of the robot’s kinematic chain. Each named pose captures the joints between a start link and an end link/site, the corresponding joint values, and the target end-effector transform encoded in the prim’s Xform ops.

Named poses are collected under a `Named_Poses` scope beneath the robot root prim and registered via the `isaac:robot:namedPoses` relationship on `IsaacRobotAPI`. They are created and managed through the [Robot Poser](../robot_setup/robot_poser.html#isaac-sim-robot-poser) UI or programmatically via the `isaacsim.robot.poser` API.

**Relationships**

| Relationship | Description |
| --- | --- |
| `isaac:robot:pose:startLink` | The start link of the kinematic chain covered by this pose. |
| `isaac:robot:pose:endLink` | The end link or site of the kinematic chain. |
| `isaac:robot:pose:joints` | Ordered list of joint prims in the chain between the start and end links. |

**Attributes**

| Attribute | Type | Description |
| --- | --- | --- |
| `isaac:robot:pose:valid` | Bool | Whether the stored pose represents a valid IK solution. |
| `isaac:robot:pose:jointValues` | Float[] | Joint values in USD native units (degrees for revolute, meters for prismatic), ordered to match the `joints` relationship. |
| `isaac:robot:pose:jointFixed` | Bool[] | Per-joint fixed flags. When `True`, the corresponding joint is held constant during IK solving. |

Because `IsaacNamedPose` inherits from `Xform`, its translate and orient ops store the target end-effector pose in the robot’s coordinate frame. Moving the prim in the viewport updates this target, and the [Robot Poser](../robot_setup/robot_poser.html#isaac-sim-robot-poser) can track the prim’s transform in real time to solve IK continuously.

# Composing Robots

Robot compositions are built by applying `IsaacRobotAPI` to each sub-robot’s root prim. The final assembly is achieved by either:

* Adding a sub-robot’s root prim to the parent robot’s links and joints lists, which causes the parent to recursively include the sub-robot’s full kinematic tree.
* Selecting specific links and joints from sub-robots and adding them directly to the parent robot’s lists.

# Applying the Robot Schema

All robots in Isaac Sim’s asset library and those imported through [URDF Importer Extension](../importer_exporter/ext_isaacsim_asset_importer_urdf.html#isaac-sim-urdf-importer) or [MJCF Importer Extension](../importer_exporter/ext_isaacsim_asset_importer_mjcf.html#isaac-sim-mjcf-importer) have the Robot Schema pre-applied. For robots imported in prior versions or from external sources, the schema must be applied manually.

## Through the GUI

1. Select the root prim of the robot in the Stage panel.
2. In the Properties panel, click the **+ Add** button.
3. Select **Isaac > Robot Schema > Robot API**.

This applies `IsaacRobotAPI` to the root prim and automatically traverses the physics articulation to apply `IsaacLinkAPI` and `IsaacJointAPI` to all discovered bodies and joints.

Properties for each schema appear in the Properties panel under their respective API sections (displayed in purple).

If the robot structure changes over time (for instance, new links or joints are added), either manually apply the individual APIs to new prims, or reapply the Robot API to the root prim to re-run automatic population.

Note

When applying the schema, if your asset follows the [Asset Structure](../robot_setup/asset_structure.html#isaac-sim-app-reference-asset-structure) guidelines, apply it either in the base layer or in a dedicated robot schema layer – not directly in the interface layer. Auto-population requires authored physics, so temporarily add the physics layer as a sublayer during schema application, then remove it before saving.

## Through Code

The following snippet applies the Robot Schema programmatically. Following the [Asset Structure](../robot_setup/asset_structure.html#isaac-sim-app-reference-asset-structure) guidelines, the schema is authored in a separate layer so it remains independent of other payloads and is easy to update as the schema evolves.

```python
import omni.usd
import pxr
import usd.schema.isaac.robot_schema as rs
from pxr import Sdf, Usd, UsdGeom

stage = omni.usd.get_context().get_stage()
robot_asset_path = "/".join(stage.GetRootLayer().identifier.split("/")[:-1])  # Get the asset path from the stage
robot_asset = ".".join(
    stage.GetRootLayer().identifier.split("/")[-1].split(".")[:-1]
)  # Get the asset name from the stage
schema_asset = f"configuration/{robot_asset}_robot_schema.usda"
edit_layer = Sdf.Layer.FindOrOpen(f"{robot_asset_path}/{schema_asset}")
if not edit_layer:
    edit_layer = Sdf.Layer.CreateNew(f"{robot_asset_path}/{schema_asset}")
# Add sublayer to the stage, but as a relative path, only if not already present
if schema_asset not in stage.GetRootLayer().subLayerPaths:
    stage.GetRootLayer().subLayerPaths.append(schema_asset)
# Make all edits in the edit layer
with pxr.Usd.EditContext(stage, edit_layer):

    default_prim = stage.GetDefaultPrim()

    # Apply the Robot API to the default prim, and auto-populate the Links and Joints lists
    rs.ApplyRobotAPI(default_prim)

edit_layer.Save()
stage.Save()
```

# Editing in the Properties Panel

When a prim with `IsaacRobotAPI` is selected, the Properties panel shows a dedicated **Robot Schema** widget that consolidates the robot metadata, the link/joint relationship lists, and a maintenance toolbar in a single Figma-style layout. The widget is provided by `isaacsim.gui.property` and replaces the generic relationship/attribute editors that previously surfaced these properties.

The widget is split into three collapsible sections.

## Robot Schema (Metadata)

The first collapsible section binds each scalar [Robot API](#isaac-sim-robot-schema-robot-api) attribute to an inline editor.

| Field | Editor | Notes |
| --- | --- | --- |
| **Description** | Text field | Free-form text. Updated on field commit (Enter / focus loss). |
| **License** | Drop-down | Populated from the schema’s `allowedTokens` so only recognized SPDX-style identifiers can be selected. |
| **Namespace** | Text field | Used for component messaging. |
| **Robot Type** | Drop-down with **(Other)** entry | Selecting **(Other)** appends a side text field for typing a custom token; selecting any predefined value clears the override. |
| **Source** | Text field | URL or reference to the original asset. |
| **Version** | Text field | Semantic version string. |
| **Changelog** | Inline editable list with **+** and **−** buttons | New entries are prepended; each entry exposes a remove button. The full list is written back as a USD string array. |

## Robot Joints and Robot Links

The next two sections expose the `isaac:physics:robotJoints` and `isaac:physics:robotLinks` relationships as scrollable, drag-reorderable lists.

Each row shows:

* A numeric index (only for direct children, not for sub-robot rows).
* A grab handle for drag-and-drop reordering. Dragging a row reveals a horizontal drop indicator at the insertion point.
* The target prim’s display name. Hovering shows a tooltip with the full prim path. Double-clicking selects the prim on the stage.
* A trailing remove button that drops the entry from the relationship.

### Adding entries

The **Add Joint** and **Add Link** buttons open a stage prim picker pre-filtered to compatible prims:

* **Add Joint** – shows prims with `IsaacJointAPI` or `IsaacRobotAPI`.
* **Add Link** – shows prims with `IsaacLinkAPI`, `IsaacSiteAPI`, or `IsaacRobotAPI`.

### Sub-robot rows

When a row targets a prim that itself has `IsaacRobotAPI`, a disclosure triangle appears next to the label. Expanding the row displays a read-only, indented preview of that sub-robot’s matching relationship – joints in the joints list, links in the links list. The preview recurses up to four levels deep so deeply nested compositions stay legible.

.
Maintenance Toolbar
——————-

Two buttons at the bottom of the widget keep the relationships consistent with the underlying physics articulation and the asset’s layer stack:

| Control | Behavior |
| --- | --- |
| **Re-Calculate Robot Tree** | Calls `RecalculateRobotSchema`: rescans the articulation, appends newly discovered links and joints, and removes invalid targets. Existing valid items keep their order. |
| **Force Update** (checkbox) | When ticked, the next **Re-Calculate Robot Tree** discards the current `robotLinks`/`robotJoints` order and rewrites both relationships from scratch. |
| **Save to Robot Layer** | Calls `SaveRobotSchemaToRobotLayer` to flush the current order to the layer that authors `IsaacRobotAPI`. Other layers (references, attachments, sublayers) are left untouched. A warning is logged if no authoring layer can be located. |

## Other Robot Schema Widgets

Selecting a prim with one of the other Robot Schema APIs surfaces a focused widget for that schema:

* **Robot Link** (`IsaacLinkAPI`) – exposes the optional `isaac:nameOverride` attribute.
* **Robot Joint** (`IsaacJointAPI`) – exposes `isaac:nameOverride`, `isaac:physics:DofOffsetOpOrder`, and the `isaac:actuator` flag.
* **Robot Site** (`IsaacSiteAPI`) – exposes the site description and forward-axis token; available on any `Xformable` prim.

Each widget has a remove button in its header that drops the schema and clears its authored properties. Use the **+ Add** menu’s `Isaac/Robot Schema/...` entries to apply any of these schemas to a new prim.

# Parsing Robot Structure

The robot kinematic tree is derived from the Physics Schema augmented with Robot Schema relationships. Parsing proceeds as follows:

1. Collect links from the `robotLinks` relationship on the `IsaacRobotAPI` prim.
2. Collect joints from the `robotJoints` relationship.
3. Starting from the first link (the base link), perform a breadth-first traversal through joints to connected links, building a tree.

The tree must be acyclic. Joints that would form loops must have their **Exclude from Articulation** attribute set; otherwise, loops are broken arbitrarily during parsing based on visit order.

## Example

1. In the Content Browser, drag a UR10e robot (`Robots/UniversalRobots/ur10e/ur10e.usd`) onto the stage.
2. In the Variant selection menu in the Properties panel, select the Robotiq 2f-140 gripper variant.

1. Open the Script Editor via **Window > Script Editor** and run:

   ```python
   import omni.usd
   from pxr import Usd, UsdGeom

   # For legacy reasons, we need to import the schema from the usd.schema.isaac package
   from usd.schema.isaac import robot_schema

   stage = omni.usd.get_context().get_stage()
   prim = stage.GetPrimAtPath("/World/ur10e")

   robot_tree = robot_schema.utils.GenerateRobotLinkTree(stage, prim)

   robot_schema.utils.PrintRobotTree(robot_tree)
   ```

   The console output:

   ```python
   base_link
     shoulder_link
       upper_arm_link
         forearm_link
           wrist_1_link
             wrist_2_link
               wrist_3_link
                 robotiq_base_link
                   left_outer_knuckle
                     left_outer_finger
                     left_inner_finger
                       left_inner_knuckle
                   right_outer_knuckle
                     right_outer_finger
                     right_inner_finger
                       right_inner_knuckle
   ```

Note how the gripper appears in the robot structure even though it is a separate sub-robot composed into the UR10e. Select the UR10e prim on the stage to see how the Robot Lists include `ee_link`.

# Utility Functions

The `isaacsim.robot.schema` extension provides a comprehensive set of utility functions in the `utils` module, accessible via:

```python
from usd.schema.isaac.robot_schema import utils
```

## Traversal and Tree Generation

| Function | Description |
| --- | --- |
| `GenerateRobotLinkTree(stage, robot_link_prim)` | Builds and returns a `RobotLinkNode` tree representing the robot’s kinematic structure. Returns the root node. |
| `GetAllRobotLinks(stage, robot_link_prim, include_reference_points)` | Returns all links of the robot. Retrieves from schema relationships and supplements with any missing links discovered through articulation traversal. |
| `GetAllRobotJoints(stage, robot_link_prim, parse_nested_robots)` | Returns all joints of the robot. Retrieves from schema relationships and supplements with any missing joints from articulation traversal. |
| `GetJointBodyRelationship(joint_prim, bodyIndex)` | Returns the target path for a joint’s body connection (index 0 or 1). Returns `None` if the joint is excluded from articulation. |
| `GetJointPose(robot_prim, joint_prim)` | Returns the joint’s pose as a 4x4 matrix in the robot’s coordinate frame. |
| `GetLinksFromJoint(root, joint_prim)` | Given a tree root and a joint, returns two lists: links before the joint (toward the base) and links after the joint (toward the leaves). |
| `PrintRobotTree(root, indent)` | Prints an indented text representation of the link tree to the console. |

The `RobotLinkNode` class (from `isaacsim.robot.schema.utils`) represents a node in the kinematic tree:

| Attribute | Description |
| --- | --- |
| `prim` | The USD prim for this link. |
| `name` | Prim name (or `None`). |
| `path` | Prim path (or `None`). |
| `parent` | Parent `RobotLinkNode` (`None` for root). |
| `children` | List of child `RobotLinkNode` instances. |

## Schema Population

| Function | Description |
| --- | --- |
| `PopulateRobotSchemaFromArticulation(stage, robot_prim, articulation_prim, *, detect_sites, sites_last)` | Traverses the physics articulation graph via DFS, applies `IsaacLinkAPI` and `IsaacJointAPI` to discovered prims, and writes the ordered `robotLinks` and `robotJoints` relationships. Optionally detects and applies `IsaacSiteAPI` to leaf Xforms under links. |
| `RecalculateRobotSchema(stage, robot_prim, articulation_prim, *, detect_sites, sites_last)` | Similar to `PopulateRobotSchemaFromArticulation` but preserves the existing order of valid items. New links and joints are appended; invalid targets are removed. Use this for incremental updates. |

Both functions accept:

* `detect_sites` (bool): When `True`, child Xforms with no children under each link are detected and have `IsaacSiteAPI` applied automatically.
* `sites_last` (bool): When `False`, detected sites are inserted immediately after their parent link. When `True`, all sites are appended at the end of the links list.

## Site Detection and Management

| Function | Description |
| --- | --- |
| `DetectAndApplySites(stage, robot_prim, *, sites_last)` | Scans all links under a robot for child Xforms that qualify as sites (leaf Xforms with no children, no existing APIs). Applies `IsaacSiteAPI` to each. Returns `(all_sites, sites_by_parent_path)`. |
| `AddSitesToRobotLinks(robot_prim, sites, sites_by_parent, *, sites_last)` | Adds detected sites to the `robotLinks` relationship, either interleaved after their parent link or appended at the end. |

## Validation and Maintenance

| Function | Description |
| --- | --- |
| `ValidateRobotSchemaRelationships(robot_prim)` | Checks all targets in `robotLinks` and `robotJoints`. Returns `(valid_links, invalid_links, valid_joints, invalid_joints)`. |
| `EnsurePrependListForRobotRelationships(robot_prim)` | Rebuilds `robotLinks` and `robotJoints` using USD prepend list operations for correct layering behavior. |
| `RebuildRelationshipAsPrepend(prim, rel_name, targets)` | Low-level helper that rebuilds a single relationship using prepend list operations. |
| `UpdateDeprecatedSchemas(robot_prim)` | Traverses the robot subtree and replaces `IsaacReferencePointAPI` with `IsaacSiteAPI`. Also migrates deprecated per-axis DOF offset attributes on joints. |
| `UpdateDeprecatedJointDofOrder(joint_prim)` | Migrates a single joint’s deprecated per-axis `DoFOffset` attributes to the `DofOffsetOpOrder` token array. Removes the deprecated attributes from the edit layer. |

## Named Pose Query

| Function | Description |
| --- | --- |
| `GetAllNamedPoses(stage, robot_prim)` | Returns all [IsaacNamedPose](#isaac-sim-robot-schema-named-pose) prims registered in the robot’s `namedPoses` relationship. |
| `GetNamedPoseStartLink(named_pose_prim)` | Returns the start link path from the named pose. |
| `GetNamedPoseEndLink(named_pose_prim)` | Returns the end link / site path from the named pose. |
| `GetNamedPoseJoints(named_pose_prim)` | Returns the ordered list of joint paths in the pose’s kinematic chain. |
| `GetNamedPoseJointValues(named_pose_prim)` | Returns the stored joint values array (native USD units). |
| `GetNamedPoseJointFixed(named_pose_prim)` | Returns the per-joint fixed flags array. |
| `GetNamedPoseValid(named_pose_prim)` | Returns whether the stored pose is valid. |

# Kinematics

The `isaacsim.robot.schema` extension includes a pure-Python kinematics stack for forward kinematics, Jacobian computation, and inverse kinematics. These modules are used internally by the [Robot Poser](../robot_setup/robot_poser.html#isaac-sim-robot-poser) and are available for direct use.

```python
from usd.schema.isaac.robot_schema.ik_solver import IKSolver, IKSolverRegistry
from usd.schema.isaac.robot_schema.kinematic_chain import KinematicChain
from usd.schema.isaac.robot_schema.math import Joint, Transform
```

## Math Primitives

The `math` module (`usd.schema.isaac.robot_schema.math`) provides foundational data structures and pure math utilities with no USD stage or simulation dependencies.

**Data structures**

| Class | Description |
| --- | --- |
| `Transform` | Rigid SE(3) transform (translation `t` + quaternion `q` in `[w, x, y, z]` order). Supports composition via `@`, inversion via `inv()`. |
| `Joint` | Single joint in a kinematic chain. Stores the screw axis (`w` for revolute, `v` for prismatic), home pose, joint limits (`lower`, `upper`), an optional trailing tip offset, and the USD `prim_path`. The `exp(q)` method returns the relative transform for a given joint value. |

**Quaternion utilities**

| Function | Description |
| --- | --- |
| `quat_mul(q1, q2)` | Hamilton product of two quaternions. |
| `quat_conj(q)` | Quaternion conjugate. |
| `quat_rotate(q, v)` | Rotate a 3D vector by a unit quaternion. |
| `axis_angle_to_quat(axis, angle)` | Build a unit quaternion from axis-angle representation. |
| `quat_to_matrix(q)` | Convert a unit quaternion to a 3x3 rotation matrix. |

**Linear algebra**

| Function | Description |
| --- | --- |
| `skew(v)` | 3x3 skew-symmetric matrix for cross-product with `v`. |
| `adjoint(T)` | 6x6 adjoint matrix for a rigid transform `T`. |

## Kinematic Chain

The `kinematic_chain` module (`usd.schema.isaac.robot_schema.kinematic_chain`) provides the `KinematicChain` class that caches the robot’s kinematic tree and builds an ordered joint chain between a start and end prim for FK and IK computation.

| Method / Property | Description |
| --- | --- |
| `KinematicChain(stage, robot_prim, start_prim, end_prim)` | Constructor. Builds the kinematic tree once and extracts the joint chain between the two prims. `start_prim` and `end_prim` are optional; when omitted the cached tree is available for teleport operations without IK. |
| `compute_fk(q)` | Compute end-effector FK for joint configuration `q`. Returns `(Transform, per_joint_transforms)`. |
| `compute_fk_and_jacobian(q)` | Fused single-pass FK and spatial Jacobian computation. Returns `(Transform, 6xN Jacobian)`. |
| `read_joint_states()` | Read current USD joint state for the chain joints. Returns a dict of prim-path to value (radians or meters). |
| `teleport(joint_dict)` | Apply joint values by propagating FK body transforms through the kinematic tree. For use when simulation is stopped. |
| `teleport_anchored(joint_dict)` | Apply joint values while keeping a fixed prim’s world position unchanged. Handles backward (child-to-parent) joints by rigidly correcting the robot after FK propagation. |
| `joints` | Ordered list of `Joint` objects in the chain. |
| `tree_root` | Cached kinematic tree root node. |

## IK Solver Interface

The `ik_solver` module (`usd.schema.isaac.robot_schema.ik_solver`) defines an abstract solver interface and a global registry.

| Class / Function | Description |
| --- | --- |
| `IKSolver` | Abstract base class. Subclasses implement `solve(chain, target, q0, **kwargs)` returning joint values that achieve the target pose. |
| `IKSolverRegistry.register(name, solver_cls, *, default)` | Register an IK solver class under the given name. Set `default=True` to make it the default solver. |
| `IKSolverRegistry.get(name)` | Return a new instance of the solver registered under the given name. `None` returns the default solver. |
| `IKSolverRegistry.available()` | List all registered solver names. |
| `pose_error(Td, T)` | Compute 6-DOF pose error between desired and actual transforms. Returns a 6-vector `[rot_x, rot_y, rot_z, pos_x, pos_y, pos_z]`. |

Custom IK solvers can be registered at import time and used by the Robot Poser by passing their name to the `solver_name` parameter.

## Levenberg-Marquardt Solver

The `lm_ik` module (`usd.schema.isaac.robot_schema.lm_ik`) provides the default IK solver registered as `"lm"`. It implements Levenberg-Marquardt optimization with adaptive damping, joint-limit clamping, null-space bias toward joint mid-range, and per-joint fixed masks.

| Parameter | Default | Description |
| --- | --- | --- |
| `lam` | `1e-3` | Initial LM damping factor. Adapts automatically: shrinks on progress, grows on overshoot. |
| `iters` | `30` | Maximum iterations. |
| `tol` | `1e-6` | Convergence tolerance on the weighted cost. |
| `w_rot` | `1.0` | Weight on rotational error components. |
| `w_pos` | `1.0` | Weight on positional error components. |
| `max_step` | `0.5` | Maximum joint-space step per iteration (prevents wild jumps). |
| `null_space_bias` | `0.05` | Strength of null-space bias toward joint mid-range. Helps escape singular configurations. |
| `joint_fixed` | `None` | Boolean mask of chain length. `True` locks that DOF (Jacobian column zeroed). |

# Named Pose CRUD

The `isaacsim.robot.poser` extension provides higher-level CRUD and I/O operations for [IsaacNamedPose](#isaac-sim-robot-schema-named-pose) prims. These functions build on the [Kinematic Chain](#isaac-sim-robot-schema-kinematics) and IK solver to create, retrieve, apply, and export named poses.

```python
from isaacsim.robot.poser import (
    apply_pose_by_name,
    delete_named_pose,
    export_poses,
    get_named_pose,
    import_poses,
    list_named_poses,
    store_named_pose,
)
```

| Function | Description |
| --- | --- |
| `store_named_pose(stage, robot_prim, pose_name, pose_result)` | Creates an `IsaacNamedPose` prim, writes joint values, relationships, and the target Xform, and registers it in the robot’s `namedPoses` relationship. |
| `get_named_pose(stage, robot_prim, pose_name)` | Retrieves a stored pose as a `PoseResult` dataclass. |
| `list_named_poses(stage, robot_prim)` | Returns the names of all named poses on the robot. |
| `delete_named_pose(stage, robot_prim, pose_name)` | Removes the pose prim and its entry from the `namedPoses` relationship. |
| `apply_pose_by_name(stage, robot_prim, pose_name)` | Applies a stored pose to the robot. Teleports when simulation is stopped; drives via joint targets when running. |
| `export_poses(stage, robot_prim, filepath)` | Exports all named poses to a JSON file. |
| `import_poses(stage, robot_prim, filepath)` | Imports named poses from a JSON file and stores them on the robot. |

Note

`pose_name` is sanitized via `pxr.Tf.MakeValidIdentifier()` before being used as a prim name. Characters outside ASCII `[A-Za-z0-9_]` are replaced with `_`, and a leading `_` is prepended when the input would otherwise start with a digit. Distinct inputs that sanitize to the same identifier (for example `"home:v2"` and `"home/v2"`) refer to the same stored pose; `store_named_pose` logs a warning when this overwrites an existing pose.

For interactive authoring of named poses, see the [Robot Poser](../robot_setup/robot_poser.html#isaac-sim-robot-poser) documentation.

The `isaacsim.robot.schema` extension provides a comprehensive set of utility functions in the `utils` module, accessible via:

```python
from usd.schema.isaac.robot_schema import utils
```

## Traversal and Tree Generation

| Function | Description |
| --- | --- |
| `GenerateRobotLinkTree(stage, robot_link_prim)` | Builds and returns a `RobotLinkNode` tree representing the robot’s kinematic structure. Returns the root node. |
| `GetAllRobotLinks(stage, robot_link_prim, include_reference_points)` | Returns all links of the robot. Retrieves from schema relationships and supplements with any missing links discovered through articulation traversal. |
| `GetAllRobotJoints(stage, robot_link_prim, parse_nested_robots)` | Returns all joints of the robot. Retrieves from schema relationships and supplements with any missing joints from articulation traversal. |
| `GetJointBodyRelationship(joint_prim, bodyIndex)` | Returns the target path for a joint’s body connection (index 0 or 1). Returns `None` if the joint is excluded from articulation. |
| `GetJointPose(robot_prim, joint_prim)` | Returns the joint’s pose as a 4x4 matrix in the robot’s coordinate frame. |
| `GetLinksFromJoint(root, joint_prim)` | Given a tree root and a joint, returns two lists: links before the joint (toward the base) and links after the joint (toward the leaves). |
| `PrintRobotTree(root, indent)` | Prints an indented text representation of the link tree to the console. |

The `RobotLinkNode` class (from `isaacsim.robot.schema.utils`) represents a node in the kinematic tree:

| Attribute | Description |
| --- | --- |
| `prim` | The USD prim for this link. |
| `name` | Prim name (or `None`). |
| `path` | Prim path (or `None`). |
| `parent` | Parent `RobotLinkNode` (`None` for root). |
| `children` | List of child `RobotLinkNode` instances. |

## Schema Population

| Function | Description |
| --- | --- |
| `PopulateRobotSchemaFromArticulation(stage, robot_prim, articulation_prim, *, detect_sites, sites_last)` | Traverses the physics articulation graph via BFS, applies `IsaacLinkAPI` and `IsaacJointAPI` to discovered prims, and writes the ordered `robotLinks` and `robotJoints` relationships. Optionally detects and applies `IsaacSiteAPI` to leaf Xforms under links. |
| `RecalculateRobotSchema(stage, robot_prim, articulation_prim, *, detect_sites, sites_last)` | Similar to `PopulateRobotSchemaFromArticulation` but preserves the existing order of valid items. New links and joints are appended; invalid targets are removed. Use this for incremental updates. |

Both functions accept:

* `detect_sites` (bool): When `True`, child Xforms with no children under each link are detected and have `IsaacSiteAPI` applied automatically.
* `sites_last` (bool): When `False`, detected sites are inserted immediately after their parent link. When `True`, all sites are appended at the end of the links list.

## Site Detection and Management

| Function | Description |
| --- | --- |
| `DetectAndApplySites(stage, robot_prim, *, sites_last)` | Scans all links under a robot for child Xforms that qualify as sites (leaf Xforms with no children, no existing APIs). Applies `IsaacSiteAPI` to each. Returns `(all_sites, sites_by_parent_path)`. |
| `AddSitesToRobotLinks(robot_prim, sites, sites_by_parent, *, sites_last)` | Adds detected sites to the `robotLinks` relationship, either interleaved after their parent link or appended at the end. |

## Validation and Maintenance

| Function | Description |
| --- | --- |
| `ValidateRobotSchemaRelationships(robot_prim)` | Checks all targets in `robotLinks` and `robotJoints`. Returns `(valid_links, invalid_links, valid_joints, invalid_joints)`. |
| `EnsurePrependListForRobotRelationships(robot_prim)` | Rebuilds `robotLinks` and `robotJoints` using USD prepend list operations for correct layering behavior. |
| `RebuildRelationshipAsPrepend(prim, rel_name, targets)` | Low-level helper that rebuilds a single relationship using prepend list operations. |
| `UpdateDeprecatedSchemas(robot_prim)` | Traverses the robot subtree and replaces `IsaacReferencePointAPI` with `IsaacSiteAPI`. Also migrates deprecated per-axis DOF offset attributes on joints. |
| `UpdateDeprecatedJointDofOrder(joint_prim)` | Migrates a single joint’s deprecated per-axis `DoFOffset` attributes to the `DofOffsetOpOrder` token array. Removes the deprecated attributes from the edit layer. |

# Asset Structure

Following the guidelines for [Asset Structure](../robot_setup/asset_structure.html#isaac-sim-app-reference-asset-structure), apply the Robot Schema on a separate layer and load it as a sublayer on the robot asset. This keeps the schema isolated from physics and geometry payloads, making it straightforward to update as the schema evolves across releases.

On this page

* [Robot Schema](#)
* [Schema Overview](#schema-overview)
  + [Robot API](#robot-api)
  + [Link API](#link-api)
  + [Joint API](#joint-api)
  + [Site API](#site-api)
  + [Named Pose](#named-pose)
* [Composing Robots](#composing-robots)
* [Applying the Robot Schema](#applying-the-robot-schema)
  + [Through the GUI](#through-the-gui)
  + [Through Code](#through-code)
* [Editing in the Properties Panel](#editing-in-the-properties-panel)
  + [Robot Schema (Metadata)](#robot-schema-metadata)
  + [Robot Joints and Robot Links](#robot-joints-and-robot-links)
    - [Adding entries](#adding-entries)
    - [Sub-robot rows](#sub-robot-rows)
  + [Other Robot Schema Widgets](#other-robot-schema-widgets)
* [Parsing Robot Structure](#parsing-robot-structure)
  + [Example](#example)
* [Utility Functions](#utility-functions)
  + [Traversal and Tree Generation](#traversal-and-tree-generation)
  + [Schema Population](#schema-population)
  + [Site Detection and Management](#site-detection-and-management)
  + [Validation and Maintenance](#validation-and-maintenance)
  + [Named Pose Query](#named-pose-query)
* [Kinematics](#kinematics)
  + [Math Primitives](#math-primitives)
  + [Kinematic Chain](#kinematic-chain)
  + [IK Solver Interface](#ik-solver-interface)
  + [Levenberg-Marquardt Solver](#levenberg-marquardt-solver)
* [Named Pose CRUD](#named-pose-crud)
  + [Traversal and Tree Generation](#id1)
  + [Schema Population](#id2)
  + [Site Detection and Management](#id3)
  + [Validation and Maintenance](#id4)
* [Asset Structure](#asset-structure)