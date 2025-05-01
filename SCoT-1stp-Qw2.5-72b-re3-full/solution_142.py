def count_samepair(list1, list2, list3):
    # Convert lists to sets for faster lookup and to remove duplicates
    set1 = set(list1)
    set2 = set(list2)
    set3 = set(list3)
    
    # Initialize the counter
    count = 0
    
    # Iterate through the elements of the first set
    for x in set1:
        # Iterate through the elements of the second set
        for y in set2:
            # Check if the pair (x, y) exists in the third set
            if (x, y) in set3:
                # Increment the counter if the pair is found
                count += 1
    
    # Return the final count
    return count