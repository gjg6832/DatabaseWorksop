"""
File: personDB
Author: Greg Godlewski
"""

from DatabaseWorkshop import connect
from datetime import date


def insertPerson(username, password, first_name, last_name, email, creationdate, laccesdate):
    """
    Inserts a user into the person table
    :param username: the username
    :param password: the password
    :param first_name: the first name
    :param last_name: the last name
    :param email: the email
    :return: NONE
    """
    cursor = connect.getCursor()
    person = [username, password, first_name, last_name, email, creationdate, laccesdate]
    cursor.execute("INSERT INTO person (username, password, firstname, lastname, email, creationdate, laccessdate) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                   person)
    connect.connectCommit()
    connect.closeCursor(cursor)


def getPerson(username):
    """
    Gets a user
    :param username: the username
    :return: the user
    """
    cursor = connect.getCursor()
    cursor.execute("select username from person where username = %s", [username])
    person = cursor.fetchone()
    connect.closeCursor(cursor)
    return person[0]


def getPassword(username):
    cursor = connect.getCursor()
    cursor.execute("select password from person where username = %s", [username])
    password = cursor.fetchone()
    connect.closeCursor(cursor)
    return password[0]


def editDateAndTime(username):
    today = date.today()
    cursor = connect.getCursor()
    cursor.execute("update person set laccessdate = %s where username = %s", [today, username])
    connect.connectCommit()
    connect.closeCursor(cursor)

