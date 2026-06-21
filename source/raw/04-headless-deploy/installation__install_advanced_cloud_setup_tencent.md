---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/installation/install_advanced_cloud_setup_tencent.html
title: "Cloud: Tencent"
section: "云厂商"
module: "04-headless-deploy"
checksum: "feccad118ef3ecb7"
fetched: "2026-06-21T14:14:24"
---

* [Installation](index.html)
* [Cloud Deployment](install_cloud.html)
* Tencent Cloud Deployment

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Tencent Cloud Deployment

## Requirements

Here are the requirements for running NVIDIA Isaac Sim on Tencent Cloud:

* A Tencent Cloud account with Computing Instance access that is able to create a Virtual Machine with GPU support.
* An Cloud Virtual Machine with the following recommended specifications:

  > + **GPU**: NVIDIA Tesla T4
  > + **Machine type**: [GN7](https://www.tencentcloud.com/document/product/560/19701#GN7)
  > + **Image**: Ubuntu Server 18.04.1 LTS

## Setup

To log in to Tencent Cloud, use the following steps:

1. Go to the [Tencent Cloud homepage](https://www.tencentcloud.com/).
2. Click **Log in**.
3. Select enterprise user login, click **CAM user sign in**.
4. Enter **Root account ID**, **Sub-user name**, and **Password**. Then click **Sign in**.
5. Enter the following page:

To launch the Tencent Cloud Virtual Machine, use the following steps:

1. In the **Products** drop-down tab, click **04 Cloud Virtual Machine**.
2. Click **Get Started**.
3. Enter the **Cloud Virtual Machine** page, select **Instances** in the leftmost column, you can create a new instance through the **Create** button, or start an existing instance by using the **Start Up** button. Here, use the **Create** button to create a new instance.
4. Enter the **Cloud Virtual Machine (CVM)** interface as follows, and create a cloud service instance.
5. For Basic configurations, choose **Spot instances** for **T4** graphics card. **China**, **Guangzhou** are selected for the region, **Random** is selected for the Availability Zone. You can also choose according to your needs.
6. For Instance configurations, choose **GPU-based**, **GPU Compute GN7** (that is, **T4** graphics card). For the operating system of the instance, select **Ubuntu**, **18.04** version. Do not check **Install GPU driver automatically**. Select **500GB** or larger capacity for Storage.
7. After **Select basic configurations** is completed, click **Next: Configure network and host**, and click **Confirm**.
8. To create a network, click **create a VPC** and **a subnet** respectively to create a private network and a subnet. Then follow the prompts. For network **Bandwidth**, select **20Mbps**.

   > Note
   >
   > * When creating a **subnet**, the region selection of **Availability zone** must be the same as **Availability zone** of **Instance configurations** in **Select basic configurations** section.
9. Mandatory. Select **Security Group** to ensure that all the ports required for Isaac Sim remote connection are open. For simplicity, you can choose **Open all ports**. During actual operation, to ensure security, you must select a port that is open to the outside world.

   > Note
   >
   > * Pay special attention here, you must ensure that all the ports required by Isaac Sim are opened and secure.
   >   Open TCP port **49100** (WebRTC signaling), UDP port **47998** (WebRTC media stream), and TCP port **8210** (web viewer, Docker Compose only).
   >   Restrict access to your client IP for security.
   > * For streaming client options (native desktop app or web-based viewer via Docker Compose), see [Livestream Clients](manual_livestream_clients.html#isaac-sim-manual-livestream-client).
10. For Other Settings, create a key for **ssh** connections. You can select an existing secret key or create a new secret key. The secret key is a file in **\*.pem** format.
11. After **Config network and host** is complete, click **Next: Confirm configuration**.
12. After the instance has been created successfully, you can start the instance, and access the instance through the public network IP.
13. See [Container Installation](install_container.html) to install NVIDIA Drivers and other
    dependencies on the VM.
14. Proceed to [Container Deployment](install_container.html#isaac-sim-setup-remote-headless-container).

On this page

* [Requirements](#requirements)
* [Setup](#setup)