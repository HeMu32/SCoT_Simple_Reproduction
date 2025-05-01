from math import comb

def even_binomial_Coeff_Sum(n):
  sum = 0
  for i in range(n + 1):
    if i % 2 == 0:
      sum += comb(n, i)
  return sum