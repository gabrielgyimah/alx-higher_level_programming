#!/usr/bin/python3

"""lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
import sys


def main():
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    host = 'localhost'
    port = 3306

    conn = MySQLdb.connect(host=host, user=user,
                           passwd=password, db=database, port=port)

    cursor = conn.cursor()

    query = 'SELECT * FROM states ORDER BY states.id'
    cursor.execute(query)
    states = cursor.fetchall()

    for state in states:
        print(state)


if __name__ == '__main__':
    main()
