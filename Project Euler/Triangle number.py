def tau(num):
    n = num
    i = 2
    p = 1
    if (num == 1):
        return 1
    while (i * i <= n):
        c = 1
        while (n % i == 0):
            n /= i
            c += 1
        i += 1
        p*= c
    if (n == num or n > 1):
        p *= 1 + 1
    return p
def trianglenumber(n):
    return int(n * (n + 1) / 2) 
for i in range(1,1000000):
    div = int(tau(trianglenumber(i)))
    if div > 1000:
        print(i,trianglenumber(i), div)
