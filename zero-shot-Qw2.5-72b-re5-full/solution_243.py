def sort_on_occurence(lst):
    """
    Write a function to sort the given list based on the occurrence of first element of tuples.
    """
    return sorted(lst, key=lambda x: (x[0], lst.count(x)))