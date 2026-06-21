# SimReady Assets

> SimReady 物理资产库 + USD 资产总览 + 物理引擎基础
> Isaac Sim 版本: 6.0
> 最后组装: 2026-06-21 11:55 UTC
> 来源页数: 11

---

## 来源链接

- [USD Assets Overview](https://docs.isaacsim.omniverse.nvidia.com/latest/assets/usd_assets_overview.html)
- [Props](https://docs.isaacsim.omniverse.nvidia.com/latest/assets/usd_assets_props.html)
- [Environments](https://docs.isaacsim.omniverse.nvidia.com/latest/assets/usd_assets_environments.html)
- [Robots](https://docs.isaacsim.omniverse.nvidia.com/latest/assets/usd_assets_robots.html)
- [Sensors](https://docs.isaacsim.omniverse.nvidia.com/latest/assets/usd_assets_sensors.html)
- [Featured](https://docs.isaacsim.omniverse.nvidia.com/latest/assets/usd_assets_featured.html)
- [Third Party](https://docs.isaacsim.omniverse.nvidia.com/latest/assets/usd_assets_third_party.html)
- [Simulation Fundamentals](https://docs.isaacsim.omniverse.nvidia.com/latest/physics/simulation_fundamentals.html)
- [Static Collision](https://docs.isaacsim.omniverse.nvidia.com/latest/physics/physics_static_collision.html)
- [Inspect Physics](https://docs.isaacsim.omniverse.nvidia.com/latest/physics/ext_isaacsim_inspect_physics.html)
- [Physics Index](https://docs.isaacsim.omniverse.nvidia.com/latest/physics/index.html)

---


## 资产库

### USD Assets Overview

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/assets/usd_assets_overview.html

* Isaac Sim Assets

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Isaac Sim Assets

Isaac Sim provides a variety of assets and robots to help you build your virtual world. Some are made specifically for Isaac Sim and robotics applications,
others are made for other NVIDIA Omniverse-based applications. The ones that are available to you by default are all located in the **Window > Browsers** tab.

The [Content Browser](../utilities/content_browser.html#isaac-sim-app-gui-content-browser) is where you can find all of Isaac Sim assets and files. This includes all of the assets listed below, as well as URDF file, config files, policy binaries, and more.

Sample assets are available for download with the [Latest Release](../installation/download.html#isaac-sim-latest-release) of Isaac Sim.
To use this content, you must download the files to the local disk or a Nucleus server.
All asset paths below are assumed to be relative to the default asset root path in the persistent.isaac.asset\_root.default setting. See [Local Assets Packs](../installation/install_faq.html#isaac-sim-setup-assets-content-pack)

Note

Assets will take longer to load when they are accessed for the first time; robots may take multiple minutes to load and larger environment scenes may take as long as ten minutes or more.

## Categories

* [Robot Assets](usd_assets_robots.html)
* [Sensor Assets](usd_assets_sensors.html)
* [Prop Assets](usd_assets_props.html)
* [Environment Assets](usd_assets_environments.html)
* [Featured Assets](usd_assets_featured.html)
* [Third-Party USD Assets](usd_assets_third_party.html)
* [Neural Volume Rendering](usd_assets_nurec.html)

## Omniverse Activity UI

The [Omniverse Activity UI](https://docs.omniverse.nvidia.com/kit/docs/omni.activity.ui) allows you to monitor the progress and activities when assets are being loaded.

Enable the `omni.activity.ui` extension in the Extension Manager (**Window > Extensions** menu),
or launch Isaac Sim from a terminal with the argument `--enable omni.activity.ui`.
Then, open the **Activity Progress** window (**Window > Utilities > Activity Progress** menu) before opening or loading the USD asset to monitor its loading progress.

On this page

* [Categories](#categories)
* [Omniverse Activity UI](#omniverse-activity-ui)

---

### Props

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/assets/usd_assets_props.html

* [Isaac Sim Assets](usd_assets_overview.html)
* Prop Assets

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Prop Assets

## Characters

Listed below are a few characters available in Isaac-Sim, located in the Content Browser inside the `Isaac Sim` folder.

### Police Man

Male character in police uniform with retargeted skeleton.

`People/Characters/original_male_adult_police_04/male_adult_police_04.usd` in the Content Browser.

### Male Doctor

Male character in doctor uniform with retargeted skeleton.

`People/Characters/origial_male_adult_medical_01/male_adult_medical_01.usd` in the Content Browser.

### Police Woman

Female character in police uniform with retargeted skeleton.

`People/Characters/female_adult_police_02/female_adult_police_02.usd` in the Content Browser.

### Construction Worker

Male character in construction uniform with retargeted skeleton.

`People/Characters/origial_male_adult_construction_03/male_adult_construction_03.usd` in the Content Browser.

Note

User can change a characterâs clothing color by modifying materialâs `Property -> Material and Shader` value

Here is an example of how to change male\_adult\_construction\_03âs safety hatâs color

* First, expand the character on the stage menu and navigate to their `Looks` folder. Example - `/World/male_adult_construction_03/Looks`.
* Next, select your target material (Example - `opaque__plastic__hardhat`) and change materialâs `Property -> Material and Shader -> Albedo -> Color Tint` value to adjust characterâs color.

### April Tags

We provide a simple mdl material that can index into a April Tag mosaic image.

To use, add the material to your stage using `Create->April Tag->`

Then create a mesh cube using `Create->Mesh->Cube` and assign the AprilTag material to that prim

The material has the following parameters which need to be configured:

* `Mosaic texture` The path to the texture that contains the grid of April tag images
* `Tag Size` The width/height of the tag in pixels
* `Tags Per Row` The number of tag images per row in the mosaic
* `Spacing` The number of padding pixels between each tag image
* `Tag ID` The index of the tag to use.

The figure below shows example usage using `tag36h11.png`,
after manually creating the mesh cube and assigning the material as described above.

On this page

* [Characters](#characters)
  + [Police Man](#police-man)
  + [Male Doctor](#male-doctor)
  + [Police Woman](#police-woman)
  + [Construction Worker](#construction-worker)
  + [April Tags](#april-tags)

---

### Environments

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/assets/usd_assets_environments.html

* [Isaac Sim Assets](usd_assets_overview.html)
* Environment Assets

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Environment Assets

## Simple Grid

This simple environment contains a flat ground and sides with a grid texture. Three configurations are provided; the first two have square corners, the third has curved corners.

|  |  |  |
| --- | --- | --- |
| search `default_environment.usd` in the Content Browser or using the create menu: *Create>Environments>Flat Grid*   Flat Grid. | search `gridroom_black.usd` in the Content Browser or using the create menu: *Create>Environments>Black Grid*   Black Grid. | search `gridroom_curved.usd` in the Content Browser   Curved Grid. |

## Simple Room

A simple room containing a table.

search `simple_room.usd` in the Content Browser or using the create menu: *Create>Environments>Simple Room*

## Warehouse

A warehouse environment with shelving and objects that can be placed on them. Four configurations are provided:

|  |  |
| --- | --- |
| search `warehouse.usd` in the Content Browser.   A small warehouse with a single shelf. | search `warehouse_with_forklifts.usd` in the Content Browser.   A small warehouse with a single shelf and forklifts. |
| search `warehouse_multiple_shelves.usd` in the Content Browser.   A small warehouse with multiple shelves. | search `full_warehouse.usd` in the Content Browser.   A full-sized warehouse with shelves, obstacles on the floors, and forklifts. |

## Hospital

A hospital environment, with multiple rooms and spaces.

Search `hospital.usd` in the Content Browser.

## Office

An Office Environment, with multiple rooms and an open plan floor.

Search `office.usd` in the Content Browser.

## JetRacer Track

A jetracer track outlined on the ground plane.

Search `jetracer_track_solid.usd` in the Content Browser.

## Small Warehouse Digital Twin

A digital twin of a small warehouse, it can be created using

Search `small_warehouse_digital_twin.usd` in the Content Browser.

On this page

* [Simple Grid](#simple-grid)
* [Simple Room](#simple-room)
* [Warehouse](#warehouse)
* [Hospital](#hospital)
* [Office](#office)
* [JetRacer Track](#jetracer-track)
* [Small Warehouse Digital Twin](#small-warehouse-digital-twin)

---

### Robots

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/assets/usd_assets_robots.html

* [Isaac Sim Assets](usd_assets_overview.html)
* Robot Assets

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Robot Assets

NVIDIA Isaac Sim supports a wide range of robots with differential bases, form factors, and functions.

These robots can be categorized as wheeled robots, holonomic robots, quadruped robots, robotic manipulator and aerial robots (drones). They can be found in the Content Browser in the `Isaac Sim/Robots` folder.

## Multiphysics Robots

A growing subset of the robot assets has also been transformed into multiphysics-ready variants that live in a parallel `Isaac Sim/Robot_Multiphysics` folder, mirroring the directory layout of `Isaac Sim/Robots`. These transformed assets follow the [Asset Structure](../robot_setup/asset_structure.html#isaac-sim-app-reference-asset-structure) guidelines and contain only neutral physics primitives, so they can be loaded by the Newton physics backend without PhysX-specific schema contamination.

For each robot in the catalog below that has been transformed, a **Multiphysics USD Path** is listed alongside the original **USD Path** (relative to the `Isaac Sim/Robot_Multiphysics` folder). Entries marked with  have been verified to behave like the original robot; unmarked entries are still undergoing validation and may exhibit issues.

Users are encouraged to start migrating their workflows to the multiphysics assets. Once conversion and validation is complete across the full catalog, the multiphysics variants will replace the original assets in a future release.

Wheeled

**iRobot**

Create3

**USD Path:** iRobot/Create3/create\_3.usd

**Multiphysics USD Path:** iRobot/Create3/create\_3/create\_3.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 4 |
| Number of Links | 5 |
| Number of DOFs | 4 |

**Physics APIs:**

* PhysX SceneAPI
* PhysX ArticulationAPI
* PhysX JointAPI

**License:** [BSD-3](https://github.com/iRobotEducation/create3_sim/tree/main)

**Turtlebot**

Turtlebot3

**USD Path:** Turtlebot/Turtlebot3/turtlebot3\_burger.usd

**Multiphysics USD Path:** Turtlebot/Turtlebot3/turtlebot3\_burger/turtlebot3\_burger.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 2 |
| Number of Links | 3 |
| Number of DOFs | 2 |

**Physics APIs:**

* PhysX ArticulationAPI
* PhysX JointAPI

**License:** [Apache 2.0](https://github.com/ROBOTIS-GIT/turtlebot3/tree/master/turtlebot3_description)

**NVIDIA**

Robomaker

**USD Path:** NVIDIA/Robomaker/aws\_robomaker\_jetbot.usd

**Multiphysics USD Path:** NVIDIA/Robomaker/aws\_robomaker\_jetbot/aws\_robomaker\_jetbot.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 5 |
| Number of Links | 6 |
| Number of DOFs | 2 |

**Physics APIs:**

* PhysX SceneAPI
* PhysX ArticulationAPI
* PhysX JointAPI

**License:** [MIT](https://github.com/aws-samples/aws-robomaker-jetbot-ros/blob/main/LICENSE)

NovaCarter

**USD Path:** NVIDIA/NovaCarter/nova\_carter.usd

Properties

|  |  |
| --- | --- |
| Number of Joints | 7 |
| Number of Links | 8 |
| Number of DOFs | 7 |

| Sensor/Accessory | Count |
| --- | --- |
| Camera | 12 |
| IMU | 5 |
| OmniSensor Lidar | 3 |

**Physics APIs:**

* PhysX RigidBodyAPI
* PhysX ArticulationAPI
* PhysX JointAPI
* PhysX CollisionAPI

**License:** [`3D Content Sharing Agreement`](../_downloads/fff9a78678f4f7d4848611da166427d1/3D%20Content%20Sharing%20-%20Nova%20Carter.pdf)

Leatherback

**USD Path:** NVIDIA/Leatherback/leatherback.usd

**Multiphysics USD Path:** NVIDIA/Leatherback/leatherback.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 26 |
| Number of Links | 27 |
| Number of DOFs | 26 |

| Sensors | Count |
| --- | --- |
| Camera | 4 |

**Physics APIs:**

* PhysX ArticulationAPI
* PhysX CollisionAPI

**License:** NVIDIA

Jetbot

**USD Path:** NVIDIA/Jetbot/jetbot.usd

**Multiphysics USD Path:** NVIDIA/Jetbot/jetbot.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 2 |
| Number of Links | 3 |
| Number of DOFs | 2 |

| Sensors | Count |
| --- | --- |
| Camera | 2 |

**Physics APIs:**

* PhysX RigidBodyAPI
* PhysX ArticulationAPI
* PhysX JointAPI
* PhysX CollisionAPI
* PhysX SceneAPI

**License:** Email confirmation: [Jetbot 3D drawing](http://www.waveshare.net/w/upload/4/49/Jetbot_3D_Drawing.zip)

Carter

Variant 1

**USD Path:** NVIDIA/Carter/carter\_v1.usd

**Multiphysics USD Path:** NVIDIA/Carter/carter\_v1/carter\_v1.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 6 |
| Number of Links | 7 |
| Number of DOFs | 4 |

| Sensors | Count |
| --- | --- |
| Camera | 5 |

**Physics APIs:**

* PhysX RigidBodyAPI
* PhysX ArticulationAPI
* PhysX JointAPI
* PhysX CollisionAPI
* PhysX SceneAPI

**License:** NVIDIA

Variant 2

**USD Path:** NVIDIA/Carter/carter\_v1\_physx\_lidar.usd

Properties

|  |  |
| --- | --- |
| Number of Joints | 6 |
| Number of Links | 7 |
| Number of DOFs | 4 |

| Sensors | Count |
| --- | --- |
| Camera | 4 |

**Physics APIs:**

* PhysX RigidBodyAPI
* PhysX ArticulationAPI
* PhysX JointAPI
* PhysX CollisionAPI
* PhysX SceneAPI

**License:** NVIDIA

**IsaacSim**

ForkliftC

**USD Path:** IsaacSim/ForkliftC/forklift\_c.usd

**Multiphysics USD Path:** IsaacSim/ForkliftC/forklift\_c/forklift\_c.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 7 |
| Number of Links | 8 |
| Number of DOFs | 7 |

**Physics APIs:**

* PhysX RigidBodyAPI
* PhysX ArticulationAPI
* PhysX CollisionAPI

ForkliftB

Variant 1

**USD Path:** IsaacSim/ForkliftB/forklift\_b.usd

**Multiphysics USD Path:** IsaacSim/ForkliftB/forklift\_b/forklift\_b.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 7 |
| Number of Links | 8 |
| Number of DOFs | 7 |

**Physics APIs:**

* PhysX RigidBodyAPI
* PhysX ArticulationAPI
* PhysX CollisionAPI

Variant 2

**USD Path:** IsaacSim/ForkliftB/forklift\_b\_sensor.usd

Properties

|  |  |
| --- | --- |
| Number of Joints | N/A |
| Number of Links | N/A |
| Number of DOFs | N/A |

| Sensor/Accessory | Count |
| --- | --- |
| Camera | 6 |
| IMU | 3 |
| OmniSensor Lidar | 1 |

**Physics APIs:**

* PhysX RigidBodyAPI
* PhysX ArticulationAPI
* PhysX CollisionAPI

**Idealworks**

iwhub

Variant 1

**USD Path:** Idealworks/iwhub/iw\_hub.usd

**Multiphysics USD Path:** Idealworks/iwhub/iw\_hub/iw\_hub.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 7 |
| Number of Links | 8 |
| Number of DOFs | 7 |

**Physics APIs:**

* PhysX RigidBodyAPI
* PhysX ArticulationAPI
* PhysX JointAPI
* PhysX CollisionAPI
* PhysX SceneAPI

Variant 2

**USD Path:** Idealworks/iwhub/iw\_hub\_sensors.usd

Properties

|  |  |
| --- | --- |
| Number of Joints | N/A |
| Number of Links | N/A |
| Number of DOFs | N/A |

| Sensors | Count |
| --- | --- |
| Camera | 2 |

**Physics APIs:**

* PhysX RigidBodyAPI
* PhysX CollisionAPI
* PhysX JointAPI
* PhysX ArticulationAPI
* PhysX SceneAPI

Variant 3

**USD Path:** Idealworks/iwhub/iw\_hub\_static.usd

Properties

|  |  |
| --- | --- |
| Number of Joints | N/A |
| Number of Links | N/A |
| Number of DOFs | N/A |

**Fraunhofer**

Evobot

**USD Path:** Fraunhofer/Evobot/evobot.usd

**Multiphysics USD Path:** Fraunhofer/Evobot/evobot.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 14 |
| Number of Links | 15 |
| Number of DOFs | 12 |

**Physics APIs:**

* PhysX RigidBodyAPI
* PhysX JointAPI
* PhysX CollisionAPI
* PhysX ArticulationAPI
* PhysX SceneAPI

**License:** [`3D Content Sharing Agreement`](../_downloads/28ec2cf24f402cb152a4463028986107/CLA-1_OpenLogisticsFoundation_Fraunhofer_-_NVIDIA.pdf)

**Clearpath**

Jackal

Variant 1

**USD Path:** Clearpath/Jackal/jackal.usd

**Multiphysics USD Path:** Clearpath/Jackal/jackal.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 4 |
| Number of Links | 5 |
| Number of DOFs | 4 |

| Sensor/Accessory | Count |
| --- | --- |
| Camera | 2 |
| IMU | 1 |

**Physics APIs:**

* PhysX SceneAPI
* PhysX ArticulationAPI
* PhysX JointAPI

**License:** [BSD-3](https://github.com/jackal/jackal/blob/noetic-devel/LICENSE)

Variant 2

**USD Path:** Clearpath/Jackal/jackal\_basic.usd

Properties

|  |  |
| --- | --- |
| Number of Joints | 4 |
| Number of Links | 5 |
| Number of DOFs | 4 |

**Physics APIs:**

* PhysX SceneAPI
* PhysX ArticulationAPI
* PhysX JointAPI

**License:** [BSD-3](https://github.com/jackal/jackal/blob/noetic-devel/LICENSE)

Dingo

Variant 1

**USD Path:** Clearpath/Dingo/dingo.usd

**Multiphysics USD Path:** Clearpath/Dingo/dingo.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 2 |
| Number of Links | 3 |
| Number of DOFs | 2 |

| Sensors | Count |
| --- | --- |
| Camera | 2 |

**Physics APIs:**

* PhysX SceneAPI
* PhysX ArticulationAPI
* PhysX JointAPI

**License:** [BSD-3](https://github.com/dingo-cpr/dingo/blob/noetic-devel/dingo_description/package.xml)

Variant 2

**USD Path:** Clearpath/Dingo/dingo\_basic.usd

Properties

|  |  |
| --- | --- |
| Number of Joints | 2 |
| Number of Links | 3 |
| Number of DOFs | 2 |

**Physics APIs:**

* PhysX SceneAPI
* PhysX ArticulationAPI
* PhysX JointAPI

**License:** [BSD-3](https://github.com/dingo-cpr/dingo/blob/noetic-devel/dingo_description/package.xml)

**AgilexRobotics**

limo

**USD Path:** AgilexRobotics/limo/limo.usd

**Multiphysics USD Path:** AgilexRobotics/limo/limo.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 4 |
| Number of Links | 5 |
| Number of DOFs | 4 |

| Sensors | Count |
| --- | --- |
| Camera | 1 |

**Physics APIs:**

* PhysX SceneAPI
* PhysX ArticulationAPI
* PhysX JointAPI
* PhysX CollisionAPI

**License:** [BSD-3](https://github.com/agilexrobotics/Limo-Isaac-Sim)

Manipulator

**Yaskawa**

Motoman Next

NHC12

**USD Path:** Yaskawa/Motoman Next/NHC12/NHC12\_A00.usd

Properties

|  |  |
| --- | --- |
| Number of Joints | 6 |
| Number of Links | 7 |
| Number of DOFs | 6 |

**Physics APIs:**

* PhysX ArticulationAPI
* PhysX JointAPI

**License:** [`3D Content Sharing Agreement`](../_downloads/1cf451af09cc528ee266470e6c74efc4/3D%20Content%20Sharing_YASKAWA%20Signed.pdf)

NEX7

**USD Path:** Yaskawa/Motoman Next/NEX7/NEX7\_C00\_c00.usd

Properties

|  |  |
| --- | --- |
| Number of Joints | 6 |
| Number of Links | 7 |
| Number of DOFs | 6 |

**Physics APIs:**

* PhysX ArticulationAPI
* PhysX JointAPI

**License:** [`3D Content Sharing Agreement`](../_downloads/1cf451af09cc528ee266470e6c74efc4/3D%20Content%20Sharing_YASKAWA%20Signed.pdf)

NEX4

**USD Path:** Yaskawa/Motoman Next/NEX4/NEX4\_C00.usd

Properties

|  |  |
| --- | --- |
| Number of Joints | 6 |
| Number of Links | 7 |
| Number of DOFs | 6 |

**Physics APIs:**

* PhysX ArticulationAPI
* PhysX JointAPI

**License:** [`3D Content Sharing Agreement`](../_downloads/1cf451af09cc528ee266470e6c74efc4/3D%20Content%20Sharing_YASKAWA%20Signed.pdf)

NEX35

**USD Path:** Yaskawa/Motoman Next/NEX35/NEX35\_C00.usd

Properties

|  |  |
| --- | --- |
| Number of Joints | 6 |
| Number of Links | 7 |
| Number of DOFs | 6 |

**Physics APIs:**

* PhysX ArticulationAPI
* PhysX JointAPI

**License:** [`3D Content Sharing Agreement`](../_downloads/1cf451af09cc528ee266470e6c74efc4/3D%20Content%20Sharing_YASKAWA%20Signed.pdf)

NEX20

**USD Path:** Yaskawa/Motoman Next/NEX20/NEX20\_C00.usd

Properties

|  |  |
| --- | --- |
| Number of Joints | 6 |
| Number of Links | 7 |
| Number of DOFs | 6 |

**Physics APIs:**

* PhysX ArticulationAPI
* PhysX JointAPI

**License:** [`3D Content Sharing Agreement`](../_downloads/1cf451af09cc528ee266470e6c74efc4/3D%20Content%20Sharing_YASKAWA%20Signed.pdf)

NEX10

**USD Path:** Yaskawa/Motoman Next/NEX10/NEX10\_C00.usd

Properties

|  |  |
| --- | --- |
| Number of Joints | 6 |
| Number of Links | 7 |
| Number of DOFs | 6 |

**Physics APIs:**

* PhysX ArticulationAPI
* PhysX JointAPI

**License:** [`3D Content Sharing Agreement`](../_downloads/1cf451af09cc528ee266470e6c74efc4/3D%20Content%20Sharing_YASKAWA%20Signed.pdf)

**Yahboom**

Dofbot

**USD Path:** Yahboom/Dofbot/dofbot.usd

**Multiphysics USD Path:** Yahboom/Dofbot/dofbot.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 11 |
| Number of Links | 12 |
| Number of DOFs | 11 |

| Sensors | Count |
| --- | --- |
| Camera | 1 |

**Physics APIs:**

* PhysX RigidBodyAPI
* PhysX ArticulationAPI
* PhysX JointAPI
* PhysX CollisionAPI
* PhysX SceneAPI

**License:** Email confirmation: [Yahboom Technology](https://github.com/YahboomTechnology/dofbot-jetson_nano)

**WonikRobotics**

AllegroHand

Variant 1

**USD Path:** WonikRobotics/AllegroHand/allegro.usd

**Multiphysics USD Path:** WonikRobotics/AllegroHand/allegro/allegro.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 20 |
| Number of Links | 21 |
| Number of DOFs | 16 |

**Physics APIs:**

* PhysX SceneAPI
* PhysX ArticulationAPI
* PhysX JointAPI

**License:** [BSD-2](https://github.com/simlabrobotics/allegro_hand_ros_v4/blob/master/LICENSE)

Variant 2

**USD Path:** WonikRobotics/AllegroHand/allegro\_hand.usd

Properties

|  |  |
| --- | --- |
| Number of Joints | 20 |
| Number of Links | 21 |
| Number of DOFs | 16 |

**Physics APIs:**

* PhysX SceneAPI
* PhysX ArticulationAPI
* PhysX JointAPI
* PhysX CollisionAPI

**License:** [BSD-2](https://github.com/simlabrobotics/allegro_hand_ros_v4/blob/master/LICENSE)

Variant 3

**USD Path:** WonikRobotics/AllegroHand/allegro\_hand\_instanceable.usd

Properties

|  |  |
| --- | --- |
| Number of Joints | 20 |
| Number of Links | 21 |
| Number of DOFs | 16 |

**Physics APIs:**

* PhysX SceneAPI
* PhysX ArticulationAPI
* PhysX JointAPI

* This robot is in Isaac Lab

**License:** [BSD-2](https://github.com/simlabrobotics/allegro_hand_ros_v4/blob/master/LICENSE)

**UniversalRobots**

ur5e

**USD Path:** UniversalRobots/ur5e/ur5e.usd

**Multiphysics USD Path:** UniversalRobots/ur5e/ur5e.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 6 |
| Number of Links | 7 |
| Number of DOFs | 6 |

**Physics APIs:**

* PhysX JointAPI
* PhysX ArticulationAPI

**License:** [BSD-3](https://github.com/fmauch/universal_robot)

ur5

**USD Path:** UniversalRobots/ur5/ur5.usd

**Multiphysics USD Path:** UniversalRobots/ur5/ur5.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 6 |
| Number of Links | 7 |
| Number of DOFs | 6 |

**Physics APIs:**

* PhysX JointAPI
* PhysX ArticulationAPI

**License:** [BSD-3](https://github.com/fmauch/universal_robot)

ur3e

**USD Path:** UniversalRobots/ur3e/ur3e.usd

**Multiphysics USD Path:** UniversalRobots/ur3e/ur3e.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 6 |
| Number of Links | 7 |
| Number of DOFs | 6 |

**Physics APIs:**

* PhysX JointAPI
* PhysX ArticulationAPI

**License:** [BSD-3](https://github.com/fmauch/universal_robot)

ur30

**USD Path:** UniversalRobots/ur30/ur30.usd

**Multiphysics USD Path:** UniversalRobots/ur30/ur30.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 6 |
| Number of Links | 7 |
| Number of DOFs | 6 |

**Physics APIs:**

* PhysX RigidBodyAPI
* PhysX JointAPI
* PhysX ArticulationAPI

**License:** [BSD-3](https://github.com/fmauch/universal_robot)

ur3

**USD Path:** UniversalRobots/ur3/ur3.usd

**Multiphysics USD Path:** UniversalRobots/ur3/ur3.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 6 |
| Number of Links | 7 |
| Number of DOFs | 6 |

**Physics APIs:**

* PhysX JointAPI
* PhysX ArticulationAPI

**License:** [BSD-3](https://github.com/fmauch/universal_robot)

ur20

**USD Path:** UniversalRobots/ur20/ur20.usd

**Multiphysics USD Path:** UniversalRobots/ur20/ur20.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 6 |
| Number of Links | 7 |
| Number of DOFs | 6 |

**Physics APIs:**

* PhysX JointAPI
* PhysX ArticulationAPI

**License:** [BSD-3](https://github.com/fmauch/universal_robot)

ur16e

**USD Path:** UniversalRobots/ur16e/ur16e.usd

**Multiphysics USD Path:** UniversalRobots/ur16e/ur16e.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 6 |
| Number of Links | 7 |
| Number of DOFs | 6 |

**Physics APIs:**

* PhysX JointAPI
* PhysX ArticulationAPI

**License:** [BSD-3](https://github.com/fmauch/universal_robot)

ur10e

**USD Path:** UniversalRobots/ur10e/ur10e.usd

**Multiphysics USD Path:** UniversalRobots/ur10e/ur10e.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 6 |
| Number of Links | 7 |
| Number of DOFs | 6 |

**Accessories:**

* Robotiq\_2f\_140
* Robotiq\_2f\_85

**Physics APIs:**

* PhysX JointAPI
* PhysX ArticulationAPI

**License:** [BSD-3](https://github.com/fmauch/universal_robot)

ur10

**USD Path:** UniversalRobots/ur10/ur10.usd

**Multiphysics USD Path:** UniversalRobots/ur10/ur10.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 7 |
| Number of Links | 8 |
| Number of DOFs | 6 |

**Accessories:**

* Long\_Suction
* Short\_Suction

**Physics APIs:**

* PhysX RigidBodyAPI
* PhysX JointAPI
* PhysX ArticulationAPI

**License:** [BSD-3](https://github.com/fmauch/universal_robot)

**Unitree**

Z1

**USD Path:** Unitree/Z1/z1.usd

**Multiphysics USD Path:** Unitree/Z1/z1.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 6 |
| Number of Links | 7 |
| Number of DOFs | 6 |

**Physics APIs:**

* PhysX ArticulationAPI
* PhysX JointAPI

**License:** [BSD-3](https://github.com/unitreerobotics/unitree_ros)

Dex5

**USD Path:** Unitree/Dex5/Dex5-URDF-R.usda

**Multiphysics USD Path:** Unitree/Dex5/Dex5-URDF-R/Dex5-URDF-R.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 20 |
| Number of Links | 21 |
| Number of DOFs | 20 |

**Physics APIs:**

* PhysX JointAPI
* PhysX ArticulationAPI

**License:** [BSD-3](https://github.com/unitreerobotics/unitree_ros)

Dex3

**USD Path:** Unitree/Dex3/dex3\_1\_r.usd

**Multiphysics USD Path:** Unitree/Dex3/dex3\_1\_r/dex3\_1\_r.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 7 |
| Number of Links | 8 |
| Number of DOFs | 7 |

**Physics APIs:**

* PhysX JointAPI
* PhysX ArticulationAPI

**License:** [BSD-3](https://github.com/unitreerobotics/unitree_ros)

**Ufactory**

xarm\_gripper

**USD Path:** Ufactory/xarm\_gripper/xarm\_gripper.usd

**Multiphysics USD Path:** Ufactory/xarm\_gripper/xarm\_gripper.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 6 |
| Number of Links | 7 |
| Number of DOFs | 6 |

**Physics APIs:**

* PhysX MimicJointAPI
* PhysX JointAPI
* PhysX ArticulationAPI

**License:** [`3D Content Sharing Agreement`](../_downloads/f609985d6b88ccff9540d799aa0bb7a8/3D%20Content%20Sharing%201_Ufactory.pdf)

xarm7

**USD Path:** Ufactory/xarm7/xarm7.usd

**Multiphysics USD Path:** Ufactory/xarm7/xarm7.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 14 |
| Number of Links | 15 |
| Number of DOFs | 13 |

**Physics APIs:**

* PhysX MimicJointAPI
* PhysX JointAPI
* PhysX ArticulationAPI

**License:** [`3D Content Sharing Agreement`](../_downloads/f609985d6b88ccff9540d799aa0bb7a8/3D%20Content%20Sharing%201_Ufactory.pdf)

xarm6

**USD Path:** Ufactory/xarm6/xarm6.usd

**Multiphysics USD Path:** Ufactory/xarm6/xarm6.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 13 |
| Number of Links | 14 |
| Number of DOFs | 12 |

**Physics APIs:**

* PhysX MimicJointAPI
* PhysX JointAPI
* PhysX ArticulationAPI

**License:** [`3D Content Sharing Agreement`](../_downloads/f609985d6b88ccff9540d799aa0bb7a8/3D%20Content%20Sharing%201_Ufactory.pdf)

uf850

**USD Path:** Ufactory/uf850/uf850.usd

**Multiphysics USD Path:** Ufactory/uf850/uf850.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 6 |
| Number of Links | 7 |
| Number of DOFs | 6 |

**Physics APIs:**

* PhysX JointAPI
* PhysX ArticulationAPI

**License:** [`3D Content Sharing Agreement`](../_downloads/f609985d6b88ccff9540d799aa0bb7a8/3D%20Content%20Sharing%201_Ufactory.pdf)

lite6\_gripper

**USD Path:** Ufactory/lite6\_gripper/uf\_lite\_gripper.usd

**Multiphysics USD Path:** Ufactory/lite6\_gripper/uf\_lite\_gripper/uf\_lite\_gripper.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 2 |
| Number of Links | 3 |
| Number of DOFs | 2 |

**Physics APIs:**

* PhysX MimicJointAPI
* PhysX JointAPI
* PhysX ArticulationAPI
* PhysX RigidBodyAPI

**License:** [`3D Content Sharing Agreement`](../_downloads/f609985d6b88ccff9540d799aa0bb7a8/3D%20Content%20Sharing%201_Ufactory.pdf)

lite6

**USD Path:** Ufactory/lite6/lite6.usd

**Multiphysics USD Path:** Ufactory/lite6/lite6.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 6 |
| Number of Links | 7 |
| Number of DOFs | 6 |

**Physics APIs:**

* PhysX JointAPI
* PhysX ArticulationAPI

**License:** [`3D Content Sharing Agreement`](../_downloads/f609985d6b88ccff9540d799aa0bb7a8/3D%20Content%20Sharing%201_Ufactory.pdf)

**Techman**

TM12

**USD Path:** Techman/TM12/tm12.usd

**Multiphysics USD Path:** Techman/TM12/tm12.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 9 |
| Number of Links | 10 |
| Number of DOFs | 6 |

| Sensors | Count |
| --- | --- |
| Camera | 1 |

**Physics APIs:**

* PhysX RigidBodyAPI
* PhysX ArticulationAPI
* PhysX SceneAPI
* PhysX JointAPI

**License:** [`3D Content Sharing Agreement`](../_downloads/806f9c68c8b77362719b0e9225321d07/Techman%20-%20Signed%203D%20Content%20Sharing.pdf)

**ShadowRobot**

ShadowHand

Variant 1

**USD Path:** ShadowRobot/ShadowHand/shadow\_hand.usd

**Multiphysics USD Path:** ShadowRobot/ShadowHand/shadow\_hand/shadow\_hand.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 25 |
| Number of Links | 26 |
| Number of DOFs | 24 |

**Physics APIs:**

* PhysX RigidBodyAPI
* PhysX ArticulationAPI
* PhysX JointAPI
* PhysX CollisionAPI

**License:** [BSD-3](https://github.com/shadow-robot/sr_common/blob/noetic-devel/LICENSE)

Variant 2

**USD Path:** ShadowRobot/ShadowHand/shadow\_hand\_instanceable.usd

**Multiphysics USD Path:** ShadowRobot/ShadowHandNewton/shadow\_hand\_instanceable/shadow\_hand\_instanceable.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 25 |
| Number of Links | 26 |
| Number of DOFs | 24 |

**Physics APIs:**

* PhysX RigidBodyAPI
* PhysX ArticulationAPI
* PhysX JointAPI

* This robot is in Isaac Lab

**License:** [BSD-3](https://github.com/shadow-robot/sr_common/blob/noetic-devel/LICENSE)

**Robotiq**

Hand-E

Variant 1

**USD Path:** Robotiq/Hand-E/Robotiq\_Hand\_E\_base.usd

**Multiphysics USD Path:** Robotiq/Hand-E/Robotiq\_Hand\_E\_base/Robotiq\_Hand\_E\_base.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 2 |
| Number of Links | 3 |
| Number of DOFs | 2 |

**Physics APIs:**

* PhysX ArticulationAPI

**License:** [`3D Content Sharing Agreement`](../_downloads/04fbcbc1621bb54adc09e6adce7cfc49/NVIDIA%20-%20Robotiq%203D%20Content%20Sharing.docx.pdf)

Variant 2

**USD Path:** Robotiq/Hand-E/Robotiq\_Hand\_E\_edit.usd

Properties

|  |  |
| --- | --- |
| Number of Joints | 2 |
| Number of Links | 3 |
| Number of DOFs | 2 |

**Physics APIs:**

* PhysX ArticulationAPI

**License:** [`3D Content Sharing Agreement`](../_downloads/04fbcbc1621bb54adc09e6adce7cfc49/NVIDIA%20-%20Robotiq%203D%20Content%20Sharing.docx.pdf)

2F-85

**USD Path:** Robotiq/2F-85/Robotiq\_2F\_85\_edit.usd

**Multiphysics USD Path:** Robotiq/2F-85/Robotiq\_2F\_85.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 8 |
| Number of Links | 9 |
| Number of DOFs | 6 |

**Physics APIs:**

* PhysX MimicJointAPI
* PhysX ArticulationAPI
* PhysX JointAPI

**License:** [`3D Content Sharing Agreement`](../_downloads/04fbcbc1621bb54adc09e6adce7cfc49/NVIDIA%20-%20Robotiq%203D%20Content%20Sharing.docx.pdf)

2F-140

Variant 1

**USD Path:** Robotiq/2F-140/2f140\_instanceable.usd

Properties

|  |  |
| --- | --- |
| Number of Joints | 10 |
| Number of Links | 11 |
| Number of DOFs | 6 |

**Physics APIs:**

* PhysX ArticulationAPI
* PhysX JointAPI

**License:** [`3D Content Sharing Agreement`](../_downloads/04fbcbc1621bb54adc09e6adce7cfc49/NVIDIA%20-%20Robotiq%203D%20Content%20Sharing.docx.pdf)

Variant 2

**USD Path:** Robotiq/2F-140/Robotiq\_2F\_140\_base.usd

**Multiphysics USD Path:** Robotiq/2F-140/Robotiq\_2F\_140.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 8 |
| Number of Links | 9 |
| Number of DOFs | 8 |

**Physics APIs:**

* PhysX ArticulationAPI

**License:** [`3D Content Sharing Agreement`](../_downloads/04fbcbc1621bb54adc09e6adce7cfc49/NVIDIA%20-%20Robotiq%203D%20Content%20Sharing.docx.pdf)

Variant 3

**USD Path:** Robotiq/2F-140/Robotiq\_2F\_140\_config.usd

Properties

|  |  |
| --- | --- |
| Number of Joints | 10 |
| Number of Links | 11 |
| Number of DOFs | 10 |

| Sensor/Accessory | Count |
| --- | --- |
| Contact Sensor | 1 |

**Physics APIs:**

* PhysX RigidBodyAPI
* PhysX ArticulationAPI
* PhysX JointAPI
* PhysX SceneAPI
* PhysX ResidualReportingAPI
* PhysX MimicJointAPI

**License:** [`3D Content Sharing Agreement`](../_downloads/04fbcbc1621bb54adc09e6adce7cfc49/NVIDIA%20-%20Robotiq%203D%20Content%20Sharing.docx.pdf)

Variant 4

**USD Path:** Robotiq/2F-140/Robotiq\_2F\_140\_physics\_edit.usd

Properties

|  |  |
| --- | --- |
| Number of Joints | 8 |
| Number of Links | 9 |
| Number of DOFs | 8 |

| Sensor/Accessory | Count |
| --- | --- |
| Contact Sensor | 1 |

**Physics APIs:**

* PhysX RigidBodyAPI
* PhysX ArticulationAPI
* PhysX MimicJointAPI
* PhysX JointAPI

**License:** [`3D Content Sharing Agreement`](../_downloads/04fbcbc1621bb54adc09e6adce7cfc49/NVIDIA%20-%20Robotiq%203D%20Content%20Sharing.docx.pdf)

Variant 5

**USD Path:** Robotiq/2F-140/Collected\_2f140\_instanceable/2f140\_instanceable.usd

Properties

|  |  |
| --- | --- |
| Number of Joints | 10 |
| Number of Links | 11 |
| Number of DOFs | 6 |

**Physics APIs:**

* PhysX ArticulationAPI
* PhysX JointAPI

**License:** [`3D Content Sharing Agreement`](../_downloads/04fbcbc1621bb54adc09e6adce7cfc49/NVIDIA%20-%20Robotiq%203D%20Content%20Sharing.docx.pdf)

**Psyonic**

ability\_hand\_left\_large

**USD Path:** Psyonic/ability\_hand\_left\_large/ability\_hand\_left\_large.usd

**Multiphysics USD Path:** Psyonic/ability\_hand\_left\_large/ability\_hand\_left\_large.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 12 |
| Number of Links | 13 |
| Number of DOFs | 11 |

**Physics APIs:**

* PhysX ArticulationAPI
* PhysX JointAPI

**License:** [`3D Content Sharing Agreement`](../_downloads/0718f65e8dfb51dc8ec9d1b07c6ceca5/3D%20Content%20Sharing%20Agreement_Psyonic%20Inc.pdf)

ability\_hand\_left\_small

**USD Path:** Psyonic/ability\_hand\_left\_small/ability\_hand\_left\_small.usd

**Multiphysics USD Path:** Psyonic/ability\_hand\_left\_small/ability\_hand\_left\_small.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 12 |
| Number of Links | 13 |
| Number of DOFs | 11 |

**Physics APIs:**

* PhysX ArticulationAPI
* PhysX JointAPI

**License:** [`3D Content Sharing Agreement`](../_downloads/0718f65e8dfb51dc8ec9d1b07c6ceca5/3D%20Content%20Sharing%20Agreement_Psyonic%20Inc.pdf)

ability\_hand\_right\_large

**USD Path:** Psyonic/ability\_hand\_right\_large/ability\_hand\_right\_large.usd

**Multiphysics USD Path:** Psyonic/ability\_hand\_right\_large/ability\_hand\_right\_large.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 12 |
| Number of Links | 13 |
| Number of DOFs | 11 |

**Physics APIs:**

* PhysX ArticulationAPI
* PhysX JointAPI

**License:** [`3D Content Sharing Agreement`](../_downloads/0718f65e8dfb51dc8ec9d1b07c6ceca5/3D%20Content%20Sharing%20Agreement_Psyonic%20Inc.pdf)

ability\_hand\_right\_small

**USD Path:** Psyonic/ability\_hand\_right\_small/ability\_hand\_right\_small.usd

**Multiphysics USD Path:** Psyonic/ability\_hand\_right\_small/ability\_hand\_right\_small.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 12 |
| Number of Links | 13 |
| Number of DOFs | 11 |

**Physics APIs:**

* PhysX ArticulationAPI
* PhysX JointAPI

**License:** [`3D Content Sharing Agreement`](../_downloads/0718f65e8dfb51dc8ec9d1b07c6ceca5/3D%20Content%20Sharing%20Agreement_Psyonic%20Inc.pdf)

**Schunk**

egk\_25

**USD Path:** Schunk/egk\_25/schunk\_egk\_25.usd

**Multiphysics USD Path:** Schunk/egk\_25/schunk\_egk\_25/schunk\_egk\_25.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 2 |
| Number of Links | 3 |
| Number of DOFs | 2 |

**Physics APIs:**

* PhysX ArticulationAPI
* PhysX JointAPI

**License:** [`3D Content Sharing Agreement`](../_downloads/6d42d30807cdc55fd6d3b7efc4d7f7ba/3D%20Content%20Sharing%20Agreement_SCHUNK%20SE%20%26%20Co%20KG.pdf)

egu\_50

**USD Path:** Schunk/egu\_50/schunk\_egu\_50.usd

**Multiphysics USD Path:** Schunk/egu\_50/schunk\_egu\_50/schunk\_egu\_50.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 2 |
| Number of Links | 3 |
| Number of DOFs | 2 |

**Physics APIs:**

* PhysX ArticulationAPI
* PhysX JointAPI

**License:** [`3D Content Sharing Agreement`](../_downloads/6d42d30807cdc55fd6d3b7efc4d7f7ba/3D%20Content%20Sharing%20Agreement_SCHUNK%20SE%20%26%20Co%20KG.pdf)

ezu\_35

**USD Path:** Schunk/ezu\_35/schunk\_ezu\_35.usd

**Multiphysics USD Path:** Schunk/ezu\_35/schunk\_ezu\_35/schunk\_ezu\_35.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 2 |
| Number of Links | 3 |
| Number of DOFs | 2 |

**Physics APIs:**

* PhysX ArticulationAPI
* PhysX JointAPI

**License:** [`3D Content Sharing Agreement`](../_downloads/6d42d30807cdc55fd6d3b7efc4d7f7ba/3D%20Content%20Sharing%20Agreement_SCHUNK%20SE%20%26%20Co%20KG.pdf)

svh-flat-l

**USD Path:** Schunk/svh-flat-l/svh-flat-l\_v2.usd

**Multiphysics USD Path:** Schunk/svh-flat-l/svh-flat-l\_v2/svh-flat-l\_v2.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 24 |
| Number of Links | 25 |
| Number of DOFs | 24 |

**Physics APIs:**

* PhysX ArticulationAPI
* PhysX JointAPI

**License:** [`3D Content Sharing Agreement`](../_downloads/6d42d30807cdc55fd6d3b7efc4d7f7ba/3D%20Content%20Sharing%20Agreement_SCHUNK%20SE%20%26%20Co%20KG.pdf)

svh-flat-r

**USD Path:** Schunk/svh-flat-r/svh-flat-r\_v2.usd

**Multiphysics USD Path:** Schunk/svh-flat-r/svh-flat-r\_v2/svh-flat-r\_v2.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 24 |
| Number of Links | 25 |
| Number of DOFs | 24 |

**Physics APIs:**

* PhysX ArticulationAPI
* PhysX JointAPI

**License:** [`3D Content Sharing Agreement`](../_downloads/6d42d30807cdc55fd6d3b7efc4d7f7ba/3D%20Content%20Sharing%20Agreement_SCHUNK%20SE%20%26%20Co%20KG.pdf)

**RobotStudio**

so101\_new\_calib

**USD Path:** RobotStudio/so101\_new\_calib/so101\_new\_calib.usd

**Multiphysics USD Path:** RobotStudio/so101\_new\_calib/so101\_new\_calib.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 6 |
| Number of Links | 7 |
| Number of DOFs | 6 |

**Physics APIs:**

* PhysX JointAPI
* PhysX ArticulationAPI

**License:** [Apache 2.0](https://github.com/TheRobotStudio/SO-ARM100/tree/main/Simulation/SO101)

so100

**USD Path:** RobotStudio/so100/so100.usd

**Multiphysics USD Path:** RobotStudio/so100/so100.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 6 |
| Number of Links | 7 |
| Number of DOFs | 6 |

**Physics APIs:**

* PhysX JointAPI
* PhysX ArticulationAPI

**License:** [Apache 2.0](https://github.com/TheRobotStudio/SO-ARM100/tree/main/Simulation/SO101)

**RethinkRobotics**

Sawyer

**USD Path:** RethinkRobotics/Sawyer/sawyer\_instanceable.usd

**Multiphysics USD Path:** RethinkRobotics/Sawyer/sawyer\_instanceable/sawyer\_instanceable.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 12 |
| Number of Links | 13 |
| Number of DOFs | 8 |

**Physics APIs:**

* PhysX RigidBodyAPI
* PhysX ArticulationAPI
* PhysX JointAPI

* This robot is in Isaac Lab

**License:** [Apache 2.0](http://github.com/RethinkRobotics/sawyer_robot)

**Kuka**

KR210\_L150

**USD Path:** Kuka/KR210\_L150/kr210\_l150.usd

**Multiphysics USD Path:** Kuka/KR210\_L150/kr210\_l150.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 8 |
| Number of Links | 9 |
| Number of DOFs | 6 |

**Physics APIs:**

* PhysX SceneAPI
* PhysX ArticulationAPI
* PhysX JointAPI

**License:** [Apache 2.0](https://github.com/ros-industrial/kuka_experimental)

**Kinova**

Jaco2

Variant 1

**USD Path:** Kinova/Jaco2/J2N7S300/j2n7s300\_instanceable.usd

Properties

|  |  |
| --- | --- |
| Number of Joints | 14 |
| Number of Links | 15 |
| Number of DOFs | 13 |

**Physics APIs:**

* PhysX RigidBodyAPI
* PhysX ArticulationAPI
* PhysX JointAPI

Variant 2

**USD Path:** Kinova/Jaco2/J2N6S300/j2n6s300\_instanceable.usd

Properties

|  |  |
| --- | --- |
| Number of Joints | 13 |
| Number of Links | 14 |
| Number of DOFs | 12 |

**Physics APIs:**

* PhysX RigidBodyAPI
* PhysX ArticulationAPI
* PhysX JointAPI

Gen3

**USD Path:** Kinova/Gen3/gen3n7\_instanceable.usd

**Multiphysics USD Path:** Kinova/Gen3/gen3n7\_instanceable/gen3n7\_instanceable.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 8 |
| Number of Links | 9 |
| Number of DOFs | 7 |

**Physics APIs:**

* PhysX RigidBodyAPI
* PhysX ArticulationAPI
* PhysX JointAPI

**Kawasaki**

RS080N

**USD Path:** Kawasaki/RS080N/rs080n\_onrobot\_rg2.usd

**Multiphysics USD Path:** Kawasaki/RS080N/rs080n\_onrobot\_rg2/rs080n\_onrobot\_rg2.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 15 |
| Number of Links | 16 |
| Number of DOFs | 12 |

**Physics APIs:**

* PhysX RigidBodyAPI
* PhysX ArticulationAPI
* PhysX SceneAPI
* PhysX JointAPI

**License:** [`3D Content Sharing Agreement`](../_downloads/c36994da30bb92b42836e211a360657b/3D%20Content%20Sharing-Kawasaki.pdf)

RS025N

**USD Path:** Kawasaki/RS025N/rs025n\_onrobot\_rg2.usd

**Multiphysics USD Path:** Kawasaki/RS025N/rs025n\_onrobot\_rg2/rs025n\_onrobot\_rg2.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 15 |
| Number of Links | 16 |
| Number of DOFs | 12 |

**Physics APIs:**

* PhysX RigidBodyAPI
* PhysX ArticulationAPI
* PhysX SceneAPI
* PhysX JointAPI

**License:** [`3D Content Sharing Agreement`](../_downloads/c36994da30bb92b42836e211a360657b/3D%20Content%20Sharing-Kawasaki.pdf)

RS013N

**USD Path:** Kawasaki/RS013N/rs013n\_onrobot\_rg2.usd

**Multiphysics USD Path:** Kawasaki/RS013N/rs013n\_onrobot\_rg2/rs013n\_onrobot\_rg2.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 15 |
| Number of Links | 16 |
| Number of DOFs | 12 |

**Physics APIs:**

* PhysX RigidBodyAPI
* PhysX ArticulationAPI
* PhysX SceneAPI
* PhysX JointAPI

**License:** [`3D Content Sharing Agreement`](../_downloads/c36994da30bb92b42836e211a360657b/3D%20Content%20Sharing-Kawasaki.pdf)

RS007N

**USD Path:** Kawasaki/RS007N/rs007n\_onrobot\_rg2.usd

**Multiphysics USD Path:** Kawasaki/RS007N/rs007n\_onrobot\_rg2/rs007n\_onrobot\_rg2.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 15 |
| Number of Links | 16 |
| Number of DOFs | 12 |

**Physics APIs:**

* PhysX RigidBodyAPI
* PhysX ArticulationAPI
* PhysX SceneAPI
* PhysX JointAPI

**License:** [`3D Content Sharing Agreement`](../_downloads/c36994da30bb92b42836e211a360657b/3D%20Content%20Sharing-Kawasaki.pdf)

RS007L

**USD Path:** Kawasaki/RS007L/rs007l\_onrobot\_rg2.usd

**Multiphysics USD Path:** Kawasaki/RS007L/rs007l\_onrobot\_rg2/rs007l\_onrobot\_rg2.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 15 |
| Number of Links | 16 |
| Number of DOFs | 12 |

**Physics APIs:**

* PhysX RigidBodyAPI
* PhysX ArticulationAPI
* PhysX SceneAPI
* PhysX JointAPI

**License:** [`3D Content Sharing Agreement`](../_downloads/c36994da30bb92b42836e211a360657b/3D%20Content%20Sharing-Kawasaki.pdf)

**FrankaRobotics**

FrankaPanda

**USD Path:** FrankaRobotics/FrankaPanda/franka.usd

**Multiphysics USD Path:** FrankaRobotics/FrankaPanda/franka/franka.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 10 |
| Number of Links | 11 |
| Number of DOFs | 9 |

**Accessories:**

* AlternateFinger
* Default
* Robotiq\_2F\_85

**Physics APIs:**

* PhysX MimicJointAPI
* PhysX ArticulationAPI
* PhysX JointAPI
* PhysX RigidBodyAPI

**License:** [Apache 2.0](https://github.com/frankaemika/franka_ros/tree/kinetic-devel/franka_description)

FrankaFR3

**USD Path:** FrankaRobotics/FrankaFR3/fr3.usd

**Multiphysics USD Path:** FrankaRobotics/FrankaFR3/fr3/fr3.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 12 |
| Number of Links | 13 |
| Number of DOFs | 9 |

**Physics APIs:**

* PhysX MimicJointAPI
* PhysX ArticulationAPI
* PhysX SceneAPI
* PhysX JointAPI

**License:** [Apache 2.0](https://github.com/frankaemika/franka_ros/tree/kinetic-devel/franka_description)

FrankaEmika

**USD Path:** FrankaRobotics/FrankaEmika/panda\_instanceable.usd

**Multiphysics USD Path:** FrankaRobotics/FrankaEmika/panda\_instanceable/panda\_instanceable.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 10 |
| Number of Links | 11 |
| Number of DOFs | 9 |

**Physics APIs:**

* PhysX ArticulationAPI
* PhysX JointAPI

**License:** [Apache 2.0](https://github.com/frankaemika/franka_ros/tree/kinetic-devel/franka_description)

FactoryFranka

Variant 1

**USD Path:** FrankaRobotics/FactoryFranka/factory\_franka.usd

**Multiphysics USD Path:** FrankaRobotics/FactoryFranka/factory\_franka/factory\_franka.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 11 |
| Number of Links | 12 |
| Number of DOFs | 9 |

**Physics APIs:**

* PhysX RigidBodyAPI
* PhysX ArticulationAPI
* PhysX JointAPI
* PhysX CollisionAPI

**License:** [Apache 2.0](https://github.com/frankaemika/franka_ros/tree/kinetic-devel/franka_description)

Variant 2

**USD Path:** FrankaRobotics/FactoryFranka/factory\_franka\_instanceable.usd

Properties

|  |  |
| --- | --- |
| Number of Joints | 11 |
| Number of Links | 12 |
| Number of DOFs | 9 |

**Physics APIs:**

* PhysX RigidBodyAPI
* PhysX ArticulationAPI
* PhysX JointAPI

**License:** [Apache 2.0](https://github.com/frankaemika/franka_ros/tree/kinetic-devel/franka_description)

**Flexiv**

Rizon4

**USD Path:** Flexiv/Rizon4/flexiv\_rizon4.usd

**Multiphysics USD Path:** Flexiv/Rizon4/flexiv\_rizon4/flexiv\_rizon4.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 8 |
| Number of Links | 9 |
| Number of DOFs | 7 |

**Physics APIs:**

* PhysX RigidBodyAPI
* PhysX ArticulationAPI
* PhysX SceneAPI
* PhysX JointAPI

**License:** [`3D Content Sharing Agreement`](../_downloads/759d641f79d23ef09d53c9a506d895b1/3D%20Content%20Sharing-%20FlexIV.pdf)

**Fanuc**

CRX10IAL

**USD Path:** Fanuc/crx10ial\_l/crx10ial\_l.usd

**Multiphysics USD Path:** Fanuc/crx10ia\_l/crx10ia\_l.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 9 |
| Number of Links | 10 |
| Number of DOFs | 6 |

**Physics APIs:**

* PhysX SceneAPI
* PhysX ArticulationAPI
* PhysX JointAPI

**License:** [`3D Content Sharing Agreement`](../_downloads/8ea27bd6ad258f4242d675e67e8f7b58/3D%20Content%20Sharing%20Agreement_FANUC.pdf)

cr\_50f\_16b

**USD Path:** Fanuc/cr\_50f\_16b/cr\_50f\_16b.usd

**Multiphysics USD Path:** Fanuc/cr\_50f\_16b/cr\_50f\_16b.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 7 |
| Number of Links | 8 |
| Number of DOFs | 6 |

**Physics APIs:**

* PhysX SceneAPI
* PhysX ArticulationAPI
* PhysX JointAPI

**License:** [`3D Content Sharing Agreement`](../_downloads/8ea27bd6ad258f4242d675e67e8f7b58/3D%20Content%20Sharing%20Agreement_FANUC.pdf)

crx10ia

**USD Path:** Fanuc/crx10ia/crx10ia.usd

**Multiphysics USD Path:** Fanuc/crx10ia/crx10ia.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 7 |
| Number of Links | 8 |
| Number of DOFs | 6 |

**Physics APIs:**

* PhysX SceneAPI
* PhysX ArticulationAPI
* PhysX JointAPI

**License:** [`3D Content Sharing Agreement`](../_downloads/8ea27bd6ad258f4242d675e67e8f7b58/3D%20Content%20Sharing%20Agreement_FANUC.pdf)

crx5ia

**USD Path:** Fanuc/crx5ia/crx5ia.usd

**Multiphysics USD Path:** Fanuc/crx5ia/crx5ia.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 7 |
| Number of Links | 8 |
| Number of DOFs | 6 |

**Physics APIs:**

* PhysX SceneAPI
* PhysX ArticulationAPI
* PhysX JointAPI

**License:** [`3D Content Sharing Agreement`](../_downloads/8ea27bd6ad258f4242d675e67e8f7b58/3D%20Content%20Sharing%20Agreement_FANUC.pdf)

lrmate200id

**USD Path:** Fanuc/lrmate200id/lrmate200id.usd

**Multiphysics USD Path:** Fanuc/lrmate200id/lrmate200id.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 7 |
| Number of Links | 8 |
| Number of DOFs | 6 |

**Physics APIs:**

* PhysX SceneAPI
* PhysX ArticulationAPI
* PhysX JointAPI

**License:** [`3D Content Sharing Agreement`](../_downloads/8ea27bd6ad258f4242d675e67e8f7b58/3D%20Content%20Sharing%20Agreement_FANUC.pdf)

m710ic\_50

**USD Path:** Fanuc/m710ic\_50/m710ic\_50.usd

**Multiphysics USD Path:** Fanuc/m710ic\_50/m710ic\_50.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 7 |
| Number of Links | 8 |
| Number of DOFs | 6 |

**Physics APIs:**

* PhysX SceneAPI
* PhysX ArticulationAPI
* PhysX JointAPI

**License:** [`3D Content Sharing Agreement`](../_downloads/8ea27bd6ad258f4242d675e67e8f7b58/3D%20Content%20Sharing%20Agreement_FANUC.pdf)

r2000ic\_165f

**USD Path:** Fanuc/r2000ic\_165f/r2000ic\_165f.usd

**Multiphysics USD Path:** Fanuc/r2000ic\_165f/r2000ic\_165f.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 7 |
| Number of Links | 8 |
| Number of DOFs | 6 |

**Physics APIs:**

* PhysX SceneAPI
* PhysX ArticulationAPI
* PhysX JointAPI

**License:** [`3D Content Sharing Agreement`](../_downloads/8ea27bd6ad258f4242d675e67e8f7b58/3D%20Content%20Sharing%20Agreement_FANUC.pdf)

sr12ia

**USD Path:** Fanuc/sr12ia/sr12ia.usd

**Multiphysics USD Path:** Fanuc/sr12ia/sr12ia.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 7 |
| Number of Links | 8 |
| Number of DOFs | 6 |

**Physics APIs:**

* PhysX SceneAPI
* PhysX ArticulationAPI
* PhysX JointAPI

**License:** [`3D Content Sharing Agreement`](../_downloads/8ea27bd6ad258f4242d675e67e8f7b58/3D%20Content%20Sharing%20Agreement_FANUC.pdf)

sr3ia

**USD Path:** Fanuc/sr3ia/sr3ia.usd

**Multiphysics USD Path:** Fanuc/sr3ia/sr3ia.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 7 |
| Number of Links | 8 |
| Number of DOFs | 6 |

**Physics APIs:**

* PhysX SceneAPI
* PhysX ArticulationAPI
* PhysX JointAPI

**License:** [`3D Content Sharing Agreement`](../_downloads/8ea27bd6ad258f4242d675e67e8f7b58/3D%20Content%20Sharing%20Agreement_FANUC.pdf)

m900ib280

**USD Path:** Fanuc/m900ib280/m900ib280.usd

**Multiphysics USD Path:** Fanuc/m900ib280/m900ib280.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 7 |
| Number of Links | 8 |
| Number of DOFs | 6 |

**Physics APIs:**

* PhysX SceneAPI
* PhysX ArticulationAPI
* PhysX JointAPI

**License:** [`3D Content Sharing Agreement`](../_downloads/8ea27bd6ad258f4242d675e67e8f7b58/3D%20Content%20Sharing%20Agreement_FANUC.pdf)

More

Note

Additional FANUC robot assets (84+ models) can be found in the Content Browser at `IsaacSim/Robots/Fanuc`. Multiphysics-ready counterparts for most of these models are also available at `IsaacSim/Robot_Multiphysics/Fanuc` (see [Multiphysics Robots](#isaac-assets-robots-multiphysics)).

**Denso**

CobottaPro900

**USD Path:** Denso/CobottaPro900/cobotta\_pro\_900.usd

**Multiphysics USD Path:** Denso/CobottaPro900/cobotta\_pro\_900/cobotta\_pro\_900.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 14 |
| Number of Links | 15 |
| Number of DOFs | 12 |

**Physics APIs:**

* PhysX MimicJointAPI
* PhysX ArticulationAPI
* PhysX SceneAPI
* PhysX JointAPI

**License:** [`3D Content Sharing Agreement`](../_downloads/3dafe8c35a9e7c525af8a0d2dce87ced/3D%20Content%20Sharing-%20Denso.pdf)

CobottaPro1300

**USD Path:** Denso/CobottaPro1300/cobotta\_pro\_1300.usd

**Multiphysics USD Path:** Denso/CobottaPro1300/cobotta\_pro\_1300/cobotta\_pro\_1300.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 14 |
| Number of Links | 15 |
| Number of DOFs | 12 |

**Physics APIs:**

* PhysX MimicJointAPI
* PhysX ArticulationAPI
* PhysX SceneAPI
* PhysX JointAPI

**License:** [`3D Content Sharing Agreement`](../_downloads/3dafe8c35a9e7c525af8a0d2dce87ced/3D%20Content%20Sharing-%20Denso.pdf)

**Comau**

n-220-27

**USD Path:** comau/n-220-27/n-220-27.usd

**Multiphysics USD Path:** comau/n-220-27/n-220-27.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 7 |
| Number of Links | 8 |
| Number of DOFs | 6 |

**Physics APIs:**

* PhysX SceneAPI
* PhysX ArticulationAPI
* PhysX JointAPI

**Addverb**

Syncro5

**USD Path:** Addverb/Syncro5.usd

**Multiphysics USD Path:** Addverb/Syncro5/Syncro5.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 6 |
| Number of Links | 7 |
| Number of DOFs | 6 |

**License:** [`3D Content Sharing Agreement`](../_downloads/a2c521c8682eada4da7b08811b2b3985/3D%20Content%20Sharing%20Agreement%20Template_Addverb%20Technologies%20Limited.pdf)

Syncro10

**USD Path:** Addverb/Syncro10.usd

**Multiphysics USD Path:** Addverb/Syncro10/Syncro10.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 6 |
| Number of Links | 7 |
| Number of DOFs | 6 |

**License:** [`3D Content Sharing Agreement`](../_downloads/a2c521c8682eada4da7b08811b2b3985/3D%20Content%20Sharing%20Agreement%20Template_Addverb%20Technologies%20Limited.pdf)

**Mecademic**

meca500

**USD Path:** Mecademic/meca500.usd

**Multiphysics USD Path:** Mecademic/meca500/meca500.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 6 |
| Number of Links | 7 |
| Number of DOFs | 6 |

**License:** [Apache 2.0](https://github.com/maximeriera/mecademic-ros)

**OpenArm**

openarm\_unimanual

**USD Path:** OpenArm/openarm\_unimanual/openarm\_unimanual.usd

**Multiphysics USD Path:** OpenArm/openarm\_unimanual/openarm\_unimanual.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 11 |
| Number of Links | 12 |
| Number of DOFs | 11 |

**Physics APIs:**

* PhysX JointAPI
* PhysX ArticulationAPI
* PhysX MimicJointAPI

**License:** [Apache 2.0](https://github.com/enactic/openarm)

openarm\_bimanual

**USD Path:** OpenArm/openarm\_bimanual/openarm\_bimanual.usd

**Multiphysics USD Path:** OpenArm/openarm\_bimanual/openarm\_bimanual.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 22 |
| Number of Links | 23 |
| Number of DOFs | 22 |

**Physics APIs:**

* PhysX JointAPI
* PhysX ArticulationAPI
* PhysX MimicJointAPI

**License:** [Apache 2.0](https://github.com/enactic/openarm)

Humanoid

**XiaoPeng**

PX5

Variant 1

**USD Path:** XiaoPeng/PX5/px5.usd

**Multiphysics USD Path:** XiaoPeng/PX5/px5.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 16 |
| Number of Links | 17 |
| Number of DOFs | 16 |

**Physics APIs:**

* PhysX JointAPI
* PhysX ArticulationAPI

**License:** [`3D Content Sharing Agreement`](../_downloads/3a03a43d65e71ab41914b819d8254eb2/XPENG%20Robotics-Signed%203D%20Content%20Sharing.pdf)

Variant 2

**USD Path:** XiaoPeng/PX5/px5\_without\_housing.usd

Properties

|  |  |
| --- | --- |
| Number of Joints | 16 |
| Number of Links | 17 |
| Number of DOFs | 16 |

**Physics APIs:**

* PhysX ArticulationAPI
* PhysX JointAPI

**License:** [`3D Content Sharing Agreement`](../_downloads/3a03a43d65e71ab41914b819d8254eb2/XPENG%20Robotics-Signed%203D%20Content%20Sharing.pdf)

**X-Humanoid**

Tien Kung

**USD Path:** XHumanoid/Tien Kung/tienkung.usd

**Multiphysics USD Path:** XHumanoid/Tien Kung/tienkung/tienkung.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 59 |
| Number of Links | 60 |
| Number of DOFs | 54 |

**Physics APIs:**

* PhysX ArticulationAPI
* PhysX JointAPI
* PhysX CollisionAPI

**License:** [`3D Content Sharing Agreement`](../_downloads/183543172a0505623f52e51688858ec3/3D%20Content%20Sharing-HRIC.pdf)

**Unitree**

H1

**USD Path:** Unitree/H1/h1.usd

**Multiphysics USD Path:** Unitree/H1/h1.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 24 |
| Number of Links | 25 |
| Number of DOFs | 19 |

**Physics APIs:**

* PhysX ArticulationAPI
* PhysX JointAPI

**License:** [BSD-3](https://github.com/unitreerobotics/unitree_ros)

G1\_23dof

Variant 1

**USD Path:** Unitree/G1\_23dof/g1.usd

**Multiphysics USD Path:** Unitree/G1\_23dof/g1/g1.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | N/A |
| Number of Links | N/A |
| Number of DOFs | N/A |

**Physics APIs:**

* PhysX SceneAPI
* PhysX CollisionAPI
* PhysX JointAPI
* PhysX ArticulationAPI

**License:** [BSD-3](https://github.com/unitreerobotics/unitree_ros)

Variant 2

**USD Path:** Unitree/G1\_23dof/g1\_minimal.usd

Properties

|  |  |
| --- | --- |
| Number of Joints | N/A |
| Number of Links | N/A |
| Number of DOFs | N/A |

**Physics APIs:**

* PhysX SceneAPI
* PhysX CollisionAPI
* PhysX JointAPI
* PhysX ArticulationAPI

**License:** [BSD-3](https://github.com/unitreerobotics/unitree_ros)

G1

**USD Path:** Unitree/G1/g1.usd

**Multiphysics USD Path:** Unitree/G1/g1.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 45 |
| Number of Links | 46 |
| Number of DOFs | 43 |

**Physics APIs:**

* PhysX RigidBodyAPI
* PhysX JointAPI
* PhysX ArticulationAPI

**License:** [BSD-3](https://github.com/unitreerobotics/unitree_ros)

**SanctuaryAI**

Phoenix

**USD Path:** SanctuaryAI/Phoenix/phoenix.usd

**Multiphysics USD Path:** SanctuaryAI/Phoenix/phoenix.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 77 |
| Number of Links | 78 |
| Number of DOFs | 77 |

**Physics APIs:**

* PhysX SceneAPI
* PhysX ArticulationAPI
* PhysX JointAPI

**License:** [`3D Content Sharing Agreement`](../_downloads/d21cf14a419597648d5d9121d9e0e3c8/Sanctuary-Signed%203D%20Content%20Sharing.pdf)

**RobotEra**

STAR1

**USD Path:** RobotEra/STAR1/star1.usd

**Multiphysics USD Path:** RobotEra/STAR1/star1.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 55 |
| Number of Links | 56 |
| Number of DOFs | 55 |

**Physics APIs:**

* PhysX JointAPI
* PhysX ArticulationAPI

**License:** [`3D Content Sharing Agreement`](../_downloads/2d7ca91a64ebcdb7366797df8b7e2ae0/3D%20Content%20Sharing-RobotEra20250117.pdf)

**Ihmcrobotics**

Valkyrie

**USD Path:** Ihmcrobotics/Valkyrie/valkyrie.usd

**Multiphysics USD Path:** Ihmcrobotics/Valkyrie/valkyrie.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 25 |
| Number of Links | 26 |
| Number of DOFs | 25 |

**Physics APIs:**

* PhysX JointAPI
* PhysX ArticulationAPI

**License:** [Apache 2.0](https://github.com/ihmcrobotics/valkyrie)

**FourierIntelligence**

GR-1

Variant 1

**USD Path:** FourierIntelligence/GR-1/GR1T2\_fourier\_hand\_6dof/GR1T2\_fourier\_hand\_6dof.usd

Properties

|  |  |
| --- | --- |
| Number of Joints | 54 |
| Number of Links | 55 |
| Number of DOFs | 54 |

**Physics APIs:**

* PhysX MimicJointAPI
* PhysX JointAPI
* PhysX SceneAPI
* PhysX ArticulationAPI

* This robot is in Isaac Lab

**License:** [`3D Content Sharing Agreement`](../_downloads/103b6bc140d62bd7103d51aef3f39215/Fourier%20Intelligence-Signed%203D%20Content%20Sharing.pdf)

Variant 2

**USD Path:** FourierIntelligence/GR-1/GR1T1/GR1\_T1.usd

Properties

|  |  |
| --- | --- |
| Number of Joints | 40 |
| Number of Links | 41 |
| Number of DOFs | 32 |

**Physics APIs:**

* PhysX SceneAPI
* PhysX ArticulationAPI
* PhysX JointAPI

**License:** [`3D Content Sharing Agreement`](../_downloads/103b6bc140d62bd7103d51aef3f39215/Fourier%20Intelligence-Signed%203D%20Content%20Sharing.pdf)

**Agility**

Digit

**USD Path:** Agility/Digit/digit\_v4.usd

**Multiphysics USD Path:** Agility/Digit/digit\_v4/digit\_v4.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 42 |
| Number of Links | 43 |
| Number of DOFs | 38 |

| Sensors | Count |
| --- | --- |
| Camera | 4 |

**Physics APIs:**

* PhysX RigidBodyAPI
* PhysX JointAPI
* PhysX CollisionAPI
* PhysX ArticulationAPI

* This robot is in Isaac Lab

**License:** [`3D Content Sharing Agreement`](../_downloads/b1c96321b1000eaf53fb43d1168f0e65/Agility%20-%20Signed%203D%20Content%20Sharing.pdf)

Cassie

**USD Path:** Agility/Cassie/cassie.usd

**Multiphysics USD Path:** Agility/Cassie/cassie.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 14 |
| Number of Links | 15 |
| Number of DOFs | 14 |

**Physics APIs:**

* PhysX ArticulationAPI
* PhysX JointAPI
* PhysX CollisionAPI

**License:** [`3D Content Sharing Agreement`](../_downloads/b1c96321b1000eaf53fb43d1168f0e65/Agility%20-%20Signed%203D%20Content%20Sharing.pdf)

**Agibot**

A2D

**USD Path:** Agibot/A2D/A2D.usd

**Multiphysics USD Path:** Agibot/A2D/A2D.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 34 |
| Number of Links | 35 |
| Number of DOFs | 34 |

**Physics APIs:**

* PhysX MimicJointAPI
* PhysX JointAPI
* PhysX ArticulationAPI

**License:** [`3D Content Sharing Agreement`](../_downloads/d27e33c5c00d3723e1c3457a04e05bc0/Agitbot%20G1%20Model%20Sharing%20Agreement.pdf)

**1X**

Neo

**USD Path:** 1X/Neo/Neo.usd

**Multiphysics USD Path:** 1X/Neo/Neo.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 33 |
| Number of Links | 34 |
| Number of DOFs | 33 |

**Physics APIs:**

* PhysX MimicJointAPI
* PhysX JointAPI
* PhysX ArticulationAPI

**License:** [`3D Content Sharing Agreement`](../_downloads/f26008f2c482c6b060d1a2ab59312a61/1X-signed%203D%20Content%20Sharing.pdf)

**BoosterRobotics**

BoosterT1

**USD Path:** BoosterRobotics/BoosterT1/T1\_locomotion.usd

**Multiphysics USD Path:** BoosterRobotics/BoosterT1/T1\_locomotion/T1\_locomotion.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 23 |
| Number of Links | 24 |
| Number of DOFs | 23 |

**Physics APIs:**

* PhysX JointAPI
* PhysX ArticulationAPI

**License:** [Apache 2.0](https://github.com/BoosterRobotics/booster_gym)

Quadruped

**Unitree**

laikago

**USD Path:** Unitree/laikago/laikago.usd

**Multiphysics USD Path:** Unitree/laikago/laikago.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 12 |
| Number of Links | 13 |
| Number of DOFs | 12 |

**Physics APIs:**

* PhysX JointAPI
* PhysX ArticulationAPI

**License:** [BSD-3](https://github.com/unitreerobotics/unitree_ros)

aliengo

**USD Path:** Unitree/aliengo/aliengo.usd

**Multiphysics USD Path:** Unitree/aliengo/aliengo.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 12 |
| Number of Links | 13 |
| Number of DOFs | 12 |

**Physics APIs:**

* PhysX JointAPI
* PhysX ArticulationAPI

**License:** [BSD-3](https://github.com/unitreerobotics/unitree_ros)

Go2

**USD Path:** Unitree/Go2/go2.usd

**Multiphysics USD Path:** Unitree/Go2/go2.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 38 |
| Number of Links | 39 |
| Number of DOFs | 12 |

**Physics APIs:**

* PhysX SceneAPI
* PhysX ArticulationAPI
* PhysX JointAPI

**License:** [BSD-3](https://github.com/unitreerobotics/unitree_ros)

Go1

Variant 1

**USD Path:** Unitree/Go1/go1.usd

**Multiphysics USD Path:** Unitree/Go1/go1.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 16 |
| Number of Links | 17 |
| Number of DOFs | 12 |

**Physics APIs:**

* PhysX ArticulationAPI
* PhysX JointAPI

**License:** [BSD-3](https://github.com/unitreerobotics/unitree_ros)

Variant 2

**USD Path:** Unitree/Go1/go1\_sensor.usd

Properties

|  |  |
| --- | --- |
| Number of Joints | 16 |
| Number of Links | 17 |
| Number of DOFs | 12 |

| Sensor/Accessory | Count |
| --- | --- |
| Contact Sensor | 4 |

**Physics APIs:**

* PhysX ArticulationAPI
* PhysX JointAPI

**License:** [BSD-3](https://github.com/unitreerobotics/unitree_ros)

B2

**USD Path:** Unitree/B2/b2.usd

**Multiphysics USD Path:** Unitree/B2/b2.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 30 |
| Number of Links | 31 |
| Number of DOFs | 12 |

**Physics APIs:**

* PhysX SceneAPI
* PhysX ArticulationAPI
* PhysX JointAPI

**License:** [BSD-3](https://github.com/unitreerobotics/unitree_ros)

A1

**USD Path:** Unitree/A1/a1.usd

**Multiphysics USD Path:** Unitree/A1/a1.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 16 |
| Number of Links | 17 |
| Number of DOFs | 12 |

**Physics APIs:**

* PhysX ArticulationAPI
* PhysX JointAPI

**License:** [BSD-3](https://github.com/unitreerobotics/unitree_ros)

**IsaacSim**

Ant

Variant 1

**USD Path:** IsaacSim/Ant/ant.usd

**Multiphysics USD Path:** IsaacSim/Ant/ant.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 8 |
| Number of Links | 9 |
| Number of DOFs | 8 |

**Physics APIs:**

* PhysX SceneAPI
* PhysX ArticulationAPI
* PhysX JointAPI

**License:** [MIT](https://github.com/openai/gym/blob/master/LICENSE.md)

Variant 2

**USD Path:** IsaacSim/Ant/ant\_colored.usd

Properties

|  |  |
| --- | --- |
| Number of Joints | N/A |
| Number of Links | N/A |
| Number of DOFs | N/A |

**Physics APIs:**

* PhysX RigidBodyAPI
* PhysX CollisionAPI
* PhysX SceneAPI

**License:** [MIT](https://github.com/openai/gym/blob/master/LICENSE.md)

Variant 3

**USD Path:** IsaacSim/Ant/ant\_instanceable.usd

Properties

|  |  |
| --- | --- |
| Number of Joints | 8 |
| Number of Links | 9 |
| Number of DOFs | 8 |

**Physics APIs:**

* PhysX SceneAPI
* PhysX ArticulationAPI
* PhysX JointAPI

* This robot is in Isaac Lab

**License:** [MIT](https://github.com/openai/gym/blob/master/LICENSE.md)

**BostonDynamics**

spot

**USD Path:** BostonDynamics/spot/spot.usd

**Multiphysics USD Path:** BostonDynamics/spot/spot.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 16 |
| Number of Links | 17 |
| Number of DOFs | 12 |

**Physics APIs:**

* PhysX SceneAPI
* PhysX ArticulationAPI
* PhysX JointAPI

* This robot is in Isaac Lab

**License:** [`3D Content Sharing Agreement`](../_downloads/585f153c86ae5f36eac8c0ab3ad566b4/Boston%20Dynamics-Signed%203D%20Content%20Sharing.pdf)

**ANYbotics**

anymal\_d

**USD Path:** ANYbotics/anymal\_d/anymal\_d.usd

**Multiphysics USD Path:** ANYbotics/anymal\_d/anymal\_d.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 16 |
| Number of Links | 17 |
| Number of DOFs | 12 |

**Physics APIs:**

* PhysX RigidBodyAPI
* PhysX JointAPI
* PhysX ArticulationAPI

**License:** [BSD-3](https://github.com/ANYbotics/anymal_d_simple_description/blob/master/LICENSE)

anymal\_c

**USD Path:** ANYbotics/anymal\_c/anymal\_c.usd

**Multiphysics USD Path:** ANYbotics/anymal\_c/anymal\_c.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 17 |
| Number of Links | 18 |
| Number of DOFs | 12 |

**Physics APIs:**

* PhysX RigidBodyAPI
* PhysX ArticulationAPI
* PhysX JointAPI

**License:** [BSD-3](https://github.com/ANYbotics/anymal_c_simple_description/blob/master/LICENSE)

anymal\_b

**USD Path:** ANYbotics/anymal\_b/anymal\_b.usd

**Multiphysics USD Path:** ANYbotics/anymal\_b/anymal\_b.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 16 |
| Number of Links | 17 |
| Number of DOFs | 12 |

**Physics APIs:**

* PhysX RigidBodyAPI
* PhysX JointAPI
* PhysX ArticulationAPI

**License:** [BSD-3](https://github.com/ANYbotics/anymal_b_simple_description/blob/master/LICENSE)

**DeepRobotics**

X30

**USD Path:** DeepRobotics/X30/X30.usd

**Multiphysics USD Path:** DeepRobotics/X30/X30.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 16 |
| Number of Links | 17 |
| Number of DOFs | 12 |

**Physics APIs:**

* PhysX ArticulationAPI
* PhysX JointAPI

**License:** [BSD-3](https://github.com/DeepRoboticsLab/deep_robotics_model/blob/main/LICENSE.txt)

M20

**USD Path:** DeepRobotics/M20/M20.usd

**Multiphysics USD Path:** DeepRobotics/M20/M20.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 16 |
| Number of Links | 17 |
| Number of DOFs | 16 |

**Physics APIs:**

* PhysX ArticulationAPI
* PhysX JointAPI

**License:** [BSD-3](https://github.com/DeepRoboticsLab/deep_robotics_model/blob/main/LICENSE.txt)

Lite3

**USD Path:** DeepRobotics/Lite3/Lite3.usd

**Multiphysics USD Path:** DeepRobotics/Lite3/Lite3.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 16 |
| Number of Links | 17 |
| Number of DOFs | 12 |

**Physics APIs:**

* PhysX ArticulationAPI
* PhysX JointAPI

**License:** [BSD-3](https://github.com/DeepRoboticsLab/deep_robotics_model/blob/main/LICENSE.txt)

**Addverb**

Trakr

**USD Path:** Addverb/Trakr/trakr.usd

**Multiphysics USD Path:** Addverb/Trakr/trakr.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 16 |
| Number of Links | 17 |
| Number of DOFs | 12 |

**License:** [`3D Content Sharing Agreement`](../_downloads/a2c521c8682eada4da7b08811b2b3985/3D%20Content%20Sharing%20Agreement%20Template_Addverb%20Technologies%20Limited.pdf)

Holonomic

**NVIDIA**

Kaya

Variant 1

**USD Path:** NVIDIA/Kaya/kaya.usd

**Multiphysics USD Path:** NVIDIA/Kaya/kaya.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 33 |
| Number of Links | 34 |
| Number of DOFs | 33 |

**Physics APIs:**

* PhysX SceneAPI
* PhysX ArticulationAPI
* PhysX JointAPI
* PhysX CollisionAPI

**License:** NVIDIA

Variant 2

**USD Path:** NVIDIA/Kaya/kaya\_ogn\_gamepad.usd

Properties

|  |  |
| --- | --- |
| Number of Joints | N/A |
| Number of Links | N/A |
| Number of DOFs | N/A |

**Physics APIs:**

* PhysX SceneAPI
* PhysX CollisionAPI
* PhysX JointAPI
* PhysX ArticulationAPI

**License:** NVIDIA

**Fraunhofer**

O3dyn

Variant 1

**USD Path:** Fraunhofer/O3dyn/o3dyn.usd

**Multiphysics USD Path:** Fraunhofer/O3dyn/o3dyn.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 76 |
| Number of Links | 77 |
| Number of DOFs | 64 |

**Physics APIs:**

* PhysX RigidBodyAPI
* PhysX ArticulationAPI
* PhysX JointAPI
* PhysX CollisionAPI
* PhysX SceneAPI

**License:** [`3D Content Sharing Agreement`](../_downloads/28ec2cf24f402cb152a4463028986107/CLA-1_OpenLogisticsFoundation_Fraunhofer_-_NVIDIA.pdf)

Variant 2

**USD Path:** Fraunhofer/O3dyn/o3dyn\_controller.usd

Properties

|  |  |
| --- | --- |
| Number of Joints | N/A |
| Number of Links | N/A |
| Number of DOFs | N/A |

**Physics APIs:**

* PhysX RigidBodyAPI
* PhysX CollisionAPI
* PhysX JointAPI
* PhysX ArticulationAPI
* PhysX SceneAPI

**License:** [`3D Content Sharing Agreement`](../_downloads/28ec2cf24f402cb152a4463028986107/CLA-1_OpenLogisticsFoundation_Fraunhofer_-_NVIDIA.pdf)

Variant 3

**USD Path:** Fraunhofer/O3dyn/o3dyn\_trimmed.usd

Properties

|  |  |
| --- | --- |
| Number of Joints | 52 |
| Number of Links | 53 |
| Number of DOFs | 40 |

**Physics APIs:**

* PhysX RigidBodyAPI
* PhysX ArticulationAPI
* PhysX JointAPI
* PhysX CollisionAPI
* PhysX SceneAPI

**License:** [`3D Content Sharing Agreement`](../_downloads/28ec2cf24f402cb152a4463028986107/CLA-1_OpenLogisticsFoundation_Fraunhofer_-_NVIDIA.pdf)

Aerial

**NASA**

Ingenuity

**USD Path:** NASA/Ingenuity/ingenuity.usd

**Multiphysics USD Path:** NASA/Ingenuity/ingenuity.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 4 |
| Number of Links | 5 |
| Number of DOFs | 4 |

**Physics APIs:**

* PhysX SceneAPI
* PhysX ArticulationAPI
* PhysX CollisionAPI

**License:** [NASA/JPL-Caltech 3D Model Download](https://science.nasa.gov/resource/mars-ingenuity-helicopter-3d-model)

**IsaacSim**

Quadcopter

**USD Path:** IsaacSim/Quadcopter/quadcopter.usd

**Multiphysics USD Path:** IsaacSim/Quadcopter/quadcopter.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 8 |
| Number of Links | 9 |
| Number of DOFs | 8 |

**Physics APIs:**

* PhysX SceneAPI
* PhysX ArticulationAPI
* PhysX JointAPI

**Bitcraze**

Crazyflie

**USD Path:** Bitcraze/Crazyflie/cf2x.usd

**Multiphysics USD Path:** Bitcraze/Crazyflie/cf2x/cf2x.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 4 |
| Number of Links | 5 |
| Number of DOFs | 4 |

**Physics APIs:**

* PhysX ArticulationAPI

* This robot is in Isaac Lab

**License:** [MIT](https://github.com/bitcraze/crazyflie-simulation/blob/main/LICENSE)

**NTNU**

ARL-Robot-1

**USD Path:** NTNU/ARL-Robot-1/arl\_robot\_1.usd

**Multiphysics USD Path:** NTNU/ARL-Robot-1/arl\_robot\_1/arl\_robot\_1.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 4 |
| Number of Links | 5 |
| Number of DOFs | 4 |

**Physics APIs:**

* PhysX SceneAPI
* PhysX ArticulationAPI
* PhysX JointAPI

**License:** [BSD-3](https://github.com/ntnu-arl/robot_model)

Isaac Sim Simple

**IsaacSim**

Vehicle

**USD Path:** IsaacSim/Vehicle/basic\_vehicle\_m.usd

**Multiphysics USD Path:** IsaacSim/Vehicle/basic\_vehicle\_m/basic\_vehicle\_m.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | N/A |
| Number of Links | N/A |
| Number of DOFs | N/A |

**Physics APIs:**

* PhysX RigidBodyAPI
* PhysX CollisionAPI
* PhysX SceneAPI

**License:** NVIDIA

SimpleArticulation

Variant 1

**USD Path:** IsaacSim/SimpleArticulation/articulation\_3\_joints.usd

**Multiphysics USD Path:** IsaacSim/SimpleArticulation/articulation\_3\_joints/articulation\_3\_joints.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 3 |
| Number of Links | 4 |
| Number of DOFs | 3 |

**Physics APIs:**

* PhysX RigidBodyAPI
* PhysX ArticulationAPI
* PhysX SceneAPI
* PhysX CollisionAPI

Variant 2

**USD Path:** IsaacSim/SimpleArticulation/revolute\_articulation.usd

Properties

|  |  |
| --- | --- |
| Number of Joints | 1 |
| Number of Links | 2 |
| Number of DOFs | 1 |

**Physics APIs:**

* PhysX RigidBodyAPI
* PhysX ArticulationAPI
* PhysX SceneAPI
* PhysX CollisionAPI

Variant 3

**USD Path:** IsaacSim/SimpleArticulation/simple\_articulation.usd

Properties

|  |  |
| --- | --- |
| Number of Joints | 2 |
| Number of Links | 3 |
| Number of DOFs | 2 |

**Physics APIs:**

* PhysX RigidBodyAPI
* PhysX ArticulationAPI
* PhysX SceneAPI
* PhysX CollisionAPI

Humanoid28

**USD Path:** IsaacSim/Humanoid28/humanoid\_28.usd

**Multiphysics USD Path:** IsaacSim/Humanoid28/humanoid\_28/humanoid\_28.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 14 |
| Number of Links | 15 |
| Number of DOFs | 12 |

**Physics APIs:**

* PhysX RigidBodyAPI
* PhysX ArticulationAPI
* PhysX JointAPI

Humanoid

Variant 1

**USD Path:** IsaacSim/Humanoid/humanoid.usd

**Multiphysics USD Path:** IsaacSim/Humanoid/humanoid.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 15 |
| Number of Links | 16 |
| Number of DOFs | 12 |

**Physics APIs:**

* PhysX RigidBodyAPI
* PhysX ArticulationAPI
* PhysX JointAPI

**License:** [MIT](https://github.com/openai/gym/blob/master/LICENSE.md)

Variant 2

**USD Path:** IsaacSim/Humanoid/humanoid\_instanceable.usd

Properties

|  |  |
| --- | --- |
| Number of Joints | 15 |
| Number of Links | 16 |
| Number of DOFs | 12 |

**Physics APIs:**

* PhysX RigidBodyAPI
* PhysX ArticulationAPI
* PhysX JointAPI

* This robot is in Isaac Lab

**License:** [MIT](https://github.com/openai/gym/blob/master/LICENSE.md)

DifferentialBase

**USD Path:** IsaacSim/DifferentialBase/differential\_base.usd

**Multiphysics USD Path:** IsaacSim/DifferentialBase/differential\_base/differential\_base.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 2 |
| Number of Links | 3 |
| Number of DOFs | 2 |

**Physics APIs:**

* PhysX RigidBodyAPI
* PhysX ArticulationAPI
* PhysX SceneAPI
* PhysX JointAPI

Cartpole

**USD Path:** IsaacSim/Cartpole/cartpole.usd

**Multiphysics USD Path:** IsaacSim/Cartpole/cartpole.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 2 |
| Number of Links | 3 |
| Number of DOFs | 2 |

**Physics APIs:**

* PhysX ArticulationAPI
* PhysX JointAPI

CartDoublePendulum

**USD Path:** IsaacSim/CartDoublePendulum/cart\_double\_pendulum.usd

**Multiphysics USD Path:** IsaacSim/CartDoublePendulum/cart\_double\_pendulum/cart\_double\_pendulum.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 3 |
| Number of Links | 4 |
| Number of DOFs | 3 |

**Physics APIs:**

* PhysX JointAPI
* PhysX ArticulationAPI

BalanceBot

**USD Path:** IsaacSim/BalanceBot/balance\_bot.usd

**Multiphysics USD Path:** IsaacSim/BalanceBot/balance\_bot/balance\_bot.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 6 |
| Number of Links | 7 |
| Number of DOFs | 6 |

**Physics APIs:**

* PhysX RigidBodyAPI
* PhysX ArticulationAPI
* PhysX JointAPI

Mobile Manipulator

**Clearpath**

RidgebackUr

**USD Path:** Clearpath/RidgebackUr/ridgeback\_ur5.usd

**Multiphysics USD Path:** Clearpath/RidgebackUr/ridgeback\_ur5.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 9 |
| Number of Links | 10 |
| Number of DOFs | 9 |

**Physics APIs:**

* PhysX SceneAPI
* PhysX ArticulationAPI
* PhysX JointAPI

**License:** [BSD-3](https://github.com/orgs/clearpathrobotics/repositories?q=dingo)

RidgebackFranka

**USD Path:** Clearpath/RidgebackFranka/ridgeback\_franka.usd

**Multiphysics USD Path:** Clearpath/RidgebackFranka/ridgeback\_franka.usda

Properties

|  |  |
| --- | --- |
| Number of Joints | 18 |
| Number of Links | 19 |
| Number of DOFs | 12 |

**Physics APIs:**

* PhysX SceneAPI
* PhysX ArticulationAPI
* PhysX JointAPI

* This robot is in Isaac Lab

**License:** [BSD-3](https://github.com/orgs/clearpathrobotics/repositories?q=dingo)

**BostonDynamics**

spot

**USD Path:** BostonDynamics/spot/spot\_with\_arm.usd

Properties

|  |  |
| --- | --- |
| Number of Joints | 19 |
| Number of Links | 20 |
| Number of DOFs | 19 |

**Physics APIs:**

* PhysX SceneAPI
* PhysX ArticulationAPI
* PhysX JointAPI

**License:** [`3D Content Sharing Agreement`](../_downloads/585f153c86ae5f36eac8c0ab3ad566b4/Boston%20Dynamics-Signed%203D%20Content%20Sharing.pdf)

**Galbot**

galbot\_g1

**USD Path:** Galbot/galbot/g1.usd

Properties

|  |  |
| --- | --- |
| Number of Joints | 86 |
| Number of Links | 87 |
| Number of DOFs | 77 |

**Physics APIs:**

* PhysX ArticulationAPI

**License:** [`3D Content Sharing Agreement`](../_downloads/d2f590ee8d0bd801d70dfd7015bcee82/3D%20Content%20Sharing%20Agreement%20Template_SHENZHEN%20GALBOT%20CO.%2CLTD.pdf)

On this page

* [Multiphysics Robots](#multiphysics-robots)

---

### Sensors

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/assets/usd_assets_sensors.html

* [Isaac Sim Assets](usd_assets_overview.html)
* Sensor Assets

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Sensor Assets

Isaac Sim ships sensor assets so you can simulate hardware behavior with the same sensor
configurations you plan to deploy. Browse them by sensor category below.

* [Camera and Depth Sensors](usd_assets_camera_depth_sensors.html)
* [Non-Visual Sensors](usd_assets_nonvisual_sensors.html)

---

### Featured

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/assets/usd_assets_featured.html

* [Isaac Sim Assets](usd_assets_overview.html)
* Featured Assets

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Featured Assets

**Nova Carter**

Powered by the [Nova Orinâ¢](https://developer.nvidia.com/isaac/nova-orin) sensor and compute architecture, Nova Carter is a complete robotics development platform that accelerates the development and deployment of next-generation Autonomous Mobile Robots (AMRs).

Nova Carter is being used as a reference platform for both Isaac AMR and Isaac ROS software, enabling real-world and simulation-based development. Nova Carter robots may be purchased from [Segway Robotics](https://robotics.segway.com/nova-carter).

For more information on the fully-featured Nova Carter Isaac Sim Asset, please refer to the [Nova Carter](nova_carter_landing_page.html#isaac-nova-carter) documentation page.

Warning

Nova Carter robot may take multiple minutes to load for the first time.

---

### Third Party

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/assets/usd_assets_third_party.html

* [Isaac Sim Assets](usd_assets_overview.html)
* Third-Party USD Assets

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Third-Party USD Assets

Isaac Sim welcomes open source assets from the community. This page outlines links to third-party assets that are compatible with Isaac Sim.

Third-Party USD Assets

| Link | Description |
| --- | --- |
| [Lightwheel SimReady store](https://simready.com) | Catalog of open sourced and closed source environments and prop assets. |
| [X-Humanoid ArtVIP Dataset](https://huggingface.co/datasets/x-humanoid-robomind/ArtVIP) | A large-scale dataset of articulated 3D objects and scenes. |
| [Synthesis Asset pack](https://synthesis.extwin.com) | A collection of assets for synthetic data generation. |
| [SpatialVerse dataset](https://huggingface.co/spatialverse) | InteriorAgent, InteriorGS, InteriorAgent\_Nav datasets for synthetic data generation. |
| [XGrid Scan to Simulation Tutorial](https://developer.xgrids.com/#/document?titleId=en-1761533581983) | Tutorial for converting a 3D scan to a simulation environment in NVIDIA Isaac Sim. |
| [MolmoSpaces](https://github.com/allenai/molmospaces/tree/main/molmo_spaces_isaac) | A large-scale dataset with articulated 3D objects and diverse indoor scenes. |
| [Extwin](https://synthesis.extwin.com) | A collection of assets for synthetic data generation. |
| [imagine.io](https://physical.imagine.io/library/assets) | A collection of usd props. |

---


## 物理

### Simulation Fundamentals

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/physics/simulation_fundamentals.html

* [Physics](index.html)
* Physics Simulation Fundamentals

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Physics Simulation Fundamentals

## Physics in USD Schemas

The physics properties of assets are all well-defined using [USD Physics Schemas](https://openusd.org/release/api/usd_physics_page_front.html) and [Physx Schemas](https://docs.omniverse.nvidia.com/kit/docs/omni_usd_schema_physics/latest/annotated.html) . The documentation of Physics properties and how to access them in code is defined in C++, but you can follow [these guidelines](https://developer.nvidia.com/usd/apinotes) to find the equivalent calls in Python. For example, where generic names are used to represent an arbitrary API, the general usage is:

```python
import omni.usd
from pxr import PhysxSchema, Usd, UsdGeom, UsdPhysics

stage = omni.usd.get_context().get_stage()
prim = stage.GetPrimAtPath("/Path/To/Prim")
physics_api_prim = UsdPhysics.SomePhysicsAPI(prim)
physx_api_prim = PhysxSchema.AnotherPhysxAPI(prim)

# Check if the API is Applied, if not, Apply it.
if not physics_api_prim:
    physics_api_prim = UsdPhysics.SomePhysicsAPI.Apply(prim)

physics_attr = physics_api_prim.GetSomePhysicsAttr()
physx_attr = physx_api_prim.GetPhysxAttr()

# Check if Attribute is authored, otherwise create it
if not physics_attr:
    physics_attr = physics_api_prim.CreateSomePhysicsAttr(1.0)
print(physics_attr.Get())
physics_attr.Set(10.0)
```

In some cases, you may need to have additional parameters when casting the Prim to a given API, for example, [Joint State](https://docs.omniverse.nvidia.com/kit/docs/omni_usd_schema_physics/latest/class_physx_schema_joint_state_a_p_i.html#afff2009176797852a1389d7244caa875) does require the joint type (âPrismaticâ, or âAngularâ, for instance). In these cases the C++ signature will contain a âTfTokenâ type. Replace it with a basic string and it should work in Python.

If you need to know the attribute name of some physics attribute you see on the UI, Hover over the attribute in the properties panel, and it will show its name in the tooltip. The attribute name standard is `schema_name:attribute_name`, so for example something like `physics:velocity` on a rigid body means itâs using the Physics Rigid Body API and the attribute name is `velocity`, so the corresponding attribute getter would be `UsdPhysics.RigidBodyAPI(prim).GetVelocityAttr()`.

## Simulation Timeline

Simulation time **differs** from real-time. Depending on system configuration and the size of the simulated environment, each time step may be computed faster or slower than the time itâs simulating, resulting in a warped speed if results are presented sequentially (often, physics simulation in Isaac Sim is faster than real-time). To mitigate this, Isaac Sim is configured by default with a limiter to match real-time speed.

Moreover, the simulation may run at a faster pace than rendering, meaning there may be more than one simulation time-step occurring in the background for every rendered frame. In the simplified example below, the simulation is set to run at 120 time steps per second, while rendering is set to 60 frames per second, resulting in two physics steps per rendered frame:

Note

The physics step time doesnât necessarily coincide with system time (from the simulation start). In cases where the simulation can run faster than real-time, itâs possible to run an accelerated version of the simulation in a timeline without rendering or frame-rate blocking.

Ideally, simulation and rendering would match or be multiples of each other, but when this isnât the case, each rendered frame may contain an uneven number of simulation timesteps. For example, simulation set to 100 steps per second, rendering set to 30 frames per second, resulting in most render updates having 3 simulation steps but occasionally 4 in a frame.

There are three event streams on the timeline (among a few others, but these are notably the most relevant for Isaac Sim). You can subscribe directly to Simulation Events or to Frame update events, either pre or post-rendering. OmniGraph nodes are typically updated on a pre-render event, but there are ways to set them to update on different events, such as every physics step.

### Configuring Frame Rate

The stageâs **Timecodes per second** can be configured by adjusting the current stage metadata. In the **Layer** tab, select the **Root Layer**, and in the properties panel modify the **Timecodes per second** property. Under the GUI default `/app/player/useFixedTimeStepping=true`, the timeline uses `1 / TimeCodesPerSecond` as its per-tick `dt`, so this value sets the simulationâs wall-clock playback rate as well as the recorded animation rate. The physics step rate is configured separately on the Physics Scene (see **Configuring Simulation Timesteps** below); for the relationship between the three rates, see [Architecture: Timeline, Physics, and the Renderer](../sensors/isaacsim_sensors_multitick_rendering.html#isaac-sim-sensors-multitick-clock-relationships).

### Configuring Simulation Timesteps

Simulation steps per second are determined in the Physics Scene. If thereâs no Physics scene in your stage, it uses the default value, which is 60 steps per second.

To add a Simulation Scene element:

1. Click on **Create** > **Physics** > **Simulation Scene**.
2. Select the Simulation scene.
3. In the Properties panel check the element **Simulation Steps per Second**.

For more details on other parameters in the Physics Scene, refer to [Omniverse Physics Developer Guide](https://docs.omniverse.nvidia.com/kit/docs/omni_physics/latest/index.html "(in Omni Physics)").

## Simulation Components

Prims in a USD stage do not have physics enabled by default, but you may add simulation properties through the UI or using Python scripts. The following creates an example scene to which elements are added as we progress through the basic physics object types.

To begin, create a new scene and add a ground plane to it: **File** > **New**, then **Create** > **Physics** > **Ground Plane**.

### Rigid Body

This is the most basic element. Adding rigid body dynamics enables an element to be subject to gravitational acceleration and other external forces.

1, Add a container to use as our Rigid Body: **Create** > **Xform**.
2. Move it up to `Z=10` in the properties panel.
3. To make it a rigid body, right-click on it in the stage, then **Add** > **Physics** > **Rigid Body**.

Verify that the Xform is now be a rigid body, although you may not see much because it has no visual meshes.

You can fix that by nesting a Cube in it:

1. **Create** > **Mesh** > **Cube**, and drag it into the Xform.
2. Ensure the cubeâs Translate is set to [0,0,0.5].

After youâve completed the same setup as the screenshot above, hit play and see what happens:

try {
var kalturaPlayer = KalturaPlayer.setup({
targetId: "kaltura\_player\_288773707",
provider: {
partnerId: 2935771,
uiConfId: 53712482
}
});
kalturaPlayer.loadMedia({entryId: '1\_0g5gsmii'});
} catch (e) {
console.error(e.message)
}

Review the following:

* Notice how the Z position gets updated as the object falls - this is because we are highlighting the rigid body directly. Try again selecting the cube, and youâll notice that it doesnât change.
* The cube falls straight through the ground. We need to let the simulation know it needs to collide with other objects.

### Colliders

To make our rigid body collide, you must indicate to the simulation that you want it to. For that, thereâs the Collider API.

1. Select the Cube prim, and click on the **Add Button** > **Physics** > **Collider**.
2. Run the simulation again and verify that the rigid body stops at the ground.

Colliders can also be added to non-movable objects. Letâs experiment:

1. Create a new cube and place it at Z=3.0.
2. Then change its scale to [2,2,0.01] to create a 2x2 meter platform.
3. Add the collider to it just like before, without adding the Rigid body.

Play the simulation again, and verify that this is the result:

Raise the Xform position to `Z=80`.
Play the simulation again.

try {
var kalturaPlayer = KalturaPlayer.setup({
targetId: "kaltura\_player\_115311347",
provider: {
partnerId: 2935771,
uiConfId: 53712482
}
});
kalturaPlayer.loadMedia({entryId: '1\_xmcdhnwb'});
} catch (e) {
console.error(e.message)
}

With this example, you are solving some of the common issues of physics simulation. Because time is discretized, if objects move too fast, during one time-step the object is above the platform, and in the next it has completely passed through it, with no collision captured.
This doesnât occur with the ground plane because it implements a âforce fieldâ that pushes penetrated objects towards the ground surface.

To remedy this, enable an option in the physics scene called **Enable CCD** (Continuous Collision Detection). CCD sweeps the object from one pose to the next. This option must also be enabled in the rigid body itself:

1. Select the Xform.
2. In the properties panel, enable CCD under the rigid body properties.

There are other ways to solve this issue, but for this scenario, this is the most effective.

Remember that collision has nothing to do with what you see on screen. For instance, you could hide the cube and the collider would behave the same, or you could add another cube or a sphere under Xform and it would have no effect unless you apply the Collision API to it.

Many object colliders are made using a composition of multiple mesh elements, giving it its shape and behavior. They work as a single rigid body even if they are physically separated on the stage, as long as they are all children of a rigid body.

Try adding and removing colliders to this rigid body or adding more rigid bodies to this scene and see how they behave.

#### Convex Hull

This next experiment with colliders removes the platform you added before and returns our Xform to `Z=10`.

1. Add a Torus mesh in the place of the platform at `Z=3.0` and scale it to [5.0, 5.0, 5.0].
2. **Add** > **Physics** > **Rigid Body With Colliders Preset**.
3. Run the simulation.

The Cube sits on top of the torus hole because the default approximation for mesh geometry is a convex hull. This is an approximation that the simulation engine can process efficiently, i.e. they are a good choice for performant simulations. We will review more complex, and therefore more computationally expensive approximations below.

To see the collision shape in use:

1. Click on the eye icon on the top-left side of the Viewport.
2. **Show by type** > **Physics** > **Colliders** > **Selected**.
3. Verify that green lines appear on the Torus.

This is a debug view of the collision shape.

You can also view a solid display of the colliders by opening the Physics debug menu:
1. **Window** > **Simulation** > **Debug**.
2. In the debug window, scroll to âCollision Mesh Debug Visualizationâ.
3. Check âSolid Mesh Collision Visualizationâ.
4 Verify that when you select the torus, its shape displays solidly.

|  |  |
| --- | --- |
|  |  |

#### Convex Decomposition

At a small expense, the torus collider can have the hole by a composition of convex shapes. This composition can be:

* manually created by adding multiple shapes
* computed with Physics Convex Decomposition

1. Select the Torus.
2. In the properties panel, scroll down to the Collision section, and select **Convex Decomposition** from the drop-down.
3. By opening the Advanced tab, you can adjust the parameters until you find a decomposition to your satisfaction.

Note

Fewer convex hulls typically results in higher performance.

In the Simulation Debug tab, you can also increase the Explode View distance to split the collider shapes and better understand how the composition is made.

The Collider drop-down contains more options to explore, like Bounding Cube and Sphere - the cheapest collisions possible, and a mode âSphere Approximationâ, which is similar to Convex decomposition but directly uses a group of spheres instead of conforming meshes.

Note

While triangle mesh and mesh simplification are not supported by rigid bodies and fall back to convex hull, it is possible to use a triangle mesh geometry directly on a rigid body by adding a signed-distance field to it; select **SDF Mesh** in the approximation drop-down to do so.

For more details on Rigid Bodies and Colliders, check [Rigid Body Simulation](https://docs.omniverse.nvidia.com/kit/docs/omni_physics/latest/dev_guide/rigid_bodies_articulations/rigid_bodies.html "(in Omni Physics)") and [Colliders](https://docs.omniverse.nvidia.com/kit/docs/omni_physics/latest/dev_guide/rigid_bodies_articulations/collision.html "(in Omni Physics)").

#### Contact and Rest Offset

In the Collider Advanced tab, there are two more parameters that can be important tuning parameters when there are collision issues, in particular with small and thin objects.

The Rest Offset can be tuned to inflate or shrink the collision geometry set; it can be useful to adjust in cases where the visual mesh is larger or smaller than the collision geometry so that the collision locations are consistent with the visual representation.

The Contact Offset dictates how far from the collision geometry, irrespective of Rest Offset, the simulation engine starts generating contact constraints. The tradeoff for tuning the contact offset is performance vs. collision fidelity: A larger Contact Offset results in many contact constraints being generated which is more computationally expensive; a smaller offset can result in issues with contacts being detected too late, and symptoms include jittering or missed contacts or even tunneling (see notes on CCD above).

### Contacts and Friction

Besides making sure that object do not interpenetrate, collisions can transfer or dissipate energy as modeled by restitution and friction.

The parameters for the contact model are available in Physics materials. To create a Physics material:

1. Go to **Create** > **Physics** > **Physics Material**.
2. Select Rigid Body Material.

Physics materials are typically assigned to **Collider Geometry** but behave analogous to USD render materials otherwise; see [Physics Materials](https://docs.omniverse.nvidia.com/kit/docs/omni_physics/latest/index.html "(in Omni Physics)") for a full explanation of USD material resolution logic. For example, you may assign different materials to different collision geometry of a rigid body, or you may assign a material to the rigid body prim and configure it to override any materials set on the collider children.

To assign a physics material:

1. Select the collider prim.
2. Scroll to the Collider settings.
3. In Physics Materials on Selected Models, select the desired material. The list only allows picking materials that have physics properties.

Note that you may also add a physics material to a render material with **âAddâ** > **Physics** > **Rigid Body Material** and assign the material in the render material section; the physics properties will be picked up.

#### Compliant Contacts

You may configure the rigid material to produce compliant (i.e. spring-damper) contact dynamics in the Advanced tab. This may be useful for approximating deformable bodies with rigid bodies.

#### Combine Modes

Because contacts are an interaction between two bodies, each contact parameter is not enough to describe how this interaction plays out. Just like in the real world, one surface material property may dominate the interaction or they may seamlessly combine into an average value. To replicate that, friction, restitution, and compliant-contact damping have a configurable combine mode field. Because both sides of the contact have this combine mode, the precedence of the combine mode matters:

The lower in the drop-down, the lower the priority of a mode in a combine mismatch resolution; so `average < min < multiply < max`.

For example, if Collider A has a friction combine mode average while Collider B has min, their interaction resolves as the minimum friction between the two. If a body C with combine mode max contacts A and B, the friction between A and C are resolved with max, as well as B and C.

### Joints

Robots are typically composed of multiple jointed rigid bodies. Joints create constraints between two bodies. In the following, you use a **Revolute Joint**, but the steps are similar for other joint types, see a list in [Joints](https://docs.omniverse.nvidia.com/kit/docs/omni_physics/latest/dev_guide/rigid_bodies_articulations/joints.html#joints "(in Omni Physics)").

You must configure the relative pose of the joint frames for each body to be jointed. Find more details, in particular the local scaling aspect of joint frames in the [Joint Frames Section](https://docs.omniverse.nvidia.com/kit/docs/omni_physics/latest/dev_guide/rigid_bodies_articulations/joints.html#jointframes "(in Omni Physics)").

Note that when creating a joint through the UI, the jointâs frames are set to match the pose of the second rigid body selected for the creation.

Now create a joint as follows:

1. Select first the Xform rigid body, and then the Torus rigid body.
2. Go to **Create** > **Physics** > **Joints** > **(Joint Type)**.

For this tutorial, use the **Revolute Joint** type. Because the Torus was selected second, the joint is at its center.

You will notice a circle on-screen, representing the origin and range of motion for the joint. If you start the simulation now, the Torus and Cube fall together. When the torus hits the ground, the cube stops moving. Itâs in a stable position, but if you nudge it, it moves down in a circular pattern. Interact with the cube by pressing shift and left-clicking the cube.

Check the properties panel and review the following attributes:

1. Body 0: /World/XForm
2. Body 1: /World/Torus

These are the Poses relative to the bodies. You will notice that Position 0 is `Z=-7.0`.

1. Position 0: `[0, 0, -7.0]`
2. Rotation 0: `[0, 0, 0.0]`
3. Position 1: `[0, 0, 0.0]`
4. Rotation 1: `[0, 0, 0.0]`

Note

When setting up joints that are part of an articulation, make sure that Body 0 will be the parent of Body 1 in the articulation-tree hierarchy. This way, joint-related quantities like link incoming joint forces or joint drive targets have a one-to-one correspondence in the PhysX SDK and USD.

#### Joint Axis

A revolute joint provides one degree of freedom and you may choose what axis of the joint frames is free. By default, the X axis is selected. You can change that in Properties, under the Revolute Joint section.

#### Joint Limits

The joint limits determine how far the joint can move from its original position. By default, when a joint is created, it comes without limits. With the joint selected, scroll down in the Properties panel and modify the Lower Limit and Upper Limit under the Revolute Joint section. Remember that USD uses degrees, not radians to represent angles.

#### Adding a Joint Drive

You may control the position and velocity of the degree of freedom that the joint added using a Joint Drive. You can do that by clicking the **Add Button** > **Physics** > **Angular Drive**. For details on configuring a joint drive, refer to [Tutorial 11: Tuning Joint Drive Gains](../robot_setup_tutorials/joint_tuning.html#isaac-sim-app-tutorial-advanced-joint-tuning).

## Articulation

An articulation is an optimized simulation structure for jointed bodies that provides superior performance, fidelity, and features for robotics. There are some limitations regarding topology (loop-closing) and joint support, which you can learn about in [Articulations](https://docs.omniverse.nvidia.com/kit/docs/omni_physics/latest/dev_guide/rigid_bodies_articulations/articulations.html#articulations "(in Omni Physics)"). For a complete guide in tuning articulations, refer to [Articulation Stability Guide](https://docs.omniverse.nvidia.com/kit/docs/omni_physics/latest/dev_guide/guides/articulation_stability_guide.html).

For overall Simulation Hints and FAQ, refer to [Physx Simulation Hints and FAQ](https://docs.omniverse.nvidia.com/kit/docs/omni_physics/107.3/dev_guide/guides.html).

## Stepping an OmniGraph with Physics

To guarantee one graph step per physics step at the moment it happens, you must use a modified version of an OmniGraph.

1. Create a new Action Graph through **Create** > **Visual Scripting** > **Action Graph**.
2. Select the created graph on the stage and in the **Raw USD Properties** section, in the pipeline stage, select *PipelineStageOnDemand*.
3. On the Action Graph window, search for **On Physics Step**. Drag and Drop it on your OmniGraph.
4. Continue your OmniGraph as usual.

On this page

* [Physics in USD Schemas](#physics-in-usd-schemas)
* [Simulation Timeline](#simulation-timeline)
  + [Configuring Frame Rate](#configuring-frame-rate)
  + [Configuring Simulation Timesteps](#configuring-simulation-timesteps)
* [Simulation Components](#simulation-components)
  + [Rigid Body](#rigid-body)
  + [Colliders](#colliders)
    - [Convex Hull](#convex-hull)
    - [Convex Decomposition](#convex-decomposition)
    - [Contact and Rest Offset](#contact-and-rest-offset)
  + [Contacts and Friction](#contacts-and-friction)
    - [Compliant Contacts](#compliant-contacts)
    - [Combine Modes](#combine-modes)
  + [Joints](#joints)
    - [Joint Axis](#joint-axis)
    - [Joint Limits](#joint-limits)
    - [Adding a Joint Drive](#adding-a-joint-drive)
* [Articulation](#articulation)
* [Stepping an OmniGraph with Physics](#stepping-an-omnigraph-short-with-physics)

---

### Static Collision

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/physics/physics_static_collision.html

* [Physics](index.html)
* Physics Static Collision Extension

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Physics Static Collision Extension

The [Physics Static Collision Extension](#isaac-static-collision-utils) Extension is used to visualize collision meshes. Use this Utility extension to add static collision APIs to an entire [Stage](../reference_material/reference_glossary.html#isaac-sim-glossary-stage). The extension can also be used to remove all physics related APIs for testing purposes.

This extension is enabled by default. If it is ever disabled, it can be re-enabled from the [Extension Manager](https://docs.omniverse.nvidia.com/extensions/latest/ext_core/ext_extension-manager.html "(in Omniverse Extensions)") by searching for `isaacsim.utils.physics`.

To access this Extension, go to the top menu bar and click **Tools** > **Physics API Editor**.

Note

Dynamic objects are currently not supported.

## User Interface

The User Interface provides options to add or clear static collision on selected static objects.

### Configuration Options

* **Apply to children**: Recursively create collision on all selected children; otherwise, create collision for just the selected object.
* **Visible only**: Ensure the prim is visible before creating collision. (Ignores hidden prims)
* **Collision Type**: Type of collision approximation to use
* **Apply Static**: Applies collision to the current selection.
* **Remove Collision API**: Clears the collision from the current selection.
* **Remove All Physics APIs**: Remove all Physics-related APIs (including collision) from the current selection.

### Enable Visualization

To visualize collision in any viewport:

1. **Select**: the  eye icon.
2. **Select**: Show by type.
3. **Select**: Physics Mesh.
4. **Check**: All.

Note

Enable visualization **after** collision APIs have been applied or removed. Otherwise there will be a loss in performance while the extension traverses the desired subtree.

On this page

* [User Interface](#user-interface)
  + [Configuration Options](#configuration-options)
  + [Enable Visualization](#enable-visualization)

---

### Inspect Physics

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/physics/ext_isaacsim_inspect_physics.html

* [Robot Setup](../robot_setup/index.html)
* [Inspector Tools](../robot_setup/inspector_tools.html)
* Simulation Data Visualizer

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Simulation Data Visualizer

The [Simulation Data Visualizer](#isaac-inspect-physics) is used to visualize information for the selected prim. You can use this tool to better understand the behaviors of physics-enabled geometry during simulation.

If a non-physics prim is selected, position changes over the course of simulation are tracked. However, when a physics element is selected, it shows more physics properties, including position and velocities (linear, angular).

## Conventions

The simulation data visualizer provides the following information:

* **Position**: in [Stage](../reference_material/reference_glossary.html#isaac-sim-glossary-stage) units [X, Y, Z]
* **Rotation**: in degrees [X, Y, Z]
* **Linear Velocity**: in [Stage](../reference_material/reference_glossary.html#isaac-sim-glossary-stage) units/s
* **Angular Velocity**: in degrees/s
* **Linear Acceleration**: in [Stage](../reference_material/reference_glossary.html#isaac-sim-glossary-stage) units/s^2
* **Mass**: in [Stage](../reference_material/reference_glossary.html#isaac-sim-glossary-stage) mass unit
* **Moment of Inertia**: in [Stage](../reference_material/reference_glossary.html#isaac-sim-glossary-stage) mass unit\*[Stage](../reference_material/reference_glossary.html#isaac-sim-glossary-stage) units^2

For velocities, thereâs a fourth plot M, which is the magnitude of the vector.

## Inspect Physics Example

To run this utility:

1. Open the Simulation Data Visualizer by going to the **Visibility Menu (eye icon on viewport) > Show by Type > Physics > Simulation Data Visualizer**.
2. Activate **Windows** > **Examples** > **Robotics Examples** which will open the `Robotics Examples` tab.
3. Load some simulation-ready example, such as the Cortex Franka example, by clicking **Robotics Examples > Cortex > Franka Cortex Examples**.
4. Press the **Load Robot** button.
5. Select the **/World/Franka/panda\_hand** prim from the [Stage](../reference_material/reference_glossary.html#isaac-sim-glossary-stage).
6. Press the **START** button to begin simulating.

After simulation starts, the physics state of the selected rigid body updates in the **Inspect Physics** window.

On this page

* [Conventions](#conventions)
* [Inspect Physics Example](#inspect-physics-example)

---

### Physics Index

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/physics/index.html

* Physics

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Physics

On a high-level, simulations with Omniverseâ¢ Physics work as follows:

* The USD Physics schema of robot and environment assets are parsed and corresponding simulation objects are created in the selected physics backend.
* Then, for each discrete-time step of the simulation, Physics advances the simulation objects given their current state and additional inputs such as, for example, control-policy torques.
* The updated state is written back to USD by default, where the state can be further processed by the user, a reinforcement-learning policy, or other extensions such as the Omniverse RTX Renderer.
* Omniverseâ¢ Physics propagates runtime changes to physics parameters in USD to the physics objects.

Isaac Sim supports multiple physics backends: the default PhysX SDK backend and the experimental Newton backend.

* [Physics Simulation Fundamentals](simulation_fundamentals.html)
  + [Physics in USD Schemas](simulation_fundamentals.html#physics-in-usd-schemas)
  + [Simulation Timeline](simulation_fundamentals.html#simulation-timeline)
    - [Configuring Frame Rate](simulation_fundamentals.html#configuring-frame-rate)
    - [Configuring Simulation Timesteps](simulation_fundamentals.html#configuring-simulation-timesteps)
  + [Simulation Components](simulation_fundamentals.html#simulation-components)
    - [Rigid Body](simulation_fundamentals.html#rigid-body)
    - [Colliders](simulation_fundamentals.html#colliders)
    - [Contacts and Friction](simulation_fundamentals.html#contacts-and-friction)
    - [Joints](simulation_fundamentals.html#joints)
  + [Articulation](simulation_fundamentals.html#articulation)
  + [Stepping an OmniGraph with Physics](simulation_fundamentals.html#stepping-an-omnigraph-short-with-physics)
* [Physics Data Flow and Engine Integration](new_physics_engine.html)
  + [Physics Data Flow](new_physics_engine.html#id1)
    - [Data Pathways Explained](new_physics_engine.html#data-pathways-explained)
    - [Per-Engine Data Pathways](new_physics_engine.html#per-engine-data-pathways)
    - [Choosing a Pathway](new_physics_engine.html#choosing-a-pathway)
  + [Implementing a Physics Engine](new_physics_engine.html#implementing-a-physics-engine)
    - [Architecture Overview](new_physics_engine.html#architecture-overview)
    - [Integration Flow](new_physics_engine.html#integration-flow)
    - [Engine Switching at Runtime](new_physics_engine.html#engine-switching-at-runtime)
* [Newton Physics Backend](newton_physics.html)
  + [Overview](newton_physics.html#overview)
    - [Using the Experimental Core API](newton_physics.html#using-the-experimental-core-api)
  + [Launching Isaac Sim with Newton](newton_physics.html#launching-isaac-sim-with-newton)
  + [Switching Physics Engines at Runtime](newton_physics.html#switching-physics-engines-at-runtime)
  + [Basic Usage Example](newton_physics.html#basic-usage-example)
  + [Scene Configuration](newton_physics.html#scene-configuration)
    - [Newton USD Schemas](newton_physics.html#newton-usd-schemas)
    - [PhysicsScene Base Class](newton_physics.html#physicsscene-base-class)
    - [MuJoCo Solver Configuration](newton_physics.html#mujoco-solver-configuration)
    - [Robot Simulation Example](newton_physics.html#robot-simulation-example)
  + [Asset Compatibility](newton_physics.html#asset-compatibility)
  + [Additional Resources](newton_physics.html#additional-resources)
* [Omniverseâ¢ Physics and PhysX SDK Limitations](physics_resources.html)

## Tools

* [Physics Simulation Management](https://docs.omniverse.nvidia.com/kit/docs/omni_physics/latest/extensions/ux/source/omni.physx.ui/docs/dev_guide/sim_management.html "(in Omni Physics)")
* [Physics Inspector](joint_inspector.html)
* [Physics Static Collision Extension](physics_static_collision.html)
* [Simulation Data Visualizer](ext_isaacsim_inspect_physics.html)
* [Physics Debug Window](https://docs.omniverse.nvidia.com/kit/docs/omni_physics/latest/extensions/ux/source/omni.physx.ui/docs/dev_guide/physics_debug_wnd.html "(in Omni Physics)")

## Additional Resources

* Omniverseâ¢ Physics [core documentation](https://docs.omniverse.nvidia.com/kit/docs/omni_physics/latest/index.html "(in Omni Physics)") and [programming guide](https://docs.omniverse.nvidia.com/kit/docs/omni_physics/latest/index.html)
* [USD Physics Schemas](https://openusd.org/release/api/usd_physics_page_front.html) and PhysX SDK-engine-specific [Physx Schemas](https://docs.omniverse.nvidia.com/kit/docs/omni_usd_schema_physics/latest/annotated.html)
* Explore further Omniverse [simulation extensions](https://docs.omniverse.nvidia.com/extensions/latest/ext_simulation.html#simoverview "(in Omniverse Extensions)").
* [PhysX SDK](https://nvidia-omniverse.github.io/PhysX/physx/5.4.2/index.html)
* [Omniverse Visual Debugger](https://nvidia-omniverse.github.io/PhysX/physx/5.4.2/docs/OmniVisualDebugger.html)
* [Flow: Fluid Dynamics](https://docs.omniverse.nvidia.com/extensions/latest/ext_fluid-dynamics.html "(in Omniverse Extensions)")
* [NVIDIA Warp](https://nvidia.github.io/warp/index.html)

On this page

* [Tools](#tools)
* [Additional Resources](#additional-resources)

---

