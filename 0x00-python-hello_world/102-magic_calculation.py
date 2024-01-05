#!/usr/bin/python3
def magic_calculation(a, b):
    result = 98                # LOAD_CONST 1 (98)
    result = (result ** a)     # LOAD_FAST a, BINARY_POWER
    result += b                # LOAD_FAST b, BINARY_ADD
    return result              # RETURN_VALUE
def magic_calculation(9,5)
