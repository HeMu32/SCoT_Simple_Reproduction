def octal_To_Decimal(n):
    decimal = 0
    base = 1
    for digit in reversed(n):
        decimal += int(digit) * base
        base *= 8
    return decimal