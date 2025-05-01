def is_woodall(x):
    """
    Write a function to check if the given number is Woodall or not.
    """
    n = 1
    while (n * 2**n - 1) < x:
        n += 1
    return (n * 2**n - 1) == x