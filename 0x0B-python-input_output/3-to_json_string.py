#!/usr/bin/python3

"""
module with function converts json object to python
"""

import json


def to_json_string(my_obj):
    """
    function that returns the JSON representation of an
    object (string)
    """
    if isinstance(my_obj, set):
        return json.dumps(list(my_obj))
    return json.dumps(my_obj)
