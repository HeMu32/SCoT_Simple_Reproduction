def babylonian_squareroot(number):
    if number <= 0:
        return 0
    
    guess = number
    tolerance = 1e-7
    
    while True:
        new_guess = (guess + number / guess) / 2
        if abs(new_guess - guess) < tolerance:
            break
        guess = new_guess
    
    return new_guess