#!/usr/bin/python

import commands,cgi


print "Content-Type:text/html"
print ""
mem='13.66'

print """<html>
<style>
#myProgress {
  width: 20%;
  background-color: #ddd;
}

#myBar {
"""
print "width: "+mem+"%;"
print """
  height: 30px;
  background-color: #4CAF50;
  text-align: center;
  line-height: 30px;
  color: white;
}
</style>
<body>

<h1>used</h1>

<div id="myProgress">
"""
web='<div id="myBar">'
print web+""+mem+"</div>"
print"""
</div>
</body>
</html>"""
