def get_carol(n):
    """
    Write a function to find the n’th carol number.
    """
    if n < 1:
        return None
    k = 2 ** n - 1
    carol_number = k * k - 2
    return carol_number