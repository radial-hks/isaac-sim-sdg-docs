---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/robot_setup_tutorials/tutorial_import_assemble_manipulator.html
title: "Import & Assemble Manipulator"
section: "Setup 教程"
module: "07-robot-setup"
checksum: "72df9992cc394d80"
fetched: "2026-06-21T14:14:34"
---

* [Robot Setup](../robot_setup/index.html)
* [Robot Setup Tutorials Series](index.html)
* Tutorial 6: Setup a Manipulator

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Tutorial 6: Setup a Manipulator

## Learning Objectives

This is the first manipulator tutorial in a series of four tutorials. This tutorial shows how to import the UR10e robot from Universal Robots and the 2F-140 gripper from Robotiq into NVIDIA Isaac Sim from URDF files and connect them together under one articulation.

*30 Minutes Tutorial*

Isaac Sim always uses Python 3.12, so the UR description package and any ROS packages used in this tutorial must be available in a Python 3.12 environment. How you obtain the package depends on your platform:

* **Ubuntu 24.04 + ROS 2 Jazzy** — install the prebuilt `ros-jazzy-ur-description` apt package; the system Python (3.12) already matches Isaac Sim.
* **Ubuntu 22.04 + ROS 2 Humble or Jazzy** — the system Python is 3.10, so the workspace must be cloned and rebuilt against Python 3.12 using the included `build_ros.sh` script.
* **Windows + Pixi-based ROS 2 Jazzy** — add the UR description package to your Pixi environment (`pixi add ros-jazzy-ur-description`); Pixi-managed ROS 2 Jazzy already runs on Python 3.12. See [ROS 2 Installation (Other Platforms)](../installation/install_ros_other_platforms.html#isaac-sim-app-install-ros-other-platforms) for Pixi setup. WSL2 is not supported for the ROS-based URDF import workflow — use the prebuilt USD files in the content browser instead.

Attention

ROS 2 Humble on Windows (Pixi) is not a supported configuration for this tutorial. On Windows, only ROS 2 Jazzy with Pixi is supported. Switch to ROS 2 Jazzy on Windows, or move to a Linux configuration, to follow this tutorial as written.

Verify or choose your configuration in the **Build Environment** banner at the top of this page to see the steps for your setup. Your selection drives the platform-specific commands throughout the rest of this page.

.config-selector {
position: fixed;
top: var(--pst-header-height, 60px);
left: 0;
right: 0;
z-index: 1020;
display: flex;
flex-wrap: wrap;
align-items: center;
justify-content: center;
gap: 12px 18px;
background-color: var(--pst-color-surface, rgba(248, 249, 250, 0.95));
border-bottom: 1px solid var(--pst-color-border, var(--color-border, #dee2e6));
border-radius: 0;
padding: 10px 24px;
margin: 0;
box-shadow: 0 4px 12px var(--pst-color-shadow, rgba(0,0,0,0.08));
backdrop-filter: saturate(180%) blur(6px);
-webkit-backdrop-filter: saturate(180%) blur(6px);
}
[data-theme="dark"] .config-selector {
background-color: var(--pst-color-surface, rgba(30, 30, 30, 0.92));
border-color: var(--pst-color-border, #404040);
box-shadow: 0 2px 8px rgba(0,0,0,0.3);
}
.config-selector h3 {
display: inline-block;
margin: 0 16px 0 0;
color: var(--pst-color-text-base, var(--color-foreground-primary, #212529));
font-size: 0.95em;
font-weight: 600;
vertical-align: middle;
}
[data-theme="dark"] .config-selector h3 {
color: var(--pst-color-text-base, #ffffff);
}
.config-options {
display: flex;
flex-direction: row;
flex-wrap: wrap;
gap: 10px 18px;
align-items: center;
}
.config-row {
display: flex;
flex-direction: row;
align-items: center;
gap: 8px;
}
.config-label {
font-weight: 600;
color: var(--pst-color-text-base, var(--color-foreground-primary, #212529));
font-size: 13px;
white-space: nowrap;
}
[data-theme="dark"] .config-label {
color: var(--pst-color-text-base, #ffffff);
}
.config-buttons {
display: flex;
flex-wrap: wrap;
gap: 6px;
}
.config-btn {
padding: 5px 10px;
border: 2px solid var(--pst-color-border, var(--color-border, #dee2e6));
border-radius: 6px;
background-color: var(--pst-color-surface, var(--color-background-primary, #ffffff));
color: var(--pst-color-text-base, var(--color-foreground-primary, #212529));
font-size: 12px;
font-weight: 500;
font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
cursor: pointer;
transition: all 0.2s ease-in-out;
white-space: nowrap;
user-select: none;
outline: none;
}
[data-theme="dark"] .config-btn {
border-color: var(--pst-color-border, #404040);
background-color: var(--pst-color-surface, #2d2d2d);
color: var(--pst-color-text-base, #cccccc);
}
.config-btn:hover {
border-color: var(--pst-color-primary, var(--color-brand-primary, #0d6efd));
background-color: var(--pst-color-primary-bg, var(--color-background-hover, #e9ecef));
color: var(--pst-color-text-base, var(--color-foreground-primary, #212529));
}
[data-theme="dark"] .config-btn:hover {
border-color: #666666;
background-color: #3d3d3d;
color: #ffffff;
}
.config-btn.active {
border-color: #76b900;
background-color: #76b900;
color: #ffffff;
font-weight: 600;
}
.config-btn.active:hover {
border-color: #669900;
background-color: #669900;
color: #ffffff;
}
.config-btn:focus {
box-shadow: 0 0 0 3px rgba(118, 185, 0, 0.2);
}
.config-content {
transition: opacity 0.3s ease-in-out;
}
.config-content.hidden {
display: none;
}
@media (max-width: 768px) {
.config-selector {
padding: 8px 10px;
}
.config-options {
flex-direction: column;
align-items: stretch;
gap: 8px;
}
}
@media print {
.config-selector {
position: static;
backdrop-filter: none;
}
}

### Build Environment

Platform:

LinuxWindows

Ubuntu Version:

Ubuntu 24.04Ubuntu 22.04

Ros Distro:

JazzyHumble

document.addEventListener('DOMContentLoaded', function() {
const buttons = document.querySelectorAll('.config-btn');
const contents = document.querySelectorAll('.config-content');
// Returns the active value for each visible config row.
// Rows hidden by a data-show-when dependency are excluded so their
// value does not accidentally filter out content blocks.
function getCurrentConfig() {
const config = {};
const buttonGroups = document.querySelectorAll('.config-buttons');
buttonGroups.forEach(group => {
const row = group.closest('.config-row');
if (row && row.style.display === 'none') return;
const activeBtn = group.querySelector('.config-btn.active');
if (activeBtn) {
config[group.dataset.configKey] = activeBtn.dataset.value;
}
});
return config;
}
// Show or hide config rows that have a data-show-when dependency.
// Must be called before updateVisibility() so getCurrentConfig() is correct.
function updateRowVisibility() {
const config = getCurrentConfig();
document.querySelectorAll('.config-row[data-show-when]').forEach(row => {
try {
const showWhen = JSON.parse(row.dataset.showWhen || '{}');
const visible = Object.entries(showWhen).every(([k, v]) => config[k] === v);
row.style.display = visible ? '' : 'none';
} catch (e) {
console.warn('Error parsing data-show-when for row:', e);
}
});
}
function updateVisibility() {
const currentConfig = getCurrentConfig();
contents.forEach(content => {
try {
const conditions = JSON.parse(content.dataset.conditions || '{}');
const shouldShow = Object.entries(conditions).every(
([key, value]) => currentConfig[key] === value
);
if (shouldShow) {
content.classList.remove('hidden');
content.style.display = 'block';
} else {
content.classList.add('hidden');
content.style.display = 'none';
}
} catch (e) {
console.warn('Error parsing conditions for content block:', e);
}
});
}
// Add click event listeners to buttons
buttons.forEach(button => {
button.addEventListener('click', function() {
this.parentNode.querySelectorAll('.config-btn').forEach(s => s.classList.remove('active'));
this.classList.add('active');
// Row visibility must be updated before content visibility.
updateRowVisibility();
updateVisibility();
});
button.addEventListener('keydown', function(e) {
if (e.key === 'Enter' || e.key === ' ') {
e.preventDefault();
this.click();
}
});
});
const banner = document.querySelector('.config-selector');
// Position the banner just below whatever is currently pinned to
// the top of the viewport (PyData navbar + version-warning + any
// announcement). Recomputed on scroll/resize so the banner shifts
// down when the version-warning is visible and up after it scrolls
// out of view.
const topElements = [
document.querySelector('.bd-header-announcement'),
document.querySelector('#bd-header-version-warning'),
document.querySelector('.bd-header.navbar'),
].filter(Boolean);
// Element that holds article content; padded down so its content
// is never overlapped by the fixed banner regardless of wrap.
const contentRoot = document.querySelector('.bd-main') ||
document.querySelector('main') ||
document.body;
function updateBannerTop() {
if (!banner) return;
let bottom = 0;
topElements.forEach(el => {
const rect = el.getBoundingClientRect();
if (rect.bottom > bottom) bottom = rect.bottom;
});
banner.style.top = Math.max(0, bottom) + 'px';
}
function updateContentOffset() {
if (!banner || !contentRoot) return;
const h = banner.offsetHeight;
contentRoot.style.paddingTop = h + 'px';
// Anchor links should land below the banner, not behind it.
document.documentElement.style.scrollPaddingTop = (h + 16) + 'px';
}
if (banner && 'ResizeObserver' in window) {
new ResizeObserver(() => {
updateContentOffset();
updateBannerTop();
}).observe(banner);
}
window.addEventListener('resize', () => {
updateContentOffset();
updateBannerTop();
});
window.addEventListener('scroll', updateBannerTop, { passive: true });
// Initial update
setTimeout(function() {
updateRowVisibility();
updateVisibility();
updateContentOffset();
updateBannerTop();
}, 100);
// Watch for theme changes
});

## Prerequisites

* If you are new to NVIDIA Isaac Sim, complete the [Wheeled Robot Set Up Tutorials](tutorial_intro_environment_setup.html#isaac-sim-app-tutorial-intro-environment-setup) tutorial prior to beginning this tutorial.
* Review the ROS 2 installations [ROS 2 Installation (Default)](../installation/install_ros.html#isaac-sim-app-install-ros) prior to beginning this tutorial.
* Review the URDF importer [URDF Importer Extension](../importer_exporter/ext_isaacsim_asset_importer_urdf.html#isaac-sim-urdf-importer) tutorial.
* In a ROS sourced terminal, install xacro for your selected configuration (see the **Build Environment** banner at the top of the page):

  ```python
  sudo apt install ros-$ROS_DISTRO-xacro
  ```

  ```python
  pixi add ros-$ROS_DISTRO-xacro
  ```

  Attention

  ROS 2 Humble on Windows (Pixi) is not a supported configuration. Switch to ROS 2 Jazzy on Windows, or move to a Linux configuration, to follow this tutorial as written.
* Locate the `import_manipulator` folder in the content browser at `Isaac Sim/Samples/Rigging/Manipulator/import_manipulator/`.

## Build and Install the UR Description Package

Follow the steps for the configuration you selected in the **Build Environment** selector at the top of this page.

Install the prebuilt UR description package and source ROS 2 Jazzy:

```python
sudo apt install ros-jazzy-ur-description
source /opt/ros/jazzy/setup.bash
```

Then launch Isaac Sim from the same terminal:

```python
./isaac-sim.sh
```

On Ubuntu 22.04, the system Python (3.10) does not match the Python 3.12 used by Isaac Sim, and the UR description package is not natively available for Python 3.12. Clone the package and rebuild it with the included `build_ros.sh` script.

Note

See [Isaac Sim ROS Workspaces](../installation/install_ros.html#isaac-sim-ros-workspace) for more information on setting up your custom ROS 2 package in your ROS workspace.

1. Change into your Isaac Sim ROS Workspace, then into the distro-specific workspace’s `src` folder:

   ```python
   cd <path to Isaac Sim ROS Workspace>
   cd jazzy_ws/src
   ```

   ```python
   cd <path to Isaac Sim ROS Workspace>
   cd humble_ws/src
   ```
2. Clone the branch of the [Universal Robots ROS 2 Description repository](https://github.com/UniversalRobots/Universal_Robots_ROS2_Description) that matches your ROS distribution:

   ```python
   git clone --branch jazzy https://github.com/UniversalRobots/Universal_Robots_ROS2_Description.git
   ```

   ```python
   git clone --branch humble https://github.com/UniversalRobots/Universal_Robots_ROS2_Description.git
   ```
3. Return to the Isaac Sim ROS Workspace root and build against Python 3.12:

   ```python
   cd ../..
   ./build_ros.sh
   ```
4. Source the Python 3.12 ROS environment and launch Isaac Sim.

   ```python
   source build_ws/jazzy/jazzy_ws/install/local_setup.bash
   source build_ws/jazzy/isaac_sim_ros_ws/install/local_setup.bash
   ./isaac-sim.sh
   ```

   ```python
   source build_ws/humble/humble_ws/install/local_setup.bash
   source build_ws/humble/isaac_sim_ros_ws/install/local_setup.bash
   ./isaac-sim.sh
   ```

Attention

ROS 2 Humble on Ubuntu 24.04 is not an officially supported configuration in [ROS 2 Installation (Default)](../installation/install_ros.html#isaac-sim-app-install-ros). Switch to ROS 2 Jazzy on Ubuntu 24.04, or move to ROS 2 Humble on Ubuntu 22.04, to follow this tutorial as written.

On Windows, the URDF import workflow in this tutorial is supported only with a [Pixi-based](https://pixi.sh/) ROS 2 Jazzy installation. Follow [ROS 2 Installation (Other Platforms)](../installation/install_ros_other_platforms.html#isaac-sim-app-install-ros-other-platforms) for Windows ROS 2 setup and to install or build the UR description package against the Pixi environment. If you are using WSL2, skip the ROS-based import steps and use the prebuilt USD files in the content browser at `Isaac Sim/Samples/Rigging/Manipulator/import_manipulator/`.

Attention

ROS 2 Humble on Windows (Pixi) is not a supported configuration in [ROS 2 Installation (Default)](../installation/install_ros.html#isaac-sim-app-install-ros). Switch to ROS 2 Jazzy on Windows, or move to a Linux configuration, to follow this tutorial as written. If you need to use the UR10e on Windows without ROS, use the prebuilt USD files in the content browser at `Isaac Sim/Samples/Rigging/Manipulator/import_manipulator/`.

## Import the UR10e Robot

### Enable the ROS 2 Robot Description URDF Importer Extension

1. Go to `Window` > `Extensions`.
2. Type `URDF` in the search box, and find the `ROS 2 Robot Description URDF Importer Extension`.
3. If you can’t find it, remove the `@feature` filter from the search box.
4. If you still can’t find it, make sure Isaac Sim was launched from the same terminal where ROS was sourced.
5. Enable the extension by clicking the toggle button labeled `ENABLE`.
6. Check the box for `AUTOLOAD`, just to the right of `ENABLE`.

### Launch the URDF Publisher Topic

1. Open a new terminal with a **native** ROS 2 environment, source ROS 2 for your configuration, and launch the UR10e description.

   Important

   Do not reuse the Python 3.12 `build_ws` shell used to launch Isaac Sim above. The `build_ws` paths exist only to source the matching ROS 2 bridge into Isaac Sim; for `ros2 launch` commands, use your OS-native ROS 2 install (or a Docker container for distros that are not natively available on your OS).

   ```python
   source /opt/ros/jazzy/setup.bash
   ros2 launch ur_description view_ur.launch.py ur_type:=ur10e
   ```

   Source your native ROS 2 Humble install. If `ur_description` is not already available, install it from apt:

   ```python
   sudo apt install ros-humble-ur-description
   source /opt/ros/humble/setup.bash
   ros2 launch ur_description view_ur.launch.py ur_type:=ur10e
   ```

   Alternatively, build `ur_description` natively (Python 3.10) into `humble_ws` with `colcon build`, then source `humble_ws/install/local_setup.bash` instead of using the apt package.

   ROS 2 Jazzy is not natively available on Ubuntu 22.04, so run the launch command from a ROS 2 Jazzy Docker container with `jazzy_ws` mounted and built natively. Follow [Running ROS in Docker Containers](../installation/install_ros_other_platforms.html#isaac-ros-docker-other-platforms) to start an `osrf/ros:jazzy-desktop` container, build `jazzy_ws` inside it, then from inside the container run:

   ```python
   source /jazzy_ws/install/local_setup.bash
   ros2 launch ur_description view_ur.launch.py ur_type:=ur10e
   ```

   Activate the Pixi environment, then run:

   ```python
   ros2 launch ur_description view_ur.launch.py ur_type:=ur10e
   ```

   Attention

   ROS 2 Humble on Windows (Pixi) is not a supported configuration. Switch to ROS 2 Jazzy on Windows, or move to a Linux configuration, to follow this tutorial as written.
2. Verify that you see a window similar to the image below:
3. Set up one more terminal for `rqt_graph`, to see ROS nodes and topics being published:

   ```python
   rqt_graph
   ```
4. Verify that you see a window similar to the image below:

Hint

If the nodes are not showing up in `rqt_graph`, press the refresh button next to the drop down menu.

### Import the UR10e Robot into Isaac Sim

1. Go to Isaac Sim.
2. Navigate to **File** > **Import from the ROS 2 URDF Node**.

   * In the **ROS2 Node** field, type `robot_state_publisher`, click **Find Node**.
   * In the **USD Output** field, select the desired output (for example, `~/Desktop/`).
   * In the **Robot Type** field, select `Manipulator`.
   * In the **Base Type** field, select `Fixed`.
3. Click **Import**, the importer should automatically open the ur robot.

For reference, the resulting USD file is available in the content browser at `Isaac Sim/Samples/Rigging/Manipulator/import_manipulator/ur10e/ur/ur.usda`.

## Set Gains Using the Gain Tuner

The importer does not set the gains for the UR robot automatically. You can use the Gain Tuner to set the gains for the UR robot.
In this tutorial, we will use the gain tuner to set the natural frequency and damping ratio for the UR robot, which are defined as:

\[ \begin{align}\begin{aligned}\omega\_n = \sqrt{\frac{K\_p}{m}}\\\zeta = \frac{K\_d}{2 m \omega\_n}\end{aligned}\end{align} \]

Where \(\omega\_n\) is the natural frequency and \(\zeta\) is the damping ratio, and \(m\) is the computed joint inertia based on the mass of the robot at both sides of the joint.
The damping ratio is such that \(\zeta = 1.0\) is a critically damped system, \(\zeta < 1.0\) is underdamped, and \(\zeta > 1.0\) is overdamped.

Use the [Gain Tuner Extension](../robot_setup/ext_isaacsim_robot_setup_gain_tuner.html#isaac-gain-tuner) to set and verify the gains for the UR robot.

1. Go to **Tools** > **Robotics** > **Asset Editors** > **Gain Tuner**.
2. On the **Gain Tuner** window, on the **Robot Selection** dropdown, select the **ur** articulation in the stage.
3. In the **Tune Gains** panel, you can adjust the gains for the robot and the gripper fingers joints. Test it with the **Test Gains Settings** panel. let’s start by setting the natural frequency to `300` and the damping ratio to `1.0`.

Hint

We recommend determining the gains for a small group of joints first, if it is difficult to tune the gains for the whole robot. Below are some tips for tuning the gains:

* Higher the natural frequency, the faster the robot will respond to the target position. Lower the damping ratio, the faster the robot will reach the target position.
* If the resulting plot shows the robot is undershooting the target position, you can increase the `Nat. Freq.` slightly.
* If the resulting plot shows the robot is overshooting the target position, you can decrease the `Nat. Freq.` slightly and increase the `Damping Ratio`.
* Disabling gravity can help you see the gains more clearly.
* Only gain test the joints that are expected to be moving together, the gain test order can be selected by the **Sequence** dropdown.
* Reduce the maximum speed of a joint that you are tuning, if it is not expected to be commanded to move that fast in practice. The default values in the Gains Test are the maximum velocity written into the USD.

Note

See [Gain Tuner Extension](../robot_setup/ext_isaacsim_robot_setup_gain_tuner.html#isaac-gain-tuner) for more information on the Gain Tuner and [Tutorial 11: Tuning Joint Drive Gains](joint_tuning.html#isaac-sim-app-tutorial-advanced-joint-tuning) for more information on how to tune the gains for the robot.

For reference, the resulting USD file is available in the content browser at `Isaac Sim/Samples/Rigging/Manipulator/import_manipulator/ur10e/ur_gains_tuner/ur.usda`.

## 2F-140 Gripper Parameters

In the next section of the tutorial, we will be connecting the UR10e robot with the 2F-140 gripper. Let’s review the expected parameters for the gripper joints.

### Expected Parameters for Finger and Knuckle Joints

| Joint Name | Lower Limit | Upper Limit | Gearing | Stiffness | Damping | Max Force |
| --- | --- | --- | --- | --- | --- | --- |
| Finger Joint | 0 | 40.107 | N/A | 37.51957 | 0.00125 | 1000 |
| Left inner Finger | -8.021 | 48.128 | -1 | N/A | N/A | N/A |
| Left Inner Knuckle | -48.128 | 8.021 | 1 | N/A | N/A | N/A |
| Right inner Knuckle | -48.128 | 8.021 | 1 | N/A | N/A | N/A |
| Right outer knuckle | -48.128 | 8.021 | 1 | N/A | N/A | N/A |
| Right inner Finger | -8.021 | 48.128 | -1 | N/A | N/A | N/A |

### Expected Parameters for Mimic Joints

* Reference Joint: `/robotiq_arg2f_140_model/joints/finger_joint`
* Reference Joint Axis: `rotX`
* Natural Frequency: `2500`
* Damping Ratio: `0.005`

## Connect the UR10e Robot with the Robotiq 2F-140 Gripper

Much like a real robot can have its tools changed for different tasks, simulated robots benefit from the same capability. This section outlines two methods to connect the UR10e robot with the Robotiq 2F-140 gripper

We will use the Robot Assembler to connect the UR10e robot with the 2F-140 gripper.

1. Open the UR10e USD file created from the last activity (`ur.usda`).
2. Drag and drop the `robotiq_2f_140.usd` file we created earlier into the stage.
3. Open the robot assembler by going to **Tools** > **Robotics** > **Asset Editor** > **Robot Assembler**.

   * In **Base Robot**, set **Select Base Robot** to `/ur`, **Attach Point** to `wrist_3_link`.
   * In **Attach Robot**, set **Select Attach Robot** to `/ur/robotiq_2f_140`, **Attach Point** to `robotiq_arg2f_base_link`.
   * Set **Assembly Namespace** to `Gripper`.
4. Click **Begin Assembling Process** to start the process.
5. Adjust the attachment point orientation to make sure the end effector is attached to the gripper correctly. Rotate the gripper 90 degrees around the z-axis by clicking **Z +90**.
6. Click **Assemble and Simulate** to test the process.
7. Click **End Simulation And Finish** to complete the process.
8. Save the asset by going to **File** > **Save** or press **Ctrl+S**.

### Run the Simulation

1. In the Stage panel, select the **ur** prim.
2. In the Property Editor at the bottom right, find the **Variants** section.
3. Beside **Gripper**, select **None** and the gripper will be removed from the robot.
4. Beside **Gripper**, select **robotiq\_2f\_140** and the gripper will be added to the robot.
5. Save the asset by going to **File** > **Save** or press **Ctrl+S**.

Note

The completed robotics arm asset with the gripper is available in the content browser at `Isaac Sim/Samples/Rigging/Manipulator/import_manipulator/ur10e/ur_gripper/ur.usda`.

## Summary

In this tutorial, you took the UR10e robot from Universal Robots and the 2F-140 gripper from Robotiq and imported them into NVIDIA Isaac Sim from URDF files and connected them together under one articulation using the GUI and Robot Assembler.

On this page

* [Learning Objectives](#learning-objectives)
* [Prerequisites](#prerequisites)
* [Build and Install the UR Description Package](#build-and-install-the-ur-description-package)
* [Import the UR10e Robot](#import-the-ur10e-robot)
  + [Enable the ROS 2 Robot Description URDF Importer Extension](#enable-the-ros-2-robot-description-urdf-importer-extension)
  + [Launch the URDF Publisher Topic](#launch-the-urdf-publisher-topic)
  + [Import the UR10e Robot into Isaac Sim](#import-the-ur10e-robot-into-isaac-sim)
* [Set Gains Using the Gain Tuner](#set-gains-using-the-gain-tuner)
* [2F-140 Gripper Parameters](#f-140-gripper-parameters)
  + [Expected Parameters for Finger and Knuckle Joints](#expected-parameters-for-finger-and-knuckle-joints)
  + [Expected Parameters for Mimic Joints](#expected-parameters-for-mimic-joints)
* [Connect the UR10e Robot with the Robotiq 2F-140 Gripper](#connect-the-ur10e-robot-with-the-robotiq-2f-140-gripper)
  + [Run the Simulation](#run-the-simulation)
* [Summary](#summary)