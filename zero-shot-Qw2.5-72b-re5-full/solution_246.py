def babylonian_squareroot(number):
    if number < 0:
        return None  # Return None for negative numbers as they don't have real square roots
    if number == 0:
        return 0  # The square root of 0 is 0

    guess = number / 2.0  # Initial guess
    while True:
        new_guess = (guess + number / guess) / 2.0
        if abs(new_guess - guess) < 1e-6:  # Convergence criterion
            return new_guess
        guess = new_guess