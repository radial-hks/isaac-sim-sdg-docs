---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/core_api_tutorials/tutorial_core_multiple_tasks.html
title: "Multiple Tasks"
section: "Core API"
module: "02-fundamentals-dev"
checksum: "020ac7bebd1e9231"
fetched: "2026-06-21T14:14:21"
---

* [Python Scripting and Tutorials](../python_scripting/index.html)
* [Core API Tutorial Series](index.html)
* Multiple Robot Scenarios

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Multiple Robot Scenarios

## Learning Objectives

This tutorial describes how to create and manage multiple robot scenarios in NVIDIA Isaac Sim.
It explains how to use parameterization and Python classes to scale your simulations with
multiple instances of robots performing similar tasks. After this tutorial, you will have
more experience building scalable multi-robot simulations in NVIDIA Isaac Sim.

*15-20 Minute Tutorial*

## Getting Started

**Prerequisites**

* Review [Adding Multiple Robots](tutorial_core_adding_multiple_robots.html#isaac-sim-app-tutorial-core-adding-multiple-robots) prior to beginning this tutorial.

Begin with the source code open from the previous tutorial, [Adding Multiple Robots](tutorial_core_adding_multiple_robots.html#isaac-sim-app-tutorial-core-adding-multiple-robots).

Note

Pressing **STOP**, then **PLAY** in this workflow might not reset the world properly. Use
the **RESET** button instead.

## Organizing Robot Scenarios with Classes

When working with multiple robots performing similar tasks, it’s helpful to encapsulate the
robot setup and control logic into reusable classes. This approach allows you to easily
create multiple instances with different parameters (like position offsets).

Create a `RobotScenario` class that manages a Jetbot pushing a cube to a Franka:

```python
  1import isaacsim.core.experimental.utils.stage as stage_utils
  2import numpy as np
  3from isaacsim.core.experimental.objects import Cube, DomeLight, GroundPlane
  4from isaacsim.core.experimental.prims import Articulation, GeomPrim, RigidPrim, XformPrim
  5from isaacsim.core.simulation_manager import SimulationEvent, SimulationManager
  6from isaacsim.examples.base.base_sample_experimental import BaseSample
  7from isaacsim.robot.experimental.manipulators.examples.franka import Franka
  8from isaacsim.storage.native import get_assets_root_path
  9
 10
 11class RobotScenario:
 12    """Encapsulates a Jetbot + Franka + Cube scenario with an offset."""
 13
 14    def __init__(self, name: str, offset: np.ndarray = np.array([0.0, 0.0, 0.0])):
 15        self.name = name
 16        self.offset = offset
 17        self.state = 0
 18        self.step_counter = 0
 19        self.pick_phase = 0
 20        self.jetbot = None
 21        self.franka = None
 22        self.cube = None
 23        self.cube_goal = np.array([1.2, 0.0, 0.0]) + offset
 24
 25    def setup_scene(self):
 26        """Create the robots and cube for this scenario."""
 27        assets_root_path = get_assets_root_path()
 28        base_path = f"/World/{self.name}"
 29
 30        # Add Jetbot
 31        stage_utils.add_reference_to_stage(
 32            usd_path=assets_root_path + "/Isaac/Robots/NVIDIA/Jetbot/jetbot.usd",
 33            path=f"{base_path}/Jetbot",
 34        )
 35        jetbot_xform = XformPrim(f"{base_path}/Jetbot")
 36        jetbot_xform.reset_xform_op_properties()
 37        jetbot_xform.set_world_poses(positions=self.offset.tolist())
 38
 39        # Add cube in front of Jetbot
 40        cube_pos = self.offset + np.array([0.15, 0.0, 0.025])
 41        cube_shape = Cube(
 42            paths=f"{base_path}/Cube",
 43            positions=cube_pos.tolist(),
 44            sizes=1.0,
 45            scales=[0.05, 0.05, 0.05],
 46            colors="red",
 47        )
 48        GeomPrim(paths=cube_shape.paths, apply_collision_apis=True)
 49        RigidPrim(paths=cube_shape.paths)
 50
 51        # Add Franka
 52        franka_pos = self.offset + np.array([0.8, -0.3, 0.0])
 53        self.franka = Franka(robot_path=f"{base_path}/Franka", create_robot=True)
 54        franka_xform = XformPrim(f"{base_path}/Franka")
 55        franka_xform.reset_xform_op_properties()
 56        franka_xform.set_world_poses(positions=franka_pos.tolist())
 57
 58    def initialize(self):
 59        """Initialize articulation handles after scene load."""
 60        base_path = f"/World/{self.name}"
 61        self.jetbot = Articulation(f"{base_path}/Jetbot")
 62        self.cube = RigidPrim(f"{base_path}/Cube")
 63
 64    def reset(self):
 65        """Reset the scenario state."""
 66        self.state = 0
 67        self.step_counter = 0
 68        self.pick_phase = 0
 69        self.franka.reset_to_default_pose()
 70
 71    def step(self):
 72        """Execute one step of the scenario logic."""
 73        if self.state == 0:
 74            # Jetbot pushes cube
 75            cube_pos = self.cube.get_world_poses()[0].numpy()[0]
 76            if np.linalg.norm(cube_pos[:2] - self.cube_goal[:2]) > 0.05:
 77                self.jetbot.set_dof_velocity_targets([10.0, 10.0])
 78            else:
 79                self.jetbot.set_dof_velocity_targets([0.0, 0.0])
 80                self.state = 1
 81                self.step_counter = 0
 82
 83        elif self.state == 1:
 84            # Jetbot backs up
 85            self.jetbot.set_dof_velocity_targets([-8.0, -8.0])
 86            self.step_counter += 1
 87            if self.step_counter > 100:
 88                self.jetbot.set_dof_velocity_targets([0.0, 0.0])
 89                self.state = 2
 90                self.step_counter = 0
 91                self.franka.open_gripper()
 92
 93        elif self.state == 2:
 94            # Franka pick-and-place
 95            self._franka_pick_place()
 96
 97    def _franka_pick_place(self):
 98        """Execute Franka pick-and-place state machine."""
 99        cube_pos = self.cube.get_world_poses()[0].numpy()[0]
100        down_orient = self.franka.get_downward_orientation()
101        self.step_counter += 1
102
103        if self.pick_phase == 0:
104            self.franka.set_end_effector_pose(np.array([cube_pos[0], cube_pos[1], cube_pos[2] + 0.2]), down_orient)
105            if self.step_counter > 120:
106                self.pick_phase = 1
107                self.step_counter = 0
108        elif self.pick_phase == 1:
109            self.franka.set_end_effector_pose(np.array([cube_pos[0], cube_pos[1], cube_pos[2] + 0.1]), down_orient)
110            if self.step_counter > 100:
111                self.pick_phase = 2
112                self.step_counter = 0
113        elif self.pick_phase == 2:
114            self.franka.close_gripper()
115            if self.step_counter > 100:
116                self.pick_phase = 3
117                self.step_counter = 0
118        elif self.pick_phase == 3:
119            _, current_position, _ = self.franka.get_current_state()
120            target = current_position + np.array([0.1, 0.0, 0.08])
121            self.franka.set_end_effector_pose(position=target, orientation=down_orient)
122            if self.step_counter > 150:
123                self.step_counter = 0
124                self.pick_phase = 4
125        elif self.pick_phase == 4:
126            _, current_position, _ = self.franka.get_current_state()
127            target = current_position + np.array([0.1, 0.0, 0.01])
128            self.franka.set_end_effector_pose(position=target, orientation=down_orient)
129            if self.step_counter > 150:
130                self.step_counter = 0
131                self.pick_phase = 5
132        elif self.pick_phase == 5:
133            self.franka.open_gripper()
134            if self.step_counter > 150:
135                self.step_counter = 0
136                self.state = 6  # Done
137
138
139class HelloWorld(BaseSample):
140    def __init__(self) -> None:
141        super().__init__()
142        self._physics_callback_id = None
143        self._scenarios = []
144
145    def setup_scene(self):
146        GroundPlane("/World/ground_plane")
147        dome_light = DomeLight("/World/DomeLight")
148        dome_light.set_intensities(1000)
149
150        # Create a single scenario
151        self._scenario = RobotScenario(name="scenario_0", offset=np.array([0.0, 0.0, 0.0]))
152        self._scenario.setup_scene()
153
154    async def setup_post_load(self):
155        self._scenario.initialize()
156
157        self._physics_callback_id = SimulationManager.register_callback(
158            self.physics_step, event=SimulationEvent.PHYSICS_POST_STEP
159        )
160
161    def physics_step(self, dt, context):
162        self._scenario.step()
163
164    async def setup_post_reset(self):
165        self._scenario.reset()
166
167    def physics_cleanup(self):
168        if self._physics_callback_id is not None:
169            SimulationManager.deregister_callback(self._physics_callback_id)
170            self._physics_callback_id = None
```

## Scaling to Multiple Scenarios

Adding the following operations:

Set number of scenarios:

```python
1        self._num_scenarios = 3  # Number of parallel scenarios
```

Creating scenarios:

```python
1        # Create multiple scenarios with Y-axis offsets
2        for i in range(self._num_scenarios):
3            offset = np.array([0.0, (i - 1) * 2.0, 0.0])  # Spread along Y-axis
4            scenario = RobotScenario(name=f"scenario_{i}", offset=offset, randomize=False)
5            scenario.setup_scene()
6            self._scenarios.append(scenario)
```

Initializing scenarios:

```python
1        # Initialize all scenarios
2        for scenario in self._scenarios:
3            scenario.initialize()
```

Stepping all scenarios:

```python
1        # Step all scenarios
2        for scenario in self._scenarios:
3            scenario.step()
```

Resetting all scenarios:

```python
1        # Reset all scenarios
2        for scenario in self._scenarios:
3            scenario.reset()
```

Clean up:

```python
1        self._scenarios = []
```

Complete code:

```python
  1import isaacsim.core.experimental.utils.stage as stage_utils
  2import numpy as np
  3from isaacsim.core.experimental.objects import Cube, DomeLight, GroundPlane
  4from isaacsim.core.experimental.prims import Articulation, GeomPrim, RigidPrim, XformPrim
  5from isaacsim.core.simulation_manager import SimulationEvent, SimulationManager
  6from isaacsim.examples.base.base_sample_experimental import BaseSample
  7from isaacsim.robot.experimental.manipulators.examples.franka import Franka
  8from isaacsim.storage.native import get_assets_root_path
  9
 10
 11class RobotScenario:
 12    """Encapsulates a Jetbot + Franka + Cube scenario with an offset."""
 13
 14    def __init__(self, name: str, offset: np.ndarray = np.array([0.0, 0.0, 0.0]), randomize: bool = False):
 15        self.name = name
 16        self.offset = offset
 17        self.state = 0
 18        self.step_counter = 0
 19        self.randomize = randomize
 20        self.pick_phase = 0
 21        self.jetbot = None
 22        self.franka = None
 23        self.cube = None
 24        self.cube_goal = np.array([1.2, 0.0, 0.0]) + offset
 25
 26        # Randomize cube goal position if enabled
 27        if self.randomize:
 28            random_x = np.random.uniform(1.0, 1.6)
 29            self.cube_goal = np.array([random_x, 0.0, 0.0]) + offset
 30        else:
 31            self.cube_goal = np.array([1.2, 0.0, 0.0]) + offset
 32
 33    def setup_scene(self):
 34        """Create the robots and cube for this scenario."""
 35        assets_root_path = get_assets_root_path()
 36        base_path = f"/World/{self.name}"
 37
 38        # Add Jetbot
 39        stage_utils.add_reference_to_stage(
 40            usd_path=assets_root_path + "/Isaac/Robots/NVIDIA/Jetbot/jetbot.usd",
 41            path=f"{base_path}/Jetbot",
 42        )
 43        jetbot_xform = XformPrim(f"{base_path}/Jetbot")
 44        jetbot_xform.reset_xform_op_properties()
 45        jetbot_xform.set_world_poses(positions=self.offset.tolist())
 46
 47        # Add cube in front of Jetbot
 48        cube_pos = self.offset + np.array([0.15, 0.0, 0.025])
 49        cube_shape = Cube(
 50            paths=f"{base_path}/Cube",
 51            positions=cube_pos.tolist(),
 52            sizes=1.0,
 53            scales=[0.05, 0.05, 0.05],
 54            colors="red",
 55        )
 56        GeomPrim(paths=cube_shape.paths, apply_collision_apis=True)
 57        RigidPrim(paths=cube_shape.paths)
 58
 59        # Add Franka
 60        franka_pos = self.offset + np.array([0.8, -0.3, 0.0])
 61        self.franka = Franka(robot_path=f"{base_path}/Franka", create_robot=True)
 62        franka_xform = XformPrim(f"{base_path}/Franka")
 63        franka_xform.reset_xform_op_properties()
 64        franka_xform.set_world_poses(positions=franka_pos.tolist())
 65
 66    def initialize(self):
 67        """Initialize articulation handles after scene load."""
 68        base_path = f"/World/{self.name}"
 69        self.jetbot = Articulation(f"{base_path}/Jetbot")
 70        self.cube = RigidPrim(f"{base_path}/Cube")
 71
 72    def reset(self):
 73        """Reset the scenario state."""
 74        self.state = 0
 75        self.step_counter = 0
 76        self.pick_phase = 0
 77        self.franka.reset_to_default_pose()
 78
 79    def step(self):
 80        """Execute one step of the scenario logic."""
 81        if self.state == 0:
 82            # Jetbot pushes cube
 83            cube_pos = self.cube.get_world_poses()[0].numpy()[0]
 84            if np.linalg.norm(cube_pos[:2] - self.cube_goal[:2]) > 0.05:
 85                self.jetbot.set_dof_velocity_targets([10.0, 10.0])
 86            else:
 87                self.jetbot.set_dof_velocity_targets([0.0, 0.0])
 88                self.state = 1
 89                self.step_counter = 0
 90
 91        elif self.state == 1:
 92            # Jetbot backs up
 93            self.jetbot.set_dof_velocity_targets([-8.0, -8.0])
 94            self.step_counter += 1
 95            if self.step_counter > 100:
 96                self.jetbot.set_dof_velocity_targets([0.0, 0.0])
 97                self.state = 2
 98                self.step_counter = 0
 99                self.franka.open_gripper()
100
101        elif self.state == 2:
102            # Franka pick-and-place
103            self._franka_pick_place()
104
105    def _franka_pick_place(self):
106        """Execute Franka pick-and-place state machine."""
107        cube_pos = self.cube.get_world_poses()[0].numpy()[0]
108        down_orient = self.franka.get_downward_orientation()
109        self.step_counter += 1
110
111        if self.pick_phase == 0:
112            self.franka.set_end_effector_pose(np.array([cube_pos[0], cube_pos[1], cube_pos[2] + 0.2]), down_orient)
113            if self.step_counter > 120:
114                self.pick_phase = 1
115                self.step_counter = 0
116        elif self.pick_phase == 1:
117            self.franka.set_end_effector_pose(np.array([cube_pos[0], cube_pos[1], cube_pos[2] + 0.1]), down_orient)
118            if self.step_counter > 100:
119                self.pick_phase = 2
120                self.step_counter = 0
121        elif self.pick_phase == 2:
122            self.franka.close_gripper()
123            if self.step_counter > 100:
124                self.pick_phase = 3
125                self.step_counter = 0
126        elif self.pick_phase == 3:
127            _, current_position, _ = self.franka.get_current_state()
128            target = current_position + np.array([0.1, 0.0, 0.08])
129            self.franka.set_end_effector_pose(position=target, orientation=down_orient)
130            if self.step_counter > 150:
131                self.step_counter = 0
132                self.pick_phase = 4
133        elif self.pick_phase == 4:
134            _, current_position, _ = self.franka.get_current_state()
135            target = current_position + np.array([0.1, 0.0, 0.01])
136            self.franka.set_end_effector_pose(position=target, orientation=down_orient)
137            if self.step_counter > 150:
138                self.step_counter = 0
139                self.pick_phase = 5
140        elif self.pick_phase == 5:
141            self.franka.open_gripper()
142            if self.step_counter > 150:
143                self.step_counter = 0
144                self.state = 6  # Done
145
146
147class HelloWorld(BaseSample):
148    def __init__(self) -> None:
149        super().__init__()
150        self._physics_callback_id = None
151        self._scenarios = []
152        # -- Begin setting scenario number -- #
153        self._num_scenarios = 3  # Number of parallel scenarios
154        # -- End of setting scenario number -- #
155
156    def setup_scene(self):
157        GroundPlane("/World/ground_plane")
158        dome_light = DomeLight("/World/DomeLight")
159        dome_light.set_intensities(1000)
160
161        # -- Begin creating scenarios -- #
162        # Create multiple scenarios with Y-axis offsets
163        for i in range(self._num_scenarios):
164            offset = np.array([0.0, (i - 1) * 2.0, 0.0])  # Spread along Y-axis
165            scenario = RobotScenario(name=f"scenario_{i}", offset=offset, randomize=False)
166            scenario.setup_scene()
167            self._scenarios.append(scenario)
168        # -- End of creating scenarios -- #
169
170    async def setup_post_load(self):
171        # -- Begin initializing scenarios -- #
172        # Initialize all scenarios
173        for scenario in self._scenarios:
174            scenario.initialize()
175        # -- End of initializing scenarios -- #
176
177        self._physics_callback_id = SimulationManager.register_callback(
178            self.physics_step, event=SimulationEvent.PHYSICS_POST_STEP
179        )
180
181    def physics_step(self, dt, context):
182        # -- Begin stepping scenarios -- #
183        # Step all scenarios
184        for scenario in self._scenarios:
185            scenario.step()
186        # -- End of stepping scenarios -- #
187
188    async def setup_post_reset(self):
189        # -- Begin resetting scenarios -- #
190        # Reset all scenarios
191        for scenario in self._scenarios:
192            scenario.reset()
193        # -- End of resetting scenarios -- #
194
195    def physics_cleanup(self):
196        if self._physics_callback_id is not None:
197            SimulationManager.deregister_callback(self._physics_callback_id)
198            self._physics_callback_id = None
199        # -- Begin remove all scenarios -- #
200        self._scenarios = []
201        # -- End of remove all scenarios -- #
```

## Adding Randomization

To make simulations more interesting, you can add randomization to the scenario parameters.
In the `setup_scene` method above, set `randomize=True` when creating each scenario:

```python
1for i in range(self._num_scenarios):
2    offset = np.array([0.0, (i - 1) * 2.0, 0.0])  # Spread along Y-axis
3    scenario = RobotScenario(name=f"scenario_{i}", offset=offset, randomize=True)
4    scenario.setup_scene()
5    self._scenarios.append(scenario)
```

## Best Practices for Scaling

When creating large-scale multi-robot simulations:

1. **Use unique paths**: Each scenario should use unique USD prim paths to avoid conflicts.
   The `RobotScenario` class uses the scenario name to create unique paths like
   `/World/scenario_0/Jetbot`.
2. **Manage state independently**: Each scenario instance maintains its own state variables,
   allowing scenarios to progress independently.
3. **Clean up properly**: The `physics_cleanup` method ensures callbacks are deregistered
   and scenario lists are cleared when the simulation is stopped.
4. **Consider performance**: With many scenarios, consider reducing physics step frequency
   or using GPU-accelerated simulation for better performance.

## Summary

This tutorial covered the following topics:

1. Organizing robot scenarios into reusable Python classes
2. Using the `offset` parameter to position multiple scenarios in the world
3. Scaling to multiple parallel scenarios with a simple loop
4. Adding randomization to scenario parameters
5. Best practices for managing multiple robot instances

On this page

* [Learning Objectives](#learning-objectives)
* [Getting Started](#getting-started)
* [Organizing Robot Scenarios with Classes](#organizing-robot-scenarios-with-classes)
* [Scaling to Multiple Scenarios](#scaling-to-multiple-scenarios)
* [Adding Randomization](#adding-randomization)
* [Best Practices for Scaling](#best-practices-for-scaling)
* [Summary](#summary)