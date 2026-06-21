---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/py/source/extensions/isaacsim.replicator.writers/config/python_api.html
title: "replicator.writers API"
section: "Replicator"
module: "05-python-api-quickref"
checksum: "0e9f82ec1b17c391"
fetched: "2026-06-21T14:14:26"
---

* Public API for module isaacsim.replicator.writers:

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Public API for module isaacsim.replicator.writers:

## Classes

* class DataVisualizationWriter(Writer)

  + BB\_2D\_TIGHT: str
  + BB\_2D\_LOOSE: str
  + BB\_3D: str
  + SUPPORTED\_BACKGROUNDS: List
  + def **init**(self, output\_dir: str, bounding\_box\_2d\_tight: bool = False, bounding\_box\_2d\_tight\_params: dict = None, bounding\_box\_2d\_loose: bool = False, bounding\_box\_2d\_loose\_params: dict = None, bounding\_box\_3d: bool = False, bounding\_box\_3d\_params: dict = None, frame\_padding: int = 4)
  + def write(self, data: dict)
  + def detach(self)
* class DOPEWriter(Writer)

  + def **init**(self, output\_dir: str, class\_name\_to\_index\_map: Dict, semantic\_types: List[str] = None, image\_output\_format: str = ‘png’, use\_s3: bool = False, bucket\_name: str = ‘’, endpoint\_url: str = ‘’, s3\_region: str = ‘us-east-1’)
  + def register\_pose\_annotator(config\_data: dict)
  + def setup\_writer(config\_data: dict, writer\_config: dict)
  + def write(self, data: dict)
  + def is\_last\_frame\_valid(self) -> bool
* class PoseWriter(Writer)

  + RGB\_ANNOT\_NAME: str
  + BB3D\_ANNOT\_NAME: str
  + CAM\_PARAMS\_ANNOT\_NAME: str
  + SUPPORTED\_FORMATS: Unknown
  + CUBOID\_KEYPOINTS\_ORDER\_DEFAULT: List
  + CUBOID\_KEYPOINT\_ORDER\_DOPE: List
  + CUBOID\_KEYPOINT\_COLORS: List
  + CUBOID\_EDGE\_COLORS: Dict
  + def **init**(self, output\_dir: str = None, use\_subfolders: bool = False, visibility\_threshold: float = 0.0, skip\_empty\_frames: bool = True, write\_debug\_images: bool = False, frame\_padding: int = 6, format: str = None, use\_s3: bool = False, s3\_bucket: str = None, s3\_endpoint\_url: str = None, s3\_region: str = None, backend: BaseBackend = None, image\_output\_format: str = ‘png’)
  + def write(self, data: dict)
  + def get\_current\_frame\_id(self)
  + def detach(self)
* class PytorchListener

  + def **init**(self)
  + def write\_data(self, data: dict)
  + def get\_rgb\_data(self) -> torch.Tensor | None
* class PytorchWriter(Writer)

  + def **init**(self, listener: PytorchListener, output\_dir: str = None, tiled\_sensor: bool = False, device: str = ‘cuda’)
  + def write(self, data: dict)
* class YCBVideoWriter(Writer)

  + def **init**(self, output\_dir: str, num\_frames: int, semantic\_types: List[str] = None, rgb: bool = False, bounding\_box\_2d\_tight: bool = False, semantic\_segmentation: bool = False, distance\_to\_image\_plane: bool = False, image\_output\_format: str = ‘png’, pose: bool = False, class\_name\_to\_index\_map: Dict = None, factor\_depth: int = 10000, intrinsic\_matrix: np.ndarray = None)
  + def register\_pose\_annotator(config\_data: dict)
  + def setup\_writer(config\_data: dict, writer\_config: dict)
  + def write(self, data: dict)
  + def save\_mesh\_vertices(mesh\_prim: UsdGeom.Mesh, coord\_prim: Usd.Prim, model\_name: str, output\_folder: str)
  + def is\_last\_frame\_valid(self) -> bool

On this page

* [Classes](#classes)