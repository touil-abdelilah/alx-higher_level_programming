#!/usr/bin/python3
""" This is square module"""


class Square:
    """Class that defines a square by its size."""

    def __init__(self, size=0):
        """Initialization method with optional size."""
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
