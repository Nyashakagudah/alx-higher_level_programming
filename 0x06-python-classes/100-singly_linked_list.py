#!/usr/bin/python3
# prints_int_or_err.py  
# Prints an integer or error message

import sys


def safe_print_integer_err(value):
    """Prints an integer or error message to stderr.

    Prints the integer using "{:d}".format() and returns True.
    If a ValueError occurs, prints the exception message to stderr 
    and returns False.

    Args:
        value (int): The integer to print.

    Returns:
        True if the integer is printed, False otherwise.
    """
    try:
        print("{:d}".format(value))
        return True
    except ValueError:
        print("ValueError: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return False

