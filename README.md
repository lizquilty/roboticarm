Python Web based OWI/Maplin Robotic Arm
==========

Buy an OWI or Maplin robotic arm (looks like the one https://github.com/lizquilty/roboticarm/blob/master/usb-robot-arm.png ). Its cheap, around $50USD or so

Purchase the USB kit to connect it to a PC

Find a child to put it together for you, it will keep them amused for hours :)

Get a Raspberry Pi or other Linux based PC to hook up to it (this is debian/ubuntu specific probably)

Set up pyusb
Install the custom pyUSB
pyusb http://sourceforge.net/projects/pyusb
```
 wget "http://downloads.sourceforge.net/project/pyusb/PyUSB%201.0/1.0.0-alpha-3/pyusb-1.0.0a3.zip?r=http%3A%2F%2Fsourceforge.net%2Fprojects%2Fpyusb%2F&ts=1377736820&use_mirror=hivelocity"
 unzip pyusb-1.0.0a3.zip
 cd pyusb
 python setup.py build
 python setup.py install
```


Edit /etc/udev/rules.d/85-robotarm.rules and add
```
SUBSYSTEM=="usb", ATTRS{idVendor}=="1267", ATTRS{idProduct}=="0000", ACTION=="add", GROUP="plugdev", MODE="0666"
````
Add apache user to plugdev group
````
sudo usermod -aG plugdev www-data
````
Configure apache to work with python by adding the following 
```apache
      <Directory /home/pi/web/>
                Options ExecCGI Indexes FollowSymLinks MultiViews
                AllowOverride All
                Order allow,deny
                allow from all
                AddHandler cgi-script .cgi .py
        </Directory>
```
Change the /home/pi/web for whatever your documentroot is. This just happened to be mine :)

Reboot

upload the contents of this directory, and it should work at http://yourip/armtrol.py

