#!/usr/bin/env python

import numpy
from scipy.stats import binomtest
from statsmodels.stats.multitest import multipletests

def simulate_coin_toss(n_tosses, prob_heads = 0.5, seed=None):
    '''
    Input: n_tosses, an integer, number of coin tosses to simulate
           prob_heads, a float, the probability the coin toss will return heads; default is 0.5, meaning a fair coin
           seed, an integer, the random seed that will be used in the simulation
    Output: results_arr, an array of 1's and 0's with 1's representing heads and 0's representing tails
    Resources: https://numpy.org/doc/stable/reference/random/generated/numpy.random.choice.html
    '''
    if seed is not None:
        numpy.random.seed(seed)
    results_arr = numpy.random.choice([0,1], size=n_tosses, p = [1-prob_heads, prob_heads])
    return (results_arr)

def perform_hypothesis_test(n_heads, n_tosses):
    binom_result = binomtest(n_heads, n_tosses)
    pval = binom_result.pvalue #grabs the pvalue attribute from the binom_result instance
    return(pval)
    
#print(perform_hypothesis_test(2, 5))

def correct_pvalues(pvals):
    corrected_pvalues = multipletests(pvals, method="bonferroni")
    return(corrected_pvalues[1])
    
#print(correct_pvalues([0.01, 0.05, 0.02, 0.11, 0.015]))


def interpret_pvalues(pvals):
    interpreted = numpy.array(pvals) < 0.05
    return(interpreted) #an array of trues/falses

#print(interpret_pvalues([0.01, 0.05, 0.03, 0.11, 0.002]))

def compute_power(n_rejected_correctly, n_tests):
    power = n_rejected_correctly / n_tests
    return(power)

def run_experiment(prob_heads, n_toss, n_iters = 100, seed = 389, correct_the_pvalues = False):
    numpy.random.seed(seed)
    pvals = []
    for k in range(n_iters):
        results_arr = simulate_coin_toss(n_toss, prob_heads = prob_heads)
        n_success = numpy.sum(results_arr)
        pvals.append(perform_hypothesis_test(n_success, n_toss))
    if correct_the_pvalues:
        pvals = correct_pvalues(pvals)
    pvals_translated_bools = interpret_pvalues(pvals)
    power = compute_power(numpy.sum(pvals_translated_bools), n_iters)
    
    return(power)
power1 = run_experiment(0.6, 500)
print(power1)
power2 = run_experiment(0.95, 10, correct_the_pvalues = True)
print(power2)

#print(run_experiment(0.2, 30, n_iters=5))