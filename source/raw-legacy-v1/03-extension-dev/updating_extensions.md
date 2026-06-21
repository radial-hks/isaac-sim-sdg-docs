---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/utilities/updating_extensions.html
title: "Updating Extensions"
section: "Extension 管理"
module: "03-extension-dev"
checksum: "78a7550cac45609e"
fetched: "2026-06-21T13:39:56"
---

* Adding and Updating Extensions Guide

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Adding and Updating Extensions Guide

This guide explains how to add or update an extension in Omniverse.

## Steps to Add an Extension

Follow these steps to add an extension from a local folder path or a new extension registry.

1. **Open the Extensions Menu**

   Open the menu by navigating to **Window > Extensions**:
2. **Add the Path to the Extension (optional)**

   This step is optional if you have already added the path to the extension in the settings panel. Or if the extension you want to add is already in an existing extension registry.

   Click the dropdown in the top right and select the settings option.

   * If you have the extension in a local folder, you can add the path to the extension by clicking the green **+** button in the **Extension Search Paths** section at the top and then typing the full path to the parent folder containing the extension’s folder. This path can contain multiple extensions.
   * If you want to add a new extension registry, click the green **+** button in the **Extension Registries** section at the bottom and type in the full URL of the extension registry.
3. **Search for the Extension**

   In the search bar, type the name of the desired extension. For example, type:

   ```python
   omni.kit.window.tests
   ```

   you can then select it from the results and click **INSTALL**.

   Note

   Custom or non NVIDIA extensions may show up under the **THIRD PARTY** tab

   After installing, click the toggle next to the extension name to enable the extension.

## Steps to Update an Extension

1. **Open the Extensions Menu**

   Open the menu by navigating to **Window > Extensions**:
2. **Search for the Extension**

   In the search bar, type the name of the desired extension. For example, to update the MJCF importer, type:

   ```python
   isaacsim.asset.importer.mjcf
   ```
3. **Click the Update Button**

   Once you find the extension, click the **UPDATE** button.

Note

For some extensions, it may be required to reload Isaac Sim to properly load the newest version.

On this page

* [Steps to Add an Extension](#steps-to-add-an-extension)
* [Steps to Update an Extension](#steps-to-update-an-extension)