#!/usr/bin/python3
# Prints integers from a list

def safe_print_list_integers(my_list=[], x=0):
    """Prints the first x integers from a list.

    Args:
        my_list (list): The list to print from.
        x (int): The max number of integers to print.

    Returns:
        The number of integers printed.
    """
    ret = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            ret += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (ret)

