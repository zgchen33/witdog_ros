# Some Functions of Witdog
## 1. Dance 
This dance function is based on [Mini Pupper](https://github.com/mangdangroboticsclub/mini_pupper_ros).
### 1.1 Run the base driver
    roslaunch witdog_config bringup.launch
### 1.2 Run the dance launch
    roslaunch witdog_functions dance.launch
After running the above two commands, you can see the Witdog dancing.
![dance](https://github.com/zgchen33/witdog_ros/raw/master/images/dance.gif)
For more dancing actions, you can revise dance_example0.json. Also you can write a new json file like dance_example0.json and change the argument "dance_config_path" in dance.launch.
There are 10 types of commands to define dance actions:
    move_forward: the robot will move forward
    move_backward: the robot will move backward
    move_left: the robot will move to the left
    move_right: the robot will move to the right
    look_up: the robot will look up
    look_down: the robot will look down
    look_left: the robot will look left
    look_right: the robot will look right
    stop: the robot will stop the last command and return to the default standing posture
    stay: the robot will keep the last command


