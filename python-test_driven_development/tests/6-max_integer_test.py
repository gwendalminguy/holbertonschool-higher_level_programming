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

    def test_large(self):
        self.assertEqual(max_integer([10, 10e1000, 10e1000 + 1]), 10e1000 + 1)
        self.assertEqual(max_integer([10, -10e1000, 0]), 10)

    def test_floats(self):
        self.assertEqual(max_integer([1.5, 2.5, 3.5]), 3.5)
        self.assertEqual(max_integer([-1.5, -2.5, -3.5]), -1.5)

    def test_mix(self):
        self.assertEqual(max_integer([1.5, -2, 3.5]), 3.5)
        self.assertEqual(max_integer([-1.5, 2.5, -3.5]), 2.5)

    def test_same_multiple(self):
        self.assertEqual(max_integer([5, 5, 10, 5, 5]), 10)
        self.assertEqual(max_integer([5, 5, -10, 5, 5]), 5)

    def test_infinity(self):
        self.assertEqual(max_integer([1, float('inf')]), float('inf'))
        self.assertEqual(max_integer([1, float('-inf')]), 1)

    def test_tuple(self):
        self.assertEqual(max_integer((1, 2, 3)), 3)

    def test_set(self):
        with self.assertRaises(TypeError):
            max_integer({1, 2, 3})

    def test_dictionary(self):
        with self.assertRaises(KeyError):
            max_integer({"one": 1, "two": 2, "three": 3})

    def test_none(self):
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_no_argument(self):
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer([]), None)

    def test_too_many(self):
        with self.assertRaises(TypeError):
            max_integer([1, 2], [1, 2])

    def test_string(self):
        self.assertEqual(max_integer("Hello"), 'o')

    def test_characters(self):
        self.assertEqual(max_integer(['H', 'e', 'l', 'l', 'o']), 'o')
