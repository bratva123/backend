#!/usr/bin/python
import cgi
import os
import random

cgitb.enable()

print "content-type:text/html"
print""

x=random.random()
str(x)
x=str(x)[-5:]
y=random.random()
str(y)
y=str(y)[-5:]
print x
print y

htmlpage=cgi.FieldStorage()
cmd1=htmlpage.getvalue('osn')
cmd2=htmlpage.getvalue('osr')
cmd3=htmlpage.getvalue('osc')
print cmd1
if cmd1=='fedora' :

	  os.system('sudo virt-install --name '+cmd1+' --ram '+cmd2+' --vcpu '+cmd3+'  --cdrom  /mnt/images/ubuntu.iso  --nodisk  --noautoconsole --graphics vnc,listen=0.0.0.0,port='+x)

          os.system('sudo  websockify --web=/usr/share/novnc 6089 192.168.10.251:'+x)
 
