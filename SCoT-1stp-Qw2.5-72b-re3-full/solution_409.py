def min_product_tuple(list1):
    min_product = None
    for pair in list1:
        product = pair[0] * pair[1]
        if min_product is None or product < min_product:
            min_product = product
    return min_product