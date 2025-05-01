def is_Sum_Of_Powers_Of_Two(n):
    while n > 0:
        if n % 2 == 1:
            return False
        n = n & (n - 1)  # Remove the lowest set bit
    return True