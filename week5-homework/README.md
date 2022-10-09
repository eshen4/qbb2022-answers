#Quant Bio Week 5 - ChIP-seq Homework

Part 1: ChIP-seq Analysis

1. 

samtools view - views and converts files ?

samtools view -q 10 -b -o (output file) (input file)
 
2. 

macs2 - model based analysis for chIP sequencing

callpeak - main macs2 function: call peaks from alignment results

target input - filtered file
control input - filtered input file
effective genome size (chr17) - 9.4e7
-B parameter: bedgraph of read pileups

macs2 callpeak -t (target file) -c (control file) -g 9.4e7 -B --outdir R1 (or R2)

3. 

bedtools intersect -a R1/NA_peaks.narrowPeak -b R2/NA_peaks.narrowPeak -wa > intersect.bed

4. 

wc -l intersect.bed = 583
bedtools intersect -a intersect.bed -b D2_Klf4_peaks.bed > klf4intersect.bed
wc -l klf4intersect.bed = 41
wc -l D2_Klf4_peaks.bed = 60

41/60 = 68%

5. 

for D0 H3K27ac:
python scale_bdg.py D0_H3K27ac_treat.bdg D0scaled.bdg
awk '{ if ($2 < 35507055 && $3 > 35502055) print $0 }' D0scaled.bdg > D0crop.bdg

for D2 H3K27ac:
python scale_bdg.py D2_H3K27ac_treat.bdg D2scaled.bdg
awk '{ if ($2 < 35507055 && $3 > 35502055) print $0 }' D2scaled.bdg > D2crop.bdg

for D2 Klf4:
python scale_bdg.py D2_Klf4_treat.bdg Klf4scaled.bdg
awk '{ if ($2 < 35507055 && $3 > 35502055) print $0 }' Klf4scaled.bdg > Klf4crop.bdg

for R1 Sox2:
python scale_bdg.py R1/NA_treat_pileup.bdg R1scaled.bdg
awk '{ if ($2 < 35507055 && $3 > 35502055) print $0 }' R1scaled.bdg > R1crop.bdg

Part 2: Motif discovery

sort -k 5,5rn intersect.bed | head -300 > sortpeaks.bed
awk '{ printf "%s:%i-%i\n", $1, $2, $3 }' sortpeaks.bed > formatpeaks.bed
samtools faidx mm10.fa -r formatpeaks.bed -o mm10extract.fa
meme-chip -maxw 7 mm10extract.fa

Part 3: Motif identification

(downloaded and unzipped motif_databases)
tomtom memechip_out/combined.meme motif_databases/MOUSE/HOCOMOCOv11_full_MOUSE_mono_meme_format.meme
open tomtom_out/tomtom.html
grep "SOX2" tomtom_out/tomtom.tsv > Sox2hits.tsv
grep "KLF4" tomtom_out/tomtom.tsv > klf4hits.tsv

There are two hits for each!

