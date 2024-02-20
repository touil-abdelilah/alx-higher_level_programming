#!/usr/bin/python3
def magic_calculation(a, b, c):
    """
    Perform a magic calculation based on the values of a, b, and c.

    Args:
        a (int): The first operand.
        b (int): The second operand.
        c (int): The third operand.

    Returns:
        int: The result of the magic calculation.
    """
    if a < b:
        return c
    elif b > c:
        return a + b
    else:
        return a * b - c
