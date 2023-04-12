#!/usr/bin/python3
""" This func. creates an obj from a json file"""
import json


def load_from_json_file(filename):
    """ we use open to read json file """
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
