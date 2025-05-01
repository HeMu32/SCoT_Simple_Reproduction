def counting_sort(my_list):
    if not my_list:  # If the list is empty, return it as is
        return my_list

    max_val = max(my_list)  # Find the maximum value in the list
    count = [0] * (max_val + 1)  # Initialize the count array

    # Count each element in the input list
    for num in my_list:
        count[num] += 1

    # Modify the count array to store the sum of previous counts
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Initialize the output array
    output = [0] * len(my_list)

    # Build the output array
    for num in reversed(my_list):
        output[count[num] - 1] = num
        count[num] -= 1

    return output