#!/usr/bin/python3

"""
4-print_square.py
Module containing a function printing a square.
"""


def print_square(size):
    """
    Prints a square.

    Parameters:
    size (int): size of the square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
