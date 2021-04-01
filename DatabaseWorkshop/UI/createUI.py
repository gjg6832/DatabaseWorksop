from DatabaseWorkshop.database import personDB
from DatabaseWorkshop.database import toolDB
from DatabaseWorkshop.database import requestDB
import random
from datetime import date

def create():
    """
    Create Menu
    :return:
    """
    print()
    print("Create action Menu")
    print("---------------------------")
    print("-u: create a new user")
    print("-t: create a new tool")
    print("-r: create a new request")
    print()
    newAction = input("Enter new action: ")
    if newAction == "-u":
        newUser()
    elif newAction == "-t":
        newTool()
    elif newAction == "-r":
        newRequest()


def newUser():
    """
    Creates a new user to the database
    :return: NONE
    """
    print()
    username = input("Enter a username for your account: ")
    password = input("Enter a password for your account: ")
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    email = input("Enter your email: ")
    creationdate = date.today()
    laccessdate = date.today()
    personDB.insertPerson(username, password, first_name, last_name, email, creationdate, laccessdate)
    print("Account has been created")
    print()

def newTool():
    """
    Creates a new tool to the database
    :return:
    """
    print()
    barcode = random.randint(900000,999999)
    name = input("Enter Tool Name: ")
    description = input("Enter description (if wanted): ")
    categories = input("Enter Categories : ")
    purchasedate = date.today()
    purchaseprice = input("Enter the purchase price: ")
    shareable_input = input("Shareable: True (1) or False (0): ")
    print()
    if shareable_input == '1':
        shareable = True
    elif shareable_input == '0':
        shareable = False
    else:
        shareable = None
    requested = False
    toolDB.insertTool(barcode, name, description,  categories, purchasedate, purchaseprice, shareable, requested)


def newRequest():
    print()
    id = random.randint(1000,1999)
    userrequesting = input("Enter username: ")
    inputPassword = input("Enter password: ")
    password = personDB.getPassword(userrequesting)
    barcode = input("Enter barcode of the tool: ")
    tool = toolDB.getTool(barcode)
    if tool[8] == None:
        print("This tool does not have a owner")
        print("Cant make a request")
        print()
        return
    today = date.today()
    duration = input("Enter duration wanted: ")
    status = "Pending"
    requestDB.insertRequest(id, userrequesting, tool[1], tool[8], today, duration, status)
    print("Request has been made")
    print()
