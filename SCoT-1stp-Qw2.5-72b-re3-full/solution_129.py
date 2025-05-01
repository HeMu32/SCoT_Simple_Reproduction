def magic_square_test(my_matrix):
    n = len(my_matrix)
    # Calculate the reference sum using the first row
    ref_sum = sum(my_matrix[0])
    
    # Check all rows
    for row in my_matrix:
        if sum(row) != ref_sum:
            return False
    
    # Check all columns
    for col in range(n):
        if sum(my_matrix[row][col] for row in range(n)) != ref_sum:
            return False
    
    # Check main diagonal
    if sum(my_matrix[i][i] for i in range(n)) != ref_sum:
        return False
    
    # Check secondary diagonal
    if sum(my_matrix[i][n-1-i] for i in range(n)) != ref_sum:
        return False
    
    return True