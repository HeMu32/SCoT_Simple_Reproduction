def is_woodall(x):
    """
    Write a function to check if the given number is Woodall or not.
    """
    n = 1
    while True:
        woodall_number = n * (2**n) - 1
        if woodall_number == x:
            return True
        elif woodall_number > x:
            return False
        n += 1