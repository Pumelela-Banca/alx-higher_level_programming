#!/usr/bin/python3

"""
Requests data from a library
"""
from urllib import request


with request.urlopen(
        'https://alx-intranet.hbtn.io/status') as response:
    content = response.read()
    print("Body response:")
    print(f"\t- type: {type(content)}")
    print(f"\t- content: {content}")
    print(f"\t- utf8 content: {content.decode('utf-8')}")
