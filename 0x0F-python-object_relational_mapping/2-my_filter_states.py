#!/usr/bin/python3
"""
takes  in an argument and displays all values
in the states table of hbtn_0e_0_us where name
matches the argument.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host='localhost',
                         user=username,
                         passwd=password,
                         db=dbname,
                         port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states \
                WHERE BINARY name = '{}' \
                ORDER BY id ASC".format(state_name))
    selection = cur.fetchall()
    for row in selection:
        print(f"({row[0]}, '{row[1]}')")
