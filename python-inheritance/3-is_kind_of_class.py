#!/usr/bin/python3
"""Module that defines is_kind_of_class function"""


def is_kind_of_class(obj, a_class):
    """
    Checks if obj is an instance of a_class or a subclass of a_class.

    Args:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
        True if obj is an instance of a_class or a subclass, False otherwise.
    """
    return isinstance(obj, a_class)
