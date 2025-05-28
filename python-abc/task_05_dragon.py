#!/usr/bin/python3
"""
Module containing class Dragon.
"""


class SwimMixin:
    """
    A class to define a creature.
    """
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """
    A class to define a creature.
    """
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    A class to define a dragon.
    """
    def roar(self):
        print("The dragon roars!")
