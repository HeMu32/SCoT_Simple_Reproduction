def combinations_colors(l, n):
    def generate_combinations(current, remaining, start):
        if remaining == 0:
            result.append(list(current))
            return
        for i in range(start, len(l)):
            current.append(l[i])
            generate_combinations(current, remaining - 1, i)
            current.pop()

    result = []
    generate_combinations([], n, 0)
    return result