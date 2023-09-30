#!/usr/bin/python3

"""
Requests header from a web-site
"""
import sys
import requests


if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    if r.status_code >= 400:
        print("Error code: ", r.status_code)
    else:
        print(r.text)
