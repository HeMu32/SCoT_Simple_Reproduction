def min_Operations(A, B):
    operations = 0
    while A != B:
        if A > B:
            B += 1
        else:
            A += 1
        operations += 1
    return operations