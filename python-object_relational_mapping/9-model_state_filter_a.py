#!/usr/bin/python3
"""Lists all State objects that contain the
letter a from the database hbtn_0e_6_usa"""
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

    etats_avec_a = (
            session.query(State)
            .filter(State.name.like('%a%'))
            .order_by(State.id)
            .all()
        )
    for etat in etats_avec_a:
        print(f"{etat.id}: {etat.name}")

    session.close()
