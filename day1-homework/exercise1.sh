#!/bin/bash

#USAGE: bash exercise1.sh input_VCF

for nuc in A C G T
do
  echo "Considering " $nuc
  #awk '/^#/{next} {if ($4 == $nuc) {print $5}}' $1 | sort | uniq -c
  awk -v var="$nuc" '/^#/{next} {if ($4 == var) {print $5}}' $1 | sort | uniq -c
done

#USAGE: ie3.sh input_vcf_file nucleotide_of_interest

#nucoi=$2
#grep -v "#" $1 | awk '{if ($4 == $nucoi) {print $5}}' | sort | uniq -c

