#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """
    prints sorted dictionary keys
    @a_dictionary: data
    """
    keep = list(sorted(a_dictionary.keys()))
    for i in keep:
        print("{}: {}".format(i, a_dictionary[i]))
