def larg_nnum(list1, n):
    """
    Write a function to get the n largest items from a dataset.
    """
    return sorted(list1, reverse=True)[:n]