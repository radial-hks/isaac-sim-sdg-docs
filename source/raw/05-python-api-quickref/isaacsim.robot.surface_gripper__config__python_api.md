---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/py/source/extensions/isaacsim.robot.surface_gripper/config/python_api.html
title: "robot.surface_gripper API"
section: "Robot"
module: "05-python-api-quickref"
checksum: "772d1f1d373f3d3a"
fetched: "2026-06-21T14:14:27"
---

* Public API for module isaacsim.robot.surface\_gripper:

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Public API for module isaacsim.robot.surface\_gripper:

## Classes

* class GripperView(XformPrim)

  + def **init**(self, paths: str = None, max\_grip\_distance: np.ndarray | wp.array | None = None, coaxial\_force\_limit: np.ndarray | wp.array | None = None, shear\_force\_limit: np.ndarray | wp.array | None = None, retry\_interval: np.ndarray | wp.array | None = None, positions: np.ndarray | wp.array | None = None, translations: np.ndarray | wp.array | None = None, orientations: np.ndarray | wp.array | None = None, scales: np.ndarray | wp.array | None = None, reset\_xform\_op\_properties: bool = True)
  + def get\_surface\_gripper\_status(self, indices: list | np.ndarray | wp.array | None = None) -> list[str]
  + def get\_gripped\_objects(self, indices: list | np.ndarray | wp.array | None = None) -> list[str]
  + def get\_surface\_gripper\_properties(self, indices: list | np.ndarray | wp.array | None = None) -> tuple[list[float], list[float], list[float], list[float]]
  + def apply\_gripper\_action(self, values: list[float], indices: list | np.ndarray | wp.array | None = None)
  + def set\_surface\_gripper\_properties(self, max\_grip\_distance: list[float] | None = None, coaxial\_force\_limit: list[float] | None = None, shear\_force\_limit: list[float] | None = None, retry\_interval: list[float] | None = None, indices: list | np.ndarray | wp.array | None = None)

## Functions

* def create\_surface\_gripper(stage: Usd.Stage, prim\_path: str) -> Usd.Prim

On this page

* [Classes](#classes)
* [Functions](#functions)