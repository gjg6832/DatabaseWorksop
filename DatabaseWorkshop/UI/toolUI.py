"""
File: toolUI
Author: Greg Godlewski
        Saakshi D'Souza
"""
from DatabaseWorkshop.database.toolDB import *
def search():
    """
    search for a tool
    :return:
    """
    print("Search action Menu")
    print("---------------------------")
    print("-a: inspect available tools list")
    print("-l: inspect lent tools list")
    print("-w: inspect borrowed tools list")
    print("-b: search by barcode")
    print("-c: search by category")
    print("-n: search by name")
    print()
    newAction = input("Enter new action: ")
    if newAction == "-b":
        searchBarcode()
    elif newAction == "-c":
        searchCategory()
    elif newAction == "-n":
        searchName()
    elif newAction == "-l":
        printLentTools()
    elif newAction == "-a":
        printAvailableTools()
    elif newAction == "-w":
        printBorrowedTools()


def searchBarcode():
    """
    search for a tool by id num
    :return:
    """
    idNum = input("Please enter the tool's ID number: ")
    printToolBarcode(idNum)

def searchCategory():
    """
    search for a tool by category
    :return:
    """
    categ = input("Please enter the tool's category: ")
    printToolCategory(categ)


def searchName():
    """
    search for a tool by name
    :return:
    """
    tName = input("Please enter the tool's name: ")
    printToolName(tName)

