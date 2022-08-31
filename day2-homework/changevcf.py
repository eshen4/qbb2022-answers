#!/usr/bin/env python3
import sys
from vcfParser import parse_vcf
#imports the vcfParser function to be used

randomsnippetvcf = parse_vcf("random_snippet.vcf")
dbSNPvcf = parse_vcf("dbSNP_snippet.vcf")
#loads the two files needed for program
dbSNPid = {}
#creates empty dictionary by name dbSNPid

for line in dbSNPvcf:
#read through dbSNPvcf file
    if line[0] == "CHROM":
        continue
    #skip first header line (column names)
    pos = line[1]
    ids = line[2]
    #labeling the necessary fields
    dbSNPid[pos] = (ids)
    #marking necessary fields as ids in created dictionary
incorrect = 0
#created a counter variable
for line in randomsnippetvcf:
#read through randomsnippetvcf file
    if line[0] == "CHROM":
        continue
        #skips the first header lines with the column names
    if line[1] in dbSNPid.keys():
    #if index 1 (the position values) can be found in the keys of the created dictionary dnSNPid
        line[2]=dbSNPid[line[1]]
        #rewrite the line 2 value (ID) with the given ID in the created dictionary of dbSNPid
    else:
    #if the line is not the header and also does NOT match a written value in the created dictionary
        incorrect +=1
        #add plus one to the counter that we created above
print(f"there are {incorrect} unmatched outcomes")
#prints the counter for incorrect (unmatched) values
        
    
    
