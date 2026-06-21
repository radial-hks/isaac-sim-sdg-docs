---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/digital_twin/troubleshooting.html
title: "Digital Twin Troubleshooting"
section: "数字孪生"
module: "06-sim2real-ue5"
checksum: "7f7aece70a5bcb85"
fetched: "2026-06-21T14:14:29"
---

* [Help & FAQ](../overview/help.html)
* [Troubleshooting](../overview/troubleshooting.html)
* Digital Twin Troubleshooting

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Digital Twin Troubleshooting

This page consolidates troubleshooting information for Digital Twin components in Isaac Sim.

## Warehouse Logistics Issues

### Warehouse Creator Issues

* If warehouse components don’t appear after generation, check for errors in the console logs
* For layout issues, ensure the grid dimensions and spacing are properly configured
* If textures appear incorrect, verify your material settings and check GPU compatibility

### Conveyor Belt Issues

* For non-functioning conveyors, ensure the physics settings are correctly applied
* If objects fall through conveyors, adjust collision settings and physics parameters
* Animation speed issues can be resolved by checking the conveyor speed settings

## Cortex Issues

### Decider Network Issues

* If decision networks fail to initialize, check that all required extensions are enabled
* For unexpected behavior, review your network configurations and connections
* Debug flows by enabling verbose logging and tracing through decisions step by step

### Asset Loading Issues

* Missing assets can be resolved by checking file paths and ensuring assets are available
* For slow loading of complex assets, consider using simpler versions for testing
* USD file compatibility issues may require updating to the latest USD schema

## Mapping Issues

### Occupancy Map Issues

* If occupancy maps fail to generate, ensure the scene has proper collision geometry
* For inaccurate maps, adjust the resolution and sensor parameters
* Missing areas in the map may indicate occlusion issues or raycast failures

On this page

* [Warehouse Logistics Issues](#warehouse-logistics-issues)
  + [Warehouse Creator Issues](#warehouse-creator-issues)
  + [Conveyor Belt Issues](#conveyor-belt-issues)
* [Cortex Issues](#cortex-issues)
  + [Decider Network Issues](#decider-network-issues)
  + [Asset Loading Issues](#asset-loading-issues)
* [Mapping Issues](#mapping-issues)
  + [Occupancy Map Issues](#occupancy-map-issues)