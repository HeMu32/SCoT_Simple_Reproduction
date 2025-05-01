def min_val(listval):
    min_value = None
    for element in listval:
        if isinstance(element, (int, float)):
            if min_value is None or element < min_value:
                min_value = element
    if min_value is None:
        raise ValueError("No numeric values found in the list")
    return min_value