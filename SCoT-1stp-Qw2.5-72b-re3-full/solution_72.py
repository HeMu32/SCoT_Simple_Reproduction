def dif_Square(n):
    # Check if n is negative
    if n < 0:
        return False
    # Check if n is 0 or 1
    if n == 0 or n == 1:
        return True
    # Check if n is odd or a multiple of 4
    if n % 2 == 1 or n % 4 == 0:
        return True
    # If n is even but not a multiple of 4, it cannot be represented as the difference of two squares
    return False