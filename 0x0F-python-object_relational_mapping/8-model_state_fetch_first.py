#!/usr/bin/python3
""" lists all State objects from the database hbtn_0e_6_usa """
import sqlalchemy
import sys
from model_state import State, Base


if __name__ == "__main__":
    usr = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]
    engine = sqlalchemy.create_engine(
             f'mysql+mysqldb://{usr}:{pwd}@localhost:3306/{db}')
    conn = engine.connect()
    query = sqlalchemy.sql.text(
            'SELECT id, name FROM states where id = 1 ORDER BY id ASC')
    execution = conn.execute(query)
    result = execution.fetchone()
    if result:
        print(f'{result[0]}: {result[1]}')
    else:
        print('Nothing')
