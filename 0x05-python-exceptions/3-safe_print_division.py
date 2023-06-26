#!/usr/bin/python3
# safe_division.py

def safe_print_division(a, b):
    '''
    Divide two integers and print the result, using except to catch zero division error
    '''
    try:
        result = a/b
    except:
        result = None
    finally:
        print("The result is: {}".format(result))
        return result

