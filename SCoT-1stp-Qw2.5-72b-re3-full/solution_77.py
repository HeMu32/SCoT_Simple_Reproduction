def is_Diff(n):
    sum_even = 0
    sum_odd = 0
    # Convert the number to a string to iterate through each digit
    for digit in str(n):
        digit = int(digit)
        if digit % 2 == 0:
            sum_even += digit
        else:
            sum_odd += digit
    # Calculate the difference between the sum of even and odd digits
    difference = sum_even - sum_odd
    return difference