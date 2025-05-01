def magic_square_test(my_matrix):
    n = len(my_matrix)
    # Calculate the sum of the first row to set as the target sum
    target_sum = sum(my_matrix[0])
    
    # Check rows and columns
    for i in range(n):
        if sum(my_matrix[i]) != target_sum or sum(row[i] for row in my_matrix) != target_sum:
            return False
    
    # Check diagonals
    if sum(my_matrix[i][i] for i in range(n)) != target_sum or sum(my_matrix[i][n-i-1] for i in range(n)) != target_sum:
        return False
    
    return True