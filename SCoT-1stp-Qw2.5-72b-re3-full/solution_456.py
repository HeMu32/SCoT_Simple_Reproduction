def reverse_string_list(stringlist):
    # Initialize an empty list to store the reversed strings
    reversed_list = []
    
    # Loop through each string in the input list
    for string in stringlist:
        # Reverse the string using slicing
        reversed_string = string[::-1]
        # Append the reversed string to the new list
        reversed_list.append(reversed_string)
    
    # Return the new list containing the reversed strings
    return reversed_list