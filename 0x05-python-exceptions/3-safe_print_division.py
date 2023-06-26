#!/usr/bin/python3
# safe_division.py
# Calculates division of a by b, catching potential errors

def safe_print_division(num1, num2):
    """Returns the division of num1 by num2, or None if an error occurred."""
    try:
        result = num1 / num2
    except (TypeError, ZeroDivisionError):
        result = None
    finally:
        print(f"Result: {result}")
    return result

