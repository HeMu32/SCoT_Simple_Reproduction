def sum(a, b):
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x
    
    def divisors(n):
        divs = []
        for i in range(1, n + 1):
            if n % i == 0:
                divs.append(i)
        return divs
    
    gcd_value = gcd(a, b)
    divs_a = divisors(a)
    divs_b = divisors(b)
    
    common_divisors = set(divs_a).intersection(divs_b)
    
    return sum(common_divisors)