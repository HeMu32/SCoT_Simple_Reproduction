def modular_inverse(arr, N, P):
    count = 0
    for i in range(N):
        if (arr[i] * arr[i]) % P == 1:
            count += 1
    return count