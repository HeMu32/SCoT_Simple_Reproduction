def odd_Equivalent(s, n):
    count = 0
    for i in range(n):
        # Rotate the string to the left by i positions
        rotated_s = s[i:] + s[:i]
        # Convert the rotated string to an integer
        num = int(rotated_s, 2)
        # Check if the number is odd
        if num % 2 == 1:
            count += 1
    return count