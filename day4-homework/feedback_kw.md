#  day 4 homework feedback

Please add your README that comments on part A (deconstructing the numpy array), part C (describing your results), and part D (comparing to the real study)

Please also plot and add the second heatmap with power computed from the p-values corrected for multiple hypothesis testing.

The code looks good overall. The assignment does ask you to incorporate the nested for loop and storing the power within the `run_experiment()` function rather than calling that function repeatedly. What you've done works and leads to the same conclusions, but consider how you might edit the function to incorporate the new code. While your results will be the same every time your script is run, will your results be the same compared to someone who only calls the `run_experiment()` function once therefore only sets the random seed once?
