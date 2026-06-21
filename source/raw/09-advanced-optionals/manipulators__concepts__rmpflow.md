---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/manipulators/concepts/rmpflow.html
title: "RMPflow"
section: "Manipulators"
module: "09-advanced-optionals"
checksum: "0c333604f026cbdf"
fetched: "2026-06-21T14:14:38"
---

* [Robot Simulation](../../robot_simulation/index.html)
* [Motion Generation (Deprecated)](../motion_generation_overview.html)
* [Motion Generation](index.html)
* RMPflow

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# RMPflow

Deprecated

For new development, consider using the newer [Robot Motion (Experimental)](../../robot_motion_experimental/index.html) API, which provides improved interfaces and additional features over Lula.

[Riemannian Motion Policy (RMP)](../../reference_material/reference_glossary.html#isaac-sim-glossary-rmp) is a set of motion generation tools that underlies most Isaac Sim manipulator controls.
It creates smooth trajectories for the robots with intelligent collision avoidance.

A **Riemannian Motion Policy**, or *RMP*, is an acceleration policy
accompanied by a matrix \(M(q, \dot{q})\) that is sometimes called an inertia matrix,
borrowing terminology from classical mechanics, but is also closely related to the concept
of a Riemannian metric.

Leveraging the machinery of Riemannian geometry, *RMPflow* is a
framework for combining RMPs representing multiple (possibly competing) objectives and
constraints into a single global acceleration policy. Within this framework, the local RMPs
can be defined on any number of intermediate task spaces (including the operational space of
the end effector, generalizing operational space control). For details, refer to
[\*RMPflow: A computational graph for automatic motion policy generation\*](https://arxiv.org/abs/1811.07049).

Broadly defined, a *motion policy* is a mathematical function that takes the current
state of a robot (for example, position and velocity in generalized coordinates) and returns
a quantity representing a desired change in that state. Such a policy can depend
implicitly on variables representing one or more objectives or constraints, the state of
the environment. An *acceleration policy* is a motion policy where the output is
desired acceleration, \(\ddot q = \pi(q, \dot{q})\), resulting in a second-order
differential equation.

For the purpose of controlling a robot by position or velocity control, typically motion policies are used
where the output is position or velocity. Such
policies can be produced from an acceleration policy using a numerical
integration scheme such as Euler integration.

The [RMPflow Debugging Features](#isaac-sim-motion-generation-rmpflow-debugging-features) section reviews functions belonging to RMPflow that are not part of the MotionPolicy interface.
You can interact with RMPflow to control a robot that is already supported. If you are interested in the internal
mechanics of RMPflow or want to configure RMPflow for an unsupported robot, continue reading the RMPflow documentation.

After reviewing the basics here, also see the [RMPflow Tuning Guide](rmpflow_tuning_guide.html) for practical advice on configuring RMPflow for a new robot.

## RMPflow Debugging Features

By directly interacting with an RmpFlow instance, you can access features that are not available in other MotionPolicy implementations.
It is common for developers to want to decouple a [Motion Policy Algorithm](motion_policy.html#isaac-sim-motion-policy) from the simulated robot Articulation in NVIDIA Isaac Sim.
For example, when the simulated robot is moving sluggishly, it is important to determine whether the MotionPolicy or the PD gains have been improperly tuned,
but this can be difficult when both the PD gains and the MotionPolicy play a role in driving the robot joints (see [Outputs: Robot Joint Targets](motion_policy.html#isaac-sim-motion-policy-joint-targets)).

RMPflow provides visualization functions to clearly show the internal state of the algorithm as part of the stage. RMPflow uses collision spheres internally to
avoid hitting obstacles in the world. These spheres can be visualized over time by calling `RmpFlow.visualize_collision_spheres()`. The visualization will stop when
`RmpFlow.stop_visualizing_collision_spheres()` is called. The nominal end effector position can likewise be visualized with
`RmpFlow.visualize_end_effector_position()` and `RmpFlow.stop_visualizing_end_effector()`.

On their own, the visualization functions can be used to make sure that RMPflow’s internal representation of the robot is reasonable, but it does not help to decouple the
simulated robot from the RmpFlow internal representation of the robot.

On each frame when `RmpFlow.compute_joint_targets(active_joint_positions,...)` is called,
the visualization is updated to use the `active_joint_positions`. This behavior can be turned off using `RmpFlow.set_ignore_state_updates(True)`. When RmpFlow
is “ignoring state updates”, it starts ignoring the `active_joint_positions` argument, and instead begins internally tracking the believed state of the robot by assuming
that is completely independent of the physical simulation of the robot. When RmpFlow is set to ignore state updates from the simulator, and the visualization functions are used,
it becomes simple to determine if an undesirable robot behavior
comes from RmpFlow or from the robot Articulation and its PD gains.

## RMPflow Configuration

Three files are necessary to configure RMPflow for use with a new robot:

> * A **URDF** (universal robot description file), used for specifying robot kinematics
>   :   as well as joint and link names. Position limits for each joint are also required.
>       Other properties in the URDF are ignored and can be omitted; these include masses,
>       moments of inertia, visual, and collision meshes.
> * A **supplementary robot description file** in YAML format. In addition to enumerating
>   :   the list of actuated joints that define the configuration space (c-space) for the robot,
>       this file includes sections for specifying the default c-space configuration
>       and sets of collision spheres used for collision avoidance. This file can also
>       be used to specify fixed positions for unactuated joints.
> * A **RMPflow configuration file** in YAML format, containing parameters for all enabled RMPs.

As a general mathematical framework, RMPflow does not prescribe the form that individual RMPs
must take. The particular implementation of RMPflow in Lula (and by extension NVIDIA Isaac Sim) does
however expose a pre-specified set of RMPs that have been constructed and empirically found
to produce smooth reactive behaviors for a variety of manipulation tasks.

## C-Space Target RMP (c-space\_target\_rmp)

**Purpose:** Specifies a default c-space configuration for the robot, used for redundancy resolution.

**Definition:** Acceleration for this RMP is given by an equation similar to a PD controller, with a
position gain and damping gain, but the magnitude of the position term is capped when the C-space
distance exceeds a threshold. This cap avoids excessive forces when the configuration is far away
from the target. Defining \(q\) to be the full configuration vector:

\[\ddot q = k\_p r(q\_0 - q) - k\_d \dot q\,,\]

where the “robust capping function” \(r(p)\) is given by:

\[\begin{split}r(p) = \left \{ \begin{array}{cl}
p, & ||p|| < \theta \\
\theta\, p / ||p|| & \textrm{otherwise.}
\end{array} \right.\end{split}\]

The inertia matrix is proportional to the identity:

\[M = \mu I\]

The c-space\_target\_rmp section of the RMPflow configuration file contains an additional
inertia parameter \(m\). When this parameter is nonzero, it results in the introduction of
a conceptually separate RMP corresponding to zero c-space acceleration, \(\ddot q = 0\), with inertia
matrix given by \(M = mI\).

**Parameters:**

Units assume revolute joints where \(q\) is expressed in radians. If joints are instead prismatic,
robust\_position\_term\_thresh will have units of meters.

| Name | Symbol | Units | Meaning |
| --- | --- | --- | --- |
| metric\_scalar | \(\mu\) | - | Priority weight relative to other RMPs |
| position\_gain | \(k\_p\) | s-2 | Position gain, determining how strongly configuration is pulled toward target |
| damping\_gain | \(k\_d\) | s-1 | Damping gain, determining amount of “drag” |
| robust\_position\_term\_thresh | \(\theta\) | rad | Distance in c-space at which the position correction vector is capped |
| inertia | \(m\) | - | Additional c-space inertia |

## Target RMP (target\_rmp)

**Purpose:** Drives end effector toward specified position target.

**Definition:** Similar to the c-space target RMP, acceleration for this RMP resembles a PD
controller, albeit with a slightly different strategy for capping the magnitude of the position
correction vector.

\[\ddot x = k\_p (x\_0 - x) / (||x\_0-x|| + \epsilon) - k\_d \dot x\]

The inertia matrix blends between a rank-deficient metric \(S = n n^T`\), where \(n\) is
the direction vector toward the target, and the identity \(I\).

Intuitively, \(S\) cares
only about the direction toward the target (letting other RMPs such as the obstacle avoidance RMP
control the orthogonal directions).

\(I\) cares about all directions.

The contribution of
\(S\) is larger farther from the goal, allowing obstacles to push the system more effectively,
while \(I\) dominates near the goal, encouraging faster convergence.

Blending is
controlled by a radial basis function, specifically a Gaussian, that transitions from a minimum
constant value far from the target to 1 near the target.

Near the target, an additional nonlinear “proximity boost” multiplier turns on. This
factor takes the form of a Gaussian:

\[M = \left[\beta(x) b + (1-\beta(x))\right] \left[\alpha(x) M\_\textrm{near} + (1-\alpha(x)) M\_\textrm{far} \right]\]

where

\[\begin{split}\begin{array}{l}
\alpha(x) = (1-\alpha\_\textrm{min})\exp \left(\frac{-||x\_0-x||^2}{2 \sigma\_a^2}\right) + \alpha\_\textrm{min} \\
\beta(x) = \exp \left(-\frac{||x\_0 - x||^2}{2 \sigma\_b^2}\right) \\
M\_\textrm{near} = \mu\_\textrm{near} I \\
M\_\textrm{far} = \mu\_\textrm{far} S = \frac{\mu\_\textrm{far}}{||x\_0-x||^2} (x\_0-x)(x\_0-x)^T\,.
\end{array}\end{split}\]

**Parameters:**

| Name | Symbol | Units | Meaning |
| --- | --- | --- | --- |
| accel\_p\_gain | \(k\_p\) | m/s2 | Position gain |
| accel\_d\_gain | \(k\_d\) | s-1 | Damping gain |
| accel\_norm\_eps | \(\epsilon\) | m | Length scale controlling transition between constant acceleration region far from target and linear region near target |
| metric\_alpha\_length\_scale | \(\sigma\_a\) | m | Length scale of the Gaussian controlling blending between \(S\) and \(I\) |
| min\_metric\_alpha | \(\alpha\_\textrm{min}\) | - | Controls the minimum contribution of the isotropic \(M\_\textrm{near}\) term to the metric (inertia matrix) |
| max\_metric\_scalar | \(\mu\_\textrm{near}\) | - | Metric scalar for the isotropic \(M\_\textrm{near}\) contribution to the metric (inertia matrix) |
| min\_metric\_scalar | \(\mu\_\textrm{far}\) | - | Metric scalar for the directional \(M\_\textrm{far}\) contribution to the metric (inertia matrix) |
| proximity\_metric\_boost\_scalar | \(b\) | - | Scale factor controlling the strength of boosting near the target |
| proximity\_metric\_boost\_length\_scale | \(\sigma\_b\) | m | Length scale of the Gaussian controlling boosting near the target |
| xi\_estimator\_gate\_std\_dev | - | - | Unused parameter (to be removed in a future release) |

## Axis Target RMP (axis\_target\_rmp)

**Purpose:** Drives x-, y-, or z-axis of end effector frame toward target orientation. This
RMP is used for general orientation targets (where an axis target RMP is added for each of the
three axes) as well as for “partial pose” targets where only alignment of a single axis is
desired.

Note

Partial pose targets are not supported by the Motion Generation extension.

**Definition:**

Similar to the (position) target RMP, the axis target RMP supports “proximity boosting,”
but only when a target RMP is active at the same time. In this case, it’s the distance to
the position target (\(||x\_0-x||\)) that controls the strength of boosting.

The current and desired axis orientations are represented by unit vectors, denoted
by \(n\) and \(n\_0\) respectively. Acceleration is given by:

\[\ddot n = k\_p (n\_0 - n) - k\_d \dot n\,\]

If a position target (that is, target RMP) is active, the metric has the form:

\[M\_\textrm{boosted} = \left[\beta(x) b + (1-\beta(x))\right] \mu I\,\]

where:

\[\beta(x) = \exp \left(-\frac{||x\_0 - x||^2}{2 \sigma\_b^2}\right)\,\]

When no position target is active, this simplifies to:

\[M = \mu I\,.\]

**Parameters:**

| Name | Symbol | Units | Meaning |
| --- | --- | --- | --- |
| accel\_p\_gain | \(k\_p\) | s-2 | Position gain |
| accel\_d\_gain | \(k\_d\) | s-1 | Damping gain |
| metric\_scalar | \(\mu\) | - | Priority weight relative to other RMPs |
| proximity\_metric\_boost\_scalar | \(b\) | - | Scale factor controlling the strength of boosting near the position target |
| proximity\_metric\_boost\_length\_scale | \(\sigma\_b\) | m | Length scale of the Gaussian controlling boosting near the position target |

## Joint Limit RMP (joint\_limit\_rmp)

**Purpose:** Avoids joint limits.

**Definition:** This is a one-dimensional RMP that depends on a single
c-space coordinate (joint) and a corresponding upper or lower joint limit as specified in
the URDF for the robot. If a robot has \(N\) joints, it follows that a total of \(2N\)
joint limit RMPs will be introduced. The joint limits specified in the URDF can be padded
(that is, made more conservative) by entering positive padding values in the joint\_limit\_buffers
array in the RMPflow configuration file. For a given joint, the same padding value is used
for both upper and lower limits.

The task space for this RMP consists of a shifted and scaled c-space coordinate, measuring
the scaled distance to either the upper or lower joint limit. Without loss of generality,
we consider a lower joint limit RMP. If \(q\) is the c-space coordinate for a given
joint, and \(q\_\textrm{upper}\) and \(q\_\textrm{lower}\) are the upper and lower
limits for that joint, respectively, we define:

\[x = \frac{q - q\_\textrm{lower}}{q\_\textrm{upper} - q\_\textrm{lower}}\,\]

The acceleration for that coordinate is then given by:

\[\ddot x = \frac{k\_p}{x^2/\ell\_p^2 + \epsilon\_p} - k\_d \dot x\,\]

The metric (inertia matrix) is a scalar given by:

\[m = \left(1 - \frac{1}{1+\exp(-\dot x/v\_m)}\right) \frac{\mu}{x/\ell\_m + \epsilon\_m}\,\]

**Parameters:**

| Name | Symbol | Units | Meaning |
| --- | --- | --- | --- |
| metric\_scalar | \(\mu\) | - | Overall priority weight relative to other RMPs |
| metric\_length\_scale | \(\ell\_m\) | - | Length scale controlling ramp-up of metric as joint limit is approached |
| metric\_exploder\_eps | \(\epsilon\_m\) | - | Offset determining \(x\) value at which metric diverges |
| metric\_velocity\_gate\_length\_scale | \(v\_m\) | s-1 | Scale determining rate at which metric increases with velocity in direction of barrier |
| accel\_damper\_gain | \(k\_d\) | s-1 | Damping gain |
| accel\_potential\_gain | \(k\_p\) | s-2 | Gain multiplying position barrier term |
| accel\_potential\_exploder\_length\_scale | \(\ell\_p\) | - | Length scale controlling steepness of position barrier |
| accel\_potential\_exploder\_eps | \(\epsilon\_p\) | - | Offset limiting divergence of position barrier strength |

## Joint Velocity Limit RMP (joint\_velocity\_cap\_rmp)

**Purpose:** Limits maximum joint velocity.

**Definition:** This RMP applies damping when the magnitude of the velocity of a given joint
approaches the specified limit.

This is a one-dimensional RMP with acceleration given by:

\[\ddot q = -k\_d\,\textrm{sgn}(\dot q) \left(|\dot q| - (v\_\textrm{max} - v\_r)\right)\,\]

The metric (inertia matrix) is a scalar given by:

\[\begin{split}m = \left \{ \begin{array}{cl}
0, & |\dot q| < (v\_\textrm{max} - v\_r) \\
\frac{\mu}{1 - \left(|\dot q| - (v\_\textrm{max} - v\_r)\right)^2 / v\_r^2} & \textrm{otherwise.}
\end{array} \right\end{split}\]

The metric is zero outside you-specified damping region, thereby disabling this RMP.
In addition, clipping is applied to avoid divergence of the metric as \(\dot q\) approaches \(v\_\textrm{max}\).

**Parameters:**

Units assume revolute joints where \(q\) is expressed in radians. If joints are instead prismatic,
max\_velocity and velocity\_damping\_region will have units of m/s.

| Name | Symbol | Units | Meaning |
| --- | --- | --- | --- |
| max\_velocity | \(v\_\textrm{max}\) | rad/s | Maximum allowed velocity magnitude |
| velocity\_damping\_region | \(v\_r\) | rad/s | Defines width of velocity region affect by damping |
| damping\_gain | \(k\_d\) | s-1 | Damping gain |
| metric\_weight | \(\mu\) | - | Overall priority weight relative to other RMPs |

## Collision Avoidance RMP (collision\_rmp)

**Purpose:** Avoids collision with obstacles in the environment.

**Definition:** This is a one-dimensional RMP where the task space consists of a single
coordinate measuring distance from a given collision sphere on the robot (specified in the
robot description YAML file) to an obstacle in the environment. Denoting that coordinate
as \(x\), the acceleration is given by:

\[\ddot x = k\_p \exp(-x / \ell\_p) - k\_d \left[1 - \frac{1}{1 + \exp(-\dot x/v\_d)} \right] \frac{\dot x}{x/\ell\_d + \epsilon\_d}\,\]

The metric (inertia matrix) is a scalar given by:

\[m = \left[1 - \frac{1}{1 + \exp(-\dot x/v\_d)} \right] g(x) \frac{\mu}{x / \ell\_m + \epsilon\_m}\,\]

where \(g(x)\) is a piecewise polynomial that varies smoothly from 1 to 0 as \(x\) varies from 0 to \(r\)

\[\begin{split}g(x) = \left \{ \begin{array}{cl}
x^2/r^2 -2s/r + 1, & x\le r \\
0, & x\gt r
\end{array} \right.\end{split}\]

**Parameters:**

| Name | Symbol | Units | Meaning |
| --- | --- | --- | --- |
| damping\_gain | \(k\_d\) | s-1 | Damping gain |
| damping\_std\_dev | \(\ell\_d\) | m | Length scale controlling increase in acceleration as obstacle is approached |
| damping\_robustness\_eps | \(\epsilon\_d\) | - | Offset determining \(x\) value at which acceleration diverges (before clipping) |
| damping\_velocity\_gate\_length\_scale | \(v\_d\) | m/s | Scale determining velocity dependence of “velocity gating” function |
| repulsion\_gain | \(k\_p\) | m/s2 | Gain for position repulsion term |
| repulsion\_std\_dev | \(\ell\_p\) | m | Length scale controlling distance dependence of repulsion |
| metric\_modulation\_radius | \(r\) | m | Length scale determining distance from obstacle at which RMP is disabled completely |
| metric\_scalar | \(\mu\) | - | Overall priority weight relative to other RMPs |
| metric\_exploder\_std\_dev | \(\ell\_m\) | m | Length scale controlling increase in metric as obstacle is approached |
| metric\_exploder\_eps | \(\epsilon\_m\) | - | Offset determining \(x\) value at which metric diverges (before clipping) |

## Damping RMP (damping\_rmp)

**Purpose:** Contributes additional nonlinear damping based on control frame
(for example, end effector) velocity relative to target.

**Definition:** This is a one-dimensional RMP where the task space consists of a single coordinate
\(x\) measuring distance from the origin of the control frame to the target.
The acceleration is given by:

\[\ddot x = -k\_d |\dot x|\dot x\]

and the metric by:

\[M = \mu |\dot x| I\,\]

The damping\_rmp section of the RMPflow configuration file contains an additional
inertia parameter \(m\). When this parameter is nonzero, it results in the introduction of
a conceptually separate RMP corresponding to zero acceleration, \(\ddot x = 0\), with inertia
matrix given by \(M = mI\).

**Parameters:**

| Name | Symbol | Units | Meaning |
| --- | --- | --- | --- |
| accel\_d\_gain | \(k\_d\) | m-1 | Nonlinear damping gain |
| metric\_scalar | \(\mu\) | (m/s)-1 | Priority weight relative to other RMPs |
| inertia | \(m\) | - | Additional inertia |

## Further Reading

Refer to the [RMPflow Tuning Guide](rmpflow_tuning_guide.html) for practical advice on configuring RMPflow for a new robot.

On this page

* [RMPflow Debugging Features](#rmpflow-debugging-features)
* [RMPflow Configuration](#rmpflow-configuration)
* [C-Space Target RMP (c-space\_target\_rmp)](#c-space-target-rmp-c-space-target-rmp)
* [Target RMP (target\_rmp)](#target-rmp-target-rmp)
* [Axis Target RMP (axis\_target\_rmp)](#axis-target-rmp-axis-target-rmp)
* [Joint Limit RMP (joint\_limit\_rmp)](#joint-limit-rmp-joint-limit-rmp)
* [Joint Velocity Limit RMP (joint\_velocity\_cap\_rmp)](#joint-velocity-limit-rmp-joint-velocity-cap-rmp)
* [Collision Avoidance RMP (collision\_rmp)](#collision-avoidance-rmp-collision-rmp)
* [Damping RMP (damping\_rmp)](#damping-rmp-damping-rmp)
* [Further Reading](#further-reading)