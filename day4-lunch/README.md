# QBB2022 - Day 4 - Lunch Exercises

Exercise 1:

a.

--- Subsetting exons.chr21.bed.vcf
    + Covering 1107407 bp
--- Subsetting processed_pseudogene.chr21.bed.vcf
    + Covering 956640 bp
--- Subsetting protein_coding.chr21.bed.vcf
    + Covering 13780687 bp

b. To confirm that the reproduced plots are the same as in the original cache/ directory, you can open the original pngs in the directory and compare them directly.
	You can also try checking based off the basepairs.
	You can also use the cmp function (compare) (cmp -b file 1 file 2)
		-b flag will print out the differences
	You can also use the diff function (difference) (diff -md5sum )

c. gene types: transcribed unprocessed pseudogene, unprocessed pseudogene, lncRNA, protein coding, processed pseudogene, snRNA, miRNA, transcribed processed pseudogene, transcribed unitary pseudogene
	snRNA:
	miRNA:
	lncRNA:

Exercise 2:

y-axis: density of alleles

These graphs represent the allele frequencies on a log scale based on specific gene types (exons, lncRNA, protein coding, and processed pseudogene). All the graphs definitely show a higher concentration between 0 and 1000 SNPs, indicating that they show higher frequency of smaller SNPs.

Exercise 3: Documentation for cmdb-plots-vcfs/do_all.sh

Synopsis:
do_all.sh is a bash executable file that will create individual .bed, .vcf, and graphed .png files for individual features of interest within a larger combined vcf and gtf file.

Usage:
bash do_all.sh [.vcf file] [.gtf file]

Dependencies:
bedtools
matplot.lib

All other necessary files listed under dependencies.txt.

Description: