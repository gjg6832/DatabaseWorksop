from DatabaseWorkshop.database import personDB
from DatabaseWorkshop.database import toolDB
from DatabaseWorkshop.database import requestDB
import random
from datetime import date
from datetime import datetime

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
    creationtime = datetime.now().time()
    personDB.insertPerson(username, password, first_name, last_name, email, creationdate, creationtime, creationdate, creationtime)
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
    print()
    shareable = False
    requested = False
    toolDB.insertTool(barcode, name, description,  categories, purchasedate, purchaseprice, shareable, requested)



def newRequest():
    print()
    id = random.randint(1000,1999)
    userrequesting = input("Enter Your Username: ")
    password = input("Enter Your Password: ")
    actual = personDB.getPassword(userrequesting)
    if actual == password:
        print("You have been signed in")
        personDB.editDateAndTime(userrequesting)
    else:
        print("incorrect password or username")
        print("")
        return
    barcode = input("Enter barcode of the tool: ")
    tool = toolDB.getTool(barcode)
    if tool[6] == "false":
        print("Tool is not Available")
        return
    if tool[8] == None:
        print("This tool does not have a owner")
        print("Cant make a request")
        print()
        return
    today = input("Enter the date you want the tool FORMAT year-month-day: ")
    duration = input("Enter duration wanted: ")
    status = "Pending"
    returndate = None
    requestDB.insertRequest(id, userrequesting, tool[1], tool[8], today, duration, status, returndate)
    toolDB.editToolRequested(True,barcode)
    print("Request has been made")
    print()

