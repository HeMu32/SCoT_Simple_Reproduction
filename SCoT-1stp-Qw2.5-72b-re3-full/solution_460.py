def Extract(lst):
    result = []
    for sublist in lst:
        if sublist:  # Check if the sublist is not empty
            result.append(sublist[0])
    return result