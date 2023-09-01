#!/usr/bin/python3
"""Lists the most recent 10 commits"""

import sys
import requests


if __name__ == '__main__':
    """Lists the most recent 10 commits"""

    username = sys.argv[2]
    repo = sys.argv[1]
    url = f'https://api.github.com/repos/{username}/{repo}/commits'

    r = requests.get(url)
    data = r.json()
    size = 0
    for commit in data:
        if size > 9:
            break
        id = commit['sha']
        author = commit['commit']
        name = author['author']['name']
        print(f'{id}: {name}')
        size += 1
