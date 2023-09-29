#!/usr/bin/python3

"""
Requests header from a web-site
"""
import sys
import requests


if __name__ == "__main__":
    load = {'email': sys.argv[2]}
    with requests.post(sys.argv[1], data=load) as response:
        print(f"Your email is: {response.text}")
