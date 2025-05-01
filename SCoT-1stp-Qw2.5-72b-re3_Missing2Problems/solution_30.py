def count_Substring_With_Equal_Ends(s):
    count = 0
    n = len(s)
    
    # Iterate through each character in the string
    for i in range(n):
        # Check all possible substrings starting from the current character
        for j in range(i, n):
            # If the substring starts and ends with the same character
            if s[i] == s[j]:
                count += 1
                
    return count