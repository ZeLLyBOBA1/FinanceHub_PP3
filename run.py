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

username_cell = None
pincode_cell = None
balance_cell = None

username = None
pincode = None
balance = None

#clears console
def console_clear():
    os.system('cls')
    os.system('clear')


#prints logo
def print_logo():
    print(bank_logo.logo)


#loads login page
def load_login_page():
    global username
    global pincode
    global balance

    global username_cell
    global pincode_cell
    global balance_cell

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
            username_cell = userdata.cell(userdata.find(username).row, userdata.find(username).col)
            pincode_cell = userdata.cell(userdata.find(username).row, userdata.find(username).col + 1)
            balance_cell = userdata.cell(userdata.find(username).row, userdata.find(username).col + 2)
            balance = balance_cell.value

            print("\n-- YOU ARE LOGED IN --")
            sleep(2)
            load_main_page()

        else:

            print("-- WRONG USERNAME OR PIN --")
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
    global username
    global pincode
    
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
                balance = 0
                print(f"\nYour pin is ==> {pincode}")
                userdata.append_row([username, pincode , balance])
                print("\nMake sure to write it down and press 'Enter'")
                input()

                sleep(2)
                load_main_page()
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

def load_main_page():
    global username
    global pincode
    global balance

    global username_cell
    global pincode_cell
    global balance_cell

    console_clear()
    print_logo()

    print(f"Welcome, {username}!")
    print(f"\n=============================== \nYour balance is {balance}$ \n=============================== \n")
    print("Choose an option below:\n")
    print("(1) Deposit money    (3) Withdraw money")
    print("(2) Change my pin    (4) Delete my account")
    print("            (0) Log out")

    choosenoption = input("\n>> ")

    if(choosenoption == "0"):
        username = None
        pincode = None
        load_entry_page()

    elif(choosenoption == "1"):
        load_deposit_page()

    elif(choosenoption == "2"):
        load_pin_change_page()

    elif(choosenoption == "3"):
        load_withdrawal_page()

    elif(choosenoption == "4"):
        load_delete_page()
    
    elif(choosenoption == "404"):
        print(f"username_cell = {username_cell}")
        print(f"pincode_cell = {pincode_cell}")
        print(f"balance_cell = {balance_cell}")
        print(f"username = {username}")
        print(f"pincode = {pincode}")
        print(f"balance = {balance}")

    else:
        print("\n-- OPTION OUT OF RANGE --")
        sleep(2)
        load_main_page()

def load_deposit_page():
    global balance
    
    console_clear()
    print_logo()

    print("\nHow much would you like to deposit?")
    deposit_amount = input("\n>> ")

    console_clear()
    print_logo()
    print("\n -- PROCESSING OPERATION -- ")
    sleep(2)

    if(balance + abs(int(deposit_amount)) <= 100000000000):
        print("\n -- SUCCESS -- ")
        sleep(2)
        load_main_page()

    else:
        print("\n -- You cant keep more than 100 billions on your balance --")
        print("\nChoose your option below:")
        print("\n(1) to try again \n\n - or - \n\n(0) to visit main page")
        choosenoption = input("\n>> ")
        
        if(choosenoption == "1"):
            load_deposit_page()
        
        elif(choosenoption == "0"):
            load_main_page()

        else:
            print("\n-- OPTION OUT OF RANGE --")

def load_withdrawal_page():

    console_clear()
    print_logo()

def load_pin_change_page():

    console_clear()
    print_logo()

def load_delete_page():

    console_clear()
    print_logo()

# SHEET.worksheet('userdata').append_row(['demon228', '6366'])
# found = SHEET.worksheet('userdata').find('huesosik')
# print(found)
# print(SHEET.worksheet('userdata').get_all_values())

load_entry_page()
