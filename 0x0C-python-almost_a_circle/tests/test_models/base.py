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

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            with open(f"{cls.__name__}.json", "w") as f:
                f.write("[]")
        else:
            with open(f"{cls.__name__}.json", "w") as f:
                dict_info = []
                for x in list_objs:
                    hold = cls.to_dictionary(x)
                    dict_info.append(hold)
                f.write(Base.to_json_string(dict_info))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        fake = cls(**dictionary)
        fake.update()
        return fake

    @classmethod
    def load_from_file(cls):
        with open(f"{cls.__name__}.json", "r") as f:
            try:
                ss = f.readline()
                json_str = json.loads(ss)

                for i in json_str:
                    cls.create(i)
                return json_str
            except FileNotFoundError:
                return []
