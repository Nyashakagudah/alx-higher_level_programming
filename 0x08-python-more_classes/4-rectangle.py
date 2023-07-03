#!/usr/bin/python3
"""
This is the "Rectangle"  module.

This module provides a Rectangle class.
"""


class Rectangle:
    """A Rectangle class with attributes width and height, and
    methods to calculate area and perimeter.
    """
    def __init__(self, width=0, height=0):
        """Initialize width and height attributes"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width, validating that it is a positive integer"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height, validating that it is a positive integer"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __repr__(self):
        """Return a string representation of the rectangle"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __str__(self):
        """Retrn string reprsentation the rectangle using # characters"""
        total = ""
        for i in range(self.__height):
            total += ("#" * self.__width)
            if i is not self.__height - 1:
                total += "\n"
        return total

    def area(self):
        """Calculate and return the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle"""
        if self.__width is 0 or self.__height is 0:
            return 0
        3return (2 * self.__width) + (2 * self.__height)
