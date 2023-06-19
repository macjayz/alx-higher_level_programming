#!/usr/bin/python3
"""
This script lists all states from the database
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    database query below
    """
    db = MySQLdb.connect(
        host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3])

    db_cursor = db.cursor()

    db_cursor.execute("SELECT * FROM states")

    rows_selected = db_cursor.fetchall()

    for row in rows_selected:
        print(row)
