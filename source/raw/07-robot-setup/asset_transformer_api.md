---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/robot_setup/asset_transformer_api.html
title: "Asset Transformer API"
section: "Setup 工具"
module: "07-robot-setup"
checksum: "39a9926438a42822"
fetched: "2026-06-21T13:05:33"
---

* [Robot Setup](index.html)
* Asset Transformer API

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Asset Transformer API

This page covers programmatic usage of the Asset Transformer, including API classes, custom rule development, and integration patterns.

For UI-based usage, refer to [Asset Transformer](asset_transformer.html#isaac-sim-app-asset-transformer). For available rules, review [Asset Transformer Rules Reference](asset_transformer_rules.html#isaac-sim-app-asset-transformer-rules).

## Rule Interface

All transformation rules implement the `RuleInterface` abstract base class. This interface defines the contract for rule implementations:

```python
from abc import ABC, abstractmethod
from typing import Any

from pxr import Usd

class RuleInterface(ABC):
    def __init__(
        self,
        source_stage: Usd.Stage,
        package_root: str,
        destination_path: str,
        args: dict[str, Any],
    ) -> None: ...

    @abstractmethod
    def process_rule(self) -> str | None:
        """Execute the rule logic. Return a stage path to switch stages, or None."""
        ...

    @abstractmethod
    def get_configuration_parameters(self) -> list:
        """Return the configuration parameters for this rule."""
        ...

    def log_operation(self, message: str) -> None:
        """Append a message to the operation log."""
        ...

    def add_affected_stage(self, stage_identifier: str) -> None:
        """Record an identifier for a stage affected by this rule."""
        ...
```

**Key Methods**:

| Method | Description |
| --- | --- |
| `process_rule()` | Execute the rule logic. Return `None` to continue with the current working stage, or return a file path to switch the working stage for subsequent rules. |
| `get_configuration_parameters()` | Return a list of `RuleConfigurationParam` objects describing the ruleâs configurable parameters. |
| `log_operation()` | Record human-readable log messages for the execution report. |
| `add_affected_stage()` | Record identifiers for stages or layers modified by the rule. |

### Rule Logging

Every rule implementation must provide adequate logging through the `log_operation()` method. This creates a detailed audit trail of transformations:

```python
def process_rule(self) -> str | None:
    self.log_operation("SchemaRoutingRule start destination=payloads/physics.usda")
    self.log_operation("Schema patterns: Physics*, Physx*")

    # ... processing ...

    self.log_operation("Moved 5 schema(s) from /World/Robot: PhysicsRigidBodyAPI, PhysicsMassAPI, ...")
    self.log_operation("Processed 12 prim(s), moved 24 schema instance(s)")
    self.log_operation("SchemaRoutingRule completed")
```

**Logging Best Practices**:

* Log the rule start with key configuration parameters
* Log pattern matches and filter criteria
* Log each significant operation (schema moves, property copies, prim transfers)
* Log summary statistics (counts of processed items)
* Log affected stages using `add_affected_stage()`
* Log completion status

## Rule Registration

The `RuleRegistry` is a singleton class that maintains a mapping of rule type names to their implementation classes. When the `AssetTransformerManager` executes a profile, it looks up each ruleâs `type` string in the registry to find the corresponding implementation class.

The `RuleRegistry` uses a singleton pattern, meaning there is only one global instance shared across all code. This allows rules registered by any extension or module to be available to all transformation profiles.

**Registry Methods**:

| Method | Description |
| --- | --- |
| `register(rule_cls)` | Register a rule class. The key is computed as `{module}.{qualname}`. Raises `TypeError` if the class does not inherit from `RuleInterface`. |
| `get(rule_type)` | Look up a rule class by its fully qualified type name. Returns `None` if not found. |
| `list_rules()` | Return a dictionary mapping all registered type names to their implementation classes. |
| `list_rule_types()` | Return a sorted list of all registered rule type names. |
| `clear()` | Remove all registered rules. Primarily used for testing. |

## Creating Custom Rules

To create a custom transformation rule, implement the `RuleInterface` abstract base class and register it with the `RuleRegistry`.

Complete Custom Rule Example

```python
from isaacsim.asset.transformer import RuleConfigurationParam, RuleInterface, RuleRegistry
from pxr import Usd

class MyCustomRule(RuleInterface):
    """A custom transformation rule."""

    def get_configuration_parameters(self) -> list:
        return [
            RuleConfigurationParam(
                name="my_param",
                display_name="My Parameter",
                param_type=str,
                description="Description of the parameter",
                default_value="default_value",
            ),
            RuleConfigurationParam(
                name="scope",
                display_name="Scope",
                param_type=str,
                description="Root prim path to process",
                default_value="/",
            ),
        ]

    def process_rule(self) -> str | None:
        params = self.args.get("params", {}) or {}
        my_param = params.get("my_param", "default_value")
        scope = params.get("scope", "/")

        self.log_operation(f"MyCustomRule start my_param={my_param} scope={scope}")
        stage = self.source_stage

        scope_prim = stage.GetPrimAtPath(scope)
        if not scope_prim.IsValid():
            self.log_operation(f"Scope prim not found: {scope}")
            return None

        processed_count = 0
        for prim in Usd.PrimRange(scope_prim):
            processed_count += 1

        self.log_operation(f"Processed {processed_count} prim(s)")
        self.log_operation("MyCustomRule completed")
        self.add_affected_stage("my_output.usda")

        return None

registry = RuleRegistry()
registry.register(MyCustomRule)
```

**Referencing a Custom Rule in a Profile**:

The rule is registered using its fully qualified class name (`{module}.{class_name}`), which becomes the `type` string in rule specifications:

```python
from isaacsim.asset.transformer import RuleSpec

# type = fully qualified class name used when registering the rule
rule_spec = RuleSpec(
    name="My Custom Transformation",
    type="my_extension.rules.MyCustomRule",
    destination="payloads",
    params={"my_param": "custom_value", "scope": "/World/Robot"},
    enabled=True,
)
```

### Extension-Based Registration

For Isaac Sim extensions, register rules when the extension loads:

```python
import omni.ext
from isaacsim.asset.transformer import RuleRegistry

from .rules import AnotherRule, MyCustomRule

class MyExtension(omni.ext.IExt):
    def on_startup(self, ext_id):
        registry = RuleRegistry()
        registry.register(MyCustomRule)
        registry.register(AnotherRule)

    def on_shutdown(self):
        pass
```

## Programmatic API Usage

The Asset Transformer can be invoked programmatically using the Python API. This enables integration into automated pipelines, batch processing, and custom tooling.

### Basic Usage

```python
from isaacsim.asset.transformer import (
    AssetTransformerManager,
    RuleProfile,
    RuleSpec,
)

# input_stage = "/path/to/robot.usd"
# package_root = "/output/robot_package"

profile = RuleProfile(
    profile_name="My Transform Profile",
    version="1.0",
    rules=[
        RuleSpec(
            name="Route Physics Schemas",
            type="isaacsim.asset.transformer.rules.core.schemas.SchemaRoutingRule",
            destination="payloads/Physics",
            params={
                "schemas": ["Physics*", "Physx*"],
                "stage_name": "physics.usda",
            },
            enabled=True,
        ),
        RuleSpec(
            name="Route Materials",
            type="isaacsim.asset.transformer.rules.perf.materials.MaterialsRoutingRule",
            destination="payloads",
            params={
                "materials_layer": "materials.usda",
                "deduplicate": True,
            },
            enabled=True,
        ),
    ],
)

manager = AssetTransformerManager()
report = manager.run(
    input_stage=input_stage,
    profile=profile,
    package_root=package_root,
)

print(f"Transform completed: {report.output_stage_path}")
for result in report.results:
    status = "SUCCESS" if result.success else "FAILED"
    print(f"  {result.rule.name}: {status}")
    if result.error:
        print(f"    Error: {result.error}")
```

### Loading a Profile from JSON

```python
import json

from isaacsim.asset.transformer import AssetTransformerManager, RuleProfile

# profile_path = "/path/to/profile.json"
# input_stage = "/path/to/robot.usd"
# package_root = "/output/robot_package"

with open(profile_path, "r") as f:
    profile_data = json.load(f)

profile = RuleProfile.from_dict(profile_data)

manager = AssetTransformerManager()
report = manager.run(
    input_stage=input_stage,
    profile=profile,
    package_root=package_root,
)
```

### Saving the Execution Report

```python
import json

# report = manager.run(input_stage, profile, package_root)

report_path = f"{report.package_root}/transform_report.json"
with open(report_path, "w") as f:
    json.dump(report.to_dict(), f, indent=2)
```

### Accessing Rule Logs

```python
# report = manager.run(input_stage, profile, package_root)

# Iterate through rule results
for result in report.results:
    print(f"\n=== {result.rule.name} ===")
    print(f"Type: {result.rule.type}")
    print(f"Success: {result.success}")
    print(f"Duration: {result.started_at} to {result.finished_at}")
    print(f"Affected stages: {result.affected_stages}")

    print("Log:")
    for entry in result.log:
        print(f"  {entry['message']}")
```

### Querying Registered Rules

```python
from isaacsim.asset.transformer import RuleRegistry

registry = RuleRegistry()
rule_types = registry.list_rule_types()
for rule_type in rule_types:
    print(rule_type)

rule_cls = registry.get("isaacsim.asset.transformer.rules.core.schemas.SchemaRoutingRule")
if rule_cls:
    temp_rule = rule_cls.__new__(rule_cls)
    temp_rule._log = []
    params = temp_rule.get_configuration_parameters()
    for param in params:
        print(f"  {param.name}: {param.param_type.__name__} = {param.default_value}")
```

## API Classes Reference

| Class | Description |
| --- | --- |
| `AssetTransformerManager` | Coordinates execution of rule profiles over USD stages. Call `run()` to execute a transformation. |
| `RuleProfile` | Defines a complete transformation pipeline with profile metadata and ordered rule specifications. |
| `RuleSpec` | Specification for a single rule including name, type, destination, parameters, and enabled state. |
| `ExecutionReport` | Contains the results of a transformation run including per-rule logs, timestamps, and the output stage path. |
| `RuleExecutionResult` | Result of executing a single rule including success status, log entries, affected stages, and error information. |
| `RuleRegistry` | Singleton registry mapping rule type names to implementation classes. Rules are registered automatically when their extensions load. |
| `RuleInterface` | Abstract base class for all transformation rules. Implement this to create custom rules. |
| `RuleConfigurationParam` | Describes a configurable parameter for a rule, including name, type, default value, and description. |

## Error Handling

```python
from isaacsim.asset.transformer import AssetTransformerManager, RuleProfile

# input_stage, profile, package_root from your context

manager = AssetTransformerManager()

try:
    report = manager.run(input_stage, profile, package_root)
except RuntimeError as e:
    print(f"Transformation failed to start: {e}")
    raise

for result in report.results:
    if not result.success:
        print(f"Rule '{result.rule.name}' failed: {result.error}")
```

**Common Errors**:

| Error | Cause |
| --- | --- |
| `RuntimeError: Failed to open source stage` | The input USD file does not exist or is corrupted |
| `RuntimeError: Failed to export base stage` | Cannot write to the output directory (permissions, disk full) |
| `TypeError: rule_cls must subclass RuleInterface` | Attempting to register a class that does not inherit from `RuleInterface` |
| Rule `error` field populated | Exception raised during `process_rule()` execution |

On this page

* [Rule Interface](#rule-interface)
  + [Rule Logging](#rule-logging)
* [Rule Registration](#rule-registration)
* [Creating Custom Rules](#creating-custom-rules)
  + [Extension-Based Registration](#extension-based-registration)
* [Programmatic API Usage](#programmatic-api-usage)
  + [Basic Usage](#basic-usage)
  + [Loading a Profile from JSON](#loading-a-profile-from-json)
  + [Saving the Execution Report](#saving-the-execution-report)
  + [Accessing Rule Logs](#accessing-rule-logs)
  + [Querying Registered Rules](#querying-registered-rules)
* [API Classes Reference](#api-classes-reference)
* [Error Handling](#error-handling)