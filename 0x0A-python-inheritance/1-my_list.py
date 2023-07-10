#!/usr/bin/python3

"""
class that inherits from list and adds a method
"""


class MyList(list):
    """
    adds print sorted to list class
    """
    def print_sorted(self):
        """
        prints sorted list
        """
        ls = self[:]
        print(sorted(ls))
