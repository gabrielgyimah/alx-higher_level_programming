#!/usr/bin/python3
"""
deletes all State objects with a name containing
the letter a from the database hbtn_0e_6_usa
"""

from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from model_state import State
from sys import argv


if __name__ == '__main__':
    engine = create_engine(
            f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}')
    session = Session(bind=engine)

    states = session.query(State).filter(State.name.like('%a%')).all()

    if states:
        for state in states:
            session.delete(state)
        session.commit()
    session.close()
