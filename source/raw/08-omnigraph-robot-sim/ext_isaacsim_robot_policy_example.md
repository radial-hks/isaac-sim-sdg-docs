---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/robot_simulation/ext_isaacsim_robot_policy_example.html
title: "Policy Example"
section: "Robot Simulation"
module: "08-omnigraph-robot-sim"
checksum: "e1b73185f11779d6"
fetched: "2026-06-21T13:05:39"
---

* [Robot Simulation](index.html)
* Reinforcement Learning Policies Examples in Isaac Sim

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Reinforcement Learning Policies Examples in Isaac Sim

## About

The isaac\_sim\_policy\_example Extension is a framework and has a set of helper functions to deploy Isaac Lab Reinforcement Learning Policies in Isaac Sim.
For details for training and building the policy in Isaac Sim, visit [deploying policy in Isaac Sim](../isaac_lab_tutorials/tutorial_policy_deployment.html#isaac-sim-app-tutorial-policy-deployment).

This Extension is enabled by default. If it is ever disabled, it can be re-enabled from the [Extension Manager](https://docs.omniverse.nvidia.com/extensions/latest/ext_core/ext_extension-manager.html "(in Omniverse Extensions)") by searching for `isaacsim.robot.policy.example`.
To run examples below activate **Windows** > **Examples** > **Robotics Examples** which will open the `Robotics Examples` tab.

### Unitree H1 Humanoid Example

1. The Unitree H1 humanoid example can be accessed by creating a empty stage.
2. Open the example menu using **Robotics Examples** > **POLICY** > **Humanoid**.
3. (Optional) Use the **Physics Engine** menu in the viewport to switch between PhysX and Newton before loading. The example automatically selects the matching policy for the active engine.
4. Press **LOAD** to open the scene.

This example uses an H1 Flat Terrain Policy trained in Isaac Lab to control the humanoidâs locomotion. Both PhysX and Newton policies are provided so you can compare locomotion behavior across physics engines.

Controls:

* Forward: UP ARROW / NUM 8
* Turn Left: LEFT ARROW / NUM 4
* Turn Right: RIGHT ARROW / NUM 6

### Boston Dynamics Spot Quadruped Example

1. The Boston Dynamics Spot quadruped example can be accessed by creating a empty stage.
2. Open the example menu using **Robotics Examples** > **POLICY** > **Quadruped**.
3. (Optional) Use the **Physics Engine** menu in the viewport to switch between PhysX and Newton before loading. The example automatically selects the matching policy for the active engine.
4. Press **LOAD** to open the scene.

This example uses a Spot Flat Terrain Policy trained in Isaac Lab to control the quadrupedâs locomotion. Both PhysX and Newton policies are provided so you can compare locomotion behavior across physics engines.

Controls:

* Forward: UP ARROW / NUM 8
* Backward: BACK ARROW / NUM 2
* Move Left: LEFT ARROW / NUM 4
* Move Right: RIGHT ARROW / NUM 6
* Turn Left: N / NUM 7
* Turn Right: M / NUM 9

### Unitree Go2 Quadruped Example

1. The Unitree Go2 quadruped example can be accessed by creating a empty stage.
2. Open the example menu using **Robotics Examples** > **POLICY** > **Go2**.
3. (Optional) Use the **Physics Engine** menu in the viewport to switch between PhysX and Newton before loading. The example automatically selects the matching policy for the active engine.
4. Press **LOAD** to open the scene.

This example uses a Go2 Flat Terrain Policy trained in Isaac Lab to control the quadrupedâs locomotion. Both PhysX and Newton policies are provided so you can compare locomotion behavior across physics engines.

Controls:

* Forward: UP ARROW / NUM 8
* Backward: BACK ARROW / NUM 2
* Move Left: LEFT ARROW / NUM 4
* Move Right: RIGHT ARROW / NUM 6
* Turn Left: N / NUM 7
* Turn Right: M / NUM 9

### Franka Panda Open Drawer Example

1. The Franka Panda Open Drawer example can be accessed by creating a empty stage.
2. Open the example menu using **Robotics Examples** > **POLICY** > **Franka**.
3. Press **LOAD** to open the scene.

This example uses the Franka Open Drawer Policy trained in Isaac Lab to control the robotâs arm.
The robot will open the drawer, hold it open until the would reset.

## Policies Files

The policies used in the examples are trained in Isaac Lab and are available here:

|  |  |  |
| --- | --- | --- |
| Name | Policy | Parameters |
| H1 Flat Terrain Policy (PhysX) | [H1 Flat Terrain Policy (PhysX)](https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Isaac/6.0/Isaac/Samples/Policies/h1/physx_policy.pt) | [H1 Flat Terrain Policy (PhysX) Environment Parameters](https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Isaac/6.0/Isaac/Samples/Policies/h1/physx_env.yaml) |
| H1 Flat Terrain Policy (Newton) | [H1 Flat Terrain Policy (Newton)](https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Isaac/6.0/Isaac/Samples/Policies/h1/newton_policy.pt) | [H1 Flat Terrain Policy (Newton) Environment Parameters](https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Isaac/6.0/Isaac/Samples/Policies/h1/newton_env.yaml) |
| Spot Flat Terrain Policy (PhysX) | [Spot Flat Terrain Policy (PhysX)](https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Isaac/6.0/Isaac/Samples/Policies/Spot_Policies/spot_policy.pt) | [Spot Flat Terrain Policy (PhysX) Environment Parameters](https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Isaac/6.0/Isaac/Samples/Policies/Spot_Policies/spot_env.yaml)  [Spot Flat Terrain Policy Network Parameters](https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Isaac/6.0/Isaac/Samples/Policies/Spot_Policies/agent.yaml) |
| Spot Flat Terrain Policy (Newton) | [Spot Flat Terrain Policy (Newton)](https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Isaac/6.0/Isaac/Samples/Policies/Spot_Policies/newton_policy.pt) | [Spot Flat Terrain Policy (Newton) Environment Parameters](https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Isaac/6.0/Isaac/Samples/Policies/Spot_Policies/newton_env.yaml) |
| ANYmal C Flat Terrain Policy | [ANYmal C Flat Terrain Policy](https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Isaac/6.0/Isaac/Samples/Policies/Anymal_Policies/anymal_policy.pt)  [ANYmal C Actuator Network](https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Isaac/6.0/Isaac/IsaacLab/ActuatorNets/ANYbotics/anydrive_3_lstm_jit.pt) | [ANYmal C Flat Terrain Policy Environment Parameters](https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Isaac/6.0/Isaac/Samples/Policies/Anymal_Policies/anymal_env.yaml)  [ANYmal C Flat Terrain Policy Network Parameters](https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Isaac/6.0/Isaac/Samples/Policies/Anymal_Policies/agent.yaml) |
| Franka Panda Open Drawer Policy | [Franka Panda Open Drawer Policy](https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Isaac/6.0/Isaac/Samples/Policies/Franka_Policies/Open_Drawer_Policy/policy.pt) | [Franka Panda Open Drawer Policy Environment Parameters](https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Isaac/6.0/Isaac/Samples/Policies/Franka_Policies/Open_Drawer_Policy/env.yaml) |
| Go2 Flat Terrain Policy (PhysX) | [Go2 Flat Terrain Policy (PhysX)](https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Isaac/6.0/Isaac/Samples/Policies/go2/physx_policy.pt) | [Go2 Flat Terrain Policy (PhysX) Environment Parameters](https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Isaac/6.0/Isaac/Samples/Policies/go2/physx_env.yaml) |
| Go2 Flat Terrain Policy (Newton) | [Go2 Flat Terrain Policy (Newton)](https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Isaac/6.0/Isaac/Samples/Policies/go2/newton_policy.pt) | [Go2 Flat Terrain Policy (Newton) Environment Parameters](https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Isaac/6.0/Isaac/Samples/Policies/go2/newton_env.yaml) |

Note

The policies can also be downloaded directly from the Content Browser by right clicking the policy and selecting `Download`.

Warning

The example policies uses separate robots for physx and newton, depending on the physics engine selected initially. Switching the physics engine will require the robot to be respawned.

## API Documentation

See the [API documentation](../py/source/extensions/isaacsim.robot.policy.examples/docs/index.html) for complete usage information.

## Standalone Examples

**h1\_standalone.py**

* This standalone example demonstrates a Unitree H1 controlled by a flat terrain policy, following a set of predetermined command sequences. It may be run via the following command:

  > ```python
  > ./python.sh standalone_examples/api/isaacsim.robot.policy.examples/h1_standalone.py --num-robots <number of robot> --env-url </path/to/environment>
  > ```
  >
  > For example, this will spawn 5 robots on the flat grid scene below:
  >
  > ```python
  > ./python.sh standalone_examples/api/isaacsim.robot.policy.examples/h1_standalone.py --num-robots 5 --env-url /Isaac/Environments/Grid/default_environment.usd
  > ```

**spot\_standalone.py**

* This standalone example demonstrates a Boston Dynamics Spot controlled by a flat terrain policy, following a set of predetermined command sequences. It may be run via the following command:

  > ```python
  > ./python.sh standalone_examples/api/isaacsim.robot.policy.examples/spot_standalone.py
  > ```

**anymal\_standalone.py**

* This standalone example demonstrates an ANYmal C robot that is controlled by a neural network policy. The rough terrain policy was trained in Isaac Lab and takes as input the state of the robot, the commanded base velocity, and the surrounding terrain and outputs joint position targets. The example may be run via the following command:

  > ```python
  > ./python.sh standalone_examples/api/isaacsim.robot.policy.examples/anymal_standalone.py
  > ```

Controls:

* Forward: UP ARROW / NUM 8
* Backward: BACK ARROW / NUM 2
* Move Left: LEFT ARROW / NUM 4
* Move Right: RIGHT ARROW / NUM 6
* Turn Left: N / NUM 7
* Turn Right: M / NUM 9

On this page

* [About](#about)
  + [Unitree H1 Humanoid Example](#unitree-h1-humanoid-example)
  + [Boston Dynamics Spot Quadruped Example](#boston-dynamics-spot-quadruped-example)
  + [Unitree Go2 Quadruped Example](#unitree-go2-quadruped-example)
  + [Franka Panda Open Drawer Example](#franka-panda-open-drawer-example)
* [Policies Files](#policies-files)
* [API Documentation](#api-documentation)
* [Standalone Examples](#standalone-examples)