---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/py/source/extensions/isaacsim.core.simulation_manager/config/python_api.html
title: "core.simulation_manager API"
section: "Core"
module: "05-python-api-quickref"
checksum: "860008a7a1efa72c"
fetched: "2026-06-21T14:14:26"
---

* Public API for module isaacsim.core.simulation\_manager:

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Public API for module isaacsim.core.simulation\_manager:

## Classes

* class PhysicsScene

  + def **init**(self, prim: str | Usd.Prim)
  + [property] def path(self) -> str
  + [property] def prim(self) -> Usd.Prim
  + [property] def physics\_scene(self) -> UsdPhysics.Scene
  + static def get\_physics\_scene\_paths(stage: Usd.Stage | None = None) -> list[str]
  + def get\_gravity(self) -> Gf.Vec3f
  + def set\_gravity(self, gravity: Gf.Vec3f | tuple[float, float, float] | list[float])
  + def get\_dt(self) -> float
  + def set\_dt(self, dt: float)
  + def get\_enabled\_gravity(self) -> bool
  + def set\_enabled\_gravity(self, enabled: bool)
  + def get\_max\_solver\_iterations(self) -> int
  + def set\_max\_solver\_iterations(self, iterations: int)
* class PhysxGpuCfg

  + gpu\_collision\_stack\_size: int | None
  + gpu\_found\_lost\_aggregate\_pairs\_capacity: int | None
  + gpu\_found\_lost\_pairs\_capacity: int | None
  + gpu\_heap\_capacity: int | None
  + gpu\_max\_deformable\_surface\_contacts: int | None
  + gpu\_max\_num\_partitions: int | None
  + gpu\_max\_particle\_contacts: int | None
  + gpu\_max\_rigid\_contact\_count: int | None
  + gpu\_max\_rigid\_patch\_count: int | None
  + gpu\_max\_soft\_body\_contacts: int | None
  + gpu\_temp\_buffer\_capacity: int | None
  + gpu\_total\_aggregate\_pairs\_capacity: int | None
* class PhysxScene(PhysicsScene)

  + def **init**(self, prim: str | Usd.Prim)
  + def get\_dt(self) -> float
  + def set\_dt(self, dt: float)
  + def get\_steps\_per\_second(self) -> int
  + def set\_steps\_per\_second(self, steps\_per\_second: int)
  + def get\_solver\_type(self) -> Literal[TGS, PGS]
  + def set\_solver\_type(self, solver\_type: Literal[TGS, PGS])
  + def get\_enabled\_gpu\_dynamics(self) -> bool
  + def set\_enabled\_gpu\_dynamics(self, enabled: bool)
  + def get\_enabled\_ccd(self) -> bool
  + def set\_enabled\_ccd(self, enabled: bool)
  + def get\_broadphase\_type(self) -> Literal[MBP, GPU, SAP]
  + def set\_broadphase\_type(self, broadphase\_type: Literal[MBP, GPU, SAP])
  + def get\_enabled\_stabilization(self) -> bool
  + def set\_enabled\_stabilization(self, enabled: bool)
  + def get\_gpu\_configuration(self) -> PhysxGpuCfg
  + def set\_gpu\_configuration(self, cfg: PhysxGpuCfg | dict)
* class SimulationEvent(Enum)

  + PHYSICS\_PRE\_STEP: str
  + PHYSICS\_POST\_STEP: str
  + SIMULATION\_SETUP: str
  + SIMULATION\_STARTED: str
  + SIMULATION\_PAUSED: str
  + SIMULATION\_RESUMED: str
  + SIMULATION\_STOPPED: str
  + PRIM\_DELETED: str
* class SimulationManager

  + class def get\_active\_physics\_engine(cls) -> Literal[physx]
  + class def get\_default\_engine(cls) -> str
  + class def get\_available\_physics\_engines(cls, verbose: bool = False) -> list[tuple[str, bool]]
  + class def switch\_physics\_engine(cls, engine\_name: Literal[physx, newton], verbose: bool = False) -> bool
  + class def initialize\_physics(cls)
  + class def invalidate\_physics(cls)
  + class def setup\_simulation(cls, dt: float | None = None, device: str | wp.Device | None = None)
  + class def get\_physics\_scenes(cls) -> list[PhysicsScene]
  + class def get\_physics\_simulation\_view(cls) -> ‘SimulationView’ | None
  + class def get\_simulation\_time(cls) -> float
  + class def get\_num\_physics\_steps(cls) -> int
  + class def is\_simulating(cls) -> bool
  + class def is\_paused(cls) -> bool
  + class def step(cls)
  + class def set\_device(cls, device: str | wp.Device)
  + class def get\_device(cls) -> wp.Device
  + class def enable\_fabric(cls, enable: bool)
  + class def is\_fabric\_enabled(cls) -> bool
  + class def register\_callback(cls, callback: Callable, event: SimulationEvent | IsaacEvents, \*\*kwargs) -> int
  + class def deregister\_callback(cls, uid: int) -> bool
  + class def deregister\_all\_callbacks(cls)
  + class def enable\_usd\_notice\_handler(cls, enable: bool)
  + class def enable\_fabric\_usd\_notice\_handler(cls, stage\_id, enable: bool)
  + class def is\_fabric\_usd\_notice\_handler\_enabled(cls, stage\_id)
  + class def assets\_loading(cls) -> bool
  + class def enable\_default\_callbacks(cls)
  + class def enable\_all\_default\_callbacks(cls, enable: bool = True)
  + class def is\_default\_callback\_enabled(cls, callback\_name: str) -> bool
  + class def get\_default\_callback\_status(cls) -> dict
  + class def enable\_post\_warm\_start\_callback(cls, enable: bool = True)
  + class def enable\_warm\_start\_callback(cls, enable: bool = True)
  + class def enable\_on\_stop\_callback(cls, enable: bool = True)
  + class def enable\_stage\_open\_callback(cls, enable: bool = True)
  + class def set\_backend(cls, val: str)
  + class def get\_backend(cls) -> str
  + class def get\_physics\_sim\_view(cls)
  + class def set\_default\_physics\_scene(cls, physics\_scene\_prim\_path: str)
  + class def get\_default\_physics\_scene(cls) -> str
  + class def set\_physics\_sim\_device(cls, val)
  + class def get\_physics\_sim\_device(cls) -> str
  + class def set\_physics\_dt(cls, dt: float = 1.0 / 60.0, physics\_scene: str = None)
  + class def get\_physics\_dt(cls, physics\_scene: str | None = None) -> float
  + class def get\_broadphase\_type(cls, physics\_scene: str | None = None) -> str
  + class def set\_broadphase\_type(cls, val: str, physics\_scene: str | None = None)
  + class def enable\_ccd(cls, flag: bool, physics\_scene: str | None = None)
  + class def is\_ccd\_enabled(cls, physics\_scene: str | None = None) -> bool
  + class def enable\_gpu\_dynamics(cls, flag: bool, physics\_scene: str | None = None)
  + class def is\_gpu\_dynamics\_enabled(cls, physics\_scene: str | None = None) -> bool
  + class def set\_solver\_type(cls, solver\_type: str, physics\_scene: str | None = None)
  + class def get\_solver\_type(cls, physics\_scene: str | None = None) -> str
  + class def enable\_stablization(cls, flag: bool, physics\_scene: str | None = None)
  + class def is\_stablization\_enabled(cls, physics\_scene: str = None) -> bool
* class IsaacEvents(Enum)

  + PHYSICS\_WARMUP: str
  + SIMULATION\_VIEW\_CREATED: str
  + PHYSICS\_READY: str
  + POST\_RESET: str
  + PRIM\_DELETION: str
  + PRE\_PHYSICS\_STEP: str
  + POST\_PHYSICS\_STEP: str
  + TIMELINE\_STOP: str

On this page

* [Classes](#classes)