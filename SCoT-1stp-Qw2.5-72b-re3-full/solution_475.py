def sort_counter(dict1):
    # Convert the dictionary into a list of tuples
    items = list(dict1.items())
    # Sort the list of tuples based on the value in descending order
    sorted_items = sorted(items, key=lambda x: x[1], reverse=True)
    # Convert the sorted list of tuples back into a dictionary
    sorted_dict = dict(sorted_items)
    # Return the sorted dictionary
    return sorted_dict