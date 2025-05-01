def find_last_occurrence(A, x):
    index = -1
    for i, value in enumerate(A):
        if value == x:
            index = i
    return index