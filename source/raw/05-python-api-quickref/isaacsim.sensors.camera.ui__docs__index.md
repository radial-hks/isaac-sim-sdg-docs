---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/py/source/extensions/isaacsim.sensors.camera.ui/docs/index.html
title: "sensors.camera.ui Docs"
section: "Sensors"
module: "05-python-api-quickref"
checksum: "b429ab04f11a3feb"
fetched: "2026-06-21T14:14:27"
---

* [isaacsim.sensors.camera.ui] Isaac Sim Camera Simulation UI Components

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# [isaacsim.sensors.camera.ui] Isaac Sim Camera Simulation UI Components

**Version**: 0.7.1

## Overview

This extension provides UI integration for creating camera and depth sensors in Isaac Sim. It adds menu items to the Create menu and context menus that enable users to create various camera and depth sensor prims from multiple vendors including Orbbec, Leopard Imaging, RealSense, Sensing, SICK, and Stereolabs.

### Functionality

The extension automatically registers sensor creation actions and organizes them into a hierarchical menu structure by vendor. Users can access sensor creation through two main pathways: the main Create menu under “Sensors > Camera and Depth Sensors” and context menus accessible via right-click in the viewport under “Isaac > Sensors”.

**Supported camera sensors include:**

* Leopard Imaging: Hawk, Owl
* Sensing: Multiple SG series models with various configurations
* SICK: Inspector83x

**Supported depth sensors include:**

* Orbbec: Gemini 2, FemtoMega, Gemini 335, Gemini 335L
* RealSense: D455, D457, D555
* Stereolabs: ZED\_X

### Key Components

#### Sensor Creation Actions

The extension creates specialized actions for each supported sensor type using the action registry. For depth sensors, it generates SingleViewDepthSensorAsset instances with proper initialization, while regular camera sensors create standard Xform prims with appropriate USD references.

#### Menu Integration

Menu items are dynamically created and organized by vendor, providing a structured approach to sensor selection. The hierarchical organization helps users locate specific sensor models efficiently within the Isaac Sim interface.

### Integration

The extension uses **omni.kit.actions.core** to register sensor creation actions and **omni.kit.context\_menu** to provide right-click access to sensor creation tools. It currently integrates with the deprecated `isaacsim.sensors.camera` for the underlying sensor implementation (pending migration to `isaacsim.sensors.experimental.rtx`) and `isaacsim.gui.components` for UI component support.

## Enable Extension

The extension can be enabled (if not already) in one of the following ways:

Command-line interface

Define the next entry as an application argument from a terminal.

```python
APP_SCRIPT.(sh|bat) --enable isaacsim.sensors.camera.ui
```

Experience/extension configuration

Define the next entry under `[dependencies]` in an experience (`.kit`) file or an extension configuration (`extension.toml`) file.

```python
[dependencies]
"isaacsim.sensors.camera.ui" = {}
```

Extension Manager UI

Open the *Window > Extensions* menu in a running application instance and search for `isaacsim.sensors.camera.ui`.
Then, toggle the enable control button if it is not already active.

### Actions in isaacsim.sensors.camera.ui

| ID | Display Name | Description |
| --- | --- | --- |
| create\_camera\_hawk |  | Create Hawk camera sensor |
| create\_camera\_inspector83x |  | Create Inspector83x camera sensor |
| create\_camera\_inspectorp61x |  | Create InspectorP61x camera sensor |
| create\_camera\_luxonis\_oak4\_d |  | Create Luxonis OAK4-D camera sensor |
| create\_camera\_luxonis\_oak4\_d\_wide |  | Create Luxonis OAK4-D Wide camera sensor |
| create\_camera\_luxonis\_oak\_d\_pro\_poe |  | Create Luxonis OAK-D Pro PoE camera sensor |
| create\_camera\_luxonis\_oak\_d\_pro\_w\_poe |  | Create Luxonis OAK-D Pro W PoE camera sensor |
| create\_camera\_luxonis\_oak\_d\_tof |  | Create Luxonis OAK-D ToF camera sensor |
| create\_camera\_orbbec\_femtomega |  | Create Orbbec FemtoMega camera sensor |
| create\_camera\_orbbec\_gemini\_2 |  | Create Orbbec Gemini 2 camera sensor |
| create\_camera\_orbbec\_gemini\_335 |  | Create Orbbec Gemini 335 camera sensor |
| create\_camera\_orbbec\_gemini\_335l |  | Create Orbbec Gemini 335L camera sensor |
| create\_camera\_owl |  | Create Owl camera sensor |
| create\_camera\_realsense\_d455 |  | Create Realsense D455 camera sensor |
| create\_camera\_realsense\_d457 |  | Create Realsense D457 camera sensor |
| create\_camera\_realsense\_d555 |  | Create Realsense D555 camera sensor |
| create\_camera\_safevisionary2 |  | Create safeVisionary2 camera sensor |
| create\_camera\_sensing\_sg2\_ar0233c\_5200\_g2a\_h100f1a |  | Create Sensing SG2-AR0233C-5200-G2A-H100F1A camera sensor |
| create\_camera\_sensing\_sg2\_ox03cc\_5200\_gmsl2\_h60ya |  | Create Sensing SG2-OX03CC-5200-GMSL2-H60YA camera sensor |
| create\_camera\_sensing\_sg3\_isx031c\_gmsl2f\_h190xa |  | Create Sensing SG3-ISX031C-GMSL2F-H190XA camera sensor |
| create\_camera\_sensing\_sg5\_imx490c\_5300\_gmsl2\_h110sa |  | Create Sensing SG5-IMX490C-5300-GMSL2-H110SA camera sensor |
| create\_camera\_sensing\_sg8s\_ar0820c\_5300\_g2a\_h120ya |  | Create Sensing SG8S-AR0820C-5300-G2A-H120YA camera sensor |
| create\_camera\_sensing\_sg8s\_ar0820c\_5300\_g2a\_h30ya |  | Create Sensing SG8S-AR0820C-5300-G2A-H30YA camera sensor |
| create\_camera\_sensing\_sg8s\_ar0820c\_5300\_g2a\_h60sa |  | Create Sensing SG8S-AR0820C-5300-G2A-H60SA camera sensor |
| create\_camera\_visionary\_t\_mini |  | Create Visionary-T Mini camera sensor |
| create\_camera\_zed\_x |  | Create ZED\_X camera sensor |

On this page

* [Overview](#overview)
  + [Functionality](#functionality)
  + [Key Components](#key-components)
    - [Sensor Creation Actions](#sensor-creation-actions)
    - [Menu Integration](#menu-integration)
  + [Integration](#integration)
* [Enable Extension](#enable-extension)
  + [Actions in isaacsim.sensors.camera.ui](#actions-in-isaacsim-sensors-camera-ui)