def is_num_keith(x):
    """
    Write a function to find if the given number is a keith number or not.
    """
    if x < 10:
        return False

    # Convert the number to a list of its digits
    digits = [int(d) for d in str(x)]
    n = len(digits)

    # Generate the sequence
    while digits[-1] < x:
        next_digit = sum(digits[-n:])
        digits.append(next_digit)

    return digits[-1] == x