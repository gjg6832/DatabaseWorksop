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
    idNum = input("Please enter the tool's ID number")
    printTool(idNum)