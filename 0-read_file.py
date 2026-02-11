#!/usr/bin/python3
"""Module 0-read_file: Reads and prints the content of a text file (UTF8)."""


def read_file(filename=""):
    """
    Reads a text file and prints it to stdout
    Args:
        filename (str): The name of the file to read.
    """
    with open(filename, "r") as file:
        print(file.read(), end="")
