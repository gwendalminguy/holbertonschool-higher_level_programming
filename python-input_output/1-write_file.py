#!/usr/bin/python3
"""
1-write_file.py
Module containing function to write to a file.
"""


def write_file(filename="", text=""):
    """
    Function writing text to a file.
    """
    with open(filename, 'w', encoding="utf-8") as f:
        written_data = f.write(text)

    return written_data
