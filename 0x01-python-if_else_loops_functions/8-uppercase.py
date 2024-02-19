#!/usr/bin/python3

def uppercase(s):
    """
    Print a string in uppercase followed by a new line.

    Args:
        s: The input string.

    Returns:
        None
    """
    # Initialize an empty string to store the uppercase characters
    result = ""
    for char in s:
        # Convert lowercase letters to uppercase
        if ord('a') <= ord(char) <= ord('z'):
            uppercase_char = chr(ord(char) - (ord('a') - ord('A')))
        else:
            uppercase_char = char
        # Append each uppercase character to the result string
        result += uppercase_char
    # Print the entire string containing the uppercase characters
    print("{}".format(result), end="")
