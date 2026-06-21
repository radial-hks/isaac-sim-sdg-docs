# Headless & 部署

> 无头模式运行、容器化、云端部署、远程可视化
> Isaac Sim 版本: 6.0
> 最后组装: 2026-06-21 13:58 UTC
> 来源页数: 8

---

## 来源链接

- [Container Install](https://docs.isaacsim.omniverse.nvidia.com/latest/installation/install_container.html)
- [Cloud Install](https://docs.isaacsim.omniverse.nvidia.com/latest/installation/install_cloud.html)
- [Advanced Remote Setup](https://docs.isaacsim.omniverse.nvidia.com/latest/installation/install_advanced_remote_setup.html)
- [Livestream Clients](https://docs.isaacsim.omniverse.nvidia.com/latest/installation/manual_livestream_clients.html)
- [Cloud: Alibaba](https://docs.isaacsim.omniverse.nvidia.com/latest/installation/install_advanced_cloud_setup_alibaba.html)
- [Cloud: AWS](https://docs.isaacsim.omniverse.nvidia.com/latest/installation/install_advanced_cloud_setup_aws.html)
- [Cloud: Tencent](https://docs.isaacsim.omniverse.nvidia.com/latest/installation/install_advanced_cloud_setup_tencent.html)
- [Performance Optimization](https://docs.isaacsim.omniverse.nvidia.com/latest/reference_material/sim_performance_optimization_handbook.html)

---


## 容器化

### Container Install

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/installation/install_container.html

* [Installation](index.html)
* Container Installation

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Container Installation

The container installation of Isaac Sim is recommended for deployment on remote headless servers or the Cloud using a Docker container running Linux.

See also

* [Differences Between Workstation And Docker](install_faq.html#isaac-sim-setup-differences)

## Container Setup

1. Ensure your system meets the [System Requirements](requirements.html#isaac-sim-requirements-isaac-sim-system) for running NVIDIA Isaac Sim.
2. Install Docker:

```python
# Docker installation using the convenience script
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Post-install steps for Docker
sudo groupadd docker
sudo usermod -aG docker $USER
newgrp docker

# Verify Docker
docker run hello-world
```

See also

* [Install Docker Engine on Ubuntu](https://docs.docker.com/engine/install/ubuntu)
* [Post-installation steps for Linux](https://docs.docker.com/engine/install/linux-postinstall)

3. Install the NVIDIA Container Toolkit:

```python
# Configure the repository
curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
    && curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | \
    sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
    sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list \
    && \
    sudo apt-get update

# Install the NVIDIA Container Toolkit packages
sudo apt-get install -y nvidia-container-toolkit
sudo systemctl restart docker

# Configure the container runtime
sudo nvidia-ctk runtime configure --runtime=docker
sudo systemctl restart docker

# Verify NVIDIA Container Toolkit
docker run --rm --runtime=nvidia --gpus all nvcr.io/nvidia/cuda:12.8.0-base-ubuntu24.04 nvidia-smi
```

Note

* Install the latest version of [NVIDIA Container Toolkit](https://github.com/NVIDIA/nvidia-container-toolkit) to get security fixes.
* The validation step uses the NGC-hosted CUDA base image (`nvcr.io/nvidia/cuda`), which is public and avoids Docker Hub’s anonymous pull rate limits (HTTP `429 Too Many Requests`). The image is multi-arch, so the same tag runs on Linux x86\_64 and aarch64.
* If a step that pulls from Docker Hub (for example `docker run hello-world`) fails with `429 Too Many Requests`, run `docker login` first or retry later, since Docker Hub enforces rate limits on anonymous pulls.

## Container Deployment

This section describes how to run the NVIDIA Isaac Sim container in headless mode with livestreaming.

**Steps:**

1. Setup and install the container prerequisites. See [Container Setup](#isaac-sim-requirements-isaac-sim-container) above.
2. Run the following command to confirm your GPU driver version:

```python
nvidia-smi
```

3. Pull the [Isaac Sim Container](https://catalog.ngc.nvidia.com/orgs/nvidia/containers/isaac-sim):

```python
docker pull nvcr.io/nvidia/isaac-sim:6.0.0
```

4. Create the cached volume mounts on host. Each directory maps to a container volume mount in the `docker run` command below:

```python
mkdir -p ~/docker/isaac-sim/cache/main
mkdir -p ~/docker/isaac-sim/cache/computecache
mkdir -p ~/docker/isaac-sim/config
mkdir -p ~/docker/isaac-sim/data
mkdir -p ~/docker/isaac-sim/logs
mkdir -p ~/docker/isaac-sim/pkg
mkdir -p ~/.cache/ov/hub
sudo chown -R 1234:1234 ~/docker/isaac-sim ~/.cache/ov/hub
```

5. Run the Isaac Sim container with an interactive Bash session:

```python
docker run --name isaac-sim --entrypoint bash -it --gpus all -e "ACCEPT_EULA=Y" --rm --network=host \
    -e "PRIVACY_CONSENT=Y" \
    -v ~/docker/isaac-sim/cache/main:/isaac-sim/.cache:rw \
    -v ~/docker/isaac-sim/cache/computecache:/isaac-sim/.nv/ComputeCache:rw \
    -v ~/docker/isaac-sim/logs:/isaac-sim/.nvidia-omniverse/logs:rw \
    -v ~/docker/isaac-sim/config:/isaac-sim/.nvidia-omniverse/config:rw \
    -v ~/docker/isaac-sim/data:/isaac-sim/.local/share/ov/data:rw \
    -v ~/docker/isaac-sim/pkg:/isaac-sim/.local/share/ov/pkg:rw \
    -v ~/.cache/ov/hub:/var/cache/hub:rw \
    -u 1234:1234 \
    nvcr.io/nvidia/isaac-sim:6.0.0
```

Important

`--network=host` is required for WebRTC livestreaming. The NVIDIA streaming SDK binds its UDP media
socket to the `ISAACSIM_HOST` address, which must be a real network interface inside the container.
Docker bridge networking (`-p` port publishing) does not work because the host IP is not available
inside the container’s network namespace — signaling may connect, but the video stream will not.

Note

* The Isaac Sim container now runs as a rootless user.
* The Isaac Sim container now supports multi-arch. The same tag can be run on Linux x86\_64 and aarch64 systems.
* By using the `-e "ACCEPT_EULA=Y"` flag, you accept the license agreement of the image found at [NVIDIA Omniverse License Agreement](../common/NVIDIA_Omniverse_License_Agreement.html).
* By using the `-e "PRIVACY_CONSENT=Y"` flag, you opt-in to the data collection agreement found at [Data Collection & Usage](../common/data-collection.html). You may opt-out by not setting this flag.
* The `-e "PRIVACY_USERID=<email>"` flag can optionally be set for tagging the session logs.
* Add the `--runtime=nvidia` flag if there are issues detecting the GPU in the container.
* For enterprise users, see [Enterprise Nucleus Server](https://docs.omniverse.nvidia.com/nucleus/latest/enterprise/installation/install-ove-nucleus.html "(in Omniverse Nucleus)").
* The Isaac Sim container uses assets in the Cloud if no Nucleus server is available.

When using a separate Nucleus server:

> * See [Problem Connecting to Docker Container](install_faq.html#isaac-sim-setup-net-host) to expose all ports of the container and connect to an external Nucleus server.
> * See [Setting the Default Nucleus Server](install_faq.html#isaac-sim-setup-set-omni-server) to set the default Nucleus server.
> * See [Setting the Default Username and Password for Connecting to the Nucleus Server](install_faq.html#isaac-sim-setup-set-omni-user) to set the default credentials for any Nucleus server.

**Environment Variables**

The following environment variables can be passed to `docker run` with `-e` to control container behavior:

| Variable | Required | Description |
| --- | --- | --- |
| `ACCEPT_EULA` | Yes | Accept the license agreement (set to `Y`). |
| `PRIVACY_CONSENT` | No | Opt-in to data collection (set to `Y`). See [Data Collection & Usage](../common/data-collection.html). |
| `PRIVACY_USERID` | No | Tag telemetry data with a user ID (for example an email address). See [Data Collection & Usage](../common/data-collection.html). |
| `OMNI_SERVER` | No | Override the default asset root (passed as `--/persistent/isaac/asset_root/default`). |
| `ISAACSIM_HOST` | No | Public or private IP of the host for livestream. Default: `127.0.0.1`. |
| `ISAACSIM_SIGNAL_PORT` | No | WebRTC signaling port. Default: `49100`. |
| `ISAACSIM_STREAM_PORT` | No | WebRTC media streaming port. Default: `47998`. |

6. Check if your system is compatible with Isaac Sim:

```python
./isaac-sim.compatibility_check.sh --/app/quitAfter=10 --no-window
```

Note

* To run the Compatibility Checker separately:

```python
docker run --entrypoint bash -it --gpus all --rm --network=host \
    nvcr.io/nvidia/isaac-sim:6.0.0 ./isaac-sim.compatibility_check.sh --/app/quitAfter=10 --no-window
```

* You should see the text “System checking result: PASSED” if your system is compaitble.

7. Start Isaac Sim with native livestream mode:

```python
./runheadless.sh -v
```

**Streaming Ports**

If the host firewall is active (e.g. UFW), allow the following ports:

| Port | Protocol | Purpose |
| --- | --- | --- |
| `8210` | TCP | Web viewer (Docker Compose only) |
| `49100` | TCP | WebRTC signaling |
| `47998` | UDP | WebRTC media stream |

If you override ports via `ISAACSIM_SIGNAL_PORT`, `ISAACSIM_STREAM_PORT`, or `WEB_VIEWER_PORT`, open those ports instead.

Note

* Before running a livestream client, you must have the Isaac Sim app loaded and ready.
  :   It may take a few minutes for Isaac Sim to completely load.
* The -v flag is used to show additional logs while the shader cache is being warmed up.
* To confirm this, look out for this line in the console or the logs:

```python
Isaac Sim Full Streaming App is loaded.
```

* The first time loading Isaac Sim, it takes a while for the shaders to be cached. Subsequent runs of Isaac Sim are quicker because the shaders are cached and the cache is mounted when the container runs.
* See [Save Isaac Sim Configs on Local Disk](install_faq.html#isaac-sim-setup-keep-configs) to make Isaac Sim configs and cache persistent when using containers.

8. Connect the native [Isaac Sim WebRTC Streaming Client](manual_livestream_clients.html#isaac-sim-setup-livestream-webrtc) to view Isaac Sim.
   Download it from the [Latest Release](download.html#isaac-sim-latest-release) section, enter the IP address of the host, and click **Connect**.

   Alternatively, if you prefer a browser-based viewer with no client installation, use the
   [Docker Compose deployment](#isaac-sim-docker-compose-deployment) below instead of the manual
   `docker run` workflow above.
9. Proceed to [Quick Tutorials](../introduction/quickstart_index.html#isaac-sim-intro-quickstart-series) to begin your first tutorial.

Note

* Some tutorials that use the Content Browser may not work when using the Isaac Sim container with no Nucleus connected.
* It is recommended to use the Workstation Isaac Sim from the Omniverse Launcher to run all tutorials.
* The Isaac Sim container supports running our Python apps and standalone examples in headless mode only.
* The latest NVIDIA drivers may not be fully supported for some features like livestreaming. See [Technical Requirements](https://docs.omniverse.nvidia.com/dev-guide/latest/common/technical-requirements.html "(in Omniverse Developer Guide)") for recommended drivers.
* See also [Isaac Sim Dockerfiles](https://github.com/isaac-sim/IsaacSim/tree/main/tools/docker) to build your own custom Isaac Sim container.
* You can debug [Python Scripts Running in Docker](../utilities/debugging/tutorial_advanced_python_debugging.html#isaac-sim-app-tutorial-advanced-python-debugging-docker).
* **Stale volume mounts**: Old cached data in Docker volume mount directories can cause crashes, config errors,
  or livestream failures. Remove the existing mounts and recreate them:

  ```python
  sudo rm -rf ~/docker/isaac-sim
  mkdir -p ~/docker/isaac-sim/cache/main
  mkdir -p ~/docker/isaac-sim/cache/computecache
  mkdir -p ~/docker/isaac-sim/config
  mkdir -p ~/docker/isaac-sim/data
  mkdir -p ~/docker/isaac-sim/logs
  mkdir -p ~/docker/isaac-sim/pkg
  mkdir -p ~/.cache/ov/hub
  sudo chown -R 1234:1234 ~/docker/isaac-sim ~/.cache/ov/hub
  ```
* **Second browser cannot connect**: Only one browser tab or window can be connected to Isaac Sim
  at a time. Close the existing browser session before opening a new one.
* **Clipboard not working in web viewer**: The browser Clipboard API requires a secure context. When
  accessing the web viewer over HTTP from a non-localhost address, clipboard forwarding is blocked.
  In Chrome, open `chrome://flags/#unsafely-treat-insecure-origin-as-secure`, add the web viewer
  URL (e.g. `http://192.168.1.100:8210`), and relaunch the browser.

Tip

To build a Docker image from source instead of pulling from NGC, see the [Docker Build Tools README](https://github.com/isaac-sim/IsaacSim/blob/main/tools/docker/README.md).
The README also covers multi-instance deployment with dedicated GPUs, cloud VM configuration (AWS, GCP, Azure), and advanced Docker options.

## Hub Workstation Cache

[Hub Workstation Cache](https://docs.omniverse.nvidia.com/utilities/latest/cache/hub-workstation.html) is a service
that speeds up USD workflows by caching storage-derived data locally. When running Isaac Sim in a container,
Hub should also run as a container on the same host so that all Kit-based clients can benefit from the shared cache.

Note

Hub Workstation Cache is designed for **local workstation use only** — for example, bare-metal runs or containers
on a local workstation. It is not intended for multi-user servers or cloud deployments. For distributed or cloud
caching, see [Derived Data Cache Service (DDCS)](https://docs.nvidia.com/cloud-functions/current/latest/ddcs.html).

The Hub Workstation Cache image is public and can be pulled without logging in to `nvcr.io`. If your Docker client
is already logged in to `nvcr.io`, NGC checks whether the governing terms have been accepted for your NGC
organization before allowing the pull.

Before pulling the Hub image with Docker credentials, open the [Hub Workstation Cache Container](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/omniverse/containers/hub_workstation_cache?version=2.0.0) page in a browser,
sign in to NGC, select version `2.0.0`, and accept the governing terms. NGC requires terms acceptance once per
NGC organization. For the official NGC procedure, see [NGC Accepting Terms Before Downloading](https://docs.nvidia.com/ngc/latest/ngc-catalog-user-guide.html#accepting-terms-before-downloading).

If Docker reports `DENIED` with `Please accept license on the browser to be able to download`, either accept the
terms in the browser for the same NGC organization used by `docker login nvcr.io`, or log out of `nvcr.io` before
pulling this public image anonymously:

```python
$ docker logout nvcr.io
$ docker pull nvcr.io/nvidia/omniverse/hub_workstation_cache:2.0.0
```

Accept the NGC governing terms for the Hub Workstation Cache image before pulling with Docker credentials.

Start the Hub container **before** launching Isaac Sim:

```python
mkdir -p ~/.cache/ov/hub
sudo chown -R 1234:1234 ~/.cache/ov/hub
docker run --name hub-cache --rm -d --network=host \
    -v ~/.cache/ov/hub:/var/cache/hub:rw \
    -u 1234:1234 \
    nvcr.io/nvidia/omniverse/hub_workstation_cache:2.0.0
```

Once the container is running, the Hub settings UI is available at `http://localhost:14090/index.html`.

The Isaac Sim container is pre-configured to discover Hub at runtime via the following environment variables
baked into the image:

| Variable | Value | Purpose |
| --- | --- | --- |
| `HUB__CACHE__PATH` | `/var/cache/hub` | Tells the local Hub executable where to find the cache |
| `HUB__ARGS__DETECT_ONLY` | `true` | Prevents the client from starting its own Hub instance |
| `OMNICLIENT_HUB_EXE` | `/usr/local/bin/hub` | Path to the Hub executable used for client coordination |

The `~/.cache/ov/hub:/var/cache/hub` volume mount in the Isaac Sim `docker run` examples maps the same
host directory into both containers so they share the cache. `--network=host` is required so the Hub client
inside Isaac Sim can reach the Hub service on `localhost`.

For more details, see the
[Hub as a Docker Container](https://docs.omniverse.nvidia.com/utilities/latest/cache/hub-workstation.html#hub-as-a-docker-container)
documentation.

## Docker Compose Deployment (Isaac Sim + Web Viewer)

Docker Compose can deploy Isaac Sim and a web-based WebRTC streaming client together. This is a simpler alternative to the manual `docker run` workflow above, and does not require downloading a native streaming client.

For full details on Docker Compose configuration, multi-instance deployment, and environment variables, see the [Docker README](https://github.com/isaac-sim/IsaacSim/blob/main/tools/docker/README.md).

The `docker-compose.yml` in `tools/docker/` handles volume mounts, GPU assignment, networking, and health checks automatically. The web viewer is built from the [NVIDIA Omniverse Web SDK](https://docs.omniverse.nvidia.com/ov-web-sdk/latest/web-sample/overview.html).

Note

Docker Compose web viewer deployment is supported only on Ubuntu hosts and DGX Spark systems.
Windows hosts, including WSL, are not supported.

Warning

Isaac Sim and the web viewer are designed for use on private/trusted networks. They do not include authentication or encryption. If you need to expose them over the Internet, add a reverse proxy with HTTPS/TLS and authentication (e.g. nginx with SSL certificates and basic auth). Users are responsible for securing any public-facing deployments.

**Quick Start:**

```python
# Create cache/log mounts (use uid 1234 to match container user)
mkdir -p ~/docker/isaac-sim/{cache/main,cache/computecache,config,data,logs,pkg}
mkdir -p ~/.cache/ov/hub
sudo chown -R 1234:1234 ~/docker/isaac-sim ~/.cache/ov/hub

# Build the Isaac Sim image (one-time)
./tools/docker/prep_docker_build.sh --build --x86_64
./tools/docker/build_docker.sh --x86_64

# Launch both services
docker compose -p isim -f tools/docker/docker-compose.yml up --build -d

# Check the web viewer URL
docker compose -p isim logs web-viewer
```

Note

On DGX Spark, use `--aarch64` instead of `--x86_64` in the build commands above.

Open the URL shown in the logs (e.g. `http://<host-ip>:8210`) in a Chromium-based browser.

If Docker Compose reports a Hub startup or connectivity issue after a previous test, restart the Hub container from
[Hub Workstation Cache](#isaac-sim-hub-workstation-cache) and retry Docker Compose.

To use a prebuilt NGC image instead of building locally:

```python
ISAAC_SIM_IMAGE=nvcr.io/nvidia/isaac-sim:6.0.0 docker compose -p isim -f tools/docker/docker-compose.yml up --build -d
```

To stop:

```python
docker compose -p isim -f tools/docker/docker-compose.yml down
```

Note

* The web viewer bakes the signaling host and ports at build time. Use `--build` when changing `ISAACSIM_HOST` or port variables.
* If Docker startup fails after an interrupted build, failed extraction, or disk-full event, clean the generated Docker build context and rebuild from a known-good build output. See the [Docker
  README troubleshooting section](https://github.com/isaac-sim/IsaacSim/blob/main/tools/docker/README.md#troubleshooting) for recovery steps.
* Docker Compose supports multi-instance deployment with dedicated GPUs, custom signal/stream ports, and more. See the [Docker README](https://github.com/isaac-sim/IsaacSim/blob/main/tools/docker/README.md) for full configuration details.

## Container Deployment with GUI

This section describes how to run the NVIDIA Isaac Sim container with GUI.

**Steps:**

1. Setup and install the container prerequisites. See [Container Setup](#isaac-sim-requirements-isaac-sim-container) above.
2. Run the following command to confirm your GPU driver version:

```python
nvidia-smi
```

3. Pull the [Isaac Sim Container](https://catalog.ngc.nvidia.com/orgs/nvidia/containers/isaac-sim):

```python
docker pull nvcr.io/nvidia/isaac-sim:6.0.0
```

4. Create the cached volume mounts on host. Each directory maps to a container volume mount in the `docker run` command below:

```python
mkdir -p ~/docker/isaac-sim/cache/main
mkdir -p ~/docker/isaac-sim/cache/computecache
mkdir -p ~/docker/isaac-sim/config
mkdir -p ~/docker/isaac-sim/data
mkdir -p ~/docker/isaac-sim/logs
mkdir -p ~/docker/isaac-sim/pkg
mkdir -p ~/.cache/ov/hub
sudo chown -R 1234:1234 ~/docker/isaac-sim ~/.cache/ov/hub
```

5. Run the Isaac Sim container with an interactive Bash session:

```python
xhost +local:
docker run --name isaac-sim --entrypoint bash -it --gpus all -e "ACCEPT_EULA=Y" --rm --network=host \
    -e "PRIVACY_CONSENT=Y" \
    -v $HOME/.Xauthority:/isaac-sim/.Xauthority \
    -e DISPLAY \
    -v ~/docker/isaac-sim/cache/main:/isaac-sim/.cache:rw \
    -v ~/docker/isaac-sim/cache/computecache:/isaac-sim/.nv/ComputeCache:rw \
    -v ~/docker/isaac-sim/logs:/isaac-sim/.nvidia-omniverse/logs:rw \
    -v ~/docker/isaac-sim/config:/isaac-sim/.nvidia-omniverse/config:rw \
    -v ~/docker/isaac-sim/data:/isaac-sim/.local/share/ov/data:rw \
    -v ~/docker/isaac-sim/pkg:/isaac-sim/.local/share/ov/pkg:rw \
    -v ~/.cache/ov/hub:/var/cache/hub:rw \
    -u 1234:1234 \
    nvcr.io/nvidia/isaac-sim:6.0.0
```

6. Check if your system is compatible with Isaac Sim:

```python
./isaac-sim.compatibility_check.sh
```

7. Start Isaac Sim with GUI:

```python
./runapp.sh
```

8. Proceed to [Quick Tutorials](../introduction/quickstart_index.html#isaac-sim-intro-quickstart-series) to begin your first tutorial.

Warning

* Running Isaac Sim with GUI in the container is generally not recommended.
* The application experience may not be as expected. For a full GUI app experience please run Isaac Sim with the [Workstation Installation](install_workstation.html#isaac-sim-app-install-workstation).

On this page

* [Container Setup](#container-setup)
* [Container Deployment](#container-deployment)
* [Hub Workstation Cache](#hub-workstation-cache)
* [Docker Compose Deployment (Isaac Sim + Web Viewer)](#docker-compose-deployment-isaac-sim-web-viewer)
* [Container Deployment with GUI](#container-deployment-with-gui)

---


## 云端

### Cloud Install

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/installation/install_cloud.html

* [Installation](index.html)
* Cloud Deployment

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Cloud Deployment

Isaac Sim is offered as a container that runs locally or on NVIDIA Brev and other Cloud service providers with the ability to stream the application directly to your desktop. This cloud-based delivery provides the latest RTX graphics and performance to any desktop system without requiring local NVIDIA RTX GPUs.

We have the following options available depending on your Cloud provider.

| Cloud Environment | Link |
| --- | --- |
| Isaac Launchable | [Isaac Launchable Instructions](install_advanced_cloud_setup_launchable.html) |
| NVIDIA Brev | [NVIDIA Brev Instructions](install_advanced_cloud_setup_brev.html) |
| AWS | [Amazon Web Instructions](install_advanced_cloud_setup_aws.html) |
| Azure | [Microsoft Cloud Instructions](install_advanced_cloud_setup_azure.html) |
| GCP | [Google Cloud Instructions](install_advanced_cloud_setup_gcp.html) |
| Tencent | [Tencent Cloud Instructions](install_advanced_cloud_setup_tencent.html) |
| Alibaba | [Alibaba Cloud Instructions](install_advanced_cloud_setup_alibaba.html) |
| Volcano Engine | [Volcano Engine Instructions](install_advanced_cloud_setup_volcano.html) |
| Baidu | [Baidu Cloud Instructions](install_advanced_cloud_setup_baidu.html) |
| Remote | [Remote Workstation Instructions](install_advanced_remote_setup.html) |

Note

* The links above provide Cloud Deployment instructions that include where you can access your instances via SSH and a remote desktop client.
* The [Isaac Automator](https://github.com/isaac-sim/IsaacAutomator) is an advanced tool that helps to automate a custom Isaac Sim deployment to public clouds. This tool allows you to access Isaac Sim instances via SSH, web-based VNC client, and remote desktop clients. AWS, Azure, GCP, and Alibaba Cloud are supported.
* If you have trouble or concerns, make your voice heard on the [Omniverse Forums](https://forums.developer.nvidia.com/c/omniverse/simulation/69).

---


## 远程

### Advanced Remote Setup

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/installation/install_advanced_remote_setup.html

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

---


## 远程可视化

### Livestream Clients

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/installation/manual_livestream_clients.html

* [Installation](index.html)
* Livestream Clients

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Livestream Clients

This section shows you the methods of livestreaming a headless instance of Isaac Sim.

Warning

Isaac Sim livestreaming (both the native desktop client and the web-based viewer) is designed
for use on private or trusted networks. The streaming endpoints do not include authentication or
encryption. Do **not** expose them on the public Internet without additional safeguards such as a
reverse proxy with HTTPS/TLS and authentication (e.g. nginx with SSL certificates and basic auth).
When deploying on cloud VMs, restrict the streaming ports to your client IP using firewall rules.
Users are responsible for securing any public-facing deployments.

Note

* Only one method of streaming can be used at a time for each Isaac Sim instance.
* Only one client can access an Isaac Sim instance at a time.
* To exit the Isaac Sim app remotely: Click the **File** menu, then click **Exit** in the streamed Isaac Sim app. Next, close the Isaac Sim WebRTC Streaming Client app.
* Livestreaming is not supported when Isaac Sim is run on the A100 GPU. NVENC (NVIDIA Encoder) is required for livestreaming and is not included in the A100 GPU.
* See [Video Encode and Decode Support Matrix](https://developer.nvidia.com/video-encode-decode-support-matrix) for supported GPU with NVENC.
* By downloading or using the NVIDIA Isaac Sim WebRTC Streaming Client, you agree to the [NVIDIA Isaac Sim WebRTC Streaming Client License Agreement](../common/license-isaac-sim-webrtc-streaming-client.html).
* Client platform support and Isaac Sim host platform support are separate. Use the downloads listed in the [Latest Release](download.html#isaac-sim-latest-release) section for supported client packages.

There are two ways to connect to a livestreaming Isaac Sim instance:

* **Isaac Sim WebRTC Streaming Client** — A native desktop application available for Windows, macOS, and Linux.
  Download it from the [Latest Release](download.html#isaac-sim-latest-release) section. Best suited for local or same-network connections.
* **Web-based viewer (Docker Compose)** — A browser-based client deployed alongside Isaac Sim using Docker Compose.
  Runs in any Chromium-based browser with no installation required. Recommended for cloud
  and remote deployments. See [Web-Based Streaming Client (Docker Compose)](#isaac-sim-web-streaming-client) below.

## Isaac Sim WebRTC Streaming Client

Isaac Sim WebRTC Streaming Client is the recommended streaming client to view Isaac Sim remotely on your desktop or workstation without a powerful GPU.

1. To use the Isaac Sim WebRTC Streaming Client, run Isaac Sim using one of the following methods:

Linux

See [Workstation Installation](install_workstation.html#isaac-sim-app-install-workstation) for full installation instructions.

```python
cd ~/isaacsim
./isaac-sim.streaming.sh
```

Windows

See [Workstation Installation](install_workstation.html#isaac-sim-app-install-workstation) for full installation instructions.

```python
cd C:\isaacsim
isaac-sim.streaming.bat
```

Docker (x86\_64)

See [Container Installation](install_container.html#isaac-sim-app-install-container) for full installation instructions.

```python
cd /isaac-sim
./runheadless.sh
```

Important

The container must be started with `--network=host` for livestreaming to work.
Docker bridge networking (`-p` port mapping) does not work with WebRTC because
the host IP is not reachable from inside the container’s network namespace.

For a simpler setup, Docker Compose is recommended for containerized streaming. It handles volume mounts, GPU assignment, networking, and health checks automatically. See [Web-Based Streaming Client (Docker Compose)](#isaac-sim-web-streaming-client) below or the [Docker README](https://github.com/isaac-sim/IsaacSim/blob/main/tools/docker/README.md) for details.

PIP

See [Python Environment Installation](install_python.html#isaac-sim-app-install-python) for full installation instructions.

```python
isaacsim isaacsim.exp.full.streaming --no-window
```

Python Sample

See [Python Environment](../python_scripting/manual_standalone_python.html#isaac-sim-python-environment) for full installation instructions.

```python
./python.sh standalone_examples/api/isaacsim.simulation_app/livestream.py
```

Note

* The machine running Isaac Sim must have an NVIDIA GPU with NVENC support and a compatible NVIDIA driver. On Linux hosts, `nvidia-smi` confirms the GPU and driver version. In containers, confirm the NVIDIA Container Toolkit exposes the encode library with `ldconfig -p | grep libnvidia-encode`.
* To run Isaac Sim on remote instance to be connected via the Internet, add these flags: `--/exts/omni.kit.livestream.app/primaryStream/publicIp=<PUBLIC_IP> --/exts/omni.kit.livestream.app/primaryStream/signalPort=49100 --/exts/omni.kit.livestream.app/primaryStream/streamPort=47998`
* For an example in a Docker container:

```python
PUBLIC_IP=$(curl -s ifconfig.me) && ./runheadless.sh --/exts/omni.kit.livestream.app/primaryStream/publicIp=$PUBLIC_IP --/exts/omni.kit.livestream.app/primaryStream/signalPort=49100 --/exts/omni.kit.livestream.app/primaryStream/streamPort=47998
```

* Use the same Public IP in the **Isaac Sim WebRTC Streaming Client** app.
* The following ports must be opened on the host running Isaac Sim:

  | Port | Protocol | Purpose |
  | --- | --- | --- |
  | `49100` | TCP | WebRTC signaling |
  | `47998` | UDP | WebRTC media stream |
  | `8210` | TCP | Web viewer (Docker Compose only) |
* If the client shows a black screen or the ports are not listening, first confirm the Isaac Sim app reached the loaded state. For containers, confirm the container was started with `--network=host`. For cloud or remote hosts, confirm the public IP passed to Isaac Sim is the same IP used by the client. Firewalls must allow both TCP `49100` and UDP `47998`; opening only TCP ports is not sufficient for WebRTC media.

2. Make sure that the Isaac Sim app is loaded and ready. It can take a few minutes for Isaac Sim to be completely loaded the first time.
3. To confirm this, look for the following message in the terminal/console output or the application logs. This line may not appear when running using PIP or Python Sample.

```python
Isaac Sim Full Streaming App is loaded.
```

4. Download **Isaac Sim WebRTC Streaming Client** from the [Latest Release](download.html#isaac-sim-latest-release) section for your platform.
5. Run the **Isaac Sim WebRTC Streaming Client** app.

6. Use the default **127.0.0.1** IP address as the server to connect to a local instance of Isaac Sim.
7. Click **Connect**. The connection process may take a few moments. You should see the Isaac Sim interface appear in the client window once connected.

Note

* Isaac Sim WebRTC Streaming Client is recommended to be used within the same network as an Isaac Sim headless instance.
* To connect to a headless instance of Isaac Sim in the same network, replace **127.0.0.1** with the IP address of the machine running Isaac Sim.
* On Linux: install the Debian package.

  > + Debian package (Ubuntu / Debian, with menu integration):
  >
  >   ```python
  >   sudo dpkg -i ./isaacsim-webrtc-streaming-client-*-linux-*.deb
  >   sudo apt -f install
  >   dpkg -l | grep isaacsim-webrtc-streaming-client
  >   ```
  >
  >   Then launch **Isaac Sim WebRTC Streaming Client** from the application menu or run
  >   `isaacsim-webrtc-streaming-client` from a terminal.
  > + No FUSE or AppImage runtime is required by the package; it runs on Ubuntu 22.04,
  >   24.04, and later without additional system libraries beyond a standard desktop
  >   environment.
  > + On Ubuntu 24.04 or later, Electron’s sandbox requires unprivileged user namespaces.
  >   If the client fails to launch with a SUID sandbox error, enable them with:
  >
  >   ```python
  >   sudo sysctl -w kernel.unprivileged_userns_clone=1
  >   sudo sysctl -w kernel.apparmor_restrict_unprivileged_userns=0
  >   ```
  >
  >   The `sysctl -w` settings are temporary and reset after reboot. To make
  >   them persistent, add them to a file under `/etc/sysctl.d/`:
  >
  >   ```python
  >   sudo tee /etc/sysctl.d/99-electron-sandbox.conf >/dev/null <<'EOF'
  >   kernel.unprivileged_userns_clone=1
  >   kernel.apparmor_restrict_unprivileged_userns=0
  >   EOF
  >   sudo sysctl --system
  >   ```
* On Windows:

  > + If you have issues connecting to a local or remote Isaac Sim instance, make sure the /kit/kit.exe and **Isaac Sim WebRTC Streaming Client** app is on the allow list in the Windows Firewall.
* On Mac:

  > + Open the DMG file then click and drag the **Isaac Sim WebRTC Streaming Client** app to the **Applications** folder icon to install.
  > + When streaming Isaac Sim app, use `Ctrl+C` and `Ctrl+V` to copy and paste respectively within the streamed app.
  > + To copy from host to client, use `⌘C` and `Ctrl+V`.
* To reload the connection, click **Reload** in the **View** menu. This may be useful if you see a blank screen after some time.

## Web-Based Streaming Client (Docker Compose)

As an alternative to the native desktop client, you can stream Isaac Sim to any Chromium-based browser using a web-based WebRTC client deployed alongside Isaac Sim via Docker Compose.

For full details on Docker Compose configuration, multi-instance deployment, and environment variables, see the [Docker README](https://github.com/isaac-sim/IsaacSim/blob/main/tools/docker/README.md).

This method does not require downloading or installing a native application. The web viewer is built from the [NVIDIA Omniverse Web SDK](https://docs.omniverse.nvidia.com/ov-web-sdk/latest/web-sample/overview.html) (`@nvidia/create-ov-web-rtc-app`) and connects to Isaac Sim over WebRTC.

Note

Docker Compose web viewer deployment is supported only on Ubuntu hosts and DGX Spark systems.
Windows hosts, including WSL, are not supported.

**Quick Start:**

```python
# Create cache/log mounts (use uid 1234 to match container user)
mkdir -p ~/docker/isaac-sim/{cache/main,cache/computecache,config,data,logs,pkg}
mkdir -p ~/.cache/ov/hub
sudo chown -R 1234:1234 ~/docker ~/.cache/ov/hub

# Build the Isaac Sim image (skip if using a prebuilt NGC image)
./tools/docker/prep_docker_build.sh --build --x86_64
./tools/docker/build_docker.sh --x86_64

# Launch Isaac Sim + web viewer
docker compose -p isim -f tools/docker/docker-compose.yml up --build -d

# Check the web viewer URL
docker compose -p isim logs web-viewer
```

Note

On DGX Spark, use `--aarch64` instead of `--x86_64` in the build commands above.

Open the URL shown in the logs (e.g. `http://<host-ip>:8210`) in a Chromium-based browser.

If Docker Compose reports a Hub startup or connectivity issue after a previous test, restart the Hub container from
[Hub Workstation Cache](install_container.html#isaac-sim-hub-workstation-cache) and retry Docker Compose.

To use a prebuilt NGC image instead of building locally:

```python
ISAAC_SIM_IMAGE=nvcr.io/nvidia/isaac-sim:6.0.0 docker compose -p isim -f tools/docker/docker-compose.yml up --build -d
```

**Keyboard Shortcuts:**

| Action | Windows / Linux | Mac |
| --- | --- | --- |
| Copy / paste | **Ctrl+C** / **Ctrl+V** | **Ctrl+C** / **Ctrl+V** |
| Refresh the browser page | **F5** or **Ctrl+R** | **Fn+F5** or **Cmd+R** |
| Maximize viewport in Isaac Sim | **F7** | **Fn+F7** |
| Toggle browser fullscreen | **F11** | **Shift+Fn+F11** |
| Open DevTools | **F12** | **Fn+F12** or **Cmd+Option+I** |

Note

* The browser Clipboard API requires a secure context. When accessing the web viewer over HTTP from a non-localhost address, clipboard forwarding to Isaac Sim is blocked. To enable it in Chrome, open `chrome://flags/#unsafely-treat-insecure-origin-as-secure`, add the web viewer URL (e.g. `http://192.168.1.100:8210`), and relaunch Chrome.
* The web viewer supports multi-instance deployment with dedicated GPUs, custom ports, and more. See the [Docker README](https://github.com/isaac-sim/IsaacSim/blob/main/tools/docker/README.md) for full configuration details.

On this page

* [Isaac Sim WebRTC Streaming Client](#isaac-sim-short-webrtc-streaming-client)
* [Web-Based Streaming Client (Docker Compose)](#web-based-streaming-client-docker-compose)

---


## 云厂商

### Cloud: Alibaba

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/installation/install_advanced_cloud_setup_alibaba.html

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

---

### Cloud: AWS

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/installation/install_advanced_cloud_setup_aws.html

* [Installation](index.html)
* [Cloud Deployment](install_cloud.html)
* AWS Deployment

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# AWS Deployment

## Requirements

The requirements for running NVIDIA Isaac Sim on Amazon Web Services (AWS) are:

1. An AWS account that is able to launch an EC2 instance with RTX GPU support.
2. An Amazon EC2 [key pair](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html) for authentication.
3. An Amazon EC2 [security group](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security-groups.html) to control access to ports:

   * TCP Port 22 for SSH
   * TCP Port 8443 for DCV
   * TCP Port 49100 for WebRTC streaming
   * UDP Port 47998 for WebRTC streaming
4. [PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html), or other SSH terminal client to connect to the AMI instance.
5. [DCV Client](https://www.amazondcv.com) or Remote Desktop app (For Windows EC2 instance).

## Setup

Follow these steps to launch an AWS EC2 instance:

1. Navigate to the [AWS Marketplace](https://aws.amazon.com/marketplace/search/results?searchTerms=isaac+sim) and search for “isaac sim”.
2. Select one of the instance type below:

Linux Instance

**NVIDIA Isaac Sim™ Development Workstation (Linux)**

* This will create an EC2 instance based on Ubuntu.

Windows Instance

**NVIDIA Isaac Sim™ Development Workstation (Windows)**

* This will create an EC2 instance based on Windows Server.

3. To deploy an AWS EC2 instance, click the **View purchase options** button.
4. If you have not already subscribed to the software, you will need to *Accept Terms* the first time. (This may take a few minutes to complete.)
5. When the subscription is complete, click the **Continue to Configuration** button.
6. On the *Configure this software* page, click the **Continue to Launch** button.
7. On the *Launch this software* page:

   * Set the **Choose Action** option to **Launch through EC2**.
   * Click the **Launch** button.
8. On the *Launch an instance* page, name your instance.
9. Set the *Instance type* to **g6e.2xlarge** or **g7e.8xlarge**, if not already listed.
10. Set the *Key Pair (login)* to use your pre-configured [key pair](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html).
11. In the *Network settings* section, select the **Select existing security group** option. In the **Common security groups** dropdown, select your [security group](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security-groups.html).
12. In the **Summary** section on the right side of the page, click **Launch instance**.
13. Locate your named instance in the table. It will take a few moments for the instance state to change from *Initializing* to *Running*. Once it’s running, it’s available to be connected to.

## Connect

Before you log in, make sure that:

* The AMI instance is running
* [PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html) (or other SSH terminal software) is installed
* The [DCV Client](https://www.amazondcv.com) is installed
* Your [key pair](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html) is created

Follow the instructions below depending on the OS you are running and the instance type:

Linux Instance

1. Copy the Public IP Address of your instance. You can find this by:

   * Clicking the checkbox next to your instance to select it.
   * In the information panel below the table, find the **Public IPv4 address** and copy it.
2. Open up PuTTY

   * In the *Host Name (or IP Address)* input, paste your instances Public IPv4 address.
   * Expand *Connection > SSH > Auth >* **Credentials**. Browse to the location of your Key Pair, and select it.
   * Select **Open** in the PuTTY dialog to connect.

   Note

   Using the Terminal, you can connect using the command `ssh -i <my_key_pair>.pem ubuntu@<public_ip>`.
3. When you are connected to the AMI, change the password. The password **must** be changed for DCV to connect in a later step.

   * Change the password for the Ubuntu account in order to use the DCV client. Use the following command to change the password: `sudo passwd ubuntu`.

   Note

   The password needs to be set via SSH each time a new instance is created, this is by design for security.

   * Enter a new password.
   * Check your session is running by using the following command: `sudo dcv list-sessions`. (There should be a ‘console’ session running.)

Windows Instance

1. Select your instance from the EC2 page and from the toolbar select **Connect**.
2. On the *Connect to instance* page select the **RDP Client** tab.
3. Set your username and then select **Get password**.
4. Upload your private key file associated with the instance and select **Decrypt password**.
5. Use this username and password to log in when you connect with the [DCV Client](https://www.amazondcv.com) or Remote Desktop app.

### Connect to the Instance with DCV Client

The [DCV Client](https://www.amazondcv.com) is available for Windows, macOS, and Linux. Install it on your local machine, then:

1. Open the locally installed [DCV Client](https://www.amazondcv.com) and enter the Public IP Address of your instance in this format `https://<public_ip>:8443`, followed by clicking **Connect**.

   * If you see the Server Identity Check message, click **Trust and Connect**.
   * Log in by entering the username `ubuntu` (or your Windows username) and the password that was set in a previous step, followed by clicking **Login**.
   * The desktop GUI will now be displayed in the DCV window.

Note

You can also use the DCV Web Browser Client by navigating to `https://<public_ip>:8443` on a browser.

You have now logged in and your AWS instance is ready for use.

## Running Isaac Sim

1. Follow the instructions below depending on the EC2 instance type selected in the previous section:

Linux Instance

1. Open Terminal and run the commands below:

```python
sudo chown -R ubuntu:root /opt/IsaacSim
cd ~/IsaacSim
./post_install.sh
./warmup.sh
./isaac-sim.sh
```

Note

The warm up script may take 15 minutes or longer to complete.

Windows Instance

1. Using the File Explorer, navigate to `C:\IsaacSim`.
2. Run `post_install.bat`.
3. Run `warmup.bat`.
4. Run `isaac-sim.bat`.

Note

The warm up script may take 15 minutes or longer to complete.

2. Proceed to [Quick Tutorials](../introduction/quickstart_index.html#isaac-sim-intro-quickstart-series) to begin the first Basic Tutorial.

See also

[Using Omniverse AMIs on the AWS Marketplace](https://docs.omniverse.nvidia.com/developer_workstations/latest/aws/overview.html "(in Omniverse Developer Workstations)")

## Running Isaac Sim Container

Warning

Isaac Sim livestreaming is designed for use on private or trusted networks. The streaming
endpoints do not include authentication or encryption. When deploying on cloud VMs, restrict the
streaming ports (49100/tcp, 47998/udp, 8210/tcp) to your client IP in the EC2 Security Group rather
than allowing all traffic. If you need broader access, add a reverse proxy with HTTPS/TLS and
authentication. Users are responsible for securing any public-facing deployments.

1. Follow the instructions below on a Linux EC2 instance:

Linux Instance

1. Open ports for WebRTC Streaming:

```python
sudo ufw allow 49100/tcp comment 'Isaac Sim WebRTC signal'
sudo ufw allow 47998/udp comment 'Isaac Sim WebRTC stream'
sudo ufw allow 8210/tcp  comment 'Isaac Sim web viewer (Docker Compose)'
sudo ufw reload
```

Also add corresponding inbound rules to the EC2 **Security Group**:

| Port | Protocol | Purpose |
| --- | --- | --- |
| `49100` | TCP | WebRTC signaling |
| `47998` | UDP | WebRTC media stream |
| `8210` | TCP | Web viewer (Docker Compose only) |

Restrict the **Source** to your client IP (e.g. `<your-ip>/32`) rather than `0.0.0.0/0` to avoid exposing the unauthenticated stream to the public Internet.

2. Install the NVIDIA Container Toolkit:

```python
# Configure the repository
$ curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
    && curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | \
    sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
    sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list \
    && \
    sudo apt-get update

# Install the NVIDIA Container Toolkit packages
$ sudo apt-get install -y nvidia-container-toolkit
$ sudo systemctl restart docker

# Configure the container runtime
$ sudo nvidia-ctk runtime configure --runtime=docker
$ sudo systemctl restart docker

# Verify NVIDIA Container Toolkit
$ docker run --rm --runtime=nvidia --gpus all nvcr.io/nvidia/cuda:12.8.0-base-ubuntu24.04 nvidia-smi
```

3. Pull the [Isaac Sim Container](https://catalog.ngc.nvidia.com/orgs/nvidia/containers/isaac-sim):

```python
$ docker pull nvcr.io/nvidia/isaac-sim:6.0.0
```

4. Create the cached volume mounts on host:

```python
$ mkdir -p ~/docker/isaac-sim/cache/main/ov
$ mkdir -p ~/docker/isaac-sim/cache/main/warp
$ mkdir -p ~/docker/isaac-sim/cache/computecache
$ mkdir -p ~/docker/isaac-sim/config
$ mkdir -p ~/docker/isaac-sim/data/documents
$ mkdir -p ~/docker/isaac-sim/data/Kit
$ mkdir -p ~/docker/isaac-sim/logs
$ mkdir -p ~/docker/isaac-sim/pkg
$ sudo chown -R 1234:1234 ~/docker/isaac-sim
```

5. Run the Isaac Sim container with an interactive Bash session:

```python
$ docker run --name isaac-sim --entrypoint bash -it --gpus all -e "ACCEPT_EULA=Y" --rm --network=host \
    -e "PRIVACY_CONSENT=Y" \
    -v ~/docker/isaac-sim/cache/main:/isaac-sim/.cache:rw \
    -v ~/docker/isaac-sim/cache/computecache:/isaac-sim/.nv/ComputeCache:rw \
    -v ~/docker/isaac-sim/logs:/isaac-sim/.nvidia-omniverse/logs:rw \
    -v ~/docker/isaac-sim/config:/isaac-sim/.nvidia-omniverse/config:rw \
    -v ~/docker/isaac-sim/data:/isaac-sim/.local/share/ov/data:rw \
    -v ~/docker/isaac-sim/pkg:/isaac-sim/.local/share/ov/pkg:rw \
    -u 1234:1234 \
    nvcr.io/nvidia/isaac-sim:6.0.0
```

Note

* By using the `-e "ACCEPT_EULA=Y"` flag, you accept the license agreement of the image found at [NVIDIA Omniverse License Agreement](../common/NVIDIA_Omniverse_License_Agreement.html).
* By using the `-e "PRIVACY_CONSENT=Y"` flag, you opt-in to the data collection agreement found at [Data Collection & Usage](../common/data-collection.html). You may opt-out by not setting this flag.
* The `-e "PRIVACY_USERID=<email>"` flag can optionally be set for tagging the session logs.
* Add the `--runtime=nvidia` flag if there are issues detecting the GPU in the container.

6. Start Isaac Sim with native livestream mode:

```python
$ PUBLIC_IP=$(curl -s ifconfig.me) && ./runheadless.sh --/exts/omni.kit.livestream.app/primaryStream/publicIp=$PUBLIC_IP --/exts/omni.kit.livestream.app/primaryStream/signalPort=49100 --/exts/omni.kit.livestream.app/primaryStream/streamPort=47998
```

7. Connect to the same public IP address of the instance using the [Isaac Sim WebRTC Streaming Client](manual_livestream_clients.html#isaac-sim-setup-livestream-webrtc) app.

Alternatively, use Docker Compose to deploy Isaac Sim with a browser-based web viewer instead of the native streaming client:

```python
$ ISAACSIM_HOST=$PUBLIC_IP ISAAC_SIM_IMAGE=nvcr.io/nvidia/isaac-sim:6.0.0 \
    docker compose -p isim -f tools/docker/docker-compose.yml up --build -d
```

Then open `http://<PUBLIC_IP>:8210` in a Chromium-based browser. See [Docker Compose Deployment (Isaac Sim + Web Viewer)](install_container.html#isaac-sim-docker-compose-deployment) or the [Docker README](https://github.com/isaac-sim/IsaacSim/blob/main/tools/docker/README.md) for full details.

See also

* [Container Deployment](install_container.html#isaac-sim-setup-remote-headless-container)
* [Livestream Clients](manual_livestream_clients.html#isaac-sim-manual-livestream-client)

On this page

* [Requirements](#requirements)
* [Setup](#setup)
* [Connect](#connect)
  + [Connect to the Instance with DCV Client](#connect-to-the-instance-with-dcv-client)
* [Running Isaac Sim](#running-isaac-sim)
* [Running Isaac Sim Container](#running-isaac-sim-container)

---

### Cloud: Tencent

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/installation/install_advanced_cloud_setup_tencent.html

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

---


## 性能优化

### Performance Optimization

> 来源: https://docs.isaacsim.omniverse.nvidia.com/latest/reference_material/sim_performance_optimization_handbook.html

* Isaac Sim Performance Optimization Handbook

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Isaac Sim Performance Optimization Handbook

## Understanding Isaac Sim Performance

The speed of the simulation can be influenced by a variety of factors. The physics step size, complexity of the scene, number of physics objects, and quantity/resolution of cameras and sensors all play a role in simulation performance. The below tips address common performance optimizations for each of these factors.

Note

The [Isaac Sim Benchmarks](benchmarks.html#isaac-sim-benchmarks-measuring-kpis) page contains common workflows to evaluate performance as well as specific optimization recommendations based on the workflow.

Note

To identify performance bottlenecks, profiling the simulation can be helpful. See [Profiling Performance Using Tracy](../utilities/debugging/profiling_performance.html#isaac-sim-app-profiling-performance) for details on using the Tracy profiler to profile the simulation.

## Physics Simulation Optimizations

1. **Physics Step Size**: The physics step size determines the time interval for each physics simulation step.

* A smaller step size will result in a more accurate simulation but will also require more computational resources and thus slow down the simulation.
* A larger step size will speed up the simulation but may result in less accurate physics.

Note

Adjust the physics step size in your script using the `SimulationManager.set_physics_dt(dt)` function, where dt is the desired step size in seconds.

2. **PhysX Minimum Frame Rate Clamp** (`--/persistent/simulation/minFrameRate`): caps how many `physics_dt` substeps PhysX will run per app update to catch up after a slow frame. The value represents the target minimum app frame rate; PhysX will not run so many catch-up substeps in one update that the effective frame rate would drop below it. This is a direct performance-vs-accuracy knob:

* **Raising the clamp** (for example to `60`) keeps the app frame rate up under load at the cost of physics-time accuracy: when an app update is slow, PhysX truncates the substep budget, so simulated time falls behind wall-clock and the simulation appears to run in slow motion (or, equivalently, some physics work is effectively dropped). Use this when responsiveness / rendering throughput matters more than 1:1 sim-time-to-wall-time playback.
* **Lowering the clamp** (for example to `15`) lets PhysX run more catch-up substeps after a slow frame, keeping simulated time closer to wall-clock at the cost of further reducing the visible frame rate. Use this when sim-time accuracy or determinism matters more than smoothness.

This setting is **not** the same as the timeline’s `targetFrameRate` (set via `isaacsim.core.rendering_manager.RenderingManager.set_dt()`) or the loop runner’s `/app/runLoops/main/rateLimitFrequency`. See [Architecture: Timeline, Physics, and the Renderer](../sensors/isaacsim_sensors_multitick_rendering.html#isaac-sim-sensors-multitick-clock-relationships) for the three-clock architecture.

Note

Adjust the PhysX minimum frame rate clamp by modifying the `--/persistent/simulation/minFrameRate=<value>` setting, where `<value>` is the target minimum app frame rate in FPS.

3. **GPU Dynamics**: Enabling GPU dynamics can potentially speed up the simulation by offloading the physics calculations to the GPU.

Note

This will only be beneficial if your GPU is powerful enough and not already fully utilized by other tasks.
Enable or disable GPU dynamics in your script using the `SimulationManager.set_physics_sim_device(device)` function, where device is a string value of either `cuda` or `cpu`. In multi-GPU setups, a specific device can be specified by passing the device index as part of the string such as `cuda:0`.

4. **Physics Scene Complexity**: The complexity of the physics objects in the scene will heavily impact the performance of the simulation.

* Simple colliders are typically the most performant. The performance scaling is as follows:

  > + Primitive colliders (box, sphere, capsule, plane) are most performant.
  > + Convex meshes are the next most performant (Convex Hull or Convex Decomposition approximation)
  > + Cylinders are a good choice for smooth, precise rolling behavior but are more expensive than a low-vertex convex mesh approximation.
* Disable or simplify colliders that are not essential for the workflow being simulated. For example, if a robot is not expected to interact with the walls of a room, the wall colliders could be disabled while keeping the floor collider enabled.

  > + Similarly, avoid unnecessary collisions. Where possible, reduce the number of object overlaps to reduce the overhead in the collision phase of the simulation.

Note

This applies to both the scene as a whole and individual physics objects. Complex colliders on highly-articulated robots as well as many complex collision meshes on walls, tables, etc. all add to the computational cost.

5. **Adjusting PhysX Thread Count**: The number of threads used by PhysX can be adjusted to improve performance depending on the workload.

Note

This is specifically applicable for CPU-based physics simulation. Dropping thread count to 0 will run synchronously on the main thread which in some simple scenes can enable speedups. The default thread count is 8. Set the thread count using `--/persistent/physics/numThreads=<value>`.

Checkout the [Physics Simulation Performance](https://docs.omniverse.nvidia.com/kit/docs/omni_physics/latest/dev_guide/guides/physics-performance.html) guide for more optimization tricks!

## Robot Asset Optimizations

A step-by-step tutorial to optimize a sample asset is provided in [Tutorial 12: Asset Optimization](../robot_setup_tutorials/optimizing_asset.html#isaac-asset-optimization).

1. **Merge Mesh Tool**: Using the Merge Mesh tool at **Tools** > **Robotics** > **Asset Editors** > **Mesh Merge Tool** can allow for a more streamlined asset structure and reduction in total mesh count.
2. **Scenegraph Instancing**: Instancing enables shareable, referenceable prim subgraphs. Using pointers to shared reference assets can reduce total memory usage for assets with repeated, identical meshes (e.g. wheels).

   * An example of instancing is described in [Tutorial 12: Asset Optimization](../robot_setup_tutorials/optimizing_asset.html#isaac-asset-optimization). A general guide to instanceable assets can be found at [Instanceable Assets](../isaac_lab_tutorials/tutorial_instanceable_assets.html#isaac-sim-app-tutorial-instanceable-assets).

Note

Instancing inherently carries some limitations related to attributes as children cannot have modified attributes from the parent reference object.

3. **Simplify Colliders**: Colliders have high computational costs. The simpler, the collision shape, the more performant the simulation behaves.

   * A reduction in contact points brings substantial performance improvements. For wheel colliders, it’s recommended to use a simple cylinder or sphere collider instead of a mesh collider. This greatly simplifies contact with the ground plane, increasing performance and allows the robot to drive smoothly over terrain.
   * For a robot, use the simplest approximations possible that provide the needed level of precision. For example, for a mobile robot, a cube approximation is often sufficient for the body.
   * Reducing the total number of colliders is also beneficial. Consider whether every collider added to the asset needs to be enabled. Selectively disabling/enabling colliders can greatly reduce computational cost.

Note

Higher precision applications require using mesh colliders rather than simplified shapes. There are different approximations available and the choice of each one is a tradeoff between performance and precision.

4. **Disable Self Collisions**: Disabling self collisions from an Articulation Root could reduce computational load and create substantial speedups at runtime if not needed.

Note

This is highly usecase-dependent. With a complex articulated hand, self collisions are necessary to avoid interpenetrations and provide realistic collisions. For a wheeled mobile robot with some internal geometries, it is likely an unnecessary load to compute any collisions other than those with the external environment.

## Scene and Rendering Optimizations

For an overview of available renderer modes and when to use each one, see [Rendering modes](rendering_modes.html#isaac-sim-rendering-modes).

1. **Simplify the Scene**: Reducing the complexity of the scene, implementing level of detail (LOD), culling invisible objects, and optimizing the physics settings.

Note

Isaac Sim provides several tools for simplifying your scene

* [Scene Optimizer](https://docs.omniverse.nvidia.com/extensions/latest/ext_scene-optimizer.html): kit extension that performs scene optimization on the USD level
* [Mesh Merge Tool](../robot_setup/ext_isaacsim_util_merge_mesh.html#isaac-merge-mesh): Isaac Sim utility to merge multiple meshes to a single mesh

Note

During realtime simulation, the gizmos (including floor grids) automatically disappear to optimize performance. They reappear when the simulation is paused or stopped.

2. **Using RTX Real-Time 2.0**: (see [RTX - Real-Time 2.0 mode](https://docs.omniverse.nvidia.com/materials-and-rendering/latest/rtx-renderer_rt.html))

   > * RT2 is the new default rendering mode in Isaac Sim. It offers both accuracy and performance improvements over the previous RTX Real-Time mode.
   > * For training-in-the-loop or other workflows that prioritize throughput over full light transport, consider RTX - Minimal for faster performance. In standalone Python, set `renderer` to `MinimalRendering` in the `SimulationApp` launch configuration and use `minimal_shading_mode` to choose the simplified shading behavior. See [Rendering modes](rendering_modes.html#isaac-sim-rendering-modes) for mode selection guidance.
   > * The retrace threshold can be decreased to improve performance at the cost of a slightly more biased result. This will still be comparable in accuracy to the legacy RTX Real-Time mode.
   >
   >   > ```python
   >   > "--/rtx/pathtracing/cached/retrace=0.1"
   >   > ```
   > * Disabling Fractional Cutout Opacity may also improve performance at the cost of losing accuracy of translucency effects.
   >
   >   > ```python
   >   > "--/rtx/pathtracing/fractionalCutoutOpacity=false"
   >   > ```

Note

On some older hardware, specifically in the Ampere generation, performance of RT2 may fall lower than RTX Real-Time mode. Using the Retrace Threshold setting above shoud improve performance of RT2 above that of the legacy mode with comparable accuracy.

3. **Disable Materials and Lights**: (see [RT2 Mode](https://docs.omniverse.nvidia.com/materials-and-rendering/latest/rtx-renderer_rt.html) for specific RT2 and Path Tracing settings)

   > * Loading time can be drastically slowed down by a large quantity of materials in the scene. Loading materials can be disabled by setting:
   >
   >   > ```python
   >   > "--/app/renderer/skipMaterialLoading=true"
   >   > ```
   > * Disabling lights can simplify the rendering workload and improve performance.
   > * Turn off rendering features in the render settings panel (these will also have equivalent carb settings that can be set in python). There is no non-rtx rendering mode in the Isaac Sim GUI application, but you can disable almost everything (reflections, transparency, etc) to increase execution speed. To disable rendering completely unless explicitly needed by a sensor, you can use the headless application workflow.
4. **Adjust DLSS Performance Mode**: DLSS performance mode is toggled by the `--/rtx/post/dlss/execMode=<value>` setting. Values are as follows:

   > * Performance (`0`) - the most performant setting, reducing VRAM consumption and rendering time but decreasing render quality. This is the default value in Isaac Sim.
   > * Balanced (`1`) - offers both optimized performance and image quality.
   > * Quality (`2`) - offers higher image quality than balanced mode, at the cost of increased render time and VRAM consumption.
   > * Auto (`3`) - Selects the best DLSS Mode for the current output resolution. When rendering 720p cameras, Auto mode tends to select Quality, so you may see performance impacts by running in Auto mode while rendering cameras at lower resolution.

Note

The DLSS mode is currently set to `Performance` by default. `Performance` mode will yield the best performance, but may result in artifacts such as smearing when rendering cameras at lower resolutions (720p or lower).

5. **Disabling viewport updates in headless mode**: Running in headless mode with `./python.sh` still renders the default viewport. This adds the overhead of rendering a view that may not be needed.

   > * To improve performance, viewport updates can be disabled by setting the `SimulationApp` configuration parameter `disable_viewport_updates=True`.
   >
   >   > ```python
   >   > from isaacsim import SimulationApp
   >   >
   >   > simulation_app = SimulationApp({"headless": True, "disable_viewport_updates": True})
   >   > ```
   > * When not using SimulationApp, users can also disable viewport updates with the following code snippet:
   >
   >   > ```python
   >   > from omni.kit.viewport.utility import get_active_viewport
   >   >
   >   > viewport = get_active_viewport()
   >   > viewport.updates_enabled = False
   >   > ```

Note

Setting `disable_viewport_updates` in SimulationApp is only supported if running in headless mode. For streaming usecases, this option should not be used.

6. **Disabling texture streaming**: Texture streaming is a feature that helps minimize GPU memory consumption, particularly in large scenes.

   > * Disabling texture streaming can have positive performance benefits but will result in increased GPU memory consumption. There’s also possible negative UX impacts if memory is running low - leading to crashes or missing some textures.
   > * To disable texture streaming, modify the value of the `/rtx-transient/resourcemanager/texturestreaming/enabled` setting.
   >
   >   > ```python
   >   > "--/rtx-transient/resourcemanager/texturestreaming/enabled=false"
   >   > ```

Note

This is not recommended for all use cases. It should be used on a case-by-case basis and evaluated for each workflow to determine its suitability. This may lead to unintended rendering behavior.

## CPU Thread Count Optimizations

Three settings control the number of CPU threads used by Isaac Sim. When left unset (the default behavior), Isaac Sim will use all available threads on the system. Standalone Python workflows are limited to 32 threads by default and can be modified by changing the `limit_cpu_threads` argument in the `SimulationApp` constructor.

1. `--/plugins/carb.tasking.plugin/threadCount`: Sets Carbonite’s maximum worker thread count.
2. `--/persistent/physics/numThreads`: Sets how many Carbonite worker threads to use for physics simulation.
3. `--/plugins/omni.tbb.globalcontrol/maxThreadCount`: Sets Omniverse TBB scheduler’s maximmum worker thread count.

Spawning too many worker threads may lead to CPU bottlenecking. Consider limiting the number of CPU threads used by Isaac Sim to fewer than the number of virtual cores on the system. Current testing indicates that 32 threads is optimal for most use cases.

For example, on Ubuntu:

```python
./isaac-sim.sh --/plugins/carb.tasking.plugin/threadCount=16 --/plugins/omni.tbb.globalcontrol/maxThreadCount=16
```

Standalone Python:

```python
from isaacsim import SimulationApp

simulation_app = SimulationApp({"headless": False, "limit_cpu_threads": 16})
```

## CPU Governor Settings on Linux

CPU governors dictate the operating clock frequency range and scaling of the CPU. This can be a limiting factor for Isaac Sim performance. For maximum performance, the CPU governor should be set to `performance`. To modify the CPU governor, run the following commands:

```python
sudo apt-get install linux-tools-common
cpupower frequency-info # Check available governors
sudo cpupower frequency-set -g performance # Set governor with root permissions
```

Note

Not all governors are available on all systems. Governors enabling higher clock speed are typically more performance-centric and can yield substantially better performance for Isaac Sim.

## Asynchronous Rendering

Asynchronous rendering is a feature that allows the rendering to run in a separate thread from the simulation thread. In Isaac Sim, asynchronous rendering is enabled by default whenever Isaac Sim is in a stoppped or paused state. This greatly improves UI responsiveness and viewport FPS, particularly for complex scenes.

### Asynchronous Rendering Toggle (Default)

This is set in the isaacsim.core.throttling extension. To disable this feature in the event of unexpected behavior, set the `exts."isaacsim.core.throttling".enable_async` setting to `false` when starting the application.

```python
./isaac-sim.sh --exts."isaacsim.core.throttling".enable_async=false
```

Note

This setting is only set true when running with `isaacsim.exp.full.kit`, not when running via a Python-based workflow. It could be enabled manually using the above setting for other workflows if desired.
In certain use cases, particularly with Replicator-based SDG workflows, it may be necessary to disable asynchronous rendering to ensure proper behavior.

### Runtime Asynchronous Rendering (Experimental)

Asynchronous rendering is experimentally supported during runtime. To enable asynchronous rendering for Python-based workflows, add the below arguments to the run command. For full Isaac Sim workflows, additionally disable the toggle in the *isaacsim.core.throttling* extension so that the application will always run asynchronously.

```python
./isaac-sim.sh --exts."isaacsim.core.throttling".enable_async=false --/app/asyncRendering=true --/app/omni.usd/asyncHandshake=true --/omni/replicator/asyncRendering=true

./python.sh script.py --/app/asyncRendering=true --/app/omni.usd/asyncHandshake=true --/omni/replicator/asyncRendering=true
```

Note

This feature is experimental and may lead to unexpected behavior. Enabling this feature will not necessarily lead to performance improvements. Possible speedups will heavily vary based on the use case and hardware, but are more likely given heavily CPU-bound workflows.

## Multi-GPU Support

The following rules of thumb may help improve multi-GPU performance, based on our multi-GPU benchmarks.

Note

Exact Isaac Sim performance metrics when using multiple data-center-grade GPUs can be found [here](benchmarks.html#isaac-sim-benchmarks-gpu-dependent).

1. **Add as many GPUs as cameras being rendered - but no more.** When rendering 2 720p cameras with 2 GPUs, we saw a speed up of 72% to 89% compared to single GPU performance, but using 4 GPUs yielded only 61 - 81% improvement.
2. **Performance scales better the more cameras you’re rendering.** Our 4 camera with 4x GPUs test scaled well with an overall speed up of about 213% - 233%, but our 8 camera with 4 GPUs test scaled even better with an overall speedup of 271% - 281%.
3. **Single high-resolution cameras render faster on multiple GPUs.** An exception to our earlier rules - if you are rendering a single high-resolution (4K or higher) camera, multiple GPUs can help accelerate rendering.
4. **Increasing GPU count does not improve scene load time.** GPU count does not influence the amount of time it takes to load a USD, or the maximum USD scene size that can be loaded.
5. **GPU Physics simulation only utilizes 1 GPU.** Increasing GPU count will not improve GPU physics simulation performance.

### Disabling IOMMU On Linux

Per the [CUDA C++ Programming Guide](https://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html#iommu-on-linux), users on bare-metal Linux should disable the IOMMU to improve multi-GPU performance.

IOMMU may be disabled from system BIOS (exact instructions vary based on motherboard specification), or from the command line via:

```python
sudo bash -c 'echo GRUB_CMDLINE_LINUX="amd_iommu=off" >> /etc/default/grub'
sudo update-grub
sudo reboot
```

After rebooting, the IOMMU should be disabled.

Note

If IOMMU is enabled, you will receive a warning like `IOMMU is enabled.` below the `nvidia-smi` output in the logs when running Isaac Sim.

## Reducing GPU Memory Utilization

These are suggestions to help reduce Isaac Sim GPU memory utilization:

1. Reduce the Texture Streaming Budget. Select the `Render Settings` tab, then select the `Common` settings. Under `Debug` > `Streaming Settings`, reduce `"Texture Streaming Budget (% of GPU memory)"`. By default this value is set to **0.6**, 60% of GPU memory capacity. To reduce GPU memory consumption, the number can be reduced further. For standalone Python workflows, you can modify the value of the `/rtx-transient/resourcemanager/texturestreaming/memoryBudget` setting.
2. Reduce total rendered pixel count by turning off unnecessary viewports or reducing rendered camera resolution, if possible.

## Experimental: Reducing Potential Memory Leaks

Experimental suggestion to help reduce Isaac Sim RAM consumption in the event of memory leaks in long-running workflows:

1. Adjusting the memory allocator to reduce memory leaks in long running workflows, particularly where stages are loaded and unloaded repeatedly.
   :   * To change the allocator configuration, set the following environment variable:

         > ```python
         > export GLIBC_TUNABLES=glibc.malloc.arena_max=1:glibc.malloc.mmap_max=0:glibc.malloc.mmap_threshold=2147483647
         > ```

## Useful Tools

### Windows

Task Manager is a great resource for giving nice clean graphs and can show peak usage on a variety of system information regarding performance.

1. Click on the Start icon
2. Type “Task Manager”
3. In Task Manager, Select the “Performance” Tab

On the left side of this pane you will see various graphs like CPU, Memory and GPU. Select any of these to get a more detailed view of the data. Generally speaking if any of these are spiking and peaking out, you should look into its cause and begin to troubleshoot.

### Linux

`nvidia-smi` is a great resource for giving useful data on Linux.

See these documents for further information:

* [NVIDIA-SMI](https://developer.nvidia.com/nvidia-system-management-interface)
* [NVIDIA-SMI Documentation (PDF)](http://developer.download.nvidia.com/compute/DCGM/docs/nvidia-smi-367.38.pdf)

On this page

* [Understanding Isaac Sim Performance](#understanding-isaac-sim-short-performance)
* [Physics Simulation Optimizations](#physics-simulation-optimizations)
* [Robot Asset Optimizations](#robot-asset-optimizations)
* [Scene and Rendering Optimizations](#scene-and-rendering-optimizations)
* [CPU Thread Count Optimizations](#cpu-thread-count-optimizations)
* [CPU Governor Settings on Linux](#cpu-governor-settings-on-linux)
* [Asynchronous Rendering](#asynchronous-rendering)
  + [Asynchronous Rendering Toggle (Default)](#asynchronous-rendering-toggle-default)
  + [Runtime Asynchronous Rendering (Experimental)](#runtime-asynchronous-rendering-experimental)
* [Multi-GPU Support](#multi-gpu-support)
  + [Disabling IOMMU On Linux](#disabling-iommu-on-linux)
* [Reducing GPU Memory Utilization](#reducing-gpu-memory-utilization)
* [Experimental: Reducing Potential Memory Leaks](#experimental-reducing-potential-memory-leaks)
* [Useful Tools](#useful-tools)
  + [Windows](#windows)
  + [Linux](#linux)

---

