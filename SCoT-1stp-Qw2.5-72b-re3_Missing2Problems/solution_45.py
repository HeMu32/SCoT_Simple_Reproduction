from math import gcd

def get_gcd(l):
    if not l:  # Check if the list is empty
        return None  # Return None or raise an error if the list is empty
    
    gcd_result = l[0]  # Initialize gcd_result with the first element of the list
    
    for num in l[1:]:  # Iterate over the list starting from the second element
        gcd_result = gcd(gcd_result, num)  # Update gcd_result with the GCD of gcd_result and num
    
    return gcd_result  # Return the final GCD result