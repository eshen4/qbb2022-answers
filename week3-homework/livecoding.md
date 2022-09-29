#Week 3: Livecoding/Homework

bwa index c_elegans.PRJNA13758.WS283.genomic.fa.gz
- creates index for files

bwa mem -R "@RG\tID:SRR16356854\tSM:SRR16356854" -o SRR16356854.sam c_elegans.PRJNA13758.WS283.genomic.fa.gz SRR16356854_1.subset.fastq.gz SRR16356854_2.subset.fastq.gz

samtools sort -O bam -o SRR16356854.bam SRR16356854.sam
- big O is output file type small o is the output file

To acquire everything all together...bash for loop:


(Homework starts below)

Step 1:

bwa index sacCer3.fa

Step 2-3:

bwa mem -R "@RG\tID:A01_09\tSM:A01_09" sacCer3.fa A01_09.fastq > A01_09.sam 

samtools sort -O bam -o A01_09.bam A01_09.sam

samtools index A01_09.bam

I tested everything with 09, then ran a bash scripted for loop for the other samples. It's uploaded under week3.sh!

Step 4:

freebayes: requires two inputs - fasta reference, bam format alignment file (sacCer3.fa and individual bam files made in steps 2-3). Detexts variants in genetic code between reference and alignment

freebayes -f sacCer3.fa (all relevant bam files, can put multiple) > var.vcf
-p flag: use a different ploidy (?) --> ploidy of 1 for haploidy

freebayes -f sacCer3.fa -p 1 --genotype-qualities *.bam > var.vcf

Step 5:

vcffilter -f "QUAL > 20" var.vcf > filter.vcf

In documentation: GUAL > 20 = not being polymorphic less than "phred 20", or polymorphism > 0.99

Step 6:

vcfallelicprimitives -k -g filter.vcf > final.vcf

-k flag: keepinfoFlag
-g flag: keepgenoFlag

Step 7:

usage: snpEff [eff] [options] genome_version [input_file]

snpEff ann R64-1-1.99 final.vcf > snpeff.vcf