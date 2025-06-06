#!/usr/bin/python3
"""
9-student.py
Module containing class Student.
"""


class Student:
    """
    A class to define a student.
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
