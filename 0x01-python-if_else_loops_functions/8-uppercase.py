#!/usr/bin/python3


def uppercase(s):
    """
    Print a string in uppercase followed by a new line.

    Args:
        s: The input string.

    Returns:
        None
    """
    for char in s:
        # Convert lowercase letters to uppercase
        if ord('a') <= ord(char) <= ord('z'):
            uppercase_char = chr(ord(char) - (ord('a') - ord('A')))
        else:
            uppercase_char = char
        # Print each character without newline
        print("{}".format(uppercase_char), end="")
    # Print newline after printing the entire string in uppercase
