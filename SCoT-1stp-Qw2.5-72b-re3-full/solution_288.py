def modular_inverse(arr, N, P):
    count = 0
    for x in arr:
        # Calculate the modular inverse of x under P using Fermat's Little Theorem
        mod_inverse = pow(x, P - 2, P)
        if mod_inverse == x:
            count += 1
    return count