#!/usr/bin/python

import commands,cgi

print "content-type:text/html"
print""


data=cgi.FieldStorage()
dire=data.getvalue('directory')

commands.getoutput('sudo mkdir /var/www/cgi-bin/upload/'+dire)
commands.getoutput('sudo chmod 777 /var/www/cgi-bin/upload/'+dire)
print """
<a href="http://192.168.1.108/service_storage.html"> GO TO DRIVE PAGE </a>
"""
