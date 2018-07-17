#!/usr/bin/python
import cgi

import os
import random,cgitb,commands

cgitb.enable()

print "content-type:text/html"
print""

data=cgi.FieldStorage()
pa=data.getvalue('gen')

if pa == 'paas':
   redirectURL = "http://192.168.10.251/pass.html"
   print('    <meta http-equiv="refresh" content="0;url='+str(redirectURL)+'" />')

if pa == 'saas':
   redirectURL = "http://192.168.10.251/saas.html"
   print('    <meta http-equiv="refresh" content="0;url='+str(redirectURL)+'" />')


if pa == 'iaas':
   redirectURL = "http://192.168.10.251/iaas.html"
   print('    <meta http-equiv="refresh" content="0;url='+str(redirectURL)+'" />')

if pa == 'staas':
   redirectURL = "http://192.168.10.251/staas.html"
   print('    <meta http-equiv="refresh" content="0;url='+str(redirectURL)+'" />') 



