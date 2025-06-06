#!/usr/bin/python3
"""
Module containing class CustomObject.
"""
import pickle


class CustomObject:
    """
    Class defining a custom object.
    """
    def __init__(self, name=None, age=None, is_student=None):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print("Name: {}".format(self.name), \
        "Age: {}".format(self.age), \
        "Is Student: {}".format(self.is_student), \
        sep="\n")

    def serialize(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self.__dict__, f)

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, 'rb') as f:
                obj = pickle.load(f)
        except FileNotFoundError:
            return None
        except EOFError:
            return None
        else:
            return cls(**obj)
