#!/usr/bin/env python

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    _, incident_type, vin_number, make, _, year, _, _ = line.split(',')
    print('%s,%s,%s,%s' % (vin_number, incident_type, make, year))