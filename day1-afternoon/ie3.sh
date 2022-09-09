#USAGE: ie3.sh input_vcf_file nucleotide_of_interest
# nucoi=$2
# grep -v "#" $1 | awk '{if ($4 == "C") {print $5}}' | sort | uniq -c
# 	bash ie3.sh ~/data/vcf_files/random_snippet.vcf

#USAGE: ie3.sh input_vcf_file nucleotide_of_interest

nucoi=$2
grep -v "#" $1 | awk '{if ($4 == $nucoi) {print $5}}' | sort | uniq -c