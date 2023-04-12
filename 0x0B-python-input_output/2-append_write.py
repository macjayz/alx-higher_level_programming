#!/usr/bin/python3
""" This function appends a string """


def append_write(filename="", text=""):
    """ This function appends text to a file """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
