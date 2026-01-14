#!/usr/bin/python3
def uppercase(str):
    """Convert a lowercase character to uppercase.

    Args:
        c (str): A single character string.
    Returns:
        str: The uppercase equivalent if c is lowercase,
        else returns c unchanged.
    """
    for c in str:
        print("{}".format(
            chr(ord(c) - 32) if ord(c) >= 97 and ord(c) <= 122 else c
        ), end="")
    print()
