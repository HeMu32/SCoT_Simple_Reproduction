def is_num_keith(x):
    # Convert the number into a list of its digits
    digits = [int(d) for d in str(x)]
    n = len(digits)
    
    # Initialize the sequence with the digits of x
    sequence = digits[:]
    
    # Generate the sequence until the last term is greater than or equal to x
    while sequence[-1] < x:
        next_term = sum(sequence[-n:])
        sequence.append(next_term)
    
    # Check if the last term is exactly x
    return sequence[-1] == x