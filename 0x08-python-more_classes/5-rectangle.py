#!/usr/bin/python3
"""
This module defines a Rectangle class.
"""


class Rectangle:
    """ A class that represents a rectangle. """

    def __init__(self, width=0, height=0):
        """ The initializer method.
        Args:
            width (int): The width of the rectangle. Default is 0.
            height (int): The height of the rectangle. Default is 0.
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """ The width of the rectangle.
        Returns:
            int: The width.
        """

        return self.__width

    @width.setter
    def width(self, value):
        """ Set the width of the rectangle.
        Args:
            value (int): The new width.
        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than 0.
        """

        if not isinstance(value, int):
            raise TypeError("Width must be an integer.")
        if value < 0:
            raise ValueError("Width must be greater than or equal to 0.")
        self.__width = value

    # Height methods...

    def area(self):
        """ Calculate the area of the rectangle.
        Returns:
            int: The area.
        """

        return self.width * self.height

    def perimeter(self):
        """ Calculate the perimeter of the rectangle.
        Returns:
            int: The perimeter.
        """

        if self.width == 0 or self.height == 0:
            return 0

        return 2 * self.width + 2 * self.height

    def __str__(self):
        """ Return a string representation of the rectangle.
        Returns:
            str: A string of # characters representing the rectangle.
        """

        rectangle = ""

        if self.width == 0 or self.height == 0:
            return rectangle

        for i in range(self.height):
            rectangle += "#" * self.width + "\n"

        return rectangle[:-1]

    # __repr__ and __del__ methods...
