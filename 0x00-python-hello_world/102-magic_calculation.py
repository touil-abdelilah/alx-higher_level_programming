#!/usr/bin/python3
def magic_calculation(a, b):
    result = 98  # LOAD_CONST 1 (98)
    result += a  # LOAD_FAST a, BINARY_ADD
    result **= b  # LOAD_FAST b, BINARY_POWER
    return result
