#!/usr/bin/python3

"""#!/usr/bin/python3
Requests header from a web-site
"""
import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) < 2:
        vals = {"q": ""}
    else:
        vals = {"q": sys.argv[1]}
    r = requests.post('http://0.0.0.0:5000/search_user',
                      data=vals)
    try:
        dd = r.json()
        if dd == {}:
            print("No result")
        else:
            print(f"[{dd.get('id')}] {dd.get('name')}")
    except ValueError:
        print("Not a valid JSON")
