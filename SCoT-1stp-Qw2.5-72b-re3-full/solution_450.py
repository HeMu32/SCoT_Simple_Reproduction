def extract_string(str, l):
    res = []  # Initialize an empty list to store the result
    for s in str:  # Loop through each string in the input list
        if len(s) == l:  # Check if the length of the string is equal to l
            res.append(s)  # Append the string to the result list
    return res  # Return the result list