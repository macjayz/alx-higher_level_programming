#!/usr/bin/python3
"""this defines a class inherits from int"""


class MyInt(int):
    """Invert int operators == and !="""

    def __eq__(self, value):
        return self.real != value

    def __ne__(self, value):
        return self.real == value
