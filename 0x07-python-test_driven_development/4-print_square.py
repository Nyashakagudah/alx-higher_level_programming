#!/usr/bin/python3
# Prints a square of # characters
"""Defines a function that prints a square."""


def print_square(size):
    """Prints a square of # characters.

    Args:
        size (int): The height and width of the square.
    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for y in range(size):   # Loop to print rows
        [print("#", end="") for k in range(size)]  # Loop to print columns
        print("")   # Print newline at end of row
