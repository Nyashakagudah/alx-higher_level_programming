#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""
# Imports the BaseGeometry class from the 7-base_geometry module
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Represent a rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """
        # Validates the width using the parent class's integer_validator method
        super().integer_validator("width", width)
        self.__width = width
        # Validates the height using the parent class's integer_validator method
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return the area of the rectangle."""
        # Calculates the area by multiplying width and height
        return self.__width * self.__height

    def __str__(self):
        """Return the print() and str() representation of a Rectangle."""
        # Returns a string representation of the Rectangle in the format [Rectangle] width/height
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
