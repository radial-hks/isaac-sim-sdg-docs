---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/py/source/extensions/isaacsim.core.cloner/config/python_api.html
title: "core.cloner API"
section: "Core"
module: "05-python-api-quickref"
checksum: "a62510e0bc7a5266"
fetched: "2026-06-21T14:14:27"
---

* Public API for module isaacsim.core.cloner:

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Public API for module isaacsim.core.cloner:

## Classes

* class Cloner

  + def **init**(self, stage: Usd.Stage = None)
  + def define\_base\_env(self, base\_env\_path: str)
  + def generate\_paths(self, root\_path: str, num\_paths: int) -> list[str]
  + def replicate\_physics(self, source\_prim\_path: str, prim\_paths: list, base\_env\_path: str, root\_path: str, enable\_env\_ids: bool = False, clone\_in\_fabric: bool = False)
  + def disable\_change\_listener(self)
  + def enable\_change\_listener(self)
  + def clone(self, source\_prim\_path: str, prim\_paths: List[str], positions: Union[np.ndarray, torch.Tensor] = None, orientations: Union[np.ndarray, torch.Tensor] = None, replicate\_physics: bool = False, base\_env\_path: str = None, root\_path: str = None, copy\_from\_source: bool = False, unregister\_physics\_replication: bool = False, enable\_env\_ids: bool = False, clone\_in\_fabric: bool = False)
  + def filter\_collisions(self, physicsscene\_path: str, collision\_root\_path: str, prim\_paths: List[str], global\_paths: List[str] = [])
* class GridCloner(Cloner)

  + def **init**(self, spacing: float, num\_per\_row: int = -1, stage: Usd.Stage = None)
  + def get\_clone\_transforms(self, num\_clones: int, position\_offsets: np.ndarray = None, orientation\_offsets: np.ndarray = None)
  + def clone(self, source\_prim\_path: str, prim\_paths: List[str], position\_offsets: np.ndarray = None, orientation\_offsets: np.ndarray = None, replicate\_physics: bool = False, base\_env\_path: str = None, root\_path: str = None, copy\_from\_source: bool = False, enable\_env\_ids: bool = False, clone\_in\_fabric: bool = False)

On this page

* [Classes](#classes)