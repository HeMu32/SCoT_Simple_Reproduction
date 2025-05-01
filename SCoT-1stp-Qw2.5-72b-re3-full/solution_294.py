def max_val(listval):
    max_value = None
    for element in listval:
        if isinstance(element, (int, float)):
            if max_value is None or element > max_value:
                max_value = element
    if max_value is None:
        raise ValueError("No numeric values found in the list.")
    return max_value