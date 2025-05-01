def find_rotation_count(A):
    count = 0
    for i in range(len(A) - 1):
        if A[i] > A[i + 1]:
            count = i + 1
            break
    return count