# Witdog ROS Repository

This is ROS packages for Witdog.

**（this is a image about Witdog's appearance）**

Witdog is a dog-shaped 12-DOF quadruped robot in small size, which is operated in ROS(Robot Operating System). The project is based on [champ](https://github.com/chvmp/champ) project.

Tested on:
- Ubuntu 18.04 (ROS Melodic)
- Ubuntu 20.04 (ROS Noetic)

# 1. Installation Guide
## 1.1 Clone and install all dependencies:
    sudo apt install -y python-rosdep
    cd <your_ws>/src
    git clone --recursive git@github.com:zgchen33/witdog_ros.git
    cd ..
    rosdep install --from-paths src --ignore-src -r -y

## 1.2 Build your workspace:
    cd <your_ws>
    catkin_make
    source <your_ws>/devel/setup.bash

# 2. Quick Start Guide

## 2.1 Calibration
    roslaunch servo_interface calibrate.launch
By default, the Witdog looks like this after calibrating. However, you can change the joint angles to what you want.

## 2.2 Walking

### 2.2.1 Run the base driver
    roslaunch witdog_config bringup.launch

### 2.2.2 Control Witdog

    roslaunch champ_teleop teleop.launch
# 3. Start Without a physical robot

You can run the following demos without a physical robot.
## 3.1 Walking demo in RVIZ:

### 3.1.1 Run the base driver:
    roslaunch witdog_config bringup.launch rviz:=true hardware_connected:=false

### 3.1.2 Run the teleop node:
    roslaunch champ_teleop teleop.launch

## 3.2 Walking demo in Gazebo:

### 3.2.1 Run the Gazebo environment:
    roslaunch witdog_config gazebo.launch 

Also, if you want to run SLAM demos or Autonomous Navigation, you are supposed to run the navigate.launch and slam.launch 

**TODO** complete the slam and navigation.






   

