#!/usr/bin/python3
""" this reads stdin line by line """
import sys


def print_stats(size, status_codes):
    """Print accumulated metrics
    """
    print("File size: {}".format(size))
    for key in sorted(status_codes):
        print("{}: {}".format(key, status_codes[key]))

if __name__ == "__main__":
    size = 0
    status_codes = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']

    for line in sys.stdin:
        line = line.split()

        try:
            size += int(line[-1])
        except (IndexError, ValueError):
            pass

        try:
            if line[-2] in valid_codes:
                status_codes[line[-2]] = status_codes.get(line[-2], 0) + 1
        except IndexError:
            pass

    print_stats(size, status_codes)
