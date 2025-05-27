#!/usr/bin/python3
"""
Module containing...
"""


class VerboseList(list):
    """
    A class...
    """
    def append(self, item):
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, item):
        super().extend(item)
        print("Extended the list with [{}] item.".format(len(item)))

    def remove(self, item):
        super().remove(item)
        print("Removed [{}] from the list.".format(item))

    def pop(self, index=-1):
        index = super().pop(index)
        print("Popped [{}] from the list.".format(index))
        return index
