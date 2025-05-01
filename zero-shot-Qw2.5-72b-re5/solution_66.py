def pos_count(lst):
    """
    Write a python function to count positive numbers in a list.
    """
    return sum(1 for num in lst if num > 0)