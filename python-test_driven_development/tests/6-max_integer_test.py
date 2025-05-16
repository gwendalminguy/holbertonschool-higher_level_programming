#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_integers(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([-1, -2, -3]), -1)

    def test_none(self):
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_no_argument(self):
        self.assertEqual(max_integer(), None)

    def test_too_many(self):
        with self.assertRaises(TypeError):
            max_integer([1, 2], [1, 2])
