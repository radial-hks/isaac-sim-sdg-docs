---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/sensors/isaacsim_sensors_rtx_custom.html
title: "RTX Custom"
section: "Sensors"
module: "09-advanced-optionals"
checksum: "1a04b83d23f4f0cf"
fetched: "2026-06-21T14:14:40"
---

* [Sensors](index.html)
* [RTX Sensors](isaacsim_sensors_rtx.html)
* Creating Custom RTX Sensor Profiles

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Creating Custom RTX Sensor Profiles

Note

This section is under development. Additional content will be added in a future update.

This page covers how to create custom RTX sensor configurations by setting attributes on `OmniLidar` and `OmniRadar` prims.

## Getting Started

When creating custom RTX sensor profiles, it is recommended to start with an existing Lidar or Radar configuration shipped with Isaac Sim as a reference:

* [RTX Lidar Asset Library](../assets/usd_assets_nonvisual_sensors.html#isaac-assets-nonvisual-sensors-rtx-lidar) - Pre-configured Lidar sensors from various vendors
* [RTX Radar Sensor](isaacsim_sensors_rtx_radar.html#isaacsim-sensors-rtx-radar) - RTX Radar documentation and examples

You can load an existing configuration, inspect its USD attributes in the *Property* panel, and modify them to suit your needs.

## Setting Lidar Attributes

RTX Lidar sensors are configured via USD attributes on `OmniLidar` prims using the `OmniSensorGenericLidarCoreAPI` schema.

Key configuration areas include:

* **Output configuration**: Setting coordinate systems, motion compensation, and auxiliary data detail levels
* **Scanning principle**: Configuring rotary vs. solid-state scanning
* **Firing pattern**: Defining scan rate, emitter patterns, and number of returns
* **Field of view**: Constraining azimuth and elevation ranges
* **Intensity modeling**: Configuring beam properties, detector sensitivity, and atmospheric effects

For complete documentation on all Lidar attributes and their values, see [Setting Lidar Attributes](https://docs.omniverse.nvidia.com/kit/docs/omni.sensors.nv.lidar/latest/lidar_extension.html#setting-lidar-attributes) in the Omniverse Lidar Extension documentation.

## Setting Radar Attributes

RTX Radar sensors are configured via USD attributes on `OmniRadar` prims using the `OmniSensorGenericRadarWpmDmatAPI` schema.

For complete documentation on all Radar attributes and their values, see [Setting Radar Attributes](https://docs.omniverse.nvidia.com/kit/docs/omni.sensors.nv.radar/latest/radar_extension.html#setting-radar-attributes) in the Omniverse Radar Extension documentation.

## Schema Reference

For the full USD schema definitions, refer to:

* [OmniSensorGenericLidarCoreAPI Schema](https://docs.omniverse.nvidia.com/kit/docs/omni.usd.schema.omni_sensors/107.3.1/omni_sensors_schema.html#omnisensorgenericlidarcoreapi)
* [OmniSensorGenericLidarCoreEmitterStateAPI Schema](https://docs.omniverse.nvidia.com/kit/docs/omni.usd.schema.omni_sensors/107.3.1/omni_sensors_schema.html#omnisensorgenericlidarcoreemitterstateapi)
* [OmniSensorGenericRadarWpmDmatAPI Schema](https://docs.omniverse.nvidia.com/kit/docs/omni.usd.schema.omni_sensors/107.3.1/omni_sensors_schema.html#omnisensorgenericradarwpmdmatapi)

## Validating Your Configuration

After creating a custom sensor configuration, you can validate it by:

1. Adding the sensor to a scene using the methods described in [RTX Lidar Sensor](isaacsim_sensors_rtx_lidar.html#isaacsim-sensors-rtx-lidar) or [RTX Radar Sensor](isaacsim_sensors_rtx_radar.html#isaacsim-sensors-rtx-radar).
2. Visualizing the sensor output using the [Debug Draw Extension](../utilities/debugging/ext_isaacsim_util_debug_draw.html#isaac-debug-draw) or the techniques described in [Visualizing RTX Lidar Output](isaacsim_sensors_rtx_lidar.html#isaacsim-sensors-rtx-lidar-visualization) and [Visualizing RTX Radar Output](isaacsim_sensors_rtx_radar.html#isaacsim-sensors-rtx-radar-visualization).
3. Collecting data using [RTX Sensor Annotators](isaacsim_sensors_rtx_annotators.html#rtx-sensor-annotator-descriptions) to verify the output matches your expectations.

On this page

* [Getting Started](#getting-started)
* [Setting Lidar Attributes](#setting-lidar-attributes)
* [Setting Radar Attributes](#setting-radar-attributes)
* [Schema Reference](#schema-reference)
* [Validating Your Configuration](#validating-your-configuration)