#!/usr/bin/python3
""" a function checks for instance """


def inherits_from(obj, a_class):
    """ This checks for instance """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
