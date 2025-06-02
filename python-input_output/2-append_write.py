#!/usr/bin/python3
"""
2-append_write.py
Module containing function to append text to a file.
"""


def append_write(filename="", text=""):
    """
    Function appending text to a file.
    """
    with open(filename, 'a', encoding="utf-8") as f:
        written_data = f.write(text)

    return written_data
