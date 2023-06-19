#!/usr/bin/python3
"""
a script that takes in arguments and
displays all values in the states
This time the script is safe from
MySQL injections!
"""

import MySQLdb as db
from sys import argv

if __name__ == "__main__":
    """
    displays all values from the database.
    """
    db = db.connect(host="localhost", port=3306,
                            user=argv[1], passwd=argv[2], db=argv[3])
    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM states WHERE name LIKE \
                    BINARY %(name)s ORDER BY states.id ASC", {'name': argv[4]})
    rows_selected = cursor.fetchall()
    for row in rows_selected:
        print(row)
