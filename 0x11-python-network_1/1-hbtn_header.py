#!/usr/bin/python3

"""
Requests data from a library
"""
import sys
from urllib import request


if __name__ == "__main__":
    with request.urlopen(sys.argv[1]) as response:
        print(response.headers.get('X-Request-Id'))
