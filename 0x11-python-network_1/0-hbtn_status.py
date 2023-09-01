#!/usr/bin/python3
""" Fetches https://alx-intranet.hbtn.io/status"""

import urllib.request


def main():
    """Fetches https://alx-intranet.hbtn.io/status"""

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        bytes = response.read()
        cntnt = f'content: {bytes}'
        res_type = f'type: {type(bytes)}'
        encoding = f'utf8 content: {bytes.decode()}'
        output = f'Body response:\n\t- {res_type}\n\t- {cntnt}\n\t- {encoding}'

    print(output)


if __name__ == '__main__':
    main()
