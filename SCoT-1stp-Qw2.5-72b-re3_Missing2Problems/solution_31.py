import heapq

def func(nums, k):
    # Initialize a dictionary to store the frequency of each integer
    freq = {}
    
    # Loop through each list in nums
    for num_list in nums:
        # For each integer in the list, increment its count in freq
        for num in num_list:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
    
    # Convert the dictionary freq into a list of tuples (integer, frequency)
    freq_list = [(num, count) for num, count in freq.items()]
    
    # Use a heap queue to find the top k elements based on their frequency
    top_k = heapq.nlargest(k, freq_list, key=lambda x: x[1])
    
    # Extract the integers from the top k elements and return them as a list
    return [num for num, count in top_k]