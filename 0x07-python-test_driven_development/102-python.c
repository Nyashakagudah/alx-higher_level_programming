/*
 * File: 102-python.c
 * Prints information about Python string objects.
 */

#include "Python.h"

/**
 * print_python_string - Prints information about a Python string object.
 * @p: A PyObject representing a Python string.
 */
void print_python_string(PyObject *p)
{
    long int length;

    fflush(stdout);

    printf("[.] String object info\n");

    // Check if p is actually a string object.
    if (strcmp(p->ob_type->tp_name, "str") != 0)
    {
        printf("  [ERROR] Invalid String Object\n");
        return;
    }

    // Get the string length.
    length = ((PyASCIIObject *)(p))->length;

    // Print the string type.
    if (PyUnicode_IS_COMPACT_ASCII(p))
        printf("  Type: Compact ASCII\n");
    else
        printf("  Type: Compact Unicode\n");

    // Print the string length.
    printf("  Length: %ld\n", length);

    // Print the string value.
    printf("  Value: %ls\n", PyUnicode_AsWideCharString(p, &length));
}
