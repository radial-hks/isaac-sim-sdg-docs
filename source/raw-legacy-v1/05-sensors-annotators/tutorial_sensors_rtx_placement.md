---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/action_and_event_data_generation/tutorial_sensors_rtx_placement.html
title: "Sensors RTX Placement Tutorial"
section: "传感器配置"
module: "05-sensors-annotators"
checksum: "b25fea46eaa26f8e"
fetched: "2026-06-21T13:58:04"
---

* [Synthetic Data Generation](../synthetic_data_generation/index.html)
* [Action and Event Data Generation](index.html)
* RTX Sensors Placement and Calibration

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# RTX Sensors Placement and Calibration

Optimizing camera placement is a crucial technique, particularly in indoor or enclosed spaces such as warehouses, retail stores, hospitals, and other similar environments, to ensure comprehensive coverage while minimizing camera deployment costs.

Isaac Sim provides two separate extensions to help you optimize camera placement and extract calibration data:

* **Camera Placement** (`isaacsim.sensors.rtx.placement`): Automatically determines optimal camera locations based on scene layout and coverage requirements.

  > + [Camera Placement](ext_sensors_rtx_placement/camera_placement.html)
* **Camera Calibration** (`isaacsim.sensors.rtx.calibration`): Extracts and manages camera calibration data, including position, orientation, and field of view information.

  > + [Camera Calibration](ext_sensors_rtx_placement/camera_calibration.html)