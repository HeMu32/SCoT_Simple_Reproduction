def smallest_missing(A, left_element, right_element):
    missing = None
    for i in range(left_element, right_element + 1):
        if i not in A:
            missing = i
            break
    return missing