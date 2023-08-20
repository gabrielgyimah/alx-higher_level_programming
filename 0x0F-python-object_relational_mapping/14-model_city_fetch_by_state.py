#!/usr/bin/python3
"""prints all City objects from the database"""

from model_city import City
from sqlalchemy.orm import Session
from sys import argv
from sqlalchemy import create_engine
from model_state import State


if __name__ == '__main__':
    engine = create_engine(
            f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}')
    session = Session(bind=engine)

    cities = session.query(City).order_by(City.id).all()
    if cities:
        for city in cities:
            state = (session.query(State)
                     .filter(State.id == city.state_id).first())
            print(f'{state.name}: ({city.id}) {city.name}')

    session.close()
