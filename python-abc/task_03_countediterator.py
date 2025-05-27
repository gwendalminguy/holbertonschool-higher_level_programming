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
        self.length = len(data)

    def __next__(self):
        self.counter += 1
        if self.length >= self.counter:
            item = next(self.iterator)
            return item
        else:
            raise StopIteration

    def get_count(self):
        return self.counter
