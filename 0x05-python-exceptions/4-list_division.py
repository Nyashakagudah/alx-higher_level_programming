#!/usr/bin/python3
# Divides two lists element by element.

def list_division(list1, list2, length):
    """Divides two lists element by element.

    Args:
        list1 (list): The first list.
        list2 (list): The second list.
        length (int): The number of elements to divide.

    Returns:
        A new list of length length containing the divisions.
    """
    result = []
    for i in range(length):
        try:
            div = list1[i] / list2[i]
        except TypeError:
            print("Incompatible types")
            div = 0
        except ZeroDivisionError:
            print("Division by zero")
            div = 0
        except IndexError:
            print("List index out of range")
            div = 0
        finally:
            result.append(div)
    return result

