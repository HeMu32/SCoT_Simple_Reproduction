def sort_on_occurence(lst):
    # Initialize a dictionary to count occurrences of the first element in each tuple
    count_dict = {}
    
    # Count the occurrences of the first element in each tuple
    for tup in lst:
        first_element = tup[0]
        if first_element in count_dict:
            count_dict[first_element] += 1
        else:
            count_dict[first_element] = 1
    
    # Define a helper function to use as the key for sorting
    def sort_key(tup):
        return count_dict[tup[0]]
    
    # Sort the list based on the occurrence of the first element
    sorted_lst = sorted(lst, key=sort_key)
    
    return sorted_lst