---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/py/source/extensions/isaacsim.core.experimental.materials/config/python_api.html
title: "core.experimental.materials API"
section: "Core"
module: "05-python-api-quickref"
checksum: "4e95b913ec4bf47e"
fetched: "2026-06-21T14:14:26"
---

* Public API for module isaacsim.core.experimental.materials:

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Public API for module isaacsim.core.experimental.materials:

## Classes

* class PhysicsMaterial(Prim, ABC)

  + def **init**(self, paths: str | list[str])
  + [property] def materials(self) -> list[UsdShade.Material]
  + static def are\_of\_type(paths: str | Usd.Prim | list[str | Usd.Prim]) -> wp.array
  + static def fetch\_instances(paths: str | Usd.Prim | list[str | Usd.Prim]) -> list[PhysicsMaterial | None]
* class RigidBodyMaterial(PhysicsMaterial)

  + def **init**(self, paths: str | list[str])
  + def set\_friction\_coefficients(self, static\_frictions: float | list | np.ndarray | wp.array = None, dynamic\_frictions: float | list | np.ndarray | wp.array = None)
  + def get\_friction\_coefficients(self) -> tuple[wp.array, wp.array]
  + def set\_restitution\_coefficients(self, restitutions: float | list | np.ndarray | wp.array)
  + def get\_restitution\_coefficients(self) -> wp.array
  + def set\_densities(self, densities: float | list | np.ndarray | wp.array)
  + def get\_densities(self) -> wp.array
  + def set\_combine\_modes(self, frictions: Literal[‘average’, ‘max’, ‘min’, ‘multiply’] | list[Literal[‘average’, ‘max’, ‘min’, ‘multiply’]] | None = None, restitutions: Literal[‘average’, ‘max’, ‘min’, ‘multiply’] | list[Literal[‘average’, ‘max’, ‘min’, ‘multiply’]] | None = None, dampings: Literal[‘average’, ‘max’, ‘min’, ‘multiply’] | list[Literal[‘average’, ‘max’, ‘min’, ‘multiply’]] | None = None)
  + def get\_combine\_modes(self) -> tuple[list[Literal[average, max, min, multiply]], list[Literal[average, max, min, multiply]], list[Literal[average, max, min, multiply]]]
  + def set\_enabled\_compliant\_contacts(self, enabled: bool | list | np.ndarray | wp.array)
  + def get\_enabled\_compliant\_contacts(self) -> wp.array
  + def set\_compliant\_contact\_gains(self, stiffnesses: float | list | np.ndarray | wp.array | None = None, dampings: float | list | np.ndarray | wp.array | None = None)
  + def get\_compliant\_contact\_gains(self) -> tuple[wp.array, wp.array]
  + static def are\_of\_type(paths: str | Usd.Prim | list[str | Usd.Prim]) -> wp.array
* class SurfaceDeformableMaterial(PhysicsMaterial)

  + def **init**(self, paths: str | list[str])
  + def set\_friction\_coefficients(self, static\_frictions: float | list | np.ndarray | wp.array = None, dynamic\_frictions: float | list | np.ndarray | wp.array = None)
  + def get\_friction\_coefficients(self) -> tuple[wp.array, wp.array]
  + def set\_youngs\_moduli(self, youngs\_moduli: float | list | np.ndarray | wp.array)
  + def get\_youngs\_moduli(self) -> wp.array
  + def set\_poissons\_ratios(self, poissons\_ratios: float | list | np.ndarray | wp.array)
  + def get\_poissons\_ratios(self) -> wp.array
  + def set\_densities(self, densities: float | list | np.ndarray | wp.array)
  + def get\_densities(self) -> wp.array
  + def set\_surface\_thicknesses(self, surface\_thicknesses: float | list | np.ndarray | wp.array)
  + def get\_surface\_thicknesses(self) -> wp.array
  + def set\_surface\_stiffnesses(self, stretch\_stiffnesses: float | list | np.ndarray | wp.array | None = None, shear\_stiffnesses: float | list | np.ndarray | wp.array | None = None, bend\_stiffnesses: float | list | np.ndarray | wp.array | None = None)
  + def get\_surface\_stiffnesses(self) -> tuple[wp.array, wp.array, wp.array]
  + static def are\_of\_type(paths: str | Usd.Prim | list[str | Usd.Prim]) -> wp.array
* class VolumeDeformableMaterial(PhysicsMaterial)

  + def **init**(self, paths: str | list[str])
  + def set\_friction\_coefficients(self, static\_frictions: float | list | np.ndarray | wp.array = None, dynamic\_frictions: float | list | np.ndarray | wp.array = None)
  + def get\_friction\_coefficients(self) -> tuple[wp.array, wp.array]
  + def set\_youngs\_moduli(self, youngs\_moduli: float | list | np.ndarray | wp.array)
  + def get\_youngs\_moduli(self) -> wp.array
  + def set\_poissons\_ratios(self, poissons\_ratios: float | list | np.ndarray | wp.array)
  + def get\_poissons\_ratios(self) -> wp.array
  + def set\_densities(self, densities: float | list | np.ndarray | wp.array)
  + def get\_densities(self) -> wp.array
  + static def are\_of\_type(paths: str | Usd.Prim | list[str | Usd.Prim]) -> wp.array
* class OmniGlassMaterial(VisualMaterial)

  + def **init**(self, paths: str | list[str])
  + static def are\_of\_type(paths: str | Usd.Prim | list[str | Usd.Prim]) -> wp.array
* class OmniPbrMaterial(VisualMaterial)

  + def **init**(self, paths: str | list[str])
  + static def are\_of\_type(paths: str | Usd.Prim | list[str | Usd.Prim]) -> wp.array
* class PreviewSurfaceMaterial(VisualMaterial)

  + def **init**(self, paths: str | list[str])
  + static def are\_of\_type(paths: str | Usd.Prim | list[str | Usd.Prim]) -> wp.array
* class VisualMaterial(Prim, ABC)

  + def **init**(self, paths: str | list[str])
  + [property] def materials(self) -> list[UsdShade.Material]
  + [property] def shaders(self) -> list[UsdShade.Shader]
  + def set\_input\_values(self, name: str, values: str | bool | int | float | list | np.ndarray | wp.array)
  + def get\_input\_values(self, name: str) -> wp.array
  + static def are\_of\_type(paths: str | Usd.Prim | list[str | Usd.Prim]) -> wp.array
  + static def fetch\_instances(paths: str | Usd.Prim | list[str | Usd.Prim]) -> list[VisualMaterial | None]

On this page

* [Classes](#classes)