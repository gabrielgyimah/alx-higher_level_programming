#!/usr/bin/python3

"""A script that lists all states with a name
    starting with N (upper N) from the database
    hbtn_0e_0_usa
"""

import sys
import MySQLdb


def main():
    conn = MySQLdb.connect(
            host='localhost', user=sys.argv[1],
            passwd=sys.argv[2], db=sys.argv[3], port=3306
            )
    cursor = conn.cursor()

    query = """
                SELECT * FROM states
                WHERE name LIKE %s
                ORDER BY states.id
    """
    like_pattern = ('N%',)
    cursor.execute(query, like_pattern)
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    conn.close()


if __name__ == '__main__':
    main()
