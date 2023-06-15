#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    """
    update a dictionary
    @a_dictionary: data
    @key: update
    """
    if key is "":
        return a_dictionary
    if key not in a_dictionary.keys():
        return a_dictionary
    else:
        del a_dictionary[key]
    return a_dictionary
