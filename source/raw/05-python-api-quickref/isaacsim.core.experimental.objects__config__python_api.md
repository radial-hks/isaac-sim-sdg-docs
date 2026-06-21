---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/py/source/extensions/isaacsim.core.experimental.objects/config/python_api.html
title: "core.experimental.objects API"
section: "Core"
module: "05-python-api-quickref"
checksum: "ed723a5e0cc2e360"
fetched: "2026-06-21T14:14:26"
---

* Public API for module isaacsim.core.experimental.objects:

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Public API for module isaacsim.core.experimental.objects:

## Classes

* class Camera(XformPrim)

  + def **init**(self, paths: str | list[str])
  + static def are\_of\_type(paths: str | Usd.Prim | list[str | Usd.Prim]) -> wp.array
  + def set\_focal\_lengths(self, focal\_lengths: float | list | np.ndarray | wp.array)
  + def get\_focal\_lengths(self) -> wp.array
  + def set\_focus\_distances(self, focus\_distances: float | list | np.ndarray | wp.array)
  + def get\_focus\_distances(self) -> wp.array
  + def set\_stereo\_roles(self, roles: Literal[‘mono’, ‘left’, ‘right’] | list[Literal[‘mono’, ‘left’, ‘right’]])
  + def get\_stereo\_roles(self) -> list[Literal[mono, left, right]]
  + def set\_fstops(self, fstops: float | list | np.ndarray | wp.array)
  + def get\_fstops(self) -> wp.array
  + def set\_apertures(self, horizontal\_apertures: float | list | np.ndarray | wp.array = None, vertical\_apertures: float | list | np.ndarray | wp.array = None)
  + def get\_apertures(self) -> tuple[wp.array, wp.array]
  + def set\_aperture\_offsets(self, horizontal\_offsets: float | list | np.ndarray | wp.array = None, vertical\_offsets: float | list | np.ndarray | wp.array = None)
  + def get\_aperture\_offsets(self) -> tuple[wp.array, wp.array]
  + def set\_projections(self, projections: Literal[‘perspective’, ‘orthographic’] | list[Literal[‘perspective’, ‘orthographic’]])
  + def get\_projections(self) -> list[Literal[perspective, orthographic]]
  + def set\_clipping\_ranges(self, near\_distances: float | list | np.ndarray | wp.array = None, far\_distances: float | list | np.ndarray | wp.array = None)
  + def get\_clipping\_ranges(self) -> tuple[wp.array, wp.array]
  + def set\_shutter\_times(self, open\_times: float | list | np.ndarray | wp.array = None, close\_times: float | list | np.ndarray | wp.array = None)
  + def get\_shutter\_times(self) -> tuple[wp.array, wp.array]
  + def enforce\_square\_pixels(self, resolutions: list | np.ndarray | wp.array)
* class GroundPlane(XformPrim)

  + def **init**(self, paths: str | list[str])
  + [property] def planes(self) -> Plane
  + [property] def meshes(self) -> Mesh
  + def set\_offsets(self, contact\_offsets: float | list | np.ndarray | wp.array = None, rest\_offsets: float | list | np.ndarray | wp.array = None)
  + def get\_offsets(self) -> tuple[wp.array, wp.array]
  + def set\_torsional\_patch\_radii(self, radii: float | list | np.ndarray | wp.array)
  + def get\_torsional\_patch\_radii(self) -> wp.array
  + def set\_enabled\_collisions(self, enabled: bool | list | np.ndarray | wp.array)
  + def get\_enabled\_collisions(self) -> wp.array
  + def apply\_physics\_materials(self, materials: type[‘PhysicsMaterial’] | list[type[‘PhysicsMaterial’]])
  + def get\_applied\_physics\_materials(self) -> list[type[‘PhysicsMaterial’] | None]
  + def apply\_visual\_templates(self, templates: TEMPLATE | list[TEMPLATE])
* class CylinderLight(Light)

  + def **init**(self, paths: str | list[str])
  + def set\_lengths(self, lengths: float | list | np.ndarray | wp.array)
  + def get\_lengths(self) -> wp.array
  + def set\_radii(self, radii: float | list | np.ndarray | wp.array)
  + def get\_radii(self) -> wp.array
  + def set\_enabled\_treat\_as\_lines(self, enabled: bool | list | np.ndarray | wp.array)
  + def get\_enabled\_treat\_as\_lines(self) -> wp.array
  + static def are\_of\_type(paths: str | Usd.Prim | list[str | Usd.Prim]) -> wp.array
* class DiskLight(Light)

  + def **init**(self, paths: str | list[str])
  + def set\_radii(self, radii: float | list | np.ndarray | wp.array)
  + def get\_radii(self) -> wp.array
  + static def are\_of\_type(paths: str | Usd.Prim | list[str | Usd.Prim]) -> wp.array
* class DistantLight(Light)

  + def **init**(self, paths: str | list[str])
  + def set\_angles(self, angles: float | list | np.ndarray | wp.array)
  + def get\_angles(self) -> wp.array
  + static def are\_of\_type(paths: str | Usd.Prim | list[str | Usd.Prim]) -> wp.array
* class DomeLight(Light)

  + def **init**(self, paths: str | list[str])
  + def set\_guide\_radii(self, radii: float | list | np.ndarray | wp.array)
  + def get\_guide\_radii(self) -> wp.array
  + def set\_texture\_files(self, texture\_files: str | list[str])
  + def get\_texture\_files(self) -> list[str]
  + def set\_texture\_formats(self, texture\_formats: Literal[‘automatic’, ‘latlong’, ‘mirroredBall’, ‘angular’, ‘cubeMapVerticalCross’] | list[Literal[‘automatic’, ‘latlong’, ‘mirroredBall’, ‘angular’, ‘cubeMapVerticalCross’]])
  + def get\_texture\_formats(self) -> list[Literal[automatic, latlong, mirroredBall, angular, cubeMapVerticalCross]]
  + static def are\_of\_type(paths: str | Usd.Prim | list[str | Usd.Prim]) -> wp.array
* class Light(XformPrim, ABC)

  + def **init**(self, paths: str | list[str])
  + [property] def lights(self) -> list[UsdLux.Light]
  + def set\_intensities(self, intensities: float | list | np.ndarray | wp.array)
  + def get\_intensities(self) -> wp.array
  + def set\_exposures(self, exposures: float | list | np.ndarray | wp.array)
  + def get\_exposures(self) -> wp.array
  + def set\_multipliers(self, diffuse\_multipliers: float | list | np.ndarray | wp.array = None, specular\_multipliers: float | list | np.ndarray | wp.array = None)
  + def get\_multipliers(self) -> tuple[wp.array, wp.array]
  + def set\_enabled\_normalizations(self, enabled: bool | list | np.ndarray | wp.array)
  + def get\_enabled\_normalizations(self) -> wp.array
  + def set\_enabled\_color\_temperatures(self, enabled: bool | list | np.ndarray | wp.array)
  + def get\_enabled\_color\_temperatures(self) -> wp.array
  + def set\_color\_temperatures(self, color\_temperatures: float | list | np.ndarray | wp.array)
  + def get\_color\_temperatures(self) -> wp.array
  + def set\_colors(self, colors: list | np.ndarray | wp.array)
  + def get\_colors(self) -> wp.array
  + static def are\_of\_type(paths: str | Usd.Prim | list[str | Usd.Prim]) -> wp.array
  + static def fetch\_instances(paths: str | Usd.Prim | list[str | Usd.Prim]) -> list[Light | None]
* class RectLight(Light)

  + def **init**(self, paths: str | list[str])
  + def set\_widths(self, widths: float | list | np.ndarray | wp.array)
  + def get\_widths(self) -> wp.array
  + def set\_heights(self, heights: float | list | np.ndarray | wp.array)
  + def get\_heights(self) -> wp.array
  + def set\_texture\_files(self, texture\_files: str | list[str])
  + def get\_texture\_files(self) -> list[str | None]
  + static def are\_of\_type(paths: str | Usd.Prim | list[str | Usd.Prim]) -> wp.array
* class SphereLight(Light)

  + def **init**(self, paths: str | list[str])
  + def set\_radii(self, radii: float | list | np.ndarray | wp.array)
  + def get\_radii(self) -> wp.array
  + def set\_enabled\_treat\_as\_points(self, enabled: bool | list | np.ndarray | wp.array)
  + def get\_enabled\_treat\_as\_points(self) -> wp.array
  + static def are\_of\_type(paths: str | Usd.Prim | list[str | Usd.Prim]) -> wp.array
* class Mesh(XformPrim)

  + def **init**(self, paths: str | list[str])
  + [property] def geoms(self) -> list[UsdGeom.Mesh]
  + [property] def num\_faces(self) -> list[int]
  + static def update\_extents(geoms: list[UsdGeom.Mesh])
  + static def are\_of\_type(paths: str | Usd.Prim | list[str | Usd.Prim]) -> wp.array
  + static def fetch\_instances(paths: str | Usd.Prim | list[str | Usd.Prim]) -> list[Mesh | None]
  + def set\_display\_colors(self, colors: str | list | np.ndarray | wp.array)
  + def set\_points(self, points: list[list | np.ndarray | wp.array])
  + def get\_points(self) -> list[wp.array]
  + def set\_normals(self, normals: list[list | np.ndarray | wp.array])
  + def get\_normals(self) -> list[wp.array]
  + def set\_face\_specs(self, vertex\_indices: list[list | np.ndarray | wp.array] | None = None, vertex\_counts: list[list | np.ndarray | wp.array] | None = None, varying\_linear\_interpolations: list[Literal[‘none’, ‘cornersOnly’, ‘cornersPlus1’, ‘cornersPlus2’, ‘boundaries’, ‘all’]] | None = None, hole\_indices: list[list | np.ndarray | wp.array] | None = None)
  + def get\_face\_specs(self) -> tuple[list[wp.array], list[wp.array], list[Literal[none, cornersOnly, cornersPlus1, cornersPlus2, boundaries, all]], list[wp.array]]
  + def set\_crease\_specs(self, crease\_indices: list[list | np.ndarray | wp.array], crease\_lengths: list[list | np.ndarray | wp.array], crease\_sharpnesses: list[list | np.ndarray | wp.array])
  + def get\_crease\_specs(self) -> tuple[list[wp.array], list[wp.array], list[wp.array]]
  + def set\_corner\_specs(self, corner\_indices: list[list | np.ndarray | wp.array], corner\_sharpnesses: list[list | np.ndarray | wp.array])
  + def get\_corner\_specs(self) -> tuple[list[wp.array], list[wp.array]]
  + def set\_subdivision\_specs(self, subdivision\_schemes: list[Literal[‘catmullClark’, ‘loop’, ‘bilinear’, ‘none’]] | None = None, interpolate\_boundaries: list[Literal[‘none’, ‘edgeOnly’, ‘edgeAndCorner’]] | None = None, triangle\_subdivision\_rules: list[Literal[‘catmullClark’, ‘smooth’]] | None = None)
  + def get\_subdivision\_specs(self) -> tuple[list[Literal[catmullClark, loop, bilinear, none]], list[Literal[none, edgeOnly, edgeAndCorner]], list[Literal[catmullClark, smooth]]]
* class Capsule(Shape)

  + def **init**(self, paths: str | list[str])
  + static def update\_extents(geoms: list[UsdGeom.Capsule])
  + static def are\_of\_type(paths: str | Usd.Prim | list[str | Usd.Prim]) -> wp.array
  + def set\_radii(self, radii: float | list | np.ndarray | wp.array)
  + def get\_radii(self) -> wp.array
  + def set\_heights(self, heights: float | list | np.ndarray | wp.array)
  + def get\_heights(self) -> wp.array
  + def set\_axes(self, axes: Literal[‘X’, ‘Y’, ‘Z’] | list[Literal[‘X’, ‘Y’, ‘Z’]])
  + def get\_axes(self) -> list[Literal[X, Y, Z]]
* class Cone(Shape)

  + def **init**(self, paths: str | list[str])
  + static def update\_extents(geoms: list[UsdGeom.Cone])
  + static def are\_of\_type(paths: str | Usd.Prim | list[str | Usd.Prim]) -> wp.array
  + def set\_radii(self, radii: float | list | np.ndarray | wp.array)
  + def get\_radii(self) -> wp.array
  + def set\_heights(self, heights: float | list | np.ndarray | wp.array)
  + def get\_heights(self) -> wp.array
  + def set\_axes(self, axes: Literal[‘X’, ‘Y’, ‘Z’] | list[Literal[‘X’, ‘Y’, ‘Z’]])
  + def get\_axes(self) -> list[Literal[X, Y, Z]]
* class Cube(Shape)

  + def **init**(self, paths: str | list[str])
  + static def update\_extents(geoms: list[UsdGeom.Cube])
  + static def are\_of\_type(paths: str | Usd.Prim | list[str | Usd.Prim]) -> wp.array
  + def set\_sizes(self, sizes: float | list | np.ndarray | wp.array)
  + def get\_sizes(self) -> wp.array
* class Cylinder(Shape)

  + def **init**(self, paths: str | list[str])
  + static def update\_extents(geoms: list[UsdGeom.Cylinder])
  + static def are\_of\_type(paths: str | Usd.Prim | list[str | Usd.Prim]) -> wp.array
  + def set\_radii(self, radii: float | list | np.ndarray | wp.array)
  + def get\_radii(self) -> wp.array
  + def set\_heights(self, heights: float | list | np.ndarray | wp.array)
  + def get\_heights(self) -> wp.array
  + def set\_axes(self, axes: Literal[‘X’, ‘Y’, ‘Z’] | list[Literal[‘X’, ‘Y’, ‘Z’]])
  + def get\_axes(self) -> list[Literal[X, Y, Z]]
* class Plane(Shape)

  + def **init**(self, paths: str | list[str])
  + static def update\_extents(geoms: list[UsdGeom.Plane])
  + static def are\_of\_type(paths: str | Usd.Prim | list[str | Usd.Prim]) -> wp.array
  + def set\_widths(self, widths: float | list | np.ndarray | wp.array)
  + def get\_widths(self) -> wp.array
  + def set\_lengths(self, lengths: float | list | np.ndarray | wp.array)
  + def get\_lengths(self) -> wp.array
  + def set\_axes(self, axes: Literal[‘X’, ‘Y’, ‘Z’] | list[Literal[‘X’, ‘Y’, ‘Z’]])
  + def get\_axes(self) -> list[Literal[X, Y, Z]]
* class Shape(XformPrim, ABC)

  + def **init**(self, paths: str | list[str])
  + [property] def geoms(self) -> list[UsdGeom.Gprim]
  + static def update\_extents(geoms: list[UsdGeom.Gprim])
  + static def are\_of\_type(paths: str | Usd.Prim | list[str | Usd.Prim]) -> wp.array
  + static def fetch\_instances(paths: str | Usd.Prim | list[str | Usd.Prim]) -> list[Shape | None]
  + def set\_display\_colors(self, colors: str | list | np.ndarray | wp.array)
* class Sphere(Shape)

  + def **init**(self, paths: str | list[str])
  + static def update\_extents(geoms: list[UsdGeom.Sphere])
  + static def are\_of\_type(paths: str | Usd.Prim | list[str | Usd.Prim]) -> wp.array
  + def set\_radii(self, radii: float | list | np.ndarray | wp.array)
  + def get\_radii(self) -> wp.array

On this page

* [Classes](#classes)