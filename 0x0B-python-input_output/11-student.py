#!/usr/bin/python3

"""
a class Student that defines a student
"""


class Student:
    """
    class with student name and age
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        jj = dict()
        if attrs is None:
            return self.__dict__
        for x in attrs:
            if x in self.__dict__.keys():
                jj[x] = self.__dict__[x]
        return jj

    def reload_from_json(self, json):
        self.__dict__ = json
