#!/usr/bin/python3
from sys import argv
import MySQLdb
"""lists all states from the database hbtn_0e_0_usa"""
if __name__ == "__main__":
    db = MySQLdb.connect("localhost", argv[1], argv[2], argv[3], port=3306)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name = %s ORDER BY id",
                  (argv[4], ))
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    db.close()
