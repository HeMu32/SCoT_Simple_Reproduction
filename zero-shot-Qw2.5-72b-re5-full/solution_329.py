def neg_count(lst):
    """
    Write a python function to count negative numbers in a list.
    """
    return sum(1 for x in lst if x < 0)