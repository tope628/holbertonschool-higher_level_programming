#!/usr/bin/python3
from sys import argv
import MySQLdb
"""lists all states from the database hbtn_0e_0_usa"""
if __name__ == "__main__":
    db = MySQLdb.connect("localhost", argv[1], argv[2], argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id")
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()
