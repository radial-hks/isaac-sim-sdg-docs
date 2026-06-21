---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/development_tools/carb_settings.html
title: "Carb Settings"
section: "开发工具"
module: "02-fundamentals-dev"
checksum: "1bdbdb3f39dc0295"
fetched: "2026-06-21T12:48:06"
---

* [Development Tools](index.html)
* Modify Carb Settings

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Modify Carb Settings

[Carbonite (carb)](../reference_material/reference_glossary.html#isaac-sim-glossary-carb) settings are used to configure default behaviors of Omniverse and Isaac Sim. They can control a wide ranges of features, such as window properties, ROS versions, browser folders, and more. You may wish to change these settings to suit your needs. Here we show the four ways to change the Carb settings in Isaac Sim.

For this tutorial, we will set a parameter inside extension `isaacsim.code_editor.python_server` named `keepalive_interval` to the value `5`. Replace these with your actual extension name, setting parameter, and value when you are working with your project.

## Script Editor Snippet

You can temporarily and quickly change the Carb settings in the [Script Editor](https://docs.omniverse.nvidia.com/extensions/latest/ext_script-editor.html "(in Omniverse Extensions)"). This is useful for testing and debugging, and can be done while Isaac Sim is open. The changes made this way will not be saved after you close the application, and relaunching the simulator will reset the settings.

```python
import carb.settings
import omni.kit

## Set Carb Setting
settings = carb.settings.get_settings()
settings.set("/exts/isaacsim.code_editor.python_server/keepalive_interval", 5)

## Restart Extension to Apply Changes
extension_manager = omni.kit.app.get_app().get_extension_manager()
extension_manager.set_extension_enabled_immediate("isaacsim.code_editor.python_server", False)
extension_manager.set_extension_enabled_immediate("isaacsim.code_editor.python_server", True)
```

## Command-Line Argument

You can launch Isaac Sim with a command-line argument to change the Carb settings. The changes made this way will not be saved after you close the application, and relaunching the simulator without the arguments will reset the settings.

At the root of your Isaac Sim installation, run the following command:

> Linux
>
> ```python
> ./isaac-sim.sh --/exts/isaacsim.code_editor.python_server/keepalive_interval=5
> ```
>
>
> Windows
>
> ```python
> .\isaac-sim.bat --/exts/isaacsim.code_editor.python_server/keepalive_interval=5
> ```

## Edit .toml File

For more permanent changes, you can edit the extensionâs .toml file. The changes made this way will persist after you close the application.

1. Navigate to the extensionâs folder. For example, if you are changing the settings for the `isaacsim.code_editor.python_server` extension, navigate to `<isaac-sim-root_dir>/exts/isaacsim.code_editor.python_server/config`.
2. Open the .toml file with a text editor, and add the following line to the file:

   > ```python
   > [settings]
   > exts."isaacsim.code_editor.python_server".keepalive_interval = 5
   > ```
3. Launch Isaac Sim to see the changes.

## Customize .kit File

If you have multiple settings in multiple extensions that you want to change, you can edit the .kit file for your application. The changes made this way will persist after you close the application.

1. From the root of your Isaac Sim installation, navigate to <isaac-sim-root\_dir>/apps/. Locate the Kit experience app file you are using in this folder. By default, it is the isaacsim.exp.full.kit.
2. Open the app file and add the following line to the file:

   > ```python
   > [settings]
   > exts."isaacsim.code_editor.python_server".keepalive_interval = 5
   > ```
3. Launch Isaac Sim to see the changes.

On this page

* [Script Editor Snippet](#script-editor-snippet)
* [Command-Line Argument](#command-line-argument)
* [Edit .toml File](#edit-toml-file)
* [Customize .kit File](#customize-kit-file)