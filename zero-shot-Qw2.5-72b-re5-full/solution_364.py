def make_flip(ch):
    def count_flips(s, start):
        flips = 0
        for char in s:
            if char != start:
                flips += 1
            start = '1' if start == '0' else '0'
        return flips

    if not ch:
        return 0

    # Count flips starting with '0' and '1'
    flips_starting_with_0 = count_flips(ch, '0')
    flips_starting_with_1 = count_flips(ch, '1')

    return min(flips_starting_with_0, flips_starting_with_1)