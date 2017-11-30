#!/usr/bin/python3
"""
fetches https://intranet.hbtn.io/status
"""
import urllib.request
from sys import argv

if __name__ == "__main__":

    with urllib.request.urlopen(argv[1]) as response:
        content = response.info().get('X-Request-Id')
    print(content)
