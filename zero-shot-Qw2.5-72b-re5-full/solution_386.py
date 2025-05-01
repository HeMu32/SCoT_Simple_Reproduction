def swap_count(s):
    open_brackets = 0
    swaps = 0
    for char in s:
        if char == '[':
            open_brackets += 1
        elif char == ']':
            if open_brackets > 0:
                open_brackets -= 1
            else:
                swaps += 1
    return swaps + open_brackets // 2