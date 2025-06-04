#!/usr/bin/python3
"""
Module containing functions serializing and deserializing XML data.
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serializes a dictionary as XML data to a file.
    """
    tree = ET.Element("data")
    for key in dictionary:
        child = ET.Element(key)
        child.text = str(dictionary[key])
        tree.append(child)

    string = ET.tostring(tree)
    with open(filename, 'wb') as f:
        f.write(string)


def deserialize_from_xml(filename):
    """
    Deserializes XML data into a dictionary.
    """
    tree = ET.parse(filename)
    root = tree.getroot()
    dictionary = {}

    for child in root:
        dictionary[child.tag] = child.text
    return dictionary
