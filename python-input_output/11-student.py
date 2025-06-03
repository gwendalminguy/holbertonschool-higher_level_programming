#!/usr/bin/python3
"""
11-student.py
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

    def to_json(self, attrs=None):
        if not isinstance(attrs, list):
            return self.__dict__

        for element in attrs:
            if not isinstance(element, str):
                return self.__dict__

        dictionary = {}
        if "first_name" in attrs:
            dictionary["first_name"] = self.first_name
        if "last_name" in attrs:
            dictionary["last_name"] = self.last_name
        if "age" in attrs:
            dictionary["age"] = self.age
        return dictionary

    def reload_from_json(self, json):
        self.first_name = json['first_name']
        self.last_name = json['last_name']
        self.age = json['age']
