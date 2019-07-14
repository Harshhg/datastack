#!/usr/bin/python3
import   cgi,subprocess,os
import  cgitb
import time
cgitb.enable()

print("Content-type:text/html")
print("")

#  get  html page code and data
web=cgi.FieldStorage()
ip=str(web.getvalue('ip'))+","
#get the value of first name	
os.system("sudo ansible-playbook /etc/ansible/project_playbooks/terminal.yml -i '%s'  &>/dev/null &"%ip)
time.sleep(5)
print('''

<html>
      <head>
        <form method="post">
       <meta http-equiv="refresh" content="0;url=http://13.126.219.100/dashboard/terminal.php" />
        </form>
      </head>
    </html>

''')
