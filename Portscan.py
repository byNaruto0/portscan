#!usr/bin/env python

import os

os.system("apt install nmap")
os.system("apt install figlet")
os.system("clear")
os.system("figlet PORT SCAN BY NARUTO")
print("""
Port Scan Tool BY Naruto

1) Quick Scan
2) Service and Version Information
3) Operating System Information

""")
os.system("figlet SELECT ACTION") 

islemno = input("Enter Your Transaction Number: ")
os.system("figlet Enter Destination Address")
if(islemno=="1"):
          hedefip = input("Enter Destination Address: ")
          os.system("nmap " + hedefip)
elif(islemno=="2"):
          hedefip = input("Enter Destination Address: ")
          os.system("nmap -sS -sC " + hedefip)
elif(islemno=="3"):
          hedefip = input("Enter Destination Address: ")
          os.system("nmap -0 " + hedefip)
else:
       print("YOU MADE A WRONG CHOICE :(")
