#!/usr/bin/python3
"""
1-my_list.py
Module containing class MyList.
"""


class MyList(list):
    """
    A class to define list methods.
    """
    def print_sorted(self):
        sorted = self.copy()
        sorted.sort()
        print(sorted)
