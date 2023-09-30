#!/usr/bin/python3
"""
Takes credentials and uses them to show ID
"""

import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    inp = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = requests.get("https://api.github.com/user", auth=inp)
    print(r.json().get('id'))
