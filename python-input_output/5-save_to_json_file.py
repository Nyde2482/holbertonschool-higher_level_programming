#!/usr/bin/python3
"""Module 5-save_to_json_file: Saves an object to a JSON file."""
import json


def save_to_json_file(my_obj, filename):
    """
    Saves an object to a JSON file.
    Args:
        my_obj: The object to save to the file.
        filename (str): The name of the file to save to.
    """
    with open(filename, "w+") as file:
        json.dump(my_obj, file)
