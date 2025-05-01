def largest_neg(list1):
    max_neg = None
    for num in list1:
        if num < 0 and (max_neg is None or num > max_neg):
            max_neg = num
    return max_neg