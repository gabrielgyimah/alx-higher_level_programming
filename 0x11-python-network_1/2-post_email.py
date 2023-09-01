#!/usr/bin/python3
"""Sends a POST request to the passed URL"""

import urllib.request
import urllib.parse
import sys


def main():
    """Sends a POST request to the passed URL"""

    url = sys.argv[1]
    email = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(email).encode('ascii')
    req = urllib.request.Request(url, data=data, method='POST')

    with urllib.request.urlopen(req) as response:
        info = response.read()

    print(info.decode())


if __name__ == '__main__':
    main()
