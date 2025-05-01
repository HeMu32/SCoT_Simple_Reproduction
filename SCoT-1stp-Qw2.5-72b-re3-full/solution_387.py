def even_or_odd(N):
    # Convert the hexadecimal number to an integer
    num = int(N, 16)
    
    # Check if the number is even or odd
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"