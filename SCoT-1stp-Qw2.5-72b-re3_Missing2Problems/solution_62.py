def smallest_num(xs):
    if not xs:  # Check if the list is empty
        return None  # or raise an error: raise ValueError("List is empty")
    
    smallest = xs[0]  # Initialize smallest with the first element of the list
    for num in xs[1:]:  # Loop through the list starting from the second element
        if num < smallest:  # If the current element is smaller than the current smallest
            smallest = num  # Update smallest
    return smallest  # Return the smallest number