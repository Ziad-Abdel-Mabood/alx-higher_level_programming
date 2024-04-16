#!/usr/bin/python3
import MySQLdb
import sys
""" a script that lists all states from the darabase hbtn_0e_0_usa """


if __name__ == "__main__":
	username = sys.argv[1]
	password = sys.argv[2]
	dbname = sys.argv[3]

	db = MySQLdb.connect(host='localhost',
						 user=username,
						 passwd=password,
						 db=dbname,
						 port=3306)
	cur = db.cursor()
	cur.execute("SELECT * FROM states ORDER BY id ASC")
	selection = cur.fetchall()
	for row in selection:
		print(f"({row[0]}, '{row[1]}')")
