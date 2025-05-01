def first_Digit(number):
    while number >= 10:
        number //= 10
    return number