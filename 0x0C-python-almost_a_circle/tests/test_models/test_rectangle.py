#!/usr/bin/python3

"""
Tests for rectangle class and its methods
"""

import unittest

from test_models.rectangle import Rectangle


class TestSquare(unittest.TestCase):

    """test start"""
    def test_init(self):
        box = Rectangle(3, 4, 6, 3)
        self.assertEqual(box.width, 3)
        self.assertEqual(box.id, 1)
        self.assertEqual(box.height, 4)
        self.assertEqual(box.x, 6)

    # Tests exception


if __name__ == '__main__':
    unittest.main()