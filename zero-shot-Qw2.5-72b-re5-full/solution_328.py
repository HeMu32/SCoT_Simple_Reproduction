def rotate_left(list1, m, n):
    """
    Write a function to rotate a given list by specified number of items to the left direction.
    """
    if n > m:
        n = n % m
    list1[:] = list1[n:] + list1[:n]