#!/usr/bin/python3
"""Prints the first State object from the database hbtn_0e_6_usa"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    detabase_name = sys.argv[3]
    engine = create_engine(
        f"mysql+pymysql://{username}:{password}"
        f"@localhost:3306/{detabase_name}"
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    premier_etat = session.query(State).order_by(State.id).first()
    if premier_etat is None:
        print("Nothing")
    else:
        print(f"{premier_etat.id}: {premier_etat.name}")
