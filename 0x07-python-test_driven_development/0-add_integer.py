#!/usr/bin/python3
# Adds two numbers
"""Defines a function that adds integers."""


def add_integer(a, b=98):
    """Adds two integers together.

    Floats are converted to ints before adding.

    Raises an error if either input is not an int or float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("First input must be an integer or float")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("Second input must be an integer or float")
    return (int(a) + int(b))
