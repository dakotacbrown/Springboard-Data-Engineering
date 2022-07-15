#!/usr/bin/env python

import sys

"""
Takes in input from a file.
Captures and parses only relevant information.
Sends that information to stdout.
"""
for line in sys.stdin:
    _, incident_type, vin_number, make, _, year, _, _ = line.split(',')
    print('%s,%s,%s,%s' % (vin_number, incident_type, make, year))