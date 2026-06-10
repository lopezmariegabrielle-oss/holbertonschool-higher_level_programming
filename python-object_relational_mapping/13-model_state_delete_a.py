#!/usr/bin/python3
"""Deletes all State objects with a name
containing the letter 'a' from the database.
"""
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

    session.query(State).filter(
        State.name.like('%a%')
    ).delete(synchronize_session='fetch')
    session.commit()

    session.close()
