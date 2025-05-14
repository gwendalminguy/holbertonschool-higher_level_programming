#!/usr/bin/python3

"""
0-add_integer.py
Module containing a function adding two integers.
Returns an integer.
"""


def add_integer(a, b=98):
    """
    Adds two integers.
    Parameters: a (int) ; b (int)
    Return: int
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return int(a + b)
