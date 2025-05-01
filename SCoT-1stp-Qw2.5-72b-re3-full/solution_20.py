def is_woodall(x):
    # Check if x + 1 is a power of 2
    if (x + 1) & x == 0 and x + 1 > 0:
        # Calculate k as log2(x + 1)
        k = (x + 1).bit_length() - 1
        # Calculate n as (x + 1) / 2^k - 1
        n = (x + 1) // (1 << k) - 1
        # Check if n is an integer
        if (x + 1) == (1 << k) * (n + 1):
            return True
    return False