#!/usr/bin/python3

"""
displays body of url
"""
import sys
from urllib import request
from urllib import error


if __name__ == "__main__":
    try:
        with request.urlopen(sys.argv[1]) as response:
            print(response.read().decode('utf-8'))
    except error.HTTPError as err:
        print(f"Error code: {err.code}")
