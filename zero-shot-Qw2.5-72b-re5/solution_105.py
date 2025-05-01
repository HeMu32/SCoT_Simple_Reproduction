def count(lst):
    """
    Write a python function to count true booleans in the given list.
    """
    return sum(1 for item in lst if item is True)