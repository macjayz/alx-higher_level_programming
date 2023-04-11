#!/usr/bin/python3
""" This checks for available attributes """


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object
    """
    attrs = []
    for attr in dir(obj):
        # ignore private and special methods
        if not attr.startswith('__'):
            attrs.append(attr)
    return attrs
