def dict_depth(d):
    if isinstance(d, dict):
        if d:
            return 1 + (max(map(dict_depth, d.values())) if isinstance(d, dict) else 0)
        else:
            return 1
    return 0