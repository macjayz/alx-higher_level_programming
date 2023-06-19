#!/usr/bin/python3
"""
a script that takes in an argument and displays all values in the states
"""

import MySQLdb as db
from sys import argv

if __name__ == '__main__':
    """
    from the database search for the passed arg.
    """
    db_connect = db.connect(host="localhost", port=3306,
                            user=argv[1], passwd=argv[2], db=argv[3])
    db_cursor = db_connect.cursor()

    db_cursor.execute(
        "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY \
                        states.id ASC".format(argv[4]))
    rows_selected = db_cursor.fetchall()

    for row in rows_selected:
        print(row)
