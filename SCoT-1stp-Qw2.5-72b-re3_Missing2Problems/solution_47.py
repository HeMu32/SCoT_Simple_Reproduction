def factorial(n):
    """Calculate the factorial of a number."""
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def compute_Last_Digit(A, B):
    """Find the last digit when factorial of A divides factorial of B."""
    # Calculate the factorials of A and B
    fact_A = factorial(A)
    fact_B = factorial(B)
    
    # Compute the division of factorial of B by factorial of A
    division_result = fact_B // fact_A
    
    # Convert the division result to a string to get the last digit
    last_digit_str = str(division_result)[-1]
    
    # Convert the last character back to an integer
    last_digit = int(last_digit_str)
    
    # Return the last digit
    return last_digit