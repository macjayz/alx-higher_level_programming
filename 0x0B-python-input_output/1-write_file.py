#!/usr/bin/python3
""" This function writes to file """


def write_file(filename="", text=""):
    """This writes to file"""
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
