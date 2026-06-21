---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/physics/index.html
title: "Physics Index"
section: "物理"
module: "06-simready-assets"
checksum: "6bb10aa6311013db"
fetched: "2026-06-21T13:58:07"
---

* Physics

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Physics

On a high-level, simulations with Omniverse™ Physics work as follows:

* The USD Physics schema of robot and environment assets are parsed and corresponding simulation objects are created in the selected physics backend.
* Then, for each discrete-time step of the simulation, Physics advances the simulation objects given their current state and additional inputs such as, for example, control-policy torques.
* The updated state is written back to USD by default, where the state can be further processed by the user, a reinforcement-learning policy, or other extensions such as the Omniverse RTX Renderer.
* Omniverse™ Physics propagates runtime changes to physics parameters in USD to the physics objects.

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
* [Omniverse™ Physics and PhysX SDK Limitations](physics_resources.html)

## Tools

* [Physics Simulation Management](https://docs.omniverse.nvidia.com/kit/docs/omni_physics/latest/extensions/ux/source/omni.physx.ui/docs/dev_guide/sim_management.html "(in Omni Physics)")
* [Physics Inspector](joint_inspector.html)
* [Physics Static Collision Extension](physics_static_collision.html)
* [Simulation Data Visualizer](ext_isaacsim_inspect_physics.html)
* [Physics Debug Window](https://docs.omniverse.nvidia.com/kit/docs/omni_physics/latest/extensions/ux/source/omni.physx.ui/docs/dev_guide/physics_debug_wnd.html "(in Omni Physics)")

## Additional Resources

* Omniverse™ Physics [core documentation](https://docs.omniverse.nvidia.com/kit/docs/omni_physics/latest/index.html "(in Omni Physics)") and [programming guide](https://docs.omniverse.nvidia.com/kit/docs/omni_physics/latest/index.html)
* [USD Physics Schemas](https://openusd.org/release/api/usd_physics_page_front.html) and PhysX SDK-engine-specific [Physx Schemas](https://docs.omniverse.nvidia.com/kit/docs/omni_usd_schema_physics/latest/annotated.html)
* Explore further Omniverse [simulation extensions](https://docs.omniverse.nvidia.com/extensions/latest/ext_simulation.html#simoverview "(in Omniverse Extensions)").
* [PhysX SDK](https://nvidia-omniverse.github.io/PhysX/physx/5.4.2/index.html)
* [Omniverse Visual Debugger](https://nvidia-omniverse.github.io/PhysX/physx/5.4.2/docs/OmniVisualDebugger.html)
* [Flow: Fluid Dynamics](https://docs.omniverse.nvidia.com/extensions/latest/ext_fluid-dynamics.html "(in Omniverse Extensions)")
* [NVIDIA Warp](https://nvidia.github.io/warp/index.html)

On this page

* [Tools](#tools)
* [Additional Resources](#additional-resources)