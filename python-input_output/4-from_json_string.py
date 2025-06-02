#!/usr/bin/python3
"""
4-from_json_string.py
Module containing function to create an object from a JSON.
"""
import json


def from_json_string(my_str):
    """
    Function creating an object from a JSON from an object.
    """
    return json.loads(my_str)
