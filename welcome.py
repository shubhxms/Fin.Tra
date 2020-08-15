import getpass as gp
import os
def welcome():
    print("Welcome to FinTra λ\nOne-Stop CLI-Based Finance-Tracker")

login_token = ""
 def login():   
    try:
        pwd_file = open("pwd.txt",'r')
        pwd = gp.getpass("Enter password: ")
        if pwd == pwd_file.read():
            global login_token = "Success"
        else:
            print("Error. Please start the program again.")
            os.exit()
    except:
        print("Please set a password.[Not changeable.]")
        pwd_file = open("pwd.txt", 'w')
        pwd = input("Enter password: ")
