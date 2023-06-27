#!/usr/bin/python3
"""Square module.  
This module contains a class that defines a square and initializes it with a size,  
checking that the input is valid. There is also an area method that calculates the area of the square.
"""


class Square():
    """Defines a square."""

    def __init__(self, size=0):
        """Initializes the Square object with a size.
        Args:
            size (int): The length of one side of the square.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if type(size) is int:
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("Size must be greater than or equal to 0.")
        else:
            raise TypeError("Size must be an integer.")

    def area(self):
        """Calculates and returns the area of the square."""
        return self.__size ** 2

