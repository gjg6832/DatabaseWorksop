"""
File: requestDB
Author: Greg Godlewski
"""
from DatabaseWorkshop import connect


def insertRequest(id, userrequesting, tool, owner, date, duration, status, returndate):
    cursor = connect.getCursor()
    request = [id, userrequesting, tool, owner, date, duration, status, returndate]
    cursor.execute(
        "INSERT INTO request (id, userrequesting, toolrequested, owner, date, duration, status, returndate) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
        request)
    connect.connectCommit()
    connect.closeCursor(cursor)


def getRequest(id):
    cursor = connect.getCursor()
    cursor.execute("select * from request where id = %s", [id])
    request = cursor.fetchone()
    connect.closeCursor(cursor)
    return request

def updateStatus(status, id):
    cursor = connect.getCursor()
    cursor.execute("update request set status = %s where id = %s", [status, id])
    connect.connectCommit()
    connect.closeCursor(cursor)

def updateReturnDate(returndate, id):
    cursor = connect.getCursor()
    cursor.execute("update request set returndate = %s where id = %s", [returndate, id])
    connect.connectCommit()
    connect.closeCursor(cursor)

def deleteRequest(id):
    cursor = connect.getCursor()
    cursor.execute("DELETE FROM request where id = %s", [id])
    connect.connectCommit()
    connect.closeCursor(cursor)



def printRequesterRequests(userrequesting):
    #TODO: Formant request better
    cursor = connect.getCursor()
    cursor.execute(
        "select * from request where userrequesting = %s",
        [userrequesting])
    row = cursor.fetchall()
    print()
    print("Requests:")
    for item in row:
        print("    id: " + str(item[0]))
        print("    User Requesting: " + str(item[1]))
        print("    Tool Requested: " + str(item[2]))
        print("    Owner: " + str(item[3]))
        print("    Date: " + str(item[4]))
        print("    Duration: " + str(item[5]))
        print("    Status: " + str(item[6]))
        print("    Return Date: " + str(item[7]))
        print()
        print()
    print()

    connect.closeCursor(cursor)


def printRequesterOwner(owner):
    #TODO: Formant request better
    cursor = connect.getCursor()
    cursor.execute(
        "select * from request where owner = %s",
        [owner])
    row = cursor.fetchall()
    print()
    print("Requests:")
    for item in row:
        print("    id: " + str(item[0]))
        print("    User Requesting: " + str(item[1]))
        print("    Tool Requested: " + str(item[2]))
        print("    Owner: " + str(item[3]))
        print("    Date: " + str(item[4]))
        print("    Duration: " + str(item[5]))
        print("    Status: " + str(item[6]))
        print("    Return Date: " + str(item[7]))
        print()
        print()

    print()

    connect.closeCursor(cursor)

