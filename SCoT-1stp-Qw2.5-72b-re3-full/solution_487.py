def sort_tuple(tup):
    # Helper function to get the last element of a tuple
    def last(n):
        return n[-1]
    
    # Sort the list of tuples using the last element of each tuple
    sorted_tup = sorted(tup, key=last)
    
    return sorted_tup