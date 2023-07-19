#!/usr/bin/python3

"""
module contains a base class tests matching
given questions
"""

import unittest

from test_models.base import Base


class TestSquare(unittest.TestCase):
    """test id track"""
    def test_ids(self):
        ints1 = Base()
        ints2 = Base()
        ints3 = Base(10)
        ints4 = Base(5)
        ints5 = Base()

        self.assertEqual(ints1.id, 1)
        self.assertEqual(ints1.id, 2)
        self.assertEqual(ints1.id, 10)
        self.assertEqual(ints1.id, 5)
        self.assertEqual(ints1.id, 3)


if __name__ == '__main__':
    unittest.main()
