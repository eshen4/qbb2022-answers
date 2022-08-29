# QBB2022: Day 1 - Homework Exercises Submission

1. 
	Error message: "awk: illegal field $(), name "nuc""
	Corrected code:
	{ for nuc in A C G T
	do
		echo "Considering " $nuc
		awk -v var="$nuc" '/^#/{next} {if ($4 == var) {print $5}}' $1 | sort | uniq -c
	done }

	Problem line in original code: awk '/^#/{next} {if ($4 == $nuc) {print $5}}' $1 | sort | uniq -c
	#Awk needs -v to set variables outside of awk. The -v flag and the var= setting sort of gives this outside variable a name within awk, allowing the program to run.
	Working script results:
		Considering  A
		 354 C
		1315 G
		 358 T
		Considering  C
		 484 A
		 384 G
		2113 T
		Considering  G
		2041 A
		 405 C
		 485 T
		Considering  T
		 358 A
		1317 C
		 386 G
	These results do make sense considering the mechanisms of transition/transversion. Transition occurs more naturally than transversion (purine -> purine, pyrimidine -> pyrimidine). Bases A and G are purines, while bases C and T are pyrimidines, hence the higher value subsitutions.
2. 
	Chosen possible promoter region categories: flanking active TSS, active TSS, bivalent/poised TSS, flanking bivalent/poised TSS (1, 2, 10, 11)
	{ awk '{ if( $4 == 1 || $4 == 2 || $4 == 10 || $4 == 11 ) print }' ~/data/bed_files/chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed > chrompromoternew.bed
	bedtools intersect -wa -a ~/data/vcf_files/random_snippet.vcf -b ~/qbb2022-answers/day1-homework/chrompromoternew.bed > intersectchrom1.vcf
	./exercise1.sh intersectchrom1.vcf }
	Results:
	Considering  A
	   6 C
	  32 G
	   8 T
	Considering  C
	  12 A
	  11 G
	  39 T
	Considering  G
	  46 A
	  17 C
	  11 T
	Considering  T
	  10 A
	  29 C
	   8 G
	Through this method of segmentation, we conclude that promoter regions are not clearly and objectively defined. Despite the success of the intersect and nucleotide count, we started our process essentially guessing possible promoter regions, and although our guesses were educated, it can't be said that the method is entirely definable.
3. 
	#!/bin/bash

	#USAGE: bash exercise3.sh input_VCF

	awk '/^#/{next} {print $1,$2-1, $2}' $1 > variants.bed
		#sorts a bed file (ignoring header) and prints columns 1, 2, and the difference between values in columns 1 and 2 into a new bed file titled "variants"
	sort -k1,1 -k2,2n ~/data/bed_files/genes.bed > genes.sorted.bed
		#sorts columns 1 and 2 first by column 1, and then by column 2 numerically. This file is then saved as genes.sorted.bed
	bedtools closest -a variants.bed -b genes.sorted.bed
		#bedtools closest command, similar to intersect, will look for overlap between variables A and B. However, in the event of no overlap, it will report the closest overlap feature.
	
	{bash exercise3.sh ~/data/vcf_files/random_snippet.vcf > snippet3.vcf
		wc -l snippet3.vcf
		cut -f 4 snippet3.vcf |  sort | uniq | wc -l}
		Results:
		WC (returned variants): 10293
		Unique genes: 200
	