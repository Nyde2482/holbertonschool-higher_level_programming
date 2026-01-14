#!/usr/bin/python3
def islower(c):
    """Check if a character is lowercase.

    Args:
        c (str): A single character string.
    Returns:
        bool: True if c is lowercase, False otherwise.
    """
    if 97 <= ord(c) <= 122:
        return True
    else:
        return False
