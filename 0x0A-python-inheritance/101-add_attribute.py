#!/usr/bin/python3
"""this module defines a function that adds attributes to objects"""


def add_attribute(obj, att, value):
    """ This adds attribute
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
