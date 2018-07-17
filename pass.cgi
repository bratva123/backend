#!/usr/bin/python
import cgi
import os
import random,cgitb,commands

cgitb.enable()

print "content-type:text/html"
print""

data=cgi.FieldStorage()
pa=data.getvalue('liv')


if pa == 'python':
	bport=random.random()
	fport=str(bport)[-4:]
	x=commands.getoutput('sudo docker run -itd  --rm -p '+fport+':4200 adhoc:paas')     
	web="http://192.168.10.251:"+fport
        print "<a href="+web+">"
	print "get python"
   	print "</a>"	

