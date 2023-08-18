#!/usr/bin/python3

"""displays all states matching name"""

import MySQLdb
import sys


def main():
    conn = MySQLdb.connect(
            host='localhost', user=sys.argv[1],
            passwd=sys.argv[2], db=sys.argv[3],
            port=3306
            )
    cursor = conn.cursor()

    query = f"""
    SELECT * FROM states WHERE name=%s
    """

    name_to_search = sys.argv[4]
    cursor.execute(query, (name_to_search,))

    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    conn.close()


if __name__ == '__main__':
    main()
