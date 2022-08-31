#!/usr/bin/env python3

import sys
from bed_parser import parse_bed
#imports the function parse_bed from previously written python code file bed_parser
import statistics
#imports statistics, an additional system with many stat functions
fname = sys.argv[1]
#defines the file name as part of the system index
bed = parse_bed(fname)
#defines the variable bed as the function parse_bed on a provided file
exons = []
#creates an empty list called exons
for line in bed:
#for lines in bed, previously defined as the parse_bed function on our provided file
    exons.append(line[9])
    #add index 9 into our exons list
exons.sort()
#sort the exons list
print(statistics.median(exons))
#utilizing the imported statistics drive, calculate the median of the exons list and print the results.


