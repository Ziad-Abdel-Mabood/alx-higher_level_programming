#!/usr/bin/python3
"""
takes in the name of a state as an argument
then lists all cities of that state, using the database hbtn_0e_4_usa
"""
import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    state_name = sys.argv[4]
    query = "SELECT cities.name\
             FROM cities JOIN states ON states.id = cities.state_id\
             WHERE states.name = %s"

    db = MySQLdb.connect(host='localhost',
                         user=username,
                         passwd=password,
                         db=dbname,
                         port=3306)
    cur = db.cursor()
    cur.execute(query, (state_name,))
    selection = cur.fetchall()
    print(', '.join(city for row in selection for city in row))
