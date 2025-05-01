def inversion_elements(test_tup):
    res = []
    for ele in test_tup:
        if isinstance(ele, tuple):
            res.append(ele[::-1])  # Reverse the tuple and append to the result list
        else:
            res.append(ele)  # Append the element as it is
    return res