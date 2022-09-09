# coverage = {}
# for line in chromHMM:
# 	chrom, start, end, state = line.split()
# 	if state not in coverage:
# 		coverage[state] = 0
# 	coverage[state] = coverage[state] + end - start

import sys
def vcf_parser(fname):
	vcf = []
	malformed = 0
	try:
		fs = open(fname)
	except:
		raise FileNotFoundError("no file by that name")
for h, line in enumerate(fs):
	if line.startswith('#'):
		continue
	try:
		fields = line.rstrip().split("\t")
		fields[1] = int(fields[1])
		if fields[5] != ".":
			fields[5] = float(fields[5])
		fields[7] = fields[7].split(";")
		if len(fields) > 8:
			fields[8] = fields[8].split(":")
			if len(fields[8]) > 1:
				for i in range(9, len(fields)):
					fields[i] = fields[i].split(':')
			else:
				fields[8] = fields[8][0]
		vcf.append(fields)
	except:
		malformed += 1
if malformed > 0:
	print(f"There were {malformed} malformed entries", file=sys.stderr)

if __name__ == "__main__":
	fname = sys.argv[1]
	vcf = vcf_parser(fname)
	for i in range(10):
		print (vcf[i])