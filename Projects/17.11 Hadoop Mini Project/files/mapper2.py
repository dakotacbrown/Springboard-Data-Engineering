#!/usr/bin/env python

import sys

"""
Takes in input from a reducer.
Captures and parses only relevant information.
Sends that information to stdout.
"""
for line in sys.stdin:
    _, make, year = line.split(',')
    year = year.strip()
    print('%s,%s,%s' % (make, year, 1))