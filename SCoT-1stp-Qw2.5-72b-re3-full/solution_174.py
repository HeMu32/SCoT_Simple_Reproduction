def group_keyvalue(l):
    result = {}
    for key, value in l:
        if key not in result:
            result[key] = []
        result[key].append(value)
    return result