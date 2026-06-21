---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/py/source/extensions/isaacsim.storage.native/config/python_api.html
title: "storage.native API"
section: "Storage"
module: "05-python-api-quickref"
checksum: "0e0edd28fbe1161f"
fetched: "2026-06-21T13:40:01"
---

* Public API for module isaacsim.storage.native:

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Public API for module isaacsim.storage.native:

## Classes

* class Version(namedtuple(‘Version’, ‘major minor patch’))

## Functions

* def get\_assets\_root\_path() -> str
* async def get\_assets\_root\_path\_async() -> str
* def path\_join(base: str, name: str) -> str
* def is\_local\_path(path: str) -> bool
* def find\_files\_recursive(abs\_path, filter\_fn = lambda a: True)
* def find\_filtered\_files(abs\_paths: List[str], max\_depth: int = None, filepath\_excludes: List[str] = [], filter\_patterns: List[str] = [], match\_all: bool = False) -> set
* def get\_stage\_references(stage\_path, resolve\_relatives = True)
* def is\_absolute\_path(path)
* def is\_valid\_usd\_file(item: str, excludes: list) -> bool
* def is\_mdl\_file(item: str) -> bool
* async def find\_absolute\_paths\_in\_usds(base\_path)
* def is\_path\_external(path: str, base\_path: str) -> bool
* async def find\_external\_references(base\_path)
* async def count\_asset\_references(base\_path)
* def find\_missing\_references(base\_path)
* async def path\_exists(path: str) -> bool
* def layer\_has\_missing\_references(layer\_identifier: str) -> bool
* def prim\_spec\_has\_missing\_references(prim\_spec) -> bool
* def prim\_has\_missing\_references(prim) -> bool
* def path\_relative(path: str, start: str) -> str
* def path\_dirname(path: str) -> str
* async def resolve\_asset\_path\_async(original\_path: str) -> str | None
* def resolve\_asset\_path(original\_path: str) -> str | None
* async def find\_filtered\_files\_async(root\_path: str, filter\_patterns: List[str] = [], match\_all: bool = False, filepath\_excludes: List[str] = [], max\_depth: int = None) -> set
* def get\_url\_root(url: str) -> str
* def create\_folder(server: str, path: str) -> bool
* def delete\_folder(server: str, path: str) -> bool
* async def download\_assets\_async(src: str, dst: str, progress\_callback, concurrency: int = 10, copy\_behaviour: omni.client.CopyBehavior = CopyBehavior.OVERWRITE, copy\_after\_delete: bool = True, timeout: float = 300.0) -> omni.client.Result
* def check\_server(server: str, path: str, timeout: float = 10.0) -> bool
* async def check\_server\_async(server: str, path: str, timeout: float = 10.0) -> bool
* def build\_server\_list() -> typing.List
* def find\_nucleus\_server(suffix: str) -> typing.Tuple[bool, str]
* def get\_server\_path(suffix: str = ‘’) -> typing.Union[str, None]
* async def get\_server\_path\_async(suffix: str = ‘’) -> typing.Union[str, None]
* def verify\_asset\_root\_path(path: str) -> typing.Tuple[omni.client.Result, str]
* def get\_full\_asset\_path(path: str) -> typing.Union[str, None]
* async def get\_full\_asset\_path\_async(path: str) -> typing.Union[str, None]
* def get\_nvidia\_asset\_root\_path() -> typing.Union[str, None]
* def get\_isaac\_asset\_root\_path() -> typing.Union[str, None]
* def get\_assets\_server() -> typing.Union[str, None]
* async def is\_dir\_async(path: str) -> bool
* def is\_dir(path: str) -> bool
* async def is\_file\_async(path: str) -> bool
* def is\_file(path: str) -> bool
* async def recursive\_list\_folder(path: str) -> typing.List
* async def list\_folder(path: str) -> typing.Tuple[typing.List, typing.List]

On this page

* [Classes](#classes)
* [Functions](#functions)