#!/usr/bin/python
import cgi
import os
import random



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
cmd4=htmlpage.getvalue('oss')
print cmd4
if cmd4 == 'ubuntu' :

	  os.system('sudo virt-install --name '+cmd1+' --ram '+cmd2+' --vcpu '+cmd3+'  --cdrom  /root/Documents/ubuntu.iso  --nodisk  --noautoconsole --graphics vnc,listen=0.0.0.0,port='+x)


          os.system('sudo  websockify --web=/usr/share/novnc'+y+' 192.168.10.251:'+x)

web="http://192.168.10.251:"+y
print "<a href="+web+">"
print "click here to get your os"
print "</a>"
         


