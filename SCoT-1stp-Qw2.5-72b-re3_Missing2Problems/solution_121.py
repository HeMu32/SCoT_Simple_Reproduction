def check_triplet(A, n, sum, count):
    # Initialize count to 0
    count = 0

    # Use three nested loops to iterate through all possible triplets
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                # Calculate the sum of the triplet
                triplet_sum = A[i] + A[j] + A[k]
                # Check if the sum of the triplet equals the target sum
                if triplet_sum == sum:
                    # Increment count by 1
                    count += 1

    # Return the count of triplets
    return count