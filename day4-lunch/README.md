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
	snRNA: small nuclear RNA, included in the genefile. 
	miRNA: micro RNA, included in the gene file. Non coding RNAs that have a hand in regulating gene expression.
	lncRNA: long coding RNA, included in the gene file. Tend to be regulators of gene expression

Exercise 2:

y-axis: density of alleles

These graphs represent the allele frequencies on a log scale based on specific gene types (exons, lncRNA, protein coding, and processed pseudogene). All the graphs definitely show a higher concentration between 0 and 1000 SNPs, indicating that they show higher frequency of smaller SNPs.

Exercise 3: Documentation for cmdb-plots-vcfs

Synopsis:
The cmdb-plots-vcfs file includes code to write .bed and .vcf files for individual features of interest after being provided a larger, combined vcf and gtf file. This is done through the do_all.sh bash executable file, which will also create graphed .png files for individual features of interest provided the appropriate gene type.

Usage:
bash do_all.sh [.vcf file] [.gtf file]
subset_regions.sh: For gene type of interest:
	Add gene type name as specified in file under for TYPE in... loop


Dependencies:
bedtools
matplot.lib

All other necessary files listed under dependencies.txt

Description:
1) Searches for entered files of interest
	- Requires command entry with one .vcf file and one .gtf file
	- If either file not found, output of "(file) not found"
2) Creates .bed files for features of interest
	- Output string "Creating .bed files for features of interest"
	- Runs subset_regions.sh
		- Output string "creating (genetype, chromosome).bed"
		- Uses grep command to isolate genetype within the chromosome.gtf file, pipes results to an awk command that prints the gene column details into a bed file
		- Loops per individual gene type
3) Creates individual .vcf files per feature
	- Uses bedtools sort by type in .bed file created in 2), pipes into bedtools merge function, followed by an awk command that prints the number of basepairs covered for each feature
	- Runs bedtools intersect to report the overlap between the original vcf file and the genetype .bed file, which is then saved as a genetype.vcf
3) Creates .png histograms of allele counts for features of interest
	- Output string "Plotting AC for (genetype).vcf"
	- Runs plot_vcf_ac.py
		- Splits out header lines from provided vcf file
		- Creates histogram figures with y axis on a log scale using matplotlib.pyplot import

Output:
bash do_all.sh random_snippet.vcf chr21.gtf 
*** Creating .bed files for features of interest
--- Creating protein_coding.chr21.bed
--- Creating processed_pseudogene.chr21.bed
--- Creating lncRNA.chr21.bed
--- Creating exons.chr21.bed
*** Subsetting .vcf for each feature
--- Subsetting exons.chr21.bed.vcf
    + Covering 1107407 bp
--- Subsetting lncRNA.chr21.bed.vcf
    + Covering 8663528 bp
--- Subsetting processed_pseudogene.chr21.bed.vcf
    + Covering 956640 bp
--- Subsetting protein_coding.chr21.bed.vcf
    + Covering 13780687 bp
*** Plotting AC for each .vcf
--- Plotting AC for exons.chr21.bed.vcf
--- Plotting AC for lncRNA.chr21.bed.vcf
--- Plotting AC for processed_pseudogene.chr21.bed.vcf
--- Plotting AC for protein_coding.chr21.bed.vcf
--- Plotting AC for random_snippet.vcf
