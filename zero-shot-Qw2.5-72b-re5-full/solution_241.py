def array_3d(m, n, o):
    """
    Write a function to generate a 3d array having each element as '*'.
    """
    return [[[ '*' for _ in range(o)] for _ in range(n)] for _ in range(m)]