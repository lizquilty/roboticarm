#!/usr/bin/python

# Unsure who wrote this code, found it on a website and cleaned up the wikihow page 
# at http://www.wikihow.com/Use-a-USB-Robotic-Arm-with-a-Raspberry-Pi-(Maplin)
# - Liz Quilty

#ROBOT ARM CONTROL PROGRAM
#import the USB and Time librarys into Python
import usb.core, usb.util, time
#Allocate the name 'RoboArm' to the USB device
RoboArm = usb.core.find(idVendor=0x1267, idProduct=0x000)
#Check if the arm is detected and warn if not
if RoboArm is None:
    raise ValueError("Arm not found")
#Create a variable for duration
Duration=1
#Define a procedure to execute each movement
def MoveArm(Duration, ArmCmd):
    #Start the movement
    RoboArm.ctrl_transfer(0x40,6,0x100,0,ArmCmd,1000)
    #Stop the movement after waiting a specified duration
    time.sleep(Duration)
    ArmCmd=[0,0,0]
    RoboArm.ctrl_transfer(0x40,6,0x100,0,ArmCmd,1000)


MoveArm(1,[0,1,0]) #Rotate base anti-clockwise
MoveArm(1,[0,2,0]) #Rotate base clockwise
MoveArm(1,[64,0,0]) #Shoulder up
MoveArm(1,[128,0,0]) #Shoulder down
MoveArm(1,[16,0,0]) #Elbow up
MoveArm(1,[32,0,0]) #Elbow down
MoveArm(1,[4,0,0]) #Wrist up
MoveArm(1,[8,0,0]) # Wrist down
MoveArm(1,[2,0,0]) #Grip open
MoveArm(1,[1,0,0]) #Grip close
MoveArm(1,[0,0,1]) #Light on
MoveArm(1,[0,0,0]) #Light off
