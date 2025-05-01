def count_occurance(s):
    # Initialize count to 0
    count = 0
    # Length of the substring to find
    sub_len = len('std')
    # Iterate through the string, stopping before the last (sub_len - 1) characters
    for i in range(len(s) - sub_len + 1):
        # Check if the substring starting at position i is 'std'
        if s[i:i+sub_len] == 'std':
            # Increment count if the substring is found
            count += 1
    # Return the final count
    return count