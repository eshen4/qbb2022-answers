#!/usr/bin/env python3

#chr21   5086739 5087232 ENST00000701545.1       0       +       5086739 5086739 0,100>0       +       5086739 5086739 0,100,0 1       493,    0,0 1       493,    0,

import sys

def parse_bed(fname):
    try:
        fs = open(fname, 'r')
    except:
        raise FileNotFoundError("That file doesn’t appear to exist")
    bed = []
    field_types = [str, int, int, str, float, str, int, int]
    counter=0
    for i, line in enumerate(fs):
        if line.startswith("#"):
            continue
        fields = line.rstrip().split()
        fieldN = len(fields)
        if not ( 3 <= fieldN <= 9 or fieldN == 12 ):
            print(f"Line {i} appears malformed", file=sys.stderr)
            counter+=1
            print(counter)
            continue

        try:
            for j in range(fieldN): #min(len(field_types), len(fields))):
                if j < 8:
                    fields[j] = field_types[j](fields[j])
                elif j == 8:
                    fields[j] = fields[j].split(",")
                    assert len(fields[j]) == 3
                elif j == 9:
                    fields[j] = int(fields[j])
                else:
                    fields[j] = fields[j].rstrip(",").split(",")
                    fields[j] = [int(k) for k in fields[j]]
                    assert len(fields[j]) == fields[9]
            bed.append(fields)
        except:
            print(f"Line {i} appears malformed", file=sys.stderr)
            counter+=1
            print(counter)
    fs.close()
    return bed

if __name__ == "__main__":
    fname = sys.argv[1]
    bed = parse_bed(fname)
