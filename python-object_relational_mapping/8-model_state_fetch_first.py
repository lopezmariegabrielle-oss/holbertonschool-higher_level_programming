#!/usr/bin/python3
"""Prints the first State object from the database hbtn_0e_6_usa"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(username, password, database_name),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    premier_etat = session.query(State).order_by(State.id).first()
    if premier_etat is None:
        print("Nothing")
    else:
        print("{}: {}".format(premier_etat.id, premier_etat.name))

    session.close()
