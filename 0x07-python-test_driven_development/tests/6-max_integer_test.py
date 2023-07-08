#!/usr/bin/python3

"""
Unit test for function: def max_integer(list=[]): and all its cases
Tests:
    1- list is not empty
    2- list is type list
    3- all items in list are ints
    4- works for negative values
    5- works for all  types  of values
"""

import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Class to test result of scenarios.
    """
    def test_empty(self):
        """test empty list"""
        self.assertEquals(max_integer(), None)

    def test_normal(self):
        """normal case"""
        self.assertEquals(max_integer([1, 2, 14, 16, 4]), 16)

    def test_one_element(self):
        """single element"""
        self.assertEquals(max_integer([16]), 16)

    def test_negative(self):
        """negative values"""
        self.assertEquals(max_integer([-1, -2, -14, -16, -4]), -1)
    
    def test_mix(self):
        """test mix values"""
        self.assertEquals(max_integer([-1, 2, -14, -16, 4]), 4)
    
    def test_with_zero(self):
        """list has zero"""
        self.assertEquals(max_integer(
            [-1, -2, -14, -16, -4, 0]), -16)

    def test_max_start(self):
        """maxt at start"""
        self.assertEquals(max_integer([21, 2, 4, -16, -1000]), 21)

    def test_max_middle(self):
        """maxt in middle"""
        self.assertEquals(max_integer([-1, 2, 4, -16, -1000]), 4)


if __name__ == '__main__':
    unittest.main()
