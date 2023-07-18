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
        r1 = Base(10)
        self.assertEqual(r1.id, 10)

        r2 = Base(2)
        self.assertEqual(r2.id, 2)
