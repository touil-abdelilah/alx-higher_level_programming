#!/usr/bin/python3
"""
 a function that creates a copy of the string,
 removing the character at the position n
 Args:
    str: the source string
    n:the removed character position
Functions:
    remove_char_at(str,n):crate a copy of the string str
    and remove the character at n
"""


def remove_char_at(str, n):
    str_copy = ""
    for i in range(len(str)):
        if i == n:
            continue
        else:
            str_copy += str[i]
    return(str_copy)
