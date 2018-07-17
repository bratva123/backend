#!/usr/bin/python
import smtplib,random,cgi


x=random.random()
str(x)
x=str(x)[-4:]


hostname = "smtp.gmail.com" 				## Mail server Hostname 
port = 587 						### port number of Mail server
server = smtplib.SMTP(hostname,port )
server.ehlo() 						### hello to mail server 
server.starttls() 					### start TLS session with Gmail
server.ehlo() 						## send Hello again to server on TLS
server.login("nishikantsingh144@gmail.com","bratvabhoodhello") 	# mail id and password 
from_mail_addr = "nishikantsingh144@gmail.com" 
to_mail_addr = "lavkr0403@gmail.com"
msg = " your otp is" +x
server.sendmail( from_mail_addr,to_mail_addr, msg) 	# from addr | to addr | ttext 
print"""
	<p><b>username</b></p>
      	<input type="text" placeholder="enter otp " name="otp" required>
"""
print "content-type:text/html"
print""


data=cgi.FieldStorage()
otp=data.getvalue('otp')

if x=otp:
	printf"""
	<a href="">
	<p>go to your drive</p>	
	</a>


