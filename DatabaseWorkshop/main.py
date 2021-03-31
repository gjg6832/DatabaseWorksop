"""
File: main.py
Runs the application
Author: Greg Godlewski
"""
import connect
import UI.ui

def main():
    connect.dbConnect()
    UI.ui.help()
    action = input("Enter the action: ").strip()
    while action != "":
        UI.ui.menu(action)
        action = input("Enter the action: ").strip()
    connect.connectClose()

main()
