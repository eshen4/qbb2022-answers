# QBB2022 - Day 4 - Homework Exercises

Exercise A:

numpy.around(numpy.arange(0.55, 1.05, 0.05), decimals=2)[::-1]

numpy.arange(): Returns evenly spaced values within a given individual. For our command, numpy.arange(0.55, 1.05, 0.05), we are indicating a need to return spaced values starting from 0.55 and ending at 1.05 with intervals of 0.05 (start, stop, step). This will return an array of evenly spaced values.

numpy.around(): Evenly rounds to the given number of decimals. The decimals parameter tells the command how many decimals to round each value to. This will return an array of the same type as the provided array a (in this case, our numpy.arange() function), but the values will be rounded based on the decimal parameter.

The last [::-1] parameter will provide our results in reverse.

Exercise D:

The study provided is interested in observing the "transmission distortion" observed in numerous organisms. This phenomenon shows moments in which Mendel's Law of Segregation seems to "fail" as certain alleles are transmitted disproportionately to the next generation. 

The powermap created in class seems to be visually similar to supplementary figure S13, which shows a power heatmap for deviations from binomial expectations across sample size. In our class experiment, prob_heads likely corresponds to the transmission rate axis, as our y axis should essentially be the number of "successes" throughout trials. Meanwhile, our n_tosses corresponds to the number of sperm axis in figure S13. Both examples use binomial tests to analyze the significance of deviations away from an expected distribution. In terms of coin toss, the expected distribution is 50/50. In terms of transmission, as per Mendel's Law, the expected allele transmission is also 50/50.

These power graphs are indicative of false negatives as we are controlling the false positive rate. Power is good at determining a minimal sample size to distinguish a signal for a specific effect size of interest. 