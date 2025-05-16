#!/usr/bin/python3
"""
Module containing a function finding the maximum integer in a list.
"""


def max_integer(list=[]):
    """
    Finds the maximum integer in a list of integers.

    Parameters:
    list (list): list of integers

    Return: maximum integer
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result
