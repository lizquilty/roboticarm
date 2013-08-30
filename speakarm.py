#!/usr/bin/python
# -*- coding: utf-8 -*-
# this works when you install espeak (for libs) and the python tts https://pypi.python.org/pypi/pyttsx 

# metadata
' robot arm python control program '
__version__ = ' 0.1 '
__license__ = ' GPL '
__author__ = ' liz quilty '
__email__ = ''
__url__ = 'https://github.com/lizquilty'
__date__ = '30/08/2013'
__prj__ = 'roboarm'
__docformat__ = 'html'


# imports
import cgi
import pyttsx
import cgitb; cgitb.enable()  # for troubleshooting
import usb.core, usb.util, time  # import the USB and Time librarys into Python


# constants
Duration = 1  # Create a variable for duration


#############################ROBOT ARM CONTROL PROGRAM##########################


print("Content-type: text/html")
print('')


#value = form.getlist("username")
#usernames = ",".join(value)

#Allocate the name 'RoboArm' to the USB device
RoboArm = usb.core.find(idVendor=0x1267, idProduct=0x000)

#Check if the arm is detected and warn if not
if RoboArm is None:
    raise ValueError("Arm not found")


#Define a procedure to execute each movement
def MoveArm(Duration, ArmCmd):  # After this, all code until the demo commands must be indented
    ' Function to start the movement '
    RoboArm.ctrl_transfer(0x40, 6, 0x100, 0, ArmCmd, 1000)
    #Stop the movement after waiting a specified duration
    time.sleep(Duration)
    ArmCmd = [0, 0, 0]
    RoboArm.ctrl_transfer(0x40, 6, 0x100, 0, ArmCmd, 1000)

#MoveArm(1, [0, 1, 0]) #Rotate base anti-clockwise
#MoveArm(1, [0, 2, 0]) #Rotate base clockwise
#MoveArm(1, [64, 0, 0]) #Shoulder up
#MoveArm(1, [128, 0, 0]) #Shoulder down
#MoveArm(1, [16, 0, 0]) #Elbow up
#MoveArm(1, [32, 0, 0]) #Elbow down
#MoveArm(1, [4, 0, 0]) #Wrist up
#MoveArm(1, [8, 0, 0]) # Wrist down
#MoveArm(1, [2, 0, 0]) #Grip open
#MoveArm(1, [1, 0, 0]) #Grip close
#MoveArm(1, [0, 0, 1]) #Light on
#MoveArm(1, [0, 0, 0]) #Light off

# Create instance of FieldStorage
form = cgi.FieldStorage()


movemap = {
   'base-anti-clockwise': [0, 1, 0],
   'base-clockwise': [0, 2, 0],
   'shoulder-up': [64, 0, 0],
   'shoulder-down': [128, 0, 0],
   'elbow-up': [16, 0, 0],
   'elbow-down': [32, 0, 0],
   'wrist-up': [4, 0, 0],
   'wrist-down': [8, 0, 0],
   'grip-open': [2, 0, 0],
   'grip-close': [1, 0, 0],
   'light-on': [0, 0, 1],
   'light-off': [0, 0, 0],
   'stop': [0, 0, 0]
}

talkmap = {
   'base-anti-clockwise': 'Base Anti Clockwise',
   'base-clockwise': 'base clockwise',
   'shoulder-up': 'Shoulder Up',
   'shoulder-down': 'Shoulder down',
   'elbow-up': 'Elbow Up',
   'elbow-down': 'Elbow Down',
   'wrist-up': 'Wrist Up',
   'wrist-down': 'Wrist Down',
   'grip-open': 'Grip open',
   'grip-close': 'Grip Close',
   'light-on': 'Light on',
   'light-off': 'Light off',
   'stop': 'Stop, Hammer time'
}

# Get data from fields
if form.getvalue('move') in movemap:
    mm = movemap[form.getvalue('move')]
    tm = talkmap[form.getvalue('move')]
    engine = pyttsx.init()
    engine.say(tm)
    engine.runAndWait()
    MoveArm(1, mm)
    subject = "Moving {}".format(form.getvalue('move'))
else:
    subject = "Nothing yet"


print("<img src='usb-robot-arm.png' width='1029' height='604' border='0' usemap='#map' />")

print("<map name='map'>")
print("<!-- #$-:GIMP Image Map plug-in by Maurits Rijk -->")
print("<!-- #$-:Please do not edit lines starting with #$ ")
print("<!-- #$VERSION:2.3 -->")
print("<!-- #$AUTHOR:Liz Quilty -->")
print("<area shape='poly' coords='68,141,119,118,289,311,230,330,71,142,72,142' href='/speakarm.py?move=grip-open' />")
print("<area shape='poly' coords='63,230,105,199,227,335,162,349,69,232' href='/speakarm.py?move=grip-close' />")
print("<area shape='poly' coords='610,63,500,143,453,60,599,22' href='/speakarm.py?move=wrist-up' />")
print("<area shape='poly' coords='610,72,498,153,528,194,617,132,633,79,618,73' href='/speakarm.py?move=wrist-down' />")
print("<area shape='poly' coords='741,88,623,167,612,144,644,65,715,51' href='/speakarm.py?move=elbow-up' />")
print("<area shape='poly' coords='621,176,740,94,773,151,721,195,666,219' href='/speakarm.py?move=elbow-down' />")
print("<area shape='poly' coords='625,311,475,411,450,338,513,282,606,249' href='/speakarm.py?move=shoulder-up' />")
print("<area shape='poly' coords='629,320,477,416,510,454,606,443,655,369' href='/speakarm.py?move=shoulder-down' />")
print("<area shape='poly' coords='627,441,662,476,547,539,428,532,378,470,420,423,484,456,544,455,627,442' href='/speakarm.py?move=base-clockwise' />")
print("<area shape='poly' coords='455,318,444,358,417,415,372,455,323,436,347,362,401,300' href='/speakarm.py?move=base-anti-clockwise' />")
print("<area shape='rect' coords='205,121,301,194' href='/speakarm.py?move=light-on' />")
print("</map>")


#print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>OWI/Maplin Robotic Arm</title>")
print("</head>")
print("<body>")
print(("<h2> Moving  {}</h2>".format(subject)))

print("</body>")
print("</html>")
