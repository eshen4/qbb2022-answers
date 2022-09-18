# Quant Bio 2022 - Week 2 Assignment

Amino Acids:
python ../align.py CTCF_38_M27_AA.faa BLOSUM62.txt -10 > AA.txt

Alignment score: 3801.0
Gaps in sequence 1: 9
Gaps in sequence 2: 0

DNA:
python ../align.py CTCF_38_M27_DNA.fna HOXD70.txt -300 > DNA.txt

Alignment score: 266300.0
Gaps in sequence 1: 46
Gaps in sequence 2: 78

These values were obtained through a bunch of print functions at the bottom of my align.py, alignment score is the bottom right of the Fmatrix, and I just used count for the gaps with the character "-"


