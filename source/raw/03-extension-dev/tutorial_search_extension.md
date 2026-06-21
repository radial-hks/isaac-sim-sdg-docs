---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/utilities/tutorial_search_extension.html
title: "Search Extension Tutorial"
section: "Extension 管理"
module: "03-extension-dev"
checksum: "1a03c5068b6f189e"
fetched: "2026-06-21T12:48:11"
---

* SimReady Content Browser Search Extension Tutorial

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# SimReady Content Browser Search Extension Tutorial

The **SimReady Asset Search** feature helps you find digital assets that match your criteria by combining a directory tree with an AI-assisted search control panel. This tutorial explains how to use these features to search your local file system and AWS S3 buckets for assets.

This tutorial assumes you are familiar with [SimReady concepts](https://github.com/NVIDIA/simready-foundation) and the [Content Browser](content_browser.html#isaac-sim-app-gui-content-browser) and workflow. It addresses the following topics:

* [Prerequisites](#prerequisites)
* [Overview](#overview)
* [How to Open and Use the SimReady Asset Search Control Panel](#how-to-open-and-use-the-simready-asset-search-control-panel)
* [How to Limit the Scope of Your Searches](#how-to-limit-the-scope-of-your-searches)
* [How to Display and Filter on Relevance Scores](#how-to-display-and-filter-on-relevance-scores)

## [Prerequisites](#id2)

* You have installed the latest versions of the Omniverse Kit and the `omni.simready.content.browser` UI extension.
* You have access to assets in local folders and AWS S3 buckets.

## [Overview](#id3)

To find assets, optionally select a folder in the directory tree to scope your search, then select a search mode and enter filters in the **SimReady Asset Search** control panel. The control panel initiates the search and displays results in the SimReady Content Browser, where you can view asset data, filter the results, and open assets.

The following sections explain how to use these features.

## [How to Open and Use the SimReady Asset Search Control Panel](#id4)

There are two ways to open the **SimReady Asset Search** control panel:

1. Click the Search icon in the SimReady Content Browser and select **Assets Search** in the context menu.
2. Right-click a folder in the directory tree, and select **AssetSearch here** in the context menu.

Both ways open the **SimReady Asset Search** control panel.

## [How to Limit the Scope of Your Searches](#id5)

Use the directory tree to limit the scope of your searches. The directory tree contains all folders that can contain assets. Selecting a folder limits your searches to the contents of that folder and its subfolders. Selecting a folder in the tree is optional; if you do not select one, **SimReady Asset Search** searches the entire directory tree by default.

The directory tree spans both your local file system and AWS S3 buckets, which gives you flexibility in how broadly or narrowly you scope your searches. You can, for example, search across all registered AWS S3 buckets or limit a search to a specific folder in your local file system. When you select a folder, it becomes the *anchor path* that the search API bases its search on. Until you change it, all searches are scoped to the contents of the selected folder and its subfolders.

As noted in the previous section, the contents of the **SimReady Asset Search** control panel are sensitive to your directory tree selection. Changing your selection initializes the control panel for a new search. (You do not need to close and reopen the control panel to initiate a new search.)

When you select a folder, the SimReady Content Browser displays its contents in a panel to the right of the directory tree. If you select a folder in that panel, the effect is the same as selecting the same folder in the directory tree.

### How to Enter Search Parameters

The **SimReady Asset Search** control panel displays the *anchor path*, **Search Mode** options, and context-sensitive filters.

* The *anchor path* reflects which folder you select in the directory tree. This is the base path for searches; all searches are restricted to the contents of this folder and its subfolders. Select a different folder in the tree to change it. For example, selecting the `Assets/Isaac/SimReady` folder changes the *anchor path* to `Assets/Isaac/SimReady`.
* The *anchor path* determines which **Search Mode** options are available. For example, if the *anchor path* is a folder in your local file system, only the **File Index** search mode is available.
* The **Search Mode** determines which filters are available. For example, if **Search Mode** is **File Index**, only the **Name** filter is available.
* The filters specify which assets the search API returns. If you do not select any filters, the search API returns all assets it finds. If you select one or more filters, the search API returns only assets that pass those filters.

There are three **Search Mode** options: **File Index**, **AI**, and **WSCache**.

* **File Index** is only available if the *anchor path* is a folder in your local file system or an `Assets/Isaac/*` S3 folder. This option enables the following filter:

  + **Name** filter - Enter text in the **Name** field to return only assets whose pathnames match the text. For example, enter ârobotâ to have the search API return all assets whose pathname contains ârobotâ.
  + **Index Files** button - Click this to index files in the selected folder. This is needed if there are files in a local folder that have been added since the last index, or if you exited and restarted Isaac Sim since the last index. (You do not need to click this button if you select an `Assets/Isaac/*` S3 folder.)
* **AI** is only available for folders in AWS S3 buckets. This option enables the following filters:

  + **Relevance cutoff** filter - Enter a value between 0 and 1 to set the minimum relevance score for assets to be returned. Assets with a relevance score lower than the specified cutoff are not returned. (*Relevance* is a measure of how well the asset matches the search query. A value of 1.0 is the highest confidence match possible, a value of 0.0 is no match, and values in between are partial matches. *Relevance* is discussed in more detail in [How to Display and Filter on Relevance Scores](#how-to-display-and-filter-on-relevance-scores).)
  + **Phrase** filter - Enter a natural language phrase to search for assets that match the phrase. For example, enter âa robot with a cameraâ to have the search API return only assets whose properties match that description.
  + These filters are cumulative. The search API returns all assets that match ALL of the filters you specify, and excludes all others.
* **WSCache** (SimReady Workspace Cache) is only available for folders in the `/SimReady` S3 bucket. This option enables the following filters:

  + **Name** filter - Enter text for **Name** to return assets whose pathnames match the text. For example, enter ârobotâ to have the search API return assets whose pathnames match ârobotâ.
  + **Profile** filter - Click the entry field and select a SimReady profile from the dropdown menu to return assets that match the selected profile.
  + **Feature** filter - Click the entry field and select a SimReady feature from the dropdown menu to return assets that match the selected feature.
  + **Tag** filter - Click the entry field and select a SimReady tag from the dropdown menu to return assets with the associated tag.
  + These filters are cumulative. Select the **Match Any** checkbox to have the search API return all assets that match ANY of the filters you specify. Select the **Match All** checkbox to have the search API return only assets that match ALL of the filters you specify.

### How to Index Local Files

For the search API to find assets in a folder, its contents must be indexed. The indexes for local files are stored in memory, and are updated only when you manually index the folder. Assets added to a local folder are not automatically indexed and, if you exit from Isaac Sim and restart it, local indexes are lost. In either case, you must index the folder to make the assets searchable.

To index a local folder and its subfolders, select the folder in the directory tree and click **Index Files**. (This option is only available when **Search Mode** is **File Index**.)

### How to Initiate a Search

When you have scoped your search, selected a search mode, entered relevant search filters, and optionally indexed local files, click **Search** in the **SimReady Asset Search** control panel to initiate the search. The search API runs the search and returns matching assets in the SimReady Content Browser, where you can see asset data, filter the results, and open an asset.

### Examples

The following examples assume you have already opened the **SimReady Asset Search** control panel.

#### Search for assets in the `Assets/Isaac/Robots` folder whose pathnames contain âFanucâ.

1. Select the `Assets/Isaac/Robots` folder in the directory tree.
2. Select **File Index** for **Search Mode**.
3. Enter *Fanuc* for **Name**.
4. Click **Search**.

Note

Unless you select a local folder, there is no need to click **Index Files**.

#### Search for assets in the `Assets/Isaac` S3 folder or its subfolders that are robots.

1. Select the `Assets/Isaac` S3 folder in the directory tree.
2. Select **AI** for **Search Mode**.
3. Enter or accept the default **Relevance cutoff** value, such as 0.5, to exclude results for which the search API has low confidence.
4. Enter *robots* for **Phrase**.
5. Click **Search**.

#### Search for assets in the `Assets/Isaac/SimReady` S3 folder whose **Profile** is âProp-Robotics-Isaacâ and **Feature** is âFET003\_BASE\_NEUTRALâ.

1. Select the `Assets/Isaac/SimReady` S3 folder in the directory tree.
2. Select **WSCache** for **Search Mode**.
3. Select âProp-Robotics-Isaacâ for **Profile**.
4. Select âFET003\_BASE\_NEUTRALâ for **Feature**.
5. Select the **Match All** checkbox.
6. Click **Search**.

In this example, the SimReady Content Browser lists only those assets that satisfy both of these conditions.

## [How to Display and Filter on Relevance Scores](#id6)

When you set **Search Mode** to **AI**, the SimReady Content Browser displays a relevance score for each asset it lists. The search API calculates this score; it is a measure of how well the asset matched the search query. A value of 1.0 is the highest confidence match possible, a value of 0.0 is no match, and values in between are partial matches. Use these scores to help you identify which assets are good matches for your search criteria.

Setting **Search Mode** to **AI** exposes a **Relevance cutoff** filter. Use this filter to limit the results to matches for which the search API has higher confidence. Enter your minimum acceptable relevance score in the control panelâs **Relevance cutoff** field. This restricts the search results to assets whose relevance scores are equal to or greater than the value you specify.

On this page

* [Prerequisites](#prerequisites)
* [Overview](#overview)
* [How to Open and Use the SimReady Asset Search Control Panel](#how-to-open-and-use-the-simready-asset-search-control-panel)
* [How to Limit the Scope of Your Searches](#how-to-limit-the-scope-of-your-searches)
  + [How to Enter Search Parameters](#how-to-enter-search-parameters)
  + [How to Index Local Files](#how-to-index-local-files)
  + [How to Initiate a Search](#how-to-initiate-a-search)
  + [Examples](#examples)
    - [Search for assets in the `Assets/Isaac/Robots` folder whose pathnames contain âFanucâ.](#search-for-assets-in-the-assets-isaac-robots-folder-whose-pathnames-contain-fanuc)
    - [Search for assets in the `Assets/Isaac` S3 folder or its subfolders that are robots.](#search-for-assets-in-the-assets-isaac-s3-folder-or-its-subfolders-that-are-robots)
    - [Search for assets in the `Assets/Isaac/SimReady` S3 folder whose **Profile** is âProp-Robotics-Isaacâ and **Feature** is âFET003\_BASE\_NEUTRALâ.](#search-for-assets-in-the-assets-isaac-simready-s3-folder-whose-profile-is-prop-robotics-isaac-and-feature-is-fet003-base-neutral)
* [How to Display and Filter on Relevance Scores](#how-to-display-and-filter-on-relevance-scores)