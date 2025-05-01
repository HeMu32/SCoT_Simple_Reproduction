def concatenate_elements(test_tup):
    result = []
    for i in range(len(test_tup) - 1):
        # Concatenate the current element with the next element
        concatenated_element = str(test_tup[i]) + str(test_tup[i + 1])
        result.append(concatenated_element)
    # Convert the result list back into a tuple
    result = tuple(result)
    return result