"""
File: toolDB
Author: Greg Godlewski
"""
from DatabaseWorkshop import connect


def insertTool(barcode, name, description, categories, purchasedate, purchaseprice, sharable, requested):
    cursor = connect.getCursor()
    tool = [barcode, name, description, categories, purchasedate, purchaseprice, sharable, requested]
    cursor.execute(
        "INSERT INTO tool (barcode, name, description, categories, purchasedate, purchaseprice, shareable, requested) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
        tool)
    connect.connectCommit()
    connect.closeCursor(cursor)


def getTool(barcode):
    cursor = connect.getCursor()
    cursor.execute("select barcode from tool where barcode = %s", [barcode])
    tool = cursor.fetchone()
    connect.closeCursor(cursor)
    return tool


def printToolBarcode(barcode):
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

def deleteTool(barcode):
    """
    Deletes a tool
    :param barcode:
    :return:
    """


def printToolName(name):
    """
    prints a tool
    :param barcode:
    :return:
    """
    cursor = connect.getCursor()
    cursor.execute(
        "select description, categories, purchasedate, purchaseprice, shareable, requested from tool where name = %s",
        [name])
    row = cursor.fetchone()
    print()
    print("Tool description: " + str(row[0]))
    print("Tool categories: " + str(row[1]))
    print("Purchase Date: " + str(row[2]))
    print("Purchase Price: " + str(row[3]))
    print("Shareable: " + str(row[4]))
    print("Requested: " + str(row[5]))
    print()

    connect.closeCursor(cursor)



