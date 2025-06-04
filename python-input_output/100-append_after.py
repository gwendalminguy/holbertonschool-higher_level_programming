#!/usr/bin/python3
"""
100-append_after.py
Module containing function to insert a line after a given string in a text.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line after every occurence of a given string in a text.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        new = ""
        line = f.readline()
        while line != "":
            new += line
            if search_string in line:
                new += new_string
            line = f.readline()

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(new)
