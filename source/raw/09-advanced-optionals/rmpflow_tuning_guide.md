---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/manipulators/concepts/rmpflow_tuning_guide.html
title: "RMPflow Tuning"
section: "Manipulators"
module: "09-advanced-optionals"
checksum: "75abd36bc621ef4f"
fetched: "2026-06-21T13:05:41"
---

* [Robot Simulation](../../robot_simulation/index.html)
* [Motion Generation (Deprecated)](../motion_generation_overview.html)
* [Motion Generation](index.html)
* RMPflow Tuning Guide

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# RMPflow Tuning Guide

Deprecated

For new development, consider using the newer [Robot Motion (Experimental)](../../robot_motion_experimental/index.html) API, which provides improved interfaces and additional features over Lula. This
page is still a valid tuning guide for RMPflow in [cuMotion](https://nvidia-isaac.github.io/cumotion/).

Given the number of parameters involved in fully specifying a complete set of RMPs,
tuning an RMPflow-based motion policy for a new robot or task can be intimidating.
In practice, however, parameters that work well for one robot are likely to work well
for other robots with similar morphology. Furthermore, for a given robot, it is
generally possible to choose a set of parameters that work well for a wide variety
of tasks.

To review RMPflow and its features see, [RMPflow](rmpflow.html).

NVIDIA Isaac Sim includes example RMPflow configuration files for multiple robot arms, including
the 7-DOF Franka Emika Panda and the 6-DOF Universal Robots UR10. When tuning RMPflow for a
new manipulator, itâs usually best to start with one of these two files. If the new robot
is significantly larger or smaller than the one used as a reference, it might be necessary
to rescale any parameters that have units of length. If the number of joints differ, the
c-space\_target\_rmp/robust\_position\_term\_thresh parameter might also have to be adjusted.
Often, these steps are sufficient to produce a working motion policy.

If adapting an existing RMPflow configuration fails to produce acceptable results, use
the following procedure to tune a new policy from scratch:

Hint

It can helpful to play with parameter values for an existing robot (for example, the Franka).

1. Turn off all RMPs.
2. Each RMP has a parameter called either metric\_weight or metric\_scalar. Setting this parameter to zero will disable the corresponding RMP. For the target RMP, set the parameters min\_metric\_scalar, max\_metric\_scalar, and min\_metric\_alpha all to zero.
3. Set all inertia terms to zero (that is, c-space\_target\_rmp/inertia and damping\_rmp/inertia).
4. Re-enable RMPs one at a time, in the following suggested order:

   1. **c-space\_target\_rmp:** To get the robot moving to a configuration in c-space robustly.
      The magnitude of the metric scalar should be kept relatively small (for example, in the range 1 to 100), because
      this sets the global scale of all RMPs.
      Remember to set the default configuration in the robot description file (YAML) to a reasonable natural
      âreadyâ posture. This will be the default posture that the robot will favor while moving from place to place.
   2. **target\_rmp:** To get the end effector moving to a target robustly while continuing
      to use the c-space target RMP for redundancy resolution.

      1. Set target\_rmp/min\_metric\_alpha to zero and target\_rmp/metric\_alpha\_length\_scale
         to a large value relative to the size of the robot (in meters), such as 100,000. This effectively turns
         off the directional \(S\) term in the metric, reducing \(M\) to a simpler isotropic metric.
      2. Set target\_rmp/proximity\_metric\_boost\_length\_scalar to 1 to turn off priority boosting.
      3. Set target\_rmp/max\_metric\_scalar to a large value relative to c-space\_target\_rmp/metric\_scalar
         so it dominates. This will effectively make the c-space target RMP operate purely in the
         nullspace of the target RMP.
      4. Tune target\_rmp/accel\_p\_gain, target\_rmp/accel\_d\_gain, and target\_rmp/accel\_norm\_eps until
         good attractor behavior for the end effector has been achieved.
      5. Experiment with reducing target\_rmp/max\_metric\_scalar to ensure that itâs not too large. As
         max\_metric\_scalar is increased toward a suitable value, convergence accuracy should progressively
         improve. If convergence accuracy saturates at small constant error before the chosen max\_metric\_scalar
         value is reached, then it is probably set too high. This will be relevant when re-enabling the directional
         term in the target RMP metric below, ensuring that it makes a difference when the metric scalar decreases.
   3. **collision\_rmp:** Enable the collision avoidance RMP by setting collision\_rmp/metric\_scalar to a value
      comparable to target\_rmp/max\_metric\_scalar. It can be useful to plot the formulas for the acceleration
      and metric to gain some understanding of the roles of the various parameters.
   4. **target\_rmp (redux):** After the collision RMP is enabled, the system will probably drag near obstacles
      more slowly than it usually moves because the target RMP is fighting with the collision RMPs.
      Turning on the directional term in the metric will correct that effect.

      1. Plot the target RMP metric (as a function of distance from target)
         to build understanding. Try this first without the boosting term, noting how the metric transitions
         from the reduced-rank far metric to the full-rank near metric.
      2. Set target\_rmp/min\_metric\_alpha to a non-zero value and reduce the value of
         target\_rmp/metric\_alpha\_length\_scale until good behavior is achieved.
   5. **axis\_target\_rmp:** If an orientation target is set, the axis target RMP will be used to bring
      the orientation of the control frame (for example, end effector) into alignment with the target orientation.
      This RMP includes a âpriority boostingâ factor that depends on distance to the current
      position target, if one is set. This allows the robot to make progress toward the position
      target before zeroing in on the desired orientation.
   6. **joint\_limit\_rmp:** When properly tuned, behavior should be unchanged, except that joint
      limits will be avoided.
   7. **damping\_rmp:** Enable the damping RMP as well as target\_rmp/inertia to reduce jerk as necessary.

Throughout this process, referring to an existing RMPflow configuration file is helpful.