def fact(n):
    if n == 0 or n == 1:
        return 1
    if n >= 2:
        return n * fact(n - 1)
    return 1
def ncr(n, r):
    num = fact(n)
    den = fact(r) * fact(n - r)
    print(num, den)
    return int(num / den)
print(ncr(40, 20))

    
