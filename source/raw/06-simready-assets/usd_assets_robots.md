---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/assets/usd_assets_robots.html
title: "Robots"
section: "资产库"
module: "06-simready-assets"
checksum: "a6623e77bff339b4"
fetched: "2026-06-21T11:55:35"
---

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