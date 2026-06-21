---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/py/source/extensions/isaacsim.core.experimental.prims/config/python_api.html
title: "core.experimental.prims API"
section: "Core"
module: "05-python-api-quickref"
checksum: "b12a8312a8055bd2"
fetched: "2026-06-21T14:14:26"
---

* Public API for module isaacsim.core.experimental.prims:

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Public API for module isaacsim.core.experimental.prims:

## Classes

* class Articulation(XformPrim)

  + def **init**(self, paths: str | list[str])
  + [property] def num\_dofs(self) -> int
  + [property] def dof\_names(self) -> list[str]
  + [property] def dof\_paths(self) -> list[list[str]]
  + [property] def dof\_types(self) -> list[omni.physics.tensors.DofType]
  + [property] def num\_joints(self) -> int
  + [property] def joint\_names(self) -> list[str]
  + [property] def joint\_paths(self) -> list[list[str]]
  + [property] def joint\_types(self) -> list[omni.physics.tensors.JointType]
  + [property] def num\_links(self) -> int
  + [property] def link\_names(self) -> list[str]
  + [property] def link\_paths(self) -> list[list[str]]
  + [property] def num\_shapes(self) -> int
  + [property] def num\_fixed\_tendons(self) -> int
  + [property] def jacobian\_matrix\_shape(self) -> tuple[int, int, int]
  + [property] def mass\_matrix\_shape(self) -> tuple[int, int]
  + static def fetch\_articulation\_root\_api\_prim\_paths(paths: str | list[str]) -> list[str | None]
  + def is\_physics\_tensor\_entity\_valid(self) -> bool
  + def is\_physics\_tensor\_entity\_initialized(self) -> bool
  + def get\_link\_indices(self, names: str | list[str]) -> wp.array
  + def get\_joint\_indices(self, names: str | list[str]) -> wp.array
  + def get\_dof\_indices(self, names: str | list[str]) -> wp.array
  + def get\_dof\_limits(self) -> tuple[wp.array, wp.array]
  + def set\_dof\_limits(self, lower: float | list | np.ndarray | wp.array | None = None, upper: float | list | np.ndarray | wp.array | None = None)
  + def get\_dof\_friction\_properties(self) -> tuple[wp.array, wp.array, wp.array]
  + def set\_dof\_friction\_properties(self, static\_frictions: float | list | np.ndarray | wp.array | None = None, dynamic\_frictions: float | list | np.ndarray | wp.array | None = None, viscous\_frictions: float | list | np.ndarray | wp.array | None = None)
  + def get\_dof\_drive\_model\_properties(self) -> tuple[wp.array, wp.array, wp.array]
  + def set\_dof\_drive\_model\_properties(self, speed\_effort\_gradients: float | list | np.ndarray | wp.array | None = None, maximum\_actuator\_velocities: float | list | np.ndarray | wp.array | None = None, velocity\_dependent\_resistances: float | list | np.ndarray | wp.array | None = None)
  + def set\_dof\_armatures(self, armatures: float | list | np.ndarray | wp.array)
  + def get\_dof\_armatures(self) -> wp.array
  + def set\_dof\_position\_targets(self, positions: float | list | np.ndarray | wp.array)
  + def set\_dof\_positions(self, positions: float | list | np.ndarray | wp.array)
  + def set\_dof\_velocity\_targets(self, velocities: float | list | np.ndarray | wp.array)
  + def set\_dof\_velocities(self, velocities: float | list | np.ndarray | wp.array)
  + def set\_dof\_efforts(self, efforts: float | list | np.ndarray | wp.array)
  + def get\_dof\_efforts(self) -> wp.array
  + def get\_dof\_projected\_joint\_forces(self) -> wp.array
  + def get\_link\_incoming\_joint\_force(self) -> tuple[wp.array, wp.array]
  + def get\_dof\_positions(self) -> wp.array
  + def get\_dof\_position\_targets(self) -> wp.array
  + def get\_dof\_velocities(self) -> wp.array
  + def get\_dof\_velocity\_targets(self) -> wp.array
  + def set\_world\_poses(self, positions: list | np.ndarray | wp.array | None = None, orientations: list | np.ndarray | wp.array | None = None)
  + def get\_world\_poses(self) -> tuple[wp.array, wp.array]
  + def get\_local\_poses(self) -> tuple[wp.array, wp.array]
  + def set\_local\_poses(self, translations: list | np.ndarray | wp.array | None = None, orientations: list | np.ndarray | wp.array | None = None)
  + def set\_velocities(self, linear\_velocities: list | np.ndarray | wp.array | None = None, angular\_velocities: list | np.ndarray | wp.array | None = None)
  + def get\_velocities(self) -> tuple[wp.array, wp.array]
  + def set\_default\_state(self, positions: list | np.ndarray | wp.array | None = None, orientations: list | np.ndarray | wp.array | None = None, linear\_velocities: list | np.ndarray | wp.array | None = None, angular\_velocities: list | np.ndarray | wp.array | None = None, dof\_positions: float | list | np.ndarray | wp.array | None = None, dof\_velocities: float | list | np.ndarray | wp.array | None = None, dof\_efforts: float | list | np.ndarray | wp.array | None = None)
  + def get\_default\_state(self) -> tuple[wp.array | None, wp.array | None, wp.array | None, wp.array | None, wp.array | None, wp.array | None, wp.array | None]
  + def reset\_to\_default\_state(self)
  + def get\_dof\_drive\_types(self) -> list[list[str]]
  + def set\_dof\_drive\_types(self, types: str | list[list[str]])
  + def set\_dof\_max\_efforts(self, max\_efforts: float | list | np.ndarray | wp.array)
  + def get\_dof\_max\_efforts(self) -> wp.array
  + def set\_dof\_max\_velocities(self, max\_velocities: float | list | np.ndarray | wp.array)
  + def get\_dof\_max\_velocities(self) -> wp.array
  + def set\_dof\_gains(self, stiffnesses: float | list | np.ndarray | wp.array | None = None, dampings: float | list | np.ndarray | wp.array | None = None)
  + def get\_dof\_gains(self) -> tuple[wp.array, wp.array]
  + def switch\_dof\_control\_mode(self, mode: str)
  + def set\_solver\_iteration\_counts(self, position\_counts: int | list | np.ndarray | wp.array | None = None, velocity\_counts: int | list | np.ndarray | wp.array | None = None)
  + def get\_solver\_iteration\_counts(self) -> tuple[wp.array, wp.array]
  + def set\_stabilization\_thresholds(self, thresholds: float | list | np.ndarray | wp.array)
  + def get\_stabilization\_thresholds(self) -> wp.array
  + def set\_enabled\_self\_collisions(self, enabled: bool | list | np.ndarray | wp.array)
  + def get\_enabled\_self\_collisions(self) -> wp.array
  + def set\_sleep\_thresholds(self, thresholds: float | list | np.ndarray | wp.array)
  + def get\_sleep\_thresholds(self) -> wp.array
  + def get\_jacobian\_matrices(self) -> wp.array
  + def get\_mass\_matrices(self) -> wp.array
  + def get\_dof\_coriolis\_and\_centrifugal\_compensation\_forces(self) -> wp.array
  + def get\_dof\_gravity\_compensation\_forces(self) -> wp.array
  + def get\_link\_masses(self) -> wp.array
  + def get\_link\_coms(self) -> tuple[wp.array, wp.array]
  + def get\_link\_inertias(self) -> wp.array
  + def get\_link\_enabled\_gravities(self) -> wp.array
  + def set\_link\_masses(self, masses: float | list | np.ndarray | wp.array)
  + def set\_link\_inertias(self, inertias: list | np.ndarray | wp.array)
  + def set\_link\_coms(self, positions: list | np.ndarray | wp.array | None = None, orientations: list | np.ndarray | wp.array | None = None)
  + def set\_link\_enabled\_gravities(self, enabled: bool | list | np.ndarray | wp.array)
  + def get\_fixed\_tendon\_stiffnesses(self) -> wp.array
  + def get\_fixed\_tendon\_dampings(self) -> wp.array
  + def get\_fixed\_tendon\_limit\_stiffnesses(self) -> wp.array
  + def get\_fixed\_tendon\_limits(self) -> tuple[wp.array, wp.array]
  + def get\_fixed\_tendon\_rest\_lengths(self) -> wp.array
  + def get\_fixed\_tendon\_offsets(self) -> wp.array
  + def set\_fixed\_tendon\_properties(self)
  + def initialize\_cpp\_data\_view(self)
* class BufferDtype(str, Enum)

  + FLOAT: str
  + FLOAT32: str
  + UINT8: str
  + UINT8\_T: str
* class DeformablePrim(XformPrim)

  + def **init**(self, paths: str | list[str])
  + [property] def deformable\_type(self) -> Literal[surface, volume]
  + [property] def simulation\_mesh\_paths(self) -> list[str]
  + [property] def collision\_mesh\_paths(self) -> list[str]
  + [property] def num\_nodes\_per\_element(self) -> int
  + [property] def num\_nodes\_per\_body(self) -> tuple[int, int, int]
  + [property] def num\_elements\_per\_body(self) -> tuple[int, int, int]
  + def is\_physics\_tensor\_entity\_valid(self) -> bool
  + def get\_element\_indices(self) -> tuple[wp.array, wp.array, wp.array]
  + def get\_nodal\_positions(self) -> tuple[wp.array, wp.array, wp.array]
  + def set\_nodal\_positions(self, positions: list | np.ndarray | wp.array | None = None)
  + def get\_nodal\_velocities(self) -> wp.array
  + def set\_nodal\_velocities(self, velocities: list | np.ndarray | wp.array | None = None)
  + def get\_nodal\_kinematic\_position\_targets(self) -> tuple[wp.array, wp.array]
  + def set\_nodal\_kinematic\_position\_targets(self, positions: list | np.ndarray | wp.array | None = None, enabled: bool | list | np.ndarray | wp.array | None = None)
  + def apply\_physics\_materials(self, materials: type[‘PhysicsMaterial’] | list[type[‘PhysicsMaterial’]])
  + def get\_applied\_physics\_materials(self) -> list[type[‘PhysicsMaterial’] | None]
  + def get\_nodal\_rotations(self) -> wp.array
  + def get\_nodal\_gradients(self) -> wp.array
  + def get\_nodal\_stresses(self) -> wp.array
* class GeomPrim(XformPrim)

  + def **init**(self, paths: str | list[str])
  + [property] def geoms(self) -> list[UsdGeom.Gprim]
  + def set\_offsets(self, contact\_offsets: float | list | np.ndarray | wp.array = None, rest\_offsets: float | list | np.ndarray | wp.array = None)
  + def get\_offsets(self) -> tuple[wp.array, wp.array]
  + def set\_torsional\_patch\_radii(self, radii: float | list | np.ndarray | wp.array)
  + def get\_torsional\_patch\_radii(self) -> wp.array
  + def set\_collision\_approximations(self, approximations: str | list[str])
  + def get\_collision\_approximations(self) -> list[str]
  + def set\_enabled\_collisions(self, enabled: bool | list | np.ndarray | wp.array)
  + def get\_enabled\_collisions(self) -> wp.array
  + def apply\_collision\_apis(self)
  + def apply\_physics\_materials(self, materials: type[‘PhysicsMaterial’] | list[type[‘PhysicsMaterial’]])
  + def get\_applied\_physics\_materials(self) -> list[type[‘PhysicsMaterial’] | None]
* class Prim(ABC)

  + def **init**(self, paths: str | list[str])
  + [property] def paths(self) -> list[str]
  + [property] def prims(self) -> list[Usd.Prim]
  + [property] def valid(self) -> bool
  + static def ensure\_api(prims: list[Usd.Prim], api: type, \*args, \*\*kwargs) -> list[type[UsdAPISchemaBase]]
  + static def resolve\_paths(paths: str | list[str], raise\_on\_mixed\_paths: bool = True) -> tuple[list[str], list[str]]
* class RigidPrim(XformPrim)

  + def **init**(self, paths: str | list[str])
  + [property] def num\_shapes(self) -> int
  + [property] def num\_contact\_filters(self) -> int
  + def is\_physics\_tensor\_entity\_valid(self) -> bool
  + def set\_world\_poses(self, positions: list | np.ndarray | wp.array | None = None, orientations: list | np.ndarray | wp.array | None = None)
  + def get\_world\_poses(self) -> tuple[wp.array, wp.array]
  + def get\_local\_poses(self) -> tuple[wp.array, wp.array]
  + def set\_local\_poses(self, translations: list | np.ndarray | wp.array | None = None, orientations: list | np.ndarray | wp.array | None = None)
  + def set\_velocities(self, linear\_velocities: list | np.ndarray | wp.array | None = None, angular\_velocities: list | np.ndarray | wp.array | None = None)
  + def get\_velocities(self) -> tuple[wp.array, wp.array]
  + def apply\_forces(self, forces: list | np.ndarray | wp.array)
  + def apply\_forces\_and\_torques\_at\_pos(self, forces: list | np.ndarray | wp.array | None = None, torques: list | np.ndarray | wp.array | None = None)
  + def get\_masses(self) -> wp.array
  + def get\_coms(self) -> tuple[wp.array, wp.array]
  + def get\_inertias(self) -> wp.array
  + def set\_masses(self, masses: float | list | np.ndarray | wp.array)
  + def set\_inertias(self, inertias: list | np.ndarray | wp.array)
  + def set\_coms(self, positions: list | np.ndarray | wp.array | None = None, orientations: list | np.ndarray | wp.array | None = None)
  + def set\_densities(self, densities: float | list | np.ndarray | wp.array)
  + def get\_densities(self) -> wp.array
  + def set\_sleep\_thresholds(self, thresholds: float | list | np.ndarray | wp.array)
  + def get\_sleep\_thresholds(self) -> wp.array
  + def set\_enabled\_rigid\_bodies(self, enabled: bool | list | np.ndarray | wp.array)
  + def get\_enabled\_rigid\_bodies(self) -> wp.array
  + def set\_enabled\_gravities(self, enabled: bool | list | np.ndarray | wp.array)
  + def get\_enabled\_gravities(self) -> wp.array
  + def set\_enabled\_contact\_tracking(self, enabled: bool | list | np.ndarray | wp.array)
  + def get\_enabled\_contact\_tracking(self) -> wp.array
  + def get\_net\_contact\_forces(self) -> wp.array
  + def get\_contact\_force\_matrix(self) -> wp.array
  + def get\_contact\_force\_data(self) -> tuple[wp.array, wp.array, wp.array, wp.array, wp.array, wp.array]
  + def get\_friction\_data(self) -> tuple[wp.array, wp.array, wp.array, wp.array]
  + def get\_raw\_contact\_data(self) -> tuple[wp.array, wp.array, wp.array, wp.array, wp.array, wp.array, wp.array]
  + def get\_actor\_paths\_from\_ids(self, actor\_ids: wp.array) -> list[str]
  + def set\_default\_state(self, positions: list | np.ndarray | wp.array | None = None, orientations: list | np.ndarray | wp.array | None = None, linear\_velocities: list | np.ndarray | wp.array | None = None, angular\_velocities: list | np.ndarray | wp.array | None = None)
  + def get\_default\_state(self) -> tuple[wp.array | None, wp.array | None, wp.array | None, wp.array | None]
  + def reset\_to\_default\_state(self)
  + def initialize\_cpp\_data\_view(self)
* class XformPrim(Prim)

  + def **init**(self, paths: str | list[str])
  + [property] def is\_non\_root\_articulation\_link(self) -> bool
  + def set\_visibilities(self, visibilities: bool | list | np.ndarray | wp.array)
  + def get\_visibilities(self) -> wp.array
  + def get\_default\_state(self) -> tuple[wp.array | None, wp.array | None]
  + def set\_default\_state(self, positions: list | np.ndarray | wp.array | None = None, orientations: list | np.ndarray | wp.array | None = None)
  + def apply\_visual\_materials(self, materials: type[‘VisualMaterial’] | list[type[‘VisualMaterial’]])
  + def get\_applied\_visual\_materials(self) -> list[type[‘VisualMaterial’] | None]
  + def get\_world\_poses(self) -> tuple[wp.array, wp.array]
  + def set\_world\_poses(self, positions: list | np.ndarray | wp.array | None = None, orientations: list | np.ndarray | wp.array | None = None)
  + def get\_local\_poses(self) -> tuple[wp.array, wp.array]
  + def set\_local\_poses(self, translations: list | np.ndarray | wp.array | None = None, orientations: list | np.ndarray | wp.array | None = None)
  + def set\_local\_scales(self, scales: list | np.ndarray | wp.array | None = None)
  + def get\_local\_scales(self) -> wp.array
  + def reset\_xform\_op\_properties(self)
  + def reset\_to\_default\_state(self)

On this page

* [Classes](#classes)