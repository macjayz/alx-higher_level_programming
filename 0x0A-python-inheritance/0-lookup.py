#!/usr/bin/python3
""" This checks for available attributes """


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object
    """
    attrs = []
    for attr in dir(obj):
        attrs.append(attr)
    return attrs
