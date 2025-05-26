#!/usr/bin/python3
"""
2-is_same_class.py
Mudule containing the function is_same_class.
"""


def is_same_class(obj, a_class):
    """
    Checks if an object is exactly an instance of a class.
    """
    if type(obj) == a_class:
        return True

    return False
