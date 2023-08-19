#!/usr/bin/python3
"""prints the first State object from the database"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import State


def main():
    """Displays first entry on the states table"""

    engine = create_engine(
            f'mysql+mysqldb://{argv[1]}:argv[2]@localhost/{argv[3]}')
    Session = sessionmaker(bind=engine)
    session = Session()

    q_res = session.query(State).first()
    print('1: ' + q_res.name)


if __name__ == '__main__':
    main()
