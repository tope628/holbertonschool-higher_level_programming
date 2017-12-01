#!/usr/bin/python3
"""
fetches https://intranet.hbtn.io/status
"""
import requests
from sys import argv
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    req = requests.get('https://api.github.com/users/{}'.format(argv[1]),
                       auth=HTTPBasicAuth(argv[1], argv[2]))
    print(req.json().get('id'))
