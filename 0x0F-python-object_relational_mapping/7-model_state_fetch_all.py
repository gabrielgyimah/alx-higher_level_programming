#!/usr/bin/python3
"""Lists all State objects from the database hbtn_0e_6_usa"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base


def main():
    """Displays all state entries in the db"""
    engine = create_engine(
            f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}')
    Session = sessionmaker(bind=engine)
    session = Session()

    res = session.query(State).order_by(State.id.asc()).all()
    counter = 1
    for state in res:
        print(f'{counter}: {state.name}')
        counter += 1


if __name__ == '__main__':
    main()
