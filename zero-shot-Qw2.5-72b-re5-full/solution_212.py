def fourth_Power_Sum(n):
    """
    Write a python function to find the sum of fourth power of n natural numbers.
    """
    return sum(i**4 for i in range(1, n+1))