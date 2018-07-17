#!/usr/bin/python
import cgi,cgitb 

cgitb.enable()

print("content-type:text/html")
print("")

htmlpage=cgi.FieldStorage()
pa=htmlpage.getvalue('genn')
print("hello world")
print(pa)
