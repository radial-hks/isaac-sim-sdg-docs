---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/digital_twin/warehouse_logistics/logistics_tutorial_cuopt.html
title: "cuOpt Logistics Tutorial"
section: "数字孪生"
module: "06-sim2real-ue5"
checksum: "eaef23cf7d4a2bce"
fetched: "2026-06-21T13:40:03"
---

* [Digital Twin](../index.html)
* NVIDIA cuOpt

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# NVIDIA cuOpt

## Learning Objectives

Demonstrate and provide a reference for the use of [NVIDIA cuOpt](https://developer.nvidia.com/cuopt-logistics-optimization) to solve routing
optimization problems in simulation.

**Topics include:**

* Creation of waypoint network
* Basic interaction with the cuOpt service
* Visualization and processing of optimization specific data
* Intra-warehouse transport use case demonstration

*15-20 Minute Tutorial*

## Getting Started

**Prerequisites**

* Access to the NVIDIA [cuOpt server](https://docs.nvidia.com/cuopt/user-guide/latest/cuopt-server/index.html) and follow the [cuOpt Quickstart Guide](https://docs.nvidia.com/cuopt/user-guide/latest/cuopt-server/quick-start.html) to setup the cuOpt server.
* Review the Core API [Hello World](../../core_api_tutorials/tutorial_core_hello_world.html#isaac-sim-app-tutorial-core-hello-world) and introductory Tutorial series [Robot Setup Tutorials Series](../../robot_setup_tutorials/index.html#isaac-sim-robot-setup-tutorials).
* NVIDIA cuOpt sample extensions are disabled by default. Enable the extensions required for this tutorial from the [Extension Manager](https://docs.omniverse.nvidia.com/extensions/latest/ext_core/ext_extension-manager.html "(in Omniverse Extensions)")
  by searching for `omni.cuopt.examples`. Enabling `omni.cuopt.examples` will automatically enable `omni.cuopt.service` and `omni.cuopt.visualization`

## NVIDIA cuOpt Examples

This tutorial is based around a set of three examples from the `omni.cuopt.examples` extension.
These examples are arranged in increasing fidelity from simple randomized routing problems
with only basic visualization, to an intra-warehouse transport scenario complete with high fidelity
warehouse assets. Each example leverages supporting extensions in order to interact with the cuOpt service
and visualize optimization data. The code for all examples and supporting extensions is available and
can be extended for use in other applications.

### Example Overview

* **Create Network** : An example demonstrating use of visualization tools to create a network. This network can be saved
  and re-used to represent the waypoint graph for optimization problems. Utilities from the `omni.cuopt.visualization` extension
  are used to create and display the waypoint graph.
* **Simple Cost Matrix** : A minimal example using simple primitives to represent a depot based fleet routing problem
  where vehicles start from a depot (Cone) and must fulfill the demand across all locations (Spheres). A cost Matrix
  representing the cost of travel between locations is created by measuring Euclidean distance between points. `omni.cuopt.service`
  is used for communication between scene data and a running cuOpt service instance.
* **Simple Waypoint Graph** : cuOpt also supports a weighted waypoint graph representation of the optimization environment,
  which is the focus of this example. Waypoint graphs are a common representation for interior environments where the cost
  between locations might not be predetermined and straight line distance is not sufficient. Here the waypoint graph represents
  the travel network, and target locations (a subset of graph nodes) represent the locations to be visited and the location
  of the fleet. In addition to using `omni.cuopt.service`, utilities from the `omni.cuopt.visualization` extension are used
  to process and display the waypoint graph as well as the resulting optimized routes. The waypoint graph, order data, and vehicle
  data are all loaded from JSON files that exist alongside the source code for this example and can be modified as needed.
* **Intra-warehouse Transport Demo** : In this example a more complex waypoint graph is generated to represent the transportation network
  for a warehouse environment. You are able to create and place semantic zones to denote high cost areas of travel to be avoided.
  In addition to the utilities used in the Simple Waypoint Graph example, additional functionality from the `omni.cuopt.visualization`
  extension is used to generate the warehouse environment from a JSON configuration files alongside the source code for the example.

### Supporting Extension Overview

* `omni.cuopt.service`: This extension contains a thin wrapper around the cuOpt service that is used for preprocessing
  scene data as well as formatting and sending requests to the cuOpt service. This extension also contains utilities for representing
  the optimization data and formatting text results to be displayed in the UI for the examples.
* `omni.cuopt.visualization`: This extension contains utilities for generating scene data including the waypoint graph, semantics zones
  and the warehouse environment. This extension also contains helper functions for adjusting the weight of graph edges based
  on proximity to a given semantic zone.

## Running cuOpt Examples

### Create Network

1. Starting from a New Isaac Sim Session (`CTRL + N`) navigate to the cuOpt menu item now present in the Isaac Sim interface and select Create Network.
2. In the Create Node section, click CREATE NODE:

   * **Create Node**: Creates a network node at default location. Move the node around to desired position. Multiple network nodes can be created
     one by one.
3. In the Create Edge section, click CREATE EDGE:

   * **Create Edge**: Creates an edge between two nodes. Select two nodes and click on create edge. Multiple edges between nodes can be created in
     the network one by one.
4. The created network will have Nodes and Edges that looks like:
5. Save the network file as USD for future use in optimization problems.
6. Click **Open Source Code** to view the reference implementation.

### Simple Cost Matrix

1. Starting from a New Isaac Sim Session (`CTRL + N`) navigate to the cuOpt menu item now present in the Isaac Sim interface and select Simple Cost Matrix.
2. Enter the credentials assigned to you for the NVIDIA cuOpt managed service.

   > See [Running cuOpt Examples](#credentials-cuopt).
3. In the Optimization Problem Setup section, select values (or use defaults) for the following, then click SETUP PROBLEM:

   * **Fleet Size**: The maximum number of vehicles available. **Note** If a solution can be found using fewer vehicles that solution will be returned.
   * **Vehicle Capacity**: The number of stops (of demand=1) each vehicle can visit.
   * **Number of Locations**: The number of non-depot locations that must be visited.
   * **Solver Time Limit**: The amount of time the cuOpt solver is given to find an optimized solution. **Note** To maintain solution quality additional time should be given for larger problems.
4. In the Run cuOpt section, click SOLVE to return optimized routes. A text representation of the routes is displayed in the UI and results are also shown in the viewport.
5. Click **Open Source Code** to view the reference implementation.

### Simple Waypoint Graph

1. Starting from a New Isaac Sim Session (`CTRL + N`) navigate to the cuOpt menu item now present in the Isaac Sim interface and select Simple Waypoint Graph.
2. Enter the credentials assigned to you for the NVIDIA cuOpt managed service.

   > See [Running cuOpt Examples](#credentials-cuopt).
3. In the Optimization Problem Setup section, click the LOAD buttons from top to bottom (Waypoint Graph, Orders, Vehicles) to setup the problem:

   * **Load Waypoint Graph** Clicking LOAD JSON loads a sample waypoint graph from `/extension_data/waypoint_graph.json`, which exists alongside
     the source code for this example. To load a network from a USD file created using the Create Network tools, drop the file into Stage window
     and click LOAD SCENE. A sample Network.usda is provided in `/extension_data/Network.usda`, which exists alongside
     the source code for this example.
   * **Load Orders** loads sample order data from `/extension_data/order_data.json`, which exists alongside the source code for this example.
     Order locations now appear in green.
   * **Load Vehicles** loads sample vehicle data from `/extension_data/vehicle_data.json`, which exists alongside the source code for this example.
     **Note** Vehicles are assigned to start from Node\_0 position, but are not shown in the viewport.
4. In the Run cuOpt section, click SOLVE to return optimized routes. A text representation of the routes is displayed in the UI and results are also shown in the viewport.
5. Click **Open Source Code** to view the reference implementation.

### Intra-warehouse Transport Demo

1. Starting from a New Isaac Sim Session (`CTRL + N`), navigate to the cuOpt menu item now present in the Isaac Sim interface and select Intra-warehouse Transport Demo.
2. Enter the credentials assigned to you for the NVIDIA cuOpt managed service.

   > See [Running cuOpt Examples](#credentials-cuopt).
3. In the Optimization Problem Setup section, click the LOAD buttons from top to bottom (Sample Warehouse, Waypoint Graph, Orders, Vehicles, Semantic Zone) to setup the problem:

   * **Load Sample Warehouse** loads a sample warehouse defined by `/extension_data/warehouse_building_data.json`, conveyors defined by
     `/extension_data/warehouse_conveyors_data.json` and shelves defined by `/extension_data/warehouse_shelves_data.json`.
     All JSON files can be found alongside the source code for this example.
   * **Load Waypoint Graph** loads a sample waypoint graph from `/extension_data/waypoint_graph.json`, which exists alongside
     the source code for this example.
   * **Load Orders** loads sample order data from `/extension_data/order_data.json`, which exists alongside the source code for this example.
     Order locations now appear in green.
   * **Load Vehicles** loads sample vehicle data from `/extension_data/vehicle_data.json`, which exists alongside the source code for this example.
     **Note** Vehicles are assigned to start from Node\_0 position but are not shown in the viewport.
   * **(OPTIONAL) Create Semantic Zone** creates a semantic zone of user defined size starting at location `(0,0,0)`. If the generated semantic zone
     is placed over one or more edges in the waypoint graph, the edge within that semantic zone is assigned a very high travel cost. cuOpt attempts
     to avoid these edges if possible in the optimized solution. **Note** Each time the Generate button is clicked a new semantic zone is created.
4. In the Run cuOpt section, if a semantic zone has been created or moved, click UPDATE to capture the current weights. Then
   click SOLVE to return optimized routes. A text representation of the routes is displayed in the UI and results is also shown in the viewport.
5. Click **Open Source Code** to view the reference implementation.

## Additional Information

The examples shown here demonstrate only a small subset of cuOpt functionality. For additional features and advanced usage
see the [cuOpt Documentation](https://docs.nvidia.com/cuopt/) and the [cuOpt-Resources Repository](https://github.com/NVIDIA/cuOpt-Resources).

On this page

* [Learning Objectives](#learning-objectives)
* [Getting Started](#getting-started)
* [NVIDIA cuOpt Examples](#nvidia-cuopt-examples)
  + [Example Overview](#example-overview)
  + [Supporting Extension Overview](#supporting-extension-overview)
* [Running cuOpt Examples](#running-cuopt-examples)
  + [Create Network](#create-network)
  + [Simple Cost Matrix](#simple-cost-matrix)
  + [Simple Waypoint Graph](#simple-waypoint-graph)
  + [Intra-warehouse Transport Demo](#intra-warehouse-transport-demo)
* [Additional Information](#additional-information)