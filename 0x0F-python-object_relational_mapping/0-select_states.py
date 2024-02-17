#!/usr/bin/python3
"""
This script that lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    username = argv[1]
    password = argv[2]
    database_name = argv[3]

    try:
        connection = MySQLdb.connect(
            host="localhost", user=username, passwd=password, db=database_name
        )

        cursor = connection.cursor()

        cursor.execute("SELECT * FROM states ORDER BY states.id ASC")

        rows = cursor.fetchall()

        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print("Error retrieving data!", e)

    finally:
        cursor.close()
        connection.close()