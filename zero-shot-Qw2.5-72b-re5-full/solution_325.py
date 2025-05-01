def get_Min_Squares(n):
    if n <= 3:
        return n
    
    # Initialize the result with a large number
    res = n
    
    # Try all numbers from 1 to the square root of n
    for x in range(1, n + 1):
        temp = x * x
        if temp > n:
            break
        else:
            res = min(res, 1 + get_Min_Squares(n - temp))
    
    return res