#!/usr/bin/python3


def islower(c):
    """
    Check if a character is lowercase.

    Args:
        c: A character (string of length 1).

    Returns:
        True if c is lowercase, False otherwise.
    """
    # Check if the ASCII value of the character
    # is within the range of lowercase letters
    return ord(c) >= ord('a') and ord(c) <= ord('z')
