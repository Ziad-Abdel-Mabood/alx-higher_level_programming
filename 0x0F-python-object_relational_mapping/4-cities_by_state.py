#!/usr/bin/python3
""" lists all  from the database hbtn_0e_4_usa. """
import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    query = "SELECT cities.id, cities.name, states.name\
             FROM cities JOIN states ON states.id = cities.state_id"

    db = MySQLdb.connect(host='localhost',
                         user=username,
                         passwd=password,
                         db=dbname,
                         port=3306)
    cur = db.cursor()
    cur.execute(query)
    selection = cur.fetchall()
    for row in selection:
        print(f"({row[0]}, '{row[1]}', '{row[2]}')")
