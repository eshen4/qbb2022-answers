# QBB 2022 - Day 1 - Lunch Exercises Submission
1. I'm excited to learn more in general about coding and how to utilize these tools within various biological scenarios. I'm particularly excited (and simultaneously anxious) to gain more fluency in python.
2. Calculate the mean number of exons per gene:
	a. working copy of files:
		cp ../../data/bed_files/genes.chr21.bed .
		cp ../../data/bed_files/exons.chr21.bed .
	b. mean number of exons per gene:
		wc genes.chr21.bed
			words: 40959
		wc exons.chr21.bed
			words: 657
		mean number = 62.3
	c. To find the median number of exons per gene, I'd try to make a histogram or find a way to sort the data set by frequency.
3. Tally chromHMM states in E116 lymphoblastoid cells
	a. cp ../../data/bed_files/chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed .
	b. 
		cut -f 4 chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed > chromcolumn
		sort chromcolumn | uniq -c
		Results:
		 305 1
		  17 10
		  17 11
		  30 12
		  62 13
		 228 14
		 992 15
		 678 2
		  79 3
		 377 4
		 808 5
		 148 6
		1050 7
		 156 8
		 654 9
	c. To determine which state comprises the largest fraction of the genome, I'd have to try to subtract column 2 from column 3 (the start and end) and then sort the differences with with the overall chromHMM states as we sorted in question 3b.
4. Tally populations among 1000 Genomes Project samples.
	a. cp ../../data/metadata_and_txt_files/integrated_call_samples.panel .
	b.
		grep AFR integrated_call_samples.panel > superpop #selected only data points in AFR super population
		sort -s -k 2 superpop #sorted new file superpop alphabetically by column 2 (population)
		cut -f 2 superpop > pop #cut population column into new file pop
		sort pop | uniq -c #sorted pop file and counted results for samples in each population of the AFR super population
		
		#one line: grep AFR integrated_call_samples.panel | sort -k 2 | cut -f 2 | uniq -c
		Results:
	    123 ACB
	    112 ASW
	    173 ESN
	    180 GWD
	    122 LWK
	    128 MSL
	    206 YRI
	c. To sort through all 5 populations combined, there's no longer a need to look for a subset of data (grep command). Everything else stays largely the same, except that the initial sort is based on column 3 (the superpop).
5. Explore SNP allele frequencies.
	a. cp ../../data/vcf_files/random_snippet.vcf .
	b. cut -f 1-9,13 random_snippet.vcf > nHG00100.vcf
	c.	
		cut -f 10 nHG00100.vcf > nHGc
		sort nHGc | uniq -c
		Results:
		9514 0|0
		 127 0|1
		 178 1|0
		 181 1|1
	d.
		cut -d ";" -f 4 random_snippet.vcf > AFsnippet.vcf
		cut -f 1 AFsnippet.vcf > AFcount.vcf
		sort AFcount.vcf | uniq -c
		Results:
		15 AF = 1
	e. AF = 1 can appear once per row.
	f. To extract the AFR values, I'd follow the same code written in part d, except for the initial cut I would put the field at 7.
	