def find_Sum(arr, n):
    # Initialize a dictionary to count occurrences of each element
    count_dict = {}
    # Initialize the sum of repeated elements
    sum_repeated = 0
    
    # Count the occurrences of each element in the array
    for element in arr:
        if element in count_dict:
            count_dict[element] += 1
        else:
            count_dict[element] = 1
    
    # Calculate the sum of repeated elements
    for element, count in count_dict.items():
        if count > 1:
            sum_repeated += element * count
    
    return sum_repeated