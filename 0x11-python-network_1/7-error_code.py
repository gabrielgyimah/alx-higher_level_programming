#!/usr/bin/python3
"""Sends a request to the URL and displays the body"""

import sys
import requests


if __name__ == '__main__':
    """Sends a request to the URL and displays the body"""

    r = requests.get(sys.argv[1])

    if r.status_code >= 400:
        print(f'Error code: {r.status_code}')
    else:
        print(r.text)
