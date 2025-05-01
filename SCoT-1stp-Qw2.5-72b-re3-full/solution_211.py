def count_Num(n):
    count = 0
    # The range of numbers to check is from 0 to 2^(n+1) - 1
    for num in range(2**(n+1)):
        # Convert the number to binary and check the 0th and nth bits
        if (num & (1 << n)) and (num & 1):
            count += 1
    return count