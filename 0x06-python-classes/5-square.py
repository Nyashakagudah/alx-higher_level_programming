#!/usr/bin/python3
"""Square module.  
This module contains a class that defines a square, its size,  
and methods to set, get, calculate area, and print the square.
"""


class Square():
    """Defines a square with size and methods."""

    def __init__(self, size=0): 
        """Constructor to initialize square with size."""
        self.size = size

    @property
    def size(self):
        """Get or set the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation."""
        if type(value) is int:
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("Size must be >= 0")
        else:
            raise TypeError("Size must be an integer")

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with # characters based on size."""
        if self.__size > 0:
            for x in range(self.__size):
                print('#' * self.__size)
        else:
            print()

