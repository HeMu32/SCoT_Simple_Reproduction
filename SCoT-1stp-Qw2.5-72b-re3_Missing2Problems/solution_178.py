def string_literals(patterns, text):
    matches = []
    for pattern in patterns:
        index = text.find(pattern)
        if index != -1:
            matches.append((pattern, index))
    return matches