#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status"""

import requests


if __name__ == '__main__':
    """fetches https://alx-intranet.hbtn.io/status"""

    r = requests.get('https://alx-intranet.hbtn.io/status')
    content = r.text
    cnt_type = type(content)
    output = f'Body response:\n\t- type: {cnt_type}\n\t- content: {content}'

    print(output)
