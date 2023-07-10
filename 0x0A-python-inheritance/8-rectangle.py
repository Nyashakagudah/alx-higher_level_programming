#!/usr/bin/python3
"""Defines rectangle instance that inherits from super class."""
# Changed to: Defines a Rectangle class that inherits from BaseGeometry

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """create new class instance."""
    # Changed to: Defines a Rectangle class

    def __init__(self, width, height):
        """Intialize a new Rectangle instance

        Args:
            width (int)
            height (int)
        """
        # Changed to: Initialize a new Rectangle
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

