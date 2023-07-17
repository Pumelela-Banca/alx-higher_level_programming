#!/usr/bin/python3

"""
module contains a base class for all classes with
attribute id
"""

import json


class Base:
    """
    tracks class and instance id for inheriting classes
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
