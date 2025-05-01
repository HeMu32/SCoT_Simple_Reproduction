def common_prefix(arr, n):
    if n == 0:
        return ""
    
    # Initialize prefix with the first string in the list
    prefix = arr[0]
    
    # Loop through the rest of the strings
    for i in range(1, n):
        # While the current string does not start with the prefix
        while arr[i].find(prefix) != 0:
            # Reduce the prefix by one character from the end
            prefix = prefix[:-1]
            # If the prefix becomes empty, return an empty string
            if not prefix:
                return ""
    
    # Return the longest common prefix
    return prefix