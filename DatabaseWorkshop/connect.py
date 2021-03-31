"""
File: connect
Author: Greg Godlewski
"""
import psycopg2

c = psycopg2.connect("host='reddwarf.cs.rit.edu' dbname='p320_01h' user='p320_01h' password='Rm9DIM3KHihG'")


def dbConnect():
    return c


def connectCommit():
    c.commit()


def connectClose():
    c.close()


def getCursor():
    return c.cursor()


def closeCursor(cursor):
    cursor.close()
