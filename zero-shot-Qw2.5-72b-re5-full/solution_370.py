def float_sort(prices):
    """
    Write a function to sort a tuple by its float element.
    """
    return tuple(sorted(prices, key=lambda x: x[1]))