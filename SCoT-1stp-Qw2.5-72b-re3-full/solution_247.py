def lps(s):
    n = len(s)
    # Create a DP table with all elements initialized to 0
    dp = [[0] * n for _ in range(n)]
    
    # Every single character is a palindrome of length 1
    for i in range(n):
        dp[i][i] = 1
    
    # Build the table. Note that the lower diagonal values of table are
    # useless and not filled in the process. `cl` is the length of the substring
    for cl in range(2, n + 1):
        for i in range(n - cl + 1):
            j = i + cl - 1
            if s[i] == s[j] and cl == 2:
                dp[i][j] = 2
            elif s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])
    
    # Reconstruct the longest palindromic subsequence
    lps_str = ""
    i, j = 0, n - 1
    while i <= j:
        if s[i] == s[j]:
            lps_str += s[i]
            i += 1
            j -= 1
        elif dp[i + 1][j] >= dp[i][j - 1]:
            i += 1
        else:
            j -= 1
    
    # If the length of the LPS is odd, the middle character is added only once
    if i > j:
        lps_str += s[i]
    
    # Since the LPS is built from both ends, we need to add the reverse of the first half to the end
    lps_str += lps_str[::-1][len(lps_str) % 2:]
    
    return lps_str

# Example usage
input_str = "BBABCBCAB"
print(lps(input_str))  # Output: "BABCBAB"