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


username_id = SHEET.worksheet('userdata')
data = username_id.get_all_values()


sleep = time.sleep



#clears console
def console_clear():
    os.system('cls')
    os.system('clear')


#prints logo
def print_logo():
    print(bank_logo.logo)


#loads login page
def load_login_page(turn_on_sleep):

    console_clear()
    print_logo()
    sleep(1 * turn_on_sleep)

    print("You are on login page")
    sleep(.5 * turn_on_sleep)
    print("Choose an option below:\n")
    sleep(1 * turn_on_sleep)

    print("(1) - Start login process")
    sleep(.25 * turn_on_sleep)
    print("(2) - Go back")
    sleep(.25 * turn_on_sleep)

    choosenoption = input("\n>> ")

    if(choosenoption == "1"):
        username = input("Enter your username: ")
        pincode = input("Enter your pin: ")

    elif(choosenoption == "2"):
        load_entry_page(1)

    else:
        print("\n-- OPTION OUT OF RANGE --")
        sleep(2 * turn_on_sleep)
        load_login_page(0)


#loads signup page
def load_signup_page(turn_on_sleep):

    console_clear()
    print_logo()
    sleep(1 * turn_on_sleep)

    print("You are on signup page")
    sleep(.5 * turn_on_sleep)
    print("Choose an option below:\n")
    sleep(1 * turn_on_sleep)

    print("(1) - Start signup process")
    sleep(.25 * turn_on_sleep)
    print("(2) - Go back")
    sleep(.25 * turn_on_sleep)

    choosenoption = input("\n>> ")

    if(choosenoption == "1"):
        username = input("Create username (8): ")
        sleep(.5 * turn_on_sleep)
        print("Your pin is...")
        sleep(1 * turn_on_sleep)
        print("5125")
        sleep(.25 * turn_on_sleep)
        print("Make sure to write it down")
        sleep(10)

    elif(choosenoption == "2"):
        load_entry_page(1)

    else:
        print("\n-- OPTION OUT OF RANGE --")
        sleep(2)
        load_signup_page(0)


#loads entry (login|signup) page
def load_entry_page(turn_on_sleep):

    console_clear()
    print_logo()
    sleep(1 * turn_on_sleep)

    print("Welcome to FinanceHub!")
    time.sleep(.5 * turn_on_sleep)
    print("Choose an option below:\n")
    sleep(1 * turn_on_sleep)

    print("(1) - Login")
    sleep(.25 * turn_on_sleep)
    print("(2) - SignUp")
    sleep(.25 * turn_on_sleep)

    choosenoption = input("\n>> ")

    if(choosenoption == "1"):
        load_login_page(1)

    elif(choosenoption == "2"):
        load_signup_page(1)

    else:
        print("\n-- OPTION OUT OF RANGE --")
        sleep(2)
        load_entry_page(0)


# SHEET.worksheet('userdata').append_row(['demon228', '6366'])
found = SHEET.worksheet('userdata').find('huesosik')
print(found)
print(SHEET.worksheet('userdata').get_all_values())

#
