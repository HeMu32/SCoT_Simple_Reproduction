def bitwise_xor(test_tup1, test_tup2):
    # Initialize an empty list to store the results
    res = []
    # Iterate over pairs of elements from both tuples
    for ele1, ele2 in zip(test_tup1, test_tup2):
        # Perform bitwise XOR operation and append the result to the list
        res.append(ele1 ^ ele2)
    # Convert the list to a tuple and return it
    return tuple(res)