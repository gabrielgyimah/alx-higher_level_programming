#!/usr/bin/python3
from sys import stderr


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))

    except Exception as e:
        stderr.write('Exception: ')
        stderr.write(str(e))
        stderr.write('\n')

        return False

    return True
