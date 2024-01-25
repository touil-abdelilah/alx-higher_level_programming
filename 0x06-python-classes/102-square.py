#!/usr/bin/python3
"""square module"""


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
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Method to calculate the area of the square."""
        return self.__size ** 2

    def __eq__(self, other):
        """Equality comparison based on area."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Inequality comparison based on area."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Less than comparison based on area."""
        return self.area() < other.area()

    def __le__(self, other):
        """Less than or equal comparison based on area."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Greater than comparison based on area."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Greater than or equal comparison based on area."""
        return self.area() >= other.area()
