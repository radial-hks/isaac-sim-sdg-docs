---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/robot_simulation/grasp_editor.html
title: "Grasp Editor"
section: "Robot Simulation"
module: "08-omnigraph-robot-sim"
checksum: "23c3f92bad572039"
fetched: "2026-06-21T13:40:10"
---

* [Robot Simulation](index.html)
* Grasp Editor

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Grasp Editor

## Learning Objectives

This tutorial explains how to use the Grasp Editor extension in NVIDIA Isaac Sim to hand-author and
simulate grasps for a specific gripper/object pair. These grasps are stored in an isaac\_grasp
YAML file that can be imported and used with a motion generation algorithm to move the gripper into
place and grasp the desired object.

## Getting Started

To get started using the Grasp Editor extension, you need to prepare your assets in NVIDIA Isaac Sim.

* You must have an Articulation capable of grasping. This can be a floating gripper, or it can be a gripper attached to an arm.
* You must have a USD version of the object you want to grasp.

For both the gripper and the object, you must be ready to identify the USD frame that should be used to
represent location. This is often the frame in the center of the object mesh and at the base of the gripper.

You can download the stage used in this tutorial
[`here`](../_downloads/4d1aeb9e29208ad4bf35f0a38d105e49/Grasp_Editor_Tutorial_Stage.zip)
and follow along.

After downloading, extract the archive. In your running NVIDIA Isaac Sim instance,
click **File > Open** and select the `grasp_editor_tutorial.usd` file.

## What is an Isaac Grasp File?

The output of the Grasp Editor extension is a YAML in the isaac\_grasp file format. A single isaac\_grasp
file stores a list of grasps for a specific gripper/object pair. The file follows a simple format:

```python
 1format: isaac_grasp
 2format_version: 1.0
 3
 4object_frame: /World/mug
 5gripper_frame: /World/panda_hand
 6
 7grasps:
 8  grasp_0:
 9      confidence: 1.0
10      position: [-0.04346, 0.06759, 0.19895]
11      orientation: {w: 0.00332, xyz: [0.98453, 0.16837, 0.04837]}
12      cspace_position:
13        panda_finger_joint1: 0.00943
14      pregrasp_cspace_position:
15        panda_finger_joint1: 0.04
```

isaac\_grasp files do not need to originate with the Grasp Editor extension. The Grasp Editor
extension is useful for both authoring isaac\_grasp files and importing grasps that were authored
elsewhere for visualization and validation.

A grasp is defined by the relative position of the gripper and object. In order for this relative
position to have meaning, a representative frame must be chosen for the gripper and object positions.
The Grasp Editor handles these frames in two distinct ways:

* On export, the USD paths of the representative frames are written to the isaac\_grasp file
  under the object\_frame and gripper\_frame fields.
* On import, the object\_frame and gripper\_frame fields are ignored, because isaac\_grasp
  files may be authored externally (possibly without going through USD at all).
* As a result, identifying the correct USD frames is the user’s responsibility when using the
  Grasp Editor for importing.

Each grasp in an isaac\_grasp file has a unique name (e.g. grasp\_0). The fields for a named
grasp are:

* confidence: A parameter describing the quality of a grasp.
* position: The translation of the gripper frame relative to the object frame.
* orientation: The orientation of the gripper frame relative to the object frame.
* cspace\_position: A dictionary of joint positions for every joint that is used to control the gripper.
  These joint positions are the state of the gripper as it is actively grasping the object.
* pregrasp\_cspace\_position: A dictionary of joint positions for every joint that is used to control the gripper.
  These joint positions represent the open position of the gripper.

All together, a grasp may be applied in practice by moving the gripper to the correct relative position and orientation
while in the pregrasp\_cspace\_position, then closing the gripper until the joints are in cspace\_position.
If the object’s position and orientation in the world frame of reference is given by \(T\_o, R\_o\), with
the position and orientation fields specifying relative transformation \(^oT\_g, ^o\!\!R\_g\)
(i.e. the translation and rotation of the gripper according to the object frame of reference),
the desired position of the gripper in the world frame \(T\_g , R\_g\) is given by:

\[\begin{split}T\_g = R\_o \cdot {^oT\_g + T\_o} \\
R\_g = R\_o \cdot {^o\!R\_g}\end{split}\]

## Using the Grasp Editor

### Selection Frame

The Grasp Editor is a UI-based extension that can be used to author and import isaac\_grasp files.
In NVIDIA Isaac Sim, the Grasp Editor can be found in the toolbar under **Tools** > **Robotics** > **Grasp Editor**.
The first step is to add an Articulation and an object to the stage. The Articulation may be an
isolated gripper, or it may be a gripper attached to a robot arm. The object can be any
non-Articulation that has an associated mesh.

To fill in the Selection Frame:

1. Select the Articulation and object of interest. The prim path for the object can be copied by
   right clicking on the desired prim and selecting “Copy Prim Path”.
2. Choose an export path for the isaac\_grasp file. This should end in ‘.yaml’.

A few rules apply to the export file:

* The Grasp Editor may be used to author a sequence of grasps to the selected export file, but
  it does not support modifying an existing file.
* If an export path is supplied that already exists, the existing file will be overwritten with a
  new isaac\_grasp file.

This tutorial will author grasps between the Panda hand gripper (isolated from the Franka Emika Panda
robot) and a mug. When “Ready” is clicked, the Grasp Editor will:

* Validate each field in the panel.
* Perform all necessary conversions of the selected object prim (the mug) to make it graspable.
  Specifically, it applies the Rigid Body and Collision APIs from Usd Physics so that the object has
  a collision geometry and can be moved by external forces.

Note

The Grasp Editor does not revert these changes to the object asset, and so it is best not to save the USD stage unless these changes are specifically desired.

Warning

There is a known issue that the mug may “disappear”, this is a visual bug. You can press “STOP”, then “PLAY” again to make it reappear.

### Select Frames of Reference

In this panel, you may select the frames of reference that should be used to describe the position
in space of the gripper and object. It is critical to understand this panel and to make the proper
selections before moving on.

Most motion generation algorithms do not natively consume USD files. It is common for motion generation
algorithms to reference a URDF file. If the Grasp Editor
uses a frame that is not defined in a corresponding URDF file, an authored grasp becomes meaningless from the
perspective of any such motion generation algorithms.

Similarly, the selected frame of reference for the object
must correspond to the existing pipeline in which the object is being manipulated. For example, if a
camera is being used to identify object pose, there is an implicit frame of reference for the object
associated with that vision system. In this case, the selected frame for the object must correspond to this
implicit frame of reference. If there is not already a frame in the USD that represents the correct frame of
reference, a new one should be authored on the stage under the selected object path (e.g. nested under “/World/mug”).

In this tutorial, the base frames for the gripper and object are used. If the entire Franka Panda robot
were being used, the correct frame of reference for the gripper would still be the panda\_hand frame.
Once “Finalize” is clicked, these frames of reference become global to the output isaac\_grasp file and
cannot be changed.

**The Grasp Editor will write the USD paths for the frames of reference to the output isaac\_grasp file,
but this information will not be interpretable by a motion generation algorithm that does not consume USD.**

### Joint Settings

In this menu, you must select which joints in the Articulation are active degrees of freedom (DOFs) in
the gripper. The Panda hand is a two finger gripper, but one of the joints is a mimic joint. Observe
in the figure below that changing the value of panda\_finger\_joint1 causes panda\_finger\_joint\_2 to
move at the same time. This means that the Panda hand gripper is effectively controlled by a single DOF.

Each active DOF in the gripper should be checked as “Part of Gripper”. This will open a new menu of
joint settings that define how the grasp will be simulated and what gets written to the output isaac\_grasp file.

* Position When Open: The position of DOF that is considered to be open. Each grasp will be simulated
  by moving from the open position towards the closed position.
* Position When Closed: The position of the DOF that is considered to be fully closed.
* Grasp Speed: The speed at which the DOF will move from the open position towards the closed position when simulating.
* Max Effort Magnitude: The maximum force/torque (N or N\*m) that this DOF will be able to apply on the object when simulating.

At least one DOF must be marked as part of the Gripper in order to author a grasp. Only active gripper DOFs will
be written to the output isaac\_grasp file.

### Utils

The Utils menu has two useful utility functions that assist in using the Grasp Editor.

The Mask Collision button will mask collisions between the gripper and object. This may be helpful
when moving the object into place in order to test a grasp. Masked collisions are unmasked when a grasp
is simulated. When importing a grasp, collisions are masked automatically.

If the simulated grasp does not appear to have complete contact between the object and gripper,
you can use the “Show Physics Colliders” button to visualize the collision geometry associated
with your assets. It is outside of the scope of this extension to fix incorrect collider geometry,
but the Grasp Editor does allow you to author grasps without simulating them. In this situation
you can mask collisions and move things into place visually.

### Author a Grasp

A grasp may be authored with the aid of simulation, since moving assets by hand into what appears to
be the right position is imprecise. The figure below demonstrates the simulated authoring workflow:

1. Move the object into roughly the right position to be grasped.
2. Click the “Simulate” button to close the gripper according to its joint settings. In the figure,
   this causes the lip of the mug to be pushed into the exact center of the gripper fingers and leaves
   the gripper fingers in the exact position of contact with the object.
3. Once the simulation is complete, the export panel will populate, and the grasp may be written
   to file.

Letting the simulation settle the contact in this way gives a high degree of confidence to the grasp
that is written to the output file.

There may be reasons that the grasp simulation does not support your use-case such as:

* The physics colliders for your assets are not accurate.
* The mechanics for opening and closing the gripper are more complicated than is represented in the Grasp Editor.

In either case, the best way to make use of the Grasp Editor is to move things into place through
external means and export the grasp without simulating by clicking the “Skip Sim” button. For example,
some real robot grippers have heavily coupled degrees of freedom with somewhat complicated mechanics.
For such a gripper, you would want to replicate the exact movement programmatically and send joint
commands to the USD asset accordingly. In this case, you could turn on collisions and use an external
script or OmniGraph node to drive your gripper into a grasping position, then use the export function of the
Grasp Editor to export the current state of grasp on the USD stage to your isaac\_grasp file.

#### Adding External Forces and Torques

An extra feature of the Grasp Editor is that you can apply external forces and torques as part of the
grasp simulation. This may help to discern which grasps have the best force closure over the object.
The amount of force and torque applied may be selected in the “Add External Rigid Body Forces” panel.
A single scalar value may be chosen for force and for torque. A non-zero value \(v\) for force will cause
a force of \(\pm v\) N along each axis, centered at the base frame of the rigid body.
Likewise for torque, a value \(v\) will cause a torque of \(\pm v\) N\*m to be applied about each axis, centered
at the base frame of the rigid body.

The figure below demonstrates closing the grasp and then applying forces of 3 N. This test fails
when the mug flies away under a force of \([3, 0, 0]\). A smaller force value of 0.5 N is then
chosen, and the mug moves under the force, but the grasp is maintained.

### Exporting Grasps

The export frame becomes available once a grasp has been fully simulated, or the option to simulate has been declined.
On clicking “Export”, the current state of the stage is used to fill in the relevant fields of the
isaac\_grasp file.

* The confidence field takes on the value of the “Confidence” field in the Export panel.
* The position and orientation fields for the grasp are determined by finding the relative position
  of the gripper in the object’s frame of reference. This uses the frames defined in
  [Select Frames of Reference](#isaac-sim-app-tutorial-grasp-editor-reference-frames).
* The cspace\_position field is determined based on the current positions of the DOFs that have been marked as
  part of the gripper.
* The pregrasp\_cspace\_position field is taken from the “Position When Open” field of Joint Settings for each
  DOF that has been marked as part of the gripper.

At this stage, multiple grasps may be authored in a row and sequentially exported to the same isaac\_grasp file.

### Importing Grasps

Apart from authoring grasps, the Grasp Editor may be used to validate grasps that were authored
elsewhere. This can be done in the Import panel by selecting an isaac\_grasp file and clicking Import.
This tutorial uses the same file that is used for export, but this does not need to be the case.

In the figure below, multiple grasps have been authored and written to file using the Grasp Editor.
These grasps are imported, and can now be quickly visualized and simulated in sequence.

## Using Authored Grasps in Isaac Sim

The Grasp Editor is primarily a UI-based extension, but it offers some utility for importing and
using authored grasps within NVIDIA Isaac Sim through a Python API.

This section presents the following stage with the goal of determining where the robot should go
to execute one of the authored grasps.

The following function snippet imports a grasp file demonstrated in [Importing Grasps](#isaac-sim-app-tutorial-grasp-editor-import) and
determines where the panda\_hand frame should be in order to duplicate grasp\_1. To try this function, copy it into the
[Script Editor](../development_tools/omniverse_script_editor.html#script-editor), and pass the import\_file\_path=”path/to/your/isaac\_grasp.yaml” argument to the function.

```python
import isaacsim.core.experimental.utils.xform as xform_utils
from isaacsim.robot_setup.grasp_editor import GraspSpec, import_grasps_from_file

def compute_gripper_pose_for_grasp(
    import_file_path: str,
    mug_reference_frame: str = "/World/mug",
    grasp_name: str = "grasp_1",
) -> tuple:
    """Compute and print the gripper pose target needed to execute a named grasp.

    Args:
        import_file_path: Path to an ``isaac_grasp`` YAML file to import.
        mug_reference_frame: USD prim path of the rigid body whose pose anchors the grasp.
        grasp_name: Name of the grasp inside the file to compute targets for.

    Returns:
        Tuple of ``(gripper_trans_target, gripper_orientation_target)``.
    """
    grasp_spec: GraspSpec = import_grasps_from_file(import_file_path)
    grasp_names = grasp_spec.get_grasp_names()

    mug_trans, mug_quat = xform_utils.get_world_pose(mug_reference_frame, device="cpu")
    mug_trans, mug_quat = mug_trans.numpy(), mug_quat.numpy()

    gripper_trans_target, gripper_orientation_target = grasp_spec.compute_gripper_pose_from_rigid_body_pose(
        grasp_name, mug_trans, mug_quat
    )

    print("Grasp Names:", grasp_names)
    print("Gripper Translation Target:", gripper_trans_target)
    print("Gripper Orientation Target:", gripper_orientation_target)

    return gripper_trans_target, gripper_orientation_target
```

```python
Grasp Names: ['grasp_0', 'grasp_1', 'grasp_2']
Gripper Translation Target: [ 0.41496072 -0.03612298  0.27738899]
Gripper Orientation Target: [-0.1690746   0.63886658  0.12752551  0.73959483]
```

The result of the code snippet shows the name of each grasp in the isaac\_grasp file, and
the translation and orientation targets that should be set for the
panda\_hand frame in the full Franka robot. Note that the code snippet uses the frame of reference
for the mug that was selected in the Grasp Editor. It is outside of the scope of this tutorial to
use a motion generation algorithm to achieve this grasp.

Check out the GraspSpec class in our [API Documentation](../py/source/extensions/isaacsim.robot_setup.grasp_editor/docs/index.html) to see the complete set of functionality.

On this page

* [Learning Objectives](#learning-objectives)
* [Getting Started](#getting-started)
* [What is an Isaac Grasp File?](#what-is-an-isaac-grasp-file)
* [Using the Grasp Editor](#using-the-grasp-editor)
  + [Selection Frame](#selection-frame)
  + [Select Frames of Reference](#select-frames-of-reference)
  + [Joint Settings](#joint-settings)
  + [Utils](#utils)
  + [Author a Grasp](#author-a-grasp)
    - [Adding External Forces and Torques](#adding-external-forces-and-torques)
  + [Exporting Grasps](#exporting-grasps)
  + [Importing Grasps](#importing-grasps)
* [Using Authored Grasps in Isaac Sim](#using-authored-grasps-in-isaac-sim)