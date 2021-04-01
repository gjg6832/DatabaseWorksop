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
    cursor.execute("select * from tool where barcode = %s", [barcode])
    tool = cursor.fetchone()
    connect.closeCursor(cursor)
    return tool

def addToolOwner(username, barcode):
    """
    add a tool to a user
    :param username:
    :param barcode:
    :return:
    """
    cursor = connect.getCursor()
    cursor.execute("update tool set owner = %s where barcode = %s", [username, barcode])
    connect.connectCommit()
    connect.closeCursor(cursor)


def deleteToolOwner(barcode):
    """
    delete a tool to a user
    :param username:
    :param barcode:
    :return:
    """
    cursor = connect.getCursor()
    cursor.execute("update tool set owner = %s where barcode = %s", [None, barcode])
    connect.connectCommit()
    connect.closeCursor(cursor)


def editToolName(name, barcode):
    cursor = connect.getCursor()
    cursor.execute("update tool set name = %s where barcode = %s", [name, barcode])
    connect.connectCommit()
    connect.closeCursor(cursor)


def editToolDescrip(descrip, barcode):
    cursor = connect.getCursor()
    cursor.execute("update tool set description = %s where barcode = %s", [descrip, barcode])
    connect.connectCommit()
    connect.closeCursor(cursor)


def editToolCategorie(categorie, barcode):
    cursor = connect.getCursor()
    cursor.execute("update tool set categories = %s where barcode = %s", [categorie, barcode])
    connect.connectCommit()
    connect.closeCursor(cursor)


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
    :param name:
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

def printToolCategory(category):
    """
    prints a tool
    :param category:
    :return:
    """
    cursor = connect.getCursor()
    cursor.execute(
        "select name from tool where categories = %s",
        [category])
    row = cursor.fetchall()
    print()
    print("Tool names:")
    for item in row:
        print("Tool name: " + str(item[0]))
    print()

    connect.closeCursor(cursor)

def printAvailableTools():
    """
    prints al available tools
    :param:
    :return:
    """
    cursor = connect.getCursor()
    cursor.execute(
        "select name from tool where shareable is true order by name asc")
    row = cursor.fetchall()
    print()
    print("Tool names:")
    for item in row:
        print(str(item[0]))
    print()

    connect.closeCursor(cursor)

def printLentTools():
    """
    INCOMPLETE: waiting for overdue


     prints all lent tools
     :param:
     :return:
     """
    cursor = connect.getCursor()
    cursor.execute(
        "select owner, userrequested, tooolrequested, date, duration, status from request where status = Accepted order by date asc")
    row = cursor.fetchall()
    print()
    print("Owner: " + str(row[0][0]))
    for item in row:
        print(str(item[1]) + " has:/t" + str(item[2]) + "")
    print()

    connect.closeCursor(cursor)

def printBorrowedTools():
    """
    INCOMPLETE: waiting for overdue
    condition not defined properly

    prints all borrowed tools
    :param:
    :return:
    """
    cursor = connect.getCursor()
    cursor.execute(
        "select owner, userrequesting, tooolrequested, date, duration, status from request where status = Accepted order by date asc")
    row = cursor.fetchall()
    print()
    print("Tool names:")
    for item in row:
        print(str(item[1]) + "borrowed from " + str(item[0]))
    print()

    connect.closeCursor(cursor)
