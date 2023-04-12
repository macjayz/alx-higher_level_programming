#!/usr/bin/python3
""" This function inserts a line of text to a file """


def append_after(filename, search_string, new_string):
    """Inserts text after a given string in a file is found."""
    with open(filename, 'r+') as f:
        lines = f.readlines()
        f.seek(0)
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
        f.truncate()
