#!/usr/bin/python3
# Import the sys module to access stderr
import sys
# Define a safe_function() that executes another function safely
def safe_function(fct, *args):
    # Try executing the function fct with arguments args
    try:
        result = fct(*args)
        # If no exception, return the result
        return result
    # Catch any exceptions
    except Exception as e:
        # Print the exception to stderr
        print("Exception:", e, file=sys.stderr)
        # Return None if an exception occurs
        return None

