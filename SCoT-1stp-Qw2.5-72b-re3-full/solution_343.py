def dig_let(s):
    digit_count = 0
    letter_count = 0
    for ch in s:
        if ch.isdigit():
            digit_count += 1
        elif ch.isalpha():
            letter_count += 1
    return (digit_count, letter_count)