#!/usr/bin/python3
""" Defines a square """


class Square:
    """ Define a constructor """
    def __init__(self, size=0):
        """ initialize square class """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = size

    def area(self):
        return self.__size * self.__size
