#!/usr/bin/python3


def print_last_digit(number):
    """
    Print the last digit of a number.

    Args:
        number: The input number.

    Returns:
        The value of the last digit.
    """
    # Calculate the remainder whendividing by 10
    last_digit = abs(number) % 10
    print("{}".format(last_digit), end="")  # Print the last digit
    return last_digit  # Return the last digit
