#!/usr/bin/python3
import   cgi,subprocess,os
import  cgitb
import time
cgitb.enable()

print("Content-type:text/html")
print("")

#  get  html page code and data
web=cgi.FieldStorage()
pip=web.getvalue('ip')
ip=str(web.getvalue('ip'))+","

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database=""
)

mycursor=mydb.cursor()
mycursor.execute("SELECT * FROM register where public_ip='{}' ".format(pip))
myresult = mycursor.fetchall()
publicdns_with_port=str(myresult[0][7]) + ":10000"
hostname=myresult[0][7]
privateip=myresult[0][8]
hadoop=myresult[0][9]

if hadoop=='0':
#get the value of first name
	subprocess.getoutput("sudo ansible-playbook /etc/ansible/project_playbooks/hadoop.yml  -i '%s'     --extra-vars 'publicdns=%s hostname=%s private_ip=%s'  &>/dev/null & "%(ip,publicdns_with_port, hostname, privateip))
         # root                       location                              passing Ip    passing variables   hostname:port   hostname     privateip
	sql=("update register set hadoop = 1 where public_ip='{}'".format(pip))
	mycursor.execute(sql)
	mydb.commit()

	print('''
<html>
      <head>
          <meta http-equiv="refresh" content="0;url=http://13.126.219.100/hadoop_wait.html" />
      </head>
    </html>
''')
elif hadoop=='1':
          print('''
<html>
      <head>
          <meta http-equiv="refresh" content="0;url=http://13.126.219.100/dashboard/hadoop.php" />                                                                  </head>
    </html>
''')

