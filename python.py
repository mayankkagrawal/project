#!/usr/bin/python36

import os
import signal
import getpass

os.system("tput setaf 1")
print("\t\twelcome to my tools ")
os.system("tput setaf 3")
print("\t\t----------------")
apassword= "redhat"
password=getpass.getpass("Enter your password")
if apassword != password:
	print("You are not a authorize person")
	exit()

print("""
Press 1: to configure hadoop namenode
Press 2: to configure hadoop datanode
Press 3: to configure hadoop jobnode
Press 4: to configure hadoop tasknode
Press 5: to configure docker in own system
Press 6: to configure httpd and haproxy server
Press 7: to make a partition and format it with ext4
Press 8: create two user with same group and encrypted with sha512 and secured with ansible vault
""")
def lw(x,y):
	os.system("tput setaf 1")
	print("\n\t\t script is forcefully closed")
	os.system("tput setaf 5")
	exit()
signal.signal(2,lw)
ch=int(input("Enter your choice"))

os.system("tput setaf 6")
if ch==1:
	os.system("ansible-playbook namenode_hadoop.yml")
elif ch==2:
	os.system("ansible-playbook datanode_hadoop.yml")
elif ch==3:
	os.system("ansible-playbook job_hadoop.yml")
elif ch==4:
	os.system("ansible-playbook task_hadoop.yml")
elif ch==5:
	os.system("ansible-playbook docker.yml")
elif ch==6:
	os.system("ansible-playbook site.yml")
elif ch==7:
	os.system("ansible-playbook partition.yml")
elif ch==8:
	os.system("ansible-playbook --vault-password-file=/root/.secret.txt user.yml")
else:
	print("please select the number between 1-8")

