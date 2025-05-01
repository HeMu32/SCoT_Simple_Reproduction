def count_binary_seq(n):
    from itertools import product
    
    count = 0
    # Generate all binary sequences of length 2n
    for seq in product([0, 1], repeat=2*n):
        # Split the sequence into two halves
        first_half = seq[:n]
        second_half = seq[n:]
        
        # Calculate the sum of the bits in each half
        sum_first_half = sum(first_half)
        sum_second_half = sum(second_half)
        
        # Check if the sums are equal
        if sum_first_half == sum_second_half:
            count += 1
    
    return count