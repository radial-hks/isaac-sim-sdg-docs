---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/installation/install_advanced_cloud_setup_alibaba.html
title: "Cloud: Alibaba"
section: "云厂商"
module: "04-headless-deploy"
checksum: "b1e8e8a7f33ca657"
fetched: "2026-06-21T12:48:13"
---

* [Installation](index.html)
* [Cloud Deployment](install_cloud.html)
* Alibaba Cloud Deployment

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Alibaba Cloud Deployment

## Requirements

The requirements for running NVIDIA Isaac Sim on Alibaba Cloud are:

* An Alibaba Cloud account with ECS Instance access that is able to create a Virtual Machine with GPU support.
* A GPU-accelerated compute-optimized instance with the following recommended specifications:

  > + **GPU**: NVIDIA Tesla T4
  > + **Instance type**: ecs.gn6i-c40g1.10xlarge
  > + **Image**: Ubuntu Server 18.04 LTS

## Setup

To launch the Alibaba ECS Instance, use the following steps:

1. Go to the [Alibaba Cloud homepage](https://us.alibabacloud.com/). Click **Log In**.
2. Select **RAM User** to log in.
3. As shown in the figure below, click the upper left corner, select **Cloud Server ECS**, click **Instance**, and click **Create Instance** to enter the instance creation interface.
4. Create instance - basic configuration.

   > As shown in the figure below, the basic configuration (configure as needed):
   >
   > * Choose payment mode.
   > * Select the region and available area.
   > * Select the instance, here select **T4** GPU.
   > * The usage time of preemptible instances.
   > * Number of purchased instances: **1**.
   > * Select image: **Ubuntu**, **18.04 64 bit**.
   > * Select storage, and set the cloud disk size to **500G**.
   > * Click **Next: Network and Security Groups**.
5. Create instance - Network and Security Group as shown below, network and security group (configure as needed).
6. Select the network, you can select an existing network, such as **isaac-sim-vpc-sh / vpc-uf6uov4wgyl1ru928mlbk** in this example. Or create a new **VPC**, click **Go to the console to create>**. A new **private network** can be created.
7. Select a security group, you can select an existing security group, such as **isaac-sim-open-all-ports/sg-uf6ix68ocmepok99yn2v** in this example. Or create a new security group, click **New Security Group>**. You can create a new **Security Group**.

   > Note
   >
   > * Pay special attention here to ensure that all the ports required by Isaac Sim are opened and secure.
   >   Open TCP port **49100** (WebRTC signaling), UDP port **47998** (WebRTC media stream), and TCP port **8210** (web viewer, Docker Compose only).
   >   Restrict access to your client IP for security.
   > * For streaming client options (native desktop app or web-based viewer via Docker Compose), see [Livestream Clients](manual_livestream_clients.html#isaac-sim-manual-livestream-client).
8. Open ports as needed.
9. Click **Next: System Configuration**.
10. Create instance - system configuration as shown below, the system configuration (configure as needed).

    > * Login credentials, select **key pair**.
    > * Login name, select **root**.
    > * Key pair, you can choose an existing key, or create a new key, the key is a file in **.pem** format.
    > * Instance name.
    > * Click **Next: Group Settings**.
11. Create instance - group configuration.

    > * The default setting is good.
    > * Click **Confirm Order**.
12. Confirm the order.

    > * Click **Create instance**.
13. After the instance has been created successfully, you can start the instance, and access the instance through the public network IP.
14. See [Container Installation](install_container.html) to install NVIDIA drivers and other
    dependencies on the VM.
15. Proceed to [Container Deployment](install_container.html#isaac-sim-setup-remote-headless-container).

On this page

* [Requirements](#requirements)
* [Setup](#setup)