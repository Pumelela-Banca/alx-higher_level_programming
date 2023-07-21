#!/usr/bin/python3

"""
Tests for rectangle class and its methods
"""

import unittest

from models.rectangle import Rectangle


class TestSquare(unittest.TestCase):

    """test start"""
    def test_init(self):
        box = Rectangle(3, 4, 6, 3, 4)
        self.assertEqual(box.width, 3)

        self.assertEqual(box.id, 4)
        self.assertEqual(box.height, 4)
        self.assertEqual(box.x, 6)
        self.assertEqual(box.id, 4)

    """test setter"""
    def test_getter_setter(self):
        box = Rectangle(1, 2)
        self.assertEqual(box.width, 1)
        self.assertEqual(box.height, 2)


if __name__ == '__main__':
    unittest.main()