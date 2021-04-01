"""
File: toolUI
Author: Greg Godlewski
"""
from DatabaseWorkshop.database.toolDB import *
def search():
    """
    search for a tool
    :return:
    """
    print("Search action Menu")
    print("---------------------------")
    print("-b: search by barcode")
    print("-c: search by category")
    print("-n: search by name")
    newAction = input("Enter new action: ")
    if newAction == "-b":
        searchBarcode()
    elif newAction == "-c":
        searchCategory()
    elif newAction == "-n":
        searchName()


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
    #printToolCategory(categ)
    pass

def searchName():
    """
    search for a tool by name
    :return:
    """
    tName = input("Please enter the tool's name: ")
    printToolName(tName)
