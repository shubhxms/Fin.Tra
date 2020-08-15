import login_and_encryption
import fintra
import getpass

print("Welcome to FinTra λ - A CLI-Based Finance Tracker.")

try:
    user_data_file = open("user_data.txt", 'r')
    fintra.login()
except FileNotFoundError:
    user_data_file = open("user_data.txt", 'w')
    login_and_encryption.signup()