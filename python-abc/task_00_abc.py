#!/usr/bin/python3
"""
Module containing class Animal and subclasses Dog and Cat.
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """
    A class to define an animal.
    """
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """
    A class to define a dog.
    """
    def sound(self):
        return "Bark"


class Cat(Animal):
    """
    A class to define a cat.
    """
    def sound(self):
        return "Meow"
