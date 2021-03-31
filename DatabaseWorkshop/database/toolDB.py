"""
File: toolDB
Author: Greg Godlewski
"""
from DatabaseWorkshop import connect


def insertTool(barcode, name, description, categories, sharable, requested):
    cursor = connect.getCursor()
    tool = [barcode, name, description, categories, sharable, requested]
    cursor.execute(
        "INSERT INTO tool (barcode, name, description, categories, shareable, requested) VALUES (%s, %s, %s, %s, %s, %s)",
        tool)
    connect.connectCommit()
    connect.closeCursor(cursor)


def getTool(barcode):
    cursor = connect.getCursor()
    cursor.execute("select barcode from person where barcode = %s", [barcode])
    tool = cursor.fetchone()
    connect.closeCursor(cursor)
    return tool


def printTool(barcode):
    """
    prints a tool
    :param barcode:
    :return:
    """
    cursor = connect.getCursor()
    cursor.execute("select name, description, categories, purchasedate, purchaseprice, shareable, requested from tool where barcode = %s", [barcode])

    row = cursor.fetchone()
    print()
    print("Tool Name: " + row[0])
    print("Tool description: " + str(row[1]))
    print("Tool categories: " + str(row[2]))
    print("Purchase Date: " + str(row[3]))
    print("Purchase Price: " + str(row[4]))
    print("Shareable: " + str(row[5]))
    print("Requested: " + str(row[6]))
    print()

    connect.closeCursor(cursor)
