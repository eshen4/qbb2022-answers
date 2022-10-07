#Quant Week 4: Homework Assignment

Exercise 2:

plink --vcf genotypes.vcf --pca 10 --freq
(Taken from bootcamp day 3 homework)

Exercise 3:

Adding the --freq flag calculated AF into a file called plink.frq (frequencies are under column MAF)

Exercise 4:

plink --vcf gwas_data/genotypes.vcf --assoc --allow-no-sex --linear --pheno gwas_data/CB1908_IC50.txt --covar plink.eigenvec --hide-covar --out CB

plink --vcf gwas_data/genotypes.vcf --assoc --allow-no-sex --linear --pheno gwas_data/GS451_IC50.txt --covar plink.eigenvec --hide-covar --out GS

Exercise 5:
in my python file as week4.py

Exercise 6:
in my python file (selected CB1908_IC50) as exercise6.py

Exercise 7:

CB most associated SNP: rs10876043
GS most associated SNP: rs7257475

^^the code for those is included in print statements in week6 because I didn't know how to do it in the terminal with bash, should be under "aSNP" and "bSNP"

CB gene: DIP2B
"disco interacting protein 2 homolog B" -- seems to be an mRNA associated gene
GS gene: ZNF826
cDNA gene, mentions that it's similar to zinc finger 91
