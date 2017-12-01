#!/usr/bin/python3
"""
fetches https://intranet.hbtn.io/status
"""
import requests
from sys import argv

if __name__ == "__main__":
    let = ""
    if len(argv) > 1:
        let = argv[1]

    dat = {'q': let}

    req = requests.post('http://0.0.0.0:5000/search_user', data=dat)

    try:
        jsn = req.json()
        if len(jsn) == 0:
            print("No result")
        else:
            print("[{}] {}".format(jsn.get('id'), jsn.get('name')))
    except BaseException:
        print("Not a valid JSON")
