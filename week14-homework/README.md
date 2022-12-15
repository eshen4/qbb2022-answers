#Quant Bio Homework Week 14: Metagenomics

###Step 1: Using KronaTools

Called the krona.py script per kraken file with: 
python krona.py SRR492183.kraken SRR492183
(python krona.py kraken file sample name)
 83 86 88 89 90 93 94 97
 
 I used the provided script and just did it manually for all 8 files
 
#####Question 1: In your README, briefly comment on the trends you see in the gut microbiota throughout the first week.
 - The portion of non lactobacillales bacteria (the things in orange, not red) get smaller throughout the first half of the week. Then, in the later half, the fraction of those bacteria (actinobacteria, staphylococcus, etc.) grow larger once again.
 
###Step 2: Deconvoluting

bwa index metagenomics_data/step0_givendata/assembly.fasta 

bwa mem -t 4 metagenomics_data/step0_givendata/assembly.fasta metagenomics_data/step0_givendata/READS/SRR492183_1.fastq metagenomics_data/step0_givendata/READS/SRR492183_2.fastq > 83.sam
samtools sort 83.sam -o 83.bam

^I used the above bwa mem format for all 8 samples and manually substituted the individual reads (ex. the next line was the same but for the 86_1 and 86_2, with output to 86)
^^I did the same for the samtools sort command
 
jgi_summarize_bam_contig_depths --outputDepth depth.txt *.bam
metabat2 -i metagenomics_data/step0_givendata/assembly.fasta -a depth.txt -o bins

#####Question 2: In your README, comment on what metrics in the contigs could we use to group them together?
- Node number, length of contig, etc.
#####Question 3a: How many bins did you get? 
- I got 6 bins.
#####Question 3b: What percentage of the assembly do they represent?
- I believe they represent 95% of the assembly.
#####Question 3c: comment on whether you think the sizes of each bin look about right, based on what you know about the size of prokaryotic genomes?
- I believe the sizes of each bin look about right, as they're quite large, as are prokaryotic genomes.
#####Question 3D: Describe how you might estimate how complete and how contaminated each bin is?
- Maybe you could divide each bin by the total genome to test for completion.

###Step 3: Predicting taxonomic composition

