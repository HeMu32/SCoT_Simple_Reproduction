def max_occurrences(nums):
    # Step 1: Initialize an empty dictionary to store the frequency of each item
    frequency = {}
    
    # Step 2: Loop through each item in the list nums
    for item in nums:
        # Step 3: If the item is not in the dictionary, add it with a count of 1
        if item not in frequency:
            frequency[item] = 1
        # Step 4: If the item is already in the dictionary, increment its count by 1
        else:
            frequency[item] += 1
    
    # Step 5: Initialize a variable max_count to 0 and max_item to None
    max_count = 0
    max_item = None
    
    # Step 6: Loop through each key-value pair (item, count) in the dictionary
    for item, count in frequency.items():
        # Step 7: If the count is greater than max_count, update max_count to count and max_item to item
        if count > max_count:
            max_count = count
            max_item = item
    
    # Step 8: Return max_item
    return max_item