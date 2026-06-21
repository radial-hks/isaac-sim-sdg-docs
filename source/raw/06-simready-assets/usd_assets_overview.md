---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/assets/usd_assets_overview.html
title: "USD Assets Overview"
section: "资产库"
module: "06-simready-assets"
checksum: "f438d652c7a9b9bd"
fetched: "2026-06-21T11:55:34"
---

* Isaac Sim Assets

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Isaac Sim Assets

Isaac Sim provides a variety of assets and robots to help you build your virtual world. Some are made specifically for Isaac Sim and robotics applications,
others are made for other NVIDIA Omniverse-based applications. The ones that are available to you by default are all located in the **Window > Browsers** tab.

The [Content Browser](../utilities/content_browser.html#isaac-sim-app-gui-content-browser) is where you can find all of Isaac Sim assets and files. This includes all of the assets listed below, as well as URDF file, config files, policy binaries, and more.

Sample assets are available for download with the [Latest Release](../installation/download.html#isaac-sim-latest-release) of Isaac Sim.
To use this content, you must download the files to the local disk or a Nucleus server.
All asset paths below are assumed to be relative to the default asset root path in the persistent.isaac.asset\_root.default setting. See [Local Assets Packs](../installation/install_faq.html#isaac-sim-setup-assets-content-pack)

Note

Assets will take longer to load when they are accessed for the first time; robots may take multiple minutes to load and larger environment scenes may take as long as ten minutes or more.

## Categories

* [Robot Assets](usd_assets_robots.html)
* [Sensor Assets](usd_assets_sensors.html)
* [Prop Assets](usd_assets_props.html)
* [Environment Assets](usd_assets_environments.html)
* [Featured Assets](usd_assets_featured.html)
* [Third-Party USD Assets](usd_assets_third_party.html)
* [Neural Volume Rendering](usd_assets_nurec.html)

## Omniverse Activity UI

The [Omniverse Activity UI](https://docs.omniverse.nvidia.com/kit/docs/omni.activity.ui) allows you to monitor the progress and activities when assets are being loaded.

Enable the `omni.activity.ui` extension in the Extension Manager (**Window > Extensions** menu),
or launch Isaac Sim from a terminal with the argument `--enable omni.activity.ui`.
Then, open the **Activity Progress** window (**Window > Utilities > Activity Progress** menu) before opening or loading the USD asset to monitor its loading progress.

On this page

* [Categories](#categories)
* [Omniverse Activity UI](#omniverse-activity-ui)