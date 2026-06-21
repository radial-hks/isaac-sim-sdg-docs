---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/installation/install_advanced_remote_setup.html
title: "Advanced Remote Setup"
section: "远程"
module: "04-headless-deploy"
checksum: "1afc7f99344cfef0"
fetched: "2026-06-21T14:14:24"
---

* [Installation](index.html)
* [Cloud Deployment](install_cloud.html)
* Remote Workstation Deployment

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Remote Workstation Deployment

## Requirements

The requirements for running NVIDIA Isaac Sim on a headless remote workstation are:

> * See [System Requirements](requirements.html#isaac-sim-requirements-isaac-sim-system).
> * See [Container Installation](install_container.html).

## Setup

Follow these steps to access a remote Ubuntu workstation:

1. If you have access to the remote workstation physically, install an SSH server to allow remote access:

   > ```python
   > $ sudo apt update
   > $ sudo apt install openssh-server
   > ```
2. Run the following command to get the remote workstation IP address:

   > ```python
   > $ ifconfig
   > ```
3. Run the following command to access the remote workstation:

   > ```python
   > $ ssh <remote_workstation_username>@<remote_workstation_ip_address>
   > <remote_workstation_username>@<remote_workstation_ip_address>'s password:
   > ```
4. Proceed to [Container Deployment](install_container.html#isaac-sim-setup-remote-headless-container).

On this page

* [Requirements](#requirements)
* [Setup](#setup)