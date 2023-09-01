#!/usr/bin/python3
"""Displays the body of the response (decoded in utf-8)"""

from urllib import request, error
import sys


if __name__ == '__main__':
    """Displays the body of the response (decoded in utf-8)"""

    try:
        with request.urlopen(sys.argv[1]) as response:
            body = response.read().decode('utf-8')

        print(body)

    except error.HTTPErro as e:
        print(f'Error code: {e.code}')
