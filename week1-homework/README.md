# Week 1 Homework Exercises

1.1) 100bp reads needed to sequence a 1Mbp genome to 5x coverage:
	1Mbp * 5x = 5Mbp data
	5Mbp / 100bp/read = 50,000 reads
to 15x coverage:
	1Mbp * 15x = 15Mbp data
	15Mbp / 100bp/read = 150,000 reads
	
1.2) (code written in document exercise12.py) (its 12 because i forgot to punctuate between 1 and 2)
plot: x = # of reads y = frequency 

1.3) count of zeros in array = 7231
	poisson expected count of zeros = 6737.9
It matches kind of well, within + or - 500 values

1.4) count of zeros in array = 3
	poisson expected count of zeros = 4.6
Our random array matches the poisson expectation decently well, better in comparison to 5x coverage.

2.1) 4 contigs were produced
	python ~/Downloads/SPAdes-3.15.5-Darwin/bin/spades.py --pe1-1 frag180.1.fq --pe1-2 frag180.2.fq --mp1-1 jump2k.1.fq --mp1-2 jump2k.2.fq -o asm -t 4 -k 31
	grep -c '>' contigs.fasta

2.2) samtools faidx - indexes or queries regions from a fasta file
Lengths of contigs:
node 1: 105830
node 2: 47860
node 3: 41351
node 4: 39426
samtools faidx contigs.fasta
less -S contigs.fasta.fai

2.3) The size of the largest contig is 105830 bp (node 1)

2.4) The N50 for these contigs is 47860 (there's only four contigs)

3.1) Average identity: 99.98%
dnadiff ~/qbb2022-answers/week1-homework/asm/ref.fa ~/qbb2022-answers/week1-homework/scaffolds.fasta
less out.report

3.2) The length of the longest alignment is 234497
nucmer ~/qbb2022-answers/week1-homework/asm/ref.fa ~/qbb2022-answers/week1-homework/scaffolds.fasta
show-coords out.delta
    [S1]     [E1]  |     [S2]     [E2]  |  [LEN 1]  [LEN 2]  |  [% IDY]  | [TAGS]
=====================================================================================
       3    26789  |        1    26787  |    26787    26787  |   100.00  | Halomonas	NODE_1_length_234497_cov_20.506978
   26790   233794  |    27500   234497  |   207005   206998  |    99.98  | Halomonas	NODE_1_length_234497_cov_20.506978

3.3) There is 1 insertion, 15 deletions (indels)

4.1) The position of the insertion is between 26787 and 27500.

4.2) The insertion is 772 bp long.

4.3) The DNA sequence of the encoded message(the insertion) is saved under "insertion.txt":

CGCCCATGCGTAGGGGCTTCTTTAATTACTTGATTGACGCATGCCCCTCGTTCTACATGT
CTAGCTTCGTAACTGCCCCGATTTATACAGGAGCATATGCGTTTCGTAGTGCCGGGAATG
CATACCAAAGGGCTCACGGCGGGTACGCCACAATGGCTCAAGTCGAAAATGAATCGAAGA
CAACAAGGAATACCGTACCCAATTACTCAAGGACCTCATACACCATCCCATGCTACTTAT
CTACAGACATACACGCCAGCACCCAGCAACCAAAGCACACCGACGATAAGACTACAATCG
CGATAAGCACAACTTACATTAGGAGGCCCGGCAAATCTTGACGGCGTTAAGTCCGACACG
AATACCCCCCGACAAAAGCCTCGTATTCCGAGAGTACGAGAGTGCACAAAGCACCAAGGC
GGGGCTTCGGTACATCCACCAGTAGTCCCGTCGTGGCGGATTTTCGTCGCGGATGATCCG
AGGATTTCCTGCCTTGCCGAACACCTTACGTCATTCGGGGATGTCATAAAGCCAAACTTA
GGCAAGTAGAAGATGGAGCACGGTCTAAAGGATTAAAGTCCTCGAATAACAAAGGACTGG
AGTGCCTCAGGCATCTCTGCCGATCTGATTGCAAGAAAAAATGACAATATTAGTAAATTA
GCCTATGAATAGCGGCTTTAAGTTAATGCCGAGGTCAATATTGACATCGGTA

4.4)
The decoded message :  Congratulations to the 2022 CMDB @ JHU class!  Keep on looking for little green aliens... 