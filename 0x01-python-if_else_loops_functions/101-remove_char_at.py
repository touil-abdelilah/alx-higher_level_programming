#!/usr/bin/python3
"""
A function that creates a copy of the string,
removing the character at the position n.
Args:
    source_str: The source string.
    position: The position of the character to remove.
Returns:
    The modified string with the character removed.
"""


def remove_char_at(str, n):
    """
    Create a copy of the string source_str
    and remove the character at the position position.
    """
    str_copy = ""
    for i in range(len(str)):
        if i == position:
            continue
        else:
            str_copy += str[i]
    return str_copy
