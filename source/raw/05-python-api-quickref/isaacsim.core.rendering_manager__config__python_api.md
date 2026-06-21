---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/py/source/extensions/isaacsim.core.rendering_manager/config/python_api.html
title: "core.rendering_manager API"
section: "Core"
module: "05-python-api-quickref"
checksum: "daf33e5a9336e6d7"
fetched: "2026-06-21T14:14:27"
---

* Public API for module isaacsim.core.rendering\_manager:

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Public API for module isaacsim.core.rendering\_manager:

## Classes

* class RenderingEvent(Enum)

  + NEW\_FRAME: str
* class RenderingManager

  + class def render(cls)
  + class async def render\_async(cls)
  + class def set\_dt(cls, dt: float)
  + class def get\_dt(cls) -> float
  + class def register\_callback(cls, event: RenderingEvent) -> int
  + class def deregister\_callback(cls, uid: int)
  + class def deregister\_all\_callbacks(cls)
* class ViewportManager

  + class def wait\_for\_viewport(cls) -> tuple[bool, int]
  + class async def wait\_for\_viewport\_async(cls) -> tuple[bool, int]
  + class def set\_camera(cls, camera: str | Usd.Prim | UsdGeom.Camera)
  + class def get\_camera(cls, render\_product\_or\_viewport: str | Usd.Prim | UsdRender.Product | ‘ViewportAPI’ | None = None) -> UsdGeom.Camera
  + class def get\_viewport\_api(cls, render\_product\_or\_viewport: str | Usd.Prim | UsdRender.Product | ‘ViewportAPI’ | None = None) -> ‘ViewportAPI’ | None
  + class def get\_render\_product(cls, render\_product\_or\_viewport: str | Usd.Prim | UsdRender.Product | ‘ViewportAPI’ | None = None) -> UsdRender.Product | None
  + class def get\_resolution(cls, render\_product\_or\_viewport: str | Usd.Prim | UsdRender.Product | ‘ViewportAPI’ | None = None) -> tuple[int, int]
  + class def set\_resolution(cls, resolution: tuple[int, int] | str)
  + class def create\_viewport\_window(cls) -> ViewportWindow
  + class def get\_viewport\_windows(cls) -> list
  + class def destroy\_viewport\_windows(cls) -> list[str]
  + class def set\_camera\_view(cls, camera: str | Usd.Prim | UsdGeom.Camera)

On this page

* [Classes](#classes)