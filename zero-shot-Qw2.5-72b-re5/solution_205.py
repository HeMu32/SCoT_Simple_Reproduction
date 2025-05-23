def inversion_elements(test_tup):
    """
    Write a function to find the inversions of tuple elements in the given tuple list.
    """
    inversions = []
    for elem in test_tup:
        if isinstance(elem, tuple):
            inversions.append(tuple(reversed(elem)))
        else:
            inversions.append(elem)
    return tuple(inversions)