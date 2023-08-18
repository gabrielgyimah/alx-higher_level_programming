#!/usr/bin/python3
"""lists all cities from the database"""

import MySQLdb
import sys


def main():
    conn = MySQLdb.connect(
            host='localhost', user=sys.argv[1],
            passwd=sys.argv[2], db=sys.argv[3],
            port=3306)
    cursor = conn.cursor()

    query = """SELECT cities.id, cities.name, states.name
    FROM cities INNER JOIN states ON cities.state_id=states.id
    ORDER BY cities.id
    """
    cursor.execute(query)
    cities = cursor.fetchall()

    for city in cities:
        print(city)

    cursor.close()
    conn.close()


if __name__ == '__main__':
    main()
