#!/usr/bin/python3
"""Lists the State object with the name
passed as argument from the database hbtn_0e_6_usa"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    nom_recherche = sys.argv[4]
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(username, password, database_name),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    etat = (
        session.query(State)
        .filter(State.name == nom_recherche)
        .first()
    )
    if etat is None:
        print("Not found")
    else:
        print(etat.id)

    session.close()
