#!/usr/bin/python3

"""
module contains a base class tests matching
given questions
"""

import unittest

from models import Base


class TestSquare(unittest.TestCase):
    """test id track"""
    def test_ids(self):
        r1 = Base(10, 2)
        self.assertEqual(r1.id, 1)

        r2 = Base(2, 10)
        self.assertEqual(r2.id, 2)

        r3 = Base(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)
