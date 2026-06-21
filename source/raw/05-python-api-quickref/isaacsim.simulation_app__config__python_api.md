---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/py/source/extensions/isaacsim.simulation_app/config/python_api.html
title: "simulation_app API"
section: "Core"
module: "05-python-api-quickref"
checksum: "c35689d7ae2b1d0b"
fetched: "2026-06-21T14:14:27"
---

* Public API for module isaacsim.simulation\_app:

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Public API for module isaacsim.simulation\_app:

## Classes

* class SimulationApp

  + DEFAULT\_LAUNCHER\_CONFIG: Dict
  + RENDERER\_DEFAULTS: Dict
  + def **init**(self, launch\_config: dict = None, experience: str = ‘’)
  + def update(self)
  + def set\_setting(self, setting: str, value: Any)
  + def reset\_render\_settings(self)
  + def run\_coroutine(self, coroutine: asyncio.Coroutine, run\_until\_complete: bool = True) -> asyncio.Task | asyncio.Future | Any
  + def close(self, wait\_for\_replicator: bool = True, skip\_cleanup: bool = False, exit\_code: int = 0)
  + def is\_running(self) -> bool
  + def is\_exiting(self) -> bool
  + [property] def app(self) -> omni.kit.app.IApp
  + [property] def context(self) -> omni.usd.UsdContext
* class AppFramework

  + def **init**(self, name: str = ‘kit’, argv: list[str] | None = None)
  + def update(self)
  + def close(self)
  + [property] def app(self) -> omni.kit.app.IApp
  + [property] def framework(self) -> typing.Any

On this page

* [Classes](#classes)