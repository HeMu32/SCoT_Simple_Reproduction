def count_integer(list1):
    """
    Write a python function to count integers from a given list.
    """
    return sum(1 for item in list1 if isinstance(item, int))