#!/usr/bin/python3
"""lists all State objects that contain the letter a"""

from model_state import State, Base
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


def main():
    if len(argv) != 4:
        return

    engine = create_engine(
            f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}')
    Base.metadata.create_all(engine)
    session = Session(engine)

    states = (session.query(State)
              .filter(State.name.like('%a%'))
              .order_by(State.id))

    if states:
        counter = 1
        for state in states:
            print(f'{counter}: {state.name}')
            counter += 1
    else:
        print('Nothing')


if __name__ == '__main__':
    main()
