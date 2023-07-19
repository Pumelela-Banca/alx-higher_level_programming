#!/usr/bin/python3

"""
Tests for square class and its methods
"""

import unittest

from models.square import Square


class TestSquare(unittest.TestCase):

    """test start"""
    def test_init(self):
        box = Square(4, 6, 3)
        self.assertEqual(box.size, 4)
        self.assertEqual(box.id, 5)
        self.assertEqual(box.x, 6)


if __name__ == '__main__':
    unittest.main()