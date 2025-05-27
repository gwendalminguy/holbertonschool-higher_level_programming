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
        try:
            item = next(self.iterator)
            self.counter += 1
            return item
        except StopIteration:
            raise

    def get_count(self):
        return self.counter
