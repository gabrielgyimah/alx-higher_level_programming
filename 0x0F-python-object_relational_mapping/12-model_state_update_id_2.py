#!/usr/bin/python3
""" changes the name of a State object in the database"""

from sqlalchemy.orm import Session
from model_state import State
from sys import argv
from sqlalchemy import create_engine


if __name__ == '__main__':
    engine = create_engine(
            f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}')
    session = Session(bind=engine)

    state = session.query(State).filter(State.id == 2).first()
    state.name = 'New Mexico'
    session.commit()
    session.close()
