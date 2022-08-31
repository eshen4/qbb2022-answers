# QBB2022 - Day 3 - Homework Exercises Submission

Exercise 1: Perform PCA using PLINK
	plink --pca --help:
		--pca [count] ['header'] ['tabs'] ['var-wts']
			You can change the number of PCs by passing a numeric parameter
			'header' - adds a header line to the .eigenvec output file
			'tabs' - causes the .eigenvec file to be tab-delimited
			'var-wts' modifier requests an additional file with PCs expressed as variant weights instead of sample weights (???)
Calculates a variance-standardized relationship matrix. EXTRACTS THE TOP 20 PRINCIPAL COMPONENTS.

Command: plink --vcf (file) --pca 3
	3 = pc numeric parameter
Results:
	48.2938
	13.8526
	5.92139

Exercise 2:
I noticed that the two images (PC 1 vs PC2 and PC1 vs PC3) are almost mirror images of each other. I also noticed that for both plots, there's much greater clustering around the lowest numbers of PC1. I suppose this represents greater similarities among the lower values.