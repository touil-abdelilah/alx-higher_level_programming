#!/usr/bin/python3
"""
Module for MagicClass.
"""


import math


class MagicClass:
    """Class that defines a magic circle with radius """

    def __init__(self, radius=0):
        """Initialize the MagicClass instance with a given rd."""
        self.__radius = 0

        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')

        self.__radius = radius

    def area(self):
        """Calculate and return the area of the magic circle. Returns float."""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Calculate and return the circumference of the magic circle"""
        return 2 * math.pi * self.__radius
