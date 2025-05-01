def div_even_odd(list1):
    first_even = None
    first_odd = None
    
    for num in list1:
        if num % 2 == 0 and first_even is None:
            first_even = num
        elif num % 2 != 0 and first_odd is None:
            first_odd = num
        if first_even is not None and first_odd is not None:
            break
    
    if first_even is None or first_odd is None:
        return "Cannot perform division: Missing even or odd number."
    
    res = first_even / first_odd
    return res