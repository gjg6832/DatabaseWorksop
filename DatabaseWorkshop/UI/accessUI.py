"""
File: accessUI
Author: Greg Godlewski
"""
from DatabaseWorkshop.database import personDB
from DatabaseWorkshop.database import toolDB
from DatabaseWorkshop.database import requestDB


def access():
    print()
    print("Access action Menu")
    print("---------------------------")
    print("-c: Access catalog of tools ")
    print("-r: Access requests")
    print()
    newAction = input("Enter new action: ")
    if newAction == "-c":
        catalogTool()
    elif newAction == "-r":
        catalogRequest()
    else:
        print(newAction,"Invalid action. Redirected to Main Page")



def catalogTool():
    print()
    username = input("Enter Your Username: ")
    password = input("Enter Your Password: ")
    actual = personDB.getPassword(username)
    if actual == password:
        print("You have been signed in")
        personDB.editDateAndTime(username)
    else:
        print("incorrect password or username")
        print("")
        return
    print()
    print("Tool Catalog Menu")
    print("---------------------------")
    print("-a: Add")
    print("-e: Edit")
    print("-d: Delete")
    print("-v: View")
    print()
    newAction = input("Enter new action: ")
    if newAction == "-a":
        print()
        barcode = input("Enter barcode of tool wanted to add: ")
        tool = toolDB.getTool(barcode)
        if tool[8] != None:
            print("Tool is already owned can not add")
            print()
        else:
            toolDB.addToolOwner(username, barcode)
            print()
    elif newAction == "-v":
        print()
        print("List of Tools you own")
        toolDB.printToolOwner(username)
    elif newAction == "-d":
        print()
        barcode = input("Enter barcode of tool wanted to delete: ")
        tool = toolDB.getTool(barcode)
        if tool[8] == username:
            toolDB.deleteToolOwner(barcode)
            print("Tool has been deleted from your Catalog")
            print()
        else:
            print("This tool is not in your catalog. You can not delete")
            print()
    elif newAction == "-e":
        print()
        barcode = input("Enter Barcode of the tool wanted to edit: ")
        tool = toolDB.getTool(barcode)
        print(tool)
        print()

        if tool[8] != username:
            print("You do not own this tool")
            print()
            return
        else:
            name = input("Enter new Name (leave blank if no edit wanted): ")
            print()
            if name == "":
                print("Name was not changed")
                print()
            else:
                toolDB.editToolName(name, barcode)
                print("Name has been changed to " + name)
                print()

            descrip = input("Enter new Description (leave blank if no edit wanted): ")
            print()
            if descrip == "":
                print("Decription was not changed")
                print()
            else:
                toolDB.editToolDescrip(descrip, barcode)
                print("Description was changed to " + descrip)
                print()

            categorie = input("Enter new categorie: (leave blank if no edit wanted): ")
            print()
            if categorie == "":
                print("Categoie was not changed")
                print()
            else:
                toolDB.editToolCategorie(categorie,barcode)
                print("Categorie was edited to: " + categorie)


def catalogRequest():
    print()
    username = input("Enter Your Username: ")
    password = input("Enter Your Password: ")
    actual = personDB.getPassword(username)
    if actual == password:
        print("You have been signed in")
        personDB.editDateAndTime(username)
    else:
        print("incorrect password or username")
        print("")
        return
    print()
    print("Request Catalog Menu")
    print("---------------------------")
    print("-r: Return")
    print("-v: View My Requests")
    print("-m: Manage Requests")
    print("-s: Requests of my tools")
    print()
    newAction = input("Enter new action: ")
    if newAction == "-r":
        print()
        id = input("Enter request id to be returned: ")
        request = requestDB.getRequest(id)
        print(request)
        if request[1] == username:
            toolDB.editToolShareable(True, request[2])
            print()
            print("Tool has been returned")
            requestDB.deleteRequest(id)
    elif newAction == "-v":
        print()
        requestDB.printRequesterRequests(username)
        print()
    elif newAction == "-s":
        print()
        requestDB.printRequesterOwner(username)
        print()
    elif newAction == "-m":
        #TODO: When Accepted add expected return date
        print()
        requestDB.printRequesterOwner(username)
        print()
        id = input("Enter id of request you would like to manage: ")
        print()
        request = requestDB.getRequest(id)
        print(request)
        print()
        status = input("Accept or Deny : ")
        if status == "Accept":
            requestDB.updateStatus("Accepted", id)
            print()
            print("Request has been Accepted")
            print()
        elif status == "Deny":
            requestDB.updateStatus("Denied", id)
            print()
            print("Request has been Denied")
            print()
        else:
            print()
            print("Not changed. Input was left empty or mistyped")
            print()















