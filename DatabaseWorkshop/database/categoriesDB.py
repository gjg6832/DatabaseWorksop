"""
File: personDB
Author: Greg Godlewski
        Saakshi D'Souza
"""

from DatabaseWorkshop import connect

def insertCategory( barcode, category):
    """
    Inserts a category into the categories table
    :param username: the username
    :param password: the password
    :param first_name: the first name
    :param last_name: the last name
    :param email: the email
    :return: NONE
    """
    cursor = connect.getCursor()
    cat = [barcode, category]
    cursor.execute("INSERT INTO categories (barcode, category) VALUES (%s, %s)",cat)
    connect.connectCommit()
    connect.closeCursor(cursor)