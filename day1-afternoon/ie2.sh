# goal: Number of SNPs in the 1000 genomes file that intersects each gene and how many unique genes are represented.

genefile=/Users/cmdb/data/bed_files/genes.bed
echo $genefile

vcffile=/Users/cmdb/data/vcf_files/random_snippet.vcf
#Alternative format: ~/data/vcf_files/random_snippet.vcf

#Intersect genomic locations from a bed and vcf file
bedtools intersect -a $genefile -b $vcffile > intersect_out_ie2.bed

#Finding intersects through word count:
wc -l intersect_out_ie2.bed
	#Ans: 4204 SNPs that intersect a gene
	cut -f 4 intersect_out_ie2.bed | sort | uniq | wc -l
	#Ans: 166 unique genes!

grep "#" ~/data/vcf_files/random_snippet.vcf | tail -n 1 | cut -f 1,2,3,4,5
#???????? Selecting for specifically the header line within random_snippet.vcf

grep -v  "#" ~/data/vcf_files/random_snippet.vcf | cut -f 4 | sort | uniq -c
#Shows the count per individual nucleotide base
awk '/^#/{next} {print $4}' ~/data/vcf_files/random_snippet.vcf | sort | uniq -c 
#
grep -v "#" ~/data/vcf_files/random_snippet.vcf | awk '{print $4}' | sort | uniq -c

grep -v "#" ~/data/vcf_files/random_snippet.vcf | awk '{if ($4== "C") {print $5}}' | sort | uniq -c
