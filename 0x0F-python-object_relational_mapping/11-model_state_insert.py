#!/usr/bin/python3
"""adds the State object “Louisiana” to the database hbtn_0e_6_usa"""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sys import argv
from model_state import State


if __name__ == '__main__':
    engine = create_engine(
            f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}')
    session = Session(bind=engine)

    state = State(name='Louisiana')
    session.add(state)
    session.commit()
    session.refresh(state)

    print(state.id)

    session.close()
