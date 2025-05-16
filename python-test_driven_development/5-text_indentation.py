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

    new = ""

    for i in text:
        new += i
        if i in ".:?":
            print("{}".format(new.strip()), end="\n\n")
            new = ""

    if new.strip() != "":
        print("{}".format(new.strip()), end="")
