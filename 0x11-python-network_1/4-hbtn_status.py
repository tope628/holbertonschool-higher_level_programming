#!/usr/bin/python3
"""
fetches https://intranet.hbtn.io/status
"""

if __name__ == "__main__":
    import requests
    content = requests.get('https://intranet.hbtn.io/status')
    text = content.text
    print("Body response:")
    print("\t- type: {}\n\t- content: {}".format(type(text), text))
