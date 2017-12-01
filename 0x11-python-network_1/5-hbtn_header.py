#!/usr/bin/python3
"""
fetches https://intranet.hbtn.io/status
"""

if __name__ == "__main__":
    import requests
    from sys import argv
    try:
        content = requests.get(argv[1])
        head = content.headers["X-Request-Id"]
        print(head)
    except:
        pass
