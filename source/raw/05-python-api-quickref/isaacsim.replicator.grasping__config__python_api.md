---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/py/source/extensions/isaacsim.replicator.grasping/config/python_api.html
title: "replicator.grasping API"
section: "Replicator"
module: "05-python-api-quickref"
checksum: "cd83894f4187099a"
fetched: "2026-06-21T14:14:27"
---

* Public API for module isaacsim.replicator.grasping:

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Public API for module isaacsim.replicator.grasping:

## Classes

* class GraspingManager

  + def **init**(self)
  + def clear(self)
  + def clear\_simulation(self, simulate\_using\_timeline: bool)
  + def clear\_gripper(self)
  + def clear\_object(self)
  + def set\_results\_output\_dir(self, dir\_path: str | None)
  + def get\_results\_output\_dir(self) -> str | None
  + def set\_overwrite\_results\_output(self, overwrite: bool)
  + def set\_gripper(self, gripper: str | Usd.Prim) -> bool
  + [property] def gripper\_path(self) -> str
  + [property] def gripper\_prim(self) -> Usd.Prim | None
  + def set\_object\_prim\_path(self, path: str)
  + def get\_object\_prim\_path(self) -> str | None
  + def get\_object\_prim(self) -> Usd.Prim | None
  + def create\_and\_add\_grasp\_phase(self, name: str, joint\_drive\_targets: dict[str, float] = None, simulation\_steps: int = DEFAULT\_NUM\_SIMULATION\_STEPS, simulation\_step\_dt: float = DEFAULT\_SIMULATION\_STEP\_DT) -> GraspPhase
  + def remove\_grasp\_phase\_by\_name(self, phase\_name: str) -> bool
  + def get\_grasp\_phase\_by\_name(self, name: str, ignore\_case: bool = True) -> GraspPhase | None
  + def get\_grasp\_phase\_by\_index(self, index: int) -> GraspPhase | None
  + def get\_grasp\_phases\_as\_dicts(self) -> list[dict]
  + def get\_grasp\_phase\_names(self) -> list[str]
  + def save\_config(self, file\_path: str, components: list[str] | None = None, overwrite: bool = False)
  + def load\_config(self, file\_path: str, components: list[str] | None = None) -> dict[str, str]
  + def request\_workflow\_stop(self)
  + async def simulate\_all\_grasp\_phases(self, render: bool = True, physics\_scene\_path: str | None = None, isolate\_simulation: bool = False, simulate\_using\_timeline: bool = False) -> bool
  + async def simulate\_single\_grasp\_phase(self, phase\_identifier: str | int, render: bool = True, physics\_scene\_path: str | None = None, isolate\_simulation: bool = False, simulate\_using\_timeline: bool = False) -> bool
  + async def evaluate\_grasp\_poses(self, grasp\_poses: list[tuple[Gf.Vec3d, Gf.Quatd]], render: bool = True, physics\_scene\_path: str | None = None, isolate\_simulation: bool = False, simulate\_using\_timeline: bool = False, progress\_callback: callable = None)
  + async def evaluate\_grasp\_pose(self, location: Gf.Vec3d, orientation: Gf.Quatd, clear\_simulation: bool = True, render: bool = True, physics\_scene\_path: str | None = None, isolate\_simulation: bool = False, simulate\_using\_timeline: bool = False)
  + async def evaluate\_grasp\_pose\_by\_index(self, index: int, render: bool = True, physics\_scene\_path: str | None = None, isolate\_simulation: bool = False, simulate\_using\_timeline: bool = False)
  + def write\_grasp\_results(self, location: Gf.Vec3d, orientation: Gf.Quatd)
  + def set\_gripper\_pose(self, location: Gf.Vec3d, orientation: Gf.Quatd)
  + def move\_gripper\_to\_grasp\_pose(self, index: int, in\_world\_frame: bool = True)
  + def store\_initial\_gripper\_pose(self, location: Gf.Vec3d = None, orientation: Gf.Quatd = None)
  + def get\_initial\_gripper\_pose(self) -> tuple[Gf.Vec3d, Gf.Quatd] | None
  + def generate\_grasp\_poses(self, config: dict = None) -> bool
  + def clear\_grasp\_poses(self)
  + def get\_grasp\_poses(self, in\_world\_frame: bool = False) -> list[tuple[Gf.Vec3d, Gf.Quatd]]
  + def get\_grasp\_pose\_at\_index(self, index: int, in\_world\_frame: bool = False) -> tuple[Gf.Vec3d, Gf.Quatd] | None
  + def update\_joint\_pregrasp\_states\_from\_current(self, joint\_info\_list: list[dict] | None = None)
* class GraspPhase

  + name: str
  + joint\_drive\_targets: dict[str, float]
  + simulation\_steps: int
  + simulation\_step\_dt: float
  + def add\_joint(self, joint\_path: str, target\_position: float = 0)
  + def remove\_joint(self, joint\_path: str)
  + def has\_joint(self, joint\_path: str) -> bool
  + def get\_joint\_target(self, joint\_path: str) -> float

On this page

* [Classes](#classes)