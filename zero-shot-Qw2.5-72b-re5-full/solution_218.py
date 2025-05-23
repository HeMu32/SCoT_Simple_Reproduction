def min_Operations(A, B):
    if A == B:
        return 0
    if A > B:
        A, B = B, A
    operations = 0
    while A < B:
        if B % 2 == 0:
            B //= 2
        else:
            B += 1
        operations += 1
    return operations + (A - B)