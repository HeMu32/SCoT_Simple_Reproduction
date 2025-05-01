def remove(lst):
    new_list = []
    for s in lst:
        new_s = ''.join([c for c in s if not c.isdigit()])
        new_list.append(new_s)
    return new_list