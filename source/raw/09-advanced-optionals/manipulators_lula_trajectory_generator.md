---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/manipulators/manipulators_lula_trajectory_generator.html
title: "Lula Trajectory Generator"
section: "Manipulators"
module: "09-advanced-optionals"
checksum: "f27f584c6a284594"
fetched: "2026-06-21T13:05:42"
---

* [Robot Simulation](../robot_simulation/index.html)
* [Motion Generation (Deprecated)](motion_generation_overview.html)
* Lula Trajectory Generator

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Lula Trajectory Generator

Deprecated

For new development, consider using the newer [Robot Motion (Experimental)](../robot_motion_experimental/index.html) API, which provides improved interfaces and additional features over Lula.

This tutorial explores how the [Lula Trajectory Generator](concepts/trajectory_interface.html#isaac-sim-lula-trajectory-generator) in the [Motion Generation](concepts/index.html#isaac-sim-motion-generation) extension can be used to create both task-space and c-space trajectories that can be easily applied to a simulated robot `Articulation`.

## Getting Started

**Prerequisites**

* Complete the [Adding a Manipulator Robot](../core_api_tutorials/tutorial_core_adding_manipulator.html#isaac-sim-app-tutorial-core-adding-manipulator) tutorial prior to beginning this tutorial.
* You can reference the [Lula Robot Description and XRDF Editor](manipulators_robot_description_editor.html#isaac-sim-app-tutorial-motion-generation-robot-description-editor) to understand how to generate your own `robot_description.yaml` file to be able to use the [Lula Trajectory Generator](concepts/trajectory_interface.html#isaac-sim-lula-trajectory-generator) on unsupported robots.
* Review the [Loaded Scenario Extension Template](../utilities/extension_templates_tutorial.html#isaac-sim-app-tutorial-extension-templates-loaded-scenario) to understand how this tutorial is structured and run.

To follow along with the tutorial, run your Isaac Sim 6.0 instance. Then open **Window > Extensions**, search for **Motion Generation Examples** (`isaacsim.robot_motion.motion_generation.examples`), and enable it. If you cannot find it, remove `@feature` from the Extensions search bar and search again.
Within the isaacsim.robot\_motion.motion\_generation.examples extension, there an example of the `LulaTaskSpaceTrajectorygenerator` and `LulaCSpaceTrajectoryGenerator` being used to generate trajectories
connecting specified c-space and task-space points.
The sections of this tutorial build up the file `scenario.py` from basic functionality to the completed code.

Note

**Motion Generation Examples** (`isaacsim.robot_motion.motion_generation.examples`) are deprecated **since Isaac Sim 6.0.0**. In the Isaac Sim source repository they live under `source/deprecated/isaacsim.robot_motion.motion_generation.examples`; the extension id is unchanged.

**Replacement:** Use the `isaacsim.robot_motion.cumotion.examples` extension and the [cuMotion Integration](../cumotion/index.html) tutorials.

## Generating a C-Space Trajectory

The `LulaCSpaceTrajectoryGenerator` class is able to generate a trajectory that connects a provided set of c-space waypoints.
The code snippet below demonstrates how, given appropriate config files,
the `LulaCSpaceTrajectoryGenerator` class can be initialized and used to create a sequence
of `ArticulationAction` that can be set on each frame to produce the desired trajectory.

The code snippet below shows the relevant contents of `/Trajectory_Generator_python/scenario.py` from the provided example.

```python
  1import os
  2
  3import carb
  4import lula
  5import numpy as np
  6from isaacsim.core.api.objects.cuboid import FixedCuboid
  7from isaacsim.core.prims import SingleArticulation as Articulation
  8from isaacsim.core.prims import SingleXFormPrim as XFormPrim
  9from isaacsim.core.utils.extensions import get_extension_path_from_name
 10from isaacsim.core.utils.numpy.rotations import rot_matrices_to_quats
 11from isaacsim.core.utils.prims import delete_prim, get_prim_at_path
 12from isaacsim.core.utils.stage import add_reference_to_stage
 13from isaacsim.robot_motion.motion_generation import (
 14    ArticulationTrajectory,
 15    LulaCSpaceTrajectoryGenerator,
 16    LulaKinematicsSolver,
 17    LulaTaskSpaceTrajectoryGenerator,
 18)
 19from isaacsim.storage.native import get_assets_root_path
 20
 21
 22class UR10TrajectoryGenerationExample:
 23    def __init__(self):
 24        self._c_space_trajectory_generator = None
 25        self._taskspace_trajectory_generator = None
 26        self._kinematics_solver = None
 27
 28        self._action_sequence = []
 29        self._action_sequence_index = 0
 30
 31        self._articulation = None
 32
 33    def load_example_assets(self):
 34        # Add the Franka and target to the stage
 35        # The position in which things are loaded is also the position in which they
 36
 37        robot_prim_path = "/ur10"
 38        path_to_robot_usd = get_assets_root_path() + "/Isaac/Robots/UniversalRobots/ur10/ur10.usd"
 39
 40        add_reference_to_stage(path_to_robot_usd, robot_prim_path)
 41        self._articulation = Articulation(robot_prim_path)
 42
 43        # Return assets that were added to the stage so that they can be registered with the core.World
 44        return [self._articulation]
 45
 46    def setup(self):
 47        # Config files for supported robots are stored in the motion_generation extension under "/motion_policy_configs"
 48        mg_extension_path = get_extension_path_from_name("isaacsim.robot_motion.motion_generation")
 49        rmp_config_dir = os.path.join(mg_extension_path, "motion_policy_configs")
 50
 51        # -- Begin LulaCSpaceTrajectoryGenerator -- #
 52        # Initialize a LulaCSpaceTrajectoryGenerator object
 53        self._c_space_trajectory_generator = LulaCSpaceTrajectoryGenerator(
 54            robot_description_path=rmp_config_dir + "/universal_robots/ur10/rmpflow/ur10_robot_description.yaml",
 55            urdf_path=rmp_config_dir + "/universal_robots/ur10/ur10_robot.urdf",
 56        )
 57        # -- End of LulaCSpaceTrajectoryGenerator -- #
 58
 59        self._taskspace_trajectory_generator = LulaTaskSpaceTrajectoryGenerator(
 60            robot_description_path=rmp_config_dir + "/universal_robots/ur10/rmpflow/ur10_robot_description.yaml",
 61            urdf_path=rmp_config_dir + "/universal_robots/ur10/ur10_robot.urdf",
 62        )
 63
 64        self._kinematics_solver = LulaKinematicsSolver(
 65            robot_description_path=rmp_config_dir + "/universal_robots/ur10/rmpflow/ur10_robot_description.yaml",
 66            urdf_path=rmp_config_dir + "/universal_robots/ur10/ur10_robot.urdf",
 67        )
 68
 69        self._end_effector_name = "ee_link"
 70
 71    def setup_cspace_trajectory(self):
 72        c_space_points = np.array(
 73            [
 74                [
 75                    -0.41,
 76                    0.5,
 77                    -2.36,
 78                    -1.28,
 79                    5.13,
 80                    -4.71,
 81                ],
 82                [
 83                    -1.43,
 84                    1.0,
 85                    -2.58,
 86                    -1.53,
 87                    6.0,
 88                    -4.74,
 89                ],
 90                [
 91                    -2.83,
 92                    0.34,
 93                    -2.11,
 94                    -1.38,
 95                    1.26,
 96                    -4.71,
 97                ],
 98                [
 99                    -0.41,
100                    0.5,
101                    -2.36,
102                    -1.28,
103                    5.13,
104                    -4.71,
105                ],
106            ]
107        )
108
109        # -- Begin time optimal -- #
110        trajectory_time_optimal = self._c_space_trajectory_generator.compute_c_space_trajectory(c_space_points)
111        # -- End of time optimal -- #
112        # -- Begin time stamped -- #
113        timestamps = np.array([0, 5, 10, 13])
114        trajectory_timestamped = self._c_space_trajectory_generator.compute_timestamped_c_space_trajectory(
115            c_space_points, timestamps
116        )
117        # -- End of time stamped -- #
118
119        # -- Begin visualization -- #
120        # Visualize c-space targets in task space
121        for i, point in enumerate(c_space_points):
122            position, rotation = self._kinematics_solver.compute_forward_kinematics(self._end_effector_name, point)
123            add_reference_to_stage(
124                get_assets_root_path() + "/Isaac/Props/UIElements/frame_prim.usd", f"/visualized_frames/target_{i}"
125            )
126            frame = XFormPrim(f"/visualized_frames/target_{i}", scale=[0.04, 0.04, 0.04])
127            frame.set_world_pose(position, rot_matrices_to_quats(rotation))
128        # -- End of visualization -- #
129
130        # -- Begin no trajectory handling -- #
131        if trajectory_time_optimal is None or trajectory_timestamped is None:
132            carb.log_warn("No trajectory could be computed")
133            self._action_sequence = []
134        # -- End of no trajectory handling -- #
135        else:
136            physics_dt = 1 / 60
137            self._action_sequence = []
138
139            # -- Begin trajectory following -- #
140            # Follow both trajectories in a row
141            articulation_trajectory_time_optimal = ArticulationTrajectory(
142                self._articulation, trajectory_time_optimal, physics_dt
143            )
144            self._action_sequence.extend(articulation_trajectory_time_optimal.get_action_sequence())
145
146            articulation_trajectory_timestamped = ArticulationTrajectory(
147                self._articulation, trajectory_timestamped, physics_dt
148            )
149            self._action_sequence.extend(articulation_trajectory_timestamped.get_action_sequence())
150            # -- End of trajectory following -- #
151
152    def update(self, step: float):
153        if len(self._action_sequence) == 0:
154            return
155
156        if self._action_sequence_index >= len(self._action_sequence):
157            self._action_sequence_index += 1
158            self._action_sequence_index %= (
159                len(self._action_sequence) + 10
160            )  # Wait 10 frames before repeating trajectories
161            return
162
163        if self._action_sequence_index == 0:
164            self._teleport_robot_to_position(self._action_sequence[0])
165
166        self._articulation.apply_action(self._action_sequence[self._action_sequence_index])
167
168        self._action_sequence_index += 1
169        self._action_sequence_index %= len(self._action_sequence) + 10  # Wait 10 frames before repeating trajectories
170
171    def reset(self):
172        # Delete any visualized frames
173        if get_prim_at_path("/visualized_frames"):
174            delete_prim("/visualized_frames")
175
176        self._action_sequence = []
177        self._action_sequence_index = 0
178
179    def _teleport_robot_to_position(self, articulation_action):
180        initial_positions = np.zeros(self._articulation.num_dof)
181        initial_positions[articulation_action.joint_indices] = articulation_action.joint_positions
182
183        self._articulation.set_joint_positions(initial_positions)
184        self._articulation.set_joint_velocities(np.zeros_like(initial_positions))
```

The `LulaCSpaceTrajectoryGenerator` class is initialized using a URDF and
[Lula Robot Description File](manipulators_robot_description_editor.html#isaac-sim-app-tutorial-motion-generation-robot-description-editor):

```python
1        # Initialize a LulaCSpaceTrajectoryGenerator object
2        self._c_space_trajectory_generator = LulaCSpaceTrajectoryGenerator(
3            robot_description_path=rmp_config_dir + "/universal_robots/ur10/rmpflow/ur10_robot_description.yaml",
4            urdf_path=rmp_config_dir + "/universal_robots/ur10/ur10_robot.urdf",
5        )
```

The `LulaCSpaceTrajectoryGenerator` takes in a series of waypoints, and it connects them in configuration space using spline-based interpolation.
There are two main objectives that can be fulfilled by the trajectory generator:

* time-optimal
* time-stamped

The provided example shows a trajectory that runs quickly, and then runs slowly.

A time-optimal trajectory is created in the form of a `LulaTrajectory` object, which fulfills the [Trajectory Interface](concepts/trajectory_interface.html#isaac-sim-trajectory):

```python
1        trajectory_time_optimal = self._c_space_trajectory_generator.compute_c_space_trajectory(c_space_points)
```

Next, a time-stamped trajectory is created that will hit the same waypoints at the times `[0,5,10,13]` seconds. Time optimality is
defined as saturating at least one of velocity, acceleration, or jerk limits of the robot throughout a trajectory:

```python
1        timestamps = np.array([0, 5, 10, 13])
2        trajectory_timestamped = self._c_space_trajectory_generator.compute_timestamped_c_space_trajectory(
3            c_space_points, timestamps
4        )
```

These `LulaTrajectory` objects are passed to `ArticulationTrajectory` to generate a sequence of `ArticulationAction` that can be passed directly to the
robot `Articulation`. The function `ArticulationTrajectory.get_action_sequence()` returns a list of `ArticulationAction` that is meant to be consumed at the specified
rate. In this case, the framerate of physics is assumed to be fixed at `1/60` seconds:

```python
 1            # Follow both trajectories in a row
 2            articulation_trajectory_time_optimal = ArticulationTrajectory(
 3                self._articulation, trajectory_time_optimal, physics_dt
 4            )
 5            self._action_sequence.extend(articulation_trajectory_time_optimal.get_action_sequence())
 6
 7            articulation_trajectory_timestamped = ArticulationTrajectory(
 8                self._articulation, trajectory_timestamped, physics_dt
 9            )
10            self._action_sequence.extend(articulation_trajectory_timestamped.get_action_sequence())
```

If no trajectory can be computed that connects the c-space waypoints, the trajectory returned by `LulaCSpaceTrajectoryGenerator.compute_c_space_trajectory`
will be `None`. This can occur when one of the specified c-space waypoints is not reachable or is very close to a joint limit:

```python
1        if trajectory_time_optimal is None or trajectory_timestamped is None:
2            carb.log_warn("No trajectory could be computed")
3            self._action_sequence = []
```

A visualization of the original `c_space_points` is created by converting them to task-space points.
This code is not functional, but it helps to verify that the robot is hitting every target:

```python
1        # Visualize c-space targets in task space
2        for i, point in enumerate(c_space_points):
3            position, rotation = self._kinematics_solver.compute_forward_kinematics(self._end_effector_name, point)
4            add_reference_to_stage(
5                get_assets_root_path() + "/Isaac/Props/UIElements/frame_prim.usd", f"/visualized_frames/target_{i}"
6            )
7            frame = XFormPrim(f"/visualized_frames/target_{i}", scale=[0.04, 0.04, 0.04])
8            frame.set_world_pose(position, rot_matrices_to_quats(rotation))
```

The `update()` function is programmed to play the sequence of `ArticulationActions` in a loop, taking a pause of `10 frames` for dramatic effect between trajectories.

## Generating a Task-Space Trajectory

### Simple Case: Linearly Connecting Waypoints

Generating a task-space trajectory is similar to generating a c-space trajectory.
In the simplest use-case, you can pass in a set of task-space position and quaternion orientation targets,
which will be linearly interpolated in task-space to produce the resulting trajectory.
An example is provided in the code snippet below:

```python
class UR10TrajectoryGenerationExample:
    def __init__(self):
        self._c_space_trajectory_generator = None
        self._taskspace_trajectory_generator = None
        self._kinematics_solver = None

        self._action_sequence = []
        self._action_sequence_index = 0

        self._articulation = None

    def load_example_assets(self):
        # Add the Franka and target to the stage
        # The position in which things are loaded is also the position in which they

        robot_prim_path = "/ur10"
        path_to_robot_usd = get_assets_root_path() + "/Isaac/Robots/UniversalRobots/ur10/ur10.usd"

        add_reference_to_stage(path_to_robot_usd, robot_prim_path)
        self._articulation = Articulation(robot_prim_path)

        # Return assets that were added to the stage so that they can be registered with the core.World
        return [self._articulation]

    def setup(self):
        # Config files for supported robots are stored in the motion_generation extension under "/motion_policy_configs"
        mg_extension_path = get_extension_path_from_name("isaacsim.robot_motion.motion_generation")
        rmp_config_dir = os.path.join(mg_extension_path, "motion_policy_configs")

        # Initialize a LulaCSpaceTrajectoryGenerator object
        self._c_space_trajectory_generator = LulaCSpaceTrajectoryGenerator(
            robot_description_path=rmp_config_dir + "/universal_robots/ur10/rmpflow/ur10_robot_description.yaml",
            urdf_path=rmp_config_dir + "/universal_robots/ur10/ur10_robot.urdf",
        )

        self._taskspace_trajectory_generator = LulaTaskSpaceTrajectoryGenerator(
            robot_description_path=rmp_config_dir + "/universal_robots/ur10/rmpflow/ur10_robot_description.yaml",
            urdf_path=rmp_config_dir + "/universal_robots/ur10/ur10_robot.urdf",
        )

        self._kinematics_solver = LulaKinematicsSolver(
            robot_description_path=rmp_config_dir + "/universal_robots/ur10/rmpflow/ur10_robot_description.yaml",
            urdf_path=rmp_config_dir + "/universal_robots/ur10/ur10_robot.urdf",
        )

        self._end_effector_name = "ee_link"

    def setup_taskspace_trajectory(self):
        task_space_position_targets = np.array(
            [[0.3, -0.3, 0.1], [0.3, 0.3, 0.1], [0.3, 0.3, 0.5], [0.3, -0.3, 0.5], [0.3, -0.3, 0.1]]
        )

        task_space_orientation_targets = np.tile(np.array([0, 1, 0, 0]), (5, 1))

        trajectory = self._taskspace_trajectory_generator.compute_task_space_trajectory_from_points(
            task_space_position_targets, task_space_orientation_targets, self._end_effector_name
        )

        # Visualize task-space targets in task space
        for i, (position, orientation) in enumerate(zip(task_space_position_targets, task_space_orientation_targets)):
            add_reference_to_stage(
                get_assets_root_path() + "/Isaac/Props/UIElements/frame_prim.usd", f"/visualized_frames/target_{i}"
            )
            frame = XFormPrim(f"/visualized_frames/target_{i}", scale=[0.04, 0.04, 0.04])
            frame.set_world_pose(position, orientation)

        if trajectory is None:
            carb.log_warn("No trajectory could be computed")
            self._action_sequence = []
        else:
            physics_dt = 1 / 60
            articulation_trajectory = ArticulationTrajectory(self._articulation, trajectory, physics_dt)

            # Get a sequence of ArticulationActions that are intended to be passed to the robot at 1/60 second intervals
            self._action_sequence = articulation_trajectory.get_action_sequence()

    def update(self, step: float):
        if len(self._action_sequence) == 0:
            return

        if self._action_sequence_index >= len(self._action_sequence):
            self._action_sequence_index += 1
            self._action_sequence_index %= (
                len(self._action_sequence) + 10
            )  # Wait 10 frames before repeating trajectories
            return

        if self._action_sequence_index == 0:
            self._teleport_robot_to_position(self._action_sequence[0])

        self._articulation.apply_action(self._action_sequence[self._action_sequence_index])

        self._action_sequence_index += 1
        self._action_sequence_index %= len(self._action_sequence) + 10  # Wait 10 frames before repeating trajectories

    def reset(self):
        # Delete any visualized frames
        if get_prim_at_path("/visualized_frames"):
            delete_prim("/visualized_frames")

        self._action_sequence = []
        self._action_sequence_index = 0

    def _teleport_robot_to_position(self, articulation_action):
        initial_positions = np.zeros(self._articulation.num_dof)
        initial_positions[articulation_action.joint_indices] = articulation_action.joint_positions

        self._articulation.set_joint_positions(initial_positions)
        self._articulation.set_joint_velocities(np.zeros_like(initial_positions))
```

In moving to the task-space trajectory generator, there are few code changes required. The initialization is nearly the same on line 36 as for the
c-space trajectory generator. The main changes are on lines 59-61 where a task-space trajectory is specified. When using the function
`LulaTaskSpaceTrajectoryGenerator.compute_task_space_trajectory_from_points`, a position and orientation target must be specified for each task-space waypoint.
Additionally, a frame from the robot URDF must be specified as the end effector frame.
If the waypoints cannot be connected to form a trajectory, the `compute_task_space_trajectory_from_points` function will return `None`.
This case is checked on line 69.

### Defining Complicated Trajectories

The `LulaTaskSpaceTrajectoryGenerator` can be used to create paths with more complicated specifications than to connect a set of task-space targets linearly.
Using the class `lula.TaskSpacePathSpec`, you can define paths with arcs and circles with multiple options for orientation targets.
The code snippet below demonstrates creating a `lula.TaskSpacePathSpec` and gives an example of each available function for adding to a task-space path.
Additionally, it shows how a `lula.TaskSpacePathSpec` can be combined with a `lula.CSpacePathSpec` in a `lula.CompositePathSpec` to specify trajectories
that contain both c-space and task-space waypoints.

```python
class UR10TrajectoryGenerationExample:
    def __init__(self):
        self._c_space_trajectory_generator = None
        self._taskspace_trajectory_generator = None
        self._kinematics_solver = None

        self._action_sequence = []
        self._action_sequence_index = 0

        self._articulation = None

    def load_example_assets(self):
        # Add the Franka and target to the stage
        # The position in which things are loaded is also the position in which they

        robot_prim_path = "/ur10"
        path_to_robot_usd = get_assets_root_path() + "/Isaac/Robots/UniversalRobots/ur10/ur10.usd"

        add_reference_to_stage(path_to_robot_usd, robot_prim_path)
        self._articulation = Articulation(robot_prim_path)

        # Return assets that were added to the stage so that they can be registered with the core.World
        return [self._articulation]

    def setup(self):
        # Config files for supported robots are stored in the motion_generation extension under "/motion_policy_configs"
        mg_extension_path = get_extension_path_from_name("isaacsim.robot_motion.motion_generation")
        rmp_config_dir = os.path.join(mg_extension_path, "motion_policy_configs")

        # Initialize a LulaCSpaceTrajectoryGenerator object
        self._c_space_trajectory_generator = LulaCSpaceTrajectoryGenerator(
            robot_description_path=rmp_config_dir + "/universal_robots/ur10/rmpflow/ur10_robot_description.yaml",
            urdf_path=rmp_config_dir + "/universal_robots/ur10/ur10_robot.urdf",
        )

        self._taskspace_trajectory_generator = LulaTaskSpaceTrajectoryGenerator(
            robot_description_path=rmp_config_dir + "/universal_robots/ur10/rmpflow/ur10_robot_description.yaml",
            urdf_path=rmp_config_dir + "/universal_robots/ur10/ur10_robot.urdf",
        )

        self._kinematics_solver = LulaKinematicsSolver(
            robot_description_path=rmp_config_dir + "/universal_robots/ur10/rmpflow/ur10_robot_description.yaml",
            urdf_path=rmp_config_dir + "/universal_robots/ur10/ur10_robot.urdf",
        )

        self._end_effector_name = "ee_link"

    def setup_advanced_trajectory(self):
        # The following code demonstrates how to specify a complicated cspace and taskspace path
        # using the lula.CompositePathSpec object

        initial_c_space_robot_pose = np.array([0, 0, 0, 0, 0, 0])

        # Combine a cspace and taskspace trajectory
        composite_path_spec = lula.create_composite_path_spec(initial_c_space_robot_pose)

        #############################################################################
        # Demonstrate all the available movements in a taskspace path spec:

        # Lula has its own classes for Rotations and 6 DOF poses: Rotation3 and Pose3
        r0 = lula.Rotation3(np.pi / 2, np.array([1.0, 0.0, 0.0]))
        t0 = np.array([0.3, -0.1, 0.3])
        task_space_spec = lula.create_task_space_path_spec(lula.Pose3(r0, t0))

        # Add path linearly interpolating between r0,r1 and t0,t1
        t1 = np.array([0.3, -0.1, 0.5])
        r1 = lula.Rotation3(np.pi / 3, np.array([1, 0, 0]))
        task_space_spec.add_linear_path(lula.Pose3(r1, t1))

        # Add pure translation.  Constant rotation is assumed
        task_space_spec.add_translation(t0)

        # Add pure rotation.
        task_space_spec.add_rotation(r0)

        # Add three-point arc with constant orientation.
        t2 = np.array(
            [
                0.3,
                0.3,
                0.3,
            ]
        )
        midpoint = np.array([0.3, 0, 0.5])
        task_space_spec.add_three_point_arc(t2, midpoint, constant_orientation=True)

        # Add three-point arc with tangent orientation.
        task_space_spec.add_three_point_arc(t0, midpoint, constant_orientation=False)

        # Add three-point arc with orientation target.
        task_space_spec.add_three_point_arc_with_orientation_target(lula.Pose3(r1, t2), midpoint)

        # Add tangent arc with constant orientation. Tangent arcs are circles that connect two points
        task_space_spec.add_tangent_arc(t0, constant_orientation=True)

        # Add tangent arc with tangent orientation.
        task_space_spec.add_tangent_arc(t2, constant_orientation=False)

        # Add tangent arc with orientation target.
        task_space_spec.add_tangent_arc_with_orientation_target(lula.Pose3(r0, t0))

        ###################################################
        # Demonstrate the usage of a c_space path spec:
        c_space_spec = lula.create_c_space_path_spec(np.array([0, 0, 0, 0, 0, 0]))

        c_space_spec.add_c_space_waypoint(np.array([0, 0.5, -2.0, -1.28, 5.13, -4.71]))

        ##############################################################
        # Combine the two path specs together into a composite spec:

        # specify how to connect initial_c_space and task_space points with transition_mode option
        transition_mode = lula.CompositePathSpec.TransitionMode.FREE
        composite_path_spec.add_task_space_path_spec(task_space_spec, transition_mode)

        transition_mode = lula.CompositePathSpec.TransitionMode.FREE
        composite_path_spec.add_c_space_path_spec(c_space_spec, transition_mode)

        # Transition Modes:
        # lula.CompositePathSpec.TransitionMode.LINEAR_TASK_SPACE:
        #      Connect cspace to taskspace points linearly through task space.  This mode is only available when adding a task_space path spec.
        # lula.CompositePathSpec.TransitionMode.FREE:
        #      Put no constraints on how cspace and taskspace points are connected
        # lula.CompositePathSpec.TransitionMode.SKIP:
        #      Skip the first point of the path spec being added, using the last pose instead

        trajectory = self._taskspace_trajectory_generator.compute_task_space_trajectory_from_path_spec(
            composite_path_spec, self._end_effector_name
        )

        if trajectory is None:
            carb.log_warn("No trajectory could be computed")
            self._action_sequence = []
        else:
            physics_dt = 1 / 60
            articulation_trajectory = ArticulationTrajectory(self._articulation, trajectory, physics_dt)

            # Get a sequence of ArticulationActions that are intended to be passed to the robot at 1/60 second intervals
            self._action_sequence = articulation_trajectory.get_action_sequence()

    def update(self, step: float):
        if len(self._action_sequence) == 0:
            return

        if self._action_sequence_index >= len(self._action_sequence):
            self._action_sequence_index += 1
            self._action_sequence_index %= (
                len(self._action_sequence) + 10
            )  # Wait 10 frames before repeating trajectories
            return

        if self._action_sequence_index == 0:
            self._teleport_robot_to_position(self._action_sequence[0])

        self._articulation.apply_action(self._action_sequence[self._action_sequence_index])

        self._action_sequence_index += 1
        self._action_sequence_index %= len(self._action_sequence) + 10  # Wait 10 frames before repeating trajectories

    def reset(self):
        # Delete any visualized frames
        if get_prim_at_path("/visualized_frames"):
            delete_prim("/visualized_frames")

        self._action_sequence = []
        self._action_sequence_index = 0

    def _teleport_robot_to_position(self, articulation_action):
        initial_positions = np.zeros(self._articulation.num_dof)
        initial_positions[articulation_action.joint_indices] = articulation_action.joint_positions

        self._articulation.set_joint_positions(initial_positions)
        self._articulation.set_joint_velocities(np.zeros_like(initial_positions))
```

The code snippet above creates a `lula.CompositePathSpec` on line 55 with an initial c-space position. It is combined with a
`lula.TaskSpacePathSpec` on lines 108-109 and it is combined with a `lula.CSpacePathSpec` on lines 111-112. The resulting path
is one that starts at the specified `initial_c_space_robot_pose`, then follows a series of taskspace targets, then hits two c-space
targets. When combining path specs, a transition mode must be specified to determine how c-space and task-space points should be connected
to each other. Reference lines 114-120 to see the possible options. In this case, no constraint is made on how the `LulaTrajectoryGenerator`
connects these points.

Each available option for specifying a `lula.TaskSpacePathSpec` is demonstrated between lines 63-94.
The code snippet above moves mainly between three translations: `t0, t1, t2` with possible rotations `r0, r1`.
The `lula.TaskSpacePathSpec` object is created with an initial position on line 63.
Each following `add` function that is called adds a path between the last position in the `path_spec` so far and a new position.
The basic possibilities are:

> 1. Linearly interpolate translation to a new point while keeping rotation fixed (line 71)
> 2. Linearly interpolate rotation to a new point while keeping translation fixed (line 74)
> 3. Linearly interpolate both rotation and translation to a new 6 DOF point (line 68)

The `lula.TaskSpacePathSpec` also makes it easy to define various arcs and circular paths that connect points in space.
A three-point arc can be defined that moves through a midpoint to a translation target.
There are three options for the orientation of the robot while moving along the path:

> 1. Keep rotation constant (line 79)
> 2. Always stay oriented tangent to the arc (line 82)
> 3. Linearly interpolate rotation to a rotation target (line 85)

Finally, a circular path can be specified without defining a midpoint as on lines 88, 91, and 94.
The same three options for specifying orientation are available.

## Summary

This tutorial shows how to use the [Lula Trajectory Generator](concepts/trajectory_interface.html#isaac-sim-lula-trajectory-generator) to generate c-space and task-space trajectories for a robot. Task-space trajectories can be specified using a series of task-space waypoints that will be connected linearly, or they can be defined piecewise with many different options for connecting each pair of points in space.

### Further Learning

Reference the [Motion Generation](concepts/index.html#isaac-sim-motion-generation) page for a complete description of trajectories in NVIDIA Isaac Sim.

On this page

* [Getting Started](#getting-started)
* [Generating a C-Space Trajectory](#generating-a-c-space-trajectory)
* [Generating a Task-Space Trajectory](#generating-a-task-space-trajectory)
  + [Simple Case: Linearly Connecting Waypoints](#simple-case-linearly-connecting-waypoints)
  + [Defining Complicated Trajectories](#defining-complicated-trajectories)
* [Summary](#summary)
  + [Further Learning](#further-learning)