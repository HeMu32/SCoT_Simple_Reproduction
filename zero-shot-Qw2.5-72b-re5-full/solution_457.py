def Find_Min(lst):
    if not lst:
        return []
    min_sublist = lst[0]
    for sublist in lst:
        if len(sublist) < len(min_sublist):
            min_sublist = sublist
    return min_sublist