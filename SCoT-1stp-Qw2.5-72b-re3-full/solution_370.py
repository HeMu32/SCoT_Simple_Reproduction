def float_sort(price):
    # Convert the tuple to a list to enable sorting
    price_list = list(price)
    
    # Define a key function that extracts the float value from each element
    def extract_float(element):
        if isinstance(element, float):
            return element
        return float('inf')  # Return a high value for non-float elements to sort them at the end
    
    # Use the sorted function with the key function to sort the list by the float values
    sorted_list = sorted(price_list, key=extract_float)
    
    # Convert the sorted list back to a tuple
    sorted_tuple = tuple(sorted_list)
    
    # Return the sorted tuple
    return sorted_tuple