def extract_missing(test_list, strt_val, stop_val):
    # Convert the test_list to a set for O(1) lookups
    test_set = set(test_list)
    missing_ranges = []
    current_start = None

    for num in range(strt_val, stop_val + 1):
        if num not in test_set:
            if current_start is None:
                # Start of a new missing range
                current_start = num
        else:
            if current_start is not None:
                # End of a missing range
                missing_ranges.append((current_start, num - 1))
                current_start = None

    # Check if the last number is part of a missing range
    if current_start is not None:
        missing_ranges.append((current_start, stop_val))

    return missing_ranges