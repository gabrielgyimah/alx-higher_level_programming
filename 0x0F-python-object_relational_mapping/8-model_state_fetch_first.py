#!/usr/bin/python3
"""prints the first State object from the database"""

from sqlalchemy import create_engine
from sqlalchemy.orm.session import Session
from sys import argv
from model_state import State, Base


def main():
    """Displays first entry on the states table"""

    if len(argv) != 4:
        return

    engine = create_engine(
            f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}')
    Base.metadata.create_all(engine)
    session = Session(engine)

    q_res = session.query(State).order_by(State.id).first()

    if (q_res):
        print(f'{q_res.id}: {q_res.name}')
    else:
        print('Nothing')


if __name__ == '__main__':
    main()
