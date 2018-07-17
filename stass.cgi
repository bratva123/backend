#!/usr/bin/python2
import os,commands,random
import cgi

print "Content-Type:text/html"
print ""
 
htmlpage=cgi.FieldStorage()

storage_name=htmlpage.getvalue('a')
size=htmlpage.getvalue('b')


commands.getoutput("lvcreate --name "+storage_name+"--size "+size+"chandan")
commands.getoutput("mkfs.xfs /dev/chandan/storage_name")
commands.getoutput("mkdir /media/go")
commands.getoutput("mount /dev/chandan/"+storage_name+" /media/go")
file=open('/etc/fstab','a')
file.write('/dev/chandan/'+storage_name+'  /media/go   xfs  defaults  0 0')
f.close()
commands.getoutput("mkdir /media/go/"+storage_name)
file=open('/etc/exports','a')
file.write('/media/go/'+storage_name+'  192.168.122.82(rw,no_root_squash)')
f.close()
commands.getouput("systemctl restart nfs-server")
commands.getoutput("exportfs -r")
print "write this on your terminal \n"
print "make sure u have started nfs-services \t now write \n"
print "showmount -e 192.168.10.72\n"
print "make dir like mkdir /media/go\n"
print "mount 192.168.10.72:/media/go/"+storage_name+" /media/go  (dir which u made)\n"
print "for permanent storage go to /var/etc/fstab and write ->192.168.10.72:/media/go/"+storage_name+" /media/go nfs defaults 0 0"


