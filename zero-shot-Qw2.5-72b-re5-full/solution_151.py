def gcd(p, q):
    def compute_gcd(x, y):
        while(y):
            x, y = y, x % y
        return x
    
    return compute_gcd(p, q) == 1

# Example usage:
# print(gcd(14, 15))  # Should return True
# print(gcd(14, 21))  # Should return False