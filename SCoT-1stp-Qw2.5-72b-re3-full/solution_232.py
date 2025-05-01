def larg_nnum(list1, n):
    # Check if n is valid
    if n < 1 or n > len(list1):
        return "Error: n is out of the valid range."
    
    # Sort the list in descending order
    sorted_list = sorted(list1, reverse=True)
    
    # Get the n largest numbers
    largest_n = sorted_list[:n]
    
    return largest_n