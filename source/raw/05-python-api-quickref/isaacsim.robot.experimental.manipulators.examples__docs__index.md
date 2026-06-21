---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/py/source/extensions/isaacsim.robot.experimental.manipulators.examples/docs/index.html
title: "robot.experimental.manipulators.examples Docs"
section: "Robot"
module: "05-python-api-quickref"
checksum: "de8d212dc840453c"
fetched: "2026-06-21T14:14:27"
---

* [isaacsim.robot.experimental.manipulators.examples] Manipulators Examples (Experimental)

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# [isaacsim.robot.experimental.manipulators.examples] Manipulators Examples (Experimental)

**Version**: 0.2.0

## Overview

Manipulation example implementations for Franka and Universal Robots manipulators demonstrating pick-and-place, follow target, and stacking tasks using the experimental Isaac Sim APIs.

## Enable Extension

The extension can be enabled (if not already) in one of the following ways:

Command-line interface

Define the next entry as an application argument from a terminal.

```python
APP_SCRIPT.(sh|bat) --enable isaacsim.robot.experimental.manipulators.examples
```

Experience/extension configuration

Define the next entry under `[dependencies]` in an experience (`.kit`) file or an extension configuration (`extension.toml`) file.

```python
[dependencies]
"isaacsim.robot.experimental.manipulators.examples" = {}
```

Extension Manager UI

Open the *Window > Extensions* menu in a running application instance and search for `isaacsim.robot.experimental.manipulators.examples`.
Then, toggle the enable control button if it is not already active.

On this page

* [Overview](#overview)
* [Enable Extension](#enable-extension)