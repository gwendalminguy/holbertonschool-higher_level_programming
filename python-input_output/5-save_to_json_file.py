#!/usr/bin/python3
"""
5-save_to_json_file.py
Module containing function to write an object as a JSON to a file.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Function writing an object as a JSON to a file.
    """
    string = json.dumps(my_obj)
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(string)
