#!/usr/bin/python
 
import cgi
import cgitb; cgitb.enable()  # for troubleshooting

#import the USB and Time librarys into Python
import usb.core, usb.util, time

#Allocate the name 'RoboArm' to the USB device
RoboArm = usb.core.find(idVendor=0x1267, idProduct=0x000)


print "Content-type: text/html"
print


#value = form.getlist("username")
#usernames = ",".join(value)

#ROBOT ARM CONTROL PROGRAM
#Check if the arm is detected and warn if not
if RoboArm is None:
    raise ValueError("Arm not found")
#Create a variable for duration
Duration=1
#Define a procedure to execute each movement
def MoveArm(Duration, ArmCmd): #After this, all code until the demo commands must be indented
    #Start the movement
    RoboArm.ctrl_transfer(0x40,6,0x100,0,ArmCmd,1000)
    #Stop the movement after waiting a specified duration
    time.sleep(Duration)
    ArmCmd=[0,0,0]
    RoboArm.ctrl_transfer(0x40,6,0x100,0,ArmCmd,1000)

#MoveArm(1,[0,1,0]) #Rotate base anti-clockwise
#MoveArm(1,[0,2,0]) #Rotate base clockwise
#MoveArm(1,[64,0,0]) #Shoulder up
#MoveArm(1,[128,0,0]) #Shoulder down
#MoveArm(1,[16,0,0]) #Elbow up
#MoveArm(1,[32,0,0]) #Elbow down
#MoveArm(1,[4,0,0]) #Wrist up
#MoveArm(1,[8,0,0]) # Wrist down
#MoveArm(1,[2,0,0]) #Grip open
#MoveArm(1,[1,0,0]) #Grip close
#MoveArm(1,[0,0,1]) #Light on
#MoveArm(1,[0,0,0]) #Light off

# Create instance of FieldStorage 
form = cgi.FieldStorage() 



movemap = {
   'base-anti-clockwise' : [0,1,0],
   'base-clockwise' : [0,2,0],
   'shoulder-up': [64,0,0],
   'shoulder-down': [128,0,0],
   'elbow-up': [16,0,0],
   'elbow-down': [32,0,0],
   'wrist-up': [4,0,0],
   'wrist-down': [8,0,0],
   'grip-open': [2,0,0],
   'grip-close': [1,0,0],
   'light-on': [0,0,1],
   'light-off': [0,0,0],
   'stop': [0,0,0]
}


# Get data from fields
if form.getvalue('move') in movemap:
   mm=movemap[form.getvalue('move')]
   MoveArm(1,mm) 
   subject = "Moving %s" % form.getvalue('move')

else:
   subject = "Nothing yet"


print "<img src='usb-robot-arm.png' width='1029' height='604' border='0' usemap='#map' />"

print "<map name='map'>"
print "<!-- #$-:GIMP Image Map plug-in by Maurits Rijk -->"
print "<!-- #$-:Please do not edit lines starting with "#$" -->"
print "<!-- #$VERSION:2.3 -->"
print "<!-- #$AUTHOR:Liz Quilty -->"
print "<area shape='poly' coords='68,141,119,118,289,311,230,330,71,142,72,142' href='/control.py?move=grip-open' />"
print "<area shape='poly' coords='63,230,105,199,227,335,162,349,69,232' href='/control.py?move=grip-close' />"
print "<area shape='poly' coords='610,63,500,143,453,60,599,22' href='/control.py?move=wrist-up' />"
print "<area shape='poly' coords='610,72,498,153,528,194,617,132,633,79,618,73' href='/control.py?move=wrist-down' />"
print "<area shape='poly' coords='741,88,623,167,612,144,644,65,715,51' href='/control.py?move=elbow-up' />"
print "<area shape='poly' coords='621,176,740,94,773,151,721,195,666,219' href='/control.py?move=elbow-down' />"
print "<area shape='poly' coords='625,311,475,411,450,338,513,282,606,249' href='/control.py?move=shoulder-up' />"
print "<area shape='poly' coords='629,320,477,416,510,454,606,443,655,369' href='/control.py?move=shoulder-down' />"
print "<area shape='poly' coords='627,441,662,476,547,539,428,532,378,470,420,423,484,456,544,455,627,442' href='/control.py?move=base-clockwise' />"
print "<area shape='poly' coords='455,318,444,358,417,415,372,455,323,436,347,362,401,300' href='/control.py?move=base-anti-clockwise' />"
print "<area shape='rect' coords='205,121,301,194' href='/control.py?move=light-on' />"
print "</map>"


#print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title>OWI/Maplin Robotic Arm</title>"
print "</head>"
print "<body>"
print "<h2> Moving  %s</h2>" % subject

print "</body>"
print "</html>"



