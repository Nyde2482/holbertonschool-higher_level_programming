#!/usr/bin/python3
"""
Module 4-from_json_string: Returns an object represented by a JSON string.
"""
import json


def from_json_string(my_str):
    """
    Convert a JSON string to a Python object.

    Args:
        my_str (str): JSON string to decode.

    Returns:
        Any: Python object decoded from the JSON string.
    """
    return json.loads(my_str)
