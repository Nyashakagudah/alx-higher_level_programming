#!/usr/bin/python3
# safe_function.py 
# Executes a function safely.

import sys


def safe_function(fct, *args):
    """Executes a function safely.

    Args:
        fct (function): The function to execute.
        *args: Arguments for fct.

    Returns:
        If an error occurs - None. 
        Otherwise - the result of the call to fct.
    """
    try:
        result = fct(*args)
        return (result)
    except:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)

