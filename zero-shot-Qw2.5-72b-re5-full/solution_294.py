def max_val(listval):
    """
    Write a function to find the maximum value in a given heterogeneous list.
    """
    return max(listval, key=lambda x: (isinstance(x, (int, float)), x))