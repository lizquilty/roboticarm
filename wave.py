#!/usr/bin/python
# This is a SLI app that makes the Robot arm 'wave' at you when it detects a person via PIR
# hardware setup at http://learn.adafruit.com/adafruits-raspberry-pi-lesson-12-sensing-movement/hardware
# If/when you need to quit, use ^C and do it when its NOT moving (should you not, motors keep going)

import time
import RPi.GPIO as io
import usb.core, usb.util
import pyttsx
import random
io.setmode(io.BCM)


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

 
pir_pin = 18
#door_pin = 23
 
io.setup(pir_pin, io.IN)         # activate input
#io.setup(door_pin, io.IN, pull_up_down=io.PUD_UP)  # activate input with PullUp
greetings = ['Hello', 'Hi', 'Sup', 'Heya', 'Gidday', 'Yo', 'Aloha', 'Ke ora', 'Howdy', 'Hiya', 'Ni hau']
 
while True:
    if io.input(pir_pin):
        print("PIR ALARM!")
	engine = pyttsx.init()
	from random import choice
	engine.say(choice(greetings))
	engine.runAndWait()
        MoveArm(1,[4,0,0]) #Wrist up
        MoveArm(1,[8,0,0]) #Wrist down
#        MoveArm(1,[4,0,0]) #Wrist up
#        MoveArm(1,[8,0,0]) #Wrist down
#        MoveArm(1,[4,0,0]) #Wrist up
#        MoveArm(1,[8,0,0]) #Wrist down
#    if io.input(door_pin):
#        print("DOOR ALARM!")
#    time.sleep(0.5)
