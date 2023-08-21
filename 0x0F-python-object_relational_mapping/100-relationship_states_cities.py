#!/usr/bin/python3

"""
Creates the State “California” with the City
"""
from sys import argv
from sqlalchemy.orm import session
from sqlalchemy import create_engine
from relationship_city import Base, City
from relationship_state import State

if __name__ == '__main__':
    engine = create_engine(
        f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}')
    session = Session(bind=engine)

    state = State(name="California")
    state.cities = [City(name='San Francisco')]
    session.add(state)
    session.commit()
