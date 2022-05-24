#!/usr/bin/env python

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    _, make, year = line.split(',')
    year = year.strip()
    print('%s,%s,%s' % (make, year, 1))