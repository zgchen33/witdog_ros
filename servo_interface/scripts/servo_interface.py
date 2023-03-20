#!/usr/bin/python3
import os
import time
import rospy
from trajectory_msgs.msg import JointTrajectory

import sys, tty, termios
fd = sys.stdin.fileno()
old_settings = termios.tcgetattr(fd)

def getch():
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

from SCServo_Python import scservo_sdk            # Uses SCServo SDK library
PI_VALUE                    = 3.1415926535
BAUDRATE                    = 1000000
DEVICENAME                  = rospy.get_param("port")
SCS_MOVING_SPEED            = 3000        
SCS_MOVING_ACC              = 250          

ZERO_STANCE                 = 2048
RIGHT_ANGLE                 = 1024


portHandler = scservo_sdk.PortHandler(DEVICENAME)
packetHandler = scservo_sdk.sms_sts(portHandler)
# Open port
if portHandler.openPort():
    print("Succeeded to open the port")
else:
    print("Failed to open the port")
    print("Press any key to terminate...")
    getch()
    quit()

# Set port baudrate
if portHandler.setBaudRate(BAUDRATE):
    print("Succeeded to change the baudrate")
else:
    print("Failed to change the baudrate")
    print("Press any key to terminate...")
    getch()
    quit()


def callback(data):

    points = data.points[0]
    joint_positions = points.positions
    lf1_position = int((2048/PI_VALUE)*joint_positions[0])
    lf2_position = int((2048/PI_VALUE)*joint_positions[1])
    lf3_position = int((2048/PI_VALUE)*joint_positions[2])
    rf1_position = int((2048/PI_VALUE)*joint_positions[3])
    rf2_position = int((2048/PI_VALUE)*joint_positions[4])
    rf3_position = int((2048/PI_VALUE)*joint_positions[5])
    lh1_position = int((2048/PI_VALUE)*joint_positions[6])
    lh2_position = int((2048/PI_VALUE)*joint_positions[7])
    lh3_position = int((2048/PI_VALUE)*joint_positions[8])
    rh1_position = int((2048/PI_VALUE)*joint_positions[9])
    rh2_position = int((2048/PI_VALUE)*joint_positions[10])
    rh3_position = int((2048/PI_VALUE)*joint_positions[11])

    scs_goal_position = []
    # lf
    scs_goal_position.append(ZERO_STANCE - lf1_position)
    scs_goal_position.append(ZERO_STANCE - lf2_position)
    scs_goal_position.append(ZERO_STANCE + lf3_position + lf2_position)
    # rf
    scs_goal_position.append(ZERO_STANCE - rf1_position)
    scs_goal_position.append(ZERO_STANCE + rf2_position)
    scs_goal_position.append(ZERO_STANCE - rf3_position - rf2_position)
    # lh
    scs_goal_position.append(ZERO_STANCE - lh1_position)
    scs_goal_position.append(ZERO_STANCE - lh2_position)
    scs_goal_position.append(ZERO_STANCE + lh3_position + lh2_position)
    # rh
    scs_goal_position.append(ZERO_STANCE - rh1_position)
    scs_goal_position.append(ZERO_STANCE + rh2_position)
    scs_goal_position.append(ZERO_STANCE - rf3_position - rh2_position)
   
    for scs_id in range(1, 13):
        scs_comm_result, scs_error = packetHandler.RegWritePosEx(scs_id, scs_goal_position[scs_id-1], SCS_MOVING_SPEED, SCS_MOVING_ACC)
        if scs_comm_result != scservo_sdk.COMM_SUCCESS:
            print("%s" % packetHandler.getTxRxResult(scs_comm_result))
        if scs_error != 0:
            print("%s" % packetHandler.getRxPacketError(scs_error))
        packetHandler.RegAction()
    

     
    

if __name__=='__main__':
    rospy.init_node('servo_interface',anonymous=True)
    rospy.Subscriber("/joint_group_position_controller/command",JointTrajectory,callback,queue_size=1)
    rospy.spin()

