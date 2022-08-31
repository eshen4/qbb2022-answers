#!/usr/bin/env python3

#chr21   5086739 5087232 ENST00000701545.1       0       +       5086739 5086739 0,100>0       +       5086739 5086739 0,100,0 1       493,    0,0 1       493,    0,

import sys

def parse_bed(fname):
#defines the function to be used out of program (parse_bed), applies it to a file
    try:
        fs = open(fname, 'r')
        #opens the given file
    except:
        raise FileNotFoundError("That file doesn’t appear to exist")
        #exception: provides an error if the given file cannot be found
    bed = []
    #creates a list called bed
    field_types = [str, int, int, str, float, str, int, int]
    #defines data types within a field types list
    counter=0
    #sets a counter variable (to be used for error counting later on)
    for i, line in enumerate(fs):
    #for index line in the given file
        if line.startswith("#"):
            continue
        #if the line starts with a #, move on. this skips the header section in bed files
        fields = line.rstrip().split()
        #strip the rightmost extra characters (until hitting a value) and then split the line by values
        fieldN = len(fields)
        #forms variable fieldN that is equal to the length of the fields lines
        if not ( 3 <= fieldN <= 9 or fieldN == 12 ):
        #this if not statement is what removes the fields we didn't want (as provided in the lunch assignment). basically, it's saying that if our variable includes fields 1, 2, 10, or 11, add to our error counter and move on.
            counter+=1
            continue

        try:
            for j in range(fieldN):
            #for variable j in range fieldN (previously defined as length of fields)
                if j < 8:
                    fields[j] = field_types[j](fields[j])
                    #for all values in our file lines that are shorter than index 8 (9 columns), match the value in that index to the corresponding data type as previously defined in field_types.
                elif j == 8:
                #if field length is equal to index 8 (9 columns)
                    fields[j] = fields[j].split(",")
                    #split fields by comma as a delimiter
                    assert len(fields[j]) == 3
                    #make sure (assert) that the length of fields j is equal to 3. this is specific for column 9 in a bed file, which should have three values separated by commas (the itemRGB)
                elif j == 9:
                    fields[j] = int(fields[j])
                    #if the length of fields is equal to index 9 (column 10), record field as an integer. this needs to be specified because we didn't go up to 10 values in the previously defined field_types.
                else:
                #else here recognizes indexes 10 and 11, with 12 columns being the max
                    fields[j] = fields[j].rstrip(",").split(",")
                    #strip the rightmost characters until a value based on delimiter "," and split the values apart based on ","
                    fields[j] = [int(k) for k in fields[j]]
                    #assigns integer values for columns 11 and 12
                    assert len(fields[j]) == fields[9]
                    #makes sure that the current lengths of columns 11 and 12 match the length of column 10.
            bed.append(fields)
            #adds new field information to previously defined bed list.
        except:
            counter+=1
    print(f"there are {counter} malformed lines")
    #for lines that do not fall under the previous if statements, add them to the previously defined error counter. then, print the number of errors in the above statment.
    fs.close()
    #close the file
    return bed
    #return the created bed list

if __name__ == "__main__":
    fname = sys.argv[1]
    #sets the filename of the vcf to be this fname variable provided (the first system index)
    bed = parse_bed(fname)
    #runs the function on our fname through a stored variable (bed)
    
