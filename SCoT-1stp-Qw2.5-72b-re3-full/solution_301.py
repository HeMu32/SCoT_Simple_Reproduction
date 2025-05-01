def dict_depth(d):
    if not isinstance(d, dict) or not d:
        return 0
    max_depth = 0
    for value in d.values():
        if isinstance(value, dict):
            max_depth = max(max_depth, dict_depth(value))
    return max_depth + 1