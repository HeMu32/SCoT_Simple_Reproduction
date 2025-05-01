def max_product_tuple(list1):
    max_product = None
    for t in list1:
        product = t[0] * t[1]
        if max_product is None or product > max_product:
            max_product = product
    return max_product