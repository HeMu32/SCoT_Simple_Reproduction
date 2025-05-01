def no_of_subsequences(arr, k):
    from itertools import combinations
    
    def product_of_elements(subseq):
        product = 1
        for num in subseq:
            product *= num
        return product
    
    count = 0
    for r in range(1, len(arr) + 1):
        for subseq in combinations(arr, r):
            if product_of_elements(subseq) < k:
                count += 1
    return count