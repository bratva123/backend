#!/usr/bin/python
import mysql.connector as my
import cgi
import os
import random,cgitb,commands

cgitb.enable()

print "content-type:text/html"
print""

def search(x,y,z):
	for i in range(len(x)) :
		for j in range(2):
			if x[i][j]==y and x[i][j+1]==z : 
				return 1


data=cgi.FieldStorage()
pa3=data.getvalue('uname')
pa1=data.getvalue('psw')
conn=my.connect(user='root',password='redhat',host='192.168.1.108',database='nishi')
q=conn.cursor()
query=("select  username,password from student;")
q.execute(query)
oput=q.fetchall()
if search(oput,pa3,pa1)==1:
				web="http://192.168.1.108/service.html"
				print "<a href="+web+">"
              			print "CLICK HERE"
				print "</a>"
				print "to select service"
else:
				print "username or password not matched"		

