#!/usr/bin/python3

"""
5-text_indentation.py
Module containing a function changing some text.
"""


def text_indentation(text):
    """
    Adding blank lines in some text.

    Parameters:
    text (str): text to change
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new = text.replace(". ", ".").replace("? ", "?").replace(": ", ":")

    for i in new:
        if i == '.' or i == '?' or i == ':':
            print("{}\n".format(i))
        else:
            print("{}".format(i), end="")
