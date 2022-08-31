# QBB2022  - Day 2 - Homework Exercises

Ex 2. Overall goals
	1. Read in the two vcfs using vcfParser
	2. Run through dbSNP vcf, storing ID info for each variant
		Make empty dictionary
		for loop over the vcf list (skip first line #)
			for line in dbSNP_vcf:
				obtain the desired variables (pos, id)
				chrom = line[0]
				pos = line[1]
				ref = line[3]
	3. Run through random_snippet vcf, pulling ID info for each line
		Look up ID based on chrom, pos, ref
		Two outcomes: ID is in dbSNP, or it isn't in dbSNP	
	4. Report the number of unmatched outcomes through a counter
	
	Results:
	unmatched outcomes = 100