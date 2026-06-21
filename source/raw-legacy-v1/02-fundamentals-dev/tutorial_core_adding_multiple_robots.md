---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/core_api_tutorials/tutorial_core_adding_multiple_robots.html
title: "Adding Multiple Robots"
section: "Core API"
module: "02-fundamentals-dev"
checksum: "237dac5ea185f820"
fetched: "2026-06-21T13:39:54"
---

* [Python Scripting and Tutorials](../python_scripting/index.html)
* [Core API Tutorial Series](index.html)
* Adding Multiple Robots

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Adding Multiple Robots

## Learning Objectives

This tutorial integrates two different types of robots into the same simulation:
a mobile robot (Jetbot) and a manipulator (Franka), working together to accomplish a task.
The Jetbot pushes a cube towards the Franka, which then picks it up.
After this tutorial, you will have experience building multi-robot simulations with object interaction.

*15-20 Minute Tutorial*

## Getting Started

**Prerequisites**

* Review [Adding a Manipulator Robot](tutorial_core_adding_manipulator.html#isaac-sim-app-tutorial-core-adding-manipulator) prior to beginning this tutorial.

Begin with the source code open from the previous tutorial, [Adding a Manipulator Robot](tutorial_core_adding_manipulator.html#isaac-sim-app-tutorial-core-adding-manipulator).

Note

Pressing **STOP**, then **PLAY** in this workflow might not reset the world properly. Use
the **RESET** button instead.

## Creating the Scene

Begin by adding the Jetbot, Franka Panda, and the Cube from the previous tutorials to the scene.

```python
 1import isaacsim.core.experimental.utils.stage as stage_utils
 2import numpy as np
 3from isaacsim.core.experimental.materials import PreviewSurfaceMaterial
 4from isaacsim.core.experimental.objects import Cube
 5from isaacsim.core.experimental.prims import Articulation, GeomPrim, RigidPrim, XformPrim
 6from isaacsim.examples.base.base_sample_experimental import BaseSample
 7from isaacsim.storage.native import get_assets_root_path
 8
 9
10class HelloWorld(BaseSample):
11    def __init__(self) -> None:
12        super().__init__()
13
14    # -- Begin setup_scene -- #
15    def setup_scene(self):
16        assets_root_path = get_assets_root_path()
17
18        # Add ground plane
19        stage_utils.add_reference_to_stage(
20            usd_path=assets_root_path + "/Isaac/Environments/Grid/default_environment.usd",
21            path="/World/ground",
22        )
23
24        # Add Jetbot mobile robot
25        stage_utils.add_reference_to_stage(
26            usd_path=assets_root_path + "/Isaac/Robots/NVIDIA/Jetbot/jetbot.usd",
27            path="/World/Jetbot",
28        )
29
30        # Add a cube in front of Jetbot for it to push
31        visual_material = PreviewSurfaceMaterial("/World/Materials/red")
32        visual_material.set_input_values("diffuseColor", [1.0, 0.0, 0.0])
33        cube_shape = Cube(
34            paths="/World/Cube",
35            positions=np.array([[0.15, 0.0, 0.025]]),  # In front of Jetbot
36            sizes=[1.0],
37            scales=np.array([[0.05, 0.05, 0.05]]),
38            reset_xform_op_properties=True,
39        )
40        GeomPrim(paths=cube_shape.paths, apply_collision_apis=True)
41        RigidPrim(paths=cube_shape.paths)
42        cube_shape.apply_visual_materials(visual_material)
43
44        # Add Franka manipulator at a position the Jetbot will push the cube to
45        stage_utils.add_reference_to_stage(
46            usd_path=assets_root_path + "/Isaac/Robots/FrankaRobotics/FrankaPanda/franka.usd",
47            path="/World/Franka",
48        )
49
50        # Position Franka so the cube will be pushed into its workspace
51        franka_xform = XformPrim("/World/Franka")
52        franka_xform.set_world_poses(positions=np.array([[0.8, -0.5, 0.0]]))
53
54    # -- End of setup_scene -- #
55
56    async def setup_post_load(self):
57        # Create Articulation handles for both robots
58        self._jetbot = Articulation("/World/Jetbot")
59        self._franka = Articulation("/World/Franka")
60
61        # Print robot info
62        print(f"Jetbot DOFs: {self._jetbot.num_dofs}, names: {self._jetbot.dof_names}")
63        print(f"Franka DOFs: {self._franka.num_dofs}, names: {self._franka.dof_names}")
```

Click the **LOAD** button to see both robots and the cube in the scene.

## Controlling Multiple Robots

Now add physics callbacks to control both robots simultaneously. The Jetbot will push the cube
forward while the Franka prepares to receive it.

```python
1        self._step_counter += 1
2        if self._step_counter < 300:
3            # Drive Jetbot forward to push the cube
4            self._jetbot.set_dof_velocity_targets([[10.0, 10.0]])
5        else:
6            # Stop the Jetbot after pushing
7            self._jetbot.set_dof_velocity_targets([[0.0, 0.0]])
```

Complete code:

```python
 1import isaacsim.core.experimental.utils.stage as stage_utils
 2import numpy as np
 3from isaacsim.core.experimental.materials import PreviewSurfaceMaterial
 4from isaacsim.core.experimental.objects import Cube
 5from isaacsim.core.experimental.prims import Articulation, GeomPrim, RigidPrim, XformPrim
 6from isaacsim.core.simulation_manager import SimulationManager
 7from isaacsim.examples.base.base_sample_experimental import BaseSample
 8from isaacsim.storage.native import get_assets_root_path
 9
10
11class HelloWorld(BaseSample):
12    def __init__(self) -> None:
13        super().__init__()
14        self._physics_callback_id = None
15        self._step_counter = 0
16
17    def setup_scene(self):
18        assets_root_path = get_assets_root_path()
19
20        # Add ground plane
21        stage_utils.add_reference_to_stage(
22            usd_path=assets_root_path + "/Isaac/Environments/Grid/default_environment.usd",
23            path="/World/ground",
24        )
25
26        # Add Jetbot mobile robot
27        stage_utils.add_reference_to_stage(
28            usd_path=assets_root_path + "/Isaac/Robots/NVIDIA/Jetbot/jetbot.usd",
29            path="/World/Jetbot",
30        )
31
32        # Add a cube in front of Jetbot for it to push
33        visual_material = PreviewSurfaceMaterial("/World/Materials/red")
34        visual_material.set_input_values("diffuseColor", [1.0, 0.0, 0.0])
35        cube_shape = Cube(
36            paths="/World/Cube",
37            positions=np.array([[0.15, 0.0, 0.025]]),
38            sizes=[1.0],
39            scales=np.array([[0.05, 0.05, 0.05]]),
40            reset_xform_op_properties=True,
41        )
42        GeomPrim(paths=cube_shape.paths, apply_collision_apis=True)
43        RigidPrim(paths=cube_shape.paths)
44        cube_shape.apply_visual_materials(visual_material)
45
46        # Add Franka manipulator
47        stage_utils.add_reference_to_stage(
48            usd_path=assets_root_path + "/Isaac/Robots/FrankaRobotics/FrankaPanda/franka.usd",
49            path="/World/Franka",
50        )
51
52        # Position Franka forward and to the right of Jetbot's path
53        franka_xform = XformPrim("/World/Franka")
54        franka_xform.set_world_poses(positions=np.array([[0.8, -0.5, 0.0]]))
55
56    async def setup_post_load(self):
57        # Create Articulation handles
58        self._jetbot = Articulation("/World/Jetbot")
59        self._franka = Articulation("/World/Franka")
60        self._cube = RigidPrim("/World/Cube")
61        self._step_counter = 0
62
63        # Register physics callback
64        from isaacsim.core.simulation_manager.impl.isaac_events import IsaacEvents
65
66        self._physics_callback_id = SimulationManager.register_callback(
67            self.physics_step, IsaacEvents.POST_PHYSICS_STEP
68        )
69
70    def physics_step(self, dt, context):
71        # -- Begin control Jetbot -- #
72        self._step_counter += 1
73        if self._step_counter < 300:
74            # Drive Jetbot forward to push the cube
75            self._jetbot.set_dof_velocity_targets([[10.0, 10.0]])
76        else:
77            # Stop the Jetbot after pushing
78            self._jetbot.set_dof_velocity_targets([[0.0, 0.0]])
79        # -- End of control Jetbot -- #
80
81    def physics_cleanup(self):
82        if self._physics_callback_id is not None:
83            SimulationManager.deregister_callback(self._physics_callback_id)
84            self._physics_callback_id = None
```

Watch as the Jetbot pushes the cube towards the Franka!

## Adding State Machine Logic

Create a state machine to coordinate the robots: first the Jetbot pushes the cube towards Franka,
then backs up to give space, and finally Franka executes a full pick-and-place sequence using
the `Franka` class for IK-based end-effector control:

```python
 1        if self._state == 0:
 2            # Jetbot pushes cube to Franka
 3            cube_pos = self._cube.get_world_poses()[0].numpy()[0]
 4            if np.linalg.norm(cube_pos[:2] - self._cube_goal[:2]) > 0.05:
 5                self._jetbot.set_dof_velocity_targets([[10.0, 10.0]])
 6            else:
 7                self._jetbot.set_dof_velocity_targets([[0.0, 0.0]])
 8                print("Cube delivered! Backing up...")
 9                self._state = 1
10                self._step_counter = 0
11
12        elif self._state == 1:
13            # Jetbot backs up
14            self._jetbot.set_dof_velocity_targets([[-8.0, -8.0]])
15            self._step_counter += 1
16            if self._step_counter > 100:
17                self._jetbot.set_dof_velocity_targets(np.array([[0.0, 0.0]]))
18                print("Franka starting pick-and-place...")
19                self._state = 2
20                self._step_counter = 0
21                self._franka.open_gripper()
22
23        elif self._state == 2:
24            # Franka pick-and-place sequence using step counter
25            cube_pos = self._cube.get_world_poses()[0].numpy()[0]
26            down_orient = self._franka.get_downward_orientation()
27            self._step_counter += 1
28
29            if self._pick_phase == 0:
30                # Move above cube (wait 120 steps)
31                self._franka.set_end_effector_pose(
32                    np.array([[cube_pos[0], cube_pos[1], cube_pos[2] + 0.2]]), down_orient
33                )
34                if self._step_counter > 120:
35                    self._pick_phase = 1
36                    self._step_counter = 0
37            elif self._pick_phase == 1:
38                # Lower to cube (wait 100 steps)
39                self._franka.set_end_effector_pose(
40                    np.array([[cube_pos[0], cube_pos[1], cube_pos[2] + 0.1]]), down_orient
41                )
42                if self._step_counter > 100:
43                    self._franka.close_gripper()
44                    self._pick_phase = 2
45                    self._step_counter = 0
46            elif self._pick_phase == 2:
47                # Close the gripper (wait 50 steps)
48                self._franka.close_gripper()
49                if self._step_counter > 50:
50                    self._pick_phase = 3
51                    self._step_counter = 0
52            elif self._pick_phase == 3:
53                # Lift cube (wait 100 steps)
54                self._franka.set_end_effector_pose(
55                    np.array([[cube_pos[0], cube_pos[1], cube_pos[2] + 0.25]]), down_orient
56                )
57                if self._step_counter > 100:
58                    self._pick_phase = 4
59                    self._step_counter = 0
60            elif self._pick_phase == 4:
61                # Move to target (wait 150 steps)
62                self._franka.set_end_effector_pose(np.array([[0.3, 0.3, 0.15]]), down_orient)
63                if self._step_counter > 150:
64                    self._franka.open_gripper()
65                    self._pick_phase = 5
66                    self._step_counter = 0
67            elif self._pick_phase == 5:
68                # Lift the arm (wait 150 steps)
69                self._franka.set_end_effector_pose(
70                    np.array([[cube_pos[0], cube_pos[1], cube_pos[2] + 0.5]]), down_orient
71                )
72                if self._step_counter > 150:
73                    self._step_counter = 0
```

Complete code:

```python
  1import isaacsim.core.experimental.utils.stage as stage_utils
  2import numpy as np
  3from isaacsim.core.experimental.materials import PreviewSurfaceMaterial
  4from isaacsim.core.experimental.objects import Cube
  5from isaacsim.core.experimental.prims import Articulation, GeomPrim, RigidPrim, XformPrim
  6from isaacsim.core.simulation_manager import SimulationManager
  7from isaacsim.examples.base.base_sample_experimental import BaseSample
  8from isaacsim.robot.experimental.manipulators.examples.franka import Franka
  9from isaacsim.storage.native import get_assets_root_path
 10
 11
 12class HelloWorld(BaseSample):
 13    def __init__(self) -> None:
 14        super().__init__()
 15        self._physics_callback_id = None
 16        self._state = 0
 17
 18    def setup_scene(self):
 19        assets_root_path = get_assets_root_path()
 20
 21        # Add ground plane
 22        stage_utils.add_reference_to_stage(
 23            usd_path=assets_root_path + "/Isaac/Environments/Grid/default_environment.usd",
 24            path="/World/ground",
 25        )
 26
 27        # Add Jetbot at origin
 28        stage_utils.add_reference_to_stage(
 29            usd_path=assets_root_path + "/Isaac/Robots/NVIDIA/Jetbot/jetbot.usd",
 30            path="/World/Jetbot",
 31        )
 32
 33        # Add cube in front of Jetbot
 34        visual_material = PreviewSurfaceMaterial("/World/Materials/blue")
 35        visual_material.set_input_values("diffuseColor", [0.0, 0.0, 1.0])
 36        cube_shape = Cube(
 37            paths="/World/Cube",
 38            positions=np.array([[0.15, 0.0, 0.0258]]),
 39            sizes=[1.0],
 40            scales=np.array([[0.05, 0.05, 0.05]]),
 41            reset_xform_op_properties=True,
 42        )
 43        GeomPrim(paths=cube_shape.paths, apply_collision_apis=True)
 44        RigidPrim(paths=cube_shape.paths)
 45        cube_shape.apply_visual_materials(visual_material)
 46
 47        # Add Franka using Franka for IK and gripper control
 48        self._franka = Franka(robot_path="/World/Franka", create_robot=True)
 49        franka_xform = XformPrim("/World/Franka")
 50        franka_xform.set_world_poses(positions=[[0.8, -0.3, 0.0]])
 51
 52    async def setup_post_load(self):
 53        self._jetbot = Articulation("/World/Jetbot")
 54        self._cube = RigidPrim("/World/Cube")
 55        self._cube_goal = np.array([1.2, 0.0, 0.0])  # Target: Franka reaches from the side
 56        self._step_counter = 0
 57        self._pick_phase = 0
 58
 59        from isaacsim.core.simulation_manager.impl.isaac_events import IsaacEvents
 60
 61        self._physics_callback_id = SimulationManager.register_callback(
 62            self.physics_step, IsaacEvents.POST_PHYSICS_STEP
 63        )
 64        self._state = 0
 65
 66    def physics_step(self, dt, context):
 67        # -- Begin state machine -- #
 68        if self._state == 0:
 69            # Jetbot pushes cube to Franka
 70            cube_pos = self._cube.get_world_poses()[0].numpy()[0]
 71            if np.linalg.norm(cube_pos[:2] - self._cube_goal[:2]) > 0.05:
 72                self._jetbot.set_dof_velocity_targets([[10.0, 10.0]])
 73            else:
 74                self._jetbot.set_dof_velocity_targets([[0.0, 0.0]])
 75                print("Cube delivered! Backing up...")
 76                self._state = 1
 77                self._step_counter = 0
 78
 79        elif self._state == 1:
 80            # Jetbot backs up
 81            self._jetbot.set_dof_velocity_targets([[-8.0, -8.0]])
 82            self._step_counter += 1
 83            if self._step_counter > 100:
 84                self._jetbot.set_dof_velocity_targets(np.array([[0.0, 0.0]]))
 85                print("Franka starting pick-and-place...")
 86                self._state = 2
 87                self._step_counter = 0
 88                self._franka.open_gripper()
 89
 90        elif self._state == 2:
 91            # Franka pick-and-place sequence using step counter
 92            cube_pos = self._cube.get_world_poses()[0].numpy()[0]
 93            down_orient = self._franka.get_downward_orientation()
 94            self._step_counter += 1
 95
 96            if self._pick_phase == 0:
 97                # Move above cube (wait 120 steps)
 98                self._franka.set_end_effector_pose(
 99                    np.array([[cube_pos[0], cube_pos[1], cube_pos[2] + 0.2]]), down_orient
100                )
101                if self._step_counter > 120:
102                    self._pick_phase = 1
103                    self._step_counter = 0
104            elif self._pick_phase == 1:
105                # Lower to cube (wait 100 steps)
106                self._franka.set_end_effector_pose(
107                    np.array([[cube_pos[0], cube_pos[1], cube_pos[2] + 0.1]]), down_orient
108                )
109                if self._step_counter > 100:
110                    self._franka.close_gripper()
111                    self._pick_phase = 2
112                    self._step_counter = 0
113            elif self._pick_phase == 2:
114                # Close the gripper (wait 50 steps)
115                self._franka.close_gripper()
116                if self._step_counter > 50:
117                    self._pick_phase = 3
118                    self._step_counter = 0
119            elif self._pick_phase == 3:
120                # Lift cube (wait 100 steps)
121                self._franka.set_end_effector_pose(
122                    np.array([[cube_pos[0], cube_pos[1], cube_pos[2] + 0.25]]), down_orient
123                )
124                if self._step_counter > 100:
125                    self._pick_phase = 4
126                    self._step_counter = 0
127            elif self._pick_phase == 4:
128                # Move to target (wait 150 steps)
129                self._franka.set_end_effector_pose(np.array([[0.3, 0.3, 0.15]]), down_orient)
130                if self._step_counter > 150:
131                    self._franka.open_gripper()
132                    self._pick_phase = 5
133                    self._step_counter = 0
134            elif self._pick_phase == 5:
135                # Lift the arm (wait 150 steps)
136                self._franka.set_end_effector_pose(
137                    np.array([[cube_pos[0], cube_pos[1], cube_pos[2] + 0.5]]), down_orient
138                )
139                if self._step_counter > 150:
140                    self._step_counter = 0
141        # -- End of state machine -- #
142
143    async def setup_post_reset(self):
144        self._state = 0
145        self._step_counter = 0
146        self._pick_phase = 0
147        self._franka.reset_to_default_pose()
148
149    def physics_cleanup(self):
150        if self._physics_callback_id is not None:
151            SimulationManager.deregister_callback(self._physics_callback_id)
152            self._physics_callback_id = None
```

## Summary

This tutorial covered the following topics:

1. Adding multiple robots and objects (cube) to the scene
2. Using `Cube`, `GeomPrim`, and `RigidPrim` to create pushable objects
3. Using the `Articulation` class to control different robot types
4. Having a mobile robot (Jetbot) push objects towards a manipulator (Franka)
5. Building state machine logic to coordinate pushing, backing up, and picking
6. Using `Franka` for IK-based end-effector control and gripper operations

### Next Steps

Continue on to the next tutorial in our Essential Tutorials series, [Multiple Robot Scenarios](tutorial_core_multiple_tasks.html#isaac-sim-app-tutorial-core-multiple-tasks),
to learn how to add multiple tasks and manage them.

On this page

* [Learning Objectives](#learning-objectives)
* [Getting Started](#getting-started)
* [Creating the Scene](#creating-the-scene)
* [Controlling Multiple Robots](#controlling-multiple-robots)
* [Adding State Machine Logic](#adding-state-machine-logic)
* [Summary](#summary)
  + [Next Steps](#next-steps)