def check_occurences(test_list):
    # Initialize an empty dictionary to store the counts
    counts = {}
    
    # Loop through each tuple in the test_list
    for tup in test_list:
        # Loop through each element in the tuple
        for elem in tup:
            # If the element is already a key in the dictionary, increment its count
            if elem in counts:
                counts[elem] += 1
            # Otherwise, add the element to the dictionary with a count of 1
            else:
                counts[elem] = 1
    
    # Return the dictionary containing the counts of each element
    return counts