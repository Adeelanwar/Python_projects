def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
def phi(n):
    value = 0
    for i in range(1,n):
        if gcd(i,n) == 1:
            value += 1
    return value
