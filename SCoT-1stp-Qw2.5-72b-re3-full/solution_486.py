import math

def binomial_probability(n, k, p):
    # Calculate the binomial coefficient (n choose k)
    binom_coeff = math.comb(n, k)
    
    # Calculate the probability of k successes
    prob_successes = p ** k
    
    # Calculate the probability of n-k failures
    prob_failures = (1 - p) ** (n - k)
    
    # Calculate the binomial probability
    binom_prob = binom_coeff * prob_successes * prob_failures
    
    return binom_prob