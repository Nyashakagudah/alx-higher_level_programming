#!/usr/bin/python3
# safe_print_integer_err.py
# Import the sys module to access stderr

import sys
# Define a function that safely prints an integer value
def safe_print_integer_err(value):
    # Try to print the integer value to stdout
    try:
        print("{:d}".format(value))
        # Return True if successful
        return True
    # If an exception occurs, print the exception to stderr
    except Exception as e:
        print("Exception:{}".format(e),file = sys.stderr)
        # Return False if an exception occurs
        return False

