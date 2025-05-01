def find_Product(arr, n):
    # Step 1: Initialize a dictionary to keep track of the frequency of each element
    frequency = {}
    
    # Step 2: Populate the dictionary with the frequency of each element
    for i in range(n):
        if arr[i] in frequency:
            frequency[arr[i]] += 1
        else:
            frequency[arr[i]] = 1
    
    # Step 3: Initialize the product to 1
    product = 1
    
    # Step 4: Loop through the dictionary
    for key, value in frequency.items():
        # Step 5: Check if the element is not repeated
        if value == 1:
            # Step 6: Multiply the product by the non-repeated element
            product *= key
    
    # Step 7: Return the product
    return product