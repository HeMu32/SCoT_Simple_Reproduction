def even_or_odd(N):
    """
    Write a python function to check whether the hexadecimal number is even or odd.
    """
    # Convert the hexadecimal string to an integer
    num = int(N, 16)
    # Check if the number is even or odd
    return "Even" if num % 2 == 0 else "Odd"