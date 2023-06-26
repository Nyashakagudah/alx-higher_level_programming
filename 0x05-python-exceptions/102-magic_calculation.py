#!/usr/bin/python3
# Defines a function that performs a "magic calculation"
def magic_calculation(a, b):
# Initializes result variable
    result = 0
# Loop runs 1-2 times
    for i in range(1, 3):
# Tries to raise an exception if i is greater than a
        try:
            if i > a:
                raise Exception('Too far')
# Calculates (a ** b) / i and adds to result
            result += (a ** b) / i
        except:
# If exception is raised, sets result to b + a and breaks loop
            result = b + a
            break
    return result # Returns final result

