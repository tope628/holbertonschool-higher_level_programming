#!/usr/bin/python3
"""
fetches https://intranet.hbtn.io/status
"""
import urllib.request
from sys import agrv

if __name__ == "__main__":
    data = {'email': argv[2]}
    url = urllib.parse.urlencode(data)
    url = url.encode('ascii')
    req = urllib.request.Request(argv[1], url)
    with urllib.request.urlopen(req) as response:
        content = response.read().decode('utf-8')
    print(content)
