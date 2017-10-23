#!/usr/bin/python3
from sys import argv
import MySQLdb
"""lists all states from the database hbtn_0e_0_usa"""
if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",port=3306,user=argv[1],passwd=argv[2],db=argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT *  FROM states  ORDER BY id")
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    db.close()
