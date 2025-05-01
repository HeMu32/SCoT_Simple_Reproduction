def max_sum(tri, n): 
    """
    Write a function to find the maximum sum in the given right triangle of numbers. 
    """
    for i in range(n-2, -1, -1):
        for j in range(i+1):
            tri[i][j] += max(tri[i+1][j], tri[i+1][j+1])
    return tri[0][0]