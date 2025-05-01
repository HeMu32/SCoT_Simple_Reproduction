def sumofFactors(n): 
    sum = 1
    # Handle 2 separately to deal with even factors
    if (n % 2 == 0):
        sum += 2
        n = n // 2
        while (n % 2 == 0):
            sum += 2
            n = n // 2
    # Check for odd factors
    for i in range(3, int(n**0.5) + 1, 2):
        count = 1
        curr_sum = 1
        curr_term = 1
        while (n % i == 0):
            curr_term *= i
            count += 1
            n = n // i
            if (curr_term % 2 == 0):
                curr_sum += curr_term
        sum *= curr_sum
    # This condition is to handle the case when n is a prime number
    if (n > 2):
        if (n % 2 == 0):
            sum += n
    return sum