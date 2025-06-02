#!/usr/bin/python3
"""
3-to_json_string.py
Module containing function to create a JSON from an object.
"""
import json


def to_json_string(my_obj):
    """
    Function creating a JSON from an object.
    """
    return json.dumps(my_obj)
