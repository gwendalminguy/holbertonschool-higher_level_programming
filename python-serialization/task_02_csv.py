#!/usr/bin/python3
"""
Module containing function converting CSV file to JSON file.
"""
import csv
import json


def convert_csv_to_json(filename):
    """
    Converts data from a CSV file to a JSON file.
    """
    new_list = []
    export = "data.json"
    try:
    	with open(filename, newline='') as f:
        	DR = csv.DictReader(f)
        	for line in DR:
                new_list.append(line)
    except FileNotFoundError:
        return False

    result = json.dumps(new_list, indent=4)

    with open(export, 'w', encoding='utf-8') as f:
        f.write(result)

    return True
