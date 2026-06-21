---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/robot_setup_tutorials/tutorial_pickplace_example.html
title: "Pick-Place Example"
section: "Setup 教程"
module: "07-robot-setup"
checksum: "316678f8e3034606"
fetched: "2026-06-21T13:05:36"
---

* [Robot Setup](../robot_setup/index.html)
* [Robot Setup Tutorials Series](index.html)
* Tutorial 9: Pick and Place Example

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Tutorial 9: Pick and Place Example

## Learning Objectives

This is the final manipulator tutorial in a series of four tutorials. It ties everything together by showing how to use the UR10e robot and the 2F-140 gripper to control the gripper, follow a Cartesian target, and perform a pick-and-place sequence.
We will be using the robot imported in [Tutorial 6: Setup a Manipulator](tutorial_import_assemble_manipulator.html) and the URDF and XRDF robot configuration files described in [Robot Configuration Tutorial](../cumotion/tutorial_robot_configuration.html#isaac-sim-cumotion-tutorial-robot-configuration).

This tutorial builds on top of the [Robot Motion (Experimental)](../robot_motion_experimental/index.html#isaac-sim-robot-motion-experimental) extension and demonstrates two motion controllers:

* **cuMotion RMPflow** â a GPU-accelerated reactive motion planner with collision avoidance. See the [cuMotion Integration](../cumotion/index.html#isaac-sim-cumotion) overview and the [RMPflow Tutorial](../cumotion/tutorial_rmpflow.html#isaac-sim-cumotion-tutorial-rmpflow) for full details.
* **PINK differential IK** â a CPU-based inverse kinematics solver using the [PINK](https://github.com/stephane-caron/pink) library. See the [PINK Integration](../pink/index.html#isaac-sim-pink) overview and the [IK Controller Tutorial](../pink/tutorial_ik_controller.html#isaac-sim-pink-tutorial-ik-controller) for full details.

*30 Minutes Tutorial*

## Prerequisites

* Review [Tutorial 6: Setup a Manipulator](tutorial_import_assemble_manipulator.html) and [Tutorial 7: Configure a Manipulator](tutorial_configure_manipulator.html) prior to beginning this tutorial to generate robot and the URDF and XRDF files required by the pick-and-place examples.

Note

If you have not completed the previous tutorial(s), you can find the prebuilt asset in the content browser at `Isaac Sim/Samples/Rigging/Manipulator/configure_manipulator/ur10e/ur/ur_gripper.usd`.

Additionally, pre-generated URDF, XRDF, and `rmp_flow.yaml` files can be found at `source/extensions/isaacsim.robot_motion.cumotion/robot_configurations/ur10/`.

## Overview

This tutorial is divided into four parts, each corresponding to a standalone example script:

| Part | Script | Description |
| --- | --- | --- |
| 1 | `tutorial_9_gripper_control.py` | Gripper control using the Articulation API |
| 2 | `tutorial_9_arm_trajectory.py` | Joint-space trajectory planning and execution |
| 3 | `tutorial_9_follow_target.py` | Real-time Cartesian target following with cuMotion RMPflow |
| 4 | `tutorial_9_pick_place_cumotion.py` / `tutorial_9_pick_place_pink.py` | Full pick-and-place sequence with cuMotion RMPflow or PINK differential IK |

All scripts are located at `standalone_examples/tutorials/manipulation/`.

## Part 1: Gripper Control

This example introduces the Articulation API by controlling the 2F-140 gripper joints directly with `set_dof_position_targets`. The gripper closes fully and then opens again.

```python
./python.sh standalone_examples/tutorials/manipulation/tutorial_9_gripper_control.py
```

**Key concepts:**

* `Articulation.dof_names` returns the list of all degrees of freedom in order. The gripper joint is named `finger_joint`.
* `set_dof_position_targets` sends a position target to one or more DOFs by index. Passing `dof_indices` restricts the command to only those joints.

tutorial\_9\_gripper\_control.py â gripper control loop

```python
    finger_idx = robot.dof_names.index("finger_joint")
    frame_count = 0

    while app.is_running():
        for target_pos, label in [(_CLOSED_POS, "closing"), (_OPEN_POS, "opening")]:
            print(f"Gripper {label}...")
            for _ in range(_HOLD_STEPS):
                robot.set_dof_position_targets(target_pos, dof_indices=finger_idx)
                app.update()
                frame_count += 1
                if args.test and frame_count >= _HOLD_STEPS * 2:
                    return
```

## Part 2: Arm Trajectory Following

This example plans and executes a joint-space trajectory using `mg.Path` and `mg.TrajectoryFollower` from the motion generation API. The robot follows a sequence of waypoints in minimal time subject to velocity and acceleration limits.

```python
./python.sh standalone_examples/tutorials/manipulation/tutorial_9_arm_trajectory.py
```

**Key concepts:**

* `mg.Path(waypoints)` wraps a sequence of joint-space configurations.
* `.to_minimal_time_joint_trajectory(max_velocities, max_accelerations, ...)` computes a time-optimal trajectory that respects joint limits.
* `mg.TrajectoryFollower` tracks the planned trajectory, calling `.forward(estimated_state, setpoint, t)` each physics step to obtain the desired joint state.
* `get_estimated_state` packages the current joint positions, velocities, and efforts into an `mg.RobotState`.
* `apply_desired_state` applies the position, velocity, and effort targets from the desired state back to the articulation.

tutorial\_9\_arm\_trajectory.py â trajectory setup

```python
    waypoints = np.array(
        [
            [0.00, -1.57, 1.57, -1.57, -1.57, 0.00],  # home
            [0.50, -1.00, 0.80, -1.30, -1.57, 0.00],  # reach-out
            [0.00, -1.57, 1.57, -1.57, -1.57, 0.00],  # back to home
        ],
    )

    max_velocities = np.array([1.0, 1.0, 1.0, 1.0, 1.0, 1.0])
    max_accelerations = np.array([0.5, 0.5, 0.5, 0.5, 0.5, 0.5])

    trajectory = mg.Path(waypoints).to_minimal_time_joint_trajectory(
        max_velocities=max_velocities,
        max_accelerations=max_accelerations,
        robot_joint_space=robot_joint_space,
        active_joints=arm_joints,
    )
    print(f"Trajectory duration: {trajectory.duration:.2f} s")

    follower = mg.TrajectoryFollower()
    follower.set_trajectory(trajectory)

    simulation_time = 0.0
    if not follower.reset(get_estimated_state(robot, robot_joint_space), None, simulation_time):
        raise RuntimeError("Failed to reset TrajectoryFollower")
```

tutorial\_9\_arm\_trajectory.py â trajectory execution loop

```python
    dt = SimulationManager.get_physics_dt()
    max_steps = int((trajectory.duration + 1.0) / dt)
    frame_count = 0

    while app.is_running():
        app.update()
        if not (app_utils.is_playing() and SimulationManager.is_simulating()):
            continue
        simulation_time = 0.0
        follower.reset(get_estimated_state(robot, robot_joint_space), None, simulation_time)
        for _ in range(max_steps):
            app.update()
            if not (app_utils.is_playing() and SimulationManager.is_simulating()):
                break
            simulation_time += dt
            desired_state = follower.forward(get_estimated_state(robot, robot_joint_space), None, simulation_time)
            if desired_state is None:
                print("Trajectory complete.")
                break
            apply_desired_state(robot, desired_state)
            frame_count += 1
            if args.test and frame_count >= 100:
                return
```

See also

* [Trajectory Planning and Execution](../motion_generation/trajectory_planning.html) â the `mg.Path` and `mg.TrajectoryFollower` API used in this part.
* [cuMotion Trajectory Generator Tutorial](../cumotion/tutorial_trajectory_generator.html#isaac-sim-cumotion-tutorial-trajectory-generator) â generating collision-aware trajectories with cuMotion.

## Part 3: Follow Target using cuMotion RMPflow

This example shows how to use the cuMotion `RmpFlowController` to make the robot track a draggable target cube in real time, with optional obstacle avoidance.

```python
./python.sh standalone_examples/tutorials/manipulation/tutorial_9_follow_target.py
```

To enable obstacle avoidance, pass `--with-obstacle`:

```python
./python.sh standalone_examples/tutorials/manipulation/tutorial_9_follow_target.py --with-obstacle
```

**Key concepts:**

* `load_cumotion_supported_robot("ur10")` loads the built-in cuMotion robot model for the UR10, which includes the kinematic chain and collision spheres.
* `mg.WorldBinding` connects the cuMotion world interface to the Isaac Sim stage. It uses `mg.SceneQuery` to find collision objects in the scene and registers them as obstacles.
* `RmpFlowController` is initialized with the robot model, world interface, joint space, and tool frame. It accepts an estimated robot state and a Cartesian setpoint each step, and returns desired joint positions.
* `create_setpoint_state` packages a target position and orientation into an `mg.RobotState` that the controller can track.
* `world_binding.synchronize_transforms()` must be called each step to update obstacle transforms before planning.

tutorial\_9\_follow\_target.py â scene and controller setup

```python
async def setup_scene_and_controller(
    with_obstacle: bool,
) -> tuple[RmpFlowController, CumotionRobot, Articulation, mg.WorldBinding, GeomPrim]:
    assets_root_path = await get_assets_root_path_async()
    stage_utils.add_reference_to_stage(
        usd_path=assets_root_path + "/Isaac/Samples/Rigging/Manipulator/configure_manipulator/ur10e/ur/ur_gripper.usd",
        path=_ROBOT_PRIM_PATH,
    )

    GroundPlane("/World/GroundPlane")
    DomeLight("/World/DomeLight").set_intensities(1000)

    target_cube = Cube(paths=_TARGET_PATH, positions=[[0.35, 0.25, 0.3]], sizes=1.0, scales=[0.05, 0.05, 0.05])
    target_object = GeomPrim(paths=target_cube.paths)

    await omni.kit.app.get_app().next_update_async()
    set_camera_view(eye=[1.5, 1.5, 1.0], target=[0.5, 0.0, 0.2], camera_prim_path="/OmniverseKit_Persp")

    articulation = Articulation(_ROBOT_PRIM_PATH)
    await omni.kit.app.get_app().next_update_async()

    if with_obstacle:
        Cube("/World/obstacle", sizes=0.05, positions=[0.35, 0.0, 0.55], colors=(1.0, 0.0, 0.0))
        GeomPrim("/World/obstacle", apply_collision_apis=True)

    robot_pos, robot_ori = articulation.get_world_poses()
    objects = mg.SceneQuery().get_prims_in_aabb(
        search_box_origin=robot_pos.numpy()[0],
        search_box_minimum=[-10.0, -10.0, -10.0],
        search_box_maximum=[10.0, 10.0, 10.0],
        tracked_api=mg.TrackableApi.PHYSICS_COLLISION,
        exclude_prim_paths=[_ROBOT_PRIM_PATH, _TARGET_PATH],
    )

    obstacle_strategy = mg.ObstacleStrategy()
    for prim_type in (Mesh, Cone, Cylinder, Cube):
        obstacle_strategy.set_default_configuration(prim_type, mg.ObstacleConfiguration("obb", 0.05))

    world_binding = mg.WorldBinding(
        world_interface=CumotionWorldInterface(),
        obstacle_strategy=obstacle_strategy,
        tracked_prims=objects,
        tracked_collision_api=mg.TrackableApi.PHYSICS_COLLISION,
    )
    world_binding.initialize()
    world_binding.get_world_interface().update_world_to_robot_root_transforms(poses=(robot_pos, robot_ori))
    world_binding.synchronize_transforms()

    if args.xrdf_dir is not None:
        cumotion_robot = load_cumotion_robot(
            directory=args.xrdf_dir,
            urdf_filename=args.urdf,
            xrdf_filename=args.xrdf,
        )
    else:
        cumotion_robot = load_cumotion_supported_robot("ur10")
    site_space = cumotion_robot.robot_description.tool_frame_names()
    controller = RmpFlowController(
        cumotion_robot=cumotion_robot,
        cumotion_world_interface=world_binding.get_world_interface(),
        robot_joint_space=articulation.dof_names,
        robot_site_space=site_space,
        tool_frame=site_space[0],
    )
    controller.get_rmp_flow_config().set_param("cspace_target_rmp/metric_scalar", 1.0)
    controller.get_rmp_flow_config().set_param("collision_rmp/metric_scalar", 10000.0)

    return controller, cumotion_robot, articulation, world_binding, target_object
```

tutorial\_9\_follow\_target.py â per-step control loop

```python
def run_step(
    controller: RmpFlowController,
    cumotion_robot: CumotionRobot,
    articulation: Articulation,
    world_binding: mg.WorldBinding,
    target_object: GeomPrim,
    t: float,
) -> None:
    world_binding.get_world_interface().update_world_to_robot_root_transforms(articulation.get_world_poses())
    world_binding.synchronize_transforms()

    estimated = get_estimated_state(articulation)
    setpoint = create_setpoint_state(cumotion_robot, target_object)
    desired = controller.forward(estimated, setpoint, t)

    if desired is not None and desired.joints.positions is not None:
        articulation.set_dof_position_targets(
            positions=desired.joints.positions,
            dof_indices=desired.joints.position_indices,
        )
```

See also

* [cuMotion RMPflow Tutorial](../cumotion/tutorial_rmpflow.html#isaac-sim-cumotion-tutorial-rmpflow) â in-depth walkthrough of `RmpFlowController` configuration and tuning.
* [cuMotion World Interface Tutorial](../cumotion/tutorial_world_interface.html#isaac-sim-cumotion-tutorial-world-interface) â details on `CumotionWorldInterface`, `SceneQuery`, and `WorldBinding`.
* [Scene Interaction](../motion_generation/scene_interaction.html) â the underlying Motion Generation API for discovering and synchronizing obstacles from the USD scene.

## Part 4: Pick and Place

This example puts it all together by implementing a pick-and-place sequence. Two example scripts are provided: one using cuMotion RMPflow and one using PINK differential IK.

### cuMotion RMPflow

Important

cuMotion requires a `tool_frames` entry in the XRDF. See [Adding a Tool to the Robot Configuration](tutorial_generate_robot_config.html#isaac-sim-app-tutorial-generate-robot-config-adding-tool).

```python
./python.sh standalone_examples/tutorials/manipulation/tutorial_9_pick_place_cumotion.py \
    --xrdf-dir /path/to/robot/config
```

Note

`--xrdf-dir` should point to the directory containing the robot URDF and XRDF files made in the previous tutorial. `--urdf` and `--xrdf` select the filenames within that directory and default to `robot.urdf` and `robot.xrdf`, respectively.

If no `--xrdf-dir` is provided, `load_cumotion_supported_robot("ur10")` will be used to load the built-in UR10 robot configuration.

**Key concepts:**

* `--xrdf-dir` (optional) points to the directory containing custom robot config files. `load_cumotion_robot` loads the URDF and XRDF from that directory using the filenames given by `--urdf` and `--xrdf`. If omitted, the built-in UR10 configuration is used via `load_cumotion_supported_robot("ur10")`.
* `RmpFlowController.get_rmp_flow_config().set_param(key, value)` allows tuning RMPflow parameters at runtime. For this example, `cspace_target_rmp/metric_scalar` is reduced to 1.0 to reduce the influence of the initial position error on the motion planning.
* `controller.reset(estimated_state, setpoint, t)` must be called at the start of each arm motion segment to re-initialize the planner from the current robot state.

tutorial\_9\_pick\_place\_cumotion.py â UR10ePickPlace state machine class

```python
class UR10ePickPlace:
    """Pick-and-place controller for the UR10e + 2F-140 gripper using cuMotion RMPflow.

    Phases:
        0  Pre-grasp  â arm moves above the cube
        1  Approach   â arm descends to grasp height
        2  Grasp      â gripper closes
        3  Lift       â arm rises with the cube
        4  Transport  â arm moves above the target location
        5  Lower      â arm descends to place height
        6  Release    â gripper opens
        7  Retract    â arm lifts away
    """

    _ROBOT_PRIM_PATH = "/World/ur10e_robot"
    _CUBE_PRIM_PATH = "/World/cube"
    _EE_LINK_NAME = "right_inner_finger"
    _GRIPPER_JOINT = "finger_joint"

    _OPEN_POS: float = 0.0
    _CLOSED_POS: float = 0.5

    _ABOVE_HEIGHT: float = 0.50
    _NEAR_HEIGHT: float = 0.185
    _TOOL_OFFSET: dict[str, float] = {
        "tool0": 0.0,
        "wrist_3_link": 0.04,
    }
    _EE_THRESHOLD: float = 0.02
    _GRIPPER_THRESHOLD: float = 0.04
    _MIN_STEPS: int = 60
    _WARMUP_FRAMES: int = 120
    _PHYSICS_DT: float = 1.0 / 60.0

    _DOWN_ORI: np.ndarray = transform_utils.euler_angles_to_quaternion(np.array([0.0, np.pi, 0.0])).numpy()

    _PHASE_LABELS: tuple[str, ...] = (
        "Pre-grasp: moving above cube",
        "Approach: descending to cube",
        "Grasp: closing gripper",
        "Lift: raising arm",
        "Transport: moving to target",
        "Lower: descending to place",
        "Release: opening gripper",
        "Retract: lifting arm away",
    )

    def __init__(
        self,
        xrdf_dir: str | None = None,
        urdf_filename: str = "robot.urdf",
        xrdf_filename: str = "robot.xrdf",
        cube_position: np.ndarray | None = None,
        target_position: np.ndarray | None = None,
        events_dt: list[int] | None = None,
    ) -> None:
        self._xrdf_dir = xrdf_dir
        self._urdf_filename = urdf_filename
        self._xrdf_filename = xrdf_filename

        self.cube_position = cube_position if cube_position is not None else np.array([0.5, 0.0, 0.025])
        self.target_position = target_position if target_position is not None else np.array([0.5, 0.5, 0.05])
        self.events_dt = events_dt or [250, 150, 100, 50, 150, 100, 100, 100]

        self._event: int = 0
        self._step: int = 0
        self._t: float = 0.0
        self._warmup_remaining: int = self._WARMUP_FRAMES

        self._articulation: Articulation | None = None
        self._ee_prim: GeomPrim | None = None
        self._finger_idx: int | None = None
        self._cumotion_robot: CumotionRobot | None = None
        self._controller: RmpFlowController | None = None
        self._world_binding: mg.WorldBinding | None = None
        self._tool_frame: str | None = None
        self._site_space: list[str] | None = None

    async def setup_scene(self) -> None:
        """Build the scene and initialize the RMPflow controller."""
        assets_root_path = await get_assets_root_path_async()
        stage_utils.add_reference_to_stage(
            usd_path=assets_root_path
            + "/Isaac/Samples/Rigging/Manipulator/configure_manipulator/ur10e/ur/ur_gripper.usd",
            path=self._ROBOT_PRIM_PATH,
        )

        GroundPlane("/World/GroundPlane")
        DomeLight("/World/DomeLight").set_intensities(1000)

        cube_obj = Cube(
            paths=self._CUBE_PRIM_PATH, positions=[self.cube_position], sizes=1.0, scales=[0.05, 0.05, 0.05]
        )
        RigidPrim(paths=cube_obj.paths)
        GeomPrim(paths=cube_obj.paths, apply_collision_apis=True)

        await omni.kit.app.get_app().next_update_async()
        set_camera_view(eye=[1.5, 1.5, 1.0], target=[0.5, 0.0, 0.2], camera_prim_path="/OmniverseKit_Persp")

        self._articulation = Articulation(self._ROBOT_PRIM_PATH)
        await omni.kit.app.get_app().next_update_async()

        robot_pos, robot_ori = self._articulation.get_world_poses()
        objects = mg.SceneQuery().get_prims_in_aabb(
            search_box_origin=robot_pos.numpy()[0],
            search_box_minimum=[-10.0, -10.0, -10.0],
            search_box_maximum=[10.0, 10.0, 10.0],
            tracked_api=mg.TrackableApi.PHYSICS_COLLISION,
            exclude_prim_paths=[self._ROBOT_PRIM_PATH, self._CUBE_PRIM_PATH],
        )

        obstacle_strategy = mg.ObstacleStrategy()
        for prim_type in (Mesh, Cone, Cylinder):
            obstacle_strategy.set_default_configuration(prim_type, mg.ObstacleConfiguration("obb", 0.01))

        self._world_binding = mg.WorldBinding(
            world_interface=CumotionWorldInterface(),
            obstacle_strategy=obstacle_strategy,
            tracked_prims=objects,
            tracked_collision_api=mg.TrackableApi.PHYSICS_COLLISION,
        )
        self._world_binding.initialize()
        self._world_binding.get_world_interface().update_world_to_robot_root_transforms(poses=(robot_pos, robot_ori))
        self._world_binding.synchronize_transforms()

        if self._xrdf_dir is not None:
            self._cumotion_robot = load_cumotion_robot(
                directory=self._xrdf_dir,
                urdf_filename=self._urdf_filename,
                xrdf_filename=self._xrdf_filename,
            )
        else:
            self._cumotion_robot = load_cumotion_supported_robot("ur10")
        tool_frames = self._cumotion_robot.robot_description.tool_frame_names()
        if len(tool_frames) == 0:
            raise ValueError("No tool frames found in the robot description.")
        self._tool_frame = tool_frames[0]
        if self._tool_frame not in self._TOOL_OFFSET:
            raise ValueError(
                f"Tool frame '{self._tool_frame}' has no entry in _TOOL_OFFSET. "
                f"Add it: {list(self._TOOL_OFFSET.keys())}"
            )
        self._site_space = tool_frames

        self._controller = RmpFlowController(
            cumotion_robot=self._cumotion_robot,
            cumotion_world_interface=self._world_binding.get_world_interface(),
            robot_joint_space=self._articulation.dof_names,
            robot_site_space=self._site_space,
            tool_frame=self._tool_frame,
        )
        cfg = self._controller.get_rmp_flow_config()
        # cspace_target_rmp weights delta error from initial position
        # doesn't really matter in our case so decrease from default 50 to 1.0
        cfg.set_param("cspace_target_rmp/metric_scalar", 1.0)

    def initialize_after_play(self) -> None:
        """Resolve EE link and gripper DOF index. Call once after physics starts."""
        link_names = self._articulation.link_names
        if self._EE_LINK_NAME in link_names:
            self._ee_prim = GeomPrim(paths=self._articulation.link_paths[0][link_names.index(self._EE_LINK_NAME)])
        else:
            print(f"WARNING: '{self._EE_LINK_NAME}' not found. Available: {link_names}")

        dof_names = self._articulation.dof_names
        if self._GRIPPER_JOINT in dof_names:
            self._finger_idx = dof_names.index(self._GRIPPER_JOINT)
        else:
            print(f"WARNING: '{self._GRIPPER_JOINT}' not found. Available: {dof_names}")

        n_dofs = len(dof_names)
        init_pos = np.zeros(n_dofs)
        self._articulation.set_dof_positions(init_pos.tolist())
        self._articulation.set_dof_position_targets(init_pos.tolist())

    def _phase_ee_target(self) -> np.ndarray:
        c, p = self.cube_position, self.target_position
        offset = self._TOOL_OFFSET[self._tool_frame]
        hi = self._ABOVE_HEIGHT + offset
        lo = self._NEAR_HEIGHT + offset
        targets = {
            0: [c[0], c[1], c[2] + hi],
            1: [c[0], c[1], c[2] + lo],
            2: [c[0], c[1], c[2] + lo],
            3: [c[0], c[1], c[2] + hi],
            4: [p[0], p[1], p[2] + hi],
            5: [p[0], p[1], p[2] + lo],
            6: [p[0], p[1], p[2] + lo],
            7: [p[0], p[1], p[2] + hi],
        }
        return np.array(targets[self._event], dtype=np.float32)

    def _make_setpoint(self, position: np.ndarray) -> mg.RobotState:
        return mg.RobotState(
            sites=mg.SpatialState.from_name(
                spatial_space=self._site_space,
                positions=([self._tool_frame], wp.array([position.tolist()], dtype=wp.float32)),
                orientations=([self._tool_frame], wp.array([self._DOWN_ORI.tolist()], dtype=wp.float32)),
            ),
        )

    def _estimated_state(self) -> mg.RobotState:
        names = self._articulation.dof_names
        return mg.RobotState(
            joints=mg.JointState.from_name(
                robot_joint_space=names,
                positions=(names, self._articulation.get_dof_positions()),
                velocities=(names, self._articulation.get_dof_velocities()),
            )
        )

    def _set_gripper(self, pos: float) -> None:
        if self._finger_idx is not None:
            self._articulation.set_dof_position_targets(
                wp.array([pos], dtype=wp.float32), dof_indices=[self._finger_idx]
            )

    def _ee_near_target(self) -> bool:
        if self._ee_prim is None:
            return False
        ee_pos = self._ee_prim.get_world_poses()[0].numpy()[0]
        return bool(np.linalg.norm(ee_pos - self._phase_ee_target()) < self._EE_THRESHOLD)

    def _gripper_at(self, target: float) -> bool:
        if self._finger_idx is None:
            return False
        pos = float(self._articulation.get_dof_positions().numpy().flatten()[self._finger_idx])
        return abs(pos - target) < self._GRIPPER_THRESHOLD

    def _phase_converged(self) -> bool:
        if self._step < self._MIN_STEPS:
            return False
        if self._event == 2:
            return self._gripper_at(self._CLOSED_POS)
        if self._event == 6:
            return self._gripper_at(self._OPEN_POS)
        return self._ee_near_target()

    def forward(self) -> bool:
        """Advance one simulation step. Returns False when the sequence is complete."""
        if self.is_done():
            return False

        if self._warmup_remaining > 0:
            n_dofs = len(self._articulation.dof_names)
            targets = np.zeros(n_dofs)
            self._articulation.set_dof_position_targets(
                wp.array(targets, dtype=wp.float32), dof_indices=list(range(n_dofs))
            )
            self._warmup_remaining -= 1
            if np.abs(self._articulation.get_dof_positions().numpy().flatten() - targets).max() < 0.1:
                self._warmup_remaining = 0
            return True

        if self._step == 0:
            print(f"  Phase {self._event}: {self._PHASE_LABELS[self._event]}")
            if self._event in (0, 3, 7):
                if not self._controller.reset(
                    self._estimated_state(), self._make_setpoint(self._phase_ee_target()), t=0.0
                ):
                    raise RuntimeError("RmpFlowController reset failed.")
                self._t = 0.0

        if self._event == 2:
            self._set_gripper(self._CLOSED_POS)
        elif self._event == 6:
            self._set_gripper(self._OPEN_POS)
        else:
            self._world_binding.get_world_interface().update_world_to_robot_root_transforms(
                self._articulation.get_world_poses()
            )
            self._world_binding.synchronize_transforms()
            desired = self._controller.forward(
                self._estimated_state(), self._make_setpoint(self._phase_ee_target()), self._t
            )
            if desired is not None and desired.joints.positions is not None:
                self._articulation.set_dof_position_targets(
                    positions=desired.joints.positions, dof_indices=desired.joints.position_indices
                )

        self._t += self._PHYSICS_DT
        self._step += 1
        if self._phase_converged() or self._step >= self.events_dt[self._event]:
            if self._step >= self.events_dt[self._event]:
                print(f"  Phase {self._event} timed out after {self.events_dt[self._event]} frames")
            self._event += 1
            self._step = 0

        return True

    def is_done(self) -> bool:
        return self._event >= len(self.events_dt)

    def reset(self) -> None:
        self._event = 0
        self._step = 0
        self._t = 0.0
        self._warmup_remaining = self._WARMUP_FRAMES
```

See also

* [cuMotion Integration](../cumotion/index.html#isaac-sim-cumotion) â overview of the [cuMotion](https://nvidia-isaac.github.io/cumotion/) integration and its components.
* [cuMotion Robot Configuration Tutorial](../cumotion/tutorial_robot_configuration.html#isaac-sim-cumotion-tutorial-robot-configuration) â generating the URDF and XRDF files used by `--xrdf-dir`, including `tool_frames`.
* [cuMotion RMPflow Tutorial](../cumotion/tutorial_rmpflow.html#isaac-sim-cumotion-tutorial-rmpflow) â full tutorial on `RmpFlowController`, including parameter tuning via `get_rmp_flow_config().set_param`.

### PINK Differential IK

This example demonstrates an alternative motion controller: **PINK differential IK**. The same pick-and-place sequence is implemented using the `PinkIKController`, which solves inverse kinematics using [PINK](https://github.com/stephane-caron/pink) and [Pinocchio](https://github.com/stack-of-tasks/pinocchio).

Run this example with:

```python
# Load the built-in PINK robot model for the UR10
./python.sh standalone_examples/tutorials/manipulation/tutorial_9_pick_place_pink.py
# Load a custom URDF
./python.sh standalone_examples/tutorials/manipulation/tutorial_9_pick_place_pink.py --urdf <path_to_urdf>
```

**Key concepts:**

* `load_pink_supported_robot("ur10")` loads the built-in PINK robot model for the UR10, backed by a Pinocchio model. Alternatively, a custom URDF can be loaded using `load_pink_robot` by passing in `--urdf <path_to_urdf>`.
* `PinkIKController` accepts a tool frame name, position and orientation costs, a posture cost, and a QP solver (`"osqp"`). It integrates Cartesian velocity commands into joint positions each step.
* `_init_pink_q0` sets `pink_robot.q0` to the elbow-up configuration. PINKâs PostureTask regularizes the IK solution toward this reference, steering the solver away from elbow-down or degenerate configurations.

tutorial\_9\_pick\_place\_pink.py â UR10ePickPlace state machine class

```python
class UR10ePickPlace:
    """Pick-and-place controller for the UR10e + 2F-140 gripper using PINK differential IK.

    Phases:
        0  Pre-grasp  â arm moves above the cube
        1  Approach   â arm descends to grasp height
        2  Grasp      â gripper closes
        3  Lift       â arm rises with the cube
        4  Transport  â arm moves above the target location
        5  Lower      â arm descends to place height
        6  Release    â gripper opens
        7  Retract    â arm lifts away
    """

    _ROBOT_PRIM_PATH = "/World/ur10e_robot"
    _CUBE_PRIM_PATH = "/World/cube"
    _EE_LINK_NAME = "tool0" if args.urdf is None else "wrist_3_link"
    _GRIPPER_JOINT = "finger_joint"
    _TOOL_FRAME = "tool0" if args.urdf is None else "wrist_3_link"

    _OPEN_POS: float = 0.0
    _CLOSED_POS: float = 0.5

    _ABOVE_HEIGHT: float = 0.30
    _NEAR_HEIGHT: float = 0.185
    _TOOL_OFFSET: dict[str, float] = {
        "tool0": 0.0,
        "wrist_3_link": 0.035,
    }
    _EE_THRESHOLD: float = 0.05
    _GRIPPER_THRESHOLD: float = 0.05
    _MIN_STEPS: int = 30
    _WARMUP_FRAMES: int = 120
    _PHYSICS_DT: float = 1.0 / 60.0

    _POSITION_COST: float = 0.5
    _ORIENTATION_COST: float = 1.0
    _POSTURE_COST: float = 1e-3

    _ELBOW_UP_ARM: np.ndarray = np.array([-np.pi, -np.pi / 2, -np.pi / 2, -np.pi / 2, np.pi / 2, 0.0])
    _DOWN_ORI: np.ndarray = np.array([0.0, 0.0, 1.0, 0.0])

    _PHASE_LABELS: tuple[str, ...] = (
        "Pre-grasp: moving above cube",
        "Approach: descending to cube",
        "Grasp: closing gripper",
        "Lift: raising arm",
        "Transport: moving to target",
        "Lower: descending to place",
        "Release: opening gripper",
        "Retract: lifting arm away",
    )

    def __init__(
        self,
        urdf_path: str | None = None,
        cube_position: np.ndarray | None = None,
        target_position: np.ndarray | None = None,
        events_dt: list[int] | None = None,
    ) -> None:
        self._urdf_path = urdf_path
        self.cube_position = cube_position if cube_position is not None else np.array([0.5, 0.0, 0.025])
        self.target_position = target_position if target_position is not None else np.array([0.5, 0.5, 0.05])
        self.events_dt = events_dt or [80, 80, 20, 40, 130, 40, 20, 40]

        self._event: int = 0
        self._step: int = 0
        self._t: float = 0.0
        self._warmup_remaining: int = self._WARMUP_FRAMES

        self._articulation: Articulation | None = None
        self._ee_prim: GeomPrim | None = None
        self._finger_idx: int | None = None
        self._pink_robot: PinkRobot | None = None
        self._controller: PinkIKController | None = None
        self._tool_frame: str | None = None

    async def setup_scene(self) -> None:
        """Build the scene and initialize the PINK IK controller."""
        assets_root_path = await get_assets_root_path_async()
        stage_utils.add_reference_to_stage(
            usd_path=assets_root_path
            + "/Isaac/Samples/Rigging/Manipulator/configure_manipulator/ur10e/ur/ur_gripper.usd",
            path=self._ROBOT_PRIM_PATH,
        )

        GroundPlane("/World/GroundPlane")
        DomeLight("/World/DomeLight").set_intensities(1000)

        cube_obj = Cube(
            paths=self._CUBE_PRIM_PATH, positions=[self.cube_position], sizes=1.0, scales=[0.05, 0.05, 0.05]
        )
        RigidPrim(paths=cube_obj.paths)
        GeomPrim(paths=cube_obj.paths, apply_collision_apis=True)

        await omni.kit.app.get_app().next_update_async()
        set_camera_view(eye=[1.5, 1.5, 1.0], target=[0.5, 0.0, 0.2], camera_prim_path="/OmniverseKit_Persp")

        self._articulation = Articulation(self._ROBOT_PRIM_PATH)
        await omni.kit.app.get_app().next_update_async()

        n_dofs = len(self._articulation.dof_names)
        self._articulation.set_default_state(
            dof_positions=np.concatenate([self._ELBOW_UP_ARM, np.zeros(max(0, n_dofs - 6))])
        )

        if self._urdf_path is not None:
            self._pink_robot = load_pink_robot(urdf_path=self._urdf_path)
        else:
            self._pink_robot = load_pink_supported_robot("ur10")
        if self._TOOL_FRAME not in self._TOOL_OFFSET:
            raise ValueError(
                f"Tool frame '{self._TOOL_FRAME}' has no entry in _TOOL_OFFSET. "
                f"Add it: {list(self._TOOL_OFFSET.keys())}"
            )
        self._init_pink_q0()

        self._controller = PinkIKController(
            pink_robot=self._pink_robot,
            robot_joint_space=self._articulation.dof_names,
            robot_site_space=[self._TOOL_FRAME],
            tool_frame=self._TOOL_FRAME,
            position_cost=self._POSITION_COST,
            orientation_cost=self._ORIENTATION_COST,
            posture_cost=self._POSTURE_COST,
            solver="osqp",
            dt=self._PHYSICS_DT,
        )

    def initialize_after_play(self) -> None:
        """Resolve EE link and gripper DOF index. Call once after physics starts."""
        link_names = self._articulation.link_names
        if self._EE_LINK_NAME in link_names:
            self._ee_prim = GeomPrim(paths=self._articulation.link_paths[0][link_names.index(self._EE_LINK_NAME)])
        else:
            print(f"WARNING: '{self._EE_LINK_NAME}' not found. Available: {link_names}")

        dof_names = self._articulation.dof_names
        if self._GRIPPER_JOINT in dof_names:
            self._finger_idx = dof_names.index(self._GRIPPER_JOINT)
        else:
            print(f"WARNING: '{self._GRIPPER_JOINT}' not found. Available: {dof_names}")

        self._articulation.reset_to_default_state()

    def _init_pink_q0(self) -> None:
        """Set pink_robot.q0 to elbow-up for PostureTask regularization."""
        import pinocchio as pin

        elbow_up_map = {
            "shoulder_pan_joint": -np.pi / 2,
            "shoulder_lift_joint": -np.pi / 2,
            "elbow_joint": -np.pi / 2,
            "wrist_1_joint": -np.pi / 2,
            "wrist_2_joint": np.pi / 2,
            "wrist_3_joint": 0.0,
        }
        q0 = pin.neutral(self._pink_robot.model)
        for name, angle in elbow_up_map.items():
            if self._pink_robot.model.existJointName(name):
                jid = self._pink_robot.model.getJointId(name)
                q0[self._pink_robot.model.joints[jid].idx_q] = angle
        self._pink_robot.q0 = q0

    def _phase_ee_target(self) -> np.ndarray:
        c, p = self.cube_position, self.target_position
        offset = self._TOOL_OFFSET[self._TOOL_FRAME]
        hi = self._ABOVE_HEIGHT + offset
        lo = self._NEAR_HEIGHT + offset
        targets = {
            0: [c[0], c[1], c[2] + hi],
            1: [c[0], c[1], c[2] + lo],
            2: [c[0], c[1], c[2] + lo],
            3: [c[0], c[1], c[2] + hi],
            4: [p[0], p[1], p[2] + hi],
            5: [p[0], p[1], p[2] + lo],
            6: [p[0], p[1], p[2] + lo],
            7: [p[0], p[1], p[2] + hi],
        }
        return np.array(targets[self._event], dtype=np.float32)

    def _make_setpoint(self, position: np.ndarray) -> mg.RobotState:
        return mg.RobotState(
            sites=mg.SpatialState.from_name(
                spatial_space=[self._TOOL_FRAME],
                positions=([self._TOOL_FRAME], wp.array([position.tolist()], dtype=wp.float32)),
                orientations=([self._TOOL_FRAME], wp.array([self._DOWN_ORI.tolist()], dtype=wp.float32)),
            ),
        )

    def _estimated_state(self) -> mg.RobotState:
        names = self._articulation.dof_names
        return mg.RobotState(
            joints=mg.JointState.from_name(
                robot_joint_space=names,
                positions=(names, self._articulation.get_dof_positions()),
                velocities=(names, self._articulation.get_dof_velocities()),
            )
        )

    def _set_gripper(self, pos: float) -> None:
        if self._finger_idx is not None:
            self._articulation.set_dof_position_targets(
                wp.array([pos], dtype=wp.float32), dof_indices=[self._finger_idx]
            )

    def _ee_near_target(self) -> bool:
        if self._ee_prim is None:
            return False
        ee_pos = self._ee_prim.get_world_poses()[0].numpy()[0]
        return bool(np.linalg.norm(ee_pos - self._phase_ee_target()) < self._EE_THRESHOLD)

    def _gripper_at(self, target: float) -> bool:
        if self._finger_idx is None:
            return False
        pos = float(self._articulation.get_dof_positions().numpy().flatten()[self._finger_idx])
        return abs(pos - target) < self._GRIPPER_THRESHOLD

    def _phase_converged(self) -> bool:
        if self._step < self._MIN_STEPS:
            return False
        if self._event == 2:
            return self._gripper_at(self._CLOSED_POS)
        if self._event == 6:
            return self._gripper_at(self._OPEN_POS)
        return self._ee_near_target()

    def forward(self) -> bool:
        """Advance one simulation step. Returns False when the sequence is complete."""
        if self.is_done():
            return False

        if self._warmup_remaining > 0:
            n_dofs = len(self._articulation.dof_names)
            targets = np.concatenate([self._ELBOW_UP_ARM, np.zeros(max(0, n_dofs - 6))])
            self._articulation.set_dof_position_targets(
                wp.array(targets, dtype=wp.float32), dof_indices=list(range(n_dofs))
            )
            self._warmup_remaining -= 1
            if np.abs(self._articulation.get_dof_positions().numpy().flatten()[:6] - self._ELBOW_UP_ARM).max() < 0.1:
                self._warmup_remaining = 0
            return True

        if self._step == 0:
            print(f"  Phase {self._event}: {self._PHASE_LABELS[self._event]}")
            if self._event in (0, 3, 7):
                if not self._controller.reset(
                    self._estimated_state(), self._make_setpoint(self._phase_ee_target()), t=0.0
                ):
                    raise RuntimeError("PinkIKController reset failed.")
                self._t = 0.0

        if self._event == 2:
            self._set_gripper(self._CLOSED_POS)
        elif self._event == 6:
            self._set_gripper(self._OPEN_POS)
        else:
            desired = self._controller.forward(
                self._estimated_state(), self._make_setpoint(self._phase_ee_target()), self._t
            )
            if desired is not None and desired.joints.positions is not None:
                self._articulation.set_dof_position_targets(
                    positions=desired.joints.positions, dof_indices=desired.joints.position_indices
                )

        self._t += self._PHYSICS_DT
        self._step += 1
        if self._phase_converged() or self._step >= self.events_dt[self._event]:
            if self._step >= self.events_dt[self._event]:
                print(f"  Phase {self._event} timed out after {self.events_dt[self._event]} frames")
            self._event += 1
            self._step = 0

        return True

    def is_done(self) -> bool:
        return self._event >= len(self.events_dt)

    def reset(self) -> None:
        self._event = 0
        self._step = 0
        self._t = 0.0
        self._warmup_remaining = self._WARMUP_FRAMES
```

See also

* [PINK Integration](../pink/index.html#isaac-sim-pink) â overview of the PINK integration and its weighted multi-task IK approach.
* [PINK IK Controller Tutorial](../pink/tutorial_ik_controller.html#isaac-sim-pink-tutorial-ik-controller) â in-depth walkthrough of `PinkIKController`, task weights, posture regularization, and QP solver selection.
* [PINK Robot Configuration Tutorial](../pink/tutorial_robot_configuration.html#isaac-sim-pink-tutorial-robot-configuration) â loading PINK robot models with `load_pink_supported_robot()` and `load_pink_robot()`.

## Summary

In this tutorial, you learned how to:

* Control the 2F-140 gripper using the Articulation API and `set_dof_position_targets`.
* Plan and execute joint-space trajectories using `mg.Path` and `mg.TrajectoryFollower`.
* Use the cuMotion `RmpFlowController` to track a Cartesian target in real time with obstacle avoidance.
* Implement an 8-phase pick-and-place sequence with cuMotion RMPflow.
* Implement the same sequence with PINK differential IK as an alternative CPU-based solver.

On this page

* [Learning Objectives](#learning-objectives)
* [Prerequisites](#prerequisites)
* [Overview](#overview)
* [Part 1: Gripper Control](#part-1-gripper-control)
* [Part 2: Arm Trajectory Following](#part-2-arm-trajectory-following)
* [Part 3: Follow Target using cuMotion RMPflow](#part-3-follow-target-using-cumotion-rmpflow)
* [Part 4: Pick and Place](#part-4-pick-and-place)
  + [cuMotion RMPflow](#cumotion-rmpflow)
  + [PINK Differential IK](#pink-differential-ik)
* [Summary](#summary)