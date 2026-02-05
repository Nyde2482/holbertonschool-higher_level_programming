#!/usr/bin/python3
"""module : this function returns the list of available
attributes and methods of an object"""


def lookup(obj):
    """
    Returns a list of attributes and methods of the given object.
    Args:
        obj: The object to inspect.
    Returns:
        List of attribute and method names (as strings).
    """
    return dir(obj)
