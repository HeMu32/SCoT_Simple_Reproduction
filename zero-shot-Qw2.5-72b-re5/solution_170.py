def sum_range_list(list1, m, n): 
    """ 
    Write a function to find sum of the numbers in a list between the indices of a specified range. 
    """ 
    if m < 0 or n >= len(list1) or m > n:
        return 0
    return sum(list1[m:n+1])