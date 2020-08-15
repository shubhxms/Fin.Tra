from getpass import getpass

uname = pwd = pwd2 = su = None
def authenticate():
    if pwd == pwd2:
        global su
        file = open('user_data.txt','a')
        a = (str(uname)+'\n')
        b = (str(pwd)+'\n')
        file.write(str(a))
        file.write(str(b))
        su = True
        print("Sign up Successful!\n")

    else:
        print("Password Mismatch detected, please try again.\n")

def signup():
    global uname, pwd, pwd2
    uname = input("Enter your username: ")
    pwd = getpass("Enter your password: ")
    pwd2 = getpass("Confirm password: ")

def run():
    while True:
        signup()
        authenticate()
        if su == True:
            break

""" def signup():
    user_data_file = open("user_data.txt", 'w')
    username = input("Please enter a username\nNOTE: Username and password cannot be changed.\nUsername: ")
    print("==========STORING==========")
    def password():
        password_entry1 = getpass.getpass("Please enter your password: ")
        password_entry2 = getpass.getpass("Please re-enter your password: ")
        if password_entry1 == password_entry2:
            password = password_entry1
        else:
            password_entry1 = password_entry2 = ''
            password()
    password()
    #credentials = [username,password]
    usr = (str(username)+'\n')
    pwd = (str(password)+'\n')
    user_data_file.write(usr)
    user_data_file.write(pwd) """


""" def login(username, password):
    user_data_file = open("user_data.txt", 'r')
    if username == user_data_file.readline():
        print("==========AUTHORISING==========")
        if password == user_data_file.readline():
            print("==========ACCESS GRANTED==========") """
