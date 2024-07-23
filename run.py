import gspread 
from google.oauth2.service_account import Credentials 
import os
import bank_logo
import time


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('financehub')

username_id = SHEET.worksheet('userdata')
data = username_id.get_all_values()

def type_text(text):
    for char in text:
        print(char, end = "")
        time.sleep(1)
    print("")

#clears console
def console_clear():
    os.system('cls')

#prints logo
def print_logo():
    print(bank_logo.logo)

#loads login page
def load_login_page():

    console_clear()
    print_logo()

    print("You are on login page")
    print("Choose your option below:\n")

    print("(1) - Start login process")
    print("(2) - Go back")

    choosenoption = input("\n>> ")

    if(choosenoption == "1"):
        username = input("Enter your username: ")
        pincode = input("Enter your pin: ")
    elif(choosenoption == "2"):
        load_entry_page()
    else:
        print("You pciked wrong option!")

#loads signup page
def load_signup_page():

    console_clear()
    print_logo()

    print("Please SignUp")

#loads entry (login|signup) page
def load_entry_page():
    console_clear()
    print_logo()
    print("Welcome to FinanceHub!\nChoose your option below:\n")
    print("(1) - Login")
    print("(2) - SignUp")

    choosenoption = input("\n>> ")

    if(choosenoption == "1"):
        load_login_page()
    elif(choosenoption == "2"):
        load_signup_page()
    else:
        print("You picked wrong option!")

print("Hello World")
time.sleep(1)
print("Hello World")
time.sleep(1)
print("Hello World")
time.sleep(1)
print("Hello World")
time.sleep(1)
type_text("Hellooooo")
load_entry_page()

