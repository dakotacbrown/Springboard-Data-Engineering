#!/usr/bin/env python

import sys
from collections import defaultdict

"""
Takes sorted input from a mapper.
Captures and parses information.
Stores relevant information in a dictionary
    to be able to increment counter variable.
Loops through dictionary and
    sends that information to stdout.
"""
  
make = None
year = 0
counter = 0
diction = defaultdict(int)
    
for line in sys.stdin:
    
    make, year, counter = line.split(",")
    counter = counter.strip()
    makeYear = make + ',' + year
    diction[makeYear] += int(counter)

for k, v in diction.items():
    print(k+','+str(v))