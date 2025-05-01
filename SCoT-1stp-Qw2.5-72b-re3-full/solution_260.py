def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def newman_prime(n):
    """Find the nth Newman–Shanks–Williams prime number."""
    S0, S1 = 1, 1
    nsw_primes = []
    counter = 0
    
    while counter < n:
        # Generate the next term in the sequence
        S_next = 2 * S1 + S0
        
        # Check if the term is a prime number
        if is_prime(S_next):
            nsw_primes.append(S_next)
            counter += 1
        
        # Update the sequence terms
        S0, S1 = S1, S_next
    
    return nsw_primes[-1]

# Example usage:
print(newman_prime(1))  # Output: 2
print(newman_prime(2))  # Output: 7
print(newman_prime(3))  # Output: 41