def is_Monotonic(A):
    increasing = all(x <= y for x, y in zip(A, A[1:]))
    decreasing = all(x >= y for x, y in zip(A, A[1:]))
    return increasing or decreasing