#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    if key not in a_dictionary.keys():
        return a_dictionary
    else:
        a_dictionary.pop(key)
        return a_dictionary
