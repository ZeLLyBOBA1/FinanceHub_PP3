import gspread 
from google.oauth2.service_account import Credentials 
import os
import bank_logo
import time
import random


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]


CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('financehub')


userdata = SHEET.worksheet('userdata')
data = userdata.get_all_values()


sleep = time.sleep

username = "username"
pincode = 1111

#clears console
def console_clear():
    os.system('cls')
    os.system('clear')


#prints logo
def print_logo():
    print(bank_logo.logo)


#loads login page
def load_login_page():

    console_clear()
    print_logo()
    
    print("You are on login page")
    print("Choose an option below:\n")
    
    print("(1) Start login process")
    print("(2) Go back")

    choosenoption = input("\n>> ")

    if(choosenoption == "1"):

        console_clear()
        print_logo()
        username = input("Enter your username: ")
        pincode = input("Enter your pin: ")
      
        if(userdata.find(username) != None and pincode == userdata.cell(userdata.find(username).row, userdata.find(username).col + 1).value):

            print("\n-- YOU ARE LOGED IN --")
            sleep(2)

        else:

            print("Wrong username or pin")
            sleep(2) 
            load_login_page()

    elif(choosenoption == "2"):
        load_entry_page()


    else:
        print("\n-- OPTION OUT OF RANGE --")
        sleep(2)
        load_login_page()


#loads signup page
def load_signup_page():
    
    console_clear()
    print_logo()

    print("You are on signup page")
    print("Choose an option below:\n")
    
    print("(1) Start signup process")
    print("(2) Go back")

    choosenoption = input("\n>> ")
    
    if(choosenoption == "1"):

        console_clear()
        print_logo()
        username = input("Create username (4-8): ")
        
        if(len(username) <= 8 and len(username) >= 4):

            if(userdata.find(username) == None):
                # userdata.append_row([username])
                pincode = random.randint(1000,9999)
                print(f"\nYour pin is ==> {pincode}")
                userdata.append_row([username, pincode])
                print("\nMake sure to write it down and press 'Enter'")
                input()
            else:
                print("This username is already in use")
                load_signup_page()
        else:
            print("\n-- WRONG USERNAME LENGTH --")
            sleep(2)
            load_signup_page()
    else:
        print("\n-- OPTION OUT OF RANGE --")
        sleep(2)
        load_signup_page()


#loads entry (login|signup) page
def load_entry_page():

    console_clear()
    print_logo()

    print("Welcome to FinanceHub!")
    print("Choose an option below:\n")
    
    print("(1) Login")
    print("(2) SignUp")

    choosenoption = input("\n>> ")

    if(choosenoption == "1"):
        load_login_page()

    elif(choosenoption == "2"):
        load_signup_page()

    else:
        print("\n-- OPTION OUT OF RANGE --")
        sleep(2)
        load_entry_page()


# SHEET.worksheet('userdata').append_row(['demon228', '6366'])
# found = SHEET.worksheet('userdata').find('huesosik')
# print(found)
# print(SHEET.worksheet('userdata').get_all_values())

load_entry_page()
