#!/usr/bin/python3
"""Module that defines inherits_from function"""


def inherits_from(obj, a_class):
    """
    Checks if obj is an instance of a subclass of a_class
    (not the class itself).

    Args:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
        True if obj is an instance of a subclass of a_class, False otherwise.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
