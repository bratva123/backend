#!/usr/bin/python
import cgi
import cgitb

cgitb.enable()

print("content-type:text/html")
print("")

data=cgi.FieldStorage()
pa=data.getvalue('gen')

if pa == 'paas':
   redirectURL = "http://192.168.1.109/pass.html"
   print('    <meta http-equiv="refresh" content="0;url='+str(redirectURL)+'" />')

