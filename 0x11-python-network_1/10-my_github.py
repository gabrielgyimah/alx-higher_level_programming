#!/usr/bin/python3
"""GitHub API Module"""

import requests
import sys
from requests.auth import HTTPBasicAuth


if __name__ == '__main__':
    """takes your GitHub credentials (username and password)
        and uses the GitHub API to display your id
    """

    username = sys.argv[1]
    password = sys.argv[2]
    url = f'https://api.github.com/user'
    cred = HTTPBasicAuth(username, password)

    response = requests.get(url, auth=cred)
    data = response.json()
    print(data.get('id'))
