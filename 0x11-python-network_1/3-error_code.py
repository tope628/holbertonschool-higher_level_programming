#!/usr/bin/python3
"""
fetches https://intranet.hbtn.io/status
"""
import urllib.request
from sys import argv

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(argv[1]) as response:
            content = response.read().decode('utf-8')
        print(content)
    except urlib.error.HTTPError as err:
        print("Error code: {}".format(err.code))
