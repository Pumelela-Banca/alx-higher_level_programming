#!/usr/bin/python3

"""
a module with class MyInt that inherits from int
"""


class MyInt(int):
    """
    inherits from int but switches == and !=
    """

    def __eq__(self, other):
        return int.__ne__(self, other)

    def __ne__(self, other):
        return int.__eq__(self, other)
