---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/py/source/extensions/isaacsim.replicator.mobility_gen.examples/config/python_api.html
title: "replicator.mobility_gen.examples API"
section: "Replicator"
module: "05-python-api-quickref"
checksum: "b2b46890beedd5aa"
fetched: "2026-06-21T14:14:27"
---

* Public API for module isaacsim.replicator.mobility\_gen.examples:

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Public API for module isaacsim.replicator.mobility\_gen.examples:

## Classes

* class HawkCamera(Module)

  + usd\_url: str
  + resolution: Tuple[int, int]
  + left\_camera\_path: str
  + right\_camera\_path: str
  + def **init**(self, left: MobilityGenCamera, right: MobilityGenCamera)
  + class def build(cls, prim\_path: str) -> HawkCamera
  + class def attach(cls, prim\_path: str) -> HawkCamera
* class WheeledMobilityGenRobot(MobilityGenRobot)

  + wheel\_dof\_names: List[str]
  + usd\_url: str
  + chassis\_subpath: str
  + wheel\_radius: float
  + wheel\_base: float
  + def **init**(self, prim\_path: str, articulation: Articulation, controller: DifferentialController, front\_camera: Module | None = None)
  + class def build(cls, prim\_path: str) -> WheeledRobot
  + def write\_action(self, step\_size: float)
* class PolicyMobilityGenRobot(MobilityGenRobot)

  + usd\_url: str
  + articulation\_path: str
  + def **init**(self, prim\_path: str, articulation: Articulation, controller: Union[H1FlatTerrainPolicy, SpotFlatTerrainPolicy], front\_camera: Module | None = None)
  + class def build\_policy(cls, prim\_path: str)
  + class def build(cls, prim\_path: str)
  + def write\_action(self, step\_size: float)
  + def set\_pose\_2d(self, pose: Pose2d)
* class JetbotRobot(WheeledMobilityGenRobot)

  + physics\_dt: float
  + z\_offset: float
  + chase\_camera\_base\_path: str
  + chase\_camera\_x\_offset: float
  + chase\_camera\_z\_offset: float
  + chase\_camera\_tilt\_angle: float
  + occupancy\_map\_radius: float
  + occupancy\_map\_z\_min: float
  + occupancy\_map\_z\_max: float
  + occupancy\_map\_cell\_size: float
  + occupancy\_map\_collision\_radius: float
  + front\_camera\_base\_path: str
  + front\_camera\_rotation: Tuple
  + front\_camera\_translation: Tuple
  + front\_camera\_type: HawkCamera
  + keyboard\_linear\_velocity\_gain: float
  + keyboard\_angular\_velocity\_gain: float
  + gamepad\_linear\_velocity\_gain: float
  + gamepad\_angular\_velocity\_gain: float
  + random\_action\_linear\_velocity\_range: Tuple[float, float]
  + random\_action\_angular\_velocity\_range: Tuple[float, float]
  + random\_action\_linear\_acceleration\_std: float
  + random\_action\_angular\_acceleration\_std: float
  + random\_action\_grid\_pose\_sampler\_grid\_size: float
  + path\_following\_speed: float
  + path\_following\_angular\_gain: float
  + path\_following\_stop\_distance\_threshold: float
  + path\_following\_forward\_angle\_threshold: Unknown
  + path\_following\_target\_point\_offset\_meters: float
  + wheel\_dof\_names: List[str]
  + usd\_url: str
  + chassis\_subpath: str
  + wheel\_base: float
  + wheel\_radius: float
* class CarterRobot(WheeledMobilityGenRobot)

  + physics\_dt: float
  + z\_offset: float
  + chase\_camera\_base\_path: str
  + chase\_camera\_x\_offset: float
  + chase\_camera\_z\_offset: float
  + chase\_camera\_tilt\_angle: float
  + occupancy\_map\_radius: float
  + occupancy\_map\_z\_min: float
  + occupancy\_map\_z\_max: float
  + occupancy\_map\_cell\_size: float
  + occupancy\_map\_collision\_radius: float
  + front\_camera\_base\_path: str
  + front\_camera\_rotation: Tuple
  + front\_camera\_translation: Tuple
  + front\_camera\_type: HawkCamera
  + keyboard\_linear\_velocity\_gain: float
  + keyboard\_angular\_velocity\_gain: float
  + gamepad\_linear\_velocity\_gain: float
  + gamepad\_angular\_velocity\_gain: float
  + random\_action\_linear\_velocity\_range: Tuple[float, float]
  + random\_action\_angular\_velocity\_range: Tuple[float, float]
  + random\_action\_linear\_acceleration\_std: float
  + random\_action\_angular\_acceleration\_std: float
  + random\_action\_grid\_pose\_sampler\_grid\_size: float
  + path\_following\_speed: float
  + path\_following\_angular\_gain: float
  + path\_following\_stop\_distance\_threshold: float
  + path\_following\_forward\_angle\_threshold: Unknown
  + path\_following\_target\_point\_offset\_meters: float
  + wheel\_dof\_names: List[str]
  + usd\_url: str
  + chassis\_subpath: str
  + wheel\_base: float
  + wheel\_radius: float
* class H1Robot(PolicyMobilityGenRobot)

  + physics\_dt: float
  + z\_offset: float
  + chase\_camera\_base\_path: str
  + chase\_camera\_x\_offset: float
  + chase\_camera\_z\_offset: float
  + chase\_camera\_tilt\_angle: float
  + occupancy\_map\_radius: float
  + occupancy\_map\_z\_min: float
  + occupancy\_map\_z\_max: float
  + occupancy\_map\_cell\_size: float
  + occupancy\_map\_collision\_radius: float
  + front\_camera\_base\_path: str
  + front\_camera\_rotation: Tuple
  + front\_camera\_translation: Tuple
  + front\_camera\_type: HawkCamera
  + keyboard\_linear\_velocity\_gain: float
  + keyboard\_angular\_velocity\_gain: float
  + gamepad\_linear\_velocity\_gain: float
  + gamepad\_angular\_velocity\_gain: float
  + random\_action\_linear\_velocity\_range: Tuple[float, float]
  + random\_action\_angular\_velocity\_range: Tuple[float, float]
  + random\_action\_linear\_acceleration\_std: float
  + random\_action\_angular\_acceleration\_std: float
  + random\_action\_grid\_pose\_sampler\_grid\_size: float
  + path\_following\_speed: float
  + path\_following\_angular\_gain: float
  + path\_following\_stop\_distance\_threshold: float
  + path\_following\_forward\_angle\_threshold: Unknown
  + path\_following\_target\_point\_offset\_meters: float
  + usd\_url: Unknown
  + articulation\_path: str
  + controller\_z\_offset: float
  + class def build\_policy(cls, prim\_path: str)
* class SpotRobot(PolicyMobilityGenRobot)

  + physics\_dt: float
  + z\_offset: float
  + chase\_camera\_base\_path: str
  + chase\_camera\_x\_offset: float
  + chase\_camera\_z\_offset: float
  + chase\_camera\_tilt\_angle: float
  + occupancy\_map\_radius: float
  + occupancy\_map\_z\_min: float
  + occupancy\_map\_z\_max: float
  + occupancy\_map\_cell\_size: float
  + occupancy\_map\_collision\_radius: float
  + front\_camera\_base\_path: str
  + front\_camera\_rotation: Tuple
  + front\_camera\_translation: Tuple
  + front\_camera\_type: HawkCamera
  + keyboard\_linear\_velocity\_gain: float
  + keyboard\_angular\_velocity\_gain: float
  + gamepad\_linear\_velocity\_gain: float
  + gamepad\_angular\_velocity\_gain: float
  + random\_action\_linear\_velocity\_range: Tuple[float, float]
  + random\_action\_angular\_velocity\_range: Tuple[float, float]
  + random\_action\_linear\_acceleration\_std: float
  + random\_action\_angular\_acceleration\_std: float
  + random\_action\_grid\_pose\_sampler\_grid\_size: float
  + path\_following\_speed: float
  + path\_following\_angular\_gain: float
  + path\_following\_stop\_distance\_threshold: float
  + path\_following\_forward\_angle\_threshold: Unknown
  + path\_following\_target\_point\_offset\_meters: float
  + usd\_url: Unknown
  + articulation\_path: str
  + controller\_z\_offset: float
  + class def build\_policy(cls, prim\_path: str) -> SpotFlatTerrainPolicy
* class KeyboardTeleoperationScenario(MobilityGenScenario)

  + def **init**(self, robot: MobilityGenRobot, occupancy\_map: OccupancyMap)
  + def reset(self)
  + def step(self, step\_size: float)
* class GamepadTeleoperationScenario(MobilityGenScenario)

  + def **init**(self, robot: MobilityGenRobot, occupancy\_map: OccupancyMap)
  + def reset(self)
  + def step(self, step\_size: float) -> bool
* class RandomAccelerationScenario(MobilityGenScenario)

  + def **init**(self, robot: MobilityGenRobot, occupancy\_map: OccupancyMap)
  + def reset(self)
  + def step(self, step\_size: float) -> bool
* class RandomPathFollowingScenario(MobilityGenScenario)

  + def **init**(self, robot: MobilityGenRobot, occupancy\_map: OccupancyMap)
  + def set\_random\_target\_path(self)
  + def reset(self)
  + def step(self, step\_size: float) -> bool
  + def get\_visualization\_image(self) -> PIL.Image.Image

On this page

* [Classes](#classes)