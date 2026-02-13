#!/usr/bin/python3
"""
Module that converts a class instance to a JSON-serializable dictionary.

This module provides a function to return the dictionary description
with simple data structure (list, dictionary, string, integer and boolean)
for JSON serialization of an object.
"""


def class_to_json(obj):
    """
    Returns the dictionary description of an object for JSON serialization.

    Args:
        obj: An instance of a Class with serializable attributes.

    Returns:
        dict: A dictionary containing all attributes of the object.
    """
    return obj.__dict__
