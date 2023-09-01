#!/usr/bin/python3
"""Sends a POST request to http://0.0.0.0:5000/search_user"""

import sys
import requests


if __name__ == '__main__':
    """Sends a POST request to http://0.0.0.0:5000/search_user"""

    data = {'q': ''}

    if sys.argv[1]:
        data['q'] = sys.argv[1]
    res = requests.post('http://0.0.0.0:5000/search_user', data=data)

    try:
        obj = res.json()
        if not obj:
            print('No result')
        else:
            print(f"[{obj.get('id')}] {obj.get('name')}")
    except Exception:
        print("Not a valid JSON")
