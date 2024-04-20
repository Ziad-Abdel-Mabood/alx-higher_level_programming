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
    meta = sqlalchemy.MetaData()
    states = sqlalchemy.Table('states', meta, autoload_with=engine)
    sel = states.select()
    result = conn.execute(sel)
    for row in result:
        print(f'{row.id}: {row.name}')
