#!/usr/bin/python3
"""
Module containing class Square.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class to define a square.
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__width = size
        self.__height = size

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        return self.__width * self.__height
