#!/usr/bin/python3

"""displays all states matching name"""

import MySQLdb
import sys


def main():
    conn = MySQLdb.connect(
            host='localhost', user=sys.argv[1],
            passwd=sys.argv[2], db=sys.argv[3],
            port=3306)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM states WHERE BINARY
    name LIKE '{}' ORDER BY states.id
    """.format(sys.argv[4]))

    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    conn.close()


if __name__ == '__main__':
    main()
