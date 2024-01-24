#!/usr/bin/python3
""" Square Module """


class Square:
    """Class that defines a square by its size."""

    def __init__(self, size=0):
        """Initialization method with optional size."""
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Method to calculate the area of the square."""
        return self.__size ** 2
