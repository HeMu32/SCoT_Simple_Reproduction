def max_aggregate(stdata):
    """
    Write a function to calculate the maximum aggregate from the list of tuples.
    """
    if not stdata:
        return 0
    return max(sum(item) for item in stdata)