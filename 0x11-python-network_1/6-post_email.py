#!/usr/bin/python3

"""
Requests header from a web-site
"""
import sys
import requests


if __name__ == "__main__":
    load = sys.argv[2]
    with requests.post(sys.argv[1],data=load) as response:
        print(response.text)
