#!/usr/bin/python3
"""Module 2-append_write: Appends text to a file (UTF8)."""


def append_write(filename="", text=""):
    """
    Appends text to a file.
    Args:
        filename (str): The name of the file to append to.
        text (str): The text to append to the file.
    Returns:
        int: The number of characters written.
    """
    with open(filename, "a") as file:
        return file.write(text)
