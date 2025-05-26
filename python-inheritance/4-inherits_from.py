#!/usr/bin/python3
"""
Module containing the function inherits_from.
"""


def inherits_from(obj, a_class):
    """
    Checks if an object inherits from a class.
    """
    if type(obj) is a_class:
        return False

    return isinstance(obj, a_class)
