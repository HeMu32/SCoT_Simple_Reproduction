def split_two_parts(list1, L):
    if len(list1) < L:
        return (list1, [])
    else:
        first_part = list1[:L]
        second_part = list1[L:]
        return (first_part, second_part)