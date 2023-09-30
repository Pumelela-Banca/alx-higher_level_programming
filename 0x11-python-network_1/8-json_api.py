#!/usr/bin/python3

"""
Requests header from a web-site
"""
import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) < 2:
        vals = {"q": ""}
    else:
        vals = {"q": sys.argv[1]}
    r = requests.post(sys.argv[1], data=vals)
