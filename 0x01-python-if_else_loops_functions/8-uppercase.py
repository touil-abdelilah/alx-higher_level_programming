#!/usr/bin/python3


def uppercase(s):
    """
    print a string in uppercase fllowed by a new line.

   Args:
        str: The iput string.

    Returns:
        None
    """
    for char in s:
        # convert lowercase letters to uppsercase
        if ord('a') <= ord(char) <= ord('z'):
            uppercase = chr(ord(char) - (ord('a') - ord('A')))
        else:
            uppercase = char
        # print each character without newline
        print("{}".format(uppercase), end="")
    # print newline
    print("\n")
