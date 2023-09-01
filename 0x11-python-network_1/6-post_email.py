#!/usr/bin/python3
"""Sends a POST request to the passed URL with the email"""

import sys
import requests


if __name__ == '__main__':
    """ends a POST request to the passed URL with the email"""
    
    data = {'email': sys.argv[2]}
    r = requests.post(sys.argv[1], data=data)
    
    print(r.text)
