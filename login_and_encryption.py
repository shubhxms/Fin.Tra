import getpass

def signup():
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
    credentials = [username,password]
    user_data_file.writelines(credentials)


def login(username, password):
    user_data_file = open("user_data.txt", 'r')
    if username == user_data_file.readline():
        print("==========AUTHORISING==========")
        if password == user_data_file.readline():
            print("==========ACCESS GRANTED==========")