#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    if value not in a_dictionary.values():
        return a_dictionary
    list = []
    for key in a_dictionary.keys():
        if value == a_dictionary[key]:
            list.append(key)

    if len(list) > 0:
        for key in list:
            a_dictionary.pop(key)

    return a_dictionary
