#!/usr/bin/python3
# safe_print_integer_err.py
# Prints an integer and handles errors

import sys


def safe_print_integer_err(value):
    """Prints an integer and handles errors.

    Prints an integer with "{:d}".format().
    If a ValueError occurs, prints an error message to stderr.

    Args:
        value (int): The integer to print.

    Returns:
        True if the integer is printed, False otherwise.
    """
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError) as err:
        print(f"Error: {err}", file=sys.stderr)
        return False

