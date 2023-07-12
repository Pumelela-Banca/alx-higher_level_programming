#!/usr/bin/python3

"""
script to create python objects to be saved in file add_item.json
"""

import json
from sys import argv


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


if len(argv) == 1:
    with open("add_item.json", "w+") as f:
        data = f.readlines()
        if not data:
            save_to_json_file([], "add_item.json")
else:
    with open("add_item.json", "w+") as f:
        data = f.readline()
        if not data:
            json.dump([argv[1]], f)
        elif data == "[]":
            for x in argv[1:]:
                data.append(x)
            json.dump(data, f)
