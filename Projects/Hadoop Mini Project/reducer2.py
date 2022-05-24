#!/usr/bin/env python

import sys
from collections import defaultdict
  
make = None
year = 0
counter = 0
diction = defaultdict(int)
    
for line in sys.stdin:
    
    make, year, counter = line.split(",")
    counter = counter.strip()
    my = make + ',' + year
    diction[my] += int(counter)

for k, v in diction.items():
    print(k+','+str(v))