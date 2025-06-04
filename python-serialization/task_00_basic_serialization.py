#!/usr/bin/python3
"""
Module containing functions to serialize and deserialize data.
"""
import json


def serialize_and_save_to_file(data, filename):
    """
    Serializes and saves data to a file.
    """
    string = json.dumps(data)
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(string)


def load_and_deserialize(filename):
    """
    Deserializes data from a file.
    """
    with open(filename, 'r', encoding="utf-8") as f:
        string = json.loads(f.read())

    return string
