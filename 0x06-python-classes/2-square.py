#!/usr/bin/python3
"""Square class definition.  
This module contains a class that defines a square and init method that
sets its size and checks if the given values are valid. There's also an
area method that calculates the area of the square.
"""


class Square():
    """Defines a square object."""

    def __init__(self, size=0):
        """Initializes the necessary attributes for the Square object.
        Args:
            size (int): Length of one side of the square.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("Size must be greater than or equal to 0.")
        else:
            raise TypeError("Size must be an integer.")

    def area(self):
        """Calculates the area of the current square."""
        return self.__size ** 2 

