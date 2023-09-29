#!/usr/bin/python3

"""
Requests data from a library
"""
from urllib import request


with request.urlopen(
        'https://alx-intranet.hbtn.io/status') as response:
    content = response.read()
    print("Body response:")
    print(f"    - type: {type(content)}")
    print(f"    - content: {content}")
    print(f"    - utf8 content: {content.decode('utf-8')}")
