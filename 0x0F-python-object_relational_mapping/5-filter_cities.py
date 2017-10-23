#!/usr/bin/python3
from sys import argv
import MySQLdb
"""lists all states from the database hbtn_0e_0_usa"""
if __name__ == "__main__":
    db = MySQLdb.connect("localhost", argv[1], argv[2], argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities JOIN states ON cities.state_id\
    = states.id WHERE states.name = '{}' ORDER BY cities.id".format(argv[4]))
    print(", ".join(city[0] for city in cur.fetchall()))
    cur.close()
    db.close()
