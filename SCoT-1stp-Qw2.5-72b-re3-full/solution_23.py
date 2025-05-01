def maximum_Sum(list1):
    max_sum = float('-inf')  # Initialize max_sum to negative infinity
    for sublist in list1:
        current_sum = sum(sublist)  # Calculate the sum of the current sublist
        if current_sum > max_sum:
            max_sum = current_sum  # Update max_sum if the current_sum is greater
    return max_sum