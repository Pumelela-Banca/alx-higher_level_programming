#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    """
    multiply all values by e
    @a_dictionary: data
    Return: new dictionary
    """
    if a_dictionary is None:
        return None
    return {x: y * 2 for (x, y) in a_dictionary.items()}
