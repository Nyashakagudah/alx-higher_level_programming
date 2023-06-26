#!/usr/bin/python3
# Prints an integer safely

def safe_print_integer(value):
    """Prints an integer using string formatting.

    Args:
        value (int): The integer to print.

    Returns:
        bool: True if the integer is printed successfully, False otherwise.
    """
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        return False

