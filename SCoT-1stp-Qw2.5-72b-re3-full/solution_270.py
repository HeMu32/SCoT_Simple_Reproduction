def sum_even_and_even_index(arr, n):
    sum = 0
    for i in range(0, n, 2):  # Loop through even indices
        if arr[i] % 2 == 0:  # Check if the element at the even index is even
            sum += arr[i]  # Add the even element to the sum
    return sum