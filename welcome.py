import login_and_encryption 

print("Welcome to FinTra λ - A CLI-Based Finance Tracker.")

try:
    user_data_file = open("user_data.txt", 'r')
    username = input("Enter username: ")
    password = getpass("Enter password: ")
    login_and_encryption.login(username, password)
except FileNotFoundError:
    user_data_file = open("user_data.txt", 'w')
    login_and_encryption.signup()