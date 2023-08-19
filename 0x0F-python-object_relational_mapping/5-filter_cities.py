#!/usr/bin/python3
"""lists all cities of a state"""

import MySQLdb
import sys


def main():
    conn = MySQLdb.connect(
            host='localhost', user=sys.argv[1],
            passwd=sys.argv[2], db=sys.argv[3],
            port=3303)
    cursor = conn.cursor()

    query = """
    SELECT cities.name FROM cities
    INNER JOIN states ON cities.state_id=states.id
    WHERE states.name=%s ORDER BY cities.id
    """

    cursor.execute(query, (sys.argv[4],))
    cities = cursor.fetchall()

    for city in cities:
        print(city, end='')

        if city != cities[-1]:
            print(',')
    print()

    cursor.close()
    conn.close()


if __name__ == '__main__':
    main()
