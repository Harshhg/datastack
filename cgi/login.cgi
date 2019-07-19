#!/usr/bin/python3
import cgi
import subprocess
import cgitb
import webbrowser
# To show common errors in webbrowser
cgitb.enable()   # CGI Traceback... display errors in browser..
print("Content-type:text/html")
print("")


webdata=cgi.FieldStorage()  
username=webdata.getvalue("username")
password=webdata.getvalue("password")

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database=""
)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM register where username='{}' and password='{}'".format(username,password))
myresult = mycursor.fetchall()

if len(myresult)>0:
	uname=myresult[0][0]
	email=myresult[0][1]
	pip=myresult[0][6]

	print('''

<html>
      <head>
	<form method="post">   
       <meta http-equiv="refresh" content="0;url=http://13.126.219.100/check.php?name=%s&ip=%s&email=%s" />
	</form>
      </head>
    </html>

'''%(uname,pip,email))
else:
	print('''
<html>
      <head>
          <meta http-equiv="refresh" content="0;url=http://13.126.219.100" />
      </head>
    </html>
''')
	print("Invalid Credentials")
