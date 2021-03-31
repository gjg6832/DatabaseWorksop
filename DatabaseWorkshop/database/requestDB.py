"""
File: requestDB
Author: Greg Godlewski
"""
from DatabaseWorkshop import connect


def insertRequest(id, userrequesting, tool, owner, date, duration, status):
    cursor = connect.getCursor()
    request = [id, userrequesting, tool, owner, date, duration, status]
    cursor.execute(
        "INSERT INTO request (id, userrequesting, tool, owner, date, duration, status) VALUES (%s,%s,%s,%s,%s,%s,%s)",
        request)
    connect.connectCommit()
    connect.closeCursor(cursor)


def getRequest(id):
    cursor = connect.getCursor()
    cursor.execute("select id from request where id = %s", [id])
    request = cursor.fetchone()
    connect.closeCursor(cursor)
    return request
