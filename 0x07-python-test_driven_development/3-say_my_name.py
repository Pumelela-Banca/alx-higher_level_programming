#!/usr/bin/python3

"""
function that prints My name is <first name> <last name>
using substitutions
"""


def say_my_name(first_name, last_name=""):
    """
    prints string formatted with first_name and last_name
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    if last_name == "":
        last_name = " "
    print(f"My name is {first_name} {last_name}")
