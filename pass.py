#!/usr/bin/python
import cgi,cgitb
import os

cgitb.enable()

print "content-type:text/html"
print ""

data=cgi.FieldStorage()
pa=data.getvalue('liv')

if liv == 'python'
	bport=random.random()
	fport=str(bport)[-5:]
	x=commands.getoutput('sudo docker run -itd  -p '+fport+':4200  centos7)
	web="http://192.168.10.251:"+fport
        print "<a href="+web+">"
	print "get python"
   	print "</a>"	

