def max_aggregate(stdata):
    # Initialize variables
    max_aggregate_sum = 0
    max_aggregate_string = ""
    aggregate_dict = {}

    # Iterate through the list of tuples
    for string, integer in stdata:
        if string in aggregate_dict:
            aggregate_dict[string] += integer
        else:
            aggregate_dict[string] = integer

    # Find the maximum aggregate
    for string, total in aggregate_dict.items():
        if total > max_aggregate_sum:
            max_aggregate_sum = total
            max_aggregate_string = string

    # Return the result
    return max_aggregate_string