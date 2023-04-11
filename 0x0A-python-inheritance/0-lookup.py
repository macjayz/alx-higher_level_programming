#!/usr/bin/python3
""" This checks for available attributes """


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object
    """
    return dir(obj)
