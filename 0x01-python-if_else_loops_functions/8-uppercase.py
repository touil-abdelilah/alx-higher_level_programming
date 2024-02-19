#!/usr/bin/python3

def uppercase(s):
    """
    Print a string in uppercase followed by a new line.

    Args:
        s: The input string.

    Returns:
        None
    """
    result = ""  # Initialize an empty string to store the uppercase characters
    for char in s:
        # Convert lowercase letters to uppercase
        if ord('a') <= ord(char) <= ord('z'):
            uppercase_char = chr(ord(char) - (ord('a') - ord('A')))
        else:
            uppercase_char = char
        result += uppercase_char  # Append each uppercase character to the result string
    print(result)  # Print the entire string containing the uppercase characters

