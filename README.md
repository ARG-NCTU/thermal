# Thermal Tools

Clone this repo
```sh
git clone https://github.com/ARG-NCTU/thermal.git
```

## 1. Thermal Camera Spinview API

This guide provides step-by-step instructions to set up and run the thermal camera acquisition system using a virtual environment and ROS Noetic.

### 1.1. Prerequisites

- Ubuntu 20.04
- Python 3.8

### 1.2. Setup Instructions

#### 1.2.1. Install Environment on local

```sh
sudo apt-get update
sudo apt-get install libusb-1.0-0 libavcodec58 libavformat58 libswscale5 libswresample3 libavutil56 qt5-default
```

#### 1.2.2. Install Spinview API 

```sh
cd ~/thermal/spinnaker-3.0.0.118-amd64
sudo sh install_spinnaker.sh
```

#### 1.2.3. Run Spinview Application

If you cannot connect to thermal, please edit your network:
```sh
sudo apt-get install network-manager
nmtui
```
Change your thermal network from "Automatic" to "Link-local".

## 2. Thermal Camera Python

This guide provides step-by-step instructions to set up and run the thermal camera acquisition system using a virtual environment and ROS Noetic.

### 2.1. Prerequisites

- Ubuntu 20.04
- Python 3.8

### 2.2. Setup Instructions

#### 2.2.1. Install Python Virtual Environment Prerequisites

```sh
sudo apt-get install python3-pip
pip3 install virtualenv
```

#### 2.2.2. Create and Activate a Virtual Environment

Create a Python virtual environment to manage dependencies:

```sh
python3.8 -m venv thermal_env
source ~/thermal_env/bin/activate
```

After creating the Python virtual environment, just activate it
```sh
source ~/thermal_env/bin/activate
```

#### 2.2.3. Install Python Dependencies

Upgrade `numpy` and `matplotlib` and install other required packages:

```sh
python3.8 -m pip install --upgrade numpy matplotlib
python3.8 -m pip install spinnaker_python-3.0.0.118-cp38-cp38-linux_x86_64/spinnaker_python-3.0.0.118-cp38-cp38-linux_x86_64.whl
python3.8 -m pip install pyyaml
pip3 install rospkg empy
```

#### 2.2.4. Install ROS Noetic

Follow the instructions on the official ROS website to install ROS Noetic:

[ROS Noetic Installation Guide for Ubuntu](https://wiki.ros.org/noetic/Installation/Ubuntu)

#### 2.2.5. Install Additional ROS Packages

Install OpenCV for Python:

```sh
pip install opencv-python-headless
```

#### 2.2.6. Build the Catkin Workspace

Navigate to your catkin workspace and build it:

```sh
cd ~/thermal/catkin_ws
catkin_make -DPYTHON_EXECUTABLE=~/thermal_env/bin/python
```

#### 2.2.7. Source the Setup File

Source the setup file to overlay the workspace on your environment:

```sh
source ~/thermal/catkin_ws/devel/setup.bash
```

#### 2.2.8. Launch the Acquisition Node

Finally, launch the thermal camera acquisition node:

```sh
roslaunch thermal_cam acquisition.launch
```