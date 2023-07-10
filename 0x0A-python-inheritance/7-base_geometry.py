#!/usr/bin/python3

class BaseGeometry:
    def area(self):
        raise Exception("Implement in child class")

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError("Must be int")
        if value <= 0:
            raise ValueError("Must be > 0")
