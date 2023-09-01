#!/usr/bin/python3
"""Displays the value of the X-Request-Id variable"""

import urllib.request


def main():
    """Displays the value of the X-Request-Id variable"""
    
    url = __import__('sys').argv[1]
    with urllib.request.urlopen(url) as response:
        headers = response.info()
        id = headers.get('X-Request-Id')
    print(id)


if __name__ == '__main__':
    main()
