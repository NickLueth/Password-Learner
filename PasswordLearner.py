#!/bin/python3
# Password Learning Tool
# Created by: Nick Lueth
# Last edited: 2/29/2020

from os import system, name

from time import sleep

# This function assigns the password to learn through user input
def get_password():
    clear()
    passwd = input("Password to learn: ").strip()
    return passwd

# This function clears the console
def clear():
    if name == 'nt':
        _ = system("cls")
    else:
        _ = system("clear")

# This function starts an user attempt
def user_attempt(passwd):
    clear()
    print("You'll have 10 seconds to remember your password:\n" + passwd)
    sleep(10)
    clear()
    attempt = input("Password: ").strip()
    if attempt == passwd:
        print("Well done!")
    else:
        print("Oh no!\n")
        print("The password was: " + passwd)
        print("You typed: " + attempt)
    input("Press enter to continue...")
    repeat()

# This function prompts the user whether they want to try again or not
def repeat():
    while True:
        clear()
        response = input("Would you like to try again?[y/n]: ").strip().lower()
        if response == 'y':
            user_attempt(password)
        elif response == 'n':
            exit(0)
        else:
            print("Not a valid input, try again...")
            sleep(2)

# Initial function calls
password = get_password()
user_attempt(password)

