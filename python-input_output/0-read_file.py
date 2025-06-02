#!/usr/bin/python3
"""
0-read_file.py
Module containing function to read a file.
"""


def read_file(filename=""):
    """
    Function reading a file and printing its content.
    """
    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.readline()
        while read_data != "":
            print(read_data, end="")
            read_data = f.readline()
