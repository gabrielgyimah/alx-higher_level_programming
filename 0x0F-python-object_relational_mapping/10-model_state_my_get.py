#!/usr/bin/python3
"""prints the State object with the name passed as argumen"""

from sqlalchemy.orm import Session
from sys import argv
from model_state import State
from sqlalchemy import create_engine


if __name__ == '__main__':
    engine = create_engine(
            f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}')
    session = Session(bind=engine)

    state = session.query(State).filter(State.name == argv[4]).first()
    if state:
        print(state.id)
    else:
        print('Not found')
