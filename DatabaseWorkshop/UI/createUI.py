from DatabaseWorkshop.database import personDB
from DatabaseWorkshop.database import toolDB
import random

def create():
    """
    Create Menu
    :return:
    """
    print("Create action Menu")
    print("---------------------------")
    print("-u: create a new user")
    print("-t: create a new tool")
    print("-r: create a new request")
    newAction = input("Enter new action: ")
    if newAction == "-u":
        newUser()
    elif newAction == "-t":
        newTool()


def newUser():
    """
    Creates a new user to the database
    :return: NONE
    """
    username = input("Enter a username for your account: ")
    password = input("Enter a password for your account: ")
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    email = input("Enter your email: ")
    personDB.insertPerson(username, password, first_name, last_name, email)
    print("Account has been created")
    print()

def newTool():
    """
    Creates a new tool to the database
    :return:
    """
    barcode = random.randint(900000,999999)
    name = input("Enter Tool Name: ")
    description = input("Enter description (if wanted): ")
    categories = input("Enter Categories : ")
    shareable_input = input("True (1) or False (0): ")
    if shareable_input == '1':
        shareable = True
    elif shareable_input == '0':
        shareable = False
    else:
        shareable = None
    requested = False
    toolDB.insertTool(barcode, name, description, categories, shareable, requested)