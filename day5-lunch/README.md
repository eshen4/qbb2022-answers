# QBB2022 - Day 5 - Lunch Exercises

1. 

dnm.csv - Chr, pos, Ref, Alt, Proband_id, Phase_combined, Crossover, Sanger
	The Phase_combined column records the inferred parent of origin of each de novo mutation. 
	Goal: Break the Phase_combined column to record the inferred parent of origin 
	(categories: mother, father)

<!--cut -f5,6 -d',' aau1043_dnm.csv | sort | uniq -c #counts by mother and father per proband id
cut -f5,6 -d',' aau1043_dnm.csv | sort | uniq -c | grep father | less -S > father.txt
cut -f5,6 -d',' aau1043_dnm.csv | sort | uniq -c | grep mother | less -S > mother.txt
join -1 2 -2 2 father.txt mother.txt > parents.txt -->

awk 'BEGIN{FS=","; OFS="\t"} {if($6 == "father") {print $5, $6}}' aau1043_dnm.csv | sort | uniq -c > father.txt
awk 'BEGIN{FS=","; OFS="\t"} {if($6 == "mother") {print $5, $6}}' aau1043_dnm.csv | sort | uniq -c > mother.txt
join -1 2 -2 2 father.txt mother.txt | cut -f 1,2,4 -d' ' > parents.txt

parental_age.csv - Proband_id, Father_age, Mother_age

awk 'BEGIN{FS=","; OFS="\t"} {$1=$1; print}' aau1043_parental_age.csv | sort -k1 > ages.txt

join -1 1 -2 1 parents.txt ages.txt > joinfull.txt
2. 
Maternal OLS Regression Results:

Size of relationship (mother age coeff) = 0.3776
P >|t|
Mother_age = < 0.001
This result proves stastically significant with p-value < 0.05.

Paternal OLS Regression Results:

Size of relationship (father age coeff) = 1.3538
P > |t|
Father_age = < 0.001
This result proves stastically significant with p-value < 0.05.

Ttest_indResult(statistic=-53.40356528726923, pvalue=2.198603179308129e-264)
 This proves statistically significant (p-value really small)
 
Number of paternal mutations at 50.5 age: 78.018535
 

