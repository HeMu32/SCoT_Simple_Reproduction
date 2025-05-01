def average_Odd(n): 
    """ 
    Write a python function to find the average of odd numbers till a given odd number. 
    """
    if n % 2 == 0:
        return "Please provide an odd number."
    
    sum_of_odds = 0
    count = 0
    for i in range(1, n + 1, 2):
        sum_of_odds += i
        count += 1
    return sum_of_odds / count