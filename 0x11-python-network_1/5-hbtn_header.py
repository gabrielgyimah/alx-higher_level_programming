#!/usr/bin/python3
"""Sends a request to the URL"""

import requests
import sys


if __name__ == '__main__':
    """Sends a request to the URL and displays
    the value of the variable X-Request-Id
    """

    r = requests.get(sys.argv[1])
    id = r.headers.get('X-Request-Id')
    print(id)
