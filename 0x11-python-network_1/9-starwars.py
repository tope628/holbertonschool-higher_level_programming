#!/usr/bin/python3
"""
fetches https://intranet.hbtn.io/status
"""
import requests
from sys import argv

if __name__ == "__main__":
    data = {'search': argv[1]}
    req = requests.get('https://swapi.co/api/people/', params=data)
    ppl = req.json()['results']
    print("Number of results: {}".format(req.json().get('count')))
    for person in ppl:
        print(person['name'])
