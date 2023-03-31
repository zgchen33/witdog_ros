# Witdog ROS

This is ROS packages for Witdog.

![witdog](https://github.com/zgchen33/witdog_ros/raw/master/images/witdog.png)

Witdog is a dog-shaped 12-DOF quadruped robot in small size, which is operated in ROS(Robot Operating System). The project is based on [champ](https://github.com/chvmp/champ) project.

Tested on:
- Ubuntu 18.04 (ROS Melodic)
- Ubuntu 20.04 (ROS Noetic)

By the way, we used visual programming to improve the application of the project in education, as well as using AI modules to achieve more convenient upper layer intelligence applications, such as face detection, target detection, etc. You can get more information in **K210 branch** and **blockly branch**.
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

**TODO**: need a image of calibrating
## 2.2 Walking

### 2.2.1 Run the base driver
    roslaunch witdog_config bringup.launch

### 2.2.2 Control Witdog

    roslaunch champ_teleop teleop.launch
![dextrorotary](https://github.com/zgchen33/witdog_ros/raw/master/images/dextrorotary.gif)

## 2.3 Some Functions of Witdog
### 2.3.1 Dance 
This dance function is based on [Mini Pupper](https://github.com/mangdangroboticsclub/mini_pupper_ros).

    roslaunch witdog_config bringup.launch
Open a new terminal, and run the following command:
    roslaunch witdog_functions dance.launch
After running the above two commands, You can see the Witdog dancing.

**TODO: A gif is needed here**
# 3. Start Without a physical robot

You can run the following demos without a physical robot.
## 3.1 Walking demo in RVIZ:

### 3.1.1 Run the base driver:
    roslaunch witdog_config bringup.launch rviz:=true hardware_connected:=false
![witdog_rviz](https://github.com/zgchen33/witdog_ros/raw/master/images/witdog_rviz.png)
### 3.1.2 Run the teleop node:
    roslaunch champ_teleop teleop.launch

## 3.2 Walking demo in Gazebo:

### 3.2.1 Run the Gazebo environment:
    roslaunch witdog_config gazebo.launch 
![witdog_gazebo](https://github.com/zgchen33/witdog_ros/raw/master/images/witdog_gazebo.png)
Also, if you want to run SLAM demos or Autonomous Navigation, you are able to run the navigate.launch and slam.launch.






   

