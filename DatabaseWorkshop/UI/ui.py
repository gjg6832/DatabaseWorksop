"""
File: ui
Ui of the application
Author: Greg Godlewski
"""
from DatabaseWorkshop.UI.createUI import *
from DatabaseWorkshop.UI.toolUI import *

def menu(action):
    """
    Menu for the application
    :param action: the actiont to be perforemed
    :return: NONE
    """
    if action == "-h":
        help()
    elif action == "-c":
        create()
    if action == "-s":
        search()
    else:
        print(action,"Invalid action. Use the menu below to pick a valid action")
        help()


def help():
    """
    help menu of the application
    :return: NONE
    """
    print()
    print("----- HELP -----")
    print("-c: Create")
    print("-h: Help")
    print("-s: Search")
    print()