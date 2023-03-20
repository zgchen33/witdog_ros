#!/usr/bin/env python
#
# *********     Gen Write Example      *********
#
#
# Available SCServo model on this example : All models using Protocol SCS
# This example is tested with a SCServo(STS/SMS), and an URT
#

import sys
import os
import rospy
port = rospy.get_param("port")


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


import scservo_sdk        # Uses SCServo SDK library

# Default setting
BAUDRATE                    = 1000000           # SCServo default baudrate : 1000000
DEVICENAME                  = port    # Check which port is being used on your controller
                                                # ex) Windows: "COM1"   Linux: "/dev/ttyUSB0" Mac: "/dev/tty.usbserial-*"
SCS_MOVING_SPEED            = 1200        # SCServo moving speed
SCS_MOVING_ACC              = 50          # SCServo moving acc
ZERO_STANCE                 = 2048
RIGHT_ANGLE                 = 1024
scs_goal_position = [ZERO_STANCE, ZERO_STANCE - 1/2 * RIGHT_ANGLE, ZERO_STANCE - RIGHT_ANGLE,\
                    ZERO_STANCE, ZERO_STANCE + 1/2 * RIGHT_ANGLE, ZERO_STANCE + RIGHT_ANGLE,\
                    ZERO_STANCE, ZERO_STANCE - 1/2 * RIGHT_ANGLE, ZERO_STANCE - RIGHT_ANGLE,\
                    ZERO_STANCE, ZERO_STANCE + 1/2 * RIGHT_ANGLE, ZERO_STANCE + RIGHT_ANGLE]         # Goal position

# Initialize PortHandler instance
# Set the port path
# Get methods and members of PortHandlerLinux or PortHandlerWindows
portHandler = scservo_sdk.PortHandler(DEVICENAME)

# Initialize PacketHandler instance
# Get methods and members of Protocol
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




# Write SCServo goal position/moving speed/moving acc
for scs_id in range(1, 13):
    scs_comm_result, scs_error = packetHandler.RegWritePosEx(scs_id, scs_goal_position[scs_id-1], SCS_MOVING_SPEED, SCS_MOVING_ACC)
    if scs_comm_result != scservo_sdk.COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(scs_comm_result))
    if scs_error != 0:
        print("%s" % packetHandler.getRxPacketError(scs_error))
packetHandler.RegAction()

# Close port
portHandler.closePort()
