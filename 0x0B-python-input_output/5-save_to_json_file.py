#!/usr/bin/python3
""" This writes json representation into a utf-8 text file"""
import json


def save_to_json_file(my_obj, filename):
    """ Writes to a text file """
    with open(filename, 'w', encoding="utf-8") as f:
        return json.dump(my_obj, f)
