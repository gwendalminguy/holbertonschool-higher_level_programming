#!/usr/bin/python3
"""
Module containing class CountedIterator.
"""


class CountedIterator:
    """
    A class to define a counted iterator.
    """
    def __init__(self, data):
        self.iterator = iter(data)
        self.counter = 0

    def __next__(self):
        self.counter += 1
        try:
            item = next(self.iterator)
        except StopIteration:
            raise
        else:
            return item

    def get_count(self):
        return self.counter
