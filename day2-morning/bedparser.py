#!/usr/bin/env python3

#import sys

#def bed_parser(fname):
#fname = sys.argv[1]
#open file and put filestream in fs
   # fs = open(fname, mode='r')
    #create empty list to hold entries
 #   bed = []
 #   data_types = [str, int, str, float, str]
    #step line by line through file
 #   for h, line in enumerate(fs):
    #get rid of newline char and split into separate fields
 #       fields = line.rstrip().split("\t")
    #name relevant fields, converting to int when needed
  #      try:
   #         for i in range(min(len(data_types),len(fields))):
   #             if fields[i] !=".":
   #                 fields[i] = data_types[i](fields[i])
   #         bed.append(fields[:min(len(datatypes),len(fields))])
   #     except:
  #          print(f"line {h} is malformed", file=sys.stderr)
  #  fs.close()
  #  return bed

#if __name__ == "__main__":
   # bed = bed_parser(sys.argv[1])
    #pull out first 2 entries as list and look at each entry in variable 1
  #  for i in bed(2):
        #print entry 1
  #      print(bed[i])

#!/usr/bin/env python

import sys

def bed_parser(fname):
	# open up file and put filestream in fs
	fs = open(fname, mode='r')
	# create empty list to hold entries
	bed = []
	data_types = [str, int, int,
				  str, float, str]
	for h, line in enumerate(fs):
		fields = line.rstrip().split("\t")
		try:
			for i in range(min(len(data_types),
							   len(fields))):
				if fields[i] != ".":
					coverter = data_types[i]
					fields[i] = converter(fields[i])
			bed.append(fields[:min(len(data_types),
							   len(fields))])
		except:
			print(f"line {h} is malformed",
				  file=sys.stderr)
	fs.close()
	return bed

if __name__ == "__main__":
	bed = bed_parser(sys.argv[1])
	# pull out first 2 entries as list and look
	# at each entry in variable i
	for i in bed[0:2]:
		#print entry i
		print(i)