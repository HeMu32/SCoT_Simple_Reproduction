def sort_matrix(M):
    # Calculate the sum of each row and store it in a list
    row_sums = [sum(row) for row in M]
    
    # Pair each row with its sum
    paired_list = [(M[i], row_sums[i]) for i in range(len(M))]
    
    # Sort the paired list based on the sum
    sorted_pairs = sorted(paired_list, key=lambda x: x[1])
    
    # Extract the rows from the sorted pairs
    sorted_matrix = [pair[0] for pair in sorted_pairs]
    
    return sorted_matrix