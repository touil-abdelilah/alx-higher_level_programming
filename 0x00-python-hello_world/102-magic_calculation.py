#!/usr/bin/python3
"""def magic_calculation(a, b):
    result = 98                # LOAD_CONST 1 (98)
    result = (result ** a)     # LOAD_FAST a, BINARY_POWER
    result += b                # LOAD_FAST b, BINARY_ADD
    return result              # RETURN_VALUE"""
def magic_calculation(a, b):
    print("3           0 LOAD_CONST               1 (98)")
    print("              3 LOAD_FAST                0 (a)")
    print("              6 LOAD_FAST                1 (b)")
    print("              9 BINARY_POWER")
    print("             10 BINARY_ADD")
    print("             11 RETURN_VALUE")

    # Perform the actual calculation
    result = 98
    result = (result ** a)
    result += b
    return result
