#!/usr/bin/python3
"""Lists all State objects from the database hbtn_0e_6_usa."""

from sqlalchemy.orm import Session
from model_state import Base, State
from sqlalchemy import create_engine
from sys import argv


if __name__ == "__main__":
    engine = create_engine(
            f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}')
    Base.metadata.create_all(engine)
    session = Session(engine)

    states = session.query(State).filter(
            State.name.like('%a%')).order_by(State.id)

    if states:
        counter = 1
        for state in states:
            print(f'{counter}: {state.name}')
            counter += 1
