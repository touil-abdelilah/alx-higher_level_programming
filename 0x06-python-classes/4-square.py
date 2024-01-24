#!/usr/bin/python3
"""Square Module"""


class Square:
    """Class that defines a square by its size."""

    def __init__(self, size=0):
        """Initialization method with optional size."""
        self.size = size

    @property
    def size(self):
        """Getter method to retrieve the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method to set the size."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Method to calculate the area of the square."""
        return self.__size ** 2
