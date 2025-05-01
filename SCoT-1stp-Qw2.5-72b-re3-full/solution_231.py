def max_sum(tri, n):
    # Start from the second last row and move upwards
    for row in range(n-2, -1, -1):
        for col in range(len(tri[row])):
            # Add the maximum of the two adjacent numbers from the row below
            tri[row][col] += max(tri[row+1][col], tri[row+1][col+1])
    
    # The top element now contains the maximum sum
    return tri[0][0]