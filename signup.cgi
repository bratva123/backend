#!/usr/bin/python
import mysql.connector as my
import cgi
import os
import random,cgitb,commands


print("content-type:text/html")
print("")


data=cgi.FieldStorage()
pa3=data.getvalue('uname')
pa2=data.getvalue('email')
pa1=data.getvalue('psw')

conn=my.connect(user='root',password='redhat',database='nishi')
q=conn.cursor()
query=("insert  into student (username,email,password) values ('{0}','{1}','{2}');").format(pa3,pa2,pa1)
q.execute(query)
conn.commit()

web="http://192.168.1.109/login.html"
print("successfully registor")
print("</br>")
print("<a href="+web+">")
print("go to login page")
print("</a>")
conn.close()




