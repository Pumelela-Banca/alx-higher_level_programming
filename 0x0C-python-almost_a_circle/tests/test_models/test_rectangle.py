#!/usr/bin/python3

"""
Tests for rectangle class and its methods
"""

import unittest

from models import Rectangle


class TestSquare(unittest.TestCase):

    """test start"""
    def test_init(self):
        box = Rectangle(3, 4, 6, 3)
        self.assertEqual(box.width, 3)
        self.assertEqual(box.id, 1)
        self.assertEqual(box.height, 4)
        self.assertEqual(box.x, 6)
        self.assertEqual(box.x, 3)

    # Tests exception
