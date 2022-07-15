#!/usr/bin/env python

import sys

"""
Takes sorted input from a mapper.
Captures and parses only relevant information.
Stores relevant information in a dictionary
    and checks to see if the incident_type is not R.
Checks if the incident_type A exists in dictionary 
    and sends that information to flush.  
Sends that information to flush then to stdout.
"""

vin_number = None
incident_type = None
make = None
year = 0
diction = {}

def flush(vin_number, make, year):
    print('%s,%s,%s' % (vin_number, make, year))
    
for line in sys.stdin:
    
    vin_number, incident_type, make, year = line.split(",")
    year = year.strip()
    
    if vin_number not in diction:
        diction[vin_number] = []
        if incident_type not in 'R':
            if incident_type in 'I':
                diction[vin_number].append(incident_type)
                diction[vin_number].append(make)
                diction[vin_number].append(year)

            else:
                diction[vin_number].append(incident_type)
    else:
        if incident_type not in 'R':
            if incident_type in 'I':
                diction[vin_number].append(incident_type)
                diction[vin_number].append(make)
                diction[vin_number].append(year)
            else:
                diction[vin_number].append(incident_type)

for key, values in diction.items():
    if 'A' in values:
        flush(key, values[2], values[3])