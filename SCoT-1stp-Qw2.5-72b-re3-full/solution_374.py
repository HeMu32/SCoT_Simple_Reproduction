def permute_string(str):
    # Base case: if the string is a single character, print it
    if len(str) == 1:
        print(str)
        return
    
    # Recursive case: for each character in the string
    for i in range(len(str)):
        # Remove the character at position i
        current_char = str[i]
        # Remaining string after removing the character
        remaining_str = str[:i] + str[i+1:]
        
        # Generate permutations of the remaining string
        for perm in permute_string(remaining_str):
            # Add the removed character to the beginning of each permutation
            print(current_char + perm)

# Example usage:
permute_string("abc")