#!/usr/bin/python3
"""
fetches https://intranet.hbtn.io/status
"""

if __name__ == "__main__":
    import requests
    from sys import argv
    data = {'email': argv[2]}
    req = urllib.request.post(argv[1], data)
    print(req.text)
