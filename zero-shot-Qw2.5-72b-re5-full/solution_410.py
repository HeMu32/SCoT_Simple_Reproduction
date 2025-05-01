def min_val(listval):
    """
    Write a function to find the minimum value in a given heterogeneous list.
    """
    # Filter out non-numeric values
    numeric_values = [x for x in listval if isinstance(x, (int, float))]
    if not numeric_values:
        return None  # Return None if no numeric values are found
    return min(numeric_values)