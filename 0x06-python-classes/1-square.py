#!/usr/bin/python3
"""Square class definition.  
This module contains a class that defines a square and initializes its size.
"""


class Square():
    """Defines a square shape."""

    def __init__(self, size):
        """Initializes the necessary attributes for the Square object.
        
        Args:
            size (int): Length of one side of the square.
        """
        self.__size = size  # Private attribute for square size

