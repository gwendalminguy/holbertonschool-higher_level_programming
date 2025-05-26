#!/usr/bin/python3
"""
1-my_list.py
Module containing ...
"""


class MyList(list):
    def print_sorted(self):
        sorted = self.copy()
        sorted.sort()
        print(sorted)
